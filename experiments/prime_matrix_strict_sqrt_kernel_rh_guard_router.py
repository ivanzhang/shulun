#!/usr/bin/env python3
"""生成 strict 平方根核 RH-level 守门路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_sqrt_kernel_rh_guard_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sqrt-kernel-rh-guard-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-sqrt-kernel-rh-guard-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-sqrt-kernel-rh-guard-router.md"

HIGH_TAIL = MONOGRAPH / "prime-matrix-strict-high-tail-b28-relaxed-kernel-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [HIGH_TAIL, CLAIM_STATUS]

TARGET = "VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger"
SCHOENFELD_COND = "SchoenfeldRHConditionalPsiSqrtKernelC1Over8PiLedger"
GLOBAL_RH = "GlobalRHOrVonKochEquivalentPNTErrorInput"
FINITE_WINDOW = "FiniteVerifiedZeroWindowPsiKernelLedger"
HIGH_ZERO_TAIL = "UnconditionalHighZeroTailDensityFreeBridgeCLe0p042304Ledger"
UNCOND_TABLE = "SchoenfeldDusartPsiEpsilonTableInternalizationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SCHOENFELD_URL = "https://www.ams.org/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf"
DUSART_URL = "https://arxiv.org/abs/1002.0442"

X_HIGH = math.exp(28.0)
TARGET_RELATIVE = 1.0 / 36260.0
ALLOWED_C = TARGET_RELATIVE * math.exp(14.0) / (28.0**2)
SCHOENFELD_C = 1.0 / (8.0 * math.pi)
SCHOENFELD_RELATIVE = SCHOENFELD_C * math.exp(-14.0) * (28.0**2)


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
    """构造平方根核 RH-level 守门证书。"""
    high_tail = load_json(HIGH_TAIL)
    active = high_tail.get("next_direct_attack_target") == TARGET
    schoenfeld_fits = SCHOENFELD_C < ALLOWED_C and SCHOENFELD_RELATIVE < TARGET_RELATIVE
    finite_window_global_tail_closed = False
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            high_tail.get("counterexample_assumption_only") is True
            and high_tail.get("row_column_unconditional_closed") is False,
            True,
            "本步只审查高尾解析核输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "SqrtKernelGateActive",
            active,
            True,
            "上一证书把下一最窄点设为 verified-zero 平方根核常数门。",
            TARGET,
        ),
        row(
            "SchoenfeldConstantArithmeticFitsB28",
            schoenfeld_fits,
            True,
            "若可使用 Schoenfeld RH 型平方根核常数 1/(8pi)，b=28 高尾常数有正余量。",
            SCHOENFELD_COND,
        ),
        row(
            "SchoenfeldKernelIsConditionalRHLevel",
            True,
            True,
            "Schoenfeld 的平方根级 psi 误差是 RH 条件型输入；不能作为无条件 verified-zero 结论直接使用。",
            GLOBAL_RH,
        ),
        row(
            "FiniteVerifiedZeroWindowDoesNotControlInfiniteTail",
            True,
            True,
            "有限高度零点验证只控制有限窗口；高于验证高度的零点仍需全局 RH、零点密度/零点自由尾项或等价 PNT 误差输入。",
            HIGH_ZERO_TAIL,
        ),
        row(
            "VerifiedZeroSqrtKernelCanCloseOnlyConditionally",
            True,
            False,
            "接受全局 RH 或等价 von-Koch 级 PNT 误差时，该核可条件关闭高尾；作者侧无条件路线不能据此闭合。",
            f"{SCHOENFELD_COND} AND {GLOBAL_RH}",
        ),
        row(
            "FiniteWindowPlusTailAlternativeOpen",
            finite_window_global_tail_closed,
            False,
            "若不接受 RH，必须给出有限 verified-zero 窗口加无限高零点尾部的无条件合成预算；当前仓库没有该常数级合成。",
            f"{FINITE_WINDOW} AND {HIGH_ZERO_TAIL}",
        ),
        row(
            TARGET,
            False,
            False,
            "该平方根核路径被标记为 RH-level 分支；不能作为行命题无条件闭合输入。",
            f"({SCHOENFELD_COND} AND {GLOBAL_RH}) OR ({FINITE_WINDOW} AND {HIGH_ZERO_TAIL})",
        ),
        row(
            "ReturnToUnconditionalDusartPsiTableRoute",
            True,
            True,
            "无条件主线应回到 Dusart/Schoenfeld 显式 psi 误差表内化，而不是用 RH 型平方根核冒充自足证明。",
            UNCOND_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "RH-level 守门审查不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_sqrt_kernel_rh_guard_router",
        "status": "sqrt_kernel_b28_marked_rh_level_unconditional_route_returns_to_dusart_psi_table",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "sqrt_kernel_constant_arithmetic_fits_b28": schoenfeld_fits,
        "sqrt_kernel_marked_rh_level": True,
        "finite_verified_zero_window_controls_infinite_tail": finite_window_global_tail_closed,
        "verified_zero_sqrt_kernel_self_contained_closed": False,
        "psi_epsilon_table_self_contained_closed": False,
        "direct_internal_dusart_theta_pnt_envelope_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "diagnostics": {
            "x_high": X_HIGH,
            "target_relative_1_over_36260": TARGET_RELATIVE,
            "allowed_sqrt_kernel_c_at_b28": ALLOWED_C,
            "schoenfeld_c_1_over_8pi": SCHOENFELD_C,
            "schoenfeld_relative_at_b28": SCHOENFELD_RELATIVE,
            "schoenfeld_margin_relative": TARGET_RELATIVE - SCHOENFELD_RELATIVE,
            "schoenfeld_constant_slack_ratio": ALLOWED_C / SCHOENFELD_C,
        },
        "external_references": [
            {
                "id": "Schoenfeld 1976 Math. Comput. 30(134)",
                "url": SCHOENFELD_URL,
                "role": "conditional RH square-root psi kernel source boundary",
            },
            {
                "id": "Dusart arXiv:1002.0442",
                "url": DUSART_URL,
                "role": "unconditional explicit psi/theta table route boundary",
            },
        ],
        "replacement_self_contained": {
            TARGET: f"({SCHOENFELD_COND} AND {GLOBAL_RH}) OR ({FINITE_WINDOW} AND {HIGH_ZERO_TAIL})",
            "UnconditionalHighTailRoute": UNCOND_TABLE,
        },
        "next_direct_attack_target": UNCOND_TABLE,
        "parallel_attack_targets": [f"{FINITE_WINDOW} AND {HIGH_ZERO_TAIL}", GLOBAL_RH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "b=28 平方根核常数门完成守门审查：`1/(8pi)` 的数值确实小于允许常数 `0.042304`，"
            "但这种对所有 `x>=e^28` 的平方根级 `psi` 误差是 RH-level 输入。有限 verified-zero "
            "窗口不能单独控制无限高尾；若不接受 RH 或等价 PNT 误差输入，就必须回到 Dusart/Schoenfeld "
            "无条件显式 `psi` 误差表内化路线。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    d = result["diagnostics"]
    lines = [
        "# Prime Matrix strict 平方根核 RH-level 守门路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sqrt_kernel_constant_arithmetic_fits_b28={fmt_bool(result['sqrt_kernel_constant_arithmetic_fits_b28'])}",
        f"sqrt_kernel_marked_rh_level={fmt_bool(result['sqrt_kernel_marked_rh_level'])}",
        f"finite_verified_zero_window_controls_infinite_tail={fmt_bool(result['finite_verified_zero_window_controls_infinite_tail'])}",
        f"verified_zero_sqrt_kernel_self_contained_closed={fmt_bool(result['verified_zero_sqrt_kernel_self_contained_closed'])}",
        f"psi_epsilon_table_self_contained_closed={fmt_bool(result['psi_epsilon_table_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 常数诊断",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| target relative `1/36260` | `{d['target_relative_1_over_36260']:.12e}` |",
        f"| allowed sqrt kernel C | `{d['allowed_sqrt_kernel_c_at_b28']:.12e}` |",
        f"| Schoenfeld C `1/(8pi)` | `{d['schoenfeld_c_1_over_8pi']:.12e}` |",
        f"| Schoenfeld relative at b=28 | `{d['schoenfeld_relative_at_b28']:.12e}` |",
        f"| relative margin | `{d['schoenfeld_margin_relative']:.12e}` |",
        f"| constant slack ratio | `{d['schoenfeld_constant_slack_ratio']:.12e}` |",
        "",
        "## 2. 外部边界",
        "",
    ]
    for ref in result["external_references"]:
        lines.append(f"- `{ref['id']}`：{ref['url']}；{ref['role']}")
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
