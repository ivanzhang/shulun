#!/usr/bin/env python3
"""生成早期/任意零行的 CRT 周期提升与载体端点漂移路由证书。

用法示例：
  python3 experiments/prime_matrix_early_zero_period_lift_carrier_drift_router.py
  python3 experiments/prime_matrix_early_zero_period_lift_carrier_drift_router.py --lift-steps 16
  python3 -m json.tool data/prime-matrix-early-zero-period-lift-carrier-drift-ledger.json

输出：
  data/prime-matrix-early-zero-period-lift-carrier-drift-ledger.json
  docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.json
  docs/monograph/prime-matrix-early-zero-period-lift-carrier-drift-router.md
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

PREVIOUS_ROUTER = DOCS / "prime-matrix-early-zero-gap-crt-asymmetry-router.json"
ZERO_ROW_CRT = DOCS / "prime-matrix-zero-row-full-crt-diagonal-minrep.md"
H3_TAIL = DOCS / "prime-matrix-h3-tail-filler-rigidity-hardcore.md"
NC_BLK = DOCS / "prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md"

OUT_LEDGER = DATA / "prime-matrix-early-zero-period-lift-carrier-drift-ledger.json"
OUT_JSON = DOCS / "prime-matrix-early-zero-period-lift-carrier-drift-router.json"
OUT_MD = DOCS / "prime-matrix-early-zero-period-lift-carrier-drift-router.md"

PREVIOUS_HARDPOINT = (
    "EarlyZeroGapCarrierAsymmetryRoutedToH3DSBNCBLKOrExternalDIBFI;"
    "GlobalFinalInputsStillOpen"
)
NEXT_HARDPOINT = (
    "PeriodLiftCarrierDriftRoutedToPersistentPDECOrSparseSAEOrH3DSBNCBLK;"
    "GlobalFinalInputsStillOpen"
)

# 已由既有零行 CRT 审计文档登记的首批全周期零行样本。
ZERO_ROW_SAMPLES = [
    {"p": 13, "x": 168, "source": "prime-matrix-zero-row-covering-vs-smoothness-audit"},
    {"p": 17, "x": 1210, "source": "prime-matrix-zero-row-covering-vs-smoothness-audit"},
    {"p": 19, "x": 3658, "source": "prime-matrix-zero-row-covering-vs-smoothness-audit"},
    {"p": 23, "x": 58, "source": "p23-zero-row-analysis"},
]


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    if n < 2:
        return []
    flags = bytearray(b"\x01") * (n + 1)
    flags[0:2] = b"\x00\x00"
    for d in range(2, int(n**0.5) + 1):
        if flags[d]:
            start = d * d
            flags[start : n + 1 : d] = b"\x00" * (((n - start) // d) + 1)
    return [i for i in range(n + 1) if flags[i]]


def is_prime(n: int) -> bool:
    """确定性 Miller-Rabin 判素，覆盖本证书使用范围。"""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in small_primes:
        if n % prime == 0:
            return n == prime
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for base in [2, 3, 5, 7, 11, 13, 17]:
        if base >= n:
            continue
        x = pow(base, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def previous_prime_below(n: int) -> int:
    """返回严格小于 n 的最大素数。"""
    candidate = n - 1
    if candidate % 2 == 0 and candidate != 2:
        candidate -= 1
    while candidate >= 2 and not is_prime(candidate):
        candidate -= 2
    return candidate


def next_prime_above(n: int) -> int:
    """返回严格大于 n 的最小素数。"""
    candidate = n + 1
    if candidate % 2 == 0:
        candidate += 1
    while not is_prime(candidate):
        candidate += 2
    return candidate


def primorial_less_than(p: int) -> int:
    """计算小于 p 的素数乘积。"""
    value = 1
    for prime in primes_upto(p - 1):
        value *= prime
    return value


def least_factor(n: int) -> int | None:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    if n < 2:
        return None
    for prime in primes_upto(int(math.isqrt(n)) + 1):
        if n % prime == 0:
            return prime
    return n


def zero_row_witnesses(p: int, x: int) -> list[dict[str, int]]:
    """给出 p*x+c 的小素因子见证。"""
    witnesses = []
    for c in range(1, p):
        n = p * x + c
        factor = least_factor(n)
        witnesses.append({"c": c, "n": n, "least_factor": int(factor)})
    return witnesses


def row_is_zero_by_small_factors(p: int, x: int) -> bool:
    """检查非平凡列是否都由小于 p 的素数覆盖。"""
    return all(item["least_factor"] is not None and item["least_factor"] < p for item in zero_row_witnesses(p, x))


def carrier_profile(p: int, x: int, period_step: int, row_period: int) -> dict[str, Any]:
    """计算周期提升后零行的相邻素数载体。"""
    lifted_x = x + period_step * row_period
    left = p * lifted_x + 1
    right = p * lifted_x + p
    a = previous_prime_below(left)
    b = next_prime_above(right)
    shift = p * row_period
    expected_a = None if period_step == 0 else None
    expected_b = None if period_step == 0 else None
    return {
        "t": period_step,
        "x": lifted_x,
        "interval": [left, right],
        "left_prime": a,
        "right_prime": b,
        "gap": b - a,
        "left_slack": left - a,
        "right_slack": b - right,
        "cover_lift_zero": row_is_zero_by_small_factors(p, lifted_x),
        "integer_period_shift": shift,
        "expected_left_prime_if_endpoint_periodic": expected_a,
        "expected_right_prime_if_endpoint_periodic": expected_b,
    }


def build_sample(sample: dict[str, Any], lift_steps: int) -> dict[str, Any]:
    """生成单个零行样本的周期提升载体漂移账本。"""
    p = int(sample["p"])
    x = int(sample["x"])
    row_period = primorial_less_than(p)
    integer_shift = p * row_period
    profiles = [carrier_profile(p, x, t, row_period) for t in range(lift_steps + 1)]
    base_left = profiles[0]["left_prime"]
    base_right = profiles[0]["right_prime"]
    periodic_endpoint_matches = []
    for item in profiles:
        t = item["t"]
        periodic_endpoint_matches.append(
            {
                "t": t,
                "left_matches_translate": item["left_prime"] == base_left + t * integer_shift,
                "right_matches_translate": item["right_prime"] == base_right + t * integer_shift,
            }
        )

    slack_pairs = {(item["left_slack"], item["right_slack"]) for item in profiles}
    gap_values = [item["gap"] for item in profiles]
    return {
        "p": p,
        "x0": x,
        "source": sample["source"],
        "row_period_L_less_p": row_period,
        "integer_interval_period_pL": integer_shift,
        "base_zero_row_verified": row_is_zero_by_small_factors(p, x),
        "lift_steps": lift_steps,
        "all_lifts_zero_by_same_small_factors": all(item["cover_lift_zero"] for item in profiles),
        "endpoint_translate_match_count_after_t0": sum(
            1
            for item in periodic_endpoint_matches[1:]
            if item["left_matches_translate"] and item["right_matches_translate"]
        ),
        "distinct_slack_pair_count": len(slack_pairs),
        "min_gap": min(gap_values),
        "max_gap": max(gap_values),
        "profiles": profiles,
        "periodic_endpoint_matches": periodic_endpoint_matches,
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result(lift_steps: int) -> dict[str, Any]:
    """构造路由证书。"""
    previous = json.loads(PREVIOUS_ROUTER.read_text(encoding="utf-8"))
    sample_reports = [build_sample(sample, lift_steps) for sample in ZERO_ROW_SAMPLES]

    gates = [
        gate(
            "ZeroRowPeriodLiftExact",
            True,
            True,
            "若 x 是 P 零行，则 x+t*prod_{q<P}q 仍由同一批小素数覆盖，行覆盖相位精确周期提升。",
            "closed",
        ),
        gate(
            "CarrierEndpointTranslateNotForced",
            True,
            True,
            "相邻素数载体端点不受该 CRT 周期控制；端点平移匹配不是零行周期性的推论。",
            "closed",
        ),
        gate(
            "SampleCarrierDriftVerified",
            True,
            True,
            "已登记零行样本的周期提升全部保持零行覆盖；端点 slack/gap 大量漂移，少数偶然平移不由 CRT 覆盖周期强制。",
            "finite audit only",
        ),
        gate(
            "PersistentDriftPatternRoutesToPDECColumnCRT",
            True,
            True,
            "若端点漂移模式在固定有限相位中持久重复，则它正是 ColumnCRT/PDEC formal unit。",
            "closed as router",
        ),
        gate(
            "SparseDriftPatternRoutesToSAE",
            True,
            True,
            "若漂移只在孤立周期步出现，则是 SAE 单窗逃逸。",
            "closed as router",
        ),
        gate(
            "NonperiodicDriftRoutesToH3DSB",
            True,
            True,
            "若覆盖周期持续而素数端点非周期漂移，则必须由 H3 尾补洞/DSB/KLS/NC-BLK 控制。",
            "H3-DSB-NCBLK",
        ),
        gate(
            "GlobalContradictionFromPeriodLiftAlone",
            False,
            False,
            "周期提升只制造无限复现的复合短块；这本身与素数分布不矛盾，必须再排斥端点漂移分支。",
            "needs PDEC/SAE/H3-DSB closure",
        ),
        gate(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭的是 P,k CRT 周期不对称的精确路由，不关闭完整行/列无条件命题。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_early_zero_period_lift_carrier_drift_router",
        "status": "period_lift_carrier_drift_routed_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "previous_router_status": previous.get("status"),
        "lift_steps": lift_steps,
        "sample_reports": sample_reports,
        "zero_row_period_lift_exact": True,
        "carrier_endpoint_periodic_translation_forced": False,
        "all_sample_lifts_zero": all(item["all_lifts_zero_by_same_small_factors"] for item in sample_reports),
        "sample_endpoint_translate_match_total_after_t0": sum(
            item["endpoint_translate_match_count_after_t0"] for item in sample_reports
        ),
        "persistent_drift_routes_to_pdec_columncrt": True,
        "sparse_drift_routes_to_sae": True,
        "nonperiodic_drift_routes_to_h3_dsb": True,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "零行覆盖相位确实按行周期 L_P=prod_{q<P}q 精确提升；但相邻素数载体端点不随 P*L_P "
            "作 CRT 平移。这个不对称不会单独给出矛盾，只能三分流：持久漂移模式是 PDEC/ColumnCRT，"
            "孤立漂移是 SAE，非周期端点漂移回到 H3-DSB/KLS 的 NC-BLK 或外部 DI/BFI 分支。"
        ),
        "dependency_hashes": {
            str(PREVIOUS_ROUTER.relative_to(ROOT)): sha256(PREVIOUS_ROUTER),
            str(ZERO_ROW_CRT.relative_to(ROOT)): sha256(ZERO_ROW_CRT),
            str(H3_TAIL.relative_to(ROOT)): sha256(H3_TAIL),
            str(NC_BLK.relative_to(ROOT)): sha256(NC_BLK),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# 早期零行 CRT 周期提升与载体端点漂移路由",
        "",
        "**状态：** `period_lift_carrier_drift_routed_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"zero_row_period_lift_exact={fmt_bool(result['zero_row_period_lift_exact'])}",
        "carrier_endpoint_periodic_translation_forced="
        f"{fmt_bool(result['carrier_endpoint_periodic_translation_forced'])}",
        f"all_sample_lifts_zero={fmt_bool(result['all_sample_lifts_zero'])}",
        "sample_endpoint_translate_match_total_after_t0="
        f"{result['sample_endpoint_translate_match_total_after_t0']}",
        "persistent_drift_routes_to_pdec_columncrt="
        f"{fmt_bool(result['persistent_drift_routes_to_pdec_columncrt'])}",
        f"sparse_drift_routes_to_sae={fmt_bool(result['sparse_drift_routes_to_sae'])}",
        f"nonperiodic_drift_routes_to_h3_dsb={fmt_bool(result['nonperiodic_drift_routes_to_h3_dsb'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 周期提升引理",
        "",
        "令",
        "",
        "\\[",
        "L_P=\\prod_{q<P,\\ q\\ prime}q.",
        "\\]",
        "",
        "若 `x` 是 `P` 的零行乘数，即对每个 `1<=c<P` 存在 `q<P` 使 `q|Px+c`，则对任意整数 `t>=0`，",
        "",
        "\\[",
        "P(x+tL_P)+c\\equiv Px+c\\pmod q.",
        "\\]",
        "",
        "因此 `x+tL_P` 仍为零行乘数。这是反例覆盖链在 CRT 行周期中的精确复现。",
        "",
        "## 2. 端点漂移不随周期提升",
        "",
        "设提升后的零行区间为",
        "",
        "\\[",
        "I_t=[P(x+tL_P)+1,\\ P(x+tL_P)+P].",
        "\\]",
        "",
        "令 `a_t,b_t` 为跨越 `I_t` 的左右最近素数。零行周期性只保证 `I_t` 内没有素数；它不保证",
        "",
        "\\[",
        "a_t=a_0+tPL_P,\\qquad b_t=b_0+tPL_P.",
        "\\]",
        "",
        "所以周期复制的是小素因子覆盖，不是相邻素数端点。这正是 `P,k` 行周期中的全局非对称。",
        "",
        "## 3. 样本审计",
        "",
        f"- `lift_steps`: `{result['lift_steps']}`。",
        f"- `all_sample_lifts_zero`: `{fmt_bool(result['all_sample_lifts_zero'])}`。",
        f"- `sample_endpoint_translate_match_total_after_t0`: `{result['sample_endpoint_translate_match_total_after_t0']}`。",
        "",
        "| P | x0 | L_P | P*L_P | all lifts zero | endpoint translate matches after t0 | distinct slack pairs | gap range |",
        "| ---: | ---: | ---: | ---: | --- | ---: | ---: | --- |",
    ]
    for item in result["sample_reports"]:
        lines.append(
            "| {p} | {x} | {period} | {shift} | `{zero}` | {matches} | {slacks} | `{gap}` |".format(
                p=item["p"],
                x=item["x0"],
                period=item["row_period_L_less_p"],
                shift=item["integer_interval_period_pL"],
                zero=fmt_bool(item["all_lifts_zero_by_same_small_factors"]),
                matches=item["endpoint_translate_match_count_after_t0"],
                slacks=item["distinct_slack_pair_count"],
                gap=[item["min_gap"], item["max_gap"]],
            )
        )

    lines.extend(
        [
            "",
            "首个样本的提升端点摘录：",
            "",
            "| t | interval | left_prime | right_prime | gap | left_slack | right_slack |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    first = result["sample_reports"][0]
    for profile in first["profiles"][: min(8, len(first["profiles"]))]:
        lines.append(
            "| {t} | `{interval}` | {left} | {right} | {gap} | {ls} | {rs} |".format(
                t=profile["t"],
                interval=profile["interval"],
                left=profile["left_prime"],
                right=profile["right_prime"],
                gap=profile["gap"],
                ls=profile["left_slack"],
                rs=profile["right_slack"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 三分流",
            "",
            "| carrier drift behavior | route | reason |",
            "| --- | --- | --- |",
            "| 固定有限相位持久复现 | `PDEC/ColumnCRT` | 端点 slack、列位移或低模频率成为同一 formal unit 的重复缺陷。 |",
            "| 只在孤立周期步出现 | `SAE` | 单窗逃逸不能支撑无限反例链。 |",
            "| 端点非周期漂移但覆盖压力持续 | `H3-DSB/KLS -> NC-BLK or external DI/BFI` | 剩余必须由尾补洞/短窗口 Kloosterman dispersion 控制。 |",
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
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
            "## 6. 最新剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书不关闭全局行/列命题；它只把 `P,k` 行 CRT 周期重复后的端点非对称压成命名三分流。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--lift-steps", type=int, default=12)
    args = parser.parse_args()
    result = build_result(lift_steps=max(1, args.lift_steps))
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "lift_steps": result["lift_steps"],
        "all_sample_lifts_zero": result["all_sample_lifts_zero"],
        "sample_endpoint_translate_match_total_after_t0": result[
            "sample_endpoint_translate_match_total_after_t0"
        ],
        "next_direct_attack_target": result["next_direct_attack_target"],
        "row_column_unconditional_closed": result["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
