#!/usr/bin/env python3
"""生成 Phi-LPF latest alpha 前沿到终端三原子的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_alpha_terminal_three_atoms_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_ALPHA = DOCS / "prime-matrix-phi-lpf-latest-trace-exit-source-rank-convergence-sync-router.json"
ALPHA_TERMINAL_LEAF = DOCS / "prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json"
POST_ALPHA_LEAF = DOCS / "prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json"
POST_ALPHA_THREE = DOCS / "prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json"

ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
WEIGHT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
NONCANONICAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
A1_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
INDEPENDENT_MOVING = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
FULLS_EXT = "AcceptFullSKLSExtExternalContract"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
TRANSPORT_COHERENCE = (
    "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND "
    "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_ALPHA,
        ALPHA_TERMINAL_LEAF,
        POST_ALPHA_LEAF,
        POST_ALPHA_THREE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain(alpha_leaf: dict[str, Any], post_leaf: dict[str, Any], post_three: dict[str, Any]) -> list[dict[str, str]]:
    """汇总 latest alpha 到终端三原子的同步链。"""
    chain: list[dict[str, str]] = [
        {
            "from": f"{ALPHA_ROW} AND {WEIGHT_IDENTITY} AND {RANK_CERT}",
            "to": alpha_leaf.get("next_direct_attack_target", f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}"),
            "meaning": "alpha/weight/rank 三腿分攻是固定点，旧 joint constructor 路线进入终端叶子。",
        }
    ]
    for item in post_leaf.get("sync_chain", []):
        chain.append(
            {
                "from": str(item.get("from", "")),
                "to": str(item.get("to", "")),
                "meaning": str(item.get("meaning", "")),
            }
        )
    for item in post_three.get("sync_chain", []):
        chain.append(
            {
                "from": str(item.get("from", "")),
                "to": str(item.get("to", "")),
                "meaning": str(item.get("meaning", "")),
            }
        )
    return chain


def build_rows(
    latest: dict[str, Any],
    alpha_leaf: dict[str, Any],
    post_leaf: dict[str, Any],
    post_three: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest alpha/terminal-three-atoms 同步判定表。"""
    latest_alpha_imported = latest.get("next_primary_attack_target") == ALPHA_ROW
    alpha_to_leaf = (
        alpha_leaf.get("post_antisplit_pointwise_frontier_imported") is True
        and alpha_leaf.get("alpha_and_weight_legs_return_to_terminal") is True
        and alpha_leaf.get("three_leg_separate_attack_fixed_point_imported") is True
        and alpha_leaf.get("current_terminal_leaf_reduced") is True
    )
    leaf_to_new_joint = (
        post_leaf.get("post_alpha_terminal_leaf_imported") is True
        and post_leaf.get("next_direct_attack_target") == NEW_JOINT
        and post_leaf.get("terminal_descent_macrocycle_detected") is True
    )
    three_atoms = set(post_three.get("terminal_atoms", []))
    terminal_three_pinned = (
        post_three.get("terminal_three_atoms_pinned") is True
        and {CANONICAL_LOCK, A1_ADMISSION, MOVING_ATOM}.issubset(three_atoms)
    )
    return [
        row(
            "LatestAlphaFrontierImported",
            latest_alpha_imported,
            False,
            "上一 latest 层把 trace-exit/source-rank 收敛前沿的第一硬点钉在 alpha row anchor/phase。",
            ALPHA_ROW,
        ),
        row(
            "AlphaThreeLegTerminalLeafImported",
            alpha_to_leaf,
            False,
            "post-antisplit alpha 证书已说明 alpha、weight、rank 三腿分攻是固定点，并进入终端叶子。",
            f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        ),
        row(
            "TerminalLeafLatestNoncycleImported",
            leaf_to_new_joint,
            False,
            "terminal leaf latest noncycle 证书把 canonical/noncanonical 宽叶同步到 new joint 或 actual-source 外环输入。",
            NEW_JOINT,
        ),
        row(
            "NewJointTraceCycleAbsorbed",
            post_three.get("post_alpha_new_joint_absorbed") is True
            and post_three.get("branch_trace_absorbed_to_signed_payload") is True
            and post_three.get("signed_lane_cycle_self_proof_eliminated") is True,
            False,
            "new joint 继续下钻会被 branch trace、signed payload 和 signed-lane cycle 吸收，不能作为当前最深自足硬点。",
            f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
        ),
        row(
            "TerminalThreeAtomsPinned",
            terminal_three_pinned,
            False,
            "删除 trace/source/terminal/pair-mass 自回流伪出口后，strict 当前全局前沿压成三原子。",
            f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
        ),
        row(
            "IndependentMovingAtomChosenAsNarrowest",
            post_three.get("next_direct_attack_target") == INDEPENDENT_MOVING,
            False,
            "三原子中最接近 actual-load 相位异常的是 clean-core moving atom 的独立非终端排斥。",
            INDEPENDENT_MOVING,
        ),
        row(
            "CanonicalLockStillOpen",
            post_three.get("terminal_three_atoms_pinned") is True,
            False,
            "canonical-lock 仍是并行终端原子；当前没有证明它。",
            CANONICAL_LOCK,
        ),
        row(
            "A1AdmissionStillOpen",
            post_three.get("terminal_three_atoms_pinned") is True,
            False,
            "A1 clean branch canonical source admission 仍是并行终端原子；当前没有证明它。",
            A1_ADMISSION,
        ),
        row(
            "MovingAtomStillOpen",
            False,
            False,
            "当前语料没有证明 actual noncanonical clean-core moving atom 排斥，也没有证明其独立非终端形式。",
            INDEPENDENT_MOVING,
        ),
        row(
            "LPFPhiSideGatesStillParallel",
            latest.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
            and latest.get("phi_lpf_rough_cofactor_transport_coherence_proved") is False,
            False,
            "LPF/Phi 的逐点 signed 表与 rough-cofactor transport/coherence 仍不能由 terminal-three-atoms 同步自动推出。",
            f"{POINTWISE_TABLE} OR {TRANSPORT_COHERENCE}",
        ),
        row(
            "ExactUVAndPromotionGatesStillParallel",
            True,
            False,
            "ExactUV/Rate/DStructure 仍作为晋级和非集中控制保留；本同步不替代它们。",
            f"{UV_INCIDENCE} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 latest alpha 前沿接到已有终端三原子；未证明三目标命题无条件闭合。",
            f"({CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}) AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 latest alpha/terminal-three-atoms 同步证书。"""
    latest = load_json(LATEST_ALPHA)
    alpha_leaf = load_json(ALPHA_TERMINAL_LEAF)
    post_leaf = load_json(POST_ALPHA_LEAF)
    post_three = load_json(POST_ALPHA_THREE)
    rows = build_rows(latest=latest, alpha_leaf=alpha_leaf, post_leaf=post_leaf, post_three=post_three)
    strict_basis = (
        f"({CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}) "
        f"AND {UV_INCIDENCE} AND {RATE} AND {DSTRUCTURE}"
    )
    retained_basis = (
        f"(({CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM} OR {PDEC_SCOPE} OR {FULLS_EXT}) "
        f"AND {UV_INCIDENCE} AND {RATE} AND {DSTRUCTURE}) OR {POINTWISE_TABLE} OR ({TRANSPORT_COHERENCE}) "
        f"OR {EXACTUV_PAIR}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_alpha_terminal_three_atoms_sync_router",
        "status": "phi_lpf_latest_alpha_frontier_synced_to_terminal_three_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_alpha_frontier_imported": rows[0]["closed"],
        "alpha_three_leg_terminal_leaf_imported": rows[1]["closed"],
        "terminal_leaf_latest_noncycle_imported": rows[2]["closed"],
        "new_joint_trace_cycle_absorbed": rows[3]["closed"],
        "terminal_three_atoms_pinned": rows[4]["closed"],
        "independent_moving_atom_chosen_as_narrowest": rows[5]["closed"],
        "acyclic_terminal_canonical_lock_proved": False,
        "a1_clean_branch_canonical_source_admission_proved": False,
        "actual_noncanonical_clean_core_moving_atom_exclusion_proved": False,
        "independent_nonterminal_moving_atom_exclusion_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "phi_lpf_rough_cofactor_transport_coherence_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": ALPHA_ROW,
        "absorbed_to": f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
        "next_primary_attack_target": INDEPENDENT_MOVING,
        "parallel_primary_attack_targets": [
            CANONICAL_LOCK,
            A1_ADMISSION,
            PDEC_SCOPE,
            UV_INCIDENCE,
            RATE,
            DSTRUCTURE,
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            TRANSPORT_COHERENCE,
        ],
        "strict_basis_after_router": strict_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(alpha_leaf=alpha_leaf, post_leaf=post_leaf, post_three=post_three),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 latest `AlphaRowAnchorPhaseEmissionFormulaLedger` 接到已有 post-antisplit alpha "
            "terminal leaf 与 post-alpha terminal-three-atoms 前沿。alpha/weight/rank 三腿分攻不是非循环闭合，"
            "旧 joint/new joint 路线又被 branch trace、signed payload 和 signed-lane cycle 吸收；删除这些自回流后，"
            "当前 strict 前沿压成 canonical-lock、A1 admission、clean-core moving atom 三原子。"
            f"最新最窄直接主攻为 `{INDEPENDENT_MOVING}`。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest alpha terminal three-atoms sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_alpha_frontier_imported={fmt_bool(cert['latest_alpha_frontier_imported'])}",
        f"alpha_three_leg_terminal_leaf_imported={fmt_bool(cert['alpha_three_leg_terminal_leaf_imported'])}",
        f"terminal_leaf_latest_noncycle_imported={fmt_bool(cert['terminal_leaf_latest_noncycle_imported'])}",
        f"new_joint_trace_cycle_absorbed={fmt_bool(cert['new_joint_trace_cycle_absorbed'])}",
        f"terminal_three_atoms_pinned={fmt_bool(cert['terminal_three_atoms_pinned'])}",
        f"independent_moving_atom_chosen_as_narrowest={fmt_bool(cert['independent_moving_atom_chosen_as_narrowest'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(cert['acyclic_terminal_canonical_lock_proved'])}",
        f"a1_clean_branch_canonical_source_admission_proved={fmt_bool(cert['a1_clean_branch_canonical_source_admission_proved'])}",
        f"actual_noncanonical_clean_core_moving_atom_exclusion_proved={fmt_bool(cert['actual_noncanonical_clean_core_moving_atom_exclusion_proved'])}",
        f"independent_nonterminal_moving_atom_exclusion_proved={fmt_bool(cert['independent_nonterminal_moving_atom_exclusion_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. strict 基",
            "",
            "```text",
            cert["strict_basis_after_router"],
            "```",
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
