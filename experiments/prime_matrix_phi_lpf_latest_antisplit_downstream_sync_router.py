#!/usr/bin/env python3
"""生成 Phi-LPF latest 反分裂下游同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_antisplit_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-antisplit-downstream-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-antisplit-downstream-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-antisplit-downstream-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-antisplit-downstream-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-antisplit-downstream-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CYCLECUT = DOCS / "prime-matrix-phi-lpf-latest-cyclecut-terminal-unified-sync-router.json"
STRICT_ANTISPLIT_DOWNSTREAM = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
JOINT_DECL_SYNC = DOCS / "prime-matrix-strict-joint-declaration-constructor-sync-router.json"
EXPLICIT_JOINT = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
ANTISPLIT_FIREWALL = DOCS / "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"
ATOMIC_ROWS = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
EXACTUV_ENTROPY = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"

JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
EXPLICIT_JOINT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
ATOMIC_ANTISPLIT = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
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
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_CYCLECUT,
        STRICT_ANTISPLIT_DOWNSTREAM,
        JOINT_DECL_SYNC,
        EXPLICIT_JOINT,
        ANTISPLIT_FIREWALL,
        ATOMIC_ROWS,
        EXACTUV_ENTROPY,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_edges(strict_downstream: dict[str, Any]) -> list[dict[str, str]]:
    """导入 strict 下游同步边。"""
    edges = strict_downstream.get("sync_edges", [])
    if edges:
        return edges
    return [
        {
            "from": JOINT_DECL,
            "to": EXPLICIT_JOINT_RULE,
            "meaning": "strict antisplit downstream 证书缺失时不能视为已同步。",
        }
    ]


def build_rows(
    latest_cyclecut: dict[str, Any],
    strict_downstream: dict[str, Any],
    joint_decl: dict[str, Any],
    explicit_joint: dict[str, Any],
    antisplit: dict[str, Any],
    atomic_rows: dict[str, Any],
    exactuv_entropy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest 反分裂下游同步判定表。"""
    latest_imported = latest_cyclecut.get("next_primary_attack_target") == JOINT_DECL
    strict_imported = strict_downstream.get("next_direct_attack_target") == BUILTIN_PAIRING
    ordinary_decl_synced = joint_decl.get("next_direct_attack_target") == EXPLICIT_JOINT_RULE
    ordinary_constructor_fixed = (
        explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True
    )
    antisplit_imported = antisplit.get("next_direct_attack_target") == ATOMIC_ANTISPLIT
    atomic_imported = atomic_rows.get("next_direct_attack_target") == BUILTIN_PAIRING
    exactuv_split = exactuv_entropy.get("next_direct_attack_target") == f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
    return [
        row(
            "LatestJointDeclarationImported",
            latest_imported,
            False,
            "latest cycle-cut/terminal 同步已把内部第一生产性单点压成 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "StrictAntiSplitDownstreamImported",
            strict_imported,
            True,
            "strict 反分裂下游证书已把普通 joint declaration 路线同步到 built-in signed pairing 与 ExactUV 并行门。",
            BUILTIN_PAIRING,
        ),
        row(
            "OrdinaryJointDeclarationSyncedToConstructor",
            ordinary_decl_synced,
            False,
            "普通 joint declaration 与 actual constructor 线同步，首个普通生产性字段是 explicit joint constructor rule。",
            EXPLICIT_JOINT_RULE,
        ),
        row(
            "OrdinaryConstructorRouteRejectedAsFixedPoint",
            ordinary_constructor_fixed
            and strict_downstream.get("ordinary_joint_declaration_route_rejected_as_nonproof") is True,
            True,
            "普通 explicit constructor 展开会回到 signed-source 固定点，不能作为非循环证明。",
            ATOMIC_ANTISPLIT,
        ),
        row(
            "AntiSplitAtomicRouteImported",
            antisplit_imported and strict_downstream.get("antisplit_atomic_route_imported") is True,
            False,
            "若要破固定点，declaration 必须走内置 rows、word/coefficient pairing 与 split firewall 的 atomic rows 路线。",
            ATOMIC_ANTISPLIT,
        ),
        row(
            "AtomicRowsReducedToBuiltInPairing",
            atomic_imported and strict_downstream.get("atomic_rows_reduced_to_builtin_pairing") is True,
            False,
            "atomic joint rows 的 signed 首缺口是每条 row 的 built-in signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberSplitImported",
            exactuv_split and strict_downstream.get("exactuv_entropy_fiber_split_imported") is True,
            False,
            "ExactUV 并行门已拆成 actual source-domain entropy 与 fixed exact-pair polylog fiber bound。",
            f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        ),
        row(
            "BuiltInPairingCurrentCorpusProved",
            False,
            False,
            "当前语料没有给出每条 atomic joint row 的 signed coefficient 闭式值及 word/coefficient 同源证明。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberCurrentCorpusProved",
            False,
            False,
            "source entropy 与 fixed exact-pair fiber bound 仍不能由 built-in pairing 自动推出。",
            f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        ),
        row(
            "ExternalAndTerminalAlternativesRetained",
            True,
            False,
            "canonical-lock、independent bridge、same-set PDEC 与外部谱仍是独立保留输入。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 latest joint declaration 接到反分裂下游；未证明 built-in pairing、ExactUV entropy/fiber 或全局晋级门。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 latest 反分裂下游同步证书。"""
    latest_cyclecut = load_json(LATEST_CYCLECUT)
    strict_downstream = load_json(STRICT_ANTISPLIT_DOWNSTREAM)
    joint_decl = load_json(JOINT_DECL_SYNC)
    explicit_joint = load_json(EXPLICIT_JOINT)
    antisplit = load_json(ANTISPLIT_FIREWALL)
    atomic_rows = load_json(ATOMIC_ROWS)
    exactuv_entropy = load_json(EXACTUV_ENTROPY)
    rows = build_rows(
        latest_cyclecut,
        strict_downstream,
        joint_decl,
        explicit_joint,
        antisplit,
        atomic_rows,
        exactuv_entropy,
    )
    internal_basis = f"{BUILTIN_PAIRING} AND {SOURCE_ENTROPY} AND {FIXED_FIBER}"
    retained_basis = (
        f"(({internal_basis}) OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} "
        f"OR {EXTERNAL_DIBFI}) AND {COMPLETE_KEY} AND {FIXED_KEY_MULT} AND {MODEL} "
        f"AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_antisplit_downstream_sync_router",
        "status": "phi_lpf_latest_joint_declaration_synced_to_builtin_pairing_and_exactuv_entropy_fiber_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_joint_declaration_imported": rows[0]["closed"],
        "strict_antisplit_downstream_imported": rows[1]["closed"],
        "ordinary_joint_declaration_synced_to_constructor": rows[2]["closed"],
        "ordinary_constructor_route_rejected_as_fixed_point": rows[3]["closed"],
        "antisplit_atomic_route_imported": rows[4]["closed"],
        "atomic_rows_reduced_to_builtin_pairing": rows[5]["closed"],
        "exactuv_entropy_fiber_split_imported": rows[6]["closed"],
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": JOINT_DECL,
        "absorbed_to": BUILTIN_PAIRING,
        "next_primary_attack_target": BUILTIN_PAIRING,
        "parallel_primary_attack_target": f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        "latest_internal_downstream_basis": internal_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_edges": sync_edges(strict_downstream),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest `PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple` "
            "接到 strict 反分裂下游。普通 joint declaration 会降到 explicit constructor，而普通 constructor "
            "已回到 signed-source 固定点；因此非循环自足路线必须走 atomic rows 反分裂，并进一步压到 "
            f"`{BUILTIN_PAIRING}`。并行 ExactUV 门为 `{SOURCE_ENTROPY} AND {FIXED_FIBER}`。"
            "built-in pairing、ExactUV entropy/fiber、canonical-lock、independent bridge、PDEC/外部谱、"
            "complete/fixed-key、模型、Rate 与 DStructure 仍开放，行/列命题未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix Phi-LPF latest antisplit downstream sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_joint_declaration_imported={fmt_bool(cert['latest_joint_declaration_imported'])}",
        f"strict_antisplit_downstream_imported={fmt_bool(cert['strict_antisplit_downstream_imported'])}",
        f"ordinary_joint_declaration_synced_to_constructor={fmt_bool(cert['ordinary_joint_declaration_synced_to_constructor'])}",
        f"ordinary_constructor_route_rejected_as_fixed_point={fmt_bool(cert['ordinary_constructor_route_rejected_as_fixed_point'])}",
        f"antisplit_atomic_route_imported={fmt_bool(cert['antisplit_atomic_route_imported'])}",
        f"atomic_rows_reduced_to_builtin_pairing={fmt_bool(cert['atomic_rows_reduced_to_builtin_pairing'])}",
        f"exactuv_entropy_fiber_split_imported={fmt_bool(cert['exactuv_entropy_fiber_split_imported'])}",
        f"built_in_signed_pairing_proved={fmt_bool(cert['built_in_signed_pairing_proved'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(cert['actual_emitter_source_domain_entropy_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(cert['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"parallel_primary_attack_target={cert['parallel_primary_attack_target']}",
        "```",
        "",
        "## 1. 下游同步边",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_edges"]:
        lines.append(
            f"| `{cell(item.get('from', ''))}` | `{cell(item.get('to', ''))}` | "
            f"{cell(item.get('meaning', ''))} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新内部下游基",
            "",
            "```text",
            cert["latest_internal_downstream_basis"],
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
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
