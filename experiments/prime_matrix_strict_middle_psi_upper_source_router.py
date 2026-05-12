#!/usr/bin/env python3
"""生成 strict 中段 psi 上界 1.00002841 来源路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_middle_psi_upper_source_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-middle-psi-upper-source-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-middle-psi-upper-source-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-middle-psi-upper-source-router.md"

ALGORITHM = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-algorithm-router.json"
PSI_TABLE = MONOGRAPH / "prime-matrix-strict-schoenfeld-dusart-psi-table-router.json"
DUSART_SPLICE = MONOGRAPH / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [ALGORITHM, PSI_TABLE, DUSART_SPLICE, CLAIM_STATUS]

TARGET = "MiddlePsiUpper100002841SourceLedger"
MIDDLE_INTERVAL = "MiddleFiniteIntervalPsiCover8e11ToE28Ledger"
EXACT_DATA = "DelegliseRivatPsiComputationDataAndHashLedger"
TABLE63_INTERPOLATION = "Table63InterpolationNotEnoughFor100002841Ledger"
TABLE62_POINT = "Table62ExactPointValuesNotIntervalCoverLedger"
ROUNDING = "MiddlePsiUpperDirectedRoundingLedger"
INTERVAL = "PsiEpsilonIntervalPropagationAndMonotonicityLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

DUSART_PDF = "https://arxiv.org/pdf/1002.0442"

X_LEFT = 8.0e11
X_RIGHT = math.exp(28)
B_LEFT = math.log(X_LEFT)
EPS27 = 3.368e-5
EPS28 = 2.224e-5
TARGET_EPS = 2.841e-5
TARGET_RATIO = 1.00002841

THETA_8E11 = 799_999_133_776.084743
PSI_MINUS_THETA_8E11 = 904_203.190001
PSI_8E11 = THETA_8E11 + PSI_MINUS_THETA_8E11
THETA_1E12 = 999_999_030_333.096225
PSI_MINUS_THETA_1E12 = 1_009_803.669232
PSI_1E12 = THETA_1E12 + PSI_MINUS_THETA_1E12


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """稳定输出浮点。"""
    return f"{value:.15e}"


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


def candidate_rows() -> list[dict[str, Any]]:
    """检验几个可能来源是否足以推出 1.00002841。"""
    linear_eps = EPS27 + (B_LEFT - 27.0) * (EPS28 - EPS27)
    log_linear_eps = math.exp(math.log(EPS27) + (B_LEFT - 27.0) * (math.log(EPS28) - math.log(EPS27)))
    candidates = [
        {
            "candidate": "Table 6.3 b=27 bound",
            "formula": "1 + 3.368e-5",
            "ratio": 1.0 + EPS27,
            "defect_vs_target": 1.0 + EPS27 - TARGET_RATIO,
            "sufficient": 1.0 + EPS27 <= TARGET_RATIO,
            "reason": "valid from e^27, but too weak for the P5.1 middle constant",
        },
        {
            "candidate": "Table 6.3 b=28 bound",
            "formula": "1 + 2.224e-5",
            "ratio": 1.0 + EPS28,
            "defect_vs_target": 1.0 + EPS28 - TARGET_RATIO,
            "sufficient": False,
            "reason": "numerically strong, but only valid from e^28, not on 8e11<=x<e^28",
        },
        {
            "candidate": "linear interpolation of rounded b=27,28 eps",
            "formula": "eps27 + (log(8e11)-27)(eps28-eps27)",
            "ratio": 1.0 + linear_eps,
            "defect_vs_target": 1.0 + linear_eps - TARGET_RATIO,
            "sufficient": 1.0 + linear_eps <= TARGET_RATIO,
            "reason": "weaker than the target and no interpolation theorem is registered",
        },
        {
            "candidate": "log-linear interpolation of rounded b=27,28 eps",
            "formula": "exp((1-t)log eps27 + t log eps28)",
            "ratio": 1.0 + log_linear_eps,
            "defect_vs_target": 1.0 + log_linear_eps - TARGET_RATIO,
            "sufficient": 1.0 + log_linear_eps <= TARGET_RATIO,
            "reason": "still slightly above target and no interpolation theorem is registered",
        },
        {
            "candidate": "Table 6.2 point value at 8e11",
            "formula": "(theta(8e11)+psi-theta(8e11))/(8e11)",
            "ratio": PSI_8E11 / X_LEFT,
            "defect_vs_target": PSI_8E11 / X_LEFT - TARGET_RATIO,
            "sufficient": PSI_8E11 / X_LEFT <= TARGET_RATIO,
            "reason": "strong at the point, but does not cover the whole interval",
        },
        {
            "candidate": "Table 6.2 point value at 1e12",
            "formula": "(theta(1e12)+psi-theta(1e12))/(1e12)",
            "ratio": PSI_1E12 / 1.0e12,
            "defect_vs_target": PSI_1E12 / 1.0e12 - TARGET_RATIO,
            "sufficient": PSI_1E12 / 1.0e12 <= TARGET_RATIO,
            "reason": "strong at the point, but does not cover jumps between points",
        },
    ]
    return candidates


def build_result() -> dict[str, Any]:
    """构造中段 psi 上界来源证书。"""
    algorithm = load_json(ALGORITHM)
    psi_table = load_json(PSI_TABLE)
    splice = load_json(DUSART_SPLICE)
    active = algorithm.get("next_direct_attack_target") == TARGET
    p51_use_site_closed = algorithm.get("p51_dependency_graph_closed") is True
    middle_needed = psi_table.get("middle_psi_upper_table_closed") is False
    splice_tiny = splice.get("dusart_analytic_kernel_threshold_arithmetic_splice_closed") is True
    candidates = candidate_rows()
    interpolation_rejected = not candidates[0]["sufficient"] and not candidates[2]["sufficient"] and not candidates[3]["sufficient"]
    point_values_not_cover = candidates[4]["sufficient"] and candidates[5]["sufficient"]
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            algorithm.get("counterexample_assumption_only") is True
            and algorithm.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计假设反例链可调用的中段 psi 上界来源，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "MiddlePsiUpperSourceGateActive",
            active,
            True,
            "psi epsilon 表算法证书已把下一最窄点压到 1.00002841 的来源账本。",
            TARGET,
        ),
        row(
            "P51UseSiteLocated",
            p51_use_site_closed and middle_needed,
            True,
            "P5.1 中段确实需要 psi(x)<1.00002841x 覆盖 8e11<=x<=e^28。",
            "use site closed, source still open",
        ),
        row(
            "TinySpliceSlackMakesSourceCritical",
            splice_tiny,
            True,
            "该常数经 psi-theta 下界接入 theta 目标后只剩约 4.46e-11 余量，不能粗化。",
            ROUNDING,
        ),
        row(
            TABLE63_INTERPOLATION,
            interpolation_rejected,
            True,
            "Table 6.3 的 b=27/28 舍入值和简单插值都不能自足推出 1.00002841。",
            MIDDLE_INTERVAL,
        ),
        row(
            TABLE62_POINT,
            point_values_not_cover,
            True,
            "Table 6.2 在 8e11 和 1e12 的点值远强于目标，但点值不是整段覆盖证书。",
            MIDDLE_INTERVAL,
        ),
        row(
            MIDDLE_INTERVAL,
            False,
            False,
            "需要覆盖 8e11<=x<=e^28 的有限区间 psi 上界证书，含节点、跳点、最大值和间隙控制。",
            f"{EXACT_DATA} AND {INTERVAL}",
        ),
        row(
            EXACT_DATA,
            False,
            False,
            "需要 Deléglise-Rivat 或等价 psi 精确计算数据、算法、版本和 hash；当前仓库没有该数据。",
            "machine-readable psi computation archive",
        ),
        row(
            ROUNDING,
            False,
            False,
            "需要证明 1.00002841 是外向上舍入值，且舍入误差仍保留中段拼接余量。",
            "directed rounding log",
        ),
        row(
            TARGET,
            False,
            False,
            "当前只定位到使用点并排除几个不足来源；尚未证明 1.00002841 的生成或覆盖。",
            f"{MIDDLE_INTERVAL} AND {EXACT_DATA} AND {ROUNDING}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "中段 psi 常数来源审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_middle_psi_upper_source_router",
        "status": "middle_psi_upper_100002841_use_site_closed_source_and_interval_cover_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "middle_psi_upper_use_site_closed": p51_use_site_closed and middle_needed,
        "tiny_splice_slack_makes_source_critical": splice_tiny,
        "table63_interpolation_not_enough": interpolation_rejected,
        "table62_point_values_not_interval_cover": point_values_not_cover,
        "middle_finite_interval_psi_cover_closed": False,
        "deleglise_rivat_psi_data_hash_closed": False,
        "middle_psi_upper_directed_rounding_closed": False,
        "middle_psi_upper_100002841_source_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "numeric_context": {
            "x_left": X_LEFT,
            "x_right_e28": X_RIGHT,
            "log_x_left": B_LEFT,
            "target_ratio": TARGET_RATIO,
            "target_eps": TARGET_EPS,
            "psi_8e11_ratio": PSI_8E11 / X_LEFT,
            "psi_1e12_ratio": PSI_1E12 / 1.0e12,
        },
        "candidate_tests": candidates,
        "external_source": {
            "id": "Dusart arXiv:1002.0442",
            "url": DUSART_PDF,
            "role": "use-site and tables source; not a reproducible middle interval cover",
        },
        "replacement_self_contained": {
            TARGET: f"{MIDDLE_INTERVAL} AND {EXACT_DATA} AND {ROUNDING}",
            MIDDLE_INTERVAL: "finite interval cover of psi(x)/x on 8e11<=x<=e^28 with directed rounding",
        },
        "next_direct_attack_target": MIDDLE_INTERVAL,
        "parallel_attack_targets": [EXACT_DATA, ROUNDING, INTERVAL],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "1.00002841 的使用点已明确，但来源尚未闭合。Table 6.3 的 b=27 界太弱，"
            "b=28 界只从 e^28 起有效；用 b=27/28 舍入值做线性或 log-线性插值也不能证明该常数。"
            "Table 6.2 的 8e11 和 1e12 点值很强，但点值不是整段覆盖。"
            "因此中段必须补一个有限区间 psi 覆盖证书，或提供 Deléglise-Rivat 等价精确计算数据和 hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 中段 psi 上界 1.00002841 来源路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"middle_psi_upper_use_site_closed={fmt_bool(result['middle_psi_upper_use_site_closed'])}",
        f"tiny_splice_slack_makes_source_critical={fmt_bool(result['tiny_splice_slack_makes_source_critical'])}",
        f"table63_interpolation_not_enough={fmt_bool(result['table63_interpolation_not_enough'])}",
        f"table62_point_values_not_interval_cover={fmt_bool(result['table62_point_values_not_interval_cover'])}",
        f"middle_finite_interval_psi_cover_closed={fmt_bool(result['middle_finite_interval_psi_cover_closed'])}",
        f"deleglise_rivat_psi_data_hash_closed={fmt_bool(result['deleglise_rivat_psi_data_hash_closed'])}",
        f"middle_psi_upper_directed_rounding_closed={fmt_bool(result['middle_psi_upper_directed_rounding_closed'])}",
        f"middle_psi_upper_100002841_source_closed={fmt_bool(result['middle_psi_upper_100002841_source_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 数值上下文",
        "",
        "```text",
    ]
    for key, value in result["numeric_context"].items():
        lines.append(f"{key}={fmt_float(value)}")
    lines.extend(["```", "", "## 2. 候选来源检验", "", "| candidate | formula | ratio | defect_vs_target | sufficient | reason |", "| --- | --- | ---: | ---: | --- | --- |"])
    for item in result["candidate_tests"]:
        lines.append(
            "| {candidate} | {formula} | `{ratio}` | `{defect}` | `{sufficient}` | {reason} |".format(
                candidate=table_cell(item["candidate"]),
                formula=table_cell(item["formula"]),
                ratio=fmt_float(float(item["ratio"])),
                defect=fmt_float(float(item["defect_vs_target"])),
                sufficient=fmt_bool(item["sufficient"]),
                reason=table_cell(item["reason"]),
            )
        )
    lines.extend(["", "## 3. 外部边界", "", f"- `{result['external_source']['id']}`：{result['external_source']['url']}；{result['external_source']['role']}", "", "## 4. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 5. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 6. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
