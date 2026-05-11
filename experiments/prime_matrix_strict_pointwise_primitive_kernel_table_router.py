#!/usr/bin/env python3
"""生成 strict 逐点 primitive alpha/delta 核表攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_pointwise_primitive_kernel_table_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pointwise-primitive-kernel-table-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-pointwise-primitive-kernel-table-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pointwise-primitive-kernel-table-router.md"

TARGET = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
PRIMARY = "AlphaRowAnchorPhaseEmissionFormulaLedger"
WEIGHT = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"

SOURCE_FILES = [
    "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json",
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-actual-emitter-source-table-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
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


def table_axioms() -> list[dict[str, str]]:
    """列出逐点 primitive 核表的最小公理。"""
    return [
        {
            "axiom": "row_existence",
            "meaning": "每个 source tuple 发射有限、有序的 alpha/delta primitive rows。",
        },
        {
            "axiom": "weight_value",
            "meaning": "每行 signed weight 来自独立 pre-Cauchy 算术恒等式。",
        },
        {
            "axiom": "uv_phi_sync",
            "meaning": "每行同时输出 exact `(u,v)` 与 Phi/payment atom，且符号和重数同口径。",
        },
        {
            "axiom": "nonzero_local_factor",
            "meaning": "local factor 非零；零权重、符号冲突和未登记项命名回流。",
        },
        {
            "axiom": "rank_multiplicity",
            "meaning": "同一表上证明 `(u,v)` fiber 的 bounded multiplicity/rank 或分散。",
        },
        {
            "axiom": "same_unit_no_recovery",
            "meaning": "全部字段都在同一 formal unit 中正向给出，不从 payment/零行/终端门反向恢复。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查逐点 primitive 核表的三条必要腿。"""
    kernel = data["kernel"]
    emission = data["emission"]
    weight = data["weight"]
    absolute = data["absolute"]
    uv_rank = data["uv_rank"]
    fixed_pair = data["fixed_pair"]
    key = data["key"]
    source_table = data["source_table"]
    alpha_rule = data["alpha_rule"]
    disintegration = data["disintegration"]

    return [
        row(
            "PointwiseKernelTableTargetActive",
            kernel.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把同 formal-unit 核恒等式压成逐点 primitive alpha/delta 核表。",
            TARGET,
        ),
        row(
            "AlphaRuleContainerReady",
            alpha_rule.get("alpha_side_primitive_rule_router_closed") is True,
            True,
            "alpha 侧规则字段和失败分类已被列出。",
            "仍缺逐行生成和值。",
        ),
        row(
            "RowEmissionFormulaMissing",
            emission.get("deterministic_alpha_row_emission_map_router_closed") is True
            and emission.get("alpha_row_anchor_phase_emission_formula_proved") is False,
            False,
            "确定性发射映射已拒绝后验选择，但没有 A/D0/K/Omega/phase 到 row 的公式。",
            PRIMARY,
        ),
        row(
            "SignedWeightIdentityMissing",
            weight.get("alpha_signed_weight_law_router_closed") is True
            and weight.get("independent_noncanonical_precauchy_arithmetic_identity_statement_proved") is False,
            False,
            "signed weight 必须来自独立 pre-Cauchy 算术恒等式；当前只有 no-go 和字段分解。",
            WEIGHT,
        ),
        row(
            "ExactUVRankMultiplicityMissing",
            absolute.get("absolute_fiber_mass_dispersion_router_closed") is True
            and uv_rank.get("exact_uv_map_rank_incidence_router_closed") is True
            and fixed_pair.get("fixed_pair_fiber_bound_router_closed") is True
            and key.get("complete_emitter_key_partition_router_closed") is True
            and absolute.get("preterminal_exact_uv_fiber_absolute_mass_dispersion_proved") is False,
            False,
            "ExactUV/fixed-pair/key partition 路线已定位，但没有同一 primitive 核表上的 rank/multiplicity 证书。",
            RANK,
        ),
        row(
            "EmitterSourceTableWouldNeedSameRows",
            source_table.get("actual_emitter_source_table_router_closed") is True
            and source_table.get("actual_noncanonical_primitive_emitter_source_table_proved") is False,
            False,
            "emitter/source table 路线也需要相同 primitive rows，不能反过来自证核表。",
            "Pointwise primitive rows first; source table second.",
        ),
        row(
            "DisintegrationNotEnoughWithoutRows",
            disintegration.get("status") == "alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open"
            or disintegration.get("signed_fiber_disintegration_formal") is True,
            False,
            "逐纤维解积分只是有 rows 后的求和形式。",
            "先提交逐点核表。",
        ),
        row(
            "PointwiseKernelTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有同时给出行公式、权重恒等式和同表 rank/multiplicity 的逐点核表。",
            f"{PRIMARY} AND {WEIGHT} AND {RANK}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造逐点 primitive 核表攻坚证书。"""
    data = {
        "kernel": load_json("prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json"),
        "emission": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "absolute": load_json("prime-matrix-strict-absolute-fiber-mass-dispersion-router.json"),
        "uv_rank": load_json("prime-matrix-strict-exact-uv-map-rank-incidence-router.json"),
        "fixed_pair": load_json("prime-matrix-strict-fixed-pair-fiber-bound-router.json"),
        "key": load_json("prime-matrix-strict-complete-emitter-key-partition-router.json"),
        "source_table": load_json("prime-matrix-strict-actual-emitter-source-table-router.json"),
        "alpha_rule": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "disintegration": load_json("prime-matrix-clean-core-alpha-delta-disintegration-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    return {
        "certificate_type": "prime_matrix_strict_pointwise_primitive_kernel_table_router",
        "status": "pointwise_primitive_kernel_table_reduced_to_row_formula_weight_identity_rank_certificate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_input_before_router": TARGET,
        "pointwise_kernel_table_router_closed": True,
        "alpha_rule_container_ready": True,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "pointwise_primitive_kernel_table_proved": False,
        "same_formal_unit_kernel_identity_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": PRIMARY,
        "parallel_required_inputs": [WEIGHT, RANK],
        "table_axioms": table_axioms(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_reduction": (
            f"{TARGET} => {PRIMARY} AND {WEIGHT} AND {RANK}. "
            f"其中 `{PRIMARY}` 是当前优先硬点：没有行发射公式，核表连行集合都没有，"
            "后续权重、Phi 推前和 rank/multiplicity 都无法绑定。"
        ),
        "plain_conclusion": (
            "逐点 primitive 核表被进一步压成三项必要输入：alpha row anchor/phase 发射公式、"
            "独立 pre-Cauchy signed 权重恒等式、同一表上的 ExactUV rank/multiplicity 证书。"
            "当前最窄优先点是 alpha row 发射公式；因为没有它，核表没有可赋权的 row，也无法对齐 Phi 或 `(u,v)` fiber。"
            "因此自足路线仍未闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 逐点 primitive 核表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pointwise_kernel_table_router_closed={fmt_bool(result['pointwise_kernel_table_router_closed'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"independent_noncanonical_precauchy_arithmetic_identity_statement_proved={fmt_bool(result['independent_noncanonical_precauchy_arithmetic_identity_statement_proved'])}",
        f"same_unit_exact_uv_rank_multiplicity_certificate_proved={fmt_bool(result['same_unit_exact_uv_rank_multiplicity_certificate_proved'])}",
        f"pointwise_primitive_kernel_table_proved={fmt_bool(result['pointwise_primitive_kernel_table_proved'])}",
        f"same_formal_unit_kernel_identity_proved={fmt_bool(result['same_formal_unit_kernel_identity_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 前沿压缩",
        "",
        result["frontier_reduction"],
        "",
        "## 2. 判定表",
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
            "## 3. 核表公理",
            "",
            "| axiom | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["table_axioms"]:
        lines.append(
            "| `{axiom}` | {meaning} |".format(
                axiom=table_cell(item["axiom"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一优先硬点",
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
