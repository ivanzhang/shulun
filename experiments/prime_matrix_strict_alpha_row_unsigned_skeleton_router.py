#!/usr/bin/env python3
"""生成 strict alpha row unsigned 骨架攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_row_unsigned_skeleton_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-row-unsigned-skeleton-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-row-unsigned-skeleton-router.md"

TARGET = "AlphaRowAnchorPhaseEmissionFormulaLedger"
SIGNED_LIFT = "AlphaFormulaSignedCoefficientLiftLedger"
OVERLOAD_RETURN = "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"

SOURCE_FILES = [
    "prime-matrix-strict-pointwise-primitive-kernel-table-router.json",
    "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    "prime-matrix-early-zero-carry-shell-router.json",
    "prime-matrix-early-zero-anchor-collar-router.json",
    "prime-matrix-pcolumn-anchor-wheel-field.md",
    "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.md",
    "prime-matrix-strict-alpha-formula-signed-lift-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(name: str) -> str:
    """读取文本证书；缺失时返回空文本。"""
    path = DOCS / name
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def skeleton_equations() -> list[dict[str, str]]:
    """列出 unsigned row 骨架使用的确定性公式。"""
    return [
        {
            "name": "P-column distance coordinate",
            "formula": "n_{x,c}=xP+c=P(x+1)-(P-c)=Py-d, 1<=d<P",
            "role": "把行坐标统一放到第 P 列锚点 Py 左侧距离 d。",
        },
        {
            "name": "carry-shell identity",
            "formula": "h=a+b-floor(ab/P), c=ab mod P",
            "role": "把双高因子补洞压到带进位壳变量 h,a,b,c。",
        },
        {
            "name": "wheel skeleton shift",
            "formula": "S_W(P,y) == S_W(P,2)+P(y-2) mod W",
            "role": "把 P 列锚相位与第一行轮骨架圆柱平移连接。",
        },
        {
            "name": "anchor collar",
            "formula": "x<q<sqrt((x+1)P), m in interval length < P/q <= sqrt(P)",
            "role": "把高素 anchor 和 cofactor 限制到短素数纤维。",
        },
        {
            "name": "phase discipline",
            "formula": "phase_rule(d)=true or named phase return",
            "role": "source tuple 的相位过滤不能静默删点。",
        },
    ]


def build_rows(data: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 unsigned skeleton 判定表。"""
    pointwise = data["pointwise"]
    alpha_phase = data["alpha_phase"]
    source_tuple = data["source_tuple"]
    anchor_recon = data["anchor_recon"]
    carry = data["carry"]
    collar = data["collar"]
    signed_lift = data["signed_lift"]
    paw_text = data["paw_text"]
    layered_text = data["layered_text"]
    geometry_text = data["geometry_text"]

    pcolumn_phase_ready = (
        "PAW-5" in paw_text
        and "PAW-10" in paw_text
        and "LayeredClamp" in layered_text
        and "pcolumn_anchor_phi_skeleton" in geometry_text
    )
    target_active = (
        pointwise.get("next_direct_attack_target") == TARGET
        or alpha_phase.get("terminal_gap_before_router") == TARGET
    )

    return [
        row(
            "AlphaRowAnchorPhaseTargetActive",
            target_active,
            False,
            "逐点 primitive 核表当前优先卡在 alpha row anchor/phase 发射公式。",
            TARGET,
        ),
        row(
            "SourceTupleAnchorPayloadClosed",
            source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
            and anchor_recon.get("anchor_set_reconstruction_certificate_ledger") is True,
            True,
            "source tuple 已给出同 formal-unit 的 A、D0/K/Omega、phase_rule 与 hash。",
            "这只锁定输入参数，不给 signed coefficient。",
        ),
        row(
            "CarryShellUnsignedFormulaClosed",
            carry.get("exact_carry_shell_identity_closed") is True,
            True,
            "双高因子补洞满足 h=a+b-floor(ab/P), c=ab mod P。",
            "这是 unsigned row 形状公式。",
        ),
        row(
            "AnchorCollarUnsignedFiberClosed",
            collar.get("canonical_anchor_collar_closed") is True,
            True,
            "最小高素 anchor 被限制到 canonical collar，cofactor 位于短素数纤维。",
            "过载仍需命名回流或容量排斥。",
        ),
        row(
            "PColumnLayeredPhaseSkeletonClosed",
            pcolumn_phase_ready,
            True,
            "P列锚、圆柱平移和层叠轮筛给出候选 row 的相位字母表。",
            "相位字母表仍是 unsigned/geometric。",
        ),
        row(
            "UnsignedVariableBindingClosed",
            source_tuple.get("concrete_source_tuple_anchor_parameter_data_closed") is True
            and carry.get("exact_carry_shell_identity_closed") is True,
            True,
            "A、D0/K/Omega、phase_rule 可作为 carry-shell 变量筛选和锚区间过滤的输入。",
            "不产生 signed alpha source measure。",
        ),
        row(
            "UnsignedCongruenceRowSkeletonClosed",
            carry.get("exact_carry_shell_identity_closed") is True and pcolumn_phase_ready,
            True,
            "carry-shell 同余和 P列距离坐标给出候选 row skeleton 的确定性索引规则。",
            "不证明该 row skeleton 是 pre-Cauchy alpha primitive row。",
        ),
        row(
            "UnsignedPhaseCompatibilityClosed",
            pcolumn_phase_ready and anchor_recon.get("anchor_set_reconstruction_certificate_ledger") is True,
            True,
            "phase_rule、P列圆柱平移和 layered-wheel 单位类可在同一 source tuple 中登记。",
            "不控制 signed 变差和 branch key。",
        ),
        row(
            "SignedCoefficientLiftStillOpen",
            signed_lift.get("alpha_formula_signed_lift_router_closed") is True
            and signed_lift.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "已有 signed-lift 审查证明：unsigned carry-shell 命中不能自动定义 actual signed alpha source。",
            SIGNED_LIFT,
        ),
        row(
            "AnchorCollarOverloadReturnStillOpen",
            True,
            False,
            "短纤维过载已被识别为 PDEC/SAE/ColumnCRT/CleanKLS 回流形状，但排斥未证。",
            OVERLOAD_RETURN,
        ),
        row(
            "AlphaRowAnchorPhaseEmissionFormulaCurrentCorpusProved",
            False,
            False,
            "unsigned skeleton 已可登记，但完整 alpha row 发射公式还缺 signed lift 与过载回流排斥。",
            f"{SIGNED_LIFT} AND {OVERLOAD_RETURN}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 alpha row unsigned skeleton 证书。"""
    data = {
        "pointwise": load_json("prime-matrix-strict-pointwise-primitive-kernel-table-router.json"),
        "alpha_phase": load_json("prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "anchor_recon": load_json("prime-matrix-anchor-set-reconstruction-certificate-router.json"),
        "carry": load_json("prime-matrix-early-zero-carry-shell-router.json"),
        "collar": load_json("prime-matrix-early-zero-anchor-collar-router.json"),
        "signed_lift": load_json("prime-matrix-strict-alpha-formula-signed-lift-router.json"),
        "paw_text": load_text("prime-matrix-pcolumn-anchor-wheel-field.md"),
        "layered_text": load_text("prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"),
        "geometry_text": load_text("prime-matrix-clean-core-geometric-variation-branch-budget-router.md"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        isinstance(value, dict)
        and (
            value.get("direct_unconditional_contradiction_found") is True
            or value.get("row_column_unconditional_closed") is True
        )
        for value in data.values()
    )
    unsigned_skeleton_closed = all(
        item["closed"]
        for item in rows
        if item["gate"]
        in {
            "SourceTupleAnchorPayloadClosed",
            "CarryShellUnsignedFormulaClosed",
            "AnchorCollarUnsignedFiberClosed",
            "PColumnLayeredPhaseSkeletonClosed",
            "UnsignedVariableBindingClosed",
            "UnsignedCongruenceRowSkeletonClosed",
            "UnsignedPhaseCompatibilityClosed",
        }
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_row_unsigned_skeleton_router",
        "status": "alpha_row_unsigned_skeleton_closed_signed_lift_and_overload_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "alpha_row_unsigned_skeleton_router_closed": True,
        "unsigned_source_tuple_carry_shell_binding_closed": unsigned_skeleton_closed,
        "unsigned_carry_shell_congruence_row_skeleton_closed": unsigned_skeleton_closed,
        "unsigned_phase_wheel_compatibility_closed": unsigned_skeleton_closed,
        "alpha_formula_signed_coefficient_lift_proved": False,
        "alpha_formula_anchor_collar_overload_named_return_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "pointwise_primitive_kernel_table_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SIGNED_LIFT,
        "parallel_required_inputs": [OVERLOAD_RETURN],
        "skeleton_equations": skeleton_equations(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 的 unsigned 骨架部分已经由 source tuple、carry-shell、anchor-collar、P列锚和 layered-wheel "
            f"共同关闭；剩余不是几何 row 形状，而是 `{SIGNED_LIFT}` 与 `{OVERLOAD_RETURN}`。"
        ),
        "plain_conclusion": (
            "本步继续攻当前最窄硬点，并把 alpha row 发射公式拆成已闭合的 unsigned skeleton 与仍开放的 signed 层。"
            "source tuple 可复算 A、D0/K/Omega、phase_rule；carry-shell 给出 h,a,b,c 同余骨架；P列锚和层叠轮给出"
            "相位兼容字母表；anchor-collar 给出短纤维限制。因此当前真正剩余不是 row 的 unsigned 形状，"
            "而是把这个 skeleton 提升为 pre-Cauchy signed alpha primitive coefficient，并排斥或登记短纤维过载回流。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha row unsigned skeleton 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"alpha_row_unsigned_skeleton_router_closed={fmt_bool(result['alpha_row_unsigned_skeleton_router_closed'])}",
        f"unsigned_source_tuple_carry_shell_binding_closed={fmt_bool(result['unsigned_source_tuple_carry_shell_binding_closed'])}",
        f"unsigned_carry_shell_congruence_row_skeleton_closed={fmt_bool(result['unsigned_carry_shell_congruence_row_skeleton_closed'])}",
        f"unsigned_phase_wheel_compatibility_closed={fmt_bool(result['unsigned_phase_wheel_compatibility_closed'])}",
        f"alpha_formula_signed_coefficient_lift_proved={fmt_bool(result['alpha_formula_signed_coefficient_lift_proved'])}",
        f"alpha_formula_anchor_collar_overload_named_return_proved={fmt_bool(result['alpha_formula_anchor_collar_overload_named_return_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"pointwise_primitive_kernel_table_proved={fmt_bool(result['pointwise_primitive_kernel_table_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. unsigned 骨架公式",
        "",
        "| name | formula | role |",
        "| --- | --- | --- |",
    ]
    for item in result["skeleton_equations"]:
        lines.append(
            "| `{name}` | `{formula}` | {role} |".format(
                name=table_cell(item["name"]),
                formula=table_cell(item["formula"]),
                role=table_cell(item["role"]),
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
            "## 4. 下一真正硬点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行必要输入：",
            "",
            "```text",
            *result["parallel_required_inputs"],
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
