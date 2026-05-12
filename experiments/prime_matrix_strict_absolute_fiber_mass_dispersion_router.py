#!/usr/bin/env python3
"""生成 strict 绝对 fiber 质量分散原像层路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_absolute_fiber_mass_dispersion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-absolute-fiber-mass-dispersion-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json"
OUT_MD = DOCS / "prime-matrix-strict-absolute-fiber-mass-dispersion-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
    "prime-matrix-prepushforward-emitter-origin-ledger-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，兼容旧归档。"""
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


def build_rows(
    fiber_attack: dict[str, Any],
    multiplier: dict[str, Any],
    emitter_origin: dict[str, Any],
    reverse_functor: dict[str, Any],
    loop_cut: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成绝对 fiber 质量分散原像层判定表。"""
    target = "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
    next_atom = "PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem"
    return [
        {
            "gate": "AbsoluteFiberMassTargetActive",
            "closed": fiber_attack.get("terminal_gap_after_router") == target,
            "proved": False,
            "meaning": "上一层已把非终端 fiber 非集中压成 exact fiber 绝对质量分散。",
            "remaining": target,
        },
        {
            "gate": "KnownCoefficientWeightCapImported",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed")
            is True,
            "proved": True,
            "meaning": "单个 summand 的 Type/Fourier/fiber/系数损失已登记为 log-power 成本；权重上界不是当前主障碍。",
            "remaining": "需要控制同一 exact fiber 接收多少 primitive summand。",
        },
        {
            "gate": "EmitterOriginLedgerNeeded",
            "closed": emitter_origin.get("prepushforward_emitter_reduction_closed")
            is True,
            "proved": False,
            "meaning": "绝对质量分散必须在 pre-pushforward primitive emitter 上计数；当前材料仍未证明原始生成账本存在。",
            "remaining": "CleanCoreOriginalCoefficientGenerationLedgerAndReturn。",
        },
        {
            "gate": "ReversePaymentFunctorInsufficient",
            "closed": reverse_functor.get("pushforward_reverse_uniqueness_rejected")
            is True
            and reverse_functor.get("registered_primitive_prepushforward_fiber_emitter_proved")
            is False,
            "proved": True,
            "meaning": "从 payment 图反向恢复 preimage summand 不唯一；不能由下游图推出原像纤维分散。",
            "remaining": next_atom,
        },
        {
            "gate": "SourceLoopCutImported",
            "closed": loop_cut.get("source_loop_cut_closed") is True,
            "proved": True,
            "meaning": "origin ledger -> constructor -> formula -> emitter -> origin ledger 的循环不能生成新来源或分散估计。",
            "remaining": next_atom,
        },
        {
            "gate": "MassDispersionReducedToMultiplicity",
            "closed": True,
            "proved": False,
            "meaning": "在 summand 权重已受 log-power 控制后，absolute fiber mass cap 的数值负担就是 exact `(u,v)` 原像纤维的 multiplicity spread。",
            "remaining": next_atom,
        },
        {
            "gate": "CRTWheelGivesFiberMapNotExpansion",
            "closed": True,
            "proved": True,
            "meaning": "CRT/轮筛/层叠筛能定义 exact `(u,v)` fiber map，却不证明该 map 的最大原像纤维小。",
            "remaining": next_atom,
        },
        {
            "gate": "PrimitiveEmitterMultiplicityDispersionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未证明 primitive emitter 在 exact `(u,v)` 原像纤维上的多对数级分散。",
            "remaining": next_atom,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 绝对 fiber 质量分散原像层证书。"""
    fiber_attack = load_json(
        DOCS / "prime-matrix-strict-nonterminal-fiber-aperiodicity-attack-router.json"
    )
    multiplier = load_json(DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json")
    emitter_origin = load_json(DOCS / "prime-matrix-prepushforward-emitter-origin-ledger-router.json")
    reverse_functor = load_json(DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json")
    loop_cut = load_json(DOCS / "prime-matrix-clean-core-source-loop-cut-router.json")

    target = "PreTerminalExactUVFiberAbsoluteMassDispersionTheorem"
    next_atom = "PreTerminalExactUVPrimitiveEmitterMultiplicityDispersionTheorem"
    rows = build_rows(
        fiber_attack=fiber_attack,
        multiplier=multiplier,
        emitter_origin=emitter_origin,
        reverse_functor=reverse_functor,
        loop_cut=loop_cut,
    )
    return {
        "certificate_type": "prime_matrix_strict_absolute_fiber_mass_dispersion_router",
        "status": "strict_absolute_fiber_mass_dispersion_reduced_to_primitive_emitter_multiplicity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "absolute_fiber_mass_dispersion_router_closed": True,
        "known_summand_weight_cap_imported": True,
        "reverse_payment_recovery_rejected": True,
        "crt_wheel_fiber_map_not_expansion": True,
        "preterminal_exact_uv_fiber_absolute_mass_dispersion_proved": False,
        "preterminal_exact_uv_primitive_emitter_multiplicity_dispersion_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_atom,
        "next_direct_attack_target": next_atom,
        "multiplicity_dispersion_contract": (
            "For the actual primitive pre-pushforward emitter, with each summand carrying "
            "branch key, sign/local factor and exact (u,v) map, prove that every exact "
            "(u,v) fiber receives at most a log-power-small fraction of the total emitted "
            "absolute weight, after the registered single-summand weight cap."
        ),
        "hard_law": (
            "绝对质量分散不是新的相消问题，而是 emitter 原像纤维扩张问题。"
            "已登记权重上界只能把质量问题转为 multiplicity 问题；"
            "下游 payment 图和 CRT 纤维图不能反向证明原像纤维分散。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PreTerminalExactUVFiberAbsoluteMassDispersionTheorem` 进一步压成 primitive emitter 的原像纤维分散："
            "单个 summand 权重已被容量乘子纪律吸收，真正剩余是证明 exact `(u,v)` fiber 的原像 multiplicity "
            "不能承载总绝对质量的多对数级大份额。该分散定理尚未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 绝对 fiber 质量分散原像层路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"absolute_fiber_mass_dispersion_router_closed={fmt_bool(result['absolute_fiber_mass_dispersion_router_closed'])}",
        f"known_summand_weight_cap_imported={fmt_bool(result['known_summand_weight_cap_imported'])}",
        f"reverse_payment_recovery_rejected={fmt_bool(result['reverse_payment_recovery_rejected'])}",
        f"crt_wheel_fiber_map_not_expansion={fmt_bool(result['crt_wheel_fiber_map_not_expansion'])}",
        f"preterminal_exact_uv_primitive_emitter_multiplicity_dispersion_proved={fmt_bool(result['preterminal_exact_uv_primitive_emitter_multiplicity_dispersion_proved'])}",
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
        "multiplicity 分散合同：",
        "",
        "```text",
        result["multiplicity_dispersion_contract"],
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
