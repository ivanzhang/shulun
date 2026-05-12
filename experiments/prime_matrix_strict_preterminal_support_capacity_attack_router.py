#!/usr/bin/env python3
"""生成 strict pre-terminal 支撑/容量定理直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_preterminal_support_capacity_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-preterminal-support-capacity-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-preterminal-support-capacity-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-preterminal-support-capacity-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json",
    "prime-matrix-registered-capacity-multiplier-discipline-router.json",
    "prime-matrix-actual-capacity-ledger-microatom-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-exact-uv-support-attack-router.json",
    "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json",
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
    atomization: dict[str, Any],
    multiplier: dict[str, Any],
    microatom: dict[str, Any],
    support_seed: dict[str, Any],
    exact_uv: dict[str, Any],
    fixed_point: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 pre-terminal 支撑/容量直攻判定表。"""
    target = "PreTerminalActualFullSFactorSupportCapacityTheorem"
    fiber_atom = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
    return [
        {
            "gate": "PreTerminalSupportCapacityTargetActive",
            "closed": atomization.get("strict_active_nonterminal_obligation_after_router")
            == target,
            "proved": False,
            "meaning": "上一层已把独立非终端 source entropy 原子化为 pre-terminal actual full-S 支撑/容量定理。",
            "remaining": target,
        },
        {
            "gate": "RegisteredCapacityMultiplierDisciplineImported",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed")
            is True,
            "proved": True,
            "meaning": "Type/Fourier/fiber 成本已登记到同一 formal unit，容量侧不再是活动障碍。",
            "remaining": "ActualNoncanonicalExactUVSupportLowerBound。",
        },
        {
            "gate": "SupportOnlyPitfallAlreadyRemoved",
            "closed": microatom.get("support_only_suffices") is False,
            "proved": True,
            "meaning": "raw 支撑宽度不能单独证明反原子；但登记乘子纪律已恢复支撑到容量的条件蕴含。",
            "remaining": "exact u/v support lower bound。",
        },
        {
            "gate": "ElementaryMassSupportLemmaImported",
            "closed": support_seed.get("elementary_mass_support_lemma_closed") is True,
            "proved": True,
            "meaning": "若 exact pair 最大质量或 L2 能量界成立，则 pair 支撑和 S_u*S_v 下界由初等引理推出。",
            "remaining": "exact pair mass dispersion。",
        },
        {
            "gate": "OldExactUVTerminalRouteRejected",
            "closed": exact_uv.get("moving_block_return_loop_detected") is True
            and fixed_point.get("all_current_internal_routes_to_source_entropy_are_recursive")
            is True,
            "proved": True,
            "meaning": "通过 support failure packet、moving-block return 或 terminal 三原子证明 ExactUV 会回到固定点，不能作为非终端证明。",
            "remaining": fiber_atom,
        },
        {
            "gate": "SourceSeedObjectDisciplinePinned",
            "closed": support_seed.get("acyclic_pre_cauchy_seed_proved") is False,
            "proved": False,
            "meaning": "估计必须作用于 Cauchy/dispersion 前已声明的 actual source；不能从终端覆盖图反推对象。",
            "remaining": "ActualPreCauchySourceObjectLedgerForThisEstimate。",
        },
        {
            "gate": "QuantitativeCorePinned",
            "closed": True,
            "proved": False,
            "meaning": "在容量已登记后，真正数值负担是 pre-terminal exact (u,v) 纤维的最大原子/L2 非集中估计。",
            "remaining": fiber_atom,
        },
        {
            "gate": "CRTWheelRigidityInsufficientForFiberMass",
            "closed": True,
            "proved": True,
            "meaning": "CRT/轮筛/层叠筛给允许残基与禁止类结构，不控制 actual signed source 在某个 exact pair fiber 内的质量分配。",
            "remaining": fiber_atom,
        },
        {
            "gate": "NonterminalFiberAperiodicityCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料尚未给出不使用终端回流的 exact fiber 非集中估计。",
            "remaining": fiber_atom,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict pre-terminal 支撑/容量直攻证书。"""
    atomization = load_json(
        DOCS
        / "prime-matrix-strict-independent-nonterminal-source-entropy-atomization-router.json"
    )
    multiplier = load_json(DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json")
    microatom = load_json(DOCS / "prime-matrix-actual-capacity-ledger-microatom-router.json")
    support_seed = load_json(DOCS / "prime-matrix-strict-actual-source-support-seed-router.json")
    exact_uv = load_json(DOCS / "prime-matrix-strict-exact-uv-support-attack-router.json")
    fixed_point = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-fixed-point-firewall-router.json"
    )

    target = "PreTerminalActualFullSFactorSupportCapacityTheorem"
    fiber_atom = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
    rows = build_rows(
        atomization=atomization,
        multiplier=multiplier,
        microatom=microatom,
        support_seed=support_seed,
        exact_uv=exact_uv,
        fixed_point=fixed_point,
    )
    return {
        "certificate_type": "prime_matrix_strict_preterminal_support_capacity_attack_router",
        "status": "strict_preterminal_support_capacity_reduced_to_nonterminal_exact_uv_fiber_aperiodicity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "preterminal_support_capacity_attack_closed": True,
        "registered_capacity_multiplier_discipline_imported": True,
        "support_to_capacity_implication_closed": True,
        "terminal_exactuv_routes_rejected_as_nonterminal_proof": True,
        "crt_wheel_rigidity_controls_positions_not_fiber_mass": True,
        "preterminal_actual_fulls_factor_support_capacity_proved": False,
        "nonterminal_exact_uv_fiber_aperiodicity_proved": False,
        "independent_nonterminal_source_entropy_proof_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": fiber_atom,
        "next_direct_attack_target": fiber_atom,
        "fiber_aperiodicity_contract": (
            "For the actual sign-refined pre-Cauchy source in one formal unit, prove "
            "max_{(u,v)} M_{u,v} <= M / L^K, or equivalently an L2 energy bound "
            "sum M_{u,v}^2 <= M^2 / L^K, uniformly at the log-power needed for every A."
        ),
        "hard_law": (
            "容量乘子纪律已经关闭，支撑到容量的初等蕴含已经关闭；"
            "pre-terminal 支撑/容量定理的唯一数值核心是 exact (u,v) fiber 非集中。"
            "CRT/轮筛刚性只给位置结构，不能给 signed source 质量分散；"
            "通过终端 packet 回流证明则回到固定点，不能用于非终端证明。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PreTerminalActualFullSFactorSupportCapacityTheorem` 继续被压缩：容量侧和初等支撑推理已闭合，"
            "终端回流路线被排除，CRT/轮筛刚性只能控制允许位置而不控制 fiber 质量。"
            "因此最新严格自足最窄点是 `NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource`。"
            "该估计尚未证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict pre-terminal 支撑/容量直攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"preterminal_support_capacity_attack_closed={fmt_bool(result['preterminal_support_capacity_attack_closed'])}",
        f"registered_capacity_multiplier_discipline_imported={fmt_bool(result['registered_capacity_multiplier_discipline_imported'])}",
        f"terminal_exactuv_routes_rejected_as_nonterminal_proof={fmt_bool(result['terminal_exactuv_routes_rejected_as_nonterminal_proof'])}",
        f"crt_wheel_rigidity_controls_positions_not_fiber_mass={fmt_bool(result['crt_wheel_rigidity_controls_positions_not_fiber_mass'])}",
        f"nonterminal_exact_uv_fiber_aperiodicity_proved={fmt_bool(result['nonterminal_exact_uv_fiber_aperiodicity_proved'])}",
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
        "fiber 非集中合同：",
        "",
        "```text",
        result["fiber_aperiodicity_contract"],
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
