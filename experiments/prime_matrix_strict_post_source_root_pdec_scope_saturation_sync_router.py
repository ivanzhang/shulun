#!/usr/bin/env python3
"""生成 post-source-root direct PDEC scope 饱和同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_source_root_pdec_scope_saturation_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json

输出：
  data/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json
  docs/monograph/prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json",
    "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json",
    "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json",
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
]

PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
KZ_NOCYCLE = "NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失只登记，不当作证明。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本与上游证书哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖文件。"""
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
    """构造 post-source-root PDEC 分支同步判定表。"""
    forward = data["forward"]
    direct = data["direct"]
    saturation = data["saturation"]
    canonical = data["canonical"]
    kz = data["kz"]
    terminal = data["terminal"]
    joint = data["joint"]

    return [
        row(
            "PostSourceRootPDECScopeActive",
            forward.get("next_direct_attack_target") == PDEC_SCOPE
            and PDEC_SCOPE in str(forward.get("hardpoint_after_router", "")),
            False,
            "source-root 被压成终端环后，下一直接主攻确认为 direct same-set PDEC scope。",
            PDEC_SCOPE,
        ),
        row(
            "ForwardKZNoCycleParallelOpen",
            KZ_NOCYCLE in str(forward.get("hardpoint_after_router", "")),
            forward.get("noncircular_kuznetsov_dls_without_source_root_reuse_proved") is True,
            "同一前沿还保留非循环 KZ/DLS；若该臂复用 NCBLK/source-root 就回到已识别环。",
            KZ_NOCYCLE,
        ),
        row(
            "DirectPDECScopeAuditImported",
            direct.get("scope_audit_closed") is True
            and direct.get("same_set_pdec_protocol_imported") is True,
            direct.get("acyclic_same_set_scope_match_proved") is True,
            "既有 direct PDEC 审计已导入 same-set 协议，但未证明 acyclic 作用域匹配。",
            "Acyclic terminal certificate must match canonical same-set formal unit.",
        ),
        row(
            "CanonicalSameSetOnlyScoped",
            direct.get("canonical_source_same_set_pdec_closed_but_scoped") is True,
            False,
            "canonical-source 同集容量边界只在 canonical 口径闭合，不能直接升级为 acyclic noncanonical 全局矛盾。",
            "No silent canonical import.",
        ),
        row(
            "PDECScopeBranchSaturatedInternally",
            saturation.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True,
            saturation.get("pdec_scope_proved") is True,
            "PDEC scope 在当前内部材料中已攻到饱和边界；它仍可作为新证书输入，但不是已证内部出口。",
            NEW_JOINT,
        ),
        row(
            "CanonicalLockDoesNotRescuePDEC",
            canonical.get("canonical_lock_direct_attack_boundary_closed") is True
            and canonical.get("canonical_equality_case_absorbed_scoped_only") is True,
            canonical.get("acyclic_terminal_canonical_lock_proved") is True,
            "direct PDEC 回到 canonical-lock 时，只得到 scoped canonical 吸收或 mismatch/DLS/终端回流。",
            "mismatch/DLS/terminal return",
        ),
        row(
            "KZRouteWouldCycleWithoutNoCycleInput",
            kz.get("kuznetsov_route_returns_to_terminal_family") is True,
            False,
            "已有 KZ/DLS 同步表明普通自足路线经 KZ-E/NCBLK 回终端；因此当前需要明确非循环 KZ/DLS。",
            KZ_NOCYCLE,
        ),
        row(
            "TerminalFamilySaturationImported",
            terminal.get("internal_terminal_cycle_obstruction_closed") is True
            and terminal.get("direct_pdec_scope_audited_but_open") is True
            and terminal.get("direct_clean_kls_returns_to_terminal") is True,
            terminal.get("strict_acyclic_terminal_family_proved") is True,
            "终端三手臂已饱和：canonical scoped、direct PDEC open、direct clean KLS returns terminal。",
            f"{NEW_JOINT} OR {PDEC_SCOPE} OR {KZ_NOCYCLE}",
        ),
        row(
            "NewJointFormulaStillAbsent",
            joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True,
            joint.get("new_explicit_joint_constructor_formula_artifact_present") is True,
            "内部破环若不靠 PDEC 新证书或非循环 KZ/DLS，只剩新的显式 joint alpha/delta 构造公式。",
            NEW_JOINT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 post-source-root 的 direct PDEC 手臂压到既有饱和边界；未得到无条件终端矛盾。",
            f"({NEW_JOINT} OR {KZ_NOCYCLE}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "forward": load_json("prime-matrix-strict-forward-source-root-terminal-cycle-sync-router.json"),
        "direct": load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"),
        "saturation": load_json("prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"),
        "canonical": load_json("prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json"),
        "kz": load_json("prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"),
        "terminal": load_json("prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"),
        "joint": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
    }
    rows = build_rows(data)
    pdec_internal_saturated = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "DirectPDECScopeAuditImported",
            "CanonicalSameSetOnlyScoped",
            "PDECScopeBranchSaturatedInternally",
            "CanonicalLockDoesNotRescuePDEC",
            "TerminalFamilySaturationImported",
        }
    )
    strict_internal_basis = f"({NEW_JOINT} OR {KZ_NOCYCLE}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    conditional_retained_basis = f"({PDEC_SCOPE} OR {DIBFI} OR {KZ_NOCYCLE}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    result = {
        "certificate_type": "prime_matrix_strict_post_source_root_pdec_scope_saturation_sync_router",
        "status": "post_source_root_pdec_scope_saturated_internal_basis_reduced_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "post_source_root_pdec_scope_active": rows[0]["closed"],
        "direct_pdec_scope_audit_imported": rows[2]["closed"],
        "pdec_scope_branch_saturated_in_current_internal_corpus": pdec_internal_saturated,
        "pdec_scope_proved": data["direct"].get("acyclic_same_set_scope_match_proved") is True,
        "noncircular_kuznetsov_dls_without_source_root_reuse_proved": data["forward"].get(
            "noncircular_kuznetsov_dls_without_source_root_reuse_proved"
        )
        is True,
        "new_explicit_joint_constructor_formula_artifact_present": data["joint"].get(
            "new_explicit_joint_constructor_formula_artifact_present"
        )
        is True,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": data["forward"].get("strict_active_basis_after_router", ""),
        "strict_internal_basis_after_router": strict_internal_basis,
        "conditional_pdec_or_external_basis_retained": conditional_retained_basis,
        "next_direct_attack_target": NEW_JOINT,
        "parallel_attack_targets": [KZ_NOCYCLE, HIGH_MODEL, RATE, DSTRUCTURE],
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步把 source-root 后继前沿中的 `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` "
            "接入既有 direct PDEC 作用域审计与 PDEC scope 饱和证书。结论是：same-set PDEC 协议和 "
            "canonical-source 容量边界可作为工具，但 strict acyclic noncanonical 分支仍缺同 formal unit、坏窗集合、"
            "U_CRT/L_PDEC 与质量推前完全同口径的 scope 证明。沿 canonical-lock 或普通 KZ/DLS 下钻会回到 scoped "
            "canonical 吸收、mismatch/DLS 或终端家族循环。因此 direct PDEC 不再是当前内部非循环出口；"
            "若不新增 PDEC scope 证书或外部 DIBFI 输入，内部破环点压成新的显式 joint alpha/delta 构造公式，"
            "并行保留不复用 NCBLK/source-root 的非循环 KZ/DLS、高段模型、RatePreservation 与 DStructure/Rankin。"
            "行/列命题仍未无条件闭合。"
        ),
    }
    return result


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix strict post-source-root PDEC scope 饱和同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"post_source_root_pdec_scope_active={fmt_bool(result['post_source_root_pdec_scope_active'])}",
        f"direct_pdec_scope_audit_imported={fmt_bool(result['direct_pdec_scope_audit_imported'])}",
        (
            "pdec_scope_branch_saturated_in_current_internal_corpus="
            f"{fmt_bool(result['pdec_scope_branch_saturated_in_current_internal_corpus'])}"
        ),
        f"pdec_scope_proved={fmt_bool(result['pdec_scope_proved'])}",
        (
            "noncircular_kuznetsov_dls_without_source_root_reuse_proved="
            f"{fmt_bool(result['noncircular_kuznetsov_dls_without_source_root_reuse_proved'])}"
        ),
        (
            "new_explicit_joint_constructor_formula_artifact_present="
            f"{fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}"
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
        "条件保留线：",
        "",
        "```text",
        result["conditional_pdec_or_external_basis_retained"],
        "```",
        "",
        "下一直接主攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "并行保留：",
        "",
        "```text",
        " AND ".join(result["parallel_attack_targets"]),
        "```",
        "",
        "## 3. 诚实边界",
        "",
        "- 本证书不证明 direct PDEC scope，也不证明非循环 KZ/DLS。",
        "- 它只说明当前内部 PDEC scope 手臂已回到既有饱和边界，不能作为已证非循环出口。",
        "- 新 PDEC scope 证书、外部 DIBFI 或非循环 KZ/DLS 仍可作为独立输入，但当前均未给出。",
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
