#!/usr/bin/env python3
"""生成 strict 稳定短复现/相位缺陷硬点拆分证书。

用法示例：
  python3 experiments/prime_matrix_strict_stable_short_return_defect_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-stable-short-return-defect-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    MONOGRAPH / "prime-matrix-early-zero-contradiction-matrix-router.json",
    MONOGRAPH / "prime-matrix-formal-unit-source-record-router.json",
    MONOGRAPH / "prime-matrix-canonical-formal-unit-hash-stability-router.json",
    MONOGRAPH / "prime-matrix-zero-row-delay-recursive-lemma.md",
    DOCS / "phase-recurrence-pressure-scan.json",
]

TYPE_COMPRESSION = "BoundaryCapFormalUnitTypeCompressionDichotomy"
LABEL_PRODUCT = "StableReturnLargeLabelSupportProductLowerBound"
DRIFT_DEFECT = "SignatureDriftToRegisteredPhaseDefectTheorem"
SHORT_RETURN = "StableShortSameLabelRecurrenceOrRegisteredPhaseDefect"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    """读取文本；缺失时返回空字符串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def subatom_rows(
    cycle_cut: dict[str, Any],
    early_zero: dict[str, Any],
    formal_record: dict[str, Any],
    hash_stability: dict[str, Any],
    delay_text: str,
    phase_scan: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成短复现硬点拆分判定表。"""
    boundary_equiv = "边界 `2p` 短复现禁止" in delay_text and "同强" in delay_text
    phase_scan_imported = (
        phase_scan.get("status")
        == "label_modulus_product_exceeds_P_but_short_recurrence_not_full_in_samples"
    )
    return [
        {
            "gate": "ShortReturnHardpointActive",
            "closed": cycle_cut.get("preferred_next_direct_attack_target") == SHORT_RETURN,
            "proved": False,
            "meaning": "上一层把直接矛盾首选点压成同 formal unit 短稳定复现或登记相位缺陷。",
            "remaining": SHORT_RETURN,
        },
        {
            "gate": "CRTPayloadContradictionImported",
            "closed": cycle_cut.get("short_same_label_recurrence_contradiction_lemma_proved") is True,
            "proved": True,
            "meaning": "若同标签稳定复现保留素标签集 Q，则 prod(Q)|Delta；短于 prod(Q) 即矛盾。",
            "remaining": "要证明的是短复现或相位缺陷的产生机制。",
        },
        {
            "gate": "Boundary2PRecurrenceNotIndependentExit",
            "closed": boundary_equiv,
            "proved": True,
            "meaning": "边界 2P 短复现禁止与首零行超过 P 同强，不能作为独立证明出口。",
            "remaining": "必须改攻边界帽 formal-unit 类型压缩或相位非覆盖。",
        },
        {
            "gate": "EarlyZeroNamedContradictionMatrixImported",
            "closed": early_zero.get("no_unnamed_exit_for_early_zero") is True,
            "proved": True,
            "meaning": "早期零行已进入 CLB、formal unit、carry-shell、anchor-collar、PDEC/SAE/ColumnCRT 命名矩阵。",
            "remaining": early_zero.get("strongest_current_frontier", "named terminal capacity"),
        },
        {
            "gate": "FormalUnitRecordsAvailableButNotCompressed",
            "closed": formal_record.get("concrete_formal_unit_source_record_closed") is True
            and hash_stability.get("canonical_formal_unit_hash_stability_closed") is True,
            "proved": True,
            "meaning": "任意假设 witness 可抽取稳定 formal unit 记录，且哈希命名稳定。",
            "remaining": "尚未证明边界帽内 formal unit 类型数小于强制实例数。",
        },
        {
            "gate": "PhaseRecurrenceScanImportedAsDiagnosticOnly",
            "closed": phase_scan_imported,
            "proved": True,
            "meaning": "诊断显示大标签乘积超过 P 的后半段压力强；但自然短步长不自动给全覆盖复现。",
            "remaining": "不能用实验样本替代类型压缩证明。",
        },
        {
            "gate": "TypeCompressionDichotomyCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明边界帽中 forced formal units 的规范类型数足够小，从而鸽巢得到同 formal unit 短复现。",
            "remaining": TYPE_COMPRESSION,
        },
        {
            "gate": "StableReturnLargeLabelProductCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "即便得到稳定复现，还需证明被保持的标签集 Q 的乘积超过位移上界。",
            "remaining": LABEL_PRODUCT,
        },
        {
            "gate": "SignatureDriftToDefectCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "若类型不复现或标签漂移，尚未证明漂移必产生已登记 PDEC/SAE/ColumnCRT 相位缺陷。",
            "remaining": DRIFT_DEFECT,
        },
        {
            "gate": "StableShortReturnOrDefectCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "短复现硬点已拆成类型压缩、标签乘积下界、漂移缺陷三原子；三者尚未合取证明。",
            "remaining": f"{TYPE_COMPRESSION} AND {LABEL_PRODUCT} AND {DRIFT_DEFECT}",
        },
    ]


def attack_plan() -> list[dict[str, str]]:
    """给出下一步证明计划，保持同一命题不转换。"""
    return [
        {
            "step": TYPE_COMPRESSION,
            "content": "在边界帽内固定 source_family、phase_key、anchor/carry-shell 字段，证明规范类型数小于被迫覆盖实例数；否则超类型增长必须登记为新 layer/phase defect。",
        },
        {
            "step": LABEL_PRODUCT,
            "content": "对重复的同 formal unit，提取保持的高标签子集 Q；用覆盖无漏和短纤维容量证明 prod(Q) 超过允许位移上界。",
        },
        {
            "step": DRIFT_DEFECT,
            "content": "若不能保持 Q，则记录标签替换、列位移或相位键变化；证明其给出 PDEC/SAE/ColumnCRT 的显式坏窗集合与同账本权重。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造稳定短复现硬点拆分证书。"""
    cycle_cut = load_json(MONOGRAPH / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json")
    early_zero = load_json(MONOGRAPH / "prime-matrix-early-zero-contradiction-matrix-router.json")
    formal_record = load_json(MONOGRAPH / "prime-matrix-formal-unit-source-record-router.json")
    hash_stability = load_json(MONOGRAPH / "prime-matrix-canonical-formal-unit-hash-stability-router.json")
    delay_text = load_text(MONOGRAPH / "prime-matrix-zero-row-delay-recursive-lemma.md")
    phase_scan = load_json(DOCS / "phase-recurrence-pressure-scan.json")

    rows = subatom_rows(
        cycle_cut=cycle_cut,
        early_zero=early_zero,
        formal_record=formal_record,
        hash_stability=hash_stability,
        delay_text=delay_text,
        phase_scan=phase_scan,
    )
    after = f"{TYPE_COMPRESSION} AND {LABEL_PRODUCT} AND {DRIFT_DEFECT}"
    return {
        "certificate_type": "prime_matrix_strict_stable_short_return_defect_attack_router",
        "status": "stable_short_return_or_phase_defect_reduced_to_type_compression_label_product_drift_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "crt_short_recurrence_contradiction_imported": True,
        "boundary_2p_recurrence_not_independent_exit": True,
        "formal_unit_hash_stability_imported": True,
        "type_compression_dichotomy_proved": False,
        "stable_return_large_label_product_proved": False,
        "signature_drift_to_registered_phase_defect_proved": False,
        "early_zero_forces_stable_short_return_or_defect_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": SHORT_RETURN,
        "hardpoint_after_router": after,
        "next_direct_attack_target": TYPE_COMPRESSION,
        "backup_parallel_attack_targets": [LABEL_PRODUCT, DRIFT_DEFECT],
        "nonclosing_reason": (
            "CRT 短复现矛盾的后半段已清楚；缺的是上游强制机制。"
            "若只说边界 2P 短复现，命题与首零行 >P 同强；若只引用实验，不能替代正式证明。"
        ),
        "rows": rows,
        "attack_plan": attack_plan(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`StableShortSameLabelRecurrenceOrRegisteredPhaseDefect` 被继续拆开："
            "短稳定同标签复现一旦成立就由 CRT 立刻矛盾，这部分已经不是硬点。"
            "真正硬点是证明早期零行强制产生这种复现；形式上需要边界帽 formal-unit 类型压缩、"
            "稳定复现保留标签集的乘积下界，以及不复现/漂移时进入已登记相位缺陷。"
            "这三项均未由当前语料证明，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 稳定短复现/相位缺陷硬点拆分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"crt_short_recurrence_contradiction_imported={fmt_bool(result['crt_short_recurrence_contradiction_imported'])}",
        f"boundary_2p_recurrence_not_independent_exit={fmt_bool(result['boundary_2p_recurrence_not_independent_exit'])}",
        f"type_compression_dichotomy_proved={fmt_bool(result['type_compression_dichotomy_proved'])}",
        f"stable_return_large_label_product_proved={fmt_bool(result['stable_return_large_label_product_proved'])}",
        f"signature_drift_to_registered_phase_defect_proved={fmt_bool(result['signature_drift_to_registered_phase_defect_proved'])}",
        f"early_zero_forces_stable_short_return_or_defect_proved={fmt_bool(result['early_zero_forces_stable_short_return_or_defect_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 硬点拆分",
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
        result["nonclosing_reason"],
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 下一步证明计划",
            "",
            "| step | content |",
            "| --- | --- |",
        ]
    )
    for row in result["attack_plan"]:
        lines.append(
            "| `{step}` | {content} |".format(
                step=table_cell(row["step"]),
                content=table_cell(row["content"]),
            )
        )

    lines.extend(
        [
            "",
            "首要硬攻点：",
            "",
            "```text",
            result["next_direct_attack_target"],
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
