#!/usr/bin/env python3
"""Prime Matrix 顶边临界半段压缩路由器。

用法示例：
  python3 experiments/prime_matrix_top_edge_symmetry_halfstrip_router.py

输出：
  docs/monograph/prime-matrix-top-edge-symmetry-halfstrip-router.json
  docs/monograph/prime-matrix-top-edge-symmetry-halfstrip-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = MONO / "prime-matrix-xi-boundary-nonzero-top-edge-reduction-router.json"
DEFAULT_JSON = MONO / "prime-matrix-top-edge-symmetry-halfstrip-router.json"
DEFAULT_MD = MONO / "prime-matrix-top-edge-symmetry-halfstrip-router.md"

OLD_ATOM = "TopEdgeXiIntervalBoxCoverLedgerT14SigmaMinus1To2"
NEW_ATOM = "TopCriticalSegmentXiBoxCoverLedgerT14SigmaHalfToOne"
WINDING_ATOM = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"


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


def reductions() -> list[dict[str, str]]:
    """给出顶边压缩分段。"""
    return [
        {
            "segment": "sigma in [-1,1/2]",
            "status": "reduced_by_functional_and_conjugate_symmetry",
            "reason": "xi(s)=xi(1-s) 且 xi(conj s)=conj xi(s)，非零性转移到 sigma in [1/2,2] 的同一高度。",
        },
        {
            "segment": "sigma in (1,2]",
            "status": "closed_by_euler_product",
            "reason": "Re(s)>1 时 zeta(s) 的 Euler product 非零，xi 显式因子也非零。",
        },
        {
            "segment": "sigma in [1/2,1]",
            "status": "open_self_contained",
            "reason": "这是顶边穿过临界带的唯一剩余半段，需要有限区间盒逐段证明 0 不在 xi 盒内。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成顶边临界半段压缩判定表。"""
    active = previous.get("next_priority") == OLD_ATOM
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
    )
    three_sides_ready = previous.get("boundary_nonzero_three_sides_structurally_closed") is True
    external_closed = previous.get("boundary_nonzero_external_closed") is True
    compression_closed = active and guard and three_sides_ready
    return [
        row(
            "TopEdgeGateActive",
            active,
            True,
            "上一层已把严格自足边界非零压缩到顶边盒覆盖。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只用 xi 的函数方程、共轭对称和 Euler product，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "LeftHalfTopEdgeReducedBySymmetry",
            compression_closed,
            True,
            "顶边 sigma<=1/2 由 xi(s)=xi(1-s) 与共轭对称转移到 sigma>=1/2。",
            "no separate boxes on [-1,1/2].",
        ),
        row(
            "RightOuterTopEdgeClosedByEulerProduct",
            compression_closed,
            True,
            "顶边 sigma>1 处 Re(s)>1，zeta Euler product 排除零点。",
            "no boxes needed on (1,2].",
        ),
        row(
            "CriticalHalfSegmentStillMissing",
            False,
            False,
            "严格自足路线只剩顶边临界半段 1/2<=sigma<=1 的有限区间盒覆盖。",
            NEW_ATOM,
        ),
        row(
            "ExternalRouteAlreadyClosesTopEdge",
            external_closed,
            False,
            "若接受外部低高度无零点证书，顶边全段和 winding 已条件闭合。",
            f"{OLD_ATOM} AND {WINDING_ATOM}",
        ),
        row(
            OLD_ATOM,
            False,
            False,
            "旧顶边全段账本已被压缩，但严格自足闭合还需临界半段盒证书。",
            NEW_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行顶边临界半段压缩路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    compression_closed = all(
        item["closed"]
        for item in rows
        if item["gate"] in {"LeftHalfTopEdgeReducedBySymmetry", "RightOuterTopEdgeClosedByEulerProduct"}
    )
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_top_edge_symmetry_halfstrip_router",
        "status": "top_edge_reduced_to_critical_half_segment_external_still_closed",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "top_edge_full_segment_compressed": compression_closed,
        "top_edge_self_contained_closed": False,
        "top_edge_external_closed": previous.get("boundary_nonzero_external_closed") is True,
        "lowheight_rectangle_count_self_contained_closed": False,
        "row_column_self_contained_closed": False,
        "replacement_self_contained": {OLD_ATOM: NEW_ATOM},
        "segment_reductions": reductions(),
        "next_priority": NEW_ATOM,
        "secondary_priority": WINDING_ATOM,
        "plain_conclusion": (
            "顶边全段盒覆盖已进一步压缩：左半由函数方程和共轭对称转移，右外段由 Euler product "
            "关闭。严格自足唯一剩余变成 Im(s)=14, 1/2<=Re(s)<=1 的临界半段盒证书。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 顶边临界半段压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"top_edge_full_segment_compressed={fmt_bool(result['top_edge_full_segment_compressed'])}",
        f"top_edge_self_contained_closed={fmt_bool(result['top_edge_self_contained_closed'])}",
        f"top_edge_external_closed={fmt_bool(result['top_edge_external_closed'])}",
        (
            "lowheight_rectangle_count_self_contained_closed="
            f"{fmt_bool(result['lowheight_rectangle_count_self_contained_closed'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 顶边分段",
        "",
        "| segment | status | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["segment_reductions"]:
        lines.append(
            "| `{segment}` | `{status}` | {reason} |".format(
                segment=table_cell(item["segment"]),
                status=table_cell(item["status"]),
                reason=table_cell(item["reason"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一步",
            "",
            f"严格自足唯一剩余：`{result['next_priority']}`。",
            f"随后仍需：`{result['secondary_priority']}`。",
            "",
            "判定：现在不再需要全顶边盒，只需要临界半段盒。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous_json,
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
