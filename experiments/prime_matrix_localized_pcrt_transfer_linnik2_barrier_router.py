#!/usr/bin/env python3
"""审计 localized P-CRT 转移与 Linnik=2 屏障。

用法示例：
  python3 experiments/prime_matrix_localized_pcrt_transfer_linnik2_barrier_router.py
  python3 experiments/prime_matrix_localized_pcrt_transfer_linnik2_barrier_router.py --max-p 3000 --top 10
  python3 -m json.tool docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json

输出：
  data/prime-matrix-localized-pcrt-transfer-linnik2-barrier-ledger.json
  docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json
  docs/monograph/prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-localized-pcrt-transfer-linnik2-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.md"

PREDECESSOR_GAP = "prime-matrix-predecessor-gap-pcrt-uniformity-router.json"
SIGNED_PAYLOAD = "prime-matrix-global-crt-signed-payload-sync-router.json"
PDEC_SCOPE = "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

LOCAL_TRANSFER = "LocalizedPCRTColumnUniformityTransferToInitialPxPSquare"
L2_AP = "PointwiseLeastPrimeInEveryNonzeroClassModPBelowP2"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / PREDECESSOR_GAP,
    DOCS / SIGNED_PAYLOAD,
    DOCS / PDEC_SCOPE,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_X,
]


def sieve(limit: int) -> tuple[bytearray, list[int]]:
    """返回素数布尔表和素数表。"""
    if limit < 2:
        return bytearray(limit + 1), []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    root = math.isqrt(limit)
    for n in range(2, root + 1):
        if flags[n]:
            start = n * n
            flags[start : limit + 1 : n] = b"\x00" * (((limit - start) // n) + 1)
    return flags, [i for i in range(2, limit + 1) if flags[i]]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result: dict[str, str] = {}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


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


def first_ap_prime_record(p: int, flags: bytearray) -> dict[str, Any]:
    """计算每个非零剩余类在 P^2 内首个素数的最坏行号。"""
    worst: dict[str, Any] = {
        "residue": None,
        "first_prime": None,
        "row_index": -1,
    }
    missing: list[int] = []
    row_sum = 0
    max_value = p * p
    for a in range(1, p):
        found = None
        for r in range(p):
            n = a + r * p
            if n <= max_value and flags[n]:
                found = n
                break
        if found is None:
            missing.append(a)
            continue
        row_index = (found - a) // p + 1
        row_sum += row_index
        if row_index > worst["row_index"]:
            worst = {"residue": a, "first_prime": found, "row_index": row_index}
    return {
        "P": p,
        "worst_residue": worst["residue"],
        "worst_first_prime": worst["first_prime"],
        "worst_row_index": worst["row_index"],
        "worst_row_fraction": worst["row_index"] / p if worst["row_index"] >= 0 else None,
        "missing_residue_count": len(missing),
        "missing_residue_sample": missing[:12],
        "mean_first_row_index": row_sum / (p - 1),
    }


def sample_ap_barrier(max_p: int, top: int) -> dict[str, Any]:
    """扫描小范围样本中的最坏 AP 首素数位置。"""
    flags, primes = sieve(max_p * max_p)
    prime_moduli = [p for p in primes if 3 <= p <= max_p]
    records = [first_ap_prime_record(p, flags) for p in prime_moduli]
    records.sort(key=lambda item: (item["missing_residue_count"], item["worst_row_index"], item["P"]), reverse=True)
    return {
        "max_p": max_p,
        "prime_moduli_checked": len(prime_moduli),
        "missing_total": sum(item["missing_residue_count"] for item in records),
        "worst_row_index_max": records[0]["worst_row_index"] if records else None,
        "worst_row_fraction_max": records[0]["worst_row_fraction"] if records else None,
        "top_records": records[:top],
    }


def equivalence_chain() -> list[dict[str, str]]:
    """列出局部化转移到 Linnik=2 屏障的等价链。"""
    return [
        {
            "from": LOCAL_TRANSFER,
            "to": "initial-square non-P column occupancy",
        },
        {
            "from": "initial-square non-P column occupancy",
            "to": L2_AP,
        },
        {
            "from": L2_AP,
            "to": "prime-modulus pointwise least-prime-in-AP exponent 2",
        },
        {
            "from": "pure complete P-wheel CRT identity",
            "to": "global average only; no pointwise short AP localization",
        },
        {
            "from": "failure to prove L2_AP internally",
            "to": f"{PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM}",
        },
    ]


def build_rows(
    predecessor: dict[str, Any],
    signed_payload: dict[str, Any],
    pdec_scope: dict[str, Any],
) -> list[dict[str, Any]]:
    """构造判定表。"""
    local_transfer_active = predecessor.get("next_direct_attack_target") == LOCAL_TRANSFER
    signed_payload_active = signed_payload.get("next_direct_attack_target") == SIGNED_PAYLOAD_ATOM
    pdec_open = (
        pdec_scope.get("pdec_scope_proved") is False
        and pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
    )

    return [
        row(
            "LocalizedPCRTTransferActive",
            local_transfer_active,
            False,
            "上一层把前素数间隙/P-wheel 均匀性路线压到初始方阵局部化转移。",
            LOCAL_TRANSFER,
        ),
        row(
            "ColumnOccupancyEquivalentToLeastPrimeAP",
            True,
            True,
            "非 P 列 c 有素数等价于存在素数 ell<=P^2 且 ell=c mod P。",
            L2_AP,
        ),
        row(
            "Linnik2BarrierIdentified",
            True,
            True,
            "对所有非零 c mod P 证明 ell<=P^2 是 prime-modulus 点态最小 AP 素数指数 2。",
            "new pointwise AP theorem required",
        ),
        row(
            "CompleteCRTUniformityOnlyAverage",
            True,
            True,
            "完整 P-wheel 非 P 列等量是全周期平均恒等式，不含短 AP 点态首素数信息。",
            f"{LOCAL_TRANSFER} or {L2_AP}",
        ),
        row(
            "BVOrMeanAPInsufficientForPointwiseAllColumns",
            True,
            True,
            "平均 AP 均匀性最多控制几乎所有列；目标要求每一列，不能留下单个异常类。",
            "pointwise capacity lower bound or new AP input",
        ),
        row(
            "LocalizedTransferCurrentCorpusProved",
            False,
            False,
            "当前语料没有从完整 CRT 周期均匀性推出每个初始短 AP 均命中的定理。",
            L2_AP,
        ),
        row(
            "SignedPayloadFrontierStillActive",
            signed_payload_active,
            False,
            "若不引入外部 AP 定理，结构路线仍需 signed payload 正向构造。",
            SIGNED_PAYLOAD_ATOM,
        ),
        row(
            "PDECScopeStillOpen",
            pdec_open,
            False,
            "PDEC same-set 作用域仍是可提交的新证书入口，但当前未证。",
            PDEC_SCOPE_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步把局部化转移压成点态 AP/Linnik=2 屏障，尚未给出全局无条件矛盾。",
            f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {L2_AP}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result(max_p: int, top: int) -> dict[str, Any]:
    """构造 localized P-CRT/Linnik=2 屏障证书。"""
    predecessor = load_json(DOCS / PREDECESSOR_GAP)
    signed_payload = load_json(DOCS / SIGNED_PAYLOAD)
    pdec_scope = load_json(DOCS / PDEC_SCOPE)
    sample = sample_ap_barrier(max_p, top)
    rows = build_rows(predecessor, signed_payload, pdec_scope)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {L2_AP}) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_localized_pcrt_transfer_linnik2_barrier_router",
        "status": "localized_pcrt_transfer_reduced_to_pointwise_linnik2_ap_or_structural_frontier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "localized_pcrt_transfer_active": rows[0]["closed"],
        "column_occupancy_equivalent_to_least_prime_ap": True,
        "linnik2_barrier_identified": True,
        "complete_crt_uniformity_only_average": True,
        "localized_transfer_current_corpus_proved": False,
        "pointwise_linnik2_ap_theorem_proved": False,
        "atomic_signed_payload_constructor_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": L2_AP,
        "structural_fallback_target": f"{PDEC_SCOPE_ATOM}_OR_{SIGNED_PAYLOAD_ATOM}",
        "latest_strict_activity_basis": latest_basis,
        "equivalence_chain": equivalence_chain(),
        "sample_ap_barrier": sample,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`LocalizedPCRTColumnUniformityTransferToInitialPxPSquare` 的列侧内容已经压成精确的点态 AP 屏障："
            "对每个非零 `c mod P`，必须证明存在素数 `ell<=P^2` 且 `ell≡c mod P`。"
            "这正是 prime-modulus 的 Linnik 指数 2 型断言。完整 P-wheel 的 CRT 非 P 列均匀性只是全周期平均恒等式，"
            "不能提供每个初始短 AP 的首素数位置；BV/平均均匀性也只给几乎所有列。"
            "因此该路线若不引入新的点态 AP 定理，就必须回流到 PDEC same-set scope 或 signed payload/ExactUV 前沿。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix localized P-CRT transfer / Linnik=2 屏障路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"localized_pcrt_transfer_active={fmt_bool(result['localized_pcrt_transfer_active'])}",
        f"column_occupancy_equivalent_to_least_prime_ap={fmt_bool(result['column_occupancy_equivalent_to_least_prime_ap'])}",
        f"linnik2_barrier_identified={fmt_bool(result['linnik2_barrier_identified'])}",
        f"localized_transfer_current_corpus_proved={fmt_bool(result['localized_transfer_current_corpus_proved'])}",
        f"pointwise_linnik2_ap_theorem_proved={fmt_bool(result['pointwise_linnik2_ap_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 等价链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["equivalence_chain"]:
        lines.append(f"| `{table_cell(item['from'])}` | `{table_cell(item['to'])}` |")

    sample = result["sample_ap_barrier"]
    lines += [
        "",
        f"## 2. 有限 AP 样本（P <= {sample['max_p']}）",
        "",
        f"- 检查素数模数：`{sample['prime_moduli_checked']}`。",
        f"- 缺失剩余类总数：`{sample['missing_total']}`。",
        f"- 最大首素数行号：`{sample['worst_row_index_max']}`。",
        "",
        "| P | worst residue | first prime | row index | row/P | missing classes | mean first row |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in sample["top_records"]:
        lines.append(
            "| {P} | {worst_residue} | {worst_first_prime} | {worst_row_index} | {worst_row_fraction:.4f} | {missing_residue_count} | {mean_first_row_index:.3f} |".format(
                **item
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
        "审稿边界：本文件没有证明 Linnik=2 型点态 AP 定理，也没有证明 PDEC scope、signed payload、ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。",
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
    parser.add_argument("--max-p", type=int, default=3000, help="扫描最大 P，默认 3000")
    parser.add_argument("--top", type=int, default=12, help="输出最坏样本数，默认 12")
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
                "next_direct_attack_target": result["next_direct_attack_target"],
                "missing_total": result["sample_ap_barrier"]["missing_total"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
