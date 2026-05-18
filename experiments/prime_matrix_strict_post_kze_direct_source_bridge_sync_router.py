#!/usr/bin/env python3
"""生成 post-KZ-E direct source-bridge 同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_kze_direct_source_bridge_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json

输出：
  data/prime-matrix-strict-post-kze-direct-source-bridge-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json
  docs/monograph/prime-matrix-strict-post-kze-direct-source-bridge-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-kze-direct-source-bridge-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-kze-direct-source-bridge-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-kze-direct-source-bridge-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json",
    "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md",
    "prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json",
    "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json",
    "prime-matrix-triad-a1-source-lock-contract-router.json",
    "prime-matrix-triad-a1-branch-statement-coverage-router.json",
    "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json",
    "prime-matrix-actual-source-bridge-global-reconciliation-router.json",
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
]

KZE_DIRECT = "AcyclicKZEWellFactorableDispersionLogSavingWithoutNCBLKProjection"
SOURCE_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
NONCANONICAL_MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
EXTERNAL_KLS = "ExactExternalDIBFIKuznetsovNoProjectionCertificate_FOR_NONCIRCULAR_KZ_ONLY"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(name: str) -> str:
    """读取文本证据；缺失时返回空串。"""
    path = DOCS / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本与上游证据哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
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


def build_rows(data: dict[str, dict[str, Any] | str]) -> list[dict[str, Any]]:
    """把 KZ-E direct gate 同步到 actual-source bridge。"""
    latest = data["latest"]
    taxonomy = data["taxonomy"]
    provenance = data["provenance"]
    source_lock = data["source_lock"]
    branch = data["branch"]
    obstruction = data["obstruction"]
    global_bridge = data["global_bridge"]
    rate_firewall = data["rate_firewall"]
    kze_spine = str(data["kze_spine"])

    assert isinstance(latest, dict)
    assert isinstance(taxonomy, dict)
    assert isinstance(provenance, dict)
    assert isinstance(source_lock, dict)
    assert isinstance(branch, dict)
    assert isinstance(obstruction, dict)
    assert isinstance(global_bridge, dict)
    assert isinstance(rate_firewall, dict)

    kze_direct_active = (
        latest.get("next_direct_attack_target") == KZE_DIRECT
        and KZE_DIRECT in str(latest.get("strict_internal_basis_after_router", ""))
    )
    kze_spine_reaches_wfd = (
        "WFD-core" in kze_spine
        and "当前真正" in kze_spine
        and "NC-BLK" in kze_spine
    )
    taxonomy_closed = (
        taxonomy.get("canonical_restricted_self_contained_version_closed") is True
        and taxonomy.get("generic_self_contained_version_refuted") is True
        and taxonomy.get("actual_source_bridge_theorem_closed") is False
    )
    provenance_closed_for_canonical = (
        provenance.get("actual_source_provenance_closed") is True
        and provenance.get("original_source_definition_declares_canonical") is True
        and provenance.get("pre_cauchy_lambda_equality_closed") is True
    )
    source_lock_scoped = (
        source_lock.get("source_lock_contract_closed_for_canonical_branch") is True
        and source_lock.get("global_internal_a1_closed") is False
        and source_lock.get("next_internal_target") == SOURCE_ADMISSION
    )
    branch_statement_closed = (
        branch.get("canonical_source_branch_internal_gap_closed") is True
        and branch.get("generic_wfd_self_contained_gap_closed") is False
    )
    obstruction_to_two_atoms = (
        obstruction.get("actual_source_bridge_boundary_sharp") is True
        and obstruction.get("source_lock_concrete_atom_proved") is False
        and obstruction.get("actual_noncanonical_clean_core_moving_atom_exclusion_proved") is False
    )
    canonical_global_not_closed = (
        global_bridge.get("actual_source_bridge_closed_for_canonical_branch") is True
        and global_bridge.get("actual_source_bridge_closes_global_unrestricted") is False
    )
    terminal_recurrence = (
        rate_firewall.get("terminal_recurrence_firewall_closed") is True
        and rate_firewall.get("terminal_route_returns_to_source_entropy_target") is True
    )

    return [
        row(
            "KZEDirectNoProjectionGateActive",
            kze_direct_active,
            False,
            "上一轮已经把非循环 KZ/DLS 压成不得经 NC-BLK 投影的 KZ-E 直接 dispersion log-saving。",
            KZE_DIRECT,
        ),
        row(
            "KZESpineStillGenericWFD",
            kze_spine_reaches_wfd,
            False,
            "KZ-E spine 的自足深核仍是 generic/full-S WFD；其完全自足旧路最终触及 NC-BLK 或外部 DI/BFI。",
            "actual-source bridge or external no-projection theorem",
        ),
        row(
            "SelfContainedTaxonomyImported",
            taxonomy_closed,
            True,
            "外部 generic 合同版闭合、canonical-restricted 自足版闭合、unrestricted generic 自足版被 moving-delta 反证。",
            "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput",
        ),
        row(
            "CanonicalProvenanceClosedOnlyForCanonicalBranch",
            provenance_closed_for_canonical,
            True,
            "canonical 分支中 pre-Cauchy lambda_c 可定义为 RIW/Buchstab 决策树系数；这不是 generic 分支闭合。",
            SOURCE_ADMISSION,
        ),
        row(
            "SourceLockScopedNotGlobal",
            source_lock_scoped,
            False,
            "source-lock 合同只在证明当前 clean A1 分支准入 canonical source 后可用，不能从下游覆盖图反推。",
            SOURCE_ADMISSION,
        ),
        row(
            "BranchStatementCoverageImported",
            branch_statement_closed,
            True,
            "canonical branch 与 generic complement 的覆盖陈述已闭合；generic complement 只能外部化或回流。",
            "generic complement external/PDEC-SAE route",
        ),
        row(
            "ActualSourceBridgeObstructionImported",
            obstruction_to_two_atoms,
            False,
            "actual-source bridge 已压到 source admission 或 noncanonical moving atom exclusion；二者当前均未证明。",
            f"{SOURCE_ADMISSION} OR {NONCANONICAL_MOVING_ATOM}",
        ),
        row(
            "NoncanonicalMovingAtomNotKZNoCycleProof",
            obstruction_to_two_atoms and terminal_recurrence,
            True,
            "noncanonical moving atom/anti-atom 线会回到终端回流链；它不是当前 KZ no-cycle gate 的直接谱证明。",
            "terminal return, not KZ-E direct log-saving",
        ),
        row(
            "CanonicalBridgeNotGlobalUnrestricted",
            canonical_global_not_closed,
            True,
            "actual-source bridge 只在 canonical 分支吸收；不能升级成完整 unrestricted/global 无条件闭合。",
            "noncanonical complement anti-atom or external DI/BFI",
        ),
        row(
            "KZEDirectCurrentInternalRouteReducedToSourceAdmission",
            kze_direct_active and taxonomy_closed and source_lock_scoped and obstruction_to_two_atoms,
            False,
            "若不走外部 no-projection 定理，KZ-E direct no-NCBLK 门的内部路线只剩 actual clean branch canonical admission。",
            SOURCE_ADMISSION,
        ),
        row(
            "ExternalNoProjectionStillConditional",
            True,
            False,
            "外部 DI/BFI/Kuznetsov no-projection 可作为条件输入，但不能作为 strict 自足证明写入。",
            EXTERNAL_KLS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 KZ-E direct 门压到 actual source admission；没有产生无条件终端矛盾。",
            f"{SOURCE_ADMISSION} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data: dict[str, dict[str, Any] | str] = {
        "latest": load_json("prime-matrix-strict-post-new-joint-kz-nocycle-gate-sync-router.json"),
        "kze_spine": read_text("prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"),
        "taxonomy": load_json("prime-matrix-triad-a1-dibfi-self-contained-closure-taxonomy-router.json"),
        "provenance": load_json("prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"),
        "source_lock": load_json("prime-matrix-triad-a1-source-lock-contract-router.json"),
        "branch": load_json("prime-matrix-triad-a1-branch-statement-coverage-router.json"),
        "obstruction": load_json("prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json"),
        "global_bridge": load_json("prime-matrix-actual-source-bridge-global-reconciliation-router.json"),
        "rate_firewall": load_json("prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"),
    }
    rows = build_rows(data)
    reduced = next(
        item["closed"] for item in rows if item["gate"] == "KZEDirectCurrentInternalRouteReducedToSourceAdmission"
    )
    strict_basis = f"{SOURCE_ADMISSION} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    conditional_basis = f"({SOURCE_ADMISSION} OR {EXTERNAL_KLS}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_post_kze_direct_source_bridge_sync_router",
        "status": "post_kze_direct_no_projection_reduced_to_actual_source_admission_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "kze_direct_no_projection_gate_active": rows[0]["closed"],
        "self_contained_taxonomy_imported": rows[2]["closed"],
        "canonical_provenance_closed_only_for_canonical_branch": rows[3]["closed"],
        "source_lock_scoped_not_global": rows[4]["closed"],
        "actual_source_bridge_obstruction_imported": rows[6]["closed"],
        "noncanonical_moving_atom_not_kz_nocycle_proof": rows[7]["closed"],
        "kze_direct_current_internal_route_reduced_to_source_admission": reduced,
        "a1_clean_branch_canonical_source_admission_proved": False,
        "exact_external_dibfi_kuznetsov_no_projection_certificate_accepted": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": KZE_DIRECT,
        "strict_internal_basis_after_router": strict_basis,
        "conditional_external_basis_retained": conditional_basis,
        "next_direct_attack_target": SOURCE_ADMISSION,
        "external_condition_target": EXTERNAL_KLS,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步继续攻击 KZ-E direct no-projection 门。既有 KZ-E spine 的泛 WFD 自足路线已经被分类："
            "canonical-restricted 分支可闭合，unrestricted generic 分支被 moving-delta 反证，外部 generic "
            "合同只能作为条件线。由于当前 no-cycle 门禁止经 NC-BLK/source-root 投影，noncanonical "
            "moving-atom/anti-atom 回流不能计入 KZ-E 直接谱证明。因此，若不接受外部 no-projection "
            "DI/BFI/Kuznetsov 证书，内部剩余压成一个具体 source bridge：在 Cauchy/dispersion 前证明当前 "
            "clean A1 反例分支准入 canonical RIW/Buchstab source。高段模型、RatePreservation 与 "
            "DStructure/Rankin 仍未闭合，行/列命题仍未无条件闭合。"
        ),
    }


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix strict post-KZ-E direct source-bridge 同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"kze_direct_no_projection_gate_active={fmt_bool(result['kze_direct_no_projection_gate_active'])}",
        f"self_contained_taxonomy_imported={fmt_bool(result['self_contained_taxonomy_imported'])}",
        (
            "canonical_provenance_closed_only_for_canonical_branch="
            f"{fmt_bool(result['canonical_provenance_closed_only_for_canonical_branch'])}"
        ),
        f"source_lock_scoped_not_global={fmt_bool(result['source_lock_scoped_not_global'])}",
        f"actual_source_bridge_obstruction_imported={fmt_bool(result['actual_source_bridge_obstruction_imported'])}",
        f"noncanonical_moving_atom_not_kz_nocycle_proof={fmt_bool(result['noncanonical_moving_atom_not_kz_nocycle_proof'])}",
        (
            "kze_direct_current_internal_route_reduced_to_source_admission="
            f"{fmt_bool(result['kze_direct_current_internal_route_reduced_to_source_admission'])}"
        ),
        f"a1_clean_branch_canonical_source_admission_proved={fmt_bool(result['a1_clean_branch_canonical_source_admission_proved'])}",
        (
            "exact_external_dibfi_kuznetsov_no_projection_certificate_accepted="
            f"{fmt_bool(result['exact_external_dibfi_kuznetsov_no_projection_certificate_accepted'])}"
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
        "- 本证书不证明 source admission，也不证明外部 no-projection 定理。",
        "- canonical 分支闭合只在源头已锁定为 RIW/Buchstab 时可用，不能偷渡到 generic/noncanonical 分支。",
        "- noncanonical moving-atom/anti-atom 回流不是当前 KZ no-cycle gate 的直接谱证明。",
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
