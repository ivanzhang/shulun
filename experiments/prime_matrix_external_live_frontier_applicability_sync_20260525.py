#!/usr/bin/env python3
"""同步 2026-05-25 外部前沿定理与当前 Phi-LPF 硬点的可用性。

用法示例：
  python3 experiments/prime_matrix_external_live_frontier_applicability_sync_20260525.py
  python3 -m json.tool docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json

输出：
  data/prime-matrix-external-live-frontier-applicability-sync-20260525-ledger.json
  docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.json
  docs/monograph/prime-matrix-external-live-frontier-applicability-sync-20260525.md

本层只做外部输入匹配审计：哪些最新定理能在后续构造出 admissible family
之后调用，哪些不能直接闭合当前 pivot/right-tail/adjacent-run 硬点。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-external-live-frontier-applicability-sync-20260525"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}.json"
OUT_MD = DOCS / f"{SLUG}.md"


CURRENT_PM_GATE = (
    "BridgeRootQSpinePivotEnclosureLawOrPDEC AND "
    "RightSelectedTerminalTailOverhangPDEC AND "
    "BoundaryAdjacentRunMassRatioLawOrPDEC AND "
    "PrimitiveOrientationLocalFactorProductLawBeforePushforward AND "
    "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving AND "
    "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily AND "
    "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"
)

CURRENT_TP_GATE = (
    "ActualDenominatorFloorWithSameSingularSeriesConvention AND "
    "ActualNumeratorBMDKLSBound AND "
    "DeltaPlusEpsilonBelowOneMinusKAlpha"
)


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        DOCS / "prime-matrix-phi-lpf-terminal-boundary-bridge-root-qspine-pivot-enclosure-router.json",
        DOCS / "three-claims-breakthrough-route-synthesis-20260525.md",
        DOCS / "three-claims-actual-load-closure-contracts.md",
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def external_inputs() -> list[dict[str, Any]]:
    """列出本轮核对的外部前沿输入。"""
    return [
        {
            "label": "Milićević-Qin-Wu arbitrary-modulus Kloosterman bilinear forms",
            "url": "https://arxiv.org/abs/2511.07550",
            "frontier_content": (
                "general bilinear forms with Kloosterman sums modulo arbitrary q, "
                "including short-variable ranges"
            ),
            "usable_after": (
                "moving Beatty numerator and prefix/source-key data have been completed "
                "into a genuine two-variable Kloosterman family"
            ),
            "missing_currently": (
                "current PM object is a finite pivot/right-tail/adjacent-run ledger, "
                "not a completed bilinear family"
            ),
            "can_close_current_pm_gate_directly": False,
        },
        {
            "label": "Wright trilinear Kloosterman fractions",
            "url": "https://arxiv.org/abs/2604.25177",
            "frontier_content": (
                "trilinear Kloosterman-fraction estimates for partially fixed moduli "
                "and unbalanced convolutions"
            ),
            "usable_after": (
                "terminal payload is lifted to a trilinear convolution with an "
                "equidistributed beta sequence"
            ),
            "missing_currently": (
                "no source-key lift, no trilinear convolution, and no beta-sequence "
                "equidistribution object has been constructed"
            ),
            "can_close_current_pm_gate_directly": False,
        },
        {
            "label": "Runbo Li large-modulus AP primes and Harman sieve refinements",
            "url": "https://arxiv.org/abs/2602.20917",
            "frontier_content": (
                "Bombieri-Vinogradov type mean value theorems for primes in large-modulus "
                "bilinear/trilinear average families and almost-all AP bounds"
            ),
            "usable_after": (
                "two-point denominator and numerator are both expressed in the same "
                "average-modulus convention"
            ),
            "missing_currently": (
                "Prime Matrix needs pointwise row/column actual load at x=P^2, not "
                "almost-all moduli distribution"
            ),
            "can_close_current_pm_gate_directly": False,
        },
        {
            "label": "Becker-Breuillard uniform spectral gaps and anti-concentration",
            "url": "https://arxiv.org/abs/2512.15364",
            "frontier_content": (
                "uniform spectral gap and anti-concentration for random walks on "
                "semisimple algebraic groups"
            ),
            "usable_after": (
                "a genuine finite-group orbit or thin-group sieve family is built from "
                "the terminal payload"
            ),
            "missing_currently": (
                "the present q-spine pivot ledger is not a group orbit and has no "
                "Cayley/expander model"
            ),
            "can_close_current_pm_gate_directly": False,
        },
    ]


def build_payload() -> dict[str, Any]:
    """构造外部前沿可用性证书。"""
    rows = external_inputs()
    return {
        "certificate_type": "prime_matrix_external_live_frontier_applicability_sync_20260525",
        "verified_date": "2026-05-25",
        "status": "external_live_frontier_synced_no_direct_phi_lpf_closure",
        "external_input_count": len(rows),
        "external_inputs": rows,
        "current_pm_gate": CURRENT_PM_GATE,
        "current_tp_gate": CURRENT_TP_GATE,
        "all_inputs_require_admissible_family_before_use": all(
            not row["can_close_current_pm_gate_directly"] for row in rows
        ),
        "admissible_averaged_signed_trace_family_constructed": False,
        "admissible_finite_group_orbit_family_constructed": False,
        "pointwise_row_column_ap_positivity_imported": False,
        "two_point_actual_denominator_floor_closed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "two_point_unconditional_closed": False,
        "rh_unconditional_closed": False,
        "plain_conclusion": (
            "The live external frontier is useful only after the project constructs an "
            "admissible averaged trace/Kloosterman/Type-II or finite-group orbit family. "
            "None of the checked inputs directly proves the current q-spine pivot, "
            "right-tail overhang, adjacent-run ratio, or pointwise P^2 row/column gate."
        ),
        "next_noncyclic_attack_target": (
            "construct SourceKeyLift/PrimitiveOrientationLocalFactorProduct before "
            "calling trace/Kloosterman/Type-II tools, or return a named PDEC/SAE/"
            "LocalSurvivor"
        ),
        "source_hashes": source_hashes(),
    }


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix 外部前沿可用性同步（2026-05-25）",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把本轮核对的 2025-2026 外部前沿输入接到当前 Phi-LPF/PM 硬点。",
        "结论是：这些定理都是潜在强工具，但都需要先构造 admissible family；",
        "不能直接替代 q-spine pivot、right-tail、相邻 run 质量比或逐列 `P^2` 正性。",
        "",
        "```text",
        f"external_input_count={payload['external_input_count']}",
        f"all_inputs_require_admissible_family_before_use={fmt_bool(payload['all_inputs_require_admissible_family_before_use'])}",
        f"admissible_averaged_signed_trace_family_constructed={fmt_bool(payload['admissible_averaged_signed_trace_family_constructed'])}",
        f"admissible_finite_group_orbit_family_constructed={fmt_bool(payload['admissible_finite_group_orbit_family_constructed'])}",
        f"pointwise_row_column_ap_positivity_imported={fmt_bool(payload['pointwise_row_column_ap_positivity_imported'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        f"phi_lpf_parity_barrier_globally_broken={fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}",
        "```",
        "",
        "## 1. 外部输入匹配表",
        "",
        "| input | source | 可用前提 | 当前缺口 | direct close |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in payload["external_inputs"]:
        lines.append(
            "| {label} | {url} | {usable_after} | {missing_currently} | `{direct}` |".format(
                label=row["label"],
                url=row["url"],
                usable_after=row["usable_after"],
                missing_currently=row["missing_currently"],
                direct=fmt_bool(row["can_close_current_pm_gate_directly"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 当前 PM 门",
            "",
            "```text",
            payload["current_pm_gate"],
            "```",
            "",
            "## 3. 非循环下一步",
            "",
            payload["next_noncyclic_attack_target"],
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.extend(["", "本层不是无条件闭合证明。", ""])
    return "\n".join(lines)


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(payload), encoding="utf-8")


def main() -> None:
    """命令入口。"""
    payload = build_payload()
    write_outputs(payload)
    print(f"external_input_count={payload['external_input_count']}")
    print(
        "all_inputs_require_admissible_family_before_use="
        f"{fmt_bool(payload['all_inputs_require_admissible_family_before_use'])}"
    )
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")
    print(
        "phi_lpf_parity_barrier_globally_broken="
        f"{fmt_bool(payload['phi_lpf_parity_barrier_globally_broken'])}"
    )


if __name__ == "__main__":
    main()
