#!/usr/bin/env python3
"""生成 strict acyclic 终端家族最新饱和同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_terminal_family_latest_saturation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json

输出：
  docs/monograph/prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json
  docs/monograph/prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.md"

STRICT_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
DIRECT_PDEC = "DirectAcyclicSameSetPDECCapDualCertificate"
DIRECT_CLEAN = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-family-attack-router.json",
    "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-self-contained-cycle-obstruction-router.json",
    "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json",
    "prime-matrix-pdec-cap-same-set-global-dual-router.json",
    "prime-matrix-strict-structured-ehpd-final-interface-audit-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录证据哈希。"""
    result = {"script": sha256(Path(__file__).resolve())}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
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
    """把三条终端手臂同步到最新饱和状态。"""
    kz_sync = load_json("prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json")
    terminal = load_json("prime-matrix-strict-acyclic-terminal-family-attack-router.json")
    canonical = load_json("prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json")
    direct_pdec = load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json")
    cycle = load_json("prime-matrix-strict-self-contained-cycle-obstruction-router.json")
    rate_packet = load_json("prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json")
    canonical_pdec = load_json("prime-matrix-pdec-cap-same-set-global-dual-router.json")
    dstruct = load_json("prime-matrix-strict-structured-ehpd-final-interface-audit-router.json")

    terminal_gate_active = kz_sync.get("next_primary_target") == STRICT_TERMINAL
    three_atom_split = (
        terminal.get("strict_acyclic_terminal_family_boundary_refined") is True
        and terminal.get("terminal_gap_after_router")
        == f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}"
    )
    canonical_scoped_only = (
        canonical.get("canonical_lock_direct_attack_boundary_closed") is True
        and canonical.get("canonical_equality_case_absorbed_scoped_only") is True
        and canonical.get("acyclic_terminal_canonical_lock_proved") is False
    )
    direct_pdec_scope_open = (
        direct_pdec.get("scope_audit_closed") is True
        and direct_pdec.get("acyclic_same_set_scope_match_proved") is False
        and direct_pdec.get("direct_acyclic_same_set_pdec_cap_dual_certificate_proved") is False
    )
    clean_kls_looped = (
        kz_sync.get("kuznetsov_route_returns_to_terminal_family") is True
        and kz_sync.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False
    )
    canonical_pdec_scoped = (
        canonical_pdec.get("canonical_source_self_contained_pdec_cap_closed") is True
        and canonical_pdec.get("row_column_unconditional_closed") is False
    )
    cycle_closed = (
        cycle.get("cycle_edges_closed") is True
        and cycle.get("current_internal_route_is_fixed_point") is True
    )
    rate_open = rate_packet.get("rate_bearing_moving_atom_packet_exclusion_proved") is False
    dstructure_open = (
        dstruct.get("author_side_structured_interface_audit_closed") is True
        and dstruct.get("final_promotion_gate_accepted") is False
    )

    latest_basis = (
        f"({NONRECURSIVE_BREAKER} OR {SCOPE_MATCH} OR "
        "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND "
        f"{MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    rows = [
        row(
            "StrictTerminalFamilyGateActive",
            terminal_gate_active,
            False,
            "上一 KZ/DLS 同步后，首攻点回到 strict acyclic noncanonical 终端家族。",
            STRICT_TERMINAL,
        ),
        row(
            "ThreeAtomSplitImported",
            three_atom_split,
            False,
            "终端家族已精确拆成 canonical-lock、direct same-set PDEC、direct CleanKLS/DLS 三手臂。",
            f"{CANONICAL_LOCK} OR {DIRECT_PDEC} OR {DIRECT_CLEAN}",
        ),
        row(
            "CanonicalLockArmAttackedButScoped",
            canonical_scoped_only,
            False,
            "canonical-lock 手臂已直接攻过；等式成立只给 scoped canonical 吸收，不给全局矛盾。",
            "mismatch exits OR direct PDEC OR clean DLS",
        ),
        row(
            "DirectPDECArmScopeAuditedButOpen",
            direct_pdec_scope_open,
            False,
            "direct PDEC 协议可导入，但 acyclic 证书与 canonical same-set 证书的 formal unit、坏窗集合和推前质量仍未证明同口径。",
            SCOPE_MATCH,
        ),
        row(
            "DirectCleanKLSArmReturnsToTerminal",
            clean_kls_looped,
            False,
            "CleanKLS/DLS 手臂经 windowed DLS、KZ-E 与 NC-BLK/source anti-atom 去重后回到 moving atom/global terminal。",
            f"{STRICT_TERMINAL} AND {MODEL_LEDGER}",
        ),
        row(
            "CanonicalPDECCapClosedOnlyInCanonicalSource",
            canonical_pdec_scoped,
            True,
            "canonical-source 同集 PDEC-CAP 已有闭合路线；但它不能自动导入 strict acyclic noncanonical seed。",
            SCOPE_MATCH,
        ),
        row(
            "InternalTerminalCycleObstructionClosed",
            cycle_closed,
            True,
            "PDEC/CleanKLS 终端门沿内部链条展开会回到自身；这排除伪出口，但不是反例矛盾。",
            NONRECURSIVE_BREAKER,
        ),
        row(
            "RateAndModelLedgersStillOpen",
            rate_open,
            False,
            "即使破开终端循环，还必须保持 moving atom packet 的速率并闭合模型/DPRC 余量账本。",
            f"{MODEL_LEDGER} AND {RATE_LEDGER}",
        ),
        row(
            "DStructurePromotionGateStillOpen",
            dstructure_open,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终独立晋级门，作者侧接口审计不能替代接受事件。",
            DSTRUCTURE,
        ),
        row(
            "StrictAcyclicTerminalFamilyCurrentCorpusProved",
            False,
            False,
            "三条手臂在当前语料下均未闭合；终端家族被攻成循环饱和状态。",
            latest_basis,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "还没有从早期零行反例链与真实结构链之间推出无条件终端矛盾。",
            latest_basis,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_terminal_family_latest_saturation_router",
        "status": "strict_acyclic_terminal_family_saturated_to_nonrecursive_breaker_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "strict_terminal_family_gate_active": terminal_gate_active,
        "three_atom_split_imported": three_atom_split,
        "canonical_lock_arm_attacked_but_scoped": canonical_scoped_only,
        "direct_pdec_scope_audited_but_open": direct_pdec_scope_open,
        "direct_clean_kls_returns_to_terminal": clean_kls_looped,
        "internal_terminal_cycle_obstruction_closed": cycle_closed,
        "strict_acyclic_terminal_family_proved": False,
        "nonrecursive_breaker_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": STRICT_TERMINAL,
        "terminal_gap_after_router": latest_basis,
        "next_primary_target": NONRECURSIVE_BREAKER,
        "next_parallel_targets": [
            SCOPE_MATCH,
            MODEL_LEDGER,
            RATE_LEDGER,
            DSTRUCTURE,
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 strict acyclic 终端家族的三条手臂同步到最新状态：canonical-lock 已被攻到 scoped canonical case，"
            "direct PDEC 已卡在 acyclic/canonical same-set 作用域匹配，direct CleanKLS/DLS 经 KZ-E/NC-BLK 去重回到 "
            "moving atom/global terminal。因而当前不是某一手臂还没展开，而是终端家族在内部语料中已经饱和为循环；"
            "要继续闭合，必须给出非递归 actual noncanonical pre-Cauchy constructor/signed-lift 破环包，或证明 direct PDEC "
            "同集作用域匹配，并同时保留模型/DPRC、RatePreservation 与 DStructure/Rankin 门。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic 终端家族最新饱和同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"three_atom_split_imported={fmt_bool(result['three_atom_split_imported'])}",
        f"canonical_lock_arm_attacked_but_scoped={fmt_bool(result['canonical_lock_arm_attacked_but_scoped'])}",
        f"direct_pdec_scope_audited_but_open={fmt_bool(result['direct_pdec_scope_audited_but_open'])}",
        f"direct_clean_kls_returns_to_terminal={fmt_bool(result['direct_clean_kls_returns_to_terminal'])}",
        f"strict_acyclic_terminal_family_proved={fmt_bool(result['strict_acyclic_terminal_family_proved'])}",
        f"nonrecursive_breaker_proved={fmt_bool(result['nonrecursive_breaker_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 三手臂状态",
        "",
        "```text",
        "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        "  -> AcyclicTerminalCanonicalLockToCanonicalSourceBoundary: attacked; scoped canonical only",
        "  -> DirectAcyclicSameSetPDECCapDualCertificate: protocol audited; scope match open",
        "  -> DirectAcyclicCleanKLSDLSEstimateWithNamedReturn: routes through KZ/NC-BLK back to terminal family",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "```",
            "",
            "## 4. 下一主攻点",
            "",
            f"首攻：`{result['next_primary_target']}`。",
            "",
            "并行保留：",
        ]
    )
    for target in result["next_parallel_targets"]:
        lines.append(f"- `{target}`。")

    lines.extend(
        [
            "",
            "审稿边界：本文件关闭的是终端家族三手臂的最新路由状态；它没有证明 nonrecursive breaker、direct PDEC scope match、模型余量、RatePreservation 或 DStructure 门。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
