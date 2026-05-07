#!/usr/bin/env python3
"""把 DI/BFI 当前窗口假设匹配压成尺度匹配与对象转移两个硬点。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_window_match_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-window-match-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-window-match-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DIBFI_THEOREM_LOCATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
)
DEFAULT_GENERIC_WFD_DIBFI = (
    DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
)
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-window-match-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-window-match-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def contains_all(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def build_gate_rows(
    theorem_location: dict[str, Any],
    generic_wfd_dibfi: dict[str, Any],
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
) -> list[dict[str, Any]]:
    """构造当前窗口匹配门控。"""
    kls_template_ready = contains_all(
        kls_template_path,
        [
            "相位归一化",
            "变量适配表",
            "B(A)",
            "gcd",
        ],
    )
    kze_spine_ready = contains_all(
        kze_spine_path,
        [
            "WFD-core",
            "KE-13",
            "well-factorable",
            "divisor-bounded",
        ],
    )
    source_cen_refuted = contains_all(
        source_cen_path,
        [
            "SOURCE-CEN is false",
            "未块中心化",
            "external DI/BFI theorem route",
        ],
    )
    return [
        {
            "gate": "TheoremLocationsPinned",
            "available": "BFI Theorem 10 and DI Theorem 12 are registered",
            "needed": "do not spend proof effort on theorem-number search",
            "gap": "none",
            "route": "use theorem-location router output",
            "closed": bool(theorem_location["theorem_locations_pinned"]),
        },
        {
            "gate": "GenericWFDContractReady",
            "available": "previous router fixes the generic noncanonical WFD external branch",
            "needed": "avoid reopening canonical RIW/Buchstab support branch",
            "gap": "none",
            "route": "stay on generic WFD external branch",
            "closed": bool(generic_wfd_dibfi["external_dibfi_contract_materialized"]),
        },
        {
            "gate": "UncenteredTargetPreserved",
            "available": "SOURCE-CEN no-go blocks free centering; generic router chooses direct uncentered estimate",
            "needed": "external theorem application must estimate the original uncentered target",
            "gap": "none at target-choice level",
            "route": "direct original dispersion, no SOURCE-CEN insertion",
            "closed": source_cen_refuted,
        },
        {
            "gate": "KloostermanPhaseAndSmoothLedgerReady",
            "available": "KLS template records CRT phase, smooth windows, gcd and B(A) log ledger",
            "needed": "local variables can be compared row-by-row to DI Theorem 12",
            "gap": "none at checklist level",
            "route": "use template as the DI hypothesis table",
            "closed": kls_template_ready,
        },
        {
            "gate": "CoefficientClassReady",
            "available": "KZ-E spine states well-factorable lambda_c, divisor-bounded beta_s, smooth omega_h",
            "needed": "coefficient class must match BFI/DI admissible weights",
            "gap": "none at formal coefficient-class level",
            "route": "lambda_c/beta_s/omega_h enter the external theorem hypotheses",
            "closed": kze_spine_ready,
        },
        {
            "gate": "OriginalAPToWFDTargetTransfer",
            "available": "KZ-E spine has a dispersion identity from AP discrepancy to WFD-core",
            "needed": "prove this transfer uses exactly BFI Theorem 10/DI Theorem 12 without changing target",
            "gap": "not yet written as a theorem-by-theorem implication",
            "route": "write AP discrepancy -> dispersion -> KE-13 transfer lemma",
            "closed": False,
        },
        {
            "gate": "WindowScaleInequalities",
            "available": "KLS template names C,S,H; KZ-E spine names R0,L0/completion lengths",
            "needed": "derive explicit inequalities putting current dyadic windows in BFI/DI admissible ranges",
            "gap": "current docs name ranges qualitatively but do not yet prove the exact exponent inequalities",
            "route": "compute C,S,H,Q,N,M against BFI x^(4/7-eps) and DI J-scale terms",
            "closed": False,
        },
    ]


def run(
    theorem_location_path: Path,
    generic_wfd_dibfi_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
) -> dict[str, Any]:
    """运行当前窗口匹配路由。"""
    theorem_location = load_json(theorem_location_path)
    generic_wfd_dibfi = load_json(generic_wfd_dibfi_path)
    gate_rows = build_gate_rows(
        theorem_location,
        generic_wfd_dibfi,
        kls_template_path,
        kze_spine_path,
        source_cen_path,
    )
    open_gates = [row["gate"] for row in gate_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_window_match_router",
        "status": "dibfi_window_match_reduced_to_target_transfer_and_scale_inequalities",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "dibfi_theorem_location_json": file_sha256(theorem_location_path),
            "generic_wfd_dibfi_json": file_sha256(generic_wfd_dibfi_path),
            "kls_template_md": file_sha256(kls_template_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
        },
        "gate_rows": gate_rows,
        "open_gates": open_gates,
        "all_gates_closed": not open_gates,
        "next_external_target": "DIBFIWindowScaleAndTargetTransferMatch",
        "terminal_gap_after_router": "DIBFIWindowScaleAndTargetTransferMatch",
        "structural_law": (
            "The current-window match is not a vague citation issue anymore. All fixed interfaces "
            "are ready: theorem locations, generic-WFD branch selection, uncentered target choice, "
            "Kloosterman phase/smoothing ledger, and formal coefficient class. The remaining proof "
            "has exactly two active obligations: show the AP discrepancy to KE-13/WFD transfer is a "
            "target-preserving application of BFI/DI, and prove the dyadic window scale inequalities "
            "fit the BFI/DI admissible ranges."
        ),
        "review_conclusion": (
            "当前窗口假设匹配已被压成两个最小硬点："
            "一是 AP discrepancy 到 KE-13/WFD-core 的对象不变转移；"
            "二是 C,S,H,Q,N,M 等 dyadic 尺度满足 BFI/DI 的显式范围。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 当前窗口匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "fixed:",
        "  BFI Theorem 10 and DI Theorem 12 are located;",
        "  generic WFD external branch is selected;",
        "  uncentered target is preserved;",
        "  Kloosterman phase and smoothing ledger are ready;",
        "  coefficient class is registered;",
        "",
        "open:",
        "  OriginalAPToWFDTargetTransfer;",
        "  WindowScaleInequalities;",
        "",
        f"terminal: {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `all_gates_closed={fmt_bool(result['all_gates_closed'])}`。",
        f"- `open_gates={result['open_gates']}`。",
        f"- `next_external_target={result['next_external_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 门控表",
        "",
        "| gate | available | needed | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=fmt_bool(bool(row["closed"])),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "定理位置和普通账本都不再是终端。下一步只剩：",
            "",
            "```text",
            "DIBFIWindowScaleAndTargetTransferMatch",
            "```",
            "",
            "也就是同时完成对象不变转移与尺度不等式。若任一项失败，外部 DI/BFI 不能诚实闭合当前 generic WFD 分支。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dibfi-theorem-location-json",
        type=Path,
        default=DEFAULT_DIBFI_THEOREM_LOCATION,
    )
    parser.add_argument(
        "--generic-wfd-dibfi-json", type=Path, default=DEFAULT_GENERIC_WFD_DIBFI
    )
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        theorem_location_path=args.dibfi_theorem_location_json,
        generic_wfd_dibfi_path=args.generic_wfd_dibfi_json,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
        source_cen_path=args.source_cen_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "open_gates": result["open_gates"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
