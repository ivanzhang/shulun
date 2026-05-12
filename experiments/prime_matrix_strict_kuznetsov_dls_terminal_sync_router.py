#!/usr/bin/env python3
"""生成 strict Kuznetsov/DLS 终端同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_kuznetsov_dls_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json
  docs/monograph/prime-matrix-strict-kuznetsov-dls-terminal-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.md"

KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
NCBLK_ANTIATOM = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
STRICT_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
NONRECURSIVE_BREAKER = "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json",
    "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json",
    "prime-matrix-strict-self-contained-cycle-obstruction-router.json",
    "prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json",
    "prime-matrix-strict-global-terminal-scope-router.json",
    "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json",
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
    """记录证据文件哈希，便于复核。"""
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
    """同步最新 canonical-lock 与既有 KZ/DLS、NC-BLK 去重证据。"""
    canonical = load_json("prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json")
    windowed = load_json("prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    kz = load_json("prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json")
    ncblk = load_json("prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json")
    cycle = load_json("prime-matrix-strict-self-contained-cycle-obstruction-router.json")
    actual_source = load_json("prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json")
    global_scope = load_json("prime-matrix-strict-global-terminal-scope-router.json")
    rate_packet = load_json("prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json")
    dstruct = load_json("prime-matrix-strict-structured-ehpd-final-interface-audit-router.json")

    latest_kz_target_imported = canonical.get("next_primary_target") == KUZNETSOV_DLS
    windowed_reduced = windowed.get("strict_gap_after_router") == KUZNETSOV_DLS
    kz_abcd_closed = all(
        kz.get(key) is True
        for key in [
            "kz_a_smoothing_closed",
            "kz_b_trace_specialization_closed",
            "kz_c_bessel_decay_closed",
            "kz_d_spectral_large_sieve_closed",
        ]
    )
    kz_to_ncblk = kz.get("strict_gap_after_router") == NCBLK_ANTIATOM
    ncblk_not_terminal = ncblk.get("acyclic_ncblk_not_separate_terminal") is True
    ncblk_returns_terminal = (
        "GlobalPDECorSparseTerminalExclusion" in str(ncblk.get("terminal_gap_after_router", ""))
        and ncblk.get("row_column_unconditional_closed") is False
    )
    cycle_obstruction = (
        cycle.get("cycle_edges_closed") is True
        and cycle.get("current_internal_route_is_fixed_point") is True
    )
    source_sync_to_terminal = (
        actual_source.get("actual_source_antiatom_to_terminal_sync_boundary_closed") is True
        and actual_source.get("strict_terminal_family_proved") is False
    )
    terminal_scope_imported = (
        global_scope.get("strict_global_terminal_scope_boundary_closed") is True
        and global_scope.get("canonical_terminal_promotion_not_importable_for_strict_noncanonical") is True
    )
    rate_packet_open = rate_packet.get("rate_bearing_moving_atom_packet_exclusion_proved") is False
    dstructure_open = (
        dstruct.get("author_side_structured_interface_audit_closed") is True
        and dstruct.get("final_promotion_gate_accepted") is False
    )

    latest_basis_after_sync = (
        f"{SEED} AND {STRICT_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE}"
    )
    nonrecursive_breaker_basis = (
        f"{NONRECURSIVE_BREAKER} OR "
        "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR "
        "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
    )

    rows = [
        row(
            "LatestCanonicalLockKuznetsovTargetImported",
            latest_kz_target_imported,
            True,
            "最新 canonical-lock 直攻把 clean DLS 出口钉到自足 Kuznetsov/DLS 大筛原子。",
            KUZNETSOV_DLS,
        ),
        row(
            "WindowedDLSFormalLayerAlreadyReduced",
            windowed_reduced,
            True,
            "windowed DLS 的对象、相位、L2 范数和失败字母表已压尽，剩纯谱/dispersion 原子。",
            KUZNETSOV_DLS,
        ),
        row(
            "KZABCDInternalSpineClosed",
            kz_abcd_closed,
            True,
            "KZ-A 平滑、KZ-B trace formula、KZ-C Bessel 衰减、KZ-D 谱大筛脊柱已在既有文件中关闭。",
            "KZ-E well-factorable dispersion log-saving",
        ),
        row(
            "KZEReducedToAcyclicNCBLK",
            kz_to_ncblk,
            False,
            "KZ-E 不能由裸谱大筛自动给出；当前自足剩余转为 acyclic actual block 非集中/source anti-atom。",
            NCBLK_ANTIATOM,
        ),
        row(
            "AcyclicNCBLKNotIndependentTerminal",
            ncblk_not_terminal,
            True,
            "NC-BLK/source anti-atom 若失败，会物化为同 formal unit 的 exact (u,v) 大原子并接回 moving atom/global terminal。",
            "GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger",
        ),
        row(
            "KuznetsovRouteReturnsToTerminalFamily",
            ncblk_returns_terminal,
            False,
            "直接沿 KZ/DLS 继续下钻不会产生新矛盾，而是回到 strict acyclic 终端门和模型余量账本。",
            f"{STRICT_TERMINAL} AND {MODEL_LEDGER}",
        ),
        row(
            "InternalCycleObstructionImported",
            cycle_obstruction,
            True,
            "PDEC/CleanKLS -> KZ/NC-BLK -> source entropy/ExactUV -> alpha signed lift -> PDEC/CleanKLS 已被识别为固定点循环。",
            NONRECURSIVE_BREAKER,
        ),
        row(
            "ActualSourceLineSyncedBackToTerminal",
            source_sync_to_terminal,
            False,
            "actual-source 反原子、ExactUV 与 pair-mass 路线也已同步回 acyclic 终端家族，不能另开隐藏出口。",
            "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
        ),
        row(
            "StrictTerminalScopeStillNoncanonical",
            terminal_scope_imported,
            False,
            "canonical-source 终端闭合不能直接导入 strict acyclic noncanonical seed；仍需同对象终端家族证明。",
            STRICT_TERMINAL,
        ),
        row(
            "RatePacketAndModelLedgerStillOpen",
            rate_packet_open,
            False,
            "moving atom 终端包还需保留 log-power 速率，并与模型/DPRC 余量账本同口径闭合。",
            f"{MODEL_LEDGER} AND RatePreservationLedger_FOR_moving_atom_packet",
        ),
        row(
            "DStructurePromotionGateStillOpen",
            dstructure_open,
            False,
            "作者侧 Structured-EHPD 接口已审计，但最终 DStructure/Tail-log4/finite Rankin 晋级门尚未独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本同步把 KZ/DLS 出口攻到底并确认其回到终端循环；没有得到排除反例的无条件终端矛盾。",
            latest_basis_after_sync,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_kuznetsov_dls_terminal_sync_router",
        "status": "strict_kuznetsov_dls_route_attacked_to_terminal_cycle_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "latest_kuznetsov_target_imported": latest_kz_target_imported,
        "windowed_dls_formal_layer_reduced": windowed_reduced,
        "kz_abcd_internal_spine_closed": kz_abcd_closed,
        "kz_e_reduced_to_acyclic_ncblk": kz_to_ncblk,
        "acyclic_ncblk_not_independent_terminal": ncblk_not_terminal,
        "kuznetsov_route_returns_to_terminal_family": ncblk_returns_terminal,
        "internal_cycle_obstruction_imported": cycle_obstruction,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "acyclic_ncblk_actual_block_nonconcentration_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": KUZNETSOV_DLS,
        "terminal_gap_after_router": latest_basis_after_sync,
        "nonrecursive_breaker_basis": nonrecursive_breaker_basis,
        "next_primary_target": STRICT_TERMINAL,
        "next_parallel_targets": [
            MODEL_LEDGER,
            "RatePreservationLedger_FOR_moving_atom_packet",
            DSTRUCTURE,
            NONRECURSIVE_BREAKER,
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 canonical-lock 后留下的 `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks` "
            "直接接到既有 KZ-A--KZ-E、NC-BLK/source anti-atom 去重和终端循环障碍证书。结论是："
            "KZ/DLS 形式层已攻到底，但没有给出自足 log-saving 定理；KZ-E 转成 acyclic NC-BLK/source anti-atom，"
            "该对象失败又回到 moving atom/global terminal。因此 KZ/DLS 不是当前闭合出口，最新严格剩余回到 "
            "`AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn`、strict acyclic 终端家族、模型/DPRC 账本和 "
            "DStructure/Rankin 晋级门。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Kuznetsov/DLS 终端同步证书",
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
        f"kz_abcd_internal_spine_closed={fmt_bool(result['kz_abcd_internal_spine_closed'])}",
        f"kz_e_reduced_to_acyclic_ncblk={fmt_bool(result['kz_e_reduced_to_acyclic_ncblk'])}",
        f"acyclic_ncblk_not_independent_terminal={fmt_bool(result['acyclic_ncblk_not_independent_terminal'])}",
        f"kuznetsov_route_returns_to_terminal_family={fmt_bool(result['kuznetsov_route_returns_to_terminal_family'])}",
        f"self_contained_kuznetsov_dls_large_sieve_inequality_proved={fmt_bool(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved'])}",
        f"strict_acyclic_terminal_family_proved={fmt_bool(result['strict_acyclic_terminal_family_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
        "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks",
        "  -> KZ-A/B/C/D internal spine closed",
        "  -> KZ-E well-factorable dispersion log-saving",
        "  -> AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom",
        "  -> exact (u,v) large atom / moving atom if failure",
        "  -> GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger",
        "  -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        "```",
        "",
        "这一步关闭的是 KZ/DLS 出口的路由边界，不是证明自足 Kuznetsov/DLS 大筛不等式。",
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
            "非递归破环备用基：",
            "",
            "```text",
            result["nonrecursive_breaker_basis"],
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
            "审稿边界：不能把 KZ-A--KZ-D、NC-BLK 去重、外部 FullS-KLS/DI-BFI、或当前终端循环识别写成行/列命题无条件闭合。",
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
