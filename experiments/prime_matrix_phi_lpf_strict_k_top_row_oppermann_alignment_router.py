#!/usr/bin/env python3
"""生成 strict-k 顶行与 Oppermann 左半窗对齐证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_top_row_oppermann_alignment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment-router.md
"""

from __future__ import annotations

import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-top-row-oppermann-alignment"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-strict-k-unified-positive-core-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-square-collar-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-top-row-perfect-tiling-router.json",
    DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.md",
    DOCS / "prime-matrix-prime-base-exponent-half-barrier-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化成小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def prime_flags(n: int) -> bytearray:
    """生成素数标记表。"""
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    for p in range(2, isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return flags


def top_counts(flags: bytearray, p: int) -> dict[str, Any]:
    """计算素数底 P 的 Oppermann 左右半窗样本。"""
    left_start = p * p - p + 1
    left_end = p * p - 1
    right_start = p * p + 1
    right_end = p * p + p - 1
    left_primes = [n for n in range(left_start, left_end + 1) if flags[n]]
    right_primes = [n for n in range(right_start, right_end + 1) if flags[n]]
    legendre_left = (p - 1) * (p - 1) + 1
    legendre_right = p * p - 1
    legendre_primes = [n for n in range(legendre_left, legendre_right + 1) if flags[n]]
    return {
        "P": p,
        "left_oppermann_count": len(left_primes),
        "right_oppermann_count": len(right_primes),
        "legendre_restricted_count": len(legendre_primes),
        "left_first": left_primes[0] if left_primes else None,
        "left_last": left_primes[-1] if left_primes else None,
        "right_first": right_primes[0] if right_primes else None,
        "left_is_top_row": True,
        "legendre_would_not_force_left_half": len(legendre_primes) >= len(left_primes),
    }


def finite_sweep(max_prime: int = 5003) -> dict[str, Any]:
    """有限审计 prime-indexed Oppermann 半窗；不作为全局证明。"""
    flags = prime_flags(max_prime * max_prime + max_prime)
    primes = [i for i in range(3, max_prime + 1) if flags[i]]
    rows = [top_counts(flags, p) for p in primes]
    left_failures = [r for r in rows if r["left_oppermann_count"] == 0]
    right_failures = [r for r in rows if r["right_oppermann_count"] == 0]
    min_left = min(r["left_oppermann_count"] for r in rows)
    min_right = min(r["right_oppermann_count"] for r in rows)
    min_left_cases = [r for r in rows if r["left_oppermann_count"] == min_left][:12]
    min_right_cases = [r for r in rows if r["right_oppermann_count"] == min_right][:12]
    sample_primes = [5, 11, 17, 101, 499, 5003]
    sample_rows = [top_counts(flags, p) for p in sample_primes if p <= max_prime]
    return {
        "max_prime": max_prime,
        "prime_base_count": len(rows),
        "all_prime_bases_left_half_positive": not left_failures,
        "all_prime_bases_right_half_positive": not right_failures,
        "left_failures": left_failures[:8],
        "right_failures": right_failures[:8],
        "minimum_left_oppermann_count": min_left,
        "minimum_right_oppermann_count": min_right,
        "minimum_left_cases": min_left_cases,
        "minimum_right_cases": min_right_cases,
        "sample_rows": sample_rows,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "TopRowEqualsPrimeIndexedOppermannLeftHalf",
            True,
            True,
            "k=P-1 顶行正性正是 Oppermann 左半窗 (P^2-P,P^2) 在素数底 P 上的特例。",
            "exact alignment",
        ),
        row(
            "FullOppermannWouldCloseTopRow",
            True,
            False,
            "完整 Oppermann 猜想会同时关闭 P^2 左右两个长度 P 半窗，但它不是已知定理。",
            "Oppermann remains conjectural",
        ),
        row(
            "LegendreDoesNotForceTopHalf",
            True,
            True,
            "Legendre 只要求 ((P-1)^2,P^2) 内有素数，可能落在下半段，不能推出 (P^2-P,P^2) 非空。",
            "need Oppermann-left strength",
        ),
        row(
            "FiniteLegendreVerificationDoesNotCloseGlobalTopRow",
            True,
            True,
            "Legendre 的有限计算验证只给有限范围且不是左半窗定理，不能作为全局证明。",
            "finite audit only",
        ),
        row(
            "KnownExternalTheoremsCloseTopRow",
            False,
            False,
            "当前接入的无条件外部短区间定理没有达到每个素数平方端点长度 P 的半窗强度。",
            "sqrt-scale or square-phase proof",
        ),
        row(
            "UnifiedPositiveCoreProved",
            False,
            False,
            "本层只把最坏子核命名为 prime-indexed Oppermann-left；未证明单核正性。",
            "SquarePhaseSpecialPhaseLongBlockPDECExclusion OR SquarePhaseRoughSurvivorUniformLowerBound",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def sample_markdown(samples: list[dict[str, Any]]) -> str:
    """输出样本表 Markdown。"""
    lines = [
        "| P | left count | left first | left last | right count | right first | Legendre count |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in samples:
        lines.append(
            f"| {item['P']} | {item['left_oppermann_count']} | {item['left_first']} | "
            f"{item['left_last']} | {item['right_oppermann_count']} | "
            f"{item['right_first']} | {item['legendre_restricted_count']} |"
        )
    return "\n".join(lines)


def cases_markdown(cases: list[dict[str, Any]], key: str) -> str:
    """压缩输出极小样本。"""
    if not cases:
        return "无"
    return "; ".join(f"P={case['P']}, {key}={case[key]}" for case in cases)


def build_payload() -> dict[str, Any]:
    """生成证书 payload。"""
    sweep = finite_sweep()
    rows = build_rows()
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "status": "top_row_identified_as_prime_indexed_oppermann_left_half",
        "exact_alignment": {
            "strict_top_row": "k=P-1 gives (P^2-P,P^2)",
            "oppermann_left_half": "for n=P, Oppermann-left is (P(P-1),P^2)",
            "legendre_interval_for_n_P_minus_1": "((P-1)^2,P^2), strictly larger and does not force the upper half",
        },
        "external_references": [
            {
                "name": "Research in Number Theory 2024 Legendre verification article",
                "url": "https://link.springer.com/article/10.1007/s40993-024-00589-4",
                "role": "states Legendre and notes Oppermann subsumes it; finite verification is not a proof of Oppermann-left",
            },
            {
                "name": "Baker-Harman-Pintz 2001",
                "url": "https://doi.org/10.1112/plms/83.3.532",
                "role": "generic prime-gap exponent remains above square-root scale after X=P^2 specialization",
            },
            {
                "name": "Runbo Li arXiv:2308.04458",
                "url": "https://arxiv.org/abs/2308.04458",
                "role": "improved generic exponent still gives P^1.04 at X=P^2, longer than P",
            },
        ],
        "finite_sweep": sweep,
        "gates": rows,
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "strict 顶行的真实硬点不是 Legendre，而是 Oppermann 左半窗的素数底特例。"
            "完整 Oppermann 可关闭该子核，但它是猜想；Legendre 及其有限验证不强制素数落在"
            "上半段。当前非循环突破必须直接证明 square-phase 特殊相位不能形成长度 P-1 的"
            "低筛全覆盖，或把该全覆盖登记并排斥为 PDEC/SAE/ColumnCRT。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    sweep = payload["finite_sweep"]
    lines = [
        "# Prime Matrix Phi-LPF strict k top-row Oppermann alignment 证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "顶行 `k=P-1` 给出：",
        "",
        "```text",
        "N_top(P)=pi(P^2-1)-pi(P^2-P).",
        "```",
        "",
        "这正是 Oppermann 左半窗 `(n^2-n,n^2)` 在 `n=P` 且 `P` 为素数时的特例。",
        "它比 Legendre 在 `((P-1)^2,P^2)` 的存在性更靠右；Legendre 允许素数落在",
        "`((P-1)^2,P^2-P]`，因此不能推出顶行正性。",
        "",
        "## 1. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"prime_base_count={sweep['prime_base_count']}",
        f"all_prime_bases_left_half_positive={fmt_bool(sweep['all_prime_bases_left_half_positive'])}",
        f"all_prime_bases_right_half_positive={fmt_bool(sweep['all_prime_bases_right_half_positive'])}",
        f"minimum_left_oppermann_count={sweep['minimum_left_oppermann_count']}",
        f"minimum_right_oppermann_count={sweep['minimum_right_oppermann_count']}",
        f"finite_evidence_not_used_as_global_proof={fmt_bool(sweep['finite_evidence_not_used_as_global_proof'])}",
        "```",
        "",
        "左半窗最小样本：",
        "",
        "```text",
        cases_markdown(sweep["minimum_left_cases"], "left_oppermann_count"),
        "```",
        "",
        "右半窗最小样本：",
        "",
        "```text",
        cases_markdown(sweep["minimum_right_cases"], "right_oppermann_count"),
        "```",
        "",
        "## 2. 样本行",
        "",
        sample_markdown(sweep["sample_rows"]),
        "",
        "## 3. 外部引理边界",
        "",
        "- 完整 Oppermann 猜想会直接关闭顶行左半窗和平方右半窗，但它仍是未证猜想。",
        "- Legendre 只给两个平方之间的某处有素数，不能强制落在 `(P^2-P,P^2)`。",
        "- 已知通用短区间指数在 `X=P^2` 上仍长于 `P`，不能关闭长度 `P` 的平方端点窗口。",
        "",
        "## 4. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 5. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "因此 `UnifiedPositiveCore` 的最坏子核可更精确写为：",
        "",
        "```text",
        "PrimeIndexedOppermannLeftHalf(P):",
        "  pi(P^2-1)-pi(P^2-P)>=1 for every prime P.",
        "```",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in payload["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
