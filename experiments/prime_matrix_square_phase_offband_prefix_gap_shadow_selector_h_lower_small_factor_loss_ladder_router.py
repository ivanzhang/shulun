#!/usr/bin/env python3
"""把伴随 m 合数损耗下界压成小素因子损耗阶梯。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_small_factor_loss_ladder_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

COMPANION_LOSS_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-router.md"

COMPANION_LOSS_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "SelectorResidueCapCompanionCompositeLossFloorOrPrimePairPersistencePDEC"
NEXT_TARGET = "SelectorResidueCapSmallFactorLossFloorOrLargePrimeCompanionPersistencePDEC"

DEFAULT_THRESHOLDS = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 67, 71, 83, 97]


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


def least_prime_factor(value: int) -> int:
    """返回 value 的最小素因子；若 value 为素数则返回自身。"""
    if value % 2 == 0:
        return 2
    limit = math.isqrt(value)
    factor = 3
    while factor <= limit:
        if value % factor == 0:
            return factor
        factor += 2
    return value


def small_factor_count(composite_slots: list[dict[str, Any]], threshold: int) -> int:
    """统计最小素因子不超过 threshold 的合数槽。"""
    return sum(1 for item in composite_slots if int(item["least_prime_factor_m"]) <= threshold)


def enrich_small_factor_rows(
    max_p: int,
    template_ledger: Path,
    target_h_coeff: float,
    thresholds: list[int],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放伴随损耗行并加入小因子阶梯字段。"""
    loss = load_module(COMPANION_LOSS_ROUTER, "small_factor_loss")
    even = load_module(EVEN_LAYER_ROUTER, "small_factor_even")
    base_rows, replay = loss.enrich_loss_rows(max_p, template_ledger, target_h_coeff)
    prime_flags = even.sieve(2 * max_p + 1000)

    rows: list[dict[str, Any]] = []
    lpf_histogram: Counter[int] = Counter()
    for base in base_rows:
        p_value = int(base["p"])
        side = str(base["side"])
        slots = loss.cap_slots(even, p_value, side, prime_flags)
        composite_slots = []
        for item in slots:
            if item["m_is_prime"]:
                continue
            enriched = {**item, "least_prime_factor_m": least_prime_factor(int(item["m"]))}
            composite_slots.append(enriched)
            lpf_histogram[int(enriched["least_prime_factor_m"])] += 1

        required_loss = int(base["required_composite_loss_for_breakpoint_safety"])
        sorted_lpf = sorted(int(item["least_prime_factor_m"]) for item in composite_slots)
        if required_loss == 0:
            exact_required_lpf_cutoff = 0
        elif required_loss <= len(sorted_lpf):
            exact_required_lpf_cutoff = sorted_lpf[required_loss - 1]
        else:
            # 低段可能本来就未满足损耗下界，此时不存在足额的第 required_loss 个合数槽。
            exact_required_lpf_cutoff = None
        threshold_records = []
        for threshold in thresholds:
            count = small_factor_count(composite_slots, threshold)
            threshold_records.append(
                {
                    "threshold": threshold,
                    "small_factor_loss_count": count,
                    "small_factor_loss_surplus_to_floor": count - required_loss,
                    "covers_required_loss": count >= required_loss,
                }
            )
        rows.append(
            {
                **base,
                "exact_required_lpf_cutoff": exact_required_lpf_cutoff,
                "small_factor_threshold_records": threshold_records,
                "small_factor_loss_count_at_7": small_factor_count(composite_slots, 7),
                "small_factor_loss_surplus_at_7": small_factor_count(composite_slots, 7) - required_loss,
                "small_factor_loss_count_at_43": small_factor_count(composite_slots, 43),
                "small_factor_loss_surplus_at_43": small_factor_count(composite_slots, 43) - required_loss,
                "least_prime_factor_histogram": dict(sorted(Counter(int(item["least_prime_factor_m"]) for item in composite_slots).items())),
                "sample_small_factor_composite_slots": composite_slots[:10],
                "sample_large_factor_composite_slots": [
                    item for item in composite_slots if int(item["least_prime_factor_m"]) > 43
                ][:10],
            }
        )
    replay["least_prime_factor_histogram"] = dict(sorted(lpf_histogram.items()))
    return rows, replay


