#!/usr/bin/env python3
"""生成 strict 反例链/真实链终端矛盾硬攻判定证书。

用法示例：
  python3 experiments/prime_matrix_strict_terminal_contradiction_hard_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-terminal-contradiction-hard-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-terminal-contradiction-hard-attack-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-terminal-contradiction-hard-attack-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.json",
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.json",
    MONOGRAPH / "prime-matrix-strict-block-coprime-dynamics-capacity-surplus-router.json",
    MONOGRAPH / "prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.json",
    MONOGRAPH / "prime-matrix-eda-diagonal-final-hardcore-boundary.md",
    MONOGRAPH / "claim-status-table.md",
]

STABLE_RETURN = "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect"
ALPHA_LOAD = "AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity"
ALPHA_TV_DEFECT = "AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def hard_attack_findings() -> list[dict[str, str]]:
    """列出本次终端硬攻得到的结构判定。"""
    return [
        {
            "point": "CRT_short_stable_return",
            "result": "closed_conditional_contradiction",
            "content": (
                "同一 formal unit 若保留同一素标签集 Q 并在行位移 Delta 短复现，"
                "则每个 q in Q 都整除 Delta；若 0<|Delta|<prod(Q)，立即矛盾。"
            ),
        },
        {
            "point": "mirror_symmetry",
            "result": "not_a_short_return_forcer",
            "content": (
                "完整 CRT 周期镜像只给出远端伴随零行，不把一个 P 行以内零行自动送回同一短窗口；"
                "因此镜像对称本身不能作为终端矛盾。"
            ),
        },
        {
            "point": "adjacent_quotient_coprime",
            "result": "closed_rigidity_not_enough",
            "content": (
                "相邻整数互质、商相邻互质和大标签短距不可复用均已闭合；"
                "但这些只给容量上界，不给强制负载下界。"
            ),
        },
        {
            "point": "alpha_capacity_surplus",
            "result": "closed_direct_criterion",
            "content": (
                "对 alpha>1/2，早期零行迫使 alpha P-rough 位置数不超过 "
                "2(pi(P)-pi(alpha P))；若粗洞负载超过该容量，即得直接矛盾。"
            ),
        },
        {
            "point": "capacity_failure_defect",
            "result": "closed_dichotomy",
            "content": (
                "若容量反超没有发生，则反例必须支付 "
                "TV_alpha >= (P-1)W^-_alpha-2(pi(P)-pi(alpha P)) 的强端点/总变差缺陷。"
            ),
        },
        {
            "point": "terminal_blocker",
            "result": "open",
            "content": (
                "当前材料仍未证明 AlphaPrefixRoughLoadLowerBound，"
                "也未全局排斥 AlphaPrefixTotalVariationOrEndpointPDECDefect。"
            ),
        },
    ]


def theorem_boundary() -> list[dict[str, Any]]:
    """给出可审查定理边界。"""
    return [
        {
            "name": "TerminalContradictionConditionalTheorem",
            "proved": True,
            "statement": (
                "若存在 alpha>1/2，使每个假设早期零行都满足 "
                "(P-1)W^-_alpha-TV_alpha > 2(pi(P)-pi(alpha P))，"
                "则该早期零行不存在。"
            ),
            "role": "这是反例链与真实容量链之间已经闭合的条件矛盾定理。",
        },
        {
            "name": "StableReturnConditionalTheorem",
            "proved": True,
            "statement": (
                "若早期零行强制同 formal unit、同标签集 Q 的非零短行位移复现，"
                "且 |Delta|<prod(Q)，则早期零行不存在。"
            ),
            "role": "这是短复现路线已经闭合的条件矛盾定理。",
        },
        {
            "name": "UnconditionalEarlyZeroExclusion",
            "proved": False,
            "statement": (
                "要升级为无条件排斥，必须证明早期零行必触发上述两个条件之一，"
                "或证明不触发时的 PDEC/SAE/ColumnCRT 缺陷全局不可存在。"
            ),
            "role": "这是作者侧尚未完成的真正终端输入。",
        },
    ]


def decision_rows(
    cycle_cut: dict[str, Any],
    stable_return: dict[str, Any],
    unified: dict[str, Any],
    block_capacity: dict[str, Any],
    alpha_defect: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成终端硬攻判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "全程只在假设早期零行反例链内推导，不用真实缺席替代证明。",
            "remaining": "无。",
        },
        {
            "gate": "ShortStableReturnContradictionClosed",
            "closed": cycle_cut.get("short_same_label_recurrence_contradiction_lemma_proved") is True
            or cycle_cut.get("crt_short_recurrence_contradiction_imported") is True
            or stable_return.get("crt_short_recurrence_contradiction_imported") is True,
            "proved": True,
            "meaning": "短稳定同标签复现一旦被强制，CRT 整除给出直接矛盾。",
            "remaining": STABLE_RETURN,
        },
        {
            "gate": "EarlyZeroForcesStableReturnCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "镜像、P 列锚、斜线覆盖和类型记录尚未推出必然短复现；类型压缩仍缺。",
            "remaining": stable_return.get("next_direct_attack_target", STABLE_RETURN),
        },
        {
            "gate": "UnifiedCoprimeCapacityFieldClosed",
            "closed": unified.get("adjacent_coprime_dynamics_closed") is True
            and unified.get("block_capacity_envelope_closed") is True,
            "proved": True,
            "meaning": "相邻互质、商互质、短距标签不可复用和块容量上界均已进入统一矛盾场。",
            "remaining": ALPHA_LOAD,
        },
        {
            "gate": "CapacitySurplusContradictionCriterionClosed",
            "closed": block_capacity.get("direct_capacity_surplus_contradiction_criterion_closed") is True,
            "proved": True,
            "meaning": "若 alphaP-rough 负载超过高标签容量，早期零行直接矛盾。",
            "remaining": ALPHA_LOAD,
        },
        {
            "gate": "CapacityFailureToDefectDichotomyClosed",
            "closed": alpha_defect.get("capacity_failure_to_tv_defect_implication_closed") is True,
            "proved": True,
            "meaning": "若不能容量反超，则必须出现强 TV/端点/PDEC 缺陷。",
            "remaining": ALPHA_TV_DEFECT,
        },
        {
            "gate": "TerminalUnconditionalContradictionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明负载反超，也未排斥强端点缺陷；因此作者侧无条件闭合未达成。",
            "remaining": f"({ALPHA_LOAD} OR {ALPHA_TV_DEFECT}) AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造终端硬攻判定证书。"""
    cycle_cut = load_json(MONOGRAPH / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json")
    stable_return = load_json(MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.json")
    unified = load_json(MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.json")
    block_capacity = load_json(MONOGRAPH / "prime-matrix-strict-block-coprime-dynamics-capacity-surplus-router.json")
    alpha_defect = load_json(MONOGRAPH / "prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.json")
    rows = decision_rows(cycle_cut, stable_return, unified, block_capacity, alpha_defect)
    return {
        "certificate_type": "prime_matrix_strict_terminal_contradiction_hard_attack_router",
        "status": "terminal_contradiction_reduced_to_alpha_rough_load_or_pdec_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "short_stable_return_conditional_contradiction_closed": True,
        "capacity_surplus_conditional_contradiction_closed": True,
        "capacity_failure_to_defect_dichotomy_closed": True,
        "early_zero_forces_stable_return_proved": False,
        "alpha_prefix_rough_load_lower_bound_proved": False,
        "alpha_prefix_tv_or_pdec_defect_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ALPHA_TV_DEFECT,
        "parallel_attack_target": ALPHA_LOAD,
        "referee_gate": DSTRUCTURE,
        "hard_attack_findings": hard_attack_findings(),
        "theorem_boundary": theorem_boundary(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本次终端硬攻把反例链与真实结构链之间的可用矛盾压到两个已闭合条件定理："
            "短稳定同标签复现会被 CRT 整除立即击败；alpha>1/2 的粗洞负载若超过高标签容量也会立即击败。"
            "但当前材料没有证明早期零行必然产生短稳定复现，也没有证明 alpha 粗洞负载必然反超容量。"
            "若容量不反超，反例必须产生强 TV/端点/PDEC 缺陷；该缺陷尚未全局排斥。"
            "因此行/列命题仍不能标为作者侧无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 反例链/真实链终端矛盾硬攻判定",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"short_stable_return_conditional_contradiction_closed={fmt_bool(result['short_stable_return_conditional_contradiction_closed'])}",
        f"capacity_surplus_conditional_contradiction_closed={fmt_bool(result['capacity_surplus_conditional_contradiction_closed'])}",
        f"capacity_failure_to_defect_dichotomy_closed={fmt_bool(result['capacity_failure_to_defect_dichotomy_closed'])}",
        f"early_zero_forces_stable_return_proved={fmt_bool(result['early_zero_forces_stable_return_proved'])}",
        f"alpha_prefix_rough_load_lower_bound_proved={fmt_bool(result['alpha_prefix_rough_load_lower_bound_proved'])}",
        f"alpha_prefix_tv_or_pdec_defect_excluded={fmt_bool(result['alpha_prefix_tv_or_pdec_defect_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 硬攻结论",
        "",
        "| point | result | content |",
        "| --- | --- | --- |",
    ]
    for row in result["hard_attack_findings"]:
        lines.append(
            "| `{point}` | `{result}` | {content} |".format(
                point=table_cell(row["point"]),
                result=table_cell(row["result"]),
                content=table_cell(row["content"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 定理边界",
            "",
            "| name | proved | statement | role |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["theorem_boundary"]:
        lines.append(
            "| `{name}` | `{proved}` | {statement} | {role} |".format(
                name=table_cell(row["name"]),
                proved=fmt_bool(row["proved"]),
                statement=table_cell(row["statement"]),
                role=table_cell(row["role"]),
            )
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
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
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
            result["parallel_attack_target"],
            "```",
            "",
            "独立晋级门仍保留：",
            "",
            "```text",
            result["referee_gate"],
            "```",
            "",
            "审稿边界：本文件闭合的是两个条件矛盾定理和二择缺陷公式；没有证明开放输入本身，因此不能把全局行/列命题升级为无条件定理。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
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
