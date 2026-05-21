#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor joint declaration 到 anti-split/builtin pairing 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_joint_declaration_antisplit_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_JOINT_DECL = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json"
STRICT_DOWNSTREAM = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
JOINT_DECL_SYNC = DOCS / "prime-matrix-strict-joint-declaration-constructor-sync-router.json"
EXPLICIT_JOINT = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
ANTISPLIT = DOCS / "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"
ATOMIC_ROWS = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
SOURCE_DOWNSTREAM = DOCS / "prime-matrix-strict-source-declaration-downstream-sync-router.json"
EXACTUV_ENTROPY = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"

JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
EXPLICIT_JOINT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
ATOMIC_ANTISPLIT = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
EXACTUV_PAIR = f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
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


def dependency_paths() -> list[Path]:
    """列出本层依赖。"""
    return [
        CURRENT_JOINT_DECL,
        STRICT_DOWNSTREAM,
        JOINT_DECL_SYNC,
        EXPLICIT_JOINT,
        ANTISPLIT,
        ATOMIC_ROWS,
        SOURCE_DOWNSTREAM,
        EXACTUV_ENTROPY,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """给出 joint declaration 下游同步链。"""
    return [
        {
            "from": JOINT_DECL,
            "to": EXPLICIT_JOINT_RULE,
            "meaning": "普通 joint declaration 同步到显式 joint alpha/delta constructor rule。",
        },
        {
            "from": EXPLICIT_JOINT_RULE,
            "to": "signed-source fixed point unless anti-split route is supplied",
            "meaning": "普通 constructor 展开回到 signed-source 固定点，不能作为非循环证明。",
        },
        {
            "from": "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection",
            "to": ATOMIC_ANTISPLIT,
            "meaning": "要避开普通固定点，声明行必须内置 atomic rows 与 word/coefficient pairing。",
        },
        {
            "from": ATOMIC_ANTISPLIT,
            "to": BUILTIN_PAIRING,
            "meaning": "atomic joint rows 的首个 signed 缺口是每条 row 的 built-in coefficient/pairing 闭式。",
        },
        {
            "from": "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem",
            "to": EXACTUV_PAIR,
            "meaning": "ExactUV incidence 并行拆成 actual source entropy 与 fixed-pair polylog fiber bound。",
        },
    ]


def build_rows(
    current: dict[str, Any],
    strict_downstream: dict[str, Any],
    joint_decl: dict[str, Any],
    explicit_joint: dict[str, Any],
    antisplit: dict[str, Any],
    atomic_rows: dict[str, Any],
    source_downstream: dict[str, Any],
    exactuv_entropy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "CurrentConstructorJointDeclarationImported",
            current.get("next_primary_attack_target") == JOINT_DECL
            and current.get("pre_cauchy_joint_declaration_line_proved") is False,
            False,
            "当前 constructor triad-unified 层已把直接主攻压到 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "StrictAntisplitDownstreamImported",
            strict_downstream.get("next_direct_attack_target") == BUILTIN_PAIRING
            and strict_downstream.get("antisplit_atomic_route_imported") is True
            and strict_downstream.get("atomic_rows_reduced_to_builtin_pairing") is True,
            False,
            "既有 strict 下游同步已把 joint declaration 的非循环路线压到 anti-split atomic rows 与 built-in pairing。",
            BUILTIN_PAIRING,
        ),
        row(
            "OrdinaryJointDeclarationSyncedToConstructorRule",
            joint_decl.get("target_input_before_router") == JOINT_DECL
            and joint_decl.get("next_direct_attack_target") == EXPLICIT_JOINT_RULE,
            False,
            "普通 joint declaration 只同步到显式 constructor rule，不是独立闭合。",
            EXPLICIT_JOINT_RULE,
        ),
        row(
            "OrdinaryConstructorRouteRejectedAsFixedPoint",
            explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True,
            True,
            "显式 constructor 普通展开经 alpha-side/same-row/row-level 回到 signed-source 固定点。",
            ATOMIC_ANTISPLIT,
        ),
        row(
            "AntiSplitFirewallImported",
            antisplit.get("next_direct_attack_target") == ATOMIC_ANTISPLIT
            and antisplit.get("ordinary_joint_declaration_route_is_nonproof_cycle") is True,
            False,
            "anti-split firewall 要求声明行内置 atomic rows、word/coefficient 同源和 split firewall。",
            ATOMIC_ANTISPLIT,
        ),
        row(
            "AtomicRowsReducedToBuiltinPairing",
            atomic_rows.get("next_direct_attack_target") == BUILTIN_PAIRING
            and source_downstream.get("next_direct_attack_target") == BUILTIN_PAIRING,
            False,
            "atomic joint rows 的 signed 首缺口已同步为 built-in signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberSplitImported",
            exactuv_entropy.get("next_direct_attack_target") == EXACTUV_PAIR
            and exactuv_entropy.get("actual_emitter_source_domain_entropy_proved") is False
            and exactuv_entropy.get("exact_uv_map_fixed_pair_polylog_fiber_bound_proved") is False,
            False,
            "built-in pairing 不支付 ExactUV；source-domain entropy 与 fixed-pair fiber bound 仍是并行门。",
            EXACTUV_PAIR,
        ),
        row(
            "BuiltInPairingCurrentCorpusProved",
            False,
            False,
            "当前语料没有每条 atomic joint row 的 signed coefficient 闭式值及 word/coefficient 同源证明。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberCurrentCorpusProved",
            False,
            False,
            "当前语料没有 actual source-domain entropy 与 fixed exact-pair polylog fiber bound 的合取证明。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只完成 constructor joint declaration 到 anti-split/builtin pairing 的同步，不是三目标命题无条件闭合。",
            f"{BUILTIN_PAIRING} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    current = load_json(CURRENT_JOINT_DECL)
    strict_downstream = load_json(STRICT_DOWNSTREAM)
    joint_decl = load_json(JOINT_DECL_SYNC)
    explicit_joint = load_json(EXPLICIT_JOINT)
    antisplit = load_json(ANTISPLIT)
    atomic_rows = load_json(ATOMIC_ROWS)
    source_downstream = load_json(SOURCE_DOWNSTREAM)
    exactuv_entropy = load_json(EXACTUV_ENTROPY)
    rows = build_rows(
        current=current,
        strict_downstream=strict_downstream,
        joint_decl=joint_decl,
        explicit_joint=explicit_joint,
        antisplit=antisplit,
        atomic_rows=atomic_rows,
        source_downstream=source_downstream,
        exactuv_entropy=exactuv_entropy,
    )
    internal_basis = f"{BUILTIN_PAIRING} AND {SOURCE_ENTROPY} AND {FIXED_FIBER}"
    retained_basis = (
        f"(({internal_basis}) OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR "
        f"{PDEC_SCOPE} OR {EXTERNAL_DIBFI}) AND {SIGNED_SURVIVAL} AND {ROW_MASS} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_joint_declaration_antisplit_sync_router",
        "status": "phi_lpf_latest_constructor_joint_declaration_synced_to_builtin_pairing_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "current_constructor_joint_declaration_imported": rows[0]["closed"],
        "strict_antisplit_downstream_imported": rows[1]["closed"],
        "ordinary_joint_declaration_synced_to_constructor_rule": rows[2]["closed"],
        "ordinary_constructor_route_rejected_as_fixed_point": rows[3]["closed"],
        "antisplit_firewall_imported": rows[4]["closed"],
        "atomic_rows_reduced_to_builtin_pairing": rows[5]["closed"],
        "exactuv_entropy_fiber_split_imported": rows[6]["closed"],
        "pre_cauchy_joint_declaration_line_proved": False,
        "atomic_antisplit_declaration_proved": False,
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": JOINT_DECL,
        "absorbed_to": BUILTIN_PAIRING,
        "next_primary_attack_target": BUILTIN_PAIRING,
        "parallel_primary_attack_targets": [
            SOURCE_ENTROPY,
            FIXED_FIBER,
            CANONICAL_LOCK,
            INDEPENDENT_BRIDGE,
            PDEC_SCOPE,
            EXTERNAL_DIBFI,
            SIGNED_SURVIVAL,
            ROW_MASS,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把 current constructor 的 `{JOINT_DECL}` 接到 anti-split 下游。"
            f"普通 declaration 只同步到 `{EXPLICIT_JOINT_RULE}`，继续展开会回到 signed-source 固定点；"
            f"非循环路线必须给 `{ATOMIC_ANTISPLIT}`，其首个 signed 缺口压到 `{BUILTIN_PAIRING}`。"
            f"`{SOURCE_ENTROPY}` 与 `{FIXED_FIBER}` 仍是并行 ExactUV 门；canonical lock、"
            "independent bridge、PDEC/外部谱、signed survival、row-mass、模型、Rate 与 DStructure "
            "仍开放。行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor joint-declaration antisplit sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"current_constructor_joint_declaration_imported={fmt_bool(cert['current_constructor_joint_declaration_imported'])}",
        f"strict_antisplit_downstream_imported={fmt_bool(cert['strict_antisplit_downstream_imported'])}",
        f"ordinary_joint_declaration_synced_to_constructor_rule={fmt_bool(cert['ordinary_joint_declaration_synced_to_constructor_rule'])}",
        f"ordinary_constructor_route_rejected_as_fixed_point={fmt_bool(cert['ordinary_constructor_route_rejected_as_fixed_point'])}",
        f"antisplit_firewall_imported={fmt_bool(cert['antisplit_firewall_imported'])}",
        f"atomic_rows_reduced_to_builtin_pairing={fmt_bool(cert['atomic_rows_reduced_to_builtin_pairing'])}",
        f"exactuv_entropy_fiber_split_imported={fmt_bool(cert['exactuv_entropy_fiber_split_imported'])}",
        f"pre_cauchy_joint_declaration_line_proved={fmt_bool(cert['pre_cauchy_joint_declaration_line_proved'])}",
        f"atomic_antisplit_declaration_proved={fmt_bool(cert['atomic_antisplit_declaration_proved'])}",
        f"built_in_signed_pairing_proved={fmt_bool(cert['built_in_signed_pairing_proved'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(cert['actual_emitter_source_domain_entropy_proved'])}",
        (
            "exact_uv_map_fixed_pair_polylog_fiber_bound_proved="
            f"{fmt_bool(cert['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in cert["gates"]:
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
            "## 3. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "## 4. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    cert = build_certificate()
    print(json.dumps(cert, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
