#!/usr/bin/env python3
"""剥离 rank-two 交比迹界中的 lambda 奇异边界。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_rank_two_trace_singularity_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-rank-two-trace-singularity-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-rank-two-trace-singularity-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-rank-two-trace-singularity-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-four-branch-hypergeometric-router.json"
SOURCE_FILES = [PREVIOUS]

OLD_TARGET = "RankTwoCrossRatioHypergeometricTraceBoundInternalizationLemma"
NEW_TARGET = "SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma"
SINGULAR_GATE = "CrossRatioSingularLambdaReductionFirewall"
SPECIAL_GATE = "SpecialAutomorphismLambdaSmoothnessFirewall"
LEGENDRE_GATE = "SmoothLegendreQuadraticCoreTraceInput"
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


def inv_mod(value: int, prime: int) -> int:
    """模素数逆元。"""
    return pow(value % prime, -1, prime)


def legendre_discriminant_mod(prime: int, lamb: int) -> int:
    """Legendre 三次核 x(1-x)(1-lambda*x) 的判别式平方因子。"""
    return (lamb * lamb * (1 - lamb) * (1 - lamb)) % prime


def legendre_j_mod(prime: int, lamb: int) -> int | None:
    """计算 Legendre j 不变量；奇异 lambda 返回 None。"""
    disc = (lamb * lamb * (1 - lamb) * (1 - lamb)) % prime
    if disc == 0:
        return None
    numerator = (256 * pow((1 - lamb + lamb * lamb) % prime, 3, prime)) % prime
    return (numerator * inv_mod(disc, prime)) % prime


def singularity_audit(primes: list[int]) -> list[dict[str, Any]]:
    """审计 lambda 奇异集与特殊自同构点；证明仍是符号判别式。"""
    rows: list[dict[str, Any]] = []
    for prime in primes:
        singular = []
        smooth = []
        j_zero = []
        j_1728 = []
        for lamb in range(prime):
            if legendre_discriminant_mod(prime, lamb) == 0:
                singular.append(lamb)
                continue
            smooth.append(lamb)
            j_value = legendre_j_mod(prime, lamb)
            if j_value == 0:
                j_zero.append(lamb)
            if j_value == 1728 % prime:
                j_1728.append(lamb)
        rows.append(
            {
                "prime": prime,
                "singular_lambdas": singular,
                "smooth_count": len(smooth),
                "expected_smooth_count": prime - 2,
                "j_zero_smooth_lambdas": j_zero,
                "j_1728_smooth_lambdas": j_1728,
                "all_special_points_smooth": all(item not in singular for item in j_zero + j_1728),
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 rank-two 奇异边界证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == OLD_TARGET
        and previous.get("rank_two_crossratio_trace_bound_internalized") is False
        and previous.get("four_branch_pgl2_crossratio_normal_form_closed") is True
    )

    singular_lambda_firewall = {
        "crossratio_domain": "lambda belongs to P^1 minus {0,1,infinity} after PGL2 normalization",
        "lambda_0": "the fourth branch collides with 0; support drops to at most three and is already closed by low-support/Jacobi routers",
        "lambda_1": "the fourth branch collides with 1; support drops to at most three and is already closed",
        "lambda_infinity": "after relabeling, infinity collision is the same support-drop case",
        "consequence": "rank-two trace input only needs smooth lambda not in {0,1,infinity}",
    }

    smoothness_certificate = {
        "legendre_core": "y^2=x(1-x)(1-lambda*x)",
        "discriminant": "Delta(lambda)=lambda^2*(1-lambda)^2 up to a nonzero square factor",
        "smooth_condition": "Delta(lambda)!=0, exactly lambda not in {0,1,infinity}",
        "j_invariant": "j(lambda)=256*(1-lambda+lambda^2)^3/(lambda^2*(1-lambda)^2)",
        "special_automorphism_points": "j=0 and j=1728 are smooth when lambda not in {0,1}; they do not create new singular gates",
    }

    rank_two_scope = {
        "old_atom": OLD_TARGET,
        "new_atom": NEW_TARGET,
        "closed_boundary": "all branch-collision lambda values are routed back to already closed <=3 visible-branch cases",
        "remaining_legendre": "prove the smooth Legendre quadratic core trace bound for every lambda not in {0,1}",
        "remaining_hypergeometric": "prove the smooth rank-two hypergeometric trace bound for every lambda not in {0,1}",
        "remaining_equivalent_pivot": "or construct an order-free Stepanov pivot block on the same smooth lambda domain",
    }

    rejected_shortcuts = {
        "special_j_as_exception": "j=0 and j=1728 may increase automorphisms but are not singular and cannot be left as separate unclosed cases",
        "lambda_zero_one": "lambda=0 or 1 must not be counted inside rank-two; they are support-drop cases already closed upstream",
        "finite_audit": "the audit confirms the symbolic discriminant pattern but is not used as proof of the trace bound",
        "hasse_weil_whole_kummer": "do not return to the full y^d=f(x) curve; the remaining input is rank-two and order-free",
    }

    singular_firewall_closed = active
    special_firewall_closed = active
    selector_internalized = False
    rank_closed = selector_internalized
    stepanov_closed = rank_closed

    rows = [
        row(
            "PreviousRankTwoTargetActive",
            active,
            active,
            "上一证书已把唯一剩余压成 rank-two 交比迹界内部化。",
            OLD_TARGET,
        ),
        row(
            SINGULAR_GATE,
            singular_firewall_closed,
            singular_firewall_closed,
            "lambda=0,1,∞ 都是分支碰撞，回到已闭合的低支撑/三分支支路。",
            "closed",
        ),
        row(
            SPECIAL_GATE,
            special_firewall_closed,
            special_firewall_closed,
            "j=0 与 j=1728 只是光滑特殊自同构点，不再作为独立未闭合边界。",
            "closed",
        ),
        row(
            OLD_TARGET,
            False,
            False,
            "rank-two 输入已去掉奇异 lambda 边界，但光滑迹界本身仍未内部证明。",
            NEW_TARGET,
        ),
        row(
            NEW_TARGET,
            False,
            False,
            "仍需在光滑 lambda 域证明 rank-two 交比迹界，或给出等价 Stepanov pivot。",
            "SmoothRankTwoTraceBoundOrPivot",
        ),
        row(
            LEGENDRE_GATE,
            False,
            False,
            "纯二次 Legendre 核仍需要光滑椭圆迹界的自足证明。",
            NEW_TARGET,
        ),
        row(
            HYPER_GATE,
            False,
            False,
            "非二次归一化超几何核仍需要 rank-two 迹界的自足证明。",
            NEW_TARGET,
        ),
        row(
            JET_GATE,
            False,
            False,
            "Hasse-jet 秩下界仍等待光滑 rank-two pivot 块。",
            NEW_TARGET,
        ),
        row(
            SELECTOR_GATE,
            False,
            False,
            "完整阶无关 selector 仍等待光滑 rank-two 输入。",
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
            "秩一 Kummer 迹界仍等待光滑 rank-two 输入内部化。",
            STEPANOV_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只剥离奇异 lambda 边界，不声明行/列命题作者侧无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_rank_two_trace_singularity_router",
        "status": "rank_two_trace_restricted_to_smooth_crossratio_domain",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "finite_audit_not_used_as_proof": True,
        "previous_rank_two_target_active": active,
        "crossratio_singular_lambda_firewall_closed": singular_firewall_closed,
        "special_automorphism_lambda_smoothness_firewall_closed": special_firewall_closed,
        "rank_two_crossratio_trace_bound_internalized": False,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEW_TARGET,
        "next_subatom": "SmoothRankTwoTraceBoundOrPivot",
        "singular_lambda_firewall": singular_lambda_firewall,
        "smoothness_certificate": smoothness_certificate,
        "rank_two_scope": rank_two_scope,
        "rejected_shortcuts": rejected_shortcuts,
        "lambda_singularity_audit": singularity_audit([17, 29, 31, 41, 43, 53]),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮没有证明 rank-two 交比迹界，但把其中的 lambda 边界完全剥离。"
            "四分支归一化后的交比参数只需考虑 `lambda notin {0,1,infinity}`："
            "`lambda=0,1,∞` 都是分支碰撞，支撑降到至多三处，已由低支撑和 exact-three Jacobi 支路关闭。"
            "对纯二次 Legendre 核 `y^2=x(1-x)(1-lambda*x)`，判别式为 "
            "`lambda^2(1-lambda)^2`；因此 `lambda notin {0,1}` 时曲线光滑。"
            "`j=0`、`j=1728` 只表示额外自同构，不是新奇异边界，不能再作为未处理特殊情形。"
            "所以唯一剩余从含糊的“所有特殊和一般 lambda”压成 "
            "`SmoothRankTwoCrossRatioTraceBoundOrStepanovPivotLemma`：在光滑交比域上自足证明 rank-two 迹界，"
            "或构造等价的 order-free Stepanov pivot 块。未完成该光滑 rank-two 输入前，"
            "Stepanov、Kummer 迹界、Burgess B4 与行/列命题仍不能作者侧无条件闭合。"
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
        "# Prime Matrix strict RKS2/RKS3 rank-two 奇异边界证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_rank_two_target_active={fmt_bool(result['previous_rank_two_target_active'])}",
        f"crossratio_singular_lambda_firewall_closed={fmt_bool(result['crossratio_singular_lambda_firewall_closed'])}",
        f"special_automorphism_lambda_smoothness_firewall_closed={fmt_bool(result['special_automorphism_lambda_smoothness_firewall_closed'])}",
        f"rank_two_crossratio_trace_bound_internalized={fmt_bool(result['rank_two_crossratio_trace_bound_internalized'])}",
        f"order_free_signature_selector_internalized={fmt_bool(result['order_free_signature_selector_internalized'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 奇异 lambda 防火墙", result["singular_lambda_firewall"])
    render_key_value_section(lines, "## 2. 光滑性证书", result["smoothness_certificate"])
    render_key_value_section(lines, "## 3. rank-two 剩余范围", result["rank_two_scope"])
    render_key_value_section(lines, "## 4. 禁止捷径", result["rejected_shortcuts"])

    lines.extend(
        [
            "",
            "## 5. lambda 奇异性审计",
            "",
            "| prime | singular_lambdas | smooth_count | expected_smooth_count | j_zero_smooth_lambdas | j_1728_smooth_lambdas | all_special_points_smooth |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["lambda_singularity_audit"]:
        lines.append(
            "| `{prime}` | `{singular_lambdas}` | `{smooth_count}` | `{expected_smooth_count}` | `{j_zero_smooth_lambdas}` | `{j_1728_smooth_lambdas}` | `{all_special_points_smooth}` |".format(
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
            "审稿边界：本证书只剥离奇异 lambda 与特殊自同构伪边界，",
            "没有证明光滑 rank-two 迹界或完整 Stepanov selector；",
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
