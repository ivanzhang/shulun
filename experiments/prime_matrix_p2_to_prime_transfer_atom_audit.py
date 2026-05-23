#!/usr/bin/env python3
"""Prime Matrix P2 到素数转移原子审计。

用法示例：
  python3 experiments/prime_matrix_p2_to_prime_transfer_atom_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-p2-to-prime-transfer-atom-audit.json

本脚本继续下钻 Li--Zhang--Cai 的 P2 almost-prime AP 输入：P2 见证能进
P^2 方阵，但若它不是素数，则必精确落入“小素因子 r + cofactor AP”的
双线性半素数纤维。该纤维分解是无条件闭合的小引理；真正未闭合的是证明
这些半素数纤维不能替代每个固定列中的素数。
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-p2-to-prime-transfer-atom"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
SAMPLE_MAX_P = 997
LZC_EXPONENT = 1.8345
SAMPLE_ROWS = [101, 199, 499, 997]

DEPENDENCIES = [
    DOCS / "prime-matrix-parity-breaking-obstruction-audit.json",
    DOCS / "prime-matrix-external-frontier-residual-gap-audit.json",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def md_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def bool_text(value: Any) -> str:
    """把布尔值输出为小写文本。"""
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
    """计算带重数素因子个数 Ω(n)，超过 2 后提前停止。"""
    count = 0
    while n > 1:
        p = spf[n]
        count += 1
        if count > 2:
            return count
        n //= p
    return count


def prime_list(limit: int, spf: list[int]) -> list[int]:
    """列出不超过 limit 的素数。"""
    return [n for n in range(2, limit + 1) if spf[n] == n]


def semiprime_pair(n: int, spf: list[int]) -> tuple[int, int]:
    """返回 Ω(n)=2 的有序因子对。"""
    r = spf[n]
    return r, n // r


def audit_modulus(P: int, spf: list[int]) -> dict[str, Any]:
    """审计一个素模数 P 的非零列 P2/prime 结构。"""
    prime_total = 0
    semiprime_total = 0
    least_p2_composite_residues = 0
    residues_without_prime_in_square = 0
    small_factor_failures = 0
    cofactor_ap_failures = 0
    lzc_small_factor_failures = 0
    lzc_bound = int(P**LZC_EXPONENT)
    lzc_prime_total = 0
    lzc_semiprime_total = 0
    lzc_residues_with_p2 = 0
    lzc_least_p2_composite_residues = 0

    for a in range(1, P):
        first_p2_kind = None
        first_p2_kind_lzc = None
        saw_prime = False
        saw_p2_lzc = False
        for n in range(a, P * P + 1, P):
            if n < 2:
                continue
            om = omega_big(n, spf)
            in_lzc = n <= lzc_bound
            if om == 1:
                prime_total += 1
                saw_prime = True
                if first_p2_kind is None:
                    first_p2_kind = "prime"
                if in_lzc:
                    lzc_prime_total += 1
                    saw_p2_lzc = True
                    if first_p2_kind_lzc is None:
                        first_p2_kind_lzc = "prime"
            elif om == 2:
                semiprime_total += 1
                if first_p2_kind is None:
                    first_p2_kind = "semiprime"
                r, m = semiprime_pair(n, spf)
                if not (r < P):
                    small_factor_failures += 1
                if (m - a * pow(r, -1, P)) % P != 0:
                    cofactor_ap_failures += 1
                if in_lzc:
                    lzc_semiprime_total += 1
                    saw_p2_lzc = True
                    if first_p2_kind_lzc is None:
                        first_p2_kind_lzc = "semiprime"
                    if not (r <= P ** (LZC_EXPONENT / 2) + 1e-12):
                        lzc_small_factor_failures += 1
        if first_p2_kind == "semiprime":
            least_p2_composite_residues += 1
        if not saw_prime:
            residues_without_prime_in_square += 1
        if saw_p2_lzc:
            lzc_residues_with_p2 += 1
        if first_p2_kind_lzc == "semiprime":
            lzc_least_p2_composite_residues += 1

    return {
        "P": P,
        "prime_total_square": prime_total,
        "semiprime_composite_total_square": semiprime_total,
        "semiprime_to_prime_ratio_square": semiprime_total / prime_total if prime_total else None,
        "least_p2_composite_residues_square": least_p2_composite_residues,
        "least_p2_composite_share_square": least_p2_composite_residues / (P - 1),
        "residues_without_prime_in_square": residues_without_prime_in_square,
        "small_factor_failures_square": small_factor_failures,
        "cofactor_ap_failures_square": cofactor_ap_failures,
        "lzc_bound_floor": lzc_bound,
        "lzc_prime_total": lzc_prime_total,
        "lzc_semiprime_composite_total": lzc_semiprime_total,
        "lzc_semiprime_to_prime_ratio": lzc_semiprime_total / lzc_prime_total if lzc_prime_total else None,
        "lzc_residues_with_p2": lzc_residues_with_p2,
        "lzc_least_p2_composite_residues": lzc_least_p2_composite_residues,
        "lzc_small_factor_failures": lzc_small_factor_failures,
    }


def source_hashes() -> dict[str, str]:
    """登记本脚本和直接依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_payload() -> dict[str, Any]:
    """构造 P2 到素数转移原子审计 payload。"""
    spf = sieve_spf(SAMPLE_MAX_P * SAMPLE_MAX_P)
    moduli = [p for p in prime_list(SAMPLE_MAX_P, spf) if p >= 11]
    audits = [audit_modulus(P, spf) for P in moduli]
    sample = [row for row in audits if row["P"] in SAMPLE_ROWS]
    max_ratio = max(audits, key=lambda row: row["semiprime_to_prime_ratio_square"] or -1)
    max_composite_share = max(audits, key=lambda row: row["least_p2_composite_share_square"])
    total_small_factor_failures = sum(row["small_factor_failures_square"] for row in audits)
    total_cofactor_ap_failures = sum(row["cofactor_ap_failures_square"] for row in audits)
    total_lzc_failures = sum(row["lzc_small_factor_failures"] for row in audits)
    return {
        "certificate_type": "prime_matrix_p2_to_prime_transfer_atom_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "p2_wrong_object_split_to_small_factor_cofactor_ap_fibers_open",
        "lzc_exponent": LZC_EXPONENT,
        "lzc_small_factor_exponent": LZC_EXPONENT / 2,
        "sample_max_prime_modulus": SAMPLE_MAX_P,
        "sample_modulus_count": len(audits),
        "exact_transfer_atom": {
            "statement": (
                "If P is prime, 1<=a<P, n≡a mod P, Ω(n)=2 and n<P^2, "
                "then n=r*m with prime r<P and m≡a*r^{-1} mod P. "
                "If n<=P^sigma with sigma<2, then r<=P^(sigma/2)."
            ),
            "proved_by_factor_ordering": True,
            "cofactor_ap_identity_closed": total_cofactor_ap_failures == 0,
            "small_factor_bound_sample_closed": total_small_factor_failures == 0,
            "lzc_small_factor_bound_sample_closed": total_lzc_failures == 0,
        },
        "sample_extrema": {
            "max_semiprime_to_prime_ratio_square": {
                "P": max_ratio["P"],
                "ratio": max_ratio["semiprime_to_prime_ratio_square"],
            },
            "max_least_p2_composite_share_square": {
                "P": max_composite_share["P"],
                "share": max_composite_share["least_p2_composite_share_square"],
            },
        },
        "sample_rows": sample,
        "aggregate_failures": {
            "small_factor_failures_square": total_small_factor_failures,
            "cofactor_ap_failures_square": total_cofactor_ap_failures,
            "lzc_small_factor_failures": total_lzc_failures,
        },
        "p2_to_prime_transfer_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "new_residual_basis_after_p2_atom": [
            "SmallFactorCofactorAPCompositeFiberDominanceBound",
            "PrimeBeforeCompositeP2SelectorInEveryFixedClass",
            "FixedPrimeModulusZeroExceptionTransferForPrimeObjects",
            "SameObjectNonlinearActualSourceConstructorBeforeProjection",
            "PointwiseShortIntervalPrimeTheoremThetaLeHalf",
            "LinnikExponentLeTwoWithSquareWindowConstants",
        ],
        "external_source_notes": [
            {
                "name": "Li-Zhang-Cai least P2 almost-prime in AP",
                "url": "https://arxiv.org/abs/2103.13360",
                "role": "supplies P2(a,q) << q^1.8345, which is square-compatible but not prime-object compatible",
            },
            {
                "name": "Ford-Maynard prime-producing sieve framework",
                "url": "https://arxiv.org/abs/2407.14368",
                "role": "indicates the right kind of Type I/II prime-producing information needed, but does not supply this Prime Matrix source",
            },
        ],
        "source_hashes": source_hashes(),
    }


