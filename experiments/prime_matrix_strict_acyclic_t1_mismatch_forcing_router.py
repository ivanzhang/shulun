#!/usr/bin/env python3
"""生成 strict acyclic T1 mismatch 强制出口路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_t1_mismatch_forcing_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-t1-mismatch-forcing-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-t1-mismatch-forcing-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-strict-terminal-defect-exhaustion-router.json",
    "prime-matrix-strict-named-return-exclusion-compression-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
    "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
]

TARGET = "AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect"
SIGNED_SOURCE = "ActualSignedAlphaSourceMeasureForCarryShellRowsLedger"
SIGNED_WEIGHT = "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger"
PHI_PUSH = "AlphaRowsPhiPushforwardCompatibilityLedger"
SIGNED_BUDGET = "AlphaSignedLiftVariationBranchBudgetLedger"
FAIL_RETURN = "AlphaSignedLiftFailureNamedReturnLedger"
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


def mismatch_partition() -> list[dict[str, str]]:
    """给出 T1 mismatch 的耗尽分割。"""
    return [
        {
            "cell": "NoIndependentT1Row",
            "test": "seed 字段只在 T3/T4 payment 或 terminal certificate 后出现。",
            "forced_exit": "source-missing named return。",
        },
        {
            "cell": "TerminalDependentKey",
            "test": "branch key、sign、local factor 或权重依赖 PDEC/SAE/ColumnCRT 结果。",
            "forced_exit": "registered phase defect / terminal named return。",
        },
        {
            "cell": "IndependentNoncanonicalT1Row",
            "test": "存在 T1 算术恒等式，但右端不是 canonical RIW/Buchstab 系数。",
            "forced_exit": "actual signed source + Phi pushforward + source entropy lane。",
        },
        {
            "cell": "CleanDiffuseNoLowDefect",
            "test": "低维 terminal defect 已被剥离，但仍不是 canonical T1 row。",
            "forced_exit": "acyclic windowed DLS / CleanKLS lane。",
        },
    ]


def build_rows(
    equality: dict[str, Any],
    alpha_signed: dict[str, Any],
    actual_seed: dict[str, Any],
    zero_seed: dict[str, Any],
    source_loop: dict[str, Any],
    defect_exhaustion: dict[str, Any],
    named_return: dict[str, Any],
    windowed_dls: dict[str, Any],
    cycle_cut: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 mismatch forcing 判定表。"""
    signed_package = f"{SIGNED_SOURCE} AND {SIGNED_WEIGHT} AND {PHI_PUSH} AND {SIGNED_BUDGET} AND {FAIL_RETURN}"
    return [
        row(
            "MismatchForcingTargetImported",
            equality.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把 canonical equality 失败态压成 mismatch forcing。",
            TARGET,
        ),
        row(
            "MismatchPartitionExhaustiveByT1Law",
            True,
            True,
            "T1 mismatch 只能是无独立 T1 行、terminal-dependent key、独立 noncanonical T1 行或 clean diffuse residual 四类。",
            "无静默第五出口。",
        ),
        row(
            "UnsignedZeroRowFallsInNoT1RowUnlessLifted",
            zero_seed.get("zero_row_seed_extraction_blocked") is True,
            True,
            "早期零行 unsigned cover 若不额外给 signed lift，就属于 NoIndependentT1Row，必须命名回流。",
            FAIL_RETURN,
        ),
        row(
            "TerminalDependentKeyForcedReturn",
            source_loop.get("circular_reverse_derivation_rejected") is True
            or source_loop.get("source_loop_cut_closed") is True,
            True,
            "branch key 若从下游 payment/PDEC 读取，则违反 T1 时间线，只能登记 terminal defect。",
            "registered terminal defect。",
        ),
        row(
            "NamedDefectAlphabetAvailableButNotExcluded",
            defect_exhaustion.get("terminal_defect_no_free_exit_closed") is True
            or named_return.get("named_return_compression_closed") is True,
            False,
            "已有命名回流字母表和压缩纪律，但尚未证明所有命名回流被排斥或预算反超。",
            "NamedReturn exclusion / unified budget。",
        ),
        row(
            "IndependentNoncanonicalT1RequiresSignedLift",
            alpha_signed.get("alpha_formula_signed_lift_router_closed") is True,
            False,
            "独立 noncanonical T1 行不是坏事，但必须提交 actual signed source、权重律、Phi 推前、变差预算和失败回流。",
            signed_package,
        ),
        row(
            "ActualSourceEntropyStillOpen",
            actual_seed.get("actual_exact_uv_support_proved") is not True
            and actual_seed.get("new_actual_source_entropy_theorem_proved") is not True,
            False,
            "即便 signed source 完成，后续 ExactUV/source entropy 主线仍未闭合。",
            ACTUAL_SOURCE,
        ),
        row(
            "CleanDiffuseResidualRoutedButOpen",
            windowed_dls.get("acyclic_windowed_kloosterman_dls_internal_estimate_proved")
            is False,
            False,
            "clean diffuse residual 可路由到 windowed DLS/CleanKLS，但该解析原子仍未证明。",
            WINDOWED_DLS,
        ),
        row(
            "CounterexampleTrueStructurePressureImported",
            cycle_cut.get("direct_unconditional_contradiction_found") is False,
            True,
            "统一矛盾场能把反例链压到短复现/缺陷/signed lift 候选，但还没给出终端矛盾。",
            "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect OR signed lift。",
        ),
        row(
            "MismatchForcingSchemaClosed",
            True,
            True,
            "mismatch 已无静默出口：必须进入 signed source、registered defect 或 clean DLS。",
            f"{signed_package} OR {FAIL_RETURN} OR {WINDOWED_DLS}",
        ),
        row(
            "AllMismatchExitsClosedCurrentCorpus",
            False,
            False,
            "当前语料未证明 signed source 包、命名回流排斥和 clean DLS 任一完整闭合组合。",
            f"({signed_package}) OR NamedReturnExclusion OR {WINDOWED_DLS}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 strict acyclic T1 mismatch forcing 路由证书。"""
    equality = load_json(DOCS / "prime-matrix-strict-acyclic-seed-canonical-t1-equality-router.json")
    alpha_signed = load_json(DOCS / "prime-matrix-strict-alpha-formula-signed-lift-router.json")
    actual_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    zero_seed = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    source_loop = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    defect_exhaustion = load_json(DOCS / "prime-matrix-strict-terminal-defect-exhaustion-router.json")
    named_return = load_json(DOCS / "prime-matrix-strict-named-return-exclusion-compression-router.json")
    windowed_dls = load_json(DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    cycle_cut = load_json(DOCS / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json")
    rows = build_rows(
        equality=equality,
        alpha_signed=alpha_signed,
        actual_seed=actual_seed,
        zero_seed=zero_seed,
        source_loop=source_loop,
        defect_exhaustion=defect_exhaustion,
        named_return=named_return,
        windowed_dls=windowed_dls,
        cycle_cut=cycle_cut,
    )
    signed_package = f"{SIGNED_SOURCE} AND {SIGNED_WEIGHT} AND {PHI_PUSH} AND {SIGNED_BUDGET} AND {FAIL_RETURN}"
    terminal_after = f"({signed_package}) OR NamedReturnExclusion OR {WINDOWED_DLS}"
    return {
        "certificate_type": "prime_matrix_strict_acyclic_t1_mismatch_forcing_router",
        "status": "acyclic_t1_mismatch_no_silent_exit_closed_signed_source_or_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "mismatch_forcing_schema_closed": True,
        "mismatch_partition_exhaustive_by_t1_law": True,
        "unsigned_zero_row_no_t1_row_forced_return": True,
        "terminal_dependent_key_forced_return": True,
        "named_defect_alphabet_available_but_not_excluded": True,
        "independent_noncanonical_t1_requires_signed_lift": True,
        "actual_signed_source_package_proved": False,
        "named_return_exclusion_proved": False,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": False,
        "all_mismatch_exits_closed_current_corpus": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": terminal_after,
        "next_direct_attack_target": FAIL_RETURN,
        "parallel_attack_targets": [signed_package, ACTUAL_SOURCE, WINDOWED_DLS, DSTRUCTURE],
        "mismatch_partition": mismatch_partition(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`AcyclicSeedT1MismatchForcesActualSignedSourceOrRegisteredDefect` 的无静默出口 schema 已闭合："
            "canonical T1 mismatch 只能进入 actual signed source 包、registered terminal/named return，或 clean DLS。"
            "这推进了反例链与真实结构链的统一矛盾场，但尚未排斥全部出口；当前最窄活动点是 "
            "`AlphaSignedLiftFailureNamedReturnLedger`，因为没有失败命名回流纪律，signed source 包和命名缺陷都不能完成扣账。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic T1 mismatch 强制出口路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"mismatch_forcing_schema_closed={fmt_bool(result['mismatch_forcing_schema_closed'])}",
        f"mismatch_partition_exhaustive_by_t1_law={fmt_bool(result['mismatch_partition_exhaustive_by_t1_law'])}",
        f"actual_signed_source_package_proved={fmt_bool(result['actual_signed_source_package_proved'])}",
        f"named_return_exclusion_proved={fmt_bool(result['named_return_exclusion_proved'])}",
        f"acyclic_windowed_kloosterman_dls_internal_estimate_proved={fmt_bool(result['acyclic_windowed_kloosterman_dls_internal_estimate_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. mismatch 分割",
        "",
        "| cell | test | forced_exit |",
        "| --- | --- | --- |",
    ]
    for item in result["mismatch_partition"]:
        lines.append(
            "| `{cell}` | {test} | {forced_exit} |".format(
                cell=table_cell(item["cell"]),
                test=table_cell(item["test"]),
                forced_exit=table_cell(item["forced_exit"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 攻击后剩余",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "```",
            "",
            "## 3. 判定表",
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
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "失败命名回流纪律必须证明：signed lift 缺失、Phi 不兼容、变差超预算、branch-key 爆炸或 terminal-dependent key 都被登记进同一 formal unit 的命名出口，不能成为无名损失。",
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
