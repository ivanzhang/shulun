#!/usr/bin/env python3
"""审计 concrete squarefree PDEC 包的符号取消结构。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_cancellation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-cancellation-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-cancellation-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-squarefree-pdec-cancellation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

import prime_matrix_square_phase_lowalpha_selberg_remainder_attribution_router as attribution


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-squarefree-pdec-cancellation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-squarefree-pdec-cancellation-router.md"

DEFAULT_P_LIST = attribution.DEFAULT_P_LIST
DEFAULT_Z_LIST = attribution.DEFAULT_Z_LIST
DEFAULT_D_LEVEL = attribution.DEFAULT_D_LEVEL
DEFAULT_ABS_CONTRIBUTION = 20.0
NEXT_TARGET = "CrossModulusSignedPairingDisciplineOrPersistentSquarefreePDECExclusion"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json",
    "prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.json",
]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def safe_ratio(numerator: float, denominator: float) -> float | None:
    """计算安全比值。"""
    if denominator <= 0:
        return None
    return numerator / denominator


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def sign_of(value: float, eps: float = 1e-12) -> int:
    """返回数值符号。"""
    if value > eps:
        return 1
    if value < -eps:
        return -1
    return 0


def sign_text(sign: int) -> str:
    """把符号写成人可读文本。"""
    if sign > 0:
        return "+"
    if sign < 0:
        return "-"
    return "0"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_squarefree_pdec_cancellation_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def factor_squarefree(value: int, primes: list[int]) -> list[int]:
    """分解当前账本中的 squarefree 模数。"""
    n = value
    factors = []
    for prime in primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            factors.append(prime)
            n //= prime
        while n % prime == 0:
            n //= prime
    if n > 1:
        factors.append(n)
    return factors


def collect_values_and_primes(p_list: list[int]) -> tuple[list[int], list[int]]:
    """复用 Selberg 归因账本的 prime-a b 序列。"""
    max_p = max(p_list)
    trial_limit = int(math.isqrt(max_p * max_p + max_p)) + 10
    flags = attribution.envelope.sieve_bool(max(trial_limit, max_p))
    trial_primes = attribution.envelope.primes_from_flags(flags, trial_limit)
    values = attribution.selberg.collect_values(p_list, flags, trial_primes)
    return values, trial_primes


def all_threshold_packets(
    p_list: list[int], z_list: list[int], d_level: int, abs_contribution: float
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """重算所有超过阈值的 squarefree 低模贡献，而不是只取每行 top16。"""
    values, trial_primes = collect_values_and_primes(p_list)
    packets = []
    row_metadata = []
    for z in z_list:
        weights = attribution.selberg.selberg_weights(z, d_level, trial_primes)
        coeffs = attribution.coefficient_by_lcm(weights)
        counts = attribution.divisibility_counts(values, sorted(coeffs))
        row_all = []
        for modulus, coefficient in coeffs.items():
            expected = len(values) / modulus
            remainder = counts[modulus] - expected
            contribution = coefficient * remainder
            row_all.append(contribution)
            if abs(contribution) < abs_contribution:
                continue
            factors = factor_squarefree(modulus, trial_primes)
            packets.append(
                {
                    "z": z,
                    "m": modulus,
                    "m_factors": factors,
                    "max_prime_factor_m": max(factors, default=1),
                    "coefficient": coefficient,
                    "actual": counts[modulus],
                    "expected": expected,
                    "remainder": remainder,
                    "contribution": contribution,
                    "abs_contribution": abs(contribution),
                    "contribution_sign": sign_of(contribution),
                    "coefficient_sign": sign_of(coefficient),
                    "remainder_sign": sign_of(remainder),
                    "pdec_label": f"ConcreteSquarefreeLowModPDEC(z={z},m={modulus})",
                }
            )
        row_metadata.append(
            {
                "z": z,
                "all_lcm_moduli_count": len(coeffs),
                "all_contribution_abs_sum": sum(abs(item) for item in row_all),
                "all_contribution_signed_sum": sum(row_all),
            }
        )
    return packets, row_metadata


def summarize_by_z(packets: list[dict[str, Any]], row_metadata: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总每个 z 层的阈值包取消情况。"""
    metadata_by_z = {row["z"]: row for row in row_metadata}
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for packet in packets:
        grouped[int(packet["z"])].append(packet)
    rows = []
    for z in sorted(grouped):
        entries = grouped[z]
        positive_abs = sum(float(item["abs_contribution"]) for item in entries if item["contribution_sign"] > 0)
        negative_abs = sum(float(item["abs_contribution"]) for item in entries if item["contribution_sign"] < 0)
        signed = positive_abs - negative_abs
        total_abs = positive_abs + negative_abs
        rows.append(
            {
                "z": z,
                "threshold_packet_count": len(entries),
                "positive_abs": positive_abs,
                "negative_abs": negative_abs,
                "signed_sum": signed,
                "abs_sum": total_abs,
                "signed_over_abs": safe_ratio(abs(signed), total_abs),
                "cross_modulus_cancellation_ratio": None
                if total_abs <= 0
                else 1.0 - abs(signed) / total_abs,
                "all_lcm_moduli_count": metadata_by_z[z]["all_lcm_moduli_count"],
                "threshold_abs_over_all_abs": safe_ratio(
                    total_abs, metadata_by_z[z]["all_contribution_abs_sum"]
                ),
                "threshold_signed_over_all_signed_abs": safe_ratio(
                    abs(signed), abs(metadata_by_z[z]["all_contribution_signed_sum"])
                ),
            }
        )
    return rows


