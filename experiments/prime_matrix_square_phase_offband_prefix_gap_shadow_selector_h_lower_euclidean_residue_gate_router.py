#!/usr/bin/env python3
"""把 fixed-u 短 Goldbach 层进一步压成 fixed-b 欧几里得余数门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_euclidean_residue_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-router.md
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

FIXED_U_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-router.md"

BREAKPOINT_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "SelectorGoodShellFixedULayerEnvelopeOrShortGoldbachLayerPDEC"
NEXT_TARGET = "SelectorGoodShellEuclideanResidueCapEnvelopeOrResiduePrimePairPDEC"


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


def slot_key(slot: dict[str, int]) -> tuple[int, int, int, int, int, int]:
    """候选槽比较键。"""
    return (slot["b"], slot["u"], slot["q"], slot["m"], slot["s"], slot["r"])


def euclidean_candidate_slots(even: Any, p_value: int, side: str, prime_flags: bytearray) -> list[dict[str, int]]:
    """用 2b^2 = u0*q + v 的欧几里得门生成候选槽。"""
    cutoff = even.cutoff_alpha45(p_value)
    max_b = (p_value - cutoff - 1) // 2
    half = (p_value - 1) // 2
    rows: list[dict[str, int]] = []
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
        if even.is_prime_by_flags(m_value, prime_flags):
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
                }
            )
    return rows


def side_cap_record(even: Any, p_value: int, prime_flags: bytearray) -> dict[str, Any]:
    """审计同一 P 下 plus/minus 两侧余数 cap 的交叠。"""
    cutoff = even.cutoff_alpha45(p_value)
    max_b = (p_value - cutoff - 1) // 2
    half = (p_value - 1) // 2
    q_prime_layers = 0
    minus_cap_layers = 0
    plus_cap_layers = 0
    both_side_cap_layers = 0
    both_side_prime_pair_layers = 0
    for b_value in range(1, max_b + 1):
        q_value = p_value - 2 * b_value
        if not even.is_prime_by_flags(q_value, prime_flags):
            continue
        q_prime_layers += 1
        quotient, residue = divmod(2 * b_value * b_value, q_value)
        minus_cap = 1 <= residue <= half
        plus_cap = 1 <= q_value - residue <= half
        minus_prime = False
        plus_prime = False
        if minus_cap:
            minus_cap_layers += 1
            minus_prime = even.is_prime_by_flags(p_value + 2 * (b_value + quotient), prime_flags)
        if plus_cap:
            plus_cap_layers += 1
            plus_prime = even.is_prime_by_flags(p_value + 2 * (b_value + quotient + 1), prime_flags)
        if minus_cap and plus_cap:
            both_side_cap_layers += 1
        if minus_prime and plus_prime:
            both_side_prime_pair_layers += 1
    return {
        "p": p_value,
        "q_prime_layers": q_prime_layers,
        "minus_cap_layers": minus_cap_layers,
        "plus_cap_layers": plus_cap_layers,
        "both_side_cap_layers": both_side_cap_layers,
        "both_side_prime_pair_layers": both_side_prime_pair_layers,
    }


def enrich_residue_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """重放断点行并核验欧几里得余数门。"""
    breakpoint = load_module(BREAKPOINT_ROUTER, "residue_gate_breakpoint")
    even = load_module(EVEN_LAYER_ROUTER, "residue_gate_even_layer")
    base_rows, replay = breakpoint.enrich_breakpoint_rows(max_p, template_ledger, target_h_coeff)
    prime_flags = even.sieve(2 * max_p + 1000)

    rows: list[dict[str, Any]] = []
    candidate_identity_failures: list[dict[str, Any]] = []
    s_formula_failures: list[dict[str, Any]] = []
    for base in base_rows:
        p_value = int(base["p"])
        side = str(base["side"])
        interval_slots = even.candidate_slots(p_value, side, prime_flags)
        residue_slots = euclidean_candidate_slots(even, p_value, side, prime_flags)
        interval_keys = {slot_key(item)[:6] for item in interval_slots}
        residue_keys = {slot_key(item)[:6] for item in residue_slots}
        if interval_keys != residue_keys:
            candidate_identity_failures.append(
                {
                    "p": p_value,
                    "side": side,
                    "template_index": base["template_index"],
                    "missing_from_residue": sorted(interval_keys - residue_keys)[:10],
                    "extra_from_residue": sorted(residue_keys - interval_keys)[:10],
                }
            )
        bad_s = [
            item
            for item in residue_slots
            if even.s_value_for(p_value, item["b"], item["u"], side) != item["s"]
        ]
        if bad_s:
            s_formula_failures.append(
                {"p": p_value, "side": side, "template_index": base["template_index"], "bad_s": bad_s[:10]}
            )
        residues = [int(item["euclidean_residue"]) for item in residue_slots]
        cap_depths = [
            int(item["euclidean_residue"]) if side == "minus" else int(item["q"] - item["euclidean_residue"])
            for item in residue_slots
        ]
        rows.append(
            {
                **base,
                "residue_gate_candidate_count": len(residue_slots),
                "residue_gate_matches_interval_candidates": interval_keys == residue_keys,
                "residue_s_formula_ok": not bad_s,
                "min_euclidean_residue": min(residues) if residues else None,
                "max_euclidean_residue": max(residues) if residues else None,
                "min_cap_depth_s": min(cap_depths) if cap_depths else None,
                "max_cap_depth_s": max(cap_depths) if cap_depths else None,
                "sample_residue_slots": residue_slots[:8],
            }
        )
    replay["candidate_identity_failures"] = candidate_identity_failures
    replay["residue_s_formula_failures"] = s_formula_failures
    replay["side_cap_records"] = [
        side_cap_record(even, p_value, prime_flags)
        for p_value in sorted({int(row["p"]) for row in base_rows})
    ]
    return rows, replay


def band_records(rows: list[dict[str, Any]], side_cap_records: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按 P 区间汇总余数门观测。"""
    records: list[dict[str, Any]] = []
    for lo, hi in bands:
        selected = [row for row in rows if lo <= int(row["p"]) <= hi]
        caps = [row for row in side_cap_records if lo <= int(row["p"]) <= hi]
        if not selected:
            records.append({"p_lo": lo, "p_hi": hi, "hit_count": 0})
            continue
        min_shortage = min(int(row["breakpoint_shortage_to_failure"]) for row in selected)
        records.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "hit_count": len(selected),
                "unique_p_count": len(caps),
                "min_breakpoint_shortage_to_failure": min_shortage,
                "max_residue_gate_candidate_count": max(int(row["residue_gate_candidate_count"]) for row in selected),
                "max_both_side_cap_layers": max(int(row["both_side_cap_layers"]) for row in caps) if caps else 0,
                "max_both_side_prime_pair_layers": max(
                    int(row["both_side_prime_pair_layers"]) for row in caps
                )
                if caps
                else 0,
                "p_values_at_min_shortage": sorted(
                    {int(row["p"]) for row in selected if int(row["breakpoint_shortage_to_failure"]) == min_shortage}
                ),
            }
        )
    return records


