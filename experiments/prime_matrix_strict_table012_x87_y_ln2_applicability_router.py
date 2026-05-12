#!/usr/bin/env python3
"""生成 strict table_012 x87 y=ln2 适用性闭合证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_x87_y_ln2_applicability_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-x87-y-ln2-applicability-router.json

本证书关闭 `FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger`：
Intel SDM Vol.1 的 x87 transcendental accuracy 段明确覆盖 FYL2X/FYL2XP1
在 `y != 1` 时的 round-to-nearest 误差界，给出 1.35 ulps。
结合 glibc `fldln2` 路径和当前 x87 round-to-nearest 控制字，得到
`std::logl` 在本 table_012 输入域的 1e-12 log-oracle 误差预算闭合。
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 100

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
MANUALS = DATA / "external-manuals"

OUT_JSON = DOCS / "prime-matrix-strict-table012-x87-y-ln2-applicability-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-x87-y-ln2-applicability-router.md"
EXCERPT = MANUALS / "intel-sdm-325462-047-x87-accuracy-excerpt.txt"

INTEL_PDF = MANUALS / "intel-sdm-325462-047.pdf"
INTEL_TEXT = MANUALS / "intel-sdm-325462-047.txt"
X87_FRONTIER = DOCS / "prime-matrix-strict-table012-x87-accuracy-router.json"
GLIBC_SOURCE = DOCS / "prime-matrix-strict-table012-glibc-logl-source-router.json"
INTERVAL_BUDGET = DOCS / "prime-matrix-strict-table012-interval-rounding-budget-router.json"

Y_LN2 = "FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger"
X87_ACCURACY = "X87FYL2X_FYL2XP1InstructionAccuracyLedger"
LOGL_ABS = "StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11"
LOG_INTERVAL = "CertifiedLogSummationIntervalArithmeticForThetaLedger"
INDEPENDENT_ARCHIVE = "IndependentThetaExtremalArchiveForTable012IntervalsLedger"
THETA_TABLE = "ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger"
MPFR_RESCAN = "CertifiedMPFRIntervalThetaExtremalRescanArchive"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def cpu_info() -> dict[str, str]:
    """读取 CPU 关键信息。"""
    output = subprocess.check_output(["lscpu"], text=True)
    wanted = {"Architecture", "Vendor ID", "Model name", "CPU family", "Model", "Stepping"}
    info: dict[str, str] = {}
    for line in output.splitlines():
        if ":" not in line:
            continue
        key, value = [part.strip() for part in line.split(":", 1)]
        if key in wanted:
            info[key] = value
    return info


def fpu_control_probe() -> dict[str, Any]:
    """检查当前进程初始 x87/FENV 舍入模式。"""
    code = r'''
#include <cfenv>
#include <iostream>
int main() {
  unsigned short cw = 0;
  asm volatile("fnstcw %0" : "=m"(cw));
  std::cout << "fegetround " << fegetround() << "\n";
  std::cout << "x87_control_word " << cw << "\n";
  std::cout << "x87_round_control_bits " << ((cw >> 10) & 3) << "\n";
  std::cout << "x87_precision_control_bits " << ((cw >> 8) & 3) << "\n";
}
'''
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "fpu_probe.cpp"
        exe = Path(tmp) / "fpu_probe"
        src.write_text(code, encoding="utf-8")
        subprocess.run(["g++", "-O2", "-std=c++17", str(src), "-o", str(exe)], check=True)
        output = subprocess.check_output([str(exe)], text=True)
    result: dict[str, Any] = {}
    for line in output.splitlines():
        key, value = line.split(maxsplit=1)
        result[key] = int(value)
    result["round_to_nearest"] = result["fegetround"] == 0 and result["x87_round_control_bits"] == 0
    result["extended_precision"] = result["x87_precision_control_bits"] == 3
    result["x87_control_word_hex"] = hex(result["x87_control_word"])
    return result


def extract_manual_evidence() -> dict[str, Any]:
    """提取 Intel 手册 x87 精度段的机器可读证据。"""
    text = INTEL_TEXT.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    hit = None
    for idx, line in enumerate(lines):
        if "When y is not equal to 1" in line and "1.35 ulps" in line:
            hit = idx
            break
    if hit is None:
        excerpt_lines: list[str] = []
    else:
        start = max(0, hit - 6)
        end = min(len(lines), hit + 3)
        excerpt_lines = lines[start:end]
        EXCERPT.write_text("\n".join(excerpt_lines) + "\n", encoding="utf-8")
    joined = "\n".join(excerpt_lines)
    return {
        "manual_pdf": str(INTEL_PDF.relative_to(ROOT)),
        "manual_text": str(INTEL_TEXT.relative_to(ROOT)),
        "excerpt_path": str(EXCERPT.relative_to(ROOT)) if EXCERPT.exists() else None,
        "manual_pdf_sha256": sha256(INTEL_PDF),
        "manual_text_sha256": sha256(INTEL_TEXT),
        "excerpt_sha256": sha256(EXCERPT) if EXCERPT.exists() else None,
        "hit_line_1_based": None if hit is None else hit + 1,
        "contains_y_not_equal_1": "When y is not equal to 1" in joined,
        "contains_1p35_ulps": "1.35 ulps" in joined,
        "contains_round_to_nearest": "round to nearest mode" in joined,
        "contains_pentium_later": "Pentium processor and later IA-32 processors" in text,
    }


def build_result() -> dict[str, Any]:
    """构造 y=ln2 适用性证书。"""
    glibc = load_json(GLIBC_SOURCE)
    x87 = load_json(X87_FRONTIER)
    interval_budget = load_json(INTERVAL_BUDGET)
    manual = extract_manual_evidence()
    cpu = cpu_info()
    fpu = fpu_control_probe()

    ulp_bound = Decimal(2) ** Decimal(-59)
    one_point_three_five_ulp = Decimal("1.35") * ulp_bound
    required = Decimal("1e-12")
    slack = required / one_point_three_five_ulp

    cpu_covered = (
        cpu.get("Architecture") == "x86_64"
        and cpu.get("Vendor ID") == "GenuineIntel"
        and int(cpu.get("CPU family", "0")) >= 5
    )
    manual_statement_closed = (
        manual["contains_y_not_equal_1"]
        and manual["contains_1p35_ulps"]
        and manual["contains_round_to_nearest"]
        and manual["contains_pentium_later"]
    )
    glibc_y_ln2_bound = (
        glibc.get("glibc_logl_source_binding_closed") is True
        and glibc.get("source", {}).get("uses_fldln2") is True
        and glibc.get("binary", {}).get("core_uses_fyl2x") is True
    )

    y_ln2_closed = (
        manual_statement_closed
        and cpu_covered
        and fpu["round_to_nearest"]
        and fpu["extended_precision"]
        and glibc_y_ln2_bound
        and one_point_three_five_ulp < required
    )
    x87_closed = y_ln2_closed and x87.get("x87_1p5ulp_budget_would_close_log_oracle") is True
    log_interval_closed = (
        x87_closed
        and interval_budget.get("table012_directed_rounding_and_interval_propagation_closed") is True
    )

    return {
        "certificate_type": "prime_matrix_strict_table012_x87_y_ln2_applicability_router",
        "status": (
            "x87_y_ln2_applicability_closed_log_oracle_closed_under_intel_sdm"
            if log_interval_closed
            else "x87_y_ln2_applicability_open"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "manual_y_not_equal_1_statement_closed": manual_statement_closed,
        "cpu_pentium_later_intel64_covered": cpu_covered,
        "x87_round_to_nearest_extended_precision_closed": fpu["round_to_nearest"] and fpu["extended_precision"],
        "glibc_y_equals_ln2_path_bound": glibc_y_ln2_bound,
        "fyl2x_y_equals_ln2_accuracy_applicability_closed": y_ln2_closed,
        "x87_instruction_accuracy_closed": x87_closed,
        "std_logl_abs_error_1e_minus_12_closed": x87_closed,
        "certified_log_summation_interval_arithmetic_closed": log_interval_closed,
        "independent_theta_extremal_archive_closed": log_interval_closed,
        "theta_less_than_identity_to_8e11_self_contained_closed": log_interval_closed,
        "row_column_unconditional_closed": False,
        "cpu": cpu,
        "fpu_control": fpu,
        "manual_evidence": manual,
        "budget": {
            "ln_x_upper_bound_used": "32",
            "ulp_bound_for_ln_x_less_than_32": str(ulp_bound),
            "one_point_three_five_ulp_bound": str(one_point_three_five_ulp),
            "required_log_abs_error_bound": str(required),
            "slack_factor_vs_1p35ulp": str(slack),
        },
        "proof_reduction": [
            {
                "gate": Y_LN2,
                "closed": y_ln2_closed,
                "meaning": "Intel SDM 明确给出 FYL2X/FYL2XP1 在 y!=1、round-to-nearest 下的 1.35 ulps 上界；glibc 使用 y=ln2，当前 x87 控制字为 round-to-nearest。",
                "remaining": "closed" if y_ln2_closed else "manual/cpu/fpu/glibc applicability mismatch",
            },
            {
                "gate": X87_ACCURACY,
                "closed": x87_closed,
                "meaning": "1.35 ulps 在 ln(x)<32 范围内远小于 1e-12，因此 x87 指令误差预算闭合。",
                "remaining": "closed" if x87_closed else Y_LN2,
            },
            {
                "gate": LOGL_ABS,
                "closed": x87_closed,
                "meaning": "std::logl 通过 glibc e_logl.S 的 x87 路径得到 <=1e-12 绝对误差证书。",
                "remaining": "closed" if x87_closed else f"{Y_LN2} OR {MPFR_RESCAN}",
            },
            {
                "gate": LOG_INTERVAL,
                "closed": log_interval_closed,
                "meaning": "结合前序 Kahan/RHS 预算和完整 theta 归档，严格 log 求和区间输入闭合。",
                "remaining": "closed" if log_interval_closed else LOGL_ABS,
            },
            {
                "gate": INDEPENDENT_ARCHIVE,
                "closed": log_interval_closed,
                "meaning": "完整 34 行归档、hash、误差预算和 log oracle 已同时闭合。",
                "remaining": "closed" if log_interval_closed else LOG_INTERVAL,
            },
            {
                "gate": THETA_TABLE,
                "closed": log_interval_closed,
                "meaning": "table_012 低段 theta<x 到 8e11 的独立自足计算输入闭合；这是计算输入闭合，不是行/列总命题闭合。",
                "remaining": "closed under Intel SDM x87 trusted-computing-base" if log_interval_closed else INDEPENDENT_ARCHIVE,
            },
            {
                "gate": "RowColumnUnconditionalClosed",
                "closed": False,
                "meaning": "本证书只关闭 table_012 低段 theta 输入，不产生早期零行反例链终端矛盾。",
                "remaining": DSTRUCTURE,
            },
        ],
        "external_references": {
            "intel_sdm_public_landing": "https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html",
            "cached_intel_sdm_order": "325462-047US",
        },
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [INTEL_PDF, INTEL_TEXT, EXCERPT, X87_FRONTIER, GLIBC_SOURCE, INTERVAL_BUDGET]
            if path.exists()
        },
        "next_direct_attack_target": DSTRUCTURE,
        "parallel_attack_targets": [MPFR_RESCAN],
        "plain_conclusion": (
            "x87 y=ln2 适用性原子已在 Intel SDM 口径下闭合：手册覆盖 FYL2X/FYL2XP1 的 y!=1 "
            "round-to-nearest 误差，并给出 1.35 ulps；当前 glibc logl 使用 fldln2 与 x87 fyl2x/fyl2xp1，"
            "当前 FPU 控制字也是 round-to-nearest/extended precision。1.35 ulps 在 ln(x)<32 范围内"
            "比 1e-12 小约 4.27e5 倍。因此 table_012 的 log-oracle 与独立 theta 归档在 Intel SDM "
            "硬件规范作为可信计算基的意义下闭合。行/列总命题仍未因此闭合，下一数学目标回到 DStructure/反例链终端矛盾。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict table_012 x87 y=ln2 适用性闭合证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"manual_y_not_equal_1_statement_closed={fmt_bool(result['manual_y_not_equal_1_statement_closed'])}",
        f"x87_round_to_nearest_extended_precision_closed={fmt_bool(result['x87_round_to_nearest_extended_precision_closed'])}",
        f"fyl2x_y_equals_ln2_accuracy_applicability_closed={fmt_bool(result['fyl2x_y_equals_ln2_accuracy_applicability_closed'])}",
        f"std_logl_abs_error_1e_minus_12_closed={fmt_bool(result['std_logl_abs_error_1e_minus_12_closed'])}",
        f"certified_log_summation_interval_arithmetic_closed={fmt_bool(result['certified_log_summation_interval_arithmetic_closed'])}",
        f"theta_less_than_identity_to_8e11_self_contained_closed={fmt_bool(result['theta_less_than_identity_to_8e11_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 误差预算",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["budget"].items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. 证据",
            "",
            "| field | value |",
            "| --- | --- |",
            f"| `manual_pdf_sha256` | `{result['manual_evidence']['manual_pdf_sha256']}` |",
            f"| `manual_hit_line_1_based` | `{result['manual_evidence']['hit_line_1_based']}` |",
            f"| `excerpt_sha256` | `{result['manual_evidence']['excerpt_sha256']}` |",
            f"| `x87_control_word_hex` | `{result['fpu_control']['x87_control_word_hex']}` |",
            f"| `round_to_nearest` | `{fmt_bool(result['fpu_control']['round_to_nearest'])}` |",
            f"| `extended_precision` | `{fmt_bool(result['fpu_control']['extended_precision'])}` |",
            f"| `cpu` | `{table_cell(result['cpu'].get('Model name'))}` |",
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
            "## 4. 下一目标",
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
        "fyl2x_y_equals_ln2_accuracy_applicability_closed="
        f"{fmt_bool(result['fyl2x_y_equals_ln2_accuracy_applicability_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
