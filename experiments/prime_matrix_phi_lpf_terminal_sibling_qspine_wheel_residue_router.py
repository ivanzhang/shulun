#!/usr/bin/env python3
"""审计 terminal primitive gap-drift 是否降为 30-wheel residue carrier。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_wheel_residue_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-router.json

上一层剥离 LPF-threshold 因子 7 后得到

  439 = 11*29 + 2*60.

由于 60=2*30，该式等价于

  439 = 11*29 + 4*30.

因此 terminal primitive drift 的非 30-wheel residue 载体只有 11*29：

  439 mod 30 = (11*29) mod 30 = 19,

而剩余差值正好是 4 个完整 30-wheel 周期。这里

  4 = 2*(60/30),

即 right primitive gap after the 7-peel 乘以 middle kernel 的 wheel 单位数。
这仍不是无条件闭合；它把 primitive gap-drift payment 门继续降为一个
30-wheel residue-carrier payment/exclusion 或 PDEC。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

GAP_DRIFT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-router.json"

PIVOT_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
WHEEL_RESIDUE_LAW = "TerminalSiblingQSpineWheelResidueCarrierPaymentOrPDEC"
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
    paths = [Path(__file__).resolve(), GAP_DRIFT_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def divmod_record(value: int, modulus: int) -> dict[str, int]:
    """稳定输出 quotient/residue。"""
    return {"value": value, "quotient": value // modulus, "residue": value % modulus}


def build_certificate() -> dict[str, Any]:
    """组装 30-wheel residue-carrier 证书。"""
    payload = load_json(GAP_DRIFT_JSON)

    wheel = 30
    q_prefix = int(payload["q_spine_for_balance"][0])
    primitive_mid_gap = int(payload["primitive_gap_vector"][0])
    paid_after_lpf = int(payload["coefficients"]["paid_sibling_tail_after_lpf_peel"])
    right_gap_after_lpf = int(payload["coefficients"]["primitive_right_gap_after_lpf_peel"])
    middle_kernel = int(payload["coefficients"]["middle_kernel"])

    carrier = primitive_mid_gap * paid_after_lpf
    wheel_neutral_mass = right_gap_after_lpf * middle_kernel
    middle_kernel_wheel_units = middle_kernel // wheel if middle_kernel % wheel == 0 else None
    predicted_wheel_lift_height = (
        right_gap_after_lpf * middle_kernel_wheel_units if middle_kernel_wheel_units is not None else None
    )
    actual_wheel_lift_height = (q_prefix - carrier) // wheel if (q_prefix - carrier) % wheel == 0 else None

    residue_match_closed = q_prefix % wheel == carrier % wheel
    wheel_neutral_mass_closed = wheel_neutral_mass % wheel == 0
    wheel_lift_closed = actual_wheel_lift_height == predicted_wheel_lift_height
    carrier_identity_closed = q_prefix == carrier + wheel_neutral_mass
    quotient_residue_lift_closed = (
        divmod(q_prefix, wheel)[0] - divmod(carrier, wheel)[0] == actual_wheel_lift_height
    )

    inherited_gap_drift_closed = (
        payload.get("terminal_sibling_qspine_gap_drift_closed") is True
        and payload.get("terminal_sibling_qspine_gap_drift_payment_law_proved") is False
    )
    reduction_closed = all(
        [
            inherited_gap_drift_closed,
            middle_kernel_wheel_units is not None,
            residue_match_closed,
            wheel_neutral_mass_closed,
            wheel_lift_closed,
            carrier_identity_closed,
            quotient_residue_lift_closed,
        ]
    )

    latest_open_gate = (
        f"{PIVOT_LAW} AND {WHEEL_RESIDUE_LAW} AND {MASS_RATIO_LAW} AND "
        f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_sibling_qspine_wheel_residue_router",
        "status": "terminal_sibling_qspine_wheel_residue_closed_payment_law_open",
        "verified_date": "2026-05-25",
        "previous_gap_drift_closed": inherited_gap_drift_closed,
        "P": int(payload["P"]),
        "wheel_modulus": wheel,
        "q_prefix": q_prefix,
        "primitive_mid_gap": primitive_mid_gap,
        "paid_after_lpf_peel": paid_after_lpf,
        "right_gap_after_lpf_peel": right_gap_after_lpf,
        "middle_kernel": middle_kernel,
        "middle_kernel_wheel_units": middle_kernel_wheel_units,
        "residue_carrier": carrier,
        "wheel_neutral_mass": wheel_neutral_mass,
        "actual_wheel_lift_height": actual_wheel_lift_height,
        "predicted_wheel_lift_height": predicted_wheel_lift_height,
        "q_prefix_divmod_wheel": divmod_record(q_prefix, wheel),
        "residue_carrier_divmod_wheel": divmod_record(carrier, wheel),
        "residue_match_closed": residue_match_closed,
        "wheel_neutral_mass_closed": wheel_neutral_mass_closed,
        "wheel_lift_closed": wheel_lift_closed,
        "carrier_identity_closed": carrier_identity_closed,
        "quotient_residue_lift_closed": quotient_residue_lift_closed,
        "wheel_residue_identity": {
            "formula": f"{q_prefix} = {primitive_mid_gap}*{paid_after_lpf} + {actual_wheel_lift_height}*{wheel}",
            "left": q_prefix,
            "right": carrier + (actual_wheel_lift_height or 0) * wheel,
        },
        "wheel_lift_height_identity": {
            "formula": f"{actual_wheel_lift_height} = {right_gap_after_lpf}*({middle_kernel}/{wheel})",
            "left": actual_wheel_lift_height,
            "right": predicted_wheel_lift_height,
        },
        "terminal_sibling_qspine_wheel_residue_closed": reduction_closed,
        "terminal_sibling_qspine_wheel_residue_payment_law_proved": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_open_gate,
        "next_primary_attack_target": WHEEL_RESIDUE_LAW,
        "gate_rows": [
            {
                "gate": "PrimitiveGapDriftImported",
                "closed": inherited_gap_drift_closed,
                "proved": inherited_gap_drift_closed,
                "meaning": "上一层 primitive gap-drift 已有限闭合，支付律仍未证明。",
                "remaining": "finite gap-drift ledger",
            },
            {
                "gate": "MiddleKernelWheelNeutrality",
                "closed": middle_kernel_wheel_units is not None,
                "proved": middle_kernel_wheel_units is not None,
                "meaning": "middle kernel coefficient 60 是两个完整 30-wheel 周期。",
                "remaining": "finite wheel-unit ledger",
            },
            {
                "gate": "ResidueCarrierCongruence",
                "closed": residue_match_closed,
                "proved": residue_match_closed,
                "meaning": "q_prefix 与 11*29 有相同 30-wheel residue，非轮周期 residue 已由 11*29 承载。",
                "remaining": "finite residue congruence",
            },
            {
                "gate": "WheelLiftHeightIdentity",
                "closed": wheel_lift_closed,
                "proved": wheel_lift_closed,
                "meaning": "q_prefix 与 residue carrier 的 quotient 差正好等于 right gap after 7-peel 乘以 middle wheel units。",
                "remaining": "finite wheel-lift ledger",
            },
            {
                "gate": "WheelResidueCarrierIdentity",
                "closed": carrier_identity_closed,
                "proved": carrier_identity_closed,
                "meaning": "7-peeled primitive drift 等价于 q_prefix=residue carrier+完整 wheel periods。",
                "remaining": "finite wheel-residue identity",
            },
            {
                "gate": "TerminalSiblingQSpineWheelResidueCarrierPaymentLaw",
                "closed": False,
                "proved": False,
                "meaning": "仍需 uniform law 支付或排除该 wheel-residue carrier，而不能只在 m773 有限点成立。",
                "remaining": WHEEL_RESIDUE_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "这是 finite wheel-residue reduction，不是全局奇偶性突破定理。",
                "remaining": f"{PIVOT_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
            },
        ],
        "plain_conclusion": (
            "The 7-peeled primitive gap-drift 439 = 11*29 + 2*60 is equivalent to "
            "a 30-wheel residue-carrier identity: 439 = 11*29 + 4*30, with "
            "439 mod 30 = 11*29 mod 30 = 19 and 4 = 2*(60/30). The remaining task "
            "is a uniform wheel-residue carrier payment/exclusion law or PDEC."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal sibling q-spine wheel-residue 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 7-peeled primitive gap-drift 改写为 30-wheel residue carrier。",
        "",
        "```text",
        f"q_prefix={payload['q_prefix']}",
        f"wheel_modulus={payload['wheel_modulus']}",
        f"residue_carrier={payload['residue_carrier']}",
        f"wheel_neutral_mass={payload['wheel_neutral_mass']}",
        f"residue_match_closed={fmt_bool(payload['residue_match_closed'])}",
        f"wheel_lift_closed={fmt_bool(payload['wheel_lift_closed'])}",
        f"carrier_identity_closed={fmt_bool(payload['carrier_identity_closed'])}",
        f"terminal_sibling_qspine_wheel_residue_closed={fmt_bool(payload['terminal_sibling_qspine_wheel_residue_closed'])}",
        f"terminal_sibling_qspine_wheel_residue_payment_law_proved={fmt_bool(payload['terminal_sibling_qspine_wheel_residue_payment_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. wheel-residue identity",
        "",
        "```text",
        payload["wheel_residue_identity"]["formula"],
        f"{payload['wheel_residue_identity']['left']} = {payload['wheel_residue_identity']['right']}",
        f"{payload['q_prefix']} mod 30 = {payload['q_prefix_divmod_wheel']['residue']}",
        f"{payload['residue_carrier']} mod 30 = {payload['residue_carrier_divmod_wheel']['residue']}",
        payload["wheel_lift_height_identity"]["formula"],
        f"{payload['wheel_lift_height_identity']['left']} = {payload['wheel_lift_height_identity']['right']}",
        "```",
        "",
        "## 2. 门控表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 最新开放口",
            "",
            "```text",
            payload["latest_open_gate"],
            "```",
            "",
            "## 4. 依赖哈希",
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
        "terminal_sibling_qspine_wheel_residue_closed="
        f"{fmt_bool(payload['terminal_sibling_qspine_wheel_residue_closed'])}"
    )
    print(f"wheel_lift_closed={fmt_bool(payload['wheel_lift_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
