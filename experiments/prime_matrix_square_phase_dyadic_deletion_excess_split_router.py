#!/usr/bin/env python3
"""生成 dyadic 负平方相位过删的一阶/二阶缺陷分裂证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_dyadic_deletion_excess_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-dyadic-deletion-excess-split-router.json

输出：
  docs/monograph/prime-matrix-square-phase-dyadic-deletion-excess-split-router.json
  docs/monograph/prime-matrix-square-phase-dyadic-deletion-excess-split-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-dyadic-deletion-excess-split-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-dyadic-deletion-excess-split-router.md"

DYADIC_DEFECT = "DyadicNegativeSquarePhaseDeletionExcessPDEC"
FIRST_MOMENT = "DyadicSquarePhaseFirstMomentLoadPDEC"
OVERLAP_DEFECT = "DyadicSquarePhaseOverlapDeficitOrPairCorrelationPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.json",
    "prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json",
]


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_dyadic_deletion_excess_split_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def split_rows() -> list[dict[str, str]]:
    """列出 dyadic 过删分裂对象。"""
    return [
        {
            "object": "survivor_set",
            "formula": "S_z={k: k survives all q<=z}",
            "meaning": "进入 dyadic 块前的条件样本空间。",
        },
        {
            "object": "block_union",
            "formula": "U_B=|{k in S_z: exists q in B, k=-P^2 mod q}|",
            "meaning": "该 dyadic 块真实删除量。",
        },
        {
            "object": "first_moment",
            "formula": "H_B=sum_{q in B} |S_z cap {-P^2 mod q}|",
            "meaning": "一阶命中负载；高于期望即线性相位 PDEC。",
        },
        {
            "object": "overlap",
            "formula": "I_B=sum_{q1<q2 in B} |S_z cap a_{q1} cap a_{q2}|",
            "meaning": "二阶重叠；低于期望则是 pair-correlation 缺陷。",
        },
        {
            "object": "bonferroni_gate",
            "formula": "U_B <= H_B, and U_B >= H_B-I_B",
            "meaning": "过删必须由一阶过载或二阶/高阶重叠异常承担。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "DyadicDeletionObjectsDefined",
            "closed": True,
            "proved": True,
            "meaning": "单块删除量、一阶负载和二阶重叠均已定义在同一进入块 survivor set 上。",
            "remaining": "none",
        },
        {
            "gate": "DeletionExcessSplitClosed",
            "closed": True,
            "proved": True,
            "meaning": "若 union 删除超过独立模型，则必须是一阶负载过高，或重叠/高阶结构低于正常抵消。",
            "remaining": f"{FIRST_MOMENT} OR {OVERLAP_DEFECT}",
        },
        {
            "gate": "FirstMomentRouteIdentified",
            "closed": True,
            "proved": False,
            "meaning": "一阶过载等价于 S_z 对移动残基 -P^2 mod q 的平均命中过高，可 Fourier 化为线性 PDEC。",
            "remaining": FIRST_MOMENT,
        },
        {
            "gate": "OverlapRouteIdentified",
            "closed": True,
            "proved": False,
            "meaning": "若一阶正常但 union 过大，则多重命中重叠不足，形成 q1*q2 交叉相位 pair-correlation PDEC。",
            "remaining": OVERLAP_DEFECT,
        },
        {
            "gate": "DyadicDefectExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未排除一阶过载与二阶重叠缺陷。",
            "remaining": f"exclude {FIRST_MOMENT} and {OVERLAP_DEFECT}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "LDG dyadic 缺陷与 RFP reciprocal-floor 缺陷仍未全部排除。",
            "remaining": "LDG dyadic split exclusions + RFP reciprocal-floor exclusion",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造分裂证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_dyadic_deletion_excess_split_router",
        "status": "dyadic_deletion_excess_split_to_first_moment_or_overlap_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "dyadic_deletion_objects_defined": True,
        "deletion_excess_split_closed": True,
        "first_moment_route_identified": True,
        "overlap_route_identified": True,
        "dyadic_defect_excluded": False,
        "row_column_unconditional_closed": False,
        "split_rows": split_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": FIRST_MOMENT,
        "parallel_attack_target": OVERLAP_DEFECT,
        "plain_conclusion": (
            "`DyadicNegativeSquarePhaseDeletionExcessPDEC` 已进一步原子化。"
            "在进入块 survivor set `S_z` 上，若 dyadic 块删除量超过独立模型，"
            "则不是无名过删：要么一阶命中负载 `H_B` 过高，给出线性 Fourier/PDEC；"
            "要么一阶负载正常但 union 仍过大，说明二阶及高阶重叠不足，给出"
            "pair-correlation/交叉相位 PDEC。两个出口尚未排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase dyadic 删除过量分裂路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"deletion_excess_split_closed={fmt_bool(result['deletion_excess_split_closed'])}",
        f"first_moment_route_identified={fmt_bool(result['first_moment_route_identified'])}",
        f"overlap_route_identified={fmt_bool(result['overlap_route_identified'])}",
        f"dyadic_defect_excluded={fmt_bool(result['dyadic_defect_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分裂对象",
        "",
        "| object | formula | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["split_rows"]:
        lines.append(f"| `{item['object']}` | `{table_cell(item['formula'])}` | {table_cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
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
            "## 3. 下一步",
            "",
            f"- 先攻 `{FIRST_MOMENT}`：对 `sum_{{q in B}} |S_z cap {{-P^2 mod q}}|` 建立 Fourier/PDEC 上界。",
            f"- 并行保留 `{OVERLAP_DEFECT}`：若一阶正常但 union 过删，必须解释为 pair-correlation 缺陷。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "parallel_attack_target": result["parallel_attack_target"],
                "dyadic_defect_excluded": result["dyadic_defect_excluded"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
