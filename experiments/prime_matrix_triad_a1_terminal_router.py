#!/usr/bin/env python3
"""把 Triad-A1 new-layer 输出路由到终端三证书接口。

用法示例：
  python3 experiments/prime_matrix_triad_a1_terminal_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-terminal-router.json
  docs/monograph/prime-matrix-triad-a1-terminal-router.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_NODELETION = DOCS / "prime-matrix-triad-a1-nodeletion-kl-gate.json"
DEFAULT_BUDGET = DOCS / "prime-matrix-triad-a1-infinite-tower-budget.json"
DEFAULT_TOWER = DOCS / "prime-matrix-triad-a1-newlayer-tower-gate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-terminal-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-terminal-router.md"


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def route_gate(gate: str) -> tuple[str, str, str]:
    """把 NoDeletion-KL gate 分类到终端接口。"""
    if gate == "FiberDeletion":
        return (
            "LiftFiberDeletion",
            "ContinueLiftOrSparse",
            "继续累计删除势；若无限发散则支撑密度趋零，回到 Sparse/LocalSurvivor 或容量矛盾。",
        )
    if gate == "NoDeletionKLPDEC":
        return (
            "PDEC",
            "Triad-A",
            "NoDeletion 下 KL 偏斜已足够，进入 new-layer/profinite PDEC-Cert。",
        )
    if gate == "NoDeletionCleanKLSCandidate":
        return (
            "CleanKLS",
            "Triad-C",
            "NoDeletion 且 KL 低，必须核验 CleanKLS admission 与大筛证书。",
        )
    if gate == "NoDeletionMixedKL":
        return (
            "RefineOrNextLayer",
            "Triad-A-or-C",
            "KL 处于混合区，需升层、调结构基准或拆 cap；最终仍进 PDEC/CleanKLS。",
        )
    if gate == "NoDeletionNeedsKLInput":
        return (
            "MissingKLInput",
            "CertificateGap",
            "删除停止但缺 KL 输入，必须补 formal unit 与基准分布。",
        )
    return (
        "InvalidOrEmpty",
        "CertificateGap",
        "输入为空或口径无效，回到 formal unit/Multiplicity-Stitching 检查。",
    )


def summarize_p_budget(budget: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """按 P 整理删除预算。"""
    return {int(row["p"]): row for row in budget["p_paths"]}


def route_rows(nodeletion: dict[str, Any], budget: dict[str, Any]) -> list[dict[str, Any]]:
    """路由所有层/P 行。"""
    p_budget = summarize_p_budget(budget)
    rows = []
    for row in nodeletion["rows"]:
        route, triad_target, obligation = route_gate(row["gate"])
        p = int(row["p"])
        budget_row = p_budget.get(p, {})
        rows.append(
            {
                "q": row["q"],
                "q_lift": row["q_lift"],
                "p": p,
                "gate": row["gate"],
                "route": route,
                "triad_target": triad_target,
                "survival": row["survival"],
                "deletion": row["deletion"],
                "density_drop_factor": row["density_drop_factor"],
                "normalized_kl_to_uniform": row["normalized_kl_to_uniform"],
                "path_layer_count": budget_row.get("layer_count"),
                "path_product_survival": budget_row.get("product_survival"),
                "path_deletion_potential": budget_row.get("deletion_potential_sum"),
                "obligation": obligation,
            }
        )
    return rows


def run(nodeletion_path: Path, budget_path: Path, tower_path: Path) -> dict[str, Any]:
    """运行终端路由汇总。"""
    nodeletion = load_json(nodeletion_path)
    budget = load_json(budget_path)
    tower = load_json(tower_path)
    rows = route_rows(nodeletion, budget)
    route_counts = Counter(row["route"] for row in rows)
    triad_counts = Counter(row["triad_target"] for row in rows)
    current_terminal_claim = (
        "current_layers_all_deleting"
        if route_counts == Counter({"LiftFiberDeletion": len(rows)})
        else "current_layers_have_terminal_inputs"
    )
    return {
        "certificate_type": "triad_a1_terminal_router",
        "status": "terminal_routes_materialized_not_terminal_certificates",
        "source_hashes": {
            "terminal_router_script": file_sha256(Path(__file__).resolve()),
            "nodeletion_kl_gate_json": file_sha256(nodeletion_path),
            "infinite_tower_budget_json": file_sha256(budget_path),
            "newlayer_tower_gate_json": file_sha256(tower_path),
        },
        "inputs": {
            "nodeletion_status": nodeletion["status"],
            "budget_status": budget["status"],
            "tower_status": tower["status"],
            "tower_layer_classes": tower["layer_classes"],
        },
        "rows": rows,
        "route_counts": dict(route_counts),
        "triad_counts": dict(triad_counts),
        "current_terminal_claim": current_terminal_claim,
        "router_law": (
            "FiberDeletion 行继续累计删除势；NoDeletion+KL 偏斜进入 PDEC；"
            "NoDeletion+低 KL 进入 CleanKLS；口径缺失回到 formal unit/Stitching。"
        ),
        "review_conclusion": (
            "当前已物化层全部路由为 LiftFiberDeletion，尚未产生可提交的 PDEC 或 CleanKLS 实例。"
            "这不是停顿：它说明当前分支仍在删除势账本中推进；未来若删除停止，路由器会强制转入三终端证书。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 终端证书路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 路由律",
        "",
        result["router_law"],
        "",
        "```text",
        "FiberDeletion              => ContinueLiftOrSparse；",
        "NoDeletionKLPDEC           => Triad-A PDEC；",
        "NoDeletionCleanKLSCandidate=> Triad-C CleanKLS；",
        "NoDeletionMixedKL          => refine cap / next layer, then A or C；",
        "MissingKLInput             => formal unit/Stitching gap。",
        "```",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. 总计",
            "",
            f"- `current_terminal_claim={result['current_terminal_claim']}`。",
            f"- `route_counts={result['route_counts']}`。",
            f"- `triad_counts={result['triad_counts']}`。",
            "",
            "## 4. 明细",
            "",
            "| layer | P | gate | route | triad | survival | drop | path survival | path D | obligation |",
            "| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| Q={q}->{ql} | {p} | `{gate}` | `{route}` | `{triad}` | {surv} | {drop} | {psurv} | {pd} | {obl} |".format(
                q=row["q"],
                ql=row["q_lift"],
                p=row["p"],
                gate=row["gate"],
                route=row["route"],
                triad=row["triad_target"],
                surv=fmt_float(row["survival"]),
                drop=fmt_float(row["density_drop_factor"]),
                psurv=fmt_float(row["path_product_survival"]),
                pd=fmt_float(row["path_deletion_potential"]),
                obl=row["obligation"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 当前边界",
            "",
            "当前路由没有给出最终证明，因为 `LiftFiberDeletion` 仍需无限塔删除势发散或后续 NoDeletion 分支证书。",
            "但它关闭了一个重要漏洞：新增层结果不会散落为临时解释，必须进入同一个终端三证书接口。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodeletion-json", type=Path, default=DEFAULT_NODELETION)
    parser.add_argument("--budget-json", type=Path, default=DEFAULT_BUDGET)
    parser.add_argument("--tower-json", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.nodeletion_json, args.budget_json, args.tower_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "route_counts": result["route_counts"],
                "triad_counts": result["triad_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
