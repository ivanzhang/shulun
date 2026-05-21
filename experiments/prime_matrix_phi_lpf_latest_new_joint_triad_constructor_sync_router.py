#!/usr/bin/env python3
"""生成 Phi-LPF latest new-joint 三破环口到显式 constructor 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_triad_constructor_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_TRIAD = DOCS / "prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-router.json"
STRICT_UNIFIED = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
SEED_CYCLE = DOCS / "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"
PDEC_SCOPE_FRONTIER = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
STRICT_NEW_JOINT_ANTISPLIT = DOCS / "prime-matrix-strict-new-joint-formula-antisplit-atom-router.json"
JOINT_FIELD_ATOM = DOCS / "prime-matrix-strict-joint-emitter-formula-field-atom-router.json"
JOINT_DECL_CONSTRUCTOR = DOCS / "prime-matrix-strict-joint-declaration-constructor-sync-router.json"

CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TRIAD = f"{CYCLE_CUT}_OR_{PDEC_SCOPE}_OR_{NEW_JOINT}"
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
EXPLICIT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
NON_SPLIT_ATOM = "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection"
DOMAIN_TARGET = "JointConstructorDomainCleanCoreMembershipAndSameSourceTupleLedger"
ROW_TARGET = "JointConstructorFormulaEmitsBasisWordUVKeySignLocalFactorCoefficientRowsLedger"
TIMESTAMP_TARGET = "SameFormalUnitPreCauchyTimestampLockLedger"
NO_LEAK_TARGET = "NoncanonicalJointDeclarationNoCanonicalOrExternalLeakLedger"
RETURN_TARGET = "JointConstructorFormulaFailureReturnTagsLedger"
JOINT_ROWS = "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward"
JOINT_IDENTITY = "JointEmitterPrepushforwardWordCoefficientIdentityLedger"
JOINT_RETURN = "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
EXACTUV_INC = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖哈希。"""
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


