#!/usr/bin/env python3
"""收束 RKS23 当前严格内部线的最终相关原子。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_final_correlation_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-final-correlation-atom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-final-correlation-atom-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-final-correlation-atom-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-slope-overlap-ratio-spectrum-router.json"
SQUARE_DIFF = MONO / "prime-matrix-strict-rks23-quadratic-energy-square-difference-router.json"
SOURCE_FILES = [PREVIOUS, SQUARE_DIFF]

TARGET = "SquareDifferenceSpectrumAgainstLowL2IntervalRatioSpectrumPowerSaving"
NEXT_ATOM = "JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum"


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
    """构造最终相关原子证书。"""
    previous = load_json(PREVIOUS)
    square = load_json(SQUARE_DIFF)

    active = previous.get("next_direct_attack_target") == TARGET
    slope_l2 = previous.get("slope_overlap_l2_divisor_ledger_closed") is True
    square_opened = square.get("m_autocorrelation_opened") is True

    final_atom_ready = active and slope_l2 and square_opened

    final_atom = {
        "square_difference_measure": "W(h)=#{(d,e) in Delta^2: d^2-e^2=h}",
        "square_difference_spectrum": "Q(lambda)=sum_h W(h)W(-lambda*h)",
        "slope_ratio_spectrum": "L(lambda)=#{(x,u) in T^2: u=lambda*x}",
        "closed_marginal_1": "sum_lambda L(lambda)=|T|^2",
        "closed_marginal_2": "sum_lambda L(lambda)^2<=|T|^2 P^o(1)",
        "closed_marginal_3": "M_A(lambda)=P*Q(lambda)-|Delta|^4",
        "required_joint_saving": "sum_lambda sqrt((P*Q(lambda)-|Delta|^4)*L(lambda)) <= P*N^2*N^(-delta)",
        "why_single_spectrum_bounds_fail": "Plancherel and the L2 ledger separately reach the natural scale; fixed power saving requires joint nonconcentration",
        "forbidden_shortcuts": "do not claim closure from average Q alone, average L alone, or plain Cauchy/Plancherel",
    }

    rows = [
        row(
            "FinalCorrelationTargetActive",
            active,
            True,
            "上一证书已把剩余固定为平方差谱与低 L2 比值谱的相关节省。",
            TARGET,
        ),
        row(
            "SquareDifferenceSpectrumReady",
            square_opened,
            True,
            "`M_A(lambda)` 已完全打开为平方差谱 `Q(lambda)`。",
            "closed marginal",
        ),
        row(
            "IntervalRatioSpectrumL2Ready",
            slope_l2,
            True,
            "`L(lambda)` 的一阶与二阶账本已由短盒整数提升闭合。",
            "closed marginal",
        ),
        row(
            "OnlyJointNonconcentrationRemains",
            final_atom_ready,
            True,
            "所有边际估计只能到自然尺度；剩余是两个谱不能同位集中。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明平方差谱峰值不能落在区间比值谱的大重叠斜率上。",
            "new internal hardpoint",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成最终相关原子收束，未证明该原子。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_final_correlation_atom_router",
        "status": "rks23_strict_internal_frontier_reduced_to_joint_nonconcentration_atom",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "final_correlation_target_active": active,
        "square_difference_spectrum_ready": square_opened,
        "interval_ratio_spectrum_l2_ready": slope_l2,
        "only_joint_nonconcentration_remains": final_atom_ready,
        "joint_nonconcentration_atom_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "final_atom": final_atom,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前严格内部 RKS23 线已收束为一个最终相关原子："
            "平方差谱 `Q(lambda)=sum_h W(h)W(-lambda*h)` 与短区间比值谱 "
            "`L(lambda)=#{(x,u):u=lambda*x}` 不能在同一批斜率上同时集中。"
            "两个边际账本已闭合，但它们单独只给自然尺度；真正剩余是联合非集中。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    final_atom = result["final_atom"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 最终相关原子证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"square_difference_spectrum_ready={fmt_bool(result['square_difference_spectrum_ready'])}",
        f"interval_ratio_spectrum_l2_ready={fmt_bool(result['interval_ratio_spectrum_l2_ready'])}",
        f"joint_nonconcentration_atom_proved={fmt_bool(result['joint_nonconcentration_atom_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最终相关原子",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in final_atom.items():
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
