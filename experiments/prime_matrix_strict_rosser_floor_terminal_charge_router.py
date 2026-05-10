#!/usr/bin/env python3
"""生成 strict Rosser floor 终端收费路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_rosser_floor_terminal_charge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rosser-floor-terminal-charge-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-rosser-floor-terminal-charge-router.json"
OUT_MD = DOCS / "prime-matrix-strict-rosser-floor-terminal-charge-router.md"

CONCRETE = DOCS / "prime-matrix-strict-concrete-same-parameter-margin-table-certificate-router.json"
ROSSLER_FLOOR = DOCS / "prime-matrix-rosser-weight-floor-ledger-router.json"
SAWTOOTH = DOCS / "prime-matrix-exact-residue-sawtooth-normal-form-router.json"
QUADRATIC = DOCS / "prime-matrix-quadratic-arc-nearsquare-spread-router.json"
SUPPORT = DOCS / "prime-matrix-rosser-weight-support-functor-router.json"
STRIP_DEFECT = DOCS / "prime-matrix-nearsquare-strip-defect-certificate-router.json"
STRIP_TERMINAL = DOCS / "prime-matrix-nearsquare-strip-terminal-admission-router.json"
STRICT_HIGH_TAIL = DOCS / "prime-matrix-strict-high-tail-corpus-reconciliation-router.json"
NAMED_RETURN = DOCS / "prime-matrix-strict-named-return-exclusion-compression-router.json"
COUPLED_LEDGER = DOCS / "prime-matrix-strict-finite-prefix-named-return-coupled-margin-ledger-router.json"

SOURCE_FILES = [
    CONCRETE,
    ROSSLER_FLOOR,
    SAWTOOTH,
    QUADRATIC,
    SUPPORT,
    STRIP_DEFECT,
    STRIP_TERMINAL,
    STRICT_HIGH_TAIL,
    NAMED_RETURN,
    COUPLED_LEDGER,
]

WEIGHTED_FLOOR = "RosserIwaniecWeightedFloorRemainderTenPercentBound"
EXTERNAL_ROUGH = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
NAMED_NUMERIC = "NamedReturnSameParameterDeductionTable"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
SAE_BUDGET = "SparseHistoryDemandExceedsNonpersistentSupplyBudget"
STRICT_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；历史文件不存在时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本证书实际依赖的文件哈希。"""
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


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def branch(
    name: str,
    condition: str,
    routed_to: str,
    closed_as_logic: bool,
    proved_now: bool,
    consequence: str,
) -> dict[str, Any]:
    """构造分支收费表行。"""
    return {
        "branch": name,
        "condition": condition,
        "routed_to": routed_to,
        "closed_as_logic": closed_as_logic,
        "proved_now": proved_now,
        "consequence": consequence,
    }


