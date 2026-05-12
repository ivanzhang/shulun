#!/usr/bin/env python3
"""生成 strict 高尾 b=28 放松平方根核路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_high_tail_b28_relaxed_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-high-tail-b28-relaxed-kernel-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-high-tail-b28-relaxed-kernel-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-high-tail-b28-relaxed-kernel-router.md"

PSI_EPS = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-internalization-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [PSI_EPS, CLAIM_STATUS]

TARGET = "PsiEpsilonHighTailB28SelfContainedLedger"
RELAXED = "PsiHighTailB28OneSidedTargetRelativeLedger"
SQRT_KERNEL = "VerifiedZeroSqrtPsiKernelCLe0p042304FromB28Ledger"
FULL_TABLE = "SchoenfeldDusartPsiEpsilonTableInternalizationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

X_HIGH = math.exp(28)
TARGET_RELATIVE = 1.0 / 36260.0
DUSART_EPS_HIGH = 0.00002224
SCHOENFELD_RH_C = 1.0 / (8.0 * math.pi)
ALLOWED_SQRT_C = TARGET_RELATIVE * math.exp(14) / (28.0**2)
C_ZERO_SUM = 65536.0
C_REGION = 1280.0
T0 = 14.0


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


def current_zero_free_relative(x: float) -> float:
    """复用当前 C=1280,C_Z=65536 模板，估计 psi 相对包络。"""
    return C_ZERO_SUM * math.log(x * (T0 + 3.0)) ** 2 * math.exp(
        -math.log(x) / (C_REGION * math.log(T0 + 3.0))
    )


def build_result() -> dict[str, Any]:
    """构造高尾放松平方根核证书。"""
    psi = load_json(PSI_EPS)
    active = psi.get("next_direct_attack_target") == TARGET
    rh_relative_at_b28 = SCHOENFELD_RH_C * math.exp(-14) * 28.0**2
    current_relative = current_zero_free_relative(X_HIGH)
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            psi.get("counterexample_assumption_only") is True and psi.get("row_column_unconditional_closed") is False,
            True,
            "本步只放松高尾解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "HighTailB28GateActive",
            active,
            True,
            "上一证书把下一最窄点设为 b=28 高尾 psi 上界。",
            TARGET,
        ),
        row(
            RELAXED,
            DUSART_EPS_HIGH < TARGET_RELATIVE,
            True,
            "高尾为了接 Dusart P5.1 只需 psi(x)-x<x/36260；完整 0.00002224 表值是更强输入。",
            TARGET,
        ),
        row(
            "SchoenfeldRHShapeWouldFitB28",
            rh_relative_at_b28 < TARGET_RELATIVE,
            True,
            "若能无条件内化 verified-zero 平方根核常数 1/(8pi)，则 b=28 高尾有正余量。",
            SQRT_KERNEL,
        ),
        row(
            "AllowedSqrtKernelConstantComputed",
            SCHOENFELD_RH_C < ALLOWED_SQRT_C,
            True,
            "b=28 处允许平方根核常数 C<=0.042304；Schoenfeld RH 型常数约 0.039789，余量约 6.3%。",
            SQRT_KERNEL,
        ),
        row(
            "CurrentC1280C65536TemplateStillFailsRelaxedHighTail",
            current_relative <= TARGET_RELATIVE,
            False,
            "即使用放松目标，当前粗 contour 在 e^28 处仍比目标大约 2.24e12 倍。",
            SQRT_KERNEL,
        ),
        row(
            TARGET,
            False,
            False,
            "高尾仍未自足闭合；最窄替代是证明 verified-zero 平方根核，或完整内化 Schoenfeld/Dusart psi 表。",
            f"{SQRT_KERNEL} OR {FULL_TABLE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "高尾放松不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_high_tail_b28_relaxed_kernel_router",
        "status": "high_tail_b28_reduced_from_full_epsilon_table_to_verified_zero_sqrt_kernel",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "high_tail_b28_relaxed_arithmetic_closed": DUSART_EPS_HIGH < TARGET_RELATIVE,
        "schoenfeld_rh_shape_would_fit_b28": rh_relative_at_b28 < TARGET_RELATIVE,
        "high_tail_b28_self_contained_closed": False,
        "psi_epsilon_table_self_contained_closed": False,
        "direct_internal_dusart_theta_pnt_envelope_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "diagnostics": {
            "x_high": X_HIGH,
            "target_relative_1_over_36260": TARGET_RELATIVE,
            "dusart_eps_high": DUSART_EPS_HIGH,
            "dusart_eps_margin_to_target": TARGET_RELATIVE - DUSART_EPS_HIGH,
            "schoenfeld_rh_c": SCHOENFELD_RH_C,
            "allowed_sqrt_kernel_c_at_b28": ALLOWED_SQRT_C,
            "sqrt_kernel_c_slack_ratio": ALLOWED_SQRT_C / SCHOENFELD_RH_C,
            "schoenfeld_rh_shape_relative_at_b28": rh_relative_at_b28,
            "schoenfeld_rh_shape_margin": TARGET_RELATIVE - rh_relative_at_b28,
            "current_c1280_c65536_relative_at_b28": current_relative,
            "current_template_gap_factor_vs_relaxed_target": current_relative / TARGET_RELATIVE,
        },
        "replacement_self_contained": {
            TARGET: f"{SQRT_KERNEL} OR {FULL_TABLE}",
            RELAXED: SQRT_KERNEL,
        },
        "next_direct_attack_target": SQRT_KERNEL,
        "parallel_attack_targets": [FULL_TABLE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "b=28 高尾不必完整复现 Dusart 表值 0.00002224；对行命题当前拼接而言，"
            "只需证明 `psi(x)-x<x/36260` for `x>=e^28`。这等价于在 RH 型平方根核 "
            "`C sqrt(x) log^2 x` 中取得 `C<=0.042304`；Schoenfeld 的 `1/(8pi)` 形状会有约 6.3% "
            "常数余量。但这是 verified-zero 平方根核输入，当前 C=1280,C_Z=65536 粗 contour 仍远远不足。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    d = result["diagnostics"]
    lines = [
        "# Prime Matrix strict 高尾 b=28 放松平方根核路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"high_tail_b28_relaxed_arithmetic_closed={fmt_bool(result['high_tail_b28_relaxed_arithmetic_closed'])}",
        f"schoenfeld_rh_shape_would_fit_b28={fmt_bool(result['schoenfeld_rh_shape_would_fit_b28'])}",
        f"high_tail_b28_self_contained_closed={fmt_bool(result['high_tail_b28_self_contained_closed'])}",
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
        f"| Dusart eps high | `{d['dusart_eps_high']:.12e}` |",
        f"| Dusart eps margin | `{d['dusart_eps_margin_to_target']:.12e}` |",
        f"| allowed sqrt kernel C | `{d['allowed_sqrt_kernel_c_at_b28']:.12e}` |",
        f"| Schoenfeld RH-shape C | `{d['schoenfeld_rh_c']:.12e}` |",
        f"| sqrt C slack ratio | `{d['sqrt_kernel_c_slack_ratio']:.12e}` |",
        f"| RH-shape relative at b=28 | `{d['schoenfeld_rh_shape_relative_at_b28']:.12e}` |",
        f"| RH-shape margin | `{d['schoenfeld_rh_shape_margin']:.12e}` |",
        f"| current C1280/C65536 relative | `{d['current_c1280_c65536_relative_at_b28']:.12e}` |",
        f"| current gap factor vs relaxed target | `{d['current_template_gap_factor_vs_relaxed_target']:.12e}` |",
        "",
        "## 2. 自足替换",
        "",
        "```text",
    ]
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
