#!/usr/bin/env python3
"""内外两线终端归约路由器。

用法示例：
  python3 experiments/prime_matrix_dual_lane_terminal_reduction_router.py

输出：
  docs/monograph/prime-matrix-dual-lane-terminal-reduction-router.json
  docs/monograph/prime-matrix-dual-lane-terminal-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_JOINT = DOCS / "prime-matrix-fulls-kls-movingblock-joint-attack-router.json"
DEFAULT_SUPPORT_RANGE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json"
DEFAULT_SOURCE_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_COMPLETION = DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"
DEFAULT_SPECTRAL_GAP = DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-dual-lane-terminal-reduction-router.json"
DEFAULT_MD = DOCS / "prime-matrix-dual-lane-terminal-reduction-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写字符串。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    joint: dict[str, Any],
    support_range: dict[str, Any],
    source_antiatom: dict[str, Any],
    completion: dict[str, Any],
    spectral_gap: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成两线终端归约判定行。"""
    return [
        {
            "lane": "joint-frontier",
            "gate": "JointFrontierPinned",
            "closed": joint.get("joint_attack_boundary_closed") is True
            and joint.get("narrowest_math_hardpoint")
            == (
                "FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource "
                "OR FullSNonAPWFDKLSTheoremInput"
            ),
            "proved_or_accepted": False,
            "meaning": "上一轮已把内外两线固定为 exact support 包或 Full-S KLS 输入。",
            "remaining": "分别压缩这两个包内部的真实终端。",
        },
        {
            "lane": "internal",
            "gate": "BalancedRangeRemoved",
            "closed": support_range.get("balanced_range_threshold_closed") is True
            and support_range.get("terminal_gap_after_router")
            == "FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov",
            "proved_or_accepted": False,
            "meaning": "full-S regime 下 U,V 多项式级大于任意固定对数阈值，balanced range 不再是硬点。",
            "remaining": "内部路只剩 exact factor support 与 Type/Fourier capacity compatibility。",
        },
        {
            "lane": "internal",
            "gate": "SupportCapacityEqualsSourceAntiAtom",
            "closed": source_antiatom.get("terminal_gap_after_router")
            == "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov",
            "proved_or_accepted": False,
            "meaning": "exact factor support 与容量兼容合并为最终 source capacity measure 无 moving same-(u,v) atom。",
            "remaining": "证明 actual noncanonical source 的强化反原子，或改走外部谱/dispersion。",
        },
        {
            "lane": "external",
            "gate": "FullSWindowCompleted",
            "closed": completion.get("terminal_gap_after_router")
            == "ModulusDependentCompletedFullSKLSInput",
            "proved_or_accepted": False,
            "meaning": "S≈P 且 C≈P/log^O P，s-window 可按模 c 完成；full-S 长度本身不是终端硬点。",
            "remaining": "处理完成后依赖 c 的 residue 权重 B_{c,x}。",
        },
        {
            "lane": "external",
            "gate": "CompletedWeightSpectralAtomPinned",
            "closed": spectral_gap.get("terminal_gap_after_router")
            == "CDependentResidueWeightSpectralCancellationInput",
            "proved_or_accepted": False,
            "meaning": "点态 Weil、L2、普通大筛和平坦 residue 捷径不足；必须有 c,h 谱/dispersion 平均抵消。",
            "remaining": "证明或引用 CDependentResidueWeightSpectralCancellationInput。",
        },
        {
            "lane": "promotion",
            "gate": "RankinPromotionStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved_or_accepted": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 晋级包边界已闭合但未独立验收。",
            "remaining": "即使二线数学输入闭合，也还需独立晋级接受。",
        },
    ]


