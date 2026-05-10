#!/usr/bin/env python3
"""最终推广审计后的 ExactUV 源侧剩余压缩。

用法示例：
  python3 experiments/prime_matrix_strict_exact_uv_after_final_promotion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-exact-uv-after-final-promotion-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-exact-uv-after-final-promotion-router.json"
OUT_MD = MONO / "prime-matrix-strict-exact-uv-after-final-promotion-router.md"

FINAL_AUDIT = MONO / "prime-matrix-strict-rks23-final-promotion-audit-router.json"
EXACT_TERMINAL = MONO / "prime-matrix-exact-uv-support-terminal-attack-router.json"
CLEAN_CORE = MONO / "prime-matrix-clean-core-support-incidence-attack-router.json"
FIBER_ATOM = MONO / "prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.json"
SOURCE_ENTROPY = MONO / "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json"

SOURCE_FILES = [FINAL_AUDIT, EXACT_TERMINAL, CLEAN_CORE, FIBER_ATOM, SOURCE_ENTROPY]

EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
CLEAN_CORE_TRANSFER = "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn"
FIBER_DISPERSION = "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
DSTRUCTURE_REPLACEMENT = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
ROW_COLUMN = "RowColumnUnconditionalTheoremFinalPromotion"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def build_result() -> dict[str, Any]:
    """构造 ExactUV 下一层压缩证书。"""
    final_audit = load_json(FINAL_AUDIT)
    exact_terminal = load_json(EXACT_TERMINAL)
    clean_core = load_json(CLEAN_CORE)
    fiber_atom = load_json(FIBER_ATOM)
    source_entropy = load_json(SOURCE_ENTROPY)

    final_audit_ready = all(
        [
            final_audit.get("author_side_rks23_energy_lane_closed") is True,
            final_audit.get("actual_exact_uv_support_closed") is False,
            final_audit.get("next_direct_attack_target")
            == "CleanCoreTerminalSupportIncidenceTheorem_FOR_ActualNoncanonicalExactUVSupportLowerBound",
        ]
    )
    exact_terminal_boundary_closed = exact_terminal.get("exact_uv_support_terminal_boundary_closed") is True
    clean_core_boundary_closed = clean_core.get("clean_core_support_incidence_attack_boundary_closed") is True
    fiber_atom_pinned = fiber_atom.get("terminal_gap_after_router") == FIBER_DISPERSION
    source_entropy_spine_imported = (
        source_entropy.get("status") == "strict_new_actual_source_entropy_direct_attack_to_support_spine_open"
    )

    false_exit_blockers_closed = all(
        [
            exact_terminal_boundary_closed,
            clean_core_boundary_closed,
            fiber_atom.get("seed_only_formal_proof_blocked") is True,
            fiber_atom.get("signed_cancellation_only_rejected") is True,
            fiber_atom.get("terminal_packetization_forbidden_for_this_proof") is True,
        ]
    )

    exact_uv_reduced_to_fiber_dispersion = all(
        [final_audit_ready, false_exit_blockers_closed, fiber_atom_pinned, source_entropy_spine_imported]
    )
    clean_core_exact_layer_transfer_closed = False
    preterminal_exact_uv_fiber_absolute_mass_dispersion_proved = False
    actual_noncanonical_exact_uv_support_closed = False
    row_column_unconditional_closed = False

    reduction_chain = {
        "from_final_audit": "after RNRS, the author-side mathematical blocker is ActualNoncanonicalExactUVSupportLowerBound",
        "terminal_boundary": "registered multiplier discipline is closed; failure cannot be charged to Type/Fourier/fiber bookkeeping",
        "blocked_false_exits": "raw Buchstab counting, K4/K6, naive incidence, canonical support import, signed-only cancellation, and terminal packetization are all insufficient",
        "clean_core_gate": "ExactUV support requires clean-core exact layer admission and nonzero transfer in the actual noncanonical source",
        "atomic_reformulation": "the sharp source-side form is an absolute mass cap on each pre-terminal exact (u,v) fiber",
        "current_atom": FIBER_DISPERSION,
    }

    rows = [
        row(
            "FinalAuditReady",
            final_audit_ready,
            True,
            "最终推广审计已确认 RNRS 不再是阻断项，ExactUV 成为作者侧数学阻断项。",
            EXACT_UV,
        ),
        row(
            "ExactUVTerminalBoundaryClosed",
            exact_terminal_boundary_closed,
            True,
            "ExactUV 终端边界、乘子纪律和 canonical 偷渡阻断已闭合。",
            EXACT_UV,
        ),
        row(
            "CleanCoreSupportIncidenceBoundaryClosed",
            clean_core_boundary_closed,
            True,
            "clean-core 支撑关联的错误方向已排除。",
            CLEAN_CORE_TRANSFER,
        ),
        row(
            "FalseExitBlockersClosed",
            false_exit_blockers_closed,
            True,
            "seed-only、signed-only、terminal packetization 等伪出口均已排除。",
            FIBER_DISPERSION,
        ),
        row(
            "ExactUVReducedToPreterminalFiberDispersion",
            exact_uv_reduced_to_fiber_dispersion,
            True,
            "ExactUV 当前最窄作者侧数学原子已压成 pre-terminal exact fiber 绝对质量分散。",
            FIBER_DISPERSION,
        ),
        row(
            "CleanCoreExactLayerTransferClosed",
            clean_core_exact_layer_transfer_closed,
            False,
            "clean-core exact 层承认与非零转移仍未证明。",
            CLEAN_CORE_TRANSFER,
        ),
        row(
            "PreTerminalExactUVFiberAbsoluteMassDispersionProved",
            preterminal_exact_uv_fiber_absolute_mass_dispersion_proved,
            False,
            "pre-Cauchy actual source 的 exact fiber 绝对质量分散仍未证明。",
            FIBER_DISPERSION,
        ),
        row(
            "ActualNoncanonicalExactUVSupportClosed",
            actual_noncanonical_exact_uv_support_closed,
            False,
            "ExactUV 支撑下界仍未闭合。",
            EXACT_UV,
        ),
        row(
            "RowColumnUnconditionalClosed",
            row_column_unconditional_closed,
            False,
            "ExactUV 与 DStructure 自足替代/独立验收未完成前，行/列命题仍不能闭合。",
            f"{EXACT_UV} AND {DSTRUCTURE_REPLACEMENT}",
        ),
    ]

    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    return {
        "certificate_type": "strict_exact_uv_after_final_promotion_router",
        "status": "exact_uv_reduced_to_preterminal_absolute_fiber_mass_dispersion_open",
        "final_audit_ready": final_audit_ready,
        "exact_terminal_boundary_closed": exact_terminal_boundary_closed,
        "clean_core_boundary_closed": clean_core_boundary_closed,
        "source_entropy_spine_imported": source_entropy_spine_imported,
        "false_exit_blockers_closed": false_exit_blockers_closed,
        "exact_uv_reduced_to_fiber_dispersion": exact_uv_reduced_to_fiber_dispersion,
        "clean_core_exact_layer_transfer_closed": clean_core_exact_layer_transfer_closed,
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved": preterminal_exact_uv_fiber_absolute_mass_dispersion_proved,
        "actual_noncanonical_exact_uv_support_closed": actual_noncanonical_exact_uv_support_closed,
        "row_column_unconditional_closed": row_column_unconditional_closed,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "counterexample_assumption_only": True,
        "reduction_chain": reduction_chain,
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "remaining_atoms": [
            {
                "atom": FIBER_DISPERSION,
                "closed": False,
                "why_remaining": "must prove an absolute mass cap on each actual pre-Cauchy exact (u,v) fiber without terminal packet return or signed-only cancellation",
            },
            {
                "atom": DSTRUCTURE_REPLACEMENT,
                "closed": False,
                "why_remaining": "after ExactUV, strict self-contained closure still needs a promotion replacement unless independent acceptance is supplied",
            },
        ],
        "next_direct_attack_target": FIBER_DISPERSION,
        "next_required_input": "Absolute mass dispersion for actual pre-Cauchy source over exact (u,v) fibers",
        "plain_conclusion": (
            "ExactUV 的当前最窄作者侧原子已压成 pre-terminal exact (u,v) fiber 的绝对质量分散。"
            "这一步没有证明分散；它删除了错误出口并固定下一主攻点。"
        ),
        "source_hashes": source_hashes(),
        "rows": rows,
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict ExactUV 最终推广后压缩证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(
        "本步接在最终推广审计之后，继续下钻 ExactUV。"
        "结论是：ExactUV 不能由 raw 计数、canonical 支撑、K4/K6、signed cancellation 或 terminal packetization 偷渡；"
        "当前最窄作者侧数学原子是 actual pre-Cauchy source 在 exact `(u,v)` fiber 上的绝对质量分散。"
    )
    lines.append("")
    lines.append("```text")
    for key in [
        "exact_uv_reduced_to_fiber_dispersion",
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved",
        "actual_noncanonical_exact_uv_support_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 压缩链")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    for key, value in result["reduction_chain"].items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.append("")
    lines.append("## 2. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=item["gate"],
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.append("")
    lines.append("## 3. 下一真正自足目标")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_direct_attack_target"])
    lines.append(result["next_required_input"])
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    MONO.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"exact_uv_reduced_to_fiber_dispersion={fmt_bool(result['exact_uv_reduced_to_fiber_dispersion'])}")
    print(
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved="
        f"{fmt_bool(result['preterminal_exact_uv_fiber_absolute_mass_dispersion_proved'])}"
    )
    print(f"actual_noncanonical_exact_uv_support_closed={fmt_bool(result['actual_noncanonical_exact_uv_support_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