def dependency_paths() -> list[Path]:
    """列出本层依赖。"""
    return [
        LATEST_TRIAD,
        STRICT_UNIFIED,
        SEED_CYCLE,
        PDEC_SCOPE_FRONTIER,
        STRICT_NEW_JOINT_ANTISPLIT,
        JOINT_FIELD_ATOM,
        JOINT_DECL_CONSTRUCTOR,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def productive_constructor_basis() -> str:
    """返回显式 joint constructor 的完整生产性字段基。"""
    return (
        f"{EXPLICIT_RULE} AND {DOMAIN_TARGET} AND {ROW_TARGET} AND "
        f"{TIMESTAMP_TARGET} AND {NO_LEAK_TARGET} AND {RETURN_TARGET}"
    )


def joint_declaration_basis() -> str:
    """返回 joint declaration 的字段基。"""
    return f"{JOINT_DECL} AND {JOINT_ROWS} AND {JOINT_IDENTITY} AND {JOINT_RETURN}"


def sync_chain() -> list[dict[str, str]]:
    """给出同步链。"""
    return [
        {
            "from": TRIAD,
            "to": f"{PDEC_SCOPE} OR {NEW_JOINT}",
            "meaning": "seed cycle-cut 分支在当前 strict 语料中已饱和；若不提交新的 source 输入，就落到 PDEC scope 或 new joint。",
        },
        {
            "from": PDEC_SCOPE,
            "to": f"{NEW_JOINT} OR {EXTERNAL_DIBFI}",
            "meaning": "same-set PDEC scope 内部分支不再给自足非循环出口，只保留条件外部线或转向 new joint。",
        },
        {
            "from": NEW_JOINT,
            "to": JOINT_DECL,
            "meaning": "strict 统一前沿把 cycle-cut/PDEC/new-joint 的内部生产性第一行同步到 joint declaration line。",
        },
        {
            "from": JOINT_DECL,
            "to": EXPLICIT_RULE,
            "meaning": "joint declaration 不是公式本身；必须给同一 actual source tuple 的显式 alpha/delta primitive constructor rule。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    strict_unified: dict[str, Any],
    seed_cycle: dict[str, Any],
    pdec: dict[str, Any],
    antisplit: dict[str, Any],
    joint_field: dict[str, Any],
    declaration: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LatestTriadImported",
            latest.get("next_primary_attack_target") == TRIAD
            and latest.get("seed_cycle_cut_input_proved") is False
            and latest.get("acyclic_same_set_scope_match_proved") is False
            and latest.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "上一层已把来源恒等式后的非循环主攻压成 cycle-cut/PDEC/new-joint 三破环口。",
            TRIAD,
        ),
        row(
            "SeedCycleCutSaturationImported",
            seed_cycle.get("seed_cycle_cut_branch_saturated") is True
            and seed_cycle.get("next_direct_attack_target") == f"{PDEC_SCOPE}_OR_{NEW_JOINT}",
            False,
            "cycle-cut 顺序拆分当前已饱和；没有新 source 输入时只剩 PDEC scope 或 new joint。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "PDECScopeInternalSaturationImported",
            pdec.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
            and pdec.get("next_direct_attack_target") == NEW_JOINT,
            False,
            "same-set PDEC 在内部语料中不再提供独立自足出口，只能作为条件证书或进入 new joint。",
            f"{NEW_JOINT} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "StrictUnifiedDeclarationLineImported",
            strict_unified.get("new_joint_formula_reduced_to_declaration_line") is True
            and strict_unified.get("next_direct_attack_target") == JOINT_DECL,
            False,
            "cycle-cut、terminal、PDEC 与 new-joint 的 strict 统一前沿已定位到 joint declaration line。",
            joint_declaration_basis(),
        ),
        row(
            "JointEmitterFieldAtomImported",
            joint_field.get("next_direct_attack_target") == JOINT_DECL
            and joint_field.get("pre_cauchy_joint_declaration_line_proved") is False,
            False,
            "联合发射公式的第一生产性字段是 pre-Cauchy joint declaration，而不是后验表或反推表。",
            JOINT_DECL,
        ),
        row(
            "DeclarationConstructorSyncImported",
            declaration.get("joint_declaration_constructor_sync_router_closed") is True
            and declaration.get("target_input_before_router") == JOINT_DECL
            and declaration.get("next_direct_attack_target") == EXPLICIT_RULE,
            False,
            "joint declaration 仍只是入口声明；下一真正单点是显式 joint alpha/delta primitive constructor rule。",
            EXPLICIT_RULE,
        ),
        row(
            "AntiSplitBoundaryCarried",
            antisplit.get("old_split_formula_route_is_nonproof_cycle") is True
            and antisplit.get("next_direct_attack_target") == NON_SPLIT_ATOM,
            True,
            "显式 constructor 不能退回旧 split alpha/delta 路线；它必须携带同排 word/coefficient 的 anti-split 约束。",
            NON_SPLIT_ATOM,
        ),
        row(
            "ExplicitJointConstructorRuleCurrentCorpusProved",
            False,
            False,
            "当前材料尚未写出从 actual noncanonical source tuple 到 joint primitive row 的显式 alpha/delta 规则。",
            EXPLICIT_RULE,
        ),
        row(
            "JointConstructorFieldBasisCurrentCorpusProved",
            False,
            False,
            "同源定义域、行输出、pre-Cauchy 时间戳、no-leak 与失败回流标签尚未合取闭合。",
            productive_constructor_basis(),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只是把 latest triad 同步到已登记 constructor 硬点，不是三目标命题无条件闭合。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    latest = load_json(LATEST_TRIAD)
    strict_unified = load_json(STRICT_UNIFIED)
    seed_cycle = load_json(SEED_CYCLE)
    pdec = load_json(PDEC_SCOPE_FRONTIER)
    antisplit = load_json(STRICT_NEW_JOINT_ANTISPLIT)
    joint_field = load_json(JOINT_FIELD_ATOM)
    declaration = load_json(JOINT_DECL_CONSTRUCTOR)
    rows = build_rows(
        latest=latest,
        strict_unified=strict_unified,
        seed_cycle=seed_cycle,
        pdec=pdec,
        antisplit=antisplit,
        joint_field=joint_field,
        declaration=declaration,
    )
    retained_basis = (
        f"(({productive_constructor_basis()}) OR {NON_SPLIT_ATOM} OR {TERMINAL_DESCENT} "
        f"OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI} "
        f"OR ({SIGNED_SURVIVAL} AND {ROW_MASS})) AND {COMPLETE_KEY} AND {FIXED_KEY_MULT} "
        f"AND {EXACTUV_INC} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_triad_constructor_sync_router",
        "status": "phi_lpf_latest_new_joint_triad_synced_to_explicit_constructor_rule_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "latest_triad_imported": rows[0]["closed"],
        "seed_cycle_cut_saturation_imported": rows[1]["closed"],
        "pdec_scope_internal_saturation_imported": rows[2]["closed"],
        "strict_unified_declaration_line_imported": rows[3]["closed"],
        "joint_emitter_field_atom_imported": rows[4]["closed"],
        "declaration_constructor_sync_imported": rows[5]["closed"],
        "antisplit_boundary_carried": rows[6]["closed"],
        "seed_cycle_cut_input_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "pre_cauchy_joint_declaration_line_proved": False,
        "explicit_joint_alpha_delta_constructor_rule_proved": False,
        "joint_constructor_field_basis_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": TRIAD,
        "intermediate_primary_attack_target": JOINT_DECL,
        "absorbed_to": EXPLICIT_RULE,
        "next_primary_attack_target": EXPLICIT_RULE,
        "productive_constructor_basis": productive_constructor_basis(),
        "joint_declaration_basis": joint_declaration_basis(),
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest 三破环口接到 strict cycle-cut/PDEC/new-joint 统一下游：cycle-cut "
            "已饱和到 PDEC 或 new-joint，same-set PDEC 内部分支再饱和到 new-joint，"
            "new-joint 的内部第一生产性字段是 joint declaration line。已有 declaration/constructor "
            f"同步继续把首攻压到 `{EXPLICIT_RULE}`。这不是显式公式证明；同源定义域、"
            "word/coefficient 同排行输出、pre-Cauchy 时间戳、no-leak、失败回流、ExactUV、"
            "模型、Rate 与 DStructure 仍开放，行/列命题未无条件闭合。"
        ),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF latest new-joint triad constructor sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
    ]
    for key in [
        "latest_triad_imported",
        "seed_cycle_cut_saturation_imported",
        "pdec_scope_internal_saturation_imported",
        "strict_unified_declaration_line_imported",
        "joint_emitter_field_atom_imported",
        "declaration_constructor_sync_imported",
        "antisplit_boundary_carried",
        "explicit_joint_alpha_delta_constructor_rule_proved",
        "joint_constructor_field_basis_proved",
        "row_column_unconditional_closed",
        "next_primary_attack_target",
    ]:
        lines.append(f"{key}={cert[key] if not isinstance(cert[key], bool) else fmt_bool(cert[key])}")
    lines.extend(
        [
            "```",
            "",
            "## 1. 同步链",
            "",
            "| from | to | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for edge in cert["sync_chain"]:
        lines.append(f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for gate in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(gate["gate"]),
                closed=fmt_bool(gate["closed"]),
                proved=fmt_bool(gate["proved"]),
                meaning=cell(gate["meaning"]),
                remaining=cell(gate["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一真正单点",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "完整 constructor 字段基：",
            "",
            "```text",
            cert["productive_constructor_basis"],
            "```",
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 ledger、JSON 与 Markdown。"""
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
