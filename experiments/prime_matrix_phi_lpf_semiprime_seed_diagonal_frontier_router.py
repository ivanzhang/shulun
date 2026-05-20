#!/usr/bin/env python3
"""生成 Phi-LPF semiprime seed diagonal/offdiagonal 前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_semiprime_seed_diagonal_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier-router.md
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

SLUG = "prime-matrix-phi-lpf-semiprime-seed-diagonal-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FIRST_EDGE_ROUTER = DOCS / "prime-matrix-phi-lpf-first-edge-slab-frontier-router.json"
SQUARE_PACKET_ROUTER = DOCS / "prime-matrix-phi-lpf-square-base-source-packet-reduction-router.json"
POINTWISE_FRONTIER_CERT = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
ORIENTATION_TRACE_CERT = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_TRACE_CERT = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"

FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
DIAGONAL_SEED = "PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward"
OFFDIAG_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
ATOMIC_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SAMPLE_N = [30, 100, 997, 5003, 10000]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
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


def primes_up_to(n: int) -> list[int]:
    """返回不超过 n 的素数表。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = [False] * (((n - start) // p) + 1)
    return [value for value, is_prime in enumerate(sieve) if is_prime]


def is_p_rough(value: int, p: int, primes: list[int]) -> bool:
    """判断 value 是否没有小于 p 的素因子。"""
    return value >= 1 and all(value % q != 0 for q in primes if q < p)


def phi_rough(x: int, p: int, primes: list[int]) -> int:
    """直接计算 Phi(x,p)，包含 1。"""
    if x < 1:
        return 0
    return sum(1 for value in range(1, x + 1) if is_p_rough(value, p, primes))


def sample_semiprime_seed_audit(n: int) -> dict[str, Any]:
    """审计 semiprime first seed 的 diagonal/offdiagonal 拆分。"""
    primes = primes_up_to(n)
    small_primes = [p for p in primes if p <= math.isqrt(n)]
    first_edge_types: list[tuple[int, int]] = []
    diagonal_types: list[tuple[int, int]] = []
    offdiag_types: list[tuple[int, int]] = []
    diagonal_occurrences = 0
    offdiag_occurrences = 0
    total_occurrences = 0
    failures: list[str] = []

    for p in small_primes:
        for q in primes:
            if q < p or p * q > n:
                continue
            mass = phi_rough(n // (p * q), q, primes)
            if mass <= 0:
                failures.append(f"zero-mass p={p},q={q}")
                continue
            first_edge_types.append((p, q))
            total_occurrences += mass
            if p == q:
                diagonal_types.append((p, q))
                diagonal_occurrences += mass
            else:
                offdiag_types.append((p, q))
                offdiag_occurrences += mass

    diagonal_identity = len(diagonal_types) == len(small_primes)
    total_identity = total_occurrences == diagonal_occurrences + offdiag_occurrences
    return {
        "N": n,
        "small_prime_layers": len(small_primes),
        "first_edge_seed_types": len(first_edge_types),
        "diagonal_square_seed_types": len(diagonal_types),
        "offdiagonal_semiprime_seed_types": len(offdiag_types),
        "first_edge_occurrences": total_occurrences,
        "diagonal_square_seed_occurrences": diagonal_occurrences,
        "offdiagonal_semiprime_seed_occurrences": offdiag_occurrences,
        "diagonal_type_equals_small_prime_layers": diagonal_identity,
        "diagonal_offdiag_occurrence_partition_holds": total_identity and not failures,
        "diagonal_type_share": round(len(diagonal_types) / max(1, len(first_edge_types)), 12),
        "offdiag_type_share": round(len(offdiag_types) / max(1, len(first_edge_types)), 12),
        "diagonal_occurrence_share": round(diagonal_occurrences / max(1, total_occurrences), 12),
        "offdiag_occurrence_share": round(offdiag_occurrences / max(1, total_occurrences), 12),
        "formal_offdiag_type_sign_shadow_bits": len(offdiag_types),
        "formal_offdiag_type_sign_shadow_log10": round(len(offdiag_types) * math.log10(2), 6),
        "formal_diagonal_type_sign_shadow_bits": len(diagonal_types),
        "formal_diagonal_type_sign_shadow_log10": round(len(diagonal_types) * math.log10(2), 6),
        "failures": failures[:10],
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        FIRST_EDGE_ROUTER,
        SQUARE_PACKET_ROUTER,
        POINTWISE_FRONTIER_CERT,
        ORIENTATION_TRACE_CERT,
        BUILTIN_TRACE_CERT,
        EXACTUV_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(
    first_edge: dict[str, Any],
    square_packet: dict[str, Any],
    pointwise: dict[str, Any],
    orientation: dict[str, Any],
    builtin: dict[str, Any],
    exactuv: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 semiprime seed 前沿判定表。"""
    samples_ok = all(
        item["diagonal_type_equals_small_prime_layers"]
        and item["diagonal_offdiag_occurrence_partition_holds"]
        for item in samples
    )
    return [
        row(
            "SemiprimeFirstSeedTargetImported",
            FIRST_SEED in first_edge.get("next_direct_attack_targets", []),
            False,
            "上一层已把 first-edge slab 的 signed 缺口命名为 semiprime first-edge signed seed table。",
            FIRST_SEED,
        ),
        row(
            "DiagonalOffDiagonalSupportSplit",
            samples_ok,
            True,
            "semiprime first-edge seed 类型唯一分成 diagonal `p=q` 与 offdiagonal `p<q`。",
            f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
        ),
        row(
            "DiagonalSquareBasePrivateEscapeAlreadyRemoved",
            square_packet.get("no_square_base_private_signed_escape_proved") is True,
            True,
            "diagonal `(p,p)` 已由 square-base source packet reduction 证明没有私有 signed 出口。",
            COMMON_PACKET,
        ),
        row(
            "DiagonalCommonPacketStillOpen",
            square_packet.get("pre_cauchy_actual_noncanonical_emitter_source_declaration_packet_proved")
            is False,
            False,
            "diagonal square seed 回到 common packet；该 packet 仍不是已闭合 signed 来源。",
            COMMON_PACKET,
        ),
        row(
            "OffDiagonalSeedTableCurrentCorpusProved",
            False,
            False,
            "当前材料没有为所有 `p<q` ordered semiprime first edges 提交 signed seed 表。",
            OFFDIAG_SEED,
        ),
        row(
            "SemiprimeFirstSeedTableCurrentCorpusProved",
            False,
            False,
            "diagonal common packet 与 offdiagonal seed table 均未给出完整 signed first seed 表。",
            FIRST_SEED,
        ),
        row(
            "PointwisePhiLPFTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 signed value table 可替代 seed 表，但当前仍未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "CompleteBranchTraceWouldSupplySemiprimeSeed",
            orientation.get("complete_branch_trace_would_imply_orientation_law") is True,
            True,
            "完整 branch trace 可为 diagonal/offdiagonal seed 同时给 signed value、return tag 与 ExactUV。",
            BRANCH_TRACE,
        ),
        row(
            "AtomicTraceWouldSupplySemiprimeSeed",
            builtin.get("branch_trace_conditionally_suffices") is True,
            True,
            "atomic trace signed coefficient 公式可把 semiprime seed 作为 trace 字段读取。",
            ATOMIC_TRACE,
        ),
        row(
            "InternalTransitionStillPairedGate",
            first_edge.get("internal_prime_adjoin_signed_transition_law_proved") is False,
            False,
            "即使 semiprime seed 表存在，内部 prime-adjoin transition law 仍是配套门。",
            INTERNAL_TRANSITION,
        ),
        row(
            "ExactUVStillParallelGate",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False
            or exactuv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "seed/transition 表即使存在，ExactUV source entropy/fiber 仍是并行门。",
            EXACTUV_PAIR,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 semiprime seed 拆成 diagonal common-packet 与 offdiagonal seed；未证明三命题无条件闭合。",
            f"{COMMON_PACKET} AND {OFFDIAG_SEED} AND {INTERNAL_TRANSITION}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 semiprime seed diagonal 前沿证书。"""
    first_edge = load_json(FIRST_EDGE_ROUTER)
    square_packet = load_json(SQUARE_PACKET_ROUTER)
    pointwise = load_json(POINTWISE_FRONTIER_CERT)
    orientation = load_json(ORIENTATION_TRACE_CERT)
    builtin = load_json(BUILTIN_TRACE_CERT)
    exactuv = load_json(EXACTUV_CERT)
    samples = [sample_semiprime_seed_audit(n) for n in SAMPLE_N]
    rows = build_rows(first_edge, square_packet, pointwise, orientation, builtin, exactuv, samples)
    retained_basis = (
        f"(({COMMON_PACKET} AND {OFFDIAG_SEED} AND {INTERNAL_TRANSITION}) OR {POINTWISE_TABLE} "
        f"OR {BRANCH_TRACE} OR {ATOMIC_TRACE} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE} OR {NEW_JOINT_FORMULA}) "
        f"AND {EXACTUV_PAIR} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_semiprime_seed_diagonal_frontier_router",
        "status": "phi_lpf_semiprime_first_seed_split_to_diagonal_common_packet_and_offdiag_seed_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "semiprime_seed_diagonal_frontier_router_closed": True,
        "semiprime_first_edge_signed_seed_target_imported": FIRST_SEED
        in first_edge.get("next_direct_attack_targets", []),
        "diagonal_offdiagonal_support_split_proved": all(
            item["diagonal_offdiag_occurrence_partition_holds"] for item in samples
        ),
        "diagonal_square_base_private_signed_escape_removed": square_packet.get(
            "no_square_base_private_signed_escape_proved"
        )
        is True,
        "diagonal_common_packet_signed_source_proved": False,
        "offdiagonal_ordered_semiprime_signed_seed_table_proved": False,
        "semiprime_first_edge_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": FIRST_SEED,
        "next_primary_attack_target": OFFDIAG_SEED,
        "paired_required_attack_targets": [COMMON_PACKET, INTERNAL_TRANSITION],
        "parallel_direct_attack_target": POINTWISE_TABLE,
        "conditional_generators": [BRANCH_TRACE, ATOMIC_TRACE],
        "retained_basis_after_router": retained_basis,
        "sample_semiprime_seed_audit": samples,
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "semiprime first-edge signed seed table 可按 `p=q` 与 `p<q` 强制拆分。"
            "diagonal `(p,p)` 正是 square-base root，既有证书已排除它的私有 signed 出口，"
            "但它回到 common pre-Cauchy source packet 后仍未闭合。offdiagonal `(p,q), p<q` "
            "没有现成 signed seed 表。因而最新最窄主攻是 "
            "`PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward`，"
            "同时仍需 diagonal common packet 和 internal prime-adjoin transition law。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF semiprime seed diagonal frontier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"semiprime_first_edge_signed_seed_target_imported={fmt_bool(cert['semiprime_first_edge_signed_seed_target_imported'])}",
        f"diagonal_offdiagonal_support_split_proved={fmt_bool(cert['diagonal_offdiagonal_support_split_proved'])}",
        f"diagonal_square_base_private_signed_escape_removed={fmt_bool(cert['diagonal_square_base_private_signed_escape_removed'])}",
        f"diagonal_common_packet_signed_source_proved={fmt_bool(cert['diagonal_common_packet_signed_source_proved'])}",
        f"offdiagonal_ordered_semiprime_signed_seed_table_proved={fmt_bool(cert['offdiagonal_ordered_semiprime_signed_seed_table_proved'])}",
        f"semiprime_first_edge_signed_seed_table_proved={fmt_bool(cert['semiprime_first_edge_signed_seed_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 样本审计摘要",
            "",
            "| N | first types | diag types | offdiag types | first occ | diag occ | offdiag occ | diag type share | diag occ share | ok |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in cert["sample_semiprime_seed_audit"]:
        lines.append(
            f"| {item['N']} | {item['first_edge_seed_types']} | {item['diagonal_square_seed_types']} | "
            f"{item['offdiagonal_semiprime_seed_types']} | {item['first_edge_occurrences']} | "
            f"{item['diagonal_square_seed_occurrences']} | {item['offdiagonal_semiprime_seed_occurrences']} | "
            f"{item['diagonal_type_share']} | {item['diagonal_occurrence_share']} | "
            f"`{fmt_bool(item['diagonal_offdiag_occurrence_partition_holds'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "```text",
            cert["retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "配套仍需：",
            "",
            "```text",
            "\n".join(cert["paired_required_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 semiprime seed diagonal 前沿证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
