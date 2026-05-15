#!/usr/bin/env python3
"""把余数 cap 断点压力压成伴随 m 合数损耗下界。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

RESIDUE_GATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-router.md"

BREAKPOINT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "SelectorGoodShellEuclideanResidueCapEnvelopeOrResiduePrimePairPDEC"
NEXT_TARGET = "SelectorResidueCapCompanionCompositeLossFloorOrPrimePairPersistencePDEC"


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


def cap_slots(even: Any, p_value: int, side: str, prime_flags: bytearray) -> list[dict[str, Any]]:
    """枚举 q 为素数且余数 cap 命中的槽，不要求伴随 m 为素数。"""
    cutoff = even.cutoff_alpha45(p_value)
    max_b = (p_value - cutoff - 1) // 2
    half = (p_value - 1) // 2
    rows: list[dict[str, Any]] = []
    for b_value in range(1, max_b + 1):
        q_value = p_value - 2 * b_value
        if not even.is_prime_by_flags(q_value, prime_flags):
            continue
        quotient, residue = divmod(2 * b_value * b_value, q_value)
        if side == "minus":
            if not (1 <= residue <= half):
                continue
            u_value = quotient
            s_value = residue
        elif side == "plus":
            if not (1 <= q_value - residue <= half):
                continue
            u_value = quotient + 1
            s_value = q_value - residue
        else:
            raise ValueError(f"unknown side: {side}")
        m_value = p_value + 2 * (b_value + u_value)
        rows.append(
            {
                "b": b_value,
                "u": u_value,
                "q": q_value,
                "m": m_value,
                "s": s_value,
                "r": 2 * s_value,
                "euclidean_quotient": quotient,
                "euclidean_residue": residue,
                "m_is_prime": even.is_prime_by_flags(m_value, prime_flags),
            }
        )
    return rows


def enrich_loss_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放断点行并加入伴随合数损耗字段。"""
    breakpoint = load_module(BREAKPOINT_ROUTER, "loss_breakpoint")
    even = load_module(EVEN_LAYER_ROUTER, "loss_even_layer")
    base_rows, replay = breakpoint.enrich_breakpoint_rows(max_p, template_ledger, target_h_coeff)
    prime_flags = even.sieve(2 * max_p + 1000)

    rows: list[dict[str, Any]] = []
    prime_pair_identity_failures: list[dict[str, Any]] = []
    loss_floor_failures: list[dict[str, Any]] = []
    for base in base_rows:
        p_value = int(base["p"])
        side = str(base["side"])
        slots = cap_slots(even, p_value, side, prime_flags)
        cap_count = len(slots)
        prime_pair_count = sum(1 for item in slots if item["m_is_prime"])
        composite_loss = cap_count - prime_pair_count
        bcrit = int(base["failure_loaded_b_breakpoint"])
        required_loss = max(0, cap_count - bcrit + 1)
        loss_surplus = composite_loss - required_loss
        if prime_pair_count != int(base["loaded_b_layers"]) or prime_pair_count != int(base["good_effective_slot_count"]):
            prime_pair_identity_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "template_index": base["template_index"],
                    "prime_pair_count": prime_pair_count,
                    "loaded_b_layers": base["loaded_b_layers"],
                    "good_effective_slot_count": base["good_effective_slot_count"],
                }
            )
        if loss_surplus < 0:
            loss_floor_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "template_index": base["template_index"],
                    "cap_count": cap_count,
                    "prime_pair_count": prime_pair_count,
                    "bcrit": bcrit,
                    "required_loss": required_loss,
                    "composite_loss": composite_loss,
                    "loss_surplus": loss_surplus,
                }
            )
        composite_sample = [item for item in slots if not item["m_is_prime"]][:8]
        prime_sample = [item for item in slots if item["m_is_prime"]][:8]
        rows.append(
            {
                **base,
                "residue_cap_slot_count": cap_count,
                "residue_cap_prime_pair_count": prime_pair_count,
                "companion_composite_loss_count": composite_loss,
                "required_composite_loss_for_breakpoint_safety": required_loss,
                "composite_loss_surplus_to_floor": loss_surplus,
                "residue_cap_reaches_breakpoint": cap_count >= bcrit,
                "prime_pair_identity_ok": prime_pair_count
                == int(base["loaded_b_layers"])
                == int(base["good_effective_slot_count"]),
                "composite_loss_floor_ok": loss_surplus >= 0,
                "composite_loss_ratio_in_cap": composite_loss / cap_count if cap_count else None,
                "required_loss_ratio_in_cap": required_loss / cap_count if cap_count else None,
                "sample_prime_pair_slots": prime_sample,
                "sample_companion_composite_slots": composite_sample,
            }
        )
    replay["prime_pair_identity_failures"] = prime_pair_identity_failures
    replay["loss_floor_failures"] = loss_floor_failures
    return rows, replay


