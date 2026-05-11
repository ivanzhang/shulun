#!/usr/bin/env python3
"""生成 independent actual-source 桥具体原子同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_independent_actual_source_bridge_concrete_atom_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.md"

INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn"
ACTUAL_BRIDGE = "ActualA1FullSSourceLockOrStrengthenedAntiAtomTheoremInput"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
SOURCE_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
EXACT_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
INDEPENDENT_PAIR_L2 = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
COMPLETED_KLS = "ModulusDependentCompletedFullSKLSInput"
HIGH_TAIL = (
    "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
    "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
)
SELF_CONTAINED_DSTRUCTURE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"

SOURCE_FILES = [
    "prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json",
    "prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json",
    "prime-matrix-strict-moving-atom-entropy-normal-form-router.json",
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-actual-source-antiatom-lane-audit-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
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
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书读取到的来源文件哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def make_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def compression_chain() -> list[dict[str, str]]:
    """列出 independent bridge 到具体原子的压缩链。"""
    return [
        {"from": INDEPENDENT_BRIDGE, "to": ACTUAL_BRIDGE},
        {"from": ACTUAL_BRIDGE, "to": f"{SOURCE_ADMISSION} OR {MOVING_ATOM}"},
        {"from": MOVING_ATOM, "to": EXACT_ENTROPY},
        {"from": EXACT_ENTROPY, "to": f"{SEED} AND {INDEPENDENT_PAIR_L2} (if attacked through ExactUV support)"},
        {"from": "parallel", "to": CANONICAL_LOCK},
    ]


def build_rows(
    alpha_return: dict[str, Any],
    bridge_obstruction: dict[str, Any],
    moving_normal: dict[str, Any],
    nonrecursive_guard: dict[str, Any],
    support_seed: dict[str, Any],
    antiatom_audit: dict[str, Any],
    canonical_absorb: dict[str, Any],
) -> list[dict[str, Any]]:
    """同步 independent actual-source 桥的具体原子。"""
    alpha_return_imported = (
        alpha_return.get("terminal_gap_after_router")
        == f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}"
        and alpha_return.get("pointwise_alpha_route_counts_as_well_founded_descent") is False
    )
    bridge_sharp = (
        bridge_obstruction.get("strict_self_contained_terminal_after_router")
        == f"{CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {MOVING_ATOM}"
        and bridge_obstruction.get("actual_source_bridge_theorem_closed") is False
    )
    source_admission_open = bridge_obstruction.get("source_lock_concrete_atom_proved") is False
    moving_to_entropy = (
        moving_normal.get("strict_self_contained_terminal_after_router")
        == f"{CANONICAL_LOCK} OR {EXACT_ENTROPY}"
        and moving_normal.get("moving_atom_entropy_normal_form_closed") is True
    )
    exact_entropy_open = moving_normal.get("exact_clean_core_source_entropy_proved") is False
    pair_loop_blocked = (
        nonrecursive_guard.get("nonrecursive_guard_closed") is True
        and nonrecursive_guard.get("pair_mass_return_loop_detected") is True
        and nonrecursive_guard.get("independent_exact_pair_l2_or_max_atom_bound_proved") is False
    )
    support_seed_open = (
        support_seed.get("acyclic_pre_cauchy_seed_proved") is False
        and support_seed.get("exact_uv_pair_mass_dispersion_proved") is False
    )
    generic_antiatom_refuted = antiatom_audit.get("generic_self_contained_antiatom_refuted") is True
    canonical_scoped_only = (
        canonical_absorb.get("canonical_lock_branch_absorption_closed") is True
        and canonical_absorb.get("acyclic_terminal_canonical_lock_proved") is False
    )
    sync_closed = all(
        [
            alpha_return_imported,
            bridge_sharp,
            source_admission_open,
            moving_to_entropy,
            exact_entropy_open,
            pair_loop_blocked,
            support_seed_open,
            generic_antiatom_refuted,
            canonical_scoped_only,
        ]
    )

    return [
        make_row(
            "AlphaReturnDisciplineImported",
            alpha_return_imported,
            True,
            "上一层已确认 pointwise/alpha 路线是终端回边，independent actual-source 桥必须在进入 alpha 前证明。",
            INDEPENDENT_BRIDGE,
        ),
        make_row(
            "ActualSourceBridgeConcreteAtomsImported",
            bridge_sharp,
            False,
            "actual-source 桥已被具体压成 pre-Cauchy canonical source admission 或 clean-core moving atom exclusion。",
            f"{SOURCE_ADMISSION} OR {MOVING_ATOM}",
        ),
        make_row(
            "SourceAdmissionStillOpen",
            source_admission_open,
            False,
            "源锁定线不能由零行几何、后验覆盖图或 canonical scoped 分支免费推出。",
            SOURCE_ADMISSION,
        ),
        make_row(
            "MovingAtomNormalFormImported",
            moving_to_entropy,
            False,
            "clean-core moving atom 排斥已标准化为 exact clean-core source entropy。",
            EXACT_ENTROPY,
        ),
        make_row(
            "GenericAntiAtomStillRejected",
            generic_antiatom_refuted,
            True,
            "generic/formal WFD 反原子被 moving-delta 模型阻断，不能替代 actual clean-core entropy。",
            EXACT_ENTROPY,
        ),
        make_row(
            "ExactEntropyStillOpen",
            exact_entropy_open,
            False,
            "当前材料尚未证明 actual clean-core full-S non-AP WFD 源满足 max_b M_b/M <= log^{-2A}。",
            EXACT_ENTROPY,
        ),
        make_row(
            "ExactUVSupportRouteNonrecursiveGuardImported",
            pair_loop_blocked,
            True,
            "若通过 ExactUV/pair-mass 证明 exact entropy，不能用 moving-atom/entropy 本身回证 pair mass。",
            INDEPENDENT_PAIR_L2,
        ),
        make_row(
            "SupportBearingSeedAndEnergyStillOpen",
            support_seed_open,
            False,
            "支撑能量形式引理已闭合；未证的是无环 actual source seed 与独立 pair L2/max-atom 能量界。",
            f"{SEED} AND {INDEPENDENT_PAIR_L2}",
        ),
        make_row(
            "CanonicalLockScopedButNotGlobal",
            canonical_scoped_only,
            False,
            "canonical-lock 若五项证书齐备只处理 scoped canonical case；否则不能作为 unrestricted noncanonical 出口。",
            CANONICAL_LOCK,
        ),
        make_row(
            "IndependentBridgeConcreteSyncClosed",
            sync_closed,
            False,
            "当前 independent actual-source 桥的非循环具体原子被钉为 source admission 或 exact entropy；exact entropy 的支撑路线还需独立 seed+能量。",
            f"{CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {EXACT_ENTROPY}",
        ),
        make_row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "尚未证明 source admission、exact entropy、canonical-lock、高段自足尾项或 DStructure/Rankin 替代包。",
            (
                f"({CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {EXACT_ENTROPY}) "
                f"AND ({HIGH_TAIL}) AND {SELF_CONTAINED_DSTRUCTURE}"
            ),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 independent actual-source 桥具体原子同步证书。"""
    alpha_return = load_json("prime-matrix-strict-descent-leaf-firewall-alpha-return-sync-router.json")
    bridge_obstruction = load_json("prime-matrix-strict-actual-source-bridge-terminal-obstruction-router.json")
    moving_normal = load_json("prime-matrix-strict-moving-atom-entropy-normal-form-router.json")
    nonrecursive_guard = load_json("prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json")
    support_seed = load_json("prime-matrix-strict-actual-source-support-seed-router.json")
    antiatom_audit = load_json("prime-matrix-actual-source-antiatom-lane-audit-router.json")
    canonical_absorb = load_json("prime-matrix-strict-canonical-lock-branch-absorption-router.json")

    rows = build_rows(
        alpha_return=alpha_return,
        bridge_obstruction=bridge_obstruction,
        moving_normal=moving_normal,
        nonrecursive_guard=nonrecursive_guard,
        support_seed=support_seed,
        antiatom_audit=antiatom_audit,
        canonical_absorb=canonical_absorb,
    )
    sync_closed = next(row["closed"] for row in rows if row["gate"] == "IndependentBridgeConcreteSyncClosed")
    terminal_after = f"{CANONICAL_LOCK} OR {SOURCE_ADMISSION} OR {EXACT_ENTROPY}"
    strict_basis = (
        f"({terminal_after}) AND ({HIGH_TAIL}) AND {SELF_CONTAINED_DSTRUCTURE}"
    )
    external_high_tail_basis = f"({terminal_after}) AND {SELF_CONTAINED_DSTRUCTURE}"
    conditional_external_basis = (
        f"({terminal_after} OR {COMPLETED_KLS}) AND ({HIGH_TAIL}) AND "
        f"{SELF_CONTAINED_DSTRUCTURE}"
    )
    exact_entropy_internal_basis = f"{SEED} AND {INDEPENDENT_PAIR_L2}"

    return {
        "certificate_type": "prime_matrix_strict_independent_actual_source_bridge_concrete_atom_sync_router",
        "status": "strict_independent_actual_source_bridge_reduced_to_concrete_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "independent_actual_source_bridge_concrete_sync_closed": sync_closed,
        "pointwise_alpha_route_counts_as_well_founded_descent": False,
        "actual_source_bridge_boundary_sharp": True,
        "source_admission_proved": False,
        "moving_atom_entropy_normal_form_closed": True,
        "exact_clean_core_source_entropy_proved": False,
        "pair_mass_return_loop_detected": True,
        "acyclic_pre_cauchy_seed_proved": False,
        "independent_exact_pair_l2_or_max_atom_bound_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": INDEPENDENT_BRIDGE,
        "terminal_gap_after_router": terminal_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "with_external_mertens_high_tail_removed_basis": external_high_tail_basis,
        "conditional_external_math_basis_after_router": conditional_external_basis,
        "exact_entropy_internal_nonrecursive_basis": exact_entropy_internal_basis,
        "next_direct_attack_target": "A1CleanBranchCanonicalSourceAdmission_OR_ExactCleanCoreFullSNonAPWFDSourceEntropy",
        "next_internal_attack_if_exact_entropy": exact_entropy_internal_basis,
        "parallel_attack_targets": [
            CANONICAL_LOCK,
            COMPLETED_KLS,
            SELF_CONTAINED_DSTRUCTURE,
        ],
        "compression_chain": compression_chain(),
        "next_attack_contract": {
            "name": "A1CleanBranchCanonicalSourceAdmission_OR_ExactCleanCoreFullSNonAPWFDSourceEntropy",
            "must_prove": [
                "源锁定线：在 Cauchy/dispersion 前证明 clean A1 分支准入 canonical RIW/Buchstab 决策树源",
                "exact entropy 线：证明 actual clean-core final capacity measure 满足 max_b M_b/M <= log^{-2A}",
                "若 exact entropy 走 ExactUV 支撑路线，必须给无环 pre-Cauchy seed 与独立 pair L2/max-atom 能量界",
                "若走 canonical-lock，必须提交同集推前、有限因子图和无 noncanonical payload 残留",
                "若走外部线，只能标为条件输入 ModulusDependentCompletedFullSKLSInput",
            ],
            "cannot_use_as_proof": [
                "把 pointwise/alpha 回边重新当作下降量",
                "用 zero-row unsigned geometry 反推 signed pre-Cauchy source",
                "用 canonical scoped 分支推出 noncanonical source admission",
                "用 exact entropy 或 moving atom 结论回证 pair-mass 能量界",
                "用 generic/formal WFD 或 fixed projection diffuse 代替 actual moving-block entropy",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续下钻 `IndependentActualSourceBridgeNotFactoredThroughAlphaReturn`。"
            "结合 actual-source 桥终端障碍、moving-atom exact entropy 标准形和非递归守门后，"
            "当前 strict 自足线被压成 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
            "A1CleanBranchCanonicalSourceAdmission OR ExactCleanCoreFullSNonAPWFDSourceEntropy`。"
            "其中 exact entropy 若继续走 ExactUV 支撑路线，必须先给无环 pre-Cauchy seed 与独立 pair L2/max-atom 能量界，"
            "不能用 moving-atom/entropy 结论回证自身。上述三个终端原子均未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict independent actual-source 桥具体原子同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"independent_actual_source_bridge_concrete_sync_closed={fmt_bool(result['independent_actual_source_bridge_concrete_sync_closed'])}",
        f"pointwise_alpha_route_counts_as_well_founded_descent={fmt_bool(result['pointwise_alpha_route_counts_as_well_founded_descent'])}",
        f"source_admission_proved={fmt_bool(result['source_admission_proved'])}",
        f"exact_clean_core_source_entropy_proved={fmt_bool(result['exact_clean_core_source_entropy_proved'])}",
        f"independent_exact_pair_l2_or_max_atom_bound_proved={fmt_bool(result['independent_exact_pair_l2_or_max_atom_bound_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 压缩链",
        "",
        "```text",
    ]
    for item in result["compression_chain"]:
        lines.append(f"{item['from']} -> {item['to']}")

    lines.extend(
        [
            "```",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    contract = result["next_attack_contract"]
    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "若 exact entropy 继续走 ExactUV 支撑路线，内部非递归基为：",
            "",
            "```text",
            result["exact_entropy_internal_nonrecursive_basis"],
            "```",
            "",
            "若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "条件外部线可写为：",
            "",
            "```text",
            result["conditional_external_math_basis_after_router"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            f"下一数学主攻点：`{contract['name']}`。",
            "",
            "必须证明：",
        ]
    )
    for item in contract["must_prove"]:
        lines.append(f"- {item}。")

    lines.extend(["", "不能作为证明使用："])
    for item in contract["cannot_use_as_proof"]:
        lines.append(f"- {item}。")

    lines.append("")
    return "\n".join(lines)


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


if __name__ == "__main__":
    main()
