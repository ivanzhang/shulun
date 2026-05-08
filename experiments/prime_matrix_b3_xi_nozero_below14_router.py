#!/usr/bin/env python3
"""Prime Matrix B=3 xi 低高度无零点路由器。

用法示例：
  python3 experiments/prime_matrix_b3_xi_nozero_below14_router.py

输出：
  docs/monograph/prime-matrix-b3-xi-nozero-below14-router.json
  docs/monograph/prime-matrix-b3-xi-nozero-below14-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-jensen-low-height-envelope-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-xi-nozero-below14-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-xi-nozero-below14-router.md"

OLD_ATOM = "BacklundXiNoNontrivialZeroBelow14FiniteCheckLedger"
XI_EQUIV_ATOM = "BacklundXiZetaNontrivialZeroEquivalenceClosed"
CRITICAL_LINE_ATOM = "CriticalLineNoZeroOn0To14FiniteLedger"
OFF_LINE_ATOM = "CriticalStripNoOffLineZeroBelow14TuringLedger"
EXTERNAL_FIRST_ZERO_ATOM = "ClassicalFirstZetaZeroHeightGT14ExternalAccepted"
EXTERNAL_CLOSED_ATOM = "BacklundXiNoNontrivialZeroBelow14ExternalClosed"
LOW_C16_CLOSED = "BacklundJensenLowHeightC16ImmediateGivenNoZeroBelow14"
RADIUS_OPT_ATOM = "BacklundJensenRadiusOptimizationOrCNRelaxationLedger"
NEAR_ZERO_ATOM = "BacklundNearZeroIndentSeparationLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

HEIGHT_TARGET = 14.0
FIRST_ZERO_REFERENCE = 14.134725141734693
ODLYZKO_FIRST_ZERO_ROUNDED = 14.134725142
LMFDB_ABSOLUTE_PRECISION_POWER = -102
LMFDB_ABSOLUTE_PRECISION = 2.0**LMFDB_ABSOLUTE_PRECISION_POWER
PLATT_TRUDGIAN_HEIGHT = 3_000_175_332_800.0
LOW_CENTER_HEIGHT = 10.0
OUTER_RADIUS = 4.0
LOW_DISK_IMAG_CEILING = LOW_CENTER_HEIGHT + OUTER_RADIUS
C_N_TARGET = 16.0
LOW_LOG_FLOOR = math.log(3.0)
LOW_ALLOWED_MIN = C_N_TARGET * LOW_LOG_FLOOR

EXTERNAL_SOURCES = [
    {
        "name": "LMFDB Riemann zeta zeros source page",
        "url": "https://www.lmfdb.org/zeros/zeta/Source",
        "claim": (
            "David Platt computed the zeta-zero database; zero heights are stored with "
            "absolute precision +-2^-102 and completeness was checked by rigorous Turing method."
        ),
    },
    {
        "name": "Odlyzko first zeta-zero table",
        "url": "https://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros1",
        "claim": "The first tabulated zeta zero has imaginary part 14.134725142.",
    },
    {
        "name": "Platt-Trudgian partial RH verification",
        "url": "https://arxiv.org/abs/2004.09765",
        "claim": "The Riemann hypothesis is rigorously verified up to height 3,000,175,332,800.",
    },
]


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


def fmt_number(value: float) -> str:
    """按量级选择可读数字格式。"""
    if value != 0.0 and abs(value) < 1e-6:
        return f"{value:.6e}"
    if abs(value) >= 1e9:
        return f"{value:.0f}"
    return fmt_float(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def self_replacement() -> str:
    """写出内部自足路线的替换包。"""
    return f"({XI_EQUIV_ATOM} AND {CRITICAL_LINE_ATOM} AND {OFF_LINE_ATOM})"


def external_replacement() -> str:
    """写出外部经典证书路线的替换包。"""
    return f"({XI_EQUIV_ATOM} AND {EXTERNAL_FIRST_ZERO_ATOM} AND {EXTERNAL_CLOSED_ATOM})"


def replace_atom(text: str, replacement: str) -> str:
    """替换低高度无零点原子。"""
    return text.replace(OLD_ATOM, replacement)


def source_rows() -> list[dict[str, Any]]:
    """生成外部证据源表。"""
    margin = FIRST_ZERO_REFERENCE - HEIGHT_TARGET
    rounded_margin = ODLYZKO_FIRST_ZERO_ROUNDED - HEIGHT_TARGET
    return [
        {
            "item": "height target",
            "value": HEIGHT_TARGET,
            "meaning": "低高度 Jensen 圆盘只需要排除 0<|Im rho|<=14。",
        },
        {
            "item": "first zero reference",
            "value": FIRST_ZERO_REFERENCE,
            "meaning": "标准首个非平凡零点高度参考值。",
        },
        {
            "item": "Odlyzko rounded first zero",
            "value": ODLYZKO_FIRST_ZERO_ROUNDED,
            "meaning": "公开首零点表首行值；即使用 9 位小数仍大于 14。",
        },
        {
            "item": "height margin",
            "value": margin,
            "meaning": "精确参考值相对 14 的安全间隔。",
        },
        {
            "item": "rounded height margin",
            "value": rounded_margin,
            "meaning": "公开表舍入值相对 14 的安全间隔。",
        },
        {
            "item": "LMFDB precision",
            "value": LMFDB_ABSOLUTE_PRECISION,
            "meaning": "LMFDB 声明零点高度精度 +-2^-102，远小于 margin。",
        },
        {
            "item": "Platt-Trudgian height",
            "value": PLATT_TRUDGIAN_HEIGHT,
            "meaning": "外部严格区间算术 RH 验证高度，远高于 14。",
        },
        {
            "item": "low disk ceiling",
            "value": LOW_DISK_IMAG_CEILING,
            "meaning": "|T|<10、R=4 时圆盘高度上界。",
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
    """生成 xi 低高度无零点判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    geometry_ready = bool(previous.get("backlund_jensen_low_height_envelope_reduced"))
    disk_ready = LOW_DISK_IMAG_CEILING <= HEIGHT_TARGET
    margin_ready = (
        FIRST_ZERO_REFERENCE > HEIGHT_TARGET
        and ODLYZKO_FIRST_ZERO_ROUNDED > HEIGHT_TARGET
        and (FIRST_ZERO_REFERENCE - HEIGHT_TARGET) > 10**20 * LMFDB_ABSOLUTE_PRECISION
    )
    external_height_ready = PLATT_TRUDGIAN_HEIGHT > HEIGHT_TARGET
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    external_closed = active and geometry_ready and disk_ready and margin_ready and external_height_ready and guard
    return [
        row(
            "XiNoZeroBelow14GateActive",
            active,
            False,
            "上一层唯一内部最窄点是 xi 在 0<|Im s|<=14 无非平凡零点的有限证书。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条调用的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LowHeightDiskGeometryReady",
            geometry_ready and disk_ready,
            True,
            "|T|<10 且 R=4 的 Jensen 圆盘已经压入 |Im s|<=14。",
            "无几何输入剩余。",
        ),
        row(
            "XiZetaZeroEquivalenceReady",
            True,
            True,
            "xi 的非平凡零点与 zeta 的非平凡零点等价；平凡零点与极点已由 xi 因子抵消。",
            XI_EQUIV_ATOM,
        ),
        row(
            "ExternalFirstZeroHeightMarginAccepted",
            margin_ready,
            False,
            "接受外部零点表/Turing 完备性时，首个非平凡零点高度大于 14，且精度误差远小于余量。",
            EXTERNAL_FIRST_ZERO_ATOM,
        ),
        row(
            "ExternalNoZeroBelow14Closed",
            external_closed,
            False,
            "外部经典证书路线可关闭 0<|Im rho|<=14 的 xi 非平凡无零点输入。",
            EXTERNAL_CLOSED_ATOM,
        ),
        row(
            "LowHeightC16ImmediateClosedExternally",
            external_closed,
            False,
            "低高度圆盘无零点后，局部零点数为 0，立即小于 16 log(T+3)。",
            LOW_C16_CLOSED,
        ),
        row(
            "SelfContainedCriticalLineFiniteLedgerStillOpen",
            False,
            False,
            "完全自足路线还需在仓库内给出临界线 0<t<=14 的严格非零有限账本。",
            CRITICAL_LINE_ATOM,
        ),
        row(
            "SelfContainedOffLineTuringLedgerStillOpen",
            False,
            False,
            "完全自足路线还需内联 Turing/argument-principle 计数，排除 0<t<=14 的离线零点。",
            OFF_LINE_ATOM,
        ),
        row(
            "RadiusOptimizationNowOnlyContingency",
            False,
            False,
            "接受外部低高度无零证书后，半径优化只剩冗余验收门；下一步应把它形式关闭为不需要。",
            RADIUS_OPT_ATOM,
        ),
        row(
            "NearZeroStillDownstream",
            False,
            False,
            "C_N=16 聚合完全验收后再进入近零分离。",
            NEAR_ZERO_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行 xi 低高度无零点路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    external_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ExternalNoZeroBelow14Closed"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), self_replacement())
    latest_external = replace_atom(previous.get("latest_self_contained_basis", ""), external_replacement())
    return {
        "certificate_type": "b3_xi_nozero_below14_router",
        "status": "xi_nozero_below14_external_closed_self_contained_finite_turing_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "xi_nozero_below14_external_closed": external_closed,
        "xi_nozero_below14_self_contained_proved": False,
        "low_height_c16_immediate_external_closed": external_closed,
        "low_height_envelope_external_closed": external_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "height_target": HEIGHT_TARGET,
        "first_zero_reference": FIRST_ZERO_REFERENCE,
        "odlyzko_first_zero_rounded": ODLYZKO_FIRST_ZERO_ROUNDED,
        "height_margin": FIRST_ZERO_REFERENCE - HEIGHT_TARGET,
        "lmfdb_absolute_precision": LMFDB_ABSOLUTE_PRECISION,
        "platt_trudgian_height": PLATT_TRUDGIAN_HEIGHT,
        "low_disk_imag_ceiling": LOW_DISK_IMAG_CEILING,
        "low_allowed_min": LOW_ALLOWED_MIN,
        "replacement_self_contained": {OLD_ATOM: self_replacement()},
        "replacement_external": {OLD_ATOM: external_replacement()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_external,
        "latest_global_with_external_basis": latest_external,
        "next_priority": CRITICAL_LINE_ATOM,
        "secondary_priority": OFF_LINE_ATOM,
        "conditional_next_priority": RADIUS_OPT_ATOM,
        "tertiary_priority": NEAR_ZERO_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "external_sources": EXTERNAL_SOURCES,
        "source_rows": source_rows(),
        "plain_conclusion": (
            "xi 低高度无零点输入可由外部经典零点表与严格 Turing 完备性证书关闭：首个非平凡零点高度 "
            "14.134725141734693 大于 14，而 Jensen 低高度圆盘只到 |Im s|<=14。"
            "但这不是仓库内自足证明；完全自足路线仍缺少临界线有限非零账本和低高度 Turing 计数账本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    self_repl = next(iter(result["replacement_self_contained"].items()))
    ext_repl = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 xi 低高度无零点路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"xi_nozero_below14_external_closed={fmt_bool(result['xi_nozero_below14_external_closed'])}",
        (
            "xi_nozero_below14_self_contained_proved="
            f"{fmt_bool(result['xi_nozero_below14_self_contained_proved'])}"
        ),
        (
            "low_height_c16_immediate_external_closed="
            f"{fmt_bool(result['low_height_c16_immediate_external_closed'])}"
        ),
        f"height_target={fmt_float(result['height_target'])}",
        f"first_zero_reference={fmt_float(result['first_zero_reference'])}",
        f"height_margin={fmt_float(result['height_margin'])}",
        f"low_disk_imag_ceiling={fmt_float(result['low_disk_imag_ceiling'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 拆分律",
        "",
        "完全自足路线：",
        "",
        "```text",
        self_repl[0],
        "  =>",
        self_repl[1],
        "```",
        "",
        "外部经典证书路线：",
        "",
        "```text",
        ext_repl[0],
        "  =>",
        ext_repl[1],
        "```",
        "",
        "外部路线只关闭解析 Backlund/Jensen 输入，不关闭行列命题本身；自足版仍需内联低高度零点验证。",
        "",
        "## 2. 数值边界",
        "",
        "| item | value | meaning |",
        "| --- | ---: | --- |",
    ]
    for item in result["source_rows"]:
        value = item["value"]
        if isinstance(value, float):
            value_text = fmt_number(value)
        else:
            value_text = str(value)
        lines.append(
            f"| {table_cell(item['item'])} | `{value_text}` | {table_cell(item['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "关键点是 margin 为常数量级 `0.1347...`，远大于零点表精度 `2^-102`；因此外部表的舍入误差不会影响 `>14` 判定。",
            "",
            "## 3. 外部来源",
            "",
            "| source | url | claim used |",
            "| --- | --- | --- |",
        ]
    )
    for source in result["external_sources"]:
        lines.append(
            "| {name} | {url} | {claim} |".format(
                name=table_cell(source["name"]),
                url=table_cell(source["url"]),
                claim=table_cell(source["claim"]),
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
            "## 5. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional/external Backlund 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"完全自足路线先攻 `{result['next_priority']}`，随后是 `{result['secondary_priority']}`；"
                f"若接受外部低高度零点证书，则下一步转为 `{result['conditional_next_priority']}`。"
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
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
