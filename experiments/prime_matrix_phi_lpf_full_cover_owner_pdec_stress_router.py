#!/usr/bin/env python3
"""生成 Phi-LPF full-cover owner-residue PDEC 压力测试证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_full_cover_owner_pdec_stress_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-router.json

输出：
  data/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-ledger.json
  docs/monograph/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-router.json
  docs/monograph/prime-matrix-phi-lpf-full-cover-owner-pdec-stress-router.md
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

SLUG = "prime-matrix-phi-lpf-full-cover-owner-pdec-stress"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TARGET_RESIDUE = DOCS / "prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.json"
ROW_FRONTIER = DOCS / "prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json"
ROW_CONTRACT = DOCS / "prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json"
PRIME_CONTRACT = DOCS / "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    TARGET_RESIDUE,
    ROW_FRONTIER,
    ROW_CONTRACT,
    PRIME_CONTRACT,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

GENERIC_FULL_COVER_INTERVALS = [(90, 96), (114, 126), (200, 210)]
TARGET_SCAN_PRIMES = [31, 101, 251, 499, 1009, 2003, 5003]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def sieve(n: int) -> bytearray:
    """生成素数布尔表。"""
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


def primes_from_flags(flags: bytearray, n: int) -> list[int]:
    """提取不超过 n 的素数。"""
    return [p for p in range(2, n + 1) if flags[p]]


def least_prime_factor(n: int, primes: list[int]) -> int:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def owner_buckets(a: int, b: int, flags: bytearray, primes: list[int]) -> dict[int, list[int]]:
    """计算区间 (a,b] 中合数的 LPF owner buckets。"""
    buckets: dict[int, list[int]] = {}
    for n in range(a + 1, b + 1):
        if flags[n]:
            continue
        lpf = least_prime_factor(n, primes)
        if lpf < n:
            buckets.setdefault(lpf, []).append(n)
    return buckets


def one_residue_per_prime(a: int, buckets: dict[int, list[int]]) -> bool:
    """检查每个 owner bucket 是否落在同一个 offset residue class。"""
    for p, values in buckets.items():
        residues = {(n - a) % p for n in values}
        if len(residues) > 1:
            return False
    return True


def generic_full_cover_witnesses() -> list[dict[str, Any]]:
    """普通短区间 full-cover 见证，用于排除 owner-only PDEC。"""
    max_b = max(b for _, b in GENERIC_FULL_COVER_INTERVALS)
    flags = sieve(max_b)
    primes = primes_from_flags(flags, isqrt(max_b))
    witnesses: list[dict[str, Any]] = []
    for a, b in GENERIC_FULL_COVER_INTERVALS:
        buckets = owner_buckets(a, b, flags, primes)
        composite_cover = sum(len(v) for v in buckets.values())
        length = b - a
        prime_count = sum(flags[n] for n in range(a + 1, b + 1))
        witnesses.append(
            {
                "interval": f"({a},{b}]",
                "a": a,
                "b": b,
                "length": length,
                "prime_count": prime_count,
                "composite_cover": composite_cover,
                "full_cover": composite_cover == length,
                "owner_bucket_count": len(buckets),
                "owner_buckets": {str(p): values for p, values in sorted(buckets.items())},
                "owner_fibers_disjoint": composite_cover == sum(len(set(v)) for v in buckets.values()),
                "one_residue_per_prime": one_residue_per_prime(a, buckets),
                "target_anchor_A_equals_kP_with_P_length_plus_one": False,
            }
        )
    return witnesses


def top_owner_counts(buckets: dict[int, list[int]], limit: int = 8) -> list[dict[str, int]]:
    """列出最大的 owner buckets。"""
    rows = sorted(((p, len(values)) for p, values in buckets.items()), key=lambda item: (-item[1], item[0]))
    return [{"p": p, "count": count} for p, count in rows[:limit]]


def target_row_scan() -> list[dict[str, Any]]:
    """扫描目标行，记录最小 survivor defect 行的 owner 结构。"""
    max_p = max(TARGET_SCAN_PRIMES)
    flags = sieve(max_p * max_p)
    prime_table = primes_from_flags(flags, max_p)
    rows: list[dict[str, Any]] = []
    for p in TARGET_SCAN_PRIMES:
        if not flags[p]:
            raise ValueError(f"P must be prime: {p}")
        min_count: int | None = None
        min_k = 0
        max_count = 0
        zero_rows: list[int] = []
        for k in range(1, p):
            a = k * p
            b = (k + 1) * p - 1
            count = sum(flags[n] for n in range(a + 1, b + 1))
            if min_count is None or count < min_count:
                min_count = count
                min_k = k
            max_count = max(max_count, count)
            if count == 0:
                zero_rows.append(k)

        assert min_count is not None
        a = min_k * p
        b = (min_k + 1) * p - 1
        local_primes = [q for q in prime_table if q <= isqrt(b)]
        buckets = owner_buckets(a, b, flags, local_primes)
        composite_cover = sum(len(values) for values in buckets.values())
        row_length = p - 1
        rows.append(
            {
                "P": p,
                "min_k": min_k,
                "row": f"({a},{b}]",
                "row_length": row_length,
                "sqrt_bound": isqrt(b),
                "min_prime_count": min_count,
                "max_prime_count": max_count,
                "composite_cover_at_min_row": composite_cover,
                "strict_defect": row_length - composite_cover,
                "full_cover": composite_cover == row_length,
                "zero_row_count": len(zero_rows),
                "owner_bucket_count": len(buckets),
                "largest_owner_prime": max(buckets) if buckets else None,
                "top_owner_counts": top_owner_counts(buckets),
                "target_anchor_A_equals_kP_with_P_length_plus_one": True,
            }
        )
    return rows


def rejected_owner_only_predicates() -> list[dict[str, str]]:
    """列出已被普通 full-cover 见证排除的 naive PDEC 形式。"""
    return [
        {
            "predicate": "LPFOwnerFibersDisjointAndCoverRow",
            "reason_rejected": "generic full-cover intervals satisfy it with no contradiction",
            "surviving_requirement": "must use target anchor A=kP, P prime, k<P, length P-1",
        },
        {
            "predicate": "OneResidueClassPerPrimeFiber",
            "reason_rejected": "every ordinary interval has one divisibility residue class per prime after choosing offset from A",
            "surviving_requirement": "must exploit the special residues -kP mod p across all p, not one class locally",
        },
        {
            "predicate": "LPFRoughCofactorOwnerPartition",
            "reason_rejected": "this is exactly the LPF definition and is true in zero-prime ordinary intervals",
            "surviving_requirement": "must add a non-tautological CRT/phase incompatibility",
        },
        {
            "predicate": "EulerProductDensityOrWheelCapacityOnly",
            "reason_rejected": "full-cover witnesses show support capacity can saturate without signed information",
            "surviving_requirement": "must add Mobius/Von Mangoldt/trace cancellation or a named PDEC",
        },
    ]


def surviving_pdec_requirements() -> list[dict[str, str]]:
    """列出仍可能非循环的 full-cover PDEC 所需字段。"""
    return [
        {
            "field": "target_affine_anchor",
            "content": "A=kP, length=P-1, P prime, 1<=k<=P-1",
            "why_needed": "ordinary full-cover intervals lack this exact anchor",
        },
        {
            "field": "global_residue_coupling",
            "content": "a_p=-kP mod p for all p<=sqrt((k+1)P-1)",
            "why_needed": "local one-residue-per-prime facts are generic and cannot produce PDEC",
        },
        {
            "field": "owner_minimality",
            "content": "O_p=D_p minus union_{q<p}D_q with a named first-owner transition",
            "why_needed": "must distinguish owner buckets from coarse divisor support",
        },
        {
            "field": "signed_or_phase_payload",
            "content": "Mobius/Von Mangoldt sign, trace phase, or CRT phase packet before pushforward",
            "why_needed": "pure support is parity-blind and already known insufficient",
        },
    ]


def external_boundary_rows() -> list[dict[str, str]]:
    """记录相关外部理论接口的边界。"""
    return [
        {
            "input": "Jacobsthal / covering-system bounds",
            "source": "https://doi.org/10.1007/BF02564232",
            "usable_content": "general bounds on long runs covered by residue classes of small primes",
            "current_gap": "known general bounds are far above the one-row P scale needed here; no target-affine PDEC follows",
        },
        {
            "input": "Short-interval prime theorems",
            "source": "https://arxiv.org/abs/2405.20552",
            "usable_content": "zero-density driven primes in intervals thicker than x^(1/2)",
            "current_gap": "at x=P^2 the theorem still covers many rows, not one target row",
        },
        {
            "input": "Spectral/Kloosterman/Type-II methods",
            "source": "https://arxiv.org/abs/2509.04883",
            "usable_content": "AP/trace technology indicates the right kind of signed family",
            "current_gap": "the current LPF owner fibers have not been promoted to an admissible source-keyed trace family",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    target_residue = load_json(TARGET_RESIDUE)
    row_frontier = load_json(ROW_FRONTIER)
    row_contract = load_json(ROW_CONTRACT)
    prime_contract = load_json(PRIME_CONTRACT)

    generic_witnesses = generic_full_cover_witnesses()
    target_rows = target_row_scan()
    owner_only_rejected = all(row["full_cover"] and row["one_residue_per_prime"] for row in generic_witnesses)
    target_scan_no_full_cover = all(not row["full_cover"] for row in target_rows)
    synced = all(
        [
            target_residue.get("target_row_residue_cover_standard_form_synced") is True,
            row_frontier.get("breakthrough_formula_frontier_synced") is True,
            row_contract.get("row_delta_phi_identity_closed") is True,
            prime_contract.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
        ]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_full_cover_owner_pdec_stress_router",
        "status": "owner_only_pdec_rejected_target_affine_pdec_still_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "full_cover_owner_pdec_stress_synced": synced,
        "owner_only_pdec_rejected": owner_only_rejected,
        "target_affine_owner_pdec_proved": False,
        "target_scan_no_full_cover": target_scan_no_full_cover,
        "row_column_unconditional_closed": False,
        "generic_full_cover_witnesses": generic_witnesses,
        "target_min_defect_scan": target_rows,
        "rejected_owner_only_predicates": rejected_owner_only_predicates(),
        "surviving_pdec_requirements": surviving_pdec_requirements(),
        "external_boundary_rows": external_boundary_rows(),
        "selected_next_primary_gate": "TargetAffineFullCoverOwnerResiduePDEC",
        "selected_parallel_signed_gate": "MobiusResidueCoverSignedTraceWithTargetAffineAnchor",
        "selected_parallel_spectral_gate": "SpectralKloostermanResidueLiftWithSourceKeys",
        "plain_conclusion": (
            "Full-cover owner PDEC 不能只依赖 LPF owner 分桶、纤维互不相交或一素数一同余类；"
            "普通零素数短区间已经满足这些性质并形成 full cover。因此 owner-only PDEC 被排除。"
            "剩余可行口必须使用目标行特有的 A=kP、P 为素数、k<P、长度 P-1 的全局仿射锚，"
            "并附带 owner minimality 与 signed/phase payload。有限目标行扫描继续未见 full cover，"
            "但仍只是证据，不是证明。"
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格转义。"""
    return str(value).replace("|", r"\|")


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix Phi-LPF full-cover owner PDEC stress 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"full_cover_owner_pdec_stress_synced={fmt_bool(cert['full_cover_owner_pdec_stress_synced'])}",
        f"owner_only_pdec_rejected={fmt_bool(cert['owner_only_pdec_rejected'])}",
        f"target_affine_owner_pdec_proved={fmt_bool(cert['target_affine_owner_pdec_proved'])}",
        f"target_scan_no_full_cover={fmt_bool(cert['target_scan_no_full_cover'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. owner-only PDEC 的反例压力",
        "",
        "| interval | length | primes | full cover | owner buckets | one residue per prime |",
        "| --- | ---: | ---: | --- | ---: | --- |",
    ]
    for row in cert["generic_full_cover_witnesses"]:
        lines.append(
            f"| `{row['interval']}` | {row['length']} | {row['prime_count']} | "
            f"`{fmt_bool(row['full_cover'])}` | {row['owner_bucket_count']} | "
            f"`{fmt_bool(row['one_residue_per_prime'])}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 目标行最小缺口有限扫描",
            "",
            "| P | min-k | row | min primes | max primes | cover at min row | owner buckets | top owners |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in cert["target_min_defect_scan"]:
        lines.append(
            f"| {row['P']} | {row['min_k']} | `{row['row']}` | {row['min_prime_count']} | "
            f"{row['max_prime_count']} | {row['composite_cover_at_min_row']} | "
            f"{row['owner_bucket_count']} | `{cell(row['top_owner_counts'])}` |"
        )

    lines.extend(
        [
            "",
            "有限扫描只显示目标行 full cover 未出现；它不替代证明。",
            "",
            "## 3. 被排除的 naive PDEC",
            "",
            "| predicate | reason rejected | surviving requirement |",
            "| --- | --- | --- |",
        ]
    )
    for row in cert["rejected_owner_only_predicates"]:
        lines.append(
            f"| `{cell(row['predicate'])}` | {cell(row['reason_rejected'])} | "
            f"{cell(row['surviving_requirement'])} |"
        )

    lines.extend(
        [
            "",
            "## 4. 仍可非循环的 PDEC 字段",
            "",
            "| field | content | why needed |",
            "| --- | --- | --- |",
        ]
    )
    for row in cert["surviving_pdec_requirements"]:
        lines.append(f"| `{cell(row['field'])}` | `{cell(row['content'])}` | {cell(row['why_needed'])} |")

    lines.extend(
        [
            "",
            "## 5. 外部边界",
            "",
            "| input | usable content | current gap | source |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_boundary_rows"]:
        lines.append(
            f"| {cell(row['input'])} | {cell(row['usable_content'])} | "
            f"{cell(row['current_gap'])} | {cell(row['source'])} |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一手",
            "",
            "```text",
            f"selected_next_primary_gate={cert['selected_next_primary_gate']}",
            f"selected_parallel_signed_gate={cert['selected_parallel_signed_gate']}",
            f"selected_parallel_spectral_gate={cert['selected_parallel_spectral_gate']}",
            "```",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"full_cover_owner_pdec_stress_synced={fmt_bool(cert['full_cover_owner_pdec_stress_synced'])}")
    print(f"owner_only_pdec_rejected={fmt_bool(cert['owner_only_pdec_rejected'])}")
    print(f"target_affine_owner_pdec_proved={fmt_bool(cert['target_affine_owner_pdec_proved'])}")
    print(f"selected_next_primary_gate={cert['selected_next_primary_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
