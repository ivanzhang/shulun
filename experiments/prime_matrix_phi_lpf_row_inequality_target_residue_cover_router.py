#!/usr/bin/env python3
"""生成 Phi-LPF 行级不等式的目标行 residue-cover 标准形证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_row_inequality_target_residue_cover_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.json

输出：
  data/prime-matrix-phi-lpf-row-inequality-target-residue-cover-ledger.json
  docs/monograph/prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.json
  docs/monograph/prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.md
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

SLUG = "prime-matrix-phi-lpf-row-inequality-target-residue-cover"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ROW_CONTRACT = DOCS / "prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json"
ROW_FRONTIER = DOCS / "prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json"
PRIME_CONTRACT = DOCS / "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json"
TRANSPORT_EDGE = DOCS / "prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    ROW_CONTRACT,
    ROW_FRONTIER,
    PRIME_CONTRACT,
    TRANSPORT_EDGE,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

SCAN_PRIMES = [31, 101, 251, 499, 1009]
PRIME_FREE_INTERVALS = [(90, 96), (114, 126), (200, 210)]


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
    """生成 0..n 的素数布尔表。"""
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
    """从素数表提取不超过 n 的素数。"""
    return [p for p in range(2, n + 1) if flags[p]]


def least_prime_factor(n: int, primes: list[int]) -> int | None:
    """返回 n 的最小素因子；n 为素数时返回 n。"""
    if n < 2:
        return None
    for p in primes:
        if p * p > n:
            return n
        if n % p == 0:
            return p
    return n


def row_prime_count(flags: bytearray, a: int, b: int) -> int:
    """统计整数区间 (a,b] 的素数个数。"""
    return sum(flags[n] for n in range(a + 1, b + 1))


def ordinary_full_cover_samples() -> list[dict[str, Any]]:
    """给出任意短区间上严格覆盖缺口的反例样本。"""
    max_b = max(b for _, b in PRIME_FREE_INTERVALS)
    flags = sieve(max_b)
    primes = primes_from_flags(flags, isqrt(max_b))
    rows: list[dict[str, Any]] = []
    for a, b in PRIME_FREE_INTERVALS:
        owners: dict[int, list[int]] = {}
        for n in range(a + 1, b + 1):
            lpf = least_prime_factor(n, primes)
            if lpf is not None and lpf < n:
                owners.setdefault(lpf, []).append(n)
        composite_cover = sum(len(values) for values in owners.values())
        length = b - a
        primes_in_row = row_prime_count(flags, a, b)
        rows.append(
            {
                "interval": f"({a},{b}]",
                "length": length,
                "prime_count": primes_in_row,
                "delta_phi_cover": composite_cover,
                "full_cover_equality": composite_cover == length,
                "strict_defect": length - composite_cover,
                "owner_buckets": {str(p): values for p, values in sorted(owners.items())},
            }
        )
    return rows


def target_row_scan() -> list[dict[str, Any]]:
    """扫描目标 punctured 行 R_{P,k}=(kP,(k+1)P)，只作有限证据。"""
    max_p = max(SCAN_PRIMES)
    flags = sieve(max_p * max_p)
    rows: list[dict[str, Any]] = []
    for p in SCAN_PRIMES:
        counts: list[int] = []
        zero_rows: list[int] = []
        for k in range(1, p):
            a = k * p
            b = (k + 1) * p - 1
            count = row_prime_count(flags, a, b)
            counts.append(count)
            if count == 0:
                zero_rows.append(k)
        min_count = min(counts)
        min_k = counts.index(min_count) + 1
        rows.append(
            {
                "P": p,
                "row_model": "R_{P,k}={kP+r:1<=r<=P-1}, 1<=k<=P-1",
                "rows_scanned": p - 1,
                "min_prime_count": min_count,
                "min_prime_count_k": min_k,
                "max_prime_count": max(counts),
                "zero_row_count": len(zero_rows),
                "zero_rows": zero_rows,
                "strict_defect_found_in_every_scanned_row": len(zero_rows) == 0,
            }
        )
    return rows


def residue_cover_normal_form() -> list[dict[str, str]]:
    """列出目标行 residue-cover 标准形。"""
    return [
        {
            "object": "target row",
            "formula": "R_{P,k}={kP+r:1<=r<=P-1}, 1<=k<=P-1",
            "meaning": "目标行端点低于 P^2，因而任何合数都有最小素因子 < P。",
        },
        {
            "object": "coarse divisor fiber",
            "formula": "D_p(P,k)={r: 1<=r<=P-1, r == -kP mod p}",
            "meaning": "p<P 时 P 可逆，斜线/圆柱 residue fiber 是一个确定同余类。",
        },
        {
            "object": "LPF owner fiber",
            "formula": "O_p(P,k)=D_p(P,k) minus union_{q<p}D_q(P,k)",
            "meaning": "按最小素因子分桶后的 owner fiber 两两不交。",
        },
        {
            "object": "row prime count",
            "formula": "pi(R_{P,k})=#[1,P-1] minus union_{p<=sqrt((k+1)P-1)}D_p(P,k)",
            "meaning": "未被任何小素因子同余类覆盖的 offset 必为素数。",
        },
        {
            "object": "full-cover equality",
            "formula": "union_p D_p(P,k)=[1,P-1]",
            "meaning": "这是行级严格不等式失败的 residue-cover 形式，也是 PDEC/SAE 的唯一可攻等号态。",
        },
    ]


def attack_interface_rows() -> list[dict[str, str]]:
    """列出从 residue-cover 标准形出发的非循环攻击接口。"""
    return [
        {
            "name": "TargetPuncturedRowResidueCoverDefect",
            "statement": "union_{p<=sqrt((k+1)P-1)}D_p(P,k) != [1,P-1]",
            "status": "open; equivalent to target row prime positivity if used alone",
            "noncircular_requirement": "prove a structural obstruction to full cover that is not just a restatement of primality",
        },
        {
            "name": "FullCoverOwnerResiduePDEC",
            "statement": "full cover => named incompatible owner-residue/phase packet",
            "status": "open; selected next primary target",
            "noncircular_requirement": "extract a forbidden CRT/phase packet from the equality case before invoking prime existence",
        },
        {
            "name": "MobiusResidueCoverSignedTrace",
            "statement": "sum_{d|Q} mu(d) N_d(P,k)>0 with controlled source-key error",
            "status": "open",
            "noncircular_requirement": "obtain cancellation in the signed divisor sum at row length P, not just Euler-product density",
        },
        {
            "name": "SpectralKloostermanResidueLift",
            "statement": "complete the kP+r residue fibers into a uniform trace family",
            "status": "open",
            "noncircular_requirement": "supply conductor/coefficient control for q-spine/hinge source keys",
        },
    ]


def external_rows() -> list[dict[str, str]]:
    """记录外部定理在目标行尺度上的剩余缺口。"""
    return [
        {
            "input": "Guth--Maynard / Hieu",
            "source": "https://arxiv.org/abs/2405.20552 and https://arxiv.org/abs/2509.04883",
            "scale_at_x=P^2": "P^(17/15)",
            "row_thickness": "P^(2/15)",
            "status": "unconditional/preprint scale still thicker than one target row",
        },
        {
            "input": "Runbo Li Harman-sieve short intervals",
            "source": "https://arxiv.org/abs/2308.04458",
            "scale_at_x=P^2": "P^(26/25)",
            "row_thickness": "P^(1/25)",
            "status": "unconditional/preprint scale still thicker than one target row",
        },
        {
            "input": "Harm conditional short AP refinement",
            "source": "https://arxiv.org/abs/2507.15334",
            "scale_at_x=P^2": "P*exp((2log P)^alpha), alpha>2/3 under GDH",
            "row_thickness": "exp((2log P)^alpha)",
            "status": "conditional and still super-one-row; useful as near-critical boundary, not a closure input",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    row_contract = load_json(ROW_CONTRACT)
    row_frontier = load_json(ROW_FRONTIER)
    prime_contract = load_json(PRIME_CONTRACT)
    transport_edge = load_json(TRANSPORT_EDGE)

    generic_samples = ordinary_full_cover_samples()
    target_scan = target_row_scan()
    generic_defect_false = any(row["full_cover_equality"] for row in generic_samples)
    target_zero_found = any(row["zero_row_count"] for row in target_scan)
    target_synced = all(
        [
            row_contract.get("row_delta_phi_identity_closed") is True,
            row_frontier.get("breakthrough_formula_frontier_synced") is True,
            prime_contract.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
            transport_edge.get("transport_edge_sync_closed") is True,
        ]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_row_inequality_target_residue_cover_router",
        "status": "target_row_residue_cover_standard_form_synced_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "target_row_residue_cover_standard_form_synced": target_synced,
        "generic_interval_uniform_defect_false": generic_defect_false,
        "target_punctured_row_full_cover_found_in_scan": target_zero_found,
        "strict_cover_inequality_proved_uniformly": False,
        "row_column_unconditional_closed": False,
        "generic_full_cover_samples": generic_samples,
        "target_punctured_row_scan": target_scan,
        "residue_cover_normal_form": residue_cover_normal_form(),
        "attack_interface_rows": attack_interface_rows(),
        "external_rows": external_rows(),
        "selected_primary_next_gate": "FullCoverOwnerResiduePDEC",
        "selected_signed_parallel_gate": "MobiusResidueCoverSignedTrace",
        "selected_spectral_parallel_gate": "SpectralKloostermanResidueLift",
        "plain_conclusion": (
            "行级严格不等式不能推广为任意短区间命题；普通短区间存在 Delta-Phi full-cover "
            "等号。目标必须限制在 Prime Matrix punctured 行 R_{P,k}。在该行上，失败态等价于"
            "小素因子同余类 D_p(P,k) 覆盖全部 offset。下一步最快的非循环攻击不是再做无符号"
            "计数，而是从 full-cover equality 中抽取命名 owner-residue PDEC，或把 Mobius/trace "
            "签名求和接到同一 residue-cover 标准形上。"
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
        "# Prime Matrix Phi-LPF row inequality target residue-cover 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"target_row_residue_cover_standard_form_synced={fmt_bool(cert['target_row_residue_cover_standard_form_synced'])}",
        f"generic_interval_uniform_defect_false={fmt_bool(cert['generic_interval_uniform_defect_false'])}",
        f"target_punctured_row_full_cover_found_in_scan={fmt_bool(cert['target_punctured_row_full_cover_found_in_scan'])}",
        f"strict_cover_inequality_proved_uniformly={fmt_bool(cert['strict_cover_inequality_proved_uniformly'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 不能推广到任意短区间",
        "",
        "| interval | length | Delta-Phi cover | primes | full cover equality | owner buckets |",
        "| --- | ---: | ---: | ---: | --- | --- |",
    ]
    for row in cert["generic_full_cover_samples"]:
        lines.append(
            f"| `{row['interval']}` | {row['length']} | {row['delta_phi_cover']} | "
            f"{row['prime_count']} | `{fmt_bool(row['full_cover_equality'])}` | "
            f"`{cell(row['owner_buckets'])}` |"
        )

    lines.extend(
        [
            "",
            "## 2. 目标 punctured 行有限扫描",
            "",
            "| P | rows scanned | min primes | min-k | max primes | zero rows |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in cert["target_punctured_row_scan"]:
        lines.append(
            f"| {row['P']} | {row['rows_scanned']} | {row['min_prime_count']} | "
            f"{row['min_prime_count_k']} | {row['max_prime_count']} | {row['zero_row_count']} |"
        )

    lines.extend(
        [
            "",
            "有限扫描只定位结构，不作为全局证明。",
            "",
            "## 3. residue-cover 标准形",
            "",
            "| object | formula | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for row in cert["residue_cover_normal_form"]:
        lines.append(f"| `{cell(row['object'])}` | `{cell(row['formula'])}` | {cell(row['meaning'])} |")

    lines.extend(
        [
            "",
            "## 4. 下一层非循环接口",
            "",
            "| name | statement | status | noncircular requirement |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in cert["attack_interface_rows"]:
        lines.append(
            f"| `{cell(row['name'])}` | `{cell(row['statement'])}` | "
            f"{cell(row['status'])} | {cell(row['noncircular_requirement'])} |"
        )

    lines.extend(
        [
            "",
            "## 5. 外部输入尺度边界",
            "",
            "| input | scale at x=P^2 | row thickness | status | source |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_rows"]:
        lines.append(
            f"| {cell(row['input'])} | `{cell(row['scale_at_x=P^2'])}` | "
            f"`{cell(row['row_thickness'])}` | {cell(row['status'])} | {cell(row['source'])} |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一手",
            "",
            "```text",
            f"selected_primary_next_gate={cert['selected_primary_next_gate']}",
            f"selected_signed_parallel_gate={cert['selected_signed_parallel_gate']}",
            f"selected_spectral_parallel_gate={cert['selected_spectral_parallel_gate']}",
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
    print(f"target_row_residue_cover_standard_form_synced={fmt_bool(cert['target_row_residue_cover_standard_form_synced'])}")
    print(f"generic_interval_uniform_defect_false={fmt_bool(cert['generic_interval_uniform_defect_false'])}")
    print(f"target_punctured_row_full_cover_found_in_scan={fmt_bool(cert['target_punctured_row_full_cover_found_in_scan'])}")
    print(f"selected_primary_next_gate={cert['selected_primary_next_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
