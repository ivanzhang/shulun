#!/usr/bin/env python3
"""生成 strict primitive 核表三腿回流同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_kernel_table_three_leg_return_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-kernel-table-three-leg-return-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-kernel-table-three-leg-return-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-kernel-table-three-leg-return-sync-router.md"

KERNEL = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"
POINTWISE_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
NONRECURSIVE_TABLE = "NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn"
ALPHA_FORMULA = "AlphaRowAnchorPhaseEmissionFormulaLedger"
WEIGHT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
PDEC_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
PDEC_KLS_PACKET = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
KZ_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"

SOURCE_FILES = [
    "prime-matrix-strict-post-mertens-nonrecursive-frontier-sync-router.json",
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
    "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json",
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-strict-self-contained-cycle-obstruction-router.json",
    "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json",
    "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记引用证据哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """把核恒等式三条下游腿同步到最新真实前沿。"""
    post = load_json("prime-matrix-strict-post-mertens-nonrecursive-frontier-sync-router.json")
    kernel = load_json("prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json")
    pointwise = load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json")
    alpha = load_json("prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json")
    weight = load_json("prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json")
    identity = load_json("prime-matrix-strict-independent-identity-statement-taxonomy-router.json")
    uv_rank = load_json("prime-matrix-strict-exact-uv-map-rank-incidence-router.json")
    fixed_pair = load_json("prime-matrix-strict-fixed-pair-fiber-bound-router.json")
    key = load_json("prime-matrix-strict-complete-emitter-key-partition-router.json")
    source_table = load_json("prime-matrix-strict-actual-emitter-source-table-router.json")
    cycle = load_json("prime-matrix-strict-self-contained-cycle-obstruction-router.json")
    pdec_split = load_json("prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json")
    dstructure = load_json("prime-matrix-dstructure-rankin-promotion-acceptance-router.json")

    post_to_kernel = (
        post.get("next_direct_attack_target") == KERNEL
        and post.get("post_mertens_nonrecursive_frontier_sync_closed") is True
    )
    kernel_to_pointwise = (
        kernel.get("next_direct_attack_target") == POINTWISE_TABLE
        and kernel.get("kernel_identity_attack_router_closed") is True
    )
    pointwise_to_three = (
        pointwise.get("pointwise_kernel_table_router_closed") is True
        and pointwise.get("next_direct_attack_target") == ALPHA_FORMULA
        and WEIGHT_IDENTITY in pointwise.get("parallel_required_inputs", [])
        and RANK_CERT in pointwise.get("parallel_required_inputs", [])
    )
    alpha_leg_returns = (
        alpha.get("alpha_row_formula_local_frontier_synced_to_terminal") is True
        and alpha.get("next_direct_attack_target") == PDEC_KLS
    )
    weight_leg_returns = (
        weight.get("downstream_sync_router_closed") is True
        and weight.get("next_direct_attack_target") == PDEC_KLS
        and identity.get("terminal_gap_after_router")
        == "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
    )
    rank_leg_needs_same_table = (
        uv_rank.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False
        and fixed_pair.get("fixed_pair_fiber_bound_router_closed") is True
        and key.get("complete_emitter_key_partition_router_closed") is True
        and source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False
    )
    internal_fixed_point = (
        cycle.get("current_internal_route_is_fixed_point") is True
        and cycle.get("cycle_returns_to_pdec_clean_kls_terminal_gate") is True
    )
    direct_terminal_open = (
        pdec_split.get("terminal_split_router_closed") is True
        and pdec_split.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    dstructure_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )

    sync_closed = all(
        [
            post_to_kernel,
            kernel_to_pointwise,
            pointwise_to_three,
            alpha_leg_returns,
            weight_leg_returns,
            rank_leg_needs_same_table,
            internal_fixed_point,
            direct_terminal_open,
            dstructure_open,
        ]
    )

    rows = [
        row(
            "PostMertensFrontierImported",
            post_to_kernel,
            False,
            "最新 post-Mertens 前沿把主攻点钉为同 formal-unit 核恒等式。",
            KERNEL,
        ),
        row(
            "KernelIdentityReducedToPointwiseTable",
            kernel_to_pointwise,
            False,
            "核恒等式不能由记录守恒或几何 Phi 自动推出；必须先提交逐点 primitive 核表。",
            POINTWISE_TABLE,
        ),
        row(
            "PointwiseTableSplitIntoThreeLegs",
            pointwise_to_three,
            False,
            "逐点核表被拆成 alpha row 发射公式、独立权重恒等式、同表 rank/multiplicity 证书。",
            f"{ALPHA_FORMULA} AND {WEIGHT_IDENTITY} AND {RANK_CERT}",
        ),
        row(
            "AlphaFormulaLegReturnsToTerminal",
            alpha_leg_returns,
            False,
            "alpha row 局部 unsigned 骨架、signed-lift 和 anchor 回流都已同步到 PDEC/CleanKLS 终端门。",
            PDEC_KLS,
        ),
        row(
            "WeightIdentityLegReturnsToTerminal",
            weight_leg_returns,
            False,
            "signed 权重律经独立恒等式分类、moving-block/NC-BLK 回到同一终端门。",
            PDEC_KLS,
        ),
        row(
            "RankMultiplicityLegNeedsSamePrimitiveTable",
            rank_leg_needs_same_table,
            False,
            "rank/multiplicity 分支需要 source table、complete key 与 fixed-pair fiber；这些又要求同一 primitive rows。",
            POINTWISE_TABLE,
        ),
        row(
            "ThreeLegSeparateAttackIsFixedPoint",
            internal_fixed_point,
            True,
            "三腿逐项攻击只会在 source table、alpha signed lift、PDEC/CleanKLS 之间循环。",
            NONRECURSIVE_TABLE,
        ),
        row(
            "NonrecursivePointwiseTableCurrentCorpusProved",
            False,
            False,
            "当前语料没有一次性正向构造逐 primitive row 的 source tuple、signed weight、Phi atom、exact-UV rank 证书。",
            NONRECURSIVE_TABLE,
        ),
        row(
            "DirectTerminalParallelArmsStillOpen",
            direct_terminal_open,
            False,
            "并行终端路线仍可攻，但 PDEC 作用域匹配与自足 KZ/DLS 都未证明。",
            f"{SCOPE_MATCH} OR {KZ_DLS}",
        ),
        row(
            "RatePreservationStillOpen",
            False,
            False,
            "moving-atom packet 的 log-power 速率保持仍未证明。",
            RATE,
        ),
        row(
            "DStructureGateStillOpen",
            dstructure_open,
            False,
            "DStructure/Tail-log4/finite Rankin 边界已命名但未独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "当前只证明三腿回流和最窄非递归表目标；尚未推出早期零行反例矛盾。",
            f"{NONRECURSIVE_TABLE} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]

    strict_active_basis = f"{NONRECURSIVE_TABLE} AND {RATE} AND {DSTRUCTURE}"
    parallel_terminal_basis = (
        f"({SCOPE_MATCH} OR {KZ_DLS}) AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_strict_kernel_table_three_leg_return_sync_router",
        "status": "kernel_table_three_leg_return_synced_nonrecursive_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "kernel_table_three_leg_return_sync_closed": sync_closed,
        "post_mertens_frontier_imported": post_to_kernel,
        "kernel_identity_reduced_to_pointwise_table": kernel_to_pointwise,
        "pointwise_table_split_into_three_legs": pointwise_to_three,
        "alpha_formula_leg_returns_to_terminal": alpha_leg_returns,
        "weight_identity_leg_returns_to_terminal": weight_leg_returns,
        "rank_multiplicity_leg_needs_same_primitive_table": rank_leg_needs_same_table,
        "three_leg_separate_attack_is_fixed_point": internal_fixed_point,
        "nonrecursive_pointwise_table_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "strict_active_basis_after_sync": strict_active_basis,
        "parallel_direct_terminal_basis": parallel_terminal_basis,
        "next_direct_attack_target": NONRECURSIVE_TABLE,
        "parallel_attack_targets": [SCOPE_MATCH, KZ_DLS, RATE, DSTRUCTURE],
        "nonrecursive_table_contract": (
            "必须在同一 formal unit、Cauchy/dispersion/terminal extraction 之前一次性列出 primitive rows："
            "source tuple、anchor/phase、signed weight、exact `(u,v)`、Phi atom、local factor 非零、"
            "rank/multiplicity 证书和命名回流。不能分别从 alpha 局部公式、权重律或 rank 支路后验拼装。"
        ),
        "if_not_supplied": (
            "若该非递归逐点表不给出，alpha、weight、rank 三腿分攻都会回到 PDEC/CleanKLS 固定点，"
            "不能闭合行/列命题。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "继续下钻核恒等式后，真正障碍变得更窄：逐点 primitive 核表的三条自然分支不能分开闭合。"
            "alpha row 公式与 signed 权重律都已回到 PDEC/CleanKLS 终端门；rank/multiplicity 分支又要求"
            "同一张 primitive source table。三腿分攻形成固定点。因此当前唯一非递归自足主攻点是"
            "`NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn`；"
            "它未被当前语料证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict primitive 核表三腿回流同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"kernel_table_three_leg_return_sync_closed={fmt_bool(result['kernel_table_three_leg_return_sync_closed'])}",
        f"alpha_formula_leg_returns_to_terminal={fmt_bool(result['alpha_formula_leg_returns_to_terminal'])}",
        f"weight_identity_leg_returns_to_terminal={fmt_bool(result['weight_identity_leg_returns_to_terminal'])}",
        f"rank_multiplicity_leg_needs_same_primitive_table={fmt_bool(result['rank_multiplicity_leg_needs_same_primitive_table'])}",
        f"three_leg_separate_attack_is_fixed_point={fmt_bool(result['three_leg_separate_attack_is_fixed_point'])}",
        f"nonrecursive_pointwise_table_proved={fmt_bool(result['nonrecursive_pointwise_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步后严格基",
        "",
        "```text",
        result["strict_active_basis_after_sync"],
        "```",
        "",
        "并行直接终端基：",
        "",
        "```text",
        result["parallel_direct_terminal_basis"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 非递归表合同",
            "",
            result["nonrecursive_table_contract"],
            "",
            result["if_not_supplied"],
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
