#!/usr/bin/env python3
"""Prime Matrix B=3 Jensen 低高度显式 envelope 路由器。

用法示例：
  python3 experiments/prime_matrix_b3_jensen_low_height_envelope_router.py

输出：
  docs/monograph/prime-matrix-b3-jensen-low-height-envelope-router.json
  docs/monograph/prime-matrix-b3-jensen-low-height-envelope-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-signed-mean-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-jensen-low-height-envelope-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-jensen-low-height-envelope-router.md"

OLD_ATOM = "BacklundJensenLowHeightExplicitEnvelopeNumericalLedger"
GEOMETRY_CLOSED = "BacklundJensenLowHeightDiskImaginaryRangeClosedT14"
FINITE_CHECK_ATOM = "BacklundXiNoNontrivialZeroBelow14FiniteCheckLedger"
LOW_C16_CLOSED = "BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14"
RADIUS_OPT_ATOM = "BacklundJensenRadiusOptimizationOrCNRelaxationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SIGNED_MEAN_CLOSED = "BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7"

OUTER_RADIUS = 4.0
LOW_CENTER_HEIGHT = 10.0
LOW_DISK_IMAG_CEILING = LOW_CENTER_HEIGHT + OUTER_RADIUS
FIRST_ZERO_HEIGHT_REFERENCE = 14.134725141734693
C_N_TARGET = 16.0
LOW_LOG_FLOOR = math.log(3.0)
LOW_ALLOWED_MIN = C_N_TARGET * LOW_LOG_FLOOR


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replacement_pair() -> str:
    """写出低高度 envelope 替换包。"""
    return f"({GEOMETRY_CLOSED} AND {FINITE_CHECK_ATOM} AND {LOW_C16_CLOSED})"


def replace_atom(text: str) -> str:
    """替换旧低高度 envelope 原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


def geometry_rows() -> list[dict[str, float | str]]:
    """生成低高度圆盘几何表。"""
    return [
        {
            "item": "low center range",
            "value": "|T|<10",
            "meaning": "signed-mean 高高度已处理 |T|>=10。",
        },
        {
            "item": "Jensen radius",
            "value": OUTER_RADIUS,
            "meaning": "沿用 R=4 的外圆盘。",
        },
        {
            "item": "imaginary range",
            "value": LOW_DISK_IMAG_CEILING,
            "meaning": "|Im s| <= |T|+4 < 14。",
        },
        {
            "item": "first zero reference",
            "value": FIRST_ZERO_HEIGHT_REFERENCE,
            "meaning": "若可复现证明首个非平凡零点高度超过该值，则低高度圆盘无非平凡零点。",
        },
        {
            "item": "C16 minimum allowance",
            "value": LOW_ALLOWED_MIN,
            "meaning": "低高度最小右侧 16 log(3) 已大于 17。",
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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 Jensen 低高度显式 envelope 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    signed_mean_ready = SIGNED_MEAN_CLOSED in basis
    jensen_ready = "BacklundJensenDiskFormulaClosed" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    geometry_closed = active and signed_mean_ready and jensen_ready and guard and LOW_DISK_IMAG_CEILING < FIRST_ZERO_HEIGHT_REFERENCE
    reduced = active and signed_mean_ready and jensen_ready and guard
    return [
        row(
            "LowHeightEnvelopeGateActive",
            active,
            False,
            "上一层唯一内部最窄点是 Jensen 低高度显式 envelope。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "SignedMeanAndJensenInputsAvailable",
            signed_mean_ready and jensen_ready,
            True,
            "高高度 signed-mean 与 Jensen 圆盘公式已可用。",
            "无形式输入剩余。",
        ),
        row(
            "LowHeightDiskImaginaryRangeClosed",
            geometry_closed,
            True,
            "当 |T|<10 且 R=4，Jensen 圆盘满足 |Im s|<14。",
            GEOMETRY_CLOSED,
        ),
        row(
            "FiniteNoZeroBelow14CheckMissing",
            False,
            False,
            "还需可复现证明 xi 在 0<|Im s|<=14 无非平凡零点；不能直接引用真实零点表口头事实。",
            FINITE_CHECK_ATOM,
        ),
        row(
            "LowHeightC16ImmediateConditional",
            False,
            False,
            "若无零点低于 14，则低高度局部零点数为 0，自动小于 16 log(T+3)。",
            LOW_C16_CLOSED,
        ),
        row(
            "LowHeightEnvelopeReduced",
            reduced,
            False,
            "旧低高度显式 envelope 原子已压成圆盘高度几何、低高度无零有限证书、C16 立即验收三包。",
            replacement_pair(),
        ),
        row(
            "RadiusOptimizationStillContingent",
            False,
            False,
            "如果有限低高度证书失败或口径改变，才需要半径优化或常数放宽。",
            RADIUS_OPT_ATOM,
        ),
        row(
            "NearZeroStillDownstream",
            False,
            False,
            "低高度完成后再进入近零分离。",
            NEAR_ZERO_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 Jensen 低高度显式 envelope 路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    reduced = next(bool(item["closed"]) for item in rows if item["gate"] == "LowHeightEnvelopeReduced")
    return {
        "certificate_type": "b3_jensen_low_height_envelope_router",
        "status": "backlund_jensen_low_height_envelope_reduced_finite_zero_check_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "backlund_jensen_low_height_envelope_reduced": reduced,
        "backlund_jensen_low_height_envelope_closed": False,
        "low_center_height": LOW_CENTER_HEIGHT,
        "outer_radius": OUTER_RADIUS,
        "low_disk_imag_ceiling": LOW_DISK_IMAG_CEILING,
        "first_zero_height_reference": FIRST_ZERO_HEIGHT_REFERENCE,
        "low_allowed_min": LOW_ALLOWED_MIN,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": FINITE_CHECK_ATOM,
        "secondary_priority": RADIUS_OPT_ATOM,
        "tertiary_priority": NEAR_ZERO_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "geometry_rows": geometry_rows(),
        "plain_conclusion": (
            "Jensen 低高度显式 envelope 尚未闭合，但已压成一个非常小的有限验收门："
            "低高度圆盘全部落在 |Im s|<14；只要给出 xi 在该高度以下无非平凡零点的可复现证书，"
            "低高度 C_N=16 立即成立。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix B=3 Jensen 低高度显式 envelope 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"backlund_jensen_low_height_envelope_reduced={fmt_bool(result['backlund_jensen_low_height_envelope_reduced'])}",
        f"backlund_jensen_low_height_envelope_closed={fmt_bool(result['backlund_jensen_low_height_envelope_closed'])}",
        f"low_center_height={fmt_float(result['low_center_height'])}",
        f"outer_radius={fmt_float(result['outer_radius'])}",
        f"low_disk_imag_ceiling={fmt_float(result['low_disk_imag_ceiling'])}",
        f"first_zero_height_reference={fmt_float(result['first_zero_height_reference'])}",
        f"low_allowed_min={fmt_float(result['low_allowed_min'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 低高度几何",
        "",
        "| item | value | meaning |",
        "| --- | ---: | --- |",
    ]
    for item in result["geometry_rows"]:
        value = item["value"]
        value_text = fmt_float(float(value)) if isinstance(value, float) else str(value)
        lines.append(
            "| {item} | `{value}` | {meaning} |".format(
                item=table_cell(item["item"]),
                value=table_cell(value_text),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "注意：本步没有把“首零点高度”当作已证输入；它只是说明下一步有限证书的精确目标。",
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
