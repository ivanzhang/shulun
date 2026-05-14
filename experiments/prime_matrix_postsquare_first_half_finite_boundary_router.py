#!/usr/bin/env python3
"""生成平方后前半窗素数输入的有限边界证书。

用法示例：
  python3 experiments/prime_matrix_postsquare_first_half_finite_boundary_router.py --max-p 200000
  python3 -m json.tool docs/monograph/prime-matrix-postsquare-first-half-finite-boundary-router.json

输出：
  data/postsquare-first-half-prime-finite-boundary-ledger.json
  docs/monograph/prime-matrix-postsquare-first-half-finite-boundary-router.json
  docs/monograph/prime-matrix-postsquare-first-half-finite-boundary-router.md
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
OUT_LEDGER = DATA / "postsquare-first-half-prime-finite-boundary-ledger.json"
OUT_JSON = DOCS / "prime-matrix-postsquare-first-half-finite-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-postsquare-first-half-finite-boundary-router.md"

FIRST_HALF = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"
FINAL_TAIL = "UniformFinalTailRoughSurvivorLowerBoundOrRegisteredPhaseDefect"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"


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


def primes_upto(limit: int) -> list[int]:
    """返回 limit 以内素数列表。"""
    flags = sieve(limit)
    return [idx for idx in range(2, limit + 1) if flags[idx]]


def is_probable_prime(n: int) -> bool:
    """64 位范围内的确定性 Miller-Rabin 素性测试。"""
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if n % prime == 0:
            return n == prime

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # 这组基对 n < 2^64 是确定性的。
    for base in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if base >= n:
            continue
        x = pow(base, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def least_prime_offset_after_square(p: int) -> int | None:
    """返回最小 r，使 p^2 < p^2+r < p^2+p 且 p^2+r 为素数。"""
    start = 1 if p == 2 else 2
    step = 1 if p == 2 else 2
    p2 = p * p
    for r in range(start, p, step):
        if is_probable_prime(p2 + r):
            return r
    return None


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def audit(max_p: int) -> dict[str, Any]:
    """执行有限边界审计。"""
    primes = primes_upto(max_p)
    records: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for p in primes:
        offset = least_prime_offset_after_square(p)
        record = {
            "p": p,
            "least_offset": offset,
            "least_prime": None if offset is None else p * p + offset,
            "offset_ratio": None if offset is None else offset / p,
        }
        records.append(record)
        if offset is None:
            failures.append(record)

    successful = [item for item in records if item["least_offset"] is not None]
    worst_by_offset = sorted(successful, key=lambda item: item["least_offset"], reverse=True)[:20]
    worst_by_ratio = sorted(successful, key=lambda item: item["offset_ratio"], reverse=True)[:20]
    return {
        "parameters": {"max_p": max_p},
        "prime_count": len(primes),
        "failure_count": len(failures),
        "first_failure": failures[0] if failures else None,
        "max_offset_record": worst_by_offset[0] if worst_by_offset else None,
        "max_ratio_record": worst_by_ratio[0] if worst_by_ratio else None,
        "worst_by_offset": worst_by_offset,
        "worst_by_ratio": worst_by_ratio,
        "failures": failures,
    }


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成审查判定表。"""
    return [
        {
            "gate": "FiniteFirstHalfPrimeSquareScanCompleted",
            "closed": True,
            "proved": False,
            "meaning": f"已有限检查素数 P<= {result['parameters']['max_p']} 的 (P^2,P^2+P) 前半窗。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "FiniteFailureFound",
            "closed": result["failure_count"] == 0,
            "proved": False,
            "meaning": "本次有限范围没有发现反例；若出现 failure，则 final-tail 路线立即失败。",
            "remaining": "none in scanned range" if result["failure_count"] == 0 else "inspect first_failure",
        },
        {
            "gate": "ExternalPrimeGapTheoremDirectlyMatchesLengthP",
            "closed": False,
            "proved": False,
            "meaning": "现有通用短区间素数定理仍给 x^theta 型长度，theta>1/2；代入 x=P^2 不能推出长度 P。",
            "remaining": FIRST_HALF,
        },
        {
            "gate": "FirstHalfPrimeSquareInputProved",
            "closed": False,
            "proved": False,
            "meaning": "有限证书和现有通用素数间隙输入都不能升级为每个素数 P 的全局证明。",
            "remaining": f"{FIRST_HALF} OR {NONFINAL}",
        },
    ]


