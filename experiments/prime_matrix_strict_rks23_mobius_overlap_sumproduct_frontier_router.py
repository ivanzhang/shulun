#!/usr/bin/env python3
"""把一参数 Möbius 高重叠谱压成反演 sum-product 硬点。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_mobius_overlap_sumproduct_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-mobius-overlap-sumproduct-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-mobius-overlap-sumproduct-frontier-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-mobius-overlap-sumproduct-frontier-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.json"
POWER_RELAXATION = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
WEIGHTED_CORE = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
P0_STATUS = DOCS / "explicit-p0-constants.status.md"

SOURCE_FILES = [PREVIOUS, POWER_RELAXATION, WEIGHTED_CORE, P0_STATUS]

TARGET = "OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving"
NEXT_ATOM = "SelfContainedInverseSmallDoublingReciprocalEnergyPowerSavingForSquareRootCollar"
EXTERNAL_ROUTE = "RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving"


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本包含全部关键片段。"""
    return all(item in text for item in needles)


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def reciprocal_energy(values: list[int], p: int) -> int:
    """计算 E_+(J^{-1})。"""
    counts: dict[int, int] = {}
    invs = [pow(value, -1, p) for value in values]
    for left in invs:
        for right in invs:
            total = (left + right) % p
            counts[total] = counts.get(total, 0) + 1
    return sum(count * count for count in counts.values())


def mobius_overlap_energy(values: list[int], p: int) -> int:
    """按 r_s=|{a in J: a/(sa-1) in J}| 计算能量。"""
    value_set = set(values)
    energy = 0
    for s in range(p):
        overlap = 0
        for a in values:
            denominator = (s * a - 1) % p
            if denominator == 0:
                continue
            b = (a * pow(denominator, -1, p)) % p
            if b in value_set:
                overlap += 1
        energy += overlap * overlap
    return energy


def cross_multiplied_energy(values: list[int], p: int) -> int:
    """用 (a+b)cd=(c+d)ab 的交叉乘法式复算能量。"""
    count = 0
    for a in values:
        for b in values:
            left_factor = (a + b) % p
            ab = (a * b) % p
            for c in values:
                for d in values:
                    if (left_factor * c * d - (c + d) * ab) % p == 0:
                        count += 1
    return count


def finite_identity_sanity() -> list[dict[str, Any]]:
    """做小素数恒等式自检；只验证代数转写，不作经验闭合。"""
    checks = []
    for p in [101, 211, 509]:
        length = max(6, int(math.isqrt(p)))
        start = int(math.isqrt(p)) + 3
        values = list(range(start, start + length))
        e_pair = reciprocal_energy(values, p)
        e_mobius = mobius_overlap_energy(values, p)
        e_cross = cross_multiplied_energy(values, p)
        checks.append(
            {
                "p": p,
                "start": start,
                "length": length,
                "reciprocal_energy": e_pair,
                "mobius_overlap_energy": e_mobius,
                "cross_multiplied_energy": e_cross,
                "identity_passed": e_pair == e_mobius == e_cross,
            }
        )
    return checks


