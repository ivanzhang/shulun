#!/usr/bin/env python3
"""把 Möbius 重叠谱压成仿射等差段倒数自交高谱。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_mobius_to_affine_inverse_high_spectrum_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-mobius-to-affine-inverse-high-spectrum-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-mobius-to-affine-inverse-high-spectrum-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-mobius-to-affine-inverse-high-spectrum-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.json"
POWER_RELAX = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
ENERGY_CORE = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
P0_STATUS = DOCS / "explicit-p0-constants.status.md"

SOURCE_FILES = [PREVIOUS, POWER_RELAX, ENERGY_CORE, P0_STATUS]

TARGET = "OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving"
NEXT_ATOM = "AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23"
INCIDENCE_ROUTE = "RudnevRNRSAffineProgressionInverseIntersectionIncidenceEstimate"
PGL2_ROUTE = "PGL2IntervalAlmostStabilizerPowerSavingForMobiusInvolutions"


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


def build_result() -> dict[str, Any]:
    """构造仿射倒数自交高谱证书。"""
    previous = load_json(PREVIOUS)
    power_relax = load_json(POWER_RELAX)
    energy_core = load_json(ENERGY_CORE)
    p0_status = read_text(P0_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    mobius_identity_imported = previous.get("mobius_overlap_identity_closed") is True
    dyadic_criterion_imported = previous.get("dyadic_spectrum_criterion_closed") is True
    power_target_imported = power_relax.get("fixed_power_saving_implies_required_log_saving") is True
    unweighted_core_imported = energy_core.get("divisor_weighted_to_unweighted_reduction_closed") is True
    incidence_route_known = contains_all(p0_status, ["Rudnev", "sum-product", "能量"])

    affine_inverse_identity_closed = (
        active
        and mobius_identity_imported
        and dyadic_criterion_imported
        and power_target_imported
        and unweighted_core_imported
    )

    # 若 r_s=|{a in J: phi_s(a) in J}|，令 x=sa-1。
    # 由 phi_s(a)=a/(sa-1)，可得 s*phi_s(a)-1=(sa-1)^(-1)。
    # 因此 b=phi_s(a) in J 等价于 x in A_s=sJ-1 且 x^(-1) in A_s。
    # 于是 r_s=|A_s cap A_s^(-1)|，这是完全等价的刚性自交形式。
    low_high_split_closed = affine_inverse_identity_closed
    high_spectrum_power_saving_proved = False

    affine_reduction = {
        "mobius_overlap": "r_J(s)=#{a in J: a/(s*a-1) in J}",
        "affine_progression": "A_s=sJ-1={s*a-1: a in J}",
        "inverse_self_intersection_identity": "r_J(s)=|A_s cap A_s^(-1)|",
        "proof_line": "x=s*a-1 and b=a/(s*a-1) imply s*b-1=x^(-1)",
        "low_overlap_absorption": "for any fixed eta>0, sum_{r_s<=N^(1-eta)} r_s^2 <= N^(1-eta) sum_s r_s = N^(3-eta)",
        "remaining_high_spectrum": "control s with |A_s cap A_s^(-1)| > N^(1-eta)",
        "structural_meaning": "a bad spectrum means many affine images of J are unusually stable under inversion",
        "allowed_next_tools": "self-contained incidence on xy=1 against affine progressions, or PGL2 almost-stabilizer expansion",
    }

    rows = [
        row(
            "MobiusSpectrumTargetActive",
            active,
            True,
            "上一证书已把固定幂能量核心压成一参数 Möbius interval-overlap 谱。",
            TARGET,
        ),
        row(
            "AffineInverseSelfIntersectionIdentityClosed",
            affine_inverse_identity_closed,
            True,
            "`phi_s` 重叠完全等价于仿射等差段 `A_s=sJ-1` 与其倒数像自交。",
            NEXT_ATOM,
        ),
        row(
            "LowOverlapLayerAutomaticallyAbsorbed",
            low_high_split_closed,
            True,
            "低重叠层由 `sum r_s=N^2` 直接给固定幂节省；只有高重叠谱需要深估计。",
            NEXT_ATOM,
        ),
        row(
            "IncidenceAndSumProductRouteStillAligned",
            incidence_route_known,
            True,
            "Rudnev/RNRS/sum-product 路线可解释为 `xy=1` 与仿射进度族的高自交排斥。",
            INCIDENCE_ROUTE,
        ),
        row(
            NEXT_ATOM,
            high_spectrum_power_saving_proved,
            False,
            "仓库内尚未证明许多 `s` 不能使 `|A_s cap A_s^{-1}|` 达到高重叠规模。",
            f"{INCIDENCE_ROUTE} OR {PGL2_ROUTE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是等价改写和低重叠吸收，不是高谱排斥本身。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_mobius_to_affine_inverse_high_spectrum_router",
        "status": "mobius_overlap_spectrum_reduced_to_affine_progression_inverse_self_intersection_high_spectrum",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "mobius_spectrum_target_active": active,
        "affine_inverse_self_intersection_identity_closed": affine_inverse_identity_closed,
        "low_overlap_layer_automatically_absorbed": low_high_split_closed,
        "incidence_and_sum_product_route_still_aligned": incidence_route_known,
        "affine_inverse_high_spectrum_power_saving_proved": high_spectrum_power_saving_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_incidence_target": INCIDENCE_ROUTE,
        "parallel_group_expansion_target": PGL2_ROUTE,
        "affine_reduction": affine_reduction,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前唯一内部自足线继续缩窄：`phi_s(a)=a/(sa-1)` 的区间重叠不是一般 Möbius 图问题，"
            "而是完全等价于仿射等差段 `A_s=sJ-1` 的倒数自交 `|A_s∩A_s^{-1}|`。"
            "同时低重叠层由 `Σ_s r_s=N^2` 自动吸收；真正剩余只剩高重叠谱排斥："
            "证明不能有许多 `s` 使同一个仿射进度段在取倒数后仍大量落回自身。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    reduction = result["affine_reduction"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 Möbius 谱到仿射倒数自交高谱证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"affine_inverse_self_intersection_identity_closed={fmt_bool(result['affine_inverse_self_intersection_identity_closed'])}",
        f"low_overlap_layer_automatically_absorbed={fmt_bool(result['low_overlap_layer_automatically_absorbed'])}",
        f"affine_inverse_high_spectrum_power_saving_proved={fmt_bool(result['affine_inverse_high_spectrum_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 仿射倒数自交改写",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in reduction.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一最窄自足目标",
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
