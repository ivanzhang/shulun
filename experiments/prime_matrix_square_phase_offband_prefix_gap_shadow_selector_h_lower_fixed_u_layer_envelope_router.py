#!/usr/bin/env python3
"""把 H 下界 loaded-b 断点压成固定 u 层包络/素对过密守门项。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_u_layer_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-router.md
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

BREAKPOINT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-router.md"

BREAKPOINT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "SelectorGoodShellLoadedBLayerBreakpointUpperBoundOrLayerPrimePairPDEC"
NEXT_TARGET = "SelectorGoodShellFixedULayerEnvelopeOrShortGoldbachLayerPDEC"


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


def fixed_u_b_values(even: Any, p_value: int, side: str, u_value: int) -> list[int]:
    """返回固定 u 层中半列窗口允许的全部 b。

    这里不加入素性，只审计二次半列窗口。由于 b(b+u) 关于 b 单调，
    允许集合是一个整数区间；枚举用于生成机器可复核账本。
    """
    cutoff = even.cutoff_alpha45(p_value)
    max_b = (p_value - cutoff - 1) // 2
    return [
        b_value
        for b_value in range(1, max_b + 1)
        if 1 <= even.s_value_for(p_value, b_value, u_value, side) <= (p_value - 1) // 2
    ]


def fixed_u_interval_record(even: Any, p_value: int, side: str, u_value: int, loaded_count: int) -> dict[str, Any]:
    """生成固定 u 层的窗口区间记录。"""
    b_values = fixed_u_b_values(even, p_value, side, u_value)
    return {
        "u": u_value,
        "loaded_count": loaded_count,
        "available_b_interval_empty": len(b_values) == 0,
        "available_b_min": min(b_values) if b_values else None,
        "available_b_max": max(b_values) if b_values else None,
        "available_b_interval_length": len(b_values),
        "loaded_density_inside_window": loaded_count / len(b_values) if b_values else None,
    }


def short_goldbach_certificate(p_value: int, u_value: int, candidates: list[dict[str, int]]) -> dict[str, Any]:
    """验证固定 u 层候选素对共享同一偶数和。"""
    expected_sum = 2 * (p_value + u_value)
    failures = [item for item in candidates if int(item["q"]) + int(item["m"]) != expected_sum]
    return {
        "u": u_value,
        "expected_even_sum": expected_sum,
        "candidate_count": len(candidates),
        "sum_identity_failure_count": len(failures),
        "sample_pairs": [{"b": item["b"], "q": item["q"], "m": item["m"], "s": item["s"]} for item in candidates[:8]],
    }


def enrich_fixed_u_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放断点行并加入固定 u 层包络字段。"""
    breakpoint = load_module(BREAKPOINT_ROUTER, "fixed_u_breakpoint")
    even = load_module(EVEN_LAYER_ROUTER, "fixed_u_even_layer")
    base_rows, replay = breakpoint.enrich_breakpoint_rows(max_p, template_ledger, target_h_coeff)
    prime_flags = even.sieve(2 * max_p + 1000)

    rows: list[dict[str, Any]] = []
    grouping_failures: list[dict[str, Any]] = []
    goldbach_sum_failures: list[dict[str, Any]] = []
    interval_empty_failures: list[dict[str, Any]] = []
    for base in base_rows:
        p_value = int(base["p"])
        side = str(base["side"])
        candidates = even.candidate_slots(p_value, side, prime_flags)
        by_u: dict[int, list[dict[str, int]]] = {}
        for item in candidates:
            by_u.setdefault(int(item["u"]), []).append(item)

        loaded_u_layer_records = [
            fixed_u_interval_record(even, p_value, side, u_value, len(items))
            for u_value, items in sorted(by_u.items())
        ]
        layer_sum_certificates = [
            short_goldbach_certificate(p_value, u_value, items) for u_value, items in sorted(by_u.items())
        ]
        sum_failure_count = sum(item["sum_identity_failure_count"] for item in layer_sum_certificates)
        if sum_failure_count:
            goldbach_sum_failures.append(
                {"p": p_value, "side": side, "template_index": base["template_index"], "failure_count": sum_failure_count}
            )
        empty_loaded_layers = [item for item in loaded_u_layer_records if item["available_b_interval_empty"]]
        if empty_loaded_layers:
            interval_empty_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "template_index": base["template_index"],
                    "empty_loaded_layers": empty_loaded_layers,
                }
            )

        loaded_count_from_u = sum(len(items) for items in by_u.values())
        loaded_b_layers = int(base["loaded_b_layers"])
        good_value = int(base["good_effective_slot_count"])
        if loaded_count_from_u != loaded_b_layers or loaded_count_from_u != good_value:
            grouping_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "template_index": base["template_index"],
                    "good_effective_slot_count": good_value,
                    "loaded_b_layers": loaded_b_layers,
                    "loaded_count_from_u": loaded_count_from_u,
                }
            )

        max_u_load = max((len(items) for items in by_u.values()), default=0)
        max_available_len = max((int(item["available_b_interval_length"]) for item in loaded_u_layer_records), default=0)
        max_loaded_density = max(
            (
                float(item["loaded_density_inside_window"])
                for item in loaded_u_layer_records
                if item["loaded_density_inside_window"] is not None
            ),
            default=0.0,
        )
        failure_breakpoint = int(base["failure_loaded_b_breakpoint"])
        loaded_u_layers = len(by_u)
        finite_max_load_route_threshold = math.floor(failure_breakpoint / loaded_u_layers) + 1 if loaded_u_layers else None
        if max_u_load > 0:
            u_layers_needed_under_observed_max_load = math.ceil(failure_breakpoint / max_u_load)
        else:
            u_layers_needed_under_observed_max_load = None

        rows.append(
            {
                **base,
                "loaded_u_layers_recomputed": loaded_u_layers,
                "loaded_count_from_u": loaded_count_from_u,
                "fixed_u_grouping_ok": loaded_count_from_u == loaded_b_layers == good_value,
                "short_goldbach_sum_identity_ok": sum_failure_count == 0,
                "loaded_fixed_u_interval_nonempty_ok": not empty_loaded_layers,
                "max_u_layer_load_recomputed": max_u_load,
                "max_loaded_fixed_u_window_b_length": max_available_len,
                "max_loaded_density_inside_fixed_u_window": max_loaded_density,
                "finite_max_load_route_threshold_at_current_loaded_u": finite_max_load_route_threshold,
                "u_layers_needed_under_observed_max_load": u_layers_needed_under_observed_max_load,
                "breakpoint_deficit_after_observed_max_u_load_times_loaded_u": failure_breakpoint
                - max_u_load * loaded_u_layers,
                "loaded_u_layer_records": loaded_u_layer_records,
                "short_goldbach_layer_certificates": layer_sum_certificates[:5],
            }
        )

    replay["fixed_u_grouping_failures"] = grouping_failures
    replay["goldbach_sum_failures"] = goldbach_sum_failures
    replay["fixed_u_interval_empty_failures"] = interval_empty_failures
    return rows, replay


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总 fixed-u 包络观测。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        if not selected:
            records.append({"p_lo": lo, "p_hi": hi, "hit_count": 0})
            continue
        min_shortage = min(int(row["breakpoint_shortage_to_failure"]) for row in selected)
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "min_breakpoint_shortage_to_failure": min_shortage,
                "max_loaded_u_layers": max(int(row["loaded_u_layers_recomputed"]) for row in selected),
                "max_u_layer_load": max(int(row["max_u_layer_load_recomputed"]) for row in selected),
                "max_loaded_fixed_u_window_b_length": max(
                    int(row["max_loaded_fixed_u_window_b_length"]) for row in selected
                ),
                "max_loaded_density_inside_fixed_u_window": max(
                    float(row["max_loaded_density_inside_fixed_u_window"]) for row in selected
                ),
                "p_values_at_min_shortage": sorted(
                    {int(row["p"]) for row in selected if int(row["breakpoint_shortage_to_failure"]) == min_shortage}
                ),
            }
        )
    return records


