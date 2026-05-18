#!/usr/bin/env python3
"""生成 post-alpha terminal leaf 到最新非循环前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_alpha_terminal_leaf_latest_noncycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json

输出：
  data/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json
  docs/monograph/prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.md"

POST_ALPHA_LEAF = DOCS / "prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json"
LATEST_SELF_CONTAINED = DOCS / "prime-matrix-strict-latest-self-contained-hardpoint-sync-router.json"
PAIR_ENERGY_NONCYCLE = DOCS / "prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json"
EXPLICIT_JOINT_ATTACK = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
TERMINAL_MACROCYCLE = DOCS / "prime-matrix-strict-terminal-descent-macrocycle-reconciliation-router.json"
SOURCE_BRIDGE_ATTACK = DOCS / "prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json"
CANONICAL_LOCK_ATTACK = DOCS / "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json"
PDEC_SCOPE_SATURATION = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
EXACT_UV_RANK = DOCS / "prime-matrix-strict-exact-uv-map-rank-incidence-router.json"
DSTRUCTURE_ACCEPTANCE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"

CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
NONCANONICAL_MODE = "NoncanonicalFullSComplementLegalClosureMode"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
PAIR_ENERGY = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
JOINT_CONSTRUCTOR = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
SOURCE_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughExactUVPairEnergyOrJointConstructorLoop"
SOURCE_IDENTITY = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab"
SOURCE_ANTIATOM = "FullSNonAPStrengthenedSourceAntiAtomForActualSource"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失文件不能被解释成证明。"""
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
    """构造审查表中的一行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记本同步吸收的证据哈希。"""
    paths = [
        Path(__file__).resolve(),
        POST_ALPHA_LEAF,
        LATEST_SELF_CONTAINED,
        PAIR_ENERGY_NONCYCLE,
        EXPLICIT_JOINT_ATTACK,
        TERMINAL_MACROCYCLE,
        SOURCE_BRIDGE_ATTACK,
        CANONICAL_LOCK_ATTACK,
        PDEC_SCOPE_SATURATION,
        EXACT_UV_RANK,
        DSTRUCTURE_ACCEPTANCE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出本轮从终端叶子到最新非循环前沿的吸收链。"""
    return [
        {
            "from": f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
            "to": f"{CANONICAL_LOCK} OR ({SEED} AND {PAIR_ENERGY})",
            "meaning": "latest self-contained 同步把 noncanonical legal mode 过滤到 actual source entropy，再压成无环 seed 与独立 pair 能量输入。",
        },
        {
            "from": PAIR_ENERGY,
            "to": "RateBearingLargePairAtomPacketExclusion -> terminal/source entropy fixed point",
            "meaning": "既有 pair-energy 攻击说明 seed-only 与定性投影不足；沿 rate-packet 终端线会回到源熵目标固定点。",
        },
        {
            "from": "terminal/source entropy fixed point",
            "to": JOINT_CONSTRUCTOR,
            "meaning": "非循环 source-entropy 证明被重钉到同 formal-unit 逐 primitive 核表，第一生产性字段是 explicit joint constructor。",
        },
        {
            "from": JOINT_CONSTRUCTOR,
            "to": f"{NEW_JOINT_FORMULA} OR {TERMINAL_DESCENT}",
            "meaning": "普通 joint 展开回到 signed-source 固定点；若没有新正向公式，只能改走终端下降替代。",
        },
        {
            "from": TERMINAL_DESCENT,
            "to": f"{CANONICAL_LOCK} OR {NEW_JOINT_FORMULA} OR {SOURCE_BRIDGE}",
            "meaning": "终端下降沿 leaf/source/pair/joint 再回到自身，形成 TERMINAL-SOURCE-PAIR-JOINT 宏循环。",
        },
        {
            "from": SOURCE_BRIDGE,
            "to": f"{SOURCE_IDENTITY} OR {SOURCE_ANTIATOM}",
            "meaning": "外环 actual-source 桥不能经 ExactUV/pair/joint 回环证明；只能证明实际源恒等或实际源强化反原子。",
        },
        {
            "from": CANONICAL_LOCK,
            "to": "scoped canonical absorption OR DLS/PDEC terminal return",
            "meaning": "canonical-lock 直攻只给 scoped canonical case；mismatch 进入 signed source、命名回流、DLS 或 PDEC/model 门。",
        },
        {
            "from": PDEC_SCOPE,
            "to": f"{NEW_JOINT_FORMULA} OR conditional {EXTERNAL_DIBFI}",
            "meaning": "PDEC same-set 分支在当前 strict 内部语料中饱和；可保留为新作用域证书或外部条件线。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总各依赖证书的当前读数。"""
    post = data["post"]
    latest = data["latest"]
    pair = data["pair"]
    joint = data["joint"]
    macro = data["macro"]
    bridge = data["bridge"]
    canonical = data["canonical"]
    pdec = data["pdec"]
    uv = data["uv"]
    dstructure = data["dstructure"]

    return [
        row(
            "PostAlphaTerminalLeafImported",
            post.get("current_terminal_leaf_reduced") is True
            and post.get("next_direct_attack_target") == f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
            False,
            "post-alpha 同步已把 alpha/weight/rank 三腿回流到 terminal leaf 二选一。",
            f"{CANONICAL_LOCK} OR {NONCANONICAL_MODE}",
        ),
        row(
            "NoncanonicalLegalModeAbsorbedByLatestSelfContainedBasis",
            latest.get("sync_closed") is True
            and latest.get("next_direct_attack_target") == PAIR_ENERGY,
            False,
            "noncanonical legal mode 已被更深自足同步压到 actual-source entropy，再压到 seed+pair-energy。",
            f"{SEED} AND {PAIR_ENERGY}",
        ),
        row(
            "PairEnergyOldSpineRejectedAsNoncycleProof",
            pair.get("current_pair_energy_attack_spine_is_recursive") is True
            and pair.get("first_productive_input_after_router") == JOINT_CONSTRUCTOR,
            True,
            "已有 pair-energy/rate-packet/terminal 脊柱形成固定点，不能作为源熵目标的非递归证明。",
            JOINT_CONSTRUCTOR,
        ),
        row(
            "JointConstructorDirectAttackLoopsWithoutNewFormula",
            joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True
            and joint.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            True,
            "普通 joint 构造器展开回到 signed-source 固定点；必须提交新正向公式或走终端下降。",
            f"{NEW_JOINT_FORMULA} OR {TERMINAL_DESCENT}",
        ),
        row(
            "TerminalDescentMacrocycleImported",
            macro.get("terminal_descent_macrocycle_detected") is True
            and macro.get("current_terminal_descent_attack_spine_is_recursive") is True,
            True,
            "终端下降直攻已被证明为 TERMINAL-SOURCE-PAIR-JOINT 宏循环，不是 well-founded descent。",
            f"{CANONICAL_LOCK} OR {NEW_JOINT_FORMULA} OR {SOURCE_BRIDGE}",
        ),
        row(
            "IndependentSourceBridgeReducedOutsideLoop",
            bridge.get("macrocycle_imported") is True
            and bridge.get("generic_wfd_template_refuted") is True,
            False,
            "独立 actual-source 外环桥只剩实际源恒等或实际源强化反原子；二者当前未证。",
            f"{SOURCE_IDENTITY} OR {SOURCE_ANTIATOM}",
        ),
        row(
            "CanonicalLockCurrentDirectAttackNotClosed",
            canonical.get("canonical_lock_direct_attack_boundary_closed") is True
            and canonical.get("acyclic_terminal_canonical_lock_proved") is False,
            False,
            "canonical-lock 直攻只得到 scoped canonical 吸收或 DLS/PDEC/model 出口，未给全局矛盾。",
            canonical.get("latest_self_contained_basis_after_router", "canonical-lock branch still open"),
        ),
        row(
            "PDECScopeInternalBranchSaturated",
            pdec.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
            and pdec.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "direct PDEC same-set 仍可作为新证书或外部线，但当前 strict 内部非循环出口压回新 joint 公式。",
            pdec.get("strict_internal_noncycle_basis_after_router", NEW_JOINT_FORMULA),
        ),
        row(
            "ExactUVIncidenceStillParallel",
            uv.get("exact_uv_map_rank_incidence_router_closed") is True
            and uv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV rank/incidence 的正面内容是 actual emitter 有界重数 incidence，当前未证。",
            EXACT_UV,
        ),
        row(
            "DStructureGateBoundaryClosedButNotAccepted",
            dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            False,
            "DStructure/Tail-log4/finite Rankin 晋级门边界已闭合，但还没有独立接受。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 post-alpha 叶子同步到最新非循环前沿；尚未证明新 joint 公式、actual-source 外环桥、ExactUV、Rate、DStructure 或条件 PDEC/外部线。",
            "row/column theorem still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成同步结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "post": load_json(POST_ALPHA_LEAF),
        "latest": load_json(LATEST_SELF_CONTAINED),
        "pair": load_json(PAIR_ENERGY_NONCYCLE),
        "joint": load_json(EXPLICIT_JOINT_ATTACK),
        "macro": load_json(TERMINAL_MACROCYCLE),
        "bridge": load_json(SOURCE_BRIDGE_ATTACK),
        "canonical": load_json(CANONICAL_LOCK_ATTACK),
        "pdec": load_json(PDEC_SCOPE_SATURATION),
        "uv": load_json(EXACT_UV_RANK),
        "dstructure": load_json(DSTRUCTURE_ACCEPTANCE),
    }
    strict_internal_basis = (
        f"({NEW_JOINT_FORMULA} OR {SOURCE_IDENTITY} OR {SOURCE_ANTIATOM} "
        f"OR {PDEC_SCOPE}) AND {EXACT_UV} AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )
    conditional_external_basis = (
        f"({NEW_JOINT_FORMULA} OR {SOURCE_IDENTITY} OR {SOURCE_ANTIATOM} "
        f"OR {PDEC_SCOPE} OR {EXTERNAL_DIBFI}) AND {EXACT_UV} AND {MODEL_GAP} "
        f"AND {RATE} AND {DSTRUCTURE}"
    )
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_strict_post_alpha_terminal_leaf_latest_noncycle_sync_router",
        "status": "post_alpha_terminal_leaf_synced_to_latest_noncycle_frontier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "post_alpha_terminal_leaf_imported": rows[0]["closed"],
        "noncanonical_legal_mode_absorbed": rows[1]["closed"],
        "pair_energy_old_spine_rejected_as_proof": rows[2]["closed"],
        "joint_constructor_route_loops_without_new_formula": rows[3]["closed"],
        "terminal_descent_macrocycle_detected": rows[4]["closed"],
        "independent_source_bridge_reduced_outside_loop": rows[5]["closed"],
        "canonical_lock_direct_attack_closed_as_routing_only": rows[6]["closed"],
        "pdec_scope_internal_branch_saturated": rows[7]["closed"],
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "source_identity_proved": False,
        "strengthened_actual_source_antiatom_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "strict_internal_noncycle_basis_after_sync": strict_internal_basis,
        "conditional_external_basis_after_sync": conditional_external_basis,
        "next_direct_attack_target": NEW_JOINT_FORMULA,
        "parallel_direct_attack_targets": [
            SOURCE_IDENTITY,
            SOURCE_ANTIATOM,
            PDEC_SCOPE,
            EXACT_UV,
            MODEL_GAP,
            RATE,
            DSTRUCTURE,
        ],
        "sync_chain": sync_chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 post-alpha terminal leaf 的二选一继续同步到仓库已有更深前沿："
            "noncanonical legal mode 不再是独立主攻标签，而是经 latest self-contained 压到 "
            "seed+pair-energy；pair-energy 旧脊柱又被既有非循环审查判为回到 joint constructor/source entropy "
            "固定点；普通 joint 构造器和终端下降也形成宏循环。因此当前 strict 内部非循环前沿不再停在 "
            "canonical/noncanonical 叶子，而是必须提交新的 actual joint 公式，或证明 actual-source 外环桥、"
            "PDEC same-set 作用域新证书，并同时保留 ExactUV、模型余量、RatePreservation 与 DStructure/Rankin。"
            "这些均未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict post-alpha terminal leaf 到最新非循环前沿同步",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"post_alpha_terminal_leaf_imported={fmt_bool(result['post_alpha_terminal_leaf_imported'])}",
        f"noncanonical_legal_mode_absorbed={fmt_bool(result['noncanonical_legal_mode_absorbed'])}",
        f"pair_energy_old_spine_rejected_as_proof={fmt_bool(result['pair_energy_old_spine_rejected_as_proof'])}",
        f"joint_constructor_route_loops_without_new_formula={fmt_bool(result['joint_constructor_route_loops_without_new_formula'])}",
        f"terminal_descent_macrocycle_detected={fmt_bool(result['terminal_descent_macrocycle_detected'])}",
        f"independent_source_bridge_reduced_outside_loop={fmt_bool(result['independent_source_bridge_reduced_outside_loop'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}",
        f"actual_emitter_exact_uv_bounded_multiplicity_incidence_proved={fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(result['rate_preservation_ledger_proved'])}",
        f"dstructure_independent_gate_closed={fmt_bool(result['dstructure_independent_gate_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for edge in result["sync_chain"]:
        lines.append(f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["rows"]:
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
            "## 3. 当前严格内部非循环基",
            "",
            "```text",
            result["strict_internal_noncycle_basis_after_sync"],
            "```",
            "",
            "条件外部线：",
            "",
            "```text",
            result["conditional_external_basis_after_sync"],
            "```",
            "",
            "## 4. 下一主攻",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行必须保留：",
            "",
            "```text",
            "\n".join(result["parallel_direct_attack_targets"]),
            "```",
            "",
            "## 5. 结论边界",
            "",
            "- 本文件只做前沿同步和循环审查，不证明行/列命题。",
            "- `NoncanonicalFullSComplementLegalClosureMode` 在当前语料中已不是最深活动标签。",
            "- pair-energy、普通 joint constructor、terminal descent 的现有路线均不能作为非循环证明。",
            "- 若无新 actual joint 公式或独立 actual-source/PDEC 证书，仍不能越过 ExactUV、RatePreservation、DStructure/Rankin 门。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    result = build_result()
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


if __name__ == "__main__":
    main()
