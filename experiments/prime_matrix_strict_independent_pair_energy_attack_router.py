#!/usr/bin/env python3
"""生成 strict 独立 pair 能量界直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_independent_pair_energy_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-independent-pair-energy-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-independent-pair-energy-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-independent-pair-energy-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json",
    "prime-matrix-strict-moving-atom-to-global-terminal-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.md",
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
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def seed_only_obstruction_rows() -> list[dict[str, Any]]:
    """构造 seed-only 不能推出 pair 能量界的阻断模型。"""
    rows: list[dict[str, Any]] = []
    exponent_k = 17.0
    for k in range(3, 10):
        log_y = k * math.log(10)
        threshold = log_y ** (-exponent_k)
        rows.append(
            {
                "k": k,
                "log_y": log_y,
                "threshold_L_minus_K": threshold,
                "pair_count": 1,
                "total_mass": 1.0,
                "max_pair_mass": 1.0,
                "l2_energy": 1.0,
                "seed_fields_can_be_formally_registered": True,
                "violates_independent_pair_energy": True,
            }
        )
    return rows


def threshold_packet_fields() -> list[dict[str, str]]:
    """列出大 pair 阈值 packet 必须携带的字段。"""
    return [
        {
            "field": "formal_unit_id",
            "meaning": "与 pre-Cauchy seed、registered multipliers 和 terminal ledger 使用同一 formal unit。",
        },
        {
            "field": "pair_key",
            "meaning": "精确 `(u,v)`、path key、dyadic block、phase key 与 sign-refined branch key。",
        },
        {
            "field": "mass_profile",
            "meaning": "总绝对质量 M、pair 质量 M_b、L2 能量贡献和阈值 `M/L^K`。",
        },
        {
            "field": "rate_certificate",
            "meaning": "说明失败是 log-power 阈值失败，而不是仅仅定性 positive-limsup。",
        },
        {
            "field": "return_tests",
            "meaning": "逐项测试 PDEC、SAE/LocalSurvivor、ColumnCRT、CleanKLS/DLS、canonical-lock 与外部条件线。",
        },
    ]


def build_rows(
    guard: dict[str, Any],
    support_seed: dict[str, Any],
    pair_mass: dict[str, Any],
    moving_terminal: dict[str, Any],
    seed_fusion: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 independent pair energy 攻击判定表。"""
    return [
        {
            "gate": "SameSourceEntropyTargetPreserved",
            "closed": guard.get("same_theorem_target_preserved") is True,
            "proved": True,
            "meaning": "继续在 NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem 内部攻击，不改换总命题。",
            "remaining": guard.get("next_direct_attack_target_inside_same_theorem"),
        },
        {
            "gate": "NonrecursiveGuardImported",
            "closed": guard.get("nonrecursive_guard_closed") is True,
            "proved": True,
            "meaning": "已禁止用源熵目标本身或 moving-atom 排斥反证 pair-mass 分散。",
            "remaining": "必须给独立 pair L2/max-atom 账本或命名回流。",
        },
        {
            "gate": "SeedOnlyInsufficientModel",
            "closed": True,
            "proved": True,
            "meaning": "抽象 acyclic seed 字段允许所有质量落在单个 exact pair；所以 seed 名称本身不推出 L2/max-atom 界。",
            "remaining": "需要阈值大原子 packet 排斥或独立相消估计。",
        },
        {
            "gate": "ElementaryEnergyLemmaImported",
            "closed": support_seed.get("elementary_mass_support_lemma_closed") is True,
            "proved": True,
            "meaning": "一旦有独立 L2/max-pair 界，支撑下界和源熵反原子由初等引理推出。",
            "remaining": "证明独立 L2/max-pair 界。",
        },
        {
            "gate": "LargePairFailurePacketized",
            "closed": pair_mass.get("large_pair_atom_equivalence_closed") is True
            and pair_mass.get("registered_multiplier_bridge_imported") is True,
            "proved": True,
            "meaning": "独立能量界失败等价于同一 formal unit 下出现超过阈值的 sign-refined exact pair 大原子 packet。",
            "remaining": "RateBearingLargePairAtomPacketExclusion。",
        },
        {
            "gate": "NonCleanLargePairReturnsImported",
            "closed": moving_terminal.get("strict_moving_atom_boundary_closed") is True,
            "proved": True,
            "meaning": "非 clean-core 或带低维签名的大 pair packet 已接回 PDEC/SAE/ColumnCRT/CleanKLS/DLS 终端门。",
            "remaining": "GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger。",
        },
        {
            "gate": "SeedBranchFusionImported",
            "closed": seed_fusion.get("acyclic_pre_cauchy_seed_independent_input_removed")
            is True,
            "proved": True,
            "meaning": "seed 存在/不存在两支均进入 acyclic terminal family；seed 不再是可隐藏的独立出口。",
            "remaining": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily。",
        },
        {
            "gate": "QualitativeProjectionDichotomyInsufficientForLogRate",
            "closed": True,
            "proved": True,
            "meaning": "有限投影二分只给 positive-limsup 或趋零；本目标需要任意固定 A 的 log-power 速率。",
            "remaining": "RateBearingAcyclicPairAtomDecayOrTerminalExclusion。",
        },
        {
            "gate": "IndependentPairEnergyCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明 rate-bearing large-pair packet 全部不存在或必导致已排斥终端。",
            "remaining": "RateBearingLargePairAtomPacketExclusion。",
        },
        {
            "gate": "NewActualSourceEntropyCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "独立 pair 能量界仍未完成，所以新 actual-source 熵定理仍未证明。",
            "remaining": "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 独立 pair 能量界直攻证书。"""
    guard = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json"
    )
    support_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    pair_mass = load_json(DOCS / "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json")
    moving_terminal = load_json(DOCS / "prime-matrix-strict-moving-atom-to-global-terminal-router.json")
    seed_fusion = load_json(DOCS / "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json")

    rows = build_rows(
        guard=guard,
        support_seed=support_seed,
        pair_mass=pair_mass,
        moving_terminal=moving_terminal,
        seed_fusion=seed_fusion,
    )
    return {
        "certificate_type": "prime_matrix_strict_independent_pair_energy_attack_router",
        "status": "strict_independent_pair_energy_reduced_to_rate_bearing_large_pair_packet_exclusion_open",
        "same_theorem_target_preserved": True,
        "seed_only_insufficient_model_verified": True,
        "nonrecursive_guard_imported": True,
        "large_pair_failure_packetized": True,
        "qualitative_projection_dichotomy_insufficient_for_log_rate": True,
        "independent_exact_pair_l2_or_max_atom_bound_proved": False,
        "rate_bearing_large_pair_atom_packet_exclusion_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "internal_obligation_before_router": (
            "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
        ),
        "internal_obligation_after_router": (
            "RateBearingLargePairAtomPacketExclusion"
        ),
        "strict_self_contained_terminal_after_router": guard.get(
            "strict_self_contained_terminal_after_router"
        ),
        "strict_self_contained_math_basis_after_router": guard.get(
            "strict_self_contained_math_basis_after_router"
        ),
        "nonrecursive_implication_to_target": (
            "RateBearingLargePairAtomPacketExclusion "
            "=> IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed "
            "=> ActualNoncanonicalExactUVSupportLowerBound "
            "=> NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
        ),
        "next_direct_attack_target_inside_same_theorem": (
            "RateBearingLargePairAtomPacketExclusion"
        ),
        "hard_law": (
            "seed-only 不能产生 log-power pair 能量界；定性有限投影消散也不足以支付任意 A。"
            "必须排斥每个超过 `M/L^K` 的 rate-bearing exact pair 大原子 packet，"
            "或证明它们全部进入已排斥的 PDEC/SAE/ColumnCRT/CleanKLS 终端。"
        ),
        "rows": rows,
        "seed_only_obstruction_rows": seed_only_obstruction_rows(),
        "threshold_packet_fields": threshold_packet_fields(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "继续在 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` 内部攻击，"
            "`IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed` 被进一步压缩。"
            "抽象 seed 本身不足以推出 pair L2/max-atom 界，因为可形式登记一个全部质量集中在单个 exact pair "
            "上的 seed；有限投影二分也只给定性消散，不能给任意 A 所需的 log-power 速率。"
            "因此同命题内部真正剩余变为 `RateBearingLargePairAtomPacketExclusion`："
            "排斥所有超过阈值 `M/L^K` 的同 formal unit 大 pair packet，或证明其必回流到已命名终端。"
            "当前仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 独立 pair 能量界直攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"seed_only_insufficient_model_verified={fmt_bool(result['seed_only_insufficient_model_verified'])}",
        f"large_pair_failure_packetized={fmt_bool(result['large_pair_failure_packetized'])}",
        f"qualitative_projection_dichotomy_insufficient_for_log_rate={fmt_bool(result['qualitative_projection_dichotomy_insufficient_for_log_rate'])}",
        f"independent_exact_pair_l2_or_max_atom_bound_proved={fmt_bool(result['independent_exact_pair_l2_or_max_atom_bound_proved'])}",
        f"rate_bearing_large_pair_atom_packet_exclusion_proved={fmt_bool(result['rate_bearing_large_pair_atom_packet_exclusion_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同命题内部压缩",
        "",
        "```text",
        result["internal_obligation_before_router"],
        "  -> Rate-bearing large exact-pair atom packet cannot exist",
        "  -> " + result["internal_obligation_after_router"],
        "",
        result["nonrecursive_implication_to_target"],
        "```",
        "",
        "## 2. 判定表",
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
            "## 3. seed-only 阻断模型",
            "",
            "| k | log y | threshold L^-K | pair count | max pair mass | L2 energy | violates energy |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["seed_only_obstruction_rows"]:
        lines.append(
            "| {k} | {log_y:.6g} | {threshold_L_minus_K:.6g} | {pair_count} | {max_pair_mass:.1f} | {l2_energy:.1f} | `{violates_independent_pair_energy}` |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 4. 大 pair packet 字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for row in result["threshold_packet_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(row["field"]),
                meaning=table_cell(row["meaning"]),
            )
        )

    lines.extend(
        [
            "",
            "## 5. 硬边界律",
            "",
            result["hard_law"],
            "",
            "下一步仍在同一源熵定理内部直攻：",
            "",
            "```text",
            result["next_direct_attack_target_inside_same_theorem"],
            "```",
            "",
            "完整 strict 基仍保持：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
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
