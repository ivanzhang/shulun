#!/usr/bin/env python3
"""生成 strict 正终端预算余量主攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_positive_terminal_budget_margin_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-positive-terminal-budget-margin-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-positive-terminal-budget-margin-attack-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-positive-terminal-budget-margin-attack-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-single-parameter-terminal-budget-margin-router.json",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json",
    MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json",
    MONOGRAPH / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json",
    MONOGRAPH / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json",
    MONOGRAPH / "prime-matrix-b3-self-contained-mertens-tail-router.json",
    MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json",
    MONOGRAPH / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
    MONOGRAPH / "prime-matrix-full-rankin-ledger-inventory-router.json",
]

POSITIVE_MARGIN = "ExplicitPositiveTerminalBudgetMarginInequality"
B3_DISCRETE = "B3DiscretePrimeSumUniformErrorPGe100000"
B3_TV = "B3RemainderTotalVariationBudgetForLengthP"
B3_EXTERNAL_MERTENS = "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted"
B3_SELF_MERTENS = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
PDEC_CLEAN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
COUPLED_MARGIN = "FinitePrefixNamedReturnCoupledPositiveMarginLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；文件不存在时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希，便于审稿时复核本路由输入。"""
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


def b3_front_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """列出 B3 前沿在本轮后的真实状态。"""
    return [
        {
            "front": "continuous beta demand",
            "closed": result["continuous_beta_demand_closed"],
            "proved": result["continuous_beta_demand_closed"],
            "effect": "连续主项余量可用，不再是正余量主阻塞。",
            "remaining": B3_DISCRETE,
        },
        {
            "front": "B3 discrete/Stieltjes external lane",
            "closed": result["b3_discrete_external_front_closed"],
            "proved": False,
            "effect": "接受外部 Mertens/Dusart 或标准 beta-sieve 时，离散误差和边界余项可进入条件闭合。",
            "remaining": B3_EXTERNAL_MERTENS,
        },
        {
            "front": "B3 signed delay anchor",
            "closed": result["b3_anchor20000_budget_closed"],
            "proved": result["b3_anchor20000_budget_closed"],
            "effect": "锚点提升到 20000 后，delay-kernel BV 乘子预算小于 1% f(s)。",
            "remaining": "closed under external Mertens tail",
        },
        {
            "front": "strict self-contained B3 tail",
            "closed": result["b3_strict_self_contained_tail_closed"],
            "proved": result["b3_strict_self_contained_tail_closed"],
            "effect": "若坚持完全自足，不接受 Dusart/Rosser-Schoenfeld 外部定理，这一尾段仍未内联。",
            "remaining": B3_SELF_MERTENS,
        },
    ]


