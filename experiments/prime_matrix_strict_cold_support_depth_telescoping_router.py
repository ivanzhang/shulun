#!/usr/bin/env python3
"""生成 strict 冷支撑深度伸缩/对数吸收路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_cold_support_depth_telescoping_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-cold-support-depth-telescoping-router.json

输出：
  docs/monograph/prime-matrix-strict-cold-support-depth-telescoping-router.json
  docs/monograph/prime-matrix-strict-cold-support-depth-telescoping-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-cold-support-depth-telescoping-router.json"
OUT_MD = DOCS / "prime-matrix-strict-cold-support-depth-telescoping-router.md"

DEPTH_TELESCOPE = "ColdSupportDepthTelescopingContractionOrLogAbsorptionTable"
SUPPORT_TABLE = "CoreHistoryWeightedSupportMeasureTable"
PER_LEVEL = "SameParameterPerLevelColdSupportExponentTable"
TPDEC_TABLE = "SameParameterPDECThresholdNumericTable"
LOAD_LOWER = "SparseTerminalForcedLoadLowerBoundFromEarlyZeroRow"
FINITE_RUNNER = "FiniteColdHistorySummationRunnerOrAnalyticEnvelope"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
LOG_EPSILON = 0.25
P_MIN = 100_000

SOURCE_FILES = [
    "prime-matrix-strict-core-history-weighted-support-measure-router.json",
    "prime-matrix-strict-same-parameter-core-threshold-summation-router.json",
    "prime-matrix-strict-same-parameter-prefix-window-spec-router.json",
    "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_cold_support_depth_telescoping_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def depth_cap_samples() -> list[dict[str, Any]]:
    """生成深度 cap 与 P^1/4 吸收样本。"""
    samples: list[dict[str, Any]] = []
    for p_value in [P_MIN, 300_000, 1_000_000, 10_000_000, 1_000_000_000]:
        depth_cap = math.floor(math.log(p_value, 2)) + 1
        p_eps = p_value**LOG_EPSILON
        samples.append(
            {
                "P": p_value,
                "depth_cap": depth_cap,
                "P_epsilon": round(p_eps, 6),
                "absorbed": depth_cap <= p_eps,
                "margin": round(p_eps - depth_cap, 6),
            }
        )
    return samples


def telescoping_rows() -> list[dict[str, str]]:
    """列出深度伸缩的严格公式。"""
    return [
        {
            "name": "strict_depth_cap",
            "formula": "depth(W)<=floor(log_2 h_0)<=floor(log_2 P)",
            "status": "closed",
            "meaning": "每一步乘子至少为 2，因此历史深度至多对数级。",
        },
        {
            "name": "explicit_log_absorption",
            "formula": "floor(log_2 P)+1 <= P^(1/4) for P>=100000",
            "status": "closed",
            "meaning": "对数深度可转成一个显式 P^0.25 预算损耗。",
        },
        {
            "name": "single_layer_to_all_depths",
            "formula": "Sigma_support <= (floor(log_2 P)+1) * max_level S_level + named returns",
            "status": "closed_as_reduction",
            "meaning": "若无严格收缩，最保守的全深度代价是一个对数因子。",
        },
        {
            "name": "weighted_log_absorption_criterion",
            "formula": "if S_level<=P^beta and T_PDEC<=P^tau and beta+tau+1/4<alpha, then weighted support < P^alpha",
            "status": "closed_criterion",
            "meaning": "最终只需每层支撑指数和 PDEC 权重留出 alpha-1/4 的余量。",
        },
        {
            "name": "strict_contraction",
            "formula": "S_{j+1} <= q S_j with q<1",
            "status": "not_proved",
            "meaning": "现有兄弟投影账本只有非扩张/收费，不含统一 q<1 收缩。",
        },
    ]


def exponent_budget_rows() -> list[dict[str, Any]]:
    """给出 alpha 预算分配表。"""
    rows: list[dict[str, Any]] = []
    remaining = ALPHA - LOG_EPSILON
    for beta, tau in [(0.10, 0.05), (0.12, 0.05), (0.15, 0.03), (0.18, 0.00), (0.20, 0.00)]:
        total = beta + tau + LOG_EPSILON
        rows.append(
            {
                "beta_per_level_support": beta,
                "tau_tpdec_weight": tau,
                "log_epsilon": LOG_EPSILON,
                "total_exponent": round(total, 6),
                "below_alpha": total < ALPHA,
                "remaining_after_log": round(remaining, 6),
                "margin": round(ALPHA - total, 6),
            }
        )
    return rows


def no_contraction_witness_rows() -> list[dict[str, Any]]:
    """说明现有单层账本没有严格收缩。"""
    return [
        {
            "level": i,
            "S_level": 1,
            "S_next": 1,
            "nonexpansion_valid": True,
            "strict_contraction_factor_needed": "<1",
            "strict_contraction_witness_fails": True,
        }
        for i in range(1, 5)
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "DepthTelescopingTargetImported",
            result["depth_telescoping_target_imported"],
            result["depth_telescoping_target_imported"],
            "上一层已把加权支撑测度的最窄剩余压成跨层深度伸缩。",
            DEPTH_TELESCOPE,
        ),
        row(
            "DepthCapLogPClosed",
            result["depth_cap_log_p_closed"],
            result["depth_cap_log_p_closed"],
            "历史深度至多 floor(log_2 P)+1。",
            DEPTH_TELESCOPE,
        ),
        row(
            "ExplicitLogQuarterAbsorptionClosed",
            result["explicit_log_quarter_absorption_closed"],
            result["explicit_log_quarter_absorption_closed"],
            "在 P>=100000 下，对数深度可被 P^1/4 吸收。",
            f"{PER_LEVEL} AND {TPDEC_TABLE}",
        ),
        row(
            "StrictContractionNotAvailableCertified",
            result["strict_contraction_not_available_certified"],
            result["strict_contraction_not_available_certified"],
            "现有单层 sibling envelope 不含统一 q<1 收缩，不能直接 telescope 成根势能。",
            PER_LEVEL,
        ),
        row(
            "LogAbsorptionCriterionClosed",
            result["log_absorption_criterion_closed"],
            result["log_absorption_criterion_closed"],
            "若每层支撑指数 beta 和 T_PDEC 指数 tau 满足 beta+tau+1/4<0.43，则深度因子可吸收。",
            f"{PER_LEVEL} AND {TPDEC_TABLE}",
        ),
        row(
            "PerLevelColdSupportExponentTableProved",
            False,
            False,
            "尚未证明每层实际冷支撑有 beta<0.18-tau 的同参数指数界。",
            PER_LEVEL,
        ),
        row(
            "ColdSupportDepthTelescopingTableProved",
            False,
            False,
            "对数吸收判据已闭合，但缺每层支撑指数和 T_PDEC 权重表。",
            f"{PER_LEVEL} AND {TPDEC_TABLE}",
        ),
        row(
            "CoreHistoryWeightedSupportMeasureTableProved",
            False,
            False,
            "深度伸缩、T_PDEC 权重和有限 runner 未全部闭合。",
            f"{DEPTH_TELESCOPE} AND {TPDEC_TABLE} AND {FINITE_RUNNER}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的最终矛盾。",
            f"{PER_LEVEL} AND {TPDEC_TABLE} AND {LOAD_LOWER} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造冷支撑深度伸缩证书。"""
    support = load_json("prime-matrix-strict-core-history-weighted-support-measure-router.json")
    target = support.get("next_direct_attack_target") == DEPTH_TELESCOPE
    depth_samples = depth_cap_samples()
    depth_cap_closed = all(item["absorbed"] for item in depth_samples)
    no_contraction = all(item["strict_contraction_witness_fails"] for item in no_contraction_witness_rows())

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_cold_support_depth_telescoping_router",
        "status": "depth_telescoping_reduced_to_per_level_support_exponent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha": ALPHA,
        "p_min": P_MIN,
        "log_absorption_epsilon": LOG_EPSILON,
        "remaining_exponent_after_log_absorption": round(ALPHA - LOG_EPSILON, 6),
        "depth_telescoping_target_imported": target,
        "depth_cap_log_p_closed": True,
        "explicit_log_quarter_absorption_closed": depth_cap_closed,
        "strict_contraction_not_available_certified": no_contraction,
        "log_absorption_criterion_closed": True,
        "same_parameter_per_level_cold_support_exponent_table_proved": False,
        "same_parameter_pdec_threshold_numeric_table_proved": False,
        "finite_cold_history_summation_runner_or_analytic_envelope_proved": False,
        "cold_support_depth_telescoping_contraction_or_log_absorption_table_proved": False,
        "core_history_weighted_support_measure_table_proved": False,
        "core_threshold_summation_dominance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": DEPTH_TELESCOPE,
        "hardpoint_after_router": f"{PER_LEVEL} AND {TPDEC_TABLE}",
        "next_direct_attack_target": PER_LEVEL,
        "parallel_attack_targets": [
            TPDEC_TABLE,
            LOAD_LOWER,
            FINITE_RUNNER,
            NAMED_RETURN,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "telescoping_rows": telescoping_rows(),
        "depth_cap_samples": depth_samples,
        "exponent_budget_rows": exponent_budget_rows(),
        "no_contraction_witness_rows": no_contraction_witness_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ColdSupportDepthTelescopingContractionOrLogAbsorptionTable` 可关闭两个基础环节："
            "实际历史深度至多 `floor(log_2 P)+1`，且在 `P>=100000` 时该对数因子可由 `P^(1/4)` 显式吸收。"
            "但现有兄弟收费/父支撑投影账本没有给出统一严格收缩 `S_{j+1}<=qS_j(q<1)`；"
            "因此不能把全深度支撑直接压成根势能。剩余变成清晰的同参数指数条件："
            "若每层冷支撑 `S_level<=P^beta` 且 `T_PDEC<=P^tau`，需要 `beta+tau+1/4<0.43`。"
            "最新最窄点是 `SameParameterPerLevelColdSupportExponentTable`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 冷支撑深度伸缩/对数吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"depth_telescoping_target_imported={fmt_bool(result['depth_telescoping_target_imported'])}",
        f"depth_cap_log_p_closed={fmt_bool(result['depth_cap_log_p_closed'])}",
        f"explicit_log_quarter_absorption_closed={fmt_bool(result['explicit_log_quarter_absorption_closed'])}",
        f"strict_contraction_not_available_certified={fmt_bool(result['strict_contraction_not_available_certified'])}",
        f"log_absorption_criterion_closed={fmt_bool(result['log_absorption_criterion_closed'])}",
        f"same_parameter_per_level_cold_support_exponent_table_proved={fmt_bool(result['same_parameter_per_level_cold_support_exponent_table_proved'])}",
        f"cold_support_depth_telescoping_contraction_or_log_absorption_table_proved={fmt_bool(result['cold_support_depth_telescoping_contraction_or_log_absorption_table_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 伸缩公式",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["telescoping_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['name'])}`",
                    table_cell(item["formula"]),
                    f"`{table_cell(item['status'])}`",
                    table_cell(item["meaning"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 对数吸收核验",
            "",
            "| P | depth cap | P^1/4 | absorbed | margin |",
            "| ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for item in result["depth_cap_samples"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["P"]),
                    str(item["depth_cap"]),
                    str(item["P_epsilon"]),
                    f"`{fmt_bool(item['absorbed'])}`",
                    str(item["margin"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 3. 指数预算",
            "",
            "| beta support | tau T_PDEC | log epsilon | total | below alpha | margin |",
            "| ---: | ---: | ---: | ---: | --- | ---: |",
        ]
    )
    for item in result["exponent_budget_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["beta_per_level_support"]),
                    str(item["tau_tpdec_weight"]),
                    str(item["log_epsilon"]),
                    str(item["total_exponent"]),
                    f"`{fmt_bool(item['below_alpha'])}`",
                    str(item["margin"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 4. 无严格收缩见证",
            "",
            "| level | S_level | S_next | nonexpansion valid | strict contraction needed | witness fails strict contraction |",
            "| ---: | ---: | ---: | --- | --- | --- |",
        ]
    )
    for item in result["no_contraction_witness_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item["level"]),
                    str(item["S_level"]),
                    str(item["S_next"]),
                    f"`{fmt_bool(item['nonexpansion_valid'])}`",
                    table_cell(item["strict_contraction_factor_needed"]),
                    f"`{fmt_bool(item['strict_contraction_witness_fails'])}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 6. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            f"- 并行：`{TPDEC_TABLE}`、`{LOAD_LOWER}`、`{FINITE_RUNNER}`。",
            "- 边界：本步关闭深度 cap 与显式对数吸收判据；未证明每层支撑指数，因此不闭合最终命题。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """入口函数。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"explicit_log_quarter_absorption_closed={fmt_bool(result['explicit_log_quarter_absorption_closed'])}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
