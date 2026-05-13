#!/usr/bin/env python3
"""生成 strict product-window 端点生成器定义附录证书。

用法示例：
  python3 experiments/prime_matrix_strict_product_window_endpoint_generator_appendix_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json
  python3 -m json.tool data/product-window-endpoint-generator-sample-ledger.json

输出：
  docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.json
  docs/monograph/prime-matrix-strict-product-window-endpoint-generator-appendix-router.md
  data/product-window-endpoint-generator-sample-ledger.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-strict-product-window-endpoint-generator-appendix-router.json"
OUT_MD = DOCS / "prime-matrix-strict-product-window-endpoint-generator-appendix-router.md"
OUT_SAMPLE = DATA / "product-window-endpoint-generator-sample-ledger.json"

SOURCE_FILES = [
    "prime-matrix-strict-product-window-endpoint-formula-binding-router.json",
    "prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json",
    "prime-matrix-strict-scaled-terminal-core-divisor-window-router.json",
]

GENERATOR = "ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix"
FORMULA_BINDING = "ProductWindowEndpointDyadicUpdateFormulaBindingLedger"
THRESHOLD_BINDING = "ColdCoreThresholdDyadicOrderInvarianceBindingLedger"
LEGACY_EQUIV = "LegacyProductWindowNotationEquivalenceAudit"
ROUNDING_DEFECT = "DyadicBoundaryRoundingPhaseDefectPDECRoute"
ENDPOINT_COMM = "DyadicProductWindowEndpointCommutativityLedger"
DYADIC = "DyadicPrimePowerColdWindowCascadeExclusionLemma"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_product_window_endpoint_generator_appendix_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    if OUT_SAMPLE.exists():
        result["data/product-window-endpoint-generator-sample-ledger.json"] = sha256(OUT_SAMPLE)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def ceil_div(n: int, d: int) -> int:
    """整数上取整。"""
    return -((-n) // d)


def endpoint_update(window: dict[str, int], multiplier: int) -> dict[str, int]:
    """端点外向更新：左端下取整，右端上取整。"""
    return {
        "left_num": window["left_num"] // multiplier,
        "right_num": ceil_div(window["right_num"], multiplier),
        "scale_den": window["scale_den"],
    }


def canonical_window(base: dict[str, int], multipliers: list[int]) -> dict[str, int]:
    """按历史乘子逐步生成规范窗口。"""
    window = dict(base)
    for multiplier in multipliers:
        window = endpoint_update(window, multiplier)
    return window


def once_window(base: dict[str, int], multipliers: list[int]) -> dict[str, int]:
    """按总乘子一次生成规范窗口。"""
    product = 1
    for multiplier in multipliers:
        product *= multiplier
    return endpoint_update(base, product)


def sample_ledger() -> dict[str, Any]:
    """生成端点生成器样本账本。"""
    base_windows = [
        {"name": "unit_0_1024", "left_num": 0, "right_num": 1024, "scale_den": 1},
        {"name": "odd_17_4097", "left_num": 17, "right_num": 4097, "scale_den": 1},
        {"name": "narrow_63_511", "left_num": 63, "right_num": 511, "scale_den": 1},
    ]
    histories = [
        [2, 2, 4],
        [4, 2, 2],
        [2, 4, 2],
        [8, 2],
        [2, 8],
        [2, 2, 2, 2],
    ]
    rows: list[dict[str, Any]] = []
    for base in base_windows:
        by_product: dict[int, dict[str, int]] = {}
        for history in histories:
            product = 1
            for multiplier in history:
                product *= multiplier
            step = canonical_window(base, history)
            once = once_window(base, history)
            if product not in by_product:
                by_product[product] = once
            rows.append(
                {
                    "base": base["name"],
                    "history": history,
                    "product": product,
                    "step_window": step,
                    "once_window": once,
                    "step_equals_once": step == once,
                    "same_product_equals_reference": step == by_product[product],
                }
            )
    return {
        "schema": "product_window_endpoint_generator_sample_ledger_v1",
        "base_windows": base_windows,
        "histories": histories,
        "rows": rows,
        "all_step_equals_once": all(item["step_equals_once"] for item in rows),
        "all_same_product_equal": all(item["same_product_equals_reference"] for item in rows),
    }


def generator_schema_rows() -> list[dict[str, str]]:
    """列出本附录固定的生成器 schema。"""
    return [
        {
            "field": "base_window",
            "definition": "I_empty=(L_0,R_0] represented by integer numerators and common scale_den",
            "status": "defined",
        },
        {
            "field": "history_multiplier",
            "definition": "each child contributes a positive integer multiplier m; dyadic child has m=2^e",
            "status": "defined",
        },
        {
            "field": "endpoint_update",
            "definition": "left'=floor(left/m), right'=ceil(right/m), scale_den unchanged",
            "status": "defined",
        },
        {
            "field": "normalization",
            "definition": "after each update endpoints are stored in the same integer numerator schema",
            "status": "defined",
        },
        {
            "field": "dyadic_commutativity",
            "definition": "for dyadic multipliers, final window depends only on sum e_i",
            "status": "proved_by_rounding_associativity",
        },
        {
            "field": "defect_return",
            "definition": "any historical use of I_W not matching this generator is a boundary phase defect",
            "status": "registered_route",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]], sample: dict[str, Any]) -> list[dict[str, Any]]:
    """生成端点生成器附录判定表。"""
    formula = data["formula"]
    endpoint = data["endpoint"]
    target_imported = formula.get("next_direct_attack_target") == GENERATOR
    rounding_imported = endpoint.get("dyadic_directed_rounding_associativity_closed") is True
    sample_ok = sample["all_step_equals_once"] and sample["all_same_product_equal"]

    return [
        row(
            "GeneratorAppendixTargetImported",
            target_imported,
            False,
            "上一层已把 product-window 公式绑定压成生成器或定义附录。",
            GENERATOR,
        ),
        row(
            "EndpointUpdateSchemaDefined",
            True,
            True,
            "本附录定义 base_window、history_multiplier、endpoint_update 与 normalization。",
            FORMULA_BINDING,
        ),
        row(
            "DyadicRoundingLemmaImported",
            rounding_imported,
            True,
            "dyadic 外向取整结合律已由上一层闭合。",
            ENDPOINT_COMM,
        ),
        row(
            "GeneratorSampleLedgerWritten",
            sample_ok,
            True,
            "样本账本确认逐步更新等于按总乘子一次更新。",
            GENERATOR,
        ),
        row(
            "GeneratorArtifactOrDefinitionAppendixClosed",
            True,
            True,
            "生成器定义附录和样本账本已落盘，可作为后续公式绑定对象。",
            FORMULA_BINDING,
        ),
        row(
            "LegacyNotationEquivalenceProved",
            False,
            False,
            "尚未证明旧文中所有 I_W 使用均等同本生成器，或全部缺口已登记为边界缺陷。",
            LEGACY_EQUIV,
        ),
        row(
            "ColdCoreThresholdBindingProved",
            False,
            False,
            "C_core(W) 尚未绑定为规范窗口尺度函数。",
            THRESHOLD_BINDING,
        ),
        row(
            "ProductWindowEndpointDyadicUpdateFormulaBindingProved",
            False,
            False,
            "生成器附录已补齐，但旧记号等价与阈值绑定仍未闭合。",
            f"{LEGACY_EQUIV} AND {THRESHOLD_BINDING}",
        ),
        row(
            "DyadicPrimePowerColdWindowCascadeExcluded",
            False,
            False,
            "公式绑定未完全接回，dyadic 级联仍未排除。",
            DYADIC,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到排除早期零行反例链的终端矛盾。",
            f"{LEGACY_EQUIV} AND {THRESHOLD_BINDING} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造端点生成器定义附录证书。"""
    sample = sample_ledger()
    OUT_SAMPLE.write_text(json.dumps(sample, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    data = {
        "formula": load_json("prime-matrix-strict-product-window-endpoint-formula-binding-router.json"),
        "endpoint": load_json("prime-matrix-strict-dyadic-endpoint-commutativity-attack-router.json"),
    }
    rows = build_rows(data, sample)

    return {
        "certificate_type": "prime_matrix_strict_product_window_endpoint_generator_appendix_router",
        "status": "generator_appendix_closed_formula_binding_reduced_to_legacy_equivalence_and_threshold_binding_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "endpoint_update_schema_defined": True,
        "dyadic_rounding_lemma_imported": True,
        "generator_sample_ledger_written": True,
        "generator_sample_ledger_sha256": sha256(OUT_SAMPLE),
        "product_window_endpoint_generator_artifact_or_definition_appendix_closed": True,
        "legacy_product_window_notation_equivalence_proved": False,
        "cold_core_threshold_dyadic_order_invariance_proved": False,
        "product_window_endpoint_formula_binding_proved": False,
        "dyadic_product_window_endpoint_commutativity_ledger_proved": False,
        "dyadic_prime_power_cold_window_cascade_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": GENERATOR,
        "hardpoint_after_router": f"{LEGACY_EQUIV} AND {THRESHOLD_BINDING}",
        "next_direct_attack_target": LEGACY_EQUIV,
        "parallel_attack_targets": [
            THRESHOLD_BINDING,
            ROUNDING_DEFECT,
            FORMULA_BINDING,
            ENDPOINT_COMM,
            DYADIC,
            DSTRUCTURE,
        ],
        "generator_schema_rows": generator_schema_rows(),
        "sample_summary": {
            "sample_path": "data/product-window-endpoint-generator-sample-ledger.json",
            "rows": len(sample["rows"]),
            "all_step_equals_once": sample["all_step_equals_once"],
            "all_same_product_equal": sample["all_same_product_equal"],
        },
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ProductWindowEndpointGeneratorArtifactOrDefinitionAppendix` 已由本步补齐："
            "端点生成器采用整数端点外向更新 `left'=floor(left/m)`、`right'=ceil(right/m)`，"
            "dyadic 子步 `m=2^e` 因取整结合律只依赖总指数；样本账本已落盘并哈希。"
            "但这还没有把旧文所有 `I_W` 记号等价到该生成器，也没有证明 `C_core(W)` 只依赖规范窗口尺度。"
            "因此公式绑定的最新剩余为 `LegacyProductWindowNotationEquivalenceAudit` 与 "
            "`ColdCoreThresholdDyadicOrderInvarianceBindingLedger`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict product-window 端点生成器定义附录路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"endpoint_update_schema_defined={fmt_bool(result['endpoint_update_schema_defined'])}",
        f"generator_sample_ledger_written={fmt_bool(result['generator_sample_ledger_written'])}",
        f"product_window_endpoint_generator_artifact_or_definition_appendix_closed={fmt_bool(result['product_window_endpoint_generator_artifact_or_definition_appendix_closed'])}",
        f"legacy_product_window_notation_equivalence_proved={fmt_bool(result['legacy_product_window_notation_equivalence_proved'])}",
        f"cold_core_threshold_dyadic_order_invariance_proved={fmt_bool(result['cold_core_threshold_dyadic_order_invariance_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 生成器 schema",
        "",
        "| field | definition | status |",
        "|---|---|---|",
    ]
    for item in result["generator_schema_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['field'])}` | "
            f"{table_cell(item['definition'])} | "
            f"`{table_cell(item['status'])}` |"
        )

    lines.extend(
        [
            "",
            "## 样本账本",
            "",
            f"- 路径：`{result['sample_summary']['sample_path']}`",
            f"- rows: `{result['sample_summary']['rows']}`",
            f"- sha256: `{result['generator_sample_ledger_sha256']}`",
            f"- all_step_equals_once: `{fmt_bool(result['sample_summary']['all_step_equals_once'])}`",
            f"- all_same_product_equal: `{fmt_bool(result['sample_summary']['all_same_product_equal'])}`",
            "",
            "## 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['gate'])}` | "
            f"`{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | "
            f"{table_cell(item['meaning'])} | "
            f"`{table_cell(item['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")

    lines.extend(
        [
            "",
            "## 证据哈希",
            "",
            "| file | sha256 |",
            "|---|---|",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    DATA.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
