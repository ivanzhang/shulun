#!/usr/bin/env python3
"""生成 1<k<P 内部行 LPF-owner 饱和证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_strict_k_internal_owner_saturation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json

输出：
  data/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-ledger.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.json
  docs/monograph/prime-matrix-phi-lpf-strict-k-internal-owner-saturation-router.md
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-strict-k-internal-owner-saturation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json",
    DOCS / "prime-matrix-phi-lpf-strict-k-endpoint-bucket-cancellation-router.json",
    DOCS / "prime-matrix-lowroot-sifted-deficit-frontier-router.json",
    DOCS / "prime-matrix-short-interval-rough-residue-barrier-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def spf_upto(n: int) -> list[int]:
    """返回最小素因子表；spf[1]=1。"""
    spf = list(range(n + 1))
    if n >= 0:
        spf[0] = 0
    if n >= 1:
        spf[1] = 1
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def phi_count(x: int, p: int, spf: list[int]) -> int:
    """计算 Phi(x,p)：1<=n<=x 且所有素因子都不小于 p 的个数。"""
    if x <= 0:
        return 0
    return sum(1 for n in range(1, x + 1) if n == 1 or spf[n] >= p)


def phi_bucket_deltas(a: int, b: int) -> dict[int, int]:
    """计算闭区间 [a,b] 的 Phi-LPF 桶端点增量。"""
    spf = spf_upto(b)
    deltas: dict[int, int] = {}
    for p in primes_upto(isqrt(b)):
        delta = phi_count(b // p, p, spf) - phi_count((a - 1) // p, p, spf)
        if delta:
            deltas[p] = delta
    return deltas


def direct_owner_partition(p_len: int, k: int) -> dict[str, Any]:
    """直接按 LPF owner 分桶内部行槽。"""
    a = k * p_len + 1
    b = k * p_len + p_len - 1
    spf = spf_upto(b)
    owners: Counter[int] = Counter()
    owner_slots: dict[int, list[int]] = {}
    prime_slots: list[int] = []
    composite_slots: list[int] = []
    for slot in range(1, p_len):
        n = k * p_len + slot
        if spf[n] == n:
            prime_slots.append(slot)
            continue
        owner = spf[n]
        owners[owner] += 1
        owner_slots.setdefault(owner, []).append(slot)
        composite_slots.append(slot)
    return {
        "owner_counts": {p: owners[p] for p in sorted(owners)},
        "owner_slots": {p: owner_slots[p] for p in sorted(owner_slots)},
        "prime_slots": prime_slots,
        "composite_slots": composite_slots,
    }


def owner_residue_rows(p_len: int, k: int, owner_slots: dict[int, list[int]]) -> list[dict[str, Any]]:
    """生成 owner residue 方程样本行。"""
    rows: list[dict[str, Any]] = []
    spf = spf_upto(k * p_len + p_len - 1)
    for owner, slots in owner_slots.items():
        residue = (-k * p_len) % owner
        rows.append(
            {
                "owner": owner,
                "residue_a_mod_owner": residue,
                "slot_count": len(slots),
                "slots_sample": slots[:12],
                "all_slots_have_owner": all(spf[k * p_len + slot] == owner for slot in slots),
                "all_slots_satisfy_residue": all(slot % owner == residue for slot in slots),
            }
        )
    return rows


def strict_k_owner_saturation_audit(p_len: int, k: int) -> dict[str, Any]:
    """审计 1<k<P 的内部行 LPF-owner 饱和形态。"""
    if not (1 < k < p_len):
        raise ValueError("本证书要求 1<k<P")
    a = k * p_len + 1
    b = k * p_len + p_len - 1
    direct = direct_owner_partition(p_len, k)
    phi_deltas = phi_bucket_deltas(a, b)
    owner_counts = direct["owner_counts"]
    length = p_len - 1
    composite_count = sum(owner_counts.values())
    prime_count = len(direct["prime_slots"])
    saturation_defect = length - composite_count
    return {
        "P": p_len,
        "k": k,
        "internal_interval": [a, b],
        "length": length,
        "root_bound": isqrt(b),
        "inside_p_square": b < p_len * p_len,
        "phi_bucket_deltas": phi_deltas,
        "direct_lpf_owner_counts": owner_counts,
        "phi_deltas_equal_direct_owner_counts": phi_deltas == owner_counts,
        "composite_count": composite_count,
        "prime_count": prime_count,
        "saturation_defect": saturation_defect,
        "saturation_defect_equals_prime_count": saturation_defect == prime_count,
        "zero_row_iff_owner_saturation": (prime_count == 0) == (composite_count == length),
        "prime_slots_sample": direct["prime_slots"][:20],
        "owner_residue_rows": owner_residue_rows(p_len, k, direct["owner_slots"]),
    }


def finite_sweep(max_prime: int = 97) -> dict[str, Any]:
    """有限审计 owner 饱和恒等式；不作全局证明。"""
    case_count = 0
    failures: list[dict[str, Any]] = []
    zero_rows_found: list[dict[str, int]] = []
    min_defect: int | None = None
    min_defect_cases: list[dict[str, int]] = []
    for p_len in [p for p in primes_upto(max_prime) if p >= 3]:
        for k in range(2, p_len):
            case_count += 1
            audit = strict_k_owner_saturation_audit(p_len, k)
            if not (
                audit["phi_deltas_equal_direct_owner_counts"]
                and audit["saturation_defect_equals_prime_count"]
                and audit["zero_row_iff_owner_saturation"]
            ):
                failures.append(audit)
            if audit["prime_count"] == 0:
                zero_rows_found.append({"P": p_len, "k": k})
            defect = audit["saturation_defect"]
            if min_defect is None or defect < min_defect:
                min_defect = defect
                min_defect_cases = [{"P": p_len, "k": k, "saturation_defect": defect}]
            elif defect == min_defect and len(min_defect_cases) < 12:
                min_defect_cases.append({"P": p_len, "k": k, "saturation_defect": defect})
    return {
        "max_prime": max_prime,
        "case_count": case_count,
        "all_owner_saturation_identities_verified": not failures,
        "failure_count": len(failures),
        "failure_sample": failures[:3],
        "zero_rows_found_in_finite_sweep": zero_rows_found,
        "minimum_saturation_defect": min_defect,
        "minimum_saturation_defect_cases": min_defect_cases,
        "finite_evidence_not_used_as_global_proof": True,
    }


def build_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "InternalPhiBucketEqualsLPFOwnerPartition",
            True,
            True,
            "内部行的 Phi 桶端点增量逐桶等于直接 LPF-owner 分桶计数。",
            "exact owner ledger",
        ),
        row(
            "OwnerResidueEquationPinned",
            True,
            True,
            "若槽 a 归入 owner p，则 a == -kP mod p 且 (kP+a)/p 为 p-rough。",
            "CRT residue plus rough cofactor",
        ),
        row(
            "SaturationDefectEqualsPrimeCount",
            True,
            True,
            "P-1 减去 owner 桶总质量，正是内部行素数数目。",
            "defect = row prime count",
        ),
        row(
            "ZeroRowIffOwnerSaturation",
            True,
            True,
            "零行反例等价于 LPF-owner 桶完全饱和 P-1 个内部槽。",
            "zero row means no saturation defect",
        ),
        row(
            "CapacityOnlyContradictionRejected",
            True,
            True,
            "owner 桶容量或样本正缺口不排除全饱和；仍需证明饱和缺陷为正。",
            "need non-circular lower bound",
        ),
        row(
            "PositiveSaturationDefectProved",
            False,
            False,
            "尚未证明每个 1<k<P 内部行的饱和缺陷为正。",
            "full-root uncovered-slot positivity",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把零行反例改写成 owner 饱和条件；未排除该条件。",
            "Q1/Q2 transport, seed/PDEC scope, signed table, Rate, DStructure",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书。"""
    sample_audits = [
        strict_k_owner_saturation_audit(5, 4),
        strict_k_owner_saturation_audit(11, 10),
        strict_k_owner_saturation_audit(17, 16),
        strict_k_owner_saturation_audit(101, 50),
        strict_k_owner_saturation_audit(101, 100),
    ]
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path) for path in DEPENDENCIES if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_phi_lpf_strict_k_internal_owner_saturation_router",
        "status": "strict_k_internal_owner_saturation_identity_closed_but_positive_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "strict_k_range": "1<k<P",
        "internal_phi_bucket_equals_lpf_owner_partition_proved": True,
        "owner_residue_equation_pinned": True,
        "saturation_defect_equals_prime_count_proved": True,
        "zero_row_iff_owner_saturation_proved": True,
        "positive_saturation_defect_proved": False,
        "row_column_unconditional_closed": False,
        "identity": "row_prime_count=(P-1)-sum_p Delta_internal_p=P-1-sum_p OwnerMass_p",
        "zero_row_condition": "zero row iff sum_p OwnerMass_p=P-1 iff LPF-owner buckets saturate every internal slot",
        "sample_audits": sample_audits,
        "finite_sweep": finite_sweep(),
        "gates": build_rows(),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            **dependency_hashes,
        },
        "plain_conclusion": (
            "严格 1<k<P 的内部行中，Phi-LPF 桶端点增量不是近似量，而是直接 LPF-owner 分桶计数。"
            "行内素数数目等于 P-1 减去所有 owner 桶质量。"
            "因此零行反例被精确改写为 owner 桶全饱和；剩余硬点是证明饱和缺陷始终为正。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF strict k internal owner saturation 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "## 1. Owner 饱和恒等式",
        "",
        "```text",
        result["identity"],
        result["zero_row_condition"],
        "```",
        "",
        "若内部槽 `a` 由 owner `p` 负责，则：",
        "",
        "```text",
        "a == -kP mod p,  (kP+a)/p is p-rough",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 样本审计",
            "",
            "| P | k | interval | owner mass | prime count | saturation defect | phi=owner | defect=prime |",
            "| ---: | ---: | --- | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for audit in result["sample_audits"]:
        lines.append(
            f"| {audit['P']} | {audit['k']} | {audit['internal_interval']} | "
            f"{audit['composite_count']} | {audit['prime_count']} | {audit['saturation_defect']} | "
            f"`{fmt_bool(audit['phi_deltas_equal_direct_owner_counts'])}` | "
            f"`{fmt_bool(audit['saturation_defect_equals_prime_count'])}` |"
        )
    lines.extend(
        [
            "",
            "## 4. Owner residue 样本",
            "",
            "| P | k | owner | residue a mod owner | slots sample | ok |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for audit in result["sample_audits"][:3]:
        for item in audit["owner_residue_rows"][:8]:
            ok = item["all_slots_have_owner"] and item["all_slots_satisfy_residue"]
            lines.append(
                f"| {audit['P']} | {audit['k']} | {item['owner']} | {item['residue_a_mod_owner']} | "
                f"`{item['slots_sample']}` | `{fmt_bool(ok)}` |"
            )
    sweep = result["finite_sweep"]
    lines.extend(
        [
            "",
            "## 5. 有限审计边界",
            "",
            "```text",
            f"max_prime={sweep['max_prime']}",
            f"case_count={sweep['case_count']}",
            f"all_owner_saturation_identities_verified={fmt_bool(sweep['all_owner_saturation_identities_verified'])}",
            f"zero_rows_found_in_finite_sweep={sweep['zero_rows_found_in_finite_sweep']}",
            f"minimum_saturation_defect={sweep['minimum_saturation_defect']}",
            "finite_evidence_not_used_as_global_proof=true",
            "```",
            "",
            "最小饱和缺陷样本：",
            "",
            "| P | k | saturation defect |",
            "| ---: | ---: | ---: |",
        ]
    )
    for item in sweep["minimum_saturation_defect_cases"]:
        lines.append(f"| {item['P']} | {item['k']} | {item['saturation_defect']} |")
    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            "Phi-LPF 已经把内部行完全变成 owner 桶账本。要证明 `[kP,kP+P]` 在 `1<k<P` 时有素数，",
            "等价于证明 owner 桶不能把 `P-1` 个内部槽全饱和。这个正缺陷仍是 row-prime 内容本身；",
            "下一步必须从 Q1/Q2 传输、seed/PDEC 作用域、signed table 或外部短区间输入中获得非循环信息。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
