#!/usr/bin/env python3
"""Prime Matrix 正式着色走廊全集清单合约路由器。

用法示例：
  python3 experiments/prime_matrix_formal_corridor_inventory_contract_router.py

输出：
  docs/monograph/prime-matrix-formal-corridor-inventory-contract-router.json
  docs/monograph/prime-matrix-formal-corridor-inventory-contract-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-full-rankin-ledger-inventory-router.json"
DEFAULT_DCS = MONOGRAPH / "prime-matrix-bpn-distributed-corridor-saturation-reduction.md"
DEFAULT_CCB = MONOGRAPH / "prime-matrix-bpn-colored-corridor-core-sieve-budget.md"
DEFAULT_FXA = MONOGRAPH / "prime-matrix-bpn-final-exit-acceptance-contract.md"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.md"

OLD_ATOM = "FormalColoredCorridorInventoryLedger"
SCHEMA_ATOM = "FormalColoredCorridorInventorySchemaClosed"
SOURCE_ATOM = "BadWindowSourceFamilyExtractionLedger"
ANCHOR_ATOM = "ComplementAnchorSetAndD0KParameterLedger"
COLORING_ATOM = "IntervalGraphColoringCoverageCertificateLedger"
BUDGET_ATOM = "AllowedBudgetAllocationLedger"
BATCH_ATOM = "BatchRankinCertificatesAllPassOrReturnToPDECSAE"
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


def inventory_schema_fields() -> list[dict[str, str]]:
    """给出正式清单每条记录的必要字段。"""
    return [
        {"field": "family_id", "meaning": "坏窗族或分支家族的稳定编号。"},
        {"field": "color_id", "meaning": "区间图着色后的颜色编号。"},
        {"field": "P_or_P_range", "meaning": "该证书覆盖的素数或素数范围。"},
        {"field": "K", "meaning": "smooth squarefree core 的 omega 截断。"},
        {"field": "D0", "meaning": "核心尺度，所有 d 走廊落在 [D0,2D0)。"},
        {"field": "Omega", "meaning": "低重叠阈值；高重叠分支必须回流 PDEC/SAE。"},
        {"field": "anchor_set_hash", "meaning": "互补锚集合 A 的可复算来源哈希。"},
        {"field": "intervals", "meaning": "同色两两不交的 [A_j,B_j] 整数走廊。"},
        {"field": "phase_moduli", "meaning": "低模相位检查模数，例如 30、210 或正式指定模数。"},
        {"field": "phase_rule", "meaning": "sigma_K(d) 中 phase(d) 的有限判定规则。"},
        {"field": "allowed_budget", "meaning": "该颜色类可用预算，供 Rankin 证书验收。"},
        {"field": "coverage_equation", "meaning": "证明这些 intervals 正好覆盖该颜色类低重叠走廊。"},
        {"field": "failure_return", "meaning": "Rankin 失败时回流 PDEC/SAE 或常数调参的路径。"},
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


def build_rows(previous: dict[str, Any], dcs: str, ccb: str, fxa: str) -> list[dict[str, Any]]:
    """生成正式着色走廊全集清单合约判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    dcs_ready = contains_all(
        dcs,
        [
            "Theorem DCS-1",
            "整数区间图是完美图",
            "不相交走廊",
            "High-overlap fixed-core defect",
        ],
    )
    ccb_ready = contains_all(
        ccb,
        ["Theorem CCB-1", "finite Rankin", "low-mod core CRTDefect"],
    )
    fxa_ready = contains_all(
        fxa,
        ["Theorem FXA-3", "所有正式着色走廊 Rankin 证书通过", "PDEC/SAE"],
    )
    schema_closed = active and dcs_ready and ccb_ready and fxa_ready
    inventory_data_present = previous.get("formal_colored_corridor_inventory_found") is True
    return [
        row(
            "FormalInventoryGateActive",
            active,
            False,
            "上一层唯一最窄点是正式着色走廊全集清单。",
            OLD_ATOM,
        ),
        row(
            "DistributedCorridorSourceLawAvailable",
            dcs_ready,
            True,
            "DCS-1 已把分布式走廊饱和拆成高重叠缺陷或低重叠着色走廊。",
            "无结构二分剩余。",
        ),
        row(
            "ColoredCorridorRankinLawAvailable",
            ccb_ready,
            True,
            "CCB-1 已把每个颜色类预算写成 finite Rankin 或 low-mod core CRTDefect。",
            "无 Rankin 逻辑格式剩余。",
        ),
        row(
            "FinalExitContractAvailable",
            fxa_ready,
            True,
            "FXA-3 已规定 Rankin 失败必须回流 PDEC/SAE 或保留常数缺口。",
            PDEC_SAE_ATOM,
        ),
        row(
            "InventorySchemaClosed",
            schema_closed,
            True,
            "正式清单字段、覆盖等式和失败回流字段已经足以定义可审稿 inventory。",
            SCHEMA_ATOM,
        ),
        row(
            "InventoryDataStillMissing",
            inventory_data_present,
            False,
            "清单 schema 已闭合，但仓库仍没有正式反例链诱导出的全量 corridor records。",
            SOURCE_ATOM,
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "FormalColoredCorridorInventoryLedger 不能由 schema 单独关闭；仍需提交全量数据和来源证明。",
            f"{SOURCE_ATOM} AND {ANCHOR_ATOM} AND {COLORING_ATOM} AND {BUDGET_ATOM}",
        ),
        row(
            "BatchRankinStillDownstream",
            False,
            False,
            "inventory 数据齐备后，才可逐条执行 Rankin 审计并处理失败回流。",
            BATCH_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行正式着色走廊全集清单合约路由。"""
    previous = load_json(paths["previous"])
    dcs = read_text(paths["dcs"])
    ccb = read_text(paths["ccb"])
    fxa = read_text(paths["fxa"])
    rows = build_rows(previous, dcs, ccb, fxa)
    schema_closed = next(item["closed"] for item in rows if item["gate"] == "InventorySchemaClosed")
    evidence_paths = [paths["previous"], paths["dcs"], paths["ccb"], paths["fxa"]]
    return {
        "certificate_type": "prime_matrix_formal_corridor_inventory_contract_router",
        "status": "formal_corridor_inventory_schema_closed_data_missing",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "formal_corridor_inventory_schema_closed": schema_closed,
        "formal_colored_corridor_inventory_closed": False,
        "inventory_schema_fields": inventory_schema_fields(),
        "current_narrowest_atom": SOURCE_ATOM,
        "secondary_narrowest_atom": ANCHOR_ATOM,
        "tertiary_narrowest_atom": COLORING_ATOM,
        "quaternary_narrowest_atom": BUDGET_ATOM,
        "downstream_atom": BATCH_ATOM,
        "reduction_formula": (
            f"{OLD_ATOM} => {SCHEMA_ATOM} AND {SOURCE_ATOM} AND {ANCHOR_ATOM} "
            f"AND {COLORING_ATOM} AND {BUDGET_ATOM}."
        ),
        "plain_conclusion": (
            "FormalColoredCorridorInventoryLedger 的 schema 层已闭合：清单必须逐条给出坏窗族、"
            "互补锚、D0/K/Omega、同色不相交 intervals、相位规则、预算和覆盖等式。"
            "但全量 corridor records 尚未提交，因此正式 inventory 本身仍未闭合。"
            "新的最窄输入是从反例链抽取全部坏窗族与走廊来源的 "
            "`BadWindowSourceFamilyExtractionLedger`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 正式着色走廊全集清单合约路由器",
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
            "formal_corridor_inventory_schema_closed="
            f"{fmt_bool(result['formal_corridor_inventory_schema_closed'])}"
        ),
        (
            "formal_colored_corridor_inventory_closed="
            f"{fmt_bool(result['formal_colored_corridor_inventory_closed'])}"
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
        "## 2. 必要字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in result["inventory_schema_fields"]:
        lines.append(
            "| {field} | {meaning} |".format(
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
            f"随后依次是 `{result['secondary_narrowest_atom']}`、"
            f"`{result['tertiary_narrowest_atom']}`、`{result['quaternary_narrowest_atom']}`；"
            f"再之后才进入 `{result['downstream_atom']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--dcs", type=Path, default=DEFAULT_DCS)
    parser.add_argument("--ccb", type=Path, default=DEFAULT_CCB)
    parser.add_argument("--fxa", type=Path, default=DEFAULT_FXA)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "dcs": args.dcs,
        "ccb": args.ccb,
        "fxa": args.fxa,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
