#!/usr/bin/env python3
"""压缩 RKS2/RKS3 大包分支的 Burgess 点态角色和输入。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_burgess_pointwise_internalization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-burgess-pointwise-internalization-router.json
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-burgess-pointwise-internalization-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-burgess-pointwise-internalization-router.md"

THRESHOLD = MONO / "prime-matrix-strict-rks23-character-moment-burgess-threshold-router.json"
THIN_CLOSURE = MONO / "prime-matrix-strict-rks23-registered-endpoint-side-cauchy-floor-router.json"
SOURCE_FILES = [THRESHOLD, THIN_CLOSURE]

TARGET = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"
GLOBAL_GATE = "BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment"
INTERNAL_PROOF_ATOM = "SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants"
MOMENT_WEIL_ATOM = "BurgessAmplificationMomentWeilLedgerForLargeDyadicIntervals"


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


def burgess_delta(epsilon: Fraction) -> tuple[int, Fraction]:
    """给定 epsilon，选 r 使 Burgess 指数产生固定幂节省。"""
    r = int(1 / (4 * epsilon)) + 1
    while Fraction(1, 4 * r) >= epsilon:
        r += 1
    delta = (epsilon - Fraction(1, 4 * r)) / r
    return r, delta


def optimization_table() -> list[dict[str, str]]:
    """生成若干 epsilon 的参数账本，验证 delta_B>0。"""
    epsilons = [Fraction(1, 16), Fraction(1, 32), Fraction(1, 64), Fraction(1, 100)]
    rows = []
    for epsilon in epsilons:
        r, delta = burgess_delta(epsilon)
        rows.append(
            {
                "epsilon_B": f"{epsilon.numerator}/{epsilon.denominator}",
                "chosen_r": str(r),
                "delta_B": f"{delta.numerator}/{delta.denominator}",
                "positive": fmt_bool(delta > 0),
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 Burgess 点态输入内部化边界证书。"""
    threshold = load_json(THRESHOLD)
    thin = load_json(THIN_CLOSURE)

    target_active = (
        thin.get("next_direct_attack_target") == TARGET
        and thin.get("thin_dyadic_packet_mass_absorption_proved") is True
        and thin.get("burgess_pointwise_input_still_open") is True
    )
    large_implication_ready = threshold.get("burgess_large_packet_implication_closed") is True
    thin_branch_closed = thin.get("thin_dyadic_packet_mass_absorption_proved") is True

    # 经典 Burgess 定理本身不在此步内部证明；这里闭合的是“所需输入与经典定理”的严格匹配。
    classical_burgess_statement_matches = target_active and large_implication_ready
    parameter_ledger_closed = classical_burgess_statement_matches
    external_burgess_sufficient = classical_burgess_statement_matches and thin_branch_closed

    burgess_internalized = False
    global_gate_closed_author_side = burgess_internalized and thin_branch_closed

    needed_pointwise_input = {
        "modulus": "prime P",
        "character": "nonprincipal multiplicative character chi mod P; for prime P it is primitive",
        "interval": "any consecutive interval I in a dyadic packet; a wrapping interval splits into at most two ordinary intervals",
        "length_condition": "|I|>=P^(1/4+epsilon_B)",
        "required_bound": "|sum_{n in I} chi(n)| <= |I| P^(-delta_B)",
        "uniformity": "epsilon_B fixed; constants may depend on epsilon_B but not on P, chi, or the dyadic packet",
    }

    classical_burgess_interface = {
        "standard_form": "|S_I(chi)| <= C_r H^(1-1/r) P^((r+1)/(4r^2)) up to harmless log/P^o(1) loss",
        "choice_of_r": "choose integer r with 1/(4r)<epsilon_B",
        "saving_exponent": "if H>=P^(1/4+epsilon_B), then |S|/H <= C_r P^{-(epsilon_B-1/(4r))/r+o(1)}",
        "delta_choice": "after absorbing C_r and polylog losses for large P, take any delta_B < (epsilon_B-1/(4r))/r",
        "dyadic_packet_match": "packet intervals are ordinary intervals after at most a two-piece split, so the same bound applies",
        "large_branch_consequence": "four large sides give the character-moment saving already registered by the Burgess-threshold router",
    }

    internalization_frontier = {
        "B1_interval_completion_and_translation": "elementary normalization; must be written with endpoint/wrap constants",
        "B2_vinogradov_shift_amplification": "needs a self-contained lemma with A,B,r parameters and no hidden range loss",
        "B3_amplified_moment_energy_ledger": "needs the exact 2r-th moment expansion and collision-count bound",
        "B4_weil_complete_rational_sum_kernel": "needs the complete character-sum bound for non-perfect-power rational functions",
        "B5_parameter_optimization_and_dyadic_uniformity": "the exponent algebra is closed here; constants still depend on B2-B4",
    }

    next_attack_order = [
        "B4_weil_complete_rational_sum_kernel",
        "B2_vinogradov_shift_amplification",
        "B3_amplified_moment_energy_ledger",
        "B1_interval_completion_and_translation",
        "B5_parameter_optimization_and_dyadic_uniformity",
    ]

    rows = [
        row(
            "BurgessPointwiseTargetActive",
            target_active,
            True,
            "薄包分支已闭合，最新全局剩余确认为大包 Burgess 点态角色和输入。",
            TARGET,
        ),
        row(
            "NeededInputMatchesClassicalBurgessPrimeModulus",
            classical_burgess_statement_matches,
            True,
            "所需输入正是素模非主角色在长度 `P^(1/4+epsilon_B)` 以上区间的经典 Burgess 点态节省。",
            "classical Burgess theorem",
        ),
        row(
            "BurgessExponentOptimizationLedgerClosed",
            parameter_ledger_closed,
            True,
            "由经典 Burgess 形式选择 `1/(4r)<epsilon_B` 可得到固定正的 `delta_B`。",
            "closed algebra",
        ),
        row(
            "ExternalClassicalBurgessWouldCloseRKS23LargeBranch",
            external_burgess_sufficient,
            True,
            "若接受经典 Burgess 定理作为外部已证定理，则大包分支与已闭合薄包分支合并后闭合 RKS23 角色矩门。",
            "external theorem acceptance",
        ),
        row(
            "BurgessProofComponentsInternalized",
            burgess_internalized,
            burgess_internalized,
            "仓库内尚未把 Burgess 的放大、矩估计与 Weil 完全和证明逐项写成自足证明。",
            INTERNAL_PROOF_ATOM,
        ),
        row(
            TARGET,
            burgess_internalized,
            burgess_internalized,
            "作者侧完全自足闭合仍需完成经典 Burgess 证明组件账本。",
            MOMENT_WEIL_ATOM,
        ),
        row(
            GLOBAL_GATE,
            global_gate_closed_author_side,
            global_gate_closed_author_side,
            "薄包已闭合；无外部 Burgess 或内部 Burgess 证明前，作者侧不声明该门无条件闭合。",
            TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只完成 Burgess 输入的严格匹配和内部化边界压缩，不声明行/列命题无条件闭合。",
            TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_burgess_pointwise_internalization_router",
        "status": "burgess_pointwise_input_strictly_matched_to_classical_burgess_internalization_frontier",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "burgess_pointwise_target_active": target_active,
        "thin_dyadic_packet_mass_absorption_proved": thin_branch_closed,
        "burgess_large_packet_implication_closed": large_implication_ready,
        "needed_input_matches_classical_burgess_prime_modulus": classical_burgess_statement_matches,
        "burgess_exponent_optimization_ledger_closed": parameter_ledger_closed,
        "external_classical_burgess_would_close_rks23_large_branch": external_burgess_sufficient,
        "burgess_pointwise_input_internalized": burgess_internalized,
        "rks23_character_moment_closed_under_external_burgess": external_burgess_sufficient,
        "rks23_character_moment_closed_author_side_self_contained": global_gate_closed_author_side,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": INTERNAL_PROOF_ATOM,
        "next_atomic_attack_target": MOMENT_WEIL_ATOM,
        "needed_pointwise_input": needed_pointwise_input,
        "classical_burgess_interface": classical_burgess_interface,
        "internalization_frontier": internalization_frontier,
        "next_attack_order": next_attack_order,
        "optimization_table": optimization_table(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前唯一内部自足线的真正剩余已精确压缩为经典 Burgess 点态角色和证明的内部化。"
            "所需大包输入与素模经典 Burgess 定理严格匹配：对任意非主角色和长度 "
            "`H>=P^(1/4+epsilon_B)` 的区间，Burgess 形式经 `1/(4r)<epsilon_B` 的参数选择给出 "
            "`|S|<=H P^(-delta_B)`。因此若接受经典 Burgess 作为外部已证定理，RKS23 大包与已闭合薄包可合并闭合；"
            "若要求作者侧完全自足，剩余不再是含糊的角色矩黑箱，而是 Burgess 放大、2r 矩能量账本、"
            "Weil 完全有理函数角色和界，以及区间/常数统一性的内部证明包。行/列命题仍未在作者侧无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 Burgess 点态输入内部化边界证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"burgess_pointwise_target_active={fmt_bool(result['burgess_pointwise_target_active'])}",
        f"thin_dyadic_packet_mass_absorption_proved={fmt_bool(result['thin_dyadic_packet_mass_absorption_proved'])}",
        f"needed_input_matches_classical_burgess_prime_modulus={fmt_bool(result['needed_input_matches_classical_burgess_prime_modulus'])}",
        f"burgess_exponent_optimization_ledger_closed={fmt_bool(result['burgess_exponent_optimization_ledger_closed'])}",
        f"external_classical_burgess_would_close_rks23_large_branch={fmt_bool(result['external_classical_burgess_would_close_rks23_large_branch'])}",
        f"burgess_pointwise_input_internalized={fmt_bool(result['burgess_pointwise_input_internalized'])}",
        f"rks23_character_moment_closed_author_side_self_contained={fmt_bool(result['rks23_character_moment_closed_author_side_self_contained'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 所需输入",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["needed_pointwise_input"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 经典 Burgess 对接",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["classical_burgess_interface"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 参数账本",
            "",
            "| epsilon_B | chosen_r | delta_B | positive |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["optimization_table"]:
        lines.append(
            f"| `{item['epsilon_B']}` | `{item['chosen_r']}` | `{item['delta_B']}` | `{item['positive']}` |"
        )

    lines.extend(
        [
            "",
            "## 4. 完全自足剩余",
            "",
            "| atom | status |",
            "| --- | --- |",
        ]
    )
    for key, value in result["internalization_frontier"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 5. 判定表",
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
            "## 6. 下一最窄攻击顺序",
            "",
            "```text",
            "\n".join(result["next_attack_order"]),
            "```",
            "",
            "审稿边界：本证书闭合的是 Burgess 输入与经典定理形式的匹配和指数账本；",
            "它不把经典 Burgess 证明本身登记为仓库内部自足证明。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
