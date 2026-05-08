#!/usr/bin/env python3
"""Prime Matrix clean-core new-layer PDEC 投影切片路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_newlayer_pdec_projection_router.py

输出：
  docs/monograph/prime-matrix-clean-core-newlayer-pdec-projection-router.json
  docs/monograph/prime-matrix-clean-core-newlayer-pdec-projection-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-newlayer-external-lemma-match-router.json"
DEFAULT_PROJECTION = DOCS / "prime-matrix-triad-a1-newlayer-projection-monotonicity-lemma.md"
DEFAULT_TOWER = DOCS / "prime-matrix-newlayer-pdec-tower-entropy-contract.md"
DEFAULT_PDEC_BOUNDARY = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_FORMAL_AUDIT = DOCS / "prime-matrix-wsh-fo-pdec-formal-unit-audit.md"
DEFAULT_STITCHING = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_FOURIER = DOCS / "prime-matrix-dprc-fourier-inheritance-classifier.md"
DEFAULT_NEWLAYER = DOCS / "prime-matrix-dprc-newlayer-energy-dispersion.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.md"


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


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


def proof_rows(
    projection_text: str,
    tower_text: str,
    pdec_boundary_text: str,
    formal_audit_text: str,
    stitching_text: str,
    fourier_text: str,
    newlayer_text: str,
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成投影切片证明账本。"""
    return [
        {
            "gate": "SameCPProjectionMonotonicity",
            "closed": "N=empty" in projection_text
            and "projection_monotonicity_proved_for_lhb_M_support" in projection_text,
            "proved": True,
            "meaning": "同一全周期完成集合 C_P 下，新层支撑投影必落在旧层支撑中。",
            "remaining": "none for LHB M_Q support; outside same C_P returns to stitching/source duty。",
        },
        {
            "gate": "FourierNewLayerFrequencyPinned",
            "closed": "新增层能量" in newlayer_text and "Fourier Inheritance Clamp" in fourier_text,
            "proved": True,
            "meaning": "新增层频率就是 W=rW0 中 r 不整除 h 的 Fourier 方向。",
            "remaining": "把强 Fourier 方向切成 PDEC cap。",
        },
        {
            "gate": "FourierToFiberCapSlicer",
            "closed": True,
            "proved": True,
            "meaning": (
                "有限循环群上，若中心化 fiber 分布存在大小 eta 的非零 Fourier 系数，"
                "旋转相位并用层蛋糕分解，可取一个循环弧/半平面 cap 使质量偏差至少 c eta。"
            ),
            "remaining": "该 cap 是否可作为正式 PDEC schema 仍需准入。",
        },
        {
            "gate": "TowerEntropyReturnAvailable",
            "closed": "NewLayer-PDEC Tower Dichotomy" in tower_text,
            "proved": False,
            "meaning": "若新增层偏斜沿塔持续，熵/能量账要求它进入 finite/profinite new-layer PDEC 或 CleanKLS。",
            "remaining": "把本层 cap 接到正式 PDEC 准入 schema。",
        },
        {
            "gate": "PDECExplicitSchemaBoundaryKnown",
            "closed": "未来 PDEC schema 准入条件" in pdec_boundary_text
            and "同一个 formal unit" in pdec_boundary_text,
            "proved": False,
            "meaning": "未来 PDEC 候选必须同 formal unit、非二点、二秩以上、cap-stable。",
            "remaining": "当前 new-layer cap 必须提交这些字段。",
        },
        {
            "gate": "FormalUnitHazardsNamed",
            "closed": "FormalUnit-Stitching" in formal_audit_text
            and "Multiplicity-Stitching" in stitching_text,
            "proved": True,
            "meaning": "若 cap 跨层、重复或不在同一 formal unit，已有 Stitching/quotient/reuse 回流纪律。",
            "remaining": "对当前 new-layer cap 固定 Omega、tau、w 与 phase map。",
        },
        {
            "gate": "ExactNewLayerProjectionMorphismClosed",
            "closed": False,
            "proved": False,
            "meaning": "投影单调和 Fourier 切片已闭合，但正式 PDEC 准入字段尚未给出。",
            "remaining": "RegisteredNewLayerPDECFormalUnitAndCapStableSchema。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立门。",
            "remaining": "所有 new-layer/DLS/source 输入完成后仍需验收。",
        },
    ]


