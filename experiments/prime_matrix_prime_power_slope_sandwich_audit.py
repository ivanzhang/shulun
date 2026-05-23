#!/usr/bin/env python3
"""Prime-power slope sandwich audit.

用法示例：
  python3 experiments/prime_matrix_prime_power_slope_sandwich_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-prime-power-slope-sandwich-audit.json

本证书审计用户提出的指数夹击：
  (P^(50/24))^0.52 与 (P^(50/26))^0.52
是否能推出中心 (P^(50/25))^0.5=P 半窗素数存在。

核心结论：指数长度出现 P 的算术巧合，但短区间容器的位置远离 P^2；
要同时满足“中心在 P^2”和“半径为 P”，仍等价要求 theta=1/2。
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

SLUG = "prime-matrix-prime-power-slope-sandwich"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
THETA = Fraction(13, 25)
CENTER_EXPONENT = Fraction(50, 25)
LOWER_EXPONENT = Fraction(50, 26)
UPPER_EXPONENT = Fraction(50, 24)

DEPENDENCIES = [
    DOCS / "prime-matrix-prime-square-pm1-sandwich-audit.json",
    DOCS / "prime-matrix-prime-square-halfscale-specialization-audit.json",
    DOCS / "prime-matrix-short-interval-transference-parity-audit.json",
    DOCS / "prime-matrix-almost-all-exceptional-spine-audit.json",
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


def frac_text(value: Fraction) -> str:
    """输出分数字符串。"""
    return f"{value.numerator}/{value.denominator}"


def p_power(value: Fraction) -> str:
    """输出 P 的幂。"""
    if value.denominator == 1:
        return f"P^{value.numerator}"
    return f"P^({value.numerator}/{value.denominator})"


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def endpoint_record(label: str, exponent: Fraction) -> dict[str, Any]:
    """登记端点位置、短区间半径和到 P^2 的距离尺度。"""
    radius_exp = exponent * THETA
    if exponent < CENTER_EXPONENT:
        side = "below_P2"
        gap_exp = CENTER_EXPONENT
        gap_shape = "P^2-P^a = P^2(1-P^(a-2))"
    elif exponent > CENTER_EXPONENT:
        side = "above_P2"
        gap_exp = exponent
        gap_shape = "P^a-P^2 = P^a(1-P^(2-a))"
    else:
        side = "at_P2"
        gap_exp = Fraction(0, 1)
        gap_shape = "0"
    return {
        "label": label,
        "endpoint": f"P^({frac_text(exponent)})",
        "endpoint_exponent": frac_text(exponent),
        "theta": frac_text(THETA),
        "guaranteed_radius": p_power(radius_exp),
        "radius_exponent": frac_text(radius_exp),
        "side": side,
        "distance_to_p2_scale": "0" if exponent == CENTER_EXPONENT else p_power(gap_exp),
        "gap_shape": gap_shape,
        "radius_reaches_p2": False if exponent != CENTER_EXPONENT else radius_exp >= 1,
    }


def build_payload() -> dict[str, Any]:
    """构造审计 payload。"""
    lower_radius = LOWER_EXPONENT * THETA
    upper_radius = UPPER_EXPONENT * THETA
    return {
        "certificate_type": "prime_matrix_prime_power_slope_sandwich_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "prime_power_slope_sandwich_has_length_coincidence_but_misses_p2_location",
        "user_question": "Can (P^(50/24))^0.52 and (P^(50/26))^0.52 sandwich (P^(50/25))^0.5?",
        "short_answer": "no: P^(50/26) gives radius P but is far below P^2, while P^(50/24) is far above P^2 and its radius is still too small to reach P^2",
        "external_input": {
            "source": "Runbo Li arXiv:2308.04458 v8 / latest 0.52 short-interval preprint stream",
            "shape": "prime in intervals of length x^0.52 for sufficiently large x",
            "theta": "13/25",
            "status_in_project": "preprint/frontier input; even granting it, this sandwich does not close halfscale",
        },
        "exponent_identity": {
            "theta": frac_text(THETA),
            "lower_endpoint_exponent": frac_text(LOWER_EXPONENT),
            "center_endpoint_exponent": frac_text(CENTER_EXPONENT),
            "upper_endpoint_exponent": frac_text(UPPER_EXPONENT),
            "lower_radius_exponent": frac_text(lower_radius),
            "center_halfscale_exponent": "1",
            "upper_radius_exponent": frac_text(upper_radius),
            "lower_radius_equals_p": lower_radius == 1,
            "center_is_p_square": CENTER_EXPONENT == 2,
            "upper_radius": p_power(upper_radius),
            "target_halfscale": "P",
        },
        "endpoint_records": [
            endpoint_record("lower_X=P^(50/26)=P^(25/13)", LOWER_EXPONENT),
            endpoint_record("center_X=P^(50/25)=P^2", CENTER_EXPONENT),
            endpoint_record("upper_X=P^(50/24)=P^(25/12)", UPPER_EXPONENT),
        ],
        "location_radius_obstruction": {
            "lower_gap_to_center": "P^2-P^(25/13)=P^2(1-P^(-1/13)) asymp P^2",
            "lower_guaranteed_radius": "P",
            "lower_gap_over_radius": "asymp P",
            "upper_gap_to_center": "P^(25/12)-P^2=P^2(P^(1/12)-1) asymp P^(25/12)",
            "upper_guaranteed_radius": "P^(13/12)",
            "upper_gap_over_radius": "asymp P",
            "conclusion": "both guaranteed containers are a factor P too far from P^2 in the power scale",
        },
        "general_gate": {
            "require_location": "a=2 for X=P^2",
            "require_radius_p": "a*theta=1",
            "simultaneous_solution_requires": "theta=1/2",
            "with_theta_13_over_25": "a=25/13 gives radius P but not location P^2",
            "closes_halfscale": False,
        },
        "decision_gates": [
            {
                "gate": "ExponentLengthCoincidenceRecognized",
                "closed": True,
                "proved": True,
                "meaning": "(P^(50/26))^(13/25)=P and (P^2)^(1/2)=P",
                "remaining": "location mismatch",
            },
            {
                "gate": "LowerContainerTouchesP2",
                "closed": False,
                "proved": False,
                "meaning": "the lower container has length P but lies around P^(25/13), far below P^2",
                "remaining": "P2MinusLowerEndpointGapExclusion",
            },
            {
                "gate": "UpperContainerTouchesP2",
                "closed": False,
                "proved": False,
                "meaning": "the upper container lies around P^(25/12), far above P^2; radius P^(13/12) is too small",
                "remaining": "UpperEndpointGapToP2Bridge",
            },
            {
                "gate": "SandwichForcesPrimeIntoP2HalfWindow",
                "closed": False,
                "proved": False,
                "meaning": "two far-away existence intervals do not imply existence in (P^2,P^2+P] or [P^2-P,P^2)",
                "remaining": "PrimeSquareEndpointLocalization",
            },
            {
                "gate": "RowColumnUnconditionalClosureReached",
                "closed": False,
                "proved": False,
                "meaning": "external lemma and internal self-contained versions remain open",
                "remaining": "row_column_unconditional_closed=false",
            },
        ],
        "new_residual_basis": [
            "PrimeSquareEndpointLocalizationNotExponentInterpolation",
            "ThetaEqualsHalfOrPrimeSquareSpecificPointwiseTheorem",
            "P2CenteredContainerPrimeLowerBound",
            "OuterScaleGapBridgeBetweenP25Over13AndP2",
            "SameObjectSignedDispersionOrAutomorphicEndpointProof",
        ],
        "prime_power_slope_sandwich_no_go_closed": True,
        "exponent_length_coincidence_closed": True,
        "lower_container_reaches_p2": False,
        "upper_container_reaches_p2": False,
        "prime_square_halfscale_closed": False,
        "row_column_unconditional_closed": False,
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "source_hashes": source_hashes(),
    }


def table(rows: list[dict[str, Any]], columns: list[str]) -> str:
    """生成 Markdown 表。"""
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        values = []
        for col in columns:
            value = row.get(col, "")
            if isinstance(value, bool):
                value = bool_text(value)
            values.append(str(value).replace("|", r"\|"))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 审计文档。"""
    identity = payload["exponent_identity"]
    obstruction = payload["location_radius_obstruction"]
    gate = payload["general_gate"]
    lines = [
        "# Prime-Power Slope Sandwich Audit",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 直接回答",
        "",
        "不能。`(P^(50/26))^0.52=P` 的确给出长度巧合，",
        "但该短区间位于 `P^(25/13)` 附近，距离 `P^2` 仍为 `asymp P^2`。",
        "`P^(50/24)` 位于 `P^2` 之上更远处，其 `0.52` 半径也只到 `P^(13/12)`，",
        "同样无法触及 `P^2` 半窗。",
        "",
        "## 2. 指数恒等式",
        "",
        "```text",
        f"theta={identity['theta']}",
        f"lower_endpoint=P^({identity['lower_endpoint_exponent']})",
        f"center_endpoint=P^({identity['center_endpoint_exponent']})=P^2",
        f"upper_endpoint=P^({identity['upper_endpoint_exponent']})",
        f"lower_radius_exponent={identity['lower_radius_exponent']}",
        f"upper_radius_exponent={identity['upper_radius_exponent']}",
        f"target_halfscale={identity['target_halfscale']}",
        "```",
        "",
        "## 3. 端点容器",
        "",
        table(
            payload["endpoint_records"],
            ["label", "endpoint", "guaranteed_radius", "side", "distance_to_p2_scale", "radius_reaches_p2"],
        ),
        "",
        "## 4. 位置-半径不相容",
        "",
        "```text",
        f"lower_gap_to_center={obstruction['lower_gap_to_center']}",
        f"lower_guaranteed_radius={obstruction['lower_guaranteed_radius']}",
        f"lower_gap_over_radius={obstruction['lower_gap_over_radius']}",
        f"upper_gap_to_center={obstruction['upper_gap_to_center']}",
        f"upper_guaranteed_radius={obstruction['upper_guaranteed_radius']}",
        f"upper_gap_over_radius={obstruction['upper_gap_over_radius']}",
        "```",
        "",
        obstruction["conclusion"],
        "",
        "一般地，若 `X=P^a`，则通用 `X^theta` 定理给长度 `P^(a theta)`。",
        "要中心在 `P^2` 必须 `a=2`；要长度为 `P` 必须 `a theta=1`。",
        "二者同时成立等价于 `theta=1/2`。",
        "",
        "```text",
        f"require_location={gate['require_location']}",
        f"require_radius_p={gate['require_radius_p']}",
        f"simultaneous_solution_requires={gate['simultaneous_solution_requires']}",
        f"with_theta_13_over_25={gate['with_theta_13_over_25']}",
        f"closes_halfscale={bool_text(gate['closes_halfscale'])}",
        "```",
        "",
        "## 5. 判定表",
        "",
        table(payload["decision_gates"], ["gate", "closed", "proved", "meaning", "remaining"]),
        "",
        "## 6. 新剩余基",
        "",
        "```text",
        *payload["new_residual_basis"],
        "```",
        "",
        "## 7. 边界声明",
        "",
        "```text",
        f"prime_power_slope_sandwich_no_go_closed={bool_text(payload['prime_power_slope_sandwich_no_go_closed'])}",
        f"exponent_length_coincidence_closed={bool_text(payload['exponent_length_coincidence_closed'])}",
        f"lower_container_reaches_p2={bool_text(payload['lower_container_reaches_p2'])}",
        f"upper_container_reaches_p2={bool_text(payload['upper_container_reaches_p2'])}",
        f"prime_square_halfscale_closed={bool_text(payload['prime_square_halfscale_closed'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    """写出证书、账本和 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("prime_power_slope_sandwich_no_go_closed=true")
    print("prime_square_halfscale_closed=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
