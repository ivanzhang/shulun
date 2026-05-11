#!/usr/bin/env python3
"""生成 strict rate-bearing packet 终端回流防火墙证书。

用法示例：
  python3 experiments/prime_matrix_strict_rate_bearing_terminal_recurrence_firewall_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"
OUT_MD = DOCS / "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-rate-bearing-large-pair-packet-router.json",
    "prime-matrix-strict-acyclic-terminal-cycle-guard-router.json",
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-noncanonical-legal-closure-mode-router.json",
    "prime-matrix-strict-source-admission-branch-absorption-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-acyclic-canonical-lock-router.json",
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
    packet: dict[str, Any],
    cycle: dict[str, Any],
    descent: dict[str, Any],
    leaf: dict[str, Any],
    noncanonical: dict[str, Any],
    source_absorb: dict[str, Any],
    entropy_firewall: dict[str, Any],
    canonical_lock: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成终端回流防火墙判定表。"""
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    canonical = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    return [
        {
            "gate": "RateBearingThreeAtomInputActive",
            "closed": packet.get("internal_obligation_after_router")
            == (
                "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
                "DirectAcyclicSameSetPDECCapDualCertificate OR "
                "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
            ),
            "proved": False,
            "meaning": "上一层把 rate-bearing 大 pair packet 压到 canonical-lock/direct PDEC/direct CleanKLS 三原子门。",
            "remaining": packet.get("internal_obligation_after_router"),
        },
        {
            "gate": "RawDirectPDECCleanCycleBlocked",
            "closed": cycle.get("terminal_family_self_return_detected") is True
            and cycle.get("raw_direct_pdec_clean_routes_count_as_closure") is False,
            "proved": True,
            "meaning": "裸 direct PDEC 与 direct CleanKLS 会形成 F -> ... -> F 自回流，不能当作闭合证明。",
            "remaining": cycle.get("terminal_gap_after_router"),
        },
        {
            "gate": "DescentSchemaImported",
            "closed": descent.get("terminal_return_well_founded_descent_schema_closed")
            is True,
            "proved": True,
            "meaning": "无隐藏终端循环已下降到叶子防火墙输入，但叶子输入本身未排斥。",
            "remaining": descent.get("terminal_gap_after_router"),
        },
        {
            "gate": "CurrentLeafInstanceReduced",
            "closed": leaf.get("current_leaf_firewall_active_basis_reduced") is True,
            "proved": True,
            "meaning": "当前已物化 PDEC/sparse 前沿为零；未来 schema 是准入纪律，当前活动叶子只剩 noncanonical 合法模式。",
            "remaining": leaf.get("terminal_gap_after_current_instance_router"),
        },
        {
            "gate": "NoncanonicalLegalModeReturnsToActualSource",
            "closed": noncanonical.get("actual_source_bridge_theorem_closed") is False
            and noncanonical.get("strict_self_contained_terminal_after_router")
            == f"{canonical} OR ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
            "proved": False,
            "meaning": "noncanonical 合法模式严格过滤后回到 actual-source 桥，不产生独立闭合。",
            "remaining": f"{canonical} OR ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
        },
        {
            "gate": "SourceAdmissionAbsorbed",
            "closed": source_absorb.get("source_admission_absorbed_from_active_or")
            is True,
            "proved": True,
            "meaning": "A1 source admission 只是分支陈述，不能作为独立 OR 终端；noncanonical 活动叶子仍是 moving atom/exact entropy。",
            "remaining": source_absorb.get("strict_self_contained_terminal_after_router"),
        },
        {
            "gate": "ExactEntropyFirewallReturnsToTarget",
            "closed": entropy_firewall.get("new_actual_source_entropy_theorem_proved")
            is False
            and entropy_firewall.get("strict_self_contained_terminal_after_router")
            == f"{canonical} OR {target}",
            "proved": False,
            "meaning": "moving atom/exact entropy 分支经防火墙精确回到同一个新 actual-source 熵定理目标。",
            "remaining": f"{canonical} OR {target}",
        },
        {
            "gate": "TerminalRouteIsRecurrenceNotProof",
            "closed": True,
            "proved": True,
            "meaning": "rate-bearing packet 的 direct-terminal 路线最终回到 canonical-lock 或原源熵目标；不能作为该目标的非递归证明。",
            "remaining": f"{canonical} OR NonrecursiveIndependentProofOf{target}",
        },
        {
            "gate": "CanonicalLockSubatomsStillOpen",
            "closed": canonical_lock.get("acyclic_terminal_canonical_lock_proved")
            is False,
            "proved": False,
            "meaning": "唯一当前非递归 strict 出口是完成 canonical-lock 三子原子，或给出全新不经终端回流的源熵证明。",
            "remaining": "AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND TerminalCertificateSameSetPushforwardIdentity AND NoNoncanonicalPayloadSurvivesCanonicalProjection",
        },
        {
            "gate": "NewActualSourceEntropyCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "终端回流被识别为循环后，新 actual-source 熵定理仍未证明。",
            "remaining": target,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict rate-bearing packet 终端回流防火墙证书。"""
    packet = load_json(DOCS / "prime-matrix-strict-rate-bearing-large-pair-packet-router.json")
    cycle = load_json(DOCS / "prime-matrix-strict-acyclic-terminal-cycle-guard-router.json")
    descent = load_json(DOCS / "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json")
    leaf = load_json(DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json")
    noncanonical = load_json(DOCS / "prime-matrix-strict-noncanonical-legal-closure-mode-router.json")
    source_absorb = load_json(DOCS / "prime-matrix-strict-source-admission-branch-absorption-router.json")
    entropy_firewall = load_json(DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json")
    canonical_lock = load_json(DOCS / "prime-matrix-strict-acyclic-canonical-lock-router.json")

    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    canonical = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    rows = build_rows(
        packet=packet,
        cycle=cycle,
        descent=descent,
        leaf=leaf,
        noncanonical=noncanonical,
        source_absorb=source_absorb,
        entropy_firewall=entropy_firewall,
        canonical_lock=canonical_lock,
    )
    return {
        "certificate_type": "prime_matrix_strict_rate_bearing_terminal_recurrence_firewall_router",
        "status": "strict_rate_bearing_terminal_route_recurrence_detected_canonical_lock_or_new_independent_source_entropy_open",
        "same_theorem_target_preserved": True,
        "terminal_recurrence_firewall_closed": True,
        "raw_direct_terminal_routes_rejected_as_closure": True,
        "terminal_route_returns_to_source_entropy_target": True,
        "acyclic_terminal_canonical_lock_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "recurrence_chain": [
            "RateBearingLargePairAtomPacketExclusion",
            "AcyclicTerminalCanonicalLock OR DirectPDEC OR DirectCleanKLS",
            "CycleGuard: AcyclicTerminalCanonicalLock OR WellFoundedDescent",
            "DescentFirewall: AcyclicTerminalCanonicalLock OR TerminalLeafFirewallInputs",
            "CurrentLeaf: AcyclicTerminalCanonicalLock OR NoncanonicalFullSComplementLegalClosureMode",
            "NoncanonicalLegalMode: AcyclicTerminalCanonicalLock OR ActualA1FullSSourceLockOrStrengthenedAntiAtom",
            "SourceAdmissionAbsorption: AcyclicTerminalCanonicalLock OR ActualNoncanonicalCleanCoreMovingAtomExclusion",
            "ExactEntropyFirewall: AcyclicTerminalCanonicalLock OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem",
        ],
        "strict_self_contained_terminal_after_router": f"{canonical} OR {target}",
        "nonrecursive_strict_open_exit": (
            "AcyclicSeedCanonicalSourceFiniteFactorEmbedding AND "
            "TerminalCertificateSameSetPushforwardIdentity AND "
            "NoNoncanonicalPayloadSurvivesCanonicalProjection"
        ),
        "alternative_open_exit": f"NonrecursiveIndependentProofOf{target}",
        "next_direct_attack_target": "AcyclicTerminalCanonicalLockSubatoms_OR_NewIndependentSourceEntropyProof",
        "hard_law": (
            "rate-bearing packet 经终端三原子、下降防火墙和 noncanonical 过滤后，"
            "回到 `AcyclicTerminalCanonicalLock OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。"
            "因此 direct PDEC/CleanKLS 标签链不能证明该源熵目标；要继续无循环推进，必须证明 canonical-lock "
            "三子原子，或给出完全独立、不经终端回流的 actual-source 熵证明。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "继续深挖后，rate-bearing 大 pair packet 的终端三原子路线被证明不是闭合证明，而是回流链："
            "direct PDEC/direct CleanKLS 经循环守卫、下降防火墙、当前叶子压缩、noncanonical 合法模式过滤、"
            "source-admission 吸收和 exact entropy 防火墙，最终又回到 "
            "`AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。"
            "所以不能再把三原子终端标签当作进展本身。当前非循环 strict 出口只剩完成 canonical-lock "
            "三子原子，或给出不经该终端回流链的独立 actual-source 熵证明。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict rate-bearing 终端回流防火墙路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"terminal_recurrence_firewall_closed={fmt_bool(result['terminal_recurrence_firewall_closed'])}",
        f"terminal_route_returns_to_source_entropy_target={fmt_bool(result['terminal_route_returns_to_source_entropy_target'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 回流链",
        "",
        "```text",
    ]
    for item in result["recurrence_chain"]:
        lines.append(f"{item}")
        if item != result["recurrence_chain"][-1]:
            lines.append("  ->")
    lines.extend(
        [
            "```",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
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
            "## 3. 非循环出口",
            "",
            "当前 strict 终端仍是：",
            "",
            "```text",
            result["strict_self_contained_terminal_after_router"],
            "```",
            "",
            "可继续硬攻的非循环 canonical-lock 子原子：",
            "",
            "```text",
            result["nonrecursive_strict_open_exit"],
            "```",
            "",
            "或者必须给出全新的独立源熵证明：",
            "",
            "```text",
            result["alternative_open_exit"],
            "```",
            "",
            "## 4. 硬边界律",
            "",
            result["hard_law"],
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
