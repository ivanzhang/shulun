#!/usr/bin/env python3
"""生成 RPZ first-grid-fail seam 标准形证书。

用法示例：
  python3 experiments/prime_matrix_rpz_first_grid_fail_seam_certificate.py

若相邻下降 `p -> r` 在 `p` 行号 `a` 处发生首个 grid_fail，令 `g=p-r` 且

  delta = -(a-1)g mod r。

grid_fail 等价于 `g < delta < r`。此时 `p` 行不是未结构化坏窗，而是跨相邻两条
`r` 行的双帽 seam：

- 前一条 `r` 行的右帽长度为 `delta`；
- 下一条 `r` 行的左帽长度为 `r+g-delta`；
- 两侧缺口长度分别为 `r-delta` 与 `delta-g`，总缺口恒为 `r-g`；
- `r`-筛幸存者至多为右端点 `ap`。

该脚本材料化这些 seam 相位行，供后续 `PDEC/ColumnCRT` 证书使用。
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def primes_upto(limit: int) -> list[int]:
    """返回不超过 `limit` 的素数表。"""
    primes: list[int] = []
    for value in range(2, limit + 1):
        if all(value % prime for prime in primes if prime * prime <= value):
            primes.append(value)
    return primes


def fraction_text(value: Fraction) -> str:
    """把有理数写成可审查字符串。"""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def first_dividing_prime(value: int, primes: list[int]) -> int | None:
    """返回第一个整除 `value` 的小素数；若不存在则返回 None。"""
    for prime in primes:
        if value % prime == 0:
            return prime
    return None


def inverse_mod(value: int, modulus: int) -> int:
    """返回模素数 `modulus` 下的乘法逆元。"""
    return pow(value % modulus, -1, modulus)


def residue_for_delta(p: int, r: int, delta: int) -> int:
    """由 `delta=-(a-1)(p-r) mod r` 反解 `a mod r`。"""
    gap = p - r
    return (1 - delta * inverse_mod(gap, r)) % r


def pdec_support_packet(Q: int, r: int, row_residue: int) -> dict[str, Any]:
    """生成 seam 相位的 PDEC 精确支持集与 Fourier 账本。"""
    support_size = Q // r
    support_residue_progression = {
        "condition": f"a ≡ {row_residue} (mod {r})",
        "modulus_Q": Q,
        "start_residue_mod_Q": row_residue,
        "step": r,
        "count": support_size,
    }
    l2_squared = Fraction(Q * (r - 1), r * r)
    lower_bound_per_unit_mass = math.sqrt(r - 1) / math.sqrt(Q * (Q - 1))
    return {
        "Q": Q,
        "support_condition": support_residue_progression,
        "support_size": support_size,
        "support_density": fraction_text(Fraction(1, r)),
        "test_function": f"F(a)=1_{{a≡{row_residue} mod {r}}}-1/{r}",
        "kappa_on_support": fraction_text(Fraction(r - 1, r)),
        "l2_squared_unnormalized": fraction_text(l2_squared),
        "nonzero_fourier_frequencies": [
            step * (Q // r) for step in range(1, r)
        ],
        "fourier_magnitude_on_nonzero_support_frequencies": support_size,
        "candidate_L_PDEC_per_unit_mass_template_norm": {
            "exact_formula": f"sqrt({r - 1})/sqrt({Q}*{Q - 1})",
            "decimal_value": lower_bound_per_unit_mass,
        },
        "missing_for_exclusion": [
            "同一正式坏窗族 S_tau 的负载 |S_tau|",
            "可逐相位验证的 CRT 上界 U_CRT",
            "严格余量 U_CRT < L_PDEC",
        ],
    }


def endpoint_split_packet(Q: int, r: int, row_residue: int, p: int) -> dict[str, Any]:
    """按端点 `ap` 是否已被下层小素数杀死，拆分 seam 支持集。"""
    primes = primes_upto(r)
    lower_primes = [prime for prime in primes if prime < r]
    rough_residues: list[int] = []
    killed_label_histogram: dict[int, int] = {}
    for residue in range(row_residue, Q, r):
        label = first_dividing_prime(residue, lower_primes)
        if label is None:
            rough_residues.append(residue)
            continue
        killed_label_histogram[label] = killed_label_histogram.get(label, 0) + 1

    expected_rough = math.prod(prime - 1 for prime in lower_primes)
    killed_size = Q // r - len(rough_residues)
    return {
        "endpoint": "ap",
        "lower_sieve_status": {
            "rough_condition": f"gcd(a, {Q})=1 under a≡{row_residue} mod {r}",
            "rough_support_size": len(rough_residues),
            "rough_support_size_expected": expected_rough,
            "rough_support_residues_mod_Q": rough_residues,
            "killed_support_size": killed_size,
            "least_lower_label_histogram": dict(sorted(killed_label_histogram.items())),
        },
        "branch_split": [
            "若 a 非 Q-unit，端点 ap 已由最小下层标签 ell<r 杀死，可进入下层标签账本",
            f"若 a 是 Q-unit，端点 ap 的唯一强制标签是新增素数 p={p}",
            "unit 端点分支若持久复现，需要列见证位移或 endpoint-PDEC 上界来排除",
        ],
    }


def seam_row(p: int, r: int, delta: int, modulus: int) -> dict[str, Any]:
    """生成单个 seam 相位行。"""
    gap = p - r
    row_residue = residue_for_delta(p, r, delta)
    left_cap_length = delta
    right_cap_length = r + gap - delta
    left_missing_length = r - delta
    right_missing_length = delta - gap
    return {
        "p": p,
        "r": r,
        "gap": gap,
        "Q": modulus,
        "delta": delta,
        "row_residue_mod_r": row_residue,
        "full_phase_cardinality_in_Q": modulus // r,
        "left_cap_length": left_cap_length,
        "right_cap_length": right_cap_length,
        "total_seam_length": left_cap_length + right_cap_length,
        "left_missing_length": left_missing_length,
        "right_missing_length": right_missing_length,
        "missing_mass": left_missing_length + right_missing_length,
        "missing_mass_expected": r - gap,
        "endpoint_survivor_position": "right_endpoint_ap_only",
        "pdec_support_description": (
            "row phases a mod Q with a mod r equal to row_residue_mod_r"
        ),
        "pdec_support_packet": pdec_support_packet(modulus, r, row_residue),
        "endpoint_split_packet": endpoint_split_packet(modulus, r, row_residue, p),
        "columncrt_hook": [
            "right endpoint ap is the only possible r-rough survivor",
            "persistent seam fixes delta and adjacent lower-row cap lengths",
            "any repeated endpoint/label displacement should enter ColumnCRT",
            "unit endpoint branch still needs label selector lambda and same-column witness Pi",
        ],
    }


def build(source_path: Path) -> dict[str, Any]:
    """构造 first-grid-fail seam 证书。"""
    source = json.loads(source_path.read_text(encoding="utf-8"))
    seam_rows = []
    transition_rows = []
    for item in source["transition_summaries"]:
        p = item["p"]
        r = item["r"]
        gap = p - r
        modulus = item["phase_modulus_primorial_r"]
        deltas = list(range(gap + 1, r))
        rows = [seam_row(p, r, delta, modulus) for delta in deltas]
        seam_rows.extend(rows)
        transition_rows.append(
            {
                "p": p,
                "r": r,
                "gap": gap,
                "Q": modulus,
                "grid_fail_delta_count": len(deltas),
                "grid_fail_deltas": deltas,
                "grid_fail_residues_mod_r": [
                    row["row_residue_mod_r"] for row in rows
                ],
                "full_Q_grid_fail_cardinality": sum(
                    row["full_phase_cardinality_in_Q"] for row in rows
                ),
                "source_grid_fail_count": item["counts"].get("grid_fail", 0),
                "count_matches_source": sum(
                    row["full_phase_cardinality_in_Q"] for row in rows
                )
                == item["counts"].get("grid_fail", 0),
            }
        )

    return {
        "status": "rpz_first_grid_fail_seam_normal_form_certificate",
        "source": str(source_path),
        "summary": {
            "transition_count": len(transition_rows),
            "transitions_with_grid_fail": sum(
                1 for row in transition_rows if row["grid_fail_delta_count"] > 0
            ),
            "seam_phase_row_count": len(seam_rows),
            "full_Q_grid_fail_cardinality": sum(
                row["full_phase_cardinality_in_Q"] for row in seam_rows
            ),
            "count_mismatches": sum(
                1 for row in transition_rows if not row["count_matches_source"]
            ),
            "endpoint_rough_phase_count": sum(
                row["endpoint_split_packet"]["lower_sieve_status"][
                    "rough_support_size"
                ]
                for row in seam_rows
            ),
            "endpoint_killed_phase_count": sum(
                row["endpoint_split_packet"]["lower_sieve_status"][
                    "killed_support_size"
                ]
                for row in seam_rows
            ),
            "pdec_support_rows_with_fourier_packet": len(seam_rows),
        },
        "transition_rows": transition_rows,
        "seam_phase_rows": seam_rows,
        "review_boundary": [
            "first-grid-fail 已压成双帽 seam 标准形",
            "该证书不排除 seam 相位",
            "后续仍需 PDEC/ColumnCRT 排斥或全局相位避开证明",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ First-Grid-Fail Seam 标准形证书",
        "",
        "**状态：** `rpz_first_grid_fail_seam_normal_form_certificate`",
        "",
        "## 标准形",
        "",
        "设 `g=p-r`，`delta=-(a-1)g mod r`。首个 `grid_fail` 当且仅当 `g<delta<r`。此时 `p` 行跨相邻两条 `r` 行：",
        "",
        "```text",
        "left cap length  = delta；",
        "right cap length = r+g-delta；",
        "left missing     = r-delta；",
        "right missing    = delta-g；",
        "missing mass     = r-g。",
        "```",
        "",
        "该 seam 内的 `r`-筛幸存者至多为右端点 `ap`。",
        "",
        "## 总结",
        "",
        f"- 转换数：`{summary['transition_count']}`。",
        f"- 含 grid_fail 的转换数：`{summary['transitions_with_grid_fail']}`。",
        f"- seam 相位行数：`{summary['seam_phase_row_count']}`。",
        f"- 完整 `Q` 中 grid_fail 相位基数：`{summary['full_Q_grid_fail_cardinality']}`。",
        f"- 端点 `ap` 为下层 `Q`-unit 的相位数：`{summary['endpoint_rough_phase_count']}`。",
        f"- 端点已由下层小素因子杀死的相位数：`{summary['endpoint_killed_phase_count']}`。",
        f"- 已生成 PDEC/Fourier 支持包的 seam 行数：`{summary['pdec_support_rows_with_fourier_packet']}`。",
        f"- 与源账本计数不一致数：`{summary['count_mismatches']}`。",
        "",
        "## 转换表",
        "",
        "| p | r | Q | gap | fail deltas | fail residues mod r | source fail count | count ok |",
        "|---:|---:|---:|---:|---|---|---:|---|",
    ]
    for row in result["transition_rows"]:
        lines.append(
            "| {p} | {r} | {Q} | {gap} | `{deltas}` | `{residues}` | {count} | {ok} |".format(
                p=row["p"],
                r=row["r"],
                Q=row["Q"],
                gap=row["gap"],
                deltas=row["grid_fail_deltas"],
                residues=row["grid_fail_residues_mod_r"],
                count=row["source_grid_fail_count"],
                ok="yes" if row["count_matches_source"] else "no",
            )
        )

    lines.extend(
        [
            "",
            "## PDEC/ColumnCRT 增强证书行",
            "",
            "每条 seam 相位现在带有两类可审查对象：",
            "",
            "1. `pdec_support_packet`：精确支持集 `a≡rho mod r`、测试函数 `F=1_{rho}-1/r`、非零 Fourier 频率与模板归一化下的 `L_PDEC/|S_tau|` 候选值；",
            "2. `endpoint_split_packet`：把端点 `ap` 分成已由下层小素数杀死的分支与 `Q`-unit 端点分支。后者的强制标签是新增素数 `p`，必须继续接入 endpoint-PDEC 或 ColumnCRT 位移证书。",
            "",
            "| p | r | delta | rho=a mod r | support | unit endpoint | killed endpoint | Fourier frequencies |",
            "|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in result["seam_phase_rows"]:
        split = row["endpoint_split_packet"]["lower_sieve_status"]
        pdec = row["pdec_support_packet"]
        lines.append(
            "| {p} | {r} | {delta} | {rho} | {support} | {unit} | {killed} | `{freq}` |".format(
                p=row["p"],
                r=row["r"],
                delta=row["delta"],
                rho=row["row_residue_mod_r"],
                support=pdec["support_size"],
                unit=split["rough_support_size"],
                killed=split["killed_support_size"],
                freq=pdec["nonzero_fourier_frequencies"],
            )
        )

    lines.extend(
        [
            "",
            "## 新的严格进展与剩余缺口",
            "",
            "本轮补强把 seam 的 `PDEC` 输入从口头描述升级为精确相位支持行：支持集是单个 `mod r` 非零余类，Fourier 支持只落在 `Q/r` 的非零倍频上，且 `F` 的 `kappa` 与 `L2` 范数均为有理可复核对象。",
            "",
            "同时，端点 `ap` 已被拆成两支：若 `a` 有下层小素因子，则端点已经由该标签解释；若 `a` 是 `Q`-unit，则 seam 的唯一新增标签是 `p`，这正是后续 `ColumnCRT` 位移选择器或 endpoint-PDEC 上界必须处理的窄接口。",
            "",
            "仍未完成的硬缺口是：尚未给出同一正式坏窗族上的 `U_CRT<L_PDEC` 上界，也尚未给出 unit 端点分支的列见证选择器 `Pi`、标签选择器 `lambda` 和位移阈值 `L_D`。因此本文件仍是证书接口增强，不是 seam 排斥定理。",
        ]
    )

    lines.extend(
        [
            "",
            "## 证书意义",
            "",
            "first-grid-fail seam 不是任意坏窗。它具有固定双帽结构、固定缺口守恒 `r-g`，且最多只有右端点 `ap` 一个 `r`-rough 幸存者。持久出现时，相位 `delta` 和行号余类 `a mod r` 被固定，适合进入 `PDEC`；若右端点幸存者携带稳定列位移或吸收标签，则进入 `ColumnCRT`。",
            "",
            "本证书只完成标准形抽取，不排除这些 seam 相位。下一步需要提交 `PDEC/ColumnCRT` 排斥证书，或证明正式反例族不能命中这些 seam 相位。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(
            "docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.json"
        ),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-first-grid-fail-seam-certificate"),
    )
    args = parser.parse_args()
    result = build(args.source)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
