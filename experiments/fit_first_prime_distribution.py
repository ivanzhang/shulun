#!/usr/bin/env python3
"""拟合 30P 链中首个素数高度的经验分布。

用法示例：
  python3 experiments/fit_first_prime_distribution.py \
    --primes 1000003,3000017,10000019 --cols 200 --delta 30 --max-mult 8

输出量说明：
  x=n/log(P)：链首素数高度的归一化变量。
  lambda_hat：把 x 近似看作指数分布时的极大似然参数。
  KS_exp：经验分布与指数模型的 Kolmogorov-Smirnov 距离。
"""
import argparse
import importlib.util
import math
import random
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "scan_chain_first_prime", Path(__file__).with_name("scan_chain_first_prime.py")
)
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)


def quantile(values, probability):
    """返回经验分位数。"""
    if not values:
        return None
    index = min(len(values) - 1, int(probability * len(values)))
    return values[index]


def ks_exponential(samples, lambda_hat):
    """计算样本与 Exp(lambda_hat) 的 KS 距离。"""
    if not samples:
        return None
    ordered = sorted(samples)
    size = len(ordered)
    best = 0.0
    for idx, value in enumerate(ordered, start=1):
        model = 1.0 - math.exp(-lambda_hat * value)
        left_gap = abs((idx - 1) / size - model)
        right_gap = abs(idx / size - model)
        best = max(best, left_gap, right_gap)
    return best


def sample_columns(P, count):
    """固定随机种子，抽样非平凡列并加入边界代表列。"""
    random.seed(P)
    anchors = [1, 2, 6, 30, P // 2, P - 1]
    random_count = min(count, max(0, P - 1))
    columns = anchors + random.sample(range(1, P), random_count)
    return list(dict.fromkeys(c for c in columns if 1 <= c < P))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes", default="1000003,3000017,10000019,30000001")
    parser.add_argument("--cols", type=int, default=200)
    parser.add_argument("--delta", type=int, default=30)
    parser.add_argument("--max-mult", type=float, default=8.0, help="扫描到 max_mult*log(P)")
    args = parser.parse_args()

    primes = [int(item) for item in args.primes.split(",") if item.strip()]
    samples = []
    missing = []
    worst = None

    for P in primes:
        max_n = int(args.max_mult * math.log(P)) + args.delta
        for c in sample_columns(P, args.cols):
            for r in scan.allowed_residues(P, c, args.delta):
                n = scan.first_prime_in_chain(P, c, r, max_n, args.delta)
                if n is None:
                    missing.append((P, c, r, max_n))
                    continue
                x_value = n / math.log(P)
                samples.append(x_value)
                record = (x_value, n, P, c, r)
                if worst is None or record > worst:
                    worst = record

    samples.sort()
    if not samples:
        print(f"count=0 missing={len(missing)}")
        return

    mean = sum(samples) / len(samples)
    lambda_hat = 1.0 / mean if mean > 0 else float("inf")
    ks_value = ks_exponential(samples, lambda_hat)

    print(f"count={len(samples)} missing={len(missing)} delta={args.delta}")
    print(
        "x=n/logP: "
        f"mean={mean:.4f} lambda_hat={lambda_hat:.4f} "
        f"q50={quantile(samples, .50):.4f} q90={quantile(samples, .90):.4f} "
        f"q99={quantile(samples, .99):.4f} max={samples[-1]:.4f} KS_exp={ks_value:.4f}"
    )
    if worst:
        x_value, n, P, c, r = worst
        print(f"worst: x={x_value:.4f} n={n} P={P} c={c} r={r}")
    if missing:
        print(f"missing_first={missing[:10]}")


if __name__ == "__main__":
    main()
