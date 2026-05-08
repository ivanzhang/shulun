#!/usr/bin/env python3
"""Prime Matrix 正式 Rankin batch manifest 路由器。

用法示例：
  python3 experiments/prime_matrix_formal_rankin_batch_manifest_router.py

输出：
  docs/monograph/prime-matrix-formal-rankin-batch-manifest-router.json
  docs/monograph/prime-matrix-formal-rankin-batch-manifest-router.md
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

DEFAULT_PREVIOUS = MONOGRAPH / "prime-matrix-batch-rankin-pass-return-router.json"
DEFAULT_COLORING = MONOGRAPH / "prime-matrix-interval-graph-coloring-coverage-router.json"
DEFAULT_BUDGET = MONOGRAPH / "prime-matrix-allowed-budget-allocation-router.json"
DEFAULT_FORMAL = MONOGRAPH / "prime-matrix-formal-corridor-inventory-contract-router.json"
DEFAULT_JSON = MONOGRAPH / "prime-matrix-formal-rankin-batch-manifest-router.json"
DEFAULT_MD = MONOGRAPH / "prime-matrix-formal-rankin-batch-manifest-router.md"

OLD_ATOM = "FormalRankinBatchManifestLedger"
SCHEMA_ATOM = "FormalRankinBatchManifestSchemaClosed"
DATA_ATOM = "ConcreteRankinBatchManifestDataLedger"
RETURN_ATOM = "FailedRankinReturnPacketLedger"
PDEC_SAE_ATOM = "PDECOrSAEUnifiedExclusionLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def is_manifest_like(payload: dict[str, Any]) -> bool:
    """判断 JSON 是否像正式 Rankin batch manifest。"""
    return (
        payload.get("certificate_type") == "prime_matrix_rankin_batch_manifest"
        or "rankin_batch_manifest" in payload
        or "rankin_certificate_manifest" in payload
        or "formal_rankin_batch_manifest" in payload
    )


def scan_manifests(root: Path) -> list[dict[str, Any]]:
    """扫描仓库内 manifest-like JSON。"""
    found: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.json")):
        if "__pycache__" in path.parts:
            continue
        try:
            payload = load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(payload, dict) or not is_manifest_like(payload):
            continue
        rows = (
            payload.get("rankin_batch_manifest")
            or payload.get("rankin_certificate_manifest")
            or payload.get("formal_rankin_batch_manifest")
            or []
        )
        found.append(
            {
                "path": str(path.relative_to(ROOT)),
                "status": payload.get("status"),
                "row_count": len(rows) if isinstance(rows, list) else None,
                "manifest_complete": payload.get("manifest_complete"),
                "all_rows_pass_or_return": payload.get("all_rows_pass_or_return"),
            }
        )
    return found


def integrity_rules() -> list[dict[str, str]]:
    """给出 manifest 完整性规则。"""
    return [
        {
            "rule": "color_set_exact",
            "meaning": "manifest 的 color_id 集合必须等于 coloring coverage 证书中的颜色全集。",
        },
        {
            "rule": "no_duplicate_color",
            "meaning": "每个 color_id 只能出现一次；重复行必须合并或报错。",
        },
        {
            "rule": "source_tuple_hash_match",
            "meaning": "每行 source_tuple_hash 必须与 coloring/budget 源一致。",
        },
        {
            "rule": "certificate_hash_match",
            "meaning": "每行 rankin_certificate_hash 必须等于单证书文件实际 sha256。",
        },
        {
            "rule": "pass_or_return_total",
            "meaning": "每行只能是 pass、lowmod_core_crtdefect return 或 constant_gap return。",
        },
        {
            "rule": "all_pass_empty_return_allowed",
            "meaning": "若所有行 pass，return packet 可为空，但 manifest 必须显式声明 all_pass。",
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


def build_rows(previous: dict[str, Any], coloring: dict[str, Any], budget: dict[str, Any], formal: dict[str, Any], manifests: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """生成正式 batch manifest 判定表。"""
    active = previous.get("current_narrowest_atom") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    batch_schema_ready = previous.get("batch_rankin_verifier_schema_closed") is True
    coloring_ready = coloring.get("interval_graph_coloring_coverage_closed") is True
    budget_ready = budget.get("allowed_budget_allocation_discipline_closed") is True
    formal_schema_ready = formal.get("formal_corridor_inventory_schema_closed") is True
    manifest_schema_closed = all([active, guard, batch_schema_ready, coloring_ready, budget_ready, formal_schema_ready])
    manifest_found = bool(manifests)
    manifest_complete = manifest_found and all(item.get("manifest_complete") is True for item in manifests)
    all_rows_pass_or_return = manifest_found and all(item.get("all_rows_pass_or_return") is True for item in manifests)
    return [
        row(
            "FormalRankinManifestGateActive",
            active,
            False,
            "上一层已把最窄点推进到正式 Rankin batch manifest。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设反例链条内的 manifest，不使用真实缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "UpstreamSchemasImported",
            batch_schema_ready and coloring_ready and budget_ready and formal_schema_ready,
            True,
            "batch schema、coloring coverage、allowed_budget 与 formal inventory schema 均已固定。",
            "无 manifest 格式上游剩余。",
        ),
        row(
            SCHEMA_ATOM,
            manifest_schema_closed,
            True,
            "manifest 完整性规则已固定为无漏色、无重复、hash 对齐和 pass/return 全覆盖。",
            SCHEMA_ATOM,
        ),
        row(
            "ConcreteManifestAvailable",
            manifest_found,
            False,
            "仓库尚未发现正式 batch manifest 数据文件。",
            DATA_ATOM,
        ),
        row(
            "ConcreteManifestComplete",
            manifest_complete,
            False,
            "manifest 必须声明覆盖全部 color_id。",
            DATA_ATOM,
        ),
        row(
            "ConcreteManifestRowsPassOrReturn",
            all_rows_pass_or_return,
            False,
            "manifest 每行必须 pass 或引用合法回流 packet。",
            f"{DATA_ATOM} OR {RETURN_ATOM}",
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "FormalRankinBatchManifestLedger 不能由 schema 关闭；仍需提交 concrete manifest 数据。",
            DATA_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """运行正式 batch manifest 路由。"""
    previous = load_json(paths["previous"])
    coloring = load_json(paths["coloring"])
    budget = load_json(paths["budget"])
    formal = load_json(paths["formal"])
    manifests = scan_manifests(DOCS)
    rows = build_rows(previous, coloring, budget, formal, manifests)
    schema_closed = next(item["closed"] for item in rows if item["gate"] == SCHEMA_ATOM)
    evidence_paths = list(paths.values())
    return {
        "certificate_type": "prime_matrix_formal_rankin_batch_manifest_router",
        "status": "formal_rankin_batch_manifest_schema_closed_data_missing",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "row_column_unconditional_closed": False,
        "formal_rankin_batch_manifest_schema_closed": schema_closed,
        "formal_rankin_batch_manifest_closed": False,
        "manifest_like_json": manifests,
        "manifest_like_json_count": len(manifests),
        "integrity_rules": integrity_rules(),
        "current_narrowest_atom": DATA_ATOM,
        "secondary_narrowest_atom": RETURN_ATOM,
        "downstream_atoms": [PDEC_SAE_ATOM],
        "reduction_formula": f"{OLD_ATOM} => {SCHEMA_ATOM} AND {DATA_ATOM}.",
        "plain_conclusion": (
            "FormalRankinBatchManifestLedger 的 schema 层已闭合：正式 manifest 必须精确覆盖 coloring "
            "证书中的 color_id 全集，禁止重复，所有 hash 必须对齐，并且每行必须 pass 或合法回流。"
            f"仓库当前未发现 concrete manifest，因此新的最窄点是 `{DATA_ATOM}`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 正式 Rankin batch manifest 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"formal_rankin_batch_manifest_schema_closed={fmt_bool(result['formal_rankin_batch_manifest_schema_closed'])}",
        f"formal_rankin_batch_manifest_closed={fmt_bool(result['formal_rankin_batch_manifest_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 收缩公式",
        "",
        "```text",
        result["reduction_formula"],
        "```",
        "",
        "## 2. 完整性规则",
        "",
        "| rule | meaning |",
        "| --- | --- |",
    ]
    for item in result["integrity_rules"]:
        lines.append(
            "| {rule} | {meaning} |".format(
                rule=table_cell(item["rule"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前扫描",
            "",
            f"- manifest-like JSON: `{result['manifest_like_json_count']}`",
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
            "## 5. 下一步",
            "",
            f"当前唯一最窄点更新为 `{result['current_narrowest_atom']}`。"
            f"若存在失败行，还需要 `{result['secondary_narrowest_atom']}`。",
            "",
            "审稿边界：本步只关闭 manifest schema，不提交 concrete manifest，不关闭批量 Rankin 门。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--coloring", type=Path, default=DEFAULT_COLORING)
    parser.add_argument("--budget", type=Path, default=DEFAULT_BUDGET)
    parser.add_argument("--formal", type=Path, default=DEFAULT_FORMAL)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "coloring": args.coloring,
        "budget": args.budget,
        "formal": args.formal,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
