#!/usr/bin/env python3
"""生成 Phi-LPF latest new-joint 反分裂原子到 built-in pairing 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_antisplit_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-antisplit-downstream-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_ANTISPLIT = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-router.json"
)
STRICT_DOWNSTREAM = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
ANTISPLIT_FIREWALL = DOCS / "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"
ATOMIC_ROWS = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
EXACTUV_ENTROPY = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"

NON_SPLIT = "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection"
ATOMIC_ROWS_TARGET = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
ACTUAL_EXACTUV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失依赖不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写成小写文本。"""
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


def dependency_paths() -> list[Path]:
    """返回本层依赖证书。"""
    return [
        LATEST_ANTISPLIT,
        STRICT_DOWNSTREAM,
        ANTISPLIT_FIREWALL,
        ATOMIC_ROWS,
        EXACTUV_ENTROPY,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def downstream_edges_cover(strict_downstream: dict[str, Any]) -> bool:
    """检查 strict 下游证书是否覆盖反分裂原子的必要边。"""
    edges = strict_downstream.get("sync_edges", [])
    checks = [
        (NON_SPLIT, ATOMIC_ROWS_TARGET),
        (ATOMIC_ROWS_TARGET, BUILTIN_PAIRING),
        (ACTUAL_EXACTUV, f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"),
    ]
    return all(
        any(edge.get("from") == source and edge.get("to") == target for edge in edges)
        for source, target in checks
    )


def sync_edges() -> list[dict[str, str]]:
    """返回本层同步边。"""
    return [
        {
            "from": NON_SPLIT,
            "to": ATOMIC_ROWS_TARGET,
            "meaning": "反分裂同排行必须内置 rows formula、word/coefficient pairing、prepushforward identity 与 split firewall。",
        },
        {
            "from": ATOMIC_ROWS_TARGET,
            "to": BUILTIN_PAIRING,
            "meaning": "atomic rows 的 signed 首缺口是每行内置 coefficient/pairing 闭式。",
        },
        {
            "from": ACTUAL_EXACTUV,
            "to": f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
            "meaning": "bounded ExactUV incidence 拆成 source-domain entropy 与 fixed exact-pair fiber bound。",
        },
        {
            "from": "retained alternatives",
            "to": f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}",
            "meaning": "canonical-lock、independent bridge、same-set PDEC 与外部谱仍是独立保留输入。",
        },
    ]


def latest_internal_basis() -> str:
    """返回最新严格内部主攻基。"""
    return (
        f"{BUILTIN_PAIRING} AND {SOURCE_ENTROPY} AND {FIXED_FIBER} AND {COMPLETE_KEY} "
        f"AND {FIXED_KEY} AND {SIGNED_ROW_LAW} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )


def retained_basis() -> str:
    """返回带保留替代输入的总基。"""
    alternatives = f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}"
    return f"(({BUILTIN_PAIRING} AND {SOURCE_ENTROPY} AND {FIXED_FIBER}) OR {alternatives}) AND {COMPLETE_KEY} AND {FIXED_KEY} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    latest = deps["latest"]
    downstream = deps["downstream"]
    firewall = deps["firewall"]
    atomic = deps["atomic"]
    exactuv = deps["exactuv"]
    exactuv_split = f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
    return [
        row(
            "LatestAntiSplitAtomImported",
            latest.get("next_primary_attack_target") == NON_SPLIT
            and latest.get("known_antisplit_downstream_available") is True,
            False,
            "上一层 latest new-joint 同步已经把主攻压到反分裂同排原子，并确认有 strict 下游可继续追击。",
            NON_SPLIT,
        ),
        row(
            "StrictAntiSplitDownstreamEdgesImported",
            downstream_edges_cover(downstream),
            True,
            "strict 下游同步边覆盖 NonSplit -> atomic rows -> built-in pairing，以及 ExactUV -> entropy/fiber。",
            f"{BUILTIN_PAIRING} AND {exactuv_split}",
        ),
        row(
            "AntiSplitFirewallToAtomicRowsImported",
            firewall.get("next_direct_attack_target") == ATOMIC_ROWS_TARGET
            and firewall.get("atomic_antisplit_declaration_proved") is False,
            False,
            "反分裂 firewall 表明普通 declaration 不够，必须提交 atomic pre-Cauchy rows 声明。",
            ATOMIC_ROWS_TARGET,
        ),
        row(
            "AtomicRowsReducedToBuiltInPairing",
            atomic.get("next_direct_attack_target") == BUILTIN_PAIRING
            and atomic.get("builtin_signed_coefficient_pairing_proved") is False,
            False,
            "atomic rows 的 row skeleton、防回退 firewall 已有；缺口集中到每行 built-in signed pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "SignedOriginTableLoopBlocked",
            atomic.get("signed_origin_table_loop_blocked") is True,
            True,
            "旧 signed-value/origin-table 路线被登记为回到 signed-source 固定点，不能替代 built-in pairing。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberSplitImported",
            exactuv.get("next_direct_attack_target") == exactuv_split,
            False,
            "ExactUV bounded multiplicity 已拆为 source-domain entropy 与 fixed-pair polylog fiber bound 两个账本。",
            exactuv_split,
        ),
        row(
            "BuiltInPairingCurrentCorpusProved",
            False,
            False,
            "当前语料没有每条 atomic joint row 的 signed coefficient 闭式值及 word/coefficient 同源证明。",
            BUILTIN_PAIRING,
        ),
        row(
            "EntropyFiberCurrentCorpusProved",
            False,
            False,
            "当前语料没有证明 actual source-domain entropy 与 fixed exact-pair polylog fiber bound 的合取。",
            exactuv_split,
        ),
        row(
            "ExternalAndTerminalAlternativesRetained",
            True,
            False,
            "canonical-lock、independent bridge、same-set PDEC 与外部谱仍作为独立输入保留。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}",
        ),
        row(
            "ModelRateDStructureStillParallel",
            True,
            False,
            "complete/fixed-key、模型余量、RatePreservation 与 DStructure/Rankin 仍未由 built-in pairing 自动推出。",
            f"{COMPLETE_KEY} AND {FIXED_KEY} AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只是把反分裂原子同步到 built-in pairing 与 ExactUV entropy/fiber；没有得到无条件闭合。",
            latest_internal_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    deps = {
        "latest": load_json(LATEST_ANTISPLIT),
        "downstream": load_json(STRICT_DOWNSTREAM),
        "firewall": load_json(ANTISPLIT_FIREWALL),
        "atomic": load_json(ATOMIC_ROWS),
        "exactuv": load_json(EXACTUV_ENTROPY),
    }
    rows = build_rows(deps)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_antisplit_downstream_sync_router",
        "status": "phi_lpf_latest_new_joint_antisplit_synced_to_builtin_pairing_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "frontier_sync_only": True,
        "missing_sources": missing_sources(),
        "latest_antisplit_atom_imported": rows[0]["closed"],
        "strict_antisplit_downstream_edges_imported": rows[1]["closed"],
        "antisplit_firewall_to_atomic_rows_imported": rows[2]["closed"],
        "atomic_rows_reduced_to_builtin_pairing": rows[3]["closed"],
        "signed_origin_table_loop_blocked": rows[4]["closed"],
        "exactuv_entropy_fiber_split_imported": rows[5]["closed"],
        "non_split_actual_joint_formula_proved": False,
        "atomic_antisplit_declaration_proved": False,
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "sync_edges": sync_edges(),
        "latest_internal_basis_after_sync": latest_internal_basis(),
        "latest_retained_basis_after_sync": retained_basis(),
        "next_primary_attack_target": BUILTIN_PAIRING,
        "parallel_primary_attack_target": f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        "retained_alternative_targets": [
            CANONICAL_LOCK,
            INDEPENDENT_BRIDGE,
            PDEC_SCOPE,
            EXTERNAL_SPECTRAL,
        ],
        "plain_conclusion": (
            "本步把 latest 反分裂原子 "
            "`NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection` 接入 strict 下游。"
            "反分裂同排行若要避免旧 split 固定点，必须升级为 "
            "`AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing`；"
            "而 atomic rows 的首个 signed 缺口是 "
            "`BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`。"
            "并行 ExactUV 门同步为 `ActualEmitterSourceDomainEntropyLedger AND "
            "ExactUVMapFixedPairPolylogFiberBoundLedger`。这些输入当前均未证明，"
            "complete/fixed-key、模型余量、Rate 与 DStructure 仍开放，行/列命题未无条件闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest new-joint antisplit downstream sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_antisplit_atom_imported={fmt_bool(result['latest_antisplit_atom_imported'])}",
        f"strict_antisplit_downstream_edges_imported={fmt_bool(result['strict_antisplit_downstream_edges_imported'])}",
        f"antisplit_firewall_to_atomic_rows_imported={fmt_bool(result['antisplit_firewall_to_atomic_rows_imported'])}",
        f"atomic_rows_reduced_to_builtin_pairing={fmt_bool(result['atomic_rows_reduced_to_builtin_pairing'])}",
        f"signed_origin_table_loop_blocked={fmt_bool(result['signed_origin_table_loop_blocked'])}",
        f"exactuv_entropy_fiber_split_imported={fmt_bool(result['exactuv_entropy_fiber_split_imported'])}",
        f"non_split_actual_joint_formula_proved={fmt_bool(result['non_split_actual_joint_formula_proved'])}",
        f"atomic_antisplit_declaration_proved={fmt_bool(result['atomic_antisplit_declaration_proved'])}",
        f"built_in_signed_pairing_proved={fmt_bool(result['built_in_signed_pairing_proved'])}",
        f"actual_emitter_source_domain_entropy_proved={fmt_bool(result['actual_emitter_source_domain_entropy_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        f"parallel_primary_attack_target={result['parallel_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步边",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_edges"]:
        lines.append(
            f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |"
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
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 3. 最新开放基",
            "",
            "严格内部基：",
            "",
            "```text",
            result["latest_internal_basis_after_sync"],
            "```",
            "",
            "带保留替代输入的基：",
            "",
            "```text",
            result["latest_retained_basis_after_sync"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            result["parallel_primary_attack_target"],
            "```",
            "",
            "## 4. 边界",
            "",
            "- 本层只同步反分裂下游，不证明 built-in pairing 或 ExactUV entropy/fiber。",
            "- LPF/Phi 桶恒等式仍不生成 signed coefficient。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 和 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_primary_attack_target={result['next_primary_attack_target']}")
    print(f"parallel_primary_attack_target={result['parallel_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
