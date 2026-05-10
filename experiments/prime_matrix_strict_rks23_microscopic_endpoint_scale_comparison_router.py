#!/usr/bin/env python3
"""把微薄端点 strip 的 Cauchy 尺度比较压成侧向乘子地板。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_microscopic_endpoint_scale_comparison_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-microscopic-endpoint-scale-comparison-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-microscopic-endpoint-scale-comparison-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-microscopic-endpoint-scale-comparison-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-endpoint-strip-multiplicity-router.json"
COLLAR = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
WEIGHTED_CORE = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
SOURCE_FILES = [PREVIOUS, COLLAR, WEIGHTED_CORE]

TARGET = "MicroscopicEndpointStripCauchyScaleComparisonForWeightedSideMass"
NEXT_ATOM = "RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets"
LEDGER_ATOM = "MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale"
BURGESS_ATOM = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"


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
    """构造微薄端点尺度比较路由证书。"""
    previous = load_json(PREVIOUS)
    collar = load_json(COLLAR)
    weighted = load_json(WEIGHTED_CORE)

    active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("endpoint_strip_pure_multiplicity_closed") is True
    )
    collar_floor_imported = (
        collar.get("fixed_power_saving_implies_required_log_saving") is True
        and collar.get("collar_log_power") == 236
    )
    weighted_collar_imported = "P^(1/2)/log^236(P)" in weighted.get("core_statement", {}).get("collar", "")

    # 设 T=P^kappa。若 CauchyScale 对短边 s 登记了侧向乘子 A_s，
    # CauchyScale_s >= A_s * TripleSideSquareMass_s，
    # 且 A_s >= P^(1/2)/log^236(P)，则任取 kappa<1/2，
    # T/A_s <= P^(-(1/2-kappa)+o(1))，给固定幂余量。
    side_floor_implication_closed = active and collar_floor_imported and weighted_collar_imported
    power_margin_algebra_closed = side_floor_implication_closed
    side_multiplier_floor_proved = False
    scale_comparison_proved = side_floor_implication_closed and side_multiplier_floor_proved
    microscopic_ledger_proved = scale_comparison_proved
    burgess_still_open = previous.get("burgess_pointwise_input_still_open") is True

    normalization = {
        "post_multiplicity_bound": "micro contribution <= P^o(1)*T*TripleSideSquareMass_s",
        "needed_comparison": "P^o(1)*T*TripleSideSquareMass_s <= CauchyScale_s*P^(-eta)",
        "side_multiplier_definition": "CauchyScale_s >= A_s*TripleSideSquareMass_s",
        "equivalent_floor": "need A_s >= T*P^(eta+o(1))",
        "new_atomic_floor": NEXT_ATOM,
        "why_this_is_exact": "after cancelling the common TripleSideSquareMass_s, only the side multiplier A_s remains",
    }

    collar_margin = {
        "collar_lower_bound": "|J|>=P^(1/2)/log^236(P)",
        "micro_width": "T=P^kappa",
        "parameter_choice": "fix any kappa<1/2 and then take eta<(1/2-kappa)",
        "algebra": "T/(P^(1/2)/log^236 P)=P^{kappa-1/2}log^236(P)=P^{-eta-o(1)}",
        "large_p_absorption": "fixed log powers are absorbed by the positive gap 1/2-kappa",
        "finite_transition": "small P remains in the existing finite/P0 lane once constants are supplied",
    }

    remaining_floor = {
        "name": NEXT_ATOM,
        "statement": (
            "for each microscopic endpoint-compatible side s, the Cauchy-scale ledger contains "
            "a side multiplier A_s with A_s >= P^(1/2)/log^236(P), or an equivalent registered floor"
        ),
        "why_needed": "pure strip multiplicity gives T, but only this floor compares T to the actual Cauchy scale",
        "not_currently_in_corpus": "existing files state root-box collar scale, but do not yet bind that scale to every endpoint-compatible side multiplier A_s",
        "what_would_close": "this floor plus the power-margin algebra closes the microscopic endpoint scale comparison",
    }

    rows = [
        row(
            "MicroscopicEndpointScaleComparisonActive",
            active,
            True,
            "上一证书已把微薄边剩余压成 `T*TripleSideSquareMass_s` 与 CauchyScale 的比较。",
            TARGET,
        ),
        row(
            "SquareRootCollarFloorImported",
            collar_floor_imported and weighted_collar_imported,
            True,
            "RKS23 平衡颈部已有 `|J|>=P^(1/2)/log^236(P)` 的环境尺度下界。",
            "collar ledger",
        ),
        row(
            "SideMultiplierNormalizationClosed",
            active,
            True,
            "把 CauchyScale 写作 `A_s*TripleSideSquareMass_s` 后，尺度比较等价于侧向乘子地板。",
            NEXT_ATOM,
        ),
        row(
            "KappaBelowHalfPowerMarginAlgebraClosed",
            power_margin_algebra_closed,
            True,
            "若 `A_s>=P^(1/2)/log^236(P)` 且 `T=P^kappa,kappa<1/2`，则 `T/A_s` 有固定幂节省。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            side_multiplier_floor_proved,
            side_multiplier_floor_proved,
            "仓库内尚未把平方根颈部环境尺度注册为每个微薄端点兼容侧的 Cauchy 乘子 `A_s`。",
            NEXT_ATOM,
        ),
        row(
            TARGET,
            scale_comparison_proved,
            scale_comparison_proved,
            "尺度比较需要侧向乘子地板；当前只闭合了归一化和幂余量代数。",
            NEXT_ATOM,
        ),
        row(
            LEDGER_ATOM,
            microscopic_ledger_proved,
            microscopic_ledger_proved,
            "微薄边总质量吸收仍等待侧向乘子地板。",
            NEXT_ATOM,
        ),
        row(
            "BurgessPointwiseInputStillOpen",
            burgess_still_open,
            False,
            "大包分支 Burgess 点态输入仍为并行开放项。",
            BURGESS_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只关闭尺度比较的代数归一化，不关闭行/列无条件命题。",
            f"{NEXT_ATOM} AND {BURGESS_ATOM}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_microscopic_endpoint_scale_comparison_router",
        "status": "microscopic_endpoint_scale_comparison_reduced_to_registered_side_multiplier_floor",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "microscopic_endpoint_scale_comparison_active": active,
        "square_root_collar_floor_imported": collar_floor_imported and weighted_collar_imported,
        "side_multiplier_normalization_closed": active,
        "kappa_below_half_power_margin_algebra_closed": power_margin_algebra_closed,
        "registered_endpoint_side_cauchy_multiplier_floor_proved": side_multiplier_floor_proved,
        "microscopic_endpoint_strip_cauchy_scale_comparison_proved": scale_comparison_proved,
        "microscopic_side_whitney_packing_mass_ledger_proved": microscopic_ledger_proved,
        "burgess_pointwise_input_still_open": burgess_still_open,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "reduced_internal_atom": TARGET,
        "parallel_required_target": BURGESS_ATOM,
        "normalization": normalization,
        "collar_margin": collar_margin,
        "remaining_floor": remaining_floor,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "微薄端点尺度比较继续缩窄。端点 strip 重数已给 "
            "`P^o(1)*T*TripleSideSquareMass_s`；若 Cauchy 尺度中同一侧登记了 "
            "`CauchyScale_s>=A_s*TripleSideSquareMass_s`，则比较只需 `A_s` 大于 `T` 一个固定幂。"
            "已有平方根颈部给 `|J|>=P^(1/2)/log^236(P)`，所以只要该环境尺度确实注册为每个"
            "微薄端点兼容侧的 Cauchy 乘子，任意 `kappa<1/2` 都能支付微观宽度。"
            "当前唯一剩余因此压成侧向乘子地板的注册问题。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 微薄端点尺度比较证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"side_multiplier_normalization_closed={fmt_bool(result['side_multiplier_normalization_closed'])}",
        f"kappa_below_half_power_margin_algebra_closed={fmt_bool(result['kappa_below_half_power_margin_algebra_closed'])}",
        f"registered_endpoint_side_cauchy_multiplier_floor_proved={fmt_bool(result['registered_endpoint_side_cauchy_multiplier_floor_proved'])}",
        f"microscopic_endpoint_strip_cauchy_scale_comparison_proved={fmt_bool(result['microscopic_endpoint_strip_cauchy_scale_comparison_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 归一化",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["normalization"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 颈部幂余量",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["collar_margin"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 新最窄输入",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["remaining_floor"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书只关闭尺度比较的侧向归一化和 `kappa<1/2` 的幂余量代数；",
            "尚未证明端点兼容侧向 Cauchy 乘子地板，也不声明薄包或行/列命题闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
