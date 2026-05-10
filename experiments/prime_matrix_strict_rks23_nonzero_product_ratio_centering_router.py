#!/usr/bin/env python3
"""把非零乘积比值谱做 F_P^* 中心化并固定剩余硬点。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_nonzero_product_ratio_centering_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-nonzero-product-ratio-centering-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-nonzero-product-ratio-centering-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-nonzero-product-ratio-centering-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-zero-product-peeling-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "DiagonalMainSubtractedNonzeroProductRatioSpectrumJointPowerSaving"
NEXT_ATOM = "CenteredNonzeroProductRatioSpectrumAgainstIntervalRatioSpectrumJointPowerSaving"
ALT_ATOM = "NonzeroFourBoxProductRatioCenteredL2OrJointNonconcentration"


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
    """构造非零乘积比值谱中心化证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    zero_peeled = previous.get("zero_product_diagonal_main_ledger_closed") is True
    product_ratio_ready = previous.get("nonzero_product_ratio_normal_form_closed") is True

    # 设 mu_*(z) 是非零平方差/乘积值的纤维质量。
    # 因为 z 只在 F_P^* 上取值，均匀基线应为 M_*^2/(P-1)，
    # 不能继续沿用包含零值的 |Delta|^4/P 基线。
    nonzero_mass_ledger_closed = active and zero_peeled and product_ratio_ready
    fstar_uniform_centering_closed = nonzero_mass_ledger_closed
    centered_correlation_identity_closed = nonzero_mass_ledger_closed

    # 这一层只闭合主项口径，不证明中心化相关有固定幂节省。
    centered_joint_saving_proved = False

    centering = {
        "nonzero_measure": "mu_*(z)=#{(a,b): a*b=z, z!=0, with root-box/parity restrictions}",
        "nonzero_mass": "M_* = sum_{z!=0} mu_*(z)=|Delta|^2-W0",
        "product_ratio_spectrum": "C_*(rho)=sum_{z!=0} mu_*(z)*mu_*(rho*z), rho in F_P^*",
        "first_moment": "sum_{rho in F_P^*} C_*(rho)=M_*^2",
        "fstar_uniform_baseline": "C_unif=M_*^2/(P-1)",
        "centered_product_ratio_spectrum": "C_*^circ(rho)=C_*(rho)-M_*^2/(P-1)",
        "interval_ratio_spectrum": "L(lambda)=#{(x,u) in T^2: u=lambda*x}",
        "diagonal_main_subtracted_correlation": "sum_lambda C_*^circ(-lambda)*L(lambda)",
        "why_p_minus_1": "after zero-product peeling the support is F_P^*, so the correct uniform denominator is P-1",
        "scale_audit": "plain first moment and L2(L) do not imply fixed power saving for the centered correlation",
    }

    expanded_core = {
        "four_box_ratio_equation": "a1*b1 = rho*a2*b2 mod P with all products nonzero",
        "six_variable_joint_equation": "u*a1*b1+x*a2*b2=0 mod P after setting rho=-u/x",
        "centered_failure_packet": "if the target fails, a dyadic set of interval ratios carries large C_*^circ mass",
        "sufficient_but_unproved_l2_route": "sum_{rho} |C_*^circ(rho)|^2 with fixed power saving would close by Cauchy and the existing L2(L) ledger",
        "direct_route": "prove joint nonconcentration of C_*^circ and L without requiring a global C_*^circ L2 theorem",
        "remaining_obstruction": "high product-ratio fibers may align with short interval ratios; this alignment is not ruled out by current ledgers",
    }

    rows = [
        row(
            "DiagonalMainSubtractedTargetActive",
            active,
            True,
            "上一证书已把零乘积同步对角层剥离，当前只剩非零乘积比值相关。",
            TARGET,
        ),
        row(
            "NonzeroMassLedgerClosed",
            nonzero_mass_ledger_closed,
            True,
            "非零质量为 `M_*=|Delta|^2-W0`，零层不会再混入非零谱。",
            "ledger",
        ),
        row(
            "FStarUniformBaselineClosed",
            fstar_uniform_centering_closed,
            True,
            "非零谱定义在 `F_P^*`，均匀主项必须是 `M_*^2/(P-1)`。",
            "ledger",
        ),
        row(
            "CenteredNonzeroProductRatioCorrelationIdentityClosed",
            centered_correlation_identity_closed,
            True,
            "扣除对角主项和 `F_P^*` 均匀项后，剩余精确为 `sum C_*^circ(-lambda)L(lambda)`。",
            NEXT_ATOM,
        ),
        row(
            "ExistingMarginalsDoNotCloseCenteredJointSaving",
            True,
            True,
            "现有一阶账本与 `L` 的低二阶账本仍只到自然尺度，不能自动给固定幂节省。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            centered_joint_saving_proved,
            centered_joint_saving_proved,
            "仓库内尚未证明中心化非零乘积比值谱不能同位集中到短区间比值谱上。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是非零谱中心化和主项口径，不是最终联合节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_nonzero_product_ratio_centering_router",
        "status": "nonzero_product_ratio_spectrum_centered_on_fstar_joint_saving_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "diagonal_main_subtracted_target_active": active,
        "nonzero_mass_ledger_closed": nonzero_mass_ledger_closed,
        "fstar_uniform_baseline_closed": fstar_uniform_centering_closed,
        "centered_nonzero_product_ratio_correlation_identity_closed": centered_correlation_identity_closed,
        "centered_nonzero_product_ratio_joint_power_saving_proved": centered_joint_saving_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "centering": centering,
        "expanded_core": expanded_core,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "扣除零乘积同步对角层以后，非零乘积谱必须在 `F_P^*` 上重新中心化。"
            "令 `M_*=|Delta|^2-W0`，则正确均匀基线是 `M_*^2/(P-1)`，"
            "剩余相关精确写成 `sum_lambda C_*^circ(-lambda)L(lambda)`。"
            "这一步闭合了主项口径和非零核心的中心化接口；真正剩余变成证明该中心化乘积比值谱"
            "不会与短区间比值谱同位集中。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 非零乘积比值谱中心化证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"nonzero_mass_ledger_closed={fmt_bool(result['nonzero_mass_ledger_closed'])}",
        f"fstar_uniform_baseline_closed={fmt_bool(result['fstar_uniform_baseline_closed'])}",
        f"centered_nonzero_product_ratio_correlation_identity_closed={fmt_bool(result['centered_nonzero_product_ratio_correlation_identity_closed'])}",
        f"centered_nonzero_product_ratio_joint_power_saving_proved={fmt_bool(result['centered_nonzero_product_ratio_joint_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. F_P^* 中心化账本",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["centering"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 展开后的真正核心",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["expanded_core"].items():
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
