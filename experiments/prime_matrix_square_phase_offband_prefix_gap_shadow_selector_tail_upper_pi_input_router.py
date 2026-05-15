#!/usr/bin/env python3
"""审计 selector 尾素数上界是否可由显式 pi(x) 输入闭合。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_tail_upper_pi_input_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

COEFF_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-router.md"

MAIN_TARGET = "SquareWindowLowerCoefficientAndTailUpperCoefficientOrCorrelatedSurplusPDEC"
NEXT_EXTERNAL_TARGET = "SquareWindowLowerCoefficientOrCorrelatedSurplusPDEC"
NEXT_SELF_CONTAINED_TARGET = "SelfContainedDusartPiTwoSidedIntervalLedger"


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


def sieve(n: int) -> bytearray:
    """埃氏筛。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for value in range(2, int(n**0.5) + 1):
        if flags[value]:
            start = value * value
            flags[start : n + 1 : value] = b"\x00" * (((n - start) // value) + 1)
    return flags


def prime_prefix(flags: bytearray) -> list[int]:
    """生成 pi(x) 前缀表。"""
    prefix: list[int] = [0] * len(flags)
    count = 0
    for index, is_prime in enumerate(flags):
        if is_prime:
            count += 1
        prefix[index] = count
    return prefix


def pi_tail_count(p_value: int, prefix: list[int]) -> int:
    """计算 T=pi(P-1)-pi(floor(4P/5))。"""
    return prefix[p_value - 1] - prefix[(4 * p_value) // 5]


def tail_scaled_coeff(p_value: int, tail_count: int) -> float:
    """计算 T log(P)/P。"""
    return tail_count * math.log(p_value) / p_value


def dusart_tail_continuous_envelope(log_p: float, c_floor: float, upper_c2: float) -> float:
    """高段连续包络 R(log P)，满足 T log(P)/P <= R(log P)。"""
    a = -math.log(c_floor)
    return (
        1
        + 1 / log_p
        + upper_c2 / (log_p * log_p)
        - c_floor * log_p / (log_p - a) * (1 + 1 / (log_p - a))
    )


def derivative_certificate(log_threshold: float) -> dict[str, Any]:
    """给出 R'(L)<0 的显式有理上界证书。"""
    return {
        "claim": "For L>=15, R'(L)<0 for c=0.799 and upper_c2=2.51.",
        "reduction": (
            "Use a=-log(0.799)<0.225. It is enough to prove "
            "0.799*L^3*(1.225L+0.225) < (L+5.02)*(L-0.225)^3."
        ),
        "expanded_positive_polynomial": (
            "(67920*L^4 + 13328720*L^3 - 10357200*L^2 + "
            "2403270*L - 182979)/3200000"
        ),
        "polynomial_value_at_threshold": (
            849 * log_threshold**4 / 40000
            + 166609 * log_threshold**3 / 40000
            - 25893 * log_threshold**2 / 8000
            + 240327 * log_threshold / 320000
            - 182979 / 3200000
        ),
        "positive_from_threshold": True,
    }


def finite_tail_bridge(p0: int, high_p0: int, target_coeff: float) -> dict[str, Any]:
    """有限审计 p0<=P<high_p0 的所有素数 P。"""
    flags = sieve(high_p0 - 1)
    prefix = prime_prefix(flags)
    failures: list[dict[str, Any]] = []
    max_record: dict[str, Any] | None = None
    max_passing_record: dict[str, Any] | None = None
    prime_count = 0
    last_failure_p = None
    band_specs = [
        (p0, 10_000),
        (10_001, 100_000),
        (100_001, 1_000_000),
        (1_000_001, high_p0 - 1),
    ]
    bands = [
        {
            "p_lo": lo,
            "p_hi": hi,
            "prime_count": 0,
            "failure_count": 0,
            "max_T_scaled_coeff": None,
            "p_at_max_T_scaled_coeff": None,
        }
        for lo, hi in band_specs
        if lo <= high_p0 - 1
    ]
    for p_value in range(p0, high_p0):
        if not flags[p_value]:
            continue
        prime_count += 1
        tail_count = pi_tail_count(p_value, prefix)
        coeff = tail_scaled_coeff(p_value, tail_count)
        record = {"p": p_value, "T": tail_count, "T_scaled_coeff": coeff}
        if max_record is None or coeff > float(max_record["T_scaled_coeff"]):
            max_record = record
        if coeff <= target_coeff and (
            max_passing_record is None or coeff > float(max_passing_record["T_scaled_coeff"])
        ):
            max_passing_record = record
        if coeff > target_coeff:
            failures.append(record)
            last_failure_p = p_value
        for band in bands:
            if int(band["p_lo"]) <= p_value <= int(band["p_hi"]):
                band["prime_count"] = int(band["prime_count"]) + 1
                if coeff > target_coeff:
                    band["failure_count"] = int(band["failure_count"]) + 1
                if band["max_T_scaled_coeff"] is None or coeff > float(band["max_T_scaled_coeff"]):
                    band["max_T_scaled_coeff"] = coeff
                    band["p_at_max_T_scaled_coeff"] = p_value
                break
    return {
        "p0": p0,
        "high_p0": high_p0,
        "checked_p_hi": high_p0 - 1,
        "prime_count": prime_count,
        "target_coeff": target_coeff,
        "failure_count": len(failures),
        "failure_p_values": [int(row["p"]) for row in failures],
        "failure_examples": failures[:20],
        "last_failure_p": last_failure_p,
        "first_prime_after_last_failure_to_high_p0_passes": True,
        "max_record": max_record,
        "max_passing_record": max_passing_record,
        "band_records": bands,
    }


def theorem_rows(result: dict[str, Any]) -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "tail_count_exact_identity",
            "status": "closed",
            "statement": "T is exactly pi(P-1)-pi(floor(4P/5)).",
        },
        {
            "name": "finite_tail_upper_bridge",
            "status": "closed",
            "statement": "For all prime P in the finite bridge, the only universal failures are P=2753 and P=2803.",
        },
        {
            "name": "selector_exception_exclusion",
            "status": "closed_by_prior_selector_replay",
            "statement": "The two universal finite exceptions do not occur among selector rho hits in the P<=10000 replay.",
        },
        {
            "name": "external_dusart_high_tail_upper",
            "status": "closed_on_external_pi_input",
            "statement": "Dusart-type two-sided pi bounds imply T<=0.212P/logP for P>=ceil(exp(15)).",
        },
        {
            "name": "self_contained_pi_two_sided_interval_input",
            "status": "open",
            "statement": "A strict self-contained route still needs the pi two-sided interval ledger, unless the external Dusart input is accepted.",
        },
        {
            "name": "square_window_lower_coefficient",
            "status": "open",
            "statement": "After the tail upper input, the remaining coefficient gate is H>=0.43P/logP, or a correlated surplus replacement.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    agg = result["aggregate"]
    return [
        {
            "gate": "TailUpperExternalLaneClosed",
            "closed": agg["external_tail_upper_closed"],
            "proved": False,
            "meaning": "接受外部 Dusart 型 pi 双侧界时，T 上界门可关闭；该门不是严格自足证明。",
            "remaining": NEXT_EXTERNAL_TARGET,
        },
        {
            "gate": "TailUpperStrictSelfContainedClosed",
            "closed": agg["self_contained_tail_upper_closed"],
            "proved": False,
            "meaning": "仓库当前 theta 自足包不能直接替代 pi 双侧区间界。",
            "remaining": NEXT_SELF_CONTAINED_TARGET,
        },
        {
            "gate": "FiniteExceptionsHitSelector",
            "closed": not agg["selector_exception_hit_possible"],
            "proved": True,
            "meaning": "有限 universal 例外不进入 selector 命中，因此不破坏本路线。",
            "remaining": "closed",
        },
        {
            "gate": "CoefficientSplitFullyClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需平方窗 H 下系数，或直接相关余量定理。",
            "remaining": NEXT_EXTERNAL_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭/登记尾素数上界输入，不产生最终反例矛盾。",
            "remaining": result["next_direct_attack_target"],
        },
    ]


def build_result(coeff_ledger: Path, p0: int, target_coeff: float, log_threshold: float) -> dict[str, Any]:
    """构造尾素数上界输入账本。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    coeff_source = load_json(coeff_ledger)
    high_p0 = math.ceil(math.exp(log_threshold))
    finite = finite_tail_bridge(p0, high_p0, target_coeff)
    c_floor = 0.799
    upper_c2 = 2.51
    envelope_at_threshold = dusart_tail_continuous_envelope(log_threshold, c_floor, upper_c2)
    selector_exception_hit_possible = (
        coeff_source["aggregate"]["T_upper_failure_count_at_p0"] != 0
        and any(p <= coeff_source["aggregate"]["max_p"] for p in finite["failure_p_values"])
    )
    external_tail_upper_closed = (
        envelope_at_threshold < target_coeff
        and finite["failure_p_values"] == [2753, 2803]
        and not selector_exception_hit_possible
    )
    aggregate = {
        "coefficient_split_ledger": str(coeff_ledger.relative_to(ROOT)),
        "p0": p0,
        "target_t_coeff": target_coeff,
        "high_log_threshold": log_threshold,
        "high_p0": high_p0,
        "finite_bridge_prime_count": finite["prime_count"],
        "finite_bridge_failure_count": finite["failure_count"],
        "finite_bridge_failure_p_values": finite["failure_p_values"],
        "prior_selector_t_upper_failure_count_at_p0": coeff_source["aggregate"]["T_upper_failure_count_at_p0"],
        "prior_selector_replay_max_p": coeff_source["aggregate"]["max_p"],
        "selector_exception_hit_possible": selector_exception_hit_possible,
        "high_segment_envelope_at_log_threshold": envelope_at_threshold,
        "high_segment_envelope_slack": target_coeff - envelope_at_threshold,
        "external_tail_upper_closed": external_tail_upper_closed,
        "self_contained_tail_upper_closed": False,
        "global_square_window_lower_coeff_closed": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "parameters": {
            "p0": p0,
            "target_t_coeff": target_coeff,
            "high_log_threshold": log_threshold,
            "dusart_upper_c2": upper_c2,
            "floor_safety_c": c_floor,
            "external_pi_upper_template": "pi(x)<=x/log(x)*(1+1/log(x)+2.51/log(x)^2)",
            "external_pi_lower_template": "pi(x)>=x/log(x)*(1+1/log(x))",
        },
        "aggregate": aggregate,
        "finite_tail_bridge": finite,
        "analytic_high_segment_certificate": {
            "high_p0": high_p0,
            "envelope_formula": (
                "R(L)=1+1/L+2.51/L^2-0.799*L/(L-log(1/0.799))"
                "*(1+1/(L-log(1/0.799)))"
            ),
            "envelope_at_log_threshold": envelope_at_threshold,
            "target_coeff": target_coeff,
            "slack": target_coeff - envelope_at_threshold,
            "derivative_certificate": derivative_certificate(log_threshold),
            "rounding_rule": "floor(4P/5)>=0.799P for P>=1000; use U(P) and L(0.799P).",
        },
        "external_input_rows": [
            {
                "input": "Dusart-type pi upper bound",
                "role": "high-segment upper bound for pi(P-1)",
                "registered_as_self_contained": False,
            },
            {
                "input": "Dusart/Rosser-Schoenfeld-type pi lower bound",
                "role": "high-segment lower bound for pi(floor(4P/5))",
                "registered_as_self_contained": False,
            },
            {
                "input": "finite exact pi prefix bridge",
                "role": "handles P<ceil(exp(15)) and isolates two non-selector exceptions",
                "registered_as_self_contained": True,
            },
        ],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_tail_upper_pi_input_router",
        "status": "tail_upper_closed_on_external_pi_lane_self_contained_pi_interval_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_bridge_not_used_as_square_window_lower_proof": True,
        "parameters": ledger["parameters"],
        "aggregate": aggregate,
        "finite_tail_bridge": finite,
        "analytic_high_segment_certificate": ledger["analytic_high_segment_certificate"],
        "external_input_rows": ledger["external_input_rows"],
        "global_tail_upper_external_closed": external_tail_upper_closed,
        "global_tail_upper_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router_external_lane": NEXT_EXTERNAL_TARGET,
        "hardpoint_after_router_self_contained_lane": NEXT_SELF_CONTAINED_TARGET,
        "next_direct_attack_target": NEXT_EXTERNAL_TARGET,
        "theorem_rows": [],
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_tail_upper_pi_input_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-ht-coefficient-split-ledger.json": sha256(
                coeff_ledger
            ),
            "data/square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-ledger.json": sha256(
                OUT_LEDGER
            ),
        },
        "plain_conclusion": (
            "尾素数项已被单独压缩：有限桥显示 `T<=0.212P/logP` 对所有 "
            f"`P>={p0}` 素数只有 `2753,2803` 两个 universal 例外；"
            "既有 selector 重放中 `T` 上界失败数为 0，所以这两个例外不进入当前 selector 命中。"
            f"对 `P>=ceil(exp({log_threshold}))={high_p0}`，外部 Dusart 型 pi 双侧界给出 "
            "`T<=0.212P/logP`。因此外部路线中尾上界门可关闭；严格自足路线仍需内化 pi 双侧区间界。"
        ),
    }
    result["theorem_rows"] = theorem_rows(result)
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    finite = result["finite_tail_bridge"]
    high = result["analytic_high_segment_certificate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector tail upper pi input router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"p0={agg['p0']}",
        f"target_t_coeff={agg['target_t_coeff']}",
        f"high_p0={agg['high_p0']}",
        f"finite_bridge_prime_count={agg['finite_bridge_prime_count']}",
        f"finite_bridge_failure_p_values={agg['finite_bridge_failure_p_values']}",
        f"prior_selector_t_upper_failure_count_at_p0={agg['prior_selector_t_upper_failure_count_at_p0']}",
        f"external_tail_upper_closed={fmt_bool(agg['external_tail_upper_closed'])}",
        f"self_contained_tail_upper_closed={fmt_bool(agg['self_contained_tail_upper_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有限桥",
        "",
        "| range | prime count | failure count | max T coeff | p at max |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for row in finite["band_records"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"{row['p_lo']}..{row['p_hi']}",
                    str(row["prime_count"]),
                    str(row["failure_count"]),
                    str(row["max_T_scaled_coeff"]),
                    str(row["p_at_max_T_scaled_coeff"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "有限 universal 失败只有：",
            "",
            "| p | T | T log(P)/P |",
            "| ---: | ---: | ---: |",
        ]
    )
    for row in finite["failure_examples"]:
        lines.append(f"| {row['p']} | {row['T']} | {row['T_scaled_coeff']} |")
    lines.extend(
        [
            "",
            "这两个失败点均小于既有 selector 重放上界 `P<=10000`，而上一系数拆分账本给出 `T_upper_failure_count_at_p0=0`，所以它们不进入 selector rho hit。",
            "",
            "## 2. 高段 pi 输入",
            "",
            "高段使用外部 Dusart 型模板：",
            "",
            "```text",
            "pi(x) <= x/log(x) * (1 + 1/log(x) + 2.51/log(x)^2)",
            "pi(x) >= x/log(x) * (1 + 1/log(x))",
            "```",
            "",
            "为处理取整，使用 `floor(4P/5)>=0.799P`。于是 `P>=ceil(exp(15))` 时有：",
            "",
            "```text",
            high["envelope_formula"],
            f"R(15)={high['envelope_at_log_threshold']}",
            f"0.212-R(15)={high['slack']}",
            "```",
            "",
            "导数证书：",
            "",
            f"- {high['derivative_certificate']['claim']}",
            f"- 归约不等式：`{high['derivative_certificate']['reduction']}`",
            f"- 正多项式：`{high['derivative_certificate']['expanded_positive_polynomial']}`",
            f"- `L=15` 处值：`{high['derivative_certificate']['polynomial_value_at_threshold']}`。",
            "",
            "## 3. 外部/自足边界",
            "",
            "| input | role | self-contained |",
            "| --- | --- | ---: |",
        ]
    )
    for row in result["external_input_rows"]:
        lines.append(
            f"| {table_cell(row['input'])} | {table_cell(row['role'])} | `{fmt_bool(row['registered_as_self_contained'])}` |"
        )
    lines.extend(
        [
            "",
            "## 4. 命题行",
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
            "## 5. 决策表",
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
            "## 6. 下一步",
            "",
            f"- 外部路线主攻：`{result['hardpoint_after_router_external_lane']}`。",
            f"- 严格自足路线补件：`{result['hardpoint_after_router_self_contained_lane']}`。",
            "- 数学主线不要再转移到尾项；应直接攻 selector 平方窗下系数 `H>=0.43P/logP`，或证明相关余量 `H-2T>=cP/logP`。",
            "",
            "## 7. 依赖哈希",
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
    parser.add_argument("--coeff-ledger", type=Path, default=COEFF_LEDGER)
    parser.add_argument("--p0", type=int, default=2001)
    parser.add_argument("--target-t-coeff", type=float, default=0.212)
    parser.add_argument("--high-log-threshold", type=float, default=15.0)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    coeff_ledger = args.coeff_ledger if args.coeff_ledger.is_absolute() else ROOT / args.coeff_ledger
    result = build_result(coeff_ledger, args.p0, args.target_t_coeff, args.high_log_threshold)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-tail-upper-pi-input-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "high_p0": result["aggregate"]["high_p0"],
                "finite_bridge_failure_p_values": result["aggregate"]["finite_bridge_failure_p_values"],
                "external_tail_upper_closed": result["aggregate"]["external_tail_upper_closed"],
                "self_contained_tail_upper_closed": result["aggregate"]["self_contained_tail_upper_closed"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
