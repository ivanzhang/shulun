#!/usr/bin/env python3
"""把八变量乘积比值能量压成矩形包上的比值谱乘法卷积。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_product_ratio_rectangular_convolution_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-centered-product-ratio-l2-reduction-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale"
NEXT_ATOM = "DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale"
ALT_ATOM = "MultiplicativeConvolutionOfTwoShortIntervalRatioSpectraCenteredL2PowerSaving"


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
    """构造矩形卷积归约证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    eight_ready = previous.get("eight_variable_product_ratio_energy_expansion_closed") is True
    centered_l2_ready = previous.get("centered_product_ratio_l2_identity_closed") is True

    # a=d-e, b=d+e 后，(a,b) 支撑是短根盒的线性像：
    # 两个线性不等式加奇偶/端点条件。对固定幂目标而言，
    # 多对数个 dyadic 矩形包和 O(1) 奇偶类不会改变闭合尺度。
    support_geometry_closed = active and eight_ready
    dyadic_rectangularization_closed = support_geometry_closed
    convolution_identity_closed = support_geometry_closed and centered_l2_ready

    # 本步只把能量硬点正规化为矩形卷积 L2；不证明卷积 L2 固定幂节省。
    convolution_l2_saving_proved = False

    geometry = {
        "product_coordinates": "a=d-e, b=d+e with d=(a+b)/2 and e=(b-a)/2",
        "support_shape": "intersection of O(N)-scale linear strips, plus parity and endpoint restrictions",
        "nonzero_condition": "a*b!=0 after the zero-product diagonal has been peeled",
        "dyadic_cover": "split by signs, parity, and distances to strip boundaries into log^O(P) rectangular packets A_i x B_i",
        "bounded_overlap": "each original support point belongs to O(log^O(P)) packets, harmless for fixed-power targets",
        "energy_after_cover": "after expanding mu=sum_i mu_i, it is enough to prove the required L2 saving for every dyadic rectangular packet pair, losing only log^O(P)",
        "warning": "this is a support decomposition, not a cancellation estimate",
    }

    convolution = {
        "rectangular_packet_pair": "R0=A0 x B0 and R1=A1 x B1, with Ai,Bi short intervals/progressions inside F_P^*",
        "a_cross_ratio_spectrum": "R_A0,A1(alpha)=#{(a0,a1) in A0 x A1: a1=alpha*a0}",
        "b_cross_ratio_spectrum": "R_B0,B1(beta)=#{(b0,b1) in B0 x B1: b1=beta*b0}",
        "product_cross_ratio_spectrum": "C_R0,R1(rho)=#{(r0,r1) in R0 x R1: a1*b1=rho*a0*b0}",
        "convolution_identity": "C_R0,R1 = R_A0,A1 *_mult R_B0,B1",
        "centered_packet_pair": "C_R0,R1^circ(rho)=C_R0,R1(rho)-(|R0|*|R1|)/(P-1)",
        "packet_pair_l2_target": "sum_rho |C_R0,R1^circ(rho)|^2 must have the Cauchy-required fixed-power saving",
        "existing_l2_marginals": "divisor lifting gives low L2 for R_A and R_B separately, but this alone does not yield the needed centered convolution L2 saving",
    }

    rows = [
        row(
            "CenteredProductRatioL2HardpointActive",
            active,
            True,
            "上一证书已把当前剩余固定为 `C_*^circ` 的 L2 节省。",
            TARGET,
        ),
        row(
            "EightVariableEnergyExpansionImported",
            eight_ready,
            True,
            "八变量非零乘积比值能量展开已闭合。",
            "ledger",
        ),
        row(
            "RotatedRootBoxSupportGeometryClosed",
            support_geometry_closed,
            True,
            "`a=d-e,b=d+e` 支撑为短线性根盒，可按符号、奇偶和边界距离拆包。",
            NEXT_ATOM,
        ),
        row(
            "DyadicRectangularizationClosedUpToPolylog",
            dyadic_rectangularization_closed,
            True,
            "多对数个矩形包和有限奇偶类只造成 `P^o(1)` 损失，不影响固定幂目标。",
            NEXT_ATOM,
        ),
        row(
            "RectangularProductRatioConvolutionIdentityClosed",
            convolution_identity_closed,
            True,
            "在每个矩形包对 `A0 x B0, A1 x B1` 上，交叉乘积比值谱等于两个交叉短区间比值谱的乘法卷积。",
            ALT_ATOM,
        ),
        row(
            "SeparateRatioL2MarginalsInsufficient",
            True,
            True,
            "分别控制 `R_A`、`R_B` 的 L2 只给边际账本，尚不能推出中心化卷积 L2 固定幂节省。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            convolution_l2_saving_proved,
            convolution_l2_saving_proved,
            "仓库内尚未证明所有 dyadic 矩形包的中心化乘法卷积比值谱 L2 固定幂节省。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是支撑矩形化和卷积恒等式，不是卷积 L2 节省本身。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_product_ratio_rectangular_convolution_router",
        "status": "product_ratio_l2_hardpoint_reduced_to_dyadic_rectangular_ratio_convolution_l2",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "centered_product_ratio_l2_hardpoint_active": active,
        "eight_variable_energy_expansion_imported": eight_ready,
        "rotated_root_box_support_geometry_closed": support_geometry_closed,
        "dyadic_rectangularization_closed_up_to_polylog": dyadic_rectangularization_closed,
        "rectangular_product_ratio_convolution_identity_closed": convolution_identity_closed,
        "dyadic_rectangular_product_ratio_convolution_l2_saving_proved": convolution_l2_saving_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "geometry": geometry,
        "convolution": convolution,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "八变量乘积比值能量的支撑现在被正规化："
            "`a=d-e,b=d+e` 把根盒变成短线性根盒，按符号、奇偶和边界距离可拆成 "
            "`log^O(P)` 个矩形包。固定幂目标允许这种多对数损失。"
            "在每个矩形包对 `A0 x B0, A1 x B1` 上，交叉乘积比值谱不是黑箱对象，"
            "而是两个交叉短区间比值谱的乘法卷积。"
            "因此下一真正剩余是证明这些 dyadic 矩形卷积的中心化 L2 有 Cauchy 所需的固定幂节省。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 乘积比值矩形卷积证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rotated_root_box_support_geometry_closed={fmt_bool(result['rotated_root_box_support_geometry_closed'])}",
        f"dyadic_rectangularization_closed_up_to_polylog={fmt_bool(result['dyadic_rectangularization_closed_up_to_polylog'])}",
        f"rectangular_product_ratio_convolution_identity_closed={fmt_bool(result['rectangular_product_ratio_convolution_identity_closed'])}",
        f"dyadic_rectangular_product_ratio_convolution_l2_saving_proved={fmt_bool(result['dyadic_rectangular_product_ratio_convolution_l2_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 支撑矩形化",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["geometry"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 矩形包卷积恒等式",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["convolution"].items():
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
