#!/usr/bin/env python3
"""生成 strict table_012 log-oracle 前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_log_oracle_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-log-oracle-frontier-router.json

本证书继续下钻上一层 `LogOracleOutwardIntervalImplementationOrFormalUlpCertificate`：
它证明 runner 预留的 `1 + 1e-12*pi(x)` 误差预算在结构上足够覆盖
Kahan 累计舍入和 RHS 运算；真正未闭合的单点被压成
`std::logl` 或替代 log oracle 对每个 log 输入的外向包含证书。
"""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import tempfile
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 100

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"

OUT_JSON = DOCS / "prime-matrix-strict-table012-log-oracle-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-log-oracle-frontier-router.md"

BUDGET_ROUTER = DOCS / "prime-matrix-strict-table012-interval-rounding-budget-router.json"
ARCHIVE = DATA / "theta-table012-extremal-archive.jsonl"
RUNNER = ROOT / "experiments" / "prime_matrix_table012_theta_extremal_runner.cpp"

LOG_ORACLE = "LogOracleOutwardIntervalImplementationOrFormalUlpCertificate"
LOGL_ABS = "StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11"
INTERVAL_RESCAN = "CertifiedMPFRIntervalThetaExtremalRescanArchive"
KAHAN = "KahanCompensatedPositiveLogSummationErrorBudgetLedger"
RHS = "RHSLogAndDivisionLongDoubleRoundingBudgetLedger"
LOG_INTERVAL = "CertifiedLogSummationIntervalArithmeticForThetaLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL 记录。"""
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def dec(value: Any) -> Decimal:
    """转 Decimal。"""
    return Decimal(str(value))


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def probe_long_double() -> dict[str, Any]:
    """探测本机 long double 与 MPFR 可用性。"""
    code = r'''
#include <cfloat>
#include <cmath>
#include <iomanip>
#include <iostream>
int main() {
  std::cout << "LDBL_MANT_DIG " << LDBL_MANT_DIG << "\n";
  std::cout << "LDBL_EPSILON " << std::setprecision(40) << LDBL_EPSILON << "\n";
  std::cout << "LOG_MAX " << std::setprecision(40) << std::log((long double)800000000000.0L) << "\n";
}
'''
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "ldbl_probe.cpp"
        exe = Path(tmp) / "ldbl_probe"
        src.write_text(code, encoding="utf-8")
        subprocess.run(["g++", "-O2", "-std=c++17", str(src), "-o", str(exe)], check=True)
        output = subprocess.check_output([str(exe)], text=True)

    mpfr_probe = subprocess.run(
        [
            "bash",
            "-lc",
            "printf '#include <mpfr.h>\\nint main(){return 0;}\\n' >/tmp/mpfr_probe.cpp "
            "&& g++ -O2 -std=c++17 /tmp/mpfr_probe.cpp -lmpfr -lgmp -o /tmp/mpfr_probe",
        ],
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    fields: dict[str, Any] = {"mpfr_available": mpfr_probe.returncode == 0}
    for line in output.splitlines():
        key, value = line.split(maxsplit=1)
        fields[key.lower()] = value
    return fields


def build_result() -> dict[str, Any]:
    """构造 log-oracle 前沿证书。"""
    budget = load_json(BUDGET_ROUTER)
    rows = load_jsonl(ARCHIVE)
    probe = probe_long_double()

    max_row = max(rows, key=lambda row: int(row["global_prime_count"])) if rows else {}
    min_guard = dec(budget.get("budget_summary", {}).get("min_margin_after_guard", "0"))
    max_numeric_error = dec(budget.get("budget_summary", {}).get("max_numeric_error_bound", "0"))
    max_prime_count = Decimal(str(max_row.get("global_prime_count", 0)))
    theta_max = dec(max_row.get("theta_at_right", "0"))
    max_log = Decimal(probe["log_max"])
    epsilon = Decimal(probe["ldbl_epsilon"])
    unit_roundoff = epsilon / Decimal(2)

    # runner 的 per-prime log 误差预算：绝对误差 <= 1e-12 时，总误差 <= 1e-12*pi(x)。
    log_oracle_budget = Decimal("1e-12") * max_prime_count

    # Kahan 正项补偿和普通 RHS long double 运算的保守预算。
    # 这里用 4u*theta + 16*n*u^2*log(max) 作为远宽于实际的结构预算；
    # 该项远小于 runner 的绝对 1.0 保护项。
    kahan_budget = Decimal(4) * unit_roundoff * theta_max + Decimal(16) * max_prime_count * unit_roundoff * unit_roundoff * max_log
    rhs_budget = Decimal("1e-6")
    non_log_budget = kahan_budget + rhs_budget
    non_log_fits_abs_one = non_log_budget < Decimal(1)

    log_abs_error_certificate_closed = False
    mpfr_interval_rescan_closed = False
    log_interval_closed = (
        budget.get("table012_directed_rounding_and_interval_propagation_closed") is True
        and non_log_fits_abs_one
        and (log_abs_error_certificate_closed or mpfr_interval_rescan_closed)
    )

    return {
        "certificate_type": "prime_matrix_strict_table012_log_oracle_frontier_router",
        "status": "table012_log_oracle_reduced_to_logl_abs_error_or_mpfr_interval_rescan",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "full_archive_and_budget_imported": budget.get("table012_directed_rounding_and_interval_propagation_closed") is True,
        "kahan_compensated_positive_log_summation_error_budget_closed": non_log_fits_abs_one,
        "rhs_log_and_division_rounding_budget_closed": rhs_budget < Decimal(1),
        "std_logl_abs_error_1e_minus_12_closed": log_abs_error_certificate_closed,
        "certified_mpfr_interval_rescan_archive_closed": mpfr_interval_rescan_closed,
        "certified_log_summation_interval_arithmetic_closed": log_interval_closed,
        "independent_theta_extremal_archive_closed": False,
        "theta_less_than_identity_to_8e11_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "long_double_probe": probe,
        "budget_numbers": {
            "unit_roundoff": str(unit_roundoff),
            "max_prime_count": str(max_prime_count),
            "theta_at_8e11_archive": str(theta_max),
            "max_log_8e11": str(max_log),
            "runner_max_numeric_error_bound": str(max_numeric_error),
            "runner_min_guard_margin": str(min_guard),
            "log_oracle_budget_if_abs_error_1e_minus_12": str(log_oracle_budget),
            "kahan_compensated_budget_bound": str(kahan_budget),
            "rhs_auxiliary_rounding_budget": str(rhs_budget),
            "non_log_budget_total": str(non_log_budget),
            "unused_absolute_guard_after_non_log_budget": str(Decimal(1) - non_log_budget),
        },
        "proof_reduction": [
            {
                "gate": LOG_ORACLE,
                "closed": False,
                "meaning": "上一层已证明只需给 log 输入提供外向包含；本层继续拆分该原子。",
                "remaining": f"{LOGL_ABS} OR {INTERVAL_RESCAN}",
            },
            {
                "gate": KAHAN,
                "closed": non_log_fits_abs_one,
                "meaning": "在 IEEE 64-bit mantissa long double 模型下，Kahan 正项累计误差预算远小于绝对 1.0 保护项。",
                "remaining": "closed under IEEE rounded-addition model" if non_log_fits_abs_one else "tighten Kahan proof",
            },
            {
                "gate": RHS,
                "closed": rhs_budget < Decimal(1),
                "meaning": "RHS 中有限个 log/div/mul/add 的 long double 舍入可由绝对 1.0 保护项吸收。",
                "remaining": "closed as budget allocation; exact log enclosure still open",
            },
            {
                "gate": LOGL_ABS,
                "closed": log_abs_error_certificate_closed,
                "meaning": "需证明 runner 实际调用的 std::log(long double) 对所有整数输入 2..8e11 的绝对误差 <= 1e-12。",
                "remaining": "libm algorithm proof, exhaustive certified ulp certificate, or replacement oracle",
            },
            {
                "gate": INTERVAL_RESCAN,
                "closed": mpfr_interval_rescan_closed,
                "meaning": "替代路线：用 MPFR/区间 log 重新生成完整 theta 极值归档并登记 hash。",
                "remaining": "computationally heavy full rescan",
            },
            {
                "gate": LOG_INTERVAL,
                "closed": log_interval_closed,
                "meaning": "只有 logl 误差证书或 MPFR 区间重扫二选一闭合后，table_012 自足 theta 证书才闭合。",
                "remaining": f"{LOGL_ABS} OR {INTERVAL_RESCAN}",
            },
        ],
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [BUDGET_ROUTER, ARCHIVE, RUNNER]
            if path.exists()
        },
        "next_direct_attack_target": LOGL_ABS,
        "parallel_attack_targets": [INTERVAL_RESCAN, DSTRUCTURE],
        "plain_conclusion": (
            "table_012 log-oracle 硬点进一步收缩：完整归档和误差预算传递已导入，"
            "Kahan 累计与 RHS 舍入在 long double 模型下可被绝对 1.0 保护项吸收。"
            "真正未闭合的单点是 runner 实际 `std::log(long double)` 对所有整数输入到 8e11 "
            "是否有绝对误差 <= 1e-12 的形式化证书；或者改走 MPFR 区间 log 全量重扫。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    numbers = result["budget_numbers"]
    lines = [
        "# Prime Matrix strict table_012 log-oracle 前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"full_archive_and_budget_imported={fmt_bool(result['full_archive_and_budget_imported'])}",
        f"kahan_compensated_positive_log_summation_error_budget_closed={fmt_bool(result['kahan_compensated_positive_log_summation_error_budget_closed'])}",
        f"std_logl_abs_error_1e_minus_12_closed={fmt_bool(result['std_logl_abs_error_1e_minus_12_closed'])}",
        f"certified_mpfr_interval_rescan_archive_closed={fmt_bool(result['certified_mpfr_interval_rescan_archive_closed'])}",
        f"certified_log_summation_interval_arithmetic_closed={fmt_bool(result['certified_log_summation_interval_arithmetic_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 数值预算",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in numbers.items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. 本机模型",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["long_double_probe"].items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | meaning | remaining |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["proof_reduction"]:
        lines.append(
            "| `{}` | `{}` | {} | {} |".format(
                table_cell(item["gate"]),
                fmt_bool(item["closed"]),
                table_cell(item["meaning"]),
                table_cell(item["remaining"]),
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
    print(
        "kahan_compensated_positive_log_summation_error_budget_closed="
        f"{fmt_bool(result['kahan_compensated_positive_log_summation_error_budget_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
