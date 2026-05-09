#!/usr/bin/env python3
"""Prime Matrix 低高度 xi 矩形零点计数压缩路由器。

用法示例：
  python3 experiments/prime_matrix_lowheight_rectangle_count_compression_router.py

输出：
  docs/monograph/prime-matrix-lowheight-rectangle-count-compression-router.json
  docs/monograph/prime-matrix-lowheight-rectangle-count-compression-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_LOWHEIGHT = MONO / "prime-matrix-lowheight-backlund-self-contained-package-router.json"
DEFAULT_XI_NOZERO = MONO / "prime-matrix-b3-xi-nozero-below14-router.json"
DEFAULT_TERMINAL = MONO / "prime-matrix-terminal-two-package-breakthrough-router.json"
DEFAULT_JSON = MONO / "prime-matrix-lowheight-rectangle-count-compression-router.json"
DEFAULT_MD = MONO / "prime-matrix-lowheight-rectangle-count-compression-router.md"

CRITICAL_LINE = "CriticalLineNoZeroOn0To14FiniteLedger"
OFF_LINE_TURING = "CriticalStripNoOffLineZeroBelow14TuringLedger"
RECT_COUNT = "LowHeightXiRectangleZeroCountZero0To14Ledger"
BOUNDARY_NONZERO = "XiBoundaryIntervalNonzeroCertificate0To14"
WINDING_ZERO = "XiBoundaryWindingNumberZeroIntervalCertificate0To14"
INTERVAL_ENGINE = "SelfContainedXiIntervalEvaluationEngine0To14"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
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


def rectangle_replacement() -> str:
    """写出二原子压缩替换。"""
    return f"({CRITICAL_LINE} AND {OFF_LINE_TURING}) => {RECT_COUNT}"


def rectangle_certificate_package() -> str:
    """写出矩形计数证书的必要子包。"""
    return f"{INTERVAL_ENGINE} AND {BOUNDARY_NONZERO} AND {WINDING_ZERO}"


def build_rows(
    lowheight: dict[str, Any],
    xi_nozero: dict[str, Any],
    terminal: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成低高度矩形计数压缩判定表。"""
    lowheight_active = (
        lowheight.get("next_finite_target") == CRITICAL_LINE
        and lowheight.get("next_turing_target") == OFF_LINE_TURING
    )
    xi_split_present = (
        xi_nozero.get("next_priority") == CRITICAL_LINE
        and xi_nozero.get("secondary_priority") == OFF_LINE_TURING
    )
    terminal_points_here = terminal.get("next_best_math_target") == "RiemannSiegelIntervalArithmetic0To14Ledger"
    replacement_valid = lowheight_active and xi_split_present and terminal_points_here

    return [
        row(
            "LowHeightSplitActive",
            lowheight_active and xi_split_present,
            True,
            "当前低高度包确实把自足剩余拆成临界线有限账本与离线 Turing 账本。",
            f"{CRITICAL_LINE} AND {OFF_LINE_TURING}",
        ),
        row(
            "RectangleCountDominatesBothAtoms",
            replacement_valid,
            True,
            (
                "若 xi 在覆盖 0<Im s<=14 的低高度矩形中零点计数为 0，"
                "则临界线和离线区域都没有零点，两个旧原子同时关闭。"
            ),
            RECT_COUNT,
        ),
        row(
            "BoundaryNonzeroCertificateRequired",
            False,
            False,
            "argument principle 需要证明矩形边界上 xi 不为 0，避免 winding 数未定义。",
            BOUNDARY_NONZERO,
        ),
        row(
            "WindingNumberZeroCertificateRequired",
            False,
            False,
            "需要用区间算术证明 xi(boundary) 曲线绕原点次数为 0，而不是只做浮点采样。",
            WINDING_ZERO,
        ),
        row(
            "SelfContainedIntervalEngineRequired",
            False,
            False,
            "必须内联 xi、Gamma、zeta 的区间求值与余项界，不能依赖外部零点表。",
            INTERVAL_ENGINE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行低高度矩形计数压缩。"""
    lowheight = load_json(paths["lowheight"])
    xi_nozero = load_json(paths["xi_nozero"])
    terminal = load_json(paths["terminal"])
    rows = build_rows(lowheight, xi_nozero, terminal)
    compression_closed = rows[1]["closed"]
    strict_rectangle_count_closed = False
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_lowheight_rectangle_count_compression_router",
        "status": "lowheight_two_zero_atoms_compressed_to_rectangle_count_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "old_lowheight_pair": f"{CRITICAL_LINE} AND {OFF_LINE_TURING}",
        "replacement": rectangle_replacement(),
        "new_single_atom": RECT_COUNT,
        "required_rectangle_certificate_package": rectangle_certificate_package(),
        "compression_closed": compression_closed,
        "strict_rectangle_count_closed": strict_rectangle_count_closed,
        "row_column_self_contained_closed": False,
        "next_priority": RECT_COUNT,
        "next_engine_priority": INTERVAL_ENGINE,
        "next_boundary_priority": BOUNDARY_NONZERO,
        "next_winding_priority": WINDING_ZERO,
        "plain_conclusion": (
            "低高度零点包可再压缩：不必分别证明临界线无零和离线 Turing 计数。"
            "一个自足的 xi 矩形零点计数为 0 证书即可同时关闭二者。"
            "这一步只完成逻辑压缩；真正证明仍需 xi 区间求值引擎、边界非零证书和 winding=0 证书。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 低高度 xi 矩形零点计数压缩路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"compression_closed={fmt_bool(result['compression_closed'])}",
        f"strict_rectangle_count_closed={fmt_bool(result['strict_rectangle_count_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 压缩替换",
        "",
        "```text",
        result["replacement"],
        "```",
        "",
        "新的单原子：",
        "",
        "```text",
        result["new_single_atom"],
        "```",
        "",
        "必要证书包：",
        "",
        "```text",
        result["required_rectangle_certificate_package"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            f"下一主攻单原子：`{result['next_priority']}`。",
            f"先补 `{{{result['next_engine_priority']}}}`，再补 `{{{result['next_boundary_priority']}}}` 与 `{{{result['next_winding_priority']}}}`。",
            "",
            "判定：这是严格自足路线的进一步压缩，不是外部零点表接受，也不是最终闭合。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lowheight-json", type=Path, default=DEFAULT_LOWHEIGHT)
    parser.add_argument("--xi-nozero-json", type=Path, default=DEFAULT_XI_NOZERO)
    parser.add_argument("--terminal-json", type=Path, default=DEFAULT_TERMINAL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "lowheight": args.lowheight_json,
        "xi_nozero": args.xi_nozero_json,
        "terminal": args.terminal_json,
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
