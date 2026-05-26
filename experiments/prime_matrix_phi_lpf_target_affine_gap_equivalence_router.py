#!/usr/bin/env python3
"""生成目标仿射锚与 sqrt 级素数空窗等价证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_target_affine_gap_equivalence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json

输出：
  data/prime-matrix-phi-lpf-target-affine-gap-equivalence-ledger.json
  docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.json
  docs/monograph/prime-matrix-phi-lpf-target-affine-gap-equivalence-router.md
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

SLUG = "prime-matrix-phi-lpf-target-affine-gap-equivalence"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

OWNER_STRESS = DOCS / "prime-matrix-phi-lpf-full-cover-owner-pdec-stress-router.json"
TARGET_RESIDUE = DOCS / "prime-matrix-phi-lpf-row-inequality-target-residue-cover-router.json"
ROW_FRONTIER = DOCS / "prime-matrix-phi-lpf-row-inequality-breakthrough-frontier-router.json"
SQRT_ALIGNMENT = DOCS / "prime-matrix-phi-lpf-sqrt-oppermann-toprow-alignment-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SOURCE_FILES = [
    Path(__file__).resolve(),
    OWNER_STRESS,
    TARGET_RESIDUE,
    ROW_FRONTIER,
    SQRT_ALIGNMENT,
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


def exponent_row_gap(theta: Fraction) -> dict[str, str]:
    """把 x^theta 换算为 x=P^2 时的行厚度。"""
    return {
        "theta": f"{theta.numerator}/{theta.denominator}",
        "interval_length_at_x=P^2": f"P^({2 * theta})",
        "row_thickness_over_P": f"P^({2 * theta - 1})",
        "single_row_closed": str(theta <= Fraction(1, 2)).lower(),
    }


def equivalence_rows() -> list[dict[str, str]]:
    """列出目标仿射锚的等价形式。"""
    return [
        {
            "name": "TargetAffineFullCover",
            "formula": "union_{p<=sqrt((k+1)P-1)}D_p(P,k)=[1,P-1]",
            "equivalent_form": "pi(kP,(k+1)P)=0 on the punctured row",
            "status": "open to exclude",
        },
        {
            "name": "PrimeGapCrossingRow",
            "formula": "there exist adjacent primes u<v with u<=kP and v>=(k+1)P",
            "equivalent_form": "a prime gap covers the whole target row",
            "status": "open to exclude uniformly",
        },
        {
            "name": "SqrtScaleLocalInput",
            "formula": "for x=kP, a prime exists in (x,x+P)",
            "equivalent_form": "H/P=1 while sqrt(x)/P=sqrt(k/P)<1",
            "status": "requires C=1 sqrt-scale pointwise input near k~P",
        },
        {
            "name": "TopRowOppermannLeft",
            "formula": "k=P-1 gives (P^2-P,P^2)",
            "equivalent_form": "prime-indexed Oppermann left half-window",
            "status": "necessary subcore, still open",
        },
    ]


def rejected_affine_only_rows() -> list[dict[str, str]]:
    """列出只靠仿射锚仍不能非循环闭合的形式。"""
    return [
        {
            "route": "Affine anchor only",
            "failure": "A=kP merely rewrites the row as a prime-gap exclusion problem",
            "surviving_need": "add a signed/phase payload or a genuine pointwise sqrt-scale prime theorem",
        },
        {
            "route": "Legendre wide square interval",
            "failure": "Legendre's interval splits into two halves and does not force the left top row (P^2-P,P^2)",
            "surviving_need": "prime-indexed Oppermann-left or full target-row positivity",
        },
        {
            "route": "Baker-Harman-Pintz x^0.525",
            "failure": "at x=P^2 it gives length P^1.05, i.e. P^0.05 rows thick",
            "surviving_need": "exponent 1/2 with constant <=1, or structural signed substitute",
        },
        {
            "route": "RH-shaped explicit formula",
            "failure": "sqrt(x) log^2 x errors are larger than the one-row main term scale",
            "surviving_need": "cancellation beyond standard RH-size bounds at H=sqrt(x)",
        },
    ]


def external_gap_rows() -> list[dict[str, str]]:
    """记录外部输入在目标仿射锚上的缺口。"""
    rows = [
        {
            "input": "Baker-Harman-Pintz prime gaps",
            "source": "https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/difference-between-consecutive-primes-ii/2EF13261B3B25458A25F41ED74AA2FC2",
            **exponent_row_gap(Fraction(21, 40)),
            "meaning": "unconditional x^0.525 prime-gap bound is still thicker than one P-row at x=P^2",
        },
        {
            "input": "Guth-Maynard short intervals",
            "source": "https://annals.math.princeton.edu/2026/203-2/p06",
            **exponent_row_gap(Fraction(17, 30)),
            "meaning": "zero-density breakthrough gives P^(2/15) row thickening at x=P^2",
        },
        {
            "input": "Runbo Li Harman-sieve short intervals",
            "source": "https://arxiv.org/abs/2308.04458",
            **exponent_row_gap(Fraction(13, 25)),
            "meaning": "nearer to 1/2, but still P^(1/25) rows thick at x=P^2",
        },
    ]
    return rows


def finite_scan_summary(owner_stress: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取上一轮目标行有限扫描摘要。"""
    rows = owner_stress.get("target_min_defect_scan", [])
    return [
        {
            "P": row.get("P"),
            "min_k": row.get("min_k"),
            "min_prime_count": row.get("min_prime_count"),
            "strict_defect": row.get("strict_defect"),
            "full_cover": row.get("full_cover"),
        }
        for row in rows
    ]