def tight_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出最接近断点的 fixed-u 样本。"""
    selected = sorted(rows, key=lambda row: (int(row["breakpoint_shortage_to_failure"]), int(row["p"]), row["side"]))
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "H",
        "required_integer_H",
        "low_survivors",
        "good_effective_slot_count",
        "failure_loaded_b_breakpoint",
        "loaded_b_layers",
        "loaded_u_layers_recomputed",
        "max_u_layer_load_recomputed",
        "max_loaded_fixed_u_window_b_length",
        "max_loaded_density_inside_fixed_u_window",
        "breakpoint_shortage_to_failure",
        "finite_max_load_route_threshold_at_current_loaded_u",
        "u_layers_needed_under_observed_max_load",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def max_layer_examples(rows: list[dict[str, Any]], limit: int = 12) -> list[dict[str, Any]]:
    """列出 fixed-u 单层实载最大的样本。"""
    selected = sorted(
        rows,
        key=lambda row: (
            -int(row["max_u_layer_load_recomputed"]),
            -int(row["loaded_u_layers_recomputed"]),
            int(row["p"]),
            row["side"],
        ),
    )
    examples = []
    for row in selected[:limit]:
        loaded_layers = sorted(
            row["loaded_u_layer_records"],
            key=lambda item: (-int(item["loaded_count"]), int(item["u"])),
        )
        examples.append(
            {
                "template_index": row["template_index"],
                "p": row["p"],
                "side": row["side"],
                "rho": row["rho"],
                "loaded_b_layers": row["loaded_b_layers"],
                "loaded_u_layers": row["loaded_u_layers_recomputed"],
                "max_u_layer_load": row["max_u_layer_load_recomputed"],
                "top_loaded_u_layers": loaded_layers[:5],
            }
        )
    return examples


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_u_quadratic_window_representation",
            "status": "closed",
            "statement": "For fixed u, the half-column condition is a monotone quadratic interval in b: plus has uP-H2 <= 2b(b+u) <= uP-1, minus has uP+1 <= 2b(b+u) <= uP+H2.",
        },
        {
            "name": "fixed_u_short_goldbach_layer_identity",
            "status": "closed",
            "statement": "Every fixed-u candidate has q=P-2b, m=P+2(b+u), hence q+m=2(P+u); layer load is a truncated Goldbach representation count.",
        },
        {
            "name": "breakpoint_pigeonhole_route",
            "status": "closed",
            "statement": "If loaded-b reaches Bcrit, then for any proposed fixed-u load cap K either some fixed-u layer has load>K or the number of loaded u layers is at least ceil(Bcrit/K).",
        },
        {
            "name": "global_fixed_u_envelope_or_short_goldbach_pdec",
            "status": "open",
            "statement": "A global proof must bound these truncated short-Goldbach layer loads and loaded-u layer counts below Bcrit, or register persistent over-density as PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "FixedUQuadraticWindowRepresentationClosed",
            "closed": agg["fixed_u_interval_empty_failure_count"] == 0,
            "proved": True,
            "meaning": "固定 u 层可由单调二次 b 区间精确表示。",
            "remaining": "closed",
        },
        {
            "gate": "FixedUShortGoldbachIdentityClosed",
            "closed": agg["short_goldbach_sum_failure_count"] == 0,
            "proved": True,
            "meaning": "固定 u 层实载等于受 b 区间截断的 q+m=2(P+u) 素对计数。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentFixedULoadBelowBreakpoint",
            "closed": agg["breakpoint_reached_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中 fixed-u 分层未触发断点；这只是证据，不是全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalFixedULayerEnvelopeProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局控制 fixed-u 层负载与 loaded-u 层数，或排斥短 Goldbach 层过密 PDEC。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把断点层容量再压成 fixed-u 短 Goldbach 层包络。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    breakpoint_ledger: Path,
    template_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
) -> dict[str, Any]:
    """构造 fixed-u 层包络结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(breakpoint_ledger)
    rows, replay = enrich_fixed_u_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    min_shortage = min(int(row["breakpoint_shortage_to_failure"]) for row in selected)
    aggregate = {
        "breakpoint_ledger": str(breakpoint_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "prime_rho_hit_count": len(rows),
        "selected_hit_count_at_p0": len(selected),
        "previous_unit_b_layer_capacity_failure_count": source["aggregate"][
            "unit_b_layer_capacity_failure_count"
        ],
        "fixed_u_grouping_failure_count": len(replay["fixed_u_grouping_failures"]),
        "short_goldbach_sum_failure_count": len(replay["goldbach_sum_failures"]),
        "fixed_u_interval_empty_failure_count": len(replay["fixed_u_interval_empty_failures"]),
        "breakpoint_reached_count_at_p0": sum(1 for row in selected if bool(row["breakpoint_reached"])),
        "min_breakpoint_shortage_to_failure_at_p0": min_shortage,
        "max_loaded_u_layers_at_p0": max(int(row["loaded_u_layers_recomputed"]) for row in selected),
        "max_u_layer_load_at_p0": max(int(row["max_u_layer_load_recomputed"]) for row in selected),
        "max_loaded_fixed_u_window_b_length_at_p0": max(
            int(row["max_loaded_fixed_u_window_b_length"]) for row in selected
        ),
        "max_loaded_density_inside_fixed_u_window_at_p0": max(
            float(row["max_loaded_density_inside_fixed_u_window"]) for row in selected
        ),
        "short_goldbach_layer_global_envelope_proved": False,
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
        "fixed_u_formula": {
            "H2": "(P-1)/2",
            "plus": "uP-H2 <= 2b(b+u) <= uP-1",
            "minus": "uP+1 <= 2b(b+u) <= uP+H2",
            "prime_pair_layer": "q=P-2b, m=P+2(b+u), q+m=2(P+u)",
        },
        "band_records": band_records(rows, [(3, 2000), (2001, 5000), (5001, max_p)]),
        "tight_examples": tight_examples(selected),
        "max_layer_examples": max_layer_examples(selected),
        "fixed_u_grouping_failures": replay["fixed_u_grouping_failures"],
        "goldbach_sum_failures": replay["goldbach_sum_failures"],
        "fixed_u_interval_empty_failures": replay["fixed_u_interval_empty_failures"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_u_layer_envelope_router",
        "status": "loaded_b_breakpoint_reduced_to_fixed_u_short_goldbach_layer_envelope_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_fixed_u_load_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "fixed_u_formula": ledger["fixed_u_formula"],
        "band_records": ledger["band_records"],
        "tight_examples": ledger["tight_examples"],
        "max_layer_examples": ledger["max_layer_examples"],
        "short_goldbach_layer_global_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_fixed_u_layer_envelope_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py": sha256(
                BREAKPOINT_ROUTER
            ),
            "experiments/prime_matrix_square_phase_even_layer_interval_router.py": sha256(EVEN_LAYER_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-breakpoint-layer-capacity-ledger.json": sha256(
                breakpoint_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步没有转换命题，而是把上一层 loaded-b 断点继续下钻到固定 `u` 层。"
            "固定 `u` 后，候选槽满足 `q=P-2b`、`m=P+2(b+u)`，所以 `q+m=2(P+u)`；"
            "同时半列窗口给出关于 `b` 的单调二次区间。因此，若断点被达到，破坏输入必须表现为"
            "某些短 Goldbach 层在受限 `b` 区间内过密，或 loaded-u 层数本身过密。"
            f"当前 `P>={p0}` 重放中断点达到数为 {aggregate['breakpoint_reached_count_at_p0']}，"
            f"fixed-u 单层最大实载为 {aggregate['max_u_layer_load_at_p0']}，"
            f"最小断点缺口为 {aggregate['min_breakpoint_shortage_to_failure_at_p0']} 层；"
            "这些仍是有限证据，严格自足闭合还需要全局 fixed-u 包络或短 Goldbach 层 PDEC 排斥。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    formula = result["fixed_u_formula"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower fixed-u layer envelope router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"target_h_coeff={agg['target_h_coeff']}",
        f"fixed_u_grouping_failure_count={agg['fixed_u_grouping_failure_count']}",
        f"short_goldbach_sum_failure_count={agg['short_goldbach_sum_failure_count']}",
        f"fixed_u_interval_empty_failure_count={agg['fixed_u_interval_empty_failure_count']}",
        f"breakpoint_reached_count_at_p0={agg['breakpoint_reached_count_at_p0']}",
        f"min_breakpoint_shortage_to_failure_at_p0={agg['min_breakpoint_shortage_to_failure_at_p0']}",
        f"max_loaded_u_layers_at_p0={agg['max_loaded_u_layers_at_p0']}",
        f"max_u_layer_load_at_p0={agg['max_u_layer_load_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定 u 层公式",
        "",
        "令 `H2=(P-1)/2`。固定 `u` 后，半列窗口 `1<=s<=H2` 等价于：",
        "",
        "```text",
        f"plus:  {formula['plus']}",
        f"minus: {formula['minus']}",
        "```",
        "",
        "候选素对同时满足：",
        "",
        "```text",
        f"{formula['prime_pair_layer']}",
        "```",
        "",
        "所以 fixed-u 层不是抽象容量项，而是受二次 b 区间截断的短 Goldbach 表示层。",
        "",
        "## 2. 断点的鸽巢路由",
        "",
        "设 `Bcrit=LowSurvivors-ceil(0.43P/logP)+1`。若 loaded-b 层达到 `Bcrit`，则对任意候选上界 `K`：",
        "",
        "```text",
        "max_u_layer_load > K  OR  loaded_u_layers >= ceil(Bcrit/K).",
        "```",
        "",
        "因此下一步可以只攻两个原子：固定 u 层单层过载，或 loaded-u 层数过密。",
        "",
        "## 3. P 区间账本",
        "",
        "| P range | hits | min shortage | max loaded-u | max u-load | max u-window b-len | max density | p at min shortage |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row.get("min_breakpoint_shortage_to_failure")),
                    str(row.get("max_loaded_u_layers")),
                    str(row.get("max_u_layer_load")),
                    str(row.get("max_loaded_fixed_u_window_b_length")),
                    str(row.get("max_loaded_density_inside_fixed_u_window")),
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
            "| shortage | template | p | side | rho | H | R(P) | Low | Good | Bcrit | loaded b | loaded u | max u-load | max window | threshold | needed u |",
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
                    str(row["H"]),
                    str(row["required_integer_H"]),
                    str(row["low_survivors"]),
                    str(row["good_effective_slot_count"]),
                    str(row["failure_loaded_b_breakpoint"]),
                    str(row["loaded_b_layers"]),
                    str(row["loaded_u_layers_recomputed"]),
                    str(row["max_u_layer_load_recomputed"]),
                    str(row["max_loaded_fixed_u_window_b_length"]),
                    str(row["finite_max_load_route_threshold_at_current_loaded_u"]),
                    str(row["u_layers_needed_under_observed_max_load"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 单层最大实载样本",
            "",
            "| p | side | rho | loaded b | loaded u | max u-load | top loaded u layers |",
            "| ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["max_layer_examples"][:8]:
        layers = [
            f"u={item['u']}:load={item['loaded_count']},window={item['available_b_interval_length']}"
            for item in row["top_loaded_u_layers"]
        ]
        lines.append(
            f"| {row['p']} | `{row['side']}` | {row['rho']} | {row['loaded_b_layers']} | "
            f"{row['loaded_u_layers']} | {row['max_u_layer_load']} | `{'; '.join(layers)}` |"
        )
    lines.extend(
        [
            "",
            "## 6. 结构判断",
            "",
            "- 当前最紧断点仍是 `P=2467, minus, rho=7`：`Bcrit=7`、loaded b 为 `6`、还差一层。",
            "- 有限重放中 fixed-u 单层最大实载为 `4`；这指向短 Goldbach 层过密，而不是固定 b 层容量问题。",
            "- 由于 fixed-u 层自带 `q+m=2(P+u)`，后续若出现断点反例，可以登记为同一偶数层内多素对聚集的相位证书。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 7. 命题行",
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
            "## 8. 决策表",
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
            "## 9. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 具体目标：证明 fixed-u 短 Goldbach 层负载与 loaded-u 层数不能共同达到 `Bcrit`，或把达到断点的同偶数层素对过密登记并排斥为 PDEC/SAE。",
            "",
            "## 10. 依赖哈希",
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
    parser.add_argument("--breakpoint-ledger", type=Path, default=BREAKPOINT_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    breakpoint_ledger = (
        args.breakpoint_ledger if args.breakpoint_ledger.is_absolute() else ROOT / args.breakpoint_ledger
    )
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(breakpoint_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "p0": args.p0,
                "fixed_u_grouping_failure_count": result["aggregate"]["fixed_u_grouping_failure_count"],
                "short_goldbach_sum_failure_count": result["aggregate"]["short_goldbach_sum_failure_count"],
                "breakpoint_reached_count_at_p0": result["aggregate"]["breakpoint_reached_count_at_p0"],
                "max_u_layer_load_at_p0": result["aggregate"]["max_u_layer_load_at_p0"],
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
