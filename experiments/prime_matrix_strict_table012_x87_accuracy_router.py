#!/usr/bin/env python3
"""生成 strict table_012 x87 log 指令精度前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_table012_x87_accuracy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table012-x87-accuracy-router.json

本证书继续下钻 `X87FYL2X_FYL2XP1InstructionAccuracyLedger`。
它证明：如果 FYL2X/FYL2XP1 在 glibc 使用的 y=ln2 乘子下满足 1.5 ulp
级绝对误差，则 1e-12 的 log oracle 预算有超过 3.8e5 倍余量。
但该“y=ln2 适用性”本身仍需 Intel/AMD 指令精度证明或实测形式化证书。
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 100

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

OUT_JSON = DOCS / "prime-matrix-strict-table012-x87-accuracy-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table012-x87-accuracy-router.md"

GLIBC_SOURCE = DOCS / "prime-matrix-strict-table012-glibc-logl-source-router.json"
POINT_AUDIT = DOCS / "prime-matrix-strict-table012-logl-mpfr-point-audit-router.json"

X87_ACCURACY = "X87FYL2X_FYL2XP1InstructionAccuracyLedger"
Y_LN2_ULP = "FYL2X_FYL2XP1_YEqualsLn2AccuracyApplicabilityLedger"
MPFR_RESCAN = "CertifiedMPFRIntervalThetaExtremalRescanArchive"
LOGL_ABS = "StdLogLAbsErrorLe1eMinus12ForIntegerInputsUpTo8e11"


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
    """读取简要 CPU 信息。"""
    output = subprocess.check_output(["lscpu"], text=True)
    wanted = {
        "Architecture",
        "Vendor ID",
        "Model name",
        "CPU family",
        "Model",
        "Stepping",
    }
    result: dict[str, str] = {}
    for line in output.splitlines():
        if ":" not in line:
            continue
        key, value = [part.strip() for part in line.split(":", 1)]
        if key in wanted:
            result[key] = value
    return result


def build_result() -> dict[str, Any]:
    """构造 x87 指令精度前沿证书。"""
    glibc = load_json(GLIBC_SOURCE)
    point = load_json(POINT_AUDIT)

    # 对 ln(x), x<=8e11，有 ln(x)<32 且 >0，落在二进制指数 4 的数量级；
    # 80-bit extended 64-bit significand 的一 ulp 不超过 2^(4-63)。
    ulp_bound = Decimal(2) ** Decimal(-59)
    one_point_five_ulp = Decimal("1.5") * ulp_bound
    log_budget = Decimal("1e-12")
    slack_factor = log_budget / one_point_five_ulp

    y_ln2_applicability_closed = False
    x87_closed = (
        glibc.get("glibc_logl_source_binding_closed") is True
        and y_ln2_applicability_closed
        and one_point_five_ulp < log_budget
    )

    return {
        "certificate_type": "prime_matrix_strict_table012_x87_accuracy_router",
        "status": "x87_accuracy_reduced_to_y_equals_ln2_applicability_or_mpfr_rescan",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "glibc_logl_source_binding_imported": glibc.get("glibc_logl_source_binding_closed") is True,
        "logl_mpfr_point_audit_imported": point.get("logl_mpfr_point_audit_closed") is True,
        "x87_1p5ulp_budget_would_close_log_oracle": one_point_five_ulp < log_budget,
        "fyl2x_y_equals_ln2_accuracy_applicability_closed": y_ln2_applicability_closed,
        "x87_instruction_accuracy_closed": x87_closed,
        "std_logl_abs_error_1e_minus_12_closed": False,
        "certified_log_summation_interval_arithmetic_closed": False,
        "theta_less_than_identity_to_8e11_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "cpu": cpu_info(),
        "budget": {
            "ln_x_upper_bound_used": "32",
            "extended_precision_significand_bits": 64,
            "ulp_bound_for_ln_x_less_than_32": str(ulp_bound),
            "one_point_five_ulp_bound": str(one_point_five_ulp),
            "required_log_abs_error_bound": str(log_budget),
            "slack_factor_vs_1p5ulp": str(slack_factor),
        },
        "proof_reduction": [
            {
                "gate": X87_ACCURACY,
                "closed": x87_closed,
                "meaning": "若 glibc 使用的 FYL2X/FYL2XP1 在 y=ln2 乘子下有 <=1.5 ulp 误差，则 log oracle 预算立即闭合。",
                "remaining": Y_LN2_ULP if not x87_closed else "closed",
            },
            {
                "gate": "X87OnePointFiveUlpWouldBeSufficient",
                "closed": one_point_five_ulp < log_budget,
                "meaning": "在 ln(x)<32 范围，1.5 ulp 约 2.60e-18，比 1e-12 小约 3.84e5 倍。",
                "remaining": "closed",
            },
            {
                "gate": Y_LN2_ULP,
                "closed": y_ln2_applicability_closed,
                "meaning": "必须证明 Intel/AMD FYL2X/FYL2XP1 的精度保证适用于 glibc 的 y=ln2 调用，而不只是 y=1 的特殊陈述。",
                "remaining": "architectural/manual proof or formally sampled microcode certificate",
            },
            {
                "gate": MPFR_RESCAN,
                "closed": False,
                "meaning": "绕开硬件指令精度：用 MPFR 外向 log 全量重扫完整 theta 归档。",
                "remaining": "heavy full rescan",
            },
            {
                "gate": LOGL_ABS,
                "closed": False,
                "meaning": "当前仍不能把有限点审计和 y=1 手册语句合成全域 logl 误差证明。",
                "remaining": f"{Y_LN2_ULP} OR {MPFR_RESCAN}",
            },
        ],
        "external_references": {
            "intel_sdm": "https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html",
            "glibc_e_logl_source": "https://codebrowser.dev/glibc/glibc/sysdeps/x86_64/fpu/e_logl.S.html",
        },
        "source_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in [GLIBC_SOURCE, POINT_AUDIT]
            if path.exists()
        },
        "next_direct_attack_target": Y_LN2_ULP,
        "parallel_attack_targets": [MPFR_RESCAN],
        "plain_conclusion": (
            "x87 精度硬点进一步压缩：如果能证明 glibc 的 y=ln2 型 FYL2X/FYL2XP1 调用"
            "有 1.5 ulp 级误差，1e-12 预算有约 3.84e5 倍余量，table_012 log oracle 即可闭合。"
            "但现阶段不能把常见的 y=1 精度陈述直接套到 y=ln2；剩余原子是该适用性证明，"
            "或改走 MPFR 外向 log 全量重扫。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict table_012 x87 指令精度前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"glibc_logl_source_binding_imported={fmt_bool(result['glibc_logl_source_binding_imported'])}",
        f"x87_1p5ulp_budget_would_close_log_oracle={fmt_bool(result['x87_1p5ulp_budget_would_close_log_oracle'])}",
        f"fyl2x_y_equals_ln2_accuracy_applicability_closed={fmt_bool(result['fyl2x_y_equals_ln2_accuracy_applicability_closed'])}",
        f"x87_instruction_accuracy_closed={fmt_bool(result['x87_instruction_accuracy_closed'])}",
        f"std_logl_abs_error_1e_minus_12_closed={fmt_bool(result['std_logl_abs_error_1e_minus_12_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 预算",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["budget"].items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. CPU 环境",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["cpu"].items():
        lines.append(f"| `{table_cell(key)}` | `{table_cell(value)}` |")
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
    print(f"x87_1p5ulp_budget_would_close_log_oracle={fmt_bool(result['x87_1p5ulp_budget_would_close_log_oracle'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
