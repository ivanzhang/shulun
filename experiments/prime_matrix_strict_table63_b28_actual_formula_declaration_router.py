#!/usr/bin/env python3
"""生成 strict Table 6.3 b=28 实际表公式/算法工件审计证书。

用法示例：
  python3 experiments/prime_matrix_strict_table63_b28_actual_formula_declaration_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table63-b28-actual-formula-declaration-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-table63-b28-actual-formula-declaration-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table63-b28-actual-formula-declaration-router.md"

PREVIOUS = DOCS / "prime-matrix-strict-table63-b28-zero-input-formula-binding-router.json"
TABLE63_ROW = DOCS / "prime-matrix-strict-machine-readable-dusart-table63-router.json"
EPS_ALGORITHM = DOCS / "prime-matrix-strict-psi-epsilon-table-algorithm-router.json"
GENERATOR = DOCS / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [PREVIOUS, TABLE63_ROW, EPS_ALGORITHM, GENERATOR, CLAIM_STATUS]

TARGET = "Table63B28ActualTableFormulaDeclarationOrExternalAlgorithmArtifactLedger"
TABLE_ROW = "Table63B28PublishedRowStatementLedger"
P51_USE = "Table63B28P51UseSiteLedger"
SOURCE_BOUNDARY = "Dusart10020442SourceBoundaryForTable63Ledger"
MISSING_ALGO = "Table63B28ExternalAlgorithmArtifactMissingLedger"
SUBMITTED_SOURCE = "DusartEpsSubmittedTableAlgorithmArtifactLedger"
INDEPENDENT_REGEN = "IndependentTable63B28RegenerationFromExplicitFormulaLedger"
PSI_CONVENTION = "Table63B28PsiVsPsi0EndpointConventionLedger"
KERNEL = "Table63B28KernelTruncationAndSmoothingConventionLedger"
FINITE_RH = "Table63B28FiniteRHHeightEndpointAndZeroBlockLedger"
ZERO_TAIL = "Table63B28ZeroFreeTailConstantsAndStartHeightLedger"
BUDGET = "Table63B28PsiEpsilonBudgetPartitionLedger"
ROUNDING = "Table63B28DirectedUpperRoundingAndIntervalPropagationLedger"
HASH = "Table63B28ReproducibleComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
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


def source_facts() -> list[dict[str, str]]:
    """记录已核验的 arXiv 源文件事实。"""
    return [
        {
            "fact": "intro_dependency",
            "source": "arXiv:1002.0442 source, introduction",
            "meaning": "文章说明 psi/theta 有效估计依赖有限 RH 验证与显式零点自由区。",
            "status": "source boundary confirmed",
        },
        {
            "fact": "gourdon_kadiri_boundary",
            "source": "arXiv:1002.0442 source, bibliography/introduction",
            "meaning": "Gourdon 10^13 零点与 Kadiri 零点自由区是外部来源边界。",
            "status": "external inputs identified",
        },
        {
            "fact": "table_eps_b28",
            "source": "arXiv:1002.0442 source, table labeled Values of epsilon(x) for psi and theta",
            "meaning": "表行给出 b=28, epsilon_psi=2.224E-5, epsilon_theta=2.308E-5。",
            "status": "published row statement confirmed",
        },
        {
            "fact": "prop_eta0_use",
            "source": "arXiv:1002.0442 source, Proposition theta(x)-x < x/36260 proof",
            "meaning": "证明使用中段 1.00002841 与 eps_28<=0.00002224 完成高尾拼接。",
            "status": "use site confirmed",
        },
        {
            "fact": "missing_generator",
            "source": "arXiv:1002.0442 source, bibliography item dusart:eps",
            "meaning": "更底层的 psi/theta 大值估计被指向一个 submitted 源，当前 arXiv 源未给出可复现表生成算法。",
            "status": "algorithm artifact absent from this source",
        },
    ]


def artifact_requirements() -> list[dict[str, str]]:
    """定义能关闭实际表公式/算法工件所需的最小字段。"""
    return [
        {
            "field": "formula_convention",
            "needed": f"{PSI_CONVENTION} AND {KERNEL}",
            "why": "必须知道表值使用 psi 还是 psi_0，以及核、截断、平滑、端点规则。",
        },
        {
            "field": "zero_inputs",
            "needed": f"{FINITE_RH} AND {ZERO_TAIL}",
            "why": "必须知道有限零点块和零点自由尾项如何进入同一个公式。",
        },
        {
            "field": "budget",
            "needed": BUDGET,
            "why": "必须证明所有误差项总和小于 b=28 的 2.224E-5 cap。",
        },
        {
            "field": "output_discipline",
            "needed": f"{ROUNDING} AND {HASH}",
            "why": "必须给出外向舍入、区间传播和可复现输出。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造实际表公式/算法工件审计证书。"""
    previous = load_json(PREVIOUS)
    table63 = load_json(TABLE63_ROW)
    algorithm = load_json(EPS_ALGORITHM)
    generator = load_json(GENERATOR)

    active = previous.get("next_direct_attack_target") == TARGET
    table_row_confirmed = table63.get("machine_readable_table63_b28_row_closed") is True
    p51_use_confirmed = table63.get("machine_readable_table63_external_row_usable") is True
    dependency_graph_closed = algorithm.get("p51_dependency_graph_closed") is True
    extraction_closed = generator.get("epsilon_table_statement_extraction_closed") is True

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            previous.get("counterexample_assumption_only") is True
            and previous.get("row_column_unconditional_closed") is False,
            True,
            "本步仍只审计假设反例链可调用的 Table 6.3 表算法输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ActualFormulaDeclarationGateActive",
            active,
            True,
            "上一证书已证明零点输入绑定必须先取得 b=28 的实际表公式或外部算法工件。",
            TARGET,
        ),
        row(
            TABLE_ROW,
            table_row_confirmed and extraction_closed,
            False,
            "b=28 的公开表行陈述已经确认：epsilon_psi=2.224E-5。",
            "statement only, not generator",
        ),
        row(
            P51_USE,
            p51_use_confirmed and dependency_graph_closed,
            False,
            "该表行在 Proposition 5.1 高尾拼接中可用，外部路线可接受。",
            "external Table 6.3 accepted",
        ),
        row(
            SOURCE_BOUNDARY,
            True,
            True,
            "arXiv 源文件给出来源边界：有限 RH 验证、零点自由区、表行和 P5.1 使用点都能定位。",
            "source boundary closed",
        ),
        row(
            MISSING_ALGO,
            True,
            True,
            "当前 arXiv 源文件没有给出生成 Table 6.3 的完整显式公式算法、舍入日志或 hash。",
            f"{SUBMITTED_SOURCE} OR {INDEPENDENT_REGEN}",
        ),
        row(
            TARGET,
            False,
            False,
            "实际表公式/算法工件尚未闭合：已知的是表行和使用点，不是可复现生成机制。",
            f"{SUBMITTED_SOURCE} OR {INDEPENDENT_REGEN}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "Table 6.3 实际表公式审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_table63_b28_actual_formula_declaration_router",
        "status": "table63_b28_published_row_and_use_site_confirmed_algorithm_artifact_missing",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "arxiv_source_boundary_checked": True,
        "table63_b28_published_row_statement_closed": table_row_confirmed and extraction_closed,
        "table63_b28_p51_use_site_closed": p51_use_confirmed and dependency_graph_closed,
        "table63_b28_external_row_accepted": p51_use_confirmed,
        "table63_b28_actual_formula_declaration_closed": False,
        "table63_b28_external_algorithm_artifact_present": False,
        "table63_b28_independent_regeneration_closed": False,
        "table63_b28_zero_input_binding_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "source_facts": source_facts(),
        "artifact_requirements": artifact_requirements(),
        "replacement_self_contained": {
            TARGET: f"{SUBMITTED_SOURCE} OR {INDEPENDENT_REGEN}",
            INDEPENDENT_REGEN: (
                f"{PSI_CONVENTION} AND {KERNEL} AND {FINITE_RH} AND {ZERO_TAIL} "
                f"AND {BUDGET} AND {ROUNDING} AND {HASH}"
            ),
        },
        "next_direct_attack_target": INDEPENDENT_REGEN,
        "parallel_attack_targets": [SUBMITTED_SOURCE, PSI_CONVENTION, KERNEL, FINITE_RH, ZERO_TAIL, BUDGET, ROUNDING, HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "arXiv 源文件足以确认 Table 6.3 的 b=28 表行和 Proposition 5.1 的使用点，"
            "因此外部表行路线可接受；但它没有给出作者侧可复现的表生成算法。"
            "实际闭合只剩二选一：取得 `dusart:eps`/等价外部算法工件，或独立重建 Table 6.3 b=28 的显式公式、"
            "零点输入、预算、外向舍入和 hash。下一最窄点为独立重建输入基。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Table 6.3 b=28 实际表公式/算法工件审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"table63_b28_published_row_statement_closed={fmt_bool(result['table63_b28_published_row_statement_closed'])}",
        f"table63_b28_p51_use_site_closed={fmt_bool(result['table63_b28_p51_use_site_closed'])}",
        f"table63_b28_actual_formula_declaration_closed={fmt_bool(result['table63_b28_actual_formula_declaration_closed'])}",
        f"table63_b28_external_algorithm_artifact_present={fmt_bool(result['table63_b28_external_algorithm_artifact_present'])}",
        f"table63_b28_independent_regeneration_closed={fmt_bool(result['table63_b28_independent_regeneration_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 源文件事实",
        "",
        "| fact | source | meaning | status |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["source_facts"]:
        lines.append(
            f"| `{table_cell(item['fact'])}` | {table_cell(item['source'])} | "
            f"{table_cell(item['meaning'])} | {table_cell(item['status'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 工件需求",
            "",
            "| field | needed | why |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["artifact_requirements"]:
        lines.append(f"| `{table_cell(item['field'])}` | `{table_cell(item['needed'])}` | {table_cell(item['why'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"table63_b28_actual_formula_declaration_closed={fmt_bool(result['table63_b28_actual_formula_declaration_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
