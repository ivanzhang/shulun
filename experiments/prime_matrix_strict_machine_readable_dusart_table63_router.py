#!/usr/bin/env python3
"""生成 strict Dusart Table 6.3 机器可读表行审计证书。

用法示例：
  python3 experiments/prime_matrix_strict_machine_readable_dusart_table63_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-machine-readable-dusart-table63-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 50

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-machine-readable-dusart-table63-router.json"
OUT_MD = DOCS / "prime-matrix-strict-machine-readable-dusart-table63-router.md"

TABLE_ALGORITHM = DOCS / "prime-matrix-strict-psi-epsilon-table-algorithm-router.json"
GENERATOR_AUDIT = DOCS / "prime-matrix-strict-epsilon-table-generator-audit-router.json"
MIDDLE_SYNC = DOCS / "prime-matrix-strict-middle-psi-upper-delta-archive-sync-router.json"
ANALYTIC_SPLICE = DOCS / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [TABLE_ALGORITHM, GENERATOR_AUDIT, MIDDLE_SYNC, ANALYTIC_SPLICE, CLAIM_STATUS]

TARGET = "MachineReadableDusartTable63EpsilonPsiLedger"
B28_ROW = "MachineReadableDusartTable63B28EpsilonPsiRowLedger"
SOURCE = "EpsilonPsi28Table63SourceLedger"
GENERATION = "Table63B28GeneratedUpperRoundingCertificateFromVerifiedZeroInputsLedger"
ZERO_BINDING = "VerifiedZeroZeroFreeInputsToTableFormulaBindingLedger"
INTERVAL = "PsiEpsilonIntervalPropagationAndMonotonicityLedger"
HASH = "ReproduciblePsiEpsilonTableComputationHashLedger"
TABLE64 = "ThetaLessThanIdentityTable64To8e11SourceLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

EPS = Decimal("0.00002224")
TARGET_RELATIVE = Decimal(1) / Decimal(36260)
HIGH_TAIL_START_B = 28


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


def table_rows() -> list[dict[str, Any]]:
    """给出本步能机器化的 Table 6.3 最小行。"""
    return [
        {
            "table": "Dusart Table 6.3",
            "b": HIGH_TAIL_START_B,
            "function": "psi",
            "epsilon_decimal": str(EPS),
            "epsilon_scientific": "2.224E-5",
            "asserted_interval": "x >= exp(28)",
            "needed_by": "PsiEpsilonHighTailB28TableCertificate",
            "source_boundary": "Dusart arXiv:1002.0442, Table 6.3 row b=28",
        }
    ]


def build_result() -> dict[str, Any]:
    """构造 Table 6.3 机器可读表行审计证书。"""
    algorithm = load_json(TABLE_ALGORITHM)
    generator = load_json(GENERATOR_AUDIT)
    middle = load_json(MIDDLE_SYNC)
    analytic = load_json(ANALYTIC_SPLICE)

    active = (
        middle.get("next_direct_attack_target") == TARGET
        or TARGET in algorithm.get("parallel_attack_targets", [])
        or TARGET in algorithm.get("open_gates", [])
    )
    source_located = algorithm.get("epsilon_psi_28_source_located") is True
    extracted = generator.get("epsilon_table_statement_extraction_closed") is True
    high_tail_splice_ready = analytic.get("dusart_analytic_kernel_threshold_arithmetic_splice_closed") is True
    p51_margin = TARGET_RELATIVE - EPS
    b28_row_closed = active and source_located and extracted and EPS == Decimal("0.00002224")
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            algorithm.get("counterexample_assumption_only") is True
            and middle.get("row_column_unconditional_closed") is False,
            True,
            "本步只登记反例链可调用的外部 Table 6.3 高尾输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "Table63GateActiveAfterMiddleSync",
            active,
            True,
            "中段 psi 上界已由 delta-aware 归档关闭后，下一表算法门确认为 Table 6.3。",
            TARGET,
        ),
        row(
            SOURCE,
            source_located,
            False,
            "已有证书把 Dusart Table 6.3 的 b=28 行定位为 epsilon_psi(28)=2.224E-5。",
            TARGET,
        ),
        row(
            "DusartTableEpsilonStatementExtractionImported",
            extracted,
            True,
            "epsilon 表审计已把 eps_psi_28=0.00002224 抽成机器可读责任项。",
            B28_ROW,
        ),
        row(
            B28_ROW,
            b28_row_closed,
            False,
            "本步形成最小机器可读外部表行：b=28, epsilon_psi=0.00002224, asserted interval x>=exp(28)。",
            GENERATION,
        ),
        row(
            "HighTailP51ArithmeticMargin",
            high_tail_splice_ready and p51_margin > 0,
            True,
            "若接受该表行的上界语义，则高尾拼接满足 0.00002224 < 1/36260。",
            f"margin={p51_margin}",
        ),
        row(
            "MachineReadableTable63ExternalRowUsable",
            b28_row_closed and high_tail_splice_ready and p51_margin > 0,
            False,
            "外部路线可严格使用 b=28 表行关闭高尾数值输入；这仍不是作者侧自足生成证明。",
            "external Table 6.3 accepted",
        ),
        row(
            GENERATION,
            False,
            False,
            "还缺从显式公式、有限零点验证、零点自由尾项与外向舍入规则生成 2.224E-5 的证明。",
            f"{ZERO_BINDING} AND {INTERVAL} AND {HASH}",
        ),
        row(
            TARGET,
            False,
            False,
            "完整 MachineReadableDusartTable63 不能只靠单行摘录闭合；还需要生成规则、舍入方向、适用区间与可复现 hash。",
            f"{GENERATION} AND {ZERO_BINDING} AND {INTERVAL} AND {HASH}",
        ),
        row(
            "PsiEpsilonTableAlgorithmStillOpen",
            False,
            False,
            "中段归档和 b=28 外部表行仍未关闭 Table 6.4、零点输入绑定、区间传播与表 hash。",
            f"{TABLE64} AND {ZERO_BINDING} AND {INTERVAL} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "Table 6.3 表行机器化不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_machine_readable_dusart_table63_router",
        "status": "table63_b28_external_row_machine_readable_full_generation_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "machine_readable_table63_b28_row_closed": b28_row_closed,
        "machine_readable_table63_external_row_usable": b28_row_closed and high_tail_splice_ready and p51_margin > 0,
        "machine_readable_table63_closed": False,
        "table63_generation_rounding_closed": False,
        "zero_input_binding_to_table_formula_closed": False,
        "psi_epsilon_interval_propagation_closed": False,
        "reproducible_table_hash_closed": False,
        "psi_epsilon_table_algorithm_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "table63_machine_rows": table_rows(),
        "arithmetic": {
            "epsilon_psi_28": str(EPS),
            "target_1_over_36260": str(TARGET_RELATIVE),
            "p51_high_tail_margin": str(p51_margin),
        },
        "replacement_self_contained": {
            TARGET: f"{GENERATION} AND {ZERO_BINDING} AND {INTERVAL} AND {HASH}",
            GENERATION: f"{ZERO_BINDING} AND {INTERVAL} AND {HASH}",
        },
        "next_direct_attack_target": GENERATION,
        "parallel_attack_targets": [ZERO_BINDING, INTERVAL, HASH, TABLE64, DSTRUCTURE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Table 6.3 的 b=28 行已被压成最小机器可读外部表行："
            "`epsilon_psi(28)=0.00002224`，适用高尾 `x>=exp(28)`。"
            "若接受 Dusart 外部表语义，它与已闭合的高尾拼接算术严格匹配，"
            "因为 `0.00002224 < 1/36260`。但作者侧自足版尚未闭合："
            "仍需证明该值如何由同一显式公式、有限零点/零点自由尾项、区间传播、外向舍入和可复现 hash 生成。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Dusart Table 6.3 机器可读表行审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"machine_readable_table63_b28_row_closed={fmt_bool(result['machine_readable_table63_b28_row_closed'])}",
        f"machine_readable_table63_external_row_usable={fmt_bool(result['machine_readable_table63_external_row_usable'])}",
        f"machine_readable_table63_closed={fmt_bool(result['machine_readable_table63_closed'])}",
        f"table63_generation_rounding_closed={fmt_bool(result['table63_generation_rounding_closed'])}",
        f"psi_epsilon_table_algorithm_closed={fmt_bool(result['psi_epsilon_table_algorithm_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 机器表行",
        "",
        "| table | b | function | epsilon | interval | needed by |",
        "| --- | ---: | --- | ---: | --- | --- |",
    ]
    for item in result["table63_machine_rows"]:
        lines.append(
            "| {table} | `{b}` | `{function}` | `{epsilon}` | {interval} | `{needed}` |".format(
                table=table_cell(item["table"]),
                b=item["b"],
                function=table_cell(item["function"]),
                epsilon=table_cell(item["epsilon_decimal"]),
                interval=table_cell(item["asserted_interval"]),
                needed=table_cell(item["needed_by"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 高尾拼接算术",
            "",
            "| field | value |",
            "| --- | ---: |",
        ]
    )
    for key, value in result["arithmetic"].items():
        lines.append(f"| `{table_cell(key)}` | `{table_cell(value)}` |")
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
    print(f"machine_readable_table63_b28_row_closed={fmt_bool(result['machine_readable_table63_b28_row_closed'])}")
    print(f"machine_readable_table63_closed={fmt_bool(result['machine_readable_table63_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
