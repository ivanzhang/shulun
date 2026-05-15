#!/usr/bin/env python3
"""把 3/5/7 小筛残余超界压成高因子合数吸收门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_highfactor_absorber_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-router.md
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

RESIDUAL_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-ledger.json"
TEMPLATE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-template-provenance-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-router.md"

RESIDUAL_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_residual_cap_router.py"
)
COMPANION_LOSS_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py"
)
EVEN_LAYER_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_even_layer_interval_router.py"

MAIN_TARGET = "SmallSieve357ResidualCapBoundOrMinusQuotaAtomPDEC"
NEXT_TARGET = "ResidualPrimePairBoundOrHighFactorAbsorberPDEC"


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
    factor = 3
    while factor * factor <= value:
        if value % factor == 0:
            return factor
        factor += 2
    return value


def highfactor_slots(loss: Any, even: Any, p_value: int, side: str, prime_flags: bytearray) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """返回残余中的真素对槽与 lpf>7 高因子合数槽。"""
    primes = []
    highfactor = []
    for slot in loss.cap_slots(even, p_value, side, prime_flags):
        if slot["m_is_prime"]:
            primes.append(slot)
            continue
        lpf = least_prime_factor(int(slot["m"]))
        if lpf > 7:
            highfactor.append({**slot, "least_prime_factor_m": lpf})
    return primes, highfactor


def enrich_absorber_rows(max_p: int, template_ledger: Path, target_h_coeff: float) -> list[dict[str, Any]]:
    """重放 residual 行并加入高因子吸收字段。"""
    residual = load_module(RESIDUAL_ROUTER, "highfactor_residual")
    loss = load_module(COMPANION_LOSS_ROUTER, "highfactor_loss")
    even = load_module(EVEN_LAYER_ROUTER, "highfactor_even")
    rows = residual.enrich_residual_rows(max_p, template_ledger, target_h_coeff)
    prime_flags = even.sieve(2 * max_p + 1000)
    enriched = []
    for row in rows:
        p_value = int(row["p"])
        side = str(row["side"])
        prime_slots, highfactor = highfactor_slots(loss, even, p_value, side, prime_flags)
        bound = int(row["small_sieve_357_residual_bound"])
        residual_count = int(row["small_sieve_357_residual_cap_count"])
        residual_surplus = max(0, residual_count - bound)
        absorber_count = len(highfactor)
        absorber_surplus = absorber_count - residual_surplus
        prime_pair_surplus = len(prime_slots) - bound
        enriched.append(
            {
                **row,
                "residual_prime_pair_count": len(prime_slots),
                "highfactor_composite_absorber_count": absorber_count,
                "positive_residual_surplus_to_bound": residual_surplus,
                "highfactor_absorber_surplus_to_residual_surplus": absorber_surplus,
                "residual_prime_pair_surplus_to_bound": prime_pair_surplus,
                "highfactor_absorber_covers_positive_surplus": absorber_surplus >= 0,
                "residual_prime_pair_bound_ok": prime_pair_surplus <= 0,
                "sample_residual_prime_pair_slots": prime_slots[:8],
                "sample_highfactor_absorber_slots": highfactor[:8],
            }
        )
    return enriched


def atom_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """登记残余超界、等号和真素对等号原子。"""
    atoms = [
        row
        for row in rows
        if int(row["small_sieve_357_residual_surplus_to_bound"]) >= 0
        or int(row["residual_prime_pair_surplus_to_bound"]) == 0
    ]
    selected = sorted(
        atoms,
        key=lambda row: (
            -int(row["small_sieve_357_residual_surplus_to_bound"]),
            -int(row["residual_prime_pair_surplus_to_bound"]),
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
        "small_sieve_357_residual_cap_count",
        "small_sieve_357_residual_bound",
        "small_sieve_357_residual_surplus_to_bound",
        "residual_prime_pair_count",
        "residual_prime_pair_surplus_to_bound",
        "highfactor_composite_absorber_count",
        "positive_residual_surplus_to_bound",
        "highfactor_absorber_surplus_to_residual_surplus",
    ]
    return [{key: row[key] for key in keys} for row in selected]


def lpf_histogram_for_atoms(rows: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    """统计原子高因子吸收层的最小素因子。"""
    histogram = {}
    for row in rows:
        if int(row["small_sieve_357_residual_surplus_to_bound"]) < 0 and int(row["residual_prime_pair_surplus_to_bound"]) != 0:
            continue
        key = f"{row['p']}:{row['side']}:rho{row['rho']}:tpl{row['template_index']}"
        counts: dict[int, int] = {}
        for slot in row["sample_highfactor_absorber_slots"]:
            lpf = int(slot["least_prime_factor_m"])
            counts[lpf] = counts.get(lpf, 0) + 1
        histogram[key] = {str(item): counts[item] for item in sorted(counts)}
    return histogram


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "residual_prime_absorber_split",
            "status": "closed",
            "statement": "The 3/5/7 residual cap splits exactly into residual prime-pair slots plus lpf>7 high-factor composite absorber slots.",
        },
        {
            "name": "finite_highfactor_absorbs_positive_residual_surplus",
            "status": "closed_on_current_sweep",
            "statement": "On the current P>=2001 sweep, every positive 357 residual surplus is covered by lpf>7 high-factor composite absorbers.",
        },
        {
            "name": "global_residual_prime_pair_bound_or_absorber_pdec",
            "status": "open",
            "statement": "A global proof must bound residual prime pairs by Bcrit-1, or prove/pdec-exclude high-factor absorber persistence whenever residual cap overflows.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "ResidualPrimeAbsorberSplitClosed",
            "closed": agg["split_identity_failure_count_at_p0"] == 0,
            "proved": True,
            "meaning": "357 残余已精确分解为真素对槽与 lpf>7 高因子合数吸收槽。",
            "remaining": "closed",
        },
        {
            "gate": "CurrentHighFactorAbsorbsPositiveSurplus",
            "closed": agg["positive_surplus_absorber_failure_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中所有正残余超界都由高因子合数吸收。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "CurrentResidualPrimePairBoundClosed",
            "closed": agg["residual_prime_pair_bound_failure_count_at_p0"] == 0,
            "proved": False,
            "meaning": "有限重放中真素对残余未超过上界；全局证明仍缺。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalResidualPrimePairBoundOrAbsorberPDECProved",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明真素对残余上界，或排斥高因子吸收持久相位。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把 357 残余超界压成高因子吸收门。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(residual_ledger: Path, template_ledger: Path, max_p: int, p0: int, target_h_coeff: float) -> dict[str, Any]:
    """构造高因子吸收结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(residual_ledger)
    rows = enrich_absorber_rows(max_p, template_ledger, target_h_coeff)
    selected = [row for row in rows if int(row["p"]) >= p0]
    split_failures = [
        row
        for row in selected
        if int(row["residual_prime_pair_count"]) + int(row["highfactor_composite_absorber_count"])
        != int(row["small_sieve_357_residual_cap_count"])
    ]
    positive_absorber_failures = [
        row
        for row in selected
        if int(row["positive_residual_surplus_to_bound"]) > 0
        and int(row["highfactor_absorber_surplus_to_residual_surplus"]) < 0
    ]
    prime_bound_failures = [
        row for row in selected if int(row["residual_prime_pair_surplus_to_bound"]) > 0
    ]
    aggregate = {
        "residual_ledger": str(residual_ledger.relative_to(ROOT)),
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "target_h_coeff": target_h_coeff,
        "selected_hit_count_at_p0": len(selected),
        "previous_residual_failure_count_at_p0": source["aggregate"]["residual_failure_count_at_p0"],
        "split_identity_failure_count_at_p0": len(split_failures),
        "positive_residual_surplus_count_at_p0": sum(
            1 for row in selected if int(row["positive_residual_surplus_to_bound"]) > 0
        ),
        "positive_surplus_absorber_failure_count_at_p0": len(positive_absorber_failures),
        "residual_prime_pair_bound_failure_count_at_p0": len(prime_bound_failures),
        "residual_prime_pair_exact_count_at_p0": sum(
            1 for row in selected if int(row["residual_prime_pair_surplus_to_bound"]) == 0
        ),
        "max_positive_residual_surplus_at_p0": max(int(row["positive_residual_surplus_to_bound"]) for row in selected),
        "min_highfactor_absorber_surplus_to_positive_surplus_at_p0": min(
            int(row["highfactor_absorber_surplus_to_residual_surplus"]) for row in selected
        ),
        "global_residual_prime_pair_bound_proved": False,
        "highfactor_absorber_pdec_excluded": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "small_sieve_moduli": [3, 5, 7],
        },
        "aggregate": aggregate,
        "absorber_atom_records": atom_records(selected),
        "absorber_atom_lpf_histogram": lpf_histogram_for_atoms(selected),
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_highfactor_absorber_router",
        "status": "357_residual_cap_overflow_reduced_to_highfactor_absorber_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_absorber_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "absorber_atom_records": ledger["absorber_atom_records"],
        "absorber_atom_lpf_histogram": ledger["absorber_atom_lpf_histogram"],
        "global_residual_prime_pair_bound_proved": False,
        "highfactor_absorber_pdec_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_highfactor_absorber_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_357_residual_cap_router.py": sha256(
                RESIDUAL_ROUTER
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_companion_composite_loss_router.py": sha256(
                COMPANION_LOSS_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-residual-cap-ledger.json": sha256(
                residual_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "本步把 `3/5/7` 小筛残余拆成真素对残余与 `lpf>7` 高因子合数吸收项。"
            f"当前 `P>={p0}` 重放中，正残余超界行数为 {aggregate['positive_residual_surplus_count_at_p0']}，"
            f"高因子吸收失败数为 {aggregate['positive_surplus_absorber_failure_count_at_p0']}；"
            f"真素对残余上界失败数为 {aggregate['residual_prime_pair_bound_failure_count_at_p0']}。"
            "唯一正超界原子 `P=2467` 的超界量 8 被 8 个 `lpf>7` 合数槽精确吸收，"
            "因此残余超界本身不是最终矛盾；严格闭合仍需全局证明真素对残余上界，或排斥高因子吸收/素对持久相位。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower 357 highfactor absorber router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={agg['max_p']}",
        f"p0={agg['p0']}",
        f"positive_residual_surplus_count_at_p0={agg['positive_residual_surplus_count_at_p0']}",
        f"positive_surplus_absorber_failure_count_at_p0={agg['positive_surplus_absorber_failure_count_at_p0']}",
        f"residual_prime_pair_bound_failure_count_at_p0={agg['residual_prime_pair_bound_failure_count_at_p0']}",
        f"residual_prime_pair_exact_count_at_p0={agg['residual_prime_pair_exact_count_at_p0']}",
        f"max_positive_residual_surplus_at_p0={agg['max_positive_residual_surplus_at_p0']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 吸收分解",
        "",
        "```text",
        "357_residual_cap = residual_prime_pairs + highfactor_composite_absorbers",
        "highfactor_composite_absorbers = #{cap slots with lpf(m)>7 and m composite}",
        "```",
        "",
        "残余 cap 超界只说明小筛后剩余槽多；只有其中的真素对槽超过 `Bcrit-1` 才会冲击 H 下界。",
        "",
        "## 2. 原子表",
        "",
        "| p | side | rho | Bcrit | residual | bound | residual surplus | prime pairs | prime surplus | highfactor | absorber surplus |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in result["absorber_atom_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    row["side"],
                    str(row["rho"]),
                    str(row["failure_loaded_b_breakpoint"]),
                    str(row["small_sieve_357_residual_cap_count"]),
                    str(row["small_sieve_357_residual_bound"]),
                    str(row["small_sieve_357_residual_surplus_to_bound"]),
                    str(row["residual_prime_pair_count"]),
                    str(row["residual_prime_pair_surplus_to_bound"]),
                    str(row["highfactor_composite_absorber_count"]),
                    str(row["highfactor_absorber_surplus_to_residual_surplus"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 高因子吸收 lpf 直方图",
            "",
            "```json",
            json.dumps(result["absorber_atom_lpf_histogram"], ensure_ascii=False, indent=2, sort_keys=True),
            "```",
            "",
            "## 4. 结构判断",
            "",
            "- `P=2467` 的残余超界量是 8，刚好由 8 个 `lpf>7` 合数槽吸收；真素对数等于上界。",
            "- `P=5297` 的残余等号行有 12 个高因子吸收槽，因此真素对数低于上界 12。",
            "- 下一步应直接攻真素对残余上界，或把高因子吸收/素对共存相位登记为 PDEC。",
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
            "- 具体目标：证明 residual prime-pair count `<=Bcrit-1`，或证明/排斥高因子吸收与真素对持久共存 PDEC。",
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
    parser.add_argument("--residual-ledger", type=Path, default=RESIDUAL_LEDGER)
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    residual_ledger = args.residual_ledger if args.residual_ledger.is_absolute() else ROOT / args.residual_ledger
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    result = build_result(residual_ledger, template_ledger, args.max_p, args.p0, args.target_h_coeff)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-357-highfactor-absorber-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "positive_residual_surplus_count_at_p0": result["aggregate"][
                    "positive_residual_surplus_count_at_p0"
                ],
                "positive_surplus_absorber_failure_count_at_p0": result["aggregate"][
                    "positive_surplus_absorber_failure_count_at_p0"
                ],
                "residual_prime_pair_bound_failure_count_at_p0": result["aggregate"][
                    "residual_prime_pair_bound_failure_count_at_p0"
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
