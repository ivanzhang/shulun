#!/usr/bin/env python3
"""审计 A1 diffuse fixed-projection 平坦到 NC-BLK moving-block 非集中的缺口。

用法示例：
  python3 experiments/prime_matrix_triad_a1_ncblk_projection_gap_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-ncblk-projection-gap-router.json
  docs/monograph/prime-matrix-triad-a1-ncblk-projection-gap-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_A1_CLEAN = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_SC9_FRONTIER = (
    DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json"
)
DEFAULT_BLK_OBSTRUCTION = DOCS / "prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_BD_CEN = DOCS / "prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-ncblk-projection-gap-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-ncblk-projection-gap-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_gap_rows() -> list[dict[str, Any]]:
    """构造 fixed-projection 到 moving-block 的缺口表。"""
    return [
        {
            "gate": "FixedProjectionDiffuse",
            "available_from_a1": "for every fixed finite payment signature, mass tends to zero on the diffuse branch",
            "needed_for_ncblk": "uniform control over moving same-(u,v) blocks whose labels grow with the scale",
            "gap": "fixed projections do not see moving blocks",
            "route": "needs moving-block spread input or external dispersion",
            "closed": False,
        },
        {
            "gate": "L2FlatFiniteAtoms",
            "available_from_a1": "max atom/L2-flat admission language after finite-projection dichotomy",
            "needed_for_ncblk": "arbitrary log saving in sum_b |S_b|^2 for actual WFD blocks",
            "gap": "L2 flatness at fixed level gives no log^{-A} saving for an adversarial moving block family",
            "route": "needs scale-uniform L2 block-energy decay",
            "closed": False,
        },
        {
            "gate": "WellFactorableSupport",
            "available_from_a1": "well-factorable/dyadic decomposition of moduli",
            "needed_for_ncblk": "block non-concentration inside each balanced factor pair",
            "gap": "well-factorable factorization allows decomposition but does not force each factor block to have zero local mean",
            "route": "needs original DI/BFI dispersion centering or source spread theorem",
            "closed": False,
        },
        {
            "gate": "CurrentNoGoResults",
            "available_from_a1": "BD-CEN, SOURCE-CEN, and raw BLK-energy routes are refuted/blocked",
            "needed_for_ncblk": "a new true source statement for actual coefficients",
            "gap": "the existing square-kernel object cannot manufacture block centering after the fact",
            "route": "prove NC-BLK from upstream coefficient generation, not from the current kernel alone",
            "closed": True,
        },
    ]


def build_required_input_rows() -> list[dict[str, str]]:
    """列出能真正闭合 NC-BLK 的可接受输入。"""
    return [
        {
            "input": "MovingBlockSpread",
            "statement": "for every balanced block b=(u,v), actual WFD mass in b has max block share o(log^{-A}) after dyadic/Type decomposition",
            "would_imply": "NC-BLK block energy saving",
            "status": "not_present_in_current_a1_ledger",
        },
        {
            "input": "SourceDispersionCentering",
            "statement": "the original dispersion identity enters KZ-E with same-(u,v) local variance already subtracted",
            "would_imply": "BD-CEN/NC-BLK without changing the target",
            "status": "refuted_for_current_rewritten_WFD_object; possible only from original DI/BFI theorem",
        },
        {
            "input": "ExternalDIBFIOriginalDispersion",
            "statement": "an external theorem directly estimates the uncentered WFD target or supplies the required local block variance subtraction",
            "would_imply": "A1 clean branch closed in external-deep-theorem version",
            "status": "acceptable_external_route",
        },
    ]


def run(
    a1_clean_path: Path,
    sc9_frontier_path: Path,
    blk_obstruction_path: Path,
    source_cen_path: Path,
    bd_cen_path: Path,
) -> dict[str, Any]:
    """运行 NC-BLK 投影缺口路由。"""
    a1_clean = load_json(a1_clean_path)
    sc9_frontier = load_json(sc9_frontier_path)
    gap_rows = build_gap_rows()
    required_inputs = build_required_input_rows()
    current_internal_ncblk_closed = all(row["closed"] for row in gap_rows)
    fixed_projection_gap_exists = any(not row["closed"] for row in gap_rows)
    return {
        "certificate_type": "triad_a1_ncblk_projection_gap_router",
        "status": "ncblk_requires_moving_block_spread_or_external_dibfi",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "a1_clean_kls_external_input_json": file_sha256(a1_clean_path),
            "sc9_frontier_json": file_sha256(sc9_frontier_path),
            "blk_energy_obstruction_md": file_sha256(blk_obstruction_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
            "bd_cen_no_go_md": file_sha256(bd_cen_path),
        },
        "a1_clean_status": a1_clean["status"],
        "sc9_frontier_status": sc9_frontier["status"],
        "gap_rows": gap_rows,
        "required_input_rows": required_inputs,
        "fixed_projection_gap_exists": fixed_projection_gap_exists,
        "current_internal_ncblk_closed": current_internal_ncblk_closed,
        "terminal_gap_after_router": "MovingBlockSpreadNCBLKOrExternalDIBFIOriginalDispersion",
        "internal_route_status": "open_needs_moving_block_spread_theorem",
        "external_route_status": "open_needs_precise_di_bfi_original_dispersion_citation",
        "structural_law": (
            "A1 diffuse/clean admission controls fixed finite signatures. NC-BLK is a moving-block "
            "statement over balanced same-(u,v) blocks created after well-factorable splitting. "
            "A sequence may be flat on every fixed finite projection while concentrating on a block "
            "whose label moves with the scale. Therefore fixed-projection flatness does not imply "
            "NC-BLK. Since BD-CEN, SOURCE-CEN, and raw BLK-energy have been blocked, the only honest "
            "internal route is a new moving-block spread theorem for the actual WFD coefficients; "
            "the honest external route is original DI/BFI dispersion with the required local variance subtraction."
        ),
        "review_conclusion": (
            "NC-BLK 不能由当前 A1 fixed-projection diffuse 账本直接推出。"
            "当前最窄硬点继续压缩为：证明 moving-block spread 定理，或精确引用外部 DI/BFI 原始 dispersion。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 NC-BLK 投影缺口路由器",
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
        "A1 diffuse branch controls fixed finite signatures;",
        "NC-BLK asks for moving same-(u,v) block non-concentration;",
        "fixed projection flatness does not control moving labels;",
        "therefore NC-BLK needs MovingBlockSpread or external DI/BFI.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `a1_clean_status={result['a1_clean_status']}`。",
        f"- `sc9_frontier_status={result['sc9_frontier_status']}`。",
        f"- `fixed_projection_gap_exists={result['fixed_projection_gap_exists']}`。",
        f"- `current_internal_ncblk_closed={result['current_internal_ncblk_closed']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        f"- `internal_route_status={result['internal_route_status']}`。",
        f"- `external_route_status={result['external_route_status']}`。",
        "",
        "## 3. 缺口表",
        "",
        "| gate | available from A1 | needed for NC-BLK | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gap_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=row["gate"],
                available=row["available_from_a1"],
                needed=row["needed_for_ncblk"],
                gap=row["gap"],
                route=row["route"],
                closed=row["closed"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 可接受输入",
            "",
            "| input | statement | would imply | status |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["required_input_rows"]:
        lines.append(
            "| `{input}` | {statement} | {would_imply} | `{status}` |".format(
                input=row["input"],
                statement=row["statement"],
                would_imply=row["would_imply"],
                status=row["status"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            "当前不能把 `NC-BLK` 标为已证。真正剩余已经比上一轮更窄：",
            "",
            "```text",
            "内部无黑箱版：证明 MovingBlockSpreadNCBLK；",
            "外部深定理版：引用带局部方差扣除的 DI/BFI 原始 dispersion。",
            "```",
            "",
            "这一步的作用是排除“fixed-projection flat => moving-block NC-BLK”的隐含跳步。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a1-clean-json", type=Path, default=DEFAULT_A1_CLEAN)
    parser.add_argument("--sc9-frontier-json", type=Path, default=DEFAULT_SC9_FRONTIER)
    parser.add_argument("--blk-obstruction-md", type=Path, default=DEFAULT_BLK_OBSTRUCTION)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--bd-cen-md", type=Path, default=DEFAULT_BD_CEN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        a1_clean_path=args.a1_clean_json,
        sc9_frontier_path=args.sc9_frontier_json,
        blk_obstruction_path=args.blk_obstruction_md,
        source_cen_path=args.source_cen_md,
        bd_cen_path=args.bd_cen_md,
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
                "fixed_projection_gap_exists": result["fixed_projection_gap_exists"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
