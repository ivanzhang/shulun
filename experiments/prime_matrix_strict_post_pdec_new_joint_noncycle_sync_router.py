#!/usr/bin/env python3
"""生成 post-PDEC new-joint 非循环路线同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_pdec_new_joint_noncycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json

输出：
  data/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json
  docs/monograph/prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-pdec-new-joint-noncycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-pdec-new-joint-noncycle-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json",
    "prime-matrix-global-crt-branch-trace-frontier-router.json",
    "prime-matrix-global-crt-signed-payload-sync-router.json",
    "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json",
    "prime-matrix-strict-signed-lane-cycle-closure-router.json",
    "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json",
    "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json",
]

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SIGNED_PAYLOAD = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
NEW_PRIMITIVE = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
KZ_NOCYCLE = "NonCircularSelfContainedKuznetsovDLSLargeSieveWithoutNCBLKSourceRootReuse"
EXACTUV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def get_any(obj: dict[str, Any], *paths: str) -> Any:
    """按候选路径读取字段，兼容嵌套 aggregate。"""
    for path in paths:
        cur: Any = obj
        ok = True
        for part in path.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            else:
                ok = False
                break
        if ok:
            return cur
    return None


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


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造 new-joint 非循环同步判定表。"""
    post_pdec = data["post_pdec"]
    branch = data["branch"]
    signed = data["signed"]
    atomic_trace = data["atomic_trace"]
    lane = data["lane"]
    new_primitive = data["new_primitive"]
    post_antisplit = data["post_antisplit"]

    new_primitive_absorbed = get_any(
        new_primitive,
        "new_primitive_exit_absorbed_to_source_rank",
        "new_primitive_artifact_reduced_to_source_rank_atom",
        "aggregate.new_primitive_artifact_reduced_to_source_rank_atom",
    ) is True
    source_rank_converged = (
        post_antisplit.get("all_internal_source_rank_routes_meet_at_pointwise_kernel_table") is True
    )

    return [
        row(
            "PostPDECNewJointActive",
            post_pdec.get("next_direct_attack_target") == NEW_JOINT
            and NEW_JOINT in str(post_pdec.get("strict_internal_basis_after_router", "")),
            False,
            "PDEC scope 饱和后，当前内部首攻点是新的显式 joint alpha/delta 构造公式。",
            NEW_JOINT,
        ),
        row(
            "NewJointToBranchTraceImported",
            branch.get("new_joint_reduced_to_antisplit_formula") is True
            and branch.get("builtin_pairing_reduced_to_exact_branch_trace") is True,
            branch.get("exact_atomic_joint_branch_trace_signed_coefficient_formula_proved") is True,
            "旧 joint/antisplit/atomic rows/builtin-pairing 链把 new-joint 生产性内容压到 exact atomic branch trace。",
            BRANCH_TRACE,
        ),
        row(
            "BranchTraceToSignedPayloadImported",
            signed.get("exact_atomic_trace_reduced_to_signed_payload") is True
            and atomic_trace.get("atomic_trace_payload_frontier_router_closed") is True,
            signed.get("atomic_signed_payload_constructor_proved") is True
            or atomic_trace.get("atomic_signed_payload_constructor_proved") is True,
            "可见 branch trace 只给坐标；signed coefficient/local factor 需要 atomic signed payload constructor。",
            SIGNED_PAYLOAD,
        ),
        row(
            "FiniteCRTDoesNotCreateSignedPayload",
            signed.get("finite_crt_cannot_generate_signed_payload") is True,
            True,
            "CRT 周期与相位复制不能生成 orientation、local factor 或 signed coefficient。",
            SIGNED_PAYLOAD,
        ),
        row(
            "SignedLaneCycleImported",
            lane.get("signed_lane_cycle_closed") is True
            and lane.get("signed_lane_self_proof_eliminated") is True,
            True,
            "branch trace、signed payload、origin identity 与 common packet 已形成闭环；环内节点不能自证。",
            NEW_PRIMITIVE,
        ),
        row(
            "NewPrimitiveMustBeOutsideCycle",
            new_primitive_absorbed,
            False,
            "new primitive 若只是 trace/payload/origin/common-packet 改名则无效；若要破环必须携带 pre-Cauchy actual source rank/no-collapse 包。",
            "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger",
        ),
        row(
            "SourceRankConvergesToPointwiseKernel",
            source_rank_converged,
            False,
            "new primitive 与 terminal descent 的内部路线已经汇到同 formal-unit pointwise kernel/alpha 前沿，不是独立终点。",
            "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
        ),
        row(
            "NewJointCurrentInternalRouteSaturated",
            (
                branch.get("new_joint_reduced_to_antisplit_formula") is True
                and signed.get("exact_atomic_trace_reduced_to_signed_payload") is True
                and lane.get("signed_lane_self_proof_eliminated") is True
                and source_rank_converged
            ),
            False,
            "当前内部 new-joint 路线回到 signed-lane/source-rank/alpha 终端循环；没有给出非循环构造公式。",
            "new external/primitive joint payload input or KZ no-cycle",
        ),
        row(
            "NonCircularKZStillOpen",
            KZ_NOCYCLE in str(post_pdec.get("strict_internal_basis_after_router", "")),
            post_pdec.get("noncircular_kuznetsov_dls_without_source_root_reuse_proved") is True,
            "并行非循环 KZ/DLS 仍未证明；普通 KZ 路线若复用 NCBLK/source-root 则循环。",
            KZ_NOCYCLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只删除 new-joint 的旧内部自证路线；没有得到无条件终端矛盾。",
            f"{KZ_NOCYCLE} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "post_pdec": load_json("prime-matrix-strict-post-source-root-pdec-scope-saturation-sync-router.json"),
        "branch": load_json("prime-matrix-global-crt-branch-trace-frontier-router.json"),
        "signed": load_json("prime-matrix-global-crt-signed-payload-sync-router.json"),
        "atomic_trace": load_json("prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json"),
        "lane": load_json("prime-matrix-strict-signed-lane-cycle-closure-router.json"),
        "new_primitive": load_json("prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"),
        "post_antisplit": load_json("prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"),
    }
    rows = build_rows(data)
    new_joint_internal_saturated = next(
        item["closed"] for item in rows if item["gate"] == "NewJointCurrentInternalRouteSaturated"
    )
    strict_internal_basis = f"{KZ_NOCYCLE} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    conditional_new_input_basis = (
        f"({NEW_JOINT} OR {NEW_PRIMITIVE} OR {PDEC_SCOPE} OR {DIBFI} OR {KZ_NOCYCLE}) "
        f"AND {EXACTUV} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    result = {
        "certificate_type": "prime_matrix_strict_post_pdec_new_joint_noncycle_sync_router",
        "status": "post_pdec_new_joint_internal_route_saturated_to_signed_lane_cycle_kz_nocycle_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "new_joint_current_internal_route_saturated": new_joint_internal_saturated,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "exact_atomic_branch_trace_formula_proved": False,
        "atomic_signed_payload_constructor_proved": False,
        "signed_lane_self_proof_eliminated": data["lane"].get("signed_lane_self_proof_eliminated") is True,
        "new_primitive_artifact_independent_present": False,
        "noncircular_kuznetsov_dls_without_source_root_reuse_proved": data["post_pdec"].get(
            "noncircular_kuznetsov_dls_without_source_root_reuse_proved"
        )
        is True,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": data["post_pdec"].get("strict_internal_basis_after_router", ""),
        "strict_internal_basis_after_router": strict_internal_basis,
        "conditional_new_input_basis_retained": conditional_new_input_basis,
        "next_direct_attack_target": KZ_NOCYCLE,
        "conditional_new_input_targets": [NEW_JOINT, NEW_PRIMITIVE, PDEC_SCOPE, DIBFI],
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步继续攻击 post-PDEC 前沿中的 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`。"
            "导入 global CRT branch-trace、signed payload、atomic trace payload、signed-lane cycle、new primitive "
            "和 source-rank convergence 证书后，当前内部 new-joint 路线已被压成 signed-lane/source-rank/alpha "
            "终端循环：旧 joint/antisplit 链只给 exact branch trace；branch trace 只给可见坐标；signed payload "
            "又回到 origin/common-packet 闭环；new primitive 若要破环必须是闭环外的 pre-Cauchy actual source "
            "rank/no-collapse 工件，而当前没有提交。因而 new-joint 不再是当前内部非循环出口。"
            "除非新增真正的 joint/payload/PDEC/external 输入，剩余内部非循环路线收窄为不复用 NCBLK/source-root 的 "
            "Kuznetsov/DLS 证明，并仍需高段模型、RatePreservation 与 DStructure/Rankin。行/列命题仍未无条件闭合。"
        ),
    }
    return result


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix strict post-PDEC new-joint 非循环同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"new_joint_current_internal_route_saturated={fmt_bool(result['new_joint_current_internal_route_saturated'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}",
        f"exact_atomic_branch_trace_formula_proved={fmt_bool(result['exact_atomic_branch_trace_formula_proved'])}",
        f"atomic_signed_payload_constructor_proved={fmt_bool(result['atomic_signed_payload_constructor_proved'])}",
        f"signed_lane_self_proof_eliminated={fmt_bool(result['signed_lane_self_proof_eliminated'])}",
        f"new_primitive_artifact_independent_present={fmt_bool(result['new_primitive_artifact_independent_present'])}",
        (
            "noncircular_kuznetsov_dls_without_source_root_reuse_proved="
            f"{fmt_bool(result['noncircular_kuznetsov_dls_without_source_root_reuse_proved'])}"
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
        "条件保留的新输入线：",
        "",
        "```text",
        result["conditional_new_input_basis_retained"],
        "```",
        "",
        "下一直接主攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "条件新输入仍可为：",
        "",
        "```text",
        " OR ".join(result["conditional_new_input_targets"]),
        "```",
        "",
        "## 3. 诚实边界",
        "",
        "- 本证书不证明 new-joint、不证明 signed payload，也不证明非循环 KZ/DLS。",
        "- 它只说明当前内部 new-joint 旧路线回到 signed-lane/source-rank/alpha 终端循环。",
        "- 新的 joint/payload/PDEC/external 输入仍可作为独立输入，但当前没有提交。",
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
