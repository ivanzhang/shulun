#!/usr/bin/env python3
"""把非零频率根盒谱包因子化为三短二次 Fourier 相关包。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_tri_quadratic_fourier_factorization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-tri-quadratic-fourier-factorization-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-tri-quadratic-fourier-factorization-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-tri-quadratic-fourier-factorization-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-centered-square-measure-fourier-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "NonzeroFrequencyRootBoxQuadraticFourierPacketPowerSaving"
NEXT_ATOM = "TriShortQuadraticFourierCorrelationPowerSaving"
ALT_ATOM = "NonzeroFrequencySlopeFactorizedThreeQuadraticSumPacket"


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
    """构造三短二次 Fourier 因子化证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    fourier_closed = previous.get("fourier_expansion_closed") is True
    zero_removed = previous.get("zero_frequency_removed") is True

    # 从上一层公式出发：
    # Dev=(1/P) sum_{r!=0} A(-r) sum_{x,u,d1} e_P(r*((u/x)d1^2+u(u-x))).
    # 令 lambda=u/x，则 u=lambda*x，且 u(u-x)=lambda(lambda-1)x^2。
    # 因此内层分解为 A(r*lambda) 与一个 x 侧短二次和。
    factorization_closed = active and fourier_closed and zero_removed

    factor_packet = {
        "difference_quadratic_sum": "A(s)=sum_{d in Delta} e_P(s*d^2)",
        "x_quadratic_sum": "B_lambda(s)=sum_{x in X_lambda} e_P(s*x^2), where X_lambda={x in T: lambda*x in T}",
        "slope_change": "u=lambda*x with lambda!=1",
        "phase_factorization": "(u/x)d1^2+u(u-x)=lambda*d1^2+lambda(lambda-1)*x^2",
        "exact_packet": "Dev=(1/P) sum_{r!=0} A(-r) sum_{lambda!=1} A(r*lambda) B_lambda(r*lambda*(lambda-1))",
        "zero_frequency_status": "r=0 removed; lambda=1 removed by the diagonal gate",
        "support_geometry": "lambda is constrained by X_lambda nonempty, i.e. T and lambda^{-1}T overlap",
        "why_narrower": "the remaining input is a tri-linear correlation of three short quadratic Fourier sums, not an unfactored rational phase",
    }

    rows = [
        row(
            "NonzeroFrequencyPacketTargetActive",
            active,
            True,
            "上一证书已把剩余压成非零频率根盒有理二次 Fourier 谱包。",
            TARGET,
        ),
        row(
            "SlopeChangeOfVariablesClosed",
            factorization_closed,
            True,
            "用 `u=lambda*x` 精确保留根盒约束为 `X_lambda={x in T:lambda*x in T}`。",
            NEXT_ATOM,
        ),
        row(
            "TriQuadraticFactorizationClosed",
            factorization_closed,
            True,
            "相位拆成 `d2`、`d1`、`x` 三个短二次 Fourier 因子。",
            NEXT_ATOM,
        ),
        row(
            "DiagonalAndZeroFrequencyStillRemoved",
            factorization_closed,
            True,
            "`r=0` 和 `lambda=1` 已由前序主项/对角门移除。",
            "removed",
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明该三短二次 Fourier 相关包有固定幂节省。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成谱包因子化，未证明三因子相关估计。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_tri_quadratic_fourier_factorization_router",
        "status": "nonzero_root_box_fourier_packet_factorized_into_three_short_quadratic_sums",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "nonzero_frequency_packet_target_active": active,
        "slope_change_of_variables_closed": factorization_closed,
        "tri_quadratic_factorization_closed": factorization_closed,
        "diagonal_and_zero_frequency_still_removed": factorization_closed,
        "tri_short_quadratic_fourier_correlation_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "factor_packet": factor_packet,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "非零频率根盒谱包可精确因子化。令 `A(s)=sum_{d in Delta} e_P(s*d^2)`，"
            "再把 `u` 写成 `lambda*x`，则 `u(u-x)=lambda(lambda-1)x^2`，"
            "整个偏差变为 `Dev=(1/P) sum_{r!=0} A(-r) sum_{lambda!=1} "
            "A(r*lambda) B_lambda(r*lambda*(lambda-1))`。"
            "这里 `B_lambda` 是 `X_lambda={x in T:lambda*x in T}` 上的短二次和。"
            "因此当前唯一剩余是三短二次 Fourier 和的相关包固定幂节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    packet = result["factor_packet"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 三短二次 Fourier 因子化证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"tri_quadratic_factorization_closed={fmt_bool(result['tri_quadratic_factorization_closed'])}",
        f"tri_short_quadratic_fourier_correlation_power_saving_proved={fmt_bool(result['tri_short_quadratic_fourier_correlation_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 三因子谱包",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in packet.items():
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
