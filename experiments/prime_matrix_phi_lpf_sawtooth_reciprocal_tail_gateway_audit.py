#!/usr/bin/env python3
"""审计 Phi-LPF sawtooth reciprocal tail 的最快可推进子门。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_sawtooth_reciprocal_tail_gateway_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-sawtooth-reciprocal-tail-gateway-audit.json

本层接在 Kloosterman gateway 之后，专攻三原子门中最容易真推进的
`SawtoothTailLogSavingForThinReciprocalFibres`。结论分两层：

1. 无权端点倒数相位可由经典二阶导数估计给出幂节省基准；
2. 真正的 Phi-LPF 对象仍带有 prime-q 与 LPF-shell 权重，不能由无权估计
   或现有 Kloosterman/smooth-number 外部定理直接闭合。
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-sawtooth-reciprocal-tail-gateway"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

GATEWAY_JSON = DOCS / "prime-matrix-phi-lpf-reciprocal-graph-kloosterman-gateway-audit.json"
LPF_TYPEII_JSON = DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json"

DEPENDENCIES = [
    GATEWAY_JSON,
    LPF_TYPEII_JSON,
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bool_text(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空记录。"""
    if not path.exists():
        return {"available": False}
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["available"] = True
    return payload


def prime_flags(n: int) -> list[bool]:
    """返回素数布尔表。"""
    flags = [False, False] + [True] * max(0, n - 1)
    for p in range(2, int(n**0.5) + 1):
        if flags[p]:
            step = p
            start = p * p
            flags[start : n + 1 : step] = [False] * (((n - start) // step) + 1)
    return flags


def primes_upto(n: int) -> list[int]:
    """列出不超过 n 的素数。"""
    flags = prime_flags(n)
    return [i for i, flag in enumerate(flags) if flag]


def high_q_primes(P: int) -> list[int]:
    """列出 P/2<q<P 的素数。"""
    return [q for q in primes_upto(P - 1) if P / 2 < q < P]


def reciprocal_phase_sum(P: int, k: int, h: int) -> complex:
    """计算无权高 q 素数倒数相位和。"""
    return sum(cmath.exp(2j * math.pi * h * k * P / q) for q in high_q_primes(P))


def vdc_surrogate_bound(P: int, k: int, h: int) -> float:
    """二阶导数估计的行尺度代理量。

    对 f(x)=A/x、A=h*k*P、x≈P，经典二阶导数估计给出
    sum e(f(n)) << sqrt(A/P)+sqrt(P^3/A)。这里不追踪绝对常数。
    """
    hk = h * k
    return math.sqrt(hk) + P / math.sqrt(hk)


def benchmark_rows() -> list[dict[str, Any]]:
    """生成无权倒数相位的有限样本读数；只作诊断，不作证明。"""
    samples: list[tuple[int, int]] = []
    for P in [101, 257, 509, 1009]:
        samples.extend(
            [
                (P, max(2, P // 2)),
                (P, max(2, P - P // 21)),
                (P, P - 1),
            ]
        )

    rows: list[dict[str, Any]] = []
    for P, k in samples:
        q_count = len(high_q_primes(P))
        best: dict[str, Any] | None = None
        for h in range(1, 9):
            actual = abs(reciprocal_phase_sum(P, k, h))
            record = {
                "h": h,
                "actual_abs_sum": round(actual, 6),
                "trivial_q_count": q_count,
                "actual_over_trivial": round(actual / q_count, 6) if q_count else None,
                "vdc_surrogate": round(vdc_surrogate_bound(P, k, h), 6),
            }
            if best is None or actual > best["actual_abs_sum"]:
                best = record
        rows.append({"P": P, "k": k, **(best or {})})
    return rows


def prior_metrics() -> dict[str, Any]:
    """抽取上一层证书的关键状态。"""
    gateway = load_json(GATEWAY_JSON)
    lpf = load_json(LPF_TYPEII_JSON)
    finite = lpf.get("finite_audit", {})
    return {
        "gateway_status": gateway.get("status"),
        "latest_narrowest_mouth": gateway.get("latest_narrowest_mouth"),
        "lpf_tail_status": lpf.get("status"),
        "finite_max_prime": finite.get("max_prime"),
        "finite_row_count": finite.get("row_count"),
        "finite_total_R30": finite.get("total_R30"),
        "thin_q_fiber": finite.get("all_q_m_windows_have_at_most_two_points"),
        "thin_reverse_fiber": finite.get("all_m_q_reverse_fibers_have_at_most_two_points"),
        "one_point_qr_fiber": finite.get("all_qr_a_fibers_have_at_most_one_point"),
    }


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造门控记录。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def table(rows: list[dict[str, Any]], fields: list[str]) -> str:
    """生成 Markdown 表格。"""
    header = "| " + " | ".join(fields) + " |"
    sep = "| " + " | ".join("---" for _ in fields) + " |"
    body = []
    for row in rows:
        cells = []
        for field in fields:
            value = row.get(field, "")
            if isinstance(value, bool):
                value = bool_text(value)
            cells.append(str(value).replace("|", r"\|"))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, sep, *body])


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    gates = [
        gate(
            "DeterministicSawtoothEndpointIdentity",
            True,
            True,
            "floor endpoint 产生 psi(kP/u) 与有限 Fourier 相位 e(h*kP/u)。",
            "identity closed; cancellation not included",
        ),
        gate(
            "VaalerTruncationTailWithThinTotalWeight",
            True,
            True,
            "若总权重为 O(P)，取 H=(log P)^B 时，截断尾项为 O(P/(log P)^B)。",
            "tail bookkeeping closed after choosing B",
        ),
        gate(
            "ActiveHighQRowsHavePScaleK",
            True,
            True,
            "若 high-q reciprocal window 非空，则 q,m>P/2 迫使 qm>P^2/4，从而 k+1>P/4。",
            "active sawtooth rows are P-scale",
        ),
        gate(
            "UnweightedReciprocalPhaseVanDerCorputBenchmark",
            True,
            True,
            "对 sum_{n≈P} e(h*kP/n)，二阶导数估计给 O(sqrt(hk)+P/sqrt(hk))；active rows 与 h≤log^B P 时给幂节省。",
            "only an unweighted interval benchmark",
        ),
        gate(
            "PrimeQLPFShellWeightedReciprocalPhaseSaving",
            False,
            False,
            "真实对象是 prime q 与 LPF-shell/rough cofactor 权重，不是无权连续区间。",
            "need weighted reciprocal phase saving uniformly in P,k,h",
        ),
        gate(
            "SawtoothTailLogSavingForThinReciprocalFibres",
            False,
            False,
            "无权 benchmark 已闭合，但带权 finite-h 相位和仍未闭合。",
            "PrimeQLPFShellWeightedReciprocalPhaseSaving",
        ),
    ]
    return {
        "certificate_type": "prime_matrix_phi_lpf_sawtooth_reciprocal_tail_gateway_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "sawtooth_reciprocal_tail_split_unweighted_closed_weighted_open",
        "selected_fastest_gate": "SawtoothTailLogSavingForThinReciprocalFibres",
        "prior_metrics": prior_metrics(),
        "analytic_benchmark": {
            "phase": "e(h*k*P/u)",
            "model_sum": "S(A;N)=sum_{N<n<=2N} e(A/n), A=h*k*P, N=P",
            "classical_second_derivative_bound": "S(A;N) << sqrt(A/N)+sqrt(N^3/A)",
            "row_scale_substitution": "S << sqrt(h*k)+P/sqrt(h*k)",
            "active_row_comparability": "if the high-q reciprocal graph is nonempty, then q,m>P/2 forces k+1>P/4, so k is P-scale away from finitely many edge rows",
            "active_row_polylog_h_consequence": "for active rows and h<=H=(log P)^B, finite unweighted sawtooth modes contribute O(P^(1/2)H^(1/2)) and truncation tail O(P/H)",
            "unweighted_log_saving_conclusion": "unweighted endpoint benchmark gives arbitrary log saving versus P for sufficiently large P",
        },
        "finite_unweighted_prime_q_benchmark": {
            "rows": benchmark_rows(),
            "sample_evidence_not_global_proof": True,
            "weights_omitted": "LPF shell and rough cofactor weights are intentionally omitted in this diagnostic benchmark",
        },
        "external_theorem_match_table": [
            {
                "source": "classical van der Corput/Kusmin-Landau second derivative estimate",
                "useful_part": "handles the unweighted real reciprocal phase e(A/u)",
                "matched_to_unweighted_benchmark": True,
                "matched_to_phi_lpf_weighted_object": False,
                "remaining": "PrimeQLPFShellWeightedReciprocalPhaseSaving",
            },
            {
                "source": "Duke-Friedlander-Iwaniec 1997",
                "useful_part": "bilinear Kloosterman fractions after inverse-modulus completion",
                "matched_to_unweighted_benchmark": False,
                "matched_to_phi_lpf_weighted_object": False,
                "remaining": "ReciprocalGraphToKloostermanCompletionIdentity",
            },
            {
                "source": "Bettin-Chandee 2015/2018 and Wright 2026",
                "useful_part": "trilinear Kloosterman fractions and partially fixed-moduli dispersion",
                "matched_to_unweighted_benchmark": False,
                "matched_to_phi_lpf_weighted_object": False,
                "remaining": "CompletedKloostermanMeanForPrimeQAndLPFShellWeights",
            },
            {
                "source": "Shao-Shparlinski-Wijaya 2025/2026, sums of Kloosterman sums over square-free and smooth integers",
                "useful_part": "power savings for finite-field Kloosterman sums with square-free or smooth parameters",
                "matched_to_unweighted_benchmark": False,
                "matched_to_phi_lpf_weighted_object": False,
                "remaining": "finite-field Kloosterman completion plus prime-q/LPF-shell transfer",
            },
        ],
        "new_narrowest_sawtooth_mouth": [
            "PrimeQLPFShellWeightedReciprocalPhaseSaving",
            "AND WeightExtractionFromLPFShellToBilinearKloostermanOrVaughanTypeII",
            "AND UniformFiniteHTruncationWithHPolylog",
        ],
        "gates": gates,
        "unweighted_sawtooth_benchmark_closed": True,
        "weighted_sawtooth_phi_lpf_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    analytic = payload["analytic_benchmark"]
    finite = payload["finite_unweighted_prime_q_benchmark"]
    lines = [
        "# Prime Matrix Phi-LPF sawtooth reciprocal tail gateway 审计",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 选择最快子门",
        "",
        "三原子门中，本轮选择先攻：",
        "",
        "```text",
        payload["selected_fastest_gate"],
        "```",
        "",
        "原因是 endpoint floor/sawtooth 已给出明确倒数相位，至少无权模型可以用经典二阶导数估计推进。",
        "",
        "## 2. 无权解析基准",
        "",
        "```text",
        f"phase={analytic['phase']}",
        f"model_sum={analytic['model_sum']}",
        f"classical_second_derivative_bound={analytic['classical_second_derivative_bound']}",
        f"row_scale_substitution={analytic['row_scale_substitution']}",
        f"active_row_comparability={analytic['active_row_comparability']}",
        f"active_row_polylog_h_consequence={analytic['active_row_polylog_h_consequence']}",
        f"unweighted_log_saving_conclusion={analytic['unweighted_log_saving_conclusion']}",
        "```",
        "",
        "这是真推进：`SawtoothTailLogSavingForThinReciprocalFibres` 中的无权倒数相位障碍已经不是主硬点。",
        "但它还不是 Phi-LPF 闭合，因为真实权重来自 prime `q`、`r=LPF(m)` 与 `r`-rough quotient。",
        "",
        "## 3. 有限无权 prime-q 诊断",
        "",
        table(
            finite["rows"],
            ["P", "k", "h", "actual_abs_sum", "trivial_q_count", "actual_over_trivial", "vdc_surrogate"],
        ),
        "",
        "该表只说明实际无权高 `q` 素数相位并不呈现结构性灾难；它不替代全局证明，也没有包含 LPF 权重。",
        "",
        "## 4. 外部定理匹配",
        "",
        table(
            payload["external_theorem_match_table"],
            [
                "source",
                "useful_part",
                "matched_to_unweighted_benchmark",
                "matched_to_phi_lpf_weighted_object",
                "remaining",
            ],
        ),
        "",
        "Shao--Shparlinski--Wijaya 的 square-free/smooth Kloosterman sum 结果是有用的新外部参考，",
        "但它工作在固定有限域 Kloosterman sum参数上；本文当前 sawtooth 相位仍是实倒数相位 `e(A/q)`，",
        "并且还带有逐行 LPF-shell 权重。因此它不能直接关闭本门。",
        "",
        "## 5. 新门控表",
        "",
        table(payload["gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 6. 最新最窄口",
        "",
        "```text",
        *payload["new_narrowest_sawtooth_mouth"],
        "```",
        "",
        "状态边界：",
        "",
        "```text",
        f"unweighted_sawtooth_benchmark_closed={bool_text(payload['unweighted_sawtooth_benchmark_closed'])}",
        f"weighted_sawtooth_phi_lpf_closed={bool_text(payload['weighted_sawtooth_phi_lpf_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={bool_text(payload['phi_lpf_parity_barrier_globally_broken'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
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
    print("unweighted_sawtooth_benchmark_closed=true")
    print("weighted_sawtooth_phi_lpf_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
