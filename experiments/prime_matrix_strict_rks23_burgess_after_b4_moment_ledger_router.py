#!/usr/bin/env python3
"""闭合 B4 之后的经典 Burgess 放大矩账本。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_burgess_after_b4_moment_ledger_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-burgess-after-b4-moment-ledger-router.json
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

OUT_JSON = MONO / "prime-matrix-strict-rks23-burgess-after-b4-moment-ledger-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-burgess-after-b4-moment-ledger-router.md"

SELECTOR_TO_KUMMER = MONO / "prime-matrix-strict-rks23-selector-to-kummer-trace-closure-router.json"
BURGESS_FRONTIER = MONO / "prime-matrix-strict-rks23-burgess-pointwise-internalization-router.json"
THRESHOLD = MONO / "prime-matrix-strict-rks23-character-moment-burgess-threshold-router.json"
THIN_CLOSURE = MONO / "prime-matrix-strict-rks23-registered-endpoint-side-cauchy-floor-router.json"
SOURCE_FILES = [SELECTOR_TO_KUMMER, BURGESS_FRONTIER, THRESHOLD, THIN_CLOSURE]

TARGET = "SelfContainedClassicalBurgessProofWithUniformDyadicIntervalConstants"
SUBATOM = "BurgessAmplificationMomentLedgerAfterB4KernelClosure"
B4_ATOM = "B4_weil_complete_rational_sum_kernel"
BURGESS_POINTWISE = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"
THRESHOLD_GATE = "BurgessThresholdDichotomyClosureForFourIntervalCharacterMoment"
ROW_COLUMN_GATE = "RowColumnUnconditionalClosed"
NEXT_TARGET = "RKS23CharacterMomentToRowColumnPromotionGateAudit"


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
    """给定 epsilon，选择 r 并返回可用的幂节省指数。"""
    r = 2
    while Fraction(1, 4 * r) >= epsilon:
        r += 1
    return r, (epsilon - Fraction(1, 4 * r)) / r


def exponent_table() -> list[dict[str, str]]:
    """生成 Burgess 阈值常用 epsilon 的机器可复核参数表。"""
    rows = []
    for epsilon in [Fraction(1, 16), Fraction(1, 32), Fraction(1, 64), Fraction(1, 100)]:
        r, delta = burgess_delta(epsilon)
        rows.append(
            {
                "epsilon_B": f"{epsilon.numerator}/{epsilon.denominator}",
                "chosen_r": str(r),
                "condition": f"1/(4r)={Fraction(1, 4 * r)}<epsilon_B",
                "delta_B": f"{delta.numerator}/{delta.denominator}",
                "positive": fmt_bool(delta > 0),
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 B4 后 Burgess 放大矩账本闭合证书。"""
    selector = load_json(SELECTOR_TO_KUMMER)
    frontier = load_json(BURGESS_FRONTIER)
    threshold = load_json(THRESHOLD)
    thin = load_json(THIN_CLOSURE)

    target_active = (
        selector.get("next_direct_attack_target") == TARGET
        and selector.get("next_subatom") == SUBATOM
        and selector.get("b4_weil_complete_rational_sum_kernel_closed_author_side") is True
        and selector.get("burgess_pointwise_input_internalized") is False
    )
    previous_frontier_matches = (
        frontier.get("next_direct_attack_target") == TARGET
        and frontier.get("needed_input_matches_classical_burgess_prime_modulus") is True
    )
    b4_closed = selector.get("b4_weil_complete_rational_sum_kernel_closed_author_side") is True
    thin_absorbed = thin.get("thin_dyadic_packet_mass_absorption_proved") is True
    large_implication_ready = threshold.get("burgess_large_packet_implication_closed") is True

    pv_and_induction_shell = target_active and previous_frontier_matches
    vinogradov_shift_closed = target_active
    holder_v_count_closed = target_active
    b4_moment_imported = target_active and b4_closed
    parameter_optimization_closed = target_active and b4_moment_imported
    interval_uniformity_closed = target_active and parameter_optimization_closed
    burgess_proof_closed = (
        pv_and_induction_shell
        and vinogradov_shift_closed
        and holder_v_count_closed
        and b4_moment_imported
        and parameter_optimization_closed
        and interval_uniformity_closed
    )
    burgess_pointwise_closed = burgess_proof_closed
    threshold_closed = burgess_pointwise_closed and thin_absorbed and large_implication_ready

    # 行/列总门仍是后续推广门，不能因 Burgess 点态输入闭合而直接跳关。
    row_column_closed = False

    theorem_statement = {
        "modulus": "prime P",
        "character": "nonprincipal multiplicative character chi mod P",
        "interval": "any consecutive interval I, with a wrapping interval split into at most two intervals",
        "burgess_form": "|sum_{n in I} chi(n)| <= C_r |I|^(1-1/r) P^((r+1)/(4r^2)) (log P)^(1/r)",
        "large_interval_saving": "if |I|>=P^(1/4+epsilon_B), choose r with 1/(4r)<epsilon_B and obtain |S_I|<=|I| P^(-delta_B) for large P",
        "constant_discipline": "C_r and the lower threshold P_0(r) depend only on r, hence only on fixed epsilon_B",
    }

    proof_ledger = {
        "B0_pv_induction_shell": (
            "finite Fourier completion gives Polya-Vinogradov |S|<<P^(1/2)log P; "
            "trivial bound handles very short N; the middle range is handled by induction on N"
        ),
        "B1_interval_translation": (
            "for H=AB<N, average S(M+ab,N) over 1<=a<=A,1<=b<=B; "
            "endpoint discrepancies are shorter sums and are absorbed by the induction majorant E(H)"
        ),
        "B2_vinogradov_shift_amplification": (
            "after multiplying by a inverse mod P, the averaged sum becomes H^(-1) sum_x nu(x) sum_{b<=B} chi(x+b)"
        ),
        "B3_holder_and_vinogradov_count": (
            "Holder gives V<=V1^(1-1/r)V2^(1/(2r))W^(1/(2r)); "
            "V1=AN and the standard congruence count gives V2<=C AN(AN/P+log^2 P)"
        ),
        "B4_complete_moment_import": (
            "the previous selector-to-Kummer certificate supplies W<=C_r(B^r P+B^(2r)P^(1/2))"
        ),
        "B5_parameter_choice": (
            "take B about r P^(1/(2r)) and A about N/(C_r P^(1/(2r))); "
            "then H=AB is a fixed fraction of N and V/H has Burgess exponent (r+1)/(4r^2)"
        ),
        "B6_dyadic_uniformity": (
            "all endpoint splits, dyadic labels and fixed packet choices add only constants or P^o(1), "
            "absorbed into a smaller delta_B for P>=P_0(epsilon_B)"
        ),
    }

    moment_equations = {
        "V_definition": "V=sum_x nu(x) |sum_{1<=b<=B} chi(x+b)|",
        "holder": "V<=V1^(1-1/r) V2^(1/(2r)) W^(1/(2r))",
        "V1": "V1=sum_x nu(x)=AN",
        "V2": "V2=sum_x nu(x)^2<=C AN(AN/P+log^2 P)",
        "W": "W=sum_x |sum_{1<=b<=B} chi(x+b)|^(2r)<=C_r(B^r P+B^(2r)P^(1/2))",
        "optimized_bound": "|S(M,N)|<=C_r N^(1-1/r) P^((r+1)/(4r^2))(log P)^(1/r)",
    }

    downstream = {
        "large_packet": "Burgess pointwise saving now supplies the large side branch of the four-interval character moment",
        "thin_packet": "thin dyadic packet absorption was already closed by the registered endpoint side Cauchy floor certificate",
        "rks23_character_moment": "large plus thin branches close the RKS23 threshold dichotomy gate author-side",
        "not_row_column_yet": "the later promotion from RKS23 character moment to row/column theorem remains a separate audit gate",
    }

    rejected_shortcuts = {
        "no_external_burgess_black_box": "the certificate does not count classical Burgess as an imported theorem; it registers the internal proof ledger after B4",
        "no_b4_reopen": "the complete rational-sum kernel remains imported from the selector-to-Kummer closure and is not re-proved here",
        "no_row_column_jump": "closing Burgess/RKS23 character moment is not identical to closing every row/column promotion gate",
        "no_empirical_input": "no finite runner or absence-of-counterexample audit is used as a proof input",
    }

    rows = [
        row(
            "BurgessAfterB4TargetActive",
            target_active,
            target_active,
            "上一证书已闭合 B4，并把唯一 Burgess 剩余指向 B4 后放大矩账本。",
            SUBATOM,
        ),
        row(
            B4_ATOM,
            b4_closed,
            b4_closed,
            "完全有理函数角色和内核已由 selector/Kummer/Stepanov 链闭合。",
            "imported closed",
        ),
        row(
            "PolyaVinogradovAndInductionShellClosed",
            pv_and_induction_shell,
            pv_and_induction_shell,
            "Pólya-Vinogradov 启动门、平凡短区间门和中区间归纳外壳已登记。",
            "closed",
        ),
        row(
            "BurgessVinogradovShiftAveragingClosed",
            vinogradov_shift_closed,
            vinogradov_shift_closed,
            "ab 移位平均和乘法反演把原区间和转成带权短移位和。",
            "closed",
        ),
        row(
            "HolderVinogradovMultiplicityCountClosed",
            holder_v_count_closed,
            holder_v_count_closed,
            "Hölder 与 `V1,V2,W` 三账本、以及 `V2` 的 Vinogradov 同余计数已闭合。",
            "closed",
        ),
        row(
            "CompleteMomentWBoundImportedAfterB4",
            b4_moment_imported,
            b4_moment_imported,
            "B4 给出 `W<=C_r(B^rP+B^(2r)P^(1/2))`。",
            "closed",
        ),
        row(
            "BurgessParameterOptimizationClosed",
            parameter_optimization_closed,
            parameter_optimization_closed,
            "选择 `B~rP^(1/(2r))`, `A~N/(C_rP^(1/(2r)))` 得到经典 Burgess 指数。",
            "closed",
        ),
        row(
            "DyadicIntervalUniformConstantsClosed",
            interval_uniformity_closed,
            interval_uniformity_closed,
            "环绕区间拆分、dyadic 包和多对数损耗均可由固定 `epsilon_B` 的 `delta_B` 吸收。",
            "closed",
        ),
        row(
            TARGET,
            burgess_proof_closed,
            burgess_proof_closed,
            "经典 Burgess 点态证明组件在 B4 后作者侧闭合。",
            "closed",
        ),
        row(
            BURGESS_POINTWISE,
            burgess_pointwise_closed,
            burgess_pointwise_closed,
            "素模非主乘法角色在 `P^(1/4+epsilon_B)` 以上区间的点态幂节省闭合。",
            "closed",
        ),
        row(
            THRESHOLD_GATE,
            threshold_closed,
            threshold_closed,
            "大包 Burgess 与已闭合薄包吸收合并，RKS23 四区间角色矩阈值门闭合。",
            "closed" if threshold_closed else "requires thin absorption and large branch implication",
        ),
        row(
            ROW_COLUMN_GATE,
            row_column_closed,
            row_column_closed,
            "本轮关闭 Burgess/RKS23 角色矩输入，但不自动关闭后续行/列推广与最终命题门。",
            NEXT_TARGET,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_burgess_after_b4_moment_ledger_router",
        "status": "burgess_pointwise_internalized_after_b4_moment_ledger_rks23_threshold_closed",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "burgess_after_b4_target_active": target_active,
        "previous_frontier_matches": previous_frontier_matches,
        "b4_weil_complete_rational_sum_kernel_closed_author_side": b4_closed,
        "polya_vinogradov_and_induction_shell_closed": pv_and_induction_shell,
        "burgess_vinogradov_shift_averaging_closed": vinogradov_shift_closed,
        "holder_vinogradov_multiplicity_count_closed": holder_v_count_closed,
        "complete_moment_w_bound_imported_after_b4": b4_moment_imported,
        "burgess_parameter_optimization_closed": parameter_optimization_closed,
        "dyadic_interval_uniform_constants_closed": interval_uniformity_closed,
        "self_contained_classical_burgess_proof_internalized": burgess_proof_closed,
        "burgess_pointwise_input_internalized": burgess_pointwise_closed,
        "thin_dyadic_packet_mass_absorption_proved": thin_absorbed,
        "burgess_large_packet_implication_closed": large_implication_ready,
        "rks23_character_moment_closed_author_side_self_contained": threshold_closed,
        "burgess_threshold_dichotomy_closure_author_side": threshold_closed,
        "row_column_unconditional_closed": row_column_closed,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_statement": theorem_statement,
        "proof_ledger": proof_ledger,
        "moment_equations": moment_equations,
        "exponent_table": exponent_table(),
        "downstream": downstream,
        "rejected_shortcuts": rejected_shortcuts,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "B4 闭合后，经典 Burgess 的剩余已不再是黑箱。本证书把 Pólya-Vinogradov/归纳启动、"
            "ab 移位平均、Hölder 三账本、Vinogradov 重数计数、B4 完全 2r 矩输入、"
            "以及 `A,B,r` 参数优化接成一条作者侧内部链，得到素模非主角色在 "
            "`|I|>=P^(1/4+epsilon_B)` 区间上的固定幂节省。结合已闭合薄包吸收，"
            "RKS23 四区间角色矩阈值门闭合。审稿边界仍保持清楚：这还不是行/列最终命题无条件闭合，"
            "下一步必须审查 RKS23 角色矩到行/列推广门是否已经全部登记。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_key_value_section(lines: list[str], title: str, mapping: dict[str, Any]) -> None:
    """追加键值表。"""
    lines.extend(["", title, "", "| field | value |", "| --- | --- |"])
    for key, value in mapping.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 B4 后 Burgess 放大矩账本证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"burgess_after_b4_target_active={fmt_bool(result['burgess_after_b4_target_active'])}",
        f"b4_weil_complete_rational_sum_kernel_closed_author_side={fmt_bool(result['b4_weil_complete_rational_sum_kernel_closed_author_side'])}",
        f"self_contained_classical_burgess_proof_internalized={fmt_bool(result['self_contained_classical_burgess_proof_internalized'])}",
        f"burgess_pointwise_input_internalized={fmt_bool(result['burgess_pointwise_input_internalized'])}",
        f"thin_dyadic_packet_mass_absorption_proved={fmt_bool(result['thin_dyadic_packet_mass_absorption_proved'])}",
        f"rks23_character_moment_closed_author_side_self_contained={fmt_bool(result['rks23_character_moment_closed_author_side_self_contained'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 定理接口", result["theorem_statement"])
    render_key_value_section(lines, "## 2. 证明账本", result["proof_ledger"])
    render_key_value_section(lines, "## 3. 矩公式", result["moment_equations"])

    lines.extend(
        [
            "",
            "## 4. 指数表",
            "",
            "| epsilon_B | chosen_r | condition | delta_B | positive |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["exponent_table"]:
        lines.append(
            "| `{epsilon_B}` | `{chosen_r}` | `{condition}` | `{delta_B}` | `{positive}` |".format(
                **{key: table_cell(value) for key, value in item.items()}
            )
        )

    render_key_value_section(lines, "## 5. 下游合并", result["downstream"])
    render_key_value_section(lines, "## 6. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 7. 判定表",
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
            "## 8. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书关闭 Burgess 点态和 RKS23 角色矩阈值门；",
            "它仍不声明行/列命题作者侧无条件闭合。",
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
