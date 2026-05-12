#!/usr/bin/env python3
"""生成 strict PDEC same-set 作用域分支饱和前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_pdec_scope_branch_saturation_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.md"

PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json",
    "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json",
    "prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json",
    "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json",
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


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


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不当成证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


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
    """同步 PDEC same-set 作用域分支的已知下钻结果。"""
    seed = data["seed"]
    pdec = data["pdec"]
    canonical = data["canonical"]
    kz = data["kz"]
    terminal = data["terminal"]
    latest = data["latest"]
    explicit_joint = data["explicit_joint"]

    return [
        row(
            "LatestFrontierContainsPDECScope",
            PDEC_SCOPE in str(seed.get("strict_active_basis_after_router")),
            False,
            "seed-cycle-cut 饱和后，strict 自足线只剩 PDEC same-set 作用域匹配或新 joint 公式。",
            PDEC_SCOPE,
        ),
        row(
            "DirectPDECScopeAuditClosed",
            pdec.get("scope_audit_closed") is True,
            pdec.get("acyclic_same_set_scope_match_proved") is True,
            "direct PDEC 已完成同集协议审计，但 canonical-source 同集结果只能 scoped 使用。",
            CANONICAL_LOCK,
        ),
        row(
            "PDECRequiresCanonicalLockOrExternalDIBFI",
            pdec.get("hardpoint_after_router")
            == f"{CANONICAL_LOCK} OR {WINDOWED_DLS} OR {DIBFI}",
            pdec.get("direct_acyclic_same_set_pdec_cap_dual_certificate_proved") is True,
            "PDEC 作用域匹配不能无条件导入；内部需 canonical lock，外部需 DIBFI，fallback 是 windowed DLS。",
            f"{CANONICAL_LOCK} OR {WINDOWED_DLS} OR {DIBFI}",
        ),
        row(
            "CanonicalLockAttackedButScoped",
            canonical.get("canonical_lock_direct_attack_boundary_closed") is True
            and canonical.get("canonical_equality_case_absorbed_scoped_only") is True,
            canonical.get("acyclic_terminal_canonical_lock_proved") is True,
            "canonical equality case 只给 scoped canonical promotion，不给 acyclic noncanonical 全局矛盾。",
            WINDOWED_DLS,
        ),
        row(
            "CleanKLSDLSTerminalReturn",
            kz.get("kuznetsov_route_returns_to_terminal_family") is True,
            kz.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is True,
            "CleanKLS/DLS 形式层已攻到底，但 KZ-E/NC-BLK 回到 acyclic 终端家族而非终端矛盾。",
            "AcyclicNoncanonicalTerminalFamily",
        ),
        row(
            "TerminalFamilyAlreadySaturated",
            terminal.get("direct_pdec_scope_audited_but_open") is True
            and terminal.get("direct_clean_kls_returns_to_terminal") is True
            and terminal.get("canonical_lock_arm_attacked_but_scoped") is True,
            terminal.get("strict_acyclic_terminal_family_proved") is True,
            "终端家族三手臂已同步：canonical scoped，direct PDEC open，CleanKLS returns terminal。",
            "Nonrecursive/PDEC/NewJoint fixed frontier.",
        ),
        row(
            "PDECScopeNotIndependentNonrecursiveExit",
            latest.get("current_nonrecursive_attack_chain_synced") is True
            and terminal.get("direct_pdec_scope_audited_but_open") is True,
            False,
            "PDEC 手臂仍可作为外部或新 scope 证书输入，但在当前内部语料中不是已证非循环出口。",
            NEW_JOINT_FORMULA,
        ),
        row(
            "NewExplicitJointFormulaStillAbsent",
            explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True,
            explicit_joint.get("new_explicit_joint_constructor_formula_artifact_present") is True,
            "剩余内部破环只能提交新的显式 joint alpha/delta 构造公式，否则仍回到 signed-source 固定点。",
            NEW_JOINT_FORMULA,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 PDEC 作用域分支饱和证书。"""
    data = {
        "seed": load_json("prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"),
        "pdec": load_json("prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"),
        "canonical": load_json("prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json"),
        "kz": load_json("prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"),
        "terminal": load_json("prime-matrix-strict-acyclic-terminal-family-latest-saturation-router.json"),
        "latest": load_json("prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"),
        "explicit_joint": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    pdec_branch_saturated = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "DirectPDECScopeAuditClosed",
            "PDECRequiresCanonicalLockOrExternalDIBFI",
            "CanonicalLockAttackedButScoped",
            "CleanKLSDLSTerminalReturn",
            "TerminalFamilyAlreadySaturated",
        }
    )
    strict_basis = f"{NEW_JOINT_FORMULA} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    conditional_pdec_basis = f"({PDEC_SCOPE} OR {DIBFI}) AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    return {
        "certificate_type": "prime_matrix_strict_pdec_scope_branch_saturation_frontier_router",
        "status": "pdec_scope_branch_saturated_internal_noncycle_exit_reduced_to_new_joint_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "pdec_scope_branch_attacked": True,
        "pdec_scope_branch_saturated_in_current_internal_corpus": pdec_branch_saturated,
        "pdec_scope_proved": data["pdec"].get("acyclic_same_set_scope_match_proved") is True,
        "canonical_lock_proved": data["canonical"].get("acyclic_terminal_canonical_lock_proved") is True,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": data["kz"].get(
            "self_contained_kuznetsov_dls_large_sieve_inequality_proved"
        )
        is True,
        "strict_acyclic_terminal_family_proved": data["terminal"].get(
            "strict_acyclic_terminal_family_proved"
        )
        is True,
        "new_explicit_joint_constructor_formula_artifact_present": data["explicit_joint"].get(
            "new_explicit_joint_constructor_formula_artifact_present"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_JOINT_FORMULA,
        "strict_internal_noncycle_basis_after_router": strict_basis,
        "conditional_pdec_or_external_basis_retained": conditional_pdec_basis,
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "`AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` 已按当前内部材料攻到边界："
            "direct PDEC 需要 canonical-lock 同口径，canonical-lock 只 scoped，CleanKLS/DLS 又回到终端家族，"
            "终端家族三手臂已饱和。因此 PDEC 手臂仍是可接受的新 scope 证书或外部 DIBFI 输入，"
            "但在当前 strict 自足内部语料中不再提供独立非循环出口。剩余真正内部破环点压成"
            "`NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`，并继续保留模型余量、RatePreservation、"
            "DStructure/Rankin 独立验收门。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict PDEC same-set 作用域分支饱和前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pdec_scope_branch_attacked={fmt_bool(result['pdec_scope_branch_attacked'])}",
        (
            "pdec_scope_branch_saturated_in_current_internal_corpus="
            f"{fmt_bool(result['pdec_scope_branch_saturated_in_current_internal_corpus'])}"
        ),
        f"pdec_scope_proved={fmt_bool(result['pdec_scope_proved'])}",
        f"canonical_lock_proved={fmt_bool(result['canonical_lock_proved'])}",
        (
            "self_contained_kuznetsov_dls_large_sieve_inequality_proved="
            f"{fmt_bool(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved'])}"
        ),
        f"strict_acyclic_terminal_family_proved={fmt_bool(result['strict_acyclic_terminal_family_proved'])}",
        (
            "new_explicit_joint_constructor_formula_artifact_present="
            f"{fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 最新严格内部非循环基",
            "",
            "```text",
            result["strict_internal_noncycle_basis_after_router"],
            "```",
            "",
            "条件 PDEC/外部保留线：",
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
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 3. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
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
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