def next_gate_rows() -> list[dict[str, str]]:
    """给出仍非循环的下一手。"""
    return [
        {
            "gate": "TargetAffineSignedPhasePayload",
            "needed_statement": "the residues a_p=-kP mod p carry a signed Mobius/Von-Mangoldt or phase law before LPF pushforward",
            "why_not_circular": "adds cancellation not present in support coverage",
        },
        {
            "gate": "PointwiseSqrtPrimeInputCOne",
            "needed_statement": "for every x=kP in the target range, (x,x+P) contains a prime; near k=P this is C=1 sqrt scale",
            "why_not_circular": "external analytic prime distribution would directly pay the row",
        },
        {
            "gate": "SpectralKloostermanResidueLiftWithSourceKeys",
            "needed_statement": "complete target-affine residue fibers into a trace family with conductor and coefficient control",
            "why_not_circular": "turns residue support into oscillatory cancellation",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    owner_stress = load_json(OWNER_STRESS)
    target_residue = load_json(TARGET_RESIDUE)
    row_frontier = load_json(ROW_FRONTIER)
    sqrt_alignment = load_json(SQRT_ALIGNMENT)
    synced = all(
        [
            owner_stress.get("owner_only_pdec_rejected") is True,
            target_residue.get("target_row_residue_cover_standard_form_synced") is True,
            row_frontier.get("breakthrough_formula_frontier_synced") is True,
        ]
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_target_affine_gap_equivalence_router",
        "status": "target_affine_anchor_reduced_to_sqrt_prime_gap_or_signed_phase_payload",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "finite_evidence_not_used_as_global_proof": True,
        "target_affine_gap_equivalence_synced": synced,
        "owner_only_pdec_rejected_imported": owner_stress.get("owner_only_pdec_rejected") is True,
        "target_affine_anchor_alone_closes": False,
        "target_affine_owner_pdec_proved": False,
        "top_row_oppermann_left_imported": bool(sqrt_alignment),
        "row_column_unconditional_closed": False,
        "equivalence_rows": equivalence_rows(),
        "rejected_affine_only_rows": rejected_affine_only_rows(),
        "external_gap_rows": external_gap_rows(),
        "finite_scan_summary": finite_scan_summary(owner_stress),
        "next_gate_rows": next_gate_rows(),
        "selected_next_primary_gate": "TargetAffineSignedPhasePayload",
        "selected_parallel_distribution_gate": "PointwiseSqrtPrimeInputCOne",
        "selected_parallel_spectral_gate": "SpectralKloostermanResidueLiftWithSourceKeys",
        "plain_conclusion": (
            "目标仿射锚 A=kP 并没有自行产生 PDEC；它把 full-cover 等号精确改写为一个 "
            "prime gap 覆盖整行的问题。最坏 k≈P 时就是 x≈P^2、H≈sqrt(x) 的 C=1 点态"
            "短区间问题；top row 是 prime-indexed Oppermann-left 半窗。因而 target-affine-only "
            "路线也不能闭合，下一手必须加入 signed/phase payload、真正 C=1 sqrt 输入，"
            "或 source-keyed spectral/Kloosterman lift。"
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
        "# Prime Matrix Phi-LPF target-affine gap equivalence 路由",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"target_affine_gap_equivalence_synced={fmt_bool(cert['target_affine_gap_equivalence_synced'])}",
        f"owner_only_pdec_rejected_imported={fmt_bool(cert['owner_only_pdec_rejected_imported'])}",
        f"target_affine_anchor_alone_closes={fmt_bool(cert['target_affine_anchor_alone_closes'])}",
        f"target_affine_owner_pdec_proved={fmt_bool(cert['target_affine_owner_pdec_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 等价形式",
        "",
        "| name | formula | equivalent form | status |",
        "| --- | --- | --- | --- |",
    ]
    for row in cert["equivalence_rows"]:
        lines.append(
            f"| `{cell(row['name'])}` | `{cell(row['formula'])}` | "
            f"{cell(row['equivalent_form'])} | {cell(row['status'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. target-affine-only 路线被压缩",
            "",
            "| route | failure | surviving need |",
            "| --- | --- | --- |",
        ]
    )
    for row in cert["rejected_affine_only_rows"]:
        lines.append(f"| {cell(row['route'])} | {cell(row['failure'])} | {cell(row['surviving_need'])} |")

    lines.extend(
        [
            "",
            "## 3. 外部 gap/短区间尺度",
            "",
            "| input | theta | length at x=P^2 | row thickness over P | closes one row | source |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_gap_rows"]:
        lines.append(
            f"| {cell(row['input'])} | `{row['theta']}` | `{row['interval_length_at_x=P^2']}` | "
            f"`{row['row_thickness_over_P']}` | `{row['single_row_closed']}` | {cell(row['source'])} |"
        )

    lines.extend(
        [
            "",
            "## 4. 已有有限扫描摘要",
            "",
            "| P | min-k | min prime count | strict defect | full cover |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in cert["finite_scan_summary"]:
        lines.append(
            f"| {row['P']} | {row['min_k']} | {row['min_prime_count']} | "
            f"{row['strict_defect']} | `{fmt_bool(row['full_cover'])}` |"
        )

    lines.extend(
        [
            "",
            "## 5. 下一手",
            "",
            "| gate | needed statement | why not circular |",
            "| --- | --- | --- |",
        ]
    )
    for row in cert["next_gate_rows"]:
        lines.append(
            f"| `{cell(row['gate'])}` | {cell(row['needed_statement'])} | "
            f"{cell(row['why_not_circular'])} |"
        )

    lines.extend(
        [
            "",
            "```text",
            f"selected_next_primary_gate={cert['selected_next_primary_gate']}",
            f"selected_parallel_distribution_gate={cert['selected_parallel_distribution_gate']}",
            f"selected_parallel_spectral_gate={cert['selected_parallel_spectral_gate']}",
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
    print(f"target_affine_gap_equivalence_synced={fmt_bool(cert['target_affine_gap_equivalence_synced'])}")
    print(f"target_affine_anchor_alone_closes={fmt_bool(cert['target_affine_anchor_alone_closes'])}")
    print(f"selected_next_primary_gate={cert['selected_next_primary_gate']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