def sample_markdown(rows: list[dict[str, Any]]) -> str:
    """生成样本表。"""
    lines = [
        "| P | primes <=P^2 | composite P2 <=P^2 | P2/prime ratio | least P2 composite share | LZC bound | LZC P2 residues |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {P} | {prime} | {semi} | {ratio:.6f} | {share:.6f} | {bound} | {lzc_res} |".format(
                P=row["P"],
                prime=row["prime_total_square"],
                semi=row["semiprime_composite_total_square"],
                ratio=row["semiprime_to_prime_ratio_square"],
                share=row["least_p2_composite_share_square"],
                bound=row["lzc_bound_floor"],
                lzc_res=row["lzc_residues_with_p2"],
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 审计文档。"""
    atom = payload["exact_transfer_atom"]
    lines = [
        "# Prime Matrix P2 到素数转移原子审计",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "- `P2` almost-prime 进入方阵只关闭位置门，不关闭素数对象门。",
        "- 合成 `P2` 见证在非零列中必有小素因子 `r<P`，并精确落到 cofactor AP `m=a*r^{-1} mod P`。",
        f"- 对 Li--Zhang--Cai 指数 `{payload['lzc_exponent']}`，小因子门进一步为 `r<=P^{payload['lzc_small_factor_exponent']}`。",
        "- 因此从 `P2` 升级到 prime 的真剩余不是筛恒等式，而是半素数 cofactor AP 纤维不能耗尽固定列。",
        "",
        "## 2. 精确转移原子",
        "",
        "```text",
        atom["statement"],
        f"cofactor_ap_identity_closed={bool_text(atom['cofactor_ap_identity_closed'])}",
        f"small_factor_bound_sample_closed={bool_text(atom['small_factor_bound_sample_closed'])}",
        f"lzc_small_factor_bound_sample_closed={bool_text(atom['lzc_small_factor_bound_sample_closed'])}",
        "```",
        "",
        "## 3. 有限样本读数",
        "",
        sample_markdown(payload["sample_rows"]),
        "",
        "样本极值：",
        "",
        "```text",
        "max_semiprime_to_prime_ratio_square: P={P}, ratio={ratio:.6f}".format(
            **payload["sample_extrema"]["max_semiprime_to_prime_ratio_square"]
        ),
        "max_least_p2_composite_share_square: P={P}, share={share:.6f}".format(
            **payload["sample_extrema"]["max_least_p2_composite_share_square"]
        ),
        "```",
        "",
        "## 4. 最新剩余基",
        "",
        "```text",
        *payload["new_residual_basis_after_p2_atom"],
        "```",
        "",
        "## 5. 边界声明",
        "",
        "本审计闭合的是 `P2` 合成见证的纤维定位，不是 P2 到素数的无条件转移。",
        "",
        "```text",
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
    print("p2_to_prime_transfer_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