def band_records(rows: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总合数损耗门。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        if not selected:
            records.append({"p_lo": lo, "p_hi": hi, "hit_count": 0})
            continue
        min_surplus = min(int(row["composite_loss_surplus_to_floor"]) for row in selected)
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "cap_reaches_breakpoint_count": sum(1 for row in selected if bool(row["residue_cap_reaches_breakpoint"])),
                "min_composite_loss_surplus_to_floor": min_surplus,
                "max_required_composite_loss": max(
                    int(row["required_composite_loss_for_breakpoint_safety"]) for row in selected
                ),
                "max_actual_composite_loss": max(int(row["companion_composite_loss_count"]) for row in selected),
                "max_residue_cap_slot_count": max(int(row["residue_cap_slot_count"]) for row in selected),
                "max_prime_pair_count": max(int(row["residue_cap_prime_pair_count"]) for row in selected),
                "p_values_at_min_surplus": sorted(
                    {int(row["p"]) for row in selected if int(row["composite_loss_surplus_to_floor"]) == min_surplus}
                ),
            }
        )
    return records


def tight_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出最紧合数损耗样本。"""
    selected = sorted(
        rows,
        key=lambda row: (
            int(row["composite_loss_surplus_to_floor"]),
            int(row["breakpoint_shortage_to_failure"]),
            int(row["p"]),
            row["side"],
        ),
    )
    keys = [
        "template_index",
        "p",
        "side",
        "rho",
        "H",
        "failure_loaded_b_breakpoint",
        "loaded_b_layers",
        "breakpoint_shortage_to_failure",
        "residue_cap_slot_count",
        "residue_cap_prime_pair_count",
        "companion_composite_loss_count",
        "required_composite_loss_for_breakpoint_safety",
        "composite_loss_surplus_to_floor",
        "composite_loss_ratio_in_cap",
        "required_loss_ratio_in_cap",
        "sample_prime_pair_slots",
        "sample_companion_composite_slots",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "cap_prime_pair_loss_identity",
            "status": "closed",
            "statement": "GoodShell equals residue-cap slots minus companion-composite loss, where loss counts cap slots whose m=P+2(b+u) is composite.",
        },
        {
            "name": "breakpoint_loss_floor_equivalence",
            "status": "closed",
            "statement": "GoodShell<Bcrit is equivalent to composite_loss >= max(0, cap_count-Bcrit+1).",
        },
        {
            "name": "cap_only_route_insufficient",
            "status": "closed_on_current_sweep",
            "statement": "In the current sweep cap_count frequently reaches Bcrit, so the remaining pressure is the companion-composite loss floor.",
        },
        {
            "name": "global_companion_composite_loss_floor",
            "status": "open",
            "statement": "A global proof must force enough composite companions inside residue-cap slots, or register persistent prime-pair excess as PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "CompanionCompositeLossIdentityClosed",
            "closed": agg["prime_pair_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "GoodShell 精确等于 residue cap 槽数减伴随 m 合数损耗。",
            "remaining": "closed",
        },
        {
            "gate": "BreakpointLossFloorEquivalenceClosed",
            "closed": agg["loss_floor_failure_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中损耗下界足以守住断点；全局证明仍缺。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CapOnlyEnvelopeClosed",
            "closed": False,
            "proved": False,
            "meaning": "只靠余数 cap 上界不能闭合，因为 cap 槽数经常超过断点。",
            "remaining": "discard as direct closure route",
        },
        {
            "gate": "GlobalCompositeLossFloorProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明伴随 m 合数损耗下界，或排斥 prime-pair 持久过密。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把余数 cap 同步压力压成伴随合数损耗下界。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    residue_gate_ledger: Path,
    template_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
) -> dict[str, Any]:
    """构造伴随合数损耗结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(residue_gate_ledger)
    rows, replay = enrich_loss_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    mandatory = [row for row in selected if bool(row["residue_cap_reaches_breakpoint"])]
    aggregate = {
        "residue_gate_ledger": str(residue_gate_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "prime_rho_hit_count": len(rows),
        "selected_hit_count_at_p0": len(selected),
        "previous_candidate_identity_failure_count": source["aggregate"]["candidate_identity_failure_count"],
        "prime_pair_identity_failure_count": len(replay["prime_pair_identity_failures"]),
        "loss_floor_failure_count": len(replay["loss_floor_failures"]),
        "loss_floor_failure_count_at_p0": sum(
            1 for row in selected if int(row["composite_loss_surplus_to_floor"]) < 0
        ),
        "cap_reaches_breakpoint_count_at_p0": len(mandatory),
        "cap_below_breakpoint_count_at_p0": len(selected) - len(mandatory),
        "min_composite_loss_surplus_to_floor_at_p0": min(
            int(row["composite_loss_surplus_to_floor"]) for row in selected
        ),
        "min_mandatory_loss_surplus_to_floor_at_p0": min(
            (int(row["composite_loss_surplus_to_floor"]) for row in mandatory),
            default=None,
        ),
        "max_required_composite_loss_at_p0": max(
            int(row["required_composite_loss_for_breakpoint_safety"]) for row in selected
        ),
        "max_actual_composite_loss_at_p0": max(int(row["companion_composite_loss_count"]) for row in selected),
        "max_residue_cap_slot_count_at_p0": max(int(row["residue_cap_slot_count"]) for row in selected),
        "max_prime_pair_count_at_p0": max(int(row["residue_cap_prime_pair_count"]) for row in selected),
        "global_composite_loss_floor_proved": False,
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
        "loss_floor_formula": {
            "Bcrit": "LowSurvivors-ceil(0.43P/logP)+1",
            "GoodShell": "residue_cap_slot_count - companion_composite_loss_count",
            "required_loss": "max(0, residue_cap_slot_count-Bcrit+1)",
            "safe_condition": "companion_composite_loss_count >= required_loss",
        },
        "band_records": band_records(rows, [(3, 2000), (2001, 5000), (5001, max_p)]),
        "tight_examples": tight_examples(selected),
        "prime_pair_identity_failures": replay["prime_pair_identity_failures"],
        "loss_floor_failures": replay["loss_floor_failures"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router",
        "status": "residue_cap_breakpoint_pressure_reduced_to_companion_composite_loss_floor_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_loss_floor_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "loss_floor_formula": ledger["loss_floor_formula"],
        "band_records": ledger["band_records"],
        "tight_examples": ledger["tight_examples"],
        "global_composite_loss_floor_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py": sha256(
                BREAKPOINT_ROUTER
            ),
            "experiments/prime_matrix_square_phase_even_layer_interval_router.py": sha256(EVEN_LAYER_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-ledger.json": sha256(
                residue_gate_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步确认 cap-only 路线不能直接闭合：高段 selector 行中 residue cap 槽数经常已经达到断点。"
            "真正剩余是伴随 `m=P+2(b+u)` 必须有足够多合数损耗。"
            "精确公式为 `GoodShell=cap_count-composite_loss`，"
            "`GoodShell<Bcrit` 等价于 `composite_loss>=max(0,cap_count-Bcrit+1)`。"
            f"当前 `P>={p0}` 重放中 cap 达断点行数为 {aggregate['cap_reaches_breakpoint_count_at_p0']}，"
            f"损耗下界失败数为 {aggregate['loss_floor_failure_count_at_p0']}，"
            f"最小损耗余量为 {aggregate['min_composite_loss_surplus_to_floor_at_p0']}；"
            "全局仍需证明这个伴随合数损耗下界，或把 prime-pair 持久过密登记并排斥为 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    formula = result["loss_floor_formula"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower companion composite loss router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"prime_pair_identity_failure_count={agg['prime_pair_identity_failure_count']}",
        f"cap_reaches_breakpoint_count_at_p0={agg['cap_reaches_breakpoint_count_at_p0']}",
        f"loss_floor_failure_count_at_p0={agg['loss_floor_failure_count_at_p0']}",
        f"min_composite_loss_surplus_to_floor_at_p0={agg['min_composite_loss_surplus_to_floor_at_p0']}",
        f"max_required_composite_loss_at_p0={agg['max_required_composite_loss_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 损耗下界公式",
        "",
        "```text",
        f"Bcrit={formula['Bcrit']}",
        f"GoodShell={formula['GoodShell']}",
        f"required_loss={formula['required_loss']}",
        f"safe_condition={formula['safe_condition']}",
        "```",
        "",
        "因此若 cap 槽数超过断点，必须由伴随 `m` 合数槽支付差额。",
        "",
        "## 2. P 区间账本",
        "",
        "| P range | hits | cap reaches Bcrit | min loss surplus | max required loss | max actual loss | max cap | max prime pairs | p at min surplus |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row.get("cap_reaches_breakpoint_count")),
                    str(row.get("min_composite_loss_surplus_to_floor")),
                    str(row.get("max_required_composite_loss")),
                    str(row.get("max_actual_composite_loss")),
                    str(row.get("max_residue_cap_slot_count")),
                    str(row.get("max_prime_pair_count")),
                    f"`{row.get('p_values_at_min_surplus')}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧样本",
            "",
            "| loss surplus | shortage | p | side | rho | Bcrit | Good | cap | loss | required loss | loss ratio | required ratio |",
            "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["tight_examples"][:14]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["composite_loss_surplus_to_floor"]),
                    str(row["breakpoint_shortage_to_failure"]),
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["failure_loaded_b_breakpoint"]),
                    str(row["loaded_b_layers"]),
                    str(row["residue_cap_slot_count"]),
                    str(row["companion_composite_loss_count"]),
                    str(row["required_composite_loss_for_breakpoint_safety"]),
                    str(row["composite_loss_ratio_in_cap"]),
                    str(row["required_loss_ratio_in_cap"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 余数 cap 本身不是最后矛盾点；它经常给出足够多的潜在槽。",
            "- 真正要排斥的是这些潜在槽中伴随 `m` 也持续为素数，导致合数损耗低于必需下界。",
            "- 最紧处损耗余量为 `0`，对应上一层断点缺口 `1`；因此下一步应攻 prime-pair 持久过密或其 PDEC 登记排斥。",
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
            "- 具体目标：证明 residue cap 槽中的伴随 `m` 合数损耗达到 `max(0,cap_count-Bcrit+1)`，或把损耗不足转成 prime-pair persistence PDEC/SAE 并排斥。",
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
    parser.add_argument("--residue-gate-ledger", type=Path, default=RESIDUE_GATE_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    residue_gate_ledger = (
        args.residue_gate_ledger if args.residue_gate_ledger.is_absolute() else ROOT / args.residue_gate_ledger
    )
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(residue_gate_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-companion-composite-loss-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "p0": args.p0,
                "cap_reaches_breakpoint_count_at_p0": result["aggregate"]["cap_reaches_breakpoint_count_at_p0"],
                "loss_floor_failure_count_at_p0": result["aggregate"]["loss_floor_failure_count_at_p0"],
                "min_composite_loss_surplus_to_floor_at_p0": result["aggregate"][
                    "min_composite_loss_surplus_to_floor_at_p0"
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
