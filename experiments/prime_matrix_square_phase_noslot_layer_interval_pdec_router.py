#!/usr/bin/env python3
"""审计平方锚无槽 floor-layer 的区间原子与 PDEC/SAE 回流口。

用法示例：
  python3 experiments/prime_matrix_square_phase_noslot_layer_interval_pdec_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-noslot-layer-interval-pdec-router.json

输出：
  data/square-phase-noslot-layer-interval-pdec-ledger.json
  docs/monograph/prime-matrix-square-phase-noslot-layer-interval-pdec-router.json
  docs/monograph/prime-matrix-square-phase-noslot-layer-interval-pdec-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "square-phase-noslot-layer-interval-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-noslot-layer-interval-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-noslot-layer-interval-pdec-router.md"

MAIN_TARGET = "NoSlotFloorLayerBandBoundOrLayerPDEC"
NEXT_TARGET = "NoSlotLayerPrimeLoadBoundOrMovingLayerPDEC"


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int) -> list[int]:
    """从筛表提取不超过 limit 的素数。"""
    return [idx for idx in range(2, min(limit + 1, len(flags))) if flags[idx]]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def cutoff_alpha45(p: int) -> int:
    """返回 floor(4P/5)。"""
    return (4 * p) // 5


def b_max_for_tail(p: int) -> int:
    """返回 q=P-2b>floor(4P/5) 的最大 b。"""
    return (p - cutoff_alpha45(p) - 1) // 2


def square_prime_count(p: int, sign: str, prime_flags: bytearray) -> int:
    """计算 P^2 正负半窗内的素数个数。"""
    base = p * p
    total = 0
    for r_value in range(1, p):
        n_value = base + r_value if sign == "plus" else base - r_value
        if prime_flags[n_value]:
            total += 1
    return total


def phase_data(p: int, b_value: int) -> dict[str, int | bool]:
    """返回 b 的层和无槽相位数据。"""
    q_value = p - 2 * b_value
    h_value = (p - 1) // 2
    k_value, residue = divmod(2 * b_value * b_value, q_value)
    plus_no = residue < q_value - h_value
    minus_no = residue > h_value
    return {
        "q": q_value,
        "k": k_value,
        "s": residue,
        "plus_no_slot": plus_no,
        "minus_no_slot": minus_no,
        "both_raw": not plus_no and not minus_no,
    }


def side_no_slot(data: dict[str, int | bool], side: str) -> bool:
    """判断给定方向是否无槽。"""
    if side == "plus":
        return bool(data["plus_no_slot"])
    if side == "minus":
        return bool(data["minus_no_slot"])
    raise ValueError(f"unknown side: {side}")


def layer_atoms_for_side(p: int, side: str, prime_flags: bytearray) -> list[dict[str, Any]]:
    """把固定 P、方向的无槽集合拆成 k 层整数区间原子。"""
    atoms: list[dict[str, Any]] = []
    open_atom: dict[str, Any] | None = None
    for b_value in range(1, b_max_for_tail(p) + 1):
        data = phase_data(p, b_value)
        if side_no_slot(data, side):
            k_value = int(data["k"])
            if open_atom is None or open_atom["k"] != k_value or b_value != open_atom["b_hi"] + 1:
                if open_atom is not None:
                    atoms.append(open_atom)
                open_atom = {
                    "k": k_value,
                    "b_lo": b_value,
                    "b_hi": b_value,
                    "length": 1,
                    "prime_load": 0,
                    "q_values": [],
                }
            else:
                open_atom["b_hi"] = b_value
                open_atom["length"] += 1
            q_value = int(data["q"])
            if prime_flags[q_value]:
                open_atom["prime_load"] += 1
                if len(open_atom["q_values"]) < 8:
                    open_atom["q_values"].append(q_value)
        elif open_atom is not None:
            atoms.append(open_atom)
            open_atom = None
    if open_atom is not None:
        atoms.append(open_atom)
    return atoms


def direct_no_slot_prime_count(p: int, side: str, prime_flags: bytearray) -> int:
    """直接数无槽尾素。"""
    total = 0
    for b_value in range(1, b_max_for_tail(p) + 1):
        data = phase_data(p, b_value)
        if side_no_slot(data, side) and prime_flags[int(data["q"])]:
            total += 1
    return total


def verify_atom_monotone(p: int, side: str, atoms: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """检查每个 k 是否只形成一个区间原子。"""
    by_k: dict[int, int] = {}
    failures = []
    for atom in atoms:
        k_value = int(atom["k"])
        by_k[k_value] = by_k.get(k_value, 0) + 1
    for k_value, count in sorted(by_k.items()):
        if count > 1:
            failures.append({"p": p, "side": side, "k": k_value, "atom_count": count})
    return failures


def audit_p(p: int, prime_flags: bytearray) -> dict[str, Any]:
    """审计单个 P 的双侧层区间。"""
    plus_atoms = layer_atoms_for_side(p, "plus", prime_flags)
    minus_atoms = layer_atoms_for_side(p, "minus", prime_flags)
    plus_direct = direct_no_slot_prime_count(p, "plus", prime_flags)
    minus_direct = direct_no_slot_prime_count(p, "minus", prime_flags)
    plus_atom_load = sum(atom["prime_load"] for atom in plus_atoms)
    minus_atom_load = sum(atom["prime_load"] for atom in minus_atoms)
    plus_prime = square_prime_count(p, "plus", prime_flags)
    minus_prime = square_prime_count(p, "minus", prime_flags)
    plus_threshold = (plus_prime + 1) // 2
    minus_threshold = (minus_prime + 1) // 2
    plus_large = plus_atom_load >= plus_threshold
    minus_large = minus_atom_load >= minus_threshold
    plus_max_atom = max(plus_atoms, key=lambda item: item["prime_load"], default=None)
    minus_max_atom = max(minus_atoms, key=lambda item: item["prime_load"], default=None)
    plus_atom_count = len(plus_atoms)
    minus_atom_count = len(minus_atoms)
    plus_forced_load = (
        0 if plus_atom_count == 0 else (plus_threshold + plus_atom_count - 1) // plus_atom_count
    )
    minus_forced_load = (
        0 if minus_atom_count == 0 else (minus_threshold + minus_atom_count - 1) // minus_atom_count
    )
    plus_logic_ok = True
    minus_logic_ok = True
    if plus_large and plus_max_atom is not None:
        plus_logic_ok = plus_max_atom["prime_load"] >= plus_forced_load
    if minus_large and minus_max_atom is not None:
        minus_logic_ok = minus_max_atom["prime_load"] >= minus_forced_load

    return {
        "p": p,
        "b_max": b_max_for_tail(p),
        "plus_prime_window": plus_prime,
        "minus_prime_window": minus_prime,
        "plus_no_slot_direct": plus_direct,
        "minus_no_slot_direct": minus_direct,
        "plus_no_slot_atom_load": plus_atom_load,
        "minus_no_slot_atom_load": minus_atom_load,
        "plus_atom_count": plus_atom_count,
        "minus_atom_count": minus_atom_count,
        "plus_max_atom": plus_max_atom,
        "minus_max_atom": minus_max_atom,
        "plus_threshold_half_primewindow": plus_threshold,
        "minus_threshold_half_primewindow": minus_threshold,
        "plus_large_branch": plus_large,
        "minus_large_branch": minus_large,
        "plus_large_branch_forces_atom_load_at_least": plus_forced_load,
        "minus_large_branch_forces_atom_load_at_least": minus_forced_load,
        "plus_atom_decomposition_delta": plus_direct - plus_atom_load,
        "minus_atom_decomposition_delta": minus_direct - minus_atom_load,
        "plus_monotone_failures": verify_atom_monotone(p, "plus", plus_atoms),
        "minus_monotone_failures": verify_atom_monotone(p, "minus", minus_atoms),
        "plus_logic_ok": plus_logic_ok,
        "minus_logic_ok": minus_logic_ok,
        "plus_atom_samples": plus_atoms[:6],
        "minus_atom_samples": minus_atoms[:6],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "layer_interval_atomization",
            "status": "closed",
            "statement": "For fixed P, side, and floor layer k, the no-slot b-support is one integer interval.",
        },
        {
            "name": "noslot_prime_load_identity",
            "status": "closed",
            "statement": "NoSlotTailPrime^side(P) is the sum of prime loads of q=P-2b over those layer intervals.",
        },
        {
            "name": "large_branch_forces_layer_atom",
            "status": "closed",
            "statement": "If NoSlotTailPrime^side(P)>=PrimeWindow^side(P)/2, one layer interval atom has load at least the pigeonhole quotient.",
        },
        {
            "name": "moving_layer_prime_load_bound",
            "status": "open",
            "statement": "A global proof needs a prime-load bound for q=P-2b in every moving layer interval, or a PDEC/SAE exclusion.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "LayerIntervalAtomizationClosed",
            "closed": result["monotone_failure_count"] == 0,
            "proved": True,
            "meaning": "固定 k 的无槽支撑是单一区间原子。",
            "remaining": "closed",
        },
        {
            "gate": "NoSlotPrimeLoadIdentityClosed",
            "closed": result["atom_decomposition_failure_count"] == 0,
            "proved": True,
            "meaning": "无槽尾素数等于层区间内 q=P-2b 取素的负载和。",
            "remaining": "closed",
        },
        {
            "gate": "LargeBranchForcesAtomClosed",
            "closed": result["large_branch_logic_failure_count"] == 0,
            "proved": True,
            "meaning": "大无槽分支会强制至少一个层区间原子出现高 prime-load。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoLargeNoSlotBranch",
            "closed": result["finite_large_branch_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 没有大无槽分支。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalMovingLayerPrimeLoadBound",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥 moving layer interval 中 q=P-2b 的高素数负载。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只登记层区间原子，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * max_p + max_p)
    primes = primes_from_flags(prime_flags, max_p)
    p_values = [p for p in primes if 3 <= p <= max_p]
    records = [audit_p(p, prime_flags) for p in p_values]

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    atom_decomposition_failures = [
        record
        for record in records
        if record["plus_atom_decomposition_delta"] != 0
        or record["minus_atom_decomposition_delta"] != 0
    ]
    monotone_failures = [
        record
        for record in records
        if record["plus_monotone_failures"] or record["minus_monotone_failures"]
    ]
    large_branch_records = [
        record for record in records if record["plus_large_branch"] or record["minus_large_branch"]
    ]
    large_branch_logic_failures = [
        record for record in records if not record["plus_logic_ok"] or not record["minus_logic_ok"]
    ]
    max_plus_atom_record = max(
        records,
        key=lambda record: (record["plus_max_atom"] or {"prime_load": -1})["prime_load"],
        default=None,
    )
    max_minus_atom_record = max(
        records,
        key=lambda record: (record["minus_max_atom"] or {"prime_load": -1})["prime_load"],
        default=None,
    )

    aggregate = {
        "plus_prime_window": sum(record["plus_prime_window"] for record in records),
        "minus_prime_window": sum(record["minus_prime_window"] for record in records),
        "plus_no_slot": sum(record["plus_no_slot_atom_load"] for record in records),
        "minus_no_slot": sum(record["minus_no_slot_atom_load"] for record in records),
        "plus_atom_count": sum(record["plus_atom_count"] for record in records),
        "minus_atom_count": sum(record["minus_atom_count"] for record in records),
        "max_plus_atom_load": (
            (max_plus_atom_record["plus_max_atom"] or {"prime_load": 0})["prime_load"]
            if max_plus_atom_record
            else 0
        ),
        "max_minus_atom_load": (
            (max_minus_atom_record["minus_max_atom"] or {"prime_load": 0})["prime_load"]
            if max_minus_atom_record
            else 0
        ),
    }
    aggregate["combined_prime_window"] = aggregate["plus_prime_window"] + aggregate["minus_prime_window"]
    aggregate["combined_no_slot"] = aggregate["plus_no_slot"] + aggregate["minus_no_slot"]
    aggregate["combined_atom_count"] = aggregate["plus_atom_count"] + aggregate["minus_atom_count"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "atom_decomposition_failure_count": len(atom_decomposition_failures),
        "monotone_failure_count": len(monotone_failures),
        "finite_large_branch_count": len(large_branch_records),
        "large_branch_logic_failure_count": len(large_branch_logic_failures),
        "max_plus_atom_record": max_plus_atom_record,
        "max_minus_atom_record": max_minus_atom_record,
        "sample_records": sample_records,
        "atom_decomposition_failures": atom_decomposition_failures[:20],
        "monotone_failures": monotone_failures[:20],
        "large_branch_records": large_branch_records[:20],
        "large_branch_logic_failures": large_branch_logic_failures[:20],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_noslot_layer_interval_pdec_router",
        "status": "noslot_floor_layer_bound_reduced_to_moving_layer_prime_load_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "atom_decomposition_failure_count": len(atom_decomposition_failures),
        "monotone_failure_count": len(monotone_failures),
        "finite_large_branch_count": len(large_branch_records),
        "large_branch_logic_failure_count": len(large_branch_logic_failures),
        "max_plus_atom_record": max_plus_atom_record,
        "max_minus_atom_record": max_minus_atom_record,
        "sample_records": sample_records,
        "layer_interval_atomization_closed": len(monotone_failures) == 0,
        "noslot_prime_load_identity_closed": len(atom_decomposition_failures) == 0,
        "large_branch_forces_layer_atom_closed": len(large_branch_logic_failures) == 0,
        "moving_layer_prime_load_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_noslot_layer_interval_pdec_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-noslot-layer-interval-pdec-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 `NoSlotFloorLayerBandBoundOrLayerPDEC` 进一步原子化。"
            "固定 `P`、方向和 floor layer `k` 后，无槽支撑在 `b` 轴上是一个整数区间；"
            "无槽尾素数正是这些区间里线性型 `q=P-2b` 取素的 prime-load 总和。"
            "若无槽分支达到 `PrimeWindow/2`，则某个 moving layer interval 必有鸽巢强制的高 prime-load。"
            "这不是全局闭合；剩余是证明所有 moving layer prime-load 上界，或把持久高负载登记并排斥为 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    max_plus = result["max_plus_atom_record"]
    max_minus = result["max_minus_atom_record"]
    lines = [
        "# Prime Matrix square-phase no-slot layer interval PDEC router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"atom_decomposition_failure_count={result['atom_decomposition_failure_count']}",
        f"monotone_failure_count={result['monotone_failure_count']}",
        f"finite_large_branch_count={result['finite_large_branch_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 层区间原子",
        "",
        "固定 `P,side,k` 后，`b` 必须同时满足 floor-layer 条件和对应端带条件。由于相应二次函数在 `b>0` 上严格递增，支撑只能是一个整数区间：",
        "",
        "```text",
        "2b^2 = k(P-2b)+s, 0<=s<P-2b.",
        "plus:  s < P-2b-(P-1)/2",
        "minus: s > (P-1)/2.",
        "```",
        "",
        "无槽尾素数于是变成这些区间里 `P-2b` 为素数的负载和。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| plus PrimeWindow | {agg['plus_prime_window']} |",
        f"| minus PrimeWindow | {agg['minus_prime_window']} |",
        f"| plus no-slot load | {agg['plus_no_slot']} |",
        f"| minus no-slot load | {agg['minus_no_slot']} |",
        f"| plus atom count | {agg['plus_atom_count']} |",
        f"| minus atom count | {agg['minus_atom_count']} |",
        f"| max plus atom load | {agg['max_plus_atom_load']} |",
        f"| max minus atom load | {agg['max_minus_atom_load']} |",
        "",
        "## 3. 最大原子",
        "",
        "| side | P | k | b interval | length | prime load | sample q |",
        "| --- | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    if max_plus and max_plus["plus_max_atom"]:
        atom = max_plus["plus_max_atom"]
        lines.append(
            f"| plus | {max_plus['p']} | {atom['k']} | [{atom['b_lo']},{atom['b_hi']}] | "
            f"{atom['length']} | {atom['prime_load']} | `{atom['q_values']}` |"
        )
    if max_minus and max_minus["minus_max_atom"]:
        atom = max_minus["minus_max_atom"]
        lines.append(
            f"| minus | {max_minus['p']} | {atom['k']} | [{atom['b_lo']},{atom['b_hi']}] | "
            f"{atom['length']} | {atom['prime_load']} | `{atom['q_values']}` |"
        )

    lines.extend(
        [
            "",
            "## 4. 样本表",
            "",
            "| P | plus prime | plus no-slot | plus atoms | plus max load | minus prime | minus no-slot | minus atoms | minus max load |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        plus_max = (row["plus_max_atom"] or {"prime_load": 0})["prime_load"]
        minus_max = (row["minus_max_atom"] or {"prime_load": 0})["prime_load"]
        lines.append(
            f"| {row['p']} | {row['plus_prime_window']} | {row['plus_no_slot_atom_load']} | "
            f"{row['plus_atom_count']} | {plus_max} | {row['minus_prime_window']} | "
            f"{row['minus_no_slot_atom_load']} | {row['minus_atom_count']} | {minus_max} |"
        )

    lines.extend(
        [
            "",
            "## 5. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    lines.extend(
        [
            "",
            "## 6. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
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
            "- 该目标必须处理 moving layer interval 中 `q=P-2b` 的素数负载；本步没有用有限样本替代全局证明。",
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_ints(raw: str) -> list[int]:
    """解析整数列表。"""
    return [int(item) for item in raw.split(",") if item.strip()]


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--sample-ps", default="13,17,19,23,29,31,101,499,1009,2003,4999")
    args = parser.parse_args()

    result = build_result(max_p=args.max_p, sample_ps=parse_ints(args.sample_ps))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["parameters"]["max_p"],
                "atom_decomposition_failure_count": result["atom_decomposition_failure_count"],
                "monotone_failure_count": result["monotone_failure_count"],
                "finite_large_branch_count": result["finite_large_branch_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