def threshold_summary(rows: list[dict[str, Any]], thresholds: list[int], p0: int) -> list[dict[str, Any]]:
    """汇总每个小因子阈值的有限覆盖情况。"""
    selected = [row for row in rows if int(row["p"]) >= p0]
    summary = []
    for threshold in thresholds:
        failures = []
        min_surplus = None
        for row in selected:
            record = next(item for item in row["small_factor_threshold_records"] if item["threshold"] == threshold)
            surplus = int(record["small_factor_loss_surplus_to_floor"])
            min_surplus = surplus if min_surplus is None else min(min_surplus, surplus)
            if surplus < 0:
                failures.append(row)
        summary.append(
            {
                "threshold": threshold,
                "failure_count_at_p0": len(failures),
                "min_surplus_at_p0": min_surplus,
                "failure_p_values_sample": sorted({int(row["p"]) for row in failures})[:20],
            }
        )
    return summary


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总小因子阶梯。"""
    records = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        if not selected:
            records.append({"p_lo": lo, "p_hi": hi, "hit_count": 0})
            continue
        finite_cutoff_rows = [row for row in selected if row["exact_required_lpf_cutoff"] is not None]
        max_cutoff = max((int(row["exact_required_lpf_cutoff"]) for row in finite_cutoff_rows), default=None)
        min_surplus_7 = min(int(row["small_factor_loss_surplus_at_7"]) for row in selected)
        min_surplus_43 = min(int(row["small_factor_loss_surplus_at_43"]) for row in selected)
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "max_exact_required_lpf_cutoff": max_cutoff,
                "min_small_factor_surplus_at_7": min_surplus_7,
                "failure_count_at_7": sum(1 for row in selected if int(row["small_factor_loss_surplus_at_7"]) < 0),
                "min_small_factor_surplus_at_43": min_surplus_43,
                "failure_count_at_43": sum(1 for row in selected if int(row["small_factor_loss_surplus_at_43"]) < 0),
                "p_values_at_max_cutoff": sorted(
                    {
                        int(row["p"])
                        for row in finite_cutoff_rows
                        if int(row["exact_required_lpf_cutoff"]) == max_cutoff
                    }
                ),
            }
        )
    return records


def tight_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出最需要大 lpf 截止的样本。"""
    selected = sorted(
        rows,
        key=lambda row: (
            -int(row["exact_required_lpf_cutoff"]),
            int(row["composite_loss_surplus_to_floor"]),
            int(row["p"]),
            row["side"],
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
        "required_composite_loss_for_breakpoint_safety",
        "companion_composite_loss_count",
        "composite_loss_surplus_to_floor",
        "exact_required_lpf_cutoff",
        "small_factor_loss_count_at_7",
        "small_factor_loss_surplus_at_7",
        "small_factor_loss_count_at_43",
        "small_factor_loss_surplus_at_43",
        "least_prime_factor_histogram",
        "sample_small_factor_composite_slots",
        "sample_large_factor_composite_slots",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "small_factor_loss_ladder_identity",
            "status": "closed",
            "statement": "For any threshold y, the y-small-factor loss is the number of residue-cap slots whose companion m has least prime factor <=y.",
        },
        {
            "name": "finite_lpf43_loss_floor",
            "status": "closed_on_current_sweep",
            "statement": "On the current P>=2001 sweep, y=43 covers the required composite-loss floor for every selector row.",
        },
        {
            "name": "finite_lpf7_single_exception",
            "status": "closed_on_current_sweep",
            "statement": "On the current P>=2001 sweep, y=7 fails only at the exact boundary row P=2467, minus, rho=7.",
        },
        {
            "name": "global_small_factor_loss_floor",
            "status": "open",
            "statement": "A global proof must derive an adaptive small-factor CRT loss floor, or route persistent large-prime companions to PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "SmallFactorLossLadderMaterialized",
            "closed": True,
            "proved": True,
            "meaning": "伴随合数损耗已按 least-prime-factor 阶梯精确拆分。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentLPF43LossFloorClosed",
            "closed": agg["failure_count_at_lpf43_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中 lpf<=43 足以支付全部损耗下界；这不是全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentLPF7SingleExceptionIdentified",
            "closed": agg["failure_count_at_lpf7_at_p0"] == 1,
            "proved": False,
            "meaning": "lpf<=7 的唯一高段失败是贴边行 P=2467, minus, rho=7。",
            "remaining": "finite boundary atom",
        },
        {
            "gate": "GlobalSmallFactorLossFloorProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需从 CRT 小模覆盖/层叠筛推出全局小因子损耗下界。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把合数损耗下界压成小因子阶梯。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    companion_loss_ledger: Path,
    template_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    thresholds: list[int],
) -> dict[str, Any]:
    """构造小因子损耗阶梯结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(companion_loss_ledger)
    rows, replay = enrich_small_factor_rows(max_p, template_ledger, target_h_coeff, thresholds)
    selected = [row for row in rows if int(row["p"]) >= p0]
    threshold_records = threshold_summary(rows, thresholds, p0)
    failure_lpf7 = next(item for item in threshold_records if item["threshold"] == 7)
    failure_lpf43 = next(item for item in threshold_records if item["threshold"] == 43)
    zero_surplus_rows = [row for row in selected if int(row["composite_loss_surplus_to_floor"]) == 0]
    aggregate = {
        "companion_loss_ledger": str(companion_loss_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "thresholds": thresholds,
        "prime_rho_hit_count": len(rows),
        "selected_hit_count_at_p0": len(selected),
        "previous_loss_floor_failure_count_at_p0": source["aggregate"]["loss_floor_failure_count_at_p0"],
        "zero_composite_loss_surplus_count_at_p0": len(zero_surplus_rows),
        "max_exact_required_lpf_cutoff_at_p0": max(int(row["exact_required_lpf_cutoff"]) for row in selected),
        "failure_count_at_lpf7_at_p0": failure_lpf7["failure_count_at_p0"],
        "min_surplus_at_lpf7_at_p0": failure_lpf7["min_surplus_at_p0"],
        "failure_count_at_lpf43_at_p0": failure_lpf43["failure_count_at_p0"],
        "min_surplus_at_lpf43_at_p0": failure_lpf43["min_surplus_at_p0"],
        "global_small_factor_loss_floor_proved": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "thresholds": thresholds,
        },
        "aggregate": aggregate,
        "threshold_summary": threshold_records,
        "band_records": band_records(rows, [(3, 2000), (2001, 5000), (5001, max_p)]),
        "tight_examples": tight_examples(selected),
        "least_prime_factor_histogram": replay["least_prime_factor_histogram"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_small_factor_loss_ladder_router",
        "status": "companion_composite_loss_floor_reduced_to_small_factor_loss_ladder_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_lpf43_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "threshold_summary": threshold_records,
        "band_records": ledger["band_records"],
        "tight_examples": ledger["tight_examples"],
        "global_small_factor_loss_floor_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_small_factor_loss_ladder_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py": sha256(
                COMPANION_LOSS_ROUTER
            ),
            "experiments/prime_matrix_square_phase_even_layer_interval_router.py": sha256(EVEN_LAYER_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-ledger.json": sha256(
                companion_loss_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把伴随合数损耗进一步分解为 least-prime-factor 小因子阶梯。"
            f"当前 `P>={p0}` 重放中，损耗余量为 0 的贴边行只有 {aggregate['zero_composite_loss_surplus_count_at_p0']} 个；"
            f"`lpf(m)<=7` 只在 {aggregate['failure_count_at_lpf7_at_p0']} 个高段行不足，"
            f"而 `lpf(m)<=43` 的小因子损耗已覆盖全部行，失败数为 {aggregate['failure_count_at_lpf43_at_p0']}。"
            "这说明当前有限障碍集中在小模 CRT 覆盖，而不是大素数尾项；"
            "但固定 43 不能当作全局定理，严格闭合仍需自足证明自适应小因子损耗下界，或排斥 large-prime companion persistence PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower small-factor loss ladder router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"zero_composite_loss_surplus_count_at_p0={agg['zero_composite_loss_surplus_count_at_p0']}",
        f"max_exact_required_lpf_cutoff_at_p0={agg['max_exact_required_lpf_cutoff_at_p0']}",
        f"failure_count_at_lpf7_at_p0={agg['failure_count_at_lpf7_at_p0']}",
        f"min_surplus_at_lpf7_at_p0={agg['min_surplus_at_lpf7_at_p0']}",
        f"failure_count_at_lpf43_at_p0={agg['failure_count_at_lpf43_at_p0']}",
        f"min_surplus_at_lpf43_at_p0={agg['min_surplus_at_lpf43_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 阶梯判据",
        "",
        "对每个 residue cap 合数槽，记 `lpf(m)` 为伴随 `m=P+2(b+u)` 的最小素因子。若",
        "",
        "```text",
        "# {cap slots with lpf(m)<=y} >= max(0, cap_count-Bcrit+1),",
        "```",
        "",
        "则该行的伴随合数损耗下界已经由 `<=y` 的小素因子完全支付。",
        "",
        "## 2. 阈值汇总",
        "",
        "| y | failure count at p0 | min surplus | failure P sample |",
        "| ---: | ---: | ---: | --- |",
    ]
    for row in result["threshold_summary"]:
        lines.append(
            f"| {row['threshold']} | {row['failure_count_at_p0']} | {row['min_surplus_at_p0']} | "
            f"`{row['failure_p_values_sample']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. P 区间账本",
            "",
            "| P range | hits | max needed lpf | min surplus y=7 | fails y=7 | min surplus y=43 | fails y=43 | p at max cutoff |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row.get("max_exact_required_lpf_cutoff")),
                    str(row.get("min_small_factor_surplus_at_7")),
                    str(row.get("failure_count_at_7")),
                    str(row.get("min_small_factor_surplus_at_43")),
                    str(row.get("failure_count_at_43")),
                    f"`{row.get('p_values_at_max_cutoff')}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 最紧样本",
            "",
            "| p | side | rho | Bcrit | Good | cap | required loss | actual loss | loss surplus | needed lpf | loss<=7 | surplus<=7 | loss<=43 | surplus<=43 |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tight_examples"][:12]:
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
                    str(row["required_composite_loss_for_breakpoint_safety"]),
                    str(row["companion_composite_loss_count"]),
                    str(row["composite_loss_surplus_to_floor"]),
                    str(row["exact_required_lpf_cutoff"]),
                    str(row["small_factor_loss_count_at_7"]),
                    str(row["small_factor_loss_surplus_at_7"]),
                    str(row["small_factor_loss_count_at_43"]),
                    str(row["small_factor_loss_surplus_at_43"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 当前贴边原子唯一：`P=2467, minus, rho=7`，要求 28 个合数损耗且实际正好 28 个。",
            "- 除该贴边原子外，`lpf(m)<=7` 的小模层已经足够支付高段损耗下界。",
            "- 加入 `11..43` 的有限小模层后，当前高段全部通过；这给下一步 CRT 小模覆盖证明提供了最窄输入形状。",
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
            "- 具体目标：把 `lpf(m)<=y` 的小模 CRT 覆盖计数转成自足下界；若无法全局覆盖，则把大素数伴随 `m` 的持续素性登记为 PDEC/SAE。",
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
    parser.add_argument("--companion-loss-ledger", type=Path, default=COMPANION_LOSS_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    parser.add_argument("--thresholds", default=",".join(str(item) for item in DEFAULT_THRESHOLDS))
    return parser.parse_args()


def parse_thresholds(raw: str) -> list[int]:
    """解析阈值列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """入口函数。"""
    args = parse_args()
    companion_loss_ledger = (
        args.companion_loss_ledger
        if args.companion_loss_ledger.is_absolute()
        else ROOT / args.companion_loss_ledger
    )
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(
        companion_loss_ledger,
        template_ledger,
        args.max_p,
        args.p0,
        args.target_h_coeff,
        parse_thresholds(args.thresholds),
    )
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-small-factor-loss-ladder-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "p0": args.p0,
                "failure_count_at_lpf7_at_p0": result["aggregate"]["failure_count_at_lpf7_at_p0"],
                "failure_count_at_lpf43_at_p0": result["aggregate"]["failure_count_at_lpf43_at_p0"],
                "max_exact_required_lpf_cutoff_at_p0": result["aggregate"]["max_exact_required_lpf_cutoff_at_p0"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
