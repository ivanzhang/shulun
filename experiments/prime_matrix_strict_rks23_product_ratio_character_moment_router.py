#!/usr/bin/env python3
"""把 dyadic 矩形乘积比值卷积 L2 压成乘法角色矩。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_product_ratio_character_moment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-product-ratio-character-moment-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-product-ratio-character-moment-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-product-ratio-character-moment-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "DyadicRectangularProductRatioConvolutionL2PowerSavingAtCauchyScale"
NEXT_ATOM = "FourShortIntervalNonprincipalMultiplicativeCharacterProductMomentPowerSaving"
ALT_ATOM = "SelfContainedBurgessOrBourgainGaraevCharacterMomentForRKS23Rectangles"


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
    """构造乘法角色矩归约证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    convolution_ready = previous.get("rectangular_product_ratio_convolution_identity_closed") is True
    rectangular_ready = previous.get("dyadic_rectangularization_closed_up_to_polylog") is True

    # 在 G=F_P^* 上对交叉比值谱做乘法 Fourier。
    # principal character 给出 |R0|*|R1|/(P-1) 的均匀主项；
    # 中心化后只剩非主角色求和。
    fstar_fourier_closed = active and convolution_ready and rectangular_ready
    principal_removed_closed = fstar_fourier_closed
    character_factorization_closed = fstar_fourier_closed
    l2_plancherel_closed = fstar_fourier_closed

    # 本步只完成等式归约，不内部证明 Burgess/BG 型非主角色矩节省。
    character_moment_saving_proved = False

    fourier = {
        "group": "G=F_P^* with |G|=P-1",
        "packet_pair": "R0=A0 x B0 and R1=A1 x B1",
        "cross_product_ratio": "C_R0,R1(rho)=#{(r0,r1): a1*b1=rho*a0*b0}",
        "centered_ratio": "C^circ(rho)=C_R0,R1(rho)-(|R0|*|R1|)/(P-1)",
        "multiplicative_fourier": "hat f(chi)=sum_{rho in G} f(rho) chi(rho)",
        "principal_character": "chi0 gives hat C(chi0)=|R0|*|R1| and is exactly removed by centering",
        "plancherel": "sum_rho |C^circ(rho)|^2=(1/(P-1))*sum_{chi!=chi0}|hat C(chi)|^2",
    }

    factorization = {
        "interval_character_sum": "S_I(chi)=sum_{n in I} chi(n)",
        "a_cross_ratio_transform": "hat R_A0,A1(chi)=S_A1(chi)*conj(S_A0(chi))",
        "b_cross_ratio_transform": "hat R_B0,B1(chi)=S_B1(chi)*conj(S_B0(chi))",
        "product_transform": "hat C(chi)=S_A1(chi)conj(S_A0(chi))S_B1(chi)conj(S_B0(chi))",
        "l2_character_moment": (
            "sum_rho |C^circ(rho)|^2=(1/(P-1))*sum_{chi!=chi0} "
            "|S_A0(chi)S_A1(chi)S_B0(chi)S_B1(chi)|^2"
        ),
        "required_saving": "prove this nonprincipal four-short-interval character product moment is below the Cauchy scale by a fixed power",
        "external_sufficient_route": "classical Burgess/BG-style character-sum input would be sufficient if accepted with the needed uniform packet constants",
        "internal_gap": "the current corpus has not internalized that character-moment proof for all dyadic rectangle packets",
    }

    rows = [
        row(
            "DyadicRectangularConvolutionHardpointActive",
            active,
            True,
            "上一证书已把当前剩余固定为 dyadic 矩形包对的中心化乘法卷积 L2 节省。",
            TARGET,
        ),
        row(
            "MultiplicativeFourierOnFStarClosed",
            fstar_fourier_closed,
            True,
            "在 `F_P^*` 上对乘积比值谱做乘法 Fourier 是精确等式。",
            NEXT_ATOM,
        ),
        row(
            "PrincipalCharacterUniformTermRemoved",
            principal_removed_closed,
            True,
            "principal character 正好给出 `(|R0||R1|)/(P-1)` 均匀主项，已由中心化扣除。",
            NEXT_ATOM,
        ),
        row(
            "CrossRatioFourierFactorizationClosed",
            character_factorization_closed,
            True,
            "乘积交叉比值谱的 Fourier 变换总计因子化为四个短区间角色和的乘积。",
            NEXT_ATOM,
        ),
        row(
            "CenteredL2EqualsNonprincipalFourIntervalMoment",
            l2_plancherel_closed,
            True,
            "中心化卷积 L2 精确等于非主角色上四个短区间角色和乘积的二阶矩。",
            NEXT_ATOM,
        ),
        row(
            "ExternalBurgessBGWouldBeSufficientButNotInternalized",
            True,
            False,
            "Burgess/BG 型角色和输入若带所需统一常数可作为充分外部闭合；本证书未把它内部化。",
            ALT_ATOM,
        ),
        row(
            NEXT_ATOM,
            character_moment_saving_proved,
            character_moment_saving_proved,
            "仓库内尚未给出该非主角色四短区间乘积矩的严格内部固定幂节省证明。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是乘法 Fourier/角色矩等式，不是角色矩节省本身。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_product_ratio_character_moment_router",
        "status": "dyadic_rectangular_convolution_l2_reduced_to_nonprincipal_character_product_moment",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dyadic_rectangular_convolution_hardpoint_active": active,
        "multiplicative_fourier_on_fstar_closed": fstar_fourier_closed,
        "principal_character_uniform_term_removed": principal_removed_closed,
        "cross_ratio_fourier_factorization_closed": character_factorization_closed,
        "centered_l2_equals_nonprincipal_four_interval_moment": l2_plancherel_closed,
        "four_short_interval_character_product_moment_saving_proved": character_moment_saving_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "fourier": fourier,
        "factorization": factorization,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "dyadic 矩形卷积 L2 已被精确对角化到乘法角色侧。"
            "principal character 恰好产生 `(|R0||R1|)/(P-1)` 的均匀主项，中心化后完全消失。"
            "每个非主角色的 Fourier 系数因子化为四个短区间角色和 "
            "`S_A0,S_A1,S_B0,S_B1` 的乘积。"
            "因此下一真正自足硬点不是抽象卷积，而是证明非主角色四短区间乘积矩具有 Cauchy 所需的固定幂节省。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 乘积比值角色矩证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"multiplicative_fourier_on_fstar_closed={fmt_bool(result['multiplicative_fourier_on_fstar_closed'])}",
        f"principal_character_uniform_term_removed={fmt_bool(result['principal_character_uniform_term_removed'])}",
        f"cross_ratio_fourier_factorization_closed={fmt_bool(result['cross_ratio_fourier_factorization_closed'])}",
        f"centered_l2_equals_nonprincipal_four_interval_moment={fmt_bool(result['centered_l2_equals_nonprincipal_four_interval_moment'])}",
        f"four_short_interval_character_product_moment_saving_proved={fmt_bool(result['four_short_interval_character_product_moment_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. F_P^* 乘法 Fourier",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["fourier"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 非主角色矩因子化",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["factorization"].items():
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
