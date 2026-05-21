#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor 到 anti-split/built-in pairing 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_antisplit_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-antisplit-downstream-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_CONSTRUCTOR = DOCS / "prime-matrix-phi-lpf-latest-new-joint-triad-constructor-sync-router.json"
STRICT_ANTISPLIT_DOWNSTREAM = DOCS / "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
EXPLICIT_DIRECT = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
SOURCE_DOWNSTREAM = DOCS / "prime-matrix-strict-source-declaration-downstream-sync-router.json"
ATOMIC_ROWS = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
EXACTUV_ENTROPY = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"

EXPLICIT_RULE = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
NON_SPLIT_ATOM = "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection"
ATOMIC_ROWS_FORMULA = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
EXACTUV_PAIR = f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
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
        LATEST_CONSTRUCTOR,
        STRICT_ANTISPLIT_DOWNSTREAM,
        EXPLICIT_DIRECT,
        SOURCE_DOWNSTREAM,
        ATOMIC_ROWS,
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
    """给出同步链。"""
    return [
        {
            "from": EXPLICIT_RULE,
            "to": "signed-source fixed point unless replaced",
            "meaning": "普通显式 constructor 继续展开会回到 alpha-side/same-row/row-level signed-source 固定点。",
        },
        {
            "from": NON_SPLIT_ATOM,
            "to": ATOMIC_ROWS_FORMULA,
            "meaning": "为避免普通分裂固定点，constructor 必须采用 anti-split atomic row 形式。",
        },
        {
            "from": ATOMIC_ROWS_FORMULA,
            "to": BUILTIN_PAIRING,
            "meaning": "atomic rows 的 signed 首缺口是每行内置 signed coefficient/pairing 闭式。",
        },
        {
            "from": "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem",
            "to": EXACTUV_PAIR,
            "meaning": "ExactUV 并行门拆成 source-domain entropy 与 fixed exact-pair polylog fiber bound。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    strict_downstream: dict[str, Any],
    explicit_direct: dict[str, Any],
    source_downstream: dict[str, Any],
    atomic_rows: dict[str, Any],
    exactuv_entropy: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LatestConstructorImported",
            latest.get("next_primary_attack_target") == EXPLICIT_RULE
            and latest.get("explicit_joint_alpha_delta_constructor_rule_proved") is False,
            False,
            "上一层把 latest 三破环口同步到显式 joint alpha/delta constructor rule。",
            EXPLICIT_RULE,
        ),
        row(
            "OrdinaryConstructorFixedPointImported",
            explicit_direct.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True
            and strict_downstream.get("ordinary_joint_declaration_route_rejected_as_nonproof") is True,
            True,
            "普通 constructor 路线经 alpha-side/same-row/row-level 回到 signed-source 固定点，不能自证。",
            ATOMIC_ROWS_FORMULA,
        ),
        row(
            "AntiSplitAtomicRouteImported",
            strict_downstream.get("antisplit_atomic_route_imported") is True,
            False,
            "若 constructor 真要破环，必须内置 anti-split atomic rows，而不是只命名显式规则。",
            ATOMIC_ROWS_FORMULA,
        ),
        row(
            "AtomicRowsToBuiltinPairingImported",
            strict_downstream.get("atomic_rows_reduced_to_builtin_pairing") is True
            and atomic_rows.get("next_direct_attack_target") == BUILTIN_PAIRING
            and source_downstream.get("next_direct_attack_target") == BUILTIN_PAIRING,
            False,
            "anti-split atomic rows 的首个 signed 缺口已经同步到 built-in pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberParallelImported",
            strict_downstream.get("parallel_direct_attack_target") == EXACTUV_PAIR
            and exactuv_entropy.get("next_direct_attack_target") == EXACTUV_PAIR,
            False,
            "built-in pairing 不自动支付 ExactUV；source entropy 与 fixed fiber 仍是并行硬点。",
            EXACTUV_PAIR,
        ),
        row(
            "BuiltInPairingCurrentCorpusProved",
            False,
            False,
            "当前材料没有每条 atomic joint row 的 signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVEntropyFiberCurrentCorpusProved",
            False,
            False,
            "当前材料没有 source-domain entropy 与 fixed exact-pair polylog fiber bound 的合取证明。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层是 latest 下游压缩，不是三目标命题无条件闭合。",
            "row/column theorem still open",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    latest = load_json(LATEST_CONSTRUCTOR)
    strict_downstream = load_json(STRICT_ANTISPLIT_DOWNSTREAM)
    explicit_direct = load_json(EXPLICIT_DIRECT)
    source_downstream = load_json(SOURCE_DOWNSTREAM)
    atomic_rows = load_json(ATOMIC_ROWS)
    exactuv_entropy = load_json(EXACTUV_ENTROPY)
    rows = build_rows(
        latest=latest,
        strict_downstream=strict_downstream,
        explicit_direct=explicit_direct,
        source_downstream=source_downstream,
        atomic_rows=atomic_rows,
        exactuv_entropy=exactuv_entropy,
    )
    retained_basis = (
        f"(({BUILTIN_PAIRING} AND {EXACTUV_PAIR}) OR {TERMINAL_DESCENT} OR "
        f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI} "
        f"OR ({SIGNED_SURVIVAL} AND {ROW_MASS})) AND {COMPLETE_KEY} AND {FIXED_KEY} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_antisplit_downstream_sync_router",
        "status": "phi_lpf_latest_constructor_synced_to_builtin_pairing_and_exactuv_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "latest_constructor_imported": rows[0]["closed"],
        "ordinary_constructor_fixed_point_imported": rows[1]["closed"],
        "antisplit_atomic_route_imported": rows[2]["closed"],
        "atomic_rows_to_builtin_pairing_imported": rows[3]["closed"],
        "exactuv_entropy_fiber_parallel_imported": rows[4]["closed"],
        "explicit_joint_alpha_delta_constructor_rule_proved": False,
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": EXPLICIT_RULE,
        "absorbed_to": BUILTIN_PAIRING,
        "next_primary_attack_target": BUILTIN_PAIRING,
        "parallel_primary_attack_target": EXACTUV_PAIR,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续推进 latest constructor 硬点：普通显式 joint constructor 会回到 "
            "signed-source 固定点，不能作为非循环证明。因此 productive 路线必须采用 anti-split "
            "atomic rows，首个 signed 缺口压到 built-in signed coefficient/pairing 闭式；"
            f"并行 ExactUV 硬点为 `{EXACTUV_PAIR}`。这些输入仍未证明，行/列命题未无条件闭合。"
        ),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF latest constructor anti-split downstream sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
    ]
    for key in [
        "latest_constructor_imported",
        "ordinary_constructor_fixed_point_imported",
        "antisplit_atomic_route_imported",
        "atomic_rows_to_builtin_pairing_imported",
        "exactuv_entropy_fiber_parallel_imported",
        "built_in_signed_pairing_proved",
        "actual_emitter_source_domain_entropy_proved",
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved",
        "row_column_unconditional_closed",
        "next_primary_attack_target",
        "parallel_primary_attack_target",
    ]:
        value = cert[key]
        lines.append(f"{key}={value if not isinstance(value, bool) else fmt_bool(value)}")
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
            "## 3. 最新主攻",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行 ExactUV 主攻：",
            "",
            "```text",
            cert["parallel_primary_attack_target"],
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
    print(f"parallel_primary_attack_target={cert['parallel_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
