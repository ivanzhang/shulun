#!/usr/bin/env python3
"""生成 stable ladder quotient phase 的 short-arc/mean 分解证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_phase_arc_mean_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-pair-quotient-phase-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrPairQuotientPhaseCyclePDECCap"

IMPORT = "StableActualLadderQuotientPhaseCycleImportedLedger"
ISOLATED = "StableLadderIsolatedSingletonCarriedForwardAfterArcMeanLedger"
SPAN = "StableLadderQuotientSpanParameterLedger"
NOWRAP = "StableLadderQuotientNoWrapZeroPhaseExclusionLedger"
SHORT_ARC = "StableLadderQuotientShortArcClusterLedger"
PERIOD_DIV = "StableLadderFullCycleEuclideanDecompositionLedger"
MEAN = "StableLadderFullCycleFormalPhaseMeanLedger"
TAIL = "StableLadderFullCycleResidualTailArcLedger"
NO_ANON = "NoAnonymousQuotientPhaseCycleExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterArcMeanLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientShortArcClusterOrPhaseCycleMeanPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {ISOLATED} AND {SPAN} AND {NOWRAP} AND {SHORT_ARC} "
    f"AND {PERIOD_DIV} AND {MEAN} AND {TAIL} AND {NO_ANON} "
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
    """把旧活动基中的 quotient-cycle 硬点替换成 short-arc/mean 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 short-arc/mean 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderQuotientPhaseCycleImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、quotient phase cycle cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderIsolatedSingletonCarriedForwardAfterArcMean",
            True,
            False,
            "孤立 singleton atom 继续作为单独 summability/cap 出口；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderQuotientSpanParameterClosed",
            True,
            True,
            "令 T=floor(H/B)，pair quotient 参数满足 1<=t<=T。",
            SPAN,
        ),
        row(
            "StableLadderQuotientNoWrapZeroPhaseExclusionClosed",
            True,
            True,
            "若 T<R，则 t in [1,T] 没有零相位；full-cell 分支在 no-wrap 区间内不可能。",
            NOWRAP,
        ),
        row(
            "StableLadderQuotientShortArcClusterRegistered",
            True,
            False,
            "no-wrap pair 只能表现为 Z/RZ 中真短弧 A_T={1,...,T} 上的实际双点聚集。",
            SHORT_ARC,
        ),
        row(
            "StableLadderFullCycleEuclideanDecompositionClosed",
            True,
            True,
            "若 T>=R，则 T=aR+s, a>=1, 0<=s<R，把 quotient 区间拆成 a 个完整周期与一个尾弧。",
            PERIOD_DIV,
        ),
        row(
            "StableLadderFullCycleFormalPhaseMeanClosed",
            True,
            True,
            "完整周期的 formal quotient 参数对每个 pivot 相位给出同样次数 a；任何 actual 偏差必须另行显化。",
            MEAN,
        ),
        row(
            "StableLadderFullCycleResidualTailArcClosed",
            True,
            True,
            "剩余 s 个参数仍是 no-wrap 尾弧，回到 short-arc cluster 口径。",
            TAIL,
        ),
        row(
            "NoAnonymousQuotientPhaseCycleExit",
            True,
            True,
            "quotient cycle 不再是匿名出口：它被拆成 no-wrap 短弧聚集或完整周期均值偏差。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterArcMean",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "ShortArcOrPhaseMeanCapStillOpen",
            False,
            False,
            "仍未证明短弧聚集 cap、完整周期 actual-mean cap，也未证明孤立 singleton 或 sparse SAE 可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、short-arc cluster、phase-cycle mean cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 short-arc/mean 分解证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "quotient phase cycle 可继续非循环化。令 T=floor(H/B)。"
        "若 T<R，则 t=1..T 在 Z/RZ 中是真短弧，且零相位不存在；"
        "pair 分支只能成为 short-arc cluster。若 T>=R，则 T=aR+s，"
        "完整周期给出 formal phase mean，尾段 s<R 回到短弧。"
        "因此剩余不是匿名周期，而是 short-arc cluster 或 phase-cycle actual-mean cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_phase_arc_mean_router",
        "status": "quotient_cycle_split_to_short_arc_or_full_mean_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "quotient_phase_cycle_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "isolated_singleton_carried_forward": True,
        "quotient_span_parameter_closed": True,
        "nowrap_zero_phase_exclusion_closed": True,
        "short_arc_cluster_registered": True,
        "full_cycle_euclidean_decomposition_closed": True,
        "full_cycle_formal_phase_mean_closed": True,
        "full_cycle_residual_tail_arc_closed": True,
        "anonymous_quotient_cycle_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "quotient_short_arc_cluster_cap_proved": False,
        "phase_cycle_actual_mean_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "quotient_formulas": {
            "span": "T=floor(H/B), 1<=t<=T",
            "nowrap": "T<R => {1,...,T} is a proper arc in Z/RZ and contains no zero phase",
            "full_cycle": "T>=R => T=aR+s, a=floor(T/R)>=1, 0<=s<R",
            "formal_mean": "each complete block of length R contains every pivot phase once",
            "tail_arc": "the residual s parameters form a proper no-wrap arc",
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
        "# Prime Matrix stable-ladder quotient short-arc/mean 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"quotient_phase_cycle_imported={fmt_bool(cert['quotient_phase_cycle_imported'])}",
        f"isolated_singleton_carried_forward={fmt_bool(cert['isolated_singleton_carried_forward'])}",
        f"quotient_span_parameter_closed={fmt_bool(cert['quotient_span_parameter_closed'])}",
        f"nowrap_zero_phase_exclusion_closed={fmt_bool(cert['nowrap_zero_phase_exclusion_closed'])}",
        f"short_arc_cluster_registered={fmt_bool(cert['short_arc_cluster_registered'])}",
        f"full_cycle_euclidean_decomposition_closed={fmt_bool(cert['full_cycle_euclidean_decomposition_closed'])}",
        f"full_cycle_formal_phase_mean_closed={fmt_bool(cert['full_cycle_formal_phase_mean_closed'])}",
        f"full_cycle_residual_tail_arc_closed={fmt_bool(cert['full_cycle_residual_tail_arc_closed'])}",
        f"anonymous_quotient_cycle_removed={fmt_bool(cert['anonymous_quotient_cycle_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"quotient_short_arc_cluster_cap_proved={fmt_bool(cert['quotient_short_arc_cluster_cap_proved'])}",
        f"phase_cycle_actual_mean_cap_proved={fmt_bool(cert['phase_cycle_actual_mean_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. quotient span",
        "",
        "沿用上一层记号：",
        "",
        "```text",
        "B=W_-j, g=gcd(q_j,B), R=q_j/g, d=n2-n1=tB.",
        "```",
        "",
        "支撑直径 `H` 给出：",
        "",
        "```text",
        "T=floor(H/B), 1<=t<=T.",
        "```",
        "",
        "## 2. no-wrap 真短弧",
        "",
        "若 `T<R`，则 `t=1,...,T` 在 `Z/RZ` 中是一段不绕回的真短弧，并且不含零相位：",
        "",
        "```text",
        "t not congruent 0 mod R for every 1<=t<=T<R.",
        "```",
        "",
        "因此 full-cell pair 在 no-wrap 分支中被排斥；实际 pair 只能登记为 quotient short-arc cluster。",
        "",
        "## 3. 完整周期均值",
        "",
        "若 `T>=R`，写：",
        "",
        "```text",
        "T=aR+s, a=floor(T/R)>=1, 0<=s<R.",
        "```",
        "",
        "每个长度为 `R` 的完整块在 formal quotient 参数中恰好覆盖每个 pivot 相位一次；`a` 个完整块给出相同相位均值 `a`。剩余 `s` 个参数仍是 no-wrap 尾弧。",
        "",
        "这一步不把 formal 均值当成 actual load 证明；它只说明任何持久 actual 偏差必须落入 phase-cycle actual-mean cap，尾段则回到 short-arc cluster。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 quotient phase cycle 黑箱变成孤立 singleton、quotient short-arc cluster、phase-cycle actual-mean cap，外加 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 quotient short-arc cluster cap。",
            "- 本证书没有证明 phase-cycle actual-mean cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 quotient phase cycle 拆成 no-wrap 短弧与完整周期均值/尾弧分解。",
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
