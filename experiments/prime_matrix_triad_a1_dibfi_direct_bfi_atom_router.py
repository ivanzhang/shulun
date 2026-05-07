#!/usr/bin/env python3
"""把 DI/BFI 量化无投影证书压成直接 BFI-AP 原子或 KE-13 逐项路线。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_direct_bfi_atom_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_TRANSFER_SCALE = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_THEOREM_LOCATION = (
    DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
)
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.md"


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


def build_route_rows(
    transfer_scale: dict[str, Any],
    theorem_location: dict[str, Any],
    external_index_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
) -> list[dict[str, Any]]:
    """构造直接 BFI 与 KE-13 逐项路线的分叉表。"""
    source_ids = {row["source_id"] for row in theorem_location["source_rows"]}
    bfi_pinned = (
        bool(theorem_location["theorem_locations_pinned"])
        and "BFI1987-Theorem10" in source_ids
        and contains_all(external_index_path, ["BFI1987-Theorem10", "well-factorable"])
    )
    kze_has_type = contains_all(kze_spine_path, ["Vaughan/Heath-Brown", "Type-I/II"])
    source_cen_blocked = contains_all(
        source_cen_path,
        ["SOURCE-CEN is false", "当前 WFD-core", "未块中心化"],
    )
    return [
        {
            "route": "DirectBFIPrimeAPAtom",
            "role": "preferred_if_source_can_be_lifted_to_prime_ap_error",
            "closed": False,
            "available": bfi_pinned and kze_has_type,
            "absorbs": [
                "DispersionCauchyNoCenteringIdentity",
                "KE13DyadicExhaustionNoProjection",
                "KLSModulusWindowQuantified",
                "InverseVariableWindowQuantified",
                "DIJScaleDominanceSubstitution",
            ],
            "still_needs": [
                "PrimeAPResidualRepresentation",
                "BFILevelSubstitution",
                "WellFactorableLambdaLevel",
            ],
            "reason": (
                "若直接引用 BFI Theorem 10，则 dispersion/DI J-scale 是定理证明内部内容；"
                "外部引用版不应再要求本文重证 KE-13 的无投影逐项展开。"
            ),
        },
        {
            "route": "SeparateKE13DIBFIWindow",
            "role": "fallback_if_only_ke13_window_is_available",
            "closed": False,
            "available": source_cen_blocked,
            "absorbs": [],
            "still_needs": [
                "NoProjectionUncenteredDispersionIdentity",
                "QuantifiedDIBFIWindowSubstitution",
            ],
            "reason": (
                "若上游只能给出孤立 KE-13/WFD-core 窗口，而不能提升回 BFI prime-AP 误差，"
                "则必须继续证明无中心化、无投影、无 dyadic 主块遗漏，并逐项代入 DI/BFI 尺度。"
            ),
        },
        {
            "route": "HLCWindowedKLSAtom",
            "role": "closed_for_clean_hlc_branch_only",
            "closed": True,
            "available": True,
            "absorbs": ["CleanHLCWindow"],
            "still_needs": [],
            "reason": (
                "A1 clean/HLC 分支已有窗口化外部 KLS 适配；但它不是 generic WFD 共同变量表的"
                "直接替代品。"
            ),
        },
        {
            "route": "CurrentTransferScaleFrontier",
            "role": "input_being_reduced",
            "closed": False,
            "available": True,
            "absorbs": [],
            "still_needs": transfer_scale["open_terminal_targets"],
            "reason": "上一轮终端被本轮二分为 DirectBFIPrimeAPAtom 或 SeparateKE13DIBFIWindow。",
        },
    ]


def build_gate_rows(route_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """列出直接 BFI 原子的最小门控。"""
    direct = next(row for row in route_rows if row["route"] == "DirectBFIPrimeAPAtom")
    separate = next(row for row in route_rows if row["route"] == "SeparateKE13DIBFIWindow")
    return [
        {
            "gate": "BFIAtomAvailable",
            "closed": bool(direct["available"]),
            "needed": "BFI Theorem 10 is pinned as a well-factorable prime-AP dispersion atom",
            "if_fail": "cannot use direct BFI route",
        },
        {
            "gate": "PrimeAPResidualRepresentation",
            "closed": False,
            "needed": (
                "把当前 clean A1/generic WFD 残差提升为 BFI prime-AP discrepancy，"
                "而不是只给一个孤立 KE-13 子窗口。"
            ),
            "if_fail": "fall back to SeparateKE13DIBFIWindow",
        },
        {
            "gate": "BFILevelSubstitution",
            "closed": False,
            "needed": "显式证明 Q <= X^(4/7-eps) 或采用已定位定理允许的等价更强范围。",
            "if_fail": "direct BFI route not closed",
        },
        {
            "gate": "WellFactorableLambdaLevel",
            "closed": False,
            "needed": "证明 lambda_q 的 level 与 well-factorable 分解正是 BFI Theorem 10 输入。",
            "if_fail": "direct BFI route not closed",
        },
        {
            "gate": "KE13FallbackStillAvailable",
            "closed": bool(separate["available"]),
            "needed": "若直接 BFI 不可用，保留 KE-13 无投影逐项路线。",
            "if_fail": "both external routes malformed",
        },
    ]


def run(
    transfer_scale_path: Path,
    common_variable_table_path: Path,
    theorem_location_path: Path,
    external_index_path: Path,
    kze_spine_path: Path,
    source_cen_path: Path,
) -> dict[str, Any]:
    """运行直接 BFI 原子路由。"""
    transfer_scale = load_json(transfer_scale_path)
    common_variable_table = load_json(common_variable_table_path)
    theorem_location = load_json(theorem_location_path)
    route_rows = build_route_rows(
        transfer_scale,
        theorem_location,
        external_index_path,
        kze_spine_path,
        source_cen_path,
    )
    gate_rows = build_gate_rows(route_rows)
    open_gates = [row["gate"] for row in gate_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_direct_bfi_atom_router",
        "status": "dibfi_quantified_no_projection_reduced_to_direct_bfi_atom_or_ke13_fallback_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "transfer_scale_json": file_sha256(transfer_scale_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "dibfi_theorem_location_json": file_sha256(theorem_location_path),
            "external_theorem_index_md": file_sha256(external_index_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
        },
        "previous_terminal_gap": transfer_scale["terminal_gap_after_router"],
        "common_table_terminal": common_variable_table["terminal_gap_after_router"],
        "route_rows": route_rows,
        "gate_rows": gate_rows,
        "open_gates": open_gates,
        "direct_bfi_atom_available": next(
            row for row in route_rows if row["route"] == "DirectBFIPrimeAPAtom"
        )["available"],
        "direct_bfi_atom_closed": False,
        "ke13_fallback_open": True,
        "next_external_target": "DIBFIDirectBFIAPAtomMatchOrKE13NoProjection",
        "terminal_gap_after_router": "DIBFIDirectBFIAPAtomMatchOrKE13NoProjection",
        "structural_law": (
            "If the current residual can be represented at the prime-AP level, BFI Theorem 10 "
            "should be used as one atom: its internal dispersion and DI/Kloosterman estimates absorb "
            "the no-projection and J-scale obligations. If the proof only has an isolated KE-13/WFD "
            "window, those obligations remain external and must be proved separately."
        ),
        "review_conclusion": (
            "量化无投影终端已被继续压缩为一个分叉：首选路线是直接 BFI prime-AP 原子，只剩"
            " prime-AP 残差表示、BFI level 代入和 well-factorable level；若不能提升回 AP 原子，"
            "则回到 KE-13 无投影逐项路线。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 直接 BFI 原子路由器",
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
        "previous:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "preferred route:",
        "  DirectBFIPrimeAPAtom;",
        "",
        "fallback route:",
        "  SeparateKE13DIBFIWindow.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `direct_bfi_atom_available={fmt_bool(result['direct_bfi_atom_available'])}`。",
        f"- `direct_bfi_atom_closed={fmt_bool(result['direct_bfi_atom_closed'])}`。",
        f"- `ke13_fallback_open={fmt_bool(result['ke13_fallback_open'])}`。",
        f"- `open_gates={result['open_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 路线表",
        "",
        "| route | role | available | closed | absorbs | still needs | reason |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["route_rows"]:
        lines.append(
            "| `{route}` | `{role}` | `{available}` | `{closed}` | {absorbs} | {needs} | {reason} |".format(
                route=table_cell(row["route"]),
                role=table_cell(row["role"]),
                available=fmt_bool(bool(row["available"])),
                closed=fmt_bool(bool(row["closed"])),
                absorbs=table_cell(", ".join(row["absorbs"])),
                needs=table_cell(", ".join(row["still_needs"])),
                reason=table_cell(row["reason"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 门控表",
            "",
            "| gate | closed | needed | if fail |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {needed} | {if_fail} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                needed=table_cell(row["needed"]),
                if_fail=table_cell(row["if_fail"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            "这一步把 DI/BFI 终端的逻辑顺序纠正为：优先尝试回到 BFI 的 prime-AP 原始误差对象。"
            "若成功，则不需要本文重证 DI 的 J-scale 或 KE-13 无投影展开；那些是 BFI 原子内部内容。"
            "若不能成功，才继续走 KE-13 逐项路线。",
            "",
            "因此下一硬点从两个并列大项压成：",
            "",
            "```text",
            "DIBFIDirectBFIAPAtomMatchOrKE13NoProjection",
            "  preferred: PrimeAPResidualRepresentation + BFILevelSubstitution + WellFactorableLambdaLevel;",
            "  fallback:  NoProjectionUncenteredDispersionIdentity + QuantifiedDIBFIWindowSubstitution.",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transfer-scale-json", type=Path, default=DEFAULT_TRANSFER_SCALE)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument(
        "--dibfi-theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION
    )
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        transfer_scale_path=args.transfer_scale_json,
        common_variable_table_path=args.common_variable_table_json,
        theorem_location_path=args.dibfi_theorem_location_json,
        external_index_path=args.external_index_md,
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
                "direct_bfi_atom_available": result["direct_bfi_atom_available"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
