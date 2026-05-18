#!/usr/bin/env python3
"""生成 row-gap 供需/相位 cycle-cut 审计证书。

用法示例：
  python3 experiments/prime_matrix_row_gap_supply_phase_cycle_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.json

输出：
  data/prime-matrix-row-gap-supply-phase-cycle-cut-ledger.json
  docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.json
  docs/monograph/prime-matrix-row-gap-supply-phase-cycle-cut-router.md
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

OUT_LEDGER = DATA / "prime-matrix-row-gap-supply-phase-cycle-cut-ledger.json"
OUT_JSON = DOCS / "prime-matrix-row-gap-supply-phase-cycle-cut-router.json"
OUT_MD = DOCS / "prime-matrix-row-gap-supply-phase-cycle-cut-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-post-source-admission-macrocycle-sync-router.json",
    "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    "prime-matrix-strict-stable-short-return-defect-attack-router.json",
    "prime-matrix-strict-terminal-defect-exhaustion-router.json",
    "prime-matrix-strict-named-return-exclusion-compression-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
]

SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
LOW_ROOT_DEFICIT = "UniformLowRootSiftedResidueDeficitAfterNearRootSlots"
Q1Q2_TRANSPORT = "AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NAMED_RETURN = "NamedReturnExclusion"
EXTERNAL_GAP = "ExactExternalPrimeGapSqrtBarrierCertificate_FOR_ROW_GAP_ONLY"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SAMPLES = [
    (5, 4),
    (7, 6),
    (101, 50),
    (101, 100),
    (1009, 10),
    (1009, 900),
    (1009, 1008),
    (10007, 100),
    (10007, 9000),
]


def primes_upto(n: int) -> list[int]:
    """返回不超过 n 的素数表。"""
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(n + 1) if sieve[i]]


def is_prime(n: int) -> bool:
    """试除判素；样本规模很小，足够稳定。"""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def slot_set(P: int, X: int, primes: list[int]) -> set[int]:
    """给定素数集合，计算其在 row 内覆盖的列槽 a=1..P-1。"""
    slots: set[int] = set()
    for q in primes:
        target = (-X) % q
        slots.update(a for a in range(1, P) if a % q == target)
    return slots


def raw_capacity(P: int, X: int, primes: list[int]) -> int:
    """计算带重数的覆盖供给容量。"""
    return sum(1 for q in primes for a in range(1, P) if (X + a) % q == 0)


def sample_profile(P: int, k: int) -> dict[str, Any]:
    """计算一个 row-gap 样本的低根/近根供需画像。"""
    X = k * P
    upper = X + P - 1
    low_bound = isqrt(X)
    full_bound = isqrt(upper)
    primes_full = primes_upto(full_bound)
    primes_low = [q for q in primes_full if q <= low_bound]
    primes_root = [q for q in primes_full if q > low_bound]

    low_slots = slot_set(P, X, primes_low)
    root_slots = slot_set(P, X, primes_root)
    full_slots = low_slots | root_slots
    root_only = root_slots - low_slots
    prime_offsets = [a for a in range(1, P) if is_prime(X + a)]

    return {
        "P": P,
        "k": k,
        "X": X,
        "row_slots": P - 1,
        "low_bound_floor_sqrt_kP": low_bound,
        "full_bound_floor_sqrt_row_upper": full_bound,
        "low_prime_count": len(primes_low),
        "near_root_prime_count": len(primes_root),
        "low_raw_capacity": raw_capacity(P, X, primes_low),
        "near_root_raw_capacity": raw_capacity(P, X, primes_root),
        "low_union_slots": len(low_slots),
        "near_root_union_slots": len(root_slots),
        "near_root_only_slots": len(root_only),
        "full_union_slots": len(full_slots),
        "low_uncovered_slots": (P - 1) - len(low_slots),
        "full_uncovered_slots": (P - 1) - len(full_slots),
        "low_uncovered_minus_near_root_only": (P - 1) - len(low_slots) - len(root_only),
        "actual_prime_offsets_in_row": len(prime_offsets),
        "first_prime_offsets": prime_offsets[:12],
        "zero_row_exact_cover_condition": "full_uncovered_slots == 0",
        "low_root_deficit_condition_needed": "low_uncovered_minus_near_root_only > 0",
    }


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [
        f"docs/monograph/{name}"
        for name in SOURCE_FILES
        if not (DOCS / name).exists()
    ]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def build_rows(macro: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 row-gap 供需/相位判定表。"""
    macrocycle_imported = macro.get("a1_pdec_kz_macrocycle_detected") is True
    return [
        row(
            "RowGapModelPinned",
            True,
            True,
            "固定奇素数 P 与 1<=k<P，审查内部行 I_k={kP+a:1<=a<P} 无素数的反例模型。",
            "zero row means every a is covered by a prime divisor < P",
        ),
        row(
            "CorrectDivisorSupplyLaw",
            True,
            True,
            "若 kP+a 合数且 a<P，则 kP+a<P^2，所以它有一个素因子 q<P。",
            "small-prime cover by q<P",
        ),
        row(
            "LowRootOnlyClaimRejected",
            True,
            True,
            "不能只用 q<=sqrt(kP)：近根带 sqrt(kP)<q<=sqrt(kP+P-1) 可能覆盖边缘半素数槽。",
            "split low-root supply and near-root slots",
        ),
        row(
            "ExactCoverObligation",
            True,
            False,
            "零行等价于所有列槽被 q<=sqrt(kP+P-1) 的 residue classes 覆盖。",
            "prove full_uncovered_slots cannot be zero",
        ),
        row(
            "CapacityOnlyContradictionRejected",
            True,
            True,
            "带重数 raw capacity 通常大于 P；单纯供给总量不矛盾，必须控制重叠、相位和筛余。",
            LOW_ROOT_DEFICIT,
        ),
        row(
            "LowRootDeficitAfterNearRootSlotsOpen",
            True,
            False,
            "真正可攻的不等式是低根筛余槽数大于近根 only 槽容量，从而留下必为素数的槽。",
            LOW_ROOT_DEFICIT,
        ),
        row(
            "AdjacentQ1Q2GapLawPinned",
            True,
            False,
            "若 Q1<kP 与 Q2>(k+1)P 是相邻素数，则得到长度超过 P 的真实素数间隙。",
            "prime-gap or CRT-transport input",
        ),
        row(
            "CRTPeriodMirrorNotContradiction",
            True,
            True,
            "CRT 周期镜像只把覆盖块送到镜像覆盖块；没有同标签短复现或登记缺陷时不产生矛盾。",
            Q1Q2_TRANSPORT,
        ),
        row(
            "StableShortReturnImported",
            macrocycle_imported,
            False,
            "若 Q1/Q2 传输强制同 formal unit 的短同标签复现，则可用 prod(Q)|Delta 引理；尚未证明该强制。",
            Q1Q2_TRANSPORT,
        ),
        row(
            "PostSourceAdmissionMacrocycleImported",
            macrocycle_imported,
            True,
            "最新 A1/PDEC/KZ 宏循环已归档；row-gap 模型必须给循环外 primitive source 或 PDEC 作用域匹配。",
            SEED_CYCLE_CUT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步给出具体 row-gap 反例的精确供需/相位拆分，但没有证明统一筛余缺口或 Q1/Q2 传输矛盾。",
            f"({LOW_ROOT_DEFICIT} OR {Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {EXTERNAL_GAP}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造证书。"""
    macro = load_json("prime-matrix-strict-post-source-admission-macrocycle-sync-router.json")
    profiles = [sample_profile(P, k) for P, k in SAMPLES]
    rows = build_rows(macro)
    strict_basis = (
        f"({LOW_ROOT_DEFICIT} OR {Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} "
        f"OR {PDEC_SCOPE} OR {EXTERNAL_GAP}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "本步把具体 row-gap 反例 I_k={kP+a:1<=a<P} 无素数的想法拆成可审查的供需/相位结构。"
        "正确供给律是每个合数有素因子 q<P；但不能把供给全部限制到 q<=sqrt(kP)，因为近根带"
        " sqrt(kP)<q<=sqrt(kP+P-1) 会产生边缘半素数槽。原始容量总和通常不短缺，真正可攻点是"
        "低根筛余槽在扣除近根 only 槽后仍有正缺口，或者 Q1/Q2 相邻素数间隙在 CRT 传输中强制"
        "同 formal unit 短复现/登记缺陷。当前材料尚未证明这两个统一输入；因此本步把具体反例"
        "压到循环外 seed cycle-cut、direct PDEC 作用域匹配或外部 prime-gap/KZ 证书。"
    )
    return {
        "certificate_type": "prime_matrix_row_gap_supply_phase_cycle_cut_router",
        "status": "row_gap_supply_phase_reduced_to_lowroot_deficit_or_q1q2_transport_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "row_gap_model_pinned": True,
        "correct_divisor_supply_law": True,
        "low_root_only_claim_rejected": True,
        "capacity_only_contradiction_rejected": True,
        "crt_period_mirror_not_contradiction": True,
        "low_root_deficit_after_near_root_slots_proved": False,
        "q1q2_transport_defect_or_stable_short_return_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LOW_ROOT_DEFICIT,
        "parallel_attack_targets": [Q1Q2_TRANSPORT, SEED_CYCLE_CUT, PDEC_SCOPE, NAMED_RETURN],
        "strict_internal_basis_after_router": strict_basis,
        "sample_profiles": profiles,
        "decision_rows": rows,
        "missing_sources": missing_sources(),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix row-gap 供需/相位 cycle-cut 审计证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"row_gap_model_pinned={fmt_bool(cert['row_gap_model_pinned'])}",
        f"correct_divisor_supply_law={fmt_bool(cert['correct_divisor_supply_law'])}",
        f"low_root_only_claim_rejected={fmt_bool(cert['low_root_only_claim_rejected'])}",
        f"capacity_only_contradiction_rejected={fmt_bool(cert['capacity_only_contradiction_rejected'])}",
        f"crt_period_mirror_not_contradiction={fmt_bool(cert['crt_period_mirror_not_contradiction'])}",
        "low_root_deficit_after_near_root_slots_proved=false",
        "q1q2_transport_defect_or_stable_short_return_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. 精确 row-gap 模型",
        "",
        "设 `I_k={kP+a:1<=a<P}` 且 `1<=k<P`。若 `I_k` 无素数，则每个 `kP+a<P^2`",
        "都有一个素因子 `q<P`。但可证明的根界是 `q<=sqrt(kP+a)<=sqrt(kP+P-1)`，",
        "不是统一的 `q<=sqrt(kP)`。",
        "",
        "因此必须拆成：",
        "",
        "```text",
        "low-root primes:      q <= floor(sqrt(kP))",
        "near-root primes:     floor(sqrt(kP)) < q <= floor(sqrt(kP+P-1))",
        "zero-row obligation:  low-root slots union near-root slots covers every a=1..P-1",
        "```",
        "",
        "## 2. 样本供需画像",
        "",
        "| P | k | low bound | full bound | low union | near-root only | full uncovered | low uncovered - near-root only | actual primes |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in cert["sample_profiles"]:
        lines.append(
            "| {P} | {k} | {lo} | {hi} | {lu} | {ro} | {fu} | {gap} | {pr} |".format(
                P=item["P"],
                k=item["k"],
                lo=item["low_bound_floor_sqrt_kP"],
                hi=item["full_bound_floor_sqrt_row_upper"],
                lu=item["low_union_slots"],
                ro=item["near_root_only_slots"],
                fu=item["full_uncovered_slots"],
                gap=item["low_uncovered_minus_near_root_only"],
                pr=item["actual_prime_offsets_in_row"],
            )
        )
    lines.extend(
        [
            "",
            "表中最后两列在样本中相同，反映精确事实：`full_uncovered_slots` 正是该行内的素数槽。",
            "要把样本现象升级为证明，必须给出统一的低根筛余正缺口定理，而不能只引用样本。",
            "",
            "## 3. Q1/Q2 相邻素数 CRT 审查",
            "",
            "若零行成立且 `Q1<kP`、`Q2>(k+1)P` 是夹住该区间的相邻素数，则得到一个长度超过 `P` 的真实素数间隙。",
            "在 CRT 周期中，这只说明一个被小素数 residue classes 覆盖的块存在；镜像对称会给出镜像覆盖块，",
            "本身不是矛盾。要变成矛盾，必须额外证明：",
            "",
            "```text",
            "Q1/Q2 transport forces a stable same-formal-unit same-label short return",
            "OR every instability is a registered PDEC/SAE/ColumnCRT defect.",
            "```",
            "",
            "这正是当前 `Q1Q2` 传输输入，而不是已经闭合的事实。",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 5. 最新非循环基",
            "",
            "```text",
            cert["strict_internal_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书修正了 `q<=sqrt(kP)` 的过强供给前提。",
            "- 本证书不证明所有 row-gap 都不可能；它把该目标压到统一低根筛余缺口或 Q1/Q2 传输矛盾。",
            "- CRT 镜像对称不是矛盾，除非能证明同 formal unit 的短稳定复现或命名缺陷排斥。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    OUT_LEDGER.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
