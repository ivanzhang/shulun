#!/usr/bin/env python3
"""生成 strict 同参数终端余量表证书。

用法示例：
  python3 experiments/prime_matrix_strict_concrete_same_parameter_margin_table_certificate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json",
    MONOGRAPH / "prime-matrix-strict-positive-terminal-budget-margin-attack-router.json",
    MONOGRAPH / "prime-matrix-linear-lower-sieve-tail-margin-router.md",
    MONOGRAPH / "prime-matrix-linear-sieve-tail-remainder-gap-router.json",
    MONOGRAPH / "prime-matrix-explicit-rosser-lower-weight-ledger-router.json",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json",
    MONOGRAPH / "prime-matrix-strict-cold-core-nonpersistent-supply-balance-router.json",
    MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.json",
    MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json",
]

CONCRETE_TABLE = "ConcreteSameParameterMarginTableCertificate"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
LINEAR_TAIL = "LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger"
WEIGHTED_FLOOR = "RosserIwaniecWeightedFloorRemainderTenPercentBound"
EXTERNAL_ROUGH = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
STANDARD_BETA = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXACT_SAWTOOTH = "ExactResidueWeightedFloorSawtoothTenPercentBound"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
NAMED_NUMERIC = "NamedReturnSameParameterDeductionTable"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
SAE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
PDEC_CLEAN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
P_MIN = 100_000
TARGET_S = 401.0
EULER_GAMMA = 0.5772156649015329
LINEAR_TAIL_MODEL_MAIN_AT_P_MIN = 4896.256004


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def linear_sieve_f(alpha: float = ALPHA) -> float:
    """计算 2<s<3 区间线性下界筛函数 f(s)。"""
    s_value = 1.0 / alpha
    return 2.0 * math.exp(EULER_GAMMA) * math.log(s_value - 1.0) / s_value


def candidate_parameter_row() -> dict[str, Any]:
    """给出唯一可尝试装配的同参数候选行。"""
    s_value = 1.0 / ALPHA
    # 与 prime-matrix-linear-lower-sieve-tail-margin-router.md 的登记口径保持一致。
    model_main = LINEAR_TAIL_MODEL_MAIN_AT_P_MIN
    ten_percent = 0.1 * model_main
    return {
        "parameter_id": "alpha043_pge100000_external_b3_pending_finite_prefix_named_return",
        "alpha": ALPHA,
        "s": s_value,
        "p_min": P_MIN,
        "z_rule": "z=P^0.43 or equivalent non-circular prefix cutoff inherited from B3 lane",
        "b3_tail_model_main_at_p_min": model_main,
        "ten_percent_model_main_at_p_min": ten_percent,
        "target_S": TARGET_S,
        "ten_percent_minus_target": ten_percent - TARGET_S,
        "d0_prefix_lower_bound": None,
        "e0_named_return_deduction": None,
        "u0_cold_supply_bound": None,
        "margin_delta": None,
        "finite_boundary_hash": None,
        "certificate_row_valid": False,
    }


def field_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """列出同参数表字段的装配状态。"""
    return [
        {
            "field": "parameter_id",
            "available": True,
            "source": "canonical alpha=0.43 / P>=100000 candidate row",
            "blocker": "none",
        },
        {
            "field": "D0_prefix_lower_bound",
            "available": result["d0_prefix_lower_bound_available"],
            "source": "B3 external lane + finite prefix certificate",
            "blocker": f"({WEIGHTED_FLOOR} OR {EXTERNAL_ROUGH}) AND {FINITE_PREFIX}",
        },
        {
            "field": "E0_named_return_deduction",
            "available": result["e0_named_return_deduction_available"],
            "source": "named return exclusion/compression ledger",
            "blocker": f"{NAMED_RETURN} AND {NAMED_NUMERIC}",
        },
        {
            "field": "U0_cold_supply_bound",
            "available": result["u0_cold_supply_bound_available"],
            "source": "cold supply upper envelope + lambda discipline",
            "blocker": COLD_NUMERIC,
        },
        {
            "field": "margin_delta",
            "available": result["margin_delta_available"],
            "source": "D0-E0-U0 under same parameter_id",
            "blocker": CONCRETE_TABLE,
        },
        {
            "field": "finite_boundary_hash",
            "available": result["finite_boundary_hash_available"],
            "source": "finite prefix audit/certificate",
            "blocker": FINITE_PREFIX,
        },
    ]


def direct_attempt_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """列出直接生成/证明尝试的结果。"""
    row = result["candidate_parameter_row"]
    return [
        {
            "attempt": "assemble candidate parameter row",
            "success": True,
            "evidence": row["parameter_id"],
            "meaning": "同一参数行可以命名，但尚不构成证明证书。",
        },
        {
            "attempt": "import external B3 tail margin",
            "success": result["b3_external_lane_imported"],
            "evidence": f"10% model main at P=100000 is {row['ten_percent_model_main_at_p_min']:.6f}",
            "meaning": "解析尾段有条件可供 D0 使用；仍需有限 prefix 和真实 D0 表。",
        },
        {
            "attempt": "prove D0 lower bound",
            "success": result["d0_prefix_lower_bound_available"],
            "evidence": "missing weighted floor/sawtooth or external rough input, plus finite prefix hash",
            "meaning": "无法从当前材料直接给出全局 D0。",
        },
        {
            "attempt": "prove E0 named deduction",
            "success": result["e0_named_return_deduction_available"],
            "evidence": "named compression closed but exclusion/numeric deduction open",
            "meaning": "无法证明 E_named 不吞掉余量。",
        },
        {
            "attempt": "prove U0 cold dominance",
            "success": result["u0_cold_supply_bound_available"],
            "evidence": "upper envelope formula exists; same-parameter numeric value missing",
            "meaning": "有供给公式，但还不能和 D0-E0 比较。",
        },
        {
            "attempt": "derive margin_delta>0",
            "success": result["concrete_same_parameter_margin_table_certificate_proved"],
            "evidence": "D0/E0/U0 not simultaneously numeric",
            "meaning": "本轮直接证明失败，失败原因已原子化。",
        },
    ]


def failure_return_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """若同参数表无法为正，列出强制回流去向。"""
    return [
        {
            "missing_or_failure": "D0 absent or finite prefix undecided",
            "forced_return": FINITE_PREFIX,
            "closed_as_logic": True,
            "proved_now": result["d0_prefix_lower_bound_available"],
        },
        {
            "missing_or_failure": "E0 named deduction absent",
            "forced_return": f"{PDEC_CLEAN} OR {NAMED_NUMERIC}",
            "closed_as_logic": True,
            "proved_now": result["e0_named_return_deduction_available"],
        },
        {
            "missing_or_failure": "U0 too large or unregistered",
            "forced_return": f"{SAE_BUDGET} OR {COLD_NUMERIC}",
            "closed_as_logic": True,
            "proved_now": result["u0_cold_supply_bound_available"],
        },
        {
            "missing_or_failure": "terminal promotion still external",
            "forced_return": DSTRUCTURE,
            "closed_as_logic": True,
            "proved_now": result["dstructure_rankin_independently_accepted"],
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本证书仍只在早期零行反例链内尝试装配终端正余量表。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "CandidateParameterRowGenerated",
            "closed": True,
            "proved": False,
            "meaning": "已生成 alpha=0.43, P>=100000 的候选同参数行；它只是装配目标，不是证明。",
            "remaining": "fill D0/E0/U0/margin_delta/hash.",
        },
        {
            "gate": "ConcreteD0Available",
            "closed": result["d0_prefix_lower_bound_available"],
            "proved": result["d0_prefix_lower_bound_available"],
            "meaning": "当前不能给出 D0_prefix_lower_bound。",
            "remaining": f"({WEIGHTED_FLOOR} OR {EXTERNAL_ROUGH}) AND {FINITE_PREFIX}",
        },
        {
            "gate": "ConcreteE0Available",
            "closed": result["e0_named_return_deduction_available"],
            "proved": result["e0_named_return_deduction_available"],
            "meaning": "当前不能给出 E0_named_return_deduction。",
            "remaining": f"{NAMED_RETURN} AND {NAMED_NUMERIC}",
        },
        {
            "gate": "ConcreteU0Available",
            "closed": result["u0_cold_supply_bound_available"],
            "proved": result["u0_cold_supply_bound_available"],
            "meaning": "当前只有 U_cold 公式，没有同参数数值上界。",
            "remaining": COLD_NUMERIC,
        },
        {
            "gate": "ConcreteSameParameterMarginTableCertificateProved",
            "closed": result["concrete_same_parameter_margin_table_certificate_proved"],
            "proved": result["concrete_same_parameter_margin_table_certificate_proved"],
            "meaning": "D0/E0/U0 未同时数值化，不能推出 margin_delta>0。",
            "remaining": result["hardpoint_after_router"],
        },
        {
            "gate": "DirectTerminalContradictionReached",
            "closed": result["direct_unconditional_contradiction_found"],
            "proved": result["direct_unconditional_contradiction_found"],
            "meaning": "还没有得到反例链与真实结构链的终端矛盾。",
            "remaining": f"{CONCRETE_TABLE} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造同参数终端余量表装配证书。"""
    coupled = load_json(MONOGRAPH / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json")
    positive = load_json(MONOGRAPH / "prime-matrix-strict-positive-terminal-budget-margin-attack-router.json")
    prefix = load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json")
    named = load_json(MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json")
    cold = load_json(MONOGRAPH / "prime-matrix-strict-cold-core-threshold-budget-gap-router.json")
    sparse = load_json(MONOGRAPH / "prime-matrix-strict-sparse-terminal-history-sae-budget-router.json")
    tail_gap = load_json(MONOGRAPH / "prime-matrix-linear-sieve-tail-remainder-gap-router.json")
    explicit_weight = load_json(MONOGRAPH / "prime-matrix-explicit-rosser-lower-weight-ledger-router.json")

    row = candidate_parameter_row()
    b3_external = positive.get("b3_external_front_no_longer_primary_blocker") is True
    finite_prefix_closed = prefix.get("finite_boundary_prefix_rough_count_certificate_proved") is True
    lower_sieve_tail_split = tail_gap.get("tail_ten_percent_margin_split") is True
    explicit_weight_compressed = explicit_weight.get("explicit_rosser_iwaniec_lower_weight_ledger_compressed") is True
    lower_sieve_tail_closed = (
        tail_gap.get("rosser_iwaniec_weighted_floor_remainder_proved") is True
        or tail_gap.get("external_short_interval_rough_lower_bound_accepted") is True
    )
    d0_available = (
        b3_external
        and finite_prefix_closed
        and lower_sieve_tail_closed
        and prefix.get("uniform_prefix_rough_count_lower_bound_proved") is True
    )
    e0_available = named.get("named_return_exclusion_proved") is True
    u0_available = (
        cold.get("cold_supply_upper_bound_closed") is True
        and cold.get("cold_supply_upper_bound_beats_load") is True
        and sparse.get("sparse_history_demand_exceeds_budget_proved") is True
    )
    finite_hash_available = finite_prefix_closed and coupled.get("finite_boundary_hash_present") is True
    margin_available = d0_available and e0_available and u0_available and finite_hash_available
    dstructure_accepted = positive.get("dstructure_rankin_independently_accepted") is True
    direct = margin_available and dstructure_accepted

    result = {
        "certificate_type": "prime_matrix_strict_concrete_same_parameter_margin_table_certificate_router",
        "status": "concrete_same_parameter_margin_table_attempted_blocked_by_missing_d0_e0_u0_fields",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "candidate_parameter_row": row,
        "candidate_parameter_row_generated": True,
        "b3_external_lane_imported": b3_external,
        "linear_lower_sieve_tail_ten_percent_margin_pge100000_proved": lower_sieve_tail_closed,
        "linear_sieve_tail_split_to_weighted_floor_or_external_rough": lower_sieve_tail_split,
        "explicit_rosser_weight_ledger_compressed": explicit_weight_compressed,
        "finite_boundary_prefix_certificate_proved": finite_prefix_closed,
        "finite_boundary_hash_available": finite_hash_available,
        "d0_prefix_lower_bound_available": d0_available,
        "e0_named_return_deduction_available": e0_available,
        "u0_cold_supply_bound_available": u0_available,
        "margin_delta_available": margin_available,
        "concrete_same_parameter_margin_table_certificate_proved": margin_available,
        "dstructure_rankin_independently_accepted": dstructure_accepted,
        "direct_unconditional_contradiction_found": direct,
        "row_column_unconditional_closed": direct,
        "hardpoint_before_router": CONCRETE_TABLE,
        "hardpoint_after_router": (
            f"({WEIGHTED_FLOOR} OR {EXTERNAL_ROUGH}) AND {FINITE_PREFIX} AND {NAMED_NUMERIC} "
            f"AND {COLD_NUMERIC} AND {SAE_BUDGET} AND {DSTRUCTURE}"
        ),
        "next_direct_attack_target": WEIGHTED_FLOOR,
        "parallel_attack_targets": [EXTERNAL_ROUGH, FINITE_PREFIX, NAMED_NUMERIC, COLD_NUMERIC, SAE_BUDGET, DSTRUCTURE],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ConcreteSameParameterMarginTableCertificate` 已被直接尝试装配。可以生成唯一候选参数行 "
            "`alpha043_pge100000_external_b3_pending_finite_prefix_named_return`，并确认外部 B3 前沿可作为 D0 的解析尾段输入；"
            "但当前材料没有 D0_prefix_lower_bound、E0_named_return_deduction、U0_cold_supply_bound 的同参数数值字段，"
            "也没有 finite_boundary_hash，因此不能证明 margin_delta>0。直接证明失败不是换命题，而是把下一原子压成 "
            "`RosserIwaniecWeightedFloorRemainderTenPercentBound` 或外部短区间 rough 下界，并行保留有限 prefix/命名扣除/冷供给数值表。"
        ),
    }
    result["field_rows"] = field_rows(result)
    result["direct_attempt_rows"] = direct_attempt_rows(result)
    result["failure_return_rows"] = failure_return_rows(result)
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    row = result["candidate_parameter_row"]
    lines = [
        "# Prime Matrix strict 同参数终端余量表证书路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"candidate_parameter_row_generated={fmt_bool(result['candidate_parameter_row_generated'])}",
        f"b3_external_lane_imported={fmt_bool(result['b3_external_lane_imported'])}",
        f"linear_lower_sieve_tail_ten_percent_margin_pge100000_proved={fmt_bool(result['linear_lower_sieve_tail_ten_percent_margin_pge100000_proved'])}",
        f"linear_sieve_tail_split_to_weighted_floor_or_external_rough={fmt_bool(result['linear_sieve_tail_split_to_weighted_floor_or_external_rough'])}",
        f"explicit_rosser_weight_ledger_compressed={fmt_bool(result['explicit_rosser_weight_ledger_compressed'])}",
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        f"finite_boundary_hash_available={fmt_bool(result['finite_boundary_hash_available'])}",
        f"d0_prefix_lower_bound_available={fmt_bool(result['d0_prefix_lower_bound_available'])}",
        f"e0_named_return_deduction_available={fmt_bool(result['e0_named_return_deduction_available'])}",
        f"u0_cold_supply_bound_available={fmt_bool(result['u0_cold_supply_bound_available'])}",
        f"margin_delta_available={fmt_bool(result['margin_delta_available'])}",
        f"concrete_same_parameter_margin_table_certificate_proved={fmt_bool(result['concrete_same_parameter_margin_table_certificate_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 候选同参数行",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key in [
        "parameter_id",
        "alpha",
        "s",
        "p_min",
        "z_rule",
        "b3_tail_model_main_at_p_min",
        "ten_percent_model_main_at_p_min",
        "target_S",
        "ten_percent_minus_target",
        "d0_prefix_lower_bound",
        "e0_named_return_deduction",
        "u0_cold_supply_bound",
        "margin_delta",
        "finite_boundary_hash",
        "certificate_row_valid",
    ]:
        value = row[key]
        if isinstance(value, float):
            value = f"{value:.12f}"
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 字段装配状态",
            "",
            "| field | available | source | blocker |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["field_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['field'])}`",
                    f"`{fmt_bool(item['available'])}`",
                    table_cell(item["source"]),
                    table_cell(item["blocker"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 直接生成/证明尝试",
            "",
            "| attempt | success | evidence | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["direct_attempt_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['attempt'])}`",
                    f"`{fmt_bool(item['success'])}`",
                    table_cell(item["evidence"]),
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 失败回流表",
            "",
            "| missing_or_failure | forced_return | closed_as_logic | proved_now |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["failure_return_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    table_cell(item["missing_or_failure"]),
                    table_cell(item["forced_return"]),
                    f"`{fmt_bool(item['closed_as_logic'])}`",
                    f"`{fmt_bool(item['proved_now'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一最窄点",
            "",
            "```text",
            result["hardpoint_after_router"],
            "```",
            "",
            "当前最先攻 `RosserIwaniecWeightedFloorRemainderTenPercentBound`，因为已有材料已经把线性筛 10% 主项包压成该加权 floor 余项或外部短区间 rough 下界；"
            "没有 D0，后续 E0/U0 即使给出也无法形成正余量比较。有限 prefix hash、命名扣除表、冷供给数值包仍并行保留。",
            "",
            "审稿边界：本文件直接生成了同参数候选行和 BLOCK 证书，但没有证明 `margin_delta>0`。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
