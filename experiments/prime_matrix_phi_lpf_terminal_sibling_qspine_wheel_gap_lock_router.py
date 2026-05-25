#!/usr/bin/env python3
"""审计 terminal wheel-residue carrier 是否锁定到 double-Awrap q-gap。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_terminal_sibling_qspine_wheel_gap_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock-router.json

上一层把 terminal residue carrier 写成

  439 = 11*29 + 4*30,

其中 wheel lift height 为 4。本层把这个 4 与 terminal double-Awrap
q-gap path [2,4] 对齐：

  first_gap = 2 = middle_kernel/30 = right_gap_after_7_peel,
  second_gap = 4 = wheel_lift_height = first_gap^2.

同时 right-side q-spine [439,461,467] 也由该 first_gap 生成：

  461-439 = 11*2,
  467-439 = 14*2 = 7*2*2.

这仍不是无条件闭合；它把 wheel-residue carrier payment 门继续降为一个
terminal q-gap lock payment/exclusion 或 PDEC。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-gap-lock"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

WHEEL_RESIDUE_JSON = DOCS / "prime-matrix-phi-lpf-terminal-sibling-qspine-wheel-residue-router.json"
SIBLING_KERNEL_JSON = DOCS / "prime-matrix-phi-lpf-terminal-double-awrap-sibling-qspine-kernel-router.json"
GAP_DRIFT_JSON = DOCS / "prime-matrix-phi-lpf-terminal-sibling-qspine-gap-drift-router.json"

PIVOT_LAW = "BridgeRootQSpinePivotEnclosureLawOrPDEC"
GAP_LOCK_LAW = "TerminalSiblingQSpineWheelGapLockPaymentOrPDEC"
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
    paths = [Path(__file__).resolve(), WHEEL_RESIDUE_JSON, SIBLING_KERNEL_JSON, GAP_DRIFT_JSON]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def fmt_bool(value: Any) -> str:
    """布尔值小写渲染。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格单元转义。"""
    return str(value).replace("|", r"\|")


def build_certificate() -> dict[str, Any]:
    """组装 wheel-gap-lock 证书。"""
    wheel = load_json(WHEEL_RESIDUE_JSON)
    sibling = load_json(SIBLING_KERNEL_JSON)
    gap_drift = load_json(GAP_DRIFT_JSON)

    q_prefix = int(wheel["q_prefix"])
    terminal_q_path = [int(x) for x in sibling["target_signature"]["q_path"]]
    q_spine = [q_prefix, terminal_q_path[0], terminal_q_path[-1]]
    q_mid = q_spine[1]
    q_right = q_spine[2]
    first_gap, second_gap = [int(x) for x in sibling["target_signature"]["q_gap_path"]]
    sibling_gap_path = [int(x) for x in sibling["sibling_signature"]["q_gap_path"]]
    carry_path = [int(x) for x in sibling["target_signature"]["carry_path"]]

    middle_wheel_units = int(wheel["middle_kernel_wheel_units"])
    right_gap_after_lpf = int(wheel["right_gap_after_lpf_peel"])
    wheel_lift_height = int(wheel["actual_wheel_lift_height"])
    primitive_mid_gap = int(wheel["primitive_mid_gap"])
    lpf_threshold = int(gap_drift["lpf_threshold_factor"])
    primitive_right_gap = int(gap_drift["primitive_gap_vector"][1])

    inherited_wheel_residue_closed = (
        wheel.get("terminal_sibling_qspine_wheel_residue_closed") is True
        and wheel.get("terminal_sibling_qspine_wheel_residue_payment_law_proved") is False
    )
    inherited_sibling_signature_closed = (
        sibling.get("terminal_double_awrap_sibling_qspine_kernel_closed") is True
        and sibling.get("same_q_path") is True
        and sibling.get("same_gap_carry") is True
        and sibling_gap_path == [first_gap, second_gap]
    )
    first_gap_lock_closed = first_gap == middle_wheel_units == right_gap_after_lpf
    second_gap_lock_closed = second_gap == wheel_lift_height == first_gap * first_gap
    q_spine_first_gap_generation_closed = q_mid - q_prefix == primitive_mid_gap * first_gap
    q_spine_right_gap_generation_closed = q_right - q_prefix == primitive_right_gap * first_gap
    lpf_right_gap_generation_closed = primitive_right_gap == lpf_threshold * right_gap_after_lpf
    carry_gap_lock_closed = carry_path[0] == first_gap and carry_path[1] == second_gap + 1
    q_spine_generation_closed = q_spine_first_gap_generation_closed and q_spine_right_gap_generation_closed
    reduction_closed = all(
        [
            inherited_wheel_residue_closed,
            inherited_sibling_signature_closed,
            first_gap_lock_closed,
            second_gap_lock_closed,
            q_spine_generation_closed,
            lpf_right_gap_generation_closed,
            carry_gap_lock_closed,
        ]
    )

    latest_open_gate = (
        f"{PIVOT_LAW} AND {GAP_LOCK_LAW} AND {MASS_RATIO_LAW} AND "
        f"{ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING} AND {TRACE_FAMILY} AND {GROUP_ORBIT_INPUT}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_terminal_sibling_qspine_wheel_gap_lock_router",
        "status": "terminal_sibling_qspine_wheel_gap_lock_closed_payment_law_open",
        "verified_date": "2026-05-25",
        "previous_wheel_residue_closed": inherited_wheel_residue_closed,
        "previous_sibling_signature_closed": inherited_sibling_signature_closed,
        "P": int(wheel["P"]),
        "q_prefix": q_prefix,
        "right_side_q_spine": q_spine,
        "terminal_q_path": terminal_q_path,
        "terminal_q_gap_path": [first_gap, second_gap],
        "terminal_carry_path": carry_path,
        "middle_wheel_units": middle_wheel_units,
        "right_gap_after_lpf_peel": right_gap_after_lpf,
        "wheel_lift_height": wheel_lift_height,
        "primitive_mid_gap": primitive_mid_gap,
        "primitive_right_gap": primitive_right_gap,
        "lpf_threshold_factor": lpf_threshold,
        "first_gap_lock_closed": first_gap_lock_closed,
        "second_gap_lock_closed": second_gap_lock_closed,
        "q_spine_first_gap_generation_closed": q_spine_first_gap_generation_closed,
        "q_spine_right_gap_generation_closed": q_spine_right_gap_generation_closed,
        "q_spine_generation_closed": q_spine_generation_closed,
        "lpf_right_gap_generation_closed": lpf_right_gap_generation_closed,
        "carry_gap_lock_closed": carry_gap_lock_closed,
        "gap_lock_identities": {
            "first_gap": f"{first_gap} = {middle_wheel_units} = {right_gap_after_lpf}",
            "second_gap": f"{second_gap} = {wheel_lift_height} = {first_gap}^2",
            "q_mid_generation": f"{q_mid}-{q_prefix} = {primitive_mid_gap}*{first_gap}",
            "q_right_generation": f"{q_right}-{q_prefix} = {primitive_right_gap}*{first_gap} = {lpf_threshold}*{right_gap_after_lpf}*{first_gap}",
            "carry_lock": f"carry_path=[{first_gap},{second_gap}+1]=[{carry_path[0]},{carry_path[1]}]",
        },
        "terminal_sibling_qspine_wheel_gap_lock_closed": reduction_closed,
        "terminal_sibling_qspine_wheel_gap_lock_payment_law_proved": False,
        "admissible_trace_or_typeii_family_constructed": False,
        "finite_group_orbit_expansion_family_constructed": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "latest_open_gate": latest_open_gate,
        "next_primary_attack_target": GAP_LOCK_LAW,
        "gate_rows": [
            {
                "gate": "WheelResidueCarrierImported",
                "closed": inherited_wheel_residue_closed,
                "proved": inherited_wheel_residue_closed,
                "meaning": "上一层 30-wheel residue carrier 已有限闭合，支付律仍未证明。",
                "remaining": "finite wheel-residue ledger",
            },
            {
                "gate": "TerminalDoubleAwrapGapPathImported",
                "closed": inherited_sibling_signature_closed,
                "proved": inherited_sibling_signature_closed,
                "meaning": "m769/m773 的 terminal q-gap/carry path 共同为 [2,4]/[2,5]。",
                "remaining": "finite terminal signature ledger",
            },
            {
                "gate": "FirstGapLock",
                "closed": first_gap_lock_closed,
                "proved": first_gap_lock_closed,
                "meaning": "first terminal gap 同时等于 middle wheel units 与 7-peel 后 right gap。",
                "remaining": "finite first-gap ledger",
            },
            {
                "gate": "SecondGapWheelLiftLock",
                "closed": second_gap_lock_closed,
                "proved": second_gap_lock_closed,
                "meaning": "second terminal gap 等于 wheel lift height，并等于 first gap 的平方。",
                "remaining": "finite second-gap ledger",
            },
            {
                "gate": "QSpineGeneratedByFirstGap",
                "closed": q_spine_generation_closed,
                "proved": q_spine_generation_closed,
                "meaning": "right-side q-spine [439,461,467] 的两条长边由 first terminal gap 生成。",
                "remaining": "finite q-spine generation ledger",
            },
            {
                "gate": "TerminalCarryGapLock",
                "closed": carry_gap_lock_closed,
                "proved": carry_gap_lock_closed,
                "meaning": "carry path [2,5] 锁定为 [first_gap, second_gap+1]。",
                "remaining": "finite carry ledger",
            },
            {
                "gate": "TerminalSiblingQSpineWheelGapLockPaymentLaw",
                "closed": False,
                "proved": False,
                "meaning": "仍需 uniform law 支付或排除该 wheel-gap lock，而不能只在 m773 有限点成立。",
                "remaining": GAP_LOCK_LAW,
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "这是 finite wheel-gap-lock reduction，不是全局奇偶性突破定理。",
                "remaining": f"{PIVOT_LAW} AND {MASS_RATIO_LAW} AND {ORIENTATION_LAW} AND {MOVING_BEATTY_SAVING}",
            },
        ],
        "plain_conclusion": (
            "The 30-wheel residue carrier is locked to the terminal double-Awrap q-gap path: "
            "first_gap=2=middle_kernel/30=right_gap_after_7_peel and "
            "second_gap=4=wheel_lift_height=first_gap^2. The right-side q-spine "
            "[439,461,467] is generated by this first gap. The remaining task is a "
            "uniform wheel-gap-lock payment/exclusion law or PDEC."
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(payload: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix Phi-LPF terminal sibling q-spine wheel-gap-lock 证书",
        "",
        f"**状态：** `{payload['status']}`",
        f"**核验日期：** `{payload['verified_date']}`",
        "",
        "本证书把 30-wheel residue carrier 锁定到 terminal double-Awrap q-gap path。",
        "",
        "```text",
        f"right_side_q_spine={payload['right_side_q_spine']}",
        f"terminal_q_gap_path={payload['terminal_q_gap_path']}",
        f"terminal_carry_path={payload['terminal_carry_path']}",
        f"first_gap_lock_closed={fmt_bool(payload['first_gap_lock_closed'])}",
        f"second_gap_lock_closed={fmt_bool(payload['second_gap_lock_closed'])}",
        f"q_spine_generation_closed={fmt_bool(payload['q_spine_generation_closed'])}",
        f"carry_gap_lock_closed={fmt_bool(payload['carry_gap_lock_closed'])}",
        f"terminal_sibling_qspine_wheel_gap_lock_closed={fmt_bool(payload['terminal_sibling_qspine_wheel_gap_lock_closed'])}",
        f"terminal_sibling_qspine_wheel_gap_lock_payment_law_proved={fmt_bool(payload['terminal_sibling_qspine_wheel_gap_lock_payment_law_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. gap-lock identities",
        "",
        "```text",
    ]
    for identity in payload["gap_lock_identities"].values():
        lines.append(identity)
    lines.extend(
        [
            "```",
            "",
            "## 2. 门控表",
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
        "terminal_sibling_qspine_wheel_gap_lock_closed="
        f"{fmt_bool(payload['terminal_sibling_qspine_wheel_gap_lock_closed'])}"
    )
    print(f"second_gap_lock_closed={fmt_bool(payload['second_gap_lock_closed'])}")
    print(f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
