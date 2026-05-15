#!/usr/bin/env python3
"""把 H 下界相关余量压成 GoodShell 断点层容量问题。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

CORRELATION_LEDGER = (
    DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-ledger.json"
)
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-router.md"

CORRELATION_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_effective_capacity_correlation_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "SelectorLowSurvivorGoodShellCorrelatedSurplusOrNearFullEffectiveTilingPDEC"
NEXT_TARGET = "SelectorGoodShellLoadedBLayerBreakpointUpperBoundOrLayerPrimePairPDEC"


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


def required_integer_h(p_value: int, target_h_coeff: float) -> tuple[float, int]:
    """返回实数目标与通过所需的最小整数 H。"""
    target_real = target_h_coeff * p_value / math.log(p_value)
    nearest = round(target_real)
    if abs(target_real - nearest) < 1e-12:
        return target_real, int(nearest)
    return target_real, math.floor(target_real) + 1


def layer_interval_length_certificate(p_value: int) -> dict[str, Any]:
    """给出固定 b 层至多一个 u 的通用证书。"""
    return {
        "reason": "For alpha=4/5, q=P-2b>4P/5 and the half-grid interval has length at most (P-1)/(2q)<5/8.",
        "p": p_value,
        "strict_upper_bound": (p_value - 1) / (2 * (4 * p_value / 5)),
        "unit_capacity_closed": True,
    }


def enrich_breakpoint_rows(
    max_p: int,
    template_ledger: Path,
    target_h_coeff: float,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放 H 相关余量行并加入断点/层容量字段。"""
    correlation = load_module(CORRELATION_ROUTER, "breakpoint_correlation")
    even = load_module(EVEN_LAYER_ROUTER, "breakpoint_even_layer")
    base_rows, replay = correlation.enrich_rows(max_p, template_ledger, target_h_coeff)
    prime_flags = even.sieve(2 * max_p + 1000)
    rows: list[dict[str, Any]] = []
    layer_failures: list[dict[str, Any]] = []
    for base in base_rows:
        p_value = int(base["p"])
        side = str(base["side"])
        candidates = even.candidate_slots(p_value, side, prime_flags)
        per_b: dict[int, int] = {}
        per_u: dict[int, int] = {}
        for item in candidates:
            per_b[int(item["b"])] = per_b.get(int(item["b"]), 0) + 1
            per_u[int(item["u"])] = per_u.get(int(item["u"]), 0) + 1
        max_b_layer_load = max(per_b.values(), default=0)
        loaded_b_layers = len(per_b)
        good_value = int(base["good_effective_slot_count"])
        unit_capacity_ok = max_b_layer_load <= 1 and loaded_b_layers == good_value == len(candidates)
        if not unit_capacity_ok:
            layer_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "good_effective_slot_count": good_value,
                    "candidate_count": len(candidates),
                    "loaded_b_layers": loaded_b_layers,
                    "max_b_layer_load": max_b_layer_load,
                }
            )
        target_real, required_h = required_integer_h(p_value, target_h_coeff)
        low_value = int(base["low_survivors"])
        failure_breakpoint = low_value - required_h + 1
        breakpoint_shortage = failure_breakpoint - loaded_b_layers
        rows.append(
            {
                **base,
                "target_real_H": target_real,
                "required_integer_H": required_h,
                "H_integer_passes_target": int(base["H"]) >= required_h,
                "failure_loaded_b_breakpoint": failure_breakpoint,
                "loaded_b_layers": loaded_b_layers,
                "loaded_u_layers": len(per_u),
                "max_b_layer_load": max_b_layer_load,
                "max_u_layer_load": max(per_u.values(), default=0),
                "unit_b_layer_capacity_ok": unit_capacity_ok,
                "breakpoint_shortage_to_failure": breakpoint_shortage,
                "breakpoint_reached": breakpoint_shortage <= 0,
                "loaded_b_scaled_coeff": loaded_b_layers * math.log(p_value) / p_value,
                "breakpoint_scaled_coeff": failure_breakpoint * math.log(p_value) / p_value,
                "breakpoint_shortage_scaled_coeff": breakpoint_shortage * math.log(p_value) / p_value,
            }
        )
    replay["layer_failures"] = layer_failures
    return rows, replay


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总断点距离。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        if not selected:
            records.append({"p_lo": lo, "p_hi": hi, "hit_count": 0})
            continue
        min_shortage = min(int(row["breakpoint_shortage_to_failure"]) for row in selected)
        max_loaded_coeff = max(float(row["loaded_b_scaled_coeff"]) for row in selected)
        max_breakpoint_coeff = max(float(row["breakpoint_scaled_coeff"]) for row in selected)
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "min_breakpoint_shortage_to_failure": min_shortage,
                "shortage_le_1_count": sum(1 for row in selected if int(row["breakpoint_shortage_to_failure"]) <= 1),
                "shortage_le_2_count": sum(1 for row in selected if int(row["breakpoint_shortage_to_failure"]) <= 2),
                "shortage_le_5_count": sum(1 for row in selected if int(row["breakpoint_shortage_to_failure"]) <= 5),
                "shortage_le_10_count": sum(1 for row in selected if int(row["breakpoint_shortage_to_failure"]) <= 10),
                "max_loaded_b_scaled_coeff": max_loaded_coeff,
                "max_breakpoint_scaled_coeff": max_breakpoint_coeff,
                "max_b_layer_load": max(int(row["max_b_layer_load"]) for row in selected),
                "max_u_layer_load": max(int(row["max_u_layer_load"]) for row in selected),
                "p_values_at_min_shortage": sorted(
                    {int(row["p"]) for row in selected if int(row["breakpoint_shortage_to_failure"]) == min_shortage}
                ),
            }
        )
    return records


