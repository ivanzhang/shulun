#!/usr/bin/env python3
"""把 selector 平方窗 H 下系数门压成低幸存/GoodShell 相关余量。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_effective_capacity_correlation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-router.md
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

TAIL_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-router.md"

EXTERNAL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py"
)
PRIMEVOID_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_primevoid_effective_tiling_router.py"
TAIL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_tail_upper_pi_input_router.py"
)

MAIN_TARGET = "SquareWindowLowerCoefficientOrCorrelatedSurplusPDEC"
NEXT_TARGET = "SelectorLowSurvivorGoodShellCorrelatedSurplusOrNearFullEffectiveTilingPDEC"
SELF_CONTAINED_SIDE_TARGET = "SelfContainedDusartPiTwoSidedIntervalLedger"


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


def enrich_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放 selector 行并加入有效容量分解。"""
    external = load_module(EXTERNAL_ROUTER, "h_lower_external")
    primevoid = load_module(PRIMEVOID_ROUTER, "h_lower_primevoid")
    base_rows, replay = external.build_rows(max_p, template_ledger)
    prime_flags = primevoid.sieve(max_p + 1)
    primes = primevoid.primes_from_flags(prime_flags)
    audit_cache: dict[tuple[int, str], dict[str, Any]] = {}
    rows: list[dict[str, Any]] = []
    identity_failures: list[dict[str, Any]] = []
    for base in base_rows:
        p_value = int(base["p"])
        side = str(base["side"])
        key = (p_value, side)
        if key not in audit_cache:
            audit_cache[key] = primevoid.audit_sign(p_value, side, primes)
        audit = audit_cache[key]
        log_p = math.log(p_value)
        h_value = int(base["H"])
        low_value = int(audit["low_survivors_H"])
        good_value = int(audit["good_effective_slot_count"])
        h_from_capacity = low_value - good_value
        identity_ok = h_value == int(audit["prime_count"]) == h_from_capacity
        if not identity_ok:
            identity_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "H": h_value,
                    "prime_count": int(audit["prime_count"]),
                    "low_survivors": low_value,
                    "good_effective_slot_count": good_value,
                    "low_minus_good": h_from_capacity,
                }
            )
        h_coeff = h_value * log_p / p_value
        low_coeff = low_value * log_p / p_value
        good_coeff = good_value * log_p / p_value
        target_real = target_h_coeff * p_value / log_p
        rows.append(
            {
                "template_index": int(base["template_index"]),
                "p": p_value,
                "side": side,
                "rho": int(base["rho"]),
                "target_W": int(base["target_W"]),
                "H": h_value,
                "low_survivors": low_value,
                "good_effective_slot_count": good_value,
                "H_from_low_minus_good": h_from_capacity,
                "T": int(base["T"]),
                "H_scaled_coeff": h_coeff,
                "low_survivor_scaled_coeff": low_coeff,
                "good_shell_scaled_coeff": good_coeff,
                "correlated_surplus_coeff": low_coeff - good_coeff,
                "H_lower_target_coeff": target_h_coeff,
                "H_lower_margin_coeff": h_coeff - target_h_coeff,
                "H_lower_integer_slack": h_value - target_real,
                "near_full_effective_tiling_pressure": good_value - (low_value - target_real),
                "identity_ok": identity_ok,
            }
        )
    return rows, {"formula_failures": replay["formula_failures"], "identity_failures": identity_failures}


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]], target_h_coeff: float) -> list[dict[str, Any]]:
    """按 P 区间汇总相关余量。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        if not selected:
            records.append({"p_lo": lo, "p_hi": hi, "hit_count": 0})
            continue
        min_h = min(float(row["H_scaled_coeff"]) for row in selected)
        min_low = min(float(row["low_survivor_scaled_coeff"]) for row in selected)
        max_good = max(float(row["good_shell_scaled_coeff"]) for row in selected)
        min_margin = min(float(row["H_lower_margin_coeff"]) for row in selected)
        min_integer_slack = min(float(row["H_lower_integer_slack"]) for row in selected)
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "min_H_scaled_coeff": min_h,
                "min_low_survivor_scaled_coeff": min_low,
                "max_good_shell_scaled_coeff": max_good,
                "independent_min_low_minus_max_good": min_low - max_good,
                "independent_gate_beats_target": min_low - max_good >= target_h_coeff,
                "min_correlated_margin_coeff": min_margin,
                "min_H_lower_integer_slack": min_integer_slack,
                "p_values_at_min_H": sorted({int(row["p"]) for row in selected if float(row["H_scaled_coeff"]) == min_h}),
                "p_values_at_max_good": sorted(
                    {int(row["p"]) for row in selected if float(row["good_shell_scaled_coeff"]) == max_good}
                ),
            }
        )
    return records


def tight_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出最紧 H 下界样本。"""
    selected = sorted(rows, key=lambda row: (float(row["H_lower_margin_coeff"]), int(row["p"]), row["side"]))
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "target_W",
        "H",
        "low_survivors",
        "good_effective_slot_count",
        "T",
        "H_scaled_coeff",
        "low_survivor_scaled_coeff",
        "good_shell_scaled_coeff",
        "H_lower_margin_coeff",
        "H_lower_integer_slack",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "selector_square_window_effective_capacity_identity",
            "status": "closed_on_replay_and_symbolic_source",
            "statement": "On each selector row, H equals LowSurvivors minus GoodShell effective slots.",
        },
        {
            "name": "independent_low_good_coefficient_split",
            "status": "rejected_as_current_narrow_route",
            "statement": "The observed min LowSurvivor coefficient and max GoodShell coefficient do not independently imply H>=0.43P/logP.",
        },
        {
            "name": "correlated_low_good_surplus",
            "status": "open",
            "statement": "The exact remaining H gate is LowSurvivors-GoodShell>=0.43P/logP on selector rho hits.",
        },
        {
            "name": "near_full_effective_tiling_pdec",
            "status": "open_return",
            "statement": "If the correlated surplus fails, GoodShell must tile all but 0.43P/logP of the low survivors, giving a near-full effective tiling defect.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "EffectiveCapacityIdentityClosed",
            "closed": agg["identity_failure_count"] == 0,
            "proved": True,
            "meaning": "`H=LowSurvivors-GoodShell` 在 selector 命中行上已对齐。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentFiniteHLowerGateHolds",
            "closed": agg["H_lower_failure_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放支持 H 下系数，但不能当作全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "IndependentCoefficientSplitSufficient",
            "closed": agg["independent_gate_beats_target_after_p0"],
            "proved": False,
            "meaning": "独立下界/上界门太粗；必须证明行级相关余量。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "CorrelatedLowGoodSurplusProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 `LowSurvivors-GoodShell>=0.43P/logP`。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "TailUpperStrictSelfContainedClosed",
            "closed": agg["tail_upper_self_contained_closed"],
            "proved": False,
            "meaning": "旁路自足缺口仍是 pi 双侧区间界内化；外部路线可先继续攻 H。",
            "remaining": SELF_CONTAINED_SIDE_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 H 下界门压成更具体的相关余量/近满铺砖缺陷。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(tail_ledger: Path, template_ledger: Path, max_p: int, p0: int, target_h_coeff: float) -> dict[str, Any]:
    """构造 H 下界相关余量证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    tail_source = load_json(tail_ledger)
    rows, replay = enrich_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    min_low = min(float(row["low_survivor_scaled_coeff"]) for row in selected)
    max_good = max(float(row["good_shell_scaled_coeff"]) for row in selected)
    aggregate = {
        "tail_ledger": str(tail_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "prime_rho_hit_count": len(rows),
        "selected_hit_count_at_p0": len(selected),
        "formula_failure_count": len(replay["formula_failures"]),
        "identity_failure_count": len(replay["identity_failures"]),
        "H_lower_failure_count_at_p0": sum(1 for row in selected if float(row["H_scaled_coeff"]) < target_h_coeff),
        "min_H_scaled_coeff_at_p0": min(float(row["H_scaled_coeff"]) for row in selected),
        "min_low_survivor_scaled_coeff_at_p0": min_low,
        "max_good_shell_scaled_coeff_at_p0": max_good,
        "independent_min_low_minus_max_good_after_p0": min_low - max_good,
        "independent_gate_beats_target_after_p0": min_low - max_good >= target_h_coeff,
        "min_correlated_margin_coeff_at_p0": min(float(row["H_lower_margin_coeff"]) for row in selected),
        "min_H_lower_integer_slack_at_p0": min(float(row["H_lower_integer_slack"]) for row in selected),
        "tail_upper_external_closed": tail_source["aggregate"]["external_tail_upper_closed"],
        "tail_upper_self_contained_closed": tail_source["aggregate"]["self_contained_tail_upper_closed"],
        "correlated_low_good_surplus_proved": False,
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
        "band_records": band_records(rows, [(3, 2000), (2001, 5000), (5001, max_p)], target_h_coeff),
        "tight_examples": tight_examples(selected),
        "identity_failures": replay["identity_failures"],
        "formula_failures": replay["formula_failures"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_effective_capacity_correlation_router",
        "status": "h_lower_reduced_to_low_survivor_goodshell_correlated_surplus_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_h_lower_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "band_records": ledger["band_records"],
        "tight_examples": ledger["tight_examples"],
        "global_h_lower_coefficient_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_effective_capacity_correlation_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_ht_external_input_match_router.py": sha256(
                EXTERNAL_ROUTER
            ),
            "experiments/prime_matrix_square_phase_primevoid_effective_tiling_router.py": sha256(PRIMEVOID_ROUTER),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_tail_upper_pi_input_router.py": sha256(
                TAIL_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-ledger.json": sha256(
                tail_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把平方窗下界 `H>=0.43P/logP` 改写成有效容量恒等式 "
            "`H=LowSurvivors-GoodShell` 后的相关余量门。当前 selector 重放中恒等式失败数为 0，"
            f"`P>={p0}` 的最小 H 系数为 {aggregate['min_H_scaled_coeff_at_p0']}。"
            "但独立系数门失败：`min LowSurvivor coeff - max GoodShell coeff` "
            f"只有 {aggregate['independent_min_low_minus_max_good_after_p0']}，低于 0.43；"
            "所以真正剩余不是两个独立估计，而是行级相关余量，或其失败时的近满有效半素数铺砖 PDEC。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower effective-capacity correlation router",
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
        f"identity_failure_count={agg['identity_failure_count']}",
        f"H_lower_failure_count_at_p0={agg['H_lower_failure_count_at_p0']}",
        f"min_H_scaled_coeff_at_p0={agg['min_H_scaled_coeff_at_p0']}",
        f"min_low_survivor_scaled_coeff_at_p0={agg['min_low_survivor_scaled_coeff_at_p0']}",
        f"max_good_shell_scaled_coeff_at_p0={agg['max_good_shell_scaled_coeff_at_p0']}",
        f"independent_gate_beats_target_after_p0={fmt_bool(agg['independent_gate_beats_target_after_p0'])}",
        f"tail_upper_external_closed={fmt_bool(agg['tail_upper_external_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确分解",
        "",
        "对 `alpha=floor(4P/5)` 的低轮幸存集合，既有有效容量恒等式给出：",
        "",
        "```text",
        "LowSurvivors = Prime + GoodShell",
        "H = Prime",
        "therefore H = LowSurvivors - GoodShell.",
        "```",
        "",
        "这里 `GoodShell` 是真正命中低幸存列的有效高尾近方半素数槽。因而 `H>=0.43P/logP` 等价于：",
        "",
        "```text",
        "LowSurvivors - GoodShell >= 0.43 P/logP.",
        "```",
        "",
        "## 2. P 区间账本",
        "",
        "| P range | hits | min H coeff | min Low coeff | max Good coeff | minLow-maxGood | independent beats 0.43 | min margin coeff | min integer slack | p at min H | p at max Good |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row.get("min_H_scaled_coeff")),
                    str(row.get("min_low_survivor_scaled_coeff")),
                    str(row.get("max_good_shell_scaled_coeff")),
                    str(row.get("independent_min_low_minus_max_good")),
                    f"`{fmt_bool(row.get('independent_gate_beats_target', False))}`",
                    str(row.get("min_correlated_margin_coeff")),
                    str(row.get("min_H_lower_integer_slack")),
                    f"`{row.get('p_values_at_min_H')}`",
                    f"`{row.get('p_values_at_max_good')}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧样本",
            "",
            "| margin coeff | integer slack | template | p | side | rho | W | H | Low | Good | T | H coeff | Low coeff | Good coeff |",
            "| ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tight_examples"][:12]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["H_lower_margin_coeff"]),
                    str(row["H_lower_integer_slack"]),
                    str(row["template_index"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["target_W"]),
                    str(row["H"]),
                    str(row["low_survivors"]),
                    str(row["good_effective_slot_count"]),
                    str(row["T"]),
                    str(row["H_scaled_coeff"]),
                    str(row["low_survivor_scaled_coeff"]),
                    str(row["good_shell_scaled_coeff"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 独立估计 `LowSurvivors` 与 `GoodShell` 不够尖：当前最小低幸存系数减最大 GoodShell 系数低于 `0.43`。",
            "- 因此必须证明行级相关余量：GoodShell 槽不能集中贴满低幸存集合的临界部分。",
            "- 若该余量失败，反例会形成 near-full effective tiling：有效半素数槽覆盖低幸存集合到只剩少于 `0.43P/logP` 个平方锚素数。",
            "- 当前仍未完成全局行/列无条件闭合。",
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
            "- 具体下钻方向：把 near-full effective tiling 写成低幸存列与 GoodShell 槽的二部匹配/容量缺陷，寻找固定相位 PDEC 或 SAE 回流。",
            "- 外部路线中尾项门已可关闭；严格自足路线仍需补 `SelfContainedDusartPiTwoSidedIntervalLedger`。",
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
    parser.add_argument("--tail-ledger", type=Path, default=TAIL_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    tail_ledger = args.tail_ledger if args.tail_ledger.is_absolute() else ROOT / args.tail_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(tail_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-effective-capacity-correlation-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "p0": args.p0,
                "identity_failure_count": result["aggregate"]["identity_failure_count"],
                "H_lower_failure_count_at_p0": result["aggregate"]["H_lower_failure_count_at_p0"],
                "independent_gate_beats_target_after_p0": result["aggregate"][
                    "independent_gate_beats_target_after_p0"
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
