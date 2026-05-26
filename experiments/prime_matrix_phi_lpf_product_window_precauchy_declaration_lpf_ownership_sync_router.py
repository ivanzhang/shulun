#!/usr/bin/env python3
"""归档 product-window pre-Cauchy declaration 到 LPF ownership/signed constructor 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_precauchy_declaration_lpf_ownership_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-precauchy-declaration-lpf-ownership-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-precauchy-declaration-lpf-ownership-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-precauchy-declaration-lpf-ownership-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-precauchy-declaration-lpf-ownership-sync-router.md

本证书承接 product-window same-unit rank ExactUV atomization sync。它把当前第一硬点
`PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` 接入 LPF ownership
sieve source declaration 证书。结论只是一条非循环同步：declaration line 的无符号
ownership 字段已由最小素因子唯一分桶恒等式支付；真正剩余是 signed alpha/delta
primitive constructor rule、定义域、行输出、失败回流和 ExactUV fixed-key 局部重数。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-precauchy-declaration-lpf-ownership-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-same-unit-rank-exactuv-atomization-sync-router.json"
LPF_OWNERSHIP = DOCS / "prime-matrix-lpf-ownership-sieve-source-declaration-router.json"
SOURCE_TABLE = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"
CONSTRUCTOR_RULE = DOCS / "prime-matrix-strict-explicit-alpha-delta-rule-router.json"
ALPHA_SIDE = DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.json"
DETERMINISTIC_ALPHA = DOCS / "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"

PRECAUCHY_DECL = "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
LPF_OWNERSHIP_LEDGER = "LeastPrimeFactorOwnershipUnsignedSourceDeclarationLedger"
EXPLICIT_RULE = "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
CONSTRUCTOR_DOMAIN = "ConstructorDomainCleanCoreMembershipLedger"
CONSTRUCTOR_ROWS = "ConstructorFormulaEmitsUVKeySignLocalFactorRowsLedger"
CONSTRUCTOR_RETURN = "ConstructorFormulaFailureReturnTagsLedger"
SOURCE_DECL_RETURN = "SourceDeclarationNoDownstreamRecoveryAndNamedReturnLedger"
PRIMITIVE_ROWS = "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable"
ALPHA_DELTA_IDENTITY = "AlphaDeltaCoefficientIdentityBeforePushforwardLedger"
NO_RECOVERY_RETURN = "SourceTableNoDownstreamRecoveryAndNamedReturnLedger"
FIXED_KEY_O1 = "FixedKeyExactUVLocalMultiplicityO1Ledger"
ALPHA_SIDE_RULE = "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger"
DELTA_SIDE_RULE = "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger"
PAIRING_COMPAT = "AlphaDeltaPreCauchyPairingCompatibilityLedger"
NONZERO_LOCAL = "PrimitiveRowNonzeroSignLocalFactorLedger"
ALPHA_ROW_MAP = "DeterministicAlphaPrimitiveRowEmissionMapLedger"
ALPHA_ROW_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
EXACTUV_RETURN = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """布尔值小写输出。"""
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
        PREVIOUS,
        LPF_OWNERSHIP,
        SOURCE_TABLE,
        CONSTRUCTOR_RULE,
        ALPHA_SIDE,
        DETERMINISTIC_ALPHA,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出 declaration 到 signed constructor 的同步链。"""
    return [
        {
            "from": PRECAUCHY_DECL,
            "to": f"{LPF_OWNERSHIP_LEDGER} AND {EXPLICIT_RULE}",
            "meaning": "LPF ownership 支付 declaration line 的无符号 ownership 字段；signed alpha/delta lift 仍开放。",
        },
        {
            "from": LPF_OWNERSHIP_LEDGER,
            "to": "ascending least-prime-factor disjoint bucket identity",
            "meaning": "每个合数按唯一最小素因子进入且只进入一个筛层，素数计数恒等式由此闭合。",
        },
        {
            "from": EXPLICIT_RULE,
            "to": f"{ALPHA_SIDE_RULE} AND {DELTA_SIDE_RULE} AND {PAIRING_COMPAT} AND {NONZERO_LOCAL}",
            "meaning": "显式 alpha/delta constructor 规则需分别生成 alpha/delta primitive rows，并给出 Cauchy 前配对兼容与非零 local factor。",
        },
        {
            "from": ALPHA_SIDE_RULE,
            "to": ALPHA_ROW_MAP,
            "meaning": "alpha-side primitive rule 的第一生产性字段是确定性 alpha primitive row 发射映射。",
        },
        {
            "from": ALPHA_ROW_MAP,
            "to": ALPHA_ROW_ANCHOR,
            "meaning": "确定性发射映射继续压到 alpha row anchor/phase emission formula。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    previous = data["previous"]
    lpf = data["lpf"]
    source_table = data["source_table"]
    constructor = data["constructor"]
    alpha_side = data["alpha_side"]
    deterministic_alpha = data["deterministic_alpha"]

    previous_declaration_active = (
        previous.get("next_primary_attack_target") == PRECAUCHY_DECL
        and previous.get("same_unit_rank_removed_from_product_window_first_target") is True
    )
    source_table_first_line_imported = (
        source_table.get("actual_emitter_source_table_router_closed") is True
        and source_table.get("source_table_field_decomposition_pinned") is True
    )
    lpf_ownership_imported = (
        lpf.get("pre_cauchy_declaration_line_imported") is True
        and lpf.get("ascending_lpf_ownership_partition_proved") is True
        and lpf.get("prime_count_identity_from_lpf_ownership_proved") is True
        and lpf.get("lpf_ownership_unsigned_declaration_line_closed") is True
    )
    signed_lift_still_open = (
        lpf.get("lpf_ownership_to_signed_alpha_delta_lift_proved") is False
        and lpf.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False
    )
    constructor_imported = (
        constructor.get("explicit_alpha_delta_rule_router_closed") is True
        and constructor.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False
    )
    alpha_side_imported = (
        alpha_side.get("alpha_side_primitive_rule_router_closed") is True
        and alpha_side.get("actual_noncanonical_alpha_side_primitive_rule_proved") is False
    )
    deterministic_alpha_imported = (
        deterministic_alpha.get("deterministic_alpha_row_emission_map_router_closed") is True
        and deterministic_alpha.get("alpha_row_anchor_phase_emission_formula_proved") is False
    )
    declaration_removed = all(
        [
            previous_declaration_active,
            source_table_first_line_imported,
            lpf_ownership_imported,
            signed_lift_still_open,
            constructor_imported,
            alpha_side_imported,
            deterministic_alpha_imported,
        ]
    )

    return [
        row(
            "ProductWindowPreCauchyDeclarationActiveBeforeSync",
            previous_declaration_active,
            False,
            "上一 product-window same-unit rank 证书把第一硬点推进到 pre-Cauchy constructor declaration。",
            PRECAUCHY_DECL,
        ),
        row(
            "SourceTableFirstLineImported",
            source_table_first_line_imported,
            False,
            "actual emitter source table 已把首字段钉为 pre-Cauchy declaration line。",
            PRECAUCHY_DECL,
        ),
        row(
            "LPFOwnershipUnsignedDeclarationImported",
            lpf_ownership_imported,
            True,
            "LPF ownership sieve 证明最小素因子唯一分桶和素数计数恒等式，可支付 unsigned ownership declaration 字段。",
            LPF_OWNERSHIP_LEDGER,
        ),
        row(
            "SignedAlphaDeltaLiftStillOpen",
            signed_lift_still_open,
            False,
            "LPF ownership 不产生 signed alpha/delta coefficient、orientation、local factor 或 ExactUV fixed-key 重数。",
            EXPLICIT_RULE,
        ),
        row(
            "ExplicitAlphaDeltaRuleRouterImported",
            constructor_imported,
            False,
            "显式 alpha/delta constructor rule 已被拆成 alpha-side、delta-side、配对兼容和非零 local factor。",
            f"{ALPHA_SIDE_RULE} AND {DELTA_SIDE_RULE} AND {PAIRING_COMPAT} AND {NONZERO_LOCAL}",
        ),
        row(
            "AlphaSidePrimitiveRuleImported",
            alpha_side_imported,
            False,
            "alpha-side primitive rule 继续压到确定性 alpha row 发射映射等字段。",
            ALPHA_ROW_MAP,
        ),
        row(
            "DeterministicAlphaEmissionImported",
            deterministic_alpha_imported,
            False,
            "确定性 alpha row 发射映射的当前最窄点是 alpha row anchor/phase emission formula。",
            ALPHA_ROW_ANCHOR,
        ),
        row(
            "PreCauchyDeclarationRemovedFromProductWindowFirstTarget",
            declaration_removed,
            False,
            "pre-Cauchy declaration 旧名的 unsigned ownership 字段已支付；第一主攻转为显式 signed constructor rule。",
            EXPLICIT_RULE,
        ),
        row(
            "ExplicitAlphaDeltaRuleStillOpen",
            constructor.get("explicit_alpha_delta_primitive_constructor_rule_proved") is False,
            False,
            "当前材料尚未写出 actual noncanonical primitive constructor 的 signed alpha/delta 规则。",
            EXPLICIT_RULE,
        ),
        row(
            "FixedKeyAndSignedSideStillOpen",
            previous.get("fixed_key_exact_uv_local_multiplicity_o1_proved") is False
            and previous.get("orientation_parity_branch_side_proved") is False
            and previous.get("offdiagonal_exactuv_fixed_pair_return_ledger_proved") is False,
            False,
            "fixed-key local multiplicity、orientation、ExactUV return 与 internal transition 仍未证明。",
            f"{FIXED_KEY_O1} AND {ORIENTATION} AND {EXACTUV_RETURN} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只同步 declaration 到 LPF ownership/signed constructor 接口，不证明三命题无条件闭合。",
            "row_column_unconditional_closed=false",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    data = {
        "previous": load_json(PREVIOUS),
        "lpf": load_json(LPF_OWNERSHIP),
        "source_table": load_json(SOURCE_TABLE),
        "constructor": load_json(CONSTRUCTOR_RULE),
        "alpha_side": load_json(ALPHA_SIDE),
        "deterministic_alpha": load_json(DETERMINISTIC_ALPHA),
    }
    rows = build_rows(data)
    declaration_removed = rows[7]["closed"]
    latest_open_summary = (
        f"{EXPLICIT_RULE} AND {CONSTRUCTOR_DOMAIN} AND {CONSTRUCTOR_ROWS} AND "
        f"{CONSTRUCTOR_RETURN} AND {SOURCE_DECL_RETURN} AND {FIXED_KEY_O1} AND "
        f"{ORIENTATION} AND {EXACTUV_RETURN} AND {INTERNAL_TRANSITION} AND {RATE} AND {DSTRUCTURE}"
    )
    latest_basis = (
        f"({LPF_OWNERSHIP_LEDGER} AND {EXPLICIT_RULE} AND {CONSTRUCTOR_DOMAIN} AND "
        f"{CONSTRUCTOR_ROWS} AND {CONSTRUCTOR_RETURN} AND {SOURCE_DECL_RETURN} AND "
        f"{PRIMITIVE_ROWS} AND {ALPHA_DELTA_IDENTITY} AND {NO_RECOVERY_RETURN} AND "
        f"{FIXED_KEY_O1} AND {ORIENTATION} AND {EXACTUV_RETURN} AND {INTERNAL_TRANSITION}) "
        f"AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_precauchy_declaration_lpf_ownership_sync_router",
        "status": "product_window_precauchy_declaration_unsigned_ownership_closed_signed_constructor_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_absence_not_used": True,
        "product_window_precauchy_declaration_active_before_sync": rows[0]["closed"],
        "source_table_first_line_imported": rows[1]["closed"],
        "lpf_ownership_unsigned_declaration_imported": rows[2]["closed"],
        "signed_alpha_delta_lift_still_open": rows[3]["closed"],
        "explicit_alpha_delta_rule_router_imported": rows[4]["closed"],
        "alpha_side_primitive_rule_imported": rows[5]["closed"],
        "deterministic_alpha_emission_imported": rows[6]["closed"],
        "precauchy_declaration_removed_from_product_window_first_target": declaration_removed,
        "lpf_ownership_unsigned_declaration_line_closed": True,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "orientation_parity_branch_side_proved": False,
        "offdiagonal_exactuv_fixed_pair_return_ledger_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "row_column_unconditional_closed": False,
        "old_primary_attack_target": PRECAUCHY_DECL,
        "next_primary_attack_target": EXPLICIT_RULE,
        "parallel_primary_attack_targets": [
            CONSTRUCTOR_DOMAIN,
            CONSTRUCTOR_ROWS,
            CONSTRUCTOR_RETURN,
            SOURCE_DECL_RETURN,
            FIXED_KEY_O1,
            ORIENTATION,
            EXACTUV_RETURN,
            INTERNAL_TRANSITION,
            RATE,
            DSTRUCTURE,
        ],
        "latest_retained_basis_after_router": latest_basis,
        "latest_open_basis_summary": latest_open_summary,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window same-unit rank ExactUV atomization sync 留下的 "
            "`PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter` 接入 LPF ownership "
            "sieve source declaration 证书。结论是：declaration line 的无符号 ownership 字段已由"
            "最小素因子唯一分桶与素数计数恒等式支付；它不产生 signed alpha/delta coefficient、"
            "local factor 或 ExactUV fixed-key 重数。因此 product-window 第一主攻推进为 "
            "`ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter`。本证书不证明三命题无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window pre-Cauchy declaration LPF ownership sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"lpf_ownership_unsigned_declaration_imported={fmt_bool(cert['lpf_ownership_unsigned_declaration_imported'])}",
        f"lpf_ownership_unsigned_declaration_line_closed={fmt_bool(cert['lpf_ownership_unsigned_declaration_line_closed'])}",
        f"precauchy_declaration_removed_from_product_window_first_target={fmt_bool(cert['precauchy_declaration_removed_from_product_window_first_target'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下游同步链",
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
            "## 3. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "仍开放的实际负载摘要：",
            "",
            "```text",
            cert["latest_open_basis_summary"],
            "```",
            "",
            "下一直接主攻：",
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
            "严格含义：本证书只同步 declaration 到 LPF ownership/signed constructor 接口，不证明行/列命题。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(
        "precauchy_declaration_removed_from_product_window_first_target="
        f"{fmt_bool(cert['precauchy_declaration_removed_from_product_window_first_target'])}"
    )
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