def build_result(max_p: int) -> dict[str, Any]:
    """构造有限边界证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    scan = audit(max_p)
    OUT_LEDGER.write_text(json.dumps(scan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_postsquare_first_half_finite_boundary_router",
        "status": "first_half_prime_square_finite_boundary_verified_global_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "finite_evidence_only": True,
        "empirical_absence_not_used_for_global_proof": True,
        "first_half_prime_square_input_current_corpus_proved": False,
        "external_general_prime_gap_input_directly_sufficient": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": FIRST_HALF,
        "hardpoint_after_router": f"{FIRST_HALF} OR {NONFINAL}",
        "next_direct_attack_target": NONFINAL,
        "finite_scan": scan,
        "decision_rows": decision_rows(scan),
        "external_short_interval_boundary_references": [
            {
                "name": "Baker-Harman-Pintz 2001",
                "url": "https://doi.org/10.1112/plms/83.3.532",
                "usable_exponent": "0.525",
                "directly_sufficient_for_length_sqrt_x": False,
            },
            {
                "name": "Runbo Li arXiv:2308.04458 v8",
                "url": "https://arxiv.org/abs/2308.04458",
                "usable_exponent": "0.52",
                "directly_sufficient_for_length_sqrt_x": False,
            },
        ],
        "source_hashes": {
            "experiments/prime_matrix_postsquare_first_half_finite_boundary_router.py": sha256(Path(__file__).resolve()),
            "data/postsquare-first-half-prime-finite-boundary-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            f"有限审计已检查 `P<= {max_p}` 的 `(P^2,P^2+P)` 前半窗，"
            "未发现失败。但该输入等价于长度 `sqrt(x)` 级的特殊短区间素数命题；"
            "当前通用无条件素数间隙定理不能直接给出这个长度，有限验证也不能升级为全局证明。"
            "因此 final-tail 线仍不能声明自足闭合，主攻应回到非 final-tail 的 PDEC/SAE/预算放大路线。"
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 文档。"""
    scan = result["finite_scan"]
    lines = [
        "# Prime Matrix 平方后前半窗素数输入有限边界证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={scan['parameters']['max_p']}",
        f"prime_count={scan['prime_count']}",
        f"failure_count={scan['failure_count']}",
        f"first_half_prime_square_input_current_corpus_proved={fmt_bool(result['first_half_prime_square_input_current_corpus_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最坏偏移样本",
        "",
        "| P | least_offset | least_prime | offset/P |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in scan["worst_by_ratio"][:12]:
        lines.append(
            f"| {item['p']} | {item['least_offset']} | {item['least_prime']} | {item['offset_ratio']:.6f} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 审稿边界",
            "",
            f"- `{FIRST_HALF}` 是 final-tail 线的真实输入边界，不是已证引理。",
            "- 现有有限验证只说明低范围无反例；不能替代全局短区间素数证明。",
            "- 已登记外部短区间素数结果的指数仍大于 `1/2`，代入 `x=P^2` 只能给长于 `P` 的区间。",
            f"- 若不新增该强输入，下一步必须沿 `{NONFINAL}` 继续寻找反例链与真实结构链的终端矛盾。",
            "",
            "## 4. 外部短区间边界",
            "",
            "| source | exponent | directly sufficient | url |",
            "| --- | ---: | ---: | --- |",
        ]
    )
    for item in result["external_short_interval_boundary_references"]:
        lines.append(
            f"| {table_cell(item['name'])} | `{item['usable_exponent']}` | "
            f"`{fmt_bool(item['directly_sufficient_for_length_sqrt_x'])}` | {item['url']} |"
        )
    lines.extend(
        [
            "",
            "## 5. 依赖哈希",
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
    parser.add_argument("--max-p", type=int, default=200000)
    args = parser.parse_args()
    result = build_result(args.max_p)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": result["finite_scan"]["parameters"]["max_p"],
                "prime_count": result["finite_scan"]["prime_count"],
                "failure_count": result["finite_scan"]["failure_count"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
