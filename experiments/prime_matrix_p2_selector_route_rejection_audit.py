#!/usr/bin/env python3
"""Prime Matrix P2 最早见证选择器路线反证审计。

用法示例：
  python3 experiments/prime_matrix_p2_selector_route_rejection_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-p2-selector-route-rejection-audit.json

上一层把合成 P2 见证拆成小素因子/cofactor AP 纤维。本层继续检查一个
自然但错误的破奇偶想法：能否把 Li--Zhang--Cai 的“最小 P2”选择器升级为
“最小 P2 就是素数”。有限反例已经排除此路线；即使只看 n>P 的非平凡
见证，很多固定列的最早 P2 仍是合数。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-p2-selector-route-rejection"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
LZC_EXPONENT = 1.8345
SAMPLE_MAX_P = 997
SAMPLE_ROWS = [101, 199, 499, 997]

DEPENDENCIES = [
    DOCS / "prime-matrix-p2-to-prime-transfer-atom-audit.json",
    DOCS / "prime-matrix-parity-breaking-obstruction-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bool_text(value: Any) -> str:
    """输出小写布尔值。"""
    return str(bool(value)).lower()


def sieve_spf(limit: int) -> list[int]:
    """生成最小素因子表。"""
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def omega_big(n: int, spf: list[int]) -> int:
    """计算 Ω(n)，超过 2 后提前停止。"""
    count = 0
    while n > 1:
        count += 1
        if count > 2:
            return count
        n //= spf[n]
    return count


def factors(n: int, spf: list[int]) -> list[int]:
    """返回带重数素因子。"""
    out: list[int] = []
    while n > 1:
        out.append(spf[n])
        n //= spf[n]
    return out


def prime_list(limit: int, spf: list[int]) -> list[int]:
    """列出素数。"""
    return [n for n in range(2, limit + 1) if spf[n] == n]


def first_p2_after_modulus(P: int, a: int, x_bound: int, spf: list[int]) -> dict[str, Any] | None:
    """找出固定列中第一个 n>P 的 P2 见证。"""
    start = a + P
    for n in range(start, x_bound + 1, P):
        om = omega_big(n, spf)
        if om <= 2:
            return {
                "a": a,
                "n": n,
                "kind": "prime" if om == 1 else "composite_p2",
                "factors": factors(n, spf),
            }
    return None


def audit_modulus(P: int, spf: list[int]) -> dict[str, Any]:
    """审计一个模数的最早 P2 选择器。"""
    x_bound = int(P**LZC_EXPONENT)
    prime_first = 0
    composite_first = 0
    missing_first = 0
    examples: list[dict[str, Any]] = []
    for a in range(1, P):
        hit = first_p2_after_modulus(P, a, x_bound, spf)
        if hit is None:
            missing_first += 1
            continue
        if hit["kind"] == "prime":
            prime_first += 1
        else:
            composite_first += 1
            if len(examples) < 5:
                examples.append(hit)
    return {
        "P": P,
        "x_bound_floor": x_bound,
        "prime_first_after_modulus_count": prime_first,
        "composite_p2_first_after_modulus_count": composite_first,
        "missing_p2_after_modulus_count": missing_first,
        "composite_first_after_modulus_share": composite_first / (P - 1),
        "least_p2_prime_selector_false_for_this_P": composite_first > 0,
        "examples": examples,
    }


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_payload() -> dict[str, Any]:
    """构造选择器反证 payload。"""
    spf = sieve_spf(SAMPLE_MAX_P * SAMPLE_MAX_P)
    moduli = [p for p in prime_list(SAMPLE_MAX_P, spf) if p >= 3]
    audits = [audit_modulus(P, spf) for P in moduli]
    first_counterexample = next(
        {
            "P": row["P"],
            "x_bound_floor": row["x_bound_floor"],
            "example": row["examples"][0],
        }
        for row in audits
        if row["examples"]
    )
    large_sample = [row for row in audits if row["P"] in SAMPLE_ROWS]
    max_composite_share = max(audits, key=lambda row: row["composite_first_after_modulus_share"])
    large_all_have_counterexamples = all(row["least_p2_prime_selector_false_for_this_P"] for row in large_sample)
    return {
        "certificate_type": "prime_matrix_p2_selector_route_rejection_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "least_p2_prime_selector_route_rejected_by_finite_counterexamples",
        "lzc_exponent": LZC_EXPONENT,
        "sample_max_prime_modulus": SAMPLE_MAX_P,
        "sample_modulus_count": len(audits),
        "selector_route_rejected": True,
        "selector_route_rejected_even_after_n_gt_P": True,
        "first_counterexample": first_counterexample,
        "large_sample_all_have_counterexamples": large_all_have_counterexamples,
        "max_composite_first_share": {
            "P": max_composite_share["P"],
            "share": max_composite_share["composite_first_after_modulus_share"],
        },
        "sample_rows": large_sample,
        "p2_to_prime_transfer_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "new_residual_basis_after_selector_rejection": [
            "SmallFactorCofactorAPCompositeFiberDominanceBound",
            "NonleastPrimeSelectorRequiresAdditionalDistributionInput",
            "FixedPrimeModulusZeroExceptionTransferForPrimeObjects",
            "SameObjectNonlinearActualSourceConstructorBeforeProjection",
            "PointwiseShortIntervalPrimeTheoremThetaLeHalf",
            "LinnikExponentLeTwoWithSquareWindowConstants",
        ],
        "external_source_notes": [
            {
                "name": "Li-Zhang-Cai least P2 almost-prime in AP",
                "url": "https://arxiv.org/abs/2103.13360",
                "role": "the least-P2 selector cannot be promoted to a prime selector",
            },
            {
                "name": "Ford-Maynard prime-producing sieve framework",
                "url": "https://arxiv.org/abs/2407.14368",
                "role": "its Type I/II prime-producing condition describes the kind of extra input needed beyond a P2 selector",
            },
            {
                "name": "Maynard well-factorable large-moduli estimates",
                "url": "https://arxiv.org/abs/2006.07088",
                "role": "mean-value AP technology remains an averaging tool, not a least-P2-to-prime selector",
            },
        ],
        "source_hashes": source_hashes(),
    }


def sample_markdown(rows: list[dict[str, Any]]) -> str:
    """生成样本表。"""
    lines = [
        "| P | X=floor(P^1.8345) | first P2 prime | first P2 composite | missing | composite share |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {P} | {X} | {prime} | {comp} | {missing} | {share:.6f} |".format(
                P=row["P"],
                X=row["x_bound_floor"],
                prime=row["prime_first_after_modulus_count"],
                comp=row["composite_p2_first_after_modulus_count"],
                missing=row["missing_p2_after_modulus_count"],
                share=row["composite_first_after_modulus_share"],
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    first = payload["first_counterexample"]
    example = first["example"]
    lines = [
        "# Prime Matrix P2 最早见证选择器路线反证审计",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "- “最早 P2 见证就是素数”不是可用破奇偶路线；它已有有限反例。",
        "- 该反例在排除平凡 `n<=P` 见证后仍存在。",
        "- 因此上一层剩余基中的 `PrimeBeforeCompositeP2SelectorInEveryFixedClass` 必须删除或改名为需要新分布输入的非最早选择器问题。",
        "",
        "## 2. 首个反例",
        "",
        "```text",
        f"P={first['P']}",
        f"X=floor(P^1.8345)={first['x_bound_floor']}",
        f"a={example['a']}",
        f"least_P2_after_P={example['n']}",
        f"factors={example['factors']}",
        "```",
        "",
        "## 3. 大样本审计",
        "",
        sample_markdown(payload["sample_rows"]),
        "",
        "```text",
        f"large_sample_all_have_counterexamples={bool_text(payload['large_sample_all_have_counterexamples'])}",
        "max_composite_first_share: P={P}, share={share:.6f}".format(**payload["max_composite_first_share"]),
        "```",
        "",
        "## 4. 更新后的剩余基",
        "",
        "```text",
        *payload["new_residual_basis_after_selector_rejection"],
        "```",
        "",
        "## 5. 边界声明",
        "",
        "本审计只排除一个错误选择器路线；它没有证明 P2 到素数的无条件转移。",
        "",
        "```text",
        f"selector_route_rejected={bool_text(payload['selector_route_rejected'])}",
        f"p2_to_prime_transfer_closed={bool_text(payload['p2_to_prime_transfer_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("selector_route_rejected=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
