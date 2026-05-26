#!/usr/bin/env python3
"""把 terminal monotone-run payload 路由到 trace/Type-II 可接入合同。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_run_trace_admissibility_contract_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json

输出：
  data/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-ledger.json
  docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.json
  docs/monograph/prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-run-trace-admissibility-contract"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

TERMINAL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-monotone-run-total-to-net-compression-frontier-router.json"
CORRECTED_JSON = DOCS / "prime-matrix-phi-lpf-corrected-lpf-signed-trace-breakthrough-router.json"

SOURCE_FILES = [
    Path(__file__).resolve(),
    TERMINAL_JSON,
    CORRECTED_JSON,
    DOCS / "prime-matrix-phi-lpf-edge-local-signed-atom-trace-sync-router.json",
    DOCS / "prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json",
    DOCS / "prime-matrix-phi-lpf-lpf-tail-typeii-obligation-audit.json",
    DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
    DOCS / "three-claims-actual-load-closure-contracts.md",
    DOCS / "external-theorem-index.md",
]

LATEST_OPEN_GATE = (
    "TerminalRunTraceAdmissibilityContractPinned "
    "AND FiniteSignedRunLedgerIsNotYetUniformTraceFamily "
    "AND NeedTraceKernelOrTypeIICoefficientFormulaOrNamedPDECSAE "
    "AND UniformAdjacentRunCancellationStillOpen"
)


EXTERNAL_TRACE_ACCEPTANCE = [
    {
        "input": "Fouvry-Kowalski-Michel-Sawin trace-family technology",
        "url": "https://arxiv.org/abs/2511.09459",
        "requires": "ell-adic/trace-function family with monodromy and conductor data",
        "current_status": "finite terminal run ledger only",
        "admissible_now": False,
    },
    {
        "input": "Milicevic-Qin-Wu bilinear Kloosterman sums",
        "url": "https://arxiv.org/abs/2511.07550",
        "requires": "genuine two-variable Kloosterman family over moving q/m variables",
        "current_status": "q-windows and signed deltas exist, but no Kloosterman kernel formula",
        "admissible_now": False,
    },
    {
        "input": "Pascadi composite-modulus Type-II input",
        "url": "https://arxiv.org/abs/2511.08445",
        "requires": "well-factorable signed coefficients and composite-modulus Type-II ranges",
        "current_status": "LPF/terminal coefficients are finite payload weights, not Type-II coefficients",
        "admissible_now": False,
    },
    {
        "input": "Wright trilinear Kloosterman fractions",
        "url": "https://arxiv.org/abs/2604.25177",
        "requires": "trilinear convolution with equidistributed beta sequence",
        "current_status": "terminal payload has q-runs and atom keys, but no trilinear beta family",
        "admissible_now": False,
    },
    {
        "input": "Runbo Li large-modulus AP/Harman sieve",
        "url": "https://arxiv.org/abs/2602.20917",
        "requires": "admissible averaged AP family in the same singular-series convention",
        "current_status": "row-column target remains pointwise at P^2 scale",
        "admissible_now": False,
    },
]


TRACE_CONTRACT_ROWS = [
    {
        "contract": "TerminalRunKernelFormula",
        "needed_statement": "give a forward formula K_P(q,m,atom) whose signed value equals the terminal run payload",
        "current_evidence": "finite signed_delta and q-interval rows exist",
        "proved": False,
        "failure_return": "MissingTraceKernelFormulaPDEC",
    },
    {
        "contract": "SameTraceKeySourceConsistency",
        "needed_statement": "source row, orientation, local factor, ExactUV pair and signed value share one pre-Cauchy trace key",
        "current_evidence": "same-key requirement is named in previous trace-sync routers",
        "proved": False,
        "failure_return": "SameTraceKeySplitPDEC",
    },
    {
        "contract": "UniformFamilyInP",
        "needed_statement": "finite terminal packets extend to a uniform family for all large P and all relevant rows",
        "current_evidence": "current ledger has finitely many atoms and runs",
        "proved": False,
        "failure_return": "FiniteLedgerOnlyLocalSurvivor",
    },
    {
        "contract": "TypeIICoefficientFactorability",
        "needed_statement": "signed weights become well-factorable coefficients with nontrivial bilinear/trilinear ranges",
        "current_evidence": "LPF tail Type-II obligation identified reciprocal graph thinness",
        "proved": False,
        "failure_return": "TypeIIFactorabilityFailureSAE",
    },
    {
        "contract": "ConductorOrModulusControl",
        "needed_statement": "trace/Kloosterman conductor or AP modulus stays in the required external-theorem range",
        "current_evidence": "q-windows are recorded in finite rows",
        "proved": False,
        "failure_return": "ConductorRangePDEC",
    },
    {
        "contract": "UniformAdjacentRunCancellation",
        "needed_statement": "extra total variation compresses to atom-local survivor uniformly, not just in finite ledger",
        "current_evidence": "finite cancellation decomposition and selected surplus are closed",
        "proved": False,
        "failure_return": "AdjacentRunCancellationFailureLocalSurvivor",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def compact_fraction(item: dict[str, Any] | None) -> str:
    """压缩已有 fraction/decimal 字段。"""
    if not item:
        return "n/a"
    frac = item.get("fraction")
    dec = item.get("decimal")
    if frac and dec:
        return f"{dec} ({frac})"
    return str(frac or dec or item)


def terminal_summary(terminal: dict[str, Any]) -> dict[str, Any]:
    """从 terminal run 证书抽取本层需要的最小摘要。"""
    metrics = terminal.get("absorption_metrics", {})
    role_rows = terminal.get("role_summary_rows", [])
    atom_rows = terminal.get("atom_cancellation_rows", [])
    largest_rows = terminal.get("largest_run_rows", [])

    roles = {row.get("role"): row for row in role_rows}
    atom_keys = sorted({row.get("atom_key") for row in atom_rows if row.get("atom_key")})
    q_windows = sorted({row.get("q_interval") for row in largest_rows if row.get("q_interval")})

    return {
        "terminal_run_count_total": terminal.get("terminal_run_count_total"),
        "selected_terminal_run_count": terminal.get("selected_terminal_run_count"),
        "extra_shell_run_count": terminal.get("extra_shell_run_count"),
        "atom_count": len(atom_keys),
        "atom_keys": atom_keys,
        "largest_run_count_sample": len(largest_rows),
        "q_window_sample_count": len(q_windows),
        "q_windows_sample": q_windows[:12],
        "strict_run_local_compression_count": terminal.get("strict_run_local_compression_count"),
        "run_local_compression_ratio_min": terminal.get("run_local_compression_ratio_min"),
        "run_local_compression_ratio_max": terminal.get("run_local_compression_ratio_max"),
        "selected_negative_excess": compact_fraction(metrics.get("selected_negative_excess")),
        "extra_total_variation": compact_fraction(metrics.get("extra_total_variation")),
        "extra_atom_local_survivor_total": compact_fraction(metrics.get("extra_atom_local_survivor_total")),
        "selected_negative_excess_minus_extra_atom_survivor": compact_fraction(
            metrics.get("selected_negative_excess_minus_extra_atom_survivor")
        ),
        "selected_negative_excess_beats_extra_atom_survivor": bool(
            metrics.get("selected_negative_excess_beats_extra_atom_survivor")
        ),
        "finite_absorption_would_close_after_uniform_cancellation_law": bool(
            metrics.get("finite_absorption_would_close_after_uniform_cancellation_law")
        ),
        "role_summary": {
            name: {
                "run_count": row.get("run_count"),
                "transition_count": row.get("transition_count"),
                "signed_net": compact_fraction(row.get("signed_net")),
                "total_variation": compact_fraction(row.get("total_variation")),
                "aggregate_total_to_net_ratio": compact_fraction(row.get("aggregate_total_to_net_ratio")),
            }
            for name, row in roles.items()
        },
    }


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    terminal = load_json(TERMINAL_JSON)
    corrected = load_json(CORRECTED_JSON)
    summary = terminal_summary(terminal)
    all_contracts_proved = all(row["proved"] for row in TRACE_CONTRACT_ROWS)

    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_run_trace_admissibility_contract_router",
        "status": "terminal_run_trace_admissibility_contract_pinned_family_open",
        "verified_date": "2026-05-26",
        "imported_terminal_status": terminal.get("status"),
        "imported_corrected_lpf_status": corrected.get("status"),
        "terminal_finite_signed_run_ledger_closed": bool(terminal.get("terminal_monotone_run_ledger_closed")),
        "finite_adjacent_cancellation_decomposition_closed": bool(
            terminal.get("atom_adjacent_cancellation_decomposition_closed")
        ),
        "finite_absorption_would_close_after_uniform_cancellation_law": summary[
            "finite_absorption_would_close_after_uniform_cancellation_law"
        ],
        "selected_negative_excess_beats_extra_atom_survivor": summary[
            "selected_negative_excess_beats_extra_atom_survivor"
        ],
        "trace_or_typeii_family_admissible_now": False,
        "all_trace_contracts_proved": all_contracts_proved,
        "external_theorems_directly_attach_now": False,
        "named_return_matrix_required_if_contract_fails": True,
        "row_column_unconditional_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "terminal_summary": summary,
        "trace_admissibility_contract": TRACE_CONTRACT_ROWS,
        "external_trace_acceptance": EXTERNAL_TRACE_ACCEPTANCE,
        "latest_open_gate": LATEST_OPEN_GATE,
        "plain_conclusion": (
            "The finite terminal monotone-run ledger already has signed mass, run decomposition, "
            "and a finite selected surplus.  It is still not an admissible trace/Type-II family: "
            "there is no forward terminal kernel formula K_P(q,m,atom), no uniform family in P, "
            "no well-factorable coefficient theorem, and no conductor/modulus control.  Hence "
            "external trace/Kloosterman/Type-II inputs can attach only after this contract is "
            "proved, or the failure must be returned as a named PDEC/SAE/LocalSurvivor."
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    summary = payload["terminal_summary"]
    lines = [
        "# Prime Matrix Phi-LPF terminal-run trace-admissibility contract 路由",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "## 1. 总裁定",
        "",
        "```text",
        f"terminal_finite_signed_run_ledger_closed={fmt_bool(payload['terminal_finite_signed_run_ledger_closed'])}",
        "finite_adjacent_cancellation_decomposition_closed="
        f"{fmt_bool(payload['finite_adjacent_cancellation_decomposition_closed'])}",
        "finite_absorption_would_close_after_uniform_cancellation_law="
        f"{fmt_bool(payload['finite_absorption_would_close_after_uniform_cancellation_law'])}",
        "selected_negative_excess_beats_extra_atom_survivor="
        f"{fmt_bool(payload['selected_negative_excess_beats_extra_atom_survivor'])}",
        f"trace_or_typeii_family_admissible_now={fmt_bool(payload['trace_or_typeii_family_admissible_now'])}",
        f"external_theorems_directly_attach_now={fmt_bool(payload['external_theorems_directly_attach_now'])}",
        f"all_trace_contracts_proved={fmt_bool(payload['all_trace_contracts_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. terminal run 摘要",
        "",
        "```text",
        f"terminal_run_count_total={summary['terminal_run_count_total']}",
        f"selected_terminal_run_count={summary['selected_terminal_run_count']}",
        f"extra_shell_run_count={summary['extra_shell_run_count']}",
        f"atom_count={summary['atom_count']}",
        f"strict_run_local_compression_count={summary['strict_run_local_compression_count']}",
        f"selected_negative_excess={summary['selected_negative_excess']}",
        f"extra_total_variation={summary['extra_total_variation']}",
        f"extra_atom_local_survivor_total={summary['extra_atom_local_survivor_total']}",
        "selected_negative_excess_minus_extra_atom_survivor="
        f"{summary['selected_negative_excess_minus_extra_atom_survivor']}",
        "```",
        "",
        "## 3. trace/Type-II 可接入合同",
        "",
        "| contract | needed statement | current evidence | proved | failure return |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in payload["trace_admissibility_contract"]:
        lines.append(
            "| {contract} | {needed} | {evidence} | {proved} | {ret} |".format(
                contract=row["contract"],
                needed=row["needed_statement"],
                evidence=row["current_evidence"],
                proved=fmt_bool(row["proved"]),
                ret=row["failure_return"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 外部定理接入验收",
            "",
            "| input | requires | current status | admissible now | url |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["external_trace_acceptance"]:
        lines.append(
            "| {inp} | {req} | {status} | {adm} | {url} |".format(
                inp=row["input"],
                req=row["requires"],
                status=row["current_status"],
                adm=fmt_bool(row["admissible_now"]),
                url=row["url"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in payload["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    text = json.dumps(payload, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")
    print(f"trace_or_typeii_family_admissible_now={fmt_bool(payload['trace_or_typeii_family_admissible_now'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
