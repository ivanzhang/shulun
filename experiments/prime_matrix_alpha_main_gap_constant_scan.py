#!/usr/bin/env python3
"""Alpha-MainGap 常数扫描。

用法示例：
  python3 experiments/prime_matrix_alpha_main_gap_constant_scan.py
  python3 experiments/prime_matrix_alpha_main_gap_constant_scan.py --cM 0.50 --Cpi 1.30

若有显式常数：
  V_alpha(p) >= cM/log p
  pi(p)-pi(alpha p) <= Cpi(1-alpha)p/log p
则 C_alpha<=2(pi(p)-pi(alpha p))，MainGap 由
  cM > 2 Cpi (1-alpha)
保证。
"""

from __future__ import annotations

import argparse


def threshold_alpha(c_mertens: float, c_prime: float) -> float:
    """返回粗容量主间隙要求的 alpha 阈值。"""
    return 1.0 - c_mertens / (2.0 * c_prime)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--cM", type=float, default=0.45)
    parser.add_argument("--Cpi", type=float, default=1.30)
    args = parser.parse_args()
    alpha0 = threshold_alpha(args.cM, args.Cpi)
    for alpha in [0.80, 0.85, 0.90, 0.92, 0.95]:
        print(
            {
                "cM": args.cM,
                "Cpi": args.Cpi,
                "threshold_alpha": alpha0,
                "alpha": alpha,
                "main_gap_constant": args.cM - 2 * args.Cpi * (1 - alpha),
                "passes": alpha > alpha0,
            },
            flush=True,
        )


if __name__ == "__main__":
    main()
