#!/usr/bin/env python3
"""生成 strict 边界帽 formal-unit 类型压缩硬攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_boundary_cap_type_compression_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-boundary-cap-type-compression-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-boundary-cap-type-compression-router.json"
OUT_MD = DOCS / "prime-matrix-strict-boundary-cap-type-compression-router.md"

TYPE_COMPRESSION = "BoundaryCapFormalUnitTypeCompressionDichotomy"
FORCED_LOWER = "BoundaryCapForcedFormalUnitObligationLowerBound"
TYPE_UPPER_OR_DEFECT = "BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect"
REPEAT_TO_RETURN = "RepeatedBoundaryTypeToStableSameLabelReturn"
LABEL_QUOTIENT = "BoundaryCapLabelPreservingQuotientEntropyDeficit"
DRIFT_DEFECT = "BoundaryCapTypeDriftToRegisteredPDECSAEColumnReturn"
LABEL_PRODUCT = "StableReturnLargeLabelSupportProductLowerBound"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-stable-short-return-defect-attack-router.json",
    "prime-matrix-early-zero-contradiction-matrix-router.json",
    "prime-matrix-formal-unit-source-record-router.json",
    "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    "prime-matrix-strict-alpha-anchor-collar-overload-return-router.json",
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


def type_key_fields() -> list[dict[str, str]]:
    """给出边界帽行无关类型键字段。"""
    return [
        {
            "field": "source_family_id",
            "role": "锁定 Endpoint/TailAnchor/HighOverlap/ColoredCorridor/SmoothCore/Sparse/RankinConstant 等有限来源族。",
        },
        {
            "field": "branch_type",
            "role": "区分 physical、phase_defect、carry_cofactor、return、quotient/reuse 等分支。",
        },
        {
            "field": "window_shape",
            "role": "只保留边界帽相对形状，不包含绝对行号；否则无法形成短复现。",
        },
        {
            "field": "D0,K,Omega",
            "role": "继承核心尺度、截断与重叠阈值；无参数时写 canonical null。",
        },
        {
            "field": "phase_key",
            "role": "相位、residue、anchor、fixed-core 或 identity；漂移必须登记为 phase defect。",
        },
        {
            "field": "anchor_set_hash",
            "role": "由同一 formal unit 的 payload 复算 A；不得后验换锚。",
        },
        {
            "field": "carry_cofactor_signature",
            "role": "记录 carry-shell、cofactor-depth、anchor-collar 需要保持的行无关壳签名。",
        },
        {
            "field": "label_support_skeleton",
            "role": "记录要在短复现中保持的素标签骨架；若漂移则进入缺陷分支。",
        },
    ]


def compression_logic_rows() -> list[dict[str, str]]:
    """给出类型压缩的形式逻辑。"""
    return [
        {
            "case": "T<N",
            "meaning": "边界帽 forced obligations 数 N 大于行无关类型数 T。",
            "consequence": "鸽巢给出两个不同边界行/位置共享同一类型，位移 Delta 小于边界帽高度。",
            "remaining": REPEAT_TO_RETURN,
        },
        {
            "case": "T>=N",
            "meaning": "类型数没有被压缩，反例链必须在边界帽中持续产生新 phase/anchor/carry/label 类型。",
            "consequence": "这不是自由增长；按 no-loss return 必须登记为 phase defect 或新 layer payload。",
            "remaining": TYPE_UPPER_OR_DEFECT,
        },
        {
            "case": "Complete key repeat",
            "meaning": "完整 key 在短位移下重复。",
            "consequence": "标签字段保持，可接同 formal unit 短复现；但当前缺少完整 key 数量上界。",
            "remaining": LABEL_QUOTIENT,
        },
        {
            "case": "Coarse key repeat",
            "meaning": "为了制造鸽巢重复而忽略 label_support_skeleton 或 phase/carry 字段。",
            "consequence": "重复不再保证同一素标签集 Q，必须证明漂移进入 PDEC/SAE/ColumnCRT。",
            "remaining": DRIFT_DEFECT,
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成类型压缩硬攻判定表。"""
    previous = data["previous"]
    early_zero = data["early_zero"]
    formal_record = data["formal_record"]
    hash_stability = data["hash_stability"]
    anchor_return = data["anchor_return"]

    return [
        row(
            "BoundaryCapTypeCompressionTargetActive",
            previous.get("next_direct_attack_target") == TYPE_COMPRESSION,
            False,
            "上一层把稳定短复现的上游强制机制压成边界帽 formal-unit 类型压缩。",
            TYPE_COMPRESSION,
        ),
        row(
            "EarlyZeroBoundaryCapPressureImported",
            early_zero.get("no_unnamed_exit_for_early_zero") is True
            and early_zero.get("strongest_current_frontier") == "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn",
            True,
            "早期零行假设已被 CLB、carry-shell、cofactor-depth、anchor-collar 与命名终端矩阵夹住。",
            "forced boundary-cap records exist only inside named contradiction matrix。",
        ),
        row(
            "FormalUnitRecordAndHashStabilityImported",
            formal_record.get("concrete_formal_unit_source_record_closed") is True
            and hash_stability.get("canonical_formal_unit_hash_stability_closed") is True,
            True,
            "任意假设 witness 可生成有限无漏 formal-unit 记录，且 source/return 哈希稳定。",
            "记录保真可用，但还不是类型数上界。",
        ),
        row(
            "NoFreeTypeCompressionLemma",
            True,
            True,
            "formal-unit 哈希是保真命名纪律：它防止账本换口径，但不会自动让不同 witness 记录落入少数类型。",
            "必须另证保标签商类型的熵亏损，或把类型增长登记为相位缺陷。",
        ),
        row(
            "RowFreeTypeKeyDefinitionClosed",
            True,
            True,
            "行无关 boundary-cap type key 的字段可定义：source family、branch、window shape、phase、anchor、carry/cofactor 与 label skeleton。",
            "定义闭合，不代表类型数上界或复现推出同标签。",
        ),
        row(
            "PigeonholeSkeletonConditionalClosed",
            True,
            True,
            "若 forced obligation 数 N 大于保标签 row-free type 数 T，则同类型短复现；若 T>=N，则必须解释类型爆炸。",
            f"{FORCED_LOWER} AND {TYPE_UPPER_OR_DEFECT}",
        ),
        row(
            "BoundaryCapForcedObligationLowerBoundCurrentCorpusProved",
            False,
            False,
            "尚未给出边界帽中必须保留的 forced formal-unit obligations 的有效下界 N。",
            FORCED_LOWER,
        ),
        row(
            "RowFreeTypeUpperOrExplosionDefectCurrentCorpusProved",
            False,
            False,
            "尚未证明保标签 row-free type alphabet 上界 T<N，或 T>=N 时自动产生登记相位缺陷。",
            TYPE_UPPER_OR_DEFECT,
        ),
        row(
            "FullKeyRepeatWouldPreserveLabelsButNoCountDeficit",
            True,
            True,
            "若完整 canonical key 重复，source_family、phase_key、anchor/carry-shell 和标签字段同时重复，可接 CRT 短复现；但当前没有证明完整 key 的数量小于 forced records。",
            LABEL_QUOTIENT,
        ),
        row(
            "CoarseTypeRepeatDoesNotPreserveLabelSupport",
            True,
            True,
            "若为了鸽巢而忽略标签字段，重复类型不再保证同一标签集 Q 保持，CRT 的 prod(Q)|Delta 后半段不能调用。",
            f"{DRIFT_DEFECT} AND {LABEL_PRODUCT}",
        ),
        row(
            "AnchorCollarOverloadReturnSchemaImported",
            anchor_return.get("alpha_formula_anchor_collar_overload_named_return_ledger_closed") is True,
            True,
            "短纤维饱和、端点相位缺陷、孤立 sparse escape 与固定位移复用已有命名回流 schema。",
            "schema closed; terminal exclusion still open。",
        ),
        row(
            "LabelPreservingQuotientEntropyDeficitCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出边界帽内保标签商类型数小于 forced records 的定量熵亏损。",
            LABEL_QUOTIENT,
        ),
        row(
            "TypeDriftToRegisteredDefectCurrentCorpusProved",
            False,
            False,
            "当前材料没有证明所有破坏标签保持的类型漂移都以同一 formal unit 权重进入 PDEC/SAE/ColumnCRT 并被排斥。",
            DRIFT_DEFECT,
        ),
        row(
            "BoundaryCapFormalUnitTypeCompressionDichotomyCurrentCorpusProved",
            False,
            False,
            "类型压缩本身保留原 N/T/复现骨架，同时新增审查结论：哈希保真不能替代保标签商类型熵亏损。",
            f"{FORCED_LOWER} AND {TYPE_UPPER_OR_DEFECT} AND {REPEAT_TO_RETURN}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "尚未得到反例链与真实结构链之间的终端矛盾；DStructure/Rankin 独立验收仍保留。",
            f"{LABEL_QUOTIENT} AND {DRIFT_DEFECT} AND {LABEL_PRODUCT} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造边界帽类型压缩硬攻证书。"""
    data = {
        "previous": load_json("prime-matrix-strict-stable-short-return-defect-attack-router.json"),
        "early_zero": load_json("prime-matrix-early-zero-contradiction-matrix-router.json"),
        "formal_record": load_json("prime-matrix-formal-unit-source-record-router.json"),
        "hash_stability": load_json("prime-matrix-canonical-formal-unit-hash-stability-router.json"),
        "anchor_return": load_json("prime-matrix-strict-alpha-anchor-collar-overload-return-router.json"),
    }
    rows = build_rows(data)
    after = f"{FORCED_LOWER} AND {TYPE_UPPER_OR_DEFECT} AND {REPEAT_TO_RETURN}"
    return {
        "certificate_type": "prime_matrix_strict_boundary_cap_type_compression_router",
        "status": "boundary_cap_type_compression_reduced_to_label_preserving_quotient_entropy_deficit_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hardpoint_before_router": TYPE_COMPRESSION,
        "hardpoint_after_router": after,
        "refined_nonfree_subatoms": f"{LABEL_QUOTIENT} AND {DRIFT_DEFECT}",
        "row_free_type_key_definition_closed": True,
        "pigeonhole_skeleton_conditional_closed": True,
        "no_free_type_compression_lemma_proved": True,
        "full_key_repeat_would_preserve_labels": True,
        "coarse_type_repeat_loses_label_support": True,
        "boundary_cap_forced_obligation_lower_bound_proved": False,
        "row_free_type_upper_or_explosion_defect_proved": False,
        "repeated_type_to_stable_same_label_return_proved": False,
        "label_preserving_quotient_entropy_deficit_proved": False,
        "type_drift_to_registered_defect_proved": False,
        "boundary_cap_type_compression_dichotomy_proved": False,
        "stable_return_large_label_product_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LABEL_QUOTIENT,
        "parallel_required_input": DRIFT_DEFECT,
        "still_required_after_type_compression": [LABEL_PRODUCT, DSTRUCTURE],
        "nonclosing_reason": (
            "现有 formal-unit 记录与哈希闭合的是保真命名，不是压缩计数。"
            "完整 key 重复足以保持标签但没有数量亏损；粗 key 可制造重复但丢失标签保持，"
            "因此必须新增保标签商类型熵亏损或把所有标签漂移登记为已排斥缺陷。"
        ),
        "conditional_contradiction_pipeline": [
            "EarlyZeroRowWithinP",
            "UniversalFormalUnitExtractor gives finite no-loss formal-unit records",
            "Boundary row-free type map pi is defined",
            "N_forced > T_type gives repeated type within boundary cap",
            "Repeated type -> stable same-label return",
            "Label product lower bound gives prod(Q)>|Delta|",
            "CRT short recurrence lemma gives contradiction",
        ],
        "type_key_fields": type_key_fields(),
        "compression_logic_rows": compression_logic_rows(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"`{TYPE_COMPRESSION}` 继续保持原 N/T/复现骨架：早期零行给出有限无漏 formal-unit obligations，"
            "行无关 type key 与条件鸽巢骨架已闭合。新增审查结论是：已闭合的 formal-unit 哈希纪律"
            "只保证同一对象不换名、不漏账，不自动给边界帽内类型数小于 forced records 的鸽巢亏损。"
            "完整 key 重复会保留标签但未证数量压缩；粗 key 重复会丢失标签集 Q，CRT 短复现矛盾无法调用。"
            f"因此真正最窄新增输入是 `{LABEL_QUOTIENT}`，并行必须保留 `{DRIFT_DEFECT}`。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict 边界帽 formal-unit 类型压缩硬攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"row_free_type_key_definition_closed={fmt_bool(result['row_free_type_key_definition_closed'])}",
        f"pigeonhole_skeleton_conditional_closed={fmt_bool(result['pigeonhole_skeleton_conditional_closed'])}",
        f"no_free_type_compression_lemma_proved={fmt_bool(result['no_free_type_compression_lemma_proved'])}",
        f"full_key_repeat_would_preserve_labels={fmt_bool(result['full_key_repeat_would_preserve_labels'])}",
        f"coarse_type_repeat_loses_label_support={fmt_bool(result['coarse_type_repeat_loses_label_support'])}",
        f"boundary_cap_forced_obligation_lower_bound_proved={fmt_bool(result['boundary_cap_forced_obligation_lower_bound_proved'])}",
        f"row_free_type_upper_or_explosion_defect_proved={fmt_bool(result['row_free_type_upper_or_explosion_defect_proved'])}",
        f"repeated_type_to_stable_same_label_return_proved={fmt_bool(result['repeated_type_to_stable_same_label_return_proved'])}",
        f"label_preserving_quotient_entropy_deficit_proved={fmt_bool(result['label_preserving_quotient_entropy_deficit_proved'])}",
        f"type_drift_to_registered_defect_proved={fmt_bool(result['type_drift_to_registered_defect_proved'])}",
        f"boundary_cap_type_compression_dichotomy_proved={fmt_bool(result['boundary_cap_type_compression_dichotomy_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["hardpoint_before_router"],
        "  => NoFreeTypeCompressionLemma",
        f"  => {result['hardpoint_after_router']}",
        f"  with refined nonfree gate: {result['refined_nonfree_subatoms']}",
        "```",
        "",
        result["nonclosing_reason"],
        "",
        "条件矛盾流水线：",
        "",
        "```text",
    ]
    for item in result["conditional_contradiction_pipeline"]:
        lines.append(item)
        if item != result["conditional_contradiction_pipeline"][-1]:
            lines.append("  ->")
    lines.extend(
        [
            "```",
            "",
            "## 2. 行无关 type key",
            "",
            "| field | role |",
            "| --- | --- |",
        ]
    )
    for item in result["type_key_fields"]:
        lines.append(
            "| `{field}` | {role} |".format(
                field=table_cell(item["field"]),
                role=table_cell(item["role"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 压缩二分",
            "",
            "| case | meaning | consequence | remaining |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["compression_logic_rows"]:
        lines.append(
            "| `{case}` | {meaning} | {consequence} | {remaining} |".format(
                case=table_cell(item["case"]),
                meaning=table_cell(item["meaning"]),
                consequence=table_cell(item["consequence"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一步最窄硬攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行必须保留：",
            "",
            "```text",
            result["parallel_required_input"],
            "```",
            "",
            "类型压缩若闭合后，仍需接上：",
            "",
            "```text",
            " AND ".join(result["still_required_after_type_compression"]),
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
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
