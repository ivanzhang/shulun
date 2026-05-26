#!/usr/bin/env python3
"""生成行级 Delta-Phi 不等式破障公式前沿证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_row_inequality_breakthrough_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-row-inequality-breakthrough-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ROW_CONTRACT = DOCS / "prime-matrix-phi-lpf-row-delta-phi-cover-contract-router.json"
PRIME_CONTRACT = DOCS / "prime-matrix-phi-lpf-parity-barrier-prime-distribution-contract-router.json"
TRANSPORT_EDGE = DOCS / "prime-matrix-phi-lpf-parity-barrier-transport-edge-sync-router.json"
FIXED_WHEEL = DOCS / "prime-matrix-phi-lpf-fixed-wheel-residual-rough-composite-audit.json"
PUNCTURED_WHEEL30 = DOCS / "prime-matrix-phi-lpf-punctured-endpoint-wheel30-capacity-router.json"
EXTERNAL_STRESS = DOCS / "prime-matrix-external-frontier-theorem-stress-router.json"
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
    PRIME_CONTRACT,
    TRANSPORT_EDGE,
    FIXED_WHEEL,
    PUNCTURED_WHEEL30,
    EXTERNAL_STRESS,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]


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


def exponent_gap(theta: Fraction) -> dict[str, str]:
    """把短区间指数 theta 换算到 x=P^2 的行厚度。"""
    row_thickness = 2 * theta - 1
    return {
        "theta": f"{theta.numerator}/{theta.denominator}",
        "interval_length_at_x=P^2": f"P^({2 * theta})",
        "row_thickening_factor": f"P^({row_thickness})",
        "strict_row_closed": str(row_thickness <= 0).lower(),
    }


def formula_frontier_rows() -> list[dict[str, Any]]:
    """列出真正能破行级不等式的公式接口。"""
    return [
        {
            "priority": 1,
            "name": "UniformDeltaPhiCoverDefect",
            "formula": "sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1",
            "new_content_needed": "prove a uniform strict deficit in the LPF owner cover, not merely the exact prefix identity",
            "current_status": "open",
            "why_non_circular": "would directly pay the row survivor without naming prime distribution separately",
        },
        {
            "priority": 2,
            "name": "NamedLPFOwnerResiduePDEC",
            "formula": "Delta-Phi cover equality => forbidden LPF-owner residue/phase packet",
            "new_content_needed": "turn the equality case into a structured contradiction involving owner residues, cofactors, and phase keys",
            "current_status": "open",
            "why_non_circular": "does not need a full prime number theorem if full cover has impossible geometry",
        },
        {
            "priority": 3,
            "name": "PointwiseThetaPsiCOneInputAtSqrtRowScale",
            "formula": "theta(B)-theta(A)>0, or psi(B)-psi(A)>PrimePowerTail(A,B)",
            "new_content_needed": "zero-exception pointwise lower bound for H=sqrt(x) rows",
            "current_status": "open; stronger than current published/preprint short-interval inputs",
            "why_non_circular": "counts prime emission directly rather than rough survivors",
        },
        {
            "priority": 4,
            "name": "SourceKeyedMobiusVonMangoldtTraceTypeIIFamily",
            "formula": "Lambda/Mobius/Type-I-II decomposition with source-keyed error < row main term",
            "new_content_needed": "admissible signed coefficients before pushforward, conductor control, and Type-II cancellation at q,m~sqrt(x)",
            "current_status": "open",
            "why_non_circular": "breaks parity by signed divisor cancellation",
        },
        {
            "priority": 5,
            "name": "SpectralKloostermanTraceLift",
            "formula": "completed trace/Kloosterman family attached to q-spine/hinge source keys",
            "new_content_needed": "upgrade finite q-spine ledgers to a uniform trace family with stable source keys",
            "current_status": "open",
            "why_non_circular": "would replace support counting by oscillatory cancellation",
        },
        {
            "priority": 6,
            "name": "ExplicitFormulaBeyondRHAtH=sqrt(x)",
            "formula": "psi(x+H)-psi(x)=H+error with error < H-PrimePowerTail, H=sqrt(x)",
            "new_content_needed": "zero cancellation stronger than the standard RH-size error at the exact square-root scale",
            "current_status": "open",
            "why_non_circular": "direct analytic positivity route, but presently as hard as a Cramer-local input",
        },
    ]


def external_rows() -> list[dict[str, Any]]:
    """列出外部输入在当前行尺度上的精确缺口。"""
    return [
        {
            "input": "Guth--Maynard zero-density / short intervals",
            "source": "https://arxiv.org/abs/2405.20552",
            **exponent_gap(Fraction(17, 30)),
            "meaning": "at x=P^2 the interval has length P^(17/15), so it can cover about P^(2/15) rows, not one fixed row",
        },
        {
            "input": "Le Duc Hieu APs of primes in short intervals",
            "source": "https://arxiv.org/abs/2509.04883",
            **exponent_gap(Fraction(17, 30)),
            "meaning": "adds prime AP structure at the same theta>17/30 scale; structure does not shrink to one row",
        },
        {
            "input": "Runbo Li Harman-sieve short intervals",
            "source": "https://arxiv.org/abs/2308.04458",
            **exponent_gap(Fraction(13, 25)),
            "meaning": "at x=P^2 the interval length is P^(26/25), still P^(1/25) rows thick",
        },
    ]


def obstruction_rows() -> list[dict[str, str]]:
    """列出会导致循环或假突破的路线。"""
    return [
        {
            "route": "more wheel refinement",
            "failure": "fixed wheel margins become N(P,k)>R_S(P,k); at primorial limit this returns to row primality itself",
            "safe_use": "use wheels only to localize a PDEC equality case or to shrink residual composites",
        },
        {
            "route": "Euler product main term only",
            "failure": "floor/periodic boundary errors at row length P are the same scale as the target survivor",
            "safe_use": "must carry exact Legendre-Phi floors or prove a signed saving",
        },
        {
            "route": "generic short interval theorem with theta>1/2",
            "failure": "proves a prime after thickening the row by P^(2theta-1), leaving fixed rows unresolved",
            "safe_use": "can bound zero-row runs, but cannot close every row",
        },
        {
            "route": "support-only P2/rough count",
            "failure": "P2 and rough composites can saturate the same support classes as primes",
            "safe_use": "only as an owner/phase ledger feeding signed trace or PDEC",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    row_contract = load_json(ROW_CONTRACT)
    prime_contract = load_json(PRIME_CONTRACT)
    transport_edge = load_json(TRANSPORT_EDGE)

    frontier_synced = all(
        [
            row_contract.get("row_delta_phi_identity_closed") is True,
            row_contract.get("strict_cover_inequality_proved_uniformly") is False,
            prime_contract.get("unsigned_lpf_bucket_count_sufficient_for_prime_extraction") is False,
            transport_edge.get("transport_edge_sync_closed") is True,
        ]
    )

    return {
        "certificate_type": "prime_matrix_phi_lpf_row_inequality_breakthrough_frontier_router",
        "status": "row_delta_phi_breakthrough_formula_frontier_synced_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "row_delta_phi_contract_imported": row_contract.get("row_delta_phi_identity_closed") is True,
        "strict_cover_inequality_proved_uniformly": False,
        "breakthrough_formula_frontier_synced": frontier_synced,
        "row_column_unconditional_closed": False,
        "critical_scale": {
            "x": "P^2",
            "row_length": "P=x^(1/2)",
            "expected_prime_count": "P/(2 log P)",
            "needed_error_strength": "total Delta-Phi/signed-distribution error must be o(P/log P) or produce one explicit survivor/PDEC",
        },
        "minimum_new_theorem_statement": (
            "For every target Prime Matrix row (A,B], either "
            "sum_{p<=sqrt(B)}(C_p(B)-C_p(A)) <= B-A-1, "
            "or the equality/overcover case returns a named LPF-owner residue PDEC/SAE."
        ),
        "formula_frontier_rows": formula_frontier_rows(),
        "external_rows": external_rows(),
        "obstruction_rows": obstruction_rows(),
        "chosen_primary_attack_target": "UniformDeltaPhiCoverDefectOrNamedLPFOwnerResiduePDEC",
        "chosen_parallel_signed_target": "SourceKeyedMobiusVonMangoldtTraceTypeIIFamily",
        "chosen_parallel_distribution_target": "PointwiseThetaPsiCOneInputAtSqrtRowScale",
        "plain_conclusion": (
            "行级奇偶性障碍现在已压成一个明确不等式，但要真正破障，必须给出严格覆盖缺口、"
            "覆盖等号 PDEC、点态 theta/psi 平方根行输入，或 source-keyed signed divisor/trace/Type-II "
            "族。当前外部短区间最强输入仍厚于一行；固定 wheel 与 Euler product 主项只能定位残差，"
            "不能独立支付正性。"
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
    scale = cert["critical_scale"]
    lines = [
        "# Prime Matrix Phi-LPF row inequality breakthrough frontier 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"breakthrough_formula_frontier_synced={fmt_bool(cert['breakthrough_formula_frontier_synced'])}",
        f"strict_cover_inequality_proved_uniformly={fmt_bool(cert['strict_cover_inequality_proved_uniformly'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 临界尺度",
        "",
        "```text",
        f"x={scale['x']}",
        f"row_length={scale['row_length']}",
        f"expected_prime_count={scale['expected_prime_count']}",
        f"needed_error_strength={scale['needed_error_strength']}",
        "```",
        "",
        "最小新定理格式：",
        "",
        "```text",
        cert["minimum_new_theorem_statement"],
        "```",
        "",
        "## 2. 可真正破障的公式接口",
        "",
        "| priority | name | formula | new content needed | status |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for row in cert["formula_frontier_rows"]:
        lines.append(
            f"| {row['priority']} | `{cell(row['name'])}` | `{cell(row['formula'])}` | "
            f"{cell(row['new_content_needed'])} | {cell(row['current_status'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. 外部短区间尺度缺口",
            "",
            "| input | theta | length at x=P^2 | row thickening | closes one strict row | source |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_rows"]:
        lines.append(
            f"| {cell(row['input'])} | `{row['theta']}` | `{row['interval_length_at_x=P^2']}` | "
            f"`{row['row_thickening_factor']}` | `{row['strict_row_closed']}` | {cell(row['source'])} |"
        )

    lines.extend(
        [
            "",
            "## 4. 假突破路线的安全用法",
            "",
            "| route | failure | safe use |",
            "| --- | --- | --- |",
        ]
    )
    for row in cert["obstruction_rows"]:
        lines.append(f"| {cell(row['route'])} | {cell(row['failure'])} | {cell(row['safe_use'])} |")

    lines.extend(
        [
            "",
            "## 5. 下一手",
            "",
            "```text",
            f"chosen_primary_attack_target={cert['chosen_primary_attack_target']}",
            f"chosen_parallel_signed_target={cert['chosen_parallel_signed_target']}",
            f"chosen_parallel_distribution_target={cert['chosen_parallel_distribution_target']}",
            "```",
            "",
            "## 6. 依赖哈希",
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
    print(f"breakthrough_formula_frontier_synced={fmt_bool(cert['breakthrough_formula_frontier_synced'])}")
    print(f"chosen_primary_attack_target={cert['chosen_primary_attack_target']}")
    print(f"strict_cover_inequality_proved_uniformly={fmt_bool(cert['strict_cover_inequality_proved_uniformly'])}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