def terminal_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """列出终端正余量的真实剩余槽位。"""
    return [
        {
            "slot": "prefix lower bound",
            "closed": result["strict_prefix_demand_proved"],
            "effect_on_margin": "决定 D_prefix 是否能给出统一显式 D0(P,z)。",
            "remaining": FINITE_PREFIX,
        },
        {
            "slot": "named return deduction",
            "closed": result["named_return_exclusion_proved"],
            "effect_on_margin": "决定 E_named 是否可以被排斥或严格计入同参数预算。",
            "remaining": f"{NAMED_RETURN} via {PDEC_CLEAN} or unified budget",
        },
        {
            "slot": "hot/fixed terminal exits",
            "closed": result["hot_fixed_terminal_exits_closed"],
            "effect_on_margin": "决定热核心与固定历史是否会吞掉余量。",
            "remaining": f"{HOT_CORE} AND {FIXED_HISTORY}",
        },
        {
            "slot": "coupled positive margin",
            "closed": result["explicit_positive_terminal_budget_margin_proved"],
            "effect_on_margin": "需要在同一参数账本下证明 D0(P,z)-E0(P,z)-U0(P,z)>0。",
            "remaining": COUPLED_MARGIN,
        },
        {
            "slot": "independent promotion gate",
            "closed": result["dstructure_rankin_independently_accepted"],
            "effect_on_margin": "即使终端余量闭合，行/列定理仍需 DStructure/Rankin 独立验收晋级。",
            "remaining": DSTRUCTURE,
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本轮仍只在 Assume EarlyZeroRowWithinP 的反例链内压缩终端余量，不使用真实零行缺席。",
            "remaining": "保持 direct_unconditional_contradiction_found=false。",
        },
        {
            "gate": "B3ExternalFrontNoLongerPrimaryBlocker",
            "closed": result["b3_external_front_no_longer_primary_blocker"],
            "proved": False,
            "meaning": "若接受外部 Mertens/Dusart 或标准 beta-sieve，B3 离散误差/TV 前沿可条件接入终端余量。",
            "remaining": "严格自足仍需 SelfContainedDusartReciprocalPrimeProofAppendixXGe10372。",
        },
        {
            "gate": "FinitePrefixCertificateStillOpen",
            "closed": not result["finite_boundary_prefix_open"],
            "proved": not result["finite_boundary_prefix_open"],
            "meaning": "正余量不能只靠渐近主项；有限 P 边界必须有机器证书或严格手算证书。",
            "remaining": FINITE_PREFIX,
        },
        {
            "gate": "NamedReturnStillOpen",
            "closed": result["named_return_exclusion_proved"],
            "proved": result["named_return_exclusion_proved"],
            "meaning": "命名回流字母表已压缩，但持久 PDEC/CleanKLS 与非持久统一预算尚未同时排斥。",
            "remaining": NAMED_RETURN,
        },
        {
            "gate": "CoupledPositiveMarginStillOpen",
            "closed": result["explicit_positive_terminal_budget_margin_proved"],
            "proved": result["explicit_positive_terminal_budget_margin_proved"],
            "meaning": "终端矛盾的必要充分口仍是同参数 D_prefix-E_named-U_cold>0。",
            "remaining": COUPLED_MARGIN,
        },
        {
            "gate": "DStructureRankinPromotionStillOpen",
            "closed": result["dstructure_rankin_independently_accepted"],
            "proved": result["dstructure_rankin_independently_accepted"],
            "meaning": "Rankin 子账本已格式化并 pass-or-return，但独立晋级验收仍未接受。",
            "remaining": DSTRUCTURE,
        },
        {
            "gate": "DirectTerminalContradictionReached",
            "closed": result["direct_unconditional_contradiction_found"],
            "proved": result["direct_unconditional_contradiction_found"],
            "meaning": "当前还没有从反例链推出与真实结构链的终端直接矛盾。",
            "remaining": f"{COUPLED_MARGIN} AND {NAMED_RETURN} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 正终端预算余量主攻证书。"""
    margin = load_json(MONOGRAPH / "prime-matrix-strict-single-parameter-terminal-budget-margin-router.json")
    prefix = load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json")
    b3_tv = load_json(MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json")
    b3_anchor = load_json(MONOGRAPH / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json")
    b3_explicit = load_json(MONOGRAPH / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json")
    b3_self = load_json(MONOGRAPH / "prime-matrix-b3-self-contained-mertens-tail-router.json")
    named = load_json(MONOGRAPH / "prime-matrix-strict-named-return-exclusion-compression-router.json")
    dstructure = load_json(MONOGRAPH / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json")
    rankin = load_json(MONOGRAPH / "prime-matrix-full-rankin-ledger-inventory-router.json")

    continuous_beta = margin.get("continuous_beta_demand_closed") is True
    b3_anchor_closed = b3_anchor.get("b3_boundary_variation_one_percent_conditional_closed") is True
    b3_tv_external = b3_tv.get("b3_tv_budget_conditional_external_closed") is True
    b3_mertens_external = b3_explicit.get("explicit_prime_reciprocal_mertens_external_closed") is True
    b3_discrete_external_front = (
        b3_anchor.get("b3_discrete_prime_sum_uniform_error_conditional_closed") is True
        and b3_tv_external
        and b3_mertens_external
    )
    b3_self_closed = (
        b3_self.get("self_contained_mertens_tail_proved") is True
        or b3_anchor.get("self_contained_mertens_tail_proved") is True
    )
    prefix_closed = prefix.get("uniform_prefix_rough_count_lower_bound_proved") is True
    finite_prefix_closed = prefix.get("finite_boundary_prefix_rough_count_certificate_proved") is True
    named_excluded = named.get("named_return_exclusion_proved") is True
    hot_fixed_closed = named.get("persistent_named_return_excluded") is True and named.get("nonpersistent_named_return_excluded") is True
    rankin_subledger_closed = rankin.get("full_rankin_ledger_still_open_closed") is True
    dstructure_accepted = dstructure.get("promotion_package_independently_accepted") is True
    positive_margin = (
        margin.get("explicit_positive_terminal_budget_margin_proved") is True
        and prefix_closed
        and finite_prefix_closed
        and named_excluded
        and hot_fixed_closed
    )
    direct_contradiction = positive_margin and dstructure_accepted

    result = {
        "certificate_type": "prime_matrix_strict_positive_terminal_budget_margin_attack_router",
        "status": "positive_terminal_budget_attack_b3_external_front_closed_structural_margin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": POSITIVE_MARGIN,
        "continuous_beta_demand_closed": continuous_beta,
        "b3_anchor20000_budget_closed": b3_anchor_closed,
        "b3_tv_external_closed": b3_tv_external,
        "b3_mertens_external_closed": b3_mertens_external,
        "b3_discrete_external_front_closed": b3_discrete_external_front,
        "b3_external_front_no_longer_primary_blocker": b3_discrete_external_front,
        "b3_strict_self_contained_tail_closed": b3_self_closed,
        "strict_prefix_demand_proved": prefix_closed,
        "finite_boundary_prefix_open": not finite_prefix_closed,
        "named_return_exclusion_proved": named_excluded,
        "hot_fixed_terminal_exits_closed": hot_fixed_closed,
        "rankin_subledger_closed": rankin_subledger_closed,
        "dstructure_rankin_independently_accepted": dstructure_accepted,
        "explicit_positive_terminal_budget_margin_proved": positive_margin,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": direct_contradiction,
        "hardpoint_after_router_external_lane": (
            f"{COUPLED_MARGIN} AND {NAMED_RETURN} AND {DSTRUCTURE}"
        ),
        "hardpoint_after_router_strict_self_contained_lane": (
            f"{B3_SELF_MERTENS} AND {COUPLED_MARGIN} AND {NAMED_RETURN} AND {DSTRUCTURE}"
        ),
        "next_direct_attack_target": COUPLED_MARGIN,
        "parallel_attack_targets": [
            FINITE_PREFIX,
            NAMED_RETURN,
            HOT_CORE,
            FIXED_HISTORY,
            PDEC_CLEAN,
            DSTRUCTURE,
            B3_SELF_MERTENS,
        ],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮把 B3 外部条件前沿接入正终端预算余量：接受外部 Mertens/Dusart 或标准 beta-sieve 时，"
            "B3 离散误差和长度 P 总变差不再是最窄主阻塞；严格自足线仍缺 Mertens 尾段内联证明。"
            "真正终端口收缩为同参数耦合余量 D0(P,z)-E0(P,z)-U0(P,z)>0，并且必须同时处理有限 prefix "
            "证书、命名回流/热核心/固定历史出口和 DStructure/Rankin 独立晋级验收。当前仍未推出直接矛盾。"
        ),
    }
    result["b3_front_rows"] = b3_front_rows(result)
    result["terminal_rows"] = terminal_rows(result)
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 正终端预算余量主攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"b3_external_front_no_longer_primary_blocker={fmt_bool(result['b3_external_front_no_longer_primary_blocker'])}",
        f"b3_strict_self_contained_tail_closed={fmt_bool(result['b3_strict_self_contained_tail_closed'])}",
        f"strict_prefix_demand_proved={fmt_bool(result['strict_prefix_demand_proved'])}",
        f"finite_boundary_prefix_open={fmt_bool(result['finite_boundary_prefix_open'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"hot_fixed_terminal_exits_closed={fmt_bool(result['hot_fixed_terminal_exits_closed'])}",
        f"rankin_subledger_closed={fmt_bool(result['rankin_subledger_closed'])}",
        f"dstructure_rankin_independently_accepted={fmt_bool(result['dstructure_rankin_independently_accepted'])}",
        f"explicit_positive_terminal_budget_margin_proved={fmt_bool(result['explicit_positive_terminal_budget_margin_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. B3 前沿",
        "",
        "| front | closed | proved | effect | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["b3_front_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['front'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["effect"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 终端余量槽位",
            "",
            "正余量只能在同一参数账本下闭合：",
            "",
            "```text",
            "D0(P,z) - E0(P,z) - U0(P,z) > 0.",
            "```",
            "",
            "| slot | closed | effect_on_margin | remaining |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["terminal_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['slot'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    table_cell(row["effect_on_margin"]),
                    table_cell(row["remaining"]),
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
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 最新最窄点",
            "",
            "外部 B3 路线下：",
            "",
            "```text",
            result["hardpoint_after_router_external_lane"],
            "```",
            "",
            "严格自足路线下：",
            "",
            "```text",
            result["hardpoint_after_router_strict_self_contained_lane"],
            "```",
            "",
            "下一步不应回到真实零行直接证明，也不应重跑 psi runner；应直接攻 `FinitePrefixNamedReturnCoupledPositiveMarginLedger`，"
            "也就是把有限 prefix 证书、命名回流扣除和冷供给上界放进同一个参数表，证明严格正余量或暴露具体失败回流。",
            "",
            "审稿边界：本文件只更新终端余量的最窄硬点，不声明行/列命题无条件闭合。",
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
