#!/usr/bin/env python3
"""审计 P^2±r 两行平方锚的层叠轮筛与逆元对齐结构。

用法示例：
  python3 experiments/prime_matrix_prime_square_pm_layered_wheel_alignment_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-prime-square-pm-layered-wheel-alignment-router.json

输出：
  data/prime-square-pm-layered-wheel-alignment-ledger.json
  docs/monograph/prime-matrix-prime-square-pm-layered-wheel-alignment-router.json
  docs/monograph/prime-matrix-prime-square-pm-layered-wheel-alignment-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-square-pm-layered-wheel-alignment-ledger.json"
OUT_JSON = DOCS / "prime-matrix-prime-square-pm-layered-wheel-alignment-router.json"
OUT_MD = DOCS / "prime-matrix-prime-square-pm-layered-wheel-alignment-router.md"

PLUS_INPUT = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"
MINUS_INPUT = "PrimeInLastHalfBeforePrimeSquareForEveryPrimeP"
LAYERED_INPUT = "TwoSidedSquarePhaseLayeredWheelSurvivorLowerBound"
TERMINAL_RETURN = "TerminalSquarePhasePDECSAEOrColumnCRTReturn"


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int | None = None) -> list[int]:
    """从筛表提取素数。"""
    end = len(flags) if limit is None else min(limit + 1, len(flags))
    return [idx for idx in range(2, end) if flags[idx]]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def wheel_product(primes: list[int]) -> int:
    """计算轮模。"""
    value = 1
    for prime in primes:
        value *= prime
    return value


def cover_residue(p: int, q: int, sign: str) -> int:
    """返回 r 坐标中被 q 覆盖的唯一正残基。

    plus:  q | P^2 + r  iff r == -P^2 mod q.
    minus: q | P^2 - r  iff r ==  P^2 mod q.
    """
    p2_mod = (p * p) % q
    residue = (-p2_mod) % q if sign == "plus" else p2_mod
    return q if residue == 0 else residue


def covered_vector(p: int, qs: list[int], sign: str) -> bytearray:
    """按给定 q 集合标记 1<=r<P 中已覆盖的位置。"""
    covered = bytearray(p)
    for q in qs:
        if q >= p:
            continue
        residue = cover_residue(p, q, sign)
        for r_value in range(residue, p, q):
            covered[r_value] = 1
    return covered


def survivors_from_qs(p: int, qs: list[int], sign: str) -> list[int]:
    """返回未被给定 q 集合覆盖的 r。"""
    covered = covered_vector(p, qs, sign)
    return [r_value for r_value in range(1, p) if not covered[r_value]]


def mirror_law_holds(p: int, qs: list[int]) -> bool:
    """检查奇素数层的正负残基互为相反数，q=2 同类。"""
    for q in qs:
        if q >= p:
            continue
        plus = cover_residue(p, q, "plus") % q
        minus = cover_residue(p, q, "minus") % q
        if q == 2:
            if plus != minus:
                return False
        elif (plus + minus) % q != 0 or plus == minus:
            return False
    return True


def primality_equivalence_holds(p: int, qs: list[int], prime_flags: bytearray, sign: str) -> bool:
    """检查最终未覆盖列与平方锚邻域素数完全一致。"""
    full_survivors = set(survivors_from_qs(p, qs, sign))
    for r_value in range(1, p):
        value = p * p + r_value if sign == "plus" else p * p - r_value
        if (r_value in full_survivors) != bool(prime_flags[value]):
            return False
    return True


def layer_rows_for_p(
    p: int,
    prime_list: list[int],
    wheel_cutoffs: list[int],
    prime_flags: bytearray,
) -> list[dict[str, Any]]:
    """生成单个 P 的轮层计数。"""
    rows: list[dict[str, Any]] = []
    previous_plus: set[int] | None = None
    previous_minus: set[int] | None = None
    for cutoff in wheel_cutoffs:
        qs = [q for q in prime_list if q < p and q <= cutoff]
        if not qs:
            continue
        plus_survivors = set(survivors_from_qs(p, qs, "plus"))
        minus_survivors = set(survivors_from_qs(p, qs, "minus"))
        both_survivors = plus_survivors & minus_survivors
        plus_killed = None if previous_plus is None else len(previous_plus - plus_survivors)
        minus_killed = None if previous_minus is None else len(previous_minus - minus_survivors)
        rows.append(
            {
                "cutoff": cutoff,
                "wheel_modulus": wheel_product(qs),
                "q_count": len(qs),
                "plus_survivor_count": len(plus_survivors),
                "minus_survivor_count": len(minus_survivors),
                "both_side_survivor_count": len(both_survivors),
                "least_plus_r": min(plus_survivors) if plus_survivors else None,
                "least_minus_r": min(minus_survivors) if minus_survivors else None,
                "least_both_r": min(both_survivors) if both_survivors else None,
                "plus_killed_from_previous": plus_killed,
                "minus_killed_from_previous": minus_killed,
                "mirror_residue_law_holds": mirror_law_holds(p, qs),
            }
        )
        previous_plus = plus_survivors
        previous_minus = minus_survivors

    final_qs = [q for q in prime_list if q < p]
    plus_final = set(survivors_from_qs(p, final_qs, "plus"))
    minus_final = set(survivors_from_qs(p, final_qs, "minus"))
    both_final = plus_final & minus_final
    rows.append(
        {
            "cutoff": "q<P",
            "wheel_modulus": None,
            "q_count": len(final_qs),
            "plus_survivor_count": len(plus_final),
            "minus_survivor_count": len(minus_final),
            "both_side_survivor_count": len(both_final),
            "least_plus_r": min(plus_final) if plus_final else None,
            "least_minus_r": min(minus_final) if minus_final else None,
            "least_both_r": min(both_final) if both_final else None,
            "least_plus_value": None if not plus_final else p * p + min(plus_final),
            "least_minus_value": None if not minus_final else p * p - min(minus_final),
            "least_both_values": None
            if not both_final
            else [p * p - min(both_final), p * p + min(both_final)],
            "least_plus_prime": None if not plus_final else bool(prime_flags[p * p + min(plus_final)]),
            "least_minus_prime": None if not minus_final else bool(prime_flags[p * p - min(minus_final)]),
            "least_both_prime_pair": None
            if not both_final
            else bool(prime_flags[p * p - min(both_final)] and prime_flags[p * p + min(both_final)]),
            "plus_primality_equivalence_holds": primality_equivalence_holds(p, final_qs, prime_flags, "plus"),
            "minus_primality_equivalence_holds": primality_equivalence_holds(p, final_qs, prime_flags, "minus"),
            "mirror_residue_law_holds": mirror_law_holds(p, final_qs),
        }
    )
    return rows


def audit_p(
    p: int,
    prime_list: list[int],
    wheel_cutoffs: list[int],
    prime_flags: bytearray,
) -> dict[str, Any]:
    """审计单个 P。"""
    layers = layer_rows_for_p(p, prime_list, wheel_cutoffs, prime_flags)
    final = layers[-1]
    return {
        "p": p,
        "layers": layers,
        "plus_full_cover": final["plus_survivor_count"] == 0,
        "minus_full_cover": final["minus_survivor_count"] == 0,
        "plus_final_survivor_count": final["plus_survivor_count"],
        "minus_final_survivor_count": final["minus_survivor_count"],
        "both_side_final_survivor_count": final["both_side_survivor_count"],
        "least_plus_r": final["least_plus_r"],
        "least_minus_r": final["least_minus_r"],
        "least_plus_value": final["least_plus_value"],
        "least_minus_value": final["least_minus_value"],
        "least_plus_prime": final["least_plus_prime"],
        "least_minus_prime": final["least_minus_prime"],
        "final_equivalence_holds": (
            final["plus_primality_equivalence_holds"]
            and final["minus_primality_equivalence_holds"]
            and final["mirror_residue_law_holds"]
        ),
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本路由器证明的确定性结构。"""
    return [
        {
            "name": "two_row_square_anchor_identity",
            "status": "closed",
            "statement": "P^2+r 是第 x=P 行第 r 列；P^2-r 是第 x=P-1 行第 P-r 列。",
        },
        {
            "name": "plus_minus_canonical_residue",
            "status": "closed",
            "statement": "q<P 覆盖 P^2+r iff r≡-P^2 mod q；覆盖 P^2-r iff r≡P^2 mod q。",
        },
        {
            "name": "quadratic_mirror_lock",
            "status": "closed",
            "statement": "P 是每个 q<P 的单位，所以 P^2 是平方类；奇 q 下正负禁类互为相反数且不重合。",
        },
        {
            "name": "inverse_alignment_specialization",
            "status": "closed",
            "statement": "plus 侧是逆元对齐系统的 x=P 特化；minus 侧是 x=P-1 反向列特化。",
        },
        {
            "name": "finite_layered_wheel_exactness",
            "status": "closed",
            "statement": "任意有限轮层只给出已加入小素数的精确合数标记；最终 q<P 层未覆盖点等价于对应平方锚素数。",
        },
        {
            "name": "global_survivor_lower_bound",
            "status": "open",
            "statement": "证明最终 q<P 层 plus 或 minus 存在幸存列，仍等价于平方根长度短区间素数输入或 PDEC 排斥。",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "TwoRowSquareAnchorCRTClosed",
            "closed": True,
            "proved": True,
            "meaning": "P^2±r 已精确接入相邻两行和逆元对齐模型。",
            "remaining": "closed",
        },
        {
            "gate": "LayeredWheelFiniteExactnessClosed",
            "closed": result["all_final_equivalences_hold"],
            "proved": True,
            "meaning": "每层轮筛给出的合数标记、最终幸存列与素数事实完全一致。",
            "remaining": "closed for finite exactness",
        },
        {
            "gate": "FinitePlusMinusNoFullCoverChecked",
            "closed": result["plus_failure_count"] == 0 and result["minus_failure_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中，前后两侧均未出现全覆盖。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "PlusGlobalSurvivorLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "证明 plus 最终层一定有幸存列就是 P^2 后长度 P 内有素数。",
            "remaining": PLUS_INPUT,
        },
        {
            "gate": "MinusGlobalSurvivorLowerBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "证明 minus 最终层一定有幸存列就是 P^2 前长度 P 内有素数。",
            "remaining": MINUS_INPUT,
        },
        {
            "gate": "TerminalFullCoverRoutesToPDEC",
            "closed": False,
            "proved": False,
            "meaning": "若假设某侧全覆盖，仍需证明层叠轮筛终端杀光必形成 PDEC/SAE/ColumnCRT 回流。",
            "remaining": TERMINAL_RETURN,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步是结构闭合和硬点压缩，不产生全局无条件矛盾。",
            "remaining": f"{LAYERED_INPUT} OR {TERMINAL_RETURN}",
        },
    ]


def build_result(max_p: int, sample_ps: list[int], wheel_cutoffs: list[int]) -> dict[str, Any]:
    """构造审计结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * max_p + max_p)
    # 覆盖方程只用 q<P<=max_p；素性判断直接查 prime_flags，避免每个 P 扫到 P^2。
    small_primes = primes_from_flags(prime_flags, max_p)
    p_values = [p for p in small_primes if p >= 3]
    sample_set = {p for p in sample_ps if p <= max_p}
    records = [audit_p(p, small_primes, wheel_cutoffs, prime_flags) for p in p_values]
    sample_records = [record for record in records if record["p"] in sample_set]
    plus_failures = [record for record in records if record["plus_full_cover"]]
    minus_failures = [record for record in records if record["minus_full_cover"]]
    equivalence_failures = [record for record in records if not record["final_equivalence_holds"]]
    worst_plus = min(records, key=lambda item: item["plus_final_survivor_count"], default=None)
    worst_minus = min(records, key=lambda item: item["minus_final_survivor_count"], default=None)
    worst_both = min(records, key=lambda item: item["both_side_final_survivor_count"], default=None)
    ledger = {
        "parameters": {
            "max_p": max_p,
            "sample_ps": sample_ps,
            "wheel_cutoffs": wheel_cutoffs,
        },
        "prime_count": len(p_values),
        "plus_failure_count": len(plus_failures),
        "minus_failure_count": len(minus_failures),
        "equivalence_failure_count": len(equivalence_failures),
        "worst_plus_record": worst_plus,
        "worst_minus_record": worst_minus,
        "worst_both_side_record": worst_both,
        "sample_records": sample_records,
        "plus_failures": plus_failures[:10],
        "minus_failures": minus_failures[:10],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_prime_square_pm_layered_wheel_alignment_router",
        "status": "p_square_pm_layered_wheel_alignment_closed_survivor_lower_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": ledger["prime_count"],
        "plus_failure_count": len(plus_failures),
        "minus_failure_count": len(minus_failures),
        "all_final_equivalences_hold": len(equivalence_failures) == 0,
        "two_row_square_anchor_crt_closed": True,
        "layered_wheel_exactness_closed": len(equivalence_failures) == 0,
        "plus_global_survivor_lower_bound_proved": False,
        "minus_global_survivor_lower_bound_proved": False,
        "terminal_full_cover_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "SquarePhaseRoughSurvivorUniformLowerBound",
        "hardpoint_after_router": f"{LAYERED_INPUT} OR {TERMINAL_RETURN}",
        "next_direct_attack_target": LAYERED_INPUT,
        "alternative_attack_target": TERMINAL_RETURN,
        "theorem_rows": theorem_rows(),
        "sample_records": sample_records,
        "worst_plus_record": worst_plus,
        "worst_minus_record": worst_minus,
        "worst_both_side_record": worst_both,
        "source_hashes": {
            "experiments/prime_matrix_prime_square_pm_layered_wheel_alignment_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/prime-square-pm-layered-wheel-alignment-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "你的 P^2 锚提示可以严格化：`P^2+r` 与 `P^2-r` 分别是相邻两行 "
            "`x=P` 与 `x=P-1` 的同一平方锚前后侧；对每个 `q<P`，合数标记只取 "
            "`r≡-P^2 mod q` 与 `r≡P^2 mod q` 两个镜像禁类。因为 `P` 是所有这些小模的单位，"
            "`P^2` 落在层叠轮筛的平方类中，所以每一层 `30,210,2310,...` 都确实给出刚性相位信息。"
            "但有限轮层只说明已加入小素数能判定哪些 r 已合成；最终 `q<P` 层仍需证明存在未覆盖 r，"
            "这正是平方根长度短区间素数硬点。新的最窄自足目标是：若最终层全覆盖，则终端杀光必须显化为 "
            "SquarePhase-PDEC/SAE/ColumnCRT；否则给出 two-sided square-phase 幸存下界。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix P^2±r 两行平方锚层叠轮筛路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"plus_failure_count={result['plus_failure_count']}",
        f"minus_failure_count={result['minus_failure_count']}",
        f"all_final_equivalences_hold={fmt_bool(result['all_final_equivalences_hold'])}",
        f"plus_global_survivor_lower_bound_proved={fmt_bool(result['plus_global_survivor_lower_bound_proved'])}",
        f"terminal_full_cover_pdec_return_proved={fmt_bool(result['terminal_full_cover_pdec_return_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 确定性结构",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    lines.extend(
        [
            "",
            "## 2. 样本最终层",
            "",
            "| P | plus survivors | least plus | minus survivors | least minus | both-side survivors |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["sample_records"]:
        lines.append(
            f"| {item['p']} | {item['plus_final_survivor_count']} | {item['least_plus_value']} | "
            f"{item['minus_final_survivor_count']} | {item['least_minus_value']} | "
            f"{item['both_side_final_survivor_count']} |"
        )

    lines.extend(
        [
            "",
            "## 3. 最紧样本",
            "",
        ]
    )
    worst_plus = result["worst_plus_record"]
    worst_minus = result["worst_minus_record"]
    worst_both = result["worst_both_side_record"]
    lines.extend(
        [
            f"- plus 侧最少幸存：`P={worst_plus['p']}`，幸存 `{worst_plus['plus_final_survivor_count']}`，最小素数 `{worst_plus['least_plus_value']}`。",
            f"- minus 侧最少幸存：`P={worst_minus['p']}`，幸存 `{worst_minus['minus_final_survivor_count']}`，最小素数 `{worst_minus['least_minus_value']}`。",
            f"- 两侧同 r 同时幸存最少样本：`P={worst_both['p']}`，数量 `{worst_both['both_side_final_survivor_count']}`。该双侧素对不是当前必需目标。",
            "",
            "## 4. 样本层叠轮筛",
            "",
            "| P | cutoff | plus survivors | minus survivors | both-side survivors | mirror law |",
            "| ---: | --- | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["sample_records"][:6]:
        for layer in item["layers"]:
            lines.append(
                f"| {item['p']} | `{layer['cutoff']}` | {layer['plus_survivor_count']} | "
                f"{layer['minus_survivor_count']} | {layer['both_side_survivor_count']} | "
                f"`{fmt_bool(layer['mirror_residue_law_holds'])}` |"
            )

    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 备选闭合口：`{result['alternative_attack_target']}`。",
            "- 不再把任意固定轮 `W` 当作全局规律；证明目标应是层层提升后，全覆盖若持续则必产生终端相位缺陷。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument("--sample-ps", default="13,17,19,23,29,31,101,499,1009,2003,4999")
    parser.add_argument("--wheel-cutoffs", default="5,7,11,13,17,19,23,29,31")
    args = parser.parse_args()

    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    wheel_cutoffs = [int(item) for item in args.wheel_cutoffs.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps, wheel_cutoffs)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["parameters"]["max_p"],
                "plus_failure_count": result["plus_failure_count"],
                "minus_failure_count": result["minus_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
