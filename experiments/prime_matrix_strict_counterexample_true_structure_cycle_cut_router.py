#!/usr/bin/env python3
"""生成 strict 反例链/真实结构链循环切断路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_counterexample_true_structure_cycle_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json"
OUT_MD = DOCS / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-independent-pair-energy-attack-router.json",
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
    "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
    "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json",
    "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json",
    "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json",
    "prime-matrix-early-zero-contradiction-matrix-router.json",
    "prime-matrix-pcolumn-anchor-wheel-field.md",
    "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md",
]

TARGET = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
CANONICAL_CERT = "AcyclicCanonicalExactSameSetPromotionCertificate"
PRECAUCHY_ID = "AcyclicCanonicalPreCauchyCoefficientIdentityLedger"
PAIR_ENERGY = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
SHORT_RETURN = "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect"
TERMINAL_LEAF = "TerminalLeafExclusionForAcyclicNoncanonicalFamily"
DSTRUCTURE_GATE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


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


def contradiction_candidate_rows() -> list[dict[str, Any]]:
    """列出反例链与真实结构链之间的直接矛盾候选。"""
    return [
        {
            "candidate": "CRTMirrorVsEarlyRow",
            "true_structure": "非平凡零行在完整 CRT 周期内关于中心镜像成对。",
            "counterexample_pressure": "假设存在 P 行以内早期零行，镜像会给出同相位的远端伴随对象。",
            "why_not_contradiction_yet": "镜像把早期行送到周期远端，不自动给同一 formal unit 的短复现。",
            "needed_cut": SHORT_RETURN,
        },
        {
            "candidate": "PColumnLayeredWheelClamp",
            "true_structure": "P 列锚、圆柱斜线和层叠轮筛把候选覆盖压到固定相位字母表。",
            "counterexample_pressure": "早期零行反例必须同时服从 carry-shell、anchor-collar 和 layered-wheel。",
            "why_not_contradiction_yet": "这些约束目前仍是 unsigned 支撑形状，不能直接产生 signed pre-Cauchy 源。",
            "needed_cut": "AlphaFormulaSignedCoefficientLiftLedger OR AlphaSignedLiftFailureNamedReturnLedger",
        },
        {
            "candidate": "SameLabelShortRecurrence",
            "true_structure": "行位移 Delta 后，同列值对每个 q<P 的变化是 Delta*P，且 P 在 mod q 下可逆。",
            "counterexample_pressure": "若同一 formal unit 的同标签覆盖证书短复现，则每个保持的素标签 q 都强制 q | Delta。",
            "why_not_contradiction_yet": "短复现引理本身已闭合；未证的是早期零行一定强制这种稳定短复现或相位缺陷。",
            "needed_cut": SHORT_RETURN,
        },
        {
            "candidate": "CurrentPDECSparseFrontierZero",
            "true_structure": "当前已物化 PDEC 与 sparse/LocalSurvivor 前沿为零。",
            "counterexample_pressure": "反例链若不稳定，必须投射成低维相位缺陷或 sparse packet。",
            "why_not_contradiction_yet": "当前前沿为零只是当前语料实例清零，不是未来全局 family 不存在证明。",
            "needed_cut": TERMINAL_LEAF,
        },
        {
            "candidate": "CanonicalSourceClosure",
            "true_structure": "canonical RIW/Buchstab 分支已有来源闭合和终端晋级材料。",
            "counterexample_pressure": "若反例链实际是 canonical 同集推前，则可调用 canonical 范围闭合。",
            "why_not_contradiction_yet": "尚未提交 exact same-set promotion：pre-Cauchy 准入、有限因子图、同集推前、无 payload 残留。",
            "needed_cut": CANONICAL_CERT,
        },
        {
            "candidate": "PairMassDispersion",
            "true_structure": "Cauchy/支撑能量引理可从独立 pair L2 或最大 pair 原子界推出支撑下界。",
            "counterexample_pressure": "反例链若集中在 moving same-(u,v) 大原子，会与源熵反原子目标正面相撞。",
            "why_not_contradiction_yet": "当前没有不依赖源熵目标自身的独立 pair L2/max-atom 界。",
            "needed_cut": PAIR_ENERGY,
        },
    ]


def cycle_cut_rows(
    moving: dict[str, Any],
    alpha_formula: dict[str, Any],
    alpha_signed: dict[str, Any],
    entropy_guard: dict[str, Any],
    energy: dict[str, Any],
    recurrence: dict[str, Any],
    canonical_exit: dict[str, Any],
    descent: dict[str, Any],
    leaf: dict[str, Any],
    source_bridge: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成循环切断判定表。"""
    return [
        {
            "gate": "SameTheoremAndCounterexampleDiscipline",
            "closed": True,
            "proved": True,
            "meaning": "本步只在假设 EarlyZeroRowWithinP 的反例链中工作，不用真实缺席或样本统计替代证明。",
            "remaining": "所有输出必须是反例链内的命名矛盾、命名回流或打开输入。",
        },
        {
            "gate": "ActualMovingBlockUnnamedExitRemoved",
            "closed": moving.get("strict_actual_moving_block_router_closed") is True,
            "proved": True,
            "meaning": "actual moving-block/NC-BLK 不能再作为独立无名出口。",
            "remaining": moving.get("terminal_gap_after_router", "PDEC/CleanKLS terminal and model ledger"),
        },
        {
            "gate": "UnsignedGeometryAmplifierImported",
            "closed": alpha_formula.get("early_zero_rigidity_imported_as_unsigned_shape_only") is True,
            "proved": True,
            "meaning": "早期零行反例已被 carry-shell、anchor-collar、P 列锚和 layered-wheel 放入同一真实结构压力场。",
            "remaining": alpha_formula.get("terminal_gap_after_router", "signed lift and overload return"),
        },
        {
            "gate": "SignedSourceExtractionStillOpen",
            "closed": alpha_signed.get("alpha_formula_signed_lift_router_closed") is True,
            "proved": False,
            "meaning": "真实几何压力仍不能反推出 signed pre-Cauchy alpha source；signed lift 是活动缺口。",
            "remaining": alpha_signed.get("terminal_gap_after_router", "AlphaFormulaSignedCoefficientLiftLedger"),
        },
        {
            "gate": "ShortSameLabelRecurrenceContradictionLemma",
            "closed": True,
            "proved": True,
            "meaning": "若同一 formal unit 的同标签证书以 0<|Delta|<prod(Q) 短复现，且保持标签集 Q，则 q|Delta 对全部 q in Q，矛盾。",
            "remaining": "必须证明早期零行强制短稳定同标签复现，或不稳定时强制登记相位缺陷。",
        },
        {
            "gate": "EarlyZeroForcesStableShortReturnOrDefect",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明早期零行反例一定产生同 formal unit 的短稳定复现，或产生可排斥 PDEC/SAE/ColumnCRT 相位缺陷。",
            "remaining": SHORT_RETURN,
        },
        {
            "gate": "PairMassEntropyLoopCut",
            "closed": entropy_guard.get("circular_entropy_proof_rejected") is True,
            "proved": True,
            "meaning": "pair-mass 分散不能用 moving-atom/source-entropy 目标自身证明，否则是回流。",
            "remaining": entropy_guard.get("nonrecursive_internal_obligation", PAIR_ENERGY),
        },
        {
            "gate": "IndependentPairEnergyStillOpen",
            "closed": energy.get("large_pair_failure_packetized") is True,
            "proved": False,
            "meaning": "独立 pair 能量界已压成 rate-bearing 大 pair packet 排斥，但该排斥再走终端标签会回流。",
            "remaining": energy.get("internal_obligation_after_router", "RateBearingLargePairAtomPacketExclusion"),
        },
        {
            "gate": "DirectTerminalRouteRecurrenceCut",
            "closed": recurrence.get("terminal_recurrence_firewall_closed") is True,
            "proved": True,
            "meaning": "direct PDEC/CleanKLS 终端标签链已识别为回到 canonical-lock 或原 actual-source 熵目标的循环。",
            "remaining": recurrence.get("strict_self_contained_terminal_after_router", f"AcyclicTerminalCanonicalLock OR {TARGET}"),
        },
        {
            "gate": "CanonicalLockReducedToExactSameSetCertificate",
            "closed": canonical_exit.get("canonical_lock_refined_to_exact_same_set_certificate") is True,
            "proved": False,
            "meaning": "canonical-lock 已压成 exact same-set 晋级证书；任一子账本缺失时不能调用 canonical 分支闭合。",
            "remaining": canonical_exit.get("canonical_exact_certificate_definition", CANONICAL_CERT),
        },
        {
            "gate": "TerminalDescentNotLeafExclusion",
            "closed": descent.get("terminal_return_well_founded_descent_schema_closed") is True,
            "proved": False,
            "meaning": "终端无隐藏循环下降 schema 已闭合，但叶子排斥没有证明；不能把下降当作最终矛盾。",
            "remaining": descent.get("terminal_gap_after_router", TERMINAL_LEAF),
        },
        {
            "gate": "CurrentLeafZeroNotGlobalNonexistence",
            "closed": leaf.get("current_leaf_firewall_active_basis_reduced") is True,
            "proved": True,
            "meaning": "当前 PDEC/sparse 前沿为零只清理当前实例；未来 schema 是准入纪律，不是全局不存在定理。",
            "remaining": leaf.get("terminal_gap_after_current_instance_router", TERMINAL_LEAF),
        },
        {
            "gate": "ActualSourceBridgeStillConcreteOpen",
            "closed": source_bridge.get("actual_source_bridge_boundary_sharp") is True,
            "proved": False,
            "meaning": "actual-source 桥已具体化为 source admission 或 moving atom 排斥，但两者均未证明。",
            "remaining": source_bridge.get("strict_self_contained_terminal_after_router", TARGET),
        },
        {
            "gate": "DirectVisibleContradictionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "反例链与真实结构链之间尚未得到无条件直接矛盾；当前得到的是最小非循环切口。",
            "remaining": (
                f"{SHORT_RETURN} OR {CANONICAL_CERT} OR "
                f"NonrecursiveIndependentProofOf{TARGET}"
            ),
        },
    ]


