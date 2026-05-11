#!/usr/bin/env python3
"""生成 strict acyclic seed signed row emitter 单点攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_seed_signed_row_emitter_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.md"

TARGET = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
NEXT_TARGET = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"

SOURCE_FILES = [
    "prime-matrix-strict-row-level-origin-generation-table-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-strict-alpha-row-unsigned-skeleton-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json",
    "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def coefficient_law_fields() -> list[dict[str, str]]:
    """列出 signed coefficient law 的必要字段。"""
    return [
        {
            "field": "basis_weight_source",
            "meaning": "系数来自哪个 pre-Cauchy 算术基函数/筛权，而不是 payment 原像。",
        },
        {
            "field": "sign_rule",
            "meaning": "每行符号由 seed 内部规则决定，并与 branch key 同步。",
        },
        {
            "field": "local_factor_rule",
            "meaning": "每行 local factor 的闭式公式和非零条件。",
        },
        {
            "field": "truncation_and_phase_charge",
            "meaning": "截断、相位过滤和 branch 变差收费的同口径登记。",
        },
        {
            "field": "alpha_delta_sum_identity",
            "meaning": "逐行 signed 系数求和后在推前前等于 actual alpha/delta 系数。",
        },
        {
            "field": "named_return",
            "meaning": "零系数、符号冲突、local factor 缺失或超预算全部命名回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查 seed signed row emitter 的下一精确缺口。"""
    previous = data["previous"]
    seed_fusion = data["seed_fusion"]
    zero_nogo = data["zero_nogo"]
    unsigned = data["unsigned"]
    weight = data["weight"]
    lift = data["lift"]
    pointwise = data["pointwise"]
    key = data["key"]
    uv_rank = data["uv_rank"]
    disintegration = data["disintegration"]

    seed_absent_return_ready = (
        seed_fusion.get("seed_absent_branch_returned_to_terminal_family") is True
        and seed_fusion.get("terminal_gap_after_router") == TERMINAL_RETURN
    )
    unsigned_ready = (
        unsigned.get("alpha_row_unsigned_skeleton_router_closed") is True
        and unsigned.get("unsigned_carry_shell_congruence_row_skeleton_closed") is True
        and unsigned.get("unsigned_phase_wheel_compatibility_closed") is True
    )

    return [
        row(
            "SeedSignedEmitterTargetActive",
            previous.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把逐行生成表压成 acyclic seed 自带 signed row emitter。",
            TARGET,
        ),
        row(
            "SeedAbsentBranchAlreadyTerminalReturn",
            seed_absent_return_ready,
            True,
            "若合法 seed 无法提交，既有融合证书已把该分支回流终端家族。",
            TERMINAL_RETURN,
        ),
        row(
            "ZeroRowUnsignedSeedNoGoImported",
            zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "早期零行覆盖不能当作 signed source seed。",
            "只分析合法 seed 已提交的分支。",
        ),
        row(
            "UnsignedRowSkeletonAvailableForSeedBranch",
            unsigned_ready,
            True,
            "source tuple/carry-shell/P列锚/layered-wheel 已给候选 row 的 unsigned skeleton。",
            "仍缺 signed coefficient law。",
        ),
        row(
            "SignedWeightLawStillOpen",
            weight.get("exact_alpha_signed_weight_formula_proved") is False
            and weight.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False,
            False,
            "alpha signed weight law 已拆开，但 exact signed formula 与 pre-Cauchy 恒等式仍未证明。",
            NEXT_TARGET,
        ),
        row(
            "SignedLiftStillNeedsPointwiseValues",
            lift.get("pointwise_signed_alpha_coefficient_value_table_proved") is False,
            False,
            "signed lift 仍需要逐 skeleton row 的 signed value table。",
            NEXT_TARGET,
        ),
        row(
            "PrimitiveSummandExpressionStillOpen",
            pointwise.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "primitive summand 推前前 signed expression 未给出。",
            NEXT_TARGET,
        ),
        row(
            "UVKeySyncIsDownstreamAfterCoefficientLaw",
            key.get("complete_emitter_key_partition_router_closed") is True
            and uv_rank.get("exact_uv_map_rank_incidence_router_closed") is True,
            False,
            "complete key 与 ExactUV/rank 只能在 row 的 signed coefficient 已给出后同步验证。",
            "不能反向生成 coefficient law。",
        ),
        row(
            "DisintegrationWaitsForSignedCoefficients",
            disintegration.get("signed_fiber_disintegration_formal") is True
            or disintegration.get("status")
            == "alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open",
            False,
            "解积分形式需要已登记 signed coefficients 才能求和。",
            "不能由解积分反推 coefficient law。",
        ),
        row(
            "AcyclicSeedPrimitiveRowSignedCoefficientLawCurrentCorpusProved",
            False,
            False,
            "当前材料没有给合法 seed 分支内每条 primitive row 的 signed coefficient law。",
            NEXT_TARGET,
        ),
        row(
            "SeedSignedEmitterCurrentCorpusProved",
            False,
            False,
            "没有 signed coefficient law，seed signed row emitter 与推前前求和恒等式仍未证明。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 seed signed row emitter 证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-row-level-origin-generation-table-router.json"),
        "seed_fusion": load_json("prime-matrix-strict-acyclic-seed-terminal-fusion-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
        "unsigned": load_json("prime-matrix-strict-alpha-row-unsigned-skeleton-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "lift": load_json("prime-matrix-strict-alpha-signed-coefficient-lift-hardpoint-router.json"),
        "pointwise": load_json("prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"),
        "key": load_json("prime-matrix-strict-complete-emitter-key-partition-router.json"),
        "uv_rank": load_json("prime-matrix-strict-exact-uv-map-rank-incidence-router.json"),
        "disintegration": load_json("prime-matrix-clean-core-alpha-delta-disintegration-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_acyclic_seed_signed_row_emitter_router",
        "status": "acyclic_seed_signed_row_emitter_reduced_to_primitive_row_signed_coefficient_law_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "acyclic_seed_signed_row_emitter_router_closed": True,
        "seed_absent_branch_terminal_return_imported": True,
        "unsigned_row_skeleton_available": True,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "acyclic_seed_signed_row_emitter_rule_proved": False,
        "row_level_clean_core_origin_generation_table_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "terminal_return_if_no_seed_or_law": TERMINAL_RETURN,
        "coefficient_law_fields": coefficient_law_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} 的 seed 缺失分支已回流终端家族；在合法 seed 分支内，真正剩余是 "
            f"`{NEXT_TARGET}`。unsigned skeleton、ExactUV key 和解积分都不能反向生成该 law。"
        ),
        "plain_conclusion": (
            "本步继续下钻 seed signed row emitter。seed 不存在时已有终端回流；若 seed 存在，"
            "unsigned skeleton 已能定位候选行，但仍没有每条 primitive row 的 signed coefficient law。"
            "该 law 必须给出筛权来源、符号、local factor、截断/相位收费和推前前 alpha/delta 求和恒等式。"
            "当前材料未证明该 law，因此行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict acyclic seed signed row emitter 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"acyclic_seed_signed_row_emitter_router_closed={fmt_bool(result['acyclic_seed_signed_row_emitter_router_closed'])}",
        f"acyclic_seed_primitive_row_signed_coefficient_law_proved={fmt_bool(result['acyclic_seed_primitive_row_signed_coefficient_law_proved'])}",
        f"acyclic_seed_signed_row_emitter_rule_proved={fmt_bool(result['acyclic_seed_signed_row_emitter_rule_proved'])}",
        f"row_level_clean_core_origin_generation_table_proved={fmt_bool(result['row_level_clean_core_origin_generation_table_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. signed coefficient law 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["coefficient_law_fields"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
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
            "## 4. 下一真正单点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "缺失或失败时的命名回流：",
            "",
            "```text",
            result["terminal_return_if_no_seed_or_law"],
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
