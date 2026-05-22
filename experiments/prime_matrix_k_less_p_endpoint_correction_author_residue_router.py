#!/usr/bin/env python3
"""生成 1<k<P 端点差修正与作者侧剩余清单证书。

用法示例：
  python3 experiments/prime_matrix_k_less_p_endpoint_correction_author_residue_router.py
  python3 -m json.tool docs/monograph/prime-matrix-k-less-p-endpoint-correction-author-residue-router.json

输出：
  data/prime-matrix-k-less-p-endpoint-correction-author-residue-ledger.json
  docs/monograph/prime-matrix-k-less-p-endpoint-correction-author-residue-router.json
  docs/monograph/prime-matrix-k-less-p-endpoint-correction-author-residue-router.md
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
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SLUG = "prime-matrix-k-less-p-endpoint-correction-author-residue"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ENDPOINT_DIFF = DOCS / "prime-matrix-phi-lpf-endpoint-interval-difference-router.json"
K_LESS_P = DOCS / "prime-matrix-phi-lpf-k-less-p-row-interval-difference-router.json"
DUAL_CLOSURE = DOCS / "prime-matrix-dual-closure-external-internal-hardpoint-router.json"
FINAL_GUARD = DOCS / "prime-matrix-final-guard-gate-completion-verdict-router.json"
AUTHOR_COMPLETION = DOCS / "prime-matrix-author-side-closure-task-completion-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"

MAX_SWEEP_PRIME = 2003

FINE_SIGNED_SOURCE_PACKAGE = (
    "AlphaRowAnchorPhaseEmissionFormulaLedger AND "
    "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND "
    "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND "
    "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND "
    "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND "
    "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND "
    "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger AND "
    "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND "
    "FixedKeyExactUVLocalMultiplicityO1Ledger"
)


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失文件只会登记为空证据。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


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


def prime_prefix_upto(n: int) -> list[int]:
    """生成素数计数前缀表 pi(x)。"""
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    prefix = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if sieve[i]:
            count += 1
        prefix[i] = count
    return prefix


def count_primes(prefix: list[int], a: int, b: int) -> int:
    """用前缀表计算闭区间 [a,b] 的素数个数。"""
    if b < a:
        return 0
    left = prefix[a - 1] if a > 0 else 0
    return prefix[b] - left


def finite_sweep(max_prime: int = MAX_SWEEP_PRIME) -> dict[str, Any]:
    """有限审计 1<k<P 行内是否出现零素数行。"""
    primes = primes_upto(max_prime)
    prefix = prime_prefix_upto(max_prime * max_prime)
    case_count = 0
    zero_rows: list[dict[str, Any]] = []
    min_count: int | None = None
    min_rows: list[dict[str, Any]] = []
    distribution: dict[int, int] = {}
    for p_len in primes:
        if p_len <= 2:
            continue
        for k in range(2, p_len):
            a = k * p_len + 1
            b = k * p_len + p_len - 1
            prime_count = count_primes(prefix, a, b)
            case_count += 1
            distribution[prime_count] = distribution.get(prime_count, 0) + 1
            if prime_count == 0:
                zero_rows.append({"P": p_len, "k": k, "interval": [a, b]})
            if min_count is None or prime_count < min_count:
                min_count = prime_count
                min_rows = [{"P": p_len, "k": k, "interval": [a, b], "prime_count": prime_count}]
            elif prime_count == min_count and len(min_rows) < 20:
                min_rows.append({"P": p_len, "k": k, "interval": [a, b], "prime_count": prime_count})
    return {
        "max_prime": max_prime,
        "case_count": case_count,
        "all_rows_positive": not zero_rows,
        "zero_row_count": len(zero_rows),
        "zero_rows_sample": zero_rows[:20],
        "minimum_prime_count": min_count,
        "minimum_rows_sample": min_rows,
        "prime_count_distribution_low": {str(k): distribution[k] for k in sorted(distribution)[:10]},
        "finite_evidence_not_used_as_global_proof": True,
    }


def row(
    gate: str,
    closed: bool,
    proved_or_accepted: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved_or_accepted": proved_or_accepted,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出依赖文件。"""
    return [
        ENDPOINT_DIFF,
        K_LESS_P,
        DUAL_CLOSURE,
        FINAL_GUARD,
        AUTHOR_COMPLETION,
        DSTRUCTURE,
        CLAIM_STATUS,
        CONTRACTS,
        FRONTIER,
        EXTERNAL_INDEX,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(data: dict[str, dict[str, Any]], sweep: dict[str, Any]) -> list[dict[str, Any]]:
    """生成严格判定行。"""
    endpoint = data["endpoint"]
    k_less_p = data["k_less_p"]
    final_guard = data["final_guard"]
    dstructure = data["dstructure"]
    crt_sample = endpoint.get("crt_prime_free_block_sample", {})
    return [
        row(
            "PreviousCRTPrimeFreeSampleOutOfStrictDomain",
            bool(crt_sample) and not (1 < crt_sample.get("k", 0) < crt_sample.get("P", 0)),
            True,
            "上一层 P=5,k=8166 的 CRT 全合数样本满足 k>P，不能用于否定 1<k<P 行区间目标。",
            "use only as unrestricted-interval warning",
        ),
        row(
            "KLessPEndpointDifferenceImported",
            k_less_p.get("status") == "k_less_p_phi_lpf_row_interval_difference_closed_but_row_positivity_open",
            True,
            "1<k<P 专门证书已经给出闭区间与内部行的 Phi-LPF 端点差公式。",
            "exact count, not positivity",
        ),
        row(
            "ClosedIntervalEqualsInternalRow",
            True,
            True,
            "1<k<P 时 kP 与 (k+1)P 都是合数端点，闭区间素数数目等于内部行素数数目。",
            "endpoints contribute zero primes",
        ),
        row(
            "InsidePSquareUncoveredIffPrime",
            True,
            True,
            "对 1<=a<P，有 kP+a<P^2；若无根内素因子则不能为合数，只能为素数。",
            "uncovered slot positivity is exactly row-prime positivity",
        ),
        row(
            "FiniteStrictKSweepPositive",
            sweep["all_rows_positive"],
            True,
            f"有限审计到 P<={sweep['max_prime']} 未发现 1<k<P 零素数行。",
            "finite evidence only",
        ),
        row(
            "StrictKPositivityFromPhiLPFIdentityAlone",
            False,
            False,
            "Phi-LPF 端点差给精确值；正性仍需证明合数桶增量和 < P-1。",
            "noncircular positive input",
        ),
        row(
            "StrictKGlobalClosureFromCurrentCorpus",
            False,
            False,
            "当前材料没有从端点差恒等式推出所有 1<k<P 行内正性。",
            "FullS/KLS, signed-source, or special square-phase structural lower bound",
        ),
        row(
            "ExternalLemmaAuthorSideTasksDone",
            final_guard.get("author_side_completable_tasks_done") is True,
            final_guard.get("author_side_completable_tasks_done") is True,
            "外部 KLS 合同版中，作者侧可合法完成的条件链和证据包已封装。",
            "non-author independent acceptance remains",
        ),
        row(
            "DStructureRankinIndependentAcceptanceStillAbsent",
            dstructure.get("promotion_package_boundary_closed") is True,
            dstructure.get("promotion_package_independently_accepted") is True,
            "DStructure/Tail-log4/finite Rankin 晋级包边界闭合，但当前没有独立接受事件。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "SelfContainedReplacementTasksStillOpen",
            True,
            False,
            "若要求内部自足闭合，仍需 signed-source 细包和自足晋级证明包。",
            "FineSignedSourcePackage AND SelfContainedDStructureTailLog4FiniteRankinProofPackage",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "endpoint": read_json(ENDPOINT_DIFF),
        "k_less_p": read_json(K_LESS_P),
        "dual_closure": read_json(DUAL_CLOSURE),
        "final_guard": read_json(FINAL_GUARD),
        "author_completion": read_json(AUTHOR_COMPLETION),
        "dstructure": read_json(DSTRUCTURE),
    }
    sweep = finite_sweep()
    endpoint = data["endpoint"]
    crt_sample = endpoint.get("crt_prime_free_block_sample", {})
    rows = build_rows(data, sweep)
    return {
        "certificate_type": "prime_matrix_k_less_p_endpoint_correction_author_residue_router",
        "status": "k_less_p_endpoint_correction_closed_author_residue_pinned",
        "strict_domain": "P prime and 1<k<P",
        "previous_crt_sample": {
            "P": crt_sample.get("P"),
            "k": crt_sample.get("k"),
            "interval": crt_sample.get("interval"),
            "in_strict_domain_1_lt_k_lt_P": bool(
                crt_sample and 1 < crt_sample.get("k", 0) < crt_sample.get("P", 0)
            ),
        },
        "strict_k_formula_status": "exact_count_closed_positivity_open",
        "strict_k_positive_iff": (
            "sum_{p<=sqrt(kP+P-1)} DeltaPhi_p < P-1 iff a full-root uncovered "
            "slot exists iff the row contains a prime"
        ),
        "finite_sweep": sweep,
        "external_lemma_author_side_remaining": [],
        "external_lemma_non_author_remaining": [
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ],
        "no_blackbox_external_author_remaining": [
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof"
        ],
        "internal_self_contained_author_remaining": [
            FINE_SIGNED_SOURCE_PACKAGE,
            "SelfContainedDStructureTailLog4FiniteRankinProofPackage",
        ],
        "row_column_unconditional_closed": False,
        "rows": rows,
        "plain_conclusion": (
            "对 1<k<P 的 restricted row，上一层 P=5,k=8166 的 CRT 全合数样本确实越界，"
            "不能作为该目标的反例或阻断证据。restricted 端点差公式已经严格落地，并且闭区间计数等于内部行计数。"
            "但 Phi-LPF 恒等式仍只给 exact count；要证明正性，必须证明合数桶端点增量和小于 P-1，"
            "这在 k<P 行内等价于存在 full-root 未覆盖槽，也就是等价于行内有素数。"
            "因此此前判断需要修正为：CRT 样例只阻断 unrestricted 断言；restricted 目标仍开放，"
            "不能由 Phi-LPF 恒等式单独非循环闭合。外部引理版作者侧证据包已封装，剩余是非作者侧独立接受；"
            "内部自足版仍需 signed-source 细包与自足 DStructure/Rankin 替代包。"
        ),
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 Markdown 判定表。"""
    lines = [
        "| gate | closed | proved/accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    sweep = payload["finite_sweep"]
    lines = [
        "# Prime Matrix 1<k<P 端点差修正与作者侧剩余清单",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 修正结论",
        "",
        "```text",
        f"previous_crt_sample_in_strict_domain={fmt_bool(payload['previous_crt_sample']['in_strict_domain_1_lt_k_lt_P'])}",
        f"strict_k_formula_status={payload['strict_k_formula_status']}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        payload["plain_conclusion"],
        "",
        "## 2. 1<k<P 精确公式",
        "",
        "```text",
        "pi(kP+P)-pi(kP-1) = pi(kP+P-1)-pi(kP)",
        "                 = (P-1) - sum_{p<=sqrt(kP+P-1)} DeltaPhi_p",
        "```",
        "",
        "正性等价于：",
        "",
        "```text",
        payload["strict_k_positive_iff"],
        "```",
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 4. 有限审计",
        "",
        "```text",
        f"max_prime={sweep['max_prime']}",
        f"case_count={sweep['case_count']}",
        f"all_rows_positive={fmt_bool(sweep['all_rows_positive'])}",
        f"minimum_prime_count={sweep['minimum_prime_count']}",
        "finite_evidence_not_used_as_global_proof=true",
        "```",
        "",
        "| P | k | interval | prime count |",
        "| ---: | ---: | --- | ---: |",
    ]
    for item in sweep["minimum_rows_sample"][:12]:
        lines.append(
            f"| {item['P']} | {item['k']} | {item['interval']} | {item['prime_count']} |"
        )
    lines.extend(
        [
            "",
            "## 5. 作者侧剩余",
            "",
            "外部引理版作者侧普通剩余：",
            "",
            "```text",
            "none; author-side dossier sealed",
            "```",
            "",
            "外部引理版非作者侧剩余：",
            "",
            "```text",
            *payload["external_lemma_non_author_remaining"],
            "```",
            "",
            "无黑箱外部版作者侧剩余：",
            "",
            "```text",
            *payload["no_blackbox_external_author_remaining"],
            "```",
            "",
            "内部自足版作者侧剩余：",
            "",
            "```text",
            *payload["internal_self_contained_author_remaining"],
            "```",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
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


if __name__ == "__main__":
    main()
