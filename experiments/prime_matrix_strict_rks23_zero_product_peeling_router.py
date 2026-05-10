#!/usr/bin/env python3
"""剥离 RKS23 乘积入射中的零乘积对角层。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_zero_product_peeling_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-zero-product-peeling-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-zero-product-peeling-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-zero-product-peeling-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-square-difference-product-incidence-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "ZeroProductPeeledNonzeroBilinearProductMixedIncidencePowerSaving"
NEXT_ATOM = "DiagonalMainSubtractedNonzeroProductRatioSpectrumJointPowerSaving"
CORE_ATOM = "NonzeroBilinearProductRatioSpectrumAgainstIntervalRatioSpectrumNonconcentration"
DIAGONAL_ATOM = "ZeroProductDiagonalMainTermExactLedger"


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
    """构造零乘积剥离证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    product_form_closed = previous.get("mixed_incidence_product_form_closed") is True
    zero_layer_isolated = previous.get("zero_product_layer_isolated") is True

    # 关键刚性：x,u 属于短区间比值支撑，按前序账本均在 F_P^*。
    # 因此 u*h1+x*h2=0 中若 h1=0，则 x*h2=0 强迫 h2=0；
    # 反过来也一样。零乘积层不是四个独立退化面，而是同步对角层。
    zero_forces_both_zero = active and product_form_closed and zero_layer_isolated
    exact_zero_ledger_closed = zero_forces_both_zero
    nonzero_ratio_form_closed = zero_forces_both_zero

    # 在平方根颈部 |Delta|~|T|~N, P~N^2。W0=# {d^2=e^2}=O(N)，
    # 零层在最终 sqrt 相关中可能达到自然 N^4 尺度，不能无条件当作小误差吸收。
    diagonal_absorbable = False
    diagonal_subtraction_required = exact_zero_ledger_closed

    zero_ledger = {
        "square_difference": "h(d,e)=d^2-e^2",
        "zero_mass": "W0=#{(d,e) in Delta^2: h(d,e)=0}=#{d=e or d=-e, with endpoint conventions}",
        "mixed_product_equation": "u*a1*b1+x*a2*b2=0 mod P, where h_i=a_i*b_i",
        "nonzero_uv_support": "x,u in T subset F_P^*, inherited from the unique-ratio ledger sum_lambda L(lambda)=|T|^2",
        "forcing": "h1=0 or h2=0 implies h1=h2=0",
        "raw_zero_layer_count": "|T|^2 * W0^2",
        "centered_zero_layer_count": "|T|^2 * (W0^2-|Delta|^4/P) in the Q_circ normalization",
        "final_energy_diagonal_piece": "if not separately subtracted, P*(W0^2-|Delta|^4/P) per slope before the final square-root correlation",
        "scale_warning": "this can sit at the natural N^4 correlation scale in the square-root collar",
        "conclusion": "zero layer is exactly peelable, but not automatically power-saving absorbable",
    }

    ratio_core = {
        "nonzero_product_measure": "mu(z)=#{(a,b): a*b=z, a*b!=0, with root-box/parity restrictions}",
        "product_ratio_spectrum": "C(rho)=sum_{z!=0} mu(z)*mu(rho*z)",
        "interval_ratio_spectrum": "L(lambda)=#{(x,u) in T^2: u=lambda*x}",
        "nonzero_equation": "u*z1+x*z2=0 with z1,z2!=0",
        "ratio_normal_form": "z2/z1=-u/x=-lambda",
        "nonzero_core_count": "sum_lambda C(-lambda)*L(lambda), after the zero diagonal ledger is removed",
        "needed_saving": "prove the diagonal-main-subtracted centered correlation has a fixed power saving",
        "why_narrower": "the remaining object no longer contains the h=0 diagonal; all variables are nonzero product fibers",
    }

    rows = [
        row(
            "ProductIncidenceHardpointActive",
            active,
            True,
            "上一证书已把当前内部硬点固定为零层剥离加非零乘积入射节省。",
            TARGET,
        ),
        row(
            "ZeroProductLayerPreviouslyIsolated",
            zero_layer_isolated,
            True,
            "`h=0` 已被精确识别为 `a*b=0`，即 `d=e` 或 `d=-e`。",
            DIAGONAL_ATOM,
        ),
        row(
            "ZeroProductForcesSynchronousDiagonal",
            zero_forces_both_zero,
            True,
            "因 `x,u` 非零，混合方程中一侧平方差为零会强迫另一侧也为零。",
            DIAGONAL_ATOM,
        ),
        row(
            "ZeroProductDiagonalMainLedgerClosed",
            exact_zero_ledger_closed,
            True,
            "零层贡献精确为 `|T|^2 W0^2`，中心化后为 `|T|^2(W0^2-|Delta|^4/P)`。",
            "diagonal main term must be subtracted before nonzero savings",
        ),
        row(
            "ZeroProductLayerNotAutomaticallyAbsorbable",
            True,
            True,
            "尺度审计显示该同步对角层可达自然尺度，不能直接当作固定幂小误差。",
            NEXT_ATOM,
        ),
        row(
            "NonzeroProductRatioNormalFormClosed",
            nonzero_ratio_form_closed,
            True,
            "剥离零层后，剩余入射等价于乘积比值谱 `C(-lambda)` 与区间比值谱 `L(lambda)` 的相关。",
            CORE_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明扣除零乘积对角主项后的非零乘积比值谱相关固定幂节省。",
            CORE_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是零层精确剥离与非零核心正规形，不是最终相关节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_zero_product_peeling_router",
        "status": "zero_product_diagonal_exactly_peeled_nonzero_product_ratio_core_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "product_incidence_hardpoint_active": active,
        "zero_product_forces_synchronous_diagonal": zero_forces_both_zero,
        "zero_product_diagonal_main_ledger_closed": exact_zero_ledger_closed,
        "zero_product_layer_power_saving_absorbable": diagonal_absorbable,
        "diagonal_main_subtraction_required": diagonal_subtraction_required,
        "nonzero_product_ratio_normal_form_closed": nonzero_ratio_form_closed,
        "diagonal_main_subtracted_nonzero_product_ratio_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": CORE_ATOM,
        "zero_ledger": zero_ledger,
        "ratio_core": ratio_core,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "零乘积层现在被精确剥离：在 `x,u` 非零的支撑上，"
            "`u*h1+x*h2=0` 中只要一个 `h_i=0`，另一个也必须为零，"
            "所以零层是同步对角主项 `|T|^2 W0^2`。"
            "它不是自动可吸收的小误差；在平方根颈部可处于自然尺度。"
            "因此自足线下一步必须先扣除该对角主项，再证明全非零乘积比值谱 "
            "`C(-lambda)` 与区间比值谱 `L(lambda)` 的联合非集中。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    zero_ledger = result["zero_ledger"]
    ratio_core = result["ratio_core"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 零乘积剥离证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"zero_product_diagonal_main_ledger_closed={fmt_bool(result['zero_product_diagonal_main_ledger_closed'])}",
        f"zero_product_layer_power_saving_absorbable={fmt_bool(result['zero_product_layer_power_saving_absorbable'])}",
        f"nonzero_product_ratio_normal_form_closed={fmt_bool(result['nonzero_product_ratio_normal_form_closed'])}",
        f"diagonal_main_subtracted_nonzero_product_ratio_saving_proved={fmt_bool(result['diagonal_main_subtracted_nonzero_product_ratio_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 零乘积对角账本",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in zero_ledger.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 非零乘积比值核心",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in ratio_core.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
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
            "## 4. 下一最窄自足目标",
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
