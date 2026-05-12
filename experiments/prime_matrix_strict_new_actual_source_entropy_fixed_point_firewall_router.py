#!/usr/bin/env python3
"""生成 strict 新 actual-source 熵定理固定点防火墙证书。

用法示例：
  python3 experiments/prime_matrix_strict_new_actual_source_entropy_fixed_point_firewall_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json"
OUT_MD = DOCS / "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json",
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-independent-pair-energy-attack-router.json",
    "prime-matrix-strict-rate-bearing-large-pair-packet-router.json",
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
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
    entropy_firewall: dict[str, Any],
    direct_attack: dict[str, Any],
    nonrecursive_guard: dict[str, Any],
    pair_attack: dict[str, Any],
    packet_router: dict[str, Any],
    recurrence: dict[str, Any],
    canonical_absorb: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成固定点防火墙判定表。"""
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    independent = f"IndependentNonterminalProofOf{target}"
    return [
        {
            "gate": "NewActualSourceEntropyTargetActive",
            "closed": entropy_firewall.get("new_actual_source_entropy_theorem_proved")
            is False,
            "proved": False,
            "meaning": "exact entropy 源律防火墙已把 moving-atom 分支固定为同一个新 actual-source 熵定理目标。",
            "remaining": target,
        },
        {
            "gate": "DirectExactUVSpineConditionalOnly",
            "closed": direct_attack.get("support_to_entropy_conditional_inequality_closed")
            is True,
            "proved": False,
            "meaning": "登记容量乘子加 ExactUV 支撑下界可条件推出熵界，但 ExactUV/pair-mass 本身未证。",
            "remaining": direct_attack.get("next_direct_attack_target_inside_same_theorem"),
        },
        {
            "gate": "PairMassLoopRejected",
            "closed": nonrecursive_guard.get("nonrecursive_guard_closed") is True
            and nonrecursive_guard.get("circular_entropy_proof_rejected") is True,
            "proved": True,
            "meaning": "不能用 moving-atom 排斥或 exact entropy 反过来证明 pair-mass，否则构成同命题循环。",
            "remaining": "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed。",
        },
        {
            "gate": "SeedOnlyPairEnergyInsufficient",
            "closed": pair_attack.get("seed_only_insufficient_model_verified")
            is True,
            "proved": True,
            "meaning": "抽象 seed 允许质量集中在单个 exact pair；定性有限投影二分也不给任意 A 的 log-power 速率。",
            "remaining": "RateBearingLargePairAtomPacketExclusion。",
        },
        {
            "gate": "RateBearingPacketReturnsToTerminalGate",
            "closed": packet_router.get("rate_bearing_packet_split_closed") is True,
            "proved": False,
            "meaning": "大 pair packet 被分到 canonical payload、有限签名、sparse/ColumnCRT、clean residual 四类，但这些只是终端门入口。",
            "remaining": packet_router.get("internal_obligation_after_router"),
        },
        {
            "gate": "TerminalGateReturnsToSourceEntropy",
            "closed": recurrence.get("terminal_route_returns_to_source_entropy_target")
            is True,
            "proved": True,
            "meaning": "direct PDEC/direct CleanKLS 经过终端回流防火墙回到 canonical-lock 或原 actual-source 熵目标。",
            "remaining": recurrence.get("strict_self_contained_terminal_after_router"),
        },
        {
            "gate": "CanonicalBranchAbsorbed",
            "closed": canonical_absorb.get("canonical_lock_branch_absorption_closed")
            is True,
            "proved": True,
            "meaning": "canonical exact same-set 证书只作为 scoped canonical case；活动 noncanonical 主线仍回到原 source entropy。",
            "remaining": canonical_absorb.get(
                "strict_active_noncanonical_terminal_after_absorption"
            ),
        },
        {
            "gate": "CurrentInternalSpineFixedPointDetected",
            "closed": True,
            "proved": True,
            "meaning": "ExactUV/pair-energy/rate-bearing/terminal/canonical 这条现有内部脊柱形成 T -> ... -> T 固定点，不能作为 T 的证明。",
            "remaining": independent,
        },
        {
            "gate": "IndependentNonterminalSourceEntropyProofCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未给出不经过 pair-mass 失败回流和终端标签的独立 actual-source 熵估计。",
            "remaining": independent,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 新 actual-source 熵定理固定点防火墙证书。"""
    entropy_firewall = load_json(
        DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
    )
    direct_attack = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json"
    )
    nonrecursive_guard = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json"
    )
    pair_attack = load_json(
        DOCS / "prime-matrix-strict-independent-pair-energy-attack-router.json"
    )
    packet_router = load_json(
        DOCS / "prime-matrix-strict-rate-bearing-large-pair-packet-router.json"
    )
    recurrence = load_json(
        DOCS / "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"
    )
    canonical_absorb = load_json(
        DOCS / "prime-matrix-strict-canonical-lock-branch-absorption-router.json"
    )

    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    independent = f"IndependentNonterminalProofOf{target}"
    rows = build_rows(
        entropy_firewall=entropy_firewall,
        direct_attack=direct_attack,
        nonrecursive_guard=nonrecursive_guard,
        pair_attack=pair_attack,
        packet_router=packet_router,
        recurrence=recurrence,
        canonical_absorb=canonical_absorb,
    )
    return {
        "certificate_type": "prime_matrix_strict_new_actual_source_entropy_fixed_point_firewall_router",
        "status": "strict_new_actual_source_entropy_current_internal_spine_fixed_point_independent_nonterminal_proof_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "new_actual_source_entropy_fixed_point_firewall_closed": True,
        "current_exactuv_pair_packet_terminal_spine_rejected_as_proof": True,
        "all_current_internal_routes_to_source_entropy_are_recursive": True,
        "canonical_branch_absorbed_from_active_noncanonical_line": True,
        "independent_nonterminal_source_entropy_proof_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "fixed_point_chain": [
            target,
            "ExactUVSupportLowerBound + PairMassDispersion",
            "IndependentExactPairL2EnergyOrMaxAtomBound",
            "RateBearingLargePairAtomPacketExclusion",
            "TerminalGate: CanonicalLock OR DirectPDEC OR DirectCleanKLS",
            "TerminalRecurrenceFirewall",
            "CanonicalBranchAbsorption",
            target,
        ],
        "strict_active_noncanonical_terminal_after_router": independent,
        "next_direct_attack_target": independent,
        "hard_law": (
            "现有 ExactUV/pair-energy/rate-bearing/terminal/canonical 内部脊柱已经形成 "
            "`T -> ... -> T` 固定点；它能澄清边界和删掉伪出口，但不能证明 T。"
            "继续 strict 自足闭合必须给出不经 pair-mass 失败回流、不经 direct 终端标签、"
            "不经 canonical scoped case 的独立 actual-source 熵估计。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步检查原 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 的现有内部证明脊柱。"
            "ExactUV 支撑、pair-mass、独立 pair 能量、rate-bearing packet、终端三原子和 canonical-lock "
            "分支吸收串起来后回到同一个源熵目标，形成固定点。因此这条路径不能作为该定理的非递归证明；"
            "最新唯一 strict 自足主攻点是 `IndependentNonterminalProofOfNewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 新 actual-source 熵定理固定点防火墙路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"new_actual_source_entropy_fixed_point_firewall_closed={fmt_bool(result['new_actual_source_entropy_fixed_point_firewall_closed'])}",
        f"current_exactuv_pair_packet_terminal_spine_rejected_as_proof={fmt_bool(result['current_exactuv_pair_packet_terminal_spine_rejected_as_proof'])}",
        f"all_current_internal_routes_to_source_entropy_are_recursive={fmt_bool(result['all_current_internal_routes_to_source_entropy_are_recursive'])}",
        f"independent_nonterminal_source_entropy_proof_proved={fmt_bool(result['independent_nonterminal_source_entropy_proof_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定点链",
        "",
        "```text",
        *result["fixed_point_chain"],
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
