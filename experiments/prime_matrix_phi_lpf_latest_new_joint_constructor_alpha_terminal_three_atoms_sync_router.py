#!/usr/bin/env python3
"""生成 Phi-LPF latest constructor alpha 前沿到终端三原子的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_constructor_alpha_terminal_three_atoms_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-constructor-alpha-terminal-three-atoms-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

CURRENT_ALPHA = DOCS / (
    "prime-matrix-phi-lpf-latest-new-joint-constructor-trace-source-rank-sync-router.json"
)
LEGACY_ALPHA_TERMINAL = DOCS / "prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.json"
ALPHA_LOCAL_TERMINAL = DOCS / "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json"
POST_ALPHA_THREE = DOCS / "prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json"

ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
WEIGHT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
A1_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
INDEPENDENT_MOVING = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
TRANSPORT_COHERENCE = (
    "PhiLPFRoughCofactorStepLocalFactorUpdateLawBeforePushforward AND "
    "PhiLPFRoughCofactorOrderedFactorizationCoherenceBeforePushforward"
)
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [CURRENT_ALPHA, LEGACY_ALPHA_TERMINAL, ALPHA_LOCAL_TERMINAL, POST_ALPHA_THREE]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记本脚本与依赖证书哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain(legacy: dict[str, Any], alpha_local: dict[str, Any], post_three: dict[str, Any]) -> list[dict[str, str]]:
    """列出从当前 alpha 前沿到终端三原子的同步链。"""
    chain = [
        {
            "from": ALPHA_ROW,
            "to": alpha_local.get("terminal_gap_after_router", "PDEC/CleanKLS terminal gate"),
            "meaning": "alpha row 局部几何分支已同步到全局终端容量/模型门。",
        },
        {
            "from": f"{ALPHA_ROW} AND {WEIGHT_IDENTITY} AND {RANK_CERT}",
            "to": legacy.get("absorbed_to", f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}"),
            "meaning": "alpha/weight/rank 三腿分攻不是非循环闭合，已有 latest alpha 证书把它们接到终端三原子。",
        },
    ]
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
    current: dict[str, Any],
    legacy: dict[str, Any],
    alpha_local: dict[str, Any],
    post_three: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 latest constructor alpha/terminal-three-atoms 同步判定表。"""
    terminal_atoms = set(post_three.get("terminal_atoms", []))
    return [
        row(
            "CurrentConstructorAlphaFrontierImported",
            current.get("next_primary_attack_target") == ALPHA_ROW
            and current.get("pointwise_kernel_frontier_imported") is True,
            False,
            "刚提交的 constructor trace/source-rank 同步层已把直接主攻推进到 alpha row anchor/phase。",
            ALPHA_ROW,
        ),
        row(
            "LegacyAlphaTerminalSameTargetImported",
            legacy.get("target_input_before_router") == ALPHA_ROW
            and legacy.get("latest_alpha_frontier_imported") is True,
            False,
            "已有 latest alpha-terminal 三原子证书的输入目标与当前 alpha 目标相同，可无换题接入。",
            legacy.get("absorbed_to", f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}"),
        ),
        row(
            "AlphaLocalFrontierTerminalSynced",
            alpha_local.get("alpha_row_formula_local_frontier_synced_to_terminal") is True
            and alpha_local.get("next_direct_attack_target") == "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
            False,
            "alpha row 局部前沿中 unsigned 分支闭合，signed/overload 分支同步到终端容量/模型门。",
            alpha_local.get("terminal_gap_after_router", "terminal capacity/model gate"),
        ),
        row(
            "TerminalThreeAtomsPinned",
            legacy.get("terminal_three_atoms_pinned") is True
            and {CANONICAL_LOCK, A1_ADMISSION, MOVING_ATOM}.issubset(terminal_atoms),
            False,
            "删除 trace/source/terminal/pair-mass 自回流伪出口后，strict 前沿压成 canonical-lock、A1 admission、moving atom 三原子。",
            f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
        ),
        row(
            "NewJointTraceCycleStillAbsorbed",
            legacy.get("new_joint_trace_cycle_absorbed") is True
            and post_three.get("signed_lane_cycle_self_proof_eliminated") is True,
            False,
            "若回到 new joint/branch trace/signed payload，会再次进入已删除的 signed-lane 自证环。",
            f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
        ),
        row(
            "IndependentMovingAtomChosenAsNarrowest",
            legacy.get("next_primary_attack_target") == INDEPENDENT_MOVING,
            False,
            "三原子中最贴近 actual-load 相位异常的是 clean-core moving atom 的独立非终端排斥。",
            INDEPENDENT_MOVING,
        ),
        row(
            "CanonicalLockStillOpen",
            False,
            False,
            "canonical-lock 仍是并行终端原子，当前未证明。",
            CANONICAL_LOCK,
        ),
        row(
            "A1AdmissionStillOpen",
            False,
            False,
            "A1 clean branch canonical source admission 仍是并行终端原子，当前未证明。",
            A1_ADMISSION,
        ),
        row(
            "MovingAtomStillOpen",
            False,
            False,
            "moving atom 排斥及其独立非终端形式仍未证明。",
            INDEPENDENT_MOVING,
        ),
        row(
            "LPFPhiAndExactUVGatesStillParallel",
            True,
            False,
            "逐点 signed 表、ExactUV entropy/fiber 与 rough-cofactor transport/coherence 仍不是由本同步推出。",
            f"{POINTWISE_TABLE} OR {EXACTUV_PAIR} OR {TRANSPORT_COHERENCE}",
        ),
        row(
            "PromotionGatesStillParallel",
            True,
            False,
            "模型余量、Rate 与 DStructure/Rankin 验收仍是晋级门。",
            f"{MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把当前 constructor alpha 前沿接到终端三原子；未证明三命题无条件闭合。",
            f"{INDEPENDENT_MOVING} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    current = load_json(CURRENT_ALPHA)
    legacy = load_json(LEGACY_ALPHA_TERMINAL)
    alpha_local = load_json(ALPHA_LOCAL_TERMINAL)
    post_three = load_json(POST_ALPHA_THREE)
    rows = build_rows(current=current, legacy=legacy, alpha_local=alpha_local, post_three=post_three)
    strict_basis = (
        f"({CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}) "
        f"AND {UV_INCIDENCE} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    retained_basis = (
        f"(({CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM} OR {PDEC_SCOPE}) "
        f"AND {UV_INCIDENCE} AND {MODEL} AND {RATE} AND {DSTRUCTURE}) "
        f"OR {POINTWISE_TABLE} OR {EXACTUV_PAIR} OR ({TRANSPORT_COHERENCE})"
    )
    cert = {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_constructor_alpha_terminal_three_atoms_sync_router",
        "status": "phi_lpf_latest_constructor_alpha_synced_to_terminal_three_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "current_constructor_alpha_frontier_imported": rows[0]["closed"],
        "legacy_alpha_terminal_same_target_imported": rows[1]["closed"],
        "alpha_local_frontier_terminal_synced": rows[2]["closed"],
        "terminal_three_atoms_pinned": rows[3]["closed"],
        "new_joint_trace_cycle_still_absorbed": rows[4]["closed"],
        "independent_moving_atom_chosen_as_narrowest": rows[5]["closed"],
        "acyclic_terminal_canonical_lock_proved": False,
        "a1_clean_branch_canonical_source_admission_proved": False,
        "actual_noncanonical_clean_core_moving_atom_exclusion_proved": False,
        "independent_nonterminal_moving_atom_exclusion_proved": False,
        "pointwise_phi_lpf_bucket_signed_value_table_proved": False,
        "exactuv_entropy_fiber_pair_proved": False,
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
            POINTWISE_TABLE,
            EXACTUV_PAIR,
            TRANSPORT_COHERENCE,
            MODEL,
            RATE,
            DSTRUCTURE,
        ],
        "strict_basis_after_router": strict_basis,
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(legacy=legacy, alpha_local=alpha_local, post_three=post_three),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本步把当前 constructor latest 的 `{ALPHA_ROW}` 接到已有 alpha-terminal 三原子前沿。"
            "alpha 局部公式的 unsigned 分支已经同步完成，signed 分支回流终端容量/模型门；"
            "旧 joint/new joint/branch trace/payload 继续下钻会进入已删除的 signed-lane 自证环。"
            f"因此最新直接主攻推进为 `{INDEPENDENT_MOVING}`，并行保留 canonical-lock、A1 admission、"
            "PDEC、ExactUV、逐点 signed 表、transport/coherence、模型、Rate 与 DStructure。"
            "行/列命题仍未无条件闭合。"
        ),
    }
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF latest constructor alpha terminal three-atoms sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"current_constructor_alpha_frontier_imported={fmt_bool(cert['current_constructor_alpha_frontier_imported'])}",
        f"legacy_alpha_terminal_same_target_imported={fmt_bool(cert['legacy_alpha_terminal_same_target_imported'])}",
        f"alpha_local_frontier_terminal_synced={fmt_bool(cert['alpha_local_frontier_terminal_synced'])}",
        f"terminal_three_atoms_pinned={fmt_bool(cert['terminal_three_atoms_pinned'])}",
        f"new_joint_trace_cycle_still_absorbed={fmt_bool(cert['new_joint_trace_cycle_still_absorbed'])}",
        f"independent_moving_atom_chosen_as_narrowest={fmt_bool(cert['independent_moving_atom_chosen_as_narrowest'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(cert['acyclic_terminal_canonical_lock_proved'])}",
        f"a1_clean_branch_canonical_source_admission_proved={fmt_bool(cert['a1_clean_branch_canonical_source_admission_proved'])}",
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
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
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
            "## 5. 依赖哈希",
            "",
            "```json",
            json.dumps(cert["source_hashes"], ensure_ascii=False, indent=2),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    cert = build_certificate()
    print(json.dumps(cert, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
