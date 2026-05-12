#!/usr/bin/env python3
"""生成 strict psi epsilon 表计算算法路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_psi_epsilon_table_algorithm_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-psi-epsilon-table-algorithm-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-algorithm-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-algorithm-router.md"

CONVENTION = MONOGRAPH / "prime-matrix-strict-same-explicit-formula-convention-router.json"
GENERATOR = MONOGRAPH / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
VERIFIED_INPUT = MONOGRAPH / "prime-matrix-strict-verified-zero-zero-free-tail-input-router.json"
TRANSITION = MONOGRAPH / "prime-matrix-strict-finite-verified-zero-tail-transition-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [CONVENTION, GENERATOR, VERIFIED_INPUT, TRANSITION, CLAIM_STATUS]

TARGET = "PsiEpsilonTableComputationAlgorithmLedger"
P51_GRAPH = "DusartP51DependencyGraphForPsiEpsilonLedger"
TABLE63 = "MachineReadableDusartTable63EpsilonPsiLedger"
MIDDLE_SOURCE = "MiddlePsiUpper100002841SourceLedger"
EPS28_SOURCE = "EpsilonPsi28Table63SourceLedger"
TABLE64 = "ThetaLessThanIdentityTable64To8e11SourceLedger"
ZERO_INPUT_BINDING = "VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger"
INTERVAL = "PsiEpsilonIntervalPropagationAndMonotonicityLedger"
HASH = "ReproduciblePsiEpsilonTableComputationHashLedger"
ROUNDING = "DirectedRoundingAndIntervalPropagationBudgetLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

DUSART_URL = "https://arxiv.org/abs/1002.0442"
DUSART_PDF = "https://arxiv.org/pdf/1002.0442"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


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


def source_evidence() -> list[dict[str, str]]:
    """记录外部原文中可安全依赖的结构边界。"""
    return [
        {
            "item": "finite RH and zero-free lineage",
            "source": DUSART_PDF,
            "location": "introduction, lines 38-48 in extracted PDF view",
            "meaning": "psi/theta estimates depend on finite zeta-zero verification and explicit zero-free regions.",
        },
        {
            "item": "Proposition 5.1 dependency graph",
            "source": DUSART_PDF,
            "location": "Proposition 5.1 proof, extracted lines 291-303",
            "meaning": "theta<x to 8e11, psi-theta lower gap, middle psi upper, and epsilon_28 are all used.",
        },
        {
            "item": "Table 6.3 epsilon psi at b=28",
            "source": DUSART_PDF,
            "location": "Table 6.3, extracted lines 1400-1412",
            "meaning": "the published table contains epsilon_psi(28)=2.224E-5.",
        },
        {
            "item": "table interval statement",
            "source": DUSART_PDF,
            "location": "Theorem 5.2 proof, extracted lines 324-340",
            "meaning": "the paper states table lines are valid between successive b_i for Tables 6.4 and 6.5.",
        },
    ]


def dependency_graph() -> list[dict[str, str]]:
    """列出 P5.1 中被 epsilon 表算法必须支撑的节点。"""
    return [
        {
            "node": "theta(x)<x for x<=8e11",
            "role": "left finite table input",
            "status": "published Table 6.4 route identified; repository self-contained table-to-8e11 proof open",
            "ledger": TABLE64,
        },
        {
            "node": "psi(x)<1.00002841x on 8e11<=x<=e^28",
            "role": "middle strip psi upper input",
            "status": "constant appears in P5.1 proof; source/generator not yet isolated",
            "ledger": MIDDLE_SOURCE,
        },
        {
            "node": "psi(x)-theta(x)>0.9999sqrt(x)",
            "role": "middle strip subtraction input",
            "status": "dependency already separated in Dusart analytic-kernel router",
            "ledger": "PsiMinusThetaLowerGap09999SqrtSelfContainedLedger",
        },
        {
            "node": "epsilon_psi(28)<=0.00002224",
            "role": "high tail psi input",
            "status": "published Table 6.3 row b=28 identified; reproducible generator open",
            "ledger": EPS28_SOURCE,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 psi epsilon 表计算算法证书。"""
    convention = load_json(CONVENTION)
    generator = load_json(GENERATOR)
    verified_input = load_json(VERIFIED_INPUT)
    transition = load_json(TRANSITION)
    active = convention.get("next_direct_attack_target") == TARGET
    p51_graph_closed = active and generator.get("epsilon_table_statement_extraction_closed") is True
    source_boundary_identified = verified_input.get("zero_input_source_extraction_closed") is True
    bridge_taxonomy_ready = transition.get("common_variable_interface_taxonomy_closed") is True
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            convention.get("counterexample_assumption_only") is True
            and convention.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计假设反例链可调用的 psi epsilon 表算法，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "PsiEpsilonTableComputationAlgorithmGateActive",
            active,
            True,
            "同一显式公式口径证书已把下一最窄点压到表计算算法。",
            TARGET,
        ),
        row(
            P51_GRAPH,
            p51_graph_closed,
            True,
            "Dusart P5.1 的表输入依赖图已从原文定位：左有限表、中段 psi 上界、psi-theta 下界和高尾 epsilon_28。",
            "dependency graph closed, computation algorithm still open",
        ),
        row(
            "PublishedSourceBoundaryIdentified",
            source_boundary_identified,
            True,
            "原文说明这些改进依赖有限 RH 验证和零点自由区；仓库已抽出 Gourdon/Kadiri 等来源边界。",
            ZERO_INPUT_BINDING,
        ),
        row(
            "BridgeCommonVariablesAlreadyTaxonomized",
            bridge_taxonomy_ready,
            True,
            "有限零点窗口、零点自由尾项、显式公式、预算和 hash 的共同变量表已关闭分类。",
            f"{ZERO_INPUT_BINDING} AND {HASH}",
        ),
        row(
            EPS28_SOURCE,
            True,
            False,
            "Table 6.3 给出 b=28 的 epsilon_psi 数值；这可关闭表值来源定位，但不是可复现算法证明。",
            f"{TABLE63} AND {HASH}",
        ),
        row(
            MIDDLE_SOURCE,
            False,
            False,
            "1.00002841 是中段最薄余量处的关键常数；当前只在 P5.1 中定位到使用点，未定位其生成公式和核验方式。",
            f"{TABLE63} OR {TABLE64} OR explicit middle psi computation source",
        ),
        row(
            TABLE63,
            False,
            False,
            "需要把 Table 6.3 转成机器可读表，并证明每个值的生成规则、舍入方向和适用区间。",
            f"{ZERO_INPUT_BINDING} AND {INTERVAL} AND {HASH}",
        ),
        row(
            TABLE64,
            False,
            False,
            "需要 theta<x 到 8e11 的表源、节点覆盖和直接计算证书；仓库现有自足有限桥只到 20000。",
            "ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger",
        ),
        row(
            ZERO_INPUT_BINDING,
            False,
            False,
            "需要证明有限零点验证和零点自由尾项按同一表算法进入 Table 6.3，而不是只作为外部背景。",
            "LargeFiniteRHVerificationForPsiEpsilonTableLedger AND ExplicitZeroFreeRegionForTableTailLedger",
        ),
        row(
            INTERVAL,
            False,
            False,
            "需要证明表格值如何覆盖连续区间，特别是 8e11 到 e^28 的中段和 x>=e^28 的高尾。",
            TARGET,
        ),
        row(
            HASH,
            False,
            False,
            "需要原始计算工件、版本、输入哈希、输出哈希和外向舍入日志。",
            "reproducible computation artifact",
        ),
        row(
            TARGET,
            False,
            False,
            "当前关闭的是 P5.1 依赖图和外部来源边界，不是表计算算法自足闭合。",
            f"{MIDDLE_SOURCE} AND {TABLE63} AND {TABLE64} AND {ZERO_INPUT_BINDING} AND {INTERVAL} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "psi epsilon 表算法审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_psi_epsilon_table_algorithm_router",
        "status": "psi_epsilon_table_algorithm_dependency_graph_closed_reproducible_algorithm_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "p51_dependency_graph_closed": p51_graph_closed,
        "published_source_boundary_identified": source_boundary_identified,
        "bridge_common_variables_taxonomized": bridge_taxonomy_ready,
        "epsilon_psi_28_source_located": True,
        "middle_psi_upper_100002841_source_closed": False,
        "machine_readable_table63_closed": False,
        "theta_table64_to_8e11_source_closed": False,
        "zero_input_binding_to_table_formula_closed": False,
        "psi_epsilon_interval_propagation_closed": False,
        "reproducible_table_hash_closed": False,
        "table_computation_algorithm_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_sources_used": source_evidence(),
        "dependency_graph": dependency_graph(),
        "replacement_self_contained": {
            TARGET: f"{MIDDLE_SOURCE} AND {TABLE63} AND {TABLE64} AND {ZERO_INPUT_BINDING} AND {INTERVAL} AND {HASH}",
            MIDDLE_SOURCE: "must locate or reproduce the source of 1.00002841 before the middle strip budget can be certified",
        },
        "next_direct_attack_target": MIDDLE_SOURCE,
        "parallel_attack_targets": [TABLE63, TABLE64, ZERO_INPUT_BINDING, INTERVAL, HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "psi epsilon 表算法的依赖图已经压清：P5.1 使用 theta<x 到 8e11、中段 "
            "psi(x)<1.00002841x、psi-theta 下界和 Table 6.3 的 epsilon_psi(28)。"
            "这关闭的是原文依赖图定位，不是作者侧可复现表算法。当前真正最窄点是 "
            "`1.00002841` 的来源/生成账本；该常数所在中段只有约 4.46e-11 余量，不能只按外部文字引用粗放通过。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict psi epsilon 表计算算法路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"p51_dependency_graph_closed={fmt_bool(result['p51_dependency_graph_closed'])}",
        f"published_source_boundary_identified={fmt_bool(result['published_source_boundary_identified'])}",
        f"bridge_common_variables_taxonomized={fmt_bool(result['bridge_common_variables_taxonomized'])}",
        f"epsilon_psi_28_source_located={fmt_bool(result['epsilon_psi_28_source_located'])}",
        f"middle_psi_upper_100002841_source_closed={fmt_bool(result['middle_psi_upper_100002841_source_closed'])}",
        f"machine_readable_table63_closed={fmt_bool(result['machine_readable_table63_closed'])}",
        f"theta_table64_to_8e11_source_closed={fmt_bool(result['theta_table64_to_8e11_source_closed'])}",
        f"zero_input_binding_to_table_formula_closed={fmt_bool(result['zero_input_binding_to_table_formula_closed'])}",
        f"psi_epsilon_interval_propagation_closed={fmt_bool(result['psi_epsilon_interval_propagation_closed'])}",
        f"reproducible_table_hash_closed={fmt_bool(result['reproducible_table_hash_closed'])}",
        f"table_computation_algorithm_closed={fmt_bool(result['table_computation_algorithm_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 原文边界",
        "",
        "| item | source | location | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["external_sources_used"]:
        lines.append(
            "| {item} | {source} | {location} | {meaning} |".format(
                item=table_cell(item["item"]),
                source=table_cell(item["source"]),
                location=table_cell(item["location"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(["", "## 2. P5.1 依赖图", "", "| node | role | status | ledger |", "| --- | --- | --- | --- |"])
    for item in result["dependency_graph"]:
        lines.append(
            "| {node} | {role} | {status} | `{ledger}` |".format(
                node=table_cell(item["node"]),
                role=table_cell(item["role"]),
                status=table_cell(item["status"]),
                ledger=table_cell(item["ledger"]),
            )
        )
    lines.extend(["", "## 3. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 4. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
