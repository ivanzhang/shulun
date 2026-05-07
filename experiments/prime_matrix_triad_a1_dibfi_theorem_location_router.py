#!/usr/bin/env python3
"""定位 DI/BFI 原始 dispersion 外部定理号，并保留窗口假设匹配缺口。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_theorem_location_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-theorem-location-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-theorem-location-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_GENERIC_WFD_DIBFI = (
    DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
)
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.md"


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


def build_source_rows() -> list[dict[str, Any]]:
    """列出精确定理位置。"""
    return [
        {
            "source_id": "BFI1986-Theorem10",
            "paper": "Bombieri--Friedlander--Iwaniec, Primes in arithmetic progressions to large moduli",
            "location": "Acta Mathematica 156(3--4), 203--251, 1986, Theorem 10",
            "doi": "ActaMath1986",
            "role": "well-factorable weighted prime AP dispersion estimate",
            "located": True,
        },
        {
            "source_id": "DI1982-Theorem12",
            "paper": "Deshouillers--Iwaniec, Kloosterman sums and Fourier coefficients of cusp forms",
            "location": "Inventiones Mathematicae 70, 219--288, 1982, Theorem 12",
            "doi": "10.1007/BF01390728",
            "role": "spectral Kloosterman estimate used inside the dispersion method",
            "located": True,
        },
        {
            "source_id": "Maynard2020-CrossCheck",
            "paper": "Maynard, Primes in arithmetic progressions to large moduli II: Well-factorable estimates",
            "location": "arXiv:2006.07088, Theorem A cites BFI Theorem 10; Lemma 6.12 cites DI Theorem 12",
            "doi": "arXiv:2006.07088",
            "role": "modern public cross-check of theorem numbering and DI estimate formula",
            "located": True,
        },
    ]


def build_gate_rows(
    generic_wfd_dibfi: dict[str, Any],
    external_index_path: Path,
    kls_template_path: Path,
) -> list[dict[str, Any]]:
    """列出定理位置与剩余假设匹配门。"""
    index_updated = contains_all(
        external_index_path,
        [
            "BFI1986-Theorem10",
            "DI1982-Theorem12",
            "DIBFIOriginalDispersionCurrentWindowHypothesisMatch",
        ],
    )
    template_ready = contains_all(
        kls_template_path,
        [
            "Kloosterman",
            "well-factorable",
            "目标强度",
        ],
    )
    return [
        {
            "gate": "BFITheorem10Located",
            "available": "BFI Acta Math theorem number and pages are pinned",
            "needed": "well-factorable weighted AP dispersion source",
            "gap": "none at theorem-location level",
            "route": "cite BFI1986 Theorem 10",
            "closed": index_updated,
        },
        {
            "gate": "DITheorem12Located",
            "available": "DI theorem number, DOI and pages are pinned",
            "needed": "spectral Kloosterman estimate source",
            "gap": "none at theorem-location level",
            "route": "cite DI1982 Theorem 12",
            "closed": index_updated,
        },
        {
            "gate": "ModernCrossCheckRegistered",
            "available": "Maynard arXiv source cross-checks BFI Theorem 10 and DI Theorem 12 numbering",
            "needed": "publicly inspectable theorem numbering check",
            "gap": "none at numbering cross-check level",
            "route": "use Maynard2020 as a numbering audit, not as a replacement for DI/BFI",
            "closed": index_updated,
        },
        {
            "gate": "CurrentGenericWFDContractReady",
            "available": "previous router materialized uncentered generic WFD DI/BFI contract",
            "needed": "do not reopen canonical support branch",
            "gap": "none",
            "route": "continue only with current-window hypothesis match",
            "closed": bool(generic_wfd_dibfi["external_dibfi_contract_materialized"]),
        },
        {
            "gate": "KLSWindowTemplateReady",
            "available": "local KLS template records phase, level, frequency, gcd and log-loss budgets",
            "needed": "use it as the checklist for the final hypothesis match",
            "gap": "none at checklist level",
            "route": "compare each KLS-template row against BFI/DI hypotheses",
            "closed": template_ready,
        },
        {
            "gate": "CurrentWindowHypothesisMatch",
            "available": "theorem locations and local checklist are now fixed",
            "needed": "prove current KE-13/WFD window satisfies every cited DI/BFI hypothesis",
            "gap": "not yet checked theorem-by-theorem inside the repository",
            "route": "match uncentered target, level, phase, Type-I/II range, gcd, smoothing and log saving",
            "closed": False,
        },
    ]


def run(
    generic_wfd_dibfi_path: Path,
    external_index_path: Path,
    kls_template_path: Path,
) -> dict[str, Any]:
    """运行 DI/BFI 定理位置路由。"""
    generic_wfd_dibfi = load_json(generic_wfd_dibfi_path)
    source_rows = build_source_rows()
    gate_rows = build_gate_rows(generic_wfd_dibfi, external_index_path, kls_template_path)
    theorem_locations_pinned = all(row["located"] for row in source_rows) and all(
        row["closed"]
        for row in gate_rows
        if row["gate"] != "CurrentWindowHypothesisMatch"
    )
    return {
        "certificate_type": "triad_a1_dibfi_theorem_location_router",
        "status": "dibfi_theorem_locations_pinned_current_window_hypothesis_match_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "generic_wfd_dibfi_json": file_sha256(generic_wfd_dibfi_path),
            "external_theorem_index_md": file_sha256(external_index_path),
            "kls_template_md": file_sha256(kls_template_path),
        },
        "source_rows": source_rows,
        "gate_rows": gate_rows,
        "theorem_locations_pinned": theorem_locations_pinned,
        "all_gates_closed": all(row["closed"] for row in gate_rows),
        "previous_terminal_gap": generic_wfd_dibfi["terminal_gap_after_router"],
        "next_external_target": "DIBFIOriginalDispersionCurrentWindowHypothesisMatch",
        "terminal_gap_after_router": "DIBFIOriginalDispersionCurrentWindowHypothesisMatch",
        "structural_law": (
            "The theorem-location part of the DI/BFI original-dispersion gap is now separated "
            "from the mathematical hypothesis match. BFI Theorem 10 supplies the well-factorable "
            "prime-AP dispersion location; DI Theorem 12 supplies the Kloosterman spectral estimate "
            "location; Maynard's public well-factorable paper cross-checks the numbering. The only "
            "remaining task is to prove that the current uncentered KE-13/WFD window satisfies the "
            "hypotheses of those located theorems without changing the target object."
        ),
        "review_conclusion": (
            "DI/BFI 原始 dispersion 的“定理位置”部分已从缺口中剥离：BFI 取 Theorem 10，"
            "DI 取 Theorem 12，并用 Maynard 公开源码作编号交叉核验。当前剩余改写为"
            "当前 KE-13/WFD 窗口对这些定理的假设逐项匹配。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 定理位置路由器",
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
        "previous gap:",
        f"  {result['previous_terminal_gap']};",
        "",
        "theorem locations:",
        "  BFI1986 Theorem 10;",
        "  DI1982 Theorem 12;",
        "  Maynard2020 cross-check;",
        "",
        "remaining gap:",
        f"  {result['terminal_gap_after_router']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `theorem_locations_pinned={fmt_bool(result['theorem_locations_pinned'])}`。",
        f"- `all_gates_closed={fmt_bool(result['all_gates_closed'])}`。",
        f"- `next_external_target={result['next_external_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 定理位置表",
        "",
        "| source | paper | location | DOI/arXiv | role | located |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["source_rows"]:
        lines.append(
            "| `{source}` | {paper} | {location} | `{doi}` | {role} | `{located}` |".format(
                source=table_cell(row["source_id"]),
                paper=table_cell(row["paper"]),
                location=table_cell(row["location"]),
                doi=table_cell(row["doi"]),
                role=table_cell(row["role"]),
                located=fmt_bool(bool(row["located"])),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 门控表",
            "",
            "| gate | available | needed | gap | route | closed |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 5. 当前结论",
            "",
            "外部 theorem/proposition/page 的定位已经不再是剩余终端。真正剩余为：",
            "",
            "```text",
            "DIBFIOriginalDispersionCurrentWindowHypothesisMatch",
            "```",
            "",
            "下一步只能逐项核对当前未中心化 WFD 窗口是否满足 BFI Theorem 10 与 DI Theorem 12 的输入假设；"
            "不能再把缺口退回为泛泛的外部引用问题。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--generic-wfd-dibfi-json", type=Path, default=DEFAULT_GENERIC_WFD_DIBFI
    )
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        generic_wfd_dibfi_path=args.generic_wfd_dibfi_json,
        external_index_path=args.external_index_md,
        kls_template_path=args.kls_template_md,
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
                "theorem_locations_pinned": result["theorem_locations_pinned"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
