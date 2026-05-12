#!/usr/bin/env python3
"""生成 strict epsilon 表生成器审计路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_epsilon_table_generator_audit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-epsilon-table-generator-audit-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-epsilon-table-generator-audit-router.md"

PSI_TABLE = MONOGRAPH / "prime-matrix-strict-schoenfeld-dusart-psi-table-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [PSI_TABLE, CLAIM_STATUS]

TARGET = "SchoenfeldDusartEpsilonTableGeneratorFormalizationLedger"
EXTRACT = "DusartTableEpsilonStatementExtractionLedger"
ALGORITHM = "PsiEpsilonTableComputationAlgorithmLedger"
ZERO_INPUT = "VerifiedZeroAndZeroFreeTailInputForSchoenfeldDusartTableLedger"
INTERVAL = "PsiEpsilonIntervalPropagationAndMonotonicityLedger"
HASH = "ReproduciblePsiEpsilonTableComputationHashLedger"
ROUNDING = "DusartP51TableRoundingMarginAuditLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

DUSART_URL = "https://arxiv.org/abs/1002.0442"

TABLE_VALUES = [
    {
        "symbol": "eps_psi_28",
        "value": 0.00002224,
        "source_role": "high tail x>=e^28",
        "needed_by": "PsiEpsilonHighTailB28TableCertificate",
    },
    {
        "symbol": "psi_middle_upper",
        "value": 1.00002841,
        "source_role": "middle strip 8e11<=x<=e^28",
        "needed_by": "PsiUpperMiddle8e11ToE28TableCertificate",
    },
]


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


def build_result() -> dict[str, Any]:
    """构造 epsilon 表生成器审计证书。"""
    psi = load_json(PSI_TABLE)
    active = psi.get("next_direct_attack_target") == TARGET
    extracted = active and len(TABLE_VALUES) == 2
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            psi.get("counterexample_assumption_only") is True and psi.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计外部表值生成责任，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "EpsilonTableGeneratorGateActive",
            active,
            True,
            "上一证书把下一最窄点设为 Schoenfeld/Dusart epsilon 表生成器形式化。",
            TARGET,
        ),
        row(
            EXTRACT,
            extracted,
            True,
            "已把 P5.1 需要的两个 psi 表值抽出为机器可读责任项。",
            "eps_psi_28=0.00002224; psi_middle_upper=1.00002841",
        ),
        row(
            "TableValuesAreNotProof",
            True,
            True,
            "表值提取只说明外部论文使用了这些数；作者侧自足证明还需要生成算法、零点输入和可复现工件。",
            f"{ALGORITHM} AND {ZERO_INPUT} AND {HASH}",
        ),
        row(
            ALGORITHM,
            False,
            False,
            "当前仓库尚无从显式公式、零点验证和零点自由尾项自动生成 eps_psi(b) 表的算法账本。",
            f"{ZERO_INPUT} AND {INTERVAL} AND {HASH}",
        ),
        row(
            ZERO_INPUT,
            False,
            False,
            "表生成器需要明确使用哪些有限零点验证、高度阈值、零点自由区和尾项常数。",
            "Verified zeros plus zero-free/tail constants with citations or internal proof。",
        ),
        row(
            INTERVAL,
            False,
            False,
            "需要证明表值如何从离散 b 或有限节点传播到整段 x 区间，包含跳点、端点和单调性规则。",
            ALGORITHM,
        ),
        row(
            HASH,
            False,
            False,
            "需要可复现计算文件、版本、输入数据 hash 和输出表 hash；当前只有路由证书，没有原始计算工件。",
            "Reproducible source tables and scripts",
        ),
        row(
            ROUNDING,
            psi.get("table_rounding_margin_audit_closed") is True,
            True,
            "P5.1 拼接余量审查已完成；这只约束表值舍入方向，不证明表值。",
            ROUNDING,
        ),
        row(
            TARGET,
            False,
            False,
            "epsilon 表生成器尚未自足形式化；当前只关闭了表值提取与责任拆包。",
            f"{EXTRACT} AND {ALGORITHM} AND {ZERO_INPUT} AND {INTERVAL} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "表生成器审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_epsilon_table_generator_audit_router",
        "status": "epsilon_table_generator_audit_extracted_values_algorithm_zero_input_hash_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "epsilon_table_statement_extraction_closed": extracted,
        "epsilon_table_generator_self_contained_closed": False,
        "psi_epsilon_table_self_contained_closed": False,
        "table_computation_algorithm_closed": False,
        "verified_zero_and_zero_free_tail_input_closed": False,
        "interval_propagation_closed": False,
        "reproducible_table_hash_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "table_values": TABLE_VALUES,
        "external_reference": {
            "id": "Dusart arXiv:1002.0442",
            "url": DUSART_URL,
            "role": "source boundary for the extracted table values; not a reproducible computation artifact",
        },
        "replacement_self_contained": {
            TARGET: f"{EXTRACT} AND {ALGORITHM} AND {ZERO_INPUT} AND {INTERVAL} AND {HASH}",
            ALGORITHM: f"{ZERO_INPUT} AND {INTERVAL} AND {HASH}",
        },
        "next_direct_attack_target": ZERO_INPUT,
        "parallel_attack_targets": [ALGORITHM, INTERVAL, HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Schoenfeld/Dusart epsilon 表生成器被进一步拆成五项：表值提取、计算算法、零点/零点自由尾项输入、"
            "区间传播规则和可复现 hash。当前只闭合表值提取；没有原始表生成算法和零点输入证书，"
            "所以不能把 `eps_psi(28)` 与 `1.00002841` 当作作者侧自足证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict epsilon 表生成器审计路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"epsilon_table_statement_extraction_closed={fmt_bool(result['epsilon_table_statement_extraction_closed'])}",
        f"epsilon_table_generator_self_contained_closed={fmt_bool(result['epsilon_table_generator_self_contained_closed'])}",
        f"table_computation_algorithm_closed={fmt_bool(result['table_computation_algorithm_closed'])}",
        f"verified_zero_and_zero_free_tail_input_closed={fmt_bool(result['verified_zero_and_zero_free_tail_input_closed'])}",
        f"interval_propagation_closed={fmt_bool(result['interval_propagation_closed'])}",
        f"reproducible_table_hash_closed={fmt_bool(result['reproducible_table_hash_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 抽取表值",
        "",
        "| symbol | value | source role | needed by |",
        "| --- | ---: | --- | --- |",
    ]
    for item in result["table_values"]:
        lines.append(
            f"| `{item['symbol']}` | `{item['value']:.12f}` | "
            f"{table_cell(item['source_role'])} | `{table_cell(item['needed_by'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 外部边界",
            "",
            f"- `{result['external_reference']['id']}`：{result['external_reference']['url']}；{result['external_reference']['role']}",
            "",
            "## 3. 自足替换",
            "",
            "```text",
        ]
    )
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
