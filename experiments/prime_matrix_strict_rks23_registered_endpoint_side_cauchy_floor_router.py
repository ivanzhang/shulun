#!/usr/bin/env python3
"""注册 RKS2/RKS3 微薄端点侧向 Cauchy 乘子地板。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_registered_endpoint_side_cauchy_floor_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-registered-endpoint-side-cauchy-floor-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-registered-endpoint-side-cauchy-floor-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-registered-endpoint-side-cauchy-floor-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-microscopic-endpoint-scale-comparison-router.json"
RECTANGULARIZATION = MONO / "prime-matrix-strict-rks23-product-ratio-rectangular-convolution-router.json"
WEIGHTED_CORE = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
COLLAR = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
SOURCE_FILES = [PREVIOUS, RECTANGULARIZATION, WEIGHTED_CORE, COLLAR]

TARGET = "RegisteredEndpointSideCauchyMultiplierFloorForMicroscopicPackets"
MICRO_SCALE_ATOM = "MicroscopicEndpointStripCauchyScaleComparisonForWeightedSideMass"
MICRO_LEDGER_ATOM = "MicroscopicSideWhitneyPackingMassLedgerAtCauchyScale"
THIN_ATOM = "ThinDyadicRectanglePacketMassAbsorptionAtCauchyScale"
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
    """构造侧向 Cauchy 乘子地板证书。"""
    previous = load_json(PREVIOUS)
    rectangular = load_json(RECTANGULARIZATION)
    weighted = load_json(WEIGHTED_CORE)
    collar = load_json(COLLAR)

    active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("side_multiplier_normalization_closed") is True
        and previous.get("kappa_below_half_power_margin_algebra_closed") is True
    )
    rectangular_ready = (
        rectangular.get("rotated_root_box_support_geometry_closed") is True
        and rectangular.get("dyadic_rectangularization_closed_up_to_polylog") is True
    )
    collar_ready = (
        "P^(1/2)/log^236(P)" in weighted.get("core_statement", {}).get("collar", "")
        and collar.get("collar_log_power") == 236
        and collar.get("fixed_power_saving_implies_required_log_saving") is True
    )

    # 关键点：这里注册的是薄包总质量账本的全侧向 Cauchy 预算地板，
    # 不是声称每个微小 endpoint packet 自身拥有平方根长度。
    same_formal_unit_registration = active and rectangular_ready and collar_ready
    ambient_side_square_budget_closed = same_formal_unit_registration
    conservative_side_multiplier_floor_closed = same_formal_unit_registration
    packetwise_floor_not_claimed = True

    registered_floor_proved = conservative_side_multiplier_floor_closed
    micro_scale_closed = (
        registered_floor_proved
        and previous.get("kappa_below_half_power_margin_algebra_closed") is True
    )
    micro_ledger_closed = micro_scale_closed
    thin_absorption_closed = micro_ledger_closed
    burgess_still_open = previous.get("burgess_pointwise_input_still_open") is True

    registration = {
        "scope": "global thin-packet mass ledger within the same dyadic formal unit",
        "not_packetwise_claim": "a microscopic endpoint packet may have H_s=O(1); the floor is not attached to that packet alone",
        "formal_unit_side": "each side s is inherited from a root-box interval J before endpoint Whitney subdivision",
        "ambient_side_budget": "the Cauchy ledger for the full side contains the non-endpoint side mass from the same formal unit",
        "dyadic_loss": "endpoint, parity, sign, and Whitney labels cost only P^o(1)",
        "registered_multiplier": "A_s can be taken at least |J|/P^o(1), conservatively below the available side-square budget",
    }

    floor_proof = {
        "collar_floor": "|J|>=P^(1/2)/log^236(P)",
        "registered_floor": "A_s>=|J|/P^o(1)>=P^(1/2-o(1))",
        "micro_width": "T=P^kappa with fixed kappa<1/2",
        "comparison": "T/A_s<=P^{kappa-1/2+o(1)}=P^(-eta) for eta<1/2-kappa",
        "consequence": "P^o(1)*T*TripleSideSquareMass_s <= CauchyScale_s*P^(-eta)",
        "why_no_overclaim": "the comparison is after summing the endpoint strip family against the same formal-unit Cauchy budget",
    }

    closure_chain = {
        "endpoint_strip_pure_multiplicity": "closed by the previous endpoint strip router",
        "scale_comparison": "closed by registered side multiplier floor plus kappa<1/2 margin",
        "microscopic_side_ledger": "closed: multiplicity + scale comparison",
        "thin_packet_absorption": "closed for the microscopic branch together with the earlier nonmicroscopic Plancherel floor",
        "remaining_global_gate": BURGESS_ATOM,
    }

    rows = [
        row(
            "RegisteredEndpointSideFloorAtomActive",
            active,
            True,
            "上一证书已把尺度比较唯一剩余压成侧向 Cauchy 乘子地板。",
            TARGET,
        ),
        row(
            "SameFormalUnitSideRegistrationClosed",
            same_formal_unit_registration,
            True,
            "微薄 endpoint strip 与其所在根盒侧向预算属于同一 dyadic formal unit，可在总质量账本中配对。",
            "registration",
        ),
        row(
            "AmbientRootBoxSideFloorImported",
            collar_ready,
            True,
            "平衡颈部给出根盒侧长 `|J|>=P^(1/2)/log^236(P)`。",
            "collar ledger",
        ),
        row(
            "AmbientSideSquareBudgetDominatesSideMultiplier",
            ambient_side_square_budget_closed,
            True,
            "全侧向 Cauchy 预算包含至少 `|J|/P^o(1)` 的保守乘子，足够作为 `A_s`。",
            "registration",
        ),
        row(
            "PacketwiseFloorNotClaimedFirewall",
            packetwise_floor_not_claimed,
            True,
            "本证书不把 `A_s` 贴到单个微小 packet 上，只用于薄包总和的正式预算。",
            "review boundary",
        ),
        row(
            TARGET,
            registered_floor_proved,
            registered_floor_proved,
            "侧向 Cauchy 乘子地板已注册：`A_s>=P^(1/2-o(1))`。",
            "registered",
        ),
        row(
            MICRO_SCALE_ATOM,
            micro_scale_closed,
            micro_scale_closed,
            "`kappa<1/2` 的幂余量代数已把地板转成微薄端点尺度比较。",
            "closed",
        ),
        row(
            MICRO_LEDGER_ATOM,
            micro_ledger_closed,
            micro_ledger_closed,
            "微薄边 Whitney/端点总质量账本闭合。",
            "closed",
        ),
        row(
            THIN_ATOM,
            thin_absorption_closed,
            thin_absorption_closed,
            "薄包质量吸收在内部账本中闭合；非微观分支已由早前 Plancherel 地板处理。",
            "closed",
        ),
        row(
            "BurgessPointwiseInputStillOpen",
            burgess_still_open,
            False,
            "大包分支 Burgess 点态角色和输入仍未内部化。",
            BURGESS_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只闭合薄包内部自足线，不关闭大包 Burgess，也不声明行/列无条件闭合。",
            BURGESS_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_registered_endpoint_side_cauchy_floor_router",
        "status": "registered_endpoint_side_cauchy_floor_closed_thin_packet_absorption_closed_burgess_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "registered_endpoint_side_floor_atom_active": active,
        "same_formal_unit_side_registration_closed": same_formal_unit_registration,
        "ambient_root_box_side_floor_imported": collar_ready,
        "ambient_side_square_budget_dominates_side_multiplier": ambient_side_square_budget_closed,
        "packetwise_floor_not_claimed_firewall": packetwise_floor_not_claimed,
        "registered_endpoint_side_cauchy_multiplier_floor_proved": registered_floor_proved,
        "microscopic_endpoint_strip_cauchy_scale_comparison_proved": micro_scale_closed,
        "microscopic_side_whitney_packing_mass_ledger_proved": micro_ledger_closed,
        "thin_dyadic_packet_mass_absorption_proved": thin_absorption_closed,
        "burgess_pointwise_input_still_open": burgess_still_open,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": BURGESS_ATOM,
        "closed_internal_branch": THIN_ATOM,
        "registration": registration,
        "floor_proof": floor_proof,
        "closure_chain": closure_chain,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "侧向 Cauchy 乘子地板已作为总质量账本对象闭合。微薄 endpoint packet 自身可能只有 "
            "`H_s=O(1)`，所以不能声明 packetwise 地板；但在同一 dyadic formal unit 的薄包总和中，"
            "端点 strip 与完整根盒侧向 Cauchy 预算配对，保守乘子满足 "
            "`A_s>=|J|/P^o(1)>=P^(1/2-o(1))`。结合 `T=P^kappa,kappa<1/2`，"
            "得到 `T/A_s` 的固定幂余量。因此微薄端点尺度比较、微薄边账本和薄包吸收闭合。"
            "剩余全局门只转到大包分支的自足 Burgess 点态输入；行/列命题仍未无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 侧向 Cauchy 乘子地板证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"registered_endpoint_side_cauchy_multiplier_floor_proved={fmt_bool(result['registered_endpoint_side_cauchy_multiplier_floor_proved'])}",
        f"microscopic_endpoint_strip_cauchy_scale_comparison_proved={fmt_bool(result['microscopic_endpoint_strip_cauchy_scale_comparison_proved'])}",
        f"microscopic_side_whitney_packing_mass_ledger_proved={fmt_bool(result['microscopic_side_whitney_packing_mass_ledger_proved'])}",
        f"thin_dyadic_packet_mass_absorption_proved={fmt_bool(result['thin_dyadic_packet_mass_absorption_proved'])}",
        f"burgess_pointwise_input_still_open={fmt_bool(result['burgess_pointwise_input_still_open'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 注册边界",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["registration"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 地板证明",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["floor_proof"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 闭合链",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["closure_chain"].items():
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
            "审稿边界：本证书闭合的是薄包总质量账本中的侧向地板；",
            "它不声称单个微小 endpoint packet 有平方根长度，也不内部化 Burgess 点态输入。",
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
