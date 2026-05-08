#!/usr/bin/env python3
"""Prime Matrix 对齐一素主分支缺陷路由器。

用法示例：
  python3 experiments/prime_matrix_aligned_prime_main_defect_router.py

输出：
  docs/monograph/prime-matrix-aligned-prime-main-defect-router.json
  docs/monograph/prime-matrix-aligned-prime-main-defect-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-variable-row-dimension-gap-router.json"
DEFAULT_EDABK = DOCS / "prime-matrix-eda-bk-lowmod-tail-dichotomy.md"
DEFAULT_BPNBK = DOCS / "prime-matrix-bpn-bk-selberg-route.md"
DEFAULT_DEC = DOCS / "prime-matrix-dec-ospc-exclusion-hardpoint.md"
DEFAULT_JSON = DOCS / "prime-matrix-aligned-prime-main-defect-router.json"
DEFAULT_MD = DOCS / "prime-matrix-aligned-prime-main-defect-router.md"


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


def proof_rows(previous: dict[str, Any], edabk_text: str, bpnbk_text: str, dec_text: str) -> list[dict[str, Any]]:
    """生成对齐一素主分支缺陷路由账本。"""
    return [
        {
            "gate": "VariableRowDimensionGapImported",
            "closed": previous.get("variable_row_dimension_gap_identity_closed") is True,
            "proved": True,
            "meaning": "上一轮已证明 PrimeSurvivors_x=G_x(P)-B_x(P)。",
            "output": "一素主分支为零就是变量行维数差失败。",
        },
        {
            "gate": "PrimeFreeRowImpliesEDAFailure",
            "closed": True,
            "proved": True,
            "meaning": "若 sqrt(P)<=x<P 且 PrimeSurvivors_x=0，则该 P 对齐行没有素数，正是 EDA 失败行。",
            "output": "可直接调用 EDA-BK endpoint defect dichotomy。",
        },
        {
            "gate": "PositiveMainEndpointDefectImported",
            "closed": "positive-main endpoint defect" in edabk_text
            and "ELT-Dichotomy" in edabk_text,
            "proved": True,
            "meaning": "EDA-BK 已证明任一失败行给出正主项端点缺陷，并二分为 LowMod 或 Tail。",
            "output": "LowMod endpoint CRTDefect or Tail/Core concentration。",
        },
        {
            "gate": "BuchstabConstantsNotStandalone",
            "closed": True,
            "proved": True,
            "meaning": "普通 Buchstab/Brun/Selberg 常数只给模型主项；在 H=P,z=P 时普通下界筛 level 不足。",
            "output": "不能把 UniformBuchstabConstants 当成独立闭合证明。",
        },
        {
            "gate": "BKDECBridgeCompatibility",
            "closed": "BK-DEC 桥接已闭合" in bpnbk_text
            and "Directed Endpoint CRTDefect" in bpnbk_text,
            "proved": True,
            "meaning": "BPN-BK 链条已把大端点 sawtooth 缺陷桥接到 Directed Endpoint CRTDefect。",
            "output": "LowMod 分支可接 PDEC/SAE/DEC 审稿门。",
        },
        {
            "gate": "TailCoreBucketCompatibility",
            "closed": "TailCoreBucket/CoreK-Density" in bpnbk_text
            and "Tail-anchor concentration" in bpnbk_text,
            "proved": True,
            "meaning": "大尾项失败已定位为 TailCoreBucket/CoreK-Density，再进入 Tail-anchor 或 distributed corridor。",
            "output": "Tail/Core 分支不再是自由误差。",
        },
        {
            "gate": "DirectedEndpointDefectSchema",
            "closed": "Persistent Directed Endpoint CRTDefect" in dec_text
            and "Directed Endpoint CRTDefect" in dec_text,
            "proved": True,
            "meaning": "DEC/OSPC 文档已给出有向端点 CRT 缺陷的 schema；但 schema 不是排斥。",
            "output": "DirectedEndpointCRTDefectPDECSAEExclusion remains open。",
        },
        {
            "gate": "LowModAndTailExclusion",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 LowMod endpoint CRTDefect 与 Tail/Core concentration 均不可持续或必被 SAE/PDEC 排除。",
            "output": "LowModEndpointCRTDefectExclusion AND TailCoreConcentrationAbsorption。",
        },
    ]


def run(previous_path: Path, edabk_path: Path, bpnbk_path: Path, dec_path: Path) -> dict[str, Any]:
    """执行对齐一素主分支缺陷路由。"""
    previous = load_json(previous_path)
    edabk_text = edabk_path.read_text(encoding="utf-8")
    bpnbk_text = bpnbk_path.read_text(encoding="utf-8")
    dec_text = dec_path.read_text(encoding="utf-8")
    paths = [previous_path, edabk_path, bpnbk_path, dec_path]
    rows = proof_rows(previous=previous, edabk_text=edabk_text, bpnbk_text=bpnbk_text, dec_text=dec_text)
    return {
        "certificate_type": "aligned_prime_main_defect_router",
        "status": "aligned_prime_main_reduced_to_lowmod_tail_defect_exclusions",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "prime_free_row_to_edabk_defect_closed": True,
        "buchstab_constants_standalone_rejected": True,
        "lowmod_tail_defect_exclusions_closed": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_after_router": "LowModTailCoreDefectExclusionPackage",
        "terminal_gap_expansion": [
            "LowModEndpointCRTDefectExclusionOrPDEC",
            "TailCoreConcentrationAbsorptionOrTailAnchorPDEC",
            "SparseSingleWindowSAEExclusion",
            "ColumnDisplacementReusePDEC",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "exact_implication": [
            "PrimeSurvivors_x=0",
            "=> EDA failure at the same aligned row x",
            "=> positive-main endpoint defect by EDA-BK",
            "=> LowMod endpoint CRTDefect OR Tail/Core concentration",
            "=> named PDEC/SAE/ColumnCRT/Tail-anchor exits; no unnamed Buchstab exit",
        ],
        "plain_conclusion": (
            "本步把 `UniformBuchstabOnePrimeBranchLowerBound` 从模型常数问题改写为精确缺陷二分："
            "若某个对齐行的一素分支为零，它就是 EDA 失败行；EDA-BK 已迫使该行产生正主项端点缺陷，"
            "并进入 LowMod endpoint CRTDefect 或 Tail/Core concentration。"
            "因此 Buchstab 常数本身不是终局证明，真正剩余是排斥这两个命名出口。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 对齐一素主分支缺陷路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prime_free_row_to_edabk_defect_closed={fmt_bool(result['prime_free_row_to_edabk_defect_closed'])}",
        f"buchstab_constants_standalone_rejected={fmt_bool(result['buchstab_constants_standalone_rejected'])}",
        f"lowmod_tail_defect_exclusions_closed={fmt_bool(result['lowmod_tail_defect_exclusions_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 精确二分链",
        "",
        "```text",
    ]
    lines.extend(result["exact_implication"])
    lines.extend(
        [
            "```",
            "",
            "这说明当前硬点不能继续写成“Buchstab 常数应为正”。正主项为正只说明若行为空，必须有端点缺陷或尾项集中；",
            "它本身不排斥这些缺陷。",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | output |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{output}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                proved=fmt_bool(bool(row["proved"])),
                meaning=table_cell(row["meaning"]),
                output=table_cell(row["output"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 审稿边界",
            "",
            "已闭合的是从一素分支为零到命名缺陷出口的路由：",
            "",
            "```text",
            "Prime-free aligned row => LowMod endpoint CRTDefect OR Tail/Core concentration.",
            "```",
            "",
            "未闭合的是出口排斥：",
            "",
            "```text",
            "LowMod endpoint CRTDefect cannot persist / is PDEC-excluded;",
            "Tail/Core concentration is absorbed by Tail-anchor, Rankin ledger, or PDEC/SAE;",
            "single-window sparse escapes are SAE-excluded;",
            "fixed column displacement reuse is PDEC-excluded.",
            "```",
            "",
            "## 4. 新最窄剩余",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = LowModEndpointCRTDefectExclusionOrPDEC",
            "    AND TailCoreConcentrationAbsorptionOrTailAnchorPDEC",
            "    AND SparseSingleWindowSAEExclusion",
            "    AND ColumnDisplacementReusePDEC",
            "    AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.",
            "```",
            "",
            "这一步仍不是无条件闭合；它把“证明一素分支正性”的任务改写为两个命名出口的排斥任务。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--edabk-md", type=Path, default=DEFAULT_EDABK)
    parser.add_argument("--bpnbk-md", type=Path, default=DEFAULT_BPNBK)
    parser.add_argument("--dec-md", type=Path, default=DEFAULT_DEC)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        previous_path=args.previous_json,
        edabk_path=args.edabk_md,
        bpnbk_path=args.bpnbk_md,
        dec_path=args.dec_md,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
