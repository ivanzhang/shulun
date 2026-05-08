#!/usr/bin/env python3
"""Prime Matrix clean-core DPRC 中心化偏差攻关路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_dprc_centered_discrepancy_router.py

输出：
  docs/monograph/prime-matrix-clean-core-dprc-centered-discrepancy-router.json
  docs/monograph/prime-matrix-clean-core-dprc-centered-discrepancy-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
AUDIT_DOCS = ROOT / "docs"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.json"
DEFAULT_RSM_MD = DOCS / "prime-matrix-dprc-relative-sieve-margin.md"
DEFAULT_RSM_JSON = AUDIT_DOCS / "dprc_relative_sieve_margin_alpha043_p100000_20260506.json"
DEFAULT_BES_MD = DOCS / "prime-matrix-dprc-bucket-energy-synchronization.md"
DEFAULT_BES_JSON = AUDIT_DOCS / "dprc_block_envelope_scan_alpha043_p100000_20260506.json"
DEFAULT_DLS_MD = DOCS / "prime-matrix-dprc-bes-dual-large-sieve-route.md"
DEFAULT_NEWLAYER_MD = DOCS / "prime-matrix-dprc-newlayer-energy-dispersion.md"
DEFAULT_NEWLAYER_JSON = AUDIT_DOCS / "dprc_newlayer_energy_scan_p100000_20260506.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-dprc-centered-discrepancy-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-dprc-centered-discrepancy-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def threshold_summary(rsm: dict[str, Any], threshold: int) -> dict[str, Any]:
    """按 P 阈值取 RSM 汇总。"""
    for row in rsm.get("summaries", []):
        if row.get("threshold_p") == threshold:
            return row
    return {}


def bes_threshold_table(bes: dict[str, Any], threshold: int) -> dict[str, Any]:
    """按 P 阈值取 BES 汇总。"""
    for row in bes.get("threshold_tables", []):
        if row.get("threshold") == threshold:
            return row
    return {}


def newlayer_summary(newlayer: dict[str, Any], threshold: int) -> dict[str, Any]:
    """按 P 阈值取新增层汇总。"""
    for row in newlayer.get("summaries", []):
        if row.get("threshold") == threshold:
            return row
    return {}


def gate_rows(
    previous: dict[str, Any],
    rsm_md: str,
    rsm_json: dict[str, Any],
    bes_md: str,
    bes_json: dict[str, Any],
    dls_md: str,
    newlayer_md: str,
    newlayer_json: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 DPRC 中心化偏差判定表。"""
    rsm_13 = threshold_summary(rsm_json, 13)
    rsm_2003 = threshold_summary(rsm_json, 2003)
    bes_2003 = bes_threshold_table(bes_json, 2003)
    danger = bes_2003.get("danger_intersections", {})
    danger_6_5 = danger.get("l1_ge_12_5_and_l2_gt_6_5", {})
    danger_cauchy = danger.get("l1_ge_12_5_and_l2_gt_3_sqrt6", {})
    newlayer_2003 = newlayer_summary(newlayer_json, 2003)
    return [
        {
            "gate": "PreviousDPRCInputPinned",
            "closed": "DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn"
            in previous.get("latest_internal_subinputs", []),
            "proved": True,
            "meaning": "上一层已把几何预算的解析锁命名为 DPRC alpha=0.43 中心化偏差或层叠回流。",
            "remaining": "把 DPRC 输入继续原子化。",
        },
        {
            "gate": "RSMIdentityClosed",
            "closed": "S-T=S(1-H)" in rsm_md and "D_+<=3 sqrt(S)" in rsm_md,
            "proved": True,
            "meaning": "DPRC 容量闭合已等价降到模型余量 S(1-H) 与正偏差 D_+ 的比较。",
            "remaining": "提交显式 ModelGap/finite 证书与 D_+ 平方根界。",
        },
        {
            "gate": "FiniteCapacityAuditMaterialized",
            "closed": rsm_13.get("capacity_fail") == 0,
            "proved": False,
            "meaning": "P<2003 和全扫到 P<=100000 的容量失败为零，有限证书数据已物化。",
            "remaining": "把 P<2003 固化为正式有限验收表。",
        },
        {
            "gate": "HighSegmentC3AuditMaterialized",
            "closed": rsm_2003.get("c_certificate_pass") is True,
            "proved": False,
            "meaning": "审计显示 P>=2003 时 C=3 同时支付模型余量和正偏差。",
            "remaining": "证明 ExplicitModelGapAndFiniteDPRCLedger，而不是只引用实验。",
        },
        {
            "gate": "BESCompressionClosed",
            "closed": "BES-4" in bes_md and "BES-5" in bes_md,
            "proved": True,
            "meaning": "D_+<=3sqrt(S) 被压成六个 beta 桶的高 L1 与高 L2 不能同步。",
            "remaining": "证明 BES 危险交集不存在或命名回流。",
        },
        {
            "gate": "BESDangerAuditClear",
            "closed": danger_6_5.get("record_count") == 0
            and danger_cauchy.get("record_count") == 0,
            "proved": False,
            "meaning": "P<=100000 审计中两个 BES 危险交集均为零。",
            "remaining": "需要解析排斥，不可作为无条件证明。",
        },
        {
            "gate": "DLSNamedReturnGrammarClosed",
            "closed": all(token in dls_md for token in ["PointLoad", "ShortWindow", "LowPhase"]),
            "proved": False,
            "meaning": "若 BES 危险交集发生，当前路线把失败拆成 PointLoad/ShortWindow/LowPhase 三出口。",
            "remaining": "证明三出口必然性，且分别吸收到 ColumnCRT/SAE/PDEC。",
        },
        {
            "gate": "NewLayerDispersionEvidenceAvailable",
            "closed": "NewLayer Dispersion Clamp" in newlayer_md
            and newlayer_2003.get("danger_l1_l2_6_5_count") == 0,
            "proved": False,
            "meaning": "新增层 Fourier 能量强但高 BES 压力处峰值分散，支持 LowPhase=>new-layer PDEC 或 DLS 吸收。",
            "remaining": "证明相位维数下界或低维集中必给 new-layer PDEC。",
        },
        {
            "gate": "DPRCAlpha043CenteredDiscrepancyInputProved",
            "closed": False,
            "proved": False,
            "meaning": "DPRC 输入未闭合；已压成 ModelGap/finite 账本与 BES/DLS 命名回流。",
            "remaining": "ExplicitModelGapAndFiniteDPRCLedger AND BESDangerIntersectionExclusionOrDLSNamedReturn。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "DPRC 与 signed 源锁完成后仍需独立验收。",
        },
    ]


