#!/usr/bin/env python3
"""Prime Matrix xi 边界非零顶边压缩路由器。

用法示例：
  python3 experiments/prime_matrix_xi_boundary_nonzero_top_edge_reduction_router.py

输出：
  docs/monograph/prime-matrix-xi-boundary-nonzero-top-edge-reduction-router.json
  docs/monograph/prime-matrix-xi-boundary-nonzero-top-edge-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_QUADRATURE = MONO / "prime-matrix-compact-theta-mellin-quadrature-router.json"
DEFAULT_XI_NOZERO = MONO / "prime-matrix-b3-xi-nozero-below14-router.json"
DEFAULT_JSON = MONO / "prime-matrix-xi-boundary-nonzero-top-edge-reduction-router.json"
DEFAULT_MD = MONO / "prime-matrix-xi-boundary-nonzero-top-edge-reduction-router.md"

OLD_ATOM = "XiBoundaryIntervalNonzeroCertificate0To14"
TOP_EDGE_ATOM = "TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"
EXTERNAL_NOZERO = "BacklundXiNoNontrivialZeroBelow14ExternalClosed"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


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


def side_reductions() -> list[dict[str, str]]:
    """给出边界四边的闭合/剩余分解。"""
    return [
        {
            "side": "right_edge_sigma_2",
            "status": "closed",
            "reason": "Re(s)=2>1，Euler product 给 zeta(s) 非零；xi 的显式因子在 2+it 上非零。",
        },
        {
            "side": "left_edge_sigma_minus_1",
            "status": "closed",
            "reason": "函数方程 xi(s)=xi(1-s) 把 -1+it 映到 2-it，继承右边界非零。",
        },
        {
            "side": "bottom_edge_t_0",
            "status": "closed",
            "reason": "实轴 [-1,2] 上 zeta 的实值符号、Gamma 极点抵消和 xi 的 s(s-1) 因子给 xi(s) 非零；s=0,1 为可去点且 xi 值非零。",
        },
        {
            "side": "top_edge_t_14",
            "status": "open_self_contained",
            "reason": "顶边穿过临界带最高处；自足路线必须给 sigma in [-1,2] 的有限区间盒并逐盒证明 0 不在 xi 盒内。",
        },
    ]


def box_certificate_contract() -> list[dict[str, str]]:
    """列出顶边盒证书的精确定义。"""
    return [
        {
            "field": "box_id",
            "meaning": "按 sigma 区间稳定排序的 dyadic 编号。",
        },
        {
            "field": "sigma_interval",
            "meaning": "顶边上的 dyadic 闭区间 [a/2^k,b/2^k]，全部覆盖 [-1,2]。",
        },
        {
            "field": "xi_rect_interval",
            "meaning": "用已闭合 xi 区间求值引擎输出的复矩形盒。",
        },
        {
            "field": "nonzero_witness",
            "meaning": "证明 0 不在复盒内：例如 Re 盒离 0、Im 盒离 0，或盒到原点距离下界为正。",
        },
        {
            "field": "parent_trace_hash",
            "meaning": "引用每盒求值 trace root，保证可复放。",
        },
    ]


def build_rows(quadrature: dict[str, Any], xi_nozero: dict[str, Any]) -> list[dict[str, Any]]:
    """生成边界非零顶边压缩判定表。"""
    active = quadrature.get("next_priority") == OLD_ATOM
    guard = (
        quadrature.get("counterexample_assumption_only") is True
        and quadrature.get("empirical_absence_not_used") is True
        and quadrature.get("hypothetical_chain_only") is True
    )
    engine_ready = quadrature.get("self_contained_xi_interval_engine_closed") is True
    external_ready = xi_nozero.get("xi_nozero_below14_external_closed") is True
    three_sides_closed = True
    top_edge_self_contained_closed = False
    self_closed = active and guard and engine_ready and three_sides_closed and top_edge_self_contained_closed
    external_closed = active and external_ready
    return [
        row(
            "BoundaryNonzeroGateActive",
            active,
            True,
            "求值引擎闭合后，当前最窄点是 xi 低高度矩形边界非零证书。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步处理低高度解析证书，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "SelfContainedXiIntervalEngineAvailable",
            engine_ready,
            True,
            "theta-Mellin 区间求值引擎已经闭合，可生成顶边有限区间盒。",
            "SelfContainedXiIntervalEvaluationEngine0To14",
        ),
        row(
            "RightLeftBottomEdgesClosedStructurally",
            three_sides_closed,
            True,
            "右边界由 Euler product，左边界由函数方程，底边由实轴非零和可去点值关闭。",
            "only top edge remains.",
        ),
        row(
            "TopEdgeBoxCoverStillMissing",
            False,
            False,
            "自足路线还必须实际给出 Im(s)=14, -1<=Re(s)<=2 的有限区间盒覆盖并逐盒排除 0。",
            TOP_EDGE_ATOM,
        ),
        row(
            "ExternalNoZeroBelow14ClosesBoundary",
            external_closed,
            False,
            "若接受外部首零点/Turing 完备性证书，矩形内无零点，边界非零与 winding=0 同时成立。",
            f"{OLD_ATOM} AND {WINDING_ATOM}",
        ),
        row(
            OLD_ATOM,
            self_closed,
            self_closed,
            "严格自足边界非零尚未闭合；已压缩为唯一顶边盒覆盖账本。",
            TOP_EDGE_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi 边界非零顶边压缩路由。"""
    quadrature = load_json(paths["quadrature"])
    xi_nozero = load_json(paths["xi_nozero"])
    rows = build_rows(quadrature, xi_nozero)
    self_closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    external_closed = next(item["closed"] for item in rows if item["gate"] == "ExternalNoZeroBelow14ClosesBoundary")
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_xi_boundary_nonzero_top_edge_reduction_router",
        "status": "boundary_nonzero_reduced_to_top_edge_box_cover_external_closed"
        if external_closed and not self_closed
        else "boundary_nonzero_self_contained_closed"
        if self_closed
        else "boundary_nonzero_top_edge_box_cover_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "boundary_nonzero_three_sides_structurally_closed": True,
        "boundary_nonzero_self_contained_closed": self_closed,
        "boundary_nonzero_external_closed": external_closed,
        "winding_external_closed": external_closed,
        "lowheight_rectangle_count_external_closed": external_closed,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: TOP_EDGE_ATOM},
        "replacement_external": {
            f"{OLD_ATOM} AND {WINDING_ATOM}": EXTERNAL_NOZERO,
        },
        "side_reductions": side_reductions(),
        "top_edge_box_certificate_contract": box_certificate_contract(),
        "next_priority": TOP_EDGE_ATOM,
        "secondary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "边界非零的自足路线已压缩到唯一顶边账本：右边、左边和底边有结构性非零证明；"
            "真正剩余是给 Im(s)=14 顶边的有限 xi 区间盒覆盖。若接受外部首零点/Turing 完备性证书，"
            "边界非零和 winding=0 可条件闭合，但严格自足版仍未闭合。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix xi 边界非零顶边压缩路由器",
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
            "boundary_nonzero_three_sides_structurally_closed="
            f"{fmt_bool(result['boundary_nonzero_three_sides_structurally_closed'])}"
        ),
        f"boundary_nonzero_self_contained_closed={fmt_bool(result['boundary_nonzero_self_contained_closed'])}",
        f"boundary_nonzero_external_closed={fmt_bool(result['boundary_nonzero_external_closed'])}",
        f"winding_external_closed={fmt_bool(result['winding_external_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 四边分解",
        "",
        "| side | status | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["side_reductions"]:
        lines.append(
            "| `{side}` | `{status}` | {reason} |".format(
                side=table_cell(item["side"]),
                status=table_cell(item["status"]),
                reason=table_cell(item["reason"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 顶边盒证书合同",
            "",
            "| field | meaning |",
            "| --- | --- |",
        ]
    )
    for item in result["top_edge_box_certificate_contract"]:
        lines.append(f"| `{table_cell(item['field'])}` | {table_cell(item['meaning'])} |")
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
            "## 4. 下一步",
            "",
            f"严格自足最窄点：`{result['next_priority']}`。",
            f"随后仍需：`{result['secondary_priority']}`。",
            "",
            "判定：外部路线可条件闭合；严格自足路线现在只差顶边有限盒证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quadrature-json", type=Path, default=DEFAULT_QUADRATURE)
    parser.add_argument("--xi-nozero-json", type=Path, default=DEFAULT_XI_NOZERO)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "quadrature": args.quadrature_json,
        "xi_nozero": args.xi_nozero_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["next_priority"])


if __name__ == "__main__":
    main()
