#!/usr/bin/env python3
"""把内部 shifted product fiber 压成和变量判别式通道。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_interior_fiber_discriminant_corridor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-interior-fiber-discriminant-corridor-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-interior-fiber-discriminant-corridor-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-interior-fiber-discriminant-corridor-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-shifted-product-fiber-signed-lift-router.json"

SOURCE_FILES = [PREVIOUS]

TARGET = "InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar"
NEXT_ATOM = "InteriorQuadraticDiscriminantCorridorHighSpectrumPowerSaving"
CHAR_SUM_TARGET = "LocalizedQuadraticCharacterCorridorPowerSaving"
INCIDENCE_TARGET = "SumVariableHarmonicMeanCollisionIncidenceBound"


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
    """构造判别式通道证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    signed_small_absorbed = previous.get("signed_small_phase_high_spectrum_absorbed") is True

    # 对内部相位 c，令 t=a+b。由于 J 是平方根颈部整数块，
    # 大 P 区间有 t<P，可把 t 当作普通整数和变量。
    # 原方程 ab=c(a+b) mod P 等价于 a,b 是
    # X^2-tX+c*t=0 mod P 的两个根。
    # 因此二维纤维只剩一维 t 通道和判别式 Delta_c(t)=t(t-4c)。
    discriminant_corridor_closed = active and signed_small_absorbed
    high_spectrum_proved = False

    compression = {
        "interior_phase_scope": "min(c,P-c)>max J after signed-small phases are absorbed",
        "sum_variable": "t=a+b with t in J+J and, for large P, 0<t<P",
        "quadratic_for_roots": "X^2-tX+c*t=0 mod P",
        "discriminant": "Delta_c(t)=t^2-4ct=t(t-4c)",
        "fiber_reconstruction": "each admissible t gives at most two ordered roots a,b, then the root-localization cut requires a,b in J",
        "high_fiber_implication": "r_c>N^(1-eta) forces >N^(1-eta)/2 localized t-values with Delta_c(t) a square",
        "dimension_drop": "2D shifted product fiber -> 1D discriminant square-return corridor",
        "why_this_is_narrower": "the remaining obstruction is no longer arbitrary modular hyperbola incidence, but a localized quadratic character corridor with root cuts",
    }

    rows = [
        row(
            "InteriorShiftedProductTargetActive",
            active,
            True,
            "上一证书已吸收有符号小相位，真正剩余是内部相位 shifted product 高谱。",
            TARGET,
        ),
        row(
            "SumVariableQuadraticCompressionClosed",
            discriminant_corridor_closed,
            True,
            "令 `t=a+b` 后，`a,b` 必为 `X^2-tX+c*t=0` 的两根。",
            NEXT_ATOM,
        ),
        row(
            "DiscriminantCorridorIdentityClosed",
            discriminant_corridor_closed,
            True,
            "纤维计数被一维条件 `Delta_c(t)=t(t-4c)` 为平方并满足根落回 `J` 控制。",
            NEXT_ATOM,
        ),
        row(
            "InteriorHighFiberForcesDenseSquareReturnCorridor",
            discriminant_corridor_closed,
            True,
            "若某内部相位仍高重叠，则对应判别式通道中有密集平方返回。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            high_spectrum_proved,
            False,
            "仓库内尚未证明内部相位不可能产生密集局部平方返回通道。",
            f"{CHAR_SUM_TARGET} OR {INCIDENCE_TARGET}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成二维到一维的等价压缩，未证明判别式通道的固定幂排斥。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_interior_fiber_discriminant_corridor_router",
        "status": "interior_shifted_product_fiber_reduced_to_quadratic_discriminant_corridor",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "interior_shifted_product_target_active": active,
        "sum_variable_quadratic_compression_closed": discriminant_corridor_closed,
        "discriminant_corridor_identity_closed": discriminant_corridor_closed,
        "interior_high_fiber_forces_dense_square_return_corridor": discriminant_corridor_closed,
        "interior_discriminant_corridor_high_spectrum_proved": high_spectrum_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_character_sum_target": CHAR_SUM_TARGET,
        "parallel_incidence_target": INCIDENCE_TARGET,
        "compression": compression,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "内部 shifted product fiber 可继续降维。对固定内部相位 `c`，令 `t=a+b`，"
            "则 `ab=c(a+b)` 等价于 `a,b` 是 `X^2-tX+c*t=0 mod P` 的两根。"
            "因此高纤维会强制一维通道 `Delta_c(t)=t(t-4c)` 在 `J+J` 中密集返回平方，"
            "并且两根还必须同时落回 `J`。下一最窄点就是排斥这种局部判别式平方返回走廊。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    compression = result["compression"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 内部纤维判别式通道证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"sum_variable_quadratic_compression_closed={fmt_bool(result['sum_variable_quadratic_compression_closed'])}",
        f"interior_discriminant_corridor_high_spectrum_proved={fmt_bool(result['interior_discriminant_corridor_high_spectrum_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 二维纤维到一维通道",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in compression.items():
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
