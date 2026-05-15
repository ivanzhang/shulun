#!/usr/bin/env python3
"""把 lpf<=7 主层压成 3/5/7 三小模 CRT 配额门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_crt_quota_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-router.md
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

BOUNDARY_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-router.md"

SMALL_FACTOR_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_small_factor_loss_ladder_router.py"
)

MAIN_TARGET = "LPF7MainLossFloorPlusBoundarySupplementOrBoundaryAtomPDEC"
NEXT_TARGET = "LPF7CRTQuotaLowerBoundOrBoundaryEqualityAtomPDEC"


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


def lpf_count(row: dict[str, Any], prime: int) -> int:
    """读取某个最小素因子层的计数。"""
    histogram = row["least_prime_factor_histogram"]
    return int(histogram.get(prime, histogram.get(str(prime), 0)))


def enrich_quota_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> list[dict[str, Any]]:
    """重放小因子行并生成 3/5/7 配额字段。"""
    small_factor = load_module(SMALL_FACTOR_ROUTER, "lpf7_crt_small_factor")
    rows, _ = small_factor.enrich_small_factor_rows(max_p, template_ledger, target_h_coeff, [3, 5, 7])
    enriched: list[dict[str, Any]] = []
    for row in rows:
        c3 = lpf_count(row, 3)
        c5 = lpf_count(row, 5)
        c7 = lpf_count(row, 7)
        lpf7_count = c3 + c5 + c7
        required = int(row["required_composite_loss_for_breakpoint_safety"])
        enriched.append(
            {
                **row,
                "lpf3_loss_count": c3,
                "lpf5_loss_count": c5,
                "lpf7_exact_loss_count": c7,
                "lpf_le_7_loss_count": lpf7_count,
                "lpf_le_7_required_loss": required,
                "lpf_le_7_surplus_to_required_loss": lpf7_count - required,
                "lpf_le_7_covers_required_loss": lpf7_count >= required,
                "small_mod_crt_identity": "lpf(m)<=7 iff m is divisible by 3, 5, or 7, since m is odd.",
            }
        )
    return enriched


def side_rho_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 side/rho 汇总配额余量。"""
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault((str(row["side"]), int(row["rho"])), []).append(row)
    records = []
    for (side, rho), items in sorted(grouped.items()):
        min_surplus = min(int(row["lpf_le_7_surplus_to_required_loss"]) for row in items)
        records.append(
            {
                "side": side,
                "rho": rho,
                "hit_count": len(items),
                "failure_count": sum(1 for row in items if int(row["lpf_le_7_surplus_to_required_loss"]) < 0),
                "exact_count": sum(1 for row in items if int(row["lpf_le_7_surplus_to_required_loss"]) == 0),
                "min_surplus": min_surplus,
                "p_values_at_min_surplus": sorted(
                    {int(row["p"]) for row in items if int(row["lpf_le_7_surplus_to_required_loss"]) == min_surplus}
                ),
            }
        )
    return records


