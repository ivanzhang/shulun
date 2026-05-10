#!/usr/bin/env python3
"""把中心化非零乘积比值相关压成 C_*^circ 的 L2 能量输入。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_centered_product_ratio_l2_reduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-centered-product-ratio-l2-reduction-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-centered-product-ratio-l2-reduction-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-centered-product-ratio-l2-reduction-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-nonzero-product-ratio-centering-router.json"
SLOPE_LEDGER = MONO / "prime-matrix-strict-rks23-slope-overlap-ratio-spectrum-router.json"
SOURCE_FILES = [PREVIOUS, SLOPE_LEDGER]

TARGET = "CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving"
NEXT_ATOM = "CenteredNonzeroProductRatioL2PowerSavingAtCauchyRequiredScale"
ALT_ATOM = "EightVariableNonzeroProductRatioEnergyDispersionPowerSaving"


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
    """构造 L2 归约证书。"""
    previous = load_json(PREVIOUS)
    slope = load_json(SLOPE_LEDGER)

    active = previous.get("next_direct_attack_target") == TARGET
    centered_identity = previous.get("centered_nonzero_product_ratio_correlation_identity_closed") is True
    slope_l2_ready = slope.get("slope_overlap_l2_divisor_ledger_closed") is True

    cauchy_reduction_closed = active and centered_identity and slope_l2_ready
    l2_energy_identity_closed = cauchy_reduction_closed
    eight_variable_expansion_closed = cauchy_reduction_closed

    # 这一层只给出充分输入和等价展开，不证明该 L2 幂节省。
    product_ratio_l2_saving_proved = False

    cauchy_gate = {
        "current_correlation": "S=sum_{lambda in F_P^*} C_*^circ(-lambda)*L(lambda)",
        "known_l2_l": "sum_lambda L(lambda)^2 <= |T|^2 P^o(1)",
        "cauchy_bound": "|S| <= (sum_rho |C_*^circ(rho)|^2)^(1/2) * (sum_lambda L(lambda)^2)^(1/2)",
        "sufficient_input": "prove sum_rho |C_*^circ(rho)|^2 is below the Cauchy-required scale by a fixed power",
        "why_no_theorem_switch": "this is the same centered nonzero product-ratio correlation, with the already proved L2(L) ledger inserted",
        "limitation": "Cauchy is sufficient but may be stronger than direct joint nonconcentration",
    }

    l2_expansion = {
        "nonzero_measure": "mu_*(z)=#{(a,b): a*b=z, z!=0}",
        "ratio_spectrum": "C_*(rho)=sum_{z!=0} mu_*(z)*mu_*(rho*z)",
        "centered_spectrum": "C_*^circ(rho)=C_*(rho)-M_*^2/(P-1)",
        "centered_l2_identity": "sum_rho |C_*^circ(rho)|^2=sum_rho C_*(rho)^2-M_*^4/(P-1)",
        "raw_l2_count": "sum_rho C_*(rho)^2",
        "eight_variable_count": "#{z1/z2=z3/z4: zi=a_i*b_i!=0, all variables in the root product boxes}",
        "multiplicative_equation": "(a1*b1)*(a4*b4)=(a2*b2)*(a3*b3) mod P",
        "uniform_term": "M_*^4/(P-1)",
        "needed_dispersion": "the eight-variable product-ratio energy must equal the uniform term plus a fixed-power-saving error",
    }

    rows = [
        row(
            "CenteredJointTargetActive",
            active,
            True,
            "上一证书已把剩余固定为 `sum C_*^circ(-lambda)L(lambda)` 的中心化相关。",
            TARGET,
        ),
        row(
            "IntervalRatioL2LedgerImported",
            slope_l2_ready,
            True,
            "短区间比值谱已有 `sum L(lambda)^2<=|T|^2 P^o(1)` 账本。",
            "ledger",
        ),
        row(
            "CauchyReductionToProductRatioL2Closed",
            cauchy_reduction_closed,
            True,
            "由 Cauchy，证明 `C_*^circ` 的足够强 L2 节省即可推出当前相关节省。",
            NEXT_ATOM,
        ),
        row(
            "CenteredProductRatioL2IdentityClosed",
            l2_energy_identity_closed,
            True,
            "`sum |C_*^circ|^2=sum C_*^2-M_*^4/(P-1)`，均匀项口径已固定。",
            ALT_ATOM,
        ),
        row(
            "EightVariableProductRatioEnergyExpansionClosed",
            eight_variable_expansion_closed,
            True,
            "`sum C_*^2` 精确等于八变量非零乘积比值能量。",
            ALT_ATOM,
        ),
        row(
            NEXT_ATOM,
            product_ratio_l2_saving_proved,
            product_ratio_l2_saving_proved,
            "仓库内尚未证明该八变量乘积比值能量相对均匀项有固定幂节省。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是 L2 归约和八变量展开，不是八变量能量节省本身。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_centered_product_ratio_l2_reduction_router",
        "status": "centered_product_ratio_joint_correlation_reduced_to_product_ratio_l2_energy",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "centered_joint_target_active": active,
        "interval_ratio_l2_ledger_imported": slope_l2_ready,
        "cauchy_reduction_to_product_ratio_l2_closed": cauchy_reduction_closed,
        "centered_product_ratio_l2_identity_closed": l2_energy_identity_closed,
        "eight_variable_product_ratio_energy_expansion_closed": eight_variable_expansion_closed,
        "centered_nonzero_product_ratio_l2_power_saving_proved": product_ratio_l2_saving_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "cauchy_gate": cauchy_gate,
        "l2_expansion": l2_expansion,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前中心化相关没有换题：把已闭合的 `L(lambda)` 低二阶账本代入 Cauchy，"
            "可把剩余压成 `C_*^circ` 的二阶能量节省。"
            "该二阶能量又精确展开为八变量非零乘积比值能量 "
            "`(a1*b1)(a4*b4)=(a2*b2)(a3*b3)` 相对均匀项 `M_*^4/(P-1)` 的偏差。"
            "因此下一真正自足硬点是证明这个八变量乘积比值能量具有 Cauchy 所需的固定幂节省。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 中心化乘积比值 L2 归约证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"interval_ratio_l2_ledger_imported={fmt_bool(result['interval_ratio_l2_ledger_imported'])}",
        f"cauchy_reduction_to_product_ratio_l2_closed={fmt_bool(result['cauchy_reduction_to_product_ratio_l2_closed'])}",
        f"centered_product_ratio_l2_identity_closed={fmt_bool(result['centered_product_ratio_l2_identity_closed'])}",
        f"eight_variable_product_ratio_energy_expansion_closed={fmt_bool(result['eight_variable_product_ratio_energy_expansion_closed'])}",
        f"centered_nonzero_product_ratio_l2_power_saving_proved={fmt_bool(result['centered_nonzero_product_ratio_l2_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Cauchy/L2 门",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["cauchy_gate"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 八变量能量展开",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["l2_expansion"].items():
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
