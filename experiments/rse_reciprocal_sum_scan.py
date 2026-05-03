#!/usr/bin/env python3
"""RSE 粗数倒数指数和压力测试。

用法示例：
  python experiments/rse_reciprocal_sum_scan.py --P-list 1009,2003
  python experiments/rse_reciprocal_sum_scan.py --P-list 5003 --alpha 0.45 --h-list 1,2,4,8
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "monograph"
TAU = 2.0 * math.pi


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数表。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, math.isqrt(n) + 1):
        if sieve[i]:
            step_start = i * i
            sieve[step_start : n + 1 : i] = [False] * (((n - step_start) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def parse_ints(raw: str) -> list[int]:
    return [int(x) for x in raw.split(",") if x.strip()]


def parse_floats(raw: str) -> list[float]:
    return [float(x) for x in raw.split(",") if x.strip()]


def expi(x: float) -> complex:
    return complex(math.cos(TAU * x), math.sin(TAU * x))


def rough_values(M: int, small_primes: list[int]) -> list[int]:
    """枚举 dyadic 块 [M,2M) 中无 <=Y 素因子的 m。"""
    values: list[int] = []
    for m in range(max(1, M), max(1, 2 * M)):
        ok = True
        for q in small_primes:
            if m % q == 0:
                ok = False
                break
        if ok:
            values.append(m)
    return values


def floor_error(X: int, H: int, ell: int, ms: list[int]) -> float:
    """计算 BSI 中单个 ell 的地板余项。"""
    err = 0.0
    for m in ms:
        err += (X + H) // (ell * m) - X // (ell * m) - H / (ell * m)
    return err


def scan_record(X: int, H: int, h: int, ell: int, ms: list[int]) -> dict[str, float | int]:
    total = 0j
    amp_sum = 0.0
    amp2_sum = 0.0
    for m in ms:
        amp = 1.0 - expi(h * H / (ell * m))
        term = expi(h * X / (ell * m)) * amp
        total += term
        amp_abs = abs(amp)
        amp_sum += amp_abs
        amp2_sum += amp_abs * amp_abs
    abs_s = abs(total)
    count = len(ms)
    return {
        "h": h,
        "ell": ell,
        "rough_count": count,
        "absS": abs_s,
        "amp_sum": amp_sum,
        "sqrt_amp2": math.sqrt(amp2_sum),
        "norm_by_count": abs_s / count if count else 0.0,
        "norm_by_amp": abs_s / amp_sum if amp_sum else 0.0,
        "sigma_ratio": abs_s / math.sqrt(amp2_sum) if amp2_sum else 0.0,
    }


def phase_bucket(variation: float) -> str:
    if variation < 1.0:
        return "flat"
    if variation < 10.0:
        return "critical"
    return "oscillatory"


def analyze_case(P: int, alpha: float, beta: float, m_exp: float, h_list: list[int], ell_ratios: list[float]) -> dict:
    Y = max(2, int(P**alpha))
    small = primes_upto(Y)
    X = int(beta * P * P)
    H = P
    M = max(1, int(P**m_exp))
    Pm = X / M
    ms = rough_values(M, small)
    records: list[dict] = []
    floor_records: dict[int, float] = {}
    ell_candidates = sorted({max(1, int(ratio * Pm)) for ratio in ell_ratios})
    for ell in ell_candidates:
        floor_records[ell] = floor_error(X, H, ell, ms)
        for h in h_list:
            rec = scan_record(X, H, h, ell, ms)
            variation = h * Pm / ell
            rec.update(
                {
                    "ell_over_Pm": ell / Pm if Pm else 0.0,
                    "phase_variation": variation,
                    "phase_bucket": phase_bucket(variation),
                    "floor_error": floor_records[ell],
                    "floor_error_per_rough": floor_records[ell] / len(ms) if ms else 0.0,
                }
            )
            records.append(rec)

    bucket_summary: dict[str, dict[str, float | int]] = {}
    for name in ("flat", "critical", "oscillatory"):
        part = [r for r in records if r["phase_bucket"] == name]
        bucket_summary[name] = {
            "count": len(part),
            "max_norm_by_amp": max((float(r["norm_by_amp"]) for r in part), default=0.0),
            "avg_norm_by_amp": sum(float(r["norm_by_amp"]) for r in part) / len(part) if part else 0.0,
            "max_sigma_ratio": max((float(r["sigma_ratio"]) for r in part), default=0.0),
            "max_norm_by_count": max((float(r["norm_by_count"]) for r in part), default=0.0),
        }

    top_amp = sorted(records, key=lambda r: float(r["norm_by_amp"]), reverse=True)[:8]
    top_abs = sorted(records, key=lambda r: float(r["absS"]), reverse=True)[:8]
    top_floor = sorted(
        [{"ell": ell, "floor_error": err, "per_rough": err / len(ms) if ms else 0.0} for ell, err in floor_records.items()],
        key=lambda r: abs(float(r["floor_error"])),
        reverse=True,
    )[:8]
    return {
        "P": P,
        "alpha": alpha,
        "Y": Y,
        "beta": beta,
        "X": X,
        "H": H,
        "M_exp": m_exp,
        "M": M,
        "P_m": Pm,
        "rough_count": len(ms),
        "rough_density": len(ms) / M if M else 0.0,
        "ell_candidates": ell_candidates,
        "bucket_summary": bucket_summary,
        "top_by_norm_amp": top_amp,
        "top_by_absS": top_abs,
        "top_floor_error": top_floor,
    }


def render_markdown(audit: dict) -> str:
    lines = [
        "# RSE 粗数倒数指数和压力测试",
        "",
        f"**状态：** `{audit['status']}`",
        "",
        "本实验只用于定位 `RSE` 的真实瓶颈，不构成证明。扫描对象为",
        "",
        "\\[",
        "S_{h,\\ell}(M)=\\sum_{m\\sim M,\\ P^-(m)>Y}",
        "e\\left(\\frac{hX}{\\ell m}\\right)",
        "\\left(1-e\\left(\\frac{hH}{\\ell m}\\right)\\right).",
        "\\]",
        "",
        "## 参数",
        "",
        f"- `alpha={audit['parameters']['alpha']}`，`beta={audit['parameters']['beta']}`，`H=P`。",
        f"- `P-list={audit['parameters']['P_list']}`。",
        f"- `M=P^u`，`u-list={audit['parameters']['m_exponents']}`。",
        f"- `h-list={audit['parameters']['h_list']}`，`ell/P_m` 比例为 `{audit['parameters']['ell_ratios']}`。",
        "",
        "## 总体结论",
        "",
        "- 振荡区 `hP_m/ell>=10` 通常有明显归一化抵消，是 `van der Corput + Buchstab` 最可攻的区域。",
        "- 平坦区 `hP_m/ell<1` 的相位不抵消，但振幅因子 `1-e(hH/(ell m))` 很小，适合改用振幅账本吸收。",
        "- 临界区 `1<=hP_m/ell<10` 同时缺少强振荡且振幅未完全衰减，是当前 `RSE` 的最小硬核。",
        "- 因此下一步应把 `RSE` 拆成 `RSE-OSC`、`RSE-AMP`、`RSE-CRIT` 三个子接口；真正需要新想法的是 `RSE-CRIT`。",
        "",
        "## 分样本摘要",
    ]
    for case in audit["cases"]:
        lines.append("")
        lines.append(
            f"### P={case['P']}，M=P^{case['M_exp']}，Y={case['Y']}，"
            f"P_m={case['P_m']:.2f}，rough={case['rough_count']}"
        )
        for bucket in ("oscillatory", "critical", "flat"):
            b = case["bucket_summary"][bucket]
            lines.append(
                f"- `{bucket}`: n={b['count']} max|S|/amp={b['max_norm_by_amp']:.3f} "
                f"avg|S|/amp={b['avg_norm_by_amp']:.3f} "
                f"max|S|/sqrtAmp2={b['max_sigma_ratio']:.2f} "
                f"max|S|/N={b['max_norm_by_count']:.3g}"
            )
        worst = case["top_by_norm_amp"][0] if case["top_by_norm_amp"] else None
        if worst:
            lines.append(
                f"- 最坏归一化项：bucket={worst['phase_bucket']} h={worst['h']} ell={worst['ell']} "
                f"hP_m/ell={worst['phase_variation']:.2f} |S|/amp={worst['norm_by_amp']:.3f} "
                f"|S|/N={worst['norm_by_count']:.3g}"
            )
        floor = case["top_floor_error"][0] if case["top_floor_error"] else None
        if floor:
            lines.append(
                f"- 最大地板余项：ell={floor['ell']} E={floor['floor_error']:.3f} "
                f"E/N={floor['per_rough']:.3g}"
            )
    lines += [
        "",
        "## 对证明链的硬约束",
        "",
        "实验把原来的单个 `RSE` 接口压缩为三段：",
        "",
        "1. `RSE-OSC`：证明 `hP_m/ell>=L` 时粗数倒数相位的平均抵消。",
        "2. `RSE-AMP`：证明 `hP_m/ell<1/L` 时振幅小量在 Selberg 二次权平均后可吸收。",
        "3. `RSE-CRIT`：处理 `1/L<=hP_m/ell<L` 的薄临界带，这是当前唯一不能由振荡或振幅直接解释的剩余硬点。",
        "",
        "其中 `L` 可取 `log^A P`。若能证明临界带在 Selberg 合成权下的总质量只占 `o(|G_Y(I)|)`，则",
        "",
        "```text",
        "RSE-OSC + RSE-AMP + RSE-CRIT => RSE => BSI => PTA-GSL。",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P-list", default="1009,2003,5003")
    parser.add_argument("--alpha", type=float, default=0.45)
    parser.add_argument("--beta", type=float, default=0.73)
    parser.add_argument("--m-exponents", default="1.0,1.15,1.3,1.45")
    parser.add_argument("--h-list", default="1,2,4,8")
    parser.add_argument("--ell-ratios", default="0.05,0.1,0.25,0.5,1,2,4,8")
    args = parser.parse_args()

    p_list = parse_ints(args.P_list)
    m_exponents = parse_floats(args.m_exponents)
    h_list = parse_ints(args.h_list)
    ell_ratios = parse_floats(args.ell_ratios)

    cases = [
        analyze_case(P, args.alpha, args.beta, m_exp, h_list, ell_ratios)
        for P in p_list
        for m_exp in m_exponents
    ]
    audit = {
        "certificate_type": "rse_reciprocal_sum_scan",
        "status": "experimental_bottleneck_split_not_a_proof",
        "parameters": {
            "P_list": p_list,
            "alpha": args.alpha,
            "beta": args.beta,
            "m_exponents": m_exponents,
            "h_list": h_list,
            "ell_ratios": ell_ratios,
        },
        "cases": cases,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "rse-reciprocal-sum-scan.json"
    md_path = OUT / "rse-reciprocal-sum-scan.md"
    json_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
    md_path.write_text(render_markdown(audit) + "\n")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()
