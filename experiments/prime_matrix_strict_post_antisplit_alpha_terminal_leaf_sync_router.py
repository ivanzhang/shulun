#!/usr/bin/env python3
"""生成 post-antisplit alpha 到终端叶子的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_antisplit_alpha_terminal_leaf_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json

输出：
  data/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json
  docs/monograph/prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.md"

POST_ANTISPLIT = DOCS / "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"
KERNEL_THREE_LEG = DOCS / "prime-matrix-strict-kernel-table-three-leg-return-sync-router.json"
NONRECURSIVE_FIELD = DOCS / "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json"
NONRECURSIVE_TO_LEAF = DOCS / "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json"
ALPHA_TERMINAL = DOCS / "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json"
WEIGHT_DOWNSTREAM = DOCS / "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"
TERMINAL_LEAF = DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"
NONCANONICAL_LEGAL = DOCS / "prime-matrix-strict-noncanonical-legal-closure-mode-router.json"
UV_RANK = DOCS / "prime-matrix-strict-exact-uv-map-rank-incidence-router.json"
DSTRUCTURE_ACCEPTANCE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"

POINTWISE_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
WEIGHT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
NONRECURSIVE_TABLE = "NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn"
JOINT_CONSTRUCTOR = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
NONCANONICAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
PDEC_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；文件缺失不能被解释成证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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


def source_hashes() -> dict[str, str]:
    """登记吸收的前沿证据哈希。"""
    paths = [
        Path(__file__).resolve(),
        POST_ANTISPLIT,
        KERNEL_THREE_LEG,
        NONRECURSIVE_FIELD,
        NONRECURSIVE_TO_LEAF,
        ALPHA_TERMINAL,
        WEIGHT_DOWNSTREAM,
        TERMINAL_LEAF,
        NONCANONICAL_LEGAL,
        UV_RANK,
        DSTRUCTURE_ACCEPTANCE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_edges() -> list[dict[str, str]]:
    """列出本次同步的主链。"""
    return [
        {
            "from": "post-antisplit source-rank convergence",
            "to": POINTWISE_TABLE,
            "meaning": "post-antisplit 后的 source-rank/no-collapse 路线已汇合到逐 primitive alpha/delta 核表。",
        },
        {
            "from": POINTWISE_TABLE,
            "to": f"{ALPHA_ROW} AND {WEIGHT_IDENTITY} AND {RANK_CERT}",
            "meaning": "逐点核表分成 alpha 发射、权重恒等式和同表 rank/multiplicity 三腿。",
        },
        {
            "from": f"{ALPHA_ROW} / {WEIGHT_IDENTITY}",
            "to": PDEC_KLS,
            "meaning": "alpha 腿和权重恒等式腿单独下钻都会回到 PDEC/CleanKLS 终端门。",
        },
        {
            "from": RANK_CERT,
            "to": POINTWISE_TABLE,
            "meaning": "rank/multiplicity 腿要求同一张 primitive source table，不能独立闭合。",
        },
        {
            "from": f"{ALPHA_ROW} AND {WEIGHT_IDENTITY} AND {RANK_CERT}",
            "to": NONRECURSIVE_TABLE,
            "meaning": "三腿分攻是固定点；必须一次性正向构造非递归逐点表。",
        },
        {
            "from": NONRECURSIVE_TABLE,
            "to": JOINT_CONSTRUCTOR,
            "meaning": "非递归逐点表的第一生产性字段是显式 joint alpha/delta constructor rule。",
        },
        {
            "from": JOINT_CONSTRUCTOR,
            "to": "signed-source fixed point -> terminal leaf firewall",
            "meaning": "若没有新公式工件，joint constructor 旧展开回到 signed-source 固定点，再进入终端叶子。",
        },
        {
            "from": "terminal leaf firewall",
            "to": f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
            "meaning": "当前已物化 PDEC/sparse 前沿清零后，活动终端叶子剩 canonical-lock 或 noncanonical legal mode。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总各证书读数。"""
    post = data["post"]
    three = data["three"]
    field = data["field"]
    leaf_sync = data["leaf_sync"]
    alpha = data["alpha"]
    weight = data["weight"]
    leaf = data["leaf"]
    legal = data["legal"]
    uv = data["uv"]
    dstructure = data["dstructure"]

    post_to_pointwise = (
        post.get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True
        and post.get("next_direct_attack_target") == ALPHA_ROW
    )
    three_leg_fixed = (
        three.get("kernel_table_three_leg_return_sync_closed") is True
        and three.get("three_leg_separate_attack_is_fixed_point") is True
        and three.get("next_direct_attack_target") == NONRECURSIVE_TABLE
    )
    alpha_returns = (
        alpha.get("alpha_row_formula_local_frontier_synced_to_terminal") is True
        and alpha.get("next_direct_attack_target") == PDEC_KLS
    )
    weight_returns = (
        weight.get("downstream_sync_router_closed") is True
        and weight.get("next_direct_attack_target") == PDEC_KLS
    )
    field_contract = (
        field.get("field_contract_boundary_closed") is True
        and field.get("next_direct_attack_target") == JOINT_CONSTRUCTOR
    )
    nonrecursive_to_leaf = (
        leaf_sync.get("sync_closed") is True
        and leaf_sync.get("next_direct_attack_target") == f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}"
    )
    leaf_current = (
        leaf.get("current_leaf_firewall_active_basis_reduced") is True
        and leaf.get("terminal_gap_after_current_instance_router")
        == f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}"
    )
    legal_open = legal.get("noncanonical_legal_closure_mode_proved") is False
    uv_open = (
        uv.get("exact_uv_map_rank_incidence_router_closed") is True
        and uv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False
    )
    dstructure_open = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )

    return [
        row(
            "PostAntiSplitPointwiseFrontierImported",
            post_to_pointwise,
            False,
            "post-antisplit source-rank/no-collapse 前沿已汇合到逐 primitive alpha/delta 核表。",
            POINTWISE_TABLE,
        ),
        row(
            "AlphaAndWeightLegsReturnToTerminal",
            alpha_returns and weight_returns,
            False,
            "alpha row 公式腿与 signed weight/identity 腿单独攻击都会回到 PDEC/CleanKLS 终端门。",
            PDEC_KLS,
        ),
        row(
            "ThreeLegSeparateAttackFixedPointImported",
            three_leg_fixed,
            True,
            "三腿逐项攻击只会在 source table、alpha signed lift、PDEC/CleanKLS 之间循环。",
            NONRECURSIVE_TABLE,
        ),
        row(
            "NonrecursivePointwiseFieldContractImported",
            field_contract,
            True,
            "非递归逐点表字段边界已闭合；第一生产性字段是显式 joint constructor rule。",
            JOINT_CONSTRUCTOR,
        ),
        row(
            "JointConstructorOldRouteReturnsToTerminalLeaf",
            nonrecursive_to_leaf,
            False,
            "若没有新的 actual joint constructor 公式工件，旧 joint 路线回到 signed-source 固定点并进入终端叶子。",
            f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        ),
        row(
            "CurrentTerminalLeafReduced",
            leaf_current,
            False,
            "当前已物化 PDEC/sparse 前沿清零后，活动终端叶子只剩 canonical-lock 或 noncanonical legal mode。",
            f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        ),
        row(
            "NoncanonicalLegalModeStillOpen",
            legal_open,
            False,
            "noncanonical full-S 合法模式仍需实际源恒等、强化反原子或外部合同；strict 自足线未闭合。",
            NONCANONICAL_MODE,
        ),
        row(
            "ExactUVIncidenceStillParallel",
            uv_open,
            False,
            "非递归核表和终端叶子路线仍需 actual exact-UV bounded multiplicity incidence。",
            UV_INCIDENCE,
        ),
        row(
            "DStructureGateStillOpen",
            dstructure_open,
            False,
            "DStructure/Rankin 晋级门仍只完成边界命名，未独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只完成 post-antisplit 到终端叶子的同步；未证明 canonical-lock、noncanonical legal mode、ExactUV、RatePreservation 或 DStructure。",
            "row/column theorem still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "post": load_json(POST_ANTISPLIT),
        "three": load_json(KERNEL_THREE_LEG),
        "field": load_json(NONRECURSIVE_FIELD),
        "leaf_sync": load_json(NONRECURSIVE_TO_LEAF),
        "alpha": load_json(ALPHA_TERMINAL),
        "weight": load_json(WEIGHT_DOWNSTREAM),
        "leaf": load_json(TERMINAL_LEAF),
        "legal": load_json(NONCANONICAL_LEGAL),
        "uv": load_json(UV_RANK),
        "dstructure": load_json(DSTRUCTURE_ACCEPTANCE),
    }
    rows = build_rows(data)
    strict_basis = (
        f"({CANONICAL_LOCK} OR {NONCANONICAL_MODE}) AND {UV_INCIDENCE} "
        f"AND {RATE} AND {DSTRUCTURE}"
    )
    result = {
        "certificate_type": "prime_matrix_strict_post_antisplit_alpha_terminal_leaf_sync_router",
        "status": "post_antisplit_alpha_frontier_synced_to_terminal_leaf_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "post_antisplit_pointwise_frontier_imported": rows[0]["closed"],
        "alpha_and_weight_legs_return_to_terminal": rows[1]["closed"],
        "three_leg_separate_attack_fixed_point_imported": rows[2]["closed"],
        "nonrecursive_pointwise_field_contract_imported": rows[3]["closed"],
        "joint_constructor_old_route_returns_to_terminal_leaf": rows[4]["closed"],
        "current_terminal_leaf_reduced": rows[5]["closed"],
        "noncanonical_legal_mode_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        "parallel_direct_attack_targets": [UV_INCIDENCE, RATE, DSTRUCTURE],
        "strict_active_basis_after_sync": strict_basis,
        "sync_edges": sync_edges(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 post-antisplit 后暴露出的 alpha row 首攻点继续同步到已有更深前沿："
            "alpha/weight/rank 三腿分攻是固定点，非递归逐点表的第一字段又会经旧 joint constructor "
            "路线回到 signed-source 固定点并进入终端叶子。因此最新严格自足活动基更新为 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NoncanonicalFullSComplementLegalClosureMode`，"
            "并行仍需 ExactUV incidence、RatePreservation 与 DStructure/Rankin。行/列命题仍未无条件闭合。"
        ),
    }
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict post-antisplit alpha 到终端叶子同步前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"post_antisplit_pointwise_frontier_imported={fmt_bool(result['post_antisplit_pointwise_frontier_imported'])}",
        f"alpha_and_weight_legs_return_to_terminal={fmt_bool(result['alpha_and_weight_legs_return_to_terminal'])}",
        f"three_leg_separate_attack_fixed_point_imported={fmt_bool(result['three_leg_separate_attack_fixed_point_imported'])}",
        f"nonrecursive_pointwise_field_contract_imported={fmt_bool(result['nonrecursive_pointwise_field_contract_imported'])}",
        f"joint_constructor_old_route_returns_to_terminal_leaf={fmt_bool(result['joint_constructor_old_route_returns_to_terminal_leaf'])}",
        f"current_terminal_leaf_reduced={fmt_bool(result['current_terminal_leaf_reduced'])}",
        f"noncanonical_legal_mode_proved={fmt_bool(result['noncanonical_legal_mode_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "parallel_direct_attack_targets=" + ", ".join(result["parallel_direct_attack_targets"]),
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for edge in result["sync_edges"]:
        lines.append(
            f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
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
            "## 3. 当前严格活动基",
            "",
            "```text",
            result["strict_active_basis_after_sync"],
            "```",
            "",
            "## 4. 结论边界",
            "",
            "- 本文件只同步当前前沿，不证明行/列命题。",
            "- alpha 单腿、weight 单腿、rank 单腿和旧 joint constructor 展开都不能作为非循环闭合。",
            "- 当前必须继续攻 canonical-lock 或 noncanonical legal mode，并同时保留 ExactUV、RatePreservation、DStructure/Rankin。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    result = build_result()
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


if __name__ == "__main__":
    main()
