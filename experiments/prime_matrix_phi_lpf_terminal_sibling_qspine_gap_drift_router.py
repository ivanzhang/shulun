#!/usr/bin/env python3
"""审计 terminal sibling q-spine integer balance 的 gap-drift 正规形。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_gap_drift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-router.json

上一层整数守恒为

  295*439 = 203*461 + 60*467 + 18*439.

把 461=439+22、467=439+28 代回，并把 offset 系数 18 移到左边，得到

  (295-203-60-18)*439 = 22*203 + 28*60.

也就是

  14*439 = 22*203 + 28*60.

除以 q-spine gap 公因子 2 后得到 primitive gap-drift 形式：

  7*439 = 11*203 + 14*60.

由于 203=7*29 且 14=7*2，还可剥离 LPF-threshold 因子 7：

  439 = 11*29 + 2*60.

这不是无条件闭合；它把 terminal integer-balance payment 门继续降成
primitive gap-drift payment/exclusion 或 PDEC。
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

SLUG = "prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

INTEGER_BALANCE_JSON = DOCS / "prime-matrix-phi-lpf-terminal-sibling-qspine-integer-balance-router.json"

PIVOT_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
GAP_DRIFT_LAW = "TerminalSiblingQSpinePrimitiveGapDriftPaymentOrPDEC"
MASS_RATIO_LAW = "BoundaryAdjacentRunMassRatioLawOrPDEC"
ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
MOVING_BEATTY_SAVING = "SelectedTerminalMovingBeattyNumeratorPrimeQPrefixPhaseSaving"
TRACE_FAMILY = "AdmissibleAveragedSignedTraceKloostermanOrTypeIIFamily"
GROUP_ORBIT_INPUT = "AdmissibleFiniteGroupOrbitExpansionOrThinGroupSieveFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), INTEGER_BALANCE_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def build_certificate() -> dict[str, Any]:
    """组装 gap-drift 证书。"""
    payload = load_json(INTEGER_BALANCE_JSON)

    q_prefix = int(payload["q_prefix"])
    q_mid = int(payload["q_mid"])
    q_right = int(payload["q_right"])
    coefficients = payload["coefficients"]
    target = int(coefficients["target_final_tail"])
    paid = int(coefficients["paid_sibling_tail"])
    middle = int(coefficients["middle_kernel"])
    offset = int(coefficients["endpoint_offset"])

    gap_mid = q_mid - q_prefix
    gap_right = q_right - q_prefix
    gap_gcd = math.gcd(gap_mid, gap_right)
    primitive_mid = gap_mid // gap_gcd
    primitive_right = gap_right // gap_gcd

    drift_defect = target - paid - middle - offset
    offset_cancels = (
        target * q_prefix
        == paid * q_prefix + middle * q_prefix + offset * q_prefix + drift_defect * q_prefix
    )
    gap_drift_left = drift_defect * q_prefix
    gap_drift_right = gap_mid * paid + gap_right * middle
    gap_drift_closed = gap_drift_left == gap_drift_right

    primitive_defect = drift_defect // gap_gcd if drift_defect % gap_gcd == 0 else None
    primitive_gap_drift_left = primitive_defect * q_prefix if primitive_defect is not None else None
    primitive_gap_drift_right = primitive_mid * paid + primitive_right * middle
    primitive_gap_drift_closed = primitive_gap_drift_left == primitive_gap_drift_right

    lpf_threshold = 7
    paid_divides_lpf = paid % lpf_threshold == 0
    primitive_right_divides_lpf = primitive_right % lpf_threshold == 0
    primitive_defect_is_lpf = primitive_defect == lpf_threshold
    lpf_peeled_left = q_prefix
    lpf_peeled_right = None
    if paid_divides_lpf and primitive_right_divides_lpf and primitive_defect_is_lpf:
        lpf_peeled_right = primitive_mid * (paid // lpf_threshold) + (primitive_right // lpf_threshold) * middle
    lpf_factor_peeling_closed = lpf_peeled_right == lpf_peeled_left

    inherited_integer_balance_closed = (
        payload.get("terminal_sibling_qspine_integer_balance_closed") is True
        and payload.get("terminal_sibling_qspine_integer_balance_payment_law_proved") is False
    )
    reduction_closed = all(
        [
            inherited_integer_balance_closed,
            offset_cancels,
            gap_drift_closed,
            primitive_gap_drift_closed,
            paid_divides_lpf,
            primitive_right_divides_lpf,
            primitive_defect_is_lpf,
            lpf_factor_peeling_closed,
        ]
    )

    latest_open_gate = (
        f"{PIVOT_LAW} AND {GAP_DRIFT_LAW} AND {MASS_RATIO_LAW} AND "
        f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_sibling_qspine_gap_drift_router",
        "status": "terminal_sibling_qspine_gap_drift_closed_payment_law_open",
        "verified_date": "2026-05-25",
        "previous_integer_balance_closed": inherited_integer_balance_closed,
        "P": int(payload["P"]),
        "q_spine_for_balance": [q_prefix, q_mid, q_right],
        "q_path_from_double_awrap": payload["q_path_from_double_awrap"],
        "q_gaps_from_prefix": [gap_mid, gap_right],
        "gap_gcd": gap_gcd,
        "primitive_gap_vector": [primitive_mid, primitive_right],
        "coefficients": {
            "target_final_tail": target,
            "paid_sibling_tail": paid,
            "middle_kernel": middle,
            "endpoint_offset": offset,
            "drift_defect": drift_defect,
            "primitive_defect": primitive_defect,
            "paid_sibling_tail_after_lpf_peel": paid // lpf_threshold if paid_divides_lpf else None,
            "primitive_right_gap_after_lpf_peel": (
                primitive_right // lpf_threshold if primitive_right_divides_lpf else None
            ),
        },
        "offset_cancels_from_gap_drift": offset_cancels,
        "gap_drift_identity_closed": gap_drift_closed,
        "gap_drift_identity": {
            "left": gap_drift_left,
            "right": gap_drift_right,
            "formula": f"({target}-{paid}-{middle}-{offset})*{q_prefix} = {gap_mid}*{paid} + {gap_right}*{middle}",
        },
        "primitive_gap_drift_identity_closed": primitive_gap_drift_closed,
        "primitive_gap_drift_identity": {
            "left": primitive_gap_drift_left,
            "right": primitive_gap_drift_right,
            "formula": f"{primitive_defect}*{q_prefix} = {primitive_mid}*{paid} + {primitive_right}*{middle}",
        },
        "lpf_threshold_factor": lpf_threshold,
        "paid_divides_lpf_threshold": paid_divides_lpf,
        "primitive_right_gap_divides_lpf_threshold": primitive_right_divides_lpf,
        "primitive_defect_is_lpf_threshold": primitive_defect_is_lpf,
        "lpf_factor_peeling_closed": lpf_factor_peeling_closed,
        "lpf_peeled_identity": {
            "left": lpf_peeled_left,
            "right": lpf_peeled_right,
            "formula": (
                f"{q_prefix} = {primitive_mid}*{paid // lpf_threshold if paid_divides_lpf else 'NA'} "
                f"+ {primitive_right // lpf_threshold if primitive_right_divides_lpf else 'NA'}*{middle}"
            ),
        },
        "terminal_sibling_qspine_gap_drift_closed": reduction_closed,
        "terminal_sibling_qspine_gap_drift_payment_law_proved": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_open_gate,
        "next_primary_attack_target": GAP_DRIFT_LAW,
        "gate_rows": [
            {
                "gate": "IntegerBalanceImported",
                "closed": inherited_integer_balance_closed,
                "proved": inherited_integer_balance_closed,
                "meaning": "上一层 terminal integer balance 已有限闭合，支付律仍未证明。",
                "remaining": "finite integer-balance ledger",
            },
            {
                "gate": "OffsetCancellationInGapDrift",
                "closed": offset_cancels,
                "proved": offset_cancels,
                "meaning": "endpoint offset 与 target 共用 q_mid*q_right 分母，清分母后只贡献 q_prefix 项并可并入 defect。",
                "remaining": "finite offset ledger",
            },
            {
                "gate": "GapDriftIdentity",
                "closed": gap_drift_closed,
                "proved": gap_drift_closed,
                "meaning": "integer balance 等价于 drift defect 支付 q-prefix 到两个 q-spine gap 的漂移。",
                "remaining": "finite gap-drift identity",
            },
            {
                "gate": "PrimitiveGapDriftIdentity",
                "closed": primitive_gap_drift_closed,
                "proved": primitive_gap_drift_closed,
                "meaning": "除以 q-spine gap 公因子 2 后得到 primitive drift law。",
                "remaining": "finite primitive gap ledger",
            },
            {
                "gate": "LPFThresholdSevenPeel",
                "closed": lpf_factor_peeling_closed,
                "proved": lpf_factor_peeling_closed,
                "meaning": "primitive defect 是 7，且 paid coefficient 与 right primitive gap 可剥离同一 LPF-threshold 因子。",
                "remaining": "finite 7-factor ledger",
            },
            {
                "gate": "TerminalSiblingQSpinePrimitiveGapDriftPaymentLaw",
                "closed": False,
                "proved": False,
                "meaning": "仍需 uniform law 支付或排除该 primitive gap-drift，而不能只在 m773 有限点成立。",
                "remaining": GAP_DRIFT_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "这是 finite gap-drift reduction，不是全局奇偶性突破定理。",
                "remaining": f"{PIVOT_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
            },
        ],
        "plain_conclusion": (
            "The terminal integer balance is equivalent to a primitive q-spine gap-drift law: "
            "14*439 = 22*203 + 28*60, hence 7*439 = 11*203 + 14*60, and after peeling "
            "the LPF-threshold factor 7, 439 = 11*29 + 2*60. The remaining task is a "
            "uniform primitive gap-drift payment/exclusion law or PDEC."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal sibling q-spine gap-drift 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 terminal integer balance 改写为 q-spine gap-drift 正规形。",
        "",
        "```text",
        f"q_spine_for_balance={payload['q_spine_for_balance']}",
        f"q_gaps_from_prefix={payload['q_gaps_from_prefix']}",
        f"primitive_gap_vector={payload['primitive_gap_vector']}",
        f"offset_cancels_from_gap_drift={fmt_bool(payload['offset_cancels_from_gap_drift'])}",
        f"gap_drift_identity_closed={fmt_bool(payload['gap_drift_identity_closed'])}",
        f"primitive_gap_drift_identity_closed={fmt_bool(payload['primitive_gap_drift_identity_closed'])}",
        f"lpf_factor_peeling_closed={fmt_bool(payload['lpf_factor_peeling_closed'])}",
        f"terminal_sibling_qspine_gap_drift_closed={fmt_bool(payload['terminal_sibling_qspine_gap_drift_closed'])}",
        f"terminal_sibling_qspine_gap_drift_payment_law_proved={fmt_bool(payload['terminal_sibling_qspine_gap_drift_payment_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. gap-drift identities",
        "",
        "```text",
        payload["gap_drift_identity"]["formula"],
        f"{payload['gap_drift_identity']['left']} = {payload['gap_drift_identity']['right']}",
        payload["primitive_gap_drift_identity"]["formula"],
        f"{payload['primitive_gap_drift_identity']['left']} = {payload['primitive_gap_drift_identity']['right']}",
        payload["lpf_peeled_identity"]["formula"],
        f"{payload['lpf_peeled_identity']['left']} = {payload['lpf_peeled_identity']['right']}",
        "```",
        "",
        "## 2. coefficients",
        "",
        "| quantity | value |",
        "| --- | ---: |",
    ]
    for key, value in payload["coefficients"].items():
        lines.append(f"| `{key}` | {value} |")
    lines.extend(
        [
            "",
            "## 3. 门控表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in payload["gate_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.extend(["", "行/列命题仍未无条件闭合。", ""])
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
    payload = build_certificate()
    write_outputs(payload)
    print(
        "terminal_sibling_qspine_gap_drift_closed="
        f"{fmt_bool(payload['terminal_sibling_qspine_gap_drift_closed'])}"
    )
    print(f"primitive_gap_drift_identity_closed={fmt_bool(payload['primitive_gap_drift_identity_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
