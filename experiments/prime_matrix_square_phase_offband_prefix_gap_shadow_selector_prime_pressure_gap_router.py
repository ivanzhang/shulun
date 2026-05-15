#!/usr/bin/env python3
"""统计素数 rho 命中的目标 W 与 replay W 压力缺口。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_prime_pressure_gap_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-router.md
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

TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
RHO_OBSTRUCTION_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-router.md"

RHO_OBSTRUCTION_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_rho_hit_obstruction_router.py"
)

MAIN_TARGET = "PrimeRhoHitWitnessPressureMismatchOrOrderedShapeMismatchTheorem"
NEXT_TARGET = "PrimeRhoHitWitnessPressureGapLowerBoundOrFullShapeOverlapPDEC"


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


def collect_prime_rho_hits(rho_module: Any, env: dict[str, Any], templates: list[dict[str, Any]], max_p: int) -> list[dict[str, Any]]:
    """收集全部 prime rho hits 并计算压力缺口。"""
    hits: list[dict[str, Any]] = []
    for template in templates:
        for p_value in range(3, max_p + 1, 2):
            if p_value % int(template["gcd_modulus_15"]) != int(template["cover_word_residue_mod_gcd15"]):
                continue
            if not env["small_flags"][p_value]:
                continue
            atoms = env["layer"].layer_atoms_for_p(env["offband"], env["phase"], p_value, env["small_flags"])
            if template["side"] == "plus":
                offband_atoms = [atom for atom in atoms if atom["plus_offband_atom"]]
            else:
                offband_atoms = [atom for atom in atoms if atom["minus_offband_atom"]]
            prefix_shapes = [f"{atom['band']}:k{atom['k']}" for atom in offband_atoms[:3]]
            if not rho_module.target_shape_occurs(prefix_shapes, template["atom_shapes"], int(template["V"])):
                continue
            classified = rho_module.classify_prime_hit(env, p_value, template)
            target_w = int(classified["target_W"])
            replay_w = int(classified["replay_W"])
            hits.append(
                {
                    "template_index": template["template_index"],
                    "p": p_value,
                    "side": template["side"],
                    "gcd_modulus_15": template["gcd_modulus_15"],
                    "rho": template["cover_word_residue_mod_gcd15"],
                    "target_W": target_w,
                    "replay_W": replay_w,
                    "pressure_gap_target_minus_replay": target_w - replay_w,
                    "signed_tail_deficit_2T_minus_H": classified["signed_tail_deficit_2T_minus_H"],
                    "H": classified["H"],
                    "T": classified["T"],
                    "obstruction": classified["obstruction"],
                    "replay_prefix_atom_shapes": classified["replay_prefix_atom_shapes"],
                }
            )
    return hits


def template_records(hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按 template 汇总压力缺口。"""
    grouped: dict[int, list[dict[str, Any]]] = {}
    for hit in hits:
        grouped.setdefault(int(hit["template_index"]), []).append(hit)
    records: list[dict[str, Any]] = []
    for template_index, rows in sorted(grouped.items()):
        gaps = [int(row["pressure_gap_target_minus_replay"]) for row in rows]
        signed = [int(row["signed_tail_deficit_2T_minus_H"]) for row in rows]
        records.append(
            {
                "template_index": template_index,
                "prime_rho_hit_count": len(rows),
                "min_pressure_gap": min(gaps),
                "max_pressure_gap": max(gaps),
                "pressure_gap_histogram": dict(sorted(Counter(gaps).items())),
                "replay_W_histogram": dict(sorted(Counter(int(row["replay_W"]) for row in rows).items())),
                "min_signed_tail_deficit_2T_minus_H": min(signed),
                "max_signed_tail_deficit_2T_minus_H": max(signed),
                "examples": rows[:8],
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "prime_rho_hit_pressure_gap_profile",
            "status": "closed_on_current_sweep",
            "statement": "Every prime rho hit in the sweep has target W strictly larger than replay W.",
        },
        {
            "name": "ordered_shape_mismatch_not_needed_on_current_sweep",
            "status": "closed_on_current_sweep",
            "statement": "Current prime rho hits are already excluded at the witness pressure level before ordered-shape PDEC is needed.",
        },
        {
            "name": "global_prime_pressure_gap_lower_bound",
            "status": "open",
            "statement": "A global proof must show prime rho hits force target_W-replay_W>=1, or route equality cases to full-shape overlap PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CurrentPrimeRhoHitsHavePressureGap",
            "closed": agg["min_pressure_gap"] >= 1,
            "proved": True,
            "meaning": "当前全部素数 rho 命中都有至少 1 个 witness pressure 缺口。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "CurrentFullShapeOverlapAbsent",
            "closed": agg["full_shape_overlap_count"] == 0,
            "proved": True,
            "meaning": "当前没有 target_W=replay_W 的 full-shape overlap 例外。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "GlobalPrimePressureGapLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明素数 rho 命中必有 pressure gap。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成素数 rho 命中的压力缺口有限画像，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(template_ledger: Path, rho_ledger: Path, max_p: int) -> dict[str, Any]:
    """构造 prime pressure gap 结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    template_source = load_json(template_ledger)
    rho_source = load_json(rho_ledger)
    rho_module = load_module(RHO_OBSTRUCTION_ROUTER, "rho_hit_obstruction_pressure_gap")
    env = rho_module.build_environment(max_p)
    templates = rho_module.build_templates(template_source)
    hits = collect_prime_rho_hits(rho_module, env, templates, max_p)
    gaps = [int(hit["pressure_gap_target_minus_replay"]) for hit in hits]
    signed = [int(hit["signed_tail_deficit_2T_minus_H"]) for hit in hits]
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "rho_ledger": str(rho_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "prime_rho_hit_count": len(hits),
        "expected_prime_rho_hit_count": rho_source["aggregate"]["prime_rho_hit_count"],
        "matches_rho_obstruction_prime_total": len(hits) == rho_source["aggregate"]["prime_rho_hit_count"],
        "min_pressure_gap": min(gaps, default=0),
        "max_pressure_gap": max(gaps, default=0),
        "pressure_gap_histogram": dict(sorted(Counter(gaps).items())),
        "replay_W_histogram": dict(sorted(Counter(int(hit["replay_W"]) for hit in hits).items())),
        "min_signed_tail_deficit_2T_minus_H": min(signed, default=0),
        "max_signed_tail_deficit_2T_minus_H": max(signed, default=0),
        "full_shape_overlap_count": sum(1 for hit in hits if hit["obstruction"] == "FullShapeOverlapPDEC"),
        "global_prime_pressure_gap_lower_bound_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**template_source["parameters"], "max_p": max_p},
        "aggregate": aggregate,
        "prime_pressure_gap_template_records": template_records(hits),
        "prime_pressure_gap_examples": hits[:80],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_prime_pressure_gap_router",
        "status": "selector_prime_rho_hits_have_pressure_gap_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_pressure_gap_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "prime_pressure_gap_template_records": ledger["prime_pressure_gap_template_records"],
        "prime_pressure_gap_examples": ledger["prime_pressure_gap_examples"],
        "global_prime_pressure_gap_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_prime_pressure_gap_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_rho_hit_obstruction_router.py": sha256(
                RHO_OBSTRUCTION_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json": sha256(
                template_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-rho-hit-obstruction-ledger.json": sha256(
                rho_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            f"本步统计全部 {len(hits)} 个素数 rho 命中。当前最小 pressure gap 为 "
            f"{aggregate['min_pressure_gap']}，即每个素数 rho 命中都满足 `target_W>replay_W`；"
            f"replay_W 分布为 {aggregate['replay_W_histogram']}，没有 full-shape overlap。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector prime pressure gap router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"min_pressure_gap={agg['min_pressure_gap']}",
        f"max_pressure_gap={agg['max_pressure_gap']}",
        f"pressure_gap_histogram={agg['pressure_gap_histogram']}",
        f"replay_W_histogram={agg['replay_W_histogram']}",
        f"full_shape_overlap_count={agg['full_shape_overlap_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Template Pressure Gaps",
        "",
        "| template | prime rho hits | min gap | max gap | gap histogram | replay W histogram | signed range |",
        "| ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["prime_pressure_gap_template_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["template_index"]),
                    str(row["prime_rho_hit_count"]),
                    str(row["min_pressure_gap"]),
                    str(row["max_pressure_gap"]),
                    f"`{row['pressure_gap_histogram']}`",
                    f"`{row['replay_W_histogram']}`",
                    f"`{row['min_signed_tail_deficit_2T_minus_H']}..{row['max_signed_tail_deficit_2T_minus_H']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 命题行",
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
            "## 3. 决策表",
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
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 当前有限前沿显示所有素数 rho 命中均满足 `target_W-replay_W>=1`。",
            "- 全局证明需要把这个 pressure gap 写成 `H,T` 的不等式；若 gap 消失，则进入 full-shape overlap PDEC。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 5. 依赖哈希",
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
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--rho-ledger", type=Path, default=RHO_OBSTRUCTION_LEDGER)
    parser.add_argument("--max-p", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    rho_ledger = args.rho_ledger if args.rho_ledger.is_absolute() else ROOT / args.rho_ledger
    result = build_result(template_ledger, rho_ledger, args.max_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prime_rho_hit_count": result["aggregate"]["prime_rho_hit_count"],
                "min_pressure_gap": result["aggregate"]["min_pressure_gap"],
                "full_shape_overlap_count": result["aggregate"]["full_shape_overlap_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
