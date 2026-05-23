#!/usr/bin/env python3
"""Prime Matrix 合成 P2 支持饱和审计。

用法示例：
  python3 experiments/prime_matrix_composite_p2_support_saturation_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-composite-p2-support-saturation-audit.json

本层继续下钻 P2 -> prime 的奇偶障碍：不再问“最早 P2 是否为素数”，而
问在 Li--Zhang--Cai 尺度 X=P^1.8345 内，合成 P2 对象自身是否已经覆盖
每个非零列，并在逐列计数上足以淹没 prime 对象。若答案为是，则任何只
使用 P2 residue 支持的路线都是奇偶盲的，必须引入真正区分素数与半素数
的对象敏感输入。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-composite-p2-support-saturation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
LZC_EXPONENT = 1.8345
SAMPLE_ROWS = [101, 199, 499, 997, 2003, 5003]

DEPENDENCIES = [
    DOCS / "prime-matrix-p2-to-prime-transfer-atom-audit.json",
    DOCS / "prime-matrix-p2-selector-route-rejection-audit.json",
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


def omega_capped(n: int, spf: list[int], cap: int = 3) -> int:
    """计算带重数素因子个数；超过 cap 后提前停止。"""
    count = 0
    while n > 1:
        count += 1
        if count >= cap:
            return count
        n //= spf[n]
    return count


def audit_modulus(P: int, spf: list[int]) -> dict[str, Any]:
    """审计一个素模数在 LZC 尺度内的 prime/P2 支持。"""
    x_bound = int(P**LZC_EXPONENT)
    prime_counts = [0] * P
    composite_p2_counts = [0] * P
    first_composite_examples: dict[int, int] = {}

    for n in range(2, x_bound + 1):
        residue = n % P
        if residue == 0:
            continue
        if spf[n] == n:
            prime_counts[residue] += 1
            continue
        if omega_capped(n, spf) == 2:
            composite_p2_counts[residue] += 1
            first_composite_examples.setdefault(residue, n)

    residues = range(1, P)
    prime_residue_count = sum(prime_counts[a] > 0 for a in residues)
    composite_residue_count = sum(composite_p2_counts[a] > 0 for a in residues)
    pointwise_ge_prime = sum(composite_p2_counts[a] >= prime_counts[a] for a in residues)
    pointwise_gt_prime = sum(composite_p2_counts[a] > prime_counts[a] for a in residues)
    count_differences = [composite_p2_counts[a] - prime_counts[a] for a in residues]
    example_items = sorted(first_composite_examples.items())[:8]

    return {
        "P": P,
        "x_bound_floor": x_bound,
        "prime_residue_count": prime_residue_count,
        "composite_p2_residue_count": composite_residue_count,
        "composite_p2_support_saturated": composite_residue_count == P - 1,
        "prime_support_saturated": prime_residue_count == P - 1,
        "min_prime_count_per_residue": min(prime_counts[1:]),
        "min_composite_p2_count_per_residue": min(composite_p2_counts[1:]),
        "total_prime_count": sum(prime_counts),
        "total_composite_p2_count": sum(composite_p2_counts),
        "composite_p2_to_prime_count_ratio": sum(composite_p2_counts) / sum(prime_counts),
        "residues_with_composite_count_ge_prime_count": pointwise_ge_prime,
        "residues_with_composite_count_gt_prime_count": pointwise_gt_prime,
        "pointwise_composite_count_ge_prime_all_residues": pointwise_ge_prime == P - 1,
        "pointwise_composite_count_gt_prime_all_residues": pointwise_gt_prime == P - 1,
        "min_composite_minus_prime_count": min(count_differences),
        "max_composite_minus_prime_count": max(count_differences),
        "first_composite_p2_examples": [
            {"residue": residue, "n": n} for residue, n in example_items
        ],
    }


def source_hashes() -> dict[str, str]:
    """登记本脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_payload() -> dict[str, Any]:
    """构造合成 P2 支持饱和 payload。"""
    max_x = int(max(SAMPLE_ROWS) ** LZC_EXPONENT)
    spf = sieve_spf(max_x)
    audits = [audit_modulus(P, spf) for P in SAMPLE_ROWS]
    first_strict_dominance = next(
        row for row in audits if row["pointwise_composite_count_gt_prime_all_residues"]
    )
    return {
        "certificate_type": "prime_matrix_composite_p2_support_saturation_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "composite_p2_residue_support_saturates_lzc_window_in_sample",
        "lzc_exponent": LZC_EXPONENT,
        "sample_rows": audits,
        "all_sample_rows_composite_p2_support_saturated": all(
            row["composite_p2_support_saturated"] for row in audits
        ),
        "first_sample_row_with_strict_pointwise_composite_dominance": {
            "P": first_strict_dominance["P"],
            "min_composite_minus_prime_count": first_strict_dominance[
                "min_composite_minus_prime_count"
            ],
        },
        "largest_sample_row": audits[-1],
        "support_only_p2_to_prime_transfer_rejected": True,
        "parity_blind_support_route_closed": False,
        "p2_to_prime_transfer_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "new_residual_basis_after_support_saturation": [
            "ObjectSensitivePrimeMinusCompositeP2SeparationInput",
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
                "role": "sets the P^1.8345 scale whose P2 support is audited here",
            },
            {
                "name": "Ford-Maynard prime-producing sieve framework",
                "url": "https://arxiv.org/abs/2407.14368",
                "role": "indicates that a true prime-producing input must be object-sensitive, not merely P2-support-positive",
            },
            {
                "name": "Runbo Li large-moduli AP mean-value inputs",
                "url": "https://arxiv.org/abs/2602.20917",
                "role": "remains mean-value AP technology and does not remove this fixed-column support obstruction",
            },
        ],
        "source_hashes": source_hashes(),
    }