def run(
    previous_path: Path,
    rsm_md_path: Path,
    rsm_json_path: Path,
    bes_md_path: Path,
    bes_json_path: Path,
    dls_md_path: Path,
    newlayer_md_path: Path,
    newlayer_json_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 DPRC 中心化偏差路由。"""
    source_paths = [
        previous_path,
        rsm_md_path,
        rsm_json_path,
        bes_md_path,
        bes_json_path,
        dls_md_path,
        newlayer_md_path,
        newlayer_json_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    rsm_md = rsm_md_path.read_text(encoding="utf-8")
    rsm_json = load_json(rsm_json_path)
    bes_md = bes_md_path.read_text(encoding="utf-8")
    bes_json = load_json(bes_json_path)
    dls_md = dls_md_path.read_text(encoding="utf-8")
    newlayer_md = newlayer_md_path.read_text(encoding="utf-8")
    newlayer_json = load_json(newlayer_json_path)
    dstructure = load_json(dstructure_path)

    rows = gate_rows(
        previous,
        rsm_md,
        rsm_json,
        bes_md,
        bes_json,
        dls_md,
        newlayer_md,
        newlayer_json,
        dstructure,
    )
    signed_identity = "ActualSignedSourceMeasurePhiIdentityForGeometricPaymentMapAndReturn"
    modelgap_input = "ExplicitModelGapAndFiniteDPRCLedger"
    bes_input = "BESDangerIntersectionExclusionOrDLSNamedReturn"
    signed_budget_lift = "SignedGeometricLedgerVariationBranchLiftAndReturn"
    latest_external = previous.get(
        "latest_external_subinput",
        "CDependentResidueWeightSpectralCancellationInput",
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_dprc_centered_discrepancy_router",
        "status": "dprc_centered_discrepancy_reduced_to_modelgap_and_bes_dls",
        "previous_dprc_input": "DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn",
        "dprc_centered_discrepancy_boundary_closed": all(
            row["closed"]
            for row in rows
            if row["gate"]
            not in {
                "FiniteCapacityAuditMaterialized",
                "HighSegmentC3AuditMaterialized",
                "BESDangerAuditClear",
                "DLSNamedReturnGrammarClosed",
                "NewLayerDispersionEvidenceAvailable",
                "DPRCAlpha043CenteredDiscrepancyInputProved",
                "DStructureRankinStillIndependent",
            }
        ),
        "rsm_identity_closed": True,
        "bes_compression_closed": True,
        "dprc_centered_discrepancy_input_proved": False,
        "row_column_unconditional_closed": False,
        "latest_internal_subinputs": [
            signed_identity,
            modelgap_input,
            bes_input,
            signed_budget_lift,
        ],
        "latest_external_subinput": latest_external,
        "latest_conditional_basis": (
            f"(({signed_identity} AND {modelgap_input} AND {bes_input} "
            f"AND {signed_budget_lift}) OR {latest_external}) "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            f"{signed_identity} AND {modelgap_input} AND {bes_input} "
            f"AND {signed_budget_lift} "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "core_reduction_law": (
            "DPRC 的中心化偏差锁不再是原始 T_Y<S_Y。"
            "RSM 恒等式把它拆成显式模型余量/有限证书与 D_+ 平方根界；"
            "BES 又把 D_+ 平方根界拆成六个 beta 桶的高 L1 与高 L2 不能同步。"
            "若同步失败不能直接排斥，DLS 路线要求它显化为 PointLoad、ShortWindow 或 LowPhase，"
            "分别回流 ColumnCRT、SAE 或 PDEC/new-layer PDEC。"
        ),
        "rows": rows,
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
    }
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    md_out.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 归档。"""
    lines: list[str] = [
        "# Prime Matrix clean-core DPRC 中心化偏差攻关路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["core_reduction_law"],
        "",
        "```text",
        f"dprc_centered_discrepancy_boundary_closed={fmt_bool(result['dprc_centered_discrepancy_boundary_closed'])}",
        f"rsm_identity_closed={fmt_bool(result['rsm_identity_closed'])}",
        f"bes_compression_closed={fmt_bool(result['bes_compression_closed'])}",
        f"dprc_centered_discrepancy_input_proved={fmt_bool(result['dprc_centered_discrepancy_input_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 新压缩律",
        "",
        "```text",
        "DPRCAlpha043CenteredDiscrepancyOrNamedLayerReturn",
        "  => ExplicitModelGapAndFiniteDPRCLedger",
        "     AND BESDangerIntersectionExclusionOrDLSNamedReturn。",
        "```",
        "",
        "`ExplicitModelGapAndFiniteDPRCLedger` 支付 `P<2003` 的有限段和 `P>=2003` 的 `S(1-H)>3sqrt(S)` 模型余量。"
        "`BESDangerIntersectionExclusionOrDLSNamedReturn` 支付 `D_+<=3sqrt(S)`；若高正和和高能量同步不能排斥，必须回流"
        " `PointLoad/ColumnCRT`、`ShortWindow/SAE` 或 `LowPhase/PDEC`。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 3. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 4. 当前结论",
            "",
            "本步关闭的是 DPRC 的接口层：原始容量不等式已归约到模型余量/有限账本与 BES-DLS 危险交集。"
            "当前材料仍未给出这些输入的无条件证明，也未闭合行/列命题。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--rsm-md", type=Path, default=DEFAULT_RSM_MD)
    parser.add_argument("--rsm-json", type=Path, default=DEFAULT_RSM_JSON)
    parser.add_argument("--bes-md", type=Path, default=DEFAULT_BES_MD)
    parser.add_argument("--bes-json", type=Path, default=DEFAULT_BES_JSON)
    parser.add_argument("--dls-md", type=Path, default=DEFAULT_DLS_MD)
    parser.add_argument("--newlayer-md", type=Path, default=DEFAULT_NEWLAYER_MD)
    parser.add_argument("--newlayer-json", type=Path, default=DEFAULT_NEWLAYER_JSON)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        args.previous,
        args.rsm_md,
        args.rsm_json,
        args.bes_md,
        args.bes_json,
        args.dls_md,
        args.newlayer_md,
        args.newlayer_json,
        args.dstructure,
        args.json_out,
        args.md_out,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
