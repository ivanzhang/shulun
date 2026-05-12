#!/usr/bin/env python3
"""生成 strict nonterminal exact-UV fiber 非集中直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_nonterminal_fiber_aperiodicity_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-preterminal-support-capacity-attack-router.json",
    "prime-matrix-strict-independent-pair-energy-attack-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-fulls-kls-movingblock-joint-attack-router.json",
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


def build_rows(
    support_capacity: dict[str, Any],
    pair_energy: dict[str, Any],
    support_seed: dict[str, Any],
    zero_seed: dict[str, Any],
    loop_cut: dict[str, Any],
    joint_attack: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 fiber 非集中直攻判定表。"""
    target = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
    atom = "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
    return [
        {
            "gate": "NonterminalFiberAperiodicityTargetActive",
            "closed": support_capacity.get("terminal_gap_after_router") == target,
            "proved": False,
            "meaning": "上一层已把 pre-terminal 支撑/容量定理压成 exact (u,v) fiber 非集中估计。",
            "remaining": target,
        },
        {
            "gate": "SeedOnlyModelBlocksFormalProof",
            "closed": pair_energy.get("seed_only_insufficient_model_verified") is True,
            "proved": True,
            "meaning": "抽象 seed 字段本身允许全部质量集中到单个 exact pair，不能推出 fiber 非集中。",
            "remaining": atom,
        },
        {
            "gate": "SignedCancellationNotEnoughForAbsoluteCapacity",
            "closed": True,
            "proved": True,
            "meaning": "source capacity 使用 fiber 绝对质量；只证明带符号和有相消，不足以排除同一 fiber 内绝对质量集中。",
            "remaining": "absolute fiber mass dispersion, not only signed cancellation。",
        },
        {
            "gate": "SourceObjectCannotBeRecoveredFromZeroRowGeometry",
            "closed": zero_seed.get("zero_row_seed_extraction_blocked") is True
            and loop_cut.get("source_loop_cut_closed") is True,
            "proved": True,
            "meaning": "早期零行覆盖、斜线/圆柱/轮筛几何和 downstream payment 图不能反推 pre-Cauchy source 对象。",
            "remaining": "source object must be declared upstream。",
        },
        {
            "gate": "ElementarySupportLemmaAlreadyImported",
            "closed": support_seed.get("elementary_mass_support_lemma_closed") is True,
            "proved": True,
            "meaning": "若 absolute fiber mass dispersion 成立，支撑下界和 source entropy 已由初等链条给出。",
            "remaining": atom,
        },
        {
            "gate": "ExternalKLSWouldBeDifferentLane",
            "closed": joint_attack.get("external_lane_proved_or_cited_in_current_corpus")
            is False,
            "proved": True,
            "meaning": "外部 Full-S KLS/dispersion 可作条件线，但不是 strict 自足 nonterminal fiber 证明。",
            "remaining": atom,
        },
        {
            "gate": "TerminalPacketizationForbiddenHere",
            "closed": support_capacity.get("terminal_exactuv_routes_rejected_as_nonterminal_proof")
            is True,
            "proved": True,
            "meaning": "把大 fiber 打包后再送 PDEC/CleanKLS 会回到固定点；当前目标必须是源侧直接估计。",
            "remaining": atom,
        },
        {
            "gate": "AbsoluteFiberDispersionAtomPinned",
            "closed": True,
            "proved": False,
            "meaning": "最新最窄数学原子是 actual pre-Cauchy source 在 exact (u,v) fiber 上的绝对质量分散定理。",
            "remaining": atom,
        },
        {
            "gate": "PreTerminalExactUVFiberAbsoluteMassDispersionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未证明该绝对 fiber 质量分散定理。",
            "remaining": atom,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict nonterminal exact-UV fiber 非集中直攻证书。"""
    support_capacity = load_json(
        DOCS / "prime-matrix-strict-preterminal-support-capacity-attack-router.json"
    )
    pair_energy = load_json(DOCS / "prime-matrix-strict-independent-pair-energy-attack-router.json")
    support_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    zero_seed = load_json(DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json")
    loop_cut = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")
    joint_attack = load_json(DOCS / "prime-matrix-fulls-kls-movingblock-joint-attack-router.json")

    target = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
    atom = "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
    rows = build_rows(
        support_capacity=support_capacity,
        pair_energy=pair_energy,
        support_seed=support_seed,
        zero_seed=zero_seed,
        loop_cut=loop_cut,
        joint_attack=joint_attack,
    )
    return {
        "certificate_type": "prime_matrix_strict_nonterminal_fiber_aperiodicity_attack_router",
        "status": "strict_nonterminal_exact_uv_fiber_aperiodicity_reduced_to_absolute_mass_dispersion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "nonterminal_fiber_aperiodicity_attack_closed": True,
        "seed_only_formal_proof_blocked": True,
        "signed_cancellation_only_rejected": True,
        "zero_row_geometry_source_recovery_blocked": True,
        "terminal_packetization_forbidden_for_this_proof": True,
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved": False,
        "nonterminal_exact_uv_fiber_aperiodicity_proved": False,
        "preterminal_actual_fulls_factor_support_capacity_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": atom,
        "next_direct_attack_target": atom,
        "absolute_mass_dispersion_contract": (
            "For the actual pre-Cauchy source measure before any terminal extraction, "
            "disintegrated over exact (u,v) fibers in one formal unit, prove an absolute "
            "mass cap M_{u,v}^{abs} <= M^{abs}/L^K or the equivalent absolute L2 fiber energy bound. "
            "The proof may not use terminal packet return, canonical branch import, or signed-only cancellation."
        ),
        "hard_law": (
            "当前不是证明 signed exponential cancellation，而是证明 absolute source mass 不集中在单个 exact fiber。"
            "CRT/轮筛刚性和早期零行覆盖只约束位置；source identity 只给对象；相消只给带符号和。"
            "要推出 source entropy，必须直接证明 pre-terminal exact fiber 的绝对质量分散。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource` 继续被压缩为更精确的绝对质量命题："
            "`PreTerminalExactUVFiberAbsoluteMassDispersionTheorem`。这不是换命题，而是排除 signed-only、seed-only、"
            "CRT/轮筛位置刚性和终端 packet 回流后的同一源熵核心。该绝对 fiber 分散定理尚未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict nonterminal exact-UV fiber 非集中直攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"nonterminal_fiber_aperiodicity_attack_closed={fmt_bool(result['nonterminal_fiber_aperiodicity_attack_closed'])}",
        f"seed_only_formal_proof_blocked={fmt_bool(result['seed_only_formal_proof_blocked'])}",
        f"signed_cancellation_only_rejected={fmt_bool(result['signed_cancellation_only_rejected'])}",
        f"terminal_packetization_forbidden_for_this_proof={fmt_bool(result['terminal_packetization_forbidden_for_this_proof'])}",
        f"preterminal_exact_uv_fiber_absolute_mass_dispersion_proved={fmt_bool(result['preterminal_exact_uv_fiber_absolute_mass_dispersion_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩",
        "",
        "压缩前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "压缩后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "绝对质量分散合同：",
        "",
        "```text",
        result["absolute_mass_dispersion_contract"],
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
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 结构结论",
            "",
            result["hard_law"],
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
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
