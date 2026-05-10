#!/usr/bin/env python3
"""把混合平方差入射改写为乘积因子入射，并隔离零乘积层。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_square_difference_product_incidence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-square-difference-product-incidence-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-square-difference-product-incidence-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-square-difference-product-incidence-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-joint-mixed-incidence-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "DyadicCenteredMixedSquareDifferenceRatioIncidencePowerSaving"
NEXT_ATOM = "ZeroProductPeeledNonzeroBilinearProductMixedIncidencePowerSaving"
PRODUCT_ATOM = "CenteredBilinearProductRatioIncidenceAfterSquareDifferenceFactorization"


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
    """构造乘积因子入射证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    mixed_closed = previous.get("mixed_incidence_identity_closed") is True

    # 在奇素数模 P 下，2 可逆。平方差可写成
    # d^2-e^2=(d-e)(d+e)。这把混合方程
    # u h1 + x h2=0 改写为
    # u a1 b1 + x a2 b2=0，并把 h=0 等价为 a=0 或 b=0。
    product_form_closed = active and mixed_closed
    zero_layer_isolated = active and mixed_closed

    product_form = {
        "change_of_variables": "a=d-e, b=d+e; since 2 is invertible, d=(a+b)/2 and e=(b-a)/2",
        "square_difference_factorization": "d^2-e^2=a*b",
        "box_constraints": "a,b lie in short O(N) boxes with parity/root-box endpoint restrictions",
        "mixed_equation_before": "u*(d1^2-e1^2)+x*(d2^2-e2^2)=0 mod P",
        "mixed_equation_after": "u*a1*b1+x*a2*b2=0 mod P",
        "zero_product_layer": "h=0 iff a*b=0, i.e. d=e or d=-e",
        "why_zero_layer_matters": "this is a structured diagonal layer; it must be peeled/accounted before claiming random-like mixed incidence",
        "nonzero_core": "a1*b1 and a2*b2 both nonzero; the remaining equation is a genuine bilinear-product ratio incidence",
    }

    rows = [
        row(
            "DyadicMixedIncidenceTargetActive",
            active,
            True,
            "上一证书已把最终相关失败压成 dyadic 中心化混合平方差-比值入射。",
            TARGET,
        ),
        row(
            "SquareDifferenceProductCoordinatesClosed",
            product_form_closed,
            True,
            "`d^2-e^2=(d-e)(d+e)` 在奇素数模下给出可逆变量替换。",
            PRODUCT_ATOM,
        ),
        row(
            "MixedIncidenceProductFormClosed",
            product_form_closed,
            True,
            "六变量混合入射化为 `u*a1*b1+x*a2*b2=0` 的乘积型入射。",
            PRODUCT_ATOM,
        ),
        row(
            "ZeroProductLayerIsolated",
            zero_layer_isolated,
            True,
            "`h=0` 精确等价于 `a*b=0`，该对角层已被显式隔离。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未完成零乘积层回扣与非零乘积混合入射的固定幂节省。",
            PRODUCT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成乘积化与零层隔离，未证明最终入射节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_square_difference_product_incidence_router",
        "status": "centered_mixed_incidence_factorized_into_product_form_with_zero_layer_isolated",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dyadic_mixed_incidence_target_active": active,
        "square_difference_product_coordinates_closed": product_form_closed,
        "mixed_incidence_product_form_closed": product_form_closed,
        "zero_product_layer_isolated": zero_layer_isolated,
        "zero_product_peeled_nonzero_product_incidence_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": PRODUCT_ATOM,
        "product_form": product_form,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "混合平方差入射可进一步乘积化。令 `a=d-e,b=d+e`，则 `d^2-e^2=a*b`，"
            "原方程 `u h1+x h2=0` 化为 `u*a1*b1+x*a2*b2=0 mod P`。"
            "同时 `h=0` 精确变成零乘积层 `a*b=0`，即 `d=e` 或 `d=-e`。"
            "因此下一真正剩余是先把零乘积对角层正确回扣，再证明非零乘积核心的中心化混合入射节省。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    product = result["product_form"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 平方差乘积入射证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"square_difference_product_coordinates_closed={fmt_bool(result['square_difference_product_coordinates_closed'])}",
        f"zero_product_layer_isolated={fmt_bool(result['zero_product_layer_isolated'])}",
        f"zero_product_peeled_nonzero_product_incidence_power_saving_proved={fmt_bool(result['zero_product_peeled_nonzero_product_incidence_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 乘积入射正规形",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in product.items():
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
