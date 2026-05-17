#!/usr/bin/env python3
"""把 1/P 级 beta-gap 风险压成 Page 稀疏单载体或非实零包出口。

用法示例：
  python3 experiments/prime_matrix_beta_gap_page_sparsity_router.py
  python3 experiments/prime_matrix_beta_gap_page_sparsity_router.py --page-c 0.05
  python3 -m json.tool docs/monograph/prime-matrix-beta-gap-page-sparsity-router.json

输出：
  data/prime-matrix-beta-gap-page-sparsity-ledger.json
  docs/monograph/prime-matrix-beta-gap-page-sparsity-router.json
  docs/monograph/prime-matrix-beta-gap-page-sparsity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

OUT_LEDGER = DATA / "prime-matrix-beta-gap-page-sparsity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-beta-gap-page-sparsity-router.json"
OUT_MD = DOCS / "prime-matrix-beta-gap-page-sparsity-router.md"

PREVIOUS = "prime-matrix-large-splitting-beta-gap-router.json"
STATUS_TABLE = "claim-status-table.md"
ACTUAL_LOAD_CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
CRITICAL_LOAD_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

PREVIOUS_TARGET = "SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2"
NEXT_TARGET = "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget"
PDEC_TARGET = "MovingPageSingletonCarrierPDECOrCoherentZeroPacket"
PAGE_INPUT = "LandauPageExceptionalZeroUniquenessWithAdaptedConstants"
SELF_CONTAINED_BETA = "SelfContainedEffectivePrimeModulusQuadraticBetaGapAtScaleOneOverP"
ZERO_PACKET = "NonrealZeroPacketResidualBelowLargeSplittingSlackAtP2"
PAGE_SINGLETON = "PageExceptionalSingletonCarrierExclusionOrMovingFamilyPDEC"

CHEBYSHEV_LOWER_ATOM = "ChebyshevPrincipalMassLowerBoundAtP2"
QUADRATIC_MARGIN_TARGET = "QuadraticHalfClassSquareScaleBiasMarginTheorem"
EFFECTIVE_NO_SIEGEL = "EffectivePrimeModulusNoSiegelZeroOrBetaGapAtSquareScale"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / PREVIOUS,
    DOCS / STATUS_TABLE,
    ACTUAL_LOAD_CONTRACTS,
    CRITICAL_LOAD_FRONTIER,
    EXTERNAL_INDEX,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_X,
    PAPER,
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result: dict[str, str] = {}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def previous_critical_constant(previous: dict[str, Any]) -> float | None:
    """从上一证书提取 P(1-beta) 临界常数。"""
    diagnostic = previous.get("finite_diagnostic", {})
    value = diagnostic.get("max_critical_beta_gap_times_P_for_P_ge_101")
    return float(value) if value is not None else None


def page_symbolic_diagnostic(previous: dict[str, Any], page_c: float) -> dict[str, Any]:
    """生成 Page 稀疏公式诊断。

    page_c 是 Page 零点唯一性区域中的符号常数示例，只用于量纲展示；
    本证书不把该数值作为已认证常数。
    """
    ccrit = previous_critical_constant(previous)
    if ccrit is None:
        fringe_multiplier = None
    else:
        fringe_multiplier = ccrit / page_c
    return {
        "page_constant_for_display_only": page_c,
        "imported_max_P_times_beta_gap_crit_for_P_ge_101": ccrit,
        "page_region": "beta > 1 - c_Page/log Q",
        "ultra_close_region": "beta > 1 - C(P)/P",
        "implication_condition": "P > C(P) log Q / c_Page",
        "fringe_bound_formula": "P <= (C_*/c_Page) log Q",
        "display_fringe_multiplier_Cstar_over_cPage": fringe_multiplier,
        "page_sparsity_bound_formula": "|E(Q)∩((C_*/c_Page)logQ,Q]| <= 1",
        "density_consequence_formula": "|E(Q)|/pi(Q) <= (1+pi((C_*/c_Page)logQ))/pi(Q)=o(1)",
        "finite_diagnostic_is_proof": False,
    }


def formula_ledger() -> list[dict[str, str]]:
    """记录本步公式。"""
    return [
        {
            "item": "ultra-close beta failure",
            "formula": "beta_P > 1 - C(P)/P, with C(P)=O(1) from the large-splitting budget",
        },
        {
            "item": "Page zero-free uniqueness region",
            "formula": "for primitive characters with conductor q<=Q, at most one real character has a zero beta>1-c_Page/log Q",
        },
        {
            "item": "region inclusion",
            "formula": "if P<=Q and P>C(P)logQ/c_Page, then 1-C(P)/P > 1-c_Page/logQ",
        },
        {
            "item": "sparsity consequence",
            "formula": "|E(Q)∩((C_*/c_Page)logQ,Q]|<=1, assuming C(P)<=C_* and Page uniqueness",
        },
        {
            "item": "CRT family exclusion",
            "formula": "a positive-density or fixed-period CRT family of ultra-close real-zero carriers is impossible under Page uniqueness",
        },
        {
            "item": "remaining shape",
            "formula": "only a moving singleton Page carrier, a nonreal zero packet, or an endpoint/finite residual can remain",
        },
    ]


def branch_ledger() -> list[dict[str, str]]:
    """记录本轮分支压缩。"""
    return [
        {
            "branch": PREVIOUS_TARGET,
            "route": NEXT_TARGET,
            "status": "sparsity reduction",
            "meaning": "1/P 级 beta-gap 风险被拆成 Page 稀疏实零载体和非实零残差预算。",
        },
        {
            "branch": "ultra-close real zero family",
            "route": PAGE_INPUT,
            "status": "external standard input, constants not internalized",
            "meaning": "Page/Landau 唯一例外定理可排除多载体周期族，但本仓库尚未适配常数。",
        },
        {
            "branch": "periodic CRT reproduction",
            "route": "excluded under Page uniqueness",
            "status": "conditional route closed",
            "meaning": "固定周期或正密度的反例载体族会在同一 Q 范围内给出多个例外零，违背 Page 唯一性。",
        },
        {
            "branch": "moving singleton carrier",
            "route": PAGE_SINGLETON,
            "status": "open",
            "meaning": "每个尺度最多一个的移动例外不能由稀疏性自动删除，需要 PDEC/有限核或另一条算术排斥。",
        },
        {
            "branch": "nonreal/endpoint residual",
            "route": ZERO_PACKET,
            "status": "open",
            "meaning": "Page 稀疏只处理实零载体，不控制非实零包同向相干。",
        },
    ]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "BetaGapBudgetImported",
            imported,
            imported,
            "上一层已把大分裂失败压成 1/P 级 beta-gap 与零包预算。",
            PREVIOUS_TARGET,
        ),
        row(
            "PageRegionInclusionAlgebraClosed",
            True,
            True,
            "beta>1-C/P 在 P>C logQ/c_Page 时落入 Page 唯一性区域。",
            "none",
        ),
        row(
            "PeriodicCRTCarrierFamilyExcludedConditionally",
            True,
            False,
            "若接受 Page 唯一例外定理与常数适配，则正密度/固定周期载体族不可能。",
            PAGE_INPUT,
        ),
        row(
            "MovingSingletonCarrierExcluded",
            False,
            False,
            "Page 稀疏性仍允许每个尺度一个移动例外载体。",
            PAGE_SINGLETON,
        ),
        row(
            "NonrealZeroPacketResidualProved",
            False,
            False,
            "非实零包/端点残差预算仍未自足证明。",
            ZERO_PACKET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只排除多载体 CRT 复现形态，不证明行/列命题。",
            "global final inputs remain open",
        ),
    ]


def build_result(page_c: float) -> dict[str, Any]:
    """构造证书对象。"""
    previous = load_json(DOCS / PREVIOUS)
    rows = build_rows(previous)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR "
        f"(({CHEBYSHEV_LOWER_ATOM} AND ({QUADRATIC_MARGIN_TARGET} OR {EFFECTIVE_NO_SIEGEL} "
        f"OR (({PAGE_INPUT} AND {PAGE_SINGLETON}) AND {ZERO_PACKET}) "
        f"OR ({SELF_CONTAINED_BETA} AND {ZERO_PACKET}) OR {PDEC_TARGET})))) AND "
        f"{EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    diagnostic = page_symbolic_diagnostic(previous, page_c)
    return {
        "certificate_type": "prime_matrix_beta_gap_page_sparsity_router",
        "status": "beta_gap_budget_routed_to_page_sparsity_singleton_or_zero_packet_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "previous_target": PREVIOUS_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "pdec_fallback_target": PDEC_TARGET,
        "page_uniqueness_input": PAGE_INPUT,
        "moving_singleton_target": PAGE_SINGLETON,
        "zero_packet_residual_target": ZERO_PACKET,
        "formula_ledger": formula_ledger(),
        "branch_ledger": branch_ledger(),
        "symbolic_diagnostic": diagnostic,
        "page_region_inclusion_algebra_closed": True,
        "page_uniqueness_constants_internalized": False,
        "moving_singleton_carrier_excluded": False,
        "nonreal_zero_packet_residual_proved": False,
        "row_column_unconditional_closed": False,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `SquareScaleQuadraticBetaGapAndZeroPacketResidualBudgetAtP2`。"
            "若实零分支导致失败，则上一层已把它压到 `beta>1-C(P)/P`。"
            "Page/Landau 唯一例外零定理的区域为 `beta>1-c_Page/log Q`。"
            "当 `P>C(P)logQ/c_Page` 且 `P<=Q` 时，超近实零载体落入 Page 区域，"
            "所以任意 `q<=Q` 范围中至多一个这样的实零载体。"
            "这排除了固定周期或正密度 CRT 反例族复现；剩余只可能是每个尺度一个的 moving singleton、"
            "非实零包相干或端点残差。本步没有完成无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    diagnostic = result["symbolic_diagnostic"]
    lines = [
        "# Prime Matrix Beta-gap Page Sparsity Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"page_region_inclusion_algebra_closed={fmt_bool(result['page_region_inclusion_algebra_closed'])}",
        f"page_uniqueness_constants_internalized={fmt_bool(result['page_uniqueness_constants_internalized'])}",
        f"moving_singleton_carrier_excluded={fmt_bool(result['moving_singleton_carrier_excluded'])}",
        f"nonreal_zero_packet_residual_proved={fmt_bool(result['nonreal_zero_packet_residual_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"pdec_fallback_target={result['pdec_fallback_target']}",
        "```",
        "",
        "## 1. 公式账本",
        "",
        "| item | formula |",
        "| --- | --- |",
    ]
    for item in result["formula_ledger"]:
        lines.append(f"| `{table_cell(item['item'])}` | `{table_cell(item['formula'])}` |")

    lines += [
        "",
        "## 2. 分支压缩",
        "",
        "| branch | route | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["branch_ledger"]:
        lines.append(
            f"| `{table_cell(item['branch'])}` | {table_cell(item['route'])} | "
            f"{table_cell(item['status'])} | {table_cell(item['meaning'])} |"
        )

    lines += [
        "",
        "## 3. 符号诊断",
        "",
        "这里的 `c_Page` 只作 Page 区域常数量纲展示；本证书没有内化 Page 定理常数。",
        "",
        "```text",
        f"page_constant_for_display_only={diagnostic['page_constant_for_display_only']}",
        f"imported_max_P_times_beta_gap_crit_for_P_ge_101={diagnostic['imported_max_P_times_beta_gap_crit_for_P_ge_101']}",
        f"page_region={diagnostic['page_region']}",
        f"ultra_close_region={diagnostic['ultra_close_region']}",
        f"implication_condition={diagnostic['implication_condition']}",
        f"fringe_bound_formula={diagnostic['fringe_bound_formula']}",
        f"display_fringe_multiplier_Cstar_over_cPage={diagnostic['display_fringe_multiplier_Cstar_over_cPage']}",
        f"page_sparsity_bound_formula={diagnostic['page_sparsity_bound_formula']}",
        f"density_consequence_formula={diagnostic['density_consequence_formula']}",
        "```",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | "
            f"{table_cell(item['remaining'])} |"
        )

    lines += [
        "",
        "## 5. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件没有证明 Page 定理常数、有效无 Siegel 零点、非实零包抵消或行/列命题；它只把超近实零族的 CRT 周期复现压成 Page 稀疏单载体出口。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--page-c",
        type=float,
        default=0.05,
        help="Page 区域 beta>1-c_Page/logQ 的展示常数；不作为已认证常数",
    )
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.page_c)
    write_outputs(result)
    summary = {
        "status": result["status"],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "pdec_fallback_target": result["pdec_fallback_target"],
        "page_region_inclusion_algebra_closed": result["page_region_inclusion_algebra_closed"],
        "page_uniqueness_constants_internalized": result["page_uniqueness_constants_internalized"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
