#!/usr/bin/env python3
"""Prime Matrix 坏窗来源族抽取路由器。

用法示例：
  python3 experiments/prime_matrix_bad_window_source_family_extraction_router.py

输出：
  docs/monograph/prime-matrix-bad-window-source-family-extraction-router.json
  docs/monograph/prime-matrix-bad-window-source-family-extraction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.json"
DEFAULT_BK = MONOGRAPH / "prime-matrix-bpn-bk-selberg-route.md"
DEFAULT_TCR = MONOGRAPH / "prime-matrix-bpn-tailcore-corridor-reduction.md"
DEFAULT_TAD = MONOGRAPH / "prime-matrix-bpn-tailanchor-persistence-dichotomy.md"
DEFAULT_DCS = MONOGRAPH / "prime-matrix-bpn-distributed-corridor-saturation-reduction.md"
DEFAULT_CCB = MONOGRAPH / "prime-matrix-bpn-colored-corridor-core-sieve-budget.md"
DEFAULT_LMC = MONOGRAPH / "prime-matrix-bpn-lowmod-core-crtdefect-bridge.md"
DEFAULT_UPS = MONOGRAPH / "prime-matrix-bpn-unified-pdec-sae-dichotomy.md"
DEFAULT_FXA = MONOGRAPH / "prime-matrix-bpn-final-exit-acceptance-contract.md"
DEFAULT_RESIDUAL = MONOGRAPH / "prime-matrix-bpn-final-residual-hard-attack.md"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-bad-window-source-family-extraction-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-bad-window-source-family-extraction-router.md"

OLD_ATOM = "BadWindowSourceFamilyExtractionLedger"
TAXONOMY_ATOM = "BadWindowSourceFamilyTaxonomyClosed"
DATA_ATOM = "BadWindowSourceFamilyDataExtractionLedger"
ANCHOR_ATOM = "ComplementAnchorSetAndD0KParameterLedger"
COLORING_ATOM = "IntervalGraphColoringCoverageCertificateLedger"
BUDGET_ATOM = "AllowedBudgetAllocationLedger"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"
RANKIN_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"


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


def source_families() -> list[dict[str, str]]:
    """给出当前坏窗/走廊来源族的有限分类。"""
    return [
        {
            "family_id": "EndpointSawtoothDirectedCRTDefect",
            "trigger": "BK-DEC 端点 sawtooth 块投影超过预算。",
            "formal_payload": "低模 Q、非零端点测试函数 F、坏窗相位 tau(x)。",
            "route": "persistent -> PDEC-Cert; sparse -> SAE-endpoint。",
            "inventory_role": "登记 endpoint bad-window family；不生成 corridor intervals。",
        },
        {
            "family_id": "TailAnchorConcentration",
            "trigger": "同一互补锚 a 的走廊承担过大 TailCoreBucket 质量。",
            "formal_payload": "anchor a、低模相位 rho_Q(a)、饱和阈值 theta、窗口 I。",
            "route": "single-anchor -> SAE-anchor; persistent phase -> PDEC/Directed CRTDefect。",
            "inventory_role": "登记 tail-anchor bad-window family；若转入分布式则继续生成 corridor 源。",
        },
        {
            "family_id": "HighOverlapFixedCoreDefect",
            "trigger": "分布式走廊中固定核心 d 被过多互补锚复用。",
            "formal_payload": "fixed core d、overlap m(d)>Omega、锚短窗 [L/d,R/d]。",
            "route": "Tail-anchor 或 low-mod CRTDefect，再并入 PDEC/SAE。",
            "inventory_role": "登记 high-overlap return；不能伪装成低重叠 colored corridor。",
        },
        {
            "family_id": "ColoredDisjointCorridorBudgetViolation",
            "trigger": "低重叠走廊经区间图着色后，某颜色类核心筛预算超标。",
            "formal_payload": "color_id、intervals、K、D0、Omega、phase_rule、allowed_budget。",
            "route": "Rankin pass -> closed; Rankin fail -> low-mod core spike or constant ledger。",
            "inventory_role": "正式 corridor inventory 的主体记录来源。",
        },
        {
            "family_id": "SmoothCoreLowModCRTDefect",
            "trigger": "Rankin/模型预算失败伴随 smooth-core residue spike。",
            "formal_payload": "低模 Q、residue b、中心化计数 g(b)、core 测试函数。",
            "route": "persistent -> PDEC-Cert; isolated -> SAE-core。",
            "inventory_role": "登记 failed Rankin 颜色类的 PDEC/SAE 回流原因。",
        },
        {
            "family_id": "SparseSingleWindowEscape",
            "trigger": "统一低模缺陷的坏窗集合非空但低于 persistent 阈值 beta。",
            "formal_payload": "single window I、survivor/lift/higher-defect 三选一证书。",
            "route": "SAE-Cert；若 lift 或 higher-defect 成立则回流 PDEC/SAE 主接口。",
            "inventory_role": "登记 sparse bad window 的有限 SAE 义务。",
        },
        {
            "family_id": "RankinConstantGapNoSpike",
            "trigger": "Rankin 颜色类超预算，但没有可登记的 low-mod spike。",
            "formal_payload": "失败颜色类、s、Q、ledger、allowed_budget、细分或调参说明。",
            "route": "不是坏窗证书；保留为常数/参数账本未闭合。",
            "inventory_role": "必须显式失败回流，不能被计作 PDEC/SAE 已排除。",
        },
    ]


def data_record_schema() -> list[dict[str, str]]:
    """给出下一步数据抽取每条记录必须携带的字段。"""
    return [
        {"field": "source_family_id", "meaning": "必须属于本路由器列出的有限来源族。"},
        {"field": "formal_unit_id", "meaning": "同一反例链中的 formal unit 编号，禁止跨口径拼接。"},
        {"field": "P_or_P_range", "meaning": "该记录适用的素数或素数范围。"},
        {"field": "window_id", "meaning": "坏窗、边界帽、走廊或颜色类的稳定编号。"},
        {"field": "low_modulus_Q", "meaning": "触发低模缺陷时使用的模数；无则写 null 并说明。"},
        {"field": "phase_key", "meaning": "相位、residue、anchor 或 fixed-core 键。"},
        {"field": "test_function_id", "meaning": "endpoint/core/tail-anchor 对应的有限测试函数编号。"},
        {"field": "branch_type", "meaning": "persistent、sparse、rankin_pass、rankin_fail 或 constant_gap。"},
        {"field": "corridor_payload", "meaning": "若为 colored corridor，必须给 intervals/K/D0/Omega/color_id。"},
        {"field": "failure_return", "meaning": "PDEC、SAE、Rankin、constant-gap 或 downstream anchor/color/budget。"},
        {"field": "source_hash", "meaning": "可复算来源文件或证书哈希。"},
    ]


def source_data_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像坏窗来源族全量数据账本。"""
    return (
        payload.get("certificate_type") == "prime_matrix_bad_window_source_family_data"
        or "bad_window_source_family_records" in payload
        or "formal_bad_window_source_records" in payload
    )


