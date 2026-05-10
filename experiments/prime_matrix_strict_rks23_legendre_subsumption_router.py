#!/usr/bin/env python3
"""把纯二次 Legendre 核并入光滑 rank-two 统一输入。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_legendre_subsumption_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-legendre-subsumption-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-legendre-subsumption-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-legendre-subsumption-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-rank-two-trace-singularity-router.json"
SOURCE_FILES = [PREVIOUS]

OLD_TARGET = "SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma"
NEW_TARGET = "UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma"
LEGENDRE_GATE = "SmoothLegendreQuadraticCoreTraceInput"
POINTCOUNT_GATE = "LegendreCoreExactEllipticPointCountIdentity"
HYPER_GATE = "SmoothRankTwoHypergeometricTraceInput"
SELECTOR_GATE = "OrderFreeKummerSignatureSelectorAndHasseJetRankLemma"
JET_GATE = "BoundedBranchSignatureHasseJetIndependenceLemma"
RANK_TARGET = "StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity"
STEPANOV_TARGET = "StepanovAuxiliaryPolynomialRankBoundForKummerSums"
KUMMER_TRACE_TARGET = "SelfContainedRankOneKummerSheafRHTraceBound"
BURGESS_POINTWISE = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"


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


def legendre_symbol(value: int, prime: int) -> int:
    """计算 Legendre 符号。"""
    value %= prime
    if value == 0:
        return 0
    power = pow(value, (prime - 1) // 2, prime)
    return -1 if power == prime - 1 else power


def legendre_kernel(prime: int, lamb: int, x: int) -> int:
    """Legendre 核 x(1-x)(1-lambda*x)。"""
    return (x * (1 - x) * (1 - lamb * x)) % prime


def legendre_sum(prime: int, lamb: int) -> int:
    """计算二次交比角色和。"""
    return sum(legendre_symbol(legendre_kernel(prime, lamb, x), prime) for x in range(prime))


def elliptic_point_count(prime: int, lamb: int) -> int:
    """直接计数 E_lambda: y^2=x(1-x)(1-lambda*x) 的点数。"""
    total = 1  # 无穷远点
    for x in range(prime):
        value = legendre_kernel(prime, lamb, x)
        total += 1 + legendre_symbol(value, prime)
    return total


def pointcount_audit(cases: list[tuple[int, int]]) -> list[dict[str, Any]]:
    """审计 Legendre 和与椭圆点数恒等式；不作为 Hasse 证明。"""
    rows: list[dict[str, Any]] = []
    for prime, lamb in cases:
        char_sum = legendre_sum(prime, lamb)
        points = elliptic_point_count(prime, lamb)
        trace = prime + 1 - points
        rows.append(
            {
                "prime": prime,
                "lambda": lamb,
                "smooth_lambda": lamb % prime not in {0, 1},
                "legendre_sum": char_sum,
                "point_count": points,
                "trace_p_plus_1_minus_points": trace,
                "identity_trace_equals_negative_sum": trace == -char_sum,
                "abs_sum_over_sqrt_p": round(abs(char_sum) / math.sqrt(prime), 12),
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 Legendre 子例并入证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == OLD_TARGET
        and previous.get("crossratio_singular_lambda_firewall_closed") is True
        and previous.get("rank_two_crossratio_trace_bound_internalized") is False
    )

    exact_identity = {
        "quadratic_sum": "L_lambda=sum_x chi(x(1-x)(1-lambda*x))",
        "curve": "E_lambda: y^2=x(1-x)(1-lambda*x), with lambda not in {0,1}",
        "point_count": "#E_lambda(F_p)=p+1+L_lambda",
        "trace_identity": "a_p(lambda)=p+1-#E_lambda(F_p)=-L_lambda",
        "meaning": "bounding the Legendre core is exactly the smooth elliptic trace subcase of the rank-two input",
    }

    subsumption = {
        "old_split": "SmoothLegendreQuadraticCoreTraceInput + SmoothRankTwoHypergeometricTraceInput",
        "new_unified_gate": NEW_TARGET,
        "legendre_role": "quadratic-character specialization of the same smooth cross-ratio trace problem",
        "not_independent": "Legendre no longer remains as a separate gate; it is carried by the unified smooth rank-two trace/pivot lemma",
        "not_claimed": "the Hasse/Stepanov trace bound itself is not proved in this certificate",
    }

    remaining_unified_input = {
        "trace_form": "prove |sum_x A(x)B(1-x)C(1-lambda*x)| <= C_m*sqrt(p) on the smooth lambda domain",
        "normalized_form": "equivalently prove the normalized rank-two trace H_lambda is O_m(1)",
        "pivot_form": "or construct an order-free Stepanov pivot block whose Hasse-jet losses are O_m(TN)",
        "domain": "lambda not in {0,1,infinity}, including j=0 and j=1728 smooth points",
        "constant_rule": "constants may depend on the fixed branch bound m, but not on d, p, chi, or branch positions",
    }

    rejected_shortcuts = {
        "separate_legendre_gate": "do not keep asking for Legendre as an independent third gate; it is a subcase of the unified smooth rank-two input",
        "pointcount_as_hasse": "the exact point-count identity is not a proof of the Hasse bound",
        "external_hasse_label": "labeling the curve elliptic is not enough for a self-contained route unless the trace bound is proved or accepted as an external lemma",
        "whole_kummer_curve": "the forbidden d-dependent Kummer curve route remains excluded",
    }

    pointcount_closed = active
    legendre_subsumed = active
    unified_trace_closed = False
    selector_internalized = False
    rank_closed = selector_internalized
    stepanov_closed = rank_closed

    rows = [
        row(
            "PreviousSmoothRankTwoTargetActive",
            active,
            active,
            "上一证书已把唯一剩余压到光滑 rank-two 交比域。",
            OLD_TARGET,
        ),
        row(
            POINTCOUNT_GATE,
            pointcount_closed,
            pointcount_closed,
            "纯二次 Legendre 和与光滑椭圆曲线点数满足精确恒等式。",
            NEW_TARGET,
        ),
        row(
            "LegendreCoreSubsumedIntoUnifiedRankTwoGate",
            legendre_subsumed,
            legendre_subsumed,
            "Legendre 核不再作为独立守门项，而是统一 smooth rank-two 输入的二次特化。",
            NEW_TARGET,
        ),
        row(
            LEGENDRE_GATE,
            legendre_subsumed,
            legendre_subsumed,
            "该项作为独立缺口已消去；实际界仍由统一 rank-two 输入承担。",
            NEW_TARGET,
        ),
        row(
            HYPER_GATE,
            False,
            False,
            "非二次与二次特化统一后，仍需证明 smooth rank-two 交比迹界。",
            NEW_TARGET,
        ),
        row(
            OLD_TARGET,
            False,
            False,
            "旧的 smooth rank-two 表述已去掉独立 Legendre 分支，但统一迹界未证。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            unified_trace_closed,
            unified_trace_closed,
            "仍需自足证明统一 smooth rank-two 迹界，或给出等价 Stepanov pivot。",
            "UnifiedSmoothRankTwoTraceBoundOrPivot",
        ),
        row(
            JET_GATE,
            False,
            False,
            "Hasse-jet 秩下界仍等待统一 smooth rank-two pivot 块。",
            NEW_TARGET,
        ),
        row(
            SELECTOR_GATE,
            False,
            False,
            "完整阶无关 selector 仍等待统一 smooth rank-two 输入。",
            NEW_TARGET,
        ),
        row(
            RANK_TARGET,
            rank_closed,
            rank_closed,
            "Stepanov-Kummer 非零秩仍等待完整 selector。",
            SELECTOR_GATE,
        ),
        row(
            STEPANOV_TARGET,
            stepanov_closed,
            stepanov_closed,
            "Stepanov 完整内部证明仍未闭合。",
            RANK_TARGET,
        ),
        row(
            KUMMER_TRACE_TARGET,
            False,
            False,
            "秩一 Kummer 迹界仍等待统一 smooth rank-two 输入内部化。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只消去独立 Legendre 分支，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_legendre_subsumption_router",
        "status": "legendre_quadratic_core_subsumed_into_unified_smooth_rank_two_gate",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_audit_not_used_as_proof": True,
        "previous_smooth_rank_two_target_active": active,
        "legendre_exact_pointcount_identity_closed": pointcount_closed,
        "legendre_core_independent_gate_eliminated": legendre_subsumed,
        "unified_smooth_rank_two_trace_bound_internalized": unified_trace_closed,
        "rank_two_crossratio_trace_bound_internalized": unified_trace_closed,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": "UnifiedSmoothRankTwoTraceBoundOrPivot",
        "exact_identity": exact_identity,
        "subsumption": subsumption,
        "remaining_unified_input": remaining_unified_input,
        "rejected_shortcuts": rejected_shortcuts,
        "pointcount_audit": pointcount_audit([(17, 3), (29, 5), (31, 3), (41, 6), (43, 7), (53, 11)]),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮没有证明统一 smooth rank-two 迹界，但消去了一个重复守门项：纯二次 Legendre 核不再作为独立缺口。"
            "对 `lambda notin {0,1}`，令 `L_lambda=sum_x chi(x(1-x)(1-lambda*x))`，"
            "光滑曲线 `E_lambda: y^2=x(1-x)(1-lambda*x)` 满足精确点数恒等式 "
            "`#E_lambda(F_p)=p+1+L_lambda`，因此 `a_p(lambda)=-L_lambda`。"
            "这说明 Legendre 核只是统一 smooth rank-two 交比迹界的二次特化；"
            "它不应再作为独立的第三个开放输入反复出现。当前唯一真正剩余压成 "
            "`UnifiedSmoothRankTwoHypergeometricTraceBoundOrPivotLemma`：在光滑交比域 "
            "`lambda notin {0,1,infinity}` 上，自足证明统一 rank-two 迹界，或构造等价 order-free Stepanov pivot。"
            "未完成该统一输入前，Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。"
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
        "# Prime Matrix strict RKS2/RKS3 Legendre 并入证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_smooth_rank_two_target_active={fmt_bool(result['previous_smooth_rank_two_target_active'])}",
        f"legendre_exact_pointcount_identity_closed={fmt_bool(result['legendre_exact_pointcount_identity_closed'])}",
        f"legendre_core_independent_gate_eliminated={fmt_bool(result['legendre_core_independent_gate_eliminated'])}",
        f"unified_smooth_rank_two_trace_bound_internalized={fmt_bool(result['unified_smooth_rank_two_trace_bound_internalized'])}",
        f"order_free_signature_selector_internalized={fmt_bool(result['order_free_signature_selector_internalized'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 精确点数恒等式", result["exact_identity"])
    render_key_value_section(lines, "## 2. 并入关系", result["subsumption"])
    render_key_value_section(lines, "## 3. 统一剩余输入", result["remaining_unified_input"])
    render_key_value_section(lines, "## 4. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 5. 点数恒等式审计",
            "",
            "| prime | lambda | smooth_lambda | legendre_sum | point_count | trace_p_plus_1_minus_points | identity_trace_equals_negative_sum | abs_sum_over_sqrt_p |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["pointcount_audit"]:
        lines.append(
            "| `{prime}` | `{lambda}` | `{smooth_lambda}` | `{legendre_sum}` | `{point_count}` | `{trace_p_plus_1_minus_points}` | `{identity_trace_equals_negative_sum}` | `{abs_sum_over_sqrt_p}` |".format(
                **{key: table_cell(value) for key, value in item.items()}
            )
        )

    lines.extend(
        [
            "",
            "## 6. 判定表",
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
            "## 7. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书只证明 Legendre 核的精确点数恒等式并消去独立分支，",
            "没有证明统一 smooth rank-two 迹界或完整 Stepanov selector；",
            "因此不声明 Kummer 迹界、Burgess B4 或行/列命题作者侧无条件闭合。",
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