def tight_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出最接近破坏断点的样本。"""
    selected = sorted(rows, key=lambda row: (int(row["breakpoint_shortage_to_failure"]), int(row["p"]), row["side"]))
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "target_W",
        "H",
        "required_integer_H",
        "low_survivors",
        "good_effective_slot_count",
        "failure_loaded_b_breakpoint",
        "loaded_b_layers",
        "breakpoint_shortage_to_failure",
        "max_b_layer_load",
        "max_u_layer_load",
        "loaded_b_scaled_coeff",
        "breakpoint_scaled_coeff",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_b_unit_capacity",
            "status": "closed",
            "statement": "For alpha=4/5, each fixed b layer contains at most one admissible u, hence at most one GoodShell slot.",
        },
        {
            "name": "h_lower_failure_breakpoint_equivalence",
            "status": "closed",
            "statement": "H>=0.43P/logP fails iff loaded GoodShell b-layers reach LowSurvivors-ceil(0.43P/logP)+1.",
        },
        {
            "name": "current_breakpoint_not_reached",
            "status": "closed_on_current_sweep",
            "statement": "The current selector sweep never reaches the loaded-b breakpoint; the closest row misses it by one layer.",
        },
        {
            "name": "global_loaded_b_layer_upper_bound",
            "status": "open",
            "statement": "A global proof must bound the number of loaded b layers below the breakpoint, or route persistent excess to LayerPrimePairPDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FixedBUnitCapacityClosed",
            "closed": agg["unit_b_layer_capacity_failure_count"] == 0,
            "proved": True,
            "meaning": "固定 b 层由长度 <1 的 u 区间控制，至多贡献一个 GoodShell 槽。",
            "remaining": "closed",
        },
        {
            "gate": "BreakpointEquivalenceClosed",
            "closed": True,
            "proved": True,
            "meaning": "H 下界失败等价于 loaded b 层数达到整数断点。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentBreakpointNotReached",
            "closed": agg["breakpoint_reached_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中断点未被达到；最紧处只差一层。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalLoadedBLayerUpperBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 loaded b 层数低于断点。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把破坏输入压成 distinct-b 素对层数量上界。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    correlation_ledger: Path,
    template_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
) -> dict[str, Any]:
    """构造断点层容量结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(correlation_ledger)
    rows, replay = enrich_breakpoint_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    min_shortage = min(int(row["breakpoint_shortage_to_failure"]) for row in selected)
    aggregate = {
        "correlation_ledger": str(correlation_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "prime_rho_hit_count": len(rows),
        "selected_hit_count_at_p0": len(selected),
        "previous_identity_failure_count": source["aggregate"]["identity_failure_count"],
        "formula_failure_count": len(replay["formula_failures"]),
        "identity_failure_count": len(replay["identity_failures"]),
        "unit_b_layer_capacity_failure_count": len(replay["layer_failures"]),
        "breakpoint_reached_count_at_p0": sum(1 for row in selected if bool(row["breakpoint_reached"])),
        "min_breakpoint_shortage_to_failure_at_p0": min_shortage,
        "shortage_le_1_count_at_p0": sum(1 for row in selected if int(row["breakpoint_shortage_to_failure"]) <= 1),
        "shortage_le_10_count_at_p0": sum(1 for row in selected if int(row["breakpoint_shortage_to_failure"]) <= 10),
        "max_loaded_b_scaled_coeff_at_p0": max(float(row["loaded_b_scaled_coeff"]) for row in selected),
        "max_breakpoint_scaled_coeff_at_p0": max(float(row["breakpoint_scaled_coeff"]) for row in selected),
        "max_b_layer_load_at_p0": max(int(row["max_b_layer_load"]) for row in selected),
        "max_u_layer_load_at_p0": max(int(row["max_u_layer_load"]) for row in selected),
        "global_loaded_b_layer_upper_bound_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "alpha_cutoff": "floor(4P/5)",
        },
        "aggregate": aggregate,
        "unit_capacity_certificate": layer_interval_length_certificate(p0),
        "band_records": band_records(rows, [(3, 2000), (2001, 5000), (5001, max_p)]),
        "tight_examples": tight_examples(selected),
        "layer_failures": replay["layer_failures"],
        "identity_failures": replay["identity_failures"],
        "formula_failures": replay["formula_failures"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router",
        "status": "h_lower_breakpoint_reduced_to_loaded_b_layer_upper_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_breakpoint_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "unit_capacity_certificate": ledger["unit_capacity_certificate"],
        "band_records": ledger["band_records"],
        "tight_examples": ledger["tight_examples"],
        "global_loaded_b_layer_upper_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_effective_capacity_correlation_router.py": sha256(
                CORRELATION_ROUTER
            ),
            "experiments/prime_matrix_square_phase_even_layer_interval_router.py": sha256(EVEN_LAYER_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-ledger.json": sha256(
                correlation_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 H 下界失败写成整数断点：失败当且仅当 GoodShell 的 loaded b 层数达到 "
            "`LowSurvivors-ceil(0.43P/logP)+1`。由于 `alpha=4/5` 时固定 b 层的 u 区间长度 "
            "<1，每层至多一个 GoodShell 槽，所以 GoodShell 计数就是 distinct loaded-b 层数。"
            f"当前 `P>={p0}` 重放没有达到断点，最小缺口为 {aggregate['min_breakpoint_shortage_to_failure_at_p0']} 层；"
            "全局剩余是证明 loaded-b 素对层数永远低于该断点，或把达到断点的持久层素对过密抽成 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    cert = result["unit_capacity_certificate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower breakpoint layer capacity router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"target_h_coeff={agg['target_h_coeff']}",
        f"prime_rho_hit_count={agg['prime_rho_hit_count']}",
        f"unit_b_layer_capacity_failure_count={agg['unit_b_layer_capacity_failure_count']}",
        f"breakpoint_reached_count_at_p0={agg['breakpoint_reached_count_at_p0']}",
        f"min_breakpoint_shortage_to_failure_at_p0={agg['min_breakpoint_shortage_to_failure_at_p0']}",
        f"shortage_le_1_count_at_p0={agg['shortage_le_1_count_at_p0']}",
        f"max_b_layer_load_at_p0={agg['max_b_layer_load_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 整数断点",
        "",
        "令",
        "",
        "```text",
        "R(P)=ceil(0.43P/logP)",
        "Bcrit(P,side)=LowSurvivors(P,side)-R(P)+1.",
        "```",
        "",
        "因为 `H=LowSurvivors-GoodShell` 且 `H` 为整数，所以",
        "",
        "```text",
        "H>=0.43P/logP fails  <=>  GoodShell >= Bcrit.",
        "```",
        "",
        "再由固定 b 层单位容量，`GoodShell` 等于 loaded b 层数。",
        "",
        "## 2. 单位容量证书",
        "",
        f"- {cert['reason']}",
        f"- 在 `P={cert['p']}` 处的通用上界样本：`{cert['strict_upper_bound']}`。",
        "",
        "## 3. P 区间账本",
        "",
        "| P range | hits | min shortage | <=1 | <=2 | <=5 | <=10 | max loaded coeff | max breakpoint coeff | max b-load | max u-load | p at min shortage |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row.get("min_breakpoint_shortage_to_failure")),
                    str(row.get("shortage_le_1_count")),
                    str(row.get("shortage_le_2_count")),
                    str(row.get("shortage_le_5_count")),
                    str(row.get("shortage_le_10_count")),
                    str(row.get("max_loaded_b_scaled_coeff")),
                    str(row.get("max_breakpoint_scaled_coeff")),
                    str(row.get("max_b_layer_load")),
                    str(row.get("max_u_layer_load")),
                    f"`{row.get('p_values_at_min_shortage')}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 最紧样本",
            "",
            "| shortage | template | p | side | rho | W | H | R(P) | Low | Good | Bcrit | loaded b | max b-load | max u-load | loaded coeff | breakpoint coeff |",
            "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tight_examples"][:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["breakpoint_shortage_to_failure"]),
                    str(row["template_index"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["target_W"]),
                    str(row["H"]),
                    str(row["required_integer_H"]),
                    str(row["low_survivors"]),
                    str(row["good_effective_slot_count"]),
                    str(row["failure_loaded_b_breakpoint"]),
                    str(row["loaded_b_layers"]),
                    str(row["max_b_layer_load"]),
                    str(row["max_u_layer_load"]),
                    str(row["loaded_b_scaled_coeff"]),
                    str(row["breakpoint_scaled_coeff"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 破坏输入已从 `GoodShell` 总量改写为 distinct `b` 层素对数量。",
            "- 固定 `b` 层不能提供多重容量；若达到断点，只能是许多不同 `b` 层同时产生素对。",
            "- 最紧样本 `P=2467, minus, rho=7` 只差一个 loaded b 层会触发 H 门失败，这是下一步应直接排斥的原子形态。",
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
            "- 具体目标：证明 distinct loaded-b prime-pair layers 低于 `Bcrit`，或把达到断点的层素对过密写成固定 b/u 相位 PDEC/SAE。",
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
    parser.add_argument("--correlation-ledger", type=Path, default=CORRELATION_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    correlation_ledger = (
        args.correlation_ledger if args.correlation_ledger.is_absolute() else ROOT / args.correlation_ledger
    )
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(correlation_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "p0": args.p0,
                "unit_b_layer_capacity_failure_count": result["aggregate"]["unit_b_layer_capacity_failure_count"],
                "breakpoint_reached_count_at_p0": result["aggregate"]["breakpoint_reached_count_at_p0"],
                "min_breakpoint_shortage_to_failure_at_p0": result["aggregate"][
                    "min_breakpoint_shortage_to_failure_at_p0"
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
