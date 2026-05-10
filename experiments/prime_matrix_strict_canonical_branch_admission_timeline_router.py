#!/usr/bin/env python3
"""生成 strict canonical branch pre-Cauchy 准入时间线守门证书。

用法示例：
  python3 experiments/prime_matrix_strict_canonical_branch_admission_timeline_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-canonical-branch-admission-timeline-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-canonical-branch-admission-timeline-router.json"
OUT_MD = DOCS / "prime-matrix-strict-canonical-branch-admission-timeline-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-acyclic-canonical-lock-router.json",
    "prime-matrix-strict-acyclic-seed-canonical-embedding-router.json",
    "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
    "prime-matrix-strict-canonical-lock-branch-absorption-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-triad-a1-canonical-branch-admission-router.json",
    "prime-matrix-triad-a1-source-lock-contract-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-precauchy-declaration-line-router.json",
    "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
]

TARGET = "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy"
CANONICAL_IDENTITY = "AcyclicCanonicalPreCauchyCoefficientIdentityLedger"
ACTUAL_SOURCE = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def timeline_layers() -> list[dict[str, str]]:
    """给出 canonical 准入的时间层。"""
    return [
        {
            "layer": "T0",
            "name": "CRT wheel and early-zero hypothesis",
            "allowed": "只给位置、同余斜线、镜像和覆盖压力。",
            "forbidden": "不能直接声明 signed canonical coefficient。",
        },
        {
            "layer": "T1",
            "name": "pre-Cauchy coefficient declaration",
            "allowed": "必须在这里声明 RIW/Buchstab canonical 系数恒等式、formal unit 和 branch key。",
            "forbidden": "不得依赖 Cauchy 选择、terminal payment、PDEC 缺陷或后验投影。",
        },
        {
            "layer": "T2",
            "name": "Cauchy / dispersion / Type-Fourier processing",
            "allowed": "只处理已经登记的 T1 系数。",
            "forbidden": "不能在处理后补造 T1 来源。",
        },
        {
            "layer": "T3",
            "name": "terminal extraction and payment skeleton",
            "allowed": "可登记缺陷、same-set 推前和容量比较。",
            "forbidden": "不能反向生成 canonical branch admission。",
        },
        {
            "layer": "T4",
            "name": "PDEC / SAE / ColumnCRT / CleanKLS returns",
            "allowed": "作为命名回流或外部/内部估计分支。",
            "forbidden": "不能冒充 pre-Cauchy canonical source。",
        },
    ]


def build_rows(
    direct_pdec: dict[str, Any],
    seed_embedding: dict[str, Any],
    canonical_exit: dict[str, Any],
    branch_absorb: dict[str, Any],
    source_loop: dict[str, Any],
    a1_admission: dict[str, Any],
    actual_seed: dict[str, Any],
    declaration_line: dict[str, Any],
    cycle_cut: dict[str, Any],
    windowed_dls: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 pre-Cauchy 准入时间线判定表。"""
    seed_gap = seed_embedding.get("seed_embedding_gap_after_router", "")
    return [
        row(
            "SameCounterexampleDisciplinePreserved",
            True,
            True,
            "本步仍在假设早期零行存在的反例链内部工作，不用真实缺席、统计样本或 runner 输出替代证明。",
            "direct_unconditional_contradiction_found=false。",
        ),
        row(
            "DirectPDECSendsBackToCanonicalLock",
            direct_pdec.get("next_direct_attack_target")
            == "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
            True,
            "direct acyclic same-set PDEC 已被作用域审计压回 canonical-lock 作用域匹配。",
            TARGET,
        ),
        row(
            "TargetIsFirstSeedEmbeddingAtom",
            TARGET in seed_gap,
            False,
            "AcyclicSeedCanonicalSourceFiniteFactorEmbedding 的第一个必要子原子正是 pre-Cauchy canonical branch 准入。",
            TARGET,
        ),
        row(
            "TimelineAdmissionLawClosed",
            True,
            True,
            "canonical 准入若合法，必须在 Cauchy/dispersion/terminal extraction 前声明；下游证书只能消费该声明，不能生成该声明。",
            CANONICAL_IDENTITY,
        ),
        row(
            "A1CanonicalBranchScopedOnly",
            a1_admission.get("canonical_source_branch_is_legal_subcase") is True
            or a1_admission.get("internal_canonical_branch_closed_conditionally") is True,
            True,
            "A1 canonical branch 是合法子分支；但它只在对象已于 T1 声明为 RIW/Buchstab canonical source 时可用。",
            "不能把 generic/noncanonical seed 静默升级为 canonical。",
        ),
        row(
            "DownstreamRecoveryRejected",
            source_loop.get("circular_reverse_derivation_rejected") is True
            or source_loop.get("source_loop_cut_closed") is True,
            True,
            "从早期零行覆盖图、payment skeleton、terminal certificate、有限投影或当前 PDEC 前沿反推 source 会落入来源环。",
            "必须提交独立 T1 账本。",
        ),
        row(
            "CanonicalExitFiveLedgerStillOpen",
            canonical_exit.get("acyclic_canonical_exact_same_set_promotion_certificate_proved")
            is False,
            False,
            "canonical-lock 非循环出口仍缺五项 exact same-set 证书，尤其缺 pre-Cauchy coefficient identity。",
            canonical_exit.get("canonical_exact_certificate_definition", CANONICAL_IDENTITY),
        ),
        row(
            "CanonicalBranchAbsorptionNotGlobalContradiction",
            branch_absorb.get("canonical_lock_standalone_global_contradiction") is False,
            True,
            "五项证书若成立，只给 canonical-source scoped promotion；证书不成立时 canonical-lock 不可用。",
            ACTUAL_SOURCE,
        ),
        row(
            "ActualSourceSeedDoesNotProveCanonicalAdmission",
            actual_seed.get("actual_exact_uv_support_proved") is not True,
            True,
            "actual noncanonical seed/ExactUV 支撑属于 noncanonical 主线，不能反向证明 canonical branch admission。",
            "若不提交 canonical T1 身份，只能回到 actual-source 熵或 clean DLS。",
        ),
        row(
            "PreCauchyDeclarationLineForNoncanonicalSeparated",
            declaration_line.get("pre_cauchy_constructor_declaration_line_proved") is False,
            True,
            "noncanonical declaration line 的合法义务已另行分类；它不能填 canonical RIW/Buchstab 身份表。",
            "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger。",
        ),
        row(
            "CounterexampleTrueStructureGivesPressureNotSignedSource",
            cycle_cut.get("direct_unconditional_contradiction_found") is False,
            True,
            "斜线覆盖、镜像、P 列锚和层叠筛形成结构压力，但目前只给 unsigned 形状，不能直接生成 T1 signed canonical 系数。",
            "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR signed lift。",
        ),
        row(
            "CleanDLSFallbackStillAnalyticOpen",
            windowed_dls.get("acyclic_windowed_kloosterman_dls_internal_estimate_proved")
            is False,
            False,
            "若 seed 不可 canonical 准入，clean residual 的自足出口仍是窗口化 Kloosterman/DLS 内部估计。",
            WINDOWED_DLS,
        ),
        row(
            "AcyclicSeedCanonicalBranchAdmissionCurrentCorpusProved",
            False,
            False,
            "当前语料没有独立提交 T1 canonical coefficient identity ledger，因此不能证明本原子。",
            f"{CANONICAL_IDENTITY} OR {ACTUAL_SOURCE} OR {WINDOWED_DLS}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict canonical branch pre-Cauchy 准入时间线守门证书。"""
    direct_pdec = load_json(DOCS / "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json")
    seed_embedding = load_json(DOCS / "prime-matrix-strict-acyclic-seed-canonical-embedding-router.json")
    canonical_exit = load_json(
        DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
    )
    branch_absorb = load_json(DOCS / "prime-matrix-strict-canonical-lock-branch-absorption-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    a1_admission = load_json(DOCS / "prime-matrix-triad-a1-canonical-branch-admission-router.json")
    actual_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    declaration_line = load_json(DOCS / "prime-matrix-strict-precauchy-declaration-line-router.json")
    cycle_cut = load_json(DOCS / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json")
    windowed_dls = load_json(DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")

    rows = build_rows(
        direct_pdec=direct_pdec,
        seed_embedding=seed_embedding,
        canonical_exit=canonical_exit,
        branch_absorb=branch_absorb,
        source_loop=source_loop,
        a1_admission=a1_admission,
        actual_seed=actual_seed,
        declaration_line=declaration_line,
        cycle_cut=cycle_cut,
        windowed_dls=windowed_dls,
    )
    terminal_after = f"{CANONICAL_IDENTITY} OR {ACTUAL_SOURCE} OR {WINDOWED_DLS}"

    return {
        "certificate_type": "prime_matrix_strict_canonical_branch_admission_timeline_router",
        "status": "canonical_branch_admission_timeline_guard_closed_precauchy_identity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "canonical_branch_admission_timeline_guard_closed": True,
        "timeline_admission_law_closed": True,
        "downstream_recovery_rejected": True,
        "a1_canonical_branch_scoped_only": True,
        "canonical_branch_absorption_not_global_contradiction": True,
        "counterexample_true_structure_pressure_not_signed_source": True,
        "acyclic_canonical_precauchy_coefficient_identity_ledger_proved": False,
        "acyclic_seed_canonical_branch_admission_before_cauchy_proved": False,
        "acyclic_seed_finite_factor_map_weight_identity_proved": False,
        "acyclic_seed_no_source_replacement_proved": False,
        "acyclic_canonical_exact_same_set_promotion_certificate_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": terminal_after,
        "next_direct_attack_target": CANONICAL_IDENTITY,
        "parallel_attack_targets": [
            ACTUAL_SOURCE,
            WINDOWED_DLS,
            DSTRUCTURE,
        ],
        "admission_timeline_layers": timeline_layers(),
        "required_precauchy_identity_ledger_fields": [
            "same formal_unit_id fixed before Cauchy/dispersion",
            "canonical RIW/Buchstab coefficient formula declared before terminal payment",
            "branch key independent of downstream PDEC/SAE/ColumnCRT outcomes",
            "weight/sign law equal to canonical source law, not merely hash-stable",
            "bad-window set and same-set pushforward consume the T1 source without changing it",
        ],
        "rejected_proof_patterns": [
            "从早期零行覆盖图直接反推 signed canonical 系数",
            "从 terminal certificate 或 payment skeleton 反推 pre-Cauchy source",
            "用 canonical-source 已闭合结论证明当前 seed 已 canonical",
            "用 formal_unit hash stability 替代测度因子与系数恒等式",
            "用 actual noncanonical ExactUV/source-entropy 路线冒充 canonical branch admission",
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接攻击 `AcyclicSeedCanonicalBranchAdmissionBeforeCauchy`。结构结论是："
            "canonical branch admission 是时间线门，而不是可由终端证书倒推的覆盖事实。"
            "若要走 canonical-lock，必须在 Cauchy/dispersion/terminal extraction 之前提交同一 formal unit 的 "
            "`AcyclicCanonicalPreCauchyCoefficientIdentityLedger`。现有早期零行几何、P 列锚、层叠筛、"
            "payment skeleton、PDEC/SAE 前沿和 formal-unit hash stability 都不能替代该 T1 身份账本。"
            "因此本轮关闭了准入时间线审查，但没有证明 canonical 准入，也没有得到反例链与真实链的无条件终端矛盾。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict canonical branch 准入时间线守门路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"canonical_branch_admission_timeline_guard_closed={fmt_bool(result['canonical_branch_admission_timeline_guard_closed'])}",
        f"timeline_admission_law_closed={fmt_bool(result['timeline_admission_law_closed'])}",
        f"downstream_recovery_rejected={fmt_bool(result['downstream_recovery_rejected'])}",
        f"acyclic_canonical_precauchy_coefficient_identity_ledger_proved={fmt_bool(result['acyclic_canonical_precauchy_coefficient_identity_ledger_proved'])}",
        f"acyclic_seed_canonical_branch_admission_before_cauchy_proved={fmt_bool(result['acyclic_seed_canonical_branch_admission_before_cauchy_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"acyclic_windowed_kloosterman_dls_internal_estimate_proved={fmt_bool(result['acyclic_windowed_kloosterman_dls_internal_estimate_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 时间线",
        "",
        "| layer | name | allowed | forbidden |",
        "| --- | --- | --- | --- |",
    ]
    for layer in result["admission_timeline_layers"]:
        lines.append(
            "| `{layer}` | {name} | {allowed} | {forbidden} |".format(
                layer=table_cell(layer["layer"]),
                name=table_cell(layer["name"]),
                allowed=table_cell(layer["allowed"]),
                forbidden=table_cell(layer["forbidden"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 收缩公式",
            "",
            "攻击前：",
            "",
            "```text",
            result["terminal_gap_before_router"],
            "```",
            "",
            "攻击后：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "```",
            "",
            "## 3. 必要 T1 账本字段",
            "",
        ]
    )
    for item in result["required_precauchy_identity_ledger_fields"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 4. 被排除的证明模式",
            "",
        ]
    )
    for item in result["rejected_proof_patterns"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 6. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "若该 T1 canonical identity 不能独立提交，canonical-lock 路线不能继续承担闭合作用；非 canonical 主线必须回到 actual-source 熵定理或 acyclic windowed DLS/CleanKLS 解析原子。",
        ]
    )
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


if __name__ == "__main__":
    main()
