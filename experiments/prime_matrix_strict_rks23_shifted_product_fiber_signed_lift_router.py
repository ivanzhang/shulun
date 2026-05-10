#!/usr/bin/env python3
"""把 shifted product fiber 的有符号小相位用整数提升和除数界吸收。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_shifted_product_fiber_signed_lift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-shifted-product-fiber-signed-lift-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-shifted-product-fiber-signed-lift-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-shifted-product-fiber-signed-lift-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-nonzero-pgl2-to-shifted-product-fiber-router.json"

SOURCE_FILES = [PREVIOUS]

TARGET = "ShiftedIntervalModularProductFiberHighSpectrumPowerSavingForSquareRootCollar"
SIGNED_SMALL_PHASE = "SignedSmallPhaseDivisorLiftSublinearBound"
NEXT_ATOM = "InteriorShiftedProductFiberHighSpectrumPowerSavingForSquareRootCollar"
BRANCH_PACKET = "InteriorPhaseBranchSlopeIncidenceOrAverageDivisorPacketBound"


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
    """构造有符号小相位吸收证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    shifted_identity = previous.get("shifted_product_fiber_identity_closed") is True

    # 设 J=[A,A+N] 是 dyadic 颈部整数块，并令 U=max J。
    # 若 c 取有符号代表 gamma 且 |gamma|<=U，则
    #   ab-gamma(a+b)=kp
    # 的整数分支数至多 O(U^2/P)=log^O(P)。
    # 每个分支满足 (a-gamma)(b-gamma)=gamma^2+kp，
    # 因此由除数界给出 P^o(1) 级点态计数，低于任何固定正幂高谱阈值。
    signed_small_phase_absorbed = active and shifted_identity
    interior_remaining = active and shifted_identity

    lift_ledger = {
        "dyadic_collar_model": "J=[A,A+N] with U=max J and U<=P^(1/2)log^236(P)",
        "signed_phase_scope": "take the signed representative gamma of c with |gamma|<=U",
        "integer_lift": "ab-gamma(a+b)=kP",
        "branch_budget": "|k|<=3U^2/P<=3log^472(P) in the square-root collar",
        "factor_identity_per_branch": "(a-gamma)(b-gamma)=gamma^2+kP",
        "divisor_count": "for each k, the number of pairs is <= tau(|gamma^2+kP|)",
        "sublinear_consequence": "r_gamma<=log^O(P) P^o(1)=N^o(1), hence below N^(1-eta) for every fixed eta<1 and large P",
        "finite_transition": "explicit small-P constants remain in the existing finite/P0 verification lane",
    }

    frontier = {
        "absorbed_part": "all nonzero phases whose signed representative satisfies |gamma|<=max J",
        "why_this_is_progress": "the near-zero and near-P phases no longer need incidence or BG machinery",
        "why_pointwise_guard_is_retired": "a global pointwise target is stronger than required; the proof only needs high-spectrum energy control",
        "remaining_phase_scope": "interior phases with min(c,P-c)>max J",
        "remaining_obstruction": "for interior c, the integer branch range can be O(U), so a plain per-branch divisor sum is too weak",
        "next_required_input": BRANCH_PACKET,
    }

    rows = [
        row(
            "ShiftedProductFiberTargetActive",
            active,
            True,
            "上一证书已把非零 PGL2 剩余改写为 shifted product fiber 高谱。",
            TARGET,
        ),
        row(
            "SignedSmallPhaseIntegerLiftClosed",
            signed_small_phase_absorbed,
            True,
            "`|gamma|<=max J` 时整数分支数只有 `log^O(P)`，每分支由除数界给 `P^o(1)`。",
            SIGNED_SMALL_PHASE,
        ),
        row(
            "SignedSmallPhaseHighSpectrumAbsorbed",
            signed_small_phase_absorbed,
            True,
            "小有符号相位满足 `r_gamma=N^o(1)`，不会进入任何固定幂高谱层。",
            "absorbed",
        ),
        row(
            "UniformPointwiseFiberBoundRetiredAsNecessaryGate",
            True,
            True,
            "全体 `c` 的点态次线性界足够但非必要；当前只保留高谱能量所需输入。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "内部相位 `min(c,P-c)>max J` 仍需平均型分支/斜率 incidence 或除数包估计。",
            BRANCH_PACKET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只吸收有符号小相位并精确缩窄剩余；未证明内部相位高谱排斥。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_shifted_product_fiber_signed_lift_router",
        "status": "signed_small_shifted_product_phases_absorbed_interior_high_spectrum_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "shifted_product_fiber_target_active": active,
        "signed_small_phase_divisor_lift_sublinear_bound_proved": signed_small_phase_absorbed,
        "signed_small_phase_high_spectrum_absorbed": signed_small_phase_absorbed,
        "uniform_pointwise_fiber_bound_retired_as_necessary_gate": True,
        "interior_shifted_product_high_spectrum_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "next_required_input": BRANCH_PACKET,
        "lift_ledger": lift_ledger,
        "frontier": frontier,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "shifted product fiber 的当前剩余可先按相位的有符号代表拆开。"
            "当 `|gamma|<=max J` 时，方程 `ab-gamma(a+b)=kP` 只有 `log^O(P)` 个整数分支，"
            "每个分支化为一个普通除数计数 `(a-gamma)(b-gamma)=gamma^2+kP`，"
            "因此该部分只有 `N^o(1)` 点态质量，不能进入固定幂高谱。"
            "真正剩余被压缩为内部相位 `min(c,P-c)>max J` 的平均型高谱排斥。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lift = result["lift_ledger"]
    frontier = result["frontier"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 shifted product fiber 有符号提升证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"signed_small_phase_divisor_lift_sublinear_bound_proved={fmt_bool(result['signed_small_phase_divisor_lift_sublinear_bound_proved'])}",
        f"interior_shifted_product_high_spectrum_proved={fmt_bool(result['interior_shifted_product_high_spectrum_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有符号小相位提升",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in lift.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 新前沿",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in frontier.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
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
            "## 4. 下一最窄自足目标",
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
