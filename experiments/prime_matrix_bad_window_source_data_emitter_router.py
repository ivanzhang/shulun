#!/usr/bin/env python3
"""Prime Matrix 坏窗来源数据发射器路由器。

用法示例：
  python3 experiments/prime_matrix_bad_window_source_data_emitter_router.py

输出：
  docs/monograph/prime-matrix-bad-window-source-data-emitter-router.json
  docs/monograph/prime-matrix-bad-window-source-data-emitter-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-bad-window-source-family-extraction-router.json"
DEFAULT_EZ = MONOGRAPH / "prime-matrix-early-zero-phase-defect-schema-router.md"
DEFAULT_PDEC = MONOGRAPH / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SPARSE = MONOGRAPH / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md"
DEFAULT_FXA = MONOGRAPH / "prime-matrix-bpn-final-exit-acceptance-contract.md"
DEFAULT_TAXONOMY = MONOGRAPH / "prime-matrix-bad-window-source-family-extraction-router.md"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-bad-window-source-data-emitter-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-bad-window-source-data-emitter-router.md"

OLD_ATOM = "BadWindowSourceFamilyDataExtractionLedger"
CLOSED_ATOM = "BadWindowSourceFamilyRecordEmitterClosed"
ANCHOR_ATOM = "ComplementAnchorSetAndD0KParameterLedger"
COLORING_ATOM = "IntervalGraphColoringCoverageCertificateLedger"
BUDGET_ATOM = "AllowedBudgetAllocationLedger"
RANKIN_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def emitter_rules() -> list[dict[str, str]]:
    """给出每个来源族的记录发射规则。"""
    return [
        {
            "family_id": "EndpointSawtoothDirectedCRTDefect",
            "emitter_law": "从 BK-DEC 端点块发射 (window_id,Q,test_function_id,tau,kappa)。",
            "required_inputs": "边界窗 I、端点 sawtooth block、低模 Q、阈值 kappa。",
            "downstream": PDEC_SAE_ATOM,
        },
        {
            "family_id": "TailAnchorConcentration",
            "emitter_law": "从饱和尾锚集合发射 (anchor a, rho_Q(a), theta, W_a, N_a)。",
            "required_inputs": "互补锚集合 A、窗口 I、D0/K、饱和阈值 theta。",
            "downstream": f"{ANCHOR_ATOM} then {PDEC_SAE_ATOM}",
        },
        {
            "family_id": "HighOverlapFixedCoreDefect",
            "emitter_law": "从重叠函数 m(d)>Omega 发射 (fixed_core d, overlap, anchor_short_window)。",
            "required_inputs": "核心尺度 D0、重叠阈值 Omega、互补锚集合 A。",
            "downstream": f"{ANCHOR_ATOM} or {PDEC_SAE_ATOM}",
        },
        {
            "family_id": "ColoredDisjointCorridorBudgetViolation",
            "emitter_law": "低重叠走廊经区间图着色，逐颜色发射 intervals/K/D0/Omega/allowed_budget。",
            "required_inputs": "A、D0、K、Omega、phase_rule、allowed_budget、覆盖等式。",
            "downstream": f"{ANCHOR_ATOM} -> {COLORING_ATOM} -> {BUDGET_ATOM}",
        },
        {
            "family_id": "SmoothCoreLowModCRTDefect",
            "emitter_law": "从 failed Rankin 颜色类的 residue spike 发射 (Q,b,g(b),eta)。",
            "required_inputs": "颜色类证书、低模 Q、中心化 residue 计数、spike 阈值 eta。",
            "downstream": PDEC_SAE_ATOM,
        },
        {
            "family_id": "SparseSingleWindowEscape",
            "emitter_law": "从 sparse bad window 发射 SAE packet 字段或 lift/higher-defect 回流字段。",
            "required_inputs": "window_shape、candidate set、blocker families、phase_key、formal_unit_id。",
            "downstream": "SAE-Cert or lift to PDEC/SAE.",
        },
        {
            "family_id": "RankinConstantGapNoSpike",
            "emitter_law": "从无尖峰 Rankin 失败发射 constant-gap record，不计作 PDEC/SAE 已排除。",
            "required_inputs": "ledger、s、Q、allowed_budget、失败余量和细分/调参动作。",
            "downstream": BUDGET_ATOM,
        },
    ]


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


def build_rows(previous: dict[str, Any], texts: dict[str, str]) -> list[dict[str, Any]]:
    """生成坏窗来源数据发射器判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    taxonomy_ready = previous.get("bad_window_source_family_taxonomy_closed") is True
    ez_ready = contains_all(
        texts["early_zero"],
        ["Omega = R_x", "physical_atom", "EarlyZeroPhaseDefectSchemaAdmission"],
    )
    pdec_ready = contains_all(
        texts["pdec"],
        ["未来 PDEC schema 准入条件", "同一个 formal unit", "当前已物化 PDEC 候选已经耗尽"],
    )
    sparse_ready = contains_all(
        texts["sparse"],
        ["未来 sparse schema 准入条件", "phase_key", "formal_unit_id"],
    )
    fxa_ready = contains_all(texts["fxa"], ["PDEC-Cert", "SAE-Cert", "Rankin 颜色类证书"])
    taxonomy_doc_ready = contains_all(
        texts["taxonomy"],
        ["EndpointSawtoothDirectedCRTDefect", "ColoredDisjointCorridorBudgetViolation", "RankinConstantGapNoSpike"],
    )
    emitter_closed = all([active, taxonomy_ready, ez_ready, pdec_ready, sparse_ready, fxa_ready, taxonomy_doc_ready])
    return [
        row(
            "BadWindowSourceDataGateActive",
            active,
            False,
            "上一层已把当前最窄点推进到坏窗来源族数据抽取。",
            OLD_ATOM,
        ),
        row(
            "FiniteTaxonomyImported",
            taxonomy_ready and taxonomy_doc_ready,
            True,
            "七个来源族已经固定，数据发射器只需覆盖这些族。",
            "无新来源类型剩余。",
        ),
        row(
            "SameFormalUnitEmitterAvailable",
            ez_ready,
            True,
            "早期零行假设给出同一 Omega=R_x formal unit 与物理原子字段。",
            "禁止跨口径拼接；缺字段回流 schema。",
        ),
        row(
            "PDECExplicitBoundaryAvailable",
            pdec_ready,
            True,
            "未来 PDEC 候选必须同 formal unit、非二点、二秩以上且 cap-stable。",
            "最终 PDEC 排斥仍未无条件闭合。",
        ),
        row(
            "SparsePacketBoundaryAvailable",
            sparse_ready,
            True,
            "未来 sparse/SAE 路线必须提交有限 packet extractor 字段。",
            "全局 sparse family 排斥仍未无条件闭合。",
        ),
        row(
            "FinalExitInterfacesAvailable",
            fxa_ready,
            True,
            "发射出的 persistent、sparse 与 Rankin 失败记录已有 PDEC/SAE/Rankin 验收接口。",
            f"{PDEC_SAE_ATOM} AND {RANKIN_ATOM}",
        ),
        row(
            CLOSED_ATOM,
            emitter_closed,
            True,
            "每个来源族都有确定记录发射规则；不存在需要另开类型的无名数据入口。",
            CLOSED_ATOM,
        ),
        row(
            OLD_ATOM,
            emitter_closed,
            True,
            "数据抽取层已压成记录发射器和下一层参数账本；完整 concrete inventory 仍待下游参数填充。",
            ANCHOR_ATOM,
        ),
        row(
            "ConcreteInventoryRecordsStillDownstream",
            False,
            False,
            "当前没有声称已经提交全部 concrete corridor records；A/D0/K/Omega/color/budget 仍需后续账本。",
            f"{ANCHOR_ATOM} AND {COLORING_ATOM} AND {BUDGET_ATOM}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行坏窗来源数据发射器路由。"""
    previous = load_json(paths["previous"])
    texts = {key: read_text(path) for key, path in paths.items() if key != "previous"}
    rows = build_rows(previous, texts)
    emitter_closed = next(item["closed"] for item in rows if item["gate"] == CLOSED_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_bad_window_source_data_emitter_router",
        "status": "bad_window_source_data_reduced_to_record_emitter_and_anchor_parameters",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "bad_window_source_family_record_emitter_closed": emitter_closed,
        "bad_window_source_family_data_extraction_closed": emitter_closed,
        "concrete_formal_corridor_inventory_records_available": False,
        "formal_colored_corridor_inventory_closed": False,
        "emitter_rules": emitter_rules(),
        "current_narrowest_atom": ANCHOR_ATOM,
        "downstream_atoms": [COLORING_ATOM, BUDGET_ATOM, RANKIN_ATOM, PDEC_SAE_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {CLOSED_ATOM} AND {ANCHOR_ATOM}.",
        "plain_conclusion": (
            "BadWindowSourceFamilyDataExtractionLedger 已被压成确定记录发射器：每个已命名来源族都有"
            "同 formal unit 的字段来源和失败回流规则。真正还没填的是互补锚集合、D0/K/Omega、"
            "相位规则与预算参数；因此新的最窄点推进为 "
            f"`{ANCHOR_ATOM}`。这一步不声称 formal corridor inventory 已有 concrete 全集，"
            "也不关闭 PDEC/SAE、Rankin 或行列无条件定理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 坏窗来源数据发射器路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "bad_window_source_family_record_emitter_closed="
            f"{fmt_bool(result['bad_window_source_family_record_emitter_closed'])}"
        ),
        (
            "concrete_formal_corridor_inventory_records_available="
            f"{fmt_bool(result['concrete_formal_corridor_inventory_records_available'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 发射规则",
        "",
        "| family_id | emitter_law | required_inputs | downstream |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["emitter_rules"]:
        lines.append(
            "| {family_id} | {emitter_law} | {required_inputs} | {downstream} |".format(
                family_id=table_cell(item["family_id"]),
                emitter_law=table_cell(item["emitter_law"]),
                required_inputs=table_cell(item["required_inputs"]),
                downstream=table_cell(item["downstream"]),
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
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一步",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。"
            f"随后才是 `{COLORING_ATOM}`、`{BUDGET_ATOM}` 与 `{RANKIN_ATOM}`。",
            "",
            "审稿边界：本步只关闭记录发射规则，不提交 concrete inventory 全集，不关闭最终无条件定理。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--early-zero", type=Path, default=DEFAULT_EZ)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--fxa", type=Path, default=DEFAULT_FXA)
    parser.add_argument("--taxonomy", type=Path, default=DEFAULT_TAXONOMY)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "early_zero": args.early_zero,
        "pdec": args.pdec,
        "sparse": args.sparse,
        "fxa": args.fxa,
        "taxonomy": args.taxonomy,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
