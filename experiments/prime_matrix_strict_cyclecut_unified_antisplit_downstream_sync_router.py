#!/usr/bin/env python3
"""生成 cycle-cut 统一前沿到反分裂 atomic rows 的下游同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_cyclecut_unified_antisplit_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json

输出：
  data/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-ledger.json
  docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json
  docs/monograph/prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.md"

UNIFIED = DOCS / "prime-matrix-strict-cyclecut-terminal-descent-unified-frontier-router.json"
JOINT_DECL = DOCS / "prime-matrix-strict-joint-declaration-constructor-sync-router.json"
EXPLICIT_JOINT = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
ANTISPLIT = DOCS / "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"
ATOMIC_ROWS = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
SOURCE_DOWNSTREAM = DOCS / "prime-matrix-strict-source-declaration-downstream-sync-router.json"
EXACTUV_ENTROPY = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"

PRECAUCHY_JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
EXPLICIT_JOINT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
ATOMIC_ANTISPLIT = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，避免把缺失误作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        UNIFIED,
        JOINT_DECL,
        EXPLICIT_JOINT,
        ANTISPLIT,
        ATOMIC_ROWS,
        SOURCE_DOWNSTREAM,
        EXACTUV_ENTROPY,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_edges() -> list[dict[str, str]]:
    """列出本次下游同步边。"""
    return [
        {
            "from": PRECAUCHY_JOINT_DECL,
            "to": EXPLICIT_JOINT_RULE,
            "meaning": "普通 joint declaration 与 actual constructor 线同步后，生产性内容是显式 joint alpha/delta rule。",
        },
        {
            "from": EXPLICIT_JOINT_RULE,
            "to": "signed-source fixed point unless replaced",
            "meaning": "显式 joint constructor 的普通展开经 alpha-side/same-row/row-level 回到 signed-source 固定点。",
        },
        {
            "from": "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection",
            "to": ATOMIC_ANTISPLIT,
            "meaning": "要避免普通分裂固定点，声明行必须内置 rows、word/coefficient pairing 与 prepushforward identity。",
        },
        {
            "from": ATOMIC_ANTISPLIT,
            "to": BUILTIN_PAIRING,
            "meaning": "atomic rows 的首个 signed 缺口是每条 row 的内置 signed coefficient/pairing 闭式。",
        },
        {
            "from": "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem",
            "to": f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
            "meaning": "ExactUV 并行门已拆成 actual source-domain entropy 与 fixed exact-pair polylog fiber bound。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """合并已有证书读数。"""
    unified = data["unified"]
    joint_decl = data["joint_decl"]
    explicit_joint = data["explicit_joint"]
    antisplit = data["antisplit"]
    atomic_rows = data["atomic_rows"]
    source_downstream = data["source_downstream"]
    exactuv_entropy = data["exactuv_entropy"]

    unified_target = unified.get("next_direct_attack_target") == PRECAUCHY_JOINT_DECL
    ordinary_decl_synced = joint_decl.get("next_direct_attack_target") == EXPLICIT_JOINT_RULE
    ordinary_fixed = explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True
    antisplit_target = antisplit.get("next_direct_attack_target") == ATOMIC_ANTISPLIT
    atomic_target = atomic_rows.get("next_direct_attack_target") == BUILTIN_PAIRING
    downstream_pairing = source_downstream.get("next_direct_attack_target") == BUILTIN_PAIRING
    exactuv_split = exactuv_entropy.get("next_direct_attack_target") == f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"

    return [
        row(
            "UnifiedFrontierImported",
            unified_target,
            False,
            "上一轮统一前沿把 strict 内部第一普通生产性字段压成 pre-Cauchy joint declaration line。",
            PRECAUCHY_JOINT_DECL,
        ),
        row(
            "OrdinaryJointDeclarationSyncedToConstructorRule",
            ordinary_decl_synced,
            False,
            "普通 joint declaration 不是新来源类；它同步到 explicit joint alpha/delta constructor rule。",
            EXPLICIT_JOINT_RULE,
        ),
        row(
            "OrdinaryConstructorRouteIsFixedPoint",
            ordinary_fixed,
            True,
            "沿普通 explicit constructor 继续展开会回到 signed-source 固定点，不能作为非循环证明。",
            ATOMIC_ANTISPLIT,
        ),
        row(
            "AntiSplitFirewallImported",
            antisplit_target,
            False,
            "真正反分裂出口要求 atomic declaration 本身内置 rows formula、word/coefficient 同源和 split firewall。",
            ATOMIC_ANTISPLIT,
        ),
        row(
            "AtomicRowsReducedToBuiltinPairing",
            atomic_target and downstream_pairing,
            False,
            "atomic joint rows 的未闭合 signed 首缺口已压成 built-in signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberSplitImported",
            exactuv_split,
            False,
            "ExactUV bounded incidence 不能由 built-in pairing 自动给出，仍需 source entropy 与 fixed-pair fiber bound。",
            f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        ),
        row(
            "BuiltInPairingCurrentCorpusProved",
            False,
            False,
            "当前材料没有每条 atomic joint row 的 signed coefficient 闭式值及 word/coefficient 同源证明。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberCurrentCorpusProved",
            False,
            False,
            "当前材料没有证明 actual source-domain entropy 与 fixed exact-pair polylog fiber bound 的合取。",
            f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        ),
        row(
            "ExternalAndPDECAlternativesRetained",
            True,
            False,
            "canonical-lock、independent bridge、PDEC same-set 与外部谱仍可作为独立输入保留。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步下游前沿；没有证明 built-in pairing、ExactUV entropy/fiber 或全局晋级门。",
            "row/column theorem still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "unified": load_json(UNIFIED),
        "joint_decl": load_json(JOINT_DECL),
        "explicit_joint": load_json(EXPLICIT_JOINT),
        "antisplit": load_json(ANTISPLIT),
        "atomic_rows": load_json(ATOMIC_ROWS),
        "source_downstream": load_json(SOURCE_DOWNSTREAM),
        "exactuv_entropy": load_json(EXACTUV_ENTROPY),
    }
    rows = build_rows(data)
    internal_basis = f"{BUILTIN_PAIRING} AND {SOURCE_ENTROPY} AND {FIXED_FIBER}"
    retained_basis = (
        f"(({internal_basis}) OR {CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) "
        f"AND {COMPLETE_KEY} AND {FIXED_KEY} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    result = {
        "certificate_type": "prime_matrix_strict_cyclecut_unified_antisplit_downstream_sync_router",
        "status": "cyclecut_unified_frontier_synced_to_builtin_pairing_and_exactuv_entropy_fiber_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "ordinary_joint_declaration_route_rejected_as_nonproof": rows[2]["closed"],
        "antisplit_atomic_route_imported": rows[3]["closed"],
        "atomic_rows_reduced_to_builtin_pairing": rows[4]["closed"],
        "exactuv_entropy_fiber_split_imported": rows[5]["closed"],
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": BUILTIN_PAIRING,
        "parallel_direct_attack_target": f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        "strict_internal_downstream_basis": internal_basis,
        "unified_retained_remaining_basis": retained_basis,
        "sync_edges": sync_edges(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把上一轮的 pre-Cauchy joint declaration line 继续沿既有下游证书同步："
            "普通 declaration 会降到 explicit joint constructor，而普通 constructor 已回到 signed-source 固定点；"
            "因此真正内部自足路线必须走反分裂 atomic rows，并进一步压到 "
            "`BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`。ExactUV 并行门同步为 "
            "`ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger`。"
            "这些输入当前均未证明，行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict cycle-cut 统一前沿反分裂下游同步",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"ordinary_joint_declaration_route_rejected_as_nonproof={fmt_bool(result['ordinary_joint_declaration_route_rejected_as_nonproof'])}",
        f"antisplit_atomic_route_imported={fmt_bool(result['antisplit_atomic_route_imported'])}",
        f"atomic_rows_reduced_to_builtin_pairing={fmt_bool(result['atomic_rows_reduced_to_builtin_pairing'])}",
        f"exactuv_entropy_fiber_split_imported={fmt_bool(result['exactuv_entropy_fiber_split_imported'])}",
        f"built_in_signed_pairing_proved={fmt_bool(result['built_in_signed_pairing_proved'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(result['actual_emitter_source_domain_entropy_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        f"parallel_direct_attack_target={result['parallel_direct_attack_target']}",
        "```",
        "",
        "## 1. 下游同步边",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_edges"]:
        lines.append(
            "| "
            + " | ".join([f"`{cell(item['from'])}`", f"`{cell(item['to'])}`", cell(item["meaning"])])
            + " |"
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
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(item['gate'])}`",
                    fmt_bool(item["closed"]),
                    fmt_bool(item["proved"]),
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新内部下游基",
            "",
            "```text",
            result["strict_internal_downstream_basis"],
            "```",
            "",
            "## 4. 统一保留剩余基",
            "",
            "```text",
            result["unified_retained_remaining_basis"],
            "```",
            "",
            "## 5. 结论边界",
            "",
            "- 本文件是下游同步，不是行/列命题证明。",
            "- 普通 joint declaration / ordinary constructor 路线已经被登记为固定点，不能作为闭合证明。",
            "- 真正直接主攻变成 built-in signed pairing；ExactUV entropy/fiber 是并行硬点。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(name)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
