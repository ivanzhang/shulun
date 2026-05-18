#!/usr/bin/env python3
"""生成 stable ladder 低纤维 singleton 的相位二分证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_low_fiber_phase_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-singleton-pair-width-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderLowFiberSingletonSurplusOrLongWidthCellPairPDECCap"

IMPORT = "StableActualLadderLowFiberSingletonOrLongPairImportedLedger"
LOW_DICHOTOMY = "StableLadderLowFiberOccupancyOneOrMultiDichotomyLedger"
ISOLATED = "StableLadderFiberIsolatedSingletonAtomLedger"
PIVOT_REDUNDANT = "StableLadderRepeatedPivotModulusForcesIsolationLedger"
COMP_PAIR = "StableLadderComplementFiberAntiPivotPairLedger"
COMP_PERIOD = "StableLadderComplementFiberPeriodAndAntiPivotPhaseLedger"
COMP_WIDTH = "StableLadderComplementFiberPairWidthDichotomyLedger"
FULL_PAIR = "StableLadderLongFullCellPairCarriedForwardLedger"
NO_ANON = "NoAnonymousLowFiberSingletonExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterLowFiberPhaseLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {LOW_DICHOTOMY} AND {ISOLATED} AND {PIVOT_REDUNDANT} "
    f"AND {COMP_PAIR} AND {COMP_PERIOD} AND {COMP_WIDTH} AND {FULL_PAIR} "
    f"AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的低纤维/长宽度硬点替换成相位二分。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造低纤维相位二分判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderLowFiberSingletonOrLongPairImported",
            imported,
            False,
            "上一层把 singleton/pair 出口压成低纤维 singleton 或长宽度 full-cell pair。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderLowFiberOccupancyOneOrMultiDichotomyClosed",
            True,
            True,
            "低纤维 singleton 分支有 1<=L<q_j，因此 L=1 或 2<=L<q_j。",
            LOW_DICHOTOMY,
        ),
        row(
            "StableLadderFiberIsolatedSingletonAtomRegistered",
            True,
            False,
            "L=1 分支登记为补坐标纤维孤立 singleton atom；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderRepeatedPivotModulusForcesIsolationClosed",
            True,
            True,
            "若 pivot 素数 q_j 已在补坐标周期 W_-j 中出现，则固定补纤维已决定 pivot 残基，M_s=1 强制 L=1。",
            PIVOT_REDUNDANT,
        ),
        row(
            "StableLadderComplementFiberAntiPivotPairClosed",
            True,
            True,
            "若 2<=L<q_j，则 singleton 点与另一补纤维点给出同补坐标但不同 pivot 残基的双点。",
            COMP_PAIR,
        ),
        row(
            "StableLadderComplementFiberPeriodAndAntiPivotPhaseClosed",
            True,
            True,
            "该双点差值被 W_-j 整除且不被 q_j 整除；这是补周期对齐与 pivot 反对齐的显式相位出口。",
            COMP_PERIOD,
        ),
        row(
            "StableLadderComplementFiberPairWidthDichotomyClosed",
            True,
            True,
            "若承载支撑直径 H<W_-j，则补纤维双点不可能；否则登记 H>=W_-j 的补纤维 pair cap。",
            COMP_WIDTH,
        ),
        row(
            "StableLadderLongFullCellPairCarriedForward",
            True,
            False,
            "上一层 H>=W 的 full-cell period-pair 继续作为长宽度 PDEC/cap 输入。",
            FULL_PAIR,
        ),
        row(
            "NoAnonymousLowFiberSingletonExit",
            True,
            True,
            "低纤维 singleton 出口被拆成孤立 atom 或 anti-pivot complement pair，不再匿名。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterLowFiberPhase",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "IsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairStillOpen",
            False,
            False,
            "仍未证明孤立 singleton 可求和，也未排斥 anti-pivot complement pair 或 long full-cell pair。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、anti-pivot complement pair、long full-cell pair 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造低纤维相位二分证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "低纤维 singleton 分支 1<=L<q_j 可继续二分。若 L=1，则它是补坐标纤维孤立 atom；"
        "若 2<=L<q_j，则 singleton 点和另一补纤维点有相同补坐标但不同 pivot 残基，"
        "故差值被 W_-j=lcm_{i!=j}(q_i) 整除且不被 q_j 整除。若 H<W_-j，该分支被排斥；"
        "否则成为显式 anti-pivot complement-pair PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_low_fiber_phase_router",
        "status": "low_fiber_singleton_split_to_isolated_or_antipivot_complement_pair_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "low_fiber_or_long_pair_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "low_fiber_occupancy_dichotomy_closed": True,
        "isolated_singleton_atom_registered": True,
        "repeated_pivot_modulus_forces_isolation": True,
        "anti_pivot_complement_pair_closed": True,
        "complement_period_and_antipivot_phase_closed": True,
        "complement_pair_width_dichotomy_closed": True,
        "long_full_cell_pair_carried_forward": True,
        "anonymous_low_fiber_singleton_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "anti_pivot_complement_pair_pdec_cap_proved": False,
        "long_full_cell_pair_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "phase_formulas": {
            "low_fiber_range": "1<=L<q_j",
            "low_fiber_dichotomy": "L=1 OR 2<=L<q_j",
            "isolated_branch": "L=1 is a complement-fiber isolated singleton atom",
            "complement_period": "W_-j=lcm_{i!=j}(q_i), with W_-j=1 for empty complement",
            "redundant_pivot": "q_j|W_-j => fixed complement already fixes pivot residue; M_s=1 forces L=1",
            "anti_pivot_pair": "2<=L<q_j => exists n1<n2 with W_-j|(n2-n1) and q_j∤(n2-n1)",
            "short_complement_width_exclusion": "H<W_-j => no anti-pivot complement pair",
            "long_full_cell_pair": "full-cell pair from previous step remains H>=W=lcm_i(q_i)",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder low-fiber phase 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"low_fiber_or_long_pair_imported={fmt_bool(cert['low_fiber_or_long_pair_imported'])}",
        f"low_fiber_occupancy_dichotomy_closed={fmt_bool(cert['low_fiber_occupancy_dichotomy_closed'])}",
        f"isolated_singleton_atom_registered={fmt_bool(cert['isolated_singleton_atom_registered'])}",
        f"repeated_pivot_modulus_forces_isolation={fmt_bool(cert['repeated_pivot_modulus_forces_isolation'])}",
        f"anti_pivot_complement_pair_closed={fmt_bool(cert['anti_pivot_complement_pair_closed'])}",
        f"complement_period_and_antipivot_phase_closed={fmt_bool(cert['complement_period_and_antipivot_phase_closed'])}",
        f"complement_pair_width_dichotomy_closed={fmt_bool(cert['complement_pair_width_dichotomy_closed'])}",
        f"long_full_cell_pair_carried_forward={fmt_bool(cert['long_full_cell_pair_carried_forward'])}",
        f"anonymous_low_fiber_singleton_removed={fmt_bool(cert['anonymous_low_fiber_singleton_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"anti_pivot_complement_pair_pdec_cap_proved={fmt_bool(cert['anti_pivot_complement_pair_pdec_cap_proved'])}",
        f"long_full_cell_pair_pdec_cap_proved={fmt_bool(cert['long_full_cell_pair_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 低纤维占位二分",
        "",
        "上一层给出低纤维 singleton：",
        "",
        "```text",
        "M_s=1, 1<=L<q_j.",
        "```",
        "",
        "因此只有：",
        "",
        "```text",
        "L=1 OR 2<=L<q_j.",
        "```",
        "",
        "`L=1` 是补坐标纤维孤立 singleton atom。",
        "",
        "## 2. 补纤维 anti-pivot 相位",
        "",
        "若 `2<=L<q_j`，取 singleton 点和同补纤维内另一点。它们补坐标相同、pivot 残基不同。令：",
        "",
        "```text",
        "W_-j=lcm_{i!=j}(q_i), empty lcm = 1.",
        "```",
        "",
        "则该双点满足：",
        "",
        "```text",
        "W_-j | (n2-n1),",
        "q_j does not divide (n2-n1).",
        "```",
        "",
        "若 `q_j|W_-j`，固定补坐标已决定 pivot 残基，所以 `M_s=1` 强制 `L=1`；非孤立分支必须是真正的 anti-pivot 相位不对齐。",
        "",
        "## 3. 宽度出口",
        "",
        "若承载支撑直径为 `H`，补纤维双点给出：",
        "",
        "```text",
        "H>=W_-j.",
        "```",
        "",
        "因此 `H<W_-j` 排斥补纤维双点；`H>=W_-j` 则登记为 anti-pivot complement-pair PDEC/cap。上一层 full-cell pair 仍作为 `H>=W=lcm_i(q_i)` 的长宽度出口前传。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从低纤维 singleton 或长宽度 pair，变成孤立 singleton、anti-pivot complement-pair、long full-cell pair，外加 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明孤立 singleton atom 全局可求和。",
            "- 本证书没有证明 anti-pivot complement-pair PDEC cap。",
            "- 本证书没有证明 long full-cell period-pair PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把低纤维 singleton 改写为孤立/anti-pivot 相位二分。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
