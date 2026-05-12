#!/usr/bin/env python3
"""生成 strict 反分裂 joint declaration 防火墙证书。

用法示例：
  python3 experiments/prime_matrix_strict_antisplit_joint_declaration_firewall_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-antisplit-joint-declaration-firewall-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"
OUT_MD = DOCS / "prime-matrix-strict-antisplit-joint-declaration-firewall-router.md"

ANTISPLIT = "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection"
JOINT_DECLARATION = "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple"
EXPLICIT_JOINT = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"
ATOMIC_DECLARATION = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-new-joint-formula-antisplit-atom-router.json",
    "prime-matrix-strict-joint-emitter-formula-field-atom-router.json",
    "prime-matrix-strict-joint-declaration-constructor-sync-router.json",
    "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
    "prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
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


def missing_sources() -> list[str]:
    """列出缺失依赖；缺失不能当成证明。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def atomic_fields() -> list[dict[str, str]]:
    """原子反分裂声明必须内置的字段。"""
    return [
        {
            "field": "actual_source_tuple_domain",
            "requirement": "定义域必须是 actual noncanonical source tuple，不借 canonical、external 或 terminal 回流。",
        },
        {
            "field": "joint_rows_formula",
            "requirement": "声明行本身正向列出 primitive rows，而不是再调用 explicit joint constructor rule。",
        },
        {
            "field": "word_coefficient_pairing",
            "requirement": "每条 row 同时给出 basis word、signed coefficient 和二者同源恒等式。",
        },
        {
            "field": "alpha_delta_payload",
            "requirement": "同一 row 内置 alpha/delta pairing、exact `(u,v)`、branch key、sign/local factor。",
        },
        {
            "field": "prepushforward_identity",
            "requirement": "在 Cauchy、Phi、payment 推前前证明求和等于 actual emitter 系数。",
        },
        {
            "field": "split_firewall",
            "requirement": "证明该声明不降解为 explicit joint constructor -> alpha-side -> row-level 来源环。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步普通 declaration 与反分裂 declaration 的差异。"""
    antisplit = data["antisplit"]
    emitter = data["emitter"]
    declaration = data["declaration"]
    explicit = data["explicit"]
    joint_fixed = data["joint_fixed"]
    seed_cycle = data["seed_cycle"]
    incidence = data["incidence"]

    return [
        row(
            "AntiSplitFormulaTargetActive",
            antisplit.get("next_direct_attack_target") == ANTISPLIT,
            antisplit.get("antisplit_joint_formula_proved") is True,
            "上一层已把新 joint 公式压成反分裂同排公式。",
            ANTISPLIT,
        ),
        row(
            "JointEmitterFieldsPointToDeclaration",
            emitter.get("next_direct_attack_target") == JOINT_DECLARATION,
            emitter.get("pre_cauchy_joint_declaration_line_proved") is True,
            "联合发射公式字段层的第一普通字段是 pre-Cauchy joint declaration line。",
            JOINT_DECLARATION,
        ),
        row(
            "OrdinaryJointDeclarationReturnsToExplicitConstructor",
            declaration.get("next_direct_attack_target") == EXPLICIT_JOINT
            and declaration.get("joint_declaration_matches_actual_constructor_formula_line") is True,
            declaration.get("pre_cauchy_joint_declaration_line_proved") is True,
            "普通 joint declaration 已同步到 explicit joint constructor rule；这不是反分裂出口。",
            EXPLICIT_JOINT,
        ),
        row(
            "ExplicitConstructorRouteIsKnownFixedPoint",
            explicit.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True
            and joint_fixed.get("cycle_cut_joint_route_returns_to_row_level_fixed_point") is True,
            explicit.get("explicit_joint_constructor_rule_proved") is True,
            "explicit constructor 继续展开会经 alpha-side/same-row/row-level 回到 signed-source 固定点。",
            "cannot count as antisplit proof。",
        ),
        row(
            "SeedCoordinateCycleStillBlocksReverseConstruction",
            seed_cycle.get("seed_coordinate_source_cycle_detected") is True
            and seed_cycle.get("raw_cycle_counts_as_closure") is False,
            True,
            "坐标-来源闭环不能被普通 declaration 重命名后当作正向公式。",
            ATOMIC_DECLARATION,
        ),
        row(
            "ExactUVParallelGateNotFormula",
            incidence.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV incidence 仍是并行守门项，不给 word/coefficient 原子声明。",
            EXACT_UV,
        ),
        row(
            "AtomicAntiSplitDeclarationCurrentCorpusProved",
            False,
            False,
            "当前语料没有一条 declaration line 同时内置 rows formula、word/coefficient 同源、prepushforward identity 和 split firewall。",
            ATOMIC_DECLARATION,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "缺少原子反分裂声明、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。",
            f"{ATOMIC_DECLARATION} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造反分裂 joint declaration 防火墙证书。"""
    data = {
        "antisplit": load_json("prime-matrix-strict-new-joint-formula-antisplit-atom-router.json"),
        "emitter": load_json("prime-matrix-strict-joint-emitter-formula-field-atom-router.json"),
        "declaration": load_json("prime-matrix-strict-joint-declaration-constructor-sync-router.json"),
        "explicit": load_json("prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"),
        "joint_fixed": load_json("prime-matrix-strict-joint-alpha-signed-source-fixed-point-sync-router.json"),
        "seed_cycle": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "incidence": load_json("prime-matrix-strict-actual-emitter-incidence-entropy-router.json"),
    }
    rows = build_rows(data)
    ordinary_declaration_is_nonproof = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "JointEmitterFieldsPointToDeclaration",
            "OrdinaryJointDeclarationReturnsToExplicitConstructor",
            "ExplicitConstructorRouteIsKnownFixedPoint",
            "SeedCoordinateCycleStillBlocksReverseConstruction",
        }
    )
    strict_basis = f"{ATOMIC_DECLARATION} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_antisplit_joint_declaration_firewall_router",
        "status": "antisplit_joint_formula_reduced_to_atomic_declaration_with_split_firewall_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "antisplit_formula_target_active": data["antisplit"].get("next_direct_attack_target") == ANTISPLIT,
        "ordinary_joint_declaration_route_is_nonproof_cycle": ordinary_declaration_is_nonproof,
        "atomic_antisplit_declaration_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": data["incidence"].get(
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ATOMIC_DECLARATION,
        "strict_author_side_remaining_basis": strict_basis,
        "atomic_fields": atomic_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步继续压缩反分裂 joint 公式。普通 `PreCauchyJointWordCoefficientEmitterDeclarationLine` "
            "已经被既有证书同步到 `ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRule`，而后者会经 "
            "alpha-side、same-row、row-level 回到 signed-source 固定点。因此普通 declaration line 不足以闭合。"
            "真正最窄点必须是带 split firewall 的原子声明："
            "`AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing`，声明行本身就要内置 rows formula、"
            "basis word/signed coefficient 同源、alpha/delta payload、prepushforward identity，并证明不降解到旧分裂链。"
            "当前语料没有该原子声明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 反分裂 joint declaration 防火墙",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"antisplit_formula_target_active={fmt_bool(result['antisplit_formula_target_active'])}",
        (
            "ordinary_joint_declaration_route_is_nonproof_cycle="
            f"{fmt_bool(result['ordinary_joint_declaration_route_is_nonproof_cycle'])}"
        ),
        f"atomic_antisplit_declaration_proved={fmt_bool(result['atomic_antisplit_declaration_proved'])}",
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 防火墙判定",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 2. 原子声明字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for item in result["atomic_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 作者侧剩余基",
            "",
            "```text",
            result["strict_author_side_remaining_basis"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["", "## 4. 缺失依赖", ""])
        for item in result["missing_sources"]:
            lines.append(f"- `{item}`")
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
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
