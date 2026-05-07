#!/usr/bin/env python3
"""把 ExternalFullSDIBFIAtomMatch 拆成外部 KLS 专门化合同。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_external_full_s_match_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-external-full-s-match-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-external-full-s-match-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_FULL_S_ATOM = (
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-dispersion-atom-router.json"
)
DEFAULT_THEOREM_LOCATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
)
DEFAULT_BFI_LEVEL_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.json"
)
DEFAULT_NONAP_OBJECT_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-nonap-object-ledger-router.json"
)
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-external-full-s-match-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-external-full-s-match-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_match_rows(
    full_s_atom: dict[str, Any],
    theorem_location: dict[str, Any],
    bfi_level_ledger: dict[str, Any],
    nonap_object_ledger: dict[str, Any],
    external_index_path: Path,
    kls_template_path: Path,
) -> list[dict[str, Any]]:
    """构造外部 full-S 匹配账本。"""
    kls_has_full_s_window = contains_all(
        kls_template_path,
        [
            "C ≍ P/log",
            "S ≍ P",
            "0<|h|<=H<=P/log",
            "目标强度",
        ],
    )
    kls_has_phase_gcd_smoothing = contains_all(
        kls_template_path,
        [
            "相位归一化",
            "非互素 gcd 层",
            "B(A)",
            "平滑",
        ],
    )
    index_has_required_sources = contains_all(
        external_index_path,
        [
            "BFI1987-Theorem10",
            "DI1982-Theorem12",
            "KLS-window",
        ],
    )
    return [
        {
            "gate": "PriorExternalFullSAtomFrontierAvailable",
            "closed": full_s_atom["terminal_gap_after_router"] == "ExternalFullSDIBFIAtomMatch",
            "evidence": "full-S 原子已被上一层改写为 ExternalFullSDIBFIAtomMatch。",
            "remaining": "none at prior-frontier level",
            "next_target": "FullSWindowKLSTemplateMatch",
        },
        {
            "gate": "DIBFITheoremLocationsPinned",
            "closed": bool(theorem_location["theorem_locations_pinned"]) and index_has_required_sources,
            "evidence": "外部索引和定理位置路由均登记 BFI Theorem 10 与 DI Theorem 12。",
            "remaining": "none at theorem-location level",
            "next_target": "FullSWindowKLSTemplateMatch",
        },
        {
            "gate": "FullSWindowKLSTemplateMatch",
            "closed": kls_has_full_s_window,
            "evidence": "KLS 模板已经写入 C≈P/log^{O(1)}P、S≈P、H<=P/log^{O(1)}P。",
            "remaining": "模板匹配不等于原文定理专门化；仍需审稿级引用语句。",
            "next_target": "ExactExternalKLSSpecialization",
        },
        {
            "gate": "BFILevelSlackAtQHalf",
            "closed": bool(bfi_level_ledger["bfi_level_exponent_ledger_closed"]),
            "evidence": "BFI level 账本已证明 X≈P^2、Q<=P log^O P 给出正指数余量。",
            "remaining": "none at BFI level exponent level",
            "next_target": "ExactExternalKLSSpecialization",
        },
        {
            "gate": "PhaseGcdSmoothingTemplateReady",
            "closed": kls_has_phase_gcd_smoothing,
            "evidence": "KLS 模板已有 CRT 相位、gcd 层、平滑和 B(A) 损失账本。",
            "remaining": "仍需把这些模板行逐项对应到最终引用定理。",
            "next_target": "ExactExternalKLSSpecialization",
        },
        {
            "gate": "NoProjectionCompatibilityStillOpen",
            "closed": False,
            "evidence": (
                "non-AP 对象侧仍开放 "
                f"{nonap_object_ledger['open_object_gates']}。"
            ),
            "remaining": "必须证明外部 KLS 专门化估计的是当前未中心化、无投影对象。",
            "next_target": "UncenteredWFDToKE13NoProjectionIdentity",
        },
        {
            "gate": "ExactExternalKLSSpecialization",
            "closed": False,
            "evidence": "当前只有功能性模板，没有把 DI/BFI 原文定理专门化为 Full-S KLS-ext 命题。",
            "remaining": (
                "写出审稿级 Theorem FullS-KLS-ext：假设 C,S,H,lambda,beta,omega 满足模板，"
                "则给出当前 full-S 窗口的任意 log-saving。"
            ),
            "next_target": "FullSKLSExternalTheoremSpecialization",
        },
    ]


def run(
    full_s_atom_path: Path,
    theorem_location_path: Path,
    bfi_level_ledger_path: Path,
    nonap_object_ledger_path: Path,
    external_index_path: Path,
    kls_template_path: Path,
) -> dict[str, Any]:
    """运行外部 full-S 匹配路由。"""
    full_s_atom = load_json(full_s_atom_path)
    theorem_location = load_json(theorem_location_path)
    bfi_level_ledger = load_json(bfi_level_ledger_path)
    nonap_object_ledger = load_json(nonap_object_ledger_path)
    match_rows = build_match_rows(
        full_s_atom,
        theorem_location,
        bfi_level_ledger,
        nonap_object_ledger,
        external_index_path,
        kls_template_path,
    )
    open_match_gates = [row["gate"] for row in match_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_external_full_s_match_router",
        "status": "external_full_s_match_reduced_to_kls_specialization_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "full_s_atom_json": file_sha256(full_s_atom_path),
            "theorem_location_json": file_sha256(theorem_location_path),
            "bfi_level_ledger_json": file_sha256(bfi_level_ledger_path),
            "nonap_object_ledger_json": file_sha256(nonap_object_ledger_path),
            "external_index_md": file_sha256(external_index_path),
            "kls_template_md": file_sha256(kls_template_path),
        },
        "previous_terminal_gap": full_s_atom["terminal_gap_after_router"],
        "match_rows": match_rows,
        "closed_match_gates": [row["gate"] for row in match_rows if row["closed"]],
        "open_match_gates": open_match_gates,
        "external_full_s_match_closed": False,
        "terminal_gap_after_router": "FullSKLSExternalTheoremSpecialization",
        "terminal_gap_expansion": [
            "ExactExternalKLSSpecialization",
            "NoProjectionCompatibilityStillOpen",
        ],
        "structural_law": (
            "The full-S external route now has a precise checklist. The local template already "
            "contains the critical full-S window C≈P/log^O(1), S≈P and H<=P/log^O(1), and the "
            "BFI level ledger has positive exponent slack. What is still missing is not another "
            "parameter search; it is an exact FullS-KLS-ext theorem specialization plus proof that "
            "the specialization estimates the current uncentered non-projected WFD object."
        ),
        "review_conclusion": (
            "`ExternalFullSDIBFIAtomMatch` 已被压成 `FullSKLSExternalTheoremSpecialization`："
            "full-S 窗口、BFI level、相位/gcd/平滑模板均已就绪；剩余是写出精确外部 KLS "
            "专门化定理，并证明其无隐藏投影地作用于当前 non-AP WFD 对象。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI external full-S match 路由器",
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
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "expansion:",
        f"  {result['terminal_gap_expansion']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `external_full_s_match_closed={fmt_bool(result['external_full_s_match_closed'])}`。",
        f"- `closed_match_gates={result['closed_match_gates']}`。",
        f"- `open_match_gates={result['open_match_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 匹配账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["match_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "最新外部解析剩余为：",
            "",
            "```text",
            "FullSKLSExternalTheoremSpecialization:",
            "  ExactExternalKLSSpecialization;",
            "  no hidden projection/centering compatibility with current non-AP WFD object.",
            "```",
            "",
            "这一步把外部 full-S 原子继续压成审稿级 KLS 专门化定理，而不是宣称已闭合。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-s-atom-json", type=Path, default=DEFAULT_FULL_S_ATOM)
    parser.add_argument("--theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION)
    parser.add_argument("--bfi-level-ledger-json", type=Path, default=DEFAULT_BFI_LEVEL_LEDGER)
    parser.add_argument(
        "--nonap-object-ledger-json", type=Path, default=DEFAULT_NONAP_OBJECT_LEDGER
    )
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        full_s_atom_path=args.full_s_atom_json,
        theorem_location_path=args.theorem_location_json,
        bfi_level_ledger_path=args.bfi_level_ledger_json,
        nonap_object_ledger_path=args.nonap_object_ledger_json,
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
                "open_match_gates": result["open_match_gates"],
                "terminal_gap": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