def tight_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出配额最紧行。"""
    selected = sorted(
        rows,
        key=lambda row: (
            int(row["lpf_le_7_surplus_to_required_loss"]),
            int(row["p"]),
            row["side"],
            int(row["rho"]),
        ),
    )
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "failure_loaded_b_breakpoint",
        "loaded_b_layers",
        "residue_cap_slot_count",
        "lpf_le_7_required_loss",
        "lpf_le_7_loss_count",
        "lpf_le_7_surplus_to_required_loss",
        "lpf3_loss_count",
        "lpf5_loss_count",
        "lpf7_exact_loss_count",
        "companion_composite_loss_count",
        "composite_loss_surplus_to_floor",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def quota_atom_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """登记失败和等号的配额原子。"""
    atoms = [
        row
        for row in rows
        if int(row["lpf_le_7_surplus_to_required_loss"]) <= 0
    ]
    return tight_examples(atoms, limit=len(atoms))


def surplus_histogram(rows: list[dict[str, Any]]) -> dict[str, int]:
    """配额余量直方图。"""
    counts = Counter(int(row["lpf_le_7_surplus_to_required_loss"]) for row in rows)
    return {str(key): counts[key] for key in sorted(counts)}


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "lpf7_three_mod_identity",
            "status": "closed",
            "statement": "Because every companion m is odd, lpf(m)<=7 is exactly the disjoint least-factor partition m divisible first by 3, then 5, then 7.",
        },
        {
            "name": "finite_lpf7_quota_atoms",
            "status": "closed_on_current_sweep",
            "statement": "On the current P>=2001 sweep, the only lpf<=7 quota failure is P=2467 minus rho=7, while exact quota equalities occur at P=5297 minus rho=2.",
        },
        {
            "name": "global_lpf7_crt_quota_lower_bound",
            "status": "open",
            "statement": "A global proof must lower-bound the 3/5/7 CRT quota in residue-cap slots or route boundary/equality atoms to PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "LPF7ThreeModIdentityClosed",
            "closed": True,
            "proved": True,
            "meaning": "`lpf<=7` 主层已化为 `3/5/7` 三小模 CRT 配额。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentLPF7QuotaFailureIsBoundary",
            "closed": agg["lpf7_quota_failure_count_at_p0"] == 1,
            "proved": False,
            "meaning": "有限重放中唯一配额失败仍是 P=2467 贴边原子。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentLPF7QuotaEqualityAtomsRegistered",
            "closed": agg["lpf7_quota_exact_count_at_p0"] == 2,
            "proved": False,
            "meaning": "有限重放中非失败等号原子为 P=5297, minus, rho=2 的两条模板记录。",
            "remaining": "finite equality atoms",
        },
        {
            "gate": "GlobalLPF7CRTQuotaLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明三小模 CRT 配额下界，或排斥边界/等号原子持久复现。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 lpf<=7 主层压成 3/5/7 配额门。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(boundary_ledger: Path, template_ledger: Path, max_p: int, p0: int, target_h_coeff: float) -> dict[str, Any]:
    """构造三小模 CRT 配额结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(boundary_ledger)
    rows = enrich_quota_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    nonboundary = [
        row
        for row in selected
        if not (int(row["p"]) == 2467 and row["side"] == "minus" and int(row["rho"]) == 7)
    ]
    exact_rows = [row for row in selected if int(row["lpf_le_7_surplus_to_required_loss"]) == 0]
    aggregate = {
        "boundary_ledger": str(boundary_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "selected_hit_count_at_p0": len(selected),
        "previous_boundary_atom_pdec_excluded": source["aggregate"]["boundary_atom_pdec_excluded"],
        "lpf7_quota_failure_count_at_p0": sum(
            1 for row in selected if int(row["lpf_le_7_surplus_to_required_loss"]) < 0
        ),
        "lpf7_quota_exact_count_at_p0": len(exact_rows),
        "min_lpf7_quota_surplus_at_p0": min(int(row["lpf_le_7_surplus_to_required_loss"]) for row in selected),
        "min_nonboundary_lpf7_quota_surplus_at_p0": min(
            int(row["lpf_le_7_surplus_to_required_loss"]) for row in nonboundary
        ),
        "total_lpf3_loss_at_p0": sum(int(row["lpf3_loss_count"]) for row in selected),
        "total_lpf5_loss_at_p0": sum(int(row["lpf5_loss_count"]) for row in selected),
        "total_lpf7_exact_loss_at_p0": sum(int(row["lpf7_exact_loss_count"]) for row in selected),
        "global_lpf7_crt_quota_lower_bound_proved": False,
        "boundary_equality_atom_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "small_moduli": [3, 5, 7],
        },
        "aggregate": aggregate,
        "side_rho_records": side_rho_records(selected),
        "quota_atom_records": quota_atom_records(selected),
        "tight_examples": tight_examples(selected),
        "surplus_histogram": surplus_histogram(selected),
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_crt_quota_router",
        "status": "lpf7_main_layer_reduced_to_three_small_mod_crt_quota_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_quota_atoms_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "side_rho_records": ledger["side_rho_records"],
        "quota_atom_records": ledger["quota_atom_records"],
        "tight_examples": ledger["tight_examples"],
        "surplus_histogram": ledger["surplus_histogram"],
        "global_lpf7_crt_quota_lower_bound_proved": False,
        "boundary_equality_atom_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_lpf7_crt_quota_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_small_factor_loss_ladder_router.py": sha256(
                SMALL_FACTOR_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-boundary-atom-ledger.json": sha256(
                boundary_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 `lpf(m)<=7` 主损耗层精确压成 `3/5/7` 三小模 CRT 配额。"
            f"当前 `P>={p0}` 重放中唯一失败仍是 `P=2467, minus, rho=7`；"
            "非边界最小余量为 0，等号原子是 `P=5297, minus, rho=2` 的两条模板记录。"
            f"三小模总支付分别为 3层 {aggregate['total_lpf3_loss_at_p0']}、"
            f"5层 {aggregate['total_lpf5_loss_at_p0']}、7层 {aggregate['total_lpf7_exact_loss_at_p0']}。"
            "严格闭合还需证明三小模 CRT 配额全局下界，并排斥边界/等号原子持久复现。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower lpf7 CRT quota router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"selected_hit_count_at_p0={agg['selected_hit_count_at_p0']}",
        f"lpf7_quota_failure_count_at_p0={agg['lpf7_quota_failure_count_at_p0']}",
        f"lpf7_quota_exact_count_at_p0={agg['lpf7_quota_exact_count_at_p0']}",
        f"min_lpf7_quota_surplus_at_p0={agg['min_lpf7_quota_surplus_at_p0']}",
        f"min_nonboundary_lpf7_quota_surplus_at_p0={agg['min_nonboundary_lpf7_quota_surplus_at_p0']}",
        f"total_lpf3_loss_at_p0={agg['total_lpf3_loss_at_p0']}",
        f"total_lpf5_loss_at_p0={agg['total_lpf5_loss_at_p0']}",
        f"total_lpf7_exact_loss_at_p0={agg['total_lpf7_exact_loss_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 三小模配额",
        "",
        "`m=P+2(b+u)` 为奇数，因此 `lpf(m)<=7` 精确等价于 `m` 被 `3`、`5` 或 `7` 整除。按最小素因子分区后三层互不重叠。",
        "",
        "## 2. side/rho 汇总",
        "",
        "| side | rho | hits | failures | exact | min surplus | p at min |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["side_rho_records"]:
        lines.append(
            f"| `{row['side']}` | {row['rho']} | {row['hit_count']} | {row['failure_count']} | "
            f"{row['exact_count']} | {row['min_surplus']} | `{row['p_values_at_min_surplus']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 失败/等号原子",
            "",
            "| p | side | rho | Bcrit | Good | cap | required | lpf<=7 | surplus | lpf3 | lpf5 | lpf7 |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["quota_atom_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["failure_loaded_b_breakpoint"]),
                    str(row["loaded_b_layers"]),
                    str(row["residue_cap_slot_count"]),
                    str(row["lpf_le_7_required_loss"]),
                    str(row["lpf_le_7_loss_count"]),
                    str(row["lpf_le_7_surplus_to_required_loss"]),
                    str(row["lpf3_loss_count"]),
                    str(row["lpf5_loss_count"]),
                    str(row["lpf7_exact_loss_count"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 最紧样本",
            "",
            "| surplus | p | side | rho | required | lpf<=7 | lpf3 | lpf5 | lpf7 | cap | Good |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tight_examples"][:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["lpf_le_7_surplus_to_required_loss"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["lpf_le_7_required_loss"]),
                    str(row["lpf_le_7_loss_count"]),
                    str(row["lpf3_loss_count"]),
                    str(row["lpf5_loss_count"]),
                    str(row["lpf7_exact_loss_count"]),
                    str(row["residue_cap_slot_count"]),
                    str(row["loaded_b_layers"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- `3` 层是主支付层，`5/7` 是补强层；三层合计才形成当前高段的主损耗安全网。",
            "- 非边界仍有等号原子，说明下一步不能只说“大多数有余量”，必须登记等号相位。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 6. 命题行",
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
            "## 7. 决策表",
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
            "## 8. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：证明 `3/5/7` 小模 CRT 配额下界；若边界或等号原子复现，则登记为 BoundaryEqualityAtom-PDEC/SAE 并排斥。",
            "",
            "## 9. 依赖哈希",
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
    parser.add_argument("--boundary-ledger", type=Path, default=BOUNDARY_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    boundary_ledger = args.boundary_ledger if args.boundary_ledger.is_absolute() else ROOT / args.boundary_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(boundary_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-lpf7-crt-quota-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "lpf7_quota_failure_count_at_p0": result["aggregate"]["lpf7_quota_failure_count_at_p0"],
                "lpf7_quota_exact_count_at_p0": result["aggregate"]["lpf7_quota_exact_count_at_p0"],
                "min_nonboundary_lpf7_quota_surplus_at_p0": result["aggregate"][
                    "min_nonboundary_lpf7_quota_surplus_at_p0"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
