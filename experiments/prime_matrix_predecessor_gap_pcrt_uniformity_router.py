#!/usr/bin/env python3
"""审计前素数间隙与 P 阶 CRT 非 P 列均匀性路线。

用法示例：
  python3 experiments/prime_matrix_predecessor_gap_pcrt_uniformity_router.py
  python3 experiments/prime_matrix_predecessor_gap_pcrt_uniformity_router.py --max-p 3000 --top 8
  python3 -m json.tool docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.json

输出：
  data/prime-matrix-predecessor-gap-pcrt-uniformity-ledger.json
  docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.json
  docs/monograph/prime-matrix-predecessor-gap-pcrt-uniformity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from bisect import bisect_right
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-predecessor-gap-pcrt-uniformity-ledger.json"
OUT_JSON = DOCS / "prime-matrix-predecessor-gap-pcrt-uniformity-router.json"
OUT_MD = DOCS / "prime-matrix-predecessor-gap-pcrt-uniformity-router.md"

SIGNED_PAYLOAD_SYNC = "prime-matrix-global-crt-signed-payload-sync-router.json"
CRT_HOMOGENEITY = "prime-matrix-global-crt-homogeneity-frontier-router.json"
EARLY_ZERO_GAP = "prime-matrix-early-zero-gap-crt-asymmetry-router.json"
PDEC_SCOPE = "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"

PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
LOCAL_TRANSFER = "LocalizedPCRTColumnUniformityTransferToInitialPxPSquare"

SOURCE_FILES = [
    SIGNED_PAYLOAD_SYNC,
    CRT_HOMOGENEITY,
    EARLY_ZERO_GAP,
    PDEC_SCOPE,
]


def sieve(limit: int) -> tuple[bytearray, list[int]]:
    """返回素数布尔表和素数表。"""
    if limit < 2:
        return bytearray(limit + 1), []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    root = int(limit**0.5)
    for n in range(2, root + 1):
        if flags[n]:
            start = n * n
            flags[start : limit + 1 : n] = b"\x00" * (((limit - start) // n) + 1)
    return flags, [i for i in range(2, limit + 1) if flags[i]]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def predecessor_gap_records(primes: list[int], max_p: int, top: int) -> list[dict[str, Any]]:
    """选出前素数间隙最大的若干 P。"""
    small = [p for p in primes if 3 < p <= max_p]
    records: list[dict[str, Any]] = []
    previous = 3
    for p in small:
        gap = p - previous
        records.append(
            {
                "P": p,
                "previous_prime": previous,
                "gap": gap,
                "first_row_gap_columns": max(0, gap - 1),
                "gap_over_log_p": gap / math.log(p),
                "gap_over_sqrt_p": gap / math.sqrt(p),
            }
        )
        previous = p
    records.sort(key=lambda item: (item["gap"], item["P"]), reverse=True)
    return records[:top]


def analyze_local_square(p: int, previous: int, prime_flags: bytearray, primes: list[int]) -> dict[str, Any]:
    """审计一个 P x P 初始方阵内的实际非 P 列素数分布。"""
    limit = p * p
    cutoff = bisect_right(primes, limit)
    counts = [0] * p
    for q in primes[:cutoff]:
        col = q % p
        if col:
            counts[col] += 1

    nonzero_counts = counts[1:]
    mean = sum(nonzero_counts) / (p - 1)
    min_count = min(nonzero_counts)
    max_count = max(nonzero_counts)
    zero_columns = [c for c in range(1, p) if counts[c] == 0]

    pair_diffs = []
    for c in range(1, (p + 1) // 2):
        pair_diffs.append((abs(counts[c] - counts[p - c]), c, p - c))
    max_pair = max(pair_diffs, default=(0, 0, 0))
    l1_pair_asymmetry = sum(item[0] for item in pair_diffs)

    gap_columns = list(range(previous + 1, p))
    repair_rows: list[int | None] = []
    unrepaired: list[int] = []
    for c in gap_columns:
        first_row = None
        for j in range(1, p):
            n = c + j * p
            if n <= limit and prime_flags[n]:
                first_row = j + 1
                break
        repair_rows.append(first_row)
        if first_row is None:
            unrepaired.append(c)

    repaired_rows = [r for r in repair_rows if r is not None]
    return {
        "P": p,
        "previous_prime": previous,
        "gap": p - previous,
        "first_row_gap_columns": len(gap_columns),
        "prime_count_in_initial_square": sum(nonzero_counts),
        "non_p_column_min": min_count,
        "non_p_column_max": max_count,
        "non_p_column_mean": mean,
        "non_p_column_zero_count": len(zero_columns),
        "zero_columns_sample": zero_columns[:12],
        "max_reflection_pair_difference": max_pair[0],
        "max_reflection_pair": [max_pair[1], max_pair[2]],
        "l1_reflection_pair_asymmetry": l1_pair_asymmetry,
        "gap_columns_repaired_in_square": len(gap_columns) - len(unrepaired),
        "gap_columns_unrepaired_in_square": len(unrepaired),
        "gap_unrepaired_columns_sample": unrepaired[:12],
        "gap_repair_row_min": min(repaired_rows) if repaired_rows else None,
        "gap_repair_row_max": max(repaired_rows) if repaired_rows else None,
        "gap_repair_row_sample": repair_rows[:12],
    }


def exact_p_wheel_identity() -> dict[str, str]:
    """登记完整 P-wheel 中的精确 CRT 均匀性恒等式。"""
    return {
        "period": "M_{<=P}=P*M_{<P}",
        "before_adding_P": (
            "在完整 M_{<=P} 周期中，对每个 c mod P，"
            "与 M_{<P} 互素的交集数均为 phi(M_{<P})。"
        ),
        "after_adding_P": (
            "加入 P 的零类后，c=0 列全部删除；每个 c in F_P^* 仍精确保留 "
            "phi(M_{<P}) 个非零同余类交集元素。"
        ),
        "reflection": "n -> -n mod M_{<=P} 给出 c <-> P-c 的精确全周期对称。",
        "gap_dependence": "前素数间隙 P-p^- 不改变上述全周期恒等式；它只说明第一行的若干实际素数原子缺失。",
    }


def build_rows(
    signed_payload_sync: dict[str, Any],
    crt_homogeneity: dict[str, Any],
    pdec_scope: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造判定表。"""
    latest_frontier_imported = (
        signed_payload_sync.get("next_direct_attack_target") == SIGNED_PAYLOAD
        and signed_payload_sync.get("row_column_unconditional_closed") is False
    )
    pure_crt_firewall_imported = (
        crt_homogeneity.get("pure_finite_crt_global_phase_contradiction_found") is False
        and crt_homogeneity.get("global_crt_homogeneity_blocks_pure_phase_contradiction") is True
    )
    pdec_scope_still_open = (
        pdec_scope.get("pdec_scope_proved") is False
        and pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
    )

    return [
        row(
            "ExactCompletePWheelNonPColumnUniformity",
            True,
            True,
            "完整 M_{<=P} 周期中，所有非 P 列的非零 CRT 交集元素数精确相等。",
            "closed as full-period identity",
        ),
        row(
            "ExactCompletePWheelReflectionSymmetry",
            True,
            True,
            "映射 n -> -n mod M_{<=P} 精确配对 c 与 P-c 两个非零列。",
            "closed as full-period identity",
        ),
        row(
            "PredecessorGapOnlyCreatesFirstRowLocalDeficit",
            True,
            True,
            "若 p^-<P 为前一素数，则第一行列 p^-+1,...,P-1 没有实际素数；这不是全周期 CRT 失衡。",
            LOCAL_TRANSFER,
        ),
        row(
            "FullWheelUniformityDoesNotLocalizeByItself",
            pure_crt_firewall_imported,
            True,
            "完整周期均匀性不能自动推出初始 P x P 短弧的列均匀或补偿位置。",
            f"{LOCAL_TRANSFER} OR {PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD}",
        ),
        row(
            "LargePredecessorGapSymmetryContradictionFound",
            False,
            False,
            "大前素数间隙没有改变完整 P-wheel 的精确均匀恒等式，也没有单独推出局部反例矛盾。",
            LOCAL_TRANSFER,
        ),
        row(
            "NonPColumnUniformityContradictionFound",
            False,
            False,
            "非 P 列全周期均匀性是真恒等式；局部非 P 列分布需要额外 actual-source 转移定理。",
            f"{PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD}",
        ),
        row(
            "LatestSignedPayloadFrontierImported",
            latest_frontier_imported,
            False,
            "最新 global CRT 路线已压到 signed payload；局部化转移若要自足，必须给出 payload 或新 PDEC scope。",
            SIGNED_PAYLOAD,
        ),
        row(
            "PDECScopeStillExternalOrNewInput",
            pdec_scope_still_open,
            False,
            "PDEC same-set 作用域仍可作为新证书输入，但当前内部语料未证。",
            PDEC_SCOPE_ATOM,
        ),
        row(
            "PredecessorGapPCRTCurrentCorpusClosesRowColumn",
            False,
            False,
            "本证书关闭的是把大前素数间隙和完整 P-wheel 均匀性误当成最终矛盾的跳步。",
            f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造前素数间隙/P-CRT 均匀性路由证书。"""
    prime_flags, primes = sieve(max_p * max_p)
    gap_records = predecessor_gap_records(primes, max_p, top)
    local_samples = [
        analyze_local_square(item["P"], item["previous_prime"], prime_flags, primes)
        for item in gap_records
    ]

    signed_payload_sync = load_json(SIGNED_PAYLOAD_SYNC)
    crt_homogeneity = load_json(CRT_HOMOGENEITY)
    pdec_scope = load_json(PDEC_SCOPE)
    rows = build_rows(signed_payload_sync, crt_homogeneity, pdec_scope)

    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD}) AND {EXACT_UV} AND {MODEL_LEDGER} "
        f"AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_predecessor_gap_pcrt_uniformity_router",
        "status": "predecessor_gap_pcrt_uniformity_routed_to_local_transfer_or_signed_payload_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "max_p_sample": max_p,
        "top_gap_sample_size": top,
        "complete_p_wheel_identity": exact_p_wheel_identity(),
        "top_predecessor_gap_records": gap_records,
        "local_square_samples": local_samples,
        "sample_non_p_column_zero_total": sum(item["non_p_column_zero_count"] for item in local_samples),
        "sample_gap_unrepaired_column_total": sum(item["gap_columns_unrepaired_in_square"] for item in local_samples),
        "complete_wheel_non_p_uniformity_proved": True,
        "complete_wheel_reflection_symmetry_proved": True,
        "localized_transfer_to_initial_square_proved": False,
        "large_predecessor_gap_symmetry_contradiction_found": False,
        "non_p_column_uniformity_contradiction_found": False,
        "atomic_signed_payload_constructor_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LOCAL_TRANSFER,
        "fallback_to_latest_frontier": f"{PDEC_SCOPE_ATOM}_OR_{SIGNED_PAYLOAD}",
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "大前素数间隙路线给出的核心事实是局部第一行实际素数缺口，而不是完整 P-wheel 的失衡。"
            "完整 M_{<=P} 周期内，CRT 交集在每个非 P 列精确等量，并且 c 与 P-c 精确反射对称；"
            "这些恒等式与 P 的前素数间隙无关。若要从该全周期均匀性推出初始 P x P 方阵内的补偿、"
            "非 P 列均匀或相位矛盾，必须新增局部化转移定理。当前语料没有该转移定理；该路线回流到 "
            "PDEC same-set scope 或 signed payload/ExactUV 前沿。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix 前素数间隙 P-CRT 均匀性路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"complete_wheel_non_p_uniformity_proved={fmt_bool(result['complete_wheel_non_p_uniformity_proved'])}",
        f"complete_wheel_reflection_symmetry_proved={fmt_bool(result['complete_wheel_reflection_symmetry_proved'])}",
        f"localized_transfer_to_initial_square_proved={fmt_bool(result['localized_transfer_to_initial_square_proved'])}",
        f"large_predecessor_gap_symmetry_contradiction_found={fmt_bool(result['large_predecessor_gap_symmetry_contradiction_found'])}",
        f"non_p_column_uniformity_contradiction_found={fmt_bool(result['non_p_column_uniformity_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 完整 P-wheel 恒等式",
        "",
        "| item | statement |",
        "| --- | --- |",
    ]
    for key, value in result["complete_p_wheel_identity"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines += [
        "",
        f"## 2. 最大前素数间隙样本（P <= {result['max_p_sample']}）",
        "",
        "| P | previous | gap | first-row gap cols | gap/log P | min/max non-P col primes | zero cols | max c/P-c diff | gap repairs |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    sample_by_p = {item["P"]: item for item in result["local_square_samples"]}
    for item in result["top_predecessor_gap_records"]:
        sample = sample_by_p[item["P"]]
        lines.append(
            "| {P} | {previous_prime} | {gap} | {first_row_gap_columns} | {gap_over_log_p:.3f} | "
            "{min_col}/{max_col} | {zero_cols} | {pair_diff} | {repairs}/{gap_cols} |".format(
                P=item["P"],
                previous_prime=item["previous_prime"],
                gap=item["gap"],
                first_row_gap_columns=item["first_row_gap_columns"],
                gap_over_log_p=item["gap_over_log_p"],
                min_col=sample["non_p_column_min"],
                max_col=sample["non_p_column_max"],
                zero_cols=sample["non_p_column_zero_count"],
                pair_diff=sample["max_reflection_pair_difference"],
                repairs=sample["gap_columns_repaired_in_square"],
                gap_cols=sample["first_row_gap_columns"],
            )
        )

    lines += [
        "",
        "样本只用于定位风险形态；证明不依赖经验无反例。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )

    lines += [
        "",
        "## 4. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件没有证明局部化转移定理，也没有证明 PDEC scope、signed payload、ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=5000, help="扫描的最大 P，默认 5000")
    parser.add_argument("--top", type=int, default=12, help="记录最大前素数间隙样本数，默认 12")
    return parser.parse_args()


def main() -> None:
    """写出路由证书。"""
    args = parse_args()
    result = build_result(args.max_p, args.top)
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p_sample": result["max_p_sample"],
                "sample_non_p_column_zero_total": result["sample_non_p_column_zero_total"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
