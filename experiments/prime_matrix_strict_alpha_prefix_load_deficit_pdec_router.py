#!/usr/bin/env python3
"""生成 strict alpha-prefix 负载缺陷到 PDEC/TV 的路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_prefix_load_deficit_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-alpha-prefix-load-deficit-pdec-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-block-coprime-dynamics-capacity-surplus-router.md",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.md",
    MONOGRAPH / "prime-matrix-eda-lowmod-pdec-certificate-route.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-dyadic-pdec-certificate.md",
]

EULER_GAMMA = 0.5772156649015329
MERTENS_ROUGH_CONSTANT = math.exp(-EULER_GAMMA)

ALPHA_LOAD = "AlphaPrefixRoughLoadLowerBoundExceedingHighLabelCapacity"
ALPHA_TV_DEFECT = "AlphaPrefixTotalVariationOrEndpointPDECDefectExclusion"
B3_REMAINDER = "B3RemainderTotalVariationBudgetForLengthP"
MAIN_COEFF = "B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def alpha_gap_profile(alpha: float) -> dict[str, Any]:
    """给出 alpha 切片的缺陷间隙常数诊断。"""
    hit_cap = math.ceil(1.0 / alpha)
    capacity_constant = hit_cap * (1.0 - alpha)
    reference_gap = MERTENS_ROUGH_CONSTANT - capacity_constant
    return {
        "alpha": alpha,
        "hit_cap": hit_cap,
        "capacity_constant": capacity_constant,
        "mertens_reference_main_constant": MERTENS_ROUGH_CONSTANT,
        "reference_defect_gap_constant": reference_gap,
        "positive_reference_gap": reference_gap > 0,
    }


def exact_implications() -> list[dict[str, str]]:
    """列出本路由闭合的蕴含。"""
    return [
        {
            "name": "early_zero_capacity_necessity",
            "formula": "Assume EarlyZeroRowWithinP and z=alpha P> P/2. Then |R_alpha(x)|<=2(pi(P)-pi(alpha P)).",
            "status": "closed_imported",
            "meaning": "来自高标签容量反超路由；这是早期零行的必要条件。",
        },
        {
            "name": "lower_weight_main_error",
            "formula": "|R_alpha(x)| >= (P-1) W^-_alpha - TV_alpha.",
            "status": "closed_imported",
            "meaning": "来自统一 prefix 粗筛余路由；TV 汇总 CRT 端点/筛权总变差。",
        },
        {
            "name": "defect_forced_if_no_surplus",
            "formula": "If EarlyZeroRowWithinP, then TV_alpha >= (P-1)W^-_alpha - 2(pi(P)-pi(alpha P)).",
            "status": "closed_implication",
            "meaning": "若没有容量反超矛盾，反例必须支付一个强负端点/总变差缺陷。",
        },
        {
            "name": "closure_if_tv_budget_beats_gap",
            "formula": "If TV_alpha < (P-1)W^-_alpha - 2(pi(P)-pi(alpha P)), then early zero row is impossible.",
            "status": "closed_implication",
            "meaning": "这把当前硬点变成一个明确的 TV/PDEC 排斥输入。",
        },
        {
            "name": "pdec_registration",
            "formula": "Failure of the TV budget must be registered as LowMod/Endpoint/Dyadic PDEC or SAE, not as a free escape.",
            "status": "registered_route",
            "meaning": "与既有 LowMod、dyadic endpoint 证书路线对接。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍只在早期零行假设链条下推出必要缺陷。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "CapacityFailureToTVDefectClosed",
            "closed": True,
            "proved": True,
            "meaning": "早期零行若不被容量反超立即击败，则必须满足 TV_alpha 大于主项-容量间隙。",
            "remaining": ALPHA_TV_DEFECT,
        },
        {
            "gate": "PDECRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "大 TV/端点偏差已有 LowMod、dyadic endpoint、SAE 路由对象；但尚未全局排斥。",
            "remaining": "LowMod/DyadicEndpoint/FarTail-Core PDEC exclusion",
        },
        {
            "gate": "AlphaLoadLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "主项常数、TV 预算、有限段证书仍未合取闭合。",
            "remaining": f"{MAIN_COEFF} AND {B3_REMAINDER} AND {FINITE_PREFIX}",
        },
        {
            "gate": "DirectUnconditionalContradictionFound",
            "closed": False,
            "proved": False,
            "meaning": "已得到二择结构：容量反超直接矛盾，或强缺陷登记；缺陷排斥尚未完成。",
            "remaining": f"{ALPHA_LOAD} OR {ALPHA_TV_DEFECT}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    alpha_values = [0.75, 0.80, 0.85, 0.90, 0.95]
    return {
        "certificate_type": "prime_matrix_strict_alpha_prefix_load_deficit_pdec_router",
        "status": "alpha_prefix_load_deficit_forces_tv_or_pdec_defect_surplus_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "capacity_failure_to_tv_defect_implication_closed": True,
        "pdec_registration_route_defined": True,
        "alpha_prefix_load_lower_bound_proved": False,
        "alpha_prefix_tv_defect_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ALPHA_TV_DEFECT,
        "parallel_targets": [MAIN_COEFF, B3_REMAINDER, FINITE_PREFIX],
        "exact_implications": exact_implications(),
        "decision_rows": decision_rows(),
        "alpha_gap_profiles": [alpha_gap_profile(alpha) for alpha in alpha_values],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "容量反超失败不是自由出口。对 z=alpha P>P/2，早期零行迫使 "
            "|R_alpha(x)|<=2(pi(P)-pi(alpha P))；而 prefix lower-weight 公式给出 "
            "|R_alpha(x)|>=(P-1)W^-_alpha-TV_alpha。因此若不能直接容量反超，"
            "就必须有 TV_alpha 至少达到主项减高标签容量的间隙。"
            "这正是一个强端点/PDEC/SAE 缺陷，而不是新的无名逃逸。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict alpha-prefix 负载缺陷到 PDEC/TV 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"capacity_failure_to_tv_defect_implication_closed={fmt_bool(result['capacity_failure_to_tv_defect_implication_closed'])}",
        f"pdec_registration_route_defined={fmt_bool(result['pdec_registration_route_defined'])}",
        f"alpha_prefix_load_lower_bound_proved={fmt_bool(result['alpha_prefix_load_lower_bound_proved'])}",
        f"alpha_prefix_tv_defect_excluded={fmt_bool(result['alpha_prefix_tv_defect_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 二择公式",
        "",
        "对 `alpha>1/2`，早期零行必须满足",
        "",
        "```text",
        "|R_alpha(x)| <= 2(pi(P)-pi(alpha P)).",
        "```",
        "",
        "另一方面，prefix lower weights 给出",
        "",
        "```text",
        "|R_alpha(x)| >= (P-1)W^-_alpha - TV_alpha.",
        "```",
        "",
        "合并得到反例必要条件：",
        "",
        "```text",
        "TV_alpha >= (P-1)W^-_alpha - 2(pi(P)-pi(alpha P)).",
        "```",
        "",
        "所以闭合路线不再模糊：要么证明 TV 小于这个间隙得到直接矛盾；要么这个大 TV 必须作为端点/PDEC/SAE 缺陷被登记并排斥。",
        "",
        "## 2. 精确蕴含",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["exact_implications"]:
        lines.append(
            "| `{name}` | {formula} | `{status}` | {meaning} |".format(
                name=table_cell(row["name"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. alpha 间隙诊断",
            "",
            "下表仍是目标定位，不是证明。正间隙表示若获得 Mertens 级粗筛主项并控制 TV，就会触发容量反超或强缺陷。",
            "",
            "| alpha | hit cap | capacity constant | Mertens main reference | reference defect gap | positive |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["alpha_gap_profiles"]:
        lines.append(
            "| {alpha:.6f} | {hit} | {cap:.6f} | {main:.6f} | {gap:.6f} | `{positive}` |".format(
                alpha=row["alpha"],
                hit=row["hit_cap"],
                cap=row["capacity_constant"],
                main=row["mertens_reference_main_constant"],
                gap=row["reference_defect_gap_constant"],
                positive=fmt_bool(row["positive_reference_gap"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 最新最窄输入",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步只证明“容量不反超则强缺陷”的二择结构；它没有排斥该强缺陷，因此不能声明无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
