#!/usr/bin/env python3
"""生成 strict 同 formal-unit pre-Cauchy alpha/delta 核恒等式攻坚证书。

用法示例：
  python3 experiments/prime_matrix_strict_same_formal_unit_kernel_identity_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.md"

TARGET = "SameFormalUnitPreCauchyAlphaDeltaKernelIdentityWithSignedPhiAndFiberDispersion"
NEXT_TARGET = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"

SOURCE_FILES = [
    "prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json",
    "prime-matrix-universal-formal-unit-extractor-router.json",
    "prime-matrix-finite-formal-unit-partition-key-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-no-loss-return-accounting-router.json",
    "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    "prime-matrix-strict-alpha-side-primitive-rule-router.json",
    "prime-matrix-strict-deterministic-alpha-row-emission-map-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-clean-core-geometric-phi-budget-bridge-router.json",
    "prime-matrix-strict-absolute-fiber-mass-dispersion-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
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


def kernel_table_fields() -> list[dict[str, str]]:
    """给出逐点 primitive 核表必须携带的字段。"""
    return [
        {
            "field": "formal_unit_id",
            "requirement": "锁定同一 witness/formal unit，不允许 source、Phi、fiber 分别换口径。",
        },
        {
            "field": "primitive_row_id",
            "requirement": "alpha/delta primitive row 的规范索引和排序，发射前确定。",
        },
        {
            "field": "source_tuple_hash",
            "requirement": "连接 source tuple、anchor 参数、branch path 和 local factor。",
        },
        {
            "field": "signed_weight",
            "requirement": "由 pre-Cauchy 算术恒等式给出，不由零行覆盖或 payment 反推。",
        },
        {
            "field": "uv_map",
            "requirement": "逐行输出 exact `(u,v)`，并与后续 fiber 分散同口径。",
        },
        {
            "field": "phi_atom",
            "requirement": "逐行给出 Phi/payment atom，含端点、重数、符号口径。",
        },
        {
            "field": "local_factor_nonzero",
            "requirement": "证明 local factor 非零；失败必须命名回流。",
        },
        {
            "field": "rank_or_multiplicity_certificate",
            "requirement": "对同一 `(u,v)`/fiber 给出 rank、bounded multiplicity 或分散证书。",
        },
        {
            "field": "return_tag",
            "requirement": "字段缺失、超预算、Phi 不等、rank 坍缩、canonical 泄漏均登记命名出口。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """审查核恒等式能否由当前材料直接闭合。"""
    breaker = data["breaker"]
    formal = data["formal"]
    key = data["key"]
    source_record = data["source_record"]
    noloss = data["noloss"]
    source_tuple = data["source_tuple"]
    alpha_rule = data["alpha_rule"]
    emission = data["emission"]
    weight = data["weight"]
    disintegration = data["disintegration"]
    phi = data["phi"]
    absolute = data["absolute"]
    source_loop = data["source_loop"]
    zero_nogo = data["zero_nogo"]

    return [
        row(
            "KernelIdentityTargetActive",
            breaker.get("next_direct_attack_target") == TARGET,
            False,
            "上一层已把非递归破环包压成同 formal-unit pre-Cauchy alpha/delta 核恒等式。",
            TARGET,
        ),
        row(
            "FormalUnitExtractionAndNoLossAvailable",
            formal.get("universal_formal_unit_extractor_theorem") is True
            and key.get("finite_formal_unit_partition_key_closed") is True
            and source_record.get("concrete_formal_unit_source_record_closed") is True
            and noloss.get("no_loss_return_accounting_closed") is True,
            True,
            "任意假设 witness 可被分割成有限 formal units，且义务不丢失。",
            "这只保证记录守恒，不给 signed coefficient value。",
        ),
        row(
            "SourceTupleContainerAvailableButNotCoefficient",
            source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True,
            True,
            "source tuple/anchor 参数字段和哈希纪律可用。",
            "容器字段不能替代 primitive row 发射公式或 signed 权重公式。",
        ),
        row(
            "PrimitiveRuleStillNeedsEmissionAndWeight",
            alpha_rule.get("alpha_side_primitive_rule_router_closed") is True
            and alpha_rule.get("actual_noncanonical_alpha_side_primitive_rule_proved") is False,
            False,
            "alpha 侧 primitive rule 已拆成定义域、发射映射、权重公式、输出字段和回流。",
            "缺少逐 primitive row 的显式发射和系数权重。",
        ),
        row(
            "EmissionMapOpenAtAnchorPhaseFormula",
            emission.get("deterministic_alpha_row_emission_map_router_closed") is True
            and emission.get("deterministic_alpha_primitive_row_emission_map_proved") is False,
            False,
            "确定性发射映射已排除 downstream/payment 反选。",
            emission.get("next_direct_attack_target", "AlphaRowAnchorPhaseEmissionFormulaLedger"),
        ),
        row(
            "WeightLawOpenAtIndependentArithmeticIdentity",
            weight.get("alpha_signed_weight_law_router_closed") is True
            and weight.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False,
            False,
            "signed 权重律已排除零行几何和 payment 反推。",
            weight.get("next_direct_attack_target", "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"),
        ),
        row(
            "DisintegrationFormalButNeedsPointwiseTable",
            disintegration.get("signed_fiber_disintegration_formal") is True
            or disintegration.get("status") == "alpha_delta_lift_reduced_to_registered_signed_disintegration_dictionary_open",
            False,
            "给定 signed source 后，逐纤维解积分只是形式闭合。",
            "必须先有逐 primitive row 核表，才能做 Phi 推前求和。",
        ),
        row(
            "PhiGeometryDoesNotCreateEquality",
            phi.get("geometry_does_not_prove_phi_pushforward_identity") is True
            or phi.get("status") == "geometric_phi_budget_bridge_closed_signed_source_and_budget_open",
            False,
            "几何 Phi/payment base 和预算形状已知。",
            "Phi_*nu 等于 payment-side 系数仍需要逐点核表求和证明。",
        ),
        row(
            "ExactUVDispersionStillNeedsSameTableRank",
            absolute.get("absolute_fiber_mass_dispersion_router_closed") is True
            and absolute.get("preterminal_exact_uv_fiber_absolute_mass_dispersion_proved") is False,
            False,
            "ExactUV fiber 分散已压到 primitive emitter multiplicity。",
            "没有同一 primitive key 表，就无法把 rank/multiplicity 证书与 signed source 对齐。",
        ),
        row(
            "ReverseSourceAndZeroRowRecoveryBlocked",
            source_loop.get("circular_reverse_derivation_rejected") is True
            and zero_nogo.get("zero_row_seed_extraction_blocked") is True,
            True,
            "不能从 downstream payment skeleton 或早期零行 unsigned cover 反推 source。",
            "核表必须正向提交，不能后验恢复。",
        ),
        row(
            "KernelIdentityCurrentCorpusProved",
            False,
            False,
            "当前材料没有逐 primitive row 的同 formal-unit alpha/delta 核表。",
            NEXT_TARGET,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同 formal-unit 核恒等式攻坚证书。"""
    data = {
        "breaker": load_json("prime-matrix-strict-nonrecursive-constructor-signed-lift-breaker-router.json"),
        "formal": load_json("prime-matrix-universal-formal-unit-extractor-router.json"),
        "key": load_json("prime-matrix-finite-formal-unit-partition-key-router.json"),
        "source_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "noloss": load_json("prime-matrix-no-loss-return-accounting-router.json"),
        "source_tuple": load_json("prime-matrix-concrete-source-tuple-anchor-parameter-router.json"),
        "alpha_rule": load_json("prime-matrix-strict-alpha-side-primitive-rule-router.json"),
        "emission": load_json("prime-matrix-strict-deterministic-alpha-row-emission-map-router.json"),
        "weight": load_json("prime-matrix-strict-alpha-signed-weight-law-router.json"),
        "disintegration": load_json("prime-matrix-clean-core-alpha-delta-disintegration-router.json"),
        "phi": load_json("prime-matrix-clean-core-geometric-phi-budget-bridge-router.json"),
        "absolute": load_json("prime-matrix-strict-absolute-fiber-mass-dispersion-router.json"),
        "source_loop": load_json("prime-matrix-clean-core-source-loop-cut-router.json"),
        "zero_nogo": load_json("prime-matrix-hypothetical-zero-row-seed-no-go-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    bridge_fields_closed = all(row_item["closed"] for row_item in rows if row_item["gate"] != "KernelIdentityCurrentCorpusProved")
    pointwise_table_proved = False
    return {
        "certificate_type": "prime_matrix_strict_same_formal_unit_kernel_identity_attack_router",
        "status": "same_formal_unit_kernel_identity_reduced_to_pointwise_primitive_kernel_table_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "target_input_before_router": TARGET,
        "kernel_identity_attack_router_closed": True,
        "bridge_fields_closed": bridge_fields_closed,
        "formal_unit_no_loss_available": True,
        "source_tuple_container_available": True,
        "reverse_source_recovery_blocked": True,
        "zero_row_unsigned_recovery_blocked": True,
        "pointwise_primitive_kernel_table_proved": pointwise_table_proved,
        "same_formal_unit_kernel_identity_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_TARGET,
        "kernel_table_fields": kernel_table_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "frontier_equivalence": (
            f"{TARGET} 不能由 formal-unit 记录守恒、几何 Phi 基底或 signed 解积分形式自动推出；"
            f"它等价于先提交 `{NEXT_TARGET}`：逐 primitive row 给出 source tuple、signed weight、"
            "exact `(u,v)`、Phi atom、local factor 非零、rank/multiplicity 证书和命名回流。"
        ),
        "plain_conclusion": (
            "本步直接攻核恒等式本身。已有 formal unit 抽取、finite key、source record 和 no-loss 账本，"
            "可以保证任意假设 witness 的对象被同一账本命名且不丢失；但这些账本不含 alpha/delta 的逐点"
            " signed coefficient value。几何 Phi、解积分和 exact-UV 分散都需要同一张 primitive 核表来对齐。"
            "因此真正最窄破坏输入继续压缩为逐点同 formal-unit primitive alpha/delta 核表，而当前仍未闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 同 formal-unit 核恒等式攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"kernel_identity_attack_router_closed={fmt_bool(result['kernel_identity_attack_router_closed'])}",
        f"bridge_fields_closed={fmt_bool(result['bridge_fields_closed'])}",
        f"formal_unit_no_loss_available={fmt_bool(result['formal_unit_no_loss_available'])}",
        f"source_tuple_container_available={fmt_bool(result['source_tuple_container_available'])}",
        f"reverse_source_recovery_blocked={fmt_bool(result['reverse_source_recovery_blocked'])}",
        f"zero_row_unsigned_recovery_blocked={fmt_bool(result['zero_row_unsigned_recovery_blocked'])}",
        f"pointwise_primitive_kernel_table_proved={fmt_bool(result['pointwise_primitive_kernel_table_proved'])}",
        f"same_formal_unit_kernel_identity_proved={fmt_bool(result['same_formal_unit_kernel_identity_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩等价",
        "",
        result["frontier_equivalence"],
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
            "## 3. 逐点核表字段",
            "",
            "| field | requirement |",
            "| --- | --- |",
        ]
    )
    for item in result["kernel_table_fields"]:
        lines.append(
            "| `{field}` | {requirement} |".format(
                field=table_cell(item["field"]),
                requirement=table_cell(item["requirement"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一真正最窄点",
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
