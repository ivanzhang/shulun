#!/usr/bin/env python3
"""归档 product-window 显式 alpha/delta 到 signed summand 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_explicit_alpha_delta_signed_summand_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-explicit-alpha-delta-signed-summand-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-explicit-alpha-delta-signed-summand-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-explicit-alpha-delta-signed-summand-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-explicit-alpha-delta-signed-summand-sync-router.md

本证书承接 product-window pre-Cauchy declaration LPF ownership sync。它把当前第一硬点
`ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` 接入 strict
explicit-rule、alpha-side primitive rule、LPF candidate-row map 和 pointwise signed
weight formula 证书。结论只是一条非循环前沿同步：LPF 可以继续支付 alpha 侧候选
row 的唯一 ownership/几何索引，但仍不能给出 actual signed primitive summand 表达式。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-explicit-alpha-delta-signed-summand-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-precauchy-declaration-lpf-ownership-sync-router.json"
EXPLICIT_RULE_ROUTER = DOCS / "prime-matrix-strict-explicit-alpha-delta-rule-router.json"
ALPHA_SIDE_ROUTER = DOCS / "prime-matrix-strict-alpha-side-primitive-rule-router.json"
DETERMINISTIC_ALPHA_ROUTER = DOCS / "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"
LPF_CANDIDATE_ROUTER = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"
SIGNED_WEIGHT_ROUTER = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"
ALPHA_TERMINAL_ROUTER = DOCS / "prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json"

EXPLICIT_RULE = "ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter"
ALPHA_SIDE_RULE = "ActualNoncanonicalSourceTupleToAlphaSidePrimitiveRuleLedger"
DELTA_SIDE_RULE = "ActualNoncanonicalSourceTupleToDeltaSidePrimitiveRuleLedger"
PAIRING_COMPAT = "AlphaDeltaPairingCompatibilityBeforeCauchyLedger"
NONZERO_LOCAL = "PrimitiveRuleNonzeroSignLocalFactorLedger"
ALPHA_ROW_MAP = "DeterministicAlphaPrimitiveRowEmissionMapLedger"
LPF_CANDIDATE_MAP = "LPFOwnershipAlphaCandidateRowEmissionMapLedger"
SIGNED_SUMMAND = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
ALPHA_DOMAIN = "ActualNoncanonicalAlphaSourceTupleDomainLedger"
ALPHA_WEIGHT = "AlphaPrimitiveCoefficientWeightFormulaLedger"
ALPHA_OUTPUT = "AlphaPrimitiveRowUVKeySignLocalFactorOutputLedger"
ALPHA_RETURN = "AlphaPrimitiveRuleFailureNamedReturnLedger"
FIXED_KEY_O1 = "FixedKeyExactUVLocalMultiplicityO1Ledger"
ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
EXACTUV_RETURN = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
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
        EXPLICIT_RULE_ROUTER,
        ALPHA_SIDE_ROUTER,
        DETERMINISTIC_ALPHA_ROUTER,
        LPF_CANDIDATE_ROUTER,
        SIGNED_WEIGHT_ROUTER,
        ALPHA_TERMINAL_ROUTER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_sync_chain() -> list[dict[str, str]]:
    """列出 product-window 显式规则到 signed summand 的同步链。"""
    return [
        {
            "from": EXPLICIT_RULE,
            "to": f"{ALPHA_SIDE_RULE} AND {DELTA_SIDE_RULE} AND {PAIRING_COMPAT} AND {NONZERO_LOCAL}",
            "meaning": "显式 alpha/delta 规则先拆成 alpha-side、delta-side、配对兼容和非零 local factor。",
        },
        {
            "from": ALPHA_SIDE_RULE,
            "to": ALPHA_ROW_MAP,
            "meaning": "alpha-side primitive rule 的第一生产性字段是确定性 alpha primitive row 发射映射。",
        },
        {
            "from": ALPHA_ROW_MAP,
            "to": f"{LPF_CANDIDATE_MAP} AND {SIGNED_SUMMAND}",
            "meaning": "LPF ownership 支付候选 row ownership/几何索引；actual row 仍需 signed summand 表达式。",
        },
        {
            "from": SIGNED_SUMMAND,
            "to": "primitive summand row, side, signed weight, local factor, exact (u,v), branch key, failure return",
            "meaning": "signed summand 表达式必须在 Phi/payment 推前前逐行给出所有 signed 字段。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    previous = data["previous"]
    explicit = data["explicit"]
    alpha_side = data["alpha_side"]
    deterministic = data["deterministic"]
    lpf_candidate = data["lpf_candidate"]
    signed_weight = data["signed_weight"]
    alpha_terminal = data["alpha_terminal"]

    explicit_active = (
        previous.get("next_primary_attack_target") == EXPLICIT_RULE
        and previous.get("precauchy_declaration_removed_from_product_window_first_target") is True
    )
    explicit_imported = (
        explicit.get("explicit_alpha_delta_rule_router_closed") is True
        and explicit.get("next_direct_attack_target") == ALPHA_SIDE_RULE
    )
    alpha_imported = (
        alpha_side.get("alpha_side_primitive_rule_router_closed") is True
        and alpha_side.get("actual_noncanonical_alpha_side_primitive_rule_proved") is False
    )
    deterministic_imported = (
        deterministic.get("deterministic_alpha_row_emission_map_router_closed") is True
        and deterministic.get("deterministic_alpha_primitive_row_emission_map_proved") is False
    )
    lpf_candidate_closed = (
        lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True
        and lpf_candidate.get("next_direct_attack_target") == SIGNED_SUMMAND
    )
    signed_summand_open = (
        signed_weight.get("primitive_summand_signed_weight_expression_proved") is False
        and signed_weight.get("next_direct_attack_target") == SIGNED_SUMMAND
    )
    alpha_terminal_sync_imported = (
        alpha_terminal.get("precauchy_alpha_terminal_sync_closed") is True
        and alpha_terminal.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )

    return [
        row(
            "ProductWindowExplicitAlphaDeltaActiveBeforeSync",
            explicit_active,
            False,
            "上一层 product-window declaration/LPF ownership 同步把第一硬点推进到显式 alpha/delta constructor rule。",
            EXPLICIT_RULE,
        ),
        row(
            "StrictExplicitRuleImported",
            explicit_imported,
            False,
            "strict explicit-rule 证书把显式规则拆成 alpha-side、delta-side、配对兼容和非零 local factor。",
            f"{ALPHA_SIDE_RULE} AND {DELTA_SIDE_RULE} AND {PAIRING_COMPAT} AND {NONZERO_LOCAL}",
        ),
        row(
            "AlphaSidePrimitiveRuleImported",
            alpha_imported,
            False,
            "alpha-side primitive rule 继续拆成定义域、确定性 row 发射、权重、输出和失败回流。",
            f"{ALPHA_DOMAIN} AND {ALPHA_ROW_MAP} AND {ALPHA_WEIGHT} AND {ALPHA_OUTPUT} AND {ALPHA_RETURN}",
        ),
        row(
            "DeterministicAlphaMapImported",
            deterministic_imported,
            False,
            "确定性 alpha row 发射映射仍需前推前 row formula；不能从 payment 或外部谱反选。",
            ALPHA_ROW_MAP,
        ),
        row(
            "LPFCandidateRowMapClosed",
            lpf_candidate_closed,
            True,
            "LPF ownership 可支付候选合数 row 的唯一 p 层/cofactor 索引与 unsigned skeleton 兼容性。",
            LPF_CANDIDATE_MAP,
        ),
        row(
            "LPFCandidateMapNotSignedPrimitiveMap",
            lpf_candidate.get("lpf_candidate_map_not_signed_primitive_map") is True,
            True,
            "候选 row map 只给 ownership 和几何索引，不给 signed weight、local factor 或 primitive summand 表达式。",
            SIGNED_SUMMAND,
        ),
        row(
            "PrimitiveSummandSignedExpressionStillOpen",
            signed_summand_open,
            False,
            "逐行 signed 权重公式已经压到 actual noncanonical primitive summand signed expression before pushforward。",
            SIGNED_SUMMAND,
        ),
        row(
            "AlphaTerminalSyncImportedButNotProof",
            alpha_terminal_sync_imported,
            False,
            "productive alpha-side 下游会接到 PDEC/CleanKLS 与模型余量，但这不是 signed summand 表达式证明。",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger",
        ),
        row(
            "SiblingFieldsStillOpen",
            True,
            False,
            "delta-side、pairing、nonzero/local-factor、fixed-key ExactUV、orientation 和 internal transition 仍并行开放。",
            f"{DELTA_SIDE_RULE} AND {PAIRING_COMPAT} AND {NONZERO_LOCAL} AND {FIXED_KEY_O1} AND {ORIENTATION} AND {EXACTUV_RETURN} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "ExplicitAlphaDeltaRemovedFromProductWindowFirstTarget",
            all(
                [
                    explicit_active,
                    explicit_imported,
                    alpha_imported,
                    deterministic_imported,
                    lpf_candidate_closed,
                    signed_summand_open,
                ]
            ),
            False,
            "显式 alpha/delta 旧名已被拆到 signed summand 表达式与并行兄弟字段，不应继续作为单名第一主攻。",
            SIGNED_SUMMAND,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只同步 product-window constructor 前沿，不证明 signed expression、delta/pairing、ExactUV 或终端排斥。",
            "row_column_unconditional_closed=false",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    data = {
        "previous": load_json(PREVIOUS),
        "explicit": load_json(EXPLICIT_RULE_ROUTER),
        "alpha_side": load_json(ALPHA_SIDE_ROUTER),
        "deterministic": load_json(DETERMINISTIC_ALPHA_ROUTER),
        "lpf_candidate": load_json(LPF_CANDIDATE_ROUTER),
        "signed_weight": load_json(SIGNED_WEIGHT_ROUTER),
        "alpha_terminal": load_json(ALPHA_TERMINAL_ROUTER),
    }
    rows = build_rows(data)
    latest_open_basis = (
        f"{SIGNED_SUMMAND} AND {ALPHA_DOMAIN} AND {ALPHA_WEIGHT} AND {ALPHA_OUTPUT} AND {ALPHA_RETURN} "
        f"AND {DELTA_SIDE_RULE} AND {PAIRING_COMPAT} AND {NONZERO_LOCAL} AND {FIXED_KEY_O1} "
        f"AND {ORIENTATION} AND {EXACTUV_RETURN} AND {INTERNAL_TRANSITION} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_explicit_alpha_delta_signed_summand_sync_router",
        "status": "product_window_explicit_alpha_delta_reduced_to_signed_summand_expression_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_absence_not_used": True,
        "old_primary_attack_target": EXPLICIT_RULE,
        "strict_explicit_rule_imported": data["explicit"].get("explicit_alpha_delta_rule_router_closed") is True,
        "alpha_side_primitive_rule_imported": data["alpha_side"].get("alpha_side_primitive_rule_router_closed") is True,
        "deterministic_alpha_map_imported": data["deterministic"].get("deterministic_alpha_row_emission_map_router_closed") is True,
        "lpf_candidate_row_map_closed": data["lpf_candidate"].get("lpf_candidate_row_emission_map_closed") is True,
        "primitive_summand_signed_expression_still_open": True,
        "productive_alpha_terminal_sync_imported": data["alpha_terminal"].get("precauchy_alpha_terminal_sync_closed") is True,
        "explicit_alpha_delta_removed_from_product_window_first_target": rows[-2]["closed"],
        "next_primary_attack_target": SIGNED_SUMMAND,
        "parallel_primary_attack_targets": [
            ALPHA_DOMAIN,
            ALPHA_WEIGHT,
            ALPHA_OUTPUT,
            ALPHA_RETURN,
            DELTA_SIDE_RULE,
            PAIRING_COMPAT,
            NONZERO_LOCAL,
            FIXED_KEY_O1,
            ORIENTATION,
            EXACTUV_RETURN,
            INTERNAL_TRANSITION,
            RATE,
            DSTRUCTURE,
        ],
        "latest_open_basis_summary": latest_open_basis,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "本步把 product-window 最新第一硬点 `ExplicitAlphaDeltaPrimitiveConstructorRuleForActualNoncanonicalEmitter` "
            "接入 strict explicit-rule、alpha-side primitive rule、deterministic alpha map、LPF candidate-row map "
            "和 pointwise signed weight formula 证书。结论是：LPF/Phi 的精确最小素因子分桶还能支付 "
            "alpha 侧候选 row ownership/几何索引；但 actual signed primitive summand expression before pushforward "
            "仍未构造，delta/pairing/nonzero、ExactUV、orientation 和 terminal 验收仍并行开放。"
        ),
        "sync_chain": build_sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window explicit alpha/delta signed-summand sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "**核验日期：** `2026-05-26`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_explicit_rule_imported={fmt_bool(result['strict_explicit_rule_imported'])}",
        f"alpha_side_primitive_rule_imported={fmt_bool(result['alpha_side_primitive_rule_imported'])}",
        f"deterministic_alpha_map_imported={fmt_bool(result['deterministic_alpha_map_imported'])}",
        f"lpf_candidate_row_map_closed={fmt_bool(result['lpf_candidate_row_map_closed'])}",
        f"primitive_summand_signed_expression_still_open={fmt_bool(result['primitive_summand_signed_expression_still_open'])}",
        f"explicit_alpha_delta_removed_from_product_window_first_target={fmt_bool(result['explicit_alpha_delta_removed_from_product_window_first_target'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下游同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_chain"]:
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
    for item in result["gates"]:
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
            "## 3. 最新保留基",
            "",
            "```text",
            result["latest_open_basis_summary"],
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
            "\n".join(result["parallel_primary_attack_targets"]),
            "```",
            "",
            "严格含义：本证书只同步 explicit alpha/delta 到 signed summand 接口，不证明行/列命题。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        "explicit_alpha_delta_removed_from_product_window_first_target="
        f"{fmt_bool(result['explicit_alpha_delta_removed_from_product_window_first_target'])}"
    )
    print(f"next_primary_attack_target={result['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
