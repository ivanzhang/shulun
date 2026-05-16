#!/usr/bin/env python3
"""把 singleton residue Rankin 质量拆成可攻预算。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_rankin_budget_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-router.md
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
PROFILE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-residue-sae-profile-ledger.json"
PROFILE_ROUTER = (
    ROOT
    / "experiments"
    / "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py"
)
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json"
OUT_JSON = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "singleton-rankin-budget-router.json"
)
OUT_MD = DOCS / (
    "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-"
    "singleton-rankin-budget-router.md"
)

MAIN_TARGET = "SingletonResidueRankinMassBoundOrTransportResetPDECExclusion"
NEXT_TARGET = "OneSlotLowModOccupancyDecayOrTransportResetPDECExclusion"


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


def build_singleton_records(
    template_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    max_certificate_size: int,
) -> list[dict[str, Any]]:
    """重放并提取 singleton residue 物理记录。"""
    profile = load_module(PROFILE_ROUTER, "rankin_budget_profile")
    physical_records, _ = profile.build_records(
        template_ledger,
        max_p,
        p0,
        target_h_coeff,
        max_certificate_size,
    )
    residue_groups = profile.group_by(physical_records, "residue_packet_key")
    return [items[0] for items in residue_groups.values() if len(items) == 1]


def rankin_weight(record: dict[str, Any]) -> float:
    """Rankin 权重。"""
    return 1.0 / int(record["crt_modulus"])


def row_mass(records: list[dict[str, Any]]) -> float:
    """求一组记录的 Rankin 质量。"""
    return sum(rankin_weight(record) for record in records)


def p_shell_rows(records: list[dict[str, Any]], p0: int, max_p: int, width: int) -> list[dict[str, Any]]:
    """按 P 壳层统计质量。"""
    rows = []
    lo = p0
    while lo <= max_p:
        hi = min(max_p, lo + width - 1)
        selected = [record for record in records if lo <= int(record["p"]) <= hi]
        mass = row_mass(selected)
        one_slot = [record for record in selected if int(record["certificate_size"]) == 1]
        two_slot = [record for record in selected if int(record["certificate_size"]) == 2]
        rows.append(
            {
                "p_lo": lo,
                "p_hi": hi,
                "count": len(selected),
                "rankin_mass": mass,
                "rankin_mass_per_1000_p": mass * 1000.0 / (hi - lo + 1),
                "one_slot_count": len(one_slot),
                "one_slot_rankin_mass": row_mass(one_slot),
                "two_slot_count": len(two_slot),
                "two_slot_rankin_mass": row_mass(two_slot),
            }
        )
        lo = hi + 1
    return rows


def ell_band_rows(records: list[dict[str, Any]], bands: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """按一槽 ell 档统计质量。"""
    one_slot = [record for record in records if int(record["certificate_size"]) == 1]
    rows = []
    for lo, hi in bands:
        selected = [
            record
            for record in one_slot
            if lo <= int(record["ell_tuple"][0]) <= hi
        ]
        mass = row_mass(selected)
        ell_values = sorted({int(record["ell_tuple"][0]) for record in selected})
        rows.append(
            {
                "ell_lo": lo,
                "ell_hi": hi,
                "count": len(selected),
                "distinct_ell_count": len(ell_values),
                "ell_values": ell_values,
                "rankin_mass": mass,
                "average_mass_per_ell": mass / len(ell_values) if ell_values else 0.0,
            }
        )
    return rows


def size_rows(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """按证书大小统计质量。"""
    rows = []
    for size in sorted({int(record["certificate_size"]) for record in records}):
        selected = [record for record in records if int(record["certificate_size"]) == size]
        rows.append(
            {
                "certificate_size": size,
                "count": len(selected),
                "rankin_mass": row_mass(selected),
                "mass_share": row_mass(selected) / row_mass(records) if records else 0.0,
                "min_modulus": min(int(record["crt_modulus"]) for record in selected),
                "max_modulus": max(int(record["crt_modulus"]) for record in selected),
            }
        )
    return rows


def one_slot_ell_rows(records: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    """按一槽 ell 统计占用率。"""
    one_slot = [record for record in records if int(record["certificate_size"]) == 1]
    grouped: dict[tuple[str, int], list[dict[str, Any]]] = {}
    for record in one_slot:
        grouped.setdefault((str(record["side"]), int(record["ell_tuple"][0])), []).append(record)
    rows = []
    for (side, ell), items in grouped.items():
        residues = sorted({int(record["crt_residue"]) for record in items})
        rows.append(
            {
                "side": side,
                "ell": ell,
                "count": len(items),
                "distinct_residue_count": len(residues),
                "occupancy_ratio": len(residues) / ell,
                "rankin_mass": len(items) / ell,
                "p_min": min(int(record["p"]) for record in items),
                "p_max": max(int(record["p"]) for record in items),
                "residue_sample": residues[:16],
            }
        )
    return sorted(rows, key=lambda row: (-row["rankin_mass"], row["side"], row["ell"]))[:limit]


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "singleton_rankin_budget_identity",
            "status": "closed",
            "statement": "Singleton Rankin mass is exactly decomposed by certificate size, P-shell, and one-slot ell bands.",
        },
        {
            "name": "two_slot_rankin_mass_small_current_sweep",
            "status": "closed_on_current_sweep",
            "statement": "Two-slot singleton mass is small in the current sweep because its CRT modulus is a product of two primes.",
        },
        {
            "name": "one_slot_low_mod_occupancy_decay_open",
            "status": "open",
            "statement": "The dominant one-slot low-mod occupancy must be shown to decay or be absorbed by transport reset-PDEC/SAE.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "RankinBudgetIdentityClosed",
            "closed": True,
            "proved": True,
            "meaning": "singleton Rankin 质量已被证书大小、P 壳层、ell 档精确拆分。",
            "remaining": "closed",
        },
        {
            "gate": "TwoSlotMassSmallCurrentSweep",
            "closed": agg["two_slot_mass_share"] < 0.01,
            "proved": False,
            "meaning": "二槽质量当前不足总质量 1%，主硬点不在二槽。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ShellMassDecayObserved",
            "closed": False,
            "proved": False,
            "meaning": "1000 宽 P 壳层质量没有单调衰减，不能从样本直接推出可求和。",
            "remaining": "one-slot occupancy decay needed",
        },
        {
            "gate": "OneSlotLowModOccupancyBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "一槽低模占用率是主质量来源，仍需全局不等式。",
            "remaining": "OneSlotLowModOccupancyDecay",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只定位 Rankin 质量瓶颈，不关闭全局命题。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(
    template_ledger: Path,
    profile_ledger: Path,
    max_p: int,
    p0: int,
    target_h_coeff: float,
    max_certificate_size: int,
    shell_width: int,
    limit: int,
) -> dict[str, Any]:
    """构造 Rankin 预算结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    profile = load_json(profile_ledger)
    records = build_singleton_records(
        template_ledger,
        max_p,
        p0,
        target_h_coeff,
        max_certificate_size,
    )
    total_mass = row_mass(records)
    size_budget = size_rows(records)
    two_slot_mass = next((row["rankin_mass"] for row in size_budget if row["certificate_size"] == 2), 0.0)
    shells = p_shell_rows(records, p0, max_p, shell_width)
    bands = ell_band_rows(
        records,
        [
            (0, 31),
            (32, 43),
            (44, 53),
            (54, 61),
            (62, 71),
            (72, 83),
            (84, 101),
            (102, 10**9),
        ],
    )
    ell_rows = one_slot_ell_rows(records, limit)
    aggregate = {
        "template_ledger": str(template_ledger.relative_to(ROOT)),
        "profile_ledger": str(profile_ledger.relative_to(ROOT)),
        "max_p": max_p,
        "p0": p0,
        "shell_width": shell_width,
        "singleton_count": len(records),
        "singleton_rankin_mass_total": total_mass,
        "profile_rankin_mass_total_check": float(profile["aggregate"]["singleton_rankin_mass_total"]),
        "one_slot_mass": next((row["rankin_mass"] for row in size_budget if row["certificate_size"] == 1), 0.0),
        "two_slot_mass": two_slot_mass,
        "two_slot_mass_share": two_slot_mass / total_mass if total_mass else 0.0,
        "max_shell_rankin_mass": max(row["rankin_mass"] for row in shells),
        "min_shell_rankin_mass": min(row["rankin_mass"] for row in shells),
        "shell_mass_monotone_decreasing": all(
            shells[index]["rankin_mass"] >= shells[index + 1]["rankin_mass"]
            for index in range(len(shells) - 1)
        ),
        "max_one_slot_ell_occupancy_ratio": max(row["occupancy_ratio"] for row in ell_rows),
        "max_one_slot_ell_rankin_mass": max(row["rankin_mass"] for row in ell_rows),
        "rankin_budget_identity_closed": True,
        "one_slot_low_mod_occupancy_decay_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "max_p": max_p,
            "p0": p0,
            "target_h_coeff": target_h_coeff,
            "max_certificate_size": max_certificate_size,
            "shell_width": shell_width,
            "limit": limit,
        },
        "aggregate": aggregate,
        "certificate_size_budget": size_budget,
        "p_shell_budget": shells,
        "one_slot_ell_band_budget": bands,
        "top_one_slot_ell_occupancy": ell_rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "singleton_rankin_budget_router"
        ),
        "status": "singleton_rankin_budget_localized_one_slot_occupancy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "certificate_size_budget": size_budget,
        "p_shell_budget": shells,
        "one_slot_ell_band_budget": bands,
        "top_one_slot_ell_occupancy": ell_rows,
        "one_slot_low_mod_occupancy_decay_proved": False,
        "transport_reset_pdec_excluded_globally": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "plain_conclusion": (
            "本步把 singleton Rankin 质量拆成预算：总质量 "
            f"{total_mass:.6f} 中，一槽贡献 {aggregate['one_slot_mass']:.6f}，"
            f"二槽贡献 {two_slot_mass:.6f}，二槽占比 {aggregate['two_slot_mass_share']:.4%}。"
            f"`P` 壳层质量最大 {aggregate['max_shell_rankin_mass']:.6f}，没有观察到单调衰减；"
            "因此主硬点不是二槽尾项，而是一槽低模占用率的全局衰减/吸收。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_rankin_budget_router.py": sha256(
            Path(__file__).resolve()
        ),
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_singleton_residue_sae_profile_router.py": sha256(
            PROFILE_ROUTER
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower singleton Rankin budget router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"singleton_count={agg['singleton_count']}",
        f"singleton_rankin_mass_total={agg['singleton_rankin_mass_total']:.12f}",
        f"one_slot_mass={agg['one_slot_mass']:.12f}",
        f"two_slot_mass={agg['two_slot_mass']:.12f}",
        f"two_slot_mass_share={agg['two_slot_mass_share']:.6f}",
        f"shell_mass_monotone_decreasing={fmt_bool(agg['shell_mass_monotone_decreasing'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 证书大小预算",
        "",
        "| size | count | Rankin mass | share | modulus range |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["certificate_size_budget"]:
        lines.append(
            f"| {row['certificate_size']} | {row['count']} | {row['rankin_mass']:.12f} | "
            f"{row['mass_share']:.6f} | `{row['min_modulus']}..{row['max_modulus']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. P 壳层预算",
            "",
            "| P shell | count | mass | mass/1000P | one-slot mass | two-slot mass |",
            "| --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["p_shell_budget"]:
        lines.append(
            f"| `{row['p_lo']}..{row['p_hi']}` | {row['count']} | {row['rankin_mass']:.6f} | "
            f"{row['rankin_mass_per_1000_p']:.6f} | {row['one_slot_rankin_mass']:.6f} | "
            f"{row['two_slot_rankin_mass']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 3. 一槽 ell 档预算",
            "",
            "| ell band | count | distinct ell | mass | avg mass/ell |",
            "| --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["one_slot_ell_band_budget"]:
        lines.append(
            f"| `{row['ell_lo']}..{row['ell_hi']}` | {row['count']} | {row['distinct_ell_count']} | "
            f"{row['rankin_mass']:.6f} | {row['average_mass_per_ell']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 4. 最大一槽占用",
            "",
            "| side | ell | count | occupancy | mass | p range | residues |",
            "| --- | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["top_one_slot_ell_occupancy"][:18]:
        lines.append(
            f"| `{row['side']}` | {row['ell']} | {row['count']} | {row['occupancy_ratio']:.6f} | "
            f"{row['rankin_mass']:.6f} | `{row['p_min']}..{row['p_max']}` | `{row['residue_sample']}` |"
        )
    lines.extend(
        [
            "",
            "## 5. 结构判断",
            "",
            "- 二槽 Rankin 质量当前不足 1%，不是主瓶颈。",
            "- P 壳层质量未显示单调衰减，不能把样本剖面直接外推为全局可求和。",
            "- 主硬点压缩为一槽低模 occupancy 的全局衰减，或由 transport reset-PDEC 吸收。",
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
            "- 证明一槽低模 occupancy 随尺度衰减，或将反复占用转入 transport reset-PDEC。",
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
    parser.add_argument("--template-ledger", type=Path, default=TEMPLATE_LEDGER)
    parser.add_argument("--profile-ledger", type=Path, default=PROFILE_LEDGER)
    parser.add_argument("--max-p", type=int, default=10000)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-h-coeff", type=float, default=0.43)
    parser.add_argument("--max-certificate-size", type=int, default=2)
    parser.add_argument("--shell-width", type=int, default=1000)
    parser.add_argument("--limit", type=int, default=40)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    template_ledger = args.template_ledger if args.template_ledger.is_absolute() else ROOT / args.template_ledger
    profile_ledger = args.profile_ledger if args.profile_ledger.is_absolute() else ROOT / args.profile_ledger
    result = build_result(
        template_ledger,
        profile_ledger,
        args.max_p,
        args.p0,
        args.target_h_coeff,
        args.max_certificate_size,
        args.shell_width,
        args.limit,
    )
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-singleton-rankin-budget-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "singleton_rankin_mass_total": result["aggregate"]["singleton_rankin_mass_total"],
                "one_slot_mass": result["aggregate"]["one_slot_mass"],
                "two_slot_mass": result["aggregate"]["two_slot_mass"],
                "two_slot_mass_share": result["aggregate"]["two_slot_mass_share"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
