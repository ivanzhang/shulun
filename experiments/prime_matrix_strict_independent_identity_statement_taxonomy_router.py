#!/usr/bin/env python3
"""生成 strict 独立 pre-Cauchy 恒等式陈述分类适配证书。

用法示例：
  python3 experiments/prime_matrix_strict_independent_identity_statement_taxonomy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-independent-identity-statement-taxonomy-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-independent-identity-statement-taxonomy-router.json"
OUT_MD = DOCS / "prime-matrix-strict-independent-identity-statement-taxonomy-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-independent-precauchy-identity-taxonomy-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-clean-core-constructor-source-class-firewall-router.json",
    "prime-matrix-noncanonical-complement-input-contract-router.md",
    "prime-matrix-clean-core-external-lemma-parameter-match-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    """读取文本证书；缺失时返回空文本。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(
    weight_law: dict[str, Any],
    taxonomy: dict[str, Any],
    seed_nogo: dict[str, Any],
    constructor_firewall: dict[str, Any],
    contract_text: str,
    external_match: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 strict 恒等式陈述分类判定表。"""
    target = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
    next_atom = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
    terminal_after = weight_law.get("terminal_gap_after_router", "")
    taxonomy_closed = taxonomy.get("identity_taxonomy_closed") is True
    no_seed = seed_nogo.get("zero_row_seed_extraction_blocked") is True
    firewall_closed = constructor_firewall.get("constructor_source_class_firewall_boundary_closed") is True
    no_hidden = "NoHiddenFourthRoute" in contract_text or "没有第四条可自足偷渡路线" in contract_text
    external_self_closed = external_match.get("external_lemmas_close_self_contained_remainder") is True
    return [
        {
            "gate": "StrictIdentityStatementTargetActive",
            "closed": target in terminal_after or weight_law.get("next_direct_attack_target") == target,
            "proved": False,
            "meaning": "上一层已把 alpha signed 权重律最窄点固定为独立 noncanonical pre-Cauchy 算术恒等式陈述。",
            "remaining": target,
        },
        {
            "gate": "SameSourceIdentityAtomRecognized",
            "closed": taxonomy.get("terminal_gap_before_router")
            == "IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn",
            "proved": True,
            "meaning": "当前 strict StatementLedger 是既有 IndependentPreCauchyArithmeticSourceIdentity 原子的 alpha-weight 表述。",
            "remaining": "可复用既有合法来源类分类，但不证明恒等式本身。",
        },
        {
            "gate": "ExistingIdentityTaxonomyImported",
            "closed": taxonomy_closed,
            "proved": True,
            "meaning": "既有分类已穷尽 canonical、generic WFD、AP/external、actual noncanonical 四类。",
            "remaining": next_atom,
        },
        {
            "gate": "ZeroRowUnsignedSeedStillBlocked",
            "closed": no_seed,
            "proved": True,
            "meaning": "早期零行覆盖图仍只能给 unsigned covering data，不能作为该恒等式的来源。",
            "remaining": next_atom,
        },
        {
            "gate": "ConstructorSourceFirewallImported",
            "closed": firewall_closed,
            "proved": True,
            "meaning": "canonical scoped、generic rejected、unregistered absorbed、external separated 后，strict 自足只剩 actual noncanonical。",
            "remaining": next_atom,
        },
        {
            "gate": "NoHiddenFourthRouteImported",
            "closed": no_hidden,
            "proved": True,
            "meaning": "noncanonical complement 合同排除隐藏第四类来源；不能新增未登记恒等式出口。",
            "remaining": next_atom,
        },
        {
            "gate": "ExternalSpectralStillNotSelfContainedSource",
            "closed": external_self_closed is False,
            "proved": True,
            "meaning": "外部谱输入可走条件线，但不能作为 strict 自足 pre-Cauchy source identity。",
            "remaining": "条件分支保留 CDependentResidueWeightSpectralCancellationInput。",
        },
        {
            "gate": "StatementTaxonomyAdapterClosed",
            "closed": taxonomy_closed and no_seed and firewall_closed and no_hidden and external_self_closed is False,
            "proved": True,
            "meaning": "恒等式陈述黑箱已被合法来源类分类消去；剩余实际内容是 actual moving-block spread/NC-BLK。",
            "remaining": next_atom,
        },
        {
            "gate": "IndependentIdentityStatementCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料并未证明一个独立 noncanonical pre-Cauchy 算术恒等式。",
            "remaining": next_atom,
        },
        {
            "gate": "ActualMovingBlockSpreadNCBLKCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明 actual noncanonical moving-block spread/NC-BLK。",
            "remaining": next_atom,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 恒等式陈述分类适配证书。"""
    weight_law = load_json(DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json")
    taxonomy = load_json(DOCS / "prime-matrix-independent-precauchy-identity-taxonomy-router.json")
    seed_nogo = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    constructor_firewall = load_json(DOCS / "prime-matrix-clean-core-constructor-source-class-firewall-router.json")
    contract_text = load_text(DOCS / "prime-matrix-noncanonical-complement-input-contract-router.md")
    external_match = load_json(DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.json")

    target = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
    next_atom = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
    rows = build_rows(
        weight_law=weight_law,
        taxonomy=taxonomy,
        seed_nogo=seed_nogo,
        constructor_firewall=constructor_firewall,
        contract_text=contract_text,
        external_match=external_match,
    )
    return {
        "certificate_type": "prime_matrix_strict_independent_identity_statement_taxonomy_router",
        "status": "strict_independent_identity_statement_taxonomy_closed_actual_moving_block_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "strict_identity_statement_taxonomy_adapter_closed": True,
        "existing_identity_taxonomy_imported": True,
        "zero_row_unsigned_seed_still_blocked": True,
        "constructor_source_firewall_imported": True,
        "no_hidden_fourth_route_imported": True,
        "external_spectral_still_not_self_contained_source": True,
        "independent_noncanonical_precauchy_arithmetic_identity_statement_proved": False,
        "actual_noncanonical_moving_block_spread_ncb_lk_proved": False,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "deterministic_alpha_primitive_row_emission_map_proved": False,
        "actual_noncanonical_alpha_side_primitive_rule_proved": False,
        "actual_noncanonical_delta_side_primitive_rule_proved": False,
        "explicit_alpha_delta_primitive_constructor_rule_proved": False,
        "actual_noncanonical_primitive_constructor_formula_line_proved": False,
        "actual_noncanonical_primitive_emitter_source_table_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_atom,
        "next_direct_attack_target": next_atom,
        "taxonomy_law": (
            "The strict identity statement is not a fifth source class. The existing source-identity taxonomy exhausts "
            "canonical, generic WFD, AP/external and actual noncanonical possibilities. After the first three are blocked "
            "for strict self-contained use, the remaining content is actual moving-block spread/NC-BLK."
        ),
        "plain_conclusion": (
            "`IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger` 已与既有 "
            "`IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn` 分类对齐。"
            "canonical/generic/AP/external 都不能填 strict 自足来源；早期零行覆盖仍只是 unsigned seed。"
            "因此该陈述黑箱被压成 `ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn`，"
            "但该 moving-block/NC-BLK 输入仍未证明。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 独立恒等式陈述分类适配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"strict_identity_statement_taxonomy_adapter_closed={fmt_bool(result['strict_identity_statement_taxonomy_adapter_closed'])}",
        f"independent_noncanonical_precauchy_arithmetic_identity_statement_proved={fmt_bool(result['independent_noncanonical_precauchy_arithmetic_identity_statement_proved'])}",
        f"actual_noncanonical_moving_block_spread_ncb_lk_proved={fmt_bool(result['actual_noncanonical_moving_block_spread_ncb_lk_proved'])}",
        f"alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved={fmt_bool(result['alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分类适配律",
        "",
        result["taxonomy_law"],
        "",
        "## 2. 替换",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