def short_recurrence_lemma_text() -> str:
    """给出短稳定复现矛盾引理的精确文本。"""
    return (
        "设固定 P、行参数 n、列坐标 c 和同一 formal unit 的标签证书。"
        "若对素标签集 Q 中每个 q<P，同一列标签在行位移 Delta 后仍由同一个 q 解释，"
        "则 x_{n+Delta,c}-x_{n,c}=Delta*P 同时被 q 整除。因 gcd(P,q)=1，得 q|Delta。"
        "所以 prod(Q)|Delta。若 0<|Delta|<prod(Q)，则同标签短复现不可能。"
        "因此，一旦早期零行反例能强制同 formal unit 的短稳定复现，或在不稳定处强制登记相位缺陷，"
        "就会给出真正直接矛盾或进入可审查 PDEC/SAE/ColumnCRT 出口。"
    )


def build_result() -> dict[str, Any]:
    """构造反例链/真实结构链循环切断证书。"""
    moving = load_json(DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json")
    alpha_formula = load_json(DOCS / "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json")
    alpha_signed = load_json(DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json")
    entropy_guard = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json"
    )
    energy = load_json(DOCS / "prime-matrix-strict-independent-pair-energy-attack-router.json")
    recurrence = load_json(
        DOCS / "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"
    )
    canonical_exit = load_json(
        DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
    )
    descent = load_json(DOCS / "prime-matrix-strict-acyclic-terminal-descent-firewall-router.json")
    leaf = load_json(DOCS / "prime-matrix-strict-terminal-leaf-firewall-current-instance-router.json")
    source_bridge = load_json(
        DOCS / "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json"
    )

    rows = cycle_cut_rows(
        moving=moving,
        alpha_formula=alpha_formula,
        alpha_signed=alpha_signed,
        entropy_guard=entropy_guard,
        energy=energy,
        recurrence=recurrence,
        canonical_exit=canonical_exit,
        descent=descent,
        leaf=leaf,
        source_bridge=source_bridge,
    )
    noncyclic_cut = [
        SHORT_RETURN,
        CANONICAL_CERT,
        f"NonrecursiveIndependentProofOf{TARGET}",
    ]
    return {
        "certificate_type": "prime_matrix_strict_counterexample_true_structure_cycle_cut_router",
        "status": "counterexample_true_structure_direct_contradiction_reduced_to_noncyclic_cut_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "true_structure_chain_imported": True,
        "short_same_label_recurrence_contradiction_lemma_proved": True,
        "early_zero_forces_stable_short_return_or_defect_proved": False,
        "terminal_recurrence_loop_cut": recurrence.get("terminal_recurrence_firewall_closed") is True,
        "pair_mass_entropy_loop_cut": entropy_guard.get("circular_entropy_proof_rejected") is True,
        "downstream_source_reconstruction_loop_cut": (
            canonical_exit.get("canonical_lock_nonrecursive_exit_firewall_closed") is True
        ),
        "acyclic_canonical_exact_same_set_promotion_certificate_proved": False,
        "acyclic_canonical_precauchy_coefficient_identity_proved": False,
        "independent_exact_pair_l2_or_max_atom_bound_proved": False,
        "nonrecursive_independent_source_entropy_proved": False,
        "terminal_leaf_exclusion_for_acyclic_noncanonical_family_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "strict_terminal_before_router": (
            "EarlyZeroCounterexampleChain AND TrueStructureRigidityChain"
        ),
        "strict_terminal_after_router": " OR ".join(noncyclic_cut),
        "noncyclic_cut_set": noncyclic_cut,
        "preferred_next_direct_attack_target": SHORT_RETURN,
        "backup_next_attack_target": f"{PRECAUCHY_ID} OR {PAIR_ENERGY}",
        "short_recurrence_contradiction_lemma": short_recurrence_lemma_text(),
        "direct_contradiction_formula": (
            "EarlyZeroRowWithinP AND StableSameFormalUnitSameLabelReturn(Delta,Q) "
            "AND 0<|Delta|<prod(Q) => contradiction, because prod(Q)|Delta."
        ),
        "instability_formula": (
            "EarlyZeroRowWithinP AND NOT StableSameFormalUnitSameLabelReturn "
            "=> RegisteredPhaseDefect(PDEC/SAE/ColumnCRT) is still open and must be proved."
        ),
        "contradiction_candidates": contradiction_candidate_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步没有换命题，而是专门审查“早期零行反例链”与“真实结构刚性链”之间能否直接撞出矛盾。"
            "结论是：真正可立即产生矛盾的核心引理已经明确，即同一 formal unit 的同标签短复现会强制 "
            "`prod(Q)|Delta`，从而与 `0<|Delta|<prod(Q)` 矛盾；但当前尚未证明早期零行必强制这种短稳定复现，"
            "也尚未证明不稳定时必生成已排斥的 PDEC/SAE/ColumnCRT 相位缺陷。另一方面，pair-mass、direct PDEC/CleanKLS、"
            "canonical-lock 下游反推 source 都已识别为循环或作用域不匹配。故当前最窄非循环切口是 "
            "`StableShortSameLabelRecurrenceOrRegisteredPhaseDefect`，并列备用为 exact same-set canonical 晋级证书或"
            "完全独立的 actual-source 熵证明。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 反例链/真实结构链循环切断路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"short_same_label_recurrence_contradiction_lemma_proved={fmt_bool(result['short_same_label_recurrence_contradiction_lemma_proved'])}",
        f"early_zero_forces_stable_short_return_or_defect_proved={fmt_bool(result['early_zero_forces_stable_short_return_or_defect_proved'])}",
        f"terminal_recurrence_loop_cut={fmt_bool(result['terminal_recurrence_loop_cut'])}",
        f"pair_mass_entropy_loop_cut={fmt_bool(result['pair_mass_entropy_loop_cut'])}",
        f"acyclic_canonical_exact_same_set_promotion_certificate_proved={fmt_bool(result['acyclic_canonical_exact_same_set_promotion_certificate_proved'])}",
        f"independent_exact_pair_l2_or_max_atom_bound_proved={fmt_bool(result['independent_exact_pair_l2_or_max_atom_bound_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 可立即闭合的短复现矛盾引理",
        "",
        result["short_recurrence_contradiction_lemma"],
        "",
        "直接矛盾公式：",
        "",
        "```text",
        result["direct_contradiction_formula"],
        "```",
        "",
        "不稳定分支仍需证明：",
        "",
        "```text",
        result["instability_formula"],
        "```",
        "",
        "## 2. 矛盾候选审查",
        "",
        "| candidate | true structure | counterexample pressure | why not contradiction yet | needed cut |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["contradiction_candidates"]:
        lines.append(
            "| `{candidate}` | {true_structure} | {counterexample_pressure} | {why_not_contradiction_yet} | {needed_cut} |".format(
                candidate=table_cell(row["candidate"]),
                true_structure=table_cell(row["true_structure"]),
                counterexample_pressure=table_cell(row["counterexample_pressure"]),
                why_not_contradiction_yet=table_cell(row["why_not_contradiction_yet"]),
                needed_cut=table_cell(row["needed_cut"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 循环切断表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 当前非循环切口",
            "",
            "```text",
            result["strict_terminal_after_router"],
            "```",
            "",
            "首选下一硬攻点：",
            "",
            "```text",
            result["preferred_next_direct_attack_target"],
            "```",
            "",
            "备用硬攻点：",
            "",
            "```text",
            result["backup_next_attack_target"],
            "```",
            "",
            "独立晋级门仍保留：",
            "",
            "```text",
            DSTRUCTURE_GATE,
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
