#!/usr/bin/env python3
"""审计平方锚 BadTail 的奇偶强制层与最小素因子残余层。

用法示例：
  python3 experiments/prime_matrix_square_phase_bad_tail_parity_lpf_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-bad-tail-parity-lpf-router.json

输出：
  data/square-phase-bad-tail-parity-lpf-ledger.json
  docs/monograph/prime-matrix-square-phase-bad-tail-parity-lpf-router.json
  docs/monograph/prime-matrix-square-phase-bad-tail-parity-lpf-router.md
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

OUT_LEDGER = DATA / "square-phase-bad-tail-parity-lpf-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-bad-tail-parity-lpf-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-bad-tail-parity-lpf-router.md"

MAIN_TARGET = "SquarePhasePrimeBeatsForcedParityPlusResidualLPFLayers"
RETURN_TARGET = "ResidualLPFLayerPDECSAEReturn"


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


def cutoff_alpha45(p: int) -> int:
    """返回 floor(4P/5)。"""
    return (4 * p) // 5


def ceil_div(numerator: int, denominator: int) -> int:
    """整数向上取整，允许 numerator 为负。"""
    return -((-numerator) // denominator)


def is_prime_by_primes(value: int, primes: list[int]) -> bool:
    """用已知素数表判定素性。"""
    if value < 2:
        return False
    for q in primes:
        if q * q > value:
            return True
        if value % q == 0:
            return value == q
    raise ValueError("prime table too short")


def least_prime_factor(value: int, primes: list[int]) -> int:
    """返回最小素因子；素数返回自身。"""
    for q in primes:
        if q * q > value:
            return value
        if value % q == 0:
            return q
    raise ValueError("prime table too short")


def tail_slots_for_q(p: int, q: int, sign: str, primes: list[int]) -> list[dict[str, Any]]:
    """给出尾素 q=P-a 的全部槽。"""
    a_value = p - q
    square_a = a_value * a_value
    if sign == "plus":
        t_start = square_a // q + 1
        t_end = (square_a + p - 1) // q
    elif sign == "minus":
        t_start = ceil_div(square_a - p + 1, q)
        t_end = (square_a - 1) // q
    else:
        raise ValueError(f"unknown sign: {sign}")

    records: list[dict[str, Any]] = []
    for t_value in range(t_start, t_end + 1):
        if sign == "plus":
            r_value = t_value * q - square_a
            value = p * p + r_value
        else:
            r_value = square_a - t_value * q
            value = p * p - r_value
        cofactor = p + a_value + t_value
        lpf = least_prime_factor(cofactor, primes)
        cofactor_prime = lpf == cofactor
        forced_parity = t_value % 2 == 1
        records.append(
            {
                "q": q,
                "a": a_value,
                "t": t_value,
                "r": r_value,
                "cofactor_m": cofactor,
                "value": value,
                "cofactor_prime": cofactor_prime,
                "cofactor_least_prime_factor": lpf,
                "bad_tail": not cofactor_prime,
                "forced_parity_bad": forced_parity,
                "residual_lpf_bad": (not cofactor_prime) and not forced_parity,
                "product_identity_ok": value == q * cofactor,
                "r_in_window": 1 <= r_value < p,
            }
        )
    return records


def square_anchor_prime_count(p: int, sign: str, primes: list[int]) -> int:
    """计算 P^2±r 中的平方锚素数数。"""
    count = 0
    for r_value in range(1, p):
        value = p * p + r_value if sign == "plus" else p * p - r_value
        if is_prime_by_primes(value, primes):
            count += 1
    return count


def audit_sign(p: int, sign: str, primes: list[int]) -> dict[str, Any]:
    """审计单个 P 的一个方向。"""
    cutoff = cutoff_alpha45(p)
    tail_primes = [q for q in primes if cutoff < q < p]
    slots = [slot for q in tail_primes for slot in tail_slots_for_q(p, q, sign, primes)]
    forced = [slot for slot in slots if slot["forced_parity_bad"]]
    residual = [slot for slot in slots if slot["residual_lpf_bad"]]
    bad = [slot for slot in slots if slot["bad_tail"]]
    good = [slot for slot in slots if slot["cofactor_prime"]]
    prime_count = square_anchor_prime_count(p, sign, primes)

    parity_failures = [slot for slot in forced if not slot["bad_tail"]]
    residual_failures = [
        slot
        for slot in residual
        if slot["t"] % 2 != 0
        or slot["cofactor_m"] % 2 == 0
        or slot["cofactor_least_prime_factor"] == slot["cofactor_m"]
        or slot["cofactor_least_prime_factor"] ** 2 > slot["cofactor_m"]
    ]
    identity_failures = [
        slot
        for slot in slots
        if not slot["product_identity_ok"]
        or not slot["r_in_window"]
        or (slot["bad_tail"] != (slot["forced_parity_bad"] or slot["residual_lpf_bad"]))
    ]
    layer_keys: dict[tuple[int, int], int] = {}
    layer_reuse_failures: list[dict[str, Any]] = []
    for slot in residual:
        key = (slot["q"], slot["cofactor_least_prime_factor"])
        layer_keys[key] = layer_keys.get(key, 0) + 1
        if layer_keys[key] > 1:
            layer_reuse_failures.append(slot)

    lpf_histogram: dict[int, int] = {}
    t_histogram: dict[int, int] = {}
    for slot in residual:
        lpf = slot["cofactor_least_prime_factor"]
        t_value = slot["t"]
        lpf_histogram[lpf] = lpf_histogram.get(lpf, 0) + 1
        t_histogram[t_value] = t_histogram.get(t_value, 0) + 1

    return {
        "p": p,
        "sign": sign,
        "cutoff": cutoff,
        "distinct_tail_prime_count": len(tail_primes),
        "tail_slot_count": len(slots),
        "square_anchor_prime_count": prime_count,
        "good_cofactor_prime_slot_count": len(good),
        "bad_tail_count": len(bad),
        "forced_parity_bad_count": len(forced),
        "residual_lpf_bad_count": len(residual),
        "prime_minus_bad": prime_count - len(bad),
        "prime_minus_forced": prime_count - len(forced),
        "prime_minus_forced_and_residual": prime_count - len(forced) - len(residual),
        "parity_failure_count": len(parity_failures),
        "residual_lpf_failure_count": len(residual_failures),
        "identity_failure_count": len(identity_failures),
        "layer_reuse_failure_count": len(layer_reuse_failures),
        "residual_lpf_histogram": dict(sorted(lpf_histogram.items())),
        "residual_t_histogram_sample": dict(sorted(t_histogram.items())[:40]),
        "forced_sample": forced[:8],
        "residual_sample": residual[:8],
        "failure_samples": {
            "parity": parity_failures[:3],
            "residual": residual_failures[:3],
            "identity": identity_failures[:3],
            "layer_reuse": layer_reuse_failures[:3],
        },
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步确定性定理。"""
    return [
        {
            "name": "forced_parity_bad_tail",
            "status": "closed",
            "statement": "For odd P and tail prime q, a=P-q is even; hence m=P+a+t is even exactly when t is odd, so every odd-t slot is forced BadTail.",
        },
        {
            "name": "residual_lpf_layer",
            "status": "closed",
            "statement": "Every BadTail not forced by parity has even t, odd composite m, and an odd least prime factor ell<=sqrt(m)<sqrt(5P/4+2).",
        },
        {
            "name": "fixed_q_ell_nonreuse",
            "status": "closed",
            "statement": "For fixed sign, q, and ell, the product interval has length P/(q ell)<1, so a residual least-prime-factor layer contributes at most one slot.",
        },
        {
            "name": "remaining_prime_vs_forced_plus_residual",
            "status": "open",
            "statement": "A global proof still needs square-anchor primes to beat forced parity slots plus residual LPF layers, or a PDEC/SAE return from residual over-density.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ForcedParityLayerClosed",
            "closed": result["total_parity_failure_count"] == 0,
            "proved": True,
            "meaning": "奇数 t 槽必为偶余因子，因而必是 BadTail。",
            "remaining": "closed",
        },
        {
            "gate": "ResidualLPFLayerClosed",
            "closed": result["total_residual_lpf_failure_count"] == 0
            and result["total_layer_reuse_failure_count"] == 0,
            "proved": True,
            "meaning": "非奇偶强制的 BadTail 已压成互不复用的最小素因子层。",
            "remaining": "closed",
        },
        {
            "gate": "PrimeBeatsForcedPlusResidual",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明平方锚素数数压过强制奇偶坏槽与残余 LPF 层总量。",
            "remaining": MAIN_TARGET,
        },
        {
            "gate": "ResidualLayerPDECReturn",
            "closed": False,
            "proved": False,
            "meaning": "若残余 LPF 层过密，必须抽取固定低模最小因子相位缺陷。",
            "remaining": RETURN_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只关闭 BadTail 内部分层，不关闭全局行/列命题。",
            "remaining": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    prime_flags = sieve(max_p * 2)
    primes = primes_from_flags(prime_flags, max_p * 2)
    p_values = [p for p in primes if 3 <= p <= max_p]
    records: list[dict[str, Any]] = []
    for p in p_values:
        records.append(audit_sign(p, "plus", primes))
        records.append(audit_sign(p, "minus", primes))

    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    total_parity_failures = sum(record["parity_failure_count"] for record in records)
    total_residual_failures = sum(record["residual_lpf_failure_count"] for record in records)
    total_identity_failures = sum(record["identity_failure_count"] for record in records)
    total_layer_reuse_failures = sum(record["layer_reuse_failure_count"] for record in records)
    worst_margin = min(records, key=lambda item: item["prime_minus_forced_and_residual"], default=None)

    plus_records = [record for record in records if record["sign"] == "plus"]
    minus_records = [record for record in records if record["sign"] == "minus"]
    aggregate = {
        "plus_prime_total": sum(record["square_anchor_prime_count"] for record in plus_records),
        "plus_forced_parity_bad_total": sum(record["forced_parity_bad_count"] for record in plus_records),
        "plus_residual_lpf_bad_total": sum(record["residual_lpf_bad_count"] for record in plus_records),
        "plus_bad_tail_total": sum(record["bad_tail_count"] for record in plus_records),
        "minus_prime_total": sum(record["square_anchor_prime_count"] for record in minus_records),
        "minus_forced_parity_bad_total": sum(record["forced_parity_bad_count"] for record in minus_records),
        "minus_residual_lpf_bad_total": sum(record["residual_lpf_bad_count"] for record in minus_records),
        "minus_bad_tail_total": sum(record["bad_tail_count"] for record in minus_records),
    }
    aggregate["combined_prime_total"] = aggregate["plus_prime_total"] + aggregate["minus_prime_total"]
    aggregate["combined_forced_parity_bad_total"] = (
        aggregate["plus_forced_parity_bad_total"] + aggregate["minus_forced_parity_bad_total"]
    )
    aggregate["combined_residual_lpf_bad_total"] = (
        aggregate["plus_residual_lpf_bad_total"] + aggregate["minus_residual_lpf_bad_total"]
    )
    aggregate["combined_bad_tail_total"] = aggregate["plus_bad_tail_total"] + aggregate["minus_bad_tail_total"]

    ledger = {
        "parameters": {"max_p": max_p, "alpha": "4/5", "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "total_parity_failure_count": total_parity_failures,
        "total_residual_lpf_failure_count": total_residual_failures,
        "total_identity_failure_count": total_identity_failures,
        "total_layer_reuse_failure_count": total_layer_reuse_failures,
        "worst_margin_record": worst_margin,
        "sample_records": sample_records,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_bad_tail_parity_lpf_router",
        "status": "square_phase_bad_tail_split_into_forced_parity_and_residual_lpf_layers_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "total_parity_failure_count": total_parity_failures,
        "total_residual_lpf_failure_count": total_residual_failures,
        "total_identity_failure_count": total_identity_failures,
        "total_layer_reuse_failure_count": total_layer_reuse_failures,
        "worst_margin_record": worst_margin,
        "sample_records": sample_records,
        "forced_parity_layer_closed": total_parity_failures == 0,
        "residual_lpf_layer_closed": total_residual_failures == 0 and total_layer_reuse_failures == 0,
        "prime_beats_forced_plus_residual_proved": False,
        "residual_lpf_pdec_return_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "SquarePhaseBadTailShiftedCompositeCofactorSlotBound",
        "hardpoint_after_router": f"{MAIN_TARGET} OR {RETURN_TARGET}",
        "next_direct_attack_target": MAIN_TARGET,
        "alternative_attack_target": RETURN_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_bad_tail_parity_lpf_router.py": sha256(
                Path(__file__).resolve()
            ),
            "data/square-phase-bad-tail-parity-lpf-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "`BadTail` 已进一步分解为两个刚性层：奇数 `t` 槽由奇偶性强制成为偶余因子坏槽；"
            "剩余坏槽只能发生在偶数 `t` 上，并且由一个奇最小素因子 `ell<=sqrt(m)` 解释。"
            "固定 `(q,ell)` 在同一侧不能复用槽，因为对应乘积区间长度小于 `1`。"
            "因此剩余硬点变为：平方锚素数数必须压过强制奇偶坏槽与残余 LPF 层；"
            "若残余层过密，则它应回流为低模最小因子 PDEC/SAE。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase BadTail parity/LPF router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"total_parity_failure_count={result['total_parity_failure_count']}",
        f"total_residual_lpf_failure_count={result['total_residual_lpf_failure_count']}",
        f"total_layer_reuse_failure_count={result['total_layer_reuse_failure_count']}",
        f"prime_beats_forced_plus_residual_proved={fmt_bool(result['prime_beats_forced_plus_residual_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 奇偶强制层",
        "",
        "对奇素数 `P` 与尾素 `q`，`a=P-q` 为偶数。槽余因子为",
        "",
        "```text",
        "m=P+a+t.",
        "```",
        "",
        "因此 `m` 的奇偶性只由 `t` 决定：`t` 为奇数时 `m` 为偶数且 `m>P>2`，所以必为合数。"
        "这部分 BadTail 是完全强制的，不是分布异常。",
        "",
        "## 2. 残余 LPF 层",
        "",
        "非奇偶强制的 BadTail 必在偶数 `t` 上，此时 `m` 为奇合数。取其最小素因子 `ell`，则",
        "",
        "```text",
        "ell <= sqrt(m),    m=P+a+t < 5P/4+2.",
        "```",
        "",
        "并且固定同侧 `q,ell` 至多贡献一个槽：因为 `q*ell*h` 落在长度为 `P` 的平方锚窗口内，而",
        "`P/(q*ell)<1`。",
        "",
        "## 3. 确定性判据",
        "",
        "| name | status | statement |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(f"| `{item['name']}` | `{item['status']}` | {table_cell(item['statement'])} |")

    agg = result["aggregate"]
    worst = result["worst_margin_record"]
    lines.extend(
        [
            "",
            "## 4. 有限审计摘要",
            "",
            "| metric | plus | minus | combined |",
            "| --- | ---: | ---: | ---: |",
            f"| square-anchor primes | {agg['plus_prime_total']} | {agg['minus_prime_total']} | {agg['combined_prime_total']} |",
            f"| forced parity BadTail | {agg['plus_forced_parity_bad_total']} | {agg['minus_forced_parity_bad_total']} | {agg['combined_forced_parity_bad_total']} |",
            f"| residual LPF BadTail | {agg['plus_residual_lpf_bad_total']} | {agg['minus_residual_lpf_bad_total']} | {agg['combined_residual_lpf_bad_total']} |",
            f"| total BadTail | {agg['plus_bad_tail_total']} | {agg['minus_bad_tail_total']} | {agg['combined_bad_tail_total']} |",
            "",
            f"最紧单侧样本：`P={worst['p']}`，`sign={worst['sign']}`，`Prime={worst['square_anchor_prime_count']}`，`Forced={worst['forced_parity_bad_count']}`，`Residual={worst['residual_lpf_bad_count']}`，`margin={worst['prime_minus_forced_and_residual']}`。",
            "",
            "## 5. 样本表",
            "",
            "| P | sign | Prime | BadTail | forced parity | residual LPF | Prime-Bad | Prime-Forced |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_records"]:
        lines.append(
            f"| {row['p']} | `{row['sign']}` | {row['square_anchor_prime_count']} | "
            f"{row['bad_tail_count']} | {row['forced_parity_bad_count']} | "
            f"{row['residual_lpf_bad_count']} | {row['prime_minus_bad']} | "
            f"{row['prime_minus_forced']} |"
        )

    lines.extend(
        [
            "",
            "## 6. 判定表",
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
            f"- 备选回流：`{result['alternative_attack_target']}`。",
            "- 必须诚实保留边界：本步没有证明平方锚素数全局下界；它只把 BadTail 的内部坏槽来源拆成强制奇偶层与残余 LPF 层。",
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
                "total_parity_failure_count": result["total_parity_failure_count"],
                "total_residual_lpf_failure_count": result["total_residual_lpf_failure_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
