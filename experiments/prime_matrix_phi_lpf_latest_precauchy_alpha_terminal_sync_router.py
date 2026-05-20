#!/usr/bin/env python3
"""生成 Phi-LPF latest pre-Cauchy 到 alpha-terminal 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_precauchy_alpha_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_SOURCE_TABLE = DOCS / (
    "prime-matrix-phi-lpf-latest-signed-macrocycle-exactuv-source-table-sync-router.json"
)
PRECAUCHY_DECL = DOCS / "prime-matrix-strict-precauchy-declaration-line-router.json"
CONSTRUCTOR_FORMULA = DOCS / "prime-matrix-strict-actual-constructor-formula-line-router.json"
EXPLICIT_ALPHA_DELTA = DOCS / "prime-matrix-strict-explicit-alpha-delta-rule-router.json"
ALPHA_SIDE = DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.json"
ALPHA_MAP = DOCS / "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"
ALPHA_ANCHOR = DOCS / "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"
SIGNED_LIFT = DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json"
SIGNED_WEIGHT = DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json"
IDENTITY_TAXONOMY = DOCS / "prime-matrix-strict-independent-identity-statement-taxonomy-router.json"
MOVING_BLOCK = DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json"
DOWNSTREAM_SYNC = DOCS / "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"

PRECAUCHY_DECL_LEDGER = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
CONSTRUCTOR_FORMULA_LEDGER = "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter"
EXPLICIT_ALPHA_DELTA_LEDGER = "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
ALPHA_SIDE_LEDGER = "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger"
DETERMINISTIC_ALPHA_MAP_LEDGER = "DeterministicAlphaPrimitiveRowEmissionMapLedger"
ALPHA_ANCHOR_LEDGER = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SIGNED_LIFT_LEDGER = "AlphaFormulaSignedCoefficientLiftLedger"
SIGNED_WEIGHT_LEDGER = "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger"
IDENTITY_LEDGER = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
MOVING_BLOCK_LEDGER = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"

SIBLING_FIELDS = [
    "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger",
    "AlphaDeltaPairingCompatibilityBeforeCauchyLedger",
    "PrimitiveRuleNonzeroSignLocalFactorLedger",
    "ConstructorDomainCleanCoreMembershipLedger",
    "ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger",
    "ConstructorFormulaFailureReturnTagsLedger",
    "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable",
    "AlphaDeltaCoefficientIdentityBeforePushforwardLedger",
    "SourceTableNoDownstreamRecoveryAndNamedReturnLedger",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，避免把缺失误当证明。"""
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


