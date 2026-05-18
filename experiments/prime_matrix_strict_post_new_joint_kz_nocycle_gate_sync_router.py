#!/usr/bin/env python3
"""生成 post-new-joint KZ 非循环门同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_new_joint_kz_nocycle_gate_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json

输出：
  data/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json
  docs/monograph/prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json",
    "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json",
    "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json",
    "prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json",
    "prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json",
    "prime-matrix-strict-global-terminal-scope-router.json",
]

KZ_NOCYCLE = "NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse"
KZ_ATOM = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
NCBLK = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
KZE_DIRECT = "AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection"
EXTERNAL_KLS = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录脚本与上游证书哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖，避免误把空输入当成证明。"""
    return [
        f"docs/monograph/{name}"
        for name in SOURCE_FILES
        if not (DOCS / name).exists()
    ]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步最新 KZ 非循环门与既有 KZ/NCBLK/source-root 路由。"""
    latest = data["latest"]
    windowed = data["windowed"]
    kz_atom = data["kz_atom"]
    kz_terminal = data["kz_terminal"]
    ncblk = data["ncblk"]
    source_root = data["source_root"]
    alpha_guard = data["alpha_guard"]
    global_scope = data["global_scope"]

    latest_kz_nocycle_active = (
        latest.get("next_direct_attack_target") == KZ_NOCYCLE
        and KZ_NOCYCLE in str(latest.get("strict_internal_basis_after_router", ""))
    )
    windowed_to_kz = (
        windowed.get("strict_gap_after_router") == KZ_ATOM
        or windowed.get("terminal_gap_before_router") == WINDOWED_DLS
    )
    kz_abcd_closed = all(
        kz_atom.get(key) is True
        for key in [
            "kz_a_smoothing_closed",
            "kz_b_trace_specialization_closed",
            "kz_c_bessel_decay_closed",
            "kz_d_spectral_large_sieve_closed",
        ]
    )
    kz_e_to_ncblk = (
        kz_atom.get("strict_gap_after_router") == NCBLK
        or kz_atom.get("kz_e_reduced_to_ncblk_or_external") is True
    )
    ncblk_returns_terminal = (
        ncblk.get("acyclic_ncblk_not_separate_terminal") is True
        and "GlobalPDECorSparseTerminalExclusion" in str(ncblk.get("terminal_gap_after_router", ""))
    )
    source_root_cycle = (
        source_root.get("forward_source_root_independent_after_router") is False
        and source_root.get("row_column_unconditional_closed") is False
    )
    terminal_cycle_guard = (
        alpha_guard.get("alpha_terminal_to_acyclic_cycle_guard_sync_router_closed") is True
        and alpha_guard.get("raw_direct_pdec_clean_routes_count_as_closure") is False
    )
    kz_terminal_returns = kz_terminal.get("kuznetsov_route_returns_to_terminal_family") is True
    global_scope_open = (
        global_scope.get("strict_global_terminal_scope_boundary_closed") is True
        and global_scope.get("strict_acyclic_terminal_family_proved") is False
    )

    return [
        row(
            "LatestKZNoCycleGateImported",
            latest_kz_nocycle_active,
            False,
            "post-new-joint 同步后，直接主攻点是不得复用 NCBLK/source-root 的非循环 KZ/DLS。",
            KZ_NOCYCLE,
        ),
        row(
            "WindowedDLSFormalLayerImported",
            windowed_to_kz,
            True,
            "windowed DLS 的对象、相位、L2 范数和失败字母表已压尽，剩 KZ/DLS 谱原子。",
            KZ_ATOM,
        ),
        row(
            "KZABCDSpineImported",
            kz_abcd_closed,
            True,
            "KZ-A 平滑、KZ-B trace formula、KZ-C Bessel 衰减、KZ-D 谱大筛脊柱已由既有证书关闭。",
            "KZ-E well-factorable dispersion log-saving",
        ),
        row(
            "ExistingKZERouteFactorsThroughNCBLK",
            kz_e_to_ncblk,
            False,
            "既有 KZ-E 路线把 log-saving 压到 NC-BLK/source anti-atom；这不是独立非循环谱证明。",
            NCBLK,
        ),
        row(
            "NCBLKProjectionForbiddenForNoCycleGate",
            kz_e_to_ncblk and source_root_cycle,
            True,
            "当前门名已经禁止复用 NCBLK/source-root；因此经 NC-BLK/source-root 的 KZ-E 证明不能计入本门闭合。",
            KZE_DIRECT,
        ),
        row(
            "NCBLKReturnToTerminalImported",
            ncblk_returns_terminal,
            True,
            "NC-BLK/source anti-atom 若失败，会物化为 moving atom 并回到 GlobalPDEC/sparse 终端与模型账本。",
            "GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger",
        ),
        row(
            "TerminalCycleGuardImported",
            terminal_cycle_guard,
            True,
            "裸 direct PDEC 与 direct CleanKLS 终端路线已识别为自回流，不能作为进展量。",
            "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate",
        ),
        row(
            "ExistingKZTerminalSyncImported",
            kz_terminal_returns,
            False,
            "直接沿现有 KZ/DLS 下钻只回到 strict acyclic 终端家族和模型余量账本。",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        ),
        row(
            "StrictGlobalTerminalScopeStillOpen",
            global_scope_open,
            False,
            "canonical-source 终端闭合不能直接导入 acyclic noncanonical seed。",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        ),
        row(
            "NonCircularKZCurrentInternalRouteSaturated",
            latest_kz_nocycle_active and kz_e_to_ncblk and source_root_cycle,
            False,
            "当前内部 KZ/DLS 旧路线不满足 no-NCBLK/source-root 限制；若要继续，必须直接证明 KZ-E log-saving。",
            KZE_DIRECT,
        ),
        row(
            "HighModelRateDStructureStillOpen",
            True,
            False,
            "KZ 门之外，高段模型、RatePreservation 与 DStructure/Rankin 仍是独立开放门。",
            f"{HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把非循环 KZ 门压到 KZ-E 直接 log-saving；没有得到无条件终端矛盾。",
            f"{KZE_DIRECT} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "latest": load_json("prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json"),
        "windowed": load_json("prime-matrix-strict-acyclic-windowed-dls-estimate-router.json"),
        "kz_atom": load_json("prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"),
        "kz_terminal": load_json("prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"),
        "ncblk": load_json("prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json"),
        "source_root": load_json("prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json"),
        "alpha_guard": load_json("prime-matrix-strict-alpha-terminal-to-acyclic-cycle-guard-sync-router.json"),
        "global_scope": load_json("prime-matrix-strict-global-terminal-scope-router.json"),
    }
    rows = build_rows(data)
    saturated = next(
        item["closed"] for item in rows if item["gate"] == "NonCircularKZCurrentInternalRouteSaturated"
    )
    strict_basis = f"{KZE_DIRECT} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    conditional_basis = f"({KZE_DIRECT} OR {EXTERNAL_KLS}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_post_new_joint_kz_nocycle_gate_sync_router",
        "status": "post_new_joint_kz_nocycle_gate_reduced_to_kze_direct_log_saving_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "latest_kz_nocycle_gate_active": rows[0]["closed"],
        "windowed_dls_formal_layer_imported": rows[1]["closed"],
        "kz_abcd_spine_imported": rows[2]["closed"],
        "existing_kz_e_route_factors_through_ncblk": rows[3]["closed"],
        "ncblk_projection_forbidden_for_nocycle_gate": rows[4]["closed"],
        "noncircular_kuznetsov_dls_without_source_root_reuse_proved": False,
        "kz_e_direct_log_saving_without_ncblk_projection_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": KZ_NOCYCLE,
        "strict_internal_basis_after_router": strict_basis,
        "conditional_external_basis_retained": conditional_basis,
        "next_direct_attack_target": KZE_DIRECT,
        "external_condition_target": EXTERNAL_KLS,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步继续攻击 post-new-joint 后的非循环 KZ/DLS 门。既有 windowed DLS 形式层和 "
            "KZ-A--KZ-D 谱脊柱已经可导入；但 KZ-E 的现有路线通过 NC-BLK/source anti-atom "
            "获得 log-saving，而该路线又回到 source-root/terminal cycle。由于当前门名要求 "
            "`without NCBLK/source-root reuse`，这条旧路线不能计入非循环证明。故当前内部 KZ "
            "路线已饱和，剩余被压成直接的 KZ-E well-factorable dispersion log-saving 证明，"
            "且不得经过 NC-BLK 投影；同时高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix strict post-new-joint KZ 非循环门同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_kz_nocycle_gate_active={fmt_bool(result['latest_kz_nocycle_gate_active'])}",
        f"windowed_dls_formal_layer_imported={fmt_bool(result['windowed_dls_formal_layer_imported'])}",
        f"kz_abcd_spine_imported={fmt_bool(result['kz_abcd_spine_imported'])}",
        f"existing_kz_e_route_factors_through_ncblk={fmt_bool(result['existing_kz_e_route_factors_through_ncblk'])}",
        f"ncblk_projection_forbidden_for_nocycle_gate={fmt_bool(result['ncblk_projection_forbidden_for_nocycle_gate'])}",
        (
            "noncircular_kuznetsov_dls_without_source_root_reuse_proved="
            f"{fmt_bool(result['noncircular_kuznetsov_dls_without_source_root_reuse_proved'])}"
        ),
        (
            "kz_e_direct_log_saving_without_ncblk_projection_proved="
            f"{fmt_bool(result['kz_e_direct_log_saving_without_ncblk_projection_proved'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["decision_rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )

    lines.extend([
        "",
        "## 2. 最新内部非循环基",
        "",
        "```text",
        result["strict_internal_basis_after_router"],
        "```",
        "",
        "条件外部线：",
        "",
        "```text",
        result["conditional_external_basis_retained"],
        "```",
        "",
        "下一直接主攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "## 3. 诚实边界",
        "",
        "- 本证书不证明 KZ-E log-saving，也不证明非循环 KZ/DLS。",
        "- 它只说明现有 KZ-E 经 NC-BLK/source-root 的路线不能满足 no-cycle 门。",
        "- 外部 DI/BFI/Kuznetsov 只能作为条件输入，不能冒充严格自足闭合。",
        "- 高段模型、RatePreservation 与 DStructure/Rankin 仍未闭合。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ])
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    if result["missing_sources"]:
        lines.extend(["", "缺失依赖："])
        for path in result["missing_sources"]:
            lines.append(f"- `{path}`")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、ledger 与 Markdown。"""
    result = build_result()
    write_json(OUT_LEDGER, result)
    write_json(OUT_JSON, result)
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