def build_result() -> dict[str, Any]:
    """构造 Rosser floor 终端收费证书。"""
    concrete = load_json(CONCRETE)
    rosser = load_json(ROSSLER_FLOOR)
    sawtooth = load_json(SAWTOOTH)
    quadratic = load_json(QUADRATIC)
    support = load_json(SUPPORT)
    strip_defect = load_json(STRIP_DEFECT)
    strip_terminal = load_json(STRIP_TERMINAL)
    high_tail = load_json(STRICT_HIGH_TAIL)
    named = load_json(NAMED_RETURN)
    coupled = load_json(COUPLED_LEDGER)

    guard = (
        concrete.get("counterexample_assumption_only") is True
        and concrete.get("empirical_absence_not_used") is True
        and concrete.get("row_column_unconditional_closed") is False
    )
    same_parameter_row = concrete.get("candidate_parameter_row", {}).get("parameter_id")
    rosser_split = rosser.get("rosser_weight_floor_remainder_split") is True
    sawtooth_normal = sawtooth.get("sawtooth_atom_compressed") is True
    quadratic_compressed = quadratic.get("quadratic_arc_discrepancy_compressed") is True
    support_absorbed = support.get("rosser_weight_support_functorially_absorbed") is True
    strip_defect_packet = strip_defect.get("failure_to_dyadic_strip_certificate_proved") is True
    strip_admitted_global = strip_terminal.get("nearsquare_strip_terminal_admission_closed") is True
    strict_charge = high_tail.get("exact_sawtooth_independent_input_removed") is True
    named_compression = named.get("named_return_compression_closed") is True

    # 中文注释：收费闭合只说明“失败不再是无名 D0 缺口”，不说明终端家族已排斥。
    no_free_sawtooth_failure = all(
        [
            guard,
            rosser_split,
            sawtooth_normal,
            quadratic_compressed,
            support_absorbed,
            strip_defect_packet,
            strip_admitted_global,
            strict_charge,
            named_compression,
        ]
    )

    weighted_floor_d0 = concrete.get("linear_lower_sieve_tail_ten_percent_margin_pge100000_proved") is True
    external_rough = concrete.get("external_short_interval_rough_lower_bound_accepted") is True
    finite_prefix = concrete.get("finite_boundary_prefix_certificate_proved") is True
    named_numeric = False
    cold_numeric = concrete.get("u0_cold_supply_bound_available") is True
    margin = concrete.get("margin_delta_available") is True
    strict_terminal_proved = high_tail.get("strict_terminal_family_proved") is True
    direct = margin and strict_terminal_proved and concrete.get("dstructure_rankin_independently_accepted") is True

    hardpoint_before = concrete.get("hardpoint_after_router", "")
    d0_front_after = (
        f"{FINITE_PREFIX} AND "
        f"({WEIGHTED_FLOOR} OR {EXTERNAL_ROUGH} OR "
        f"SawtoothFailureChargedToNamedTerminalFamily)"
    )
    hardpoint_after = (
        f"{d0_front_after} AND ({NAMED_NUMERIC} OR {STRICT_TERMINAL}) "
        f"AND {COLD_NUMERIC} AND {SAE_BUDGET} AND {DSTRUCTURE}"
    )

    branch_rows = [
        branch(
            "weighted_floor_success",
            "Rosser floor/sawtooth loss is within the 10% budget",
            "D0_prefix_lower_bound",
            True,
            weighted_floor_d0,
            "可给 D0，但仍需 finite prefix hash 与 E0/U0 同参数字段。",
        ),
        branch(
            "external_rough_success",
            "ExternalShortIntervalRoughNumberLowerBoundForAlpha043 is accepted",
            "D0_prefix_lower_bound",
            True,
            external_rough,
            "外部 rough 下界可绕过内部 sawtooth，但仍是外部输入。",
        ),
        branch(
            "sawtooth_or_strip_failure",
            "weighted floor bound fails through exact sawtooth / near-square strip",
            f"{STRICT_TERMINAL} and then {NAMED_NUMERIC}",
            no_free_sawtooth_failure,
            False,
            "失败态必须登记为同 formal unit 的 PDEC/SAE/ColumnCRT/CleanKLS 终端收费，不能作为无名 D0 损失。",
        ),
        branch(
            "finite_prefix_absent",
            "tail lane available but finite boundary prefix certificate is absent",
            FINITE_PREFIX,
            True,
            finite_prefix,
            "没有有限边界 hash，任何渐近尾段余量都不能升级为全局 D0。",
        ),
        branch(
            "named_return_not_numeric",
            "terminal charge exists but same-parameter E_named table is absent",
            NAMED_NUMERIC,
            True,
            named_numeric,
            "下一步必须给同一 parameter_id 下的命名扣除表，否则收费不能进入 margin_delta。",
        ),
        branch(
            "cold_supply_not_numeric",
            "nonpersistent supply can still absorb demand",
            f"{COLD_NUMERIC} AND {SAE_BUDGET}",
            True,
            cold_numeric,
            "冷供给上界仍需和 D0-E0 做同参数比较。",
        ),
    ]

    decision_rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍在假设早期零行反例链内部收费，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "RosserFloorSplitImported",
            rosser_split,
            True,
            "Rosser floor 旧原子已拆成 lower weights 与 exact sawtooth。",
            "继续接 sawtooth/条带失败态。",
        ),
        row(
            "SawtoothFailureNoFreeD0Loss",
            no_free_sawtooth_failure,
            False,
            "若 sawtooth/近平方条带估计失败，失败态已经强制变成命名终端家族，不再是无名 D0 黑洞。",
            f"{STRICT_TERMINAL} OR {NAMED_NUMERIC}",
        ),
        row(
            "D0FrontRewritten",
            no_free_sawtooth_failure,
            False,
            "D0 前沿由单纯 Rosser floor 证明，改写为 floor 成功、外部 rough 成功、或失败收费三分支。",
            d0_front_after,
        ),
        row(
            "ConcreteD0AvailableNow",
            weighted_floor_d0 or external_rough,
            weighted_floor_d0 or external_rough,
            "本轮没有证明新的 D0 数值下界；只关闭了失败态收费纪律。",
            f"{WEIGHTED_FLOOR} OR {EXTERNAL_ROUGH} OR charged terminal exclusion",
        ),
        row(
            "NamedReturnSameParameterNeeded",
            named_numeric,
            named_numeric,
            "收费后真正需要把终端回流写成同一参数行的 E0 扣除表。",
            NAMED_NUMERIC,
        ),
        row(
            "ConcreteSameParameterMarginTableProved",
            margin,
            margin,
            "D0/E0/U0 仍未同时数值化，不能推出 margin_delta>0。",
            hardpoint_after,
        ),
        row(
            "DirectTerminalContradictionReached",
            direct,
            direct,
            "尚未得到反例链与真实结构链的无条件终端矛盾。",
            f"{NAMED_NUMERIC} OR {STRICT_TERMINAL} OR {EXTERNAL_ROUGH} OR {FINITE_PREFIX}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rosser_floor_terminal_charge_router",
        "status": "rosser_floor_failure_charged_to_named_terminal_family_margin_table_still_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "parameter_id": same_parameter_row,
        "rosser_floor_split_imported": rosser_split,
        "sawtooth_normal_form_imported": sawtooth_normal,
        "quadratic_nearsquare_compression_imported": quadratic_compressed,
        "rosser_support_absorbed": support_absorbed,
        "strip_failure_packetized": strip_defect_packet,
        "strip_terminal_admitted": strip_admitted_global,
        "strict_sawtooth_failure_charged": strict_charge,
        "named_return_compression_imported": named_compression,
        "sawtooth_failure_no_free_d0_loss_closed": no_free_sawtooth_failure,
        "weighted_floor_d0_available": weighted_floor_d0,
        "external_short_interval_rough_lower_bound_accepted": external_rough,
        "finite_boundary_prefix_certificate_proved": finite_prefix,
        "named_return_same_parameter_deduction_table_proved": named_numeric,
        "cold_supply_same_parameter_numeric_envelope_proved": cold_numeric,
        "concrete_same_parameter_margin_table_certificate_proved": margin,
        "direct_unconditional_contradiction_found": direct,
        "row_column_unconditional_closed": direct,
        "hardpoint_before_router": hardpoint_before,
        "d0_front_after_router": d0_front_after,
        "hardpoint_after_router": hardpoint_after,
        "next_direct_attack_target": NAMED_NUMERIC,
        "parallel_attack_targets": [
            STRICT_TERMINAL,
            EXTERNAL_ROUGH,
            FINITE_PREFIX,
            COLD_NUMERIC,
            SAE_BUDGET,
            DSTRUCTURE,
        ],
        "branch_rows": branch_rows,
        "decision_rows": decision_rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接硬攻 D0 前沿的 Rosser floor 缺口。结论不是证明 D0 已有数值下界，"
            "而是证明一个更窄的收费纪律：内部 sawtooth/近平方条带若失败，不能继续作为无名 D0 损失；"
            "它已经由 exact sawtooth 标准形、二次圆弧、近平方条带缺陷证书和 strict high-tail 校准，"
            "强制进入同 formal unit 的 PDEC/SAE/ColumnCRT/CleanKLS 终端家族。"
            "因此下一步最窄点从“继续盲攻 Rosser floor”转为生成同一 parameter_id 下的 "
            "NamedReturnSameParameterDeductionTable；并行保留 strict 终端家族排斥、外部 rough 下界、"
            "finite prefix hash、冷供给数值表和 DStructure/Rankin 独立验收门。"
        ),
        "coupled_status_snapshot": {
            "coupled_margin_schema_closed": coupled.get("coupled_margin_schema_closed"),
            "concrete_parameter_table_present": coupled.get("concrete_parameter_table_present"),
            "finite_boundary_hash_present": coupled.get("finite_boundary_hash_present"),
            "named_return_numeric_bound_present": coupled.get("named_return_numeric_bound_present"),
            "cold_supply_numeric_bound_present": coupled.get("cold_supply_numeric_bound_present"),
        },
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Rosser floor 终端收费路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"parameter_id={result['parameter_id']}",
        f"sawtooth_failure_no_free_d0_loss_closed={fmt_bool(result['sawtooth_failure_no_free_d0_loss_closed'])}",
        f"weighted_floor_d0_available={fmt_bool(result['weighted_floor_d0_available'])}",
        (
            "external_short_interval_rough_lower_bound_accepted="
            f"{fmt_bool(result['external_short_interval_rough_lower_bound_accepted'])}"
        ),
        f"finite_boundary_prefix_certificate_proved={fmt_bool(result['finite_boundary_prefix_certificate_proved'])}",
        (
            "named_return_same_parameter_deduction_table_proved="
            f"{fmt_bool(result['named_return_same_parameter_deduction_table_proved'])}"
        ),
        (
            "concrete_same_parameter_margin_table_certificate_proved="
            f"{fmt_bool(result['concrete_same_parameter_margin_table_certificate_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. D0 前沿改写",
        "",
        "改写前：",
        "",
        "```text",
        result["hardpoint_before_router"],
        "```",
        "",
        "改写后：",
        "",
        "```text",
        result["hardpoint_after_router"],
        "```",
        "",
        "核心收费律：",
        "",
        "```text",
        result["d0_front_after_router"],
        "```",
        "",
        "## 2. 分支收费表",
        "",
        "| branch | condition | routed_to | closed_as_logic | proved_now | consequence |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["branch_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['branch'])}`",
                    table_cell(item["condition"]),
                    table_cell(item["routed_to"]),
                    f"`{fmt_bool(item['closed_as_logic'])}`",
                    f"`{fmt_bool(item['proved_now'])}`",
                    table_cell(item["consequence"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 下一真正最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " OR ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本文件只关闭 Rosser floor 失败态的收费纪律；它没有证明同参数 E0 数值表，也没有证明行/列命题无条件闭合。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
