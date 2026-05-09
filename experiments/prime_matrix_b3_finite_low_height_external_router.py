#!/usr/bin/env python3
"""Prime Matrix B=3 低高度零点外部闭合路由器。

用法示例：
  python3 experiments/prime_matrix_b3_finite_low_height_external_router.py

输出：
  docs/monograph/prime-matrix-b3-finite-low-height-external-router.json
  docs/monograph/prime-matrix-b3-finite-low-height-external-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-theta-target-dusart-router.json"
DEFAULT_XI_NOZERO = DOCS / "prime-matrix-b3-xi-nozero-below14-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-finite-low-height-external-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-finite-low-height-external-router.md"

OLD_ATOM = "FiniteLowHeightZeroCheckLedger"
CLOSED_ATOM = "FiniteLowHeightZeroCheckExternalClosedFirstZeroGT14TuringComplete"
THETA_CLOSED = "DusartThetaEnvelopeTargetAt20000ExternalClosedOneOver36260"
XI_EXTERNAL_CLOSED = "BacklundXiNoNontrivialZeroBelow14ExternalClosed"
FIRST_ZERO_EXTERNAL = "ClassicalFirstZetaZeroHeightGT14ExternalAccepted"
EXPLICIT_CONTOUR = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
FINITE_BRIDGE = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
MERTENS_INTERVAL = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
CRITICAL_LINE_SELF = "CriticalLineNoZeroOn0To14FiniteLedger"
OFF_LINE_SELF = "CriticalStripNoOffLineZeroBelow14TuringLedger"
BACKLUND_INTERNAL = "ClassicalBacklundZeroIndentationCostInternalProofLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

HEIGHT_TARGET = 14.0


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
    """按量级输出数字，避免极小精度显示成零。"""
    if value != 0.0 and abs(value) < 1e-6:
        return f"{value:.6e}"
    if abs(value) >= 1e9:
        return f"{value:.0f}"
    return fmt_float(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom(text: str) -> str:
    """只在外部路线输入基中替换低高度原子。"""
    return text.replace(OLD_ATOM, CLOSED_ATOM)


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def xi_external_ready(xi_nozero: dict[str, Any]) -> bool:
    """判断已有 xi 低高度外部证书是否足以服务本主链低高度原子。"""
    margin = float(xi_nozero.get("height_margin", 0.0))
    target = float(xi_nozero.get("height_target", HEIGHT_TARGET))
    first_zero = float(xi_nozero.get("first_zero_reference", 0.0))
    platt_height = float(xi_nozero.get("platt_trudgian_height", 0.0))
    return (
        xi_nozero.get("xi_nozero_below14_external_closed") is True
        and xi_nozero.get("low_height_envelope_external_closed") is True
        and XI_EXTERNAL_CLOSED in xi_nozero.get("latest_conditional_basis", "")
        and FIRST_ZERO_EXTERNAL in xi_nozero.get("latest_conditional_basis", "")
        and target <= HEIGHT_TARGET
        and first_zero > HEIGHT_TARGET
        and margin > 0
        and platt_height > HEIGHT_TARGET
    )


def source_table(xi_nozero: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取低高度外部证书关键数字。"""
    return [
        {
            "item": "height target",
            "value": float(xi_nozero.get("height_target", HEIGHT_TARGET)),
            "meaning": "本主链只需排除 0<|gamma|<=14 的低高度非平凡零点。",
        },
        {
            "item": "first zero reference",
            "value": float(xi_nozero.get("first_zero_reference", 0.0)),
            "meaning": "外部首个非平凡零点高度参考值。",
        },
        {
            "item": "height margin",
            "value": float(xi_nozero.get("height_margin", 0.0)),
            "meaning": "首零点高度相对 14 的安全余量。",
        },
        {
            "item": "LMFDB precision",
            "value": float(xi_nozero.get("lmfdb_absolute_precision", 0.0)),
            "meaning": "零点高度登记精度，远小于安全余量。",
        },
        {
            "item": "Platt-Trudgian height",
            "value": float(xi_nozero.get("platt_trudgian_height", 0.0)),
            "meaning": "外部严格验证高度，远高于 14。",
        },
    ]


