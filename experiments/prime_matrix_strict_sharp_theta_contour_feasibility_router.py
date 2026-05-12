#!/usr/bin/env python3
"""生成 strict 尖锐 theta contour 起点可行性路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_sharp_theta_contour_feasibility_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-sharp-theta-contour-feasibility-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-sharp-theta-contour-feasibility-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-sharp-theta-contour-feasibility-router.md"

GAP = MONOGRAPH / "prime-matrix-strict-internal-theta-contour-budget-gap-router.json"
FINITE_THETA = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [GAP, FINITE_THETA, CLAIM_STATUS]

TARGET = "SharpInternalThetaContourStartBudgetLedger"
DIRECT_PNT = "DirectInternalDusartThetaPNTEnvelopeLedger"
SHARP_ZERO_FREE = "SharpZeroFreeExponentAndZeroSumConstantLedger"
HUGE_FINITE = "RaisedAnalyticThresholdFiniteThetaBridgeExtensionLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000.0
HEIGHT_T0 = 14.0
TARGET_DENOMINATOR = 36_260.0
TARGET_RELATIVE = 1.0 / TARGET_DENOMINATOR
CURRENT_C_ZERO_SUM = 65_536.0
CURRENT_C_REGION = 1_280.0


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


def fmt_float(value: float) -> str:
    """固定数值格式。"""
    return f"{value:.12g}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contour_relative(c_zero_sum: float, c_region: float, x: float = ANCHOR_X, height: float = HEIGHT_T0) -> float:
    """当前模板的相对包络：C_Z log^2(x(T+3)) exp(-log x/(C_region log(T+3)))。"""
    log_kernel = math.log(x * (height + 3.0))
    suppression = math.exp(-math.log(x) / (c_region * math.log(height + 3.0)))
    return c_zero_sum * log_kernel * log_kernel * suppression


def required_c_zero_sum(c_region: float = CURRENT_C_REGION) -> float:
    """在固定零点自由区常数时允许的 C_Z 上界。"""
    log_kernel = math.log(ANCHOR_X * (HEIGHT_T0 + 3.0))
    suppression = math.exp(-math.log(ANCHOR_X) / (c_region * math.log(HEIGHT_T0 + 3.0)))
    return TARGET_RELATIVE / (log_kernel * log_kernel * suppression)


def required_c_region(c_zero_sum: float = CURRENT_C_ZERO_SUM) -> float:
    """在固定 C_Z 时所需的零点自由区常数上界。"""
    log_kernel = math.log(ANCHOR_X * (HEIGHT_T0 + 3.0))
    needed_suppression = TARGET_RELATIVE / (c_zero_sum * log_kernel * log_kernel)
    if not 0 < needed_suppression < 1:
        return math.inf
    return -math.log(ANCHOR_X) / (math.log(HEIGHT_T0 + 3.0) * math.log(needed_suppression))


def feasibility_rows() -> list[dict[str, Any]]:
    """生成可行性量化表。"""
    current = contour_relative(CURRENT_C_ZERO_SUM, CURRENT_C_REGION)
    allowed_cz = required_c_zero_sum(CURRENT_C_REGION)
    required_cr = required_c_region(CURRENT_C_ZERO_SUM)
    return [
        {
            "scenario": "current template",
            "C_zero_sum": CURRENT_C_ZERO_SUM,
            "C_region": CURRENT_C_REGION,
            "relative_bound": current,
            "ratio_to_target": current / TARGET_RELATIVE,
            "passes": current <= TARGET_RELATIVE,
        },
        {
            "scenario": "keep C_region=1280",
            "C_zero_sum": allowed_cz,
            "C_region": CURRENT_C_REGION,
            "relative_bound": TARGET_RELATIVE,
            "ratio_to_target": 1.0,
            "passes": allowed_cz >= 1.0,
        },
        {
            "scenario": "keep C_zero_sum=65536",
            "C_zero_sum": CURRENT_C_ZERO_SUM,
            "C_region": required_cr,
            "relative_bound": TARGET_RELATIVE,
            "ratio_to_target": 1.0,
            "passes": required_cr >= 1.0,
        },
        {
            "scenario": "even C_zero_sum=1",
            "C_zero_sum": 1.0,
            "C_region": required_c_region(1.0),
            "relative_bound": TARGET_RELATIVE,
            "ratio_to_target": 1.0,
            "passes": required_c_region(1.0) >= 1.0,
        },
    ]


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
    """构造尖锐 contour 可行性证书。"""
    gap = load_json(GAP)
    finite = load_json(FINITE_THETA)
    feasibility = feasibility_rows()
    current = feasibility[0]
    allowed_cz = feasibility[1]["C_zero_sum"]
    required_cr = feasibility[2]["C_region"]
    shallow_constant_tuning_possible = allowed_cz >= 1.0 or required_cr >= 1.0
    finite_bridge_ready = finite.get("finite_theta_bridge_below_20000_self_contained_closed") is True
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            gap.get("counterexample_assumption_only") is True and gap.get("row_column_unconditional_closed") is False,
            True,
            "本步只量化高段 theta contour 起点输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "FiniteThetaInterfaceReady",
            finite_bridge_ready,
            True,
            "有限 theta 桥已把接口左侧闭合，尖锐 contour 只需从 x=20000 右侧接上。",
            "接口不是剩余硬点。",
        ),
        row(
            "CurrentContourTemplateFailsAtAnchor",
            current["passes"] is False,
            True,
            "当前 C_Z=65536、C_region=1280 模板在锚点处远超目标。",
            TARGET,
        ),
        row(
            "ShallowConstantTuningPossible",
            shallow_constant_tuning_possible,
            shallow_constant_tuning_possible,
            "若只沿当前模板调常数，则需 C_Z<1 或 C_region<1，已经不是小修小补。",
            f"{DIRECT_PNT} OR {SHARP_ZERO_FREE}",
        ),
        row(
            "SharpInternalThetaContourStartBudgetClosed",
            False,
            False,
            "当前分析只证明必须换更强的显式 PNT/theta 机制，不能关闭尖锐 contour 输入。",
            f"{DIRECT_PNT} OR {SHARP_ZERO_FREE} OR {HUGE_FINITE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "该可行性证书不产生最终反例矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_sharp_theta_contour_feasibility_router",
        "status": "sharp_theta_contour_start_requires_new_pnt_mechanism_not_constant_tuning",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_theta_interface_ready": finite_bridge_ready,
        "current_contour_template_fails_at_anchor": current["passes"] is False,
        "shallow_constant_tuning_possible": shallow_constant_tuning_possible,
        "sharp_internal_theta_contour_start_budget_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_relative_error": TARGET_RELATIVE,
        "current_ratio_to_target": current["ratio_to_target"],
        "allowed_c_zero_sum_if_c_region_1280": allowed_cz,
        "required_c_region_if_c_zero_sum_65536": required_cr,
        "required_c_region_if_c_zero_sum_1": feasibility[3]["C_region"],
        "replacement_self_contained": {
            TARGET: f"{DIRECT_PNT} OR {SHARP_ZERO_FREE} OR {HUGE_FINITE}",
        },
        "next_direct_attack_target": DIRECT_PNT,
        "parallel_attack_targets": [SHARP_ZERO_FREE, HUGE_FINITE],
        "feasibility_rows": feasibility,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "尖锐 theta contour 起点不能靠当前模板的常数微调闭合：若保留 `C_region=1280`，"
            "允许的 `C_Z` 只有约 `1.70e-7`；若保留 `C_Z=65536`，所需 `C_region` 约为 `0.131`。"
            "即使把 `C_Z` 降到 `1`，仍需 `C_region≈0.224`。这说明剩余不是算术微调，"
            "而是必须内化 Dusart 型直接 theta/PNT 机制，或引入实质更强的零点自由/零点和输入。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix strict 尖锐 theta contour 起点可行性路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_theta_interface_ready={fmt_bool(result['finite_theta_interface_ready'])}",
        f"current_contour_template_fails_at_anchor={fmt_bool(result['current_contour_template_fails_at_anchor'])}",
        f"shallow_constant_tuning_possible={fmt_bool(result['shallow_constant_tuning_possible'])}",
        f"sharp_internal_theta_contour_start_budget_closed={fmt_bool(result['sharp_internal_theta_contour_start_budget_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 可行性门槛",
        "",
        "| scenario | C_zero_sum | C_region | relative_bound | ratio_to_target | passes |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in result["feasibility_rows"]:
        lines.append(
            f"| {table_cell(item['scenario'])} | `{fmt_float(float(item['C_zero_sum']))}` | "
            f"`{fmt_float(float(item['C_region']))}` | `{fmt_float(float(item['relative_bound']))}` | "
            f"`{fmt_float(float(item['ratio_to_target']))}` | `{fmt_bool(item['passes'])}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
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
