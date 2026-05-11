#!/usr/bin/env python3
"""生成 preterminal exact-UV fiber 分散的源域原子化证书。

用法示例：
  python3 experiments/prime_matrix_strict_preterminal_fiber_dispersion_source_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
OUT_MD = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-exact-uv-after-final-promotion-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
    "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json",
    "prime-matrix-strict-emitter-multiplicity-rank-attack-router.json",
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
]

EXACT_UV = "ActualNoncanonicalExactUVSupportLowerBound"
FIBER_ABS = "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
SOURCE_RANK_PACKAGE = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
DSTRUCTURE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，兼容未归档的历史工作树材料。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书参考过的可用证据哈希。"""
    hashes: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            hashes[f"docs/monograph/{name}"] = sha256(path)
    return hashes


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
    exact_uv_after: dict[str, Any],
    multiplier: dict[str, Any],
    absolute_router: dict[str, Any],
    rank_router: dict[str, Any],
    fixed_pair: dict[str, Any],
    complete_key: dict[str, Any],
    source_table: dict[str, Any],
    kernel_identity: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成源域原子化判定表。"""
    target_active = (
        exact_uv_after.get("next_direct_attack_target") == FIBER_ABS
        or exact_uv_after.get("exact_uv_reduced_to_fiber_dispersion") is True
    )
    capacity_closed = multiplier.get("registered_capacity_multiplier_discipline_closed") is True
    absolute_optional_seen = absolute_router.get("terminal_gap_before_router") == FIBER_ABS
    rank_optional_seen = (
        rank_router.get("terminal_gap_after_router")
        == "PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem"
    )
    fixed_pair_formal_seen = fixed_pair.get("deterministic_key_fiber_inequality_closed") is True
    complete_key_open = (
        complete_key.get("registered_complete_primitive_emitter_key_partition_polylog_proved")
        is False
    )
    source_table_open = (
        source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False
    )
    kernel_table_open = kernel_identity.get("pointwise_primitive_kernel_table_proved") is False

    return [
        row(
            "PreTerminalFiberDispersionTargetActive",
            target_active,
            False,
            "最终推广后 ExactUV 的作者侧核心已经压到 preterminal exact `(u,v)` fiber 绝对质量分散。",
            FIBER_ABS,
        ),
        row(
            "RegisteredCapacityMultiplierImported",
            capacity_closed,
            True,
            "Type/Fourier/fiber/系数等乘子已登记到同一 formal unit；它们只提供 log-power 成本账本。",
            EXACT_UV,
        ),
        row(
            "OptionalAbsoluteToMultiplicityFrontierSeen",
            absolute_optional_seen,
            False,
            "历史工作树中已有把绝对质量问题转成 primitive emitter 原像 multiplicity 的草稿路由；本证书只吸收其结构，不把它当作最终证明。",
            "PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem",
        ),
        row(
            "OptionalRankNoCollapseFrontierSeen",
            rank_optional_seen,
            False,
            "历史工作树中已有把 multiplicity 继续压到 exact-UV map rank/no-collapse 的草稿路由；当前仍未证明。",
            "PreCauchyEmitterExactUVMapRankAndNoFiberCollapseTheorem",
        ),
        row(
            "DeterministicSourceAtomImplicationClosed",
            True,
            True,
            "若同一源表同时给出源域绝对熵、complete key 多对数分区、固定 key 下 exact-UV 局部 O(1) 重数，则按 key 求和立即得到每个 `(u,v)` 的绝对质量上界。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "FixedPairFormalInequalityRecognized",
            fixed_pair_formal_seen,
            True,
            "fixed-pair 形式不等式本身只是代数求和：key 数乘以固定 key 局部重数给出 fiber 上界。",
            f"{COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "ActualSourceDomainEntropyCurrentCorpusProved",
            False,
            False,
            "当前材料尚未给出 actual pre-Cauchy source 域的绝对质量熵账本；没有该账本，O(1) 原像也不能转成总质量小比例。",
            DOMAIN_ENTROPY,
        ),
        row(
            "CompletePrimitiveEmitterKeyPartitionCurrentCorpusProved",
            not complete_key_open and complete_key.get("registered_complete_primitive_emitter_key_partition_polylog_proved")
            is True,
            False,
            "complete key 必须在发射前登记 formal unit、branch path、exact `(u,v)`、sign/local factor 和 truncation 状态；当前未证明。",
            COMPLETE_KEY,
        ),
        row(
            "FixedKeyExactUVLocalMultiplicityCurrentCorpusProved",
            False,
            False,
            "当前材料尚未证明固定 complete key 与固定 exact `(u,v)` 下只有 O(1) 个 actual primitive source 原像。",
            FIXED_KEY_MULT,
        ),
        row(
            "ActualPrimitiveSourceTableStillUpstreamOpen",
            not source_table_open
            and source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is True,
            False,
            "若没有 actual noncanonical primitive emitter 源表，domain entropy、complete key 与局部重数都只是后验标签。",
            "ActualNoncanonicalPrimitiveEmitterSourceTableLedger",
        ),
        row(
            "PointwiseKernelTableStillUpstreamOpen",
            not kernel_table_open and kernel_identity.get("pointwise_primitive_kernel_table_proved") is True,
            False,
            "同一 formal unit 的逐 primitive 核表仍未提交；它是把 signed source、Phi 和 exact-UV rank 对齐的上游字段。",
            "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate",
        ),
        row(
            "FalseSourceRoutesRejected",
            True,
            True,
            "raw Buchstab 计数、canonical 支撑导入、signed-only 相消、terminal packet 回流、CRT/轮筛位置刚性都不能生成源域绝对熵或 no-collapse。",
            SOURCE_RANK_PACKAGE,
        ),
        row(
            "PreTerminalExactUVFiberAbsoluteMassDispersionCurrentCorpusProved",
            False,
            False,
            "三个源域原子未合取证明前，preterminal exact-UV fiber 绝对质量分散仍未闭合。",
            SOURCE_RANK_PACKAGE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "ExactUV 源域分散与 DStructure/Rankin 独立验收门未完成前，行/列命题不能标为无条件闭合。",
            f"{EXACT_UV} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造源域原子化证书。"""
    exact_uv_after = load_json(DOCS / "prime-matrix-strict-exact-uv-after-final-promotion-router.json")
    multiplier = load_json(DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json")
    absolute_router = load_json(DOCS / "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json")
    rank_router = load_json(DOCS / "prime-matrix-strict-emitter-multiplicity-rank-attack-router.json")
    fixed_pair = load_json(DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json")
    complete_key = load_json(DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json")
    source_table = load_json(DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json")
    kernel_identity = load_json(DOCS / "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json")

    rows = build_rows(
        exact_uv_after=exact_uv_after,
        multiplier=multiplier,
        absolute_router=absolute_router,
        rank_router=rank_router,
        fixed_pair=fixed_pair,
        complete_key=complete_key,
        source_table=source_table,
        kernel_identity=kernel_identity,
    )
    closed_gates = [item["gate"] for item in rows if item["closed"]]
    open_gates = [item["gate"] for item in rows if not item["closed"]]

    source_atom_package = [
        {
            "atom": DOMAIN_ENTROPY,
            "proved": False,
            "role": "给出 actual pre-Cauchy source 的绝对质量不集中账本，排除少数 primitive rows 承载总质量。",
        },
        {
            "atom": COMPLETE_KEY,
            "proved": False,
            "role": "把所有 primitive summands 在发射前分到多对数个 complete keys，禁止后验补标签。",
        },
        {
            "atom": FIXED_KEY_MULT,
            "proved": False,
            "role": "证明固定 complete key 与固定 exact `(u,v)` 下没有大原像坍缩。",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_preterminal_fiber_dispersion_source_atom_router",
        "status": "strict_preterminal_fiber_dispersion_reduced_to_source_rank_atom_package_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "preterminal_fiber_dispersion_source_atomization_closed": True,
        "deterministic_source_atom_implication_closed": True,
        "registered_capacity_multiplier_imported": multiplier.get(
            "registered_capacity_multiplier_discipline_closed"
        )
        is True,
        "actual_precauchy_source_domain_absolute_entropy_ledger_proved": False,
        "complete_primitive_emitter_key_partition_ledger_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_ledger_proved": False,
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved": False,
        "actual_noncanonical_exact_uv_support_closed": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": FIBER_ABS,
        "terminal_gap_after_router": SOURCE_RANK_PACKAGE,
        "next_direct_attack_target": DOMAIN_ENTROPY,
        "preferred_attack_order": [DOMAIN_ENTROPY, COMPLETE_KEY, FIXED_KEY_MULT],
        "source_atom_package": source_atom_package,
        "deterministic_implication": (
            "Let D be the actual pre-Cauchy primitive source rows in one formal unit, "
            "pi:D->Omega_exact the exact (u,v) map, kappa:D->K a complete key map, "
            "and M_abs=sum_D |w(d)|. If |K|<=L^C, single-row absolute weights are "
            "registered into the same log budget, and every fixed pair/key fiber "
            "pi^{-1}(u,v) cap kappa^{-1}(k) has O(1) admissible source rows with "
            "no heavy-row exception, then M_abs(u,v)<=M_abs/L^A after choosing the "
            "stored log slack. Thus the remaining burden is exactly source entropy "
            "plus no-fiber-collapse, not CRT position counting."
        ),
        "hard_law": (
            "preterminal exact-UV 绝对 fiber 分散不是短区间统计或 signed cancellation；"
            "它是同一 formal unit 内 actual pre-Cauchy source 的源域熵与 exact-UV 映射无坍缩命题。"
            "早期零行、斜线覆盖、圆柱螺旋和轮筛刚性只能给位置/回流约束，不能替代源表、complete key 或局部重数证明。"
        ),
        "plain_conclusion": (
            "本步把当前唯一内部自足线的真正剩余继续压窄："
            "`PreTerminalExactUVFiberAbsoluteMassDispersionTheorem` 等价地需要一个源域 rank/no-collapse 包。"
            "形式求和蕴含已闭合；未闭合的是 actual source domain absolute entropy、complete key 分区、"
            "fixed-key exact-UV 局部 O(1) 重数三项。行/列命题仍未无条件闭合。"
        ),
        "closed_gates": closed_gates,
        "open_gates": open_gates,
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict preterminal fiber dispersion 源域原子化证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "same_theorem_target_preserved",
        "no_theorem_switch",
        "preterminal_fiber_dispersion_source_atomization_closed",
        "deterministic_source_atom_implication_closed",
        "actual_precauchy_source_domain_absolute_entropy_ledger_proved",
        "complete_primitive_emitter_key_partition_ledger_proved",
        "fixed_key_exact_uv_local_multiplicity_o1_ledger_proved",
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved",
        "actual_noncanonical_exact_uv_support_closed",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 当前压缩")
    lines.append("")
    lines.append("压缩前：")
    lines.append("")
    lines.append("```text")
    lines.append(result["terminal_gap_before_router"])
    lines.append("```")
    lines.append("")
    lines.append("压缩后：")
    lines.append("")
    lines.append("```text")
    lines.append(result["terminal_gap_after_router"])
    lines.append("```")
    lines.append("")
    lines.append("## 2. 源域原子包")
    lines.append("")
    lines.append("| atom | proved | role |")
    lines.append("| --- | --- | --- |")
    for atom in result["source_atom_package"]:
        lines.append(
            "| `{atom}` | `{proved}` | {role} |".format(
                atom=atom["atom"],
                proved=fmt_bool(atom["proved"]),
                role=table_cell(atom["role"]),
            )
        )
    lines.append("")
    lines.append("## 3. 判定表")
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
    lines.append("## 4. 确定性蕴含")
    lines.append("")
    lines.append("```text")
    lines.append(result["deterministic_implication"])
    lines.append("```")
    lines.append("")
    lines.append("## 5. 结构律")
    lines.append("")
    lines.append(result["hard_law"])
    lines.append("")
    lines.append("## 6. 下一主攻顺序")
    lines.append("")
    for index, atom in enumerate(result["preferred_attack_order"], start=1):
        lines.append(f"{index}. `{atom}`")
    lines.append("")
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
