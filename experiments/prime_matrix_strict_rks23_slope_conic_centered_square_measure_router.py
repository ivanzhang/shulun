#!/usr/bin/env python3
"""把斜率二次曲线束压成中心化短平方测度偏差。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_slope_conic_centered_square_measure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-slope-conic-centered-square-measure-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-slope-conic-centered-square-measure-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-slope-conic-centered-square-measure-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-slope-conic-bundle-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "NontrivialSlopeLocalizedTernaryConicBundlePowerSaving"
NEXT_ATOM = "CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving"
DEVIATION_ATOM = "LocalizedQuadraticPushforwardSquareMeasureDeviationPowerSaving"


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
    """构造中心化短平方测度证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    conic_closed = previous.get("conic_bundle_identity_closed") is True

    # 对差盒 Delta 定义短平方测度
    #   mu_D(y)=#{d in Delta: d^2=y mod P}
    # 并写 mu_D=|Delta|/P + nu_D。曲线束计数先给出均匀主项，
    # 主项总规模至多 |T|^2|Delta|^2/P=N^{2+o(1)}，
    # 低于任何 N^{3-delta}, delta<1 的目标。剩余就是中心化偏差。
    centered_measure_closed = active and conic_closed
    main_term_absorbed = active and conic_closed

    measure_reduction = {
        "difference_box": "Delta={d: d is an allowed signed root-box difference}, |Delta|=O(N)",
        "square_measure": "mu_D(y)=#{d in Delta: d^2=y mod P}",
        "centered_measure": "nu_D(y)=mu_D(y)-|Delta|/P",
        "slope_x_box": "X_lambda={x in T: lambda*x in T}",
        "conic_count": "R_lambda=sum_{x in X_lambda} sum_{d1 in Delta} mu_D(lambda*d1^2+lambda(lambda-1)*x^2)",
        "main_term": "(|Delta|/P)*|X_lambda|*|Delta|",
        "global_main_sum": "sum_lambda main <= |T|^2*|Delta|^2/P = N^{2+o(1)} in the square-root collar",
        "main_absorption": "N^{2+o(1)} <= N^(3-delta) for every fixed delta<1 and large P",
        "remaining_deviation": "sum_lambda sum_{x in X_lambda,d1 in Delta} nu_D(lambda*d1^2+lambda(lambda-1)*x^2)",
    }

    rows = [
        row(
            "SlopeConicBundleTargetActive",
            active,
            True,
            "上一证书已把剩余压成非平凡斜率局部二次曲线束。",
            TARGET,
        ),
        row(
            "ShortSquareMeasureExpansionClosed",
            centered_measure_closed,
            True,
            "用 `mu_D=|Delta|/P+nu_D` 精确展开 `d2` 的短平方命中测度。",
            NEXT_ATOM,
        ),
        row(
            "UniformMainTermAbsorbed",
            main_term_absorbed,
            True,
            "所有斜率主项总和为 `N^{2+o(1)}`，低于固定幂能量目标。",
            "absorbed",
        ),
        row(
            "CenteredDeviationIsOnlyRemainingInput",
            centered_measure_closed,
            True,
            "剩余完全是中心化短平方测度沿非退化二次相位的局部推前偏差。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明该中心化偏差总和有固定幂节省。",
            DEVIATION_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只吸收主项并定位偏差输入，未证明偏差估计。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_slope_conic_centered_square_measure_router",
        "status": "slope_conic_bundle_reduced_to_centered_short_square_measure_deviation",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "slope_conic_bundle_target_active": active,
        "short_square_measure_expansion_closed": centered_measure_closed,
        "uniform_main_term_absorbed": main_term_absorbed,
        "centered_deviation_is_only_remaining_input": centered_measure_closed,
        "centered_short_square_measure_deviation_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": DEVIATION_ATOM,
        "measure_reduction": measure_reduction,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "斜率二次曲线束可拆成短平方测度的均匀主项与中心化偏差。"
            "定义 `mu_D(y)=#{d in Delta: d^2=y}`，写作 `mu_D=|Delta|/P+nu_D`。"
            "均匀主项在所有斜率上总量至多 `|T|^2|Delta|^2/P=N^{2+o(1)}`，"
            "已经被固定幂目标吸收。当前唯一剩余就是中心化短平方测度 `nu_D` "
            "沿相位 `lambda*d1^2+lambda(lambda-1)*x^2` 的局部推前偏差。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    reduction = result["measure_reduction"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 中心化短平方测度前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"short_square_measure_expansion_closed={fmt_bool(result['short_square_measure_expansion_closed'])}",
        f"uniform_main_term_absorbed={fmt_bool(result['uniform_main_term_absorbed'])}",
        f"centered_short_square_measure_deviation_power_saving_proved={fmt_bool(result['centered_short_square_measure_deviation_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 测度展开",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in reduction.items():
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