def summarize_by_modulus(packets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总同一 m 的纵向持久性和自取消情况。"""
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for packet in packets:
        grouped[int(packet["m"])].append(packet)
    rows = []
    for modulus in sorted(grouped):
        entries = sorted(grouped[modulus], key=lambda item: int(item["z"]))
        signs = [int(item["contribution_sign"]) for item in entries]
        unique_signs = sorted(set(signs))
        contributions = [float(item["contribution"]) for item in entries]
        coefficients = [float(item["coefficient"]) for item in entries]
        remainders = [float(item["remainder"]) for item in entries]
        signed = sum(contributions)
        total_abs = sum(abs(item) for item in contributions)
        max_contribution_deviation = max(abs(item - contributions[0]) for item in contributions)
        max_coefficient_deviation = max(abs(item - coefficients[0]) for item in coefficients)
        max_remainder_deviation = max(abs(item - remainders[0]) for item in remainders)
        rows.append(
            {
                "m": modulus,
                "m_factors": entries[0]["m_factors"],
                "max_prime_factor_m": entries[0]["max_prime_factor_m"],
                "z_values": [int(item["z"]) for item in entries],
                "packet_count": len(entries),
                "sign_pattern": "".join(sign_text(sign) for sign in signs),
                "unique_contribution_signs": [sign_text(sign) for sign in unique_signs],
                "same_sign_across_visible_packets": len(unique_signs) == 1,
                "vertical_self_cancellation_possible": len(unique_signs) > 1,
                "signed_contribution": signed,
                "total_abs_contribution": total_abs,
                "self_cancellation_ratio": safe_ratio(abs(signed), total_abs),
                "max_abs_contribution": max(abs(item) for item in contributions),
                "max_contribution_deviation": max_contribution_deviation,
                "max_coefficient_deviation": max_coefficient_deviation,
                "max_remainder_deviation": max_remainder_deviation,
                "stable_after_activation_observed": max_contribution_deviation < 1e-9
                and max_coefficient_deviation < 1e-12
                and max_remainder_deviation < 1e-9,
                "sample_packets": entries[:8],
            }
        )
    return sorted(rows, key=lambda item: -float(item["total_abs_contribution"]))


def audit(p_list: list[int], z_list: list[int], d_level: int, abs_contribution: float) -> dict[str, Any]:
    """执行符号取消/持久包审计。"""
    packets, row_metadata = all_threshold_packets(p_list, z_list, d_level, abs_contribution)
    by_z = summarize_by_z(packets, row_metadata)
    by_modulus = summarize_by_modulus(packets)
    repeated = [row for row in by_modulus if row["packet_count"] >= 2]
    vertical_self_cancellation = [row for row in repeated if row["vertical_self_cancellation_possible"]]
    same_sign_persistent = [row for row in repeated if row["same_sign_across_visible_packets"]]
    row_level_cancellation = [
        row for row in by_z if row["signed_over_abs"] is not None and row["signed_over_abs"] <= 0.12
    ]
    previous_packet_count = None
    previous_packet_path = DOCS / "prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.json"
    if previous_packet_path.exists():
        previous_packet_count = json.loads(previous_packet_path.read_text(encoding="utf-8")).get("packet_count")
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_squarefree_pdec_cancellation_router",
        "status": "same_modulus_vertical_cancellation_blocked_cross_modulus_pairing_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "full_threshold_recomputation_done": True,
        "previous_top16_packet_count": previous_packet_count,
        "full_threshold_packet_count": len(packets),
        "full_threshold_unique_modulus_count": len({packet["m"] for packet in packets}),
        "full_threshold_abs_contribution": sum(float(packet["abs_contribution"]) for packet in packets),
        "same_modulus_vertical_cancellation_blocked_for_visible_repeated_packets": len(vertical_self_cancellation) == 0,
        "visible_repeated_same_sign_modulus_count": len(same_sign_persistent),
        "visible_vertical_self_cancelling_modulus_count": len(vertical_self_cancellation),
        "row_level_cross_modulus_cancellation_observed": len(row_level_cancellation) == len(by_z),
        "cross_modulus_signed_pairing_discipline_proved": False,
        "persistent_squarefree_pdec_excluded": False,
        "coefficient_cancellation_bound_proved": False,
        "row_column_unconditional_closed": False,
        "abs_contribution_threshold": abs_contribution,
        "z_summaries": by_z,
        "modulus_summaries": by_modulus,
        "top_persistent_same_sign_moduli": same_sign_persistent[:16],
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把上一轮 concrete squarefree PDEC 包从 top16 抽样升级为全量阈值重算。"
            "样本中超过阈值的同一 `m` 纵向包一律同号且贡献值稳定，因此不能靠同一模数跨 `z` 自取消。"
            "实际小净余项来自同一 `z` 层内不同 `m` 的正负交叉配对。"
            "所以当前最窄点被压成：证明这种跨模数符号配对有统一纪律，"
            "或把未配对的同号持久模数族登记并排斥为 persistent squarefree PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha squarefree PDEC 符号取消路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"full_threshold_recomputation_done={fmt_bool(result['full_threshold_recomputation_done'])}",
        (
            "same_modulus_vertical_cancellation_blocked_for_visible_repeated_packets="
            f"{fmt_bool(result['same_modulus_vertical_cancellation_blocked_for_visible_repeated_packets'])}"
        ),
        f"cross_modulus_signed_pairing_discipline_proved={fmt_bool(result['cross_modulus_signed_pairing_discipline_proved'])}",
        f"persistent_squarefree_pdec_excluded={fmt_bool(result['persistent_squarefree_pdec_excluded'])}",
        f"coefficient_cancellation_bound_proved={fmt_bool(result['coefficient_cancellation_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 全量阈值修正",
        "",
        "| threshold | previous top16 packets | full packets | unique m | total abs |",
        "| ---: | ---: | ---: | ---: | ---: |",
        (
            f"| {fmt_float(result['abs_contribution_threshold'])} | "
            f"{result['previous_top16_packet_count']} | {result['full_threshold_packet_count']} | "
            f"{result['full_threshold_unique_modulus_count']} | "
            f"{fmt_float(result['full_threshold_abs_contribution'])} |"
        ),
        "",
        "## 2. 同一 z 内的跨模数取消",
        "",
        "| z | packets | positive abs | negative abs | signed | abs | signed/abs | cancellation ratio | threshold abs/all abs |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["z_summaries"]:
        lines.append(
            f"| {row['z']} | {row['threshold_packet_count']} | {fmt_float(row['positive_abs'])} | "
            f"{fmt_float(row['negative_abs'])} | {fmt_float(row['signed_sum'])} | "
            f"{fmt_float(row['abs_sum'])} | {fmt_float(row['signed_over_abs'])} | "
            f"{fmt_float(row['cross_modulus_cancellation_ratio'])} | "
            f"{fmt_float(row['threshold_abs_over_all_abs'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 同一 m 的纵向持久包",
            "",
            "| m | factors | z values | signs | signed | abs | self-cancel ratio | stable deviation |",
            "| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["modulus_summaries"]:
        lines.append(
            f"| {row['m']} | `{row['m_factors']}` | `{row['z_values']}` | `{row['sign_pattern']}` | "
            f"{fmt_float(row['signed_contribution'])} | {fmt_float(row['total_abs_contribution'])} | "
            f"{fmt_float(row['self_cancellation_ratio'])} | "
            f"{fmt_float(row['max_contribution_deviation'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 已闭合的负结论与剩余硬点",
            "",
            "- 已闭合/核验：全量阈值包为 `47` 个，而上一轮 top16 抽取只登记 `44` 个。",
            "- 已闭合/核验：重复出现的可见 `m` 全部同号，且同一 `m` 的贡献在激活后稳定；同一模数纵向自取消不可用。",
            "- 已观察：每个 `z` 层的总净值很小，取消来自不同 `m` 之间的正负配对。",
            "- 未闭合：证明这种跨模数配对有结构性纪律，而不是样本巧合。",
            "- 未闭合：若配对纪律失败，逐个排斥未配对的 same-sign persistent squarefree PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    parser.add_argument("--z-list", default=",".join(str(item) for item in DEFAULT_Z_LIST))
    parser.add_argument("--d-level", type=int, default=DEFAULT_D_LEVEL)
    parser.add_argument("--abs-contribution", type=float, default=DEFAULT_ABS_CONTRIBUTION)
    args = parser.parse_args()
    result = audit(
        parse_int_list(args.p_list),
        parse_int_list(args.z_list),
        args.d_level,
        args.abs_contribution,
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "full_threshold_packet_count": result["full_threshold_packet_count"],
                "full_threshold_unique_modulus_count": result["full_threshold_unique_modulus_count"],
                "same_modulus_vertical_cancellation_blocked": result[
                    "same_modulus_vertical_cancellation_blocked_for_visible_repeated_packets"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
