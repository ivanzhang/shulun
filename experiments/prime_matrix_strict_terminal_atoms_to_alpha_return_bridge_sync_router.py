#!/usr/bin/env python3
"""生成 terminal three atoms 到 alpha-return 独立桥前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_atoms_to_alpha_return_bridge_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json

输出：
  data/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-ledger.json
  docs/monograph/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json
  docs/monograph/prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json",
    "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
    "prime-matrix-strict-moving-atom-entropy-normal-form-router.json",
    "prime-matrix-strict-post-mertens-nonrecursive-frontier-sync-router.json",
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
    "prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json",
    "prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.json",
    "prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json",
]

CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
A1_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
EXACT_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
KERNEL_IDENTITY = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"
POINTWISE_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
NONRECURSIVE_TABLE = "NonrecursivePointwisePrimitiveKernelTableConstructionWithoutTerminalReturn"
JOINT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
LEGAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
ACTUAL_SOURCE_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn"
DSTRUCTURE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
MERTENS_TAIL = (
    "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 "
    "AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
)


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象并由 missing_sources 暴露。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值渲染为小写文本。"""
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


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def sync_chain() -> list[dict[str, str]]:
    """给出本轮从三原子到 alpha-return 独立桥的吸收链。"""
    return [
        {
            "from": f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
            "to": f"{CANONICAL_LOCK} OR {MOVING_ATOM}",
            "meaning": "A1 clean branch admission 已被 canonical scoped 分支吸收；它不是 unrestricted noncanonical 全局矛盾。",
        },
        {
            "from": MOVING_ATOM,
            "to": EXACT_ENTROPY,
            "meaning": "moving atom 标准形等价到 actual clean-core exact source entropy。",
        },
        {
            "from": EXACT_ENTROPY,
            "to": KERNEL_IDENTITY,
            "meaning": "post-Mertens 非递归同步删除终端标签回流，把破环原子压到同 formal-unit kernel identity。",
        },
        {
            "from": KERNEL_IDENTITY,
            "to": POINTWISE_TABLE,
            "meaning": "kernel identity 攻坚显示必须先给逐 primitive row 的同 formal-unit alpha/delta 核表。",
        },
        {
            "from": POINTWISE_TABLE,
            "to": NONRECURSIVE_TABLE,
            "meaning": "三腿后验拼装会回流，合法路线必须一次性提交非递归 primitive 表字段合同。",
        },
        {
            "from": NONRECURSIVE_TABLE,
            "to": JOINT_RULE,
            "meaning": "字段合同第一生产性原子是 actual noncanonical joint primitive word/coefficient constructor rule。",
        },
        {
            "from": JOINT_RULE,
            "to": f"{CANONICAL_LOCK} OR {LEGAL_MODE}",
            "meaning": "旧 joint-alpha/same-row/row-level 展开回到 signed-source 固定点并进入终端叶子。",
        },
        {
            "from": LEGAL_MODE,
            "to": ACTUAL_SOURCE_BRIDGE,
            "meaning": "strict 自足过滤外部 FullS-KLS 与 generic WFD 后，noncanonical 叶子只能靠进入 alpha 回边前的独立 actual-source 桥。",
        },
        {
            "from": "old pointwise/alpha descent route",
            "to": "terminal-family backedge",
            "meaning": "alpha row formula 经 PDEC/CleanKLS 回到终端家族，不能当作 well-founded descent 进展量。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """读取关键证书并汇总当前前沿。"""
    terminal = data["terminal"]
    canonical = data["canonical"]
    moving = data["moving"]
    post_mertens = data["post_mertens"]
    kernel = data["kernel"]
    pointwise = data["pointwise"]
    field = data["field"]
    to_leaf = data["to_leaf"]
    leaf = data["leaf"]
    legal = data["legal"]
    alpha_return = data["alpha_return"]
    three_atoms = set(terminal.get("terminal_atoms", terminal.get("three_atoms", [])))

    return [
        row(
            "TerminalThreeAtomsImported",
            terminal.get("terminal_three_atoms_pinned") is True
            and {CANONICAL_LOCK, A1_ADMISSION, MOVING_ATOM}.issubset(three_atoms),
            False,
            "上一轮最新提交把 post-alpha 非循环前沿压成三原子。",
            f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
        ),
        row(
            "A1AdmissionAbsorbedAsScopedBranch",
            canonical.get("canonical_lock_nonrecursive_exit_firewall_closed") is True
            and canonical.get("canonical_lock_refined_to_exact_same_set_certificate") is True,
            False,
            "A1/canonical 分支只能作为 scoped canonical 晋级证书；缺五项同集证书时不能闭合 unrestricted 分支。",
            CANONICAL_LOCK,
        ),
        row(
            "MovingAtomReducedToExactEntropy",
            moving.get("moving_atom_entropy_normal_form_closed") is True
            and moving.get("actual_noncanonical_clean_core_moving_atom_exclusion_proved") is False,
            False,
            "moving atom 不是孤立硬点，已等价到 exact clean-core source entropy。",
            EXACT_ENTROPY,
        ),
        row(
            "PostMertensReducedToKernelIdentity",
            post_mertens.get("post_mertens_nonrecursive_frontier_sync_closed") is True
            and post_mertens.get("next_direct_attack_target") == KERNEL_IDENTITY,
            False,
            "Mertens/解析尾段移出活动剩余后，非递归破环原子被压到同 formal-unit kernel identity。",
            KERNEL_IDENTITY,
        ),
        row(
            "KernelIdentityReducedToPointwiseTable",
            kernel.get("kernel_identity_attack_router_closed") is True
            and kernel.get("next_direct_attack_target") == POINTWISE_TABLE,
            False,
            "kernel identity 不能由记录守恒或几何 Phi 自动推出，需要逐 primitive row 核表。",
            POINTWISE_TABLE,
        ),
        row(
            "PointwiseTableCannotBeThreeLegPatch",
            pointwise.get("pointwise_kernel_table_router_closed") is True
            and pointwise.get("pointwise_primitive_kernel_table_proved") is False
            and field.get("field_contract_boundary_closed") is True,
            False,
            "alpha/weight/rank 三腿后验拼装会回流；字段合同要求同一 formal unit 一次性给出非递归表。",
            NONRECURSIVE_TABLE,
        ),
        row(
            "NonrecursiveTableReturnsToTerminalLeafWithoutNewFormula",
            to_leaf.get("sync_closed") is True
            and to_leaf.get("joint_constructor_path_is_fixed_point_without_new_formula") is True,
            False,
            "旧 joint constructor 展开回到 signed-source 固定点；无新公式时只能进入终端叶子。",
            f"{CANONICAL_LOCK} OR {LEGAL_MODE}",
        ),
        row(
            "CurrentLeafReducedToLegalModeOrCanonicalLock",
            leaf.get("current_leaf_firewall_active_basis_reduced") is True
            and leaf.get("future_schema_global_nonexistence_claimed") is False,
            False,
            "当前物化 PDEC/sparse 前沿只作为当前实例清零，不能宣称 future family 全局不存在。",
            f"{CANONICAL_LOCK} OR {LEGAL_MODE}",
        ),
        row(
            "LegalModeFilteredToActualSourceBridge",
            legal.get("noncanonical_legal_closure_boundary_refined") is True
            and legal.get("actual_source_bridge_theorem_closed") is False,
            False,
            "strict 自足线过滤外部 FullS-KLS 和 generic WFD 后，noncanonical 叶子压到 actual-source 锁定或强化反原子。",
            "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
        ),
        row(
            "AlphaReturnRouteReclassifiedAsBackedge",
            alpha_return.get("descent_leaf_firewall_alpha_return_sync_router_closed") is True
            and alpha_return.get("pointwise_alpha_route_counts_as_well_founded_descent") is False,
            True,
            "旧 pointwise/alpha 下钻经 PDEC/CleanKLS 回到终端家族，只能登记为回边，不能登记为下降量。",
            f"{CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}",
        ),
        row(
            "CurrentStrictSelfContainedFrontierPinned",
            alpha_return.get("terminal_gap_after_router")
            == f"{CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}",
            False,
            "三原子前沿继续同步后，当前最窄 strict 自足数学输入是 canonical-lock 或进入 alpha 回边前的独立 actual-source 桥。",
            f"({CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}) AND ({MERTENS_TAIL}) AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只完成跨前沿同步与回边分类；尚未提交 canonical-lock、独立 actual-source 桥、高段自足尾项或 DStructure/Rankin 替代包。",
            f"({CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}) AND ({MERTENS_TAIL}) AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造本轮同步证书。"""
    data = {
        "terminal": load_json("prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json"),
        "canonical": load_json("prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"),
        "moving": load_json("prime-matrix-strict-moving-atom-entropy-normal-form-router.json"),
        "post_mertens": load_json("prime-matrix-strict-post-mertens-nonrecursive-frontier-sync-router.json"),
        "kernel": load_json("prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json"),
        "pointwise": load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json"),
        "field": load_json("prime-matrix-strict-nonrecursive-pointwise-kernel-table-field-contract-router.json"),
        "to_leaf": load_json("prime-matrix-strict-nonrecursive-kernel-to-terminal-leaf-sync-router.json"),
        "leaf": load_json("prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"),
        "legal": load_json("prime-matrix-strict-noncanonical-legal-closure-mode-router.json"),
        "alpha_return": load_json("prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    strict_basis = (
        f"({CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}) "
        f"AND ({MERTENS_TAIL}) AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_strict_terminal_atoms_to_alpha_return_bridge_sync_router",
        "status": "terminal_atoms_synced_to_alpha_return_independent_bridge_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "terminal_three_atoms_imported": rows[0]["closed"],
        "a1_admission_absorbed_as_scoped_branch": rows[1]["closed"],
        "moving_atom_reduced_to_exact_entropy": rows[2]["closed"],
        "post_mertens_reduced_to_kernel_identity": rows[3]["closed"],
        "kernel_identity_reduced_to_pointwise_table": rows[4]["closed"],
        "nonrecursive_table_field_contract_imported": rows[5]["closed"],
        "joint_constructor_route_to_terminal_leaf_imported": rows[6]["closed"],
        "terminal_leaf_current_instance_reduced": rows[7]["closed"],
        "noncanonical_legal_mode_filtered": rows[8]["closed"],
        "alpha_return_route_reclassified_as_backedge": rows[9]["closed"],
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": f"{CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}",
        "strict_self_contained_math_basis_after_router": strict_basis,
        "with_external_mertens_high_tail_removed_basis": (
            f"({CANONICAL_LOCK} OR {ACTUAL_SOURCE_BRIDGE}) AND {DSTRUCTURE}"
        ),
        "conditional_external_math_basis_after_router": (
            f"({CANONICAL_LOCK} OR ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab "
            "OR FullSNonAPStrengthenedSourceAntiAtomForActualSource "
            f"OR AcceptOrProveExactFullS-KLS-ext) AND ({MERTENS_TAIL}) AND {DSTRUCTURE}"
        ),
        "sync_chain": sync_chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "上一轮三原子前沿不能停在 `IndependentNonterminalMovingAtomExclusion`。"
            "沿已有 moving-atom entropy、post-Mertens、kernel identity、pointwise table、"
            "nonrecursive field contract、terminal leaf firewall 与 alpha-return 防火墙继续同步后，"
            "旧 pointwise/alpha 下钻被判为回到终端家族的回边。"
            "当前 strict 自足主攻更新为 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
            "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn`；行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict terminal atoms 到 alpha-return 独立桥同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"terminal_three_atoms_imported={fmt_bool(result['terminal_three_atoms_imported'])}",
        f"moving_atom_reduced_to_exact_entropy={fmt_bool(result['moving_atom_reduced_to_exact_entropy'])}",
        f"post_mertens_reduced_to_kernel_identity={fmt_bool(result['post_mertens_reduced_to_kernel_identity'])}",
        f"kernel_identity_reduced_to_pointwise_table={fmt_bool(result['kernel_identity_reduced_to_pointwise_table'])}",
        f"alpha_return_route_reclassified_as_backedge={fmt_bool(result['alpha_return_route_reclassified_as_backedge'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")

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
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "必须证明 canonical-lock 的同集推前/有限因子图/无 payload 残留五项证书，或在进入 exact-UV/rank/alpha 回边前独立证明 actual-source 恒等或强化反原子。不能把旧 pointwise/alpha 展开、当前 PDEC/sparse 清零、外部 FullS-KLS 或下游 payment 恢复当作 strict 自足证明。",
            "",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["## 5. 缺失依赖", ""])
        for name in result["missing_sources"]:
            lines.append(f"- `{name}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
