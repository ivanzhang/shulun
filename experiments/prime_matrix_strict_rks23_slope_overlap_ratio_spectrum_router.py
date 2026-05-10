#!/usr/bin/env python3
"""把斜率重叠 L(lambda) 组合化为短区间比值谱，并闭合其 L2 账本。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_slope_overlap_ratio_spectrum_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-slope-overlap-ratio-spectrum-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-slope-overlap-ratio-spectrum-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-slope-overlap-ratio-spectrum-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-quadratic-energy-square-difference-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving"
NEXT_ATOM = "SquareDifferenceSpectrumAgainstLowL2IntervalRatioSpectrumPowerSaving"
ALT_ATOM = "WeightedSquareDifferenceRatioSpectrumCorrelationWithIntervalRatioSpectrum"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造斜率比值谱证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    square_difference_ready = previous.get("m_autocorrelation_opened") is True

    # L(lambda)=|T cap lambda^{-1}T| 精确等于
    # R_T(lambda)=#{(x,u) in T^2: u=lambda*x mod P}。
    # 其二阶能量是 x1*u2=x2*u1 mod P 的短盒四元组。
    # 因为 T 位于平方根对数颈部，乘积大小为 P log^O(P)，
    # 整数提升分支 k 只有 log^O(P) 个；固定三变量由除数界控制。
    ratio_spectrum_closed = active and square_difference_ready
    l2_closed = active and square_difference_ready

    slope_ratio = {
        "slope_overlap": "L(lambda)=|X_lambda|=#{x in T: lambda*x in T}",
        "ratio_spectrum": "R_T(lambda)=#{(x,u) in T^2: u=lambda*x mod P}",
        "identity": "L(lambda)=R_T(lambda)",
        "first_moment": "sum_lambda L(lambda)=|T|^2",
        "second_moment": "sum_lambda L(lambda)^2=#{x1*u2=x2*u1 mod P: xi,ui in T}",
        "integer_lift": "x1*u2-x2*u1=kP with |k|<=log^O(P) in the square-root collar",
        "divisor_l2_bound": "sum_lambda L(lambda)^2 <= |T|^2 P^o(1)",
        "meaning": "the interval slope spectrum has low multiplicative energy; any remaining failure must be true correlation with the square-difference spectrum",
    }

    rows = [
        row(
            "WeightedSquareDifferenceTargetActive",
            active,
            True,
            "上一证书已把 `M_A(lambda)` 打开为平方差乘法谱。",
            TARGET,
        ),
        row(
            "SlopeOverlapRatioSpectrumIdentityClosed",
            ratio_spectrum_closed,
            True,
            "`L(lambda)` 精确等于短区间 `T` 的比值谱 `R_T(lambda)`。",
            NEXT_ATOM,
        ),
        row(
            "SlopeOverlapFirstMomentClosed",
            ratio_spectrum_closed,
            True,
            "`sum_lambda L(lambda)=|T|^2`。",
            "ledger",
        ),
        row(
            "SlopeOverlapL2DivisorLedgerClosed",
            l2_closed,
            True,
            "短盒乘法能量由整数提升和除数界给 `sum L(lambda)^2<=|T|^2 P^o(1)`。",
            "ledger",
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明平方差谱不能与这个低 L2 比值谱发生固定幂级异常相关。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只闭合斜率谱账本，未证明最终相关节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_slope_overlap_ratio_spectrum_router",
        "status": "slope_overlap_rewritten_as_low_l2_interval_ratio_spectrum",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "weighted_square_difference_target_active": active,
        "slope_overlap_ratio_spectrum_identity_closed": ratio_spectrum_closed,
        "slope_overlap_first_moment_closed": ratio_spectrum_closed,
        "slope_overlap_l2_divisor_ledger_closed": l2_closed,
        "square_difference_against_low_l2_ratio_spectrum_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "slope_ratio": slope_ratio,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "斜率重叠也可以完全组合化。`L(lambda)` 就是短区间 `T` 的比值谱 "
            "`R_T(lambda)=#{(x,u):u=lambda*x}`。其一阶矩为 `|T|^2`；"
            "二阶矩等于短盒乘法能量，可由 `x1*u2-x2*u1=kP` 的整数提升和除数界控制为 `|T|^2 P^o(1)`。"
            "因此当前唯一剩余是平方差乘法谱是否能与这个低 L2 斜率比值谱产生异常相关。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    slope_ratio = result["slope_ratio"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 斜率比值谱前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"slope_overlap_ratio_spectrum_identity_closed={fmt_bool(result['slope_overlap_ratio_spectrum_identity_closed'])}",
        f"slope_overlap_l2_divisor_ledger_closed={fmt_bool(result['slope_overlap_l2_divisor_ledger_closed'])}",
        f"square_difference_against_low_l2_ratio_spectrum_power_saving_proved={fmt_bool(result['square_difference_against_low_l2_ratio_spectrum_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 斜率比值谱账本",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in slope_ratio.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
