#!/usr/bin/env python3
"""生成 latest constructor built-in 宏循环切除与 signed-survival 侧门同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_macrocycle_cut_signed_survival_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-macrocycle-cut-signed-survival-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-joint-declaration-antisplit-sync-router.json"
BUILTIN_TRACE = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-builtin-trace-sync-router.json"
TRACE_SOURCE_RANK = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-router.json"
ALPHA_TERMINAL = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-router.json"
MOVING_SIGNED_TABLE = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-moving-atom-signed-table-sync-router.json"
POINTWISE_ORIGIN = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-pointwise-origin-sync-router.json"
ORIGIN_CYCLECUT = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-origin-cyclecut-sync-router.json"
TRIAD_UNIFIED = DOCS / "prime-matrix-phi-lpf-latest-new-joint-constructor-triad-unified-sync-router.json"
SIGNED_SURVIVAL_ORIGIN = DOCS / "prime-matrix-phi-lpf-signed-survival-origin-table-sync-router.json"
SOURCE_ENTROPY_BUILTIN = DOCS / "prime-matrix-phi-lpf-latest-source-entropy-to-builtin-pairing-sync-router.json"

BUILTIN = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ORIGIN_ID = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TRIAD = (
    "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput_OR_"
    "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate_OR_"
    "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
)
JOINT_DECL = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失文件不视为证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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
    """列出本层依赖证书。"""
    return [
        CURRENT,
        BUILTIN_TRACE,
        TRACE_SOURCE_RANK,
        ALPHA_TERMINAL,
        MOVING_SIGNED_TABLE,
        POINTWISE_ORIGIN,
        ORIGIN_CYCLECUT,
        TRIAD_UNIFIED,
        SIGNED_SURVIVAL_ORIGIN,
        SOURCE_ENTROPY_BUILTIN,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖证书哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def macrocycle_chain() -> list[dict[str, str]]:
    """给出 constructor signed 主线宏循环。"""
    return [
        {
            "from": BUILTIN,
            "to": NEW_PAYLOAD,
            "meaning": "built-in pairing 的 trace 展开删除 signed-lane 自证后只留下 new primitive payload/trace 出口。",
        },
        {
            "from": NEW_PAYLOAD,
            "to": ALPHA_ROW,
            "meaning": "new payload 若非环内改名，既有 source-rank absorber 把它压到同 formal-unit alpha/delta 核表。",
        },
        {
            "from": ALPHA_ROW,
            "to": MOVING_ATOM,
            "meaning": "constructor alpha 三原子前沿选择 clean-core moving atom 独立非终端排斥为最窄口。",
        },
        {
            "from": MOVING_ATOM,
            "to": POINTWISE_TABLE,
            "meaning": "moving atom 的 signed split 回到 Phi-LPF 支撑上的逐点 signed coefficient value table。",
        },
        {
            "from": POINTWISE_TABLE,
            "to": ORIGIN_ID,
            "meaning": "逐点 signed 表的第一生产性字段是 primitive summand signed coefficient origin identity。",
        },
        {
            "from": ORIGIN_ID,
            "to": TRIAD,
            "meaning": "origin identity 的非循环展开进入 seed cycle-cut、same-set PDEC 或 new joint triad。",
        },
        {
            "from": TRIAD,
            "to": JOINT_DECL,
            "meaning": "triad 统一前沿把内部生产性字段压回 pre-Cauchy joint declaration line。",
        },
        {
            "from": JOINT_DECL,
            "to": BUILTIN,
            "meaning": "ordinary declaration 是 fixed point；anti-split atomic rows 的首 signed 缺口又是 built-in pairing。",
        },
    ]


def retained_basis() -> str:
    """返回宏循环切除后的保留基。"""
    return (
        f"(({ROW_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {TERMINAL_DESCENT} OR {CANONICAL_LOCK} "
        f"OR {INDEPENDENT_BRIDGE} OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) "
        f"AND {EXACTUV_PAIR} AND ({COMPLETE_KEY} OR {REGISTERED_KEY}) AND {FIXED_KEY} "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成宏循环切除判定表。"""
    current = data["current"]
    builtin_trace = data["builtin_trace"]
    trace_rank = data["trace_rank"]
    alpha_terminal = data["alpha_terminal"]
    moving = data["moving"]
    pointwise_origin = data["pointwise_origin"]
    origin_cyclecut = data["origin_cyclecut"]
    triad = data["triad"]
    survival_origin = data["survival_origin"]
    source_entropy_builtin = data["source_entropy_builtin"]
    current_basis = current.get("latest_retained_basis_after_router", "")
    return [
        row(
            "CurrentConstructorBuiltInImported",
            current.get("next_primary_attack_target") == BUILTIN
            and current.get("built_in_signed_pairing_proved") is False,
            False,
            "最新 constructor joint-declaration antisplit 层把 signed 主口压到 built-in pairing。",
            BUILTIN,
        ),
        row(
            "BuiltInTraceReturnsToNewPayload",
            builtin_trace.get("target_input_before_router") == BUILTIN
            and builtin_trace.get("next_primary_attack_target") == NEW_PAYLOAD
            and builtin_trace.get("signed_lane_cycle_guard_imported") is True,
            False,
            "built-in trace 展开不能闭合，只能留下 new primitive payload/trace 或受控出口。",
            NEW_PAYLOAD,
        ),
        row(
            "NewPayloadAbsorbedToAlphaKernel",
            trace_rank.get("target_input_before_router") == NEW_PAYLOAD
            and trace_rank.get("next_primary_attack_target") == ALPHA_ROW
            and trace_rank.get("pointwise_kernel_frontier_imported") is True,
            False,
            "new payload/source-rank 线已汇入逐点 primitive alpha/delta 核表。",
            ALPHA_ROW,
        ),
        row(
            "AlphaKernelReturnsToMovingAtom",
            alpha_terminal.get("target_input_before_router") == ALPHA_ROW
            and alpha_terminal.get("next_primary_attack_target") == MOVING_ATOM,
            False,
            "alpha 三原子前沿继续同步到 clean-core moving atom 独立非终端排斥。",
            MOVING_ATOM,
        ),
        row(
            "MovingAtomReturnsToPointwiseSignedTable",
            moving.get("target_input_before_router") == MOVING_ATOM
            and moving.get("next_primary_attack_target") == POINTWISE_TABLE,
            False,
            "moving atom 的 signed split 又要求逐点 Phi-LPF signed 表。",
            POINTWISE_TABLE,
        ),
        row(
            "PointwiseTableReturnsToOriginIdentity",
            pointwise_origin.get("target_input_before_router") == POINTWISE_TABLE
            and pointwise_origin.get("next_primary_attack_target") == ORIGIN_ID,
            False,
            "逐点 signed 表继续回到 primitive summand origin identity。",
            ORIGIN_ID,
        ),
        row(
            "OriginIdentityReturnsToTriad",
            origin_cyclecut.get("target_input_before_router") == ORIGIN_ID
            and origin_cyclecut.get("next_primary_attack_target") == TRIAD,
            False,
            "origin identity 经 cycle-cut/PDEC/new-joint 三出口回到 triad 统一层。",
            TRIAD,
        ),
        row(
            "TriadReturnsToJointDeclaration",
            triad.get("target_input_before_router") == TRIAD
            and triad.get("next_primary_attack_target") == JOINT_DECL,
            False,
            "triad 统一层把生产性字段压回 pre-Cauchy joint declaration line。",
            JOINT_DECL,
        ),
        row(
            "JointDeclarationReturnsToBuiltIn",
            current.get("target_input_before_router") == JOINT_DECL
            and current.get("next_primary_attack_target") == BUILTIN,
            False,
            "joint declaration anti-split 层又回到 built-in pairing，形成 constructor signed 宏循环。",
            "constructor signed macrocycle",
        ),
        row(
            "ConstructorMacrocycleSelfProofRejected",
            True,
            True,
            "环内任一节点不能作为非循环证明；必须支付环外 signed-survival/row-mass/ExactUV 或受控出口。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS} AND {EXACTUV_PAIR}",
        ),
        row(
            "SignedSurvivalGateMandatoryInLatestBasis",
            SIGNED_SURVIVAL in current_basis and ROW_MASS in current_basis,
            False,
            "最新 385 保留基中 signed survival 与 row-mass 是 built-in 主线之外仍必须支付的侧门。",
            f"{SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "SignedSurvivalReducedToRowLevelOriginTable",
            survival_origin.get("next_primary_attack_target") == ROW_TABLE
            and survival_origin.get("origin_identity_reduced_to_row_level_generation") is True,
            False,
            "已有 Phi-LPF signed-survival 同步把推前前 signed expression 压到逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "SourceEntropyBuiltinCycleCarried",
            source_entropy_builtin.get("next_primary_attack_target") == BUILTIN
            and source_entropy_builtin.get("builtin_pairing_trace_cycle_carried") is True,
            True,
            "source-entropy 下游也会回到 built-in pairing/trace 环，不能替代 signed-survival 支付。",
            BUILTIN,
        ),
        row(
            "ExactUVAndPromotionGatesRemainOpen",
            current.get("actual_emitter_source_domain_entropy_proved") is False
            and current.get("exact_uv_map_fixed_pair_polylog_fiber_bound_proved") is False,
            False,
            "ExactUV entropy/fiber、complete/fixed key、模型、Rate 与 DStructure 仍是独立门。",
            f"{EXACTUV_PAIR} AND {COMPLETE_KEY}/{REGISTERED_KEY} AND {FIXED_KEY} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只切除 constructor signed 宏循环并选择 mandatory signed-survival 侧门；未证明三命题无条件闭合。",
            f"{ROW_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装宏循环切除证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "current": load_json(CURRENT),
        "builtin_trace": load_json(BUILTIN_TRACE),
        "trace_rank": load_json(TRACE_SOURCE_RANK),
        "alpha_terminal": load_json(ALPHA_TERMINAL),
        "moving": load_json(MOVING_SIGNED_TABLE),
        "pointwise_origin": load_json(POINTWISE_ORIGIN),
        "origin_cyclecut": load_json(ORIGIN_CYCLECUT),
        "triad": load_json(TRIAD_UNIFIED),
        "survival_origin": load_json(SIGNED_SURVIVAL_ORIGIN),
        "source_entropy_builtin": load_json(SOURCE_ENTROPY_BUILTIN),
    }
    rows = build_rows(data)
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_macrocycle_cut_signed_survival_sync_router",
        "status": "phi_lpf_latest_constructor_builtin_macrocycle_cut_signed_survival_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "cycle_cut_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "constructor_signed_macrocycle_closed": all(item["closed"] for item in rows[:9]),
        "constructor_macrocycle_self_proof_rejected": rows[9]["proved"],
        "signed_survival_gate_mandatory_in_latest_basis": rows[10]["closed"],
        "signed_survival_reduced_to_row_level_origin_table": rows[11]["closed"],
        "source_entropy_builtin_cycle_carried": rows[12]["closed"],
        "row_level_clean_core_origin_generation_table_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": BUILTIN,
        "absorbed_cycle": "constructor signed macrocycle",
        "next_primary_attack_target": ROW_TABLE,
        "parallel_primary_attack_targets": [
            SIGNED_SURVIVAL,
            ROW_MASS,
            EXACTUV_PAIR,
            COMPLETE_KEY,
            REGISTERED_KEY,
            FIXED_KEY,
            TERMINAL_DESCENT,
            CANONICAL_LOCK,
            INDEPENDENT_BRIDGE,
            PDEC_SCOPE,
            EXTERNAL_DIBFI,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "macrocycle_chain": macrocycle_chain(),
        "latest_retained_basis_after_router": retained_basis(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest constructor antisplit 后的 built-in signed pairing 口接入既有下游，"
            "并确认它不是新的非循环闭合：built-in -> new payload -> alpha kernel -> moving atom "
            "-> pointwise signed table -> origin identity -> triad -> joint declaration -> built-in 构成宏循环。"
            f"删除环内自证后，最新可硬攻的 mandatory signed 侧门是 `{ROW_TABLE}`，并行仍需 "
            f"`{SIGNED_SURVIVAL}`、`{ROW_MASS}`、ExactUV entropy/fiber、complete/fixed key、terminal/PDEC/"
            "external exits、模型、Rate 与 DStructure。行/列命题仍未无条件闭合。"
        ),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Phi-LPF latest constructor macrocycle cut signed-survival sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
    ]
    for key in [
        "constructor_signed_macrocycle_closed",
        "constructor_macrocycle_self_proof_rejected",
        "signed_survival_gate_mandatory_in_latest_basis",
        "signed_survival_reduced_to_row_level_origin_table",
        "source_entropy_builtin_cycle_carried",
        "row_level_clean_core_origin_generation_table_proved",
        "nonzero_signed_row_survival_proved",
        "same_formal_unit_row_mass_normalization_proved",
        "row_column_unconditional_closed",
        "next_primary_attack_target",
    ]:
        value = cert[key]
        lines.append(f"{key}={value if not isinstance(value, bool) else fmt_bool(value)}")
    lines.extend(
        [
            "```",
            "",
            "## 1. 宏循环链",
            "",
            "| from | to | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for edge in cert["macrocycle_chain"]:
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
            "并行仍需：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
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
    print(f"constructor_signed_macrocycle_closed={fmt_bool(cert['constructor_signed_macrocycle_closed'])}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
