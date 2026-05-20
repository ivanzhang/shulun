#!/usr/bin/env python3
"""生成 Phi-LPF moving-atom 源桶前像同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_moving_atom_source_bucket_preimage_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.json

输出：
  data/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync-router.md
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

SLUG = "prime-matrix-phi-lpf-moving-atom-source-bucket-preimage-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_THREE_ATOMS = DOCS / "prime-matrix-phi-lpf-latest-alpha-terminal-three-atoms-sync-router.json"
LPF_OWNERSHIP = DOCS / "prime-matrix-lpf-ownership-sieve-source-declaration-router.json"
PHI_RECURSIVE = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
SUPPORT_STRIPPED = DOCS / "prime-matrix-phi-lpf-support-stripped-signed-kernel-router.json"
ROW_ORIGIN = DOCS / "prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json"
SOURCE_ENTROPY = DOCS / "prime-matrix-phi-lpf-source-entropy-signed-survival-router.json"
POINTWISE_TABLE = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
SQUARE_BASE = DOCS / "prime-matrix-phi-lpf-square-base-diagonal-source-router.json"
RATE_PACKET = DOCS / "prime-matrix-strict-rate-bearing-moving-atom-packet-dprc-sync-router.json"

INDEPENDENT_MOVING = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
A1_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
LPF_PREIMAGE = "LPFMovingAtomSourceBucketPreimagePartitionLedger"
SIGNED_INJECTION = "LPFMovingAtomSignedPreimageMassInjectionLedger"
POINTWISE_VALUE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
HIGH_SEGMENT = "HighSegmentModelGapAlpha043C3AnalyticLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
UV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 依赖；缺失视为未闭合。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
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


def primes_and_lpf(n: int) -> tuple[list[int], list[int]]:
    """给出素数表和最小素因子表。"""
    lpf = [0] * (n + 1)
    primes: list[int] = []
    for value in range(2, n + 1):
        if lpf[value] == 0:
            lpf[value] = value
            primes.append(value)
        for prime in primes:
            product = value * prime
            if product > n or prime > lpf[value]:
                break
            lpf[product] = prime
    return primes, lpf


def phi_rough_count(x: int, p: int, lpf: list[int]) -> int:
    """计算 Phi(x,p)：1 与所有最小素因子不小于 p 的整数。"""
    return sum(1 for value in range(1, x + 1) if value == 1 or lpf[value] >= p)


def sample_lpf_bucket_audit(n: int = 10_000) -> dict[str, Any]:
    """用 N=10000 审计 LPF/Phi 精确桶恒等式。"""
    primes, lpf = primes_and_lpf(n)
    sqrt_n = isqrt(n)
    prime_count = sum(1 for prime in primes if prime <= n)
    composite_count = n - 1 - prime_count
    bucket_rows: list[dict[str, int]] = []
    for prime in primes:
        if prime > sqrt_n:
            break
        x = n // prime
        phi_value = phi_rough_count(x, prime, lpf)
        bucket_rows.append(
            {
                "p": prime,
                "floor_n_over_p": x,
                "phi_floor_n_over_p_p": phi_value,
                "new_composites_c_p": phi_value - 1,
            }
        )
    bucket_sum = sum(item["new_composites_c_p"] for item in bucket_rows)
    return {
        "N": n,
        "sqrt_N": sqrt_n,
        "pi_actual": prime_count,
        "composite_actual": composite_count,
        "bucket_sum": bucket_sum,
        "pi_by_identity": n - 1 - bucket_sum,
        "identity_verified": bucket_sum == composite_count and n - 1 - bucket_sum == prime_count,
        "bucket_count": len(bucket_rows),
        "first_buckets": bucket_rows[:10],
        "last_bucket": bucket_rows[-1] if bucket_rows else {},
    }


def source_hashes() -> dict[str, str]:
    """登记本层依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        LATEST_THREE_ATOMS,
        LPF_OWNERSHIP,
        PHI_RECURSIVE,
        SUPPORT_STRIPPED,
        ROW_ORIGIN,
        SOURCE_ENTROPY,
        POINTWISE_TABLE,
        SQUARE_BASE,
        RATE_PACKET,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(deps: dict[str, dict[str, Any]], sample: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 moving-atom / LPF 源桶前像同步判定表。"""
    latest = deps["latest"]
    ownership = deps["ownership"]
    phi_recursive = deps["phi_recursive"]
    support = deps["support"]
    row_origin = deps["row_origin"]
    source_entropy = deps["source_entropy"]
    pointwise = deps["pointwise"]
    square_base = deps["square_base"]
    rate_packet = deps["rate_packet"]

    moving_frontier = latest.get("next_primary_attack_target") == INDEPENDENT_MOVING
    lpf_identity = (
        ownership.get("status") == "lpf_ownership_unsigned_declaration_closed_signed_constructor_open"
        and phi_recursive.get("status") == "phi_recursive_lpf_ownership_closed_signed_summand_expression_open"
        and support.get("status") == "phi_lpf_support_closed_signed_bucket_law_open"
        and row_origin.get("phi_lpf_support_and_capacity_closed") is True
        and sample["identity_verified"] is True
    )
    signed_open = (
        source_entropy.get("nonzero_signed_row_survival_proved") is False
        and source_entropy.get("same_formal_unit_row_mass_normalization_proved") is False
        and pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False
    )
    rate_interface = rate_packet.get("moving_atom_low_dim_or_no_signature_interface_closed") is True
    return [
        row(
            "LatestIndependentMovingAtomFrontierImported",
            moving_frontier,
            False,
            "latest alpha terminal three-atoms 同步已把当前直接主攻钉在 independent nonterminal moving atom。",
            INDEPENDENT_MOVING,
        ),
        row(
            "LPFPhiCompositeOwnershipIdentityImported",
            lpf_identity,
            True,
            "LPF ownership 与 Phi 递推给出合数支撑的唯一 owner bucket 和精确容量；N=10000 样本恒等式通过。",
            LPF_PREIMAGE,
        ),
        row(
            "MovingAtomUnsignedSourcePreimagePartitionClosed",
            moving_frontier and lpf_identity,
            True,
            "clean-core moving atom 若来自 actual composite source，其推前前源支撑可按唯一 `(p,m)`、`p=LPF(pm)`、`m` p-rough 分桶；无主 moving atom 出口被删除。",
            SIGNED_INJECTION,
        ),
        row(
            "PrimeRowLeakAndVirtualUnitPreimageBlocked",
            square_base.get("virtual_unit_not_composite_support_proved") is True
            and square_base.get("square_base_minimal_support_root_proved") is True,
            True,
            "Phi 公式中的 `m=1` 是 prime row 修正，不是 composite moving-atom source；真实最小源桶从 square-base `(p,p)` 开始。",
            SIGNED_INJECTION,
        ),
        row(
            "SignedMassInjectionNotGeneratedByUnsignedPhi",
            signed_open,
            False,
            "LPF/Phi 只给无符号支撑与容量；从 large same-(u,v) final atom 反推同 formal unit 的 signed preimage 质量仍需正向系数表与 no-heavy-row 账本。",
            f"{SIGNED_INJECTION} AND {POINTWISE_VALUE_TABLE} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "RateBearingPacketInterfaceImported",
            rate_interface,
            False,
            "已有 moving-block 同步消除了无名低维出口：低维签名进 PDEC/SAE/ColumnCRT，无签名进速率型终端包。",
            f"{PDEC_CLEAN_KLS} AND {HIGH_SEGMENT} AND {RATE}",
        ),
        row(
            "IndependentMovingAtomExclusionAfterLPFProved",
            False,
            False,
            "本层只删除无主/prime-row 源前像出口；仍未排斥 LPF-owned signed preimage 或速率型终端包。",
            f"{SIGNED_INJECTION} OR ({PDEC_CLEAN_KLS} AND {HIGH_SEGMENT} AND {RATE})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层是前沿同步与源桶前像归约，不是三目标命题无条件闭合。",
            f"({CANONICAL_LOCK} OR {A1_ADMISSION} OR {SIGNED_INJECTION}) AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Phi-LPF moving-atom 源桶前像同步证书。"""
    deps = {
        "latest": load_json(LATEST_THREE_ATOMS),
        "ownership": load_json(LPF_OWNERSHIP),
        "phi_recursive": load_json(PHI_RECURSIVE),
        "support": load_json(SUPPORT_STRIPPED),
        "row_origin": load_json(ROW_ORIGIN),
        "source_entropy": load_json(SOURCE_ENTROPY),
        "pointwise": load_json(POINTWISE_TABLE),
        "square_base": load_json(SQUARE_BASE),
        "rate_packet": load_json(RATE_PACKET),
    }
    sample = sample_lpf_bucket_audit()
    rows = build_rows(deps=deps, sample=sample)
    strict_basis = (
        f"({CANONICAL_LOCK} OR {A1_ADMISSION} OR {SIGNED_INJECTION}) "
        f"AND {UV_INCIDENCE} AND {RATE} AND {DSTRUCTURE}"
    )
    retained_basis = (
        f"(({LPF_PREIMAGE} AND {SIGNED_INJECTION}) OR {POINTWISE_VALUE_TABLE} OR "
        f"({PDEC_CLEAN_KLS} AND {HIGH_SEGMENT}) OR {MOVING_ATOM}) "
        f"AND {SIGNED_SURVIVAL} AND {ROW_MASS} AND {RATE} AND {DSTRUCTURE}"
    )
    sync_chain = [
        {
            "from": INDEPENDENT_MOVING,
            "to": MOVING_ATOM,
            "meaning": "independent nonterminal 版本仍以排斥 actual clean-core moving atom 为目标。",
        },
        {
            "from": MOVING_ATOM,
            "to": LPF_PREIMAGE,
            "meaning": "若 moving atom 来自 actual composite source，则每个推前前源键有唯一 LPF owner bucket。",
        },
        {
            "from": LPF_PREIMAGE,
            "to": SIGNED_INJECTION,
            "meaning": "无符号前像分桶已闭合；剩余是 signed 质量、local factor、branch 与 no-heavy-row 的同单位注入。",
        },
        {
            "from": SIGNED_INJECTION,
            "to": f"{POINTWISE_VALUE_TABLE} OR ({PDEC_CLEAN_KLS} AND {HIGH_SEGMENT})",
            "meaning": "若 signed 注入闭合，下一步必须由逐点 signed 表排斥，或落入速率型终端包/PDEC-CleanKLS 账本。",
        },
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_moving_atom_source_bucket_preimage_sync_router",
        "status": "phi_lpf_moving_atom_source_bucket_preimage_synced_signed_injection_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "latest_independent_moving_atom_frontier_imported": rows[0]["closed"],
        "lpf_phi_composite_ownership_identity_imported": rows[1]["closed"],
        "lpf_bucket_identity_sample_verified": sample["identity_verified"],
        "moving_atom_unsigned_source_preimage_partition_closed": rows[2]["closed"],
        "prime_row_leak_and_virtual_unit_preimage_blocked": rows[3]["closed"],
        "signed_mass_injection_proved": False,
        "rate_bearing_packet_exclusion_proved": False,
        "independent_nonterminal_moving_atom_exclusion_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": INDEPENDENT_MOVING,
        "absorbed_unsigned_escape": LPF_PREIMAGE,
        "next_primary_attack_target": SIGNED_INJECTION,
        "parallel_primary_attack_targets": [
            POINTWISE_VALUE_TABLE,
            SIGNED_SURVIVAL,
            ROW_MASS,
            PDEC_CLEAN_KLS,
            HIGH_SEGMENT,
            RATE,
            DSTRUCTURE,
        ],
        "strict_basis_after_router": strict_basis,
        "latest_retained_basis_after_router": retained_basis,
        "lpf_bucket_audit_sample": sample,
        "sync_chain": sync_chain,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把最新 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore` "
            "接到 LPF/Phi 源桶前像。LPF ownership 与 Phi 递推已经严格删除无主 moving atom "
            "和 prime-row/virtual-unit 源前像出口：若 clean-core moving atom 真实来自 composite source，"
            "它的推前前支撑必须分解为唯一 `(p,m)` 桶。这个结论仍是无符号支撑层，不能自动产生 "
            "signed coefficient、local factor、alpha/delta branch 或同 formal unit 的 no-heavy-row 质量注入。"
            f"最新直接主攻因此收窄为 `{SIGNED_INJECTION}`，并行保留逐点 Phi-LPF signed 表、"
            "signed survival/row-mass、PDEC/CleanKLS 速率包、高段模型余量、Rate 和 DStructure。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    sample = cert["lpf_bucket_audit_sample"]
    lines = [
        "# Prime Matrix Phi-LPF moving-atom source-bucket preimage sync 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"latest_independent_moving_atom_frontier_imported={fmt_bool(cert['latest_independent_moving_atom_frontier_imported'])}",
        f"lpf_phi_composite_ownership_identity_imported={fmt_bool(cert['lpf_phi_composite_ownership_identity_imported'])}",
        f"lpf_bucket_identity_sample_verified={fmt_bool(cert['lpf_bucket_identity_sample_verified'])}",
        f"moving_atom_unsigned_source_preimage_partition_closed={fmt_bool(cert['moving_atom_unsigned_source_preimage_partition_closed'])}",
        f"prime_row_leak_and_virtual_unit_preimage_blocked={fmt_bool(cert['prime_row_leak_and_virtual_unit_preimage_blocked'])}",
        f"signed_mass_injection_proved={fmt_bool(cert['signed_mass_injection_proved'])}",
        f"rate_bearing_packet_exclusion_proved={fmt_bool(cert['rate_bearing_packet_exclusion_proved'])}",
        f"independent_nonterminal_moving_atom_exclusion_proved={fmt_bool(cert['independent_nonterminal_moving_atom_exclusion_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. LPF/Phi 桶恒等式读数",
        "",
        "```text",
        "Phi(x,p_k) = Phi(x,p_{k+1}) + Phi(floor(x/p_k),p_k)",
        "C(N) = sum_{p<=sqrt(N)} (Phi(floor(N/p),p)-1)",
        "pi(N) = N - 1 - C(N)",
        "```",
        "",
        f"N={sample['N']} 的机器审计：`bucket_sum={sample['bucket_sum']}`，"
        f"`composite_actual={sample['composite_actual']}`，`pi_by_identity={sample['pi_by_identity']}`，"
        f"`pi_actual={sample['pi_actual']}`。",
        "",
        "| p | floor(N/p) | Phi(floor(N/p),p) | c(p) |",
        "| ---: | ---: | ---: | ---: |",
    ]
    for item in sample["first_buckets"]:
        lines.append(
            f"| {item['p']} | {item['floor_n_over_p']} | "
            f"{item['phi_floor_n_over_p_p']} | {item['new_composites_c_p']} |"
        )
    lines.extend(
        [
            "",
            "## 2. 同步链",
            "",
            "| from | to | meaning |",
            "| --- | --- | --- |",
        ]
    )
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. strict 基",
            "",
            "```text",
            cert["strict_basis_after_router"],
            "```",
            "",
            "## 5. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行主攻：",
            "",
            "```text",
            "\n".join(cert["parallel_primary_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
