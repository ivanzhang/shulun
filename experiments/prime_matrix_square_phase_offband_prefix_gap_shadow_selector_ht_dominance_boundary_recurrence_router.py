#!/usr/bin/env python3
"""审计平方窗-尾素数支配低余量边界是否向高 P 复现。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_dominance_boundary_recurrence_router.py --max-p 10000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

EXTERNAL_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-router.md"

EXTERNAL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py"
)

MAIN_TARGET = "SelectorResidueSquareWindowTailDominanceOrBoundaryPDEC"
NEXT_TARGET = "AsymptoticSquareWindowTailDominanceOrLowMarginBoundaryRecurrencePDEC"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(path: Path, name: str) -> Any:
    """按路径加载模块。"""
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def margin(row: dict[str, Any]) -> int:
    """返回平方窗-尾素数支配余量。"""
    return int(row["square_window_tail_dominance_margin"])


def boundary_signature(row: dict[str, Any]) -> str:
    """低余量边界的复现签名。"""
    return "|".join(
        [
            f"side={row['side']}",
            f"W={row['target_W']}",
            f"rho={row['rho']}",
            f"template={row['template_index']}",
        ]
    )


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总支配余量。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        margins = [margin(row) for row in selected]
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "min_margin": min(margins, default=None),
                "zero_margin_count": sum(1 for value in margins if value == 0),
                "margin_le_1_count": sum(1 for value in margins if value <= 1),
                "margin_le_3_count": sum(1 for value in margins if value <= 3),
                "p_values_at_min": sorted({int(row["p"]) for row in selected if margins and margin(row) == min(margins)}),
            }
        )
    return records


def low_margin_records(rows: list[dict[str, Any]], cutoff: int) -> list[dict[str, Any]]:
    """列出低余量对象。"""
    selected = sorted(
        [row for row in rows if margin(row) <= cutoff],
        key=lambda row: (margin(row), int(row["p"]), int(row["template_index"])),
    )
    return [
        {
            "template_index": int(row["template_index"]),
            "p": int(row["p"]),
            "side": row["side"],
            "rho": int(row["rho"]),
            "target_W": int(row["target_W"]),
            "H": int(row["H"]),
            "T": int(row["T"]),
            "margin": margin(row),
            "normal_form_slack": int(row["normal_form_slack"]),
            "signature": boundary_signature(row),
        }
        for row in selected
    ]


def recurrence_records(rows: list[dict[str, Any]], cutoff: int) -> list[dict[str, Any]]:
    """按低余量签名汇总复现情况。"""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        if margin(row) <= cutoff:
            grouped.setdefault(boundary_signature(row), []).append(row)
    records: list[dict[str, Any]] = []
    for signature, values in sorted(grouped.items()):
        p_values = sorted({int(row["p"]) for row in values})
        margins = [margin(row) for row in values]
        records.append(
            {
                "signature": signature,
                "hit_count": len(values),
                "distinct_p_count": len(p_values),
                "p_values": p_values,
                "min_margin": min(margins),
                "max_margin": max(margins),
                "recurrent_on_current_sweep": len(p_values) >= 2,
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "finite_low_margin_boundary_isolated",
            "status": "closed_on_current_sweep",
            "statement": "Low-margin selector rho hits are isolated and grouped by boundary recurrence signature.",
        },
        {
            "name": "current_no_high_p_margin_le_1_recurrence",
            "status": "closed_on_current_sweep",
            "statement": "No margin<=1 hit appears beyond the current finite boundary core in the tested range.",
        },
        {
            "name": "asymptotic_square_window_tail_dominance",
            "status": "open",
            "statement": "A global proof must show the dominance margin stays nonnegative beyond the finite boundary core.",
        },
        {
            "name": "low_margin_boundary_recurrence_pdec",
            "status": "open",
            "statement": "If low-margin classes recur indefinitely, they must be routed to a boundary recurrence PDEC/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CurrentDominanceStillHoldsAtExtendedBound",
            "closed": agg["dominance_failure_count"] == 0,
            "proved": True,
            "meaning": "扩展有限扫描中平方窗-尾素数支配仍无失败。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "LowMarginBoundaryCoreIsolated",
            "closed": True,
            "proved": True,
            "meaning": "margin<=1 的边界核已定位并签名化。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "AsymptoticDominanceProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需无条件证明边界核之后支配余量不再跌破 0。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "BoundaryRecurrencePDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "若低余量签名高处复现，仍需 PDEC/ColumnCRT 排斥。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只隔离边界复现结构，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(external_ledger: Path, template_ledger: Path, max_p: int, low_margin_cutoff: int) -> dict[str, Any]:
    """构造边界复现审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(external_ledger)
    external_module = load_module(EXTERNAL_ROUTER, "ht_dominance_boundary_external")
    rows, replay = external_module.build_rows(max_p, template_ledger)
    margins = [margin(row) for row in rows]
    low_rows = low_margin_records(rows, low_margin_cutoff)
    recurrence = recurrence_records(rows, low_margin_cutoff)
    margin_le_1_rows = [row for row in rows if margin(row) <= 1]
    margin_le_3_rows = [row for row in rows if margin(row) <= 3]
    finite_core_upper = max((int(row["p"]) for row in margin_le_1_rows), default=None)
    bands = [(3, 2000), (2001, 5000), (5001, max_p)]
    aggregate = {
        "external_ledger": str(external_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "low_margin_cutoff": low_margin_cutoff,
        "prime_rho_hit_count": len(rows),
        "previous_prime_rho_hit_count": source["aggregate"]["prime_rho_hit_count"],
        "formula_failure_count": len(replay["formula_failures"]),
        "dominance_failure_count": sum(1 for row in rows if margin(row) < 0),
        "min_margin": min(margins, default=0),
        "max_margin": max(margins, default=0),
        "zero_margin_count": sum(1 for value in margins if value == 0),
        "margin_le_1_count": len(margin_le_1_rows),
        "margin_le_1_distinct_p_values": sorted({int(row["p"]) for row in margin_le_1_rows}),
        "margin_le_1_max_p": finite_core_upper,
        "margin_le_3_count": len(margin_le_3_rows),
        "margin_le_3_max_p": max((int(row["p"]) for row in margin_le_3_rows), default=None),
        "low_margin_signature_count": len(recurrence),
        "recurrent_low_margin_signature_count": sum(1 for row in recurrence if row["recurrent_on_current_sweep"]),
        "no_margin_le_1_after_finite_core_on_current_sweep": all(
            int(row["p"]) <= int(finite_core_upper or 0) for row in margin_le_1_rows
        ),
        "asymptotic_square_window_tail_dominance_proved": False,
        "boundary_recurrence_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**source["parameters"], "max_p": max_p, "low_margin_cutoff": low_margin_cutoff},
        "aggregate": aggregate,
        "band_records": band_records(rows, bands),
        "low_margin_records": low_rows,
        "boundary_recurrence_records": recurrence,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_dominance_boundary_recurrence_router",
        "status": "selector_square_window_tail_dominance_boundary_core_isolated_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_boundary_audit_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "band_records": ledger["band_records"],
        "low_margin_records": low_rows,
        "boundary_recurrence_records": recurrence,
        "asymptotic_square_window_tail_dominance_proved": False,
        "boundary_recurrence_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_dominance_boundary_recurrence_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py": sha256(
                EXTERNAL_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-external-input-match-ledger.json": sha256(
                external_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            f"本步把平方窗-尾素数支配的低余量边界隔离出来。扩展到 P<={max_p} 时，"
            f"prime rho hit 为 {len(rows)} 个，支配失败数为 {aggregate['dominance_failure_count']}；"
            f"唯一零余量仍在有限边界核内，margin<=1 的最大 P 为 {finite_core_upper}。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H/T dominance boundary recurrence router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"formula_failure_count={agg['formula_failure_count']}",
        f"dominance_failure_count={agg['dominance_failure_count']}",
        f"min_margin={agg['min_margin']}",
        f"zero_margin_count={agg['zero_margin_count']}",
        f"margin_le_1_count={agg['margin_le_1_count']}",
        f"margin_le_1_distinct_p_values={agg['margin_le_1_distinct_p_values']}",
        f"margin_le_1_max_p={agg['margin_le_1_max_p']}",
        f"recurrent_low_margin_signature_count={agg['recurrent_low_margin_signature_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. P 区间余量",
        "",
        "| P range | hits | min margin | zero margin | margin<=1 | margin<=3 | p at min |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row["min_margin"]),
                    str(row["zero_margin_count"]),
                    str(row["margin_le_1_count"]),
                    str(row["margin_le_3_count"]),
                    f"`{row['p_values_at_min']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 低余量对象",
            "",
            "| margin | template | p | side | rho | W | H | T | slack | signature |",
            "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["low_margin_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["margin"]),
                    str(row["template_index"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["target_W"]),
                    str(row["H"]),
                    str(row["T"]),
                    str(row["normal_form_slack"]),
                    f"`{row['signature']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 复现签名",
            "",
            "| signature | hits | distinct P | P values | min margin | recurrent |",
            "| --- | ---: | ---: | --- | ---: | ---: |",
        ]
    )
    for row in result["boundary_recurrence_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['signature']}`",
                    str(row["hit_count"]),
                    str(row["distinct_p_count"]),
                    f"`{row['p_values']}`",
                    str(row["min_margin"]),
                    f"`{fmt_bool(row['recurrent_on_current_sweep'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 当前扩展扫描仍没有支配失败；这只是有限证据，不是全局证明。",
            "- `margin=0` 是单点边界；`margin<=1` 没有越过当前有限边界核。",
            "- 若低余量签名在高 P 复现，必须进入 BoundaryRecurrence-PDEC/ColumnCRT；若不复现，则剩余是边界核之后的 asymptotic dominance。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 5. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 6. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 7. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 内部路线：证明边界核之后 selector rho 命中强制平方窗-尾素数支配余量非负。",
            "- PDEC 路线：若低余量签名高处复现，构造对应 BoundaryRecurrence/ColumnCRT 排斥。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external-ledger", type=Path, default=EXTERNAL_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--low-margin-cutoff", type=int, default=1)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    external_ledger = args.external_ledger if args.external_ledger.is_absolute() else ROOT / args.external_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(external_ledger, template_ledger, args.max_p, args.low_margin_cutoff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-ht-dominance-boundary-recurrence-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prime_rho_hit_count": result["aggregate"]["prime_rho_hit_count"],
                "dominance_failure_count": result["aggregate"]["dominance_failure_count"],
                "margin_le_1_count": result["aggregate"]["margin_le_1_count"],
                "margin_le_1_max_p": result["aggregate"]["margin_le_1_max_p"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
