#!/usr/bin/env python3
"""Prime Matrix 调和窗口 Dusart 显式账本路由器。

用法示例：
  python3 experiments/prime_matrix_harmonic_window_dusart_ledger_router.py

输出：
  docs/monograph/prime-matrix-harmonic-window-dusart-ledger-router.json
  docs/monograph/prime-matrix-harmonic-window-dusart-ledger-router.md
"""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-high-segment-model-gap-factorization-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-harmonic-window-dusart-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-harmonic-window-dusart-ledger-router.md"

HARMONIC_ATOM = "HarmonicWindowAlpha043PGe3001Upper0850Ledger"
SKELETON_ATOM = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
EXTERNAL_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
CLOSED_ATOM = "DusartPrimeReciprocalWindowAlpha043Upper0850Closed"

ALPHA = 0.43
TAIL_START = 500_000
FINITE_START = 3001
TARGET = 0.850
DUSART_UPPER_VALID = 10_372
DUSART_SOURCE = "https://arxiv.org/abs/1002.0442"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def sieve_primes(limit: int) -> list[int]:
    """生成不超过 limit 的素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return [idx for idx, flag in enumerate(flags) if flag]


def prefix_reciprocals(primes: list[int]) -> list[float]:
    """素数倒数前缀和。"""
    total = 0.0
    values: list[float] = []
    for prime in primes:
        total += 1.0 / prime
        values.append(total)
    return values


def harmonic_window_for_prime(p: int, primes: list[int], prefix: list[float]) -> float:
    """计算 sum_{floor(P^alpha)<q<P} 1/q。"""
    cutoff = int(p**ALPHA)
    low_idx = bisect.bisect_right(primes, cutoff) - 1
    high_idx = bisect.bisect_left(primes, p) - 1
    high_sum = prefix[high_idx] if high_idx >= 0 else 0.0
    low_sum = prefix[low_idx] if low_idx >= 0 else 0.0
    return high_sum - low_sum


def finite_audit(start: int, stop: int) -> dict[str, Any]:
    """精确核查 start<=P<stop 的调和窗口。"""
    primes = sieve_primes(stop)
    prefix = prefix_reciprocals(primes)
    records = []
    for p in primes:
        if p < start or p >= stop:
            continue
        value = harmonic_window_for_prime(p, primes, prefix)
        records.append({"p": p, "cutoff": int(p**ALPHA), "harmonic": value})
    worst = max(records, key=lambda row: row["harmonic"])
    return {
        "start": start,
        "stop": stop,
        "prime_count": len(records),
        "max_harmonic": worst["harmonic"],
        "max_record": worst,
        "target": TARGET,
        "pass": worst["harmonic"] <= TARGET,
    }


def dusart_error(log_x: float) -> float:
    """Dusart 素数倒数和误差项。"""
    return 1.0 / (10.0 * log_x**2) + 4.0 / (15.0 * log_x**3)


def dusart_tail_bound(p: int) -> dict[str, Any]:
    """计算 P>=p 的 Dusart 尾段上界。"""
    log_p = math.log(p)
    log_y = ALPHA * log_p
    base = math.log(1.0 / ALPHA)
    error_p = dusart_error(log_p)
    error_y = dusart_error(log_y)
    bound = base + error_p + error_y
    return {
        "tail_start": p,
        "alpha": ALPHA,
        "log_start": log_p,
        "log_y_start": log_y,
        "y_start": p**ALPHA,
        "base_log_1_over_alpha": base,
        "error_at_p": error_p,
        "error_at_y": error_y,
        "bound": bound,
        "target": TARGET,
        "dusart_upper_valid": p >= DUSART_UPPER_VALID,
        "pass": bound <= TARGET and p >= DUSART_UPPER_VALID,
    }


def remove_atom(text: str, atom: str) -> str:
    """从 AND 输入基中删除闭合原子。"""
    updated = text
    for pattern in (
        f"({atom} AND ",
        f" AND {atom})",
        f" AND {atom} AND ",
        f"{atom} AND ",
        f" AND {atom}",
        atom,
    ):
        if pattern == f"({atom} AND ":
            updated = updated.replace(pattern, "(")
        elif pattern == f" AND {atom})":
            updated = updated.replace(pattern, ")")
        elif pattern == f" AND {atom} AND ":
            updated = updated.replace(pattern, " AND ")
        else:
            updated = updated.replace(pattern, "")
    updated = updated.replace("(AND ", "(").replace(" AND )", ")")
    return " ".join(updated.split())


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], finite: dict[str, Any], tail: dict[str, Any]) -> list[dict[str, Any]]:
    """生成调和窗口判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == HARMONIC_ATOM and HARMONIC_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    theorem_specialized = (
        tail["pass"]
        and tail["y_start"] > 1.0
        and tail["dusart_upper_valid"]
        and tail["bound"] < TARGET
    )
    harmonic_closed = active and guard and finite["pass"] and theorem_specialized
    return [
        row(
            "HarmonicWindowGateActive",
            active,
            False,
            "最新最窄点是 P>=3001 的高素窗口调和和上界。",
            HARMONIC_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍在假设早期零行反例链条的模型余量账本内，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FiniteHarmonicWindow3001To499999",
            finite["pass"],
            True,
            "3001<=P<500000 的素数窗口已精确枚举，最大调和和仍小于 0.850。",
            "有限段关闭。",
        ),
        row(
            "DusartPrimeReciprocalTheoremSpecialized",
            theorem_specialized,
            True,
            "Dusart 素数倒数和显式误差给出 P>=500000 的窗口上界。",
            CLOSED_ATOM,
        ),
        row(
            HARMONIC_ATOM,
            harmonic_closed,
            True,
            "有限核查与 Dusart 尾段合并，调和窗口 H(P)<=0.850 已闭合。",
            CLOSED_ATOM,
        ),
        row(
            SKELETON_ATOM,
            False,
            False,
            "动态粗骨架 S_Y(P)>=401 仍是模型余量侧的剩余解析输入。",
            SKELETON_ATOM,
        ),
        row(
            EXTERNAL_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path], finite_stop: int) -> dict[str, Any]:
    """执行调和窗口路由。"""
    previous = load_json(paths["previous"])
    finite = finite_audit(FINITE_START, finite_stop)
    tail = dusart_tail_bound(finite_stop)
    rows = build_rows(previous, finite, tail)
    harmonic_closed = next(bool(item["closed"]) for item in rows if item["gate"] == HARMONIC_ATOM)
    latest_self = remove_atom(previous.get("latest_self_contained_basis", ""), HARMONIC_ATOM)
    latest_cond = remove_atom(previous.get("latest_conditional_basis", ""), HARMONIC_ATOM)
    latest_global = remove_atom(previous.get("latest_global_with_external_basis", ""), HARMONIC_ATOM)

    source_paths = list(paths.values())
    return {
        "certificate_type": "harmonic_window_dusart_ledger_router",
        "status": "harmonic_window_alpha043_upper0850_closed_skeleton_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "external_standard_theorem_used": "Dusart reciprocal prime sum explicit estimate",
        "external_standard_theorem_source": DUSART_SOURCE,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "harmonic_window_alpha043_upper0850_closed": harmonic_closed,
        "dynamic_rough_skeleton_lower401_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "closed_input_removed": HARMONIC_ATOM,
        "closed_interface_atom": CLOSED_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "replacement": {HARMONIC_ATOM: CLOSED_ATOM},
        "next_priority": SKELETON_ATOM,
        "external_next_priority": EXTERNAL_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "finite_audit": finite,
        "dusart_tail_bound": tail,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步关闭调和窗口上界。有限段 3001<=P<500000 直接精确枚举，最大值为 "
            f"{finite['max_harmonic']:.12f}；尾段 P>=500000 用 Dusart 素数倒数和显式误差，"
            f"得到统一上界 {tail['bound']:.12f}<0.850。"
            "因此 HarmonicWindowAlpha043PGe3001Upper0850Ledger 可从活动输入基中删除，"
            "下一最窄点转为动态粗骨架下界 S_Y(P)>=401。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    finite = result["finite_audit"]
    tail = result["dusart_tail_bound"]
    lines = [
        "# Prime Matrix 调和窗口 Dusart 显式账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"harmonic_window_alpha043_upper0850_closed={fmt_bool(result['harmonic_window_alpha043_upper0850_closed'])}",
        f"dynamic_rough_skeleton_lower401_proved={fmt_bool(result['dynamic_rough_skeleton_lower401_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"closed_input_removed={result['closed_input_removed']}",
        f"closed_interface_atom={result['closed_interface_atom']}",
        "```",
        "",
        "## 1. 闭合律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "  => 从活动输入基删除该调和窗口门。",
        "```",
        "",
        "使用的标准显式定理：Dusart, *Estimates of some functions over primes without R.H.*, arXiv:1002.0442。其素数倒数和定理给出上下误差项 `1/(10 log^2 x)+4/(15 log^3 x)`；上界侧要求 `x>=10372`，本路由尾段从 `P=500000` 起满足。",
        "",
        "## 2. 两段账本",
        "",
        "| segment | count/bound | worst | target | closed |",
        "| --- | ---: | --- | ---: | --- |",
        (
            f"| finite 3001<=P<500000 | {finite['prime_count']} primes | "
            f"P={finite['max_record']['p']}, cutoff={finite['max_record']['cutoff']}, "
            f"H={finite['max_harmonic']:.12f} | {finite['target']:.3f} | {fmt_bool(finite['pass'])} |"
        ),
        (
            f"| Dusart P>=500000 | bound | "
            f"log(1/alpha)+err(P)+err(P^alpha)={tail['bound']:.12f} | "
            f"{tail['target']:.3f} | {fmt_bool(tail['pass'])} |"
        ),
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            "下一步直接攻 `DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger`：证明把所有 `q<=P^0.43` 提升进底座后，`1<=k<P` 中避开这些低素同余类的动态粗骨架在 plus/minus 两侧均至少 `401`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--finite-stop", type=int, default=TAIL_START)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths, args.finite_stop)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")


if __name__ == "__main__":
    main()
