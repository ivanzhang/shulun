#!/usr/bin/env python3
"""审计 z=61 dyadic lift companion 的自足闭合边界。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_companion_boundary_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
PREFIX_BALANCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.json"
SHIFTED_FACTOR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json"
SQUARE_WINDOW_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
POSITIVE_SHIFTED_BRIDGE_JSON = (
    DOCS / "prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json"
)
FIXED_CYCLE_COMPARATOR_JSON = (
    DOCS / "prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.json"
)
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.md"

NEXT_TARGET = "IndependentShiftedSquareWindowInputOrPersistentPhasePDECExclusion"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-signed-balance-router.json",
    "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json",
    "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json",
    "prime-matrix-square-phase-lowalpha-z61-positive-lift-shifted-pair-bridge-router.json",
    "prime-matrix-square-phase-lowalpha-z61-fixed-core-cycle-nonpersistence-comparator.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_dyadic_companion_boundary_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        result[f"docs/monograph/{name}"] = file_sha256(DOCS / name)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def audit() -> dict[str, Any]:
    """执行 companion 闭合边界审计。"""
    balance = load(PREFIX_BALANCE_JSON)
    shifted = load(SHIFTED_FACTOR_JSON)
    square = load(SQUARE_WINDOW_JSON)
    bridge = load(POSITIVE_SHIFTED_BRIDGE_JSON)
    comparator = load(FIXED_CYCLE_COMPARATOR_JSON)

    shifted_row = shifted["shifted_factor_rows"][0]
    square_row = square["square_window_rows"][0]
    local_companion_closed = (
        balance["prefix_gate_signed_phase_balance_closed_for_sample"]
        and balance["positive_dyadic_lift_companion_closed_for_sample"]
        and shifted["all_endpoint_shifted_factor_groups_closed"]
        and square["all_shifted_square_window_groups_closed"]
        and bridge["positive_lift_shifted_pair_bridge_closed_for_sample"]
    )

    global_inputs = {
        "dyadic_lift_companion_proved_globally": balance["dyadic_lift_companion_proved_globally"],
        "shifted_linear_prime_pair_global_bound_proved": shifted[
            "shifted_linear_prime_pair_global_bound_proved"
        ],
        "shifted_square_window_global_bound_proved": square[
            "shifted_square_window_global_bound_proved"
        ],
        "positive_dyadic_lift_existence_proved_globally": bridge[
            "positive_dyadic_lift_existence_proved_globally"
        ],
        "persistent_phase_pdec_excluded": comparator["persistent_phase_pdec_excluded"],
        "missing_lift_pdec_excluded": bridge["missing_lift_pdec_excluded"],
    }
    self_contained_closed = all(global_inputs.values())

    obstruction_formula = {
        "phase_modulus": balance["phase_modulus"],
        "negative_anchor": {
            "quotient": 1,
            "condition": "one negative phase hit of weight w",
        },
        "required_positive_companion": {
            "quotients": [2, 4],
            "same_p": balance["positive_same_p"],
            "carry_equation": balance["positive_same_p_semiprime_carry_equation"],
            "linear_forms": shifted_row["linear_prime_pair_forms"],
            "square_window": {
                "M": square_row["base_modulus"],
                "p": square_row["p"],
                "delta": square_row["delta_low"],
                "congruence": f"p^2 ≡ {-square_row['delta_low']} mod {square_row['base_modulus']}",
                "window": (
                    "delta + M*span <= p-1 < delta + M*(span+1)"
                ),
                "recovered_s": square_row["s_recovered_from_square_window"],
            },
        },
    }

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_dyadic_companion_boundary_router",
        "status": "z61_dyadic_companion_boundary_requires_independent_square_window_input_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "target_bucket": balance["target_bucket"],
        "target_omega": balance["target_omega"],
        "target_shell": balance["target_shell"],
        "local_dyadic_companion_equivalence_closed": local_companion_closed,
        "obstruction_formula": obstruction_formula,
        "global_inputs": global_inputs,
        "all_required_global_inputs_available": self_contained_closed,
        "self_contained_row_column_closure_reached": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "dyadic lift companion 的局部等价链已经闭合，但仓库内尚无独立的全局输入："
            "`ShiftedLinearPrimePairGlobalBound`、`ShiftedSquareWindowGlobalBound`、"
            "`dyadic_lift_companion_proved_globally` 与 `PersistentPhase/MissingLift-PDEC` "
            "排斥均未完成。因而当前自足路线的真正闭合边界是：提交独立 shifted-square-window "
            "全局输入，或排斥该命名持久相位 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    obs = result["obstruction_formula"]
    req = obs["required_positive_companion"]
    square = req["square_window"]
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 dyadic companion boundary",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"local_dyadic_companion_equivalence_closed={fmt_bool(result['local_dyadic_companion_equivalence_closed'])}",
        f"all_required_global_inputs_available={fmt_bool(result['all_required_global_inputs_available'])}",
        f"self_contained_row_column_closure_reached={fmt_bool(result['self_contained_row_column_closure_reached'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Companion 公式",
        "",
        "| object | value |",
        "| --- | --- |",
        f"| phase modulus | `{obs['phase_modulus']}` |",
        f"| negative anchor | `{obs['negative_anchor']}` |",
        f"| positive quotients | `{req['quotients']}` |",
        f"| same-p | `{req['same_p']}` |",
        f"| carry equation | `{req['carry_equation']}` |",
        f"| linear forms | `{req['linear_forms']}` |",
        f"| square congruence | `{square['congruence']}` |",
        f"| square window | `{square['window']}` |",
        f"| recovered s | `{square['recovered_s']}` |",
        "",
        "## 2. 全局输入验收",
        "",
        "| input | available |",
        "| --- | --- |",
    ]
    for name, value in result["global_inputs"].items():
        lines.append(f"| `{name}` | {fmt_bool(value)} |")
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：当前 formal unit 的 dyadic companion 局部等价链。",
            "- 未闭合：独立 shifted-square-window/shifted-prime-pair 全局输入，或命名 PersistentPhase/MissingLift-PDEC 排斥。",
            "- 结论：不能据此宣称行/列命题无条件闭合。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "local_dyadic_companion_equivalence_closed": result[
                    "local_dyadic_companion_equivalence_closed"
                ],
                "all_required_global_inputs_available": result[
                    "all_required_global_inputs_available"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