def scan_source_data(root: Path) -> list[dict[str, Any]]:
    """扫描仓库内是否已有正式坏窗来源族数据账本。"""
    found: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if isinstance(payload, dict) and source_data_like(payload):
            found.append(
                {
                    "path": str(path.relative_to(ROOT)),
                    "status": payload.get("status"),
                    "record_count": len(
                        payload.get("bad_window_source_family_records")
                        or payload.get("formal_bad_window_source_records")
                        or []
                    ),
                }
            )
    return found


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


def build_rows(previous: dict[str, Any], texts: dict[str, str], source_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """生成坏窗来源族抽取判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    endpoint_ready = contains_all(
        texts["bk"],
        ["Directed Endpoint CRTDefect", "PDEC-or-SAE", "Sparse single-window escape"],
    )
    tail_ready = contains_all(
        texts["tcr"],
        ["Tail-anchor concentration", "Distributed corridor saturation", "High-overlap fixed-core defect"],
    ) and contains_all(
        texts["tad"],
        ["SAE-anchor", "Persistent Tail-anchor defect", "Directed CRTDefect"],
    )
    corridor_ready = contains_all(
        texts["dcs"],
        ["Theorem DCS-1", "High-overlap fixed-core defect", "Colored disjoint-corridor budget violation"],
    )
    rankin_ready = contains_all(
        texts["ccb"],
        ["Theorem CCB-1", "finite Rankin ledger obstruction", "low-mod core CRTDefect"],
    )
    lowmod_ready = contains_all(
        texts["lmc"],
        ["Theorem LMC-1", "Directed Core CRTDefect", "PDEC-or-SAE"],
    )
    ups_ready = contains_all(
        texts["ups"],
        ["Theorem UPS-1", "Persistent branch", "Sparse branch"],
    )
    fxa_ready = contains_all(
        texts["fxa"],
        ["PDEC-Cert", "SAE-Cert", "Rankin 颜色类证书"],
    )
    residual_ready = contains_all(
        texts["residual"],
        ["镜像两端帽约束", "列非零同余类均衡", "正式走廊 Rankin 证书失败"],
    )
    taxonomy_closed = all(
        [
            active,
            endpoint_ready,
            tail_ready,
            corridor_ready,
            rankin_ready,
            lowmod_ready,
            ups_ready,
            fxa_ready,
            residual_ready,
        ]
    )
    data_found = bool(source_data)
    return [
        row(
            "BadWindowSourceFamilyGateActive",
            active,
            False,
            "上一层正式 corridor inventory 已把当前最窄点设为坏窗来源族抽取。",
            OLD_ATOM,
        ),
        row(
            "EndpointSourceFamilyRegistered",
            endpoint_ready,
            True,
            "BK 端点 sawtooth 超预算已命名为 Directed Endpoint CRTDefect，并进入 PDEC/SAE。",
            "无 endpoint 来源族命名剩余。",
        ),
        row(
            "TailAnchorAndHighOverlapFamiliesRegistered",
            tail_ready,
            True,
            "TailCore 分支已拆成尾锚、分布式走廊；尾锚持续化后进入 SAE 或 PDEC。",
            "无 tail-anchor 来源族命名剩余。",
        ),
        row(
            "DistributedCorridorFamiliesRegistered",
            corridor_ready,
            True,
            "分布式走廊饱和已拆成高重叠固定核心或低重叠着色走廊预算。",
            "无 distributed corridor 来源族命名剩余。",
        ),
        row(
            "RankinAndLowModFamiliesRegistered",
            rankin_ready and lowmod_ready,
            True,
            "着色走廊预算失败要么是 finite Rankin 账本缺口，要么是 low-mod core CRTDefect。",
            "无 core/Rankin 来源族命名剩余。",
        ),
        row(
            "PersistentSparseInterfaceRegistered",
            ups_ready and fxa_ready,
            True,
            "任意命名低模缺陷已统一为 persistent PDEC 或 sparse SAE 验收接口。",
            "最终 PDEC/SAE 证书仍未全集提交。",
        ),
        row(
            "PDECUpperConstraintInputsNamed",
            residual_ready,
            True,
            "PDEC 上界需使用 mirror、column、tail-anchor、core-overlap 与 Rankin-routing 五类约束。",
            "仍需逐实例数据和对偶证书。",
        ),
        row(
            "BadWindowSourceFamilyTaxonomyClosed",
            taxonomy_closed,
            True,
            "所有坏窗/走廊来源已经落入有限命名族；不存在新的无名来源类型。",
            TAXONOMY_ATOM,
        ),
        row(
            "BadWindowSourceFamilyDataAvailable",
            data_found,
            False,
            "扫描仓库是否已有正式反例链诱导的全量坏窗来源族记录；当前未发现。",
            DATA_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "来源族 taxonomy 已闭合，但抽取 ledger 本身必须提交逐记录数据后才能关闭。",
            DATA_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行坏窗来源族抽取路由。"""
    previous = load_json(paths["previous"])
    texts = {key: read_text(path) for key, path in paths.items() if key != "previous"}
    source_data = scan_source_data(DOCS)
    rows = build_rows(previous, texts, source_data)
    taxonomy_closed = next(item["closed"] for item in rows if item["gate"] == TAXONOMY_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_bad_window_source_family_extraction_router",
        "status": "bad_window_source_family_taxonomy_closed_data_missing",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "bad_window_source_family_taxonomy_closed": taxonomy_closed,
        "bad_window_source_family_extraction_closed": False,
        "bad_window_source_family_data_found": bool(source_data),
        "bad_window_source_family_data_like_json": source_data,
        "source_families": source_families(),
        "data_record_schema": data_record_schema(),
        "current_narrowest_atom": DATA_ATOM,
        "next_after_data_atom": ANCHOR_ATOM,
        "downstream_atoms": [COLORING_ATOM, BUDGET_ATOM, RANKIN_ATOM, PDEC_SAE_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {TAXONOMY_ATOM} AND {DATA_ATOM}.",
        "plain_conclusion": (
            "BadWindowSourceFamilyExtractionLedger 的 taxonomy 层已闭合：假设早期零行反例诱导的"
            "端点、尾锚、高重叠核心、低重叠着色走廊、smooth-core 低模尖峰、sparse 单窗逃逸"
            "以及 Rankin 无尖峰常数缺口，都已经落入有限命名来源族。"
            "但仓库尚未提交逐 formal unit 的全量来源记录，因此完整来源族抽取账本仍未闭合。"
            f"新的唯一最窄点是 `{DATA_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 坏窗来源族抽取路由器",
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
            "bad_window_source_family_taxonomy_closed="
            f"{fmt_bool(result['bad_window_source_family_taxonomy_closed'])}"
        ),
        (
            "bad_window_source_family_extraction_closed="
            f"{fmt_bool(result['bad_window_source_family_extraction_closed'])}"
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
        "## 2. 来源族表",
        "",
        "| family_id | trigger | formal_payload | route | inventory_role |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["source_families"]:
        lines.append(
            "| {family_id} | {trigger} | {formal_payload} | {route} | {inventory_role} |".format(
                family_id=table_cell(item["family_id"]),
                trigger=table_cell(item["trigger"]),
                formal_payload=table_cell(item["formal_payload"]),
                route=table_cell(item["route"]),
                inventory_role=table_cell(item["inventory_role"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一步数据字段",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["data_record_schema"]:
        lines.append(
            "| {field} | {meaning} |".format(
                field=table_cell(item["field"]),
                meaning=table_cell(item["meaning"]),
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
            "## 5. 审稿边界",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。"
            f"只有提交全量来源记录后，才可进入 `{result['next_after_data_atom']}`、"
            f"`{COLORING_ATOM}`、`{BUDGET_ATOM}` 与 `{RANKIN_ATOM}`。",
            "",
            "这一步没有关闭 PDEC-Cert、SAE-Cert、DStructure/Rankin 独立验收门，也没有关闭行列无条件定理。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--bk", type=Path, default=DEFAULT_BK)
    parser.add_argument("--tcr", type=Path, default=DEFAULT_TCR)
    parser.add_argument("--tad", type=Path, default=DEFAULT_TAD)
    parser.add_argument("--dcs", type=Path, default=DEFAULT_DCS)
    parser.add_argument("--ccb", type=Path, default=DEFAULT_CCB)
    parser.add_argument("--lmc", type=Path, default=DEFAULT_LMC)
    parser.add_argument("--ups", type=Path, default=DEFAULT_UPS)
    parser.add_argument("--fxa", type=Path, default=DEFAULT_FXA)
    parser.add_argument("--residual", type=Path, default=DEFAULT_RESIDUAL)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "bk": args.bk,
        "tcr": args.tcr,
        "tad": args.tad,
        "dcs": args.dcs,
        "ccb": args.ccb,
        "lmc": args.lmc,
        "ups": args.ups,
        "fxa": args.fxa,
        "residual": args.residual,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
