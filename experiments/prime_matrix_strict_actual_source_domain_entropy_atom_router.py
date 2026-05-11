#!/usr/bin/env python3
"""生成 actual pre-Cauchy source domain 绝对熵原子化证书。

用法示例：
  python3 experiments/prime_matrix_strict_actual_source_domain_entropy_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-actual-source-domain-entropy-atom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
OUT_MD = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json",
    "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
]

TARGET = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
SIGNED_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
ROW_SUPPORT = "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger"
ENTROPY_PACKAGE = "ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger"
EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
DSTRUCTURE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
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
    """登记依赖文件哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    preterminal_atom: dict[str, Any],
    incidence_entropy: dict[str, Any],
    support_seed: dict[str, Any],
    row_origin: dict[str, Any],
    seed_emitter: dict[str, Any],
    unsigned_skeleton: dict[str, Any],
    alpha_weight_law: dict[str, Any],
    pointwise_weight: dict[str, Any],
    multiplier: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 source-domain entropy 原子化判定表。"""
    target_active = preterminal_atom.get("next_direct_attack_target") == TARGET
    incidence_aligned = "ActualEmitterSourceDomainEntropyLedger" in str(
        incidence_entropy.get("terminal_gap_after_router", "")
    )
    support_seed_aligned = (
        support_seed.get("terminal_gap_after_router")
        == "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND ExactUVPairMassDispersionOrMaxAtomBoundLedger"
    )
    row_table_reduced_to_seed = row_origin.get("next_direct_attack_target") == EMITTER
    seed_reduced_to_signed_law = seed_emitter.get("next_direct_attack_target") == SIGNED_LAW
    unsigned_skeleton_closed = unsigned_skeleton.get("alpha_row_unsigned_skeleton_router_closed") is True
    weight_law_open = alpha_weight_law.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False
    pointwise_weight_open = (
        pointwise_weight.get("primitive_summand_signed_weight_expression_proved") is False
    )
    multiplier_closed = multiplier.get("registered_capacity_multiplier_discipline_closed") is True

    return [
        row(
            "ActualSourceDomainEntropyTargetActive",
            target_active,
            False,
            "上一层已把 preterminal fiber 分散源域包的第一优先项定为 actual pre-Cauchy source domain 绝对熵。",
            TARGET,
        ),
        row(
            "EmitterIncidenceEntropyAligned",
            incidence_aligned,
            False,
            "actual emitter incidence 路线同样把有界重数拆成 source-domain entropy 与 fixed-pair fiber bound。",
            "ActualEmitterSourceDomainEntropyLedger",
        ),
        row(
            "SupportSeedPairMassSpineImported",
            support_seed_aligned,
            False,
            "ExactUV 支撑路线已说明：没有无环 pre-Cauchy source seed，任何 pair-mass 或 row-mass 熵都没有对象。",
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn",
        ),
        row(
            "RowLevelOriginTableReducedToSeedEmitter",
            row_table_reduced_to_seed,
            False,
            "逐行原始生成表必须由无环 seed 自带 signed row emitter 产生，不能从 payment 或零行覆盖反推。",
            EMITTER,
        ),
        row(
            "SeedEmitterReducedToSignedCoefficientLaw",
            seed_reduced_to_signed_law,
            False,
            "在合法 seed 分支内，真正缺口是每条 primitive row 的 signed coefficient law。",
            SIGNED_LAW,
        ),
        row(
            "UnsignedSkeletonAvailableButNotEntropy",
            unsigned_skeleton_closed,
            True,
            "source tuple、carry-shell、P列锚和层叠轮筛给出 unsigned row skeleton；它只定位候选行，不给绝对质量熵。",
            SIGNED_LAW,
        ),
        row(
            "RegisteredMultiplierGivesOnlyRowWeightScale",
            multiplier_closed,
            True,
            "登记乘子纪律控制单行权重尺度的 log 成本，但不证明有足够多非零 signed rows。",
            ROW_SUPPORT,
        ),
        row(
            "DeterministicRowEntropyImplicationClosed",
            True,
            True,
            "若 signed row emitter 给出同 formal unit 的 N 个非零 primitive rows，且行权重可比或满足 L2/no-heavy-row，则 source domain absolute entropy 由 M^2/E2 或 max-row 形式推出。",
            f"{EMITTER} AND {ROW_MASS} AND {ROW_SUPPORT}",
        ),
        row(
            "AlphaWeightLawStillOpen",
            weight_law_open,
            False,
            "alpha signed 权重律仍未由独立 pre-Cauchy 算术恒等式和精确权重公式证明。",
            SIGNED_LAW,
        ),
        row(
            "PointwiseSignedWeightExpressionStillOpen",
            pointwise_weight_open,
            False,
            "逐行 signed alpha 权重公式仍缺 actual noncanonical primitive summand signed expression before pushforward。",
            "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward",
        ),
        row(
            "RowMassNormalizationCurrentCorpusProved",
            False,
            False,
            "当前材料没有在同一 row table 中证明总绝对质量、单行上界、L2 行能量和零权重回流。",
            ROW_MASS,
        ),
        row(
            "PrimitiveRowSupportLowerBoundCurrentCorpusProved",
            False,
            False,
            "当前材料没有证明发射前 primitive row 支撑数达到所需 log-power 阈值。",
            ROW_SUPPORT,
        ),
        row(
            "ActualSourceDomainEntropyCurrentCorpusProved",
            False,
            False,
            "signed row emitter、row-mass normalization 与 row support 下界未合取证明，源域绝对熵仍未闭合。",
            ENTROPY_PACKAGE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "ExactUV 源域包、complete key、fixed-key multiplicity 与 DStructure/Rankin 独立门未完成前，行/列命题不能闭合。",
            f"{EXACT_UV} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 actual source-domain entropy 原子化证书。"""
    preterminal_atom = load_json(
        DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
    )
    incidence_entropy = load_json(
        DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"
    )
    support_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    row_origin = load_json(DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.json")
    seed_emitter = load_json(DOCS / "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json")
    unsigned_skeleton = load_json(DOCS / "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json")
    alpha_weight_law = load_json(DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json")
    pointwise_weight = load_json(
        DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"
    )
    multiplier = load_json(DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json")

    rows = build_rows(
        preterminal_atom=preterminal_atom,
        incidence_entropy=incidence_entropy,
        support_seed=support_seed,
        row_origin=row_origin,
        seed_emitter=seed_emitter,
        unsigned_skeleton=unsigned_skeleton,
        alpha_weight_law=alpha_weight_law,
        pointwise_weight=pointwise_weight,
        multiplier=multiplier,
    )
    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    entropy_atoms = [
        {
            "atom": EMITTER,
            "proved": False,
            "role": "先正向生成 actual noncanonical primitive rows，并给出推前前 signed 求和恒等式。",
        },
        {
            "atom": ROW_MASS,
            "proved": False,
            "role": "在同一 row table 中登记总绝对质量、单行上界、L2 行能量和零权重命名回流。",
        },
        {
            "atom": ROW_SUPPORT,
            "proved": False,
            "role": "证明发射前非零 primitive row 支撑达到可推出源域绝对熵的 log-power 阈值。",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_actual_source_domain_entropy_atom_router",
        "status": "strict_actual_source_domain_entropy_reduced_to_signed_row_mass_entropy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "actual_source_domain_entropy_atomization_closed": True,
        "deterministic_row_entropy_implication_closed": True,
        "actual_precauchy_source_domain_absolute_entropy_ledger_proved": False,
        "acyclic_seed_signed_row_emitter_rule_proved": False,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "primitive_row_support_lower_bound_proved": False,
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved": False,
        "actual_noncanonical_exact_uv_support_closed": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": ENTROPY_PACKAGE,
        "next_direct_attack_target": SIGNED_LAW,
        "failure_return_if_no_signed_rows": TERMINAL_RETURN,
        "entropy_atoms": entropy_atoms,
        "deterministic_implication": (
            "Let R be the nonzero primitive rows emitted before pushforward in one actual formal unit, "
            "with absolute row weights a_r. If M=sum_R a_r>0, either max_r a_r<=M/L^K "
            "or sum_R a_r^2<=M^2/L^K, then the effective source-domain support is at least L^K. "
            "Thus ActualPreCauchySourceDomainAbsoluteEntropyLedger reduces to a signed row emitter "
            "plus row-mass normalization and row-support lower bound. Unsigned geometry can index R, "
            "but cannot supply the signed weights a_r."
        ),
        "hard_law": (
            "源域绝对熵是发射前 row-mass 命题，不是 exact `(u,v)` 映射后的支撑命题。"
            "P列锚、斜线覆盖、圆柱螺旋和 layered-wheel 只给 unsigned skeleton；"
            "登记乘子只给单行成本；真正缺口是合法 seed 分支内的 signed coefficient law，"
            "以及同一表内的 no-heavy-row/L2 行质量账本。"
        ),
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ActualPreCauchySourceDomainAbsoluteEntropyLedger` 已被压成 signed row-mass entropy 包："
            "必须先由无环 pre-Cauchy actual noncanonical seed 正向发射 signed primitive rows，"
            "再证明同一 formal unit 中的 row-mass normalization/no-heavy-row 与 row support 下界。"
            "当前最窄可攻单点是 `AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward`。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict actual source-domain entropy 原子化证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
    ]
    for key in [
        "same_theorem_target_preserved",
        "no_theorem_switch",
        "actual_source_domain_entropy_atomization_closed",
        "deterministic_row_entropy_implication_closed",
        "actual_precauchy_source_domain_absolute_entropy_ledger_proved",
        "acyclic_seed_signed_row_emitter_rule_proved",
        "acyclic_seed_primitive_row_signed_coefficient_law_proved",
        "same_formal_unit_row_mass_normalization_proved",
        "primitive_row_support_lower_bound_proved",
        "actual_noncanonical_exact_uv_support_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.extend(
        [
            "```",
            "",
            "## 1. 当前压缩",
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
            "## 2. 熵原子包",
            "",
            "| atom | proved | role |",
            "| --- | --- | --- |",
        ]
    )
    for atom in result["entropy_atoms"]:
        lines.append(
            "| `{atom}` | `{proved}` | {role} |".format(
                atom=atom["atom"],
                proved=fmt_bool(atom["proved"]),
                role=table_cell(atom["role"]),
            )
        )
    lines.extend(
        [
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
                gate=item["gate"],
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 确定性蕴含",
            "",
            "```text",
            result["deterministic_implication"],
            "```",
            "",
            "## 5. 结构律",
            "",
            result["hard_law"],
            "",
            "## 6. 下一真正单点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["failure_return_if_no_signed_rows"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
