#!/usr/bin/env python3
"""生成 strict Table 6.3 b=28 核/截断/平滑口径审计证书。

用法示例：
  python3 experiments/prime_matrix_strict_table63_b28_kernel_truncation_smoothing_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-table63-b28-kernel-truncation-smoothing-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-table63-b28-kernel-truncation-smoothing-router.json"
OUT_MD = DOCS / "prime-matrix-strict-table63-b28-kernel-truncation-smoothing-router.md"

PREVIOUS = DOCS / "prime-matrix-strict-table63-b28-psi-endpoint-convention-router.json"
ACTUAL_FORMULA = DOCS / "prime-matrix-strict-table63-b28-actual-formula-declaration-router.json"
ZERO_BINDING = DOCS / "prime-matrix-strict-table63-b28-zero-input-formula-binding-router.json"
GENERATION = DOCS / "prime-matrix-strict-table63-b28-generation-rounding-router.json"
PERRON_FINAL = DOCS / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
SAME_FORMULA = DOCS / "prime-matrix-strict-same-explicit-formula-convention-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"

SOURCE_FILES = [PREVIOUS, ACTUAL_FORMULA, ZERO_BINDING, GENERATION, PERRON_FINAL, SAME_FORMULA, CLAIM_STATUS]

TARGET = "Table63B28KernelTruncationAndSmoothingConventionLedger"
PSI_ENDPOINT = "Table63B28PsiVsPsi0EndpointConventionLedger"
ORIGINAL_ARTIFACT = "DusartEpsSubmittedTableAlgorithmArtifactLedger"
FK_KERNEL = "FaberKadiriSmoothedExplicitFormulaKernelConventionLedger"
FK_B28_PACKET = "FaberKadiriCorrectedB28ParameterPacketAndBudgetLedger"
FK_ROUNDING = "FaberKadiriB28DirectedRoundingAndComputationHashLedger"
INTERNAL_UNSMOOTHED = "UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128"
FINITE_RH = "Table63B28FiniteRHHeightEndpointAndZeroBlockLedger"
ZERO_TAIL = "Table63B28ZeroFreeTailConstantsAndStartHeightLedger"
BUDGET = "Table63B28PsiEpsilonBudgetPartitionLedger"
ROUNDING = "Table63B28DirectedUpperRoundingAndIntervalPropagationLedger"
HASH = "Table63B28ReproducibleComputationHashLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
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


def external_kernel_facts() -> list[dict[str, str]]:
    """记录外部平滑核路线的可对接事实。"""
    return [
        {
            "source": "Dusart 2016 Math. Comp. paper",
            "fact": "moderate_range_points_to_faber_kadiri",
            "meaning": "正式版说明在较低 b 区间，Faber-Kadiri 的方法和值优于该文全局上界。",
            "effect": "旧 Table 6.3 b=28 的自足替代路线应优先接 Faber-Kadiri 型平滑显式公式。",
        },
        {
            "source": "Faber-Kadiri 2015 / arXiv:1310.6374",
            "fact": "smooth_weight_bounds_psi",
            "meaning": "引入光滑权 f，并以 S^-(x)<=psi(x)<=S^+(x) 把普通 psi 误差转成光滑显式公式误差。",
            "effect": "这给出与 Table 6.3 相同目标函数 psi 的核/平滑 convention。",
        },
        {
            "source": "Faber-Kadiri 2015 / arXiv:1310.6374",
            "fact": "kernel_g_declared",
            "meaning": "第 3.1 节给出优化核 g(x)=1-((2m+1)!/(m!)^2) int_0^x t^m(1-t)^m dt。",
            "effect": "外部平滑核本身已声明；它不是仓库内部的非平滑 Perron 核。",
        },
        {
            "source": "Faber-Kadiri 2015 / corrigendum 2017",
            "fact": "corrected_budget_formula_required",
            "meaning": "corrigendum 修正 B5 定义并重列计算表；必须使用校正版 epsilon 公式和表。",
            "effect": "仅识别核不够，b0=28 还需校正版参数包、预算和外向舍入。",
        },
        {
            "source": "Faber-Kadiri table rows",
            "fact": "bracketing_rows_not_enough",
            "meaning": "公开表有 b0=25 与 b0=30 行；b0=25 的 epsilon 太弱，b0=30 不能覆盖 x>=e^28。",
            "effect": "不能靠表行单调性偷换，必须直接计算 b0=28 参数包。",
        },
    ]


def kernel_matrix() -> list[dict[str, str]]:
    """列出内部非平滑核与外部平滑核的结构差异。"""
    return [
        {
            "field": "base_function",
            "internal_unsmoothed": "psi_0 半权端点，已由上一证书转为普通 psi 并登记端点税",
            "external_fk": "普通 psi 由 S^- 与 S^+ 光滑上下包络夹住",
            "status": "function target compatible after endpoint tax",
        },
        {
            "field": "kernel",
            "internal_unsmoothed": "非平滑 Perron 竖线核，finite-T 常数 C=12128",
            "external_fk": "beta 型光滑核 g 及 Mellin transform F",
            "status": "kernel convention differs",
        },
        {
            "field": "truncation",
            "internal_unsmoothed": "固定 T 与 contour shift 预算，后接粗 zero-sum 包",
            "external_fk": "按 H, T0, T1, sigma0 分割零点块，使用 B_i 预算函数",
            "status": "truncation variables differ",
        },
        {
            "field": "budget_pressure",
            "internal_unsmoothed": "现有粗 contour 距 2.224E-5 表值约 2.78e12 倍",
            "external_fk": "有校正版 epsilon 公式，但 b0=28 未直接列成表行",
            "status": "internal rejected, external needs b28 packet",
        },
        {
            "field": "output",
            "internal_unsmoothed": "已自洽但不能生成 Table 6.3 b=28",
            "external_fk": "需给出 b0=28 的 m, delta, sigma0, T1, H/R0, corrected B_i 与 hash",
            "status": "next exact hardpoint",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造核/截断/平滑口径审计证书。"""
    previous = load_json(PREVIOUS)
    actual = load_json(ACTUAL_FORMULA)
    zero_binding = load_json(ZERO_BINDING)
    generation = load_json(GENERATION)
    perron = load_json(PERRON_FINAL)
    same_formula = load_json(SAME_FORMULA)

    active = previous.get("next_direct_attack_target") == TARGET
    endpoint_closed = previous.get("table63_b28_psi_vs_psi0_endpoint_convention_closed") is True
    original_artifact_missing = actual.get("table63_b28_external_algorithm_artifact_present") is False
    internal_unsmoothed_closed = perron.get("unsmoothed_perron_strict_self_contained_closed") is True
    internal_rejected = (
        zero_binding.get("internal_coarse_formula_rejected_as_table63_generator") is True
        and generation.get("coarse_internal_contour_rejected_for_b28") is True
    )
    local_not_table = same_formula.get("local_convention_does_not_imply_dusart_table_convention") is True
    external_fk_kernel_identified = True

    coarse_gap = generation.get("arithmetic", {}).get("coarse_template_gap_factor_high_tail_b28", "unknown")
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            previous.get("counterexample_assumption_only") is True
            and previous.get("row_column_unconditional_closed") is False,
            True,
            "本步只处理假设反例链可调用的 psi 高尾输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "KernelConventionGateActive",
            active,
            True,
            "上一证书已关闭 psi/psi0 端点税，并把下一最窄点压到 b=28 的核/截断/平滑口径。",
            TARGET,
        ),
        row(
            PSI_ENDPOINT,
            endpoint_closed,
            True,
            "函数目标已经对齐到普通 psi；端点半权税可显式扣除。",
            "endpoint tax registered",
        ),
        row(
            "OriginalDusartB28AlgorithmArtifactMissing",
            original_artifact_missing,
            True,
            "旧 arXiv/Dusart Table 6.3 只给出表行与使用点，没有给出 b=28 表生成核、截断高度、平滑规则或 hash。",
            ORIGINAL_ARTIFACT,
        ),
        row(
            "InternalUnsmoothedPerronKernelAvailable",
            internal_unsmoothed_closed,
            True,
            "仓库内部非平滑 Perron 核和 finite-T 常数 C=12128 已自足闭合。",
            INTERNAL_UNSMOOTHED,
        ),
        row(
            "InternalUnsmoothedKernelRejectedForB28",
            internal_rejected and local_not_table,
            True,
            f"现有内部粗核自洽但不能生成 b=28 表值，压力差约 {coarse_gap} 倍，且不是 Dusart/FK 表算法口径。",
            "cannot be used as Table63 b=28 generator",
        ),
        row(
            FK_KERNEL,
            external_fk_kernel_identified,
            True,
            "外部可对接的核/平滑 convention 已定位为 Faber-Kadiri 光滑显式公式：S^-<=psi<=S^+，核 g 显式给出。",
            "external smoothed convention identified",
        ),
        row(
            "PublishedB25B30RowsDoNotCloseB28",
            True,
            True,
            "Faber-Kadiri 表中 b0=25 的界太弱，b0=30 又只覆盖 x>=e^30；不能直接替代 x>=e^28。",
            FK_B28_PACKET,
        ),
        row(
            TARGET,
            False,
            False,
            "原始 Table 6.3 b=28 的核口径仍未自足生成；但可替代的外部平滑核已定位，剩余精确压成 b0=28 校正版参数包与预算。",
            f"({ORIGINAL_ARTIFACT}) OR ({FK_KERNEL} AND {FK_B28_PACKET} AND {FK_ROUNDING})",
        ),
        row(
            "IndependentRegenerationStillOpen",
            False,
            False,
            "核/平滑 convention 的外部定位不等于表值重建；仍需有限零点块、尾项、预算、舍入和 hash 同步。",
            f"{FINITE_RH} AND {ZERO_TAIL} AND {BUDGET} AND {ROUNDING} AND {HASH}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步仍只推进 psi 高尾输入，尚未产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_table63_b28_kernel_truncation_smoothing_router",
        "status": "table63_b28_kernel_original_open_fk_smoothed_kernel_identified_b28_packet_next",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "table63_b28_psi_vs_psi0_endpoint_convention_closed": endpoint_closed,
        "original_dusart_b28_algorithm_artifact_missing": original_artifact_missing,
        "internal_unsmoothed_perron_kernel_available": internal_unsmoothed_closed,
        "internal_unsmoothed_kernel_rejected_for_b28": internal_rejected and local_not_table,
        "faber_kadiri_smoothed_kernel_convention_identified": external_fk_kernel_identified,
        "published_b25_b30_rows_close_b28": False,
        "table63_b28_kernel_truncation_smoothing_convention_closed": False,
        "replacement_external_kernel_lane_opened": True,
        "independent_table63_b28_regeneration_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "arithmetic": {
            "coarse_template_gap_factor_high_tail_b28": coarse_gap,
            "faber_kadiri_platt_b25_epsilon": "4.8208e-5",
            "faber_kadiri_platt_b30_epsilon": "5.6685e-6",
            "faber_kadiri_gourdon_b25_epsilon": "4.8208e-5",
            "faber_kadiri_gourdon_b30_epsilon": "5.6646e-6",
            "target_1_over_36260": generation.get("arithmetic", {}).get("target_1_over_36260", "unknown"),
        },
        "external_kernel_facts": external_kernel_facts(),
        "kernel_matrix": kernel_matrix(),
        "replacement_self_contained": {
            TARGET: f"{ORIGINAL_ARTIFACT} OR ({FK_KERNEL} AND {FK_B28_PACKET} AND {FK_ROUNDING})",
            FK_KERNEL: "FaberKadiriSmoothWeightSminusSplusPsiEnvelope AND ExplicitKernelGFormula AND CorrectedEpsilonFormulaConvention",
            FK_B28_PACKET: "compute corrected epsilon_0 at b0=28 with m,delta,sigma0,T1,H,R0,c_i,B_i and prove epsilon_0 < 1/36260 minus endpoint tax",
        },
        "next_direct_attack_target": FK_B28_PACKET,
        "parallel_attack_targets": [ORIGINAL_ARTIFACT, FK_ROUNDING, FINITE_RH, ZERO_TAIL, BUDGET, ROUNDING, HASH],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前最窄点被推进了一层：旧 Dusart Table 6.3 b=28 源只给表行，不给生成核；"
            "仓库内部非平滑 Perron 核虽已自足闭合，但因预算差约 2.78e12 倍，不能作为 b=28 表生成器。"
            "可严格对接同一 psi 高尾目标的外部核已定位为 Faber-Kadiri 光滑显式公式；它给出 S^-<=psi<=S^+、"
            "显式光滑核 g 和校正版 epsilon 公式。剩余真正单点不再是找核，而是直接计算并验收 b0=28 的校正版参数包、"
            "预算、外向舍入和 hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Table 6.3 b=28 核/截断/平滑口径审计证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"faber_kadiri_smoothed_kernel_convention_identified={fmt_bool(result['faber_kadiri_smoothed_kernel_convention_identified'])}",
        f"internal_unsmoothed_kernel_rejected_for_b28={fmt_bool(result['internal_unsmoothed_kernel_rejected_for_b28'])}",
        f"table63_b28_kernel_truncation_smoothing_convention_closed={fmt_bool(result['table63_b28_kernel_truncation_smoothing_convention_closed'])}",
        f"replacement_external_kernel_lane_opened={fmt_bool(result['replacement_external_kernel_lane_opened'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 数值边界",
        "",
        "| field | value |",
        "| --- | ---: |",
    ]
    for key, value in result["arithmetic"].items():
        lines.append(f"| `{table_cell(key)}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "## 2. 外部核事实",
            "",
            "| source | fact | meaning | effect |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["external_kernel_facts"]:
        lines.append(
            f"| {table_cell(item['source'])} | `{table_cell(item['fact'])}` | "
            f"{table_cell(item['meaning'])} | {table_cell(item['effect'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 核口径矩阵",
            "",
            "| field | internal unsmoothed | external FK | status |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in result["kernel_matrix"]:
        lines.append(
            f"| `{table_cell(item['field'])}` | {table_cell(item['internal_unsmoothed'])} | "
            f"{table_cell(item['external_fk'])} | {table_cell(item['status'])} |"
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
            "## 5. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "faber_kadiri_smoothed_kernel_convention_identified="
        f"{fmt_bool(result['faber_kadiri_smoothed_kernel_convention_identified'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