def build_rows(previous: dict[str, Any], xi_nozero: dict[str, Any]) -> list[dict[str, Any]]:
    """生成低高度外部闭合判定表。"""
    external_basis = previous.get("latest_external_titchmarsh_cn16_basis", "")
    self_basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in external_basis
    guard = (
        previous.get("counterexample_assumption_only") is True
        and previous.get("empirical_absence_not_used") is True
        and previous.get("hypothetical_chain_only") is True
        and previous.get("row_column_unconditional_closed") is False
    )
    theta_ready = previous.get("theta_target_external_closed") is True and THETA_CLOSED in external_basis
    xi_ready = xi_external_ready(xi_nozero)
    closed = active and guard and theta_ready and xi_ready
    return [
        row(
            "FiniteLowHeightGateActive",
            active,
            True,
            "Dusart theta 目标之后，外部主链当前最窄点是 T<=14 的有限低高度零点核验。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只补假设反例链条的解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ThetaTargetAlreadyClosedExternally",
            theta_ready,
            False,
            "上一层已经在外部路线中用 Dusart 显式 theta 界关闭 anchor 小误差目标。",
            THETA_CLOSED,
        ),
        row(
            "XiNoZeroBelow14ExternalCertificateReady",
            xi_ready,
            False,
            "已有 xi/no-zero-below14 证书登记首零点大于 14、零点表精度余量和 Platt-Trudgian/Turing 完备性。",
            XI_EXTERNAL_CLOSED,
        ),
        row(
            OLD_ATOM,
            closed,
            False,
            "接受外部低高度零点证书后，0<|gamma|<=14 没有非平凡零点，有限低高度核验在外部条件路线中关闭。",
            CLOSED_ATOM,
        ),
        row(
            "SelfContainedLowHeightStillOpen",
            False,
            False,
            "严格自足路线仍需文内 Riemann-Siegel 区间算术、临界线符号分离和 Turing/argument-principle 计数。",
            f"{CRITICAL_LINE_SELF} AND {OFF_LINE_SELF}",
        ),
        row(
            "SelfContainedBasisUnchanged",
            OLD_ATOM in self_basis,
            True,
            "本路由只替换外部输入基；自足输入基保留低高度原子，防止误报自足闭合。",
            OLD_ATOM,
        ),
        row(
            "DStructureRankinGateStillSeparate",
            False,
            False,
            "低高度解析输入闭合不触动最终行列命题的 DStructure/Rankin 独立验收门。",
            DSTRUCTURE_GATE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行低高度外部闭合路由。"""
    previous = load_json(paths["previous"])
    xi_nozero = load_json(paths["xi_nozero"])
    rows = build_rows(previous, xi_nozero)
    closed = next(item["closed"] for item in rows if item["gate"] == OLD_ATOM)
    latest_external = replace_atom(previous.get("latest_external_titchmarsh_cn16_basis", ""))
    return {
        "certificate_type": "b3_finite_low_height_external_router",
        "status": "finite_low_height_external_closed_self_contained_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "finite_low_height_external_closed": closed,
        "finite_low_height_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "height_target": HEIGHT_TARGET,
        "source_table": source_table(xi_nozero),
        "external_sources": xi_nozero.get("external_sources", []),
        "replacement_external": {OLD_ATOM: CLOSED_ATOM},
        "latest_external_titchmarsh_cn16_basis": latest_external,
        "latest_self_contained_basis": previous.get("latest_self_contained_basis", ""),
        "next_priority": EXPLICIT_CONTOUR,
        "secondary_priority": FINITE_BRIDGE,
        "mertens_interval_priority": MERTENS_INTERVAL,
        "parallel_self_contained_priorities": [CRITICAL_LINE_SELF, OFF_LINE_SELF, BACKLUND_INTERNAL],
        "final_independent_acceptance_gate": DSTRUCTURE_GATE,
        "plain_conclusion": (
            "外部条件路线下，`FiniteLowHeightZeroCheckLedger` 可由已有 xi 低高度无零点证书聚合关闭："
            "首个非平凡 zeta 零点高度约 `14.134725141734693` 大于 `14`，且外部 Turing/Platt-Trudgian "
            "完备性排除 `0<|gamma|<=14` 的漏零。该步不是仓库内自足证明；严格自足路线仍需内联 "
            "Riemann-Siegel/Turing 有限账本。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_external"].items()))
    lines = [
        "# Prime Matrix B=3 低高度零点外部闭合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"finite_low_height_external_closed={fmt_bool(result['finite_low_height_external_closed'])}",
        f"finite_low_height_self_contained_closed={fmt_bool(result['finite_low_height_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部条件替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 低高度证据数字",
        "",
        "| item | value | meaning |",
        "| --- | ---: | --- |",
    ]
    for item in result["source_table"]:
        lines.append(
            f"| {table_cell(item['item'])} | `{fmt_number(float(item['value']))}` | {table_cell(item['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 外部来源",
            "",
            "| source | url | claim |",
            "| --- | --- | --- |",
        ]
    )
    for source in result["external_sources"]:
        lines.append(
            "| {name} | {url} | {claim} |".format(
                name=table_cell(source.get("name", "")),
                url=table_cell(source.get("url", "")),
                claim=table_cell(source.get("claim", "")),
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
            "外部 Titchmarsh+CN16 路线输入基：",
            "",
            "```text",
            result["latest_external_titchmarsh_cn16_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            (
                f"下一步攻 `{result['next_priority']}`；随后连接 `{result['secondary_priority']}` 和 "
                f"`{result['mertens_interval_priority']}`。自足路线仍保留 "
                f"`{', '.join(result['parallel_self_contained_priorities'])}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--xi-nozero", type=Path, default=DEFAULT_XI_NOZERO)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "xi_nozero": args.xi_nozero}
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