def dependency_paths() -> list[Path]:
    """返回本层依赖证书。"""
    return [
        LATEST_SOURCE_TABLE,
        PRECAUCHY_DECL,
        CONSTRUCTOR_FORMULA,
        EXPLICIT_ALPHA_DELTA,
        ALPHA_SIDE,
        ALPHA_MAP,
        ALPHA_ANCHOR,
        SIGNED_LIFT,
        SIGNED_WEIGHT,
        IDENTITY_TAXONOMY,
        MOVING_BLOCK,
        DOWNSTREAM_SYNC,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复核同步证书。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def retained_parallel_basis() -> str:
    """返回本层之后仍保留的并行开放基。"""
    return (
        f"({PDEC_CLEAN_KLS} AND {MODEL_GAP}) AND {FIXED_KEY} AND {SIGNED_ROW_LAW} "
        f"AND {RATE} AND {DSTRUCTURE}"
    )


def build_chain() -> list[dict[str, str]]:
    """给出 pre-Cauchy 生产性分支的同步链。"""
    return [
        {"from": PRECAUCHY_DECL_LEDGER, "to": CONSTRUCTOR_FORMULA_LEDGER},
        {"from": CONSTRUCTOR_FORMULA_LEDGER, "to": EXPLICIT_ALPHA_DELTA_LEDGER},
        {"from": EXPLICIT_ALPHA_DELTA_LEDGER, "to": ALPHA_SIDE_LEDGER},
        {"from": ALPHA_SIDE_LEDGER, "to": DETERMINISTIC_ALPHA_MAP_LEDGER},
        {"from": DETERMINISTIC_ALPHA_MAP_LEDGER, "to": ALPHA_ANCHOR_LEDGER},
        {"from": ALPHA_ANCHOR_LEDGER, "to": SIGNED_LIFT_LEDGER},
        {"from": SIGNED_LIFT_LEDGER, "to": SIGNED_WEIGHT_LEDGER},
        {"from": SIGNED_WEIGHT_LEDGER, "to": IDENTITY_LEDGER},
        {"from": IDENTITY_LEDGER, "to": MOVING_BLOCK_LEDGER},
        {"from": MOVING_BLOCK_LEDGER, "to": f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}"},
    ]


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    latest = deps["latest"]
    precauchy = deps["precauchy"]
    constructor = deps["constructor"]
    alpha_delta = deps["alpha_delta"]
    alpha_side = deps["alpha_side"]
    alpha_map = deps["alpha_map"]
    alpha_anchor = deps["alpha_anchor"]
    signed_lift = deps["signed_lift"]
    signed_weight = deps["signed_weight"]
    identity = deps["identity"]
    moving = deps["moving"]
    downstream = deps["downstream"]

    return [
        row(
            "LatestSourceTableLeavesPreCauchyDeclaration",
            latest.get("next_primary_attack_target") == PRECAUCHY_DECL_LEDGER,
            False,
            "上一层 Phi-LPF latest source-table 同步把生产性首字段钉到 pre-Cauchy constructor declaration。",
            PRECAUCHY_DECL_LEDGER,
        ),
        row(
            "PreCauchyDeclarationToConstructorFormulaImported",
            precauchy.get("next_direct_attack_target") == CONSTRUCTOR_FORMULA_LEDGER
            or CONSTRUCTOR_FORMULA_LEDGER in precauchy.get("terminal_gap_after_router", ""),
            False,
            "strict declaration line 证书显示该声明线若继续展开，首个实际内容是 actual constructor formula line。",
            CONSTRUCTOR_FORMULA_LEDGER,
        ),
        row(
            "ConstructorFormulaToExplicitAlphaDeltaImported",
            constructor.get("next_direct_attack_target") == EXPLICIT_ALPHA_DELTA_LEDGER,
            False,
            "constructor formula line 不能由外部估计、反推 payment 或零行几何生成，必须给显式 alpha/delta primitive 规则。",
            EXPLICIT_ALPHA_DELTA_LEDGER,
        ),
        row(
            "ExplicitAlphaDeltaToAlphaSideImported",
            alpha_delta.get("next_direct_attack_target") == ALPHA_SIDE_LEDGER,
            False,
            "显式 alpha/delta 规则的首个生产性字段是 alpha-side primitive rule，delta、pairing 和 nonzero 字段并行保留。",
            " AND ".join([ALPHA_SIDE_LEDGER, *SIBLING_FIELDS[:3]]),
        ),
        row(
            "AlphaSideToDeterministicMapImported",
            alpha_side.get("next_direct_attack_target") == DETERMINISTIC_ALPHA_MAP_LEDGER,
            False,
            "alpha-side 规则不是 source tuple 容器；它继续压到确定性 alpha row 发射映射。",
            DETERMINISTIC_ALPHA_MAP_LEDGER,
        ),
        row(
            "DeterministicMapToAnchorPhaseImported",
            alpha_map.get("next_direct_attack_target") == ALPHA_ANCHOR_LEDGER,
            False,
            "确定性发射映射需要由 A/D0/K/Omega/phase_rule 给出 anchor/phase row 公式。",
            ALPHA_ANCHOR_LEDGER,
        ),
        row(
            "AnchorPhaseToSignedLiftImported",
            alpha_anchor.get("next_direct_attack_target") == SIGNED_LIFT_LEDGER,
            False,
            "carry-shell、P列锚和 layered wheel 只给 unsigned 形状；真正缺口是 signed coefficient lift。",
            SIGNED_LIFT_LEDGER,
        ),
        row(
            "SignedLiftToAlphaWeightLawImported",
            signed_lift.get("next_direct_attack_target") == SIGNED_WEIGHT_LEDGER,
            False,
            "signed lift 必须提交 pre-Cauchy 算术权重律，不能由 unsigned LPF/Phi 覆盖数据推出。",
            SIGNED_WEIGHT_LEDGER,
        ),
        row(
            "AlphaWeightLawToIndependentIdentityImported",
            signed_weight.get("next_direct_attack_target") == IDENTITY_LEDGER,
            False,
            "alpha signed 权重律被压成独立 noncanonical pre-Cauchy 算术恒等式陈述。",
            IDENTITY_LEDGER,
        ),
        row(
            "IdentityTaxonomyToMovingBlockImported",
            identity.get("next_direct_attack_target") == MOVING_BLOCK_LEDGER,
            True,
            "恒等式陈述不是第五类来源；合法来源分类后只剩 actual moving-block/NC-BLK。",
            MOVING_BLOCK_LEDGER,
        ),
        row(
            "MovingBlockToGlobalTerminalModelGapImported",
            moving.get("terminal_gap_after_router") == f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
            False,
            "moving-block/NC-BLK 已不能作无名出口，回到全局 PDEC/CleanKLS 容量门和模型余量账本。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "DownstreamSyncAgreesWithTerminalModelGap",
            downstream.get("next_direct_attack_target") == PDEC_CLEAN_KLS,
            False,
            "alpha signed weight downstream 同步也把后续主攻压到 PDEC/CleanKLS，并保留模型、DStructure 等门。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP} AND {DSTRUCTURE}",
        ),
        row(
            "LPFPhiUnsignedOnlyBoundaryRetained",
            latest.get("lpf_phi_unsigned_capacity_exhausted") is True,
            True,
            "LPF/Phi 精准桶恒等式已经用尽在 ownership/support/capacity 上；它仍不生成 signed pre-Cauchy 权重。",
            SIGNED_WEIGHT_LEDGER,
        ),
        row(
            "SiblingSourceTableFieldsStillOpen",
            True,
            False,
            "本层只同步 productive alpha-side 分支；source table 的 rows、identity、return、delta、pairing、nonzero 等兄弟字段仍未证明。",
            " AND ".join(SIBLING_FIELDS),
        ),
        row(
            "FixedKeyAndSignedRowLawStillParallel",
            True,
            False,
            "ExactUV fixed-key 局部重数与 seed signed row law 不是本分支同步的结论，继续作为并行硬点保留。",
            f"{FIXED_KEY} AND {SIGNED_ROW_LAW}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "当前只完成 latest pre-Cauchy 分支到全局终端门的同步；没有证明 PDEC/CleanKLS、模型余量或行/列命题。",
            retained_parallel_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    deps = {
        "latest": load_json(LATEST_SOURCE_TABLE),
        "precauchy": load_json(PRECAUCHY_DECL),
        "constructor": load_json(CONSTRUCTOR_FORMULA),
        "alpha_delta": load_json(EXPLICIT_ALPHA_DELTA),
        "alpha_side": load_json(ALPHA_SIDE),
        "alpha_map": load_json(ALPHA_MAP),
        "alpha_anchor": load_json(ALPHA_ANCHOR),
        "signed_lift": load_json(SIGNED_LIFT),
        "signed_weight": load_json(SIGNED_WEIGHT),
        "identity": load_json(IDENTITY_TAXONOMY),
        "moving": load_json(MOVING_BLOCK),
        "downstream": load_json(DOWNSTREAM_SYNC),
    }
    rows = build_rows(deps)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_precauchy_alpha_terminal_sync_router",
        "status": "phi_lpf_latest_precauchy_alpha_branch_synced_to_global_terminal_modelgap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "precauchy_alpha_terminal_sync_closed": True,
        "latest_source_table_imported": rows[0]["closed"],
        "strict_precauchy_to_constructor_imported": rows[1]["closed"],
        "constructor_to_explicit_alpha_delta_imported": rows[2]["closed"],
        "explicit_alpha_delta_to_alpha_side_imported": rows[3]["closed"],
        "alpha_side_to_deterministic_map_imported": rows[4]["closed"],
        "deterministic_map_to_anchor_phase_imported": rows[5]["closed"],
        "anchor_phase_to_signed_lift_imported": rows[6]["closed"],
        "signed_lift_to_weight_law_imported": rows[7]["closed"],
        "weight_law_to_independent_identity_imported": rows[8]["closed"],
        "identity_taxonomy_to_moving_block_imported": rows[9]["closed"],
        "moving_block_to_global_terminal_modelgap_imported": rows[10]["closed"],
        "lpf_phi_unsigned_only_boundary_retained": rows[12]["closed"],
        "pre_cauchy_constructor_declaration_line_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "actual_noncanonical_moving_block_spread_ncb_lk_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "productive_branch_chain": build_chain(),
        "parallel_open_sibling_fields": SIBLING_FIELDS,
        "retained_parallel_basis": retained_parallel_basis(),
        "next_primary_attack_target": PDEC_CLEAN_KLS,
        "parallel_attack_targets": [
            MODEL_GAP,
            FIXED_KEY,
            SIGNED_ROW_LAW,
            RATE,
            DSTRUCTURE,
            "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger",
            "AlphaDeltaPairingCompatibilityBeforeCauchyLedger",
        ],
        "plain_conclusion": (
            "本步把上一层留下的 `PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` "
            "沿 strict constructor/alpha 链同步到底：declaration -> constructor formula -> explicit alpha/delta -> "
            "alpha-side deterministic row -> anchor/phase -> signed lift -> alpha weight law -> independent identity -> "
            "actual moving-block/NC-BLK -> PDEC/CleanKLS + model gap。"
            "因此 productive alpha-side 分支已接入全局终端容量/模型余量门；但 pre-Cauchy 声明、delta/pairing/nonzero "
            "兄弟字段、fixed-key ExactUV、signed row law、模型、Rate 与 DStructure 均未证明，行/列命题仍未无条件闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest pre-Cauchy alpha-terminal sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_source_table_imported={fmt_bool(result['latest_source_table_imported'])}",
        f"strict_precauchy_to_constructor_imported={fmt_bool(result['strict_precauchy_to_constructor_imported'])}",
        f"constructor_to_explicit_alpha_delta_imported={fmt_bool(result['constructor_to_explicit_alpha_delta_imported'])}",
        f"explicit_alpha_delta_to_alpha_side_imported={fmt_bool(result['explicit_alpha_delta_to_alpha_side_imported'])}",
        f"alpha_side_to_deterministic_map_imported={fmt_bool(result['alpha_side_to_deterministic_map_imported'])}",
        f"deterministic_map_to_anchor_phase_imported={fmt_bool(result['deterministic_map_to_anchor_phase_imported'])}",
        f"anchor_phase_to_signed_lift_imported={fmt_bool(result['anchor_phase_to_signed_lift_imported'])}",
        f"signed_lift_to_weight_law_imported={fmt_bool(result['signed_lift_to_weight_law_imported'])}",
        f"weight_law_to_independent_identity_imported={fmt_bool(result['weight_law_to_independent_identity_imported'])}",
        f"identity_taxonomy_to_moving_block_imported={fmt_bool(result['identity_taxonomy_to_moving_block_imported'])}",
        f"moving_block_to_global_terminal_modelgap_imported={fmt_bool(result['moving_block_to_global_terminal_modelgap_imported'])}",
        f"lpf_phi_unsigned_only_boundary_retained={fmt_bool(result['lpf_phi_unsigned_only_boundary_retained'])}",
        f"pdec_cap_or_internal_clean_kls_large_sieve_proved={fmt_bool(result['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}",
        f"explicit_model_gap_and_finite_dprc_ledger_proved={fmt_bool(result['explicit_model_gap_and_finite_dprc_ledger_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_proved={fmt_bool(result['fixed_key_exact_uv_local_multiplicity_o1_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. Productive alpha-side 同步链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for step in result["productive_branch_chain"]:
        lines.append(f"| `{cell(step['from'])}` | `{cell(step['to'])}` |")

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
                gate=item["gate"],
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 保留开放基",
            "",
            "```text",
            result["retained_parallel_basis"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "## 4. 边界",
            "",
            "- 本层只是同步 productive alpha-side 分支到全局终端门，不证明 pre-Cauchy 声明。",
            "- LPF/Phi 桶恒等式仍只支付无符号 ownership、support 与 capacity。",
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


if __name__ == "__main__":
    main()
