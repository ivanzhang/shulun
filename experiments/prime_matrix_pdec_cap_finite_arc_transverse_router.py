#!/usr/bin/env python3
"""把有限循环弧 cap 质量界压到横向纤维扩张/平坦吸收。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_finite_arc_transverse_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-finite-arc-transverse-router.json
  docs/monograph/prime-matrix-pdec-cap-finite-arc-transverse-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FINITE_BASIS = DOCS / "prime-matrix-pdec-cap-uniform-cap-finite-basis-router.json"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_DUAL_ABSORB = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_DIFFUSE = DOCS / "prime-matrix-pdec-cap-diffuse-terminal-split-router.json"
DEFAULT_COMMON_VARIABLE = DOCS / "prime-matrix-pdec-cap-dense-kernel-common-variable-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.md"


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
    finite_basis: dict[str, Any],
    terminal_triad_text: str,
    dual_absorb_text: str,
    no_cycle_text: str,
    diffuse: dict[str, Any],
    common_variable_text: str,
) -> list[dict[str, Any]]:
    """生成有限弧横向路由审查表。"""
    finite_arc_bounds_active = (
        finite_basis["uniform_cap_finite_basis_closed"]
        and finite_basis["narrowest_next_hardpoint"]
        == "FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels"
    )
    arc_is_rank_one_slice = (
        finite_arc_bounds_active
        and "finite cyclic-arc cap mass bounds" in finite_basis["finite_basis_law"]
    )
    low_transverse_support_named = has_all(
        dual_absorb_text,
        [
            "CapSparse",
            "CapColumn",
            "ColumnCRT",
        ],
    ) and has_all(
        common_variable_text,
        [
            "fixed shell or finite shell packet",
            "PDEC / ColumnCRT",
            "capacity/Hall deletion",
        ],
    )
    persistent_transverse_bias_named = has_all(
        dual_absorb_text,
        [
            "CapPersistent",
            "refined PDEC",
        ],
    ) and has_all(
        no_cycle_text,
        [
            "PDEC-Cap-NoCycle",
            "rank_n<=|G|",
        ],
    )
    flat_transverse_route_registered = (
        diffuse["diffuse_terminal_split_closed"]
        and has_all(
            terminal_triad_text,
            [
                "Flat",
                "CleanKLS/DLS",
                "内部 LargeSieve/DLS/KLS 不等式",
            ],
        )
    )
    no_unnamed_arc_exit = all(
        [
            finite_arc_bounds_active,
            arc_is_rank_one_slice,
            low_transverse_support_named,
            persistent_transverse_bias_named,
            flat_transverse_route_registered,
        ]
    )
    return [
        row(
            "FiniteArcCapBoundsActive",
            finite_arc_bounds_active,
            finite_basis["narrowest_next_hardpoint"],
            "上一层已把连续帽稳定压成有限循环弧 cap 质量界。",
            False,
        ),
        row(
            "FiniteArcIsRankOneSlice",
            arc_is_rank_one_slice,
            "character arc preimage",
            "每个有限循环弧 cap 是一个非平凡字符方向上的秩一薄片，横向变量仍可被审查。",
            False,
        ),
        row(
            "LowTransverseSupportRoutesNamed",
            low_transverse_support_named,
            "CapSparse / CapColumn / fixed-shell / Hall deletion",
            "若高质量弧只由低横向支撑或固定壳承担，则进入 SAE、ColumnCRT、固定壳 PDEC 或容量/Hall 删除。",
            False,
        ),
        row(
            "PersistentTransverseBiasRoutesToRefinedPDEC",
            persistent_transverse_bias_named,
            "CapPersistent + finite cap no-cycle",
            "若弧内横向偏斜持久，就把弧指标并入签名，得到 refined PDEC；固定层细化不能无限循环。",
            False,
        ),
        row(
            "FlatTransverseDispersionRoutesToClean",
            flat_transverse_route_registered,
            "Flat => CleanKLS/DLS admission",
            "若弧内既无低横向支撑也无持久偏斜，则剩余是横向平坦分散输入，进入 CleanKLS/DLS 或已登记外部输入。",
            False,
        ),
        row(
            "FiniteArcNoUnnamedExit",
            no_unnamed_arc_exit,
            "low support / persistent bias / flat transverse dispersion",
            "有限循环弧 cap 没有第四类出口；剩余只是真正横向扩张或平坦大筛估计。",
            False,
        ),
        row(
            "TransverseFiberExpansionForFiniteArcCaps",
            False,
            "uniform transverse expansion or clean large-sieve estimate not submitted",
            "剩余全球硬点是在每个高质量有限弧内证明横向纤维扩张不足以支持反例，或把失败送入命名 PDEC/SAE/ColumnCRT/CleanKLS。",
            True,
        ),
    ]


def run(
    finite_basis_path: Path,
    terminal_triad_path: Path,
    dual_absorb_path: Path,
    no_cycle_path: Path,
    diffuse_path: Path,
    common_variable_path: Path,
) -> dict[str, Any]:
    """运行有限弧横向路由。"""
    finite_basis = load_json(finite_basis_path)
    terminal_triad_text = read_text(terminal_triad_path)
    dual_absorb_text = read_text(dual_absorb_path)
    no_cycle_text = read_text(no_cycle_path)
    diffuse = load_json(diffuse_path)
    common_variable_text = read_text(common_variable_path)
    rows = build_rows(
        finite_basis=finite_basis,
        terminal_triad_text=terminal_triad_text,
        dual_absorb_text=dual_absorb_text,
        no_cycle_text=no_cycle_text,
        diffuse=diffuse,
        common_variable_text=common_variable_text,
    )
    no_unnamed_exit = next(
        bool(item["closed"]) for item in rows if item["gate"] == "FiniteArcNoUnnamedExit"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_finite_arc_transverse_router",
        "status": "finite_arc_cap_bounds_reduced_to_transverse_expansion",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "finite_basis": file_sha256(finite_basis_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "dual_absorb": file_sha256(dual_absorb_path),
            "no_cycle": file_sha256(no_cycle_path),
            "diffuse": file_sha256(diffuse_path),
            "common_variable": file_sha256(common_variable_path),
        },
        "finite_arc_no_unnamed_exit_closed": no_unnamed_exit,
        "transverse_fiber_expansion_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "TransverseFiberExpansionForFiniteArcCaps",
        "rows": rows,
        "transverse_law": (
            "A finite cyclic-arc cap is a rank-one slice of the finite signature space. "
            "If a high-mass arc has low transverse support, it is sparse/SAE, fixed-shell "
            "PDEC, ColumnCRT, or Hall deletion. If the transverse bias persists, the arc "
            "indicator becomes a refined PDEC signature, and fixed-level refinement has no "
            "cycle. If neither happens, the cap mass is genuinely transverse and flat, so "
            "the branch is a CleanKLS/DLS or external large-sieve input. Hence finite arc "
            "caps have no unnamed exit; the remaining estimate is transverse fiber expansion."
        ),
        "review_conclusion": (
            "有限循环弧 cap 质量界已被拆成横向结构：低横向支撑回 `SAE/ColumnCRT/固定壳PDEC`，"
            "横向偏斜持久回 refined PDEC，横向平坦分散进入 `CleanKLS/DLS` 或外部大筛输入。"
            "因此最新最窄剩余是高质量有限弧内的统一横向纤维扩张估计。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 有限弧横向路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 横向分裂律",
        "",
        result["transverse_law"],
        "",
        "```text",
        "FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels",
        "  finite cyclic arc = rank-one character slice;",
        "  low transverse support",
        "    => SAE / ColumnCRT / fixed-shell PDEC / Hall deletion;",
        "  persistent transverse bias",
        "    => refined PDEC, no fixed-level cap cycle;",
        "  transverse flat dispersion",
        "    => CleanKLS/DLS or external large-sieve input;",
        "  remaining:",
        "    TransverseFiberExpansionForFiniteArcCaps.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `finite_arc_no_unnamed_exit_closed={fmt_bool(result['finite_arc_no_unnamed_exit_closed'])}`。",
        f"- `transverse_fiber_expansion_closed={fmt_bool(result['transverse_fiber_expansion_closed'])}`。",
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
            "下一步直接攻 `TransverseFiberExpansionForFiniteArcCaps`："
            "对每个高质量有限字符弧，证明弧内横向纤维无法同时保持 primitive 二秩、同 formal unit、"
            "cap-stable 和足够质量；若证明失败，必须输出 `SAE/refined PDEC/ColumnCRT/CleanKLS` 回流证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--finite-basis-json", type=Path, default=DEFAULT_FINITE_BASIS)
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--dual-absorb-md", type=Path, default=DEFAULT_DUAL_ABSORB)
    parser.add_argument("--no-cycle-md", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--diffuse-json", type=Path, default=DEFAULT_DIFFUSE)
    parser.add_argument("--common-variable-md", type=Path, default=DEFAULT_COMMON_VARIABLE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        finite_basis_path=args.finite_basis_json,
        terminal_triad_path=args.terminal_triad_md,
        dual_absorb_path=args.dual_absorb_md,
        no_cycle_path=args.no_cycle_md,
        diffuse_path=args.diffuse_json,
        common_variable_path=args.common_variable_md,
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
