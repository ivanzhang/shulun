#!/usr/bin/env python3
"""生成 strict 独立非终端 source entropy 原子化证书。

用法示例：
  python3 experiments/prime_matrix_strict_independent_nonterminal_source_entropy_atomization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json"
OUT_MD = DOCS / "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json",
    "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-noncanonical-source-core-atomization-router.json",
    "prime-matrix-fulls-kls-movingblock-joint-attack-router.json",
    "prime-matrix-unconditional-closure-final-attempt-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(
    fixed_point: dict[str, Any],
    direct_attack: dict[str, Any],
    entropy_firewall: dict[str, Any],
    source_core: dict[str, Any],
    joint_attack: dict[str, Any],
    final_attempt: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成独立非终端 source entropy 原子化判定表。"""
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    atom = "PreTerminalActualFullSFactorSupportCapacityTheorem"
    return [
        {
            "gate": "IndependentNonterminalTargetActive",
            "closed": fixed_point.get("new_actual_source_entropy_fixed_point_firewall_closed")
            is True,
            "proved": False,
            "meaning": "上一层已删除 ExactUV/pair/terminal 固定点证明脊柱，留下独立非终端证明目标。",
            "remaining": fixed_point.get("next_direct_attack_target"),
        },
        {
            "gate": "SameTheoremEntropyNormalFormPreserved",
            "closed": direct_attack.get("support_to_entropy_conditional_inequality_closed")
            is True
            and entropy_firewall.get("new_actual_source_entropy_theorem_proved")
            is False,
            "proved": False,
            "meaning": "仍证明同一 source entropy 定理；只允许使用源侧支撑/容量估计加登记容量乘子纪律。",
            "remaining": target,
        },
        {
            "gate": "OldNoncanonicalCoreAligned",
            "closed": source_core.get("source_core_atomization_closed") is True
            and source_core.get("actual_support_capacity_core_proved") is False,
            "proved": False,
            "meaning": "旧 noncanonical 源核心已把 entropy/anti-atom 二义性压成 actual 支撑/容量核心。",
            "remaining": source_core.get("atomized_self_contained_basis"),
        },
        {
            "gate": "MovingBlockJointAttackAligned",
            "closed": joint_attack.get("joint_attack_boundary_closed") is True,
            "proved": False,
            "meaning": "moving-block 内部路与 Full-S KLS 外部路已对齐；strict 自足线只能走内部 exact support/capacity。",
            "remaining": "FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource",
        },
        {
            "gate": "ExternalLaneNotUsedForStrictSelfContainedProof",
            "closed": final_attempt.get("external_math_match_found_in_current_corpus")
            is False,
            "proved": True,
            "meaning": "外部 dispersion/KLS 仍可作条件路线，但不能用于 strict 自足证明当前非终端目标。",
            "remaining": "internal support/capacity atom only。",
        },
        {
            "gate": "BalancedRangeAlreadyRemoved",
            "closed": source_core.get("balanced_range_threshold_closed") is True,
            "proved": True,
            "meaning": "balanced range 阈值不再是活动障碍；剩余必须直接控制 actual exact factor support 和容量兼容。",
            "remaining": atom,
        },
        {
            "gate": "K4K6IncidenceCanonicalShortcutsRejected",
            "closed": source_core.get("k4_k6_or_naive_incidence_suffices") is False
            and source_core.get("canonical_import_allowed") is False,
            "proved": True,
            "meaning": "K4/K6、朴素 incidence、canonical 支撑偷渡均不能证明 moving same-(u,v) 源熵。",
            "remaining": atom,
        },
        {
            "gate": "IndependentNonterminalAtomPinned",
            "closed": True,
            "proved": False,
            "meaning": "独立非终端证明等价压成 pre-terminal actual full-S 因子支撑/容量定理。",
            "remaining": atom,
        },
        {
            "gate": "PreTerminalActualFullSFactorSupportCapacityCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未证明该源侧支撑/容量定理，因此不能升级为 source entropy 或行/列无条件闭合。",
            "remaining": atom,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 独立非终端 source entropy 原子化证书。"""
    fixed_point = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json"
    )
    direct_attack = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json"
    )
    entropy_firewall = load_json(
        DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
    )
    source_core = load_json(
        DOCS / "prime-matrix-noncanonical-source-core-atomization-router.json"
    )
    joint_attack = load_json(
        DOCS / "prime-matrix-fulls-kls-movingblock-joint-attack-router.json"
    )
    final_attempt = load_json(
        DOCS / "prime-matrix-unconditional-closure-final-attempt-router.json"
    )

    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    atom = "PreTerminalActualFullSFactorSupportCapacityTheorem"
    rows = build_rows(
        fixed_point=fixed_point,
        direct_attack=direct_attack,
        entropy_firewall=entropy_firewall,
        source_core=source_core,
        joint_attack=joint_attack,
        final_attempt=final_attempt,
    )
    return {
        "certificate_type": "prime_matrix_strict_independent_nonterminal_source_entropy_atomization_router",
        "status": "strict_independent_nonterminal_source_entropy_atomized_to_preterminal_support_capacity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "independent_nonterminal_atomization_closed": True,
        "fixed_point_spine_rejected_as_proof": True,
        "external_lane_excluded_from_strict_self_contained_line": True,
        "balanced_range_threshold_closed": True,
        "preterminal_actual_fulls_factor_support_capacity_proved": False,
        "independent_nonterminal_source_entropy_proof_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "source_entropy_target": target,
        "atomized_internal_equivalent_target": atom,
        "conditional_implication": (
            f"{atom} AND RegisteredCapacityMultiplierDiscipline "
            f"=> {target}"
        ),
        "strict_active_nonterminal_obligation_after_router": atom,
        "next_direct_attack_target": atom,
        "hard_law": (
            "独立非终端 source entropy 证明不能再经 ExactUV/pair-mass 失败、终端三原子或 canonical scoped case。"
            "在当前语料中，它与 actual noncanonical full-S 的 pre-terminal 因子支撑/容量定理同义："
            "对每个幸存 formal unit，直接证明 exact (u,v) 支撑下界与 Type/Fourier 容量兼容。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步没有换命题，而是把 `IndependentNonterminalProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` "
            "压成同一命题内部的唯一非终端源侧原子：`PreTerminalActualFullSFactorSupportCapacityTheorem`。"
            "balanced range 已关闭；K4/K6、朴素 incidence、canonical 偷渡和外部 KLS 都不能作为 strict 自足证明。"
            "该原子尚未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 独立非终端 source entropy 原子化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"independent_nonterminal_atomization_closed={fmt_bool(result['independent_nonterminal_atomization_closed'])}",
        f"fixed_point_spine_rejected_as_proof={fmt_bool(result['fixed_point_spine_rejected_as_proof'])}",
        f"external_lane_excluded_from_strict_self_contained_line={fmt_bool(result['external_lane_excluded_from_strict_self_contained_line'])}",
        f"preterminal_actual_fulls_factor_support_capacity_proved={fmt_bool(result['preterminal_actual_fulls_factor_support_capacity_proved'])}",
        f"independent_nonterminal_source_entropy_proof_proved={fmt_bool(result['independent_nonterminal_source_entropy_proof_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同命题原子化",
        "",
        "目标仍是：",
        "",
        "```text",
        result["source_entropy_target"],
        "```",
        "",
        "非终端内部原子为：",
        "",
        "```text",
        result["atomized_internal_equivalent_target"],
        "```",
        "",
        "条件推出式：",
        "",
        "```text",
        result["conditional_implication"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 结构结论",
            "",
            result["hard_law"],
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
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
