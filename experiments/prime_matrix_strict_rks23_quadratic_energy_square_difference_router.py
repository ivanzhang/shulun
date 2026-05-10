#!/usr/bin/env python3
"""把二次 Fourier 能量自相关打开为短平方差谱的乘法自交。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_quadratic_energy_square_difference_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-quadratic-energy-square-difference-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-quadratic-energy-square-difference-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-quadratic-energy-square-difference-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-tri-quadratic-plancherel-barrier-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "CorrelatedQuadraticFourierEnergyOverlapPowerSaving"
NEXT_ATOM = "WeightedSquareDifferenceRatioOverlapAgainstSlopeOverlapPowerSaving"
ALT_ATOM = "SquareDifferenceMultiplicativeSpectrumSlopeCorrelationSaving"


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
    """构造平方差谱证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    barrier_closed = previous.get("per_slope_cauchy_plancherel_envelope_closed") is True

    # A(s)=sum_d e(s d^2)。展开 |A(r)|^2 得到平方差测度
    # W(h)=#{(d,e): d^2-e^2=h}。于是对 lambda!=0，
    # M_A(lambda)=sum_{r!=0}|A(r)|^2|A(lambda r)|^2
    # = P*sum_h W(h)W(-lambda*h)-|Delta|^4。
    identity_closed = active and barrier_closed
    zero_subtraction_closed = active and barrier_closed

    square_difference = {
        "quadratic_sum": "A(s)=sum_{d in Delta} e_P(s*d^2)",
        "square_difference_measure": "W(h)=#{(d,e) in Delta^2: d^2-e^2=h mod P}",
        "fourier_identity": "|A(r)|^2=sum_h W(h)e_P(r*h)",
        "energy_autocorrelation": "M_A(lambda)=sum_{r!=0}|A(r)|^2|A(lambda*r)|^2",
        "opened_formula": "M_A(lambda)=P*sum_h W(h)W(-lambda*h)-|Delta|^4",
        "meaning": "large M_A(lambda) is exactly a large multiplicative overlap of the square-difference measure W with its lambda-dilate",
        "correlation_target": "sum_lambda sqrt((P*<W,lambda W>-|Delta|^4)*L(lambda))",
        "new_language": "weighted square-difference ratio spectrum correlated with the interval slope-overlap spectrum",
    }

    rows = [
        row(
            "CorrelatedEnergyOverlapTargetActive",
            active,
            True,
            "上一证书已把剩余压成 `M_A(lambda)` 与 `L(lambda)` 的相关节省。",
            TARGET,
        ),
        row(
            "SquareDifferenceMeasureIdentityClosed",
            identity_closed,
            True,
            "`|A(r)|^2` 精确等于平方差测度 `W` 的 Fourier 变换。",
            NEXT_ATOM,
        ),
        row(
            "MAutocorrelationOpened",
            identity_closed,
            True,
            "`M_A(lambda)=P*sum_h W(h)W(-lambda*h)-|Delta|^4`，无隐藏解析输入。",
            NEXT_ATOM,
        ),
        row(
            "ZeroFrequencySubtractionAccounted",
            zero_subtraction_closed,
            True,
            "`-|Delta|^4` 正是去掉 `r=0` 后的零频扣除。",
            "accounted",
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明平方差乘法谱与斜率重叠谱之间有固定幂相关节省。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只把 Fourier 能量改写为平方差谱，未证明相关节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_quadratic_energy_square_difference_router",
        "status": "quadratic_fourier_energy_opened_as_square_difference_multiplicative_overlap",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "correlated_energy_overlap_target_active": active,
        "square_difference_measure_identity_closed": identity_closed,
        "m_autocorrelation_opened": identity_closed,
        "zero_frequency_subtraction_accounted": zero_subtraction_closed,
        "weighted_square_difference_slope_correlation_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "square_difference": square_difference,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "二次 Fourier 能量自相关可以完全组合化。"
            "令 `W(h)=#{(d,e):d^2-e^2=h}`，则 `|A(r)|^2` 是 `W` 的 Fourier 变换，"
            "并且 `M_A(lambda)=P*sum_h W(h)W(-lambda*h)-|Delta|^4`。"
            "所以当前剩余不再是抽象 Fourier 能量，而是平方差测度的乘法重叠谱与根盒斜率重叠谱之间的相关节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    square_difference = result["square_difference"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 平方差谱前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"square_difference_measure_identity_closed={fmt_bool(result['square_difference_measure_identity_closed'])}",
        f"m_autocorrelation_opened={fmt_bool(result['m_autocorrelation_opened'])}",
        f"weighted_square_difference_slope_correlation_saving_proved={fmt_bool(result['weighted_square_difference_slope_correlation_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 平方差谱展开",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in square_difference.items():
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