def tight_examples(rows: list[dict[str, Any]], limit: int = 20) -> list[dict[str, Any]]:
    """列出最接近断点的余数门样本。"""
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
        "residue_gate_candidate_count",
        "breakpoint_shortage_to_failure",
        "min_cap_depth_s",
        "max_cap_depth_s",
        "sample_residue_slots",
    ]
    return [{key: row[key] for key in keys} for row in selected[:limit]]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "fixed_b_euclidean_residue_gate",
            "status": "closed",
            "statement": "Writing q=P-2b and 2b^2=u0*q+v, the minus side is exactly 1<=v<=H2 with u=u0, and the plus side is exactly 1<=q-v<=H2 with u=u0+1.",
        },
        {
            "name": "residue_gate_candidate_identity",
            "status": "closed",
            "statement": "The Euclidean residue gate generates exactly the same GoodShell candidate slots as the fixed-b interval formula.",
        },
        {
            "name": "crt_ready_residue_cap_form",
            "status": "closed",
            "statement": "GoodShell is now a high-prime q layer plus a residue cap condition on 2b^2 mod q and a companion primality condition for m.",
        },
        {
            "name": "global_residue_cap_prime_pair_envelope",
            "status": "open",
            "statement": "A global proof must control how often the residue cap and companion prime condition can jointly reach Bcrit, or register that persistence as PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "EuclideanResidueGateClosed",
            "closed": agg["candidate_identity_failure_count"] == 0 and agg["residue_s_formula_failure_count"] == 0,
            "proved": True,
            "meaning": "fixed-b/fixed-u 候选槽精确等价于欧几里得余数 cap 门。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentResidueGateBelowBreakpoint",
            "closed": agg["breakpoint_reached_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中余数门候选未触发断点；这不是全局证明。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalResidueCapEnvelopeProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明高素数 q 层、余数 cap 与 companion prime 不能共同达到断点。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 fixed-u 短 Goldbach 层压成 CRT-ready 余数门。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    fixed_u_ledger: Path,
    template_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
) -> dict[str, Any]:
    """构造欧几里得余数门结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(fixed_u_ledger)
    rows, replay = enrich_residue_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    min_shortage = min(int(row["breakpoint_shortage_to_failure"]) for row in selected)
    aggregate = {
        "fixed_u_ledger": str(fixed_u_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "prime_rho_hit_count": len(rows),
        "selected_hit_count_at_p0": len(selected),
        "previous_fixed_u_grouping_failure_count": source["aggregate"]["fixed_u_grouping_failure_count"],
        "candidate_identity_failure_count": len(replay["candidate_identity_failures"]),
        "residue_s_formula_failure_count": len(replay["residue_s_formula_failures"]),
        "breakpoint_reached_count_at_p0": sum(1 for row in selected if bool(row["breakpoint_reached"])),
        "min_breakpoint_shortage_to_failure_at_p0": min_shortage,
        "max_residue_gate_candidate_count_at_p0": max(int(row["residue_gate_candidate_count"]) for row in selected),
        "max_both_side_cap_layers_at_p0": max(
            int(row["both_side_cap_layers"]) for row in replay["side_cap_records"] if int(row["p"]) >= p0
        ),
        "max_both_side_prime_pair_layers_at_p0": max(
            int(row["both_side_prime_pair_layers"]) for row in replay["side_cap_records"] if int(row["p"]) >= p0
        ),
        "global_residue_cap_envelope_proved": False,
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
        "euclidean_gate_formula": {
            "H2": "(P-1)/2",
            "q": "P-2b",
            "division": "2b^2 = u0*q + v, 0<=v<q",
            "minus": "1<=v<=H2, u=u0, s=v, m=P+2(b+u0)",
            "plus": "1<=q-v<=H2, u=u0+1, s=q-v, m=P+2(b+u0+1)",
        },
        "band_records": band_records(rows, replay["side_cap_records"], [(3, 2000), (2001, 5000), (5001, max_p)]),
        "tight_examples": tight_examples(selected),
        "side_cap_records": replay["side_cap_records"],
        "candidate_identity_failures": replay["candidate_identity_failures"],
        "residue_s_formula_failures": replay["residue_s_formula_failures"],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_euclidean_residue_gate_router",
        "status": "fixed_u_short_goldbach_layer_reduced_to_euclidean_residue_cap_gate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_residue_gate_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "euclidean_gate_formula": ledger["euclidean_gate_formula"],
        "band_records": ledger["band_records"],
        "tight_examples": ledger["tight_examples"],
        "global_residue_cap_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_euclidean_residue_gate_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_breakpoint_layer_capacity_router.py": sha256(
                BREAKPOINT_ROUTER
            ),
            "experiments/prime_matrix_square_phase_even_layer_interval_router.py": sha256(EVEN_LAYER_ROUTER),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-fixed-u-layer-envelope-ledger.json": sha256(
                fixed_u_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 fixed-u 短 Goldbach 层再压成 fixed-b 欧几里得余数门。"
            "令 `q=P-2b` 且 `2b^2=u0*q+v`，则 minus 候选恰为 `1<=v<=H2`、`u=u0`，"
            "plus 候选恰为 `1<=q-v<=H2`、`u=u0+1`。"
            "因此 GoodShell 的破坏输入已变成高素数 `q`、余数 cap、伴随素数 `m` 三者的同步事件。"
            f"当前 `P>={p0}` 重放中候选恒等失败数为 {aggregate['candidate_identity_failure_count']}，"
            f"断点达到数为 {aggregate['breakpoint_reached_count_at_p0']}，"
            f"最小断点缺口为 {aggregate['min_breakpoint_shortage_to_failure_at_p0']}；"
            "全局仍需证明余数 cap 素对同步不能达到断点，或将其登记并排斥为 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    formula = result["euclidean_gate_formula"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower Euclidean residue gate router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"candidate_identity_failure_count={agg['candidate_identity_failure_count']}",
        f"residue_s_formula_failure_count={agg['residue_s_formula_failure_count']}",
        f"breakpoint_reached_count_at_p0={agg['breakpoint_reached_count_at_p0']}",
        f"min_breakpoint_shortage_to_failure_at_p0={agg['min_breakpoint_shortage_to_failure_at_p0']}",
        f"max_residue_gate_candidate_count_at_p0={agg['max_residue_gate_candidate_count_at_p0']}",
        f"max_both_side_prime_pair_layers_at_p0={agg['max_both_side_prime_pair_layers_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 欧几里得余数门",
        "",
        "```text",
        f"H2={formula['H2']}",
        f"q={formula['q']}",
        f"{formula['division']}",
        f"minus: {formula['minus']}",
        f"plus:  {formula['plus']}",
        "```",
        "",
        "这个公式把半列窗口、fixed-u 选择、左右侧符号统一成一个余数 cap 判据。",
        "",
        "## 2. P 区间账本",
        "",
        "| P range | hits | unique P | min shortage | max residue candidates | max both-side cap | max both-side prime-pair | p at min shortage |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["hit_count"]),
                    str(row.get("unique_p_count")),
                    str(row.get("min_breakpoint_shortage_to_failure")),
                    str(row.get("max_residue_gate_candidate_count")),
                    str(row.get("max_both_side_cap_layers")),
                    str(row.get("max_both_side_prime_pair_layers")),
                    f"`{row.get('p_values_at_min_shortage')}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最紧样本",
            "",
            "| shortage | template | p | side | rho | H | R(P) | Low | Good | Bcrit | loaded b | residue candidates | cap s range | sample slots |",
            "| ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["tight_examples"][:10]:
        sample = [
            f"b={item['b']},u={item['u']},q={item['q']},m={item['m']},v={item['euclidean_residue']}"
            for item in row["sample_residue_slots"][:3]
        ]
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
                    str(row["residue_gate_candidate_count"]),
                    f"{row['min_cap_depth_s']}..{row['max_cap_depth_s']}",
                    f"`{'; '.join(sample)}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 结构判断",
            "",
            "- 余数门把候选槽改写为 `2b^2 mod (P-2b)` 落入左右 cap，并要求伴随 `m` 为素数。",
            "- 这与用户提出的 CRT/逆元最小对齐思路同形：零行或反例链若存在，必须在这些余数 cap 中形成同步对齐。",
            "- 当前最紧样本仍只差一层；尚未从余数 cap 同步中推出全局矛盾。",
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
            "- 具体目标：控制 `q=P-2b` 为素数、`2b^2 mod q` 落入 cap、`m` 为素数三条件的同步密度；若不能直接上界，则登记为 residue-prime-pair PDEC/SAE。",
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
    parser.add_argument("--fixed-u-ledger", type=Path, default=FIXED_U_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    fixed_u_ledger = args.fixed_u_ledger if args.fixed_u_ledger.is_absolute() else ROOT / args.fixed_u_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(fixed_u_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-euclidean-residue-gate-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "p0": args.p0,
                "candidate_identity_failure_count": result["aggregate"]["candidate_identity_failure_count"],
                "residue_s_formula_failure_count": result["aggregate"]["residue_s_formula_failure_count"],
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
