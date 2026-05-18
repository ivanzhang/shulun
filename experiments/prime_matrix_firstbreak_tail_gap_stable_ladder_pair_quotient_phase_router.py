#!/usr/bin/env python3
"""生成 stable ladder 剩余 pair 的 quotient-phase 统一证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_pair_quotient_phase_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-low-fiber-phase-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrAntiPivotComplementPairOrLongFullCellPairPDECCap"

IMPORT = "StableActualLadderIsolatedSingletonOrPairImportedLedger"
ISOLATED = "StableLadderIsolatedSingletonCarriedForwardLedger"
BASE = "StableLadderComplementBasePeriodLedger"
QUOTIENT = "StableLadderPairDifferenceQuotientNormalizationLedger"
PHASE_PERIOD = "StableLadderPivotPhaseQuotientPeriodLedger"
ANTI = "StableLadderAntiPivotPairNonzeroQuotientPhaseLedger"
FULL = "StableLadderFullCellPairZeroQuotientPhaseLedger"
WIDTH = "StableLadderPairQuotientWidthEnvelopeLedger"
RANGE = "StableLadderQuotientNoWrapOrFullPeriodDichotomyLedger"
NO_ANON = "NoAnonymousAntiPivotOrFullPairExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPairQuotientPhaseLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrPairQuotientPhaseCyclePDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {ISOLATED} AND {BASE} AND {QUOTIENT} AND {PHASE_PERIOD} "
    f"AND {ANTI} AND {FULL} AND {WIDTH} AND {RANGE} AND {NO_ANON} "
    f"AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的孤立/anti-pivot/full-cell 硬点替换成 quotient-phase 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 quotient-phase 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderIsolatedSingletonOrPairImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、anti-pivot complement pair、long full-cell pair 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderIsolatedSingletonCarriedForward",
            True,
            False,
            "孤立 singleton atom 作为单独求和/cap 出口前传；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderComplementBasePeriodClosed",
            True,
            True,
            "所有 pair 分支统一使用补坐标基周期 B=W_-j=lcm_{i!=j}(q_i)。",
            BASE,
        ),
        row(
            "StableLadderPairDifferenceQuotientNormalizationClosed",
            True,
            True,
            "pair 差值可唯一写成 n2-n1=tB，t>=1；full-cell pair 是 t 为 R 的倍数的子类。",
            QUOTIENT,
        ),
        row(
            "StableLadderPivotPhaseQuotientPeriodClosed",
            True,
            True,
            "令 g=gcd(q_j,B), R=q_j/g，则 pivot 相位只由 t mod R 决定。",
            PHASE_PERIOD,
        ),
        row(
            "StableLadderAntiPivotPairNonzeroQuotientPhaseClosed",
            True,
            True,
            "anti-pivot complement pair 等价于 t mod R 非零。",
            ANTI,
        ),
        row(
            "StableLadderFullCellPairZeroQuotientPhaseClosed",
            True,
            True,
            "full-cell pair 等价于 t mod R 为零，即 t=Ru。",
            FULL,
        ),
        row(
            "StableLadderPairQuotientWidthEnvelopeClosed",
            True,
            True,
            "承载支撑直径 H 给出 1<=t<=floor(H/B)。",
            WIDTH,
        ),
        row(
            "StableLadderQuotientNoWrapOrFullPeriodDichotomyClosed",
            True,
            False,
            "若 floor(H/B)<R，则 quotient 无完整 pivot 周期；若 >=R，则存在完整 quotient phase 周期块。",
            RANGE,
        ),
        row(
            "NoAnonymousAntiPivotOrFullPairExit",
            True,
            True,
            "anti-pivot 与 full-cell pair 被统一为 quotient phase 的非零/零相位出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPairQuotientPhase",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "IsolatedSingletonOrPairQuotientPhaseCycleStillOpen",
            False,
            False,
            "仍未证明孤立 singleton 可求和，也未排斥 quotient phase cycle PDEC/cap。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、quotient phase pair/cycle 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 pair quotient-phase 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "剩余 pair 出口可统一到补周期商变量。令 B=W_-j, d=n2-n1=tB。"
        "设 g=gcd(q_j,B), R=q_j/g，则 pivot 相位 d mod q_j 只由 t mod R 决定。"
        "anti-pivot complement pair 是非零 quotient 相位，full-cell pair 是零 quotient 相位 t=Ru。"
        "支撑直径 H 给出 t<=floor(H/B)，于是 pair 剩余变成明确的 quotient phase cycle PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_pair_quotient_phase_router",
        "status": "pair_branches_unified_as_quotient_phase_cycle_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "isolated_or_pair_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "isolated_singleton_carried_forward": True,
        "complement_base_period_closed": True,
        "pair_difference_quotient_normalized": True,
        "pivot_phase_quotient_period_closed": True,
        "anti_pivot_nonzero_quotient_phase_closed": True,
        "full_cell_zero_quotient_phase_closed": True,
        "pair_quotient_width_envelope_closed": True,
        "quotient_nowrap_or_period_dichotomy_closed": True,
        "anonymous_pair_branches_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "pair_quotient_phase_cycle_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "quotient_formulas": {
            "base_period": "B=W_-j=lcm_{i!=j}(q_i), empty lcm=1",
            "pair_difference": "d=n2-n1=tB, t in Z_{>=1}",
            "phase_period": "g=gcd(q_j,B), R=q_j/g",
            "pivot_phase": "d mod q_j is determined by t mod R",
            "anti_pivot_branch": "anti-pivot complement pair <=> t not congruent 0 mod R",
            "full_cell_branch": "full-cell pair <=> t congruent 0 mod R, equivalently t=R*u",
            "width_envelope": "1<=t<=floor(H/B)",
            "range_dichotomy": "floor(H/B)<R is no-wrap; floor(H/B)>=R contains a full quotient phase period",
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
        "# Prime Matrix stable-ladder pair quotient-phase 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"isolated_or_pair_imported={fmt_bool(cert['isolated_or_pair_imported'])}",
        f"isolated_singleton_carried_forward={fmt_bool(cert['isolated_singleton_carried_forward'])}",
        f"complement_base_period_closed={fmt_bool(cert['complement_base_period_closed'])}",
        f"pair_difference_quotient_normalized={fmt_bool(cert['pair_difference_quotient_normalized'])}",
        f"pivot_phase_quotient_period_closed={fmt_bool(cert['pivot_phase_quotient_period_closed'])}",
        f"anti_pivot_nonzero_quotient_phase_closed={fmt_bool(cert['anti_pivot_nonzero_quotient_phase_closed'])}",
        f"full_cell_zero_quotient_phase_closed={fmt_bool(cert['full_cell_zero_quotient_phase_closed'])}",
        f"pair_quotient_width_envelope_closed={fmt_bool(cert['pair_quotient_width_envelope_closed'])}",
        f"quotient_nowrap_or_period_dichotomy_closed={fmt_bool(cert['quotient_nowrap_or_period_dichotomy_closed'])}",
        f"anonymous_pair_branches_removed={fmt_bool(cert['anonymous_pair_branches_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"pair_quotient_phase_cycle_pdec_cap_proved={fmt_bool(cert['pair_quotient_phase_cycle_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 补周期商变量",
        "",
        "对 anti-pivot complement pair 和 long full-cell pair 统一取补坐标基周期：",
        "",
        "```text",
        "B=W_-j=lcm_{i!=j}(q_i), empty lcm=1.",
        "```",
        "",
        "任一 pair 差值写成：",
        "",
        "```text",
        "d=n2-n1=tB, t>=1.",
        "```",
        "",
        "## 2. pivot 相位周期",
        "",
        "设：",
        "",
        "```text",
        "g=gcd(q_j,B), R=q_j/g.",
        "```",
        "",
        "则 `d mod q_j` 只由 `t mod R` 决定。于是：",
        "",
        "```text",
        "anti-pivot complement pair <=> t not congruent 0 mod R,",
        "full-cell pair <=> t congruent 0 mod R.",
        "```",
        "",
        "特别地，上一层 `q_j|W_-j` 的情形就是 `R=1`，非零 quotient 相位不存在。",
        "",
        "## 3. quotient 宽度包络",
        "",
        "承载支撑直径 `H` 给出：",
        "",
        "```text",
        "1<=t<=floor(H/B).",
        "```",
        "",
        "若 `floor(H/B)<R`，则 quotient 相位没有完成一个 pivot 周期；若 `floor(H/B)>=R`，则 quotient 区间已经包含完整相位周期块。该周期块是新的显式 PDEC/cap 输入。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从孤立 singleton、anti-pivot complement-pair、long full-cell pair，变成孤立 singleton 或统一的 quotient phase cycle PDEC/cap，外加 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 quotient phase cycle PDEC/cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 anti-pivot/full-cell pair 统一到补周期商变量与 pivot 相位周期。",
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
