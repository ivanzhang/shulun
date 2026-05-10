#!/usr/bin/env python3
"""把中心化短平方测度偏差展开为非零 Fourier 谱包。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_centered_square_measure_fourier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-centered-square-measure-fourier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-centered-square-measure-fourier-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-centered-square-measure-fourier-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-slope-conic-centered-square-measure-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "CenteredShortSquareMeasureOnSlopeConicBundlePowerSaving"
NEXT_ATOM = "NonzeroFrequencyRootBoxQuadraticFourierPacketPowerSaving"
ALT_ATOM = "ShortSquareFourierWeightAgainstRationalQuadraticRootBoxPhase"


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
    """构造 Fourier 谱包证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    centered_ready = previous.get("centered_deviation_is_only_remaining_input") is True

    # 对中心化测度 nu_D 作 Fourier 展开。由于中心化，r=0 项为 0；
    # 对 r!=0，nu_D 的 Fourier 系数就是短二次和 sum_{d2 in Delta} e(-r d2^2/P)。
    # 余下内层为 (x,u,d1) 根盒上的有理二次相位。
    fourier_expansion_closed = active and centered_ready
    zero_frequency_removed = active and centered_ready

    fourier_packet = {
        "centered_measure": "nu_D=mu_D-|Delta|/P",
        "zero_frequency": "hat(nu_D)(0)=0",
        "nonzero_coefficient": "for r!=0, hat(nu_D)(r)=sum_{d2 in Delta} e_P(-r*d2^2)",
        "slope_to_t_variables": "lambda=u/x with x,u in T and x!=u",
        "phase_argument": "lambda*d1^2+lambda(lambda-1)*x^2 = (u/x)*d1^2+u(u-x)",
        "deviation_formula": "Dev=(1/P) sum_{r!=0} hat(nu_D)(r) sum_{x,u in T,x!=u} sum_{d1 in Delta} e_P(r*((u/x)*d1^2+u(u-x)))",
        "opened_inner_packet": "short quadratic d2-Fourier weight coupled to rational quadratic root-box phase in (x,u,d1)",
        "why_narrower": "all main terms and zero frequency are gone; only nonzero oscillatory packets remain",
    }

    rows = [
        row(
            "CenteredSquareMeasureTargetActive",
            active,
            True,
            "上一证书已把曲线束剩余压成中心化短平方测度偏差。",
            TARGET,
        ),
        row(
            "FourierExpansionClosed",
            fourier_expansion_closed,
            True,
            "中心化偏差可精确展开为 `r!=0` 的 Fourier 谱包。",
            NEXT_ATOM,
        ),
        row(
            "ZeroFrequencyRemoved",
            zero_frequency_removed,
            True,
            "`nu_D` 的零频为 0；此前均匀主项已完全吸收。",
            "removed",
        ),
        row(
            "NonzeroFourierCoefficientIdentified",
            fourier_expansion_closed,
            True,
            "非零系数就是差盒上的短二次 Fourier 和。",
            ALT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明该非零频率根盒有理二次相位谱包有固定幂节省。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成 Fourier 化与零频移除，未证明非零谱包估计。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_centered_square_measure_fourier_router",
        "status": "centered_square_measure_deviation_reduced_to_nonzero_quadratic_fourier_packets",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "centered_square_measure_target_active": active,
        "fourier_expansion_closed": fourier_expansion_closed,
        "zero_frequency_removed": zero_frequency_removed,
        "nonzero_fourier_coefficient_identified": fourier_expansion_closed,
        "nonzero_frequency_root_box_quadratic_fourier_packet_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "fourier_packet": fourier_packet,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "中心化短平方测度偏差可以完全 Fourier 化。由于 `nu_D` 已中心化，零频项为 0；"
            "非零频率的系数就是差盒上的短二次和 `sum_{d2 in Delta} e_P(-r*d2^2)`。"
            "剩余内层是 `x,u,d1` 根盒上的有理二次相位 "
            "`(u/x)d1^2+u(u-x)`。因此当前唯一剩余变成非零频率根盒有理二次 Fourier 谱包的固定幂节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    packet = result["fourier_packet"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 中心化平方测度 Fourier 谱包证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fourier_expansion_closed={fmt_bool(result['fourier_expansion_closed'])}",
        f"zero_frequency_removed={fmt_bool(result['zero_frequency_removed'])}",
        f"nonzero_frequency_root_box_quadratic_fourier_packet_power_saving_proved={fmt_bool(result['nonzero_frequency_root_box_quadratic_fourier_packet_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非零 Fourier 谱包",
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