def run(
    joint_path: Path,
    support_range_path: Path,
    source_antiatom_path: Path,
    completion_path: Path,
    spectral_gap_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行两线终端归约。"""
    source_paths = [
        joint_path,
        support_range_path,
        source_antiatom_path,
        completion_path,
        spectral_gap_path,
        dstructure_path,
    ]
    joint = load_json(joint_path)
    support_range = load_json(support_range_path)
    source_antiatom = load_json(source_antiatom_path)
    completion = load_json(completion_path)
    spectral_gap = load_json(spectral_gap_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(
        joint=joint,
        support_range=support_range,
        source_antiatom=source_antiatom,
        completion=completion,
        spectral_gap=spectral_gap,
        dstructure=dstructure,
    )
    terminal_reduction_boundary_closed = all(row["closed"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_dual_lane_terminal_reduction_router",
        "status": "dual_lane_reduced_to_source_antiatom_or_c_dependent_spectral_input_open",
        "terminal_reduction_boundary_closed": terminal_reduction_boundary_closed,
        "internal_lane_closed": False,
        "external_lane_closed": False,
        "rankin_promotion_accepted": False,
        "row_column_unconditional_closed": False,
        "previous_basis": (
            "(FullSNonAPExactFactorSupportPackageForActualNoncanonicalSource OR "
            "FullSNonAPWFDKLSTheoremInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "internal_terminal_input": (
            "FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource"
        ),
        "external_terminal_input": "CDependentResidueWeightSpectralCancellationInput",
        "refined_final_basis": (
            "(FullSNonAPStrengthenedSourceAntiAtomContractForActualNoncanonicalSource OR "
            "CDependentResidueWeightSpectralCancellationInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "internal_terminal_contract": (
            "For the final full-S non-AP WFD source capacity measure M_{u,v}, prove "
            "max_{u,v} M_{u,v}/sum M_{u,v} <= log^{-2A} for every A."
        ),
        "external_terminal_contract": (
            "Prove or cite spectral DI/BFI/Kuznetsov cancellation for completed Kloosterman "
            "sums with c-dependent residue weights B_{c,x}, keeping the current uncentered "
            "no-projection non-AP WFD target and arbitrary log saving."
        ),
        "plain_conclusion": (
            "内外两条线继续压窄但仍未闭合：内部线的 balanced range 已消去，支撑+容量兼容等价于"
            " actual noncanonical source 的强化反原子；外部线的 full-S 窗口已完成，剩余是 "
            "c-dependent residue 权重的谱抵消。当前材料没有证明任一输入，也没有完成 DStructure/Rankin "
            "独立验收。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix 内外两线终端归约路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_reduction_boundary_closed={fmt_bool(result['terminal_reduction_boundary_closed'])}",
        f"internal_lane_closed={fmt_bool(result['internal_lane_closed'])}",
        f"external_lane_closed={fmt_bool(result['external_lane_closed'])}",
        f"rankin_promotion_accepted={fmt_bool(result['rankin_promotion_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| lane | gate | closed | proved_or_accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{lane}` | `{gate}` | `{closed}` | `{accepted}` | {meaning} | {remaining} |".format(
                lane=table_cell(row["lane"]),
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                accepted=fmt_bool(row["proved_or_accepted"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 上一层输入基",
            "",
            "```text",
            result["previous_basis"],
            "```",
            "",
            "## 3. 最新输入基",
            "",
            "```text",
            result["refined_final_basis"],
            "```",
            "",
            "## 4. 内部线终端合同",
            "",
            result["internal_terminal_contract"],
            "",
            "## 5. 外部线终端合同",
            "",
            result["external_terminal_contract"],
            "",
            "## 6. 当前结论",
            "",
            "本路由关闭的是两条线内部的命名松散性，不是证明缺口。完全闭合仍需要：",
            "",
            "- 证明内部强化反原子，或证明/引用外部 c-dependent 谱抵消；",
            "- 完成 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance` 独立验收。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--joint", type=Path, default=DEFAULT_JOINT)
    parser.add_argument("--support-range", type=Path, default=DEFAULT_SUPPORT_RANGE)
    parser.add_argument("--source-antiatom", type=Path, default=DEFAULT_SOURCE_ANTIATOM)
    parser.add_argument("--completion", type=Path, default=DEFAULT_COMPLETION)
    parser.add_argument("--spectral-gap", type=Path, default=DEFAULT_SPECTRAL_GAP)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        joint_path=args.joint,
        support_range_path=args.support_range,
        source_antiatom_path=args.source_antiatom,
        completion_path=args.completion,
        spectral_gap_path=args.spectral_gap,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["refined_final_basis"])


if __name__ == "__main__":
    main()
