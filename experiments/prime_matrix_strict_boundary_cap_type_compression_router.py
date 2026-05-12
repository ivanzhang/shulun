#!/usr/bin/env python3
"""生成 strict 边界帽 formal-unit 类型压缩路由证书。

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
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.md"

TYPE_COMPRESSION = "BoundaryCapFormalUnitTypeCompressionDichotomy"
FORCED_LOWER = "BoundaryCapForcedFormalUnitObligationLowerBound"
TYPE_UPPER_OR_DEFECT = "BoundaryCapRowFreeTypeAlphabetUpperBoundOrTypeExplosionDefect"
REPEAT_TO_RETURN = "RepeatedBoundaryTypeToStableSameLabelReturn"
SHORT_RETURN = "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect"
LABEL_PRODUCT = "StableReturnLargeLabelSupportProductLowerBound"
DRIFT_DEFECT = "SignatureDriftToRegisteredPhaseDefectTheorem"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.json",
    MONOGRAPH / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    MONOGRAPH / "prime-matrix-universal-formal-unit-extractor-router.json",
    MONOGRAPH / "prime-matrix-formal-unit-partition-coverage-router.json",
    MONOGRAPH / "prime-matrix-source-family-assignment-totality-router.json",
    MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.json",
    MONOGRAPH / "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    MONOGRAPH / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json",
    MONOGRAPH / "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    MONOGRAPH / "prime-matrix-early-zero-contradiction-matrix-router.json",
    DOCS / "phase-recurrence-pressure-scan.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
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
            "case": "Repeated type",
            "meaning": "同一行无关 type key 在短位移下复现。",
            "consequence": "若 type key 足够完整，得到同 formal unit 同标签短复现；再接标签乘积下界和 CRT 矛盾。",
            "remaining": f"{REPEAT_TO_RETURN} AND {LABEL_PRODUCT}",
        },
        {
            "case": "Drifting type",
            "meaning": "为避免复现而改变 phase_key、anchor_set_hash、carry/cofactor 或 label skeleton。",
            "consequence": "漂移必须作为已登记坏窗/位移/相位缺陷进入 PDEC/SAE/ColumnCRT。",
            "remaining": DRIFT_DEFECT,
        },
    ]


def build_rows(
    stable: dict[str, Any],
    extractor: dict[str, Any],
    partition: dict[str, Any],
    assignment: dict[str, Any],
    noloss: dict[str, Any],
    hash_stability: dict[str, Any],
    source_tuple: dict[str, Any],
    anchor_recon: dict[str, Any],
    early_zero: dict[str, Any],
    phase_scan: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "BoundaryTypeCompressionInputActive",
            "closed": stable.get("next_direct_attack_target") == TYPE_COMPRESSION,
            "proved": False,
            "meaning": "上一层已把首要硬点固定为边界帽 formal-unit 类型压缩。",
            "remaining": TYPE_COMPRESSION,
        },
        {
            "gate": "UniversalFormalUnitExtractorImported",
            "closed": extractor.get("universal_extractor_theorem_closed") is True,
            "proved": True,
            "meaning": "任意早期零行 witness 可产出有限、无漏、可哈希的 formal unit records。",
            "remaining": "这只给有限记录，不给类型数量上界。",
        },
        {
            "gate": "PartitionAndAssignmentImported",
            "closed": partition.get("formal_unit_partition_coverage_lemma_closed") is True
            and assignment.get("source_family_assignment_totality_closed") is True,
            "proved": True,
            "meaning": "义务域 O(w) 已被有限 key-fibers 覆盖，且每个 key 归入有限 source family 或命名 return。",
            "remaining": "仍需边界帽上的计数压缩。",
        },
        {
            "gate": "NoLossAndHashStabilityImported",
            "closed": noloss.get("no_loss_return_accounting_closed") is True
            and hash_stability.get("canonical_formal_unit_hash_stability_closed") is True,
            "proved": True,
            "meaning": "未闭合对象不会丢失，formal_unit/source_tuple/hash 在回流下稳定。",
            "remaining": "稳定命名不等于类型数足够小。",
        },
        {
            "gate": "AnchorAndSourceTupleFieldsImported",
            "closed": source_tuple.get("source_tuple_anchor_parameter_schema_closed") is True
            and anchor_recon.get("anchor_set_reconstruction_certificate_ledger") is True,
            "proved": True,
            "meaning": "A、D0/K/Omega、phase_rule、anchor_set_hash 可由同一 formal unit payload 复算。",
            "remaining": "需要将这些字段投影成行无关 type key 并计数。",
        },
        {
            "gate": "EarlyZeroRigidityPressureImported",
            "closed": early_zero.get("no_unnamed_exit_for_early_zero") is True,
            "proved": True,
            "meaning": "早期零行已被 CLB、carry-shell、cofactor-depth、anchor-collar 与终端无第四出口约束。",
            "remaining": early_zero.get("strongest_current_frontier", "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn"),
        },
        {
            "gate": "RowFreeTypeKeyDefinitionClosed",
            "closed": True,
            "proved": True,
            "meaning": "可定义不含绝对行号的 boundary-cap type key；重复才有可能推出短复现。",
            "remaining": "定义闭合，不代表类型数上界或复现推出同标签。",
        },
        {
            "gate": "PigeonholeSkeletonConditionalClosed",
            "closed": True,
            "proved": True,
            "meaning": "若 forced obligation 数 N 大于 row-free type 数 T，则同类型短复现；若 T>=N，则必须解释类型爆炸。",
            "remaining": f"{FORCED_LOWER} AND {TYPE_UPPER_OR_DEFECT}",
        },
        {
            "gate": "PhaseScanImportedAsHeuristicSupportOnly",
            "closed": phase_scan.get("status")
            == "label_modulus_product_exceeds_P_but_short_recurrence_not_full_in_samples",
            "proved": True,
            "meaning": "大标签乘积超过 P 支持 CRT 后半段，但实验不能证明类型压缩。",
            "remaining": "仍需正式 N/T 不等式。",
        },
        {
            "gate": "BoundaryCapForcedObligationLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未给出边界帽中必须保留的 forced formal-unit obligations 的有效下界 N。",
            "remaining": FORCED_LOWER,
        },
        {
            "gate": "RowFreeTypeUpperOrExplosionDefectCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 row-free type alphabet 上界 T<N，或 T>=N 时自动产生登记相位缺陷。",
            "remaining": TYPE_UPPER_OR_DEFECT,
        },
        {
            "gate": "RepeatedTypeToStableReturnCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明重复 type key 足以保持同一素标签集 Q 并得到同 formal unit 的同标签短复现。",
            "remaining": REPEAT_TO_RETURN,
        },
        {
            "gate": "BoundaryCapTypeCompressionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "类型压缩只完成了定义与条件鸽巢骨架，核心 N/T/重复到标签 三项仍未证明。",
            "remaining": f"{FORCED_LOWER} AND {TYPE_UPPER_OR_DEFECT} AND {REPEAT_TO_RETURN}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造边界帽类型压缩路由证书。"""
    stable = load_json(MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.json")
    cycle_cut = load_json(MONOGRAPH / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json")
    extractor = load_json(MONOGRAPH / "prime-matrix-universal-formal-unit-extractor-router.json")
    partition = load_json(MONOGRAPH / "prime-matrix-formal-unit-partition-coverage-router.json")
    assignment = load_json(MONOGRAPH / "prime-matrix-source-family-assignment-totality-router.json")
    noloss = load_json(MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.json")
    hash_stability = load_json(MONOGRAPH / "prime-matrix-canonical-formal-unit-hash-stability-router.json")
    source_tuple = load_json(MONOGRAPH / "prime-matrix-concrete-source-tuple-anchor-parameter-router.json")
    anchor_recon = load_json(MONOGRAPH / "prime-matrix-anchor-set-reconstruction-certificate-router.json")
    early_zero = load_json(MONOGRAPH / "prime-matrix-early-zero-contradiction-matrix-router.json")
    phase_scan = load_json(DOCS / "phase-recurrence-pressure-scan.json")

    after = f"{FORCED_LOWER} AND {TYPE_UPPER_OR_DEFECT} AND {REPEAT_TO_RETURN}"
    rows = build_rows(
        stable=stable,
        extractor=extractor,
        partition=partition,
        assignment=assignment,
        noloss=noloss,
        hash_stability=hash_stability,
        source_tuple=source_tuple,
        anchor_recon=anchor_recon,
        early_zero=early_zero,
        phase_scan=phase_scan,
    )
    return {
        "certificate_type": "prime_matrix_strict_boundary_cap_type_compression_router",
        "status": "boundary_cap_type_compression_reduced_to_forced_count_type_bound_repeated_label_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "row_free_type_key_definition_closed": True,
        "pigeonhole_skeleton_conditional_closed": True,
        "universal_formal_unit_extractor_imported": extractor.get("universal_extractor_theorem_closed") is True,
        "no_loss_hash_stability_imported": (
            noloss.get("no_loss_return_accounting_closed") is True
            and hash_stability.get("canonical_formal_unit_hash_stability_closed") is True
        ),
        "boundary_cap_forced_obligation_lower_bound_proved": False,
        "row_free_type_upper_or_explosion_defect_proved": False,
        "repeated_type_to_stable_same_label_return_proved": False,
        "boundary_cap_formal_unit_type_compression_dichotomy_proved": False,
        "early_zero_forces_stable_short_return_or_defect_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TYPE_COMPRESSION,
        "hardpoint_after_router": after,
        "next_direct_attack_target": FORCED_LOWER,
        "parallel_attack_targets": [TYPE_UPPER_OR_DEFECT, REPEAT_TO_RETURN],
        "full_remaining_chain_after_router": (
            f"({after}) AND {LABEL_PRODUCT} AND {DRIFT_DEFECT}"
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
            "`BoundaryCapFormalUnitTypeCompressionDichotomy` 继续下钻后，真正能形成明显矛盾的统一场已经固定："
            "早期零行给出有限无漏 formal-unit obligations；把每个 obligation 投影到不含绝对行号的 boundary type。"
            "若强制实例数 `N` 大于类型数 `T`，鸽巢给出短复现；若类型数不被压缩，则类型增长必须登记为相位缺陷。"
            "当前已闭合的是 type key 定义和条件鸽巢骨架；未闭合的是 `N` 的有效下界、`T` 的上界或类型爆炸回流、"
            "以及重复 type 是否确实保持同一素标签集。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 边界帽 formal-unit 类型压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"row_free_type_key_definition_closed={fmt_bool(result['row_free_type_key_definition_closed'])}",
        f"pigeonhole_skeleton_conditional_closed={fmt_bool(result['pigeonhole_skeleton_conditional_closed'])}",
        f"boundary_cap_forced_obligation_lower_bound_proved={fmt_bool(result['boundary_cap_forced_obligation_lower_bound_proved'])}",
        f"row_free_type_upper_or_explosion_defect_proved={fmt_bool(result['row_free_type_upper_or_explosion_defect_proved'])}",
        f"repeated_type_to_stable_same_label_return_proved={fmt_bool(result['repeated_type_to_stable_same_label_return_proved'])}",
        f"boundary_cap_formal_unit_type_compression_dichotomy_proved={fmt_bool(result['boundary_cap_formal_unit_type_compression_dichotomy_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 类型压缩骨架",
        "",
        "拆分前：",
        "",
        "```text",
        result["hardpoint_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["hardpoint_after_router"],
        "```",
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
    for row in result["type_key_fields"]:
        lines.append(
            "| `{field}` | {role} |".format(
                field=table_cell(row["field"]),
                role=table_cell(row["role"]),
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
    for row in result["compression_logic_rows"]:
        lines.append(
            "| `{case}` | {meaning} | {consequence} | {remaining} |".format(
                case=table_cell(row["case"]),
                meaning=table_cell(row["meaning"]),
                consequence=table_cell(row["consequence"]),
                remaining=table_cell(row["remaining"]),
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
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行硬点：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "完整剩余链：",
            "",
            "```text",
            result["full_remaining_chain_after_router"],
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
