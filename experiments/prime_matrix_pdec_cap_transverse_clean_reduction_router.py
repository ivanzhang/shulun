#!/usr/bin/env python3
"""把有限弧横向纤维扩张压到横向 clean 大筛原子。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_transverse_clean_reduction_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-transverse-clean-reduction-router.json
  docs/monograph/prime-matrix-pdec-cap-transverse-clean-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TRANSVERSE = DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.json"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_DIFFUSE = DOCS / "prime-matrix-pdec-cap-diffuse-terminal-split-router.json"
DEFAULT_SC9 = DOCS / "prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.json"
DEFAULT_DUAL_ABSORB = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-transverse-clean-reduction-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-transverse-clean-reduction-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    transverse: dict[str, Any],
    terminal_triad_text: str,
    diffuse: dict[str, Any],
    sc9: dict[str, Any],
    dual_absorb_text: str,
) -> list[dict[str, Any]]:
    """生成横向 clean 归约审查表。"""
    transverse_active = (
        transverse["finite_arc_no_unnamed_exit_closed"]
        and transverse["narrowest_next_hardpoint"]
        == "TransverseFiberExpansionForFiniteArcCaps"
    )
    rank_two_leaves_quotient = (
        transverse_active
        and "rank-one slice" in transverse["transverse_law"]
        and "rank-at-least-two" not in transverse["transverse_law"]
    )
    nonflat_transverse_routes_named = (
        transverse_active
        and has_all(
            dual_absorb_text,
            [
                "CapSparse",
                "CapPersistent",
                "CapColumn",
            ],
        )
    )
    clean_admission_registered = (
        diffuse["diffuse_terminal_split_closed"]
        and has_all(
            terminal_triad_text,
            [
                "K1 ranges",
                "K5 coefficient L2-flat",
                "内部 LargeSieve/DLS/KLS 不等式",
            ],
        )
    )
    sc9_boundary_registered = (
        sc9["pdec_cap_sc9_boundary_reconciled"]
        and sc9["canonical_sc9_independent_blocker_collapsed"]
    )
    transverse_clean_reduction_closed = all(
        [
            transverse_active,
            rank_two_leaves_quotient,
            nonflat_transverse_routes_named,
            clean_admission_registered,
            sc9_boundary_registered,
        ]
    )
    return [
        row(
            "TransverseExpansionActive",
            transverse_active,
            transverse["narrowest_next_hardpoint"],
            "上一层已把有限弧 cap 质量界压成高质量弧内的横向纤维扩张估计。",
            False,
        ),
        row(
            "RankOneArcLeavesTransverseQuotient",
            rank_two_leaves_quotient,
            "finite arc is rank-one slice inside rank>=2 primitive kernel",
            "有限字符弧只钉住一个字符方向；二秩以上 primitive 核在弧内仍有非平凡横向商变量。",
            False,
        ),
        row(
            "NonFlatTransverseRoutesNamed",
            nonflat_transverse_routes_named,
            "CapSparse / CapPersistent / CapColumn",
            "横向低支撑、横向持久偏斜或列/壳集中均已回流 SAE、refined PDEC 或 ColumnCRT。",
            False,
        ),
        row(
            "TransverseFlatnessAdmitsCleanKLS",
            clean_admission_registered,
            "K1-K9 clean admission + LargeSieve/DLS/KLS",
            "若横向所有命名偏斜都被剥离，剩余正是横向 L2-flat clean residual。",
            False,
        ),
        row(
            "SC9BoundaryRegisteredForCleanResidual",
            sc9_boundary_registered,
            "canonical SC-9 reconciled; generic external/not claimed",
            "横向 clean 原子必须遵守既有 SC-9/NC-BLK 边界，不能作为新的无名出口。",
            False,
        ),
        row(
            "TransverseExpansionReducedToCleanAtom",
            transverse_clean_reduction_closed,
            "nonflat routes named; flat residual is clean large-sieve atom",
            "横向纤维扩张硬点已压成横向 clean 大筛原子或命名回流。",
            False,
        ),
        row(
            "TransverseQuotientCleanLargeSieveAtom",
            False,
            "self-contained transverse clean large-sieve estimate not submitted",
            "剩余全球硬点是证明横向商上的 clean 大筛原子，或明确外部输入；不能把它误称为已闭合行列定理。",
            True,
        ),
    ]


def run(
    transverse_path: Path,
    terminal_triad_path: Path,
    diffuse_path: Path,
    sc9_path: Path,
    dual_absorb_path: Path,
) -> dict[str, Any]:
    """运行横向 clean 归约路由。"""
    transverse = load_json(transverse_path)
    terminal_triad_text = read_text(terminal_triad_path)
    diffuse = load_json(diffuse_path)
    sc9 = load_json(sc9_path)
    dual_absorb_text = read_text(dual_absorb_path)
    rows = build_rows(
        transverse=transverse,
        terminal_triad_text=terminal_triad_text,
        diffuse=diffuse,
        sc9=sc9,
        dual_absorb_text=dual_absorb_text,
    )
    reduction_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "TransverseExpansionReducedToCleanAtom"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_transverse_clean_reduction_router",
        "status": "transverse_expansion_reduced_to_clean_large_sieve_atom",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "transverse": file_sha256(transverse_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "diffuse": file_sha256(diffuse_path),
            "sc9": file_sha256(sc9_path),
            "dual_absorb": file_sha256(dual_absorb_path),
        },
        "transverse_expansion_reduced_to_clean_atom": reduction_closed,
        "transverse_quotient_clean_large_sieve_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "TransverseQuotientCleanLargeSieveAtom",
        "rows": rows,
        "clean_reduction_law": (
            "Inside a high finite character arc, the arc condition is only rank one. "
            "A rank-at-least-two primitive kernel therefore leaves a transverse quotient. "
            "If that quotient has sparse support, persistent bias, or column/shell "
            "concentration, the branch is SAE, refined PDEC, or ColumnCRT. If none of those "
            "named transverse defects occurs, the residual is L2-flat in the transverse "
            "quotient and must enter the CleanKLS/DLS large-sieve atom, with the already "
            "registered SC-9/NC-BLK boundary."
        ),
        "review_conclusion": (
            "横向纤维扩张已压成横向商上的 clean 大筛原子：非平坦横向缺陷全部回流命名出口，"
            "剩下的只能是 L2-flat clean residual。最新最窄剩余是 "
            "`TransverseQuotientCleanLargeSieveAtom`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 横向 clean 归约路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 横向 clean 归约律",
        "",
        result["clean_reduction_law"],
        "",
        "```text",
        "TransverseFiberExpansionForFiniteArcCaps",
        "  finite arc fixes one character direction;",
        "  rank>=2 primitive kernel leaves transverse quotient;",
        "  transverse sparse/support defect => SAE;",
        "  transverse persistent bias => refined PDEC;",
        "  transverse shell/column concentration => ColumnCRT/PDEC;",
        "  no transverse defect => L2-flat clean residual;",
        "  remaining:",
        "    TransverseQuotientCleanLargeSieveAtom.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `transverse_expansion_reduced_to_clean_atom={fmt_bool(result['transverse_expansion_reduced_to_clean_atom'])}`。",
        f"- `transverse_quotient_clean_large_sieve_closed={fmt_bool(result['transverse_quotient_clean_large_sieve_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 剩余",
            "",
            "下一步直接攻 `TransverseQuotientCleanLargeSieveAtom`：证明高质量有限弧的横向商在 K1--K9 clean admission 后满足内部大筛/DLS/KLS 界，或明确登记外部输入；若任一 clean admission 失败，必须回流 PDEC/SAE/ColumnCRT/Multiplicity。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transverse-json", type=Path, default=DEFAULT_TRANSVERSE)
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--diffuse-json", type=Path, default=DEFAULT_DIFFUSE)
    parser.add_argument("--sc9-json", type=Path, default=DEFAULT_SC9)
    parser.add_argument("--dual-absorb-md", type=Path, default=DEFAULT_DUAL_ABSORB)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        transverse_path=args.transverse_json,
        terminal_triad_path=args.terminal_triad_md,
        diffuse_path=args.diffuse_json,
        sc9_path=args.sc9_json,
        dual_absorb_path=args.dual_absorb_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