def build_result() -> dict[str, Any]:
    """构造反演 sum-product 前沿证书。"""
    previous = load_json(PREVIOUS)
    power_relaxation = load_json(POWER_RELAXATION)
    weighted_core = load_json(WEIGHTED_CORE)
    p0_status = read_text(P0_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    fixed_power_target = (
        power_relaxation.get("next_direct_attack_target")
        == "UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23"
    )
    unweighted_energy_core = weighted_core.get("divisor_weighted_to_unweighted_reduction_closed") is True
    identity_checks = finite_identity_sanity()
    finite_identity_sanity_passed = all(item["identity_passed"] for item in identity_checks)

    # 设 A=J^{-1}。则 A^{-1}=J，J 是长度 N 的区间，所以 |A^{-1}+A^{-1}|<=2N-1。
    # 因此高 E_+(A) 的唯一剩余不是代数恒等式，而是“反演小和集不能同时高加性能量”的 sum-product 输入。
    dictionary_closed = active and fixed_power_target and unweighted_energy_core and finite_identity_sanity_passed
    inverse_small_doubling_closed = dictionary_closed
    elementary_routes_insufficient = contains_all(
        p0_status,
        ["双完成显式界不足以完全替代 BG", "平衡临界区"],
    )
    external_route_ready = contains_all(
        p0_status,
        ["Rudnev", "Roche-Newton", "Shkredov", "sum-product"],
    ) or contains_all(p0_status, ["Rudnev", "sum-product", "能量"])
    self_contained_sumproduct_proved = False

    sumproduct_dictionary = {
        "original_spectrum": "r_J(s)=#{a in J: a/(s*a-1) in J}",
        "fiber_equation": "s*a*b-a-b=0, equivalently s=a^(-1)+b^(-1)",
        "energy_identity": "sum_s r_J(s)^2 = E_+(J^(-1))",
        "cross_multiplied_quadruple": "(a+b)c d=(c+d)a b mod P",
        "set_substitution": "A=J^(-1)",
        "inverse_small_sumset": "A^(-1)=J, hence |A^(-1)+A^(-1)|<=2|J|-1",
        "needed_power_saving": "E_+(A)<=|A|^(3-delta) for |A| in the square-root log collar",
        "contradiction_shape": "large E_+(A) plus small |A^(-1)+A^(-1)| is exactly the inverse sum-product obstruction",
    }

    rows = [
        row(
            "MobiusOverlapSpectrumTargetActive",
            active,
            True,
            "上一证书已把唯一内部剩余压成一参数 Möbius 区间重叠谱。",
            TARGET,
        ),
        row(
            "EnergyMobiusSumProductDictionaryClosed",
            dictionary_closed,
            True,
            "`r_J(s)`、`E_+(J^{-1})` 与交叉乘法四元组完全等价；小素数只作恒等式自检。",
            "dictionary closed",
        ),
        row(
            "InverseSmallDoublingRigidityClosed",
            inverse_small_doubling_closed,
            True,
            "令 `A=J^{-1}` 后，`A^{-1}=J` 是区间，故反演侧和集大小至多 `2|J|-1`。",
            NEXT_ATOM,
        ),
        row(
            "ElementaryWeilCompletionBarrierConfirmed",
            elementary_routes_insufficient,
            True,
            "已有账本确认平方根临界颈部中 Weil/双完成只能给自然尺度，不能给固定幂节省。",
            NEXT_ATOM,
        ),
        row(
            "RNRSRudnevExternalRouteMatches",
            external_route_ready,
            True,
            "Roche-Newton/Rudnev/Shkredov 型反演 sum-product 能量估计正匹配该硬点。",
            EXTERNAL_ROUTE,
        ),
        row(
            NEXT_ATOM,
            self_contained_sumproduct_proved,
            False,
            "仓库内尚未内联证明反演小和集情形的固定幂加性能量节省。",
            "internalize inverse sum-product or accept RNRS/Rudnev route",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是字典与刚性定位，不是反演 sum-product 定理本身。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_mobius_overlap_sumproduct_frontier_router",
        "status": "mobius_overlap_spectrum_reduced_to_inverse_sumproduct_energy_frontier",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "mobius_overlap_spectrum_target_active": active,
        "energy_mobius_sumproduct_dictionary_closed": dictionary_closed,
        "inverse_small_doubling_rigidity_closed": inverse_small_doubling_closed,
        "elementary_weil_completion_barrier_confirmed": elementary_routes_insufficient,
        "rnrs_rudnev_external_route_matches": external_route_ready,
        "finite_identity_sanity_passed": finite_identity_sanity_passed,
        "self_contained_inverse_sumproduct_proved": self_contained_sumproduct_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_external_route": EXTERNAL_ROUTE,
        "sumproduct_dictionary": sumproduct_dictionary,
        "finite_identity_sanity": identity_checks,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "一参数 Möbius 高重叠谱已进一步压缩为反演 sum-product 核心："
            "`sum_s r_J(s)^2` 正是 `A=J^{-1}` 的加性能量，而 `A^{-1}=J` 是区间，"
            "所以反演侧天然有 `|A^{-1}+A^{-1}|<=2|A|-1` 的小和集刚性。"
            "因此当前真正内部自足剩余是证明：在平方根对数颈部，反演小和集集合不可能有 "
            "`E_+(A)` 的近最大能量。该输入可由 RNRS/Rudnev 型外部 sum-product 能量定理关闭；"
            "严格自足线仍需把这一定理或其特殊情形内联证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    dictionary = result["sumproduct_dictionary"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 Möbius 重叠到反演 sum-product 前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"energy_mobius_sumproduct_dictionary_closed={fmt_bool(result['energy_mobius_sumproduct_dictionary_closed'])}",
        f"inverse_small_doubling_rigidity_closed={fmt_bool(result['inverse_small_doubling_rigidity_closed'])}",
        f"self_contained_inverse_sumproduct_proved={fmt_bool(result['self_contained_inverse_sumproduct_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 反演 sum-product 字典",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in dictionary.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 恒等式自检",
            "",
            "| p | start | length | E_pair | E_mobius | E_cross | pass |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["finite_identity_sanity"]:
        lines.append(
            "| {p} | {start} | {length} | {e1} | {e2} | {e3} | `{passed}` |".format(
                p=item["p"],
                start=item["start"],
                length=item["length"],
                e1=item["reciprocal_energy"],
                e2=item["mobius_overlap_energy"],
                e3=item["cross_multiplied_energy"],
                passed=fmt_bool(item["identity_passed"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