def sample_markdown(rows: list[dict[str, Any]]) -> str:
    """生成样本表。"""
    lines = [
        "| P | X=floor(P^1.8345) | prime support | composite P2 support | min comp P2 | comp/prime ratio | comp>=prime cols | comp>prime cols | min(comp-prime) |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {P} | {X} | {ps}/{cols} | {cs}/{cols} | {minc} | {ratio:.6f} | {ge}/{cols} | {gt}/{cols} | {mindiff} |".format(
                P=row["P"],
                X=row["x_bound_floor"],
                ps=row["prime_residue_count"],
                cs=row["composite_p2_residue_count"],
                cols=row["P"] - 1,
                minc=row["min_composite_p2_count_per_residue"],
                ratio=row["composite_p2_to_prime_count_ratio"],
                ge=row["residues_with_composite_count_ge_prime_count"],
                gt=row["residues_with_composite_count_gt_prime_count"],
                mindiff=row["min_composite_minus_prime_count"],
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    first_strict = payload["first_sample_row_with_strict_pointwise_composite_dominance"]
    largest = payload["largest_sample_row"]
    lines = [
        "# Prime Matrix 合成 P2 支持饱和审计",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "- 在 Li--Zhang--Cai 尺度 `X=P^1.8345` 内，样本行的合成 `P2` 对象本身已经覆盖全部非零列。",
        "- 从 `P=499` 起，样本中每个非零列的合成 `P2` 计数都严格大于素数计数。",
        "- 因此只使用 `P2` residue 支持或列覆盖的路线是奇偶盲的；必须加入区分 prime 与合成 `P2` 的对象敏感输入。",
        "",
        "## 2. 样本审计",
        "",
        sample_markdown(payload["sample_rows"]),
        "",
        "```text",
        f"all_sample_rows_composite_p2_support_saturated={bool_text(payload['all_sample_rows_composite_p2_support_saturated'])}",
        "first_strict_pointwise_composite_dominance: P={P}, min(comp-prime)={min_composite_minus_prime_count}".format(
            **first_strict
        ),
        "largest_sample: P={P}, min_composite_p2_count={minc}, comp/prime_ratio={ratio:.6f}".format(
            P=largest["P"],
            minc=largest["min_composite_p2_count_per_residue"],
            ratio=largest["composite_p2_to_prime_count_ratio"],
        ),
        "```",
        "",
        "## 3. 更新后的剩余基",
        "",
        "```text",
        *payload["new_residual_basis_after_support_saturation"],
        "```",
        "",
        "## 4. 边界声明",
        "",
        "本审计删除的是 support-only 的 P2-to-prime 伪路线；它不是全 P 的定理，也没有证明素数存在命题。",
        "",
        "```text",
        f"support_only_p2_to_prime_transfer_rejected={bool_text(payload['support_only_p2_to_prime_transfer_rejected'])}",
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
    print("support_only_p2_to_prime_transfer_rejected=true")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