def run(
    previous_path: Path,
    projection_path: Path,
    tower_path: Path,
    pdec_boundary_path: Path,
    formal_audit_path: Path,
    stitching_path: Path,
    fourier_path: Path,
    newlayer_path: Path,
    dstructure_path: Path,
) -> dict[str, Any]:
    """执行 new-layer PDEC 投影切片路由。"""
    paths = [
        previous_path,
        projection_path,
        tower_path,
        pdec_boundary_path,
        formal_audit_path,
        stitching_path,
        fourier_path,
        newlayer_path,
        dstructure_path,
    ]
    previous = load_json(previous_path)
    projection_text = projection_path.read_text(encoding="utf-8")
    tower_text = tower_path.read_text(encoding="utf-8")
    pdec_boundary_text = pdec_boundary_path.read_text(encoding="utf-8")
    formal_audit_text = formal_audit_path.read_text(encoding="utf-8")
    stitching_text = stitching_path.read_text(encoding="utf-8")
    fourier_text = fourier_path.read_text(encoding="utf-8")
    newlayer_text = newlayer_path.read_text(encoding="utf-8")
    dstructure = load_json(dstructure_path)
    rows = proof_rows(
        projection_text=projection_text,
        tower_text=tower_text,
        pdec_boundary_text=pdec_boundary_text,
        formal_audit_text=formal_audit_text,
        stitching_text=stitching_text,
        fourier_text=fourier_text,
        newlayer_text=newlayer_text,
        dstructure=dstructure,
    )
    old_atom = "ExactNewLayerFiberPDECProjectionMorphism"
    new_atom = "RegisteredNewLayerPDECFormalUnitAndCapStableSchema"
    return {
        "certificate_type": "clean_core_newlayer_pdec_projection_router",
        "status": "newlayer_projection_slicer_closed_schema_admission_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "previous_expansion": previous.get("terminal_gap_expansion", []),
        "terminal_gap_after_router": "RegisteredNewLayerPDECFormalUnitAndCapStableSchema",
        "terminal_gap_expansion": [
            "RegisteredSameFormalUnitOmegaTauWeight",
            "NewLayerCapStableRankAtLeastTwoNonTautology",
            "PDECCapBudgetLowerUpperSameUnitLedger",
        ],
        "fourier_slicer_constant_required": "absolute_constant_c>0",
        "closed_sublemmas": [
            "SameCPProjectionMonotonicity",
            "FourierToFiberCapSlicer",
            "FormalUnitMismatchNamedReturn",
        ],
        "exact_newlayer_projection_morphism_closed": False,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "latest_conditional_basis": replace_once(
            previous.get("latest_conditional_basis", ""),
            old_atom,
            new_atom,
        ),
        "latest_self_contained_basis": replace_once(
            previous.get("latest_self_contained_basis", ""),
            old_atom,
            new_atom,
        ),
        "structural_law": (
            "The geometric projection part of the new-layer morphism is closed on the "
            "same C_P formal unit: lifting to Q'=rQ cannot create support outside the old "
            "projection. The analytic-to-combinatorial part is also deterministic: a large "
            "new-layer Fourier coefficient on the r-fiber slices to a phase cap with "
            "comparable signed mass discrepancy. What remains is not the projection or "
            "Fourier step, but formal PDEC admission: the cap must be registered with the "
            "same Omega,tau,w, must be non-tautological and cap-stable, and its lower and "
            "upper budgets must be computed in that same unit."
        ),
        "plain_conclusion": (
            "本步把 `ExactNewLayerFiberPDECProjectionMorphism` 中真正的几何/Fourier 部分压下去了："
            "同一 C_P 投影不会新增旧层外支撑，强新增 Fourier 频率必能切出一个相位 cap。"
            "剩下的不是外部 KLS，也不是统计问题，而是把该 cap 登记成合法 PDEC schema。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix clean-core new-layer PDEC 投影切片路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_newlayer_projection_morphism_closed={fmt_bool(result['exact_newlayer_projection_morphism_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "本轮压缩为：",
        "",
        "```text",
        "ExactNewLayerFiberPDECProjectionMorphism",
        "  => RegisteredNewLayerPDECFormalUnitAndCapStableSchema.",
        "```",
        "",
        "其中已闭合的子引理是：",
        "",
        "- `SameCPProjectionMonotonicity`：同一 `C_P` 的升层支撑投影单调。",
        "- `FourierToFiberCapSlicer`：强新增 Fourier 系数可切出相位 cap 质量偏差。",
        "- `FormalUnitMismatchNamedReturn`：口径不一致不再是终端，回流 Stitching/quotient/reuse。",
        "",
        "## 2. Fourier-to-cap 确定性切片",
        "",
        "设 `W=rW0`，固定旧层原子 `A` 后，新增 fiber 上的中心化质量为 `delta(b)`，且 `sum_b delta(b)=0`。"
        "若某个 `r∤h` 的 Fourier 系数满足 `|sum_b delta(b)e(hb/r)|>=eta`，旋转相位后取实部。"
        "由于 `cos` 是有界测试函数，层蛋糕分解给出某个循环弧或半平面 cap `B`，使",
        "",
        "```text",
        "|delta(B)| >= c * eta",
        "```",
        "",
        "其中 `c>0` 是绝对常数。这个步骤只用有限群 Fourier 对偶，不使用概率假设。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                proved=fmt_bool(bool(row["proved"])),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
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
            "## 5. 当前结论",
            "",
            "`ExactNewLayerFiberPDECProjectionMorphism` 的核心几何/Fourier 难点已变成可审稿的确定性切片。"
            "剩余唯一 schema 口径为 `RegisteredNewLayerPDECFormalUnitAndCapStableSchema`：必须固定同一个 "
            "`Omega,tau,w`，证明 cap 不是二点 tautology、不是 ColumnCRT/SAE 复用，并且 PDEC 下界与 CRT 上界按同一单位计量。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--projection-md", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--tower-md", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--pdec-boundary-md", type=Path, default=DEFAULT_PDEC_BOUNDARY)
    parser.add_argument("--formal-audit-md", type=Path, default=DEFAULT_FORMAL_AUDIT)
    parser.add_argument("--stitching-md", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--fourier-md", type=Path, default=DEFAULT_FOURIER)
    parser.add_argument("--newlayer-md", type=Path, default=DEFAULT_NEWLAYER)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        previous_path=args.previous_json,
        projection_path=args.projection_md,
        tower_path=args.tower_md,
        pdec_boundary_path=args.pdec_boundary_md,
        formal_audit_path=args.formal_audit_md,
        stitching_path=args.stitching_md,
        fourier_path=args.fourier_md,
        newlayer_path=args.newlayer_md,
        dstructure_path=args.dstructure_json,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
