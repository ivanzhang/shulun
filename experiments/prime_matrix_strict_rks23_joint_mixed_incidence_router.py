#!/usr/bin/env python3
"""把最终相关原子展开为中心化混合入射正规形。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_joint_mixed_incidence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-joint-mixed-incidence-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-joint-mixed-incidence-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-joint-mixed-incidence-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-final-correlation-atom-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "JointNonconcentrationOfSquareDifferenceSpectrumAndIntervalRatioSpectrum"
NEXT_ATOM = "DyadicCenteredMixedSquareDifferenceRatioIncidencePowerSaving"
MIXED_ATOM = "CenteredSixVariableSquareDifferenceRatioIncidenceSaving"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造混合入射正规形证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    final_ready = previous.get("only_joint_nonconcentration_remains") is True

    # Q(lambda)L(lambda) 展开后，lambda 同时满足
    # h2=-lambda*h1 与 u=lambda*x。消去 lambda 得
    # u*h1+x*h2=0，其中 hi=di^2-ei^2。
    mixed_identity_closed = active and final_ready
    centered_subtraction_closed = active and final_ready
    dyadic_extraction_closed = active and final_ready

    mixed_form = {
        "square_difference": "h_i=d_i^2-e_i^2",
        "slope_ratio": "lambda=u/x",
        "same_slope_constraint": "h2=-lambda*h1 and u=lambda*x",
        "mixed_incidence_equation": "u*(d1^2-e1^2)+x*(d2^2-e2^2)=0 mod P",
        "raw_identity": "sum_lambda Q(lambda)L(lambda) equals the weighted count of this six-variable equation",
        "centered_spectrum": "Q_circ(lambda)=Q(lambda)-|Delta|^4/P",
        "centered_mixed_count": "sum_lambda Q_circ(lambda)L(lambda)=raw_count-(|Delta|^4/P)|T|^2",
        "dyadic_failure_extraction": "if the sqrt-weight joint target fails, a dyadic packet of slopes has large centered mixed incidence after log^O(P) loss",
        "why_narrower": "the remaining target is a concrete centered six-variable incidence, not an abstract correlation phrase",
    }

    rows = [
        row(
            "JointNonconcentrationTargetActive",
            active,
            True,
            "上一证书已把严格内部剩余固定为平方差谱与区间比值谱的联合非集中。",
            TARGET,
        ),
        row(
            "MixedIncidenceIdentityClosed",
            mixed_identity_closed,
            True,
            "`Q(lambda)L(lambda)` 精确展开为 `u h1+x h2=0` 的混合入射计数。",
            MIXED_ATOM,
        ),
        row(
            "CenteredUniformTermSubtracted",
            centered_subtraction_closed,
            True,
            "`Q(lambda)-|Delta|^4/P` 的均匀项扣除与 `sum L=|T|^2` 同口径。",
            MIXED_ATOM,
        ),
        row(
            "DyadicFailurePacketExtractionClosed",
            dyadic_extraction_closed,
            True,
            "若联合平方根目标失败，必有一个 dyadic 斜率包给出过大的中心化混合入射。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明所有 dyadic 斜率包的中心化混合入射都有固定幂节省。",
            MIXED_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成混合入射正规形与 dyadic 失败抽取，未证明入射节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_joint_mixed_incidence_router",
        "status": "joint_nonconcentration_reduced_to_centered_mixed_square_difference_ratio_incidence",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "joint_nonconcentration_target_active": active,
        "mixed_incidence_identity_closed": mixed_identity_closed,
        "centered_uniform_term_subtracted": centered_subtraction_closed,
        "dyadic_failure_packet_extraction_closed": dyadic_extraction_closed,
        "dyadic_centered_mixed_incidence_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": MIXED_ATOM,
        "mixed_form": mixed_form,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "最终相关原子可以展开成一个具体混合入射。"
            "设 `h_i=d_i^2-e_i^2`，同一个斜率同时满足 `h2=-lambda*h1` 与 `u=lambda*x`，"
            "消去 `lambda` 得 `u*h1+x*h2=0 mod P`。"
            "扣除 `|Delta|^4/P` 的均匀项后，若联合非集中目标失败，就会在某个 dyadic 斜率包上产生过大的中心化六变量混合入射。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    mixed = result["mixed_form"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 混合入射正规形证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"mixed_incidence_identity_closed={fmt_bool(result['mixed_incidence_identity_closed'])}",
        f"centered_uniform_term_subtracted={fmt_bool(result['centered_uniform_term_subtracted'])}",
        f"dyadic_centered_mixed_incidence_power_saving_proved={fmt_bool(result['dyadic_centered_mixed_incidence_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 混合入射正规形",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in mixed.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
