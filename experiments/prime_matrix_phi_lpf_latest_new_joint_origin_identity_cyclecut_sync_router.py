#!/usr/bin/env python3
"""生成 Phi-LPF latest new-joint 来源恒等式到 cycle-cut 三出口的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_origin_identity_cyclecut_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-origin-identity-cyclecut-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_ORIGIN = DOCS / "prime-matrix-phi-lpf-latest-new-joint-pointwise-table-origin-sync-router.json"
PRIMITIVE_ORIGIN = DOCS / "prime-matrix-strict-primitive-summand-origin-identity-router.json"
ROW_LEVEL = DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.json"
COORD_CYCLE = DOCS / "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"
NONRECURSIVE_BREAKER = DOCS / "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"

ORIGIN_IDENTITY = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
SIGNED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TRIAD = f"{CYCLE_CUT}_OR_{PDEC_SCOPE}_OR_{NEW_JOINT}"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
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
    return [LATEST_ORIGIN, PRIMITIVE_ORIGIN, ROW_LEVEL, COORD_CYCLE, NONRECURSIVE_BREAKER]


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
            "from": ORIGIN_IDENTITY,
            "to": ROW_TABLE,
            "meaning": "来源恒等式等价于逐 actual noncanonical primitive summand 的 clean-core 原始生成表。",
        },
        {
            "from": ROW_TABLE,
            "to": SIGNED_EMITTER,
            "meaning": "逐行原始生成表必须由无环 pre-Cauchy source seed 自带 signed row emitter 产生。",
        },
        {
            "from": SIGNED_EMITTER,
            "to": f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
            "meaning": "signed row emitter 沿既有 signed law/basis source 链进入坐标-来源环；不能自证。",
        },
        {
            "from": f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
            "to": f"{CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
            "meaning": "latest nonrecursive breaker 进一步把 terminal 回流纳入三破环口或独立 WFD 输入。",
        },
    ]


def build_rows(
    latest: dict[str, Any],
    primitive_origin: dict[str, Any],
    row_level: dict[str, Any],
    coord_cycle: dict[str, Any],
    breaker: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LatestOriginIdentityImported",
            latest.get("next_primary_attack_target") == ORIGIN_IDENTITY
            and latest.get("primitive_summand_origin_identity_proved") is False,
            False,
            "上一层把 latest pointwise table 的首个真正 signed 字段压到 primitive summand 来源恒等式。",
            ORIGIN_IDENTITY,
        ),
        row(
            "OriginIdentityToRowTableImported",
            primitive_origin.get("target_input_before_router") == ORIGIN_IDENTITY
            and primitive_origin.get("next_direct_attack_target") == ROW_TABLE
            and primitive_origin.get("origin_identity_is_row_level_origin_generation") is True,
            False,
            "来源恒等式不是孤立口号；它等价于提交逐行 clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "RowTableToSignedEmitterImported",
            row_level.get("target_input_before_router") == ROW_TABLE
            and row_level.get("next_direct_attack_target") == SIGNED_EMITTER
            and row_level.get("table_requires_acyclic_seed_with_emitter") is True,
            False,
            "逐行表的生成器必须是无环 pre-Cauchy seed 自带的 signed row emitter 与推前前求和恒等式。",
            SIGNED_EMITTER,
        ),
        row(
            "ReverseAndUnsignedRoutesBlocked",
            primitive_origin.get("source_loop_self_proof_cut") is True
            and primitive_origin.get("unsigned_skeleton_not_signed_origin") is True
            and row_level.get("zero_row_signed_seed_blocked_imported") is True,
            True,
            "formal-unit 容器、unsigned skeleton、零行覆盖、payment 反推和 source-loop 都不能生成 signed origin。",
            SIGNED_EMITTER,
        ),
        row(
            "CoordinateSourceCycleGuardImported",
            coord_cycle.get("seed_coordinate_source_cycle_detected") is True
            and coord_cycle.get("raw_cycle_counts_as_closure") is False
            and coord_cycle.get("primitive_basis_and_coefficient_source_input_proved") is False,
            True,
            "signed weight coordinate、coefficient assignment、origin identity、row emitter 与 basis alphabet 形成已登记闭环；原环不能算证明。",
            f"{CYCLE_CUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "LatestNonrecursiveBreakerTriadImported",
            breaker.get("current_chain_contains_nonproof_cycle") is True
            and breaker.get("seed_cycle_cut_input_proved") is False
            and breaker.get("acyclic_same_set_scope_match_proved") is False
            and breaker.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "latest nonrecursive breaker 将继续路线压到无环 seed cycle-cut、same-set PDEC scope 或新显式 joint 公式。",
            f"{CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "OriginIdentityCurrentCorpusProved",
            False,
            False,
            "当前材料没有 primitive summand signed coefficient 来源恒等式。",
            ORIGIN_IDENTITY,
        ),
        row(
            "CycleCutPDECorNewJointCurrentCorpusProved",
            False,
            False,
            "当前材料没有三破环输入中的任意一项无条件证明。",
            f"{CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层仍是非循环前沿同步，不是三目标命题无条件闭合。",
            f"{TRIAD} AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    latest = load_json(LATEST_ORIGIN)
    primitive_origin = load_json(PRIMITIVE_ORIGIN)
    row_level = load_json(ROW_LEVEL)
    coord_cycle = load_json(COORD_CYCLE)
    breaker = load_json(NONRECURSIVE_BREAKER)
    rows = build_rows(
        latest=latest,
        primitive_origin=primitive_origin,
        row_level=row_level,
        coord_cycle=coord_cycle,
        breaker=breaker,
    )
    retained_basis = (
        f"({CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT} OR {TERMINAL_DESCENT}) "
        f"AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_origin_identity_cyclecut_sync_router",
        "status": "phi_lpf_latest_new_joint_origin_identity_synced_to_cyclecut_pdec_newjoint_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "latest_origin_identity_imported": rows[0]["closed"],
        "origin_identity_to_row_table_imported": rows[1]["closed"],
        "row_table_to_signed_emitter_imported": rows[2]["closed"],
        "reverse_and_unsigned_routes_blocked": rows[3]["closed"],
        "coordinate_source_cycle_guard_imported": rows[4]["closed"],
        "latest_nonrecursive_breaker_triad_imported": rows[5]["closed"],
        "primitive_summand_origin_identity_proved": False,
        "row_level_origin_generation_table_proved": False,
        "acyclic_seed_signed_row_emitter_rule_proved": False,
        "seed_cycle_cut_input_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": ORIGIN_IDENTITY,
        "absorbed_to": TRIAD,
        "next_primary_attack_target": TRIAD,
        "parallel_primary_attack_targets": [
            TERMINAL_DESCENT,
            SIGNED_SURVIVAL,
            ROW_MASS,
            EXACTUV_PAIR,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把 latest new-joint 的 `{ORIGIN_IDENTITY}` 继续接到既有来源下游。"
            f"来源恒等式等价于 `{ROW_TABLE}`，而逐行表必须由 `{SIGNED_EMITTER}` 正向生成。"
            "该 emitter 沿当前语料展开会进入 signed 坐标-来源闭环；原环不能作为证明。"
            f"因此 latest 非循环主攻同步为 `{CYCLE_CUT}`、`{PDEC_SCOPE}` 或 `{NEW_JOINT}`。"
            "terminal WFD、signed survival/row-mass、ExactUV、模型、Rate、DStructure 仍开放；"
            "行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest new-joint origin-identity cycle-cut sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_origin_identity_imported={fmt_bool(cert['latest_origin_identity_imported'])}",
        f"origin_identity_to_row_table_imported={fmt_bool(cert['origin_identity_to_row_table_imported'])}",
        f"row_table_to_signed_emitter_imported={fmt_bool(cert['row_table_to_signed_emitter_imported'])}",
        f"reverse_and_unsigned_routes_blocked={fmt_bool(cert['reverse_and_unsigned_routes_blocked'])}",
        f"coordinate_source_cycle_guard_imported={fmt_bool(cert['coordinate_source_cycle_guard_imported'])}",
        f"latest_nonrecursive_breaker_triad_imported={fmt_bool(cert['latest_nonrecursive_breaker_triad_imported'])}",
        f"primitive_summand_origin_identity_proved={fmt_bool(cert['primitive_summand_origin_identity_proved'])}",
        f"seed_cycle_cut_input_proved={fmt_bool(cert['seed_cycle_cut_input_proved'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(cert['acyclic_same_set_scope_match_proved'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(cert['new_explicit_joint_constructor_formula_artifact_present'])}",
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
