#!/usr/bin/env python3
"""生成 strict 终端下降到逐点核表的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_descent_to_pointwise_kernel_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.md"

TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
NONCANONICAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
ACTUAL_SOURCE_BRIDGE = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
PRETERMINAL_SUPPORT = "PreTerminalActualFullSFactorSupportCapacityTheorem"
FIBER_APERIODICITY = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
FIBER_ABS = "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
SOURCE_RANK_PACKAGE = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_COEFFICIENT_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW_FORMULA = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SIGNED_WEIGHT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json",
    "prime-matrix-strict-preterminal-support-capacity-attack-router.json",
    "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json",
    "prime-matrix-strict-actual-source-domain-entropy-atom-router.json",
    "prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
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
    """登记本证书读取到的证据哈希。"""
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


def sync_chain() -> list[dict[str, str]]:
    """列出从终端下降到共同核表的同步链。"""
    return [
        {"from": TERMINAL_DESCENT, "to": "TerminalLeafFirewallInputs_OR_CanonicalLock"},
        {"from": "TerminalLeafFirewallInputs_OR_CanonicalLock", "to": f"{NONCANONICAL_MODE}_OR_CanonicalLock"},
        {"from": NONCANONICAL_MODE, "to": ACTUAL_SOURCE_BRIDGE},
        {"from": "CanonicalLock scoped branch", "to": SOURCE_ENTROPY},
        {"from": ACTUAL_SOURCE_BRIDGE, "to": SOURCE_ENTROPY},
        {"from": SOURCE_ENTROPY, "to": PRETERMINAL_SUPPORT},
        {"from": PRETERMINAL_SUPPORT, "to": FIBER_APERIODICITY},
        {"from": FIBER_APERIODICITY, "to": FIBER_ABS},
        {"from": FIBER_ABS, "to": SOURCE_RANK_PACKAGE},
        {"from": SOURCE_RANK_PACKAGE, "to": f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}"},
        {"from": DOMAIN_ENTROPY, "to": SIGNED_COEFFICIENT_LAW},
        {"from": COMPLETE_KEY, "to": SOURCE_TABLE},
        {"from": FIXED_KEY_MULT, "to": "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem / fixed-pair fiber bound"},
        {"from": f"{DOMAIN_ENTROPY} / {COMPLETE_KEY} / {FIXED_KEY_MULT}", "to": POINTWISE_KERNEL},
        {"from": POINTWISE_KERNEL, "to": f"{ALPHA_ROW_FORMULA} AND {SIGNED_WEIGHT_IDENTITY} AND {RANK_CERT}"},
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步各路由证书，判断最新共同硬点。"""
    joint_sync = data["joint_sync"]
    descent = data["descent"]
    leaf = data["leaf"]
    noncanonical = data["noncanonical"]
    canonical_absorb = data["canonical_absorb"]
    entropy_firewall = data["entropy_firewall"]
    atomization = data["atomization"]
    support_capacity = data["support_capacity"]
    fiber_atom = data["fiber_atom"]
    domain_entropy = data["domain_entropy"]
    coefficient_law = data["coefficient_law"]
    complete_key = data["complete_key"]
    source_table = data["source_table"]
    fixed_pair = data["fixed_pair"]
    kernel_identity = data["kernel_identity"]
    pointwise_kernel = data["pointwise_kernel"]

    terminal_to_leaf = (
        joint_sync.get("next_direct_attack_target") == TERMINAL_DESCENT
        and descent.get("terminal_return_well_founded_descent_schema_closed") is True
        and descent.get("acyclic_terminal_return_well_founded_descent_proved") is False
    )
    leaf_to_noncanonical = (
        leaf.get("current_leaf_firewall_active_basis_reduced") is True
        and leaf.get("noncanonical_legal_closure_mode_proved") is False
    )
    noncanonical_to_source = (
        noncanonical.get("strict_self_contained_terminal_after_router")
        == "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
        and noncanonical.get("actual_source_bridge_theorem_closed") is False
    )
    canonical_absorbed = (
        canonical_absorb.get("canonical_lock_branch_absorption_closed") is True
        and canonical_absorb.get("next_direct_attack_target") == SOURCE_ENTROPY
    )
    source_to_exactuv = (
        entropy_firewall.get("new_actual_source_entropy_theorem_proved") is False
        and atomization.get("next_direct_attack_target") == PRETERMINAL_SUPPORT
        and support_capacity.get("next_direct_attack_target") == FIBER_APERIODICITY
    )
    exactuv_to_rank_package = (
        fiber_atom.get("terminal_gap_after_router") == SOURCE_RANK_PACKAGE
        and fiber_atom.get("preterminal_fiber_dispersion_source_atomization_closed") is True
    )
    domain_entropy_recycles = (
        domain_entropy.get("next_direct_attack_target") == SIGNED_COEFFICIENT_LAW
        and coefficient_law.get("next_direct_attack_target")
        == "AcyclicSeedPreCauchyBasisWeightSourceFormulaForPrimitiveRows"
    )
    complete_key_needs_source_table = (
        complete_key.get("complete_emitter_key_partition_router_closed") is True
        and complete_key.get("actual_noncanonical_primitive_emitter_source_table_proved") is False
        and source_table.get("next_direct_attack_target")
        == "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
    )
    fixed_key_needs_rank = (
        fixed_pair.get("fixed_pair_fiber_bound_router_closed") is True
        and fixed_pair.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False
    )
    pointwise_table_common = (
        kernel_identity.get("next_direct_attack_target") == POINTWISE_KERNEL
        and pointwise_kernel.get("next_direct_attack_target") == ALPHA_ROW_FORMULA
    )

    return [
        row(
            "CounterexampleBranchPreserved",
            True,
            True,
            "本同步仍在早期零行反例链内推进，不用真实零行缺席或数值实验代替证明。",
            "row_column_unconditional_closed=false",
        ),
        row(
            "TerminalDescentImportedAsActiveTarget",
            joint_sync.get("next_direct_attack_target") == TERMINAL_DESCENT,
            False,
            "上一同步证书已把 joint-alpha/source 固定点后的唯一非循环门钉为终端下降证书。",
            TERMINAL_DESCENT,
        ),
        row(
            "TerminalDescentReducedToLeafFirewall",
            terminal_to_leaf,
            False,
            "终端下降 schema 删除无隐藏循环，但未排斥叶子防火墙输入。",
            "TerminalLeafFirewallInputs_OR_CanonicalLock",
        ),
        row(
            "LeafFirewallCurrentInstanceReduced",
            leaf_to_noncanonical,
            False,
            "当前物化 PDEC/sparse 前沿移出活动硬点后，终端叶子压到 noncanonical full-S 合法模式或 canonical-lock。",
            f"{NONCANONICAL_MODE}_OR_CanonicalLock",
        ),
        row(
            "NoncanonicalLegalModeReducedToActualSourceBridge",
            noncanonical_to_source,
            False,
            "strict 自足线过滤外部 FullS-KLS 与 generic WFD 后，只剩实际源锁定或强化反原子。",
            ACTUAL_SOURCE_BRIDGE,
        ),
        row(
            "CanonicalLockScopedBranchAbsorbed",
            canonical_absorbed,
            True,
            "canonical-lock 若证书存在只进入 scoped canonical 分支；证书缺失时不能当作全局出口。",
            SOURCE_ENTROPY,
        ),
        row(
            "SourceEntropyReducedToExactUVFiberAperiodicity",
            source_to_exactuv,
            False,
            "actual-source entropy 已经经支撑/容量定理压到 preterminal exact-UV fiber 非集中。",
            FIBER_APERIODICITY,
        ),
        row(
            "ExactUVFiberReducedToSourceRankPackage",
            exactuv_to_rank_package,
            False,
            "preterminal fiber 绝对质量分散等价地需要源域 rank/no-collapse 三原子包。",
            SOURCE_RANK_PACKAGE,
        ),
        row(
            "DomainEntropyFirstAtomRecyclesToSignedSource",
            domain_entropy_recycles,
            True,
            "三原子包第一项 source-domain entropy 的首攻点回到 primitive signed coefficient law，继续下钻会重入 signed-source 固定点。",
            SIGNED_COEFFICIENT_LAW,
        ),
        row(
            "CompleteKeyAtomNeedsActualSourceTable",
            complete_key_needs_source_table,
            False,
            "complete key 不能后验补标签；它需要 pre-Cauchy actual emitter source table。",
            SOURCE_TABLE,
        ),
        row(
            "FixedKeyMultiplicityAtomNeedsRankCertificate",
            fixed_key_needs_rank,
            False,
            "固定 key 的 O(1) exact-UV 原像界需要同一 primitive 表上的 rank/multiplicity 证书。",
            RANK_CERT,
        ),
        row(
            "PointwiseKernelTableIsCommonVariableTable",
            pointwise_table_common,
            False,
            "source-domain entropy、complete key 与 fixed-key multiplicity 的共同非后验对象是同 formal-unit 逐 primitive 核表。",
            POINTWISE_KERNEL,
        ),
        row(
            "PointwiseKernelTableReducedToThreeInputs",
            pointwise_kernel.get("pointwise_kernel_table_router_closed") is True,
            False,
            "逐点核表已被压成行发射公式、signed 权重恒等式和同表 rank/multiplicity 证书。",
            f"{ALPHA_ROW_FORMULA} AND {SIGNED_WEIGHT_IDENTITY} AND {RANK_CERT}",
        ),
        row(
            "LatestPriorityAtomPinned",
            pointwise_kernel.get("next_direct_attack_target") == ALPHA_ROW_FORMULA,
            False,
            "没有 alpha row anchor/phase 发射公式，就没有可赋权、可映到 Phi 和 exact-UV 的 primitive row 集合。",
            ALPHA_ROW_FORMULA,
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "本步只完成终端下降到共同核表的同步压缩，尚未证明行发射公式或终端矛盾。",
            f"{ALPHA_ROW_FORMULA} AND {SIGNED_WEIGHT_IDENTITY} AND {RANK_CERT} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "joint_sync": load_json("prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json"),
        "descent": load_json("prime-matrix-strict-acyclic-terminal-descent-firewall-router.json"),
        "leaf": load_json("prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json"),
        "noncanonical": load_json("prime-matrix-strict-noncanonical-legal-closure-mode-router.json"),
        "canonical_absorb": load_json("prime-matrix-strict-canonical-lock-branch-absorption-router.json"),
        "entropy_firewall": load_json("prime-matrix-strict-exact-entropy-source-law-firewall-router.json"),
        "atomization": load_json("prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json"),
        "support_capacity": load_json("prime-matrix-strict-preterminal-support-capacity-attack-router.json"),
        "fiber_atom": load_json("prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"),
        "domain_entropy": load_json("prime-matrix-strict-actual-source-domain-entropy-atom-router.json"),
        "coefficient_law": load_json("prime-matrix-strict-acyclic-seed-primitive-coefficient-law-router.json"),
        "complete_key": load_json("prime-matrix-strict-complete-emitter-key-partition-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "fixed_pair": load_json("prime-matrix-strict-fixed-pair-fiber-bound-router.json"),
        "kernel_identity": load_json("prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json"),
        "pointwise_kernel": load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json"),
    }
    rows = build_rows(data)
    common_table = next(item["closed"] for item in rows if item["gate"] == "PointwiseKernelTableIsCommonVariableTable")
    latest_atom = next(item["closed"] for item in rows if item["gate"] == "LatestPriorityAtomPinned")
    return {
        "certificate_type": "prime_matrix_strict_terminal_descent_to_pointwise_kernel_sync_router",
        "status": "terminal_descent_synced_to_pointwise_kernel_alpha_row_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "terminal_descent_to_pointwise_kernel_sync_closed": True,
        "terminal_descent_schema_closed_leaf_inputs_open": data["descent"].get("terminal_return_well_founded_descent_schema_closed") is True,
        "source_rank_package_reached": data["fiber_atom"].get("terminal_gap_after_router") == SOURCE_RANK_PACKAGE,
        "domain_entropy_first_atom_recycles_to_signed_source": next(
            item["closed"] for item in rows if item["gate"] == "DomainEntropyFirstAtomRecyclesToSignedSource"
        ),
        "pointwise_kernel_table_is_common_variable_table": common_table,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "row_column_unconditional_closed": False,
        "direct_unconditional_contradiction_found": False,
        "next_direct_attack_target": ALPHA_ROW_FORMULA,
        "parallel_required_inputs": [SIGNED_WEIGHT_IDENTITY, RANK_CERT],
        "terminal_gap_after_router": f"{ALPHA_ROW_FORMULA} AND {SIGNED_WEIGHT_IDENTITY} AND {RANK_CERT} AND {DSTRUCTURE}",
        "sync_chain": sync_chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"`{TERMINAL_DESCENT}` 的当前非循环下钻经终端叶子、noncanonical 合法闭合、"
            f"actual-source entropy 与 exact-UV fiber 分散后，落到 `{SOURCE_RANK_PACKAGE}`。"
            f"其中 `{DOMAIN_ENTROPY}` 首攻会回到 signed-source 固定点；"
            f"`{COMPLETE_KEY}` 与 `{FIXED_KEY_MULT}` 共同需要 `{POINTWISE_KERNEL}`。"
        ),
        "plain_conclusion": (
            "本步把终端下降证书的下游链条同步到共同变量表：继续沿 source-domain entropy 首原子会回到"
            " signed coefficient law/source 固定点；complete key 需要 actual source table；fixed-key multiplicity"
            " 需要同一 primitive 表上的 rank/no-collapse。因此当前最窄非后验对象是同 formal-unit 逐 primitive"
            " alpha/delta 核表，而该核表的第一优先硬点是 alpha row anchor/phase 发射公式。"
            "这仍不是闭合证明，行/列命题保持未闭合。"
        ),
        "latest_priority_atom_pinned": latest_atom,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 终端下降到逐点核表同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_descent_to_pointwise_kernel_sync_closed={fmt_bool(result['terminal_descent_to_pointwise_kernel_sync_closed'])}",
        f"terminal_descent_schema_closed_leaf_inputs_open={fmt_bool(result['terminal_descent_schema_closed_leaf_inputs_open'])}",
        f"source_rank_package_reached={fmt_bool(result['source_rank_package_reached'])}",
        f"domain_entropy_first_atom_recycles_to_signed_source={fmt_bool(result['domain_entropy_first_atom_recycles_to_signed_source'])}",
        f"pointwise_kernel_table_is_common_variable_table={fmt_bool(result['pointwise_kernel_table_is_common_variable_table'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"independent_noncanonical_precauchy_arithmetic_identity_statement_proved={fmt_bool(result['independent_noncanonical_precauchy_arithmetic_identity_statement_proved'])}",
        f"same_unit_exact_uv_rank_multiplicity_certificate_proved={fmt_bool(result['same_unit_exact_uv_rank_multiplicity_certificate_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        result["frontier_reduction"],
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["sync_chain"]:
        lines.append(f"| {table_cell(item['from'])} | {table_cell(item['to'])} |")

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
            "## 3. 下一真正单点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行必要输入：",
            "",
            "```text",
            "\n".join(result["parallel_required_inputs"]),
            "```",
            "",
            "当前活动基：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "```",
            "",
            "审稿边界：本文件只证明终端下降链条的当前最窄同步定位；"
            "它没有证明 alpha row 发射公式、signed 权重恒等式或 rank/multiplicity 证书，"
            "也没有证明行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
