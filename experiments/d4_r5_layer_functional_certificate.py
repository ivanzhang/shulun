#!/usr/bin/env python3
"""D4/R5 层泛函有限单元证书原型。

用法示例：
  python3 experiments/d4_r5_layer_functional_certificate.py \
    --units "1088472:1088477,1088496:1088499,1088506:1088507,1088551:1088555" \
    --H 80 --hi 400 --q 0.958 --threshold-tau 60 \
    --json docs/d4-r5-light-H80-layer-functional-certificate.json

说明：
  该脚本复用 d4_lowblock_phase_capacity 的 term_rows/offset_stats 口径，
  对每个 H80 资源锁相位单元逐行重算 U,V,L,E2,W,N,M，并输出 bound 查询。
  目前仍是有限整数单元证书；下一步与 phasecell root 证书合并以覆盖开单元极值。
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

# 允许直接从仓库根目录运行脚本。
sys.path.insert(0, str(Path(__file__).resolve().parent))
from d4_lowblock_phase_capacity import build, offset_stats, term_rows  # noqa: E402


def parse_units(raw: str) -> list[tuple[int, int]]:
    """解析 a:b,c:d 形式的闭区间单元。"""
    units = []
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        left, right = item.split(":", 1)
        units.append((int(left), int(right)))
    return units


def classify_offsets(offsets: list[dict], threshold_tau: int) -> tuple[list[dict], list[dict], list[dict]]:
    """返回 light、transition、short_chain 三类异常偏移。"""
    light = [item for item in offsets if item["tau_sum"] < threshold_tau]
    heavy = [item for item in offsets if item["tau_sum"] >= threshold_tau]
    transition = [item for item in heavy if 20 < item["count"] <= 25]
    short_chain = [item for item in heavy if item["count"] <= 20]
    return light, transition, short_chain


def layer_summary_for_x(x: int, hi: int, q: float, threshold_tau: int, H: int, tau: list[int], prefix: list[int]) -> dict:
    """计算单行的 H 前缀/尾部 light 层与异常层势能。"""
    rows = term_rows(x, hi, q, tau, prefix)
    offsets = offset_stats(x, rows)
    light, transition, short_chain = classify_offsets(offsets, threshold_tau)
    exceptional = light + transition + short_chain
    prefix_light = [item for item in light if item["offset"] <= H]
    tail_light = [item for item in light if item["offset"] > H]

    def total(items: list[dict], key: str = "positive_contract_sum") -> float:
        return sum(item[key] for item in items)

    def energy(items: list[dict]) -> float:
        return sum(item["positive_contract_sum"] ** 2 for item in items)

    def weight(items: list[dict]) -> int:
        return sum(item["tau_sum"] for item in items)

    def count(items: list[dict]) -> int:
        return sum(item["count"] for item in items)

    L = total(exceptional)
    E2 = energy(exceptional)
    U = total(prefix_light)
    V = total(tail_light)
    light_L = total(light)
    return {
        "x": x,
        "L": L,
        "E2": E2,
        "ratio": E2 / (L * L) if L else None,
        "potential": E2 - L * L / 20.0,
        "U": U,
        "V": V,
        "light_L": light_L,
        "light_E2": energy(light),
        "short_L": total(short_chain),
        "transition_L": total(transition),
        "W_pref": weight(prefix_light),
        "N_pref": count(prefix_light),
        "M_pref": len(prefix_light),
        "W_tail": weight(tail_light),
        "N_tail": count(tail_light),
        "M_tail": len(tail_light),
        "light_count": len(light),
        "transition_count": len(transition),
        "short_chain_count": len(short_chain),
        "top_pref": sorted(prefix_light, key=lambda item: item["positive_contract_sum"], reverse=True)[:10],
        "top_tail": sorted(tail_light, key=lambda item: item["positive_contract_sum"], reverse=True)[:10],
    }


def max_row(rows: list[dict], key: str, predicate=lambda row: True) -> dict | None:
    """在满足谓词的行中按 key 取最大。"""
    selected = [row for row in rows if predicate(row)]
    return max(selected, key=lambda row: row[key]) if selected else None


def min_row(rows: list[dict], key: str, predicate=lambda row: True) -> dict | None:
    """在满足谓词的行中按 key 取最小。"""
    selected = [row for row in rows if predicate(row)]
    return min(selected, key=lambda row: row[key]) if selected else None


def compact_witness(row: dict | None) -> dict | None:
    """压缩 witness，保留审查所需字段。"""
    if row is None:
        return None
    keys = [
        "x",
        "L",
        "E2",
        "ratio",
        "potential",
        "U",
        "V",
        "light_L",
        "short_L",
        "transition_L",
        "W_pref",
        "N_pref",
        "M_pref",
        "W_tail",
        "N_tail",
        "M_tail",
    ]
    return {key: row[key] for key in keys if key in row}


def make_check(name: str, predicate: str, bound: float, observed_key: str, witness: dict | None, sense: str = "<=") -> dict:
    """构造单条界证书。"""
    observed = None if witness is None else witness[observed_key]
    if observed is None:
        ok = True
    elif sense == "<=":
        ok = observed <= bound
    elif sense == ">=":
        ok = observed >= bound
    else:
        raise ValueError(f"unknown sense: {sense}")
    return {
        "name": name,
        "predicate": predicate,
        "bound": bound,
        "observed": observed,
        "sense": sense,
        "ok": ok,
        "witness": compact_witness(witness),
    }


def unit_certificate(unit_id: int, start: int, end: int, args, tau: list[int], prefix: list[int]) -> dict:
    """生成一个闭整数相位单元的层泛函证书。"""
    rows = [layer_summary_for_x(x, args.hi, args.q, args.threshold_tau, args.H, tau, prefix) for x in range(start, end + 1)]
    low_prefix_light = max_row(rows, "light_L", lambda row: row["U"] < args.U_split)
    high_prefix_U = max_row(rows, "U", lambda row: row["U"] >= args.U_split)
    high_prefix_V = max_row(rows, "V", lambda row: row["U"] >= args.U_split)
    max_light = max_row(rows, "light_L")
    min_potential = min_row(rows, "potential", lambda row: row["L"] >= 0.35)
    checks = [
        make_check(
            "R5global1-local U<Hsplit implies light_L<=0.245",
            f"U < {args.U_split}",
            0.245,
            "light_L",
            low_prefix_light,
            "<=",
        ),
        make_check(
            "R5global2-local U>=Hsplit implies U<=0.182",
            f"U >= {args.U_split}",
            0.182,
            "U",
            high_prefix_U,
            "<=",
        ),
        make_check(
            "R5global2-local U>=Hsplit implies V<=0.074",
            f"U >= {args.U_split}",
            0.074,
            "V",
            high_prefix_V,
            "<=",
        ),
        make_check(
            "R5global-light-local light_L<=0.26",
            "all rows",
            0.26,
            "light_L",
            max_light,
            "<=",
        ),
        make_check(
            "R5global3-local L>=0.35 implies E2-L2/20>=0",
            "L >= 0.35",
            0.0,
            "potential",
            min_potential,
            ">=",
        ),
    ]
    return {
        "unit_id": unit_id,
        "x_range": [start, end],
        "length": end - start + 1,
        "checks": checks,
        "max_U": compact_witness(max_row(rows, "U")),
        "max_V": compact_witness(max_row(rows, "V")),
        "max_light_L": compact_witness(max_light),
        "min_potential_L_ge_035": compact_witness(min_potential),
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--units", default="1088472:1088477,1088496:1088499,1088506:1088507,1088551:1088555")
    parser.add_argument("--H", type=int, default=80)
    parser.add_argument("--hi", type=int, default=400)
    parser.add_argument("--q", type=float, default=0.958)
    parser.add_argument("--threshold-tau", type=int, default=60)
    parser.add_argument("--U-split", type=float, default=0.16)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    units = parse_units(args.units)
    max_end = max(end for _, end in units)
    tau, prefix = build(2 * max_end + 10)
    unit_payloads = [unit_certificate(i + 1, start, end, args, tau, prefix) for i, (start, end) in enumerate(units)]
    all_checks = [check for unit in unit_payloads for check in unit["checks"]]
    payload = {
        "certificate_type": "D4-R5-layer-functional-unit-certificate",
        "status": "finite integer-unit certificate; phasecell root integration still required for open-cell global closure",
        "H": args.H,
        "hi": args.hi,
        "q": args.q,
        "threshold_tau": args.threshold_tau,
        "U_split": args.U_split,
        "units": unit_payloads,
        "all_checks_ok": all(check["ok"] for check in all_checks),
        "failed_checks": [check for check in all_checks if not check["ok"]],
    }
    print(
        json.dumps(
            {
                "certificate_type": payload["certificate_type"],
                "all_checks_ok": payload["all_checks_ok"],
                "unit_count": len(unit_payloads),
                "failed_checks": payload["failed_checks"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
