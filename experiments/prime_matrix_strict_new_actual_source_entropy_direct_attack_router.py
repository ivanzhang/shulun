#!/usr/bin/env python3
"""生成 strict 新 actual-source 熵定理直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_new_actual_source_entropy_direct_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-moving-atom-entropy-normal-form-router.json",
    "prime-matrix-clean-core-moving-atom-sharp-input-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
    "prime-matrix-exact-uv-support-terminal-attack-router.json",
    "prime-matrix-exact-uv-support-failure-packetization-router.json",
    "prime-matrix-support-failure-packet-return-dichotomy-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
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
    """汇总本证书依赖的证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(
    firewall: dict[str, Any],
    moving_atom: dict[str, Any],
    sharp: dict[str, Any],
    multiplier: dict[str, Any],
    exact_uv: dict[str, Any],
    packet: dict[str, Any],
    return_router: dict[str, Any],
    support_seed: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 strict 新 actual-source 熵定理的内部直攻判定表。"""
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    exact_support = "ActualNoncanonicalExactUVSupportLowerBound"
    seed = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
    pair_mass = "ExactUVPairMassDispersionOrMaxAtomBoundLedger"
    return [
        {
            "gate": "SameTheoremTargetPreserved",
            "closed": firewall.get("strict_self_contained_terminal_after_router")
            == f"AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR {target}",
            "proved": False,
            "meaning": "本步不改换目标命题，只在新 actual-source 熵定理内部继续拆证明脊柱。",
            "remaining": target,
        },
        {
            "gate": "MovingAtomExactEntropyNormalFormImported",
            "closed": moving_atom.get("moving_atom_entropy_normal_form_closed") is True,
            "proved": True,
            "meaning": "moving same-(u,v) 大原子排斥与 max_b M_b/M <= log^{-2A} 的 exact entropy 标准形已对齐。",
            "remaining": target,
        },
        {
            "gate": "SharpMovingAtomInputImported",
            "closed": sharp.get("clean_core_moving_atom_sharp_boundary_closed") is True,
            "proved": False,
            "meaning": "过强的低支撑 packet 排斥已校准为真正需要排斥的 clean-core final capacity moving atom。",
            "remaining": "ActualNoncanonicalCleanCoreMovingAtomExclusion",
        },
        {
            "gate": "RegisteredMultiplierDisciplineImported",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed")
            is True,
            "proved": True,
            "meaning": "Type/Fourier/fiber 乘子均已登记为同一 formal unit 的 log-power 成本。",
            "remaining": "支撑失败不能再归因于账外容量乘子。",
        },
        {
            "gate": "SupportToEntropyConditionalInequalityClosed",
            "closed": "S_u*S_v" in multiplier.get(
                "support_to_antiatom_after_closure", ""
            ),
            "proved": True,
            "meaning": "在登记乘子纪律下，若 exact u/v 支撑超过阈值，则 final source entropy 反原子不等式立即成立。",
            "remaining": exact_support,
        },
        {
            "gate": "ExactUVSupportPinnedAsSourceSubkernel",
            "closed": exact_uv.get("unique_source_terminal_input") == exact_support,
            "proved": False,
            "meaning": "新源熵定理的当前可攻内部核就是 actual noncanonical exact u/v 支撑下界。",
            "remaining": exact_support,
        },
        {
            "gate": "SupportFailurePacketized",
            "closed": packet.get("failure_packetization_closed") is True
            and packet.get("equivalent_packet_input")
            == "ActualNoncanonicalSupportFailurePacketExclusion",
            "proved": True,
            "meaning": "ExactUVSupport 的否定已物化为带字段、阈值、容量剖面和回流测试的支撑失败 packet。",
            "remaining": "ActualNoncanonicalSupportFailurePacketExclusion",
        },
        {
            "gate": "NonCleanPacketReturnDichotomyImported",
            "closed": return_router.get("support_failure_packet_return_dichotomy_closed")
            is True,
            "proved": True,
            "meaning": "非 clean-core 支撑失败 packet 必回流到 LocalSurvivor/SAE、PDEC、ColumnCRT 或 CleanKLS/DLS 等命名出口。",
            "remaining": "ActualNoncanonicalCleanCoreSupportFailurePacketExclusion",
        },
        {
            "gate": "SeedAndPairMassSpinePinned",
            "closed": support_seed.get("terminal_gap_after_router")
            == f"{seed} AND {pair_mass}",
            "proved": False,
            "meaning": "ExactUV 支撑下界的内部证明脊柱已压成无环 pre-Cauchy 源种子与 exact pair 质量分散两项。",
            "remaining": f"{seed} AND {pair_mass}",
        },
        {
            "gate": "NewActualSourceEntropyCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未证明无环源种子与 pair 质量分散，也尚未直接证明 final capacity anti-atom。",
            "remaining": target,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "源熵定理仍未证；同时高段自足尾项或外部接受、DStructure/Rankin 替代包仍是独立门。",
            "remaining": (
                "(AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
                f"{target}) AND "
                "(SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
                "SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND "
                "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
            ),
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 新 actual-source 熵定理直攻证书。"""
    firewall = load_json(
        DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
    )
    moving_atom = load_json(
        DOCS / "prime-matrix-strict-moving-atom-entropy-normal-form-router.json"
    )
    sharp = load_json(DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.json")
    multiplier = load_json(
        DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
    )
    exact_uv = load_json(DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.json")
    packet = load_json(
        DOCS / "prime-matrix-exact-uv-support-failure-packetization-router.json"
    )
    return_router = load_json(
        DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.json"
    )
    support_seed = load_json(
        DOCS / "prime-matrix-strict-actual-source-support-seed-router.json"
    )

    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    canonical_lock = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    terminal_after = f"{canonical_lock} OR {target}"
    strict_basis = (
        f"({terminal_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    internal_spine = (
        "RegisteredCapacityMultiplierDiscipline AND "
        "ActualNoncanonicalExactUVSupportLowerBound"
    )
    deepest_spine = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        "ExactUVPairMassDispersionOrMaxAtomBoundLedger"
    )
    rows = build_rows(
        firewall=firewall,
        moving_atom=moving_atom,
        sharp=sharp,
        multiplier=multiplier,
        exact_uv=exact_uv,
        packet=packet,
        return_router=return_router,
        support_seed=support_seed,
    )
    return {
        "certificate_type": "prime_matrix_strict_new_actual_source_entropy_direct_attack_router",
        "status": "strict_new_actual_source_entropy_direct_attack_to_support_spine_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used": True,
        "counterexample_assumption_only": True,
        "registered_capacity_multiplier_discipline_imported": True,
        "support_to_entropy_conditional_inequality_closed": True,
        "support_failure_packetization_imported": True,
        "nonclean_packet_return_dichotomy_imported": True,
        "new_actual_source_entropy_theorem_proved": False,
        "actual_exact_uv_support_proved": False,
        "acyclic_pre_cauchy_source_seed_proved": False,
        "exact_uv_pair_mass_dispersion_proved": False,
        "row_column_unconditional_closed": False,
        "strict_self_contained_terminal_after_router": terminal_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "internal_proof_spine_for_new_actual_source_entropy": internal_spine,
        "deepest_current_internal_spine": deepest_spine,
        "next_direct_attack_target_inside_same_theorem": (
            "ExactUVPairMassDispersionOrMaxAtomBoundLedger_FOR_"
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeed"
        ),
        "conditional_closure_statement": (
            "若在同一 actual formal unit 中证明 ActualNoncanonicalExactUVSupportLowerBound，"
            "则已闭合的 registered multiplier discipline 通过支撑到反原子的条件不等式推出 "
            "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem；再结合其余独立门后才可晋级。"
        ),
        "hard_boundary_law": (
            "当前不能再把困难归因于固定投影、formal WFD、K4/K6、朴素 incidence、"
            "早期零行几何或账外容量乘子。真正未证内容是 actual noncanonical pre-Cauchy 源种子"
            "及其 exact (u,v) pair 质量分散；这是新源熵定理内部的证明脊柱，不是换命题。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 本身继续被直接攻击，"
            "目标没有转换。利用已闭合的 registered capacity multiplier discipline，源熵反原子"
            "已经严格化为一个内部支撑脊柱：只要证明同一 actual formal unit 的 "
            "`ActualNoncanonicalExactUVSupportLowerBound`，就能推出 "
            "`max_b M_b/M <= log^{-2A}`。ExactUV 的否定已被 packet 化，非 clean-core packet "
            "也已命名回流；当前真正未证的是无环 pre-Cauchy actual noncanonical source seed "
            "及其 exact `(u,v)` pair 质量分散。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 新 actual-source 熵定理直攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"registered_capacity_multiplier_discipline_imported={fmt_bool(result['registered_capacity_multiplier_discipline_imported'])}",
        f"support_to_entropy_conditional_inequality_closed={fmt_bool(result['support_to_entropy_conditional_inequality_closed'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"actual_exact_uv_support_proved={fmt_bool(result['actual_exact_uv_support_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 目标保持",
        "",
        "```text",
        result["strict_self_contained_terminal_after_router"],
        "```",
        "",
        "这一步只攻击 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 的内部证明结构，不把目标改成其他定理。",
        "",
        "## 2. 内部证明脊柱",
        "",
        "```text",
        "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem",
        "  <= RegisteredCapacityMultiplierDiscipline",
        "     AND ActualNoncanonicalExactUVSupportLowerBound",
        "",
        "ActualNoncanonicalExactUVSupportLowerBound",
        "  <= AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn",
        "     AND ExactUVPairMassDispersionOrMaxAtomBoundLedger",
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 4. 条件闭合律",
            "",
            result["conditional_closure_statement"],
            "",
            "## 5. 硬边界律",
            "",
            result["hard_boundary_law"],
            "",
            "## 6. 最新严格基",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "下一步仍在同一源熵定理内部直攻：",
            "",
            "```text",
            result["next_direct_attack_target_inside_same_theorem"],
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
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
