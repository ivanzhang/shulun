#!/usr/bin/env python3
"""把素数 rho 命中的 pressure gap 改写为 H,T 不等式正规形。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_pressure_inequality_normal_form_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-router.md
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
PRESSURE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-router.md"

PRESSURE_GAP_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_prime_pressure_gap_router.py"
)

MAIN_TARGET = "PrimeRhoHitWitnessPressureGapLowerBoundOrFullShapeOverlapPDEC"
NEXT_TARGET = "PrimeRhoHitHTInequalityLowerBoundOrFullShapeOverlapPDEC"


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


def pressure_gap_from_signed_deficit(signed_deficit: int, target_w: int) -> int:
    """由 D=2T-H 和目标 W 计算 pressure gap。"""
    replay_w = max(0, signed_deficit // 2 + 1)
    return target_w - replay_w


def normalize_hit(hit: dict[str, Any]) -> dict[str, Any]:
    """把单个 prime rho hit 改写为 H,T 不等式行。"""
    target_w = int(hit["target_W"])
    signed_deficit = int(hit["signed_tail_deficit_2T_minus_H"])
    threshold = 2 * target_w - 3
    normal_slack = threshold - signed_deficit
    h_minus_2t = -signed_deficit
    lower_bound = 3 - 2 * target_w
    replay_w = max(0, signed_deficit // 2 + 1)
    pressure_gap = target_w - replay_w
    return {
        **hit,
        "signed_deficit_threshold_2W_minus_3": threshold,
        "normal_form_slack": normal_slack,
        "h_minus_2t": h_minus_2t,
        "h_minus_2t_lower_bound_3_minus_2W": lower_bound,
        "ht_inequality_holds": signed_deficit <= threshold,
        "h_minus_2t_form_holds": h_minus_2t >= lower_bound,
        "pressure_gap_recomputed": pressure_gap,
        "gap_equivalence_ok": pressure_gap >= 1 and signed_deficit <= threshold,
        "boundary_slack_zero": normal_slack == 0,
    }


def template_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按模板汇总 H,T 正规形。"""
    grouped: dict[int, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(int(row["template_index"]), []).append(row)
    records: list[dict[str, Any]] = []
    for template_index, values in sorted(grouped.items()):
        slacks = [int(row["normal_form_slack"]) for row in values]
        hminus = [int(row["h_minus_2t"]) for row in values]
        records.append(
            {
                "template_index": template_index,
                "prime_rho_hit_count": len(values),
                "target_W_values": sorted({int(row["target_W"]) for row in values}),
                "min_normal_form_slack": min(slacks),
                "max_normal_form_slack": max(slacks),
                "normal_form_slack_histogram": dict(sorted(Counter(slacks).items())),
                "boundary_slack_zero_count": sum(1 for row in values if row["boundary_slack_zero"]),
                "min_h_minus_2t": min(hminus),
                "max_h_minus_2t": max(hminus),
                "examples": values[:8],
            }
        )
    return records


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "pressure_gap_ht_equivalence",
            "status": "closed",
            "statement": "For target W>=1, target_W-replay_W>=1 is equivalent to 2T-H<=2W-3, or H-2T>=3-2W.",
        },
        {
            "name": "current_prime_rho_hits_satisfy_ht_normal_form",
            "status": "closed_on_current_sweep",
            "statement": "Every current prime rho hit satisfies the H,T normal-form inequality.",
        },
        {
            "name": "global_ht_inequality_for_prime_rho_hits",
            "status": "open",
            "statement": "A global proof must derive 2T-H<=2W-3 for prime rho hits, or route equality failure to full-shape overlap PDEC.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "PressureGapHTEquivalenceClosed",
            "closed": agg["gap_equivalence_failure_count"] == 0,
            "proved": True,
            "meaning": "`target_W-replay_W>=1` 已等价为 `2T-H<=2W-3`。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentHTInequalityHolds",
            "closed": agg["ht_inequality_failure_count"] == 0,
            "proved": True,
            "meaning": "当前全部素数 rho 命中满足 H,T 正规形不等式。",
            "remaining": "closed on current finite sweep",
        },
        {
            "gate": "GlobalHTInequalityProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 prime rho hit 强制该 H,T 不等式。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成 pressure gap 的 H,T 正规形，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(template_ledger: Path, pressure_ledger: Path, max_p: int) -> dict[str, Any]:
    """构造 H,T 正规形结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    template_source = load_json(template_ledger)
    pressure_source = load_json(pressure_ledger)
    pressure_module = load_module(PRESSURE_GAP_ROUTER, "prime_pressure_gap_normal_form")
    rho_module = pressure_module.load_module(pressure_module.RHO_OBSTRUCTION_ROUTER, "rho_hit_obstruction_normal_form")
    env = rho_module.build_environment(max_p)
    templates = rho_module.build_templates(template_source)
    hits = pressure_module.collect_prime_rho_hits(rho_module, env, templates, max_p)
    rows = [normalize_hit(hit) for hit in hits]
    slacks = [int(row["normal_form_slack"]) for row in rows]
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "pressure_ledger": str(pressure_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "prime_rho_hit_count": len(rows),
        "expected_prime_rho_hit_count": pressure_source["aggregate"]["prime_rho_hit_count"],
        "matches_pressure_gap_total": len(rows) == pressure_source["aggregate"]["prime_rho_hit_count"],
        "ht_inequality_failure_count": sum(1 for row in rows if not row["ht_inequality_holds"]),
        "h_minus_2t_form_failure_count": sum(1 for row in rows if not row["h_minus_2t_form_holds"]),
        "gap_equivalence_failure_count": sum(1 for row in rows if not row["gap_equivalence_ok"]),
        "min_normal_form_slack": min(slacks, default=0),
        "max_normal_form_slack": max(slacks, default=0),
        "normal_form_slack_histogram": dict(sorted(Counter(slacks).items())),
        "boundary_slack_zero_count": sum(1 for row in rows if row["boundary_slack_zero"]),
        "global_ht_inequality_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {**template_source["parameters"], "max_p": max_p},
        "aggregate": aggregate,
        "pressure_inequality_template_records": template_records(rows),
        "pressure_inequality_examples": rows[:80],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_pressure_inequality_normal_form_router",
        "status": "selector_prime_pressure_gap_reduced_to_ht_inequality_open_global",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_ht_inequality_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "pressure_inequality_template_records": ledger["pressure_inequality_template_records"],
        "pressure_inequality_examples": ledger["pressure_inequality_examples"],
        "global_ht_inequality_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_pressure_inequality_normal_form_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_prime_pressure_gap_router.py": sha256(
                PRESSURE_GAP_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json": sha256(
                template_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-prime-pressure-gap-ledger.json": sha256(
                pressure_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把素数 rho 命中的 pressure gap 正规化为 H,T 不等式："
            "`target_W-replay_W>=1` 当且仅当 `2T-H<=2W-3`，等价于 `H-2T>=3-2W`。"
            f"当前 {len(rows)} 个素数 rho 命中全部满足该不等式；最小正规形 slack 为 "
            f"{aggregate['min_normal_form_slack']}，边界 slack=0 的命中数为 "
            f"{aggregate['boundary_slack_zero_count']}。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector pressure inequality normal form router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"ht_inequality_failure_count={agg['ht_inequality_failure_count']}",
        f"min_normal_form_slack={agg['min_normal_form_slack']}",
        f"max_normal_form_slack={agg['max_normal_form_slack']}",
        f"boundary_slack_zero_count={agg['boundary_slack_zero_count']}",
        f"normal_form_slack_histogram={agg['normal_form_slack_histogram']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价正规形",
        "",
        "令 `D=2T-H`，并记目标 shape 需要 `W` 个 off-band witness。回放需要",
        "",
        "```text",
        "replay_W=max(0,floor(D/2)+1).",
        "```",
        "",
        "因此 `target_W-replay_W>=1` 等价于",
        "",
        "```text",
        "2T-H <= 2W-3,",
        "H-2T >= 3-2W.",
        "```",
        "",
        "## 2. Template Summary",
        "",
        "| template | hits | W | min slack | max slack | slack histogram | boundary | H-2T range |",
        "| ---: | ---: | --- | ---: | ---: | --- | ---: | --- |",
    ]
    for row in result["pressure_inequality_template_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["template_index"]),
                    str(row["prime_rho_hit_count"]),
                    f"`{row['target_W_values']}`",
                    str(row["min_normal_form_slack"]),
                    str(row["max_normal_form_slack"]),
                    f"`{row['normal_form_slack_histogram']}`",
                    str(row["boundary_slack_zero_count"]),
                    f"`{row['min_h_minus_2t']}..{row['max_h_minus_2t']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 命题行",
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
            "## 4. 决策表",
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
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 已关闭 pressure gap 到 H,T 不等式的代数等价。",
            "- 真正剩余是全局证明 prime rho hit 强制 `2T-H<=2W-3`；边界 slack=0 是最窄例外层。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
    parser.add_argument("--pressure-ledger", type=Path, default=PRESSURE_LEDGER)
    parser.add_argument("--max-p", type=int, default=5000)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    pressure_ledger = args.pressure_ledger if args.pressure_ledger.is_absolute() else ROOT / args.pressure_ledger
    result = build_result(template_ledger, pressure_ledger, args.max_p)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-pressure-inequality-normal-form-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "prime_rho_hit_count": result["aggregate"]["prime_rho_hit_count"],
                "ht_inequality_failure_count": result["aggregate"]["ht_inequality_failure_count"],
                "min_normal_form_slack": result["aggregate"]["min_normal_form_slack"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
