#!/usr/bin/env python3
"""生成 strict 原子 joint rows 内置配对公式证书。

用法示例：
  python3 experiments/prime_matrix_strict_atomic_joint_rows_builtin_pairing_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
OUT_MD = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.md"

ATOMIC_DECLARATION = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SIGNED_VALUE_TABLE = "PointwiseSignedAlphaCoefficientValueTableForUnsignedCarryShellSkeleton"
SIGNED_WEIGHT = "PointwiseNonrecursiveSignedAlphaWeightFormulaForEachCarryShellSkeletonRow"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json",
    "prime-matrix-strict-joint-emitter-formula-field-atom-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-value-table-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-primitive-summand-signed-expression-router.json",
    "prime-matrix-strict-primitive-summand-origin-identity-router.json",
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


def builtin_pairing_fields() -> list[dict[str, str]]:
    """内置配对闭式公式必须给出的字段。"""
    return [
        {
            "field": "unsigned_joint_row_skeleton",
            "requirement": "从 source tuple 正向给出 carry-shell/P列锚/phase-compatible row skeleton。",
        },
        {
            "field": "signed_coefficient_value",
            "requirement": "对每条 skeleton row 给出 signed coefficient 的闭式值，不能由 origin table 后验读取。",
        },
        {
            "field": "word_coefficient_pairing_identity",
            "requirement": "证明 basis word 与 signed coefficient 是同一 pre-Cauchy 算术对象的两面。",
        },
        {
            "field": "alpha_delta_prepushforward_sum",
            "requirement": "证明这些 row 在 Phi/payment/Cauchy 前求和等于 actual alpha/delta 贡献。",
        },
        {
            "field": "exact_uv_local_factor",
            "requirement": "同步输出 exact `(u,v)`、branch key、sign/local factor 与非零条件。",
        },
        {
            "field": "no_origin_table_fallback",
            "requirement": "失败时命名回流；不得退回 row-level origin table、signed-source 固定点或零行/payment 反推。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把 atomic declaration 压到内置 signed coefficient/pairing 闭式公式。"""
    firewall = data["firewall"]
    joint_emitter = data["joint_emitter"]
    unsigned = data["unsigned"]
    signed_lift = data["signed_lift"]
    signed_value = data["signed_value"]
    signed_weight = data["signed_weight"]
    primitive_expr = data["primitive_expr"]
    origin = data["origin"]
    incidence = data["incidence"]

    unsigned_skeleton_closed = (
        unsigned.get("unsigned_source_tuple_carry_shell_binding_closed") is True
        and unsigned.get("unsigned_carry_shell_congruence_row_skeleton_closed") is True
        and unsigned.get("unsigned_phase_wheel_compatibility_closed") is True
    )
    signed_route_returns_origin = (
        signed_value.get("next_direct_attack_target") == SIGNED_WEIGHT
        and signed_weight.get("next_direct_attack_target")
        == "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
        and primitive_expr.get("next_direct_attack_target")
        == "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
        and origin.get("next_direct_attack_target")
        == "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
    )
    return [
        row(
            "AtomicDeclarationTargetActive",
            firewall.get("next_direct_attack_target") == ATOMIC_DECLARATION,
            firewall.get("atomic_antisplit_declaration_proved") is True,
            "上一层已把反分裂 joint 公式压成原子 pre-Cauchy rows 声明。",
            ATOMIC_DECLARATION,
        ),
        row(
            "SourceTupleAndDownstreamFirewallImported",
            joint_emitter.get("source_tuple_input_closed") is True
            and joint_emitter.get("downstream_recovery_firewall_imported") is True,
            True,
            "source tuple 输入和禁止 payment/零行/终端后验恢复的原则已可用。",
            "这些只给容器和防火墙，不给 signed coefficient。",
        ),
        row(
            "UnsignedJointRowSkeletonClosed",
            unsigned_skeleton_closed,
            True,
            "carry-shell 绑定、同余 row skeleton、P列锚/phase wheel 兼容已给出 unsigned row 形状。",
            "需要 signed coefficient/pairing。",
        ),
        row(
            "JointRowsFormulaStillMissingSignedPayload",
            joint_emitter.get("joint_emitter_rows_formula_proved") is False
            and unsigned_skeleton_closed,
            False,
            "已有 unsigned row skeleton 不等于 joint rows formula；joint row 必须自带 signed coefficient 与 pairing payload。",
            BUILTIN_PAIRING,
        ),
        row(
            "SignedLiftReducesToPointwiseValueTable",
            signed_lift.get("next_direct_attack_target") == SIGNED_VALUE_TABLE,
            signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is True,
            "从 unsigned skeleton 提升到 signed 层的首缺口是逐 row signed coefficient value table。",
            SIGNED_VALUE_TABLE,
        ),
        row(
            "SignedValueRouteWouldReturnOriginTable",
            signed_route_returns_origin,
            False,
            "若继续按旧 signed value 链展开，会回到 primitive origin identity 与 row-level origin table。",
            "origin-table route is blocked for atomic declaration。",
        ),
        row(
            "PrepushforwardIdentityNotAvailableWithoutBuiltinPairing",
            joint_emitter.get("joint_word_coefficient_identity_proved") is False
            and joint_emitter.get("joint_emitter_prepushforward_sum_identity_proved") is False,
            False,
            "word/coefficient 同源与推前前 alpha/delta 求和恒等式都依赖内置 signed pairing 公式。",
            BUILTIN_PAIRING,
        ),
        row(
            "ExactUVParallelGateNotPairingFormula",
            incidence.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV bounded incidence 仍是并行守门项，不能替代 signed coefficient/pairing 闭式值。",
            EXACT_UV,
        ),
        row(
            "BuiltInSignedCoefficientPairingCurrentCorpusProved",
            False,
            False,
            "当前语料没有给出每条 atomic joint row 的 signed coefficient 闭式值及其 word/coefficient 同源证明。",
            BUILTIN_PAIRING,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "缺少内置配对闭式公式、ExactUV、模型余量、RatePreservation 与 DStructure/Rankin 验收门。",
            f"{BUILTIN_PAIRING} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造原子 joint rows 内置配对证书。"""
    data = {
        "firewall": load_json("prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"),
        "joint_emitter": load_json("prime-matrix-strict-joint-emitter-formula-field-atom-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "signed_value": load_json("prime-matrix-strict-pointwise-signed-alpha-value-table-router.json"),
        "signed_weight": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "primitive_expr": load_json("prime-matrix-strict-primitive-summand-signed-expression-router.json"),
        "origin": load_json("prime-matrix-strict-primitive-summand-origin-identity-router.json"),
        "incidence": load_json("prime-matrix-strict-actual-emitter-incidence-entropy-router.json"),
    }
    rows = build_rows(data)
    unsigned_skeleton_closed = any(
        item["gate"] == "UnsignedJointRowSkeletonClosed" and item["closed"] is True for item in rows
    )
    signed_origin_loop_blocked = any(
        item["gate"] == "SignedValueRouteWouldReturnOriginTable" and item["closed"] is True for item in rows
    )
    strict_basis = f"{BUILTIN_PAIRING} AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_atomic_joint_rows_builtin_pairing_router",
        "status": "atomic_joint_rows_formula_reduced_to_builtin_signed_pairing_closed_form_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "atomic_declaration_target_active": data["firewall"].get("next_direct_attack_target") == ATOMIC_DECLARATION,
        "unsigned_joint_row_skeleton_closed": unsigned_skeleton_closed,
        "signed_origin_table_loop_blocked": signed_origin_loop_blocked,
        "builtin_signed_coefficient_pairing_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": data["incidence"].get(
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved"
        )
        is True,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": BUILTIN_PAIRING,
        "strict_author_side_remaining_basis": strict_basis,
        "builtin_pairing_fields": builtin_pairing_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步直接攻击 `AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing`。"
            "source tuple 容器、防后验恢复防火墙和 unsigned carry-shell/phase row skeleton 已可用；"
            "真正缺口不是再找 row 形状，而是每条 atomic joint row 的内置 signed coefficient/pairing 闭式值。"
            "若沿旧 signed-value 链推进，它会回到 origin table 与 signed-source 固定点，因此不能用作原子声明。"
            "最新最窄点压成 `BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows`；当前语料没有该闭式公式，"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 原子 joint rows 内置配对公式",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"atomic_declaration_target_active={fmt_bool(result['atomic_declaration_target_active'])}",
        f"unsigned_joint_row_skeleton_closed={fmt_bool(result['unsigned_joint_row_skeleton_closed'])}",
        f"signed_origin_table_loop_blocked={fmt_bool(result['signed_origin_table_loop_blocked'])}",
        f"builtin_signed_coefficient_pairing_proved={fmt_bool(result['builtin_signed_coefficient_pairing_proved'])}",
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
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
            "## 2. 内置配对字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for item in result["builtin_pairing_fields"]:
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
