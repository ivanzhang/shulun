#!/usr/bin/env python3
"""把 A1 clean KLS 的 SC-9 谱大筛原子路由到 NC-BLK 或外部 DI/BFI。

用法示例：
  python3 experiments/prime_matrix_triad_a1_kuznetsov_ls_atom_frontier_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json
  docs/monograph/prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.md
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
DEFAULT_KLS_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kls-core-self-contained-spine.md"
DEFAULT_KZ_EXPANSION = DOCS / "prime-matrix-h3-dsb-hlc-kuznetsov-ls-atom-expansion.md"
DEFAULT_KZ_B = DOCS / "prime-matrix-h3-dsb-hlc-kz-b-kuznetsov-trace-specialization.md"
DEFAULT_KZ_C = DOCS / "prime-matrix-h3-dsb-hlc-kz-c-bessel-transform-decay.md"
DEFAULT_KZ_D = DOCS / "prime-matrix-h3-dsb-hlc-kz-d-spectral-large-sieve-spine.md"
DEFAULT_KZ_E = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_SOURCE_CEN = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_BD_CEN = DOCS / "prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md"
DEFAULT_BLK_OBSTRUCTION = DOCS / "prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_subatom_rows() -> list[dict[str, str]]:
    """列出 SC-9 的子原子当前状态。"""
    return [
        {
            "subatom": "KZ-A",
            "role": "Kloosterman modulus smoothing and L2 bookkeeping",
            "status": "closed_elementary_smoothing",
            "remaining": "none",
        },
        {
            "subatom": "KZ-B",
            "role": "Kuznetsov trace formula specialization",
            "status": "closed_by_trace_specialization_document",
            "remaining": "none",
        },
        {
            "subatom": "KZ-C",
            "role": "Bessel transform window decay",
            "status": "closed_by_bessel_decay_document",
            "remaining": "none",
        },
        {
            "subatom": "KZ-D",
            "role": "spectral large sieve with oldform/Eisenstein bookkeeping",
            "status": "closed_by_pretrace_kernel_chain",
            "remaining": "none",
        },
        {
            "subatom": "KZ-E",
            "role": "well-factorable dispersion logarithmic saving",
            "status": "reduced_to_ncblk_or_external_dibfi",
            "remaining": "NC-BLK actual block non-concentration or external DI/BFI original dispersion",
        },
    ]


def build_blocking_rows() -> list[dict[str, str]]:
    """列出 KZ-E 内部路线已排除的伪出口。"""
    return [
        {
            "candidate": "BD-CEN identity",
            "verdict": "blocked",
            "reason": "h=0 frequency centering is not same-(u,v) block centering",
        },
        {
            "candidate": "SOURCE-CEN identity",
            "verdict": "refuted",
            "reason": "it changes the current WFD target rather than rewriting it",
        },
        {
            "candidate": "raw BLK-energy-core",
            "verdict": "false_for_arbitrary_coefficient_arrays",
            "reason": "single-block single-atom test defeats arbitrary log saving",
        },
        {
            "candidate": "NC-BLK",
            "verdict": "remaining_internal_route",
            "reason": "must prove actual WFD coefficients are block-nonconcentrated",
        },
        {
            "candidate": "external DI/BFI",
            "verdict": "remaining_external_route",
            "reason": "original dispersion theorem may supply the needed block variance subtraction",
        },
    ]


def run(
    a1_clean_path: Path,
    kls_spine_path: Path,
    kz_expansion_path: Path,
    kz_b_path: Path,
    kz_c_path: Path,
    kz_d_path: Path,
    kz_e_path: Path,
    source_cen_path: Path,
    bd_cen_path: Path,
    blk_obstruction_path: Path,
) -> dict[str, Any]:
    """运行 SC-9 前沿路由。"""
    a1_clean = load_json(a1_clean_path)
    subatom_rows = build_subatom_rows()
    blocking_rows = build_blocking_rows()
    all_sc9_subatoms_routed = all(row["status"] != "open" for row in subatom_rows)
    return {
        "certificate_type": "triad_a1_kuznetsov_ls_atom_frontier_router",
        "status": "a1_sc9_frontier_routed_to_ncblk_or_external_dibfi",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "a1_clean_kls_external_input_json": file_sha256(a1_clean_path),
            "kls_core_self_contained_spine_md": file_sha256(kls_spine_path),
            "kuznetsov_ls_atom_expansion_md": file_sha256(kz_expansion_path),
            "kz_b_trace_specialization_md": file_sha256(kz_b_path),
            "kz_c_bessel_decay_md": file_sha256(kz_c_path),
            "kz_d_spectral_large_sieve_md": file_sha256(kz_d_path),
            "kz_e_dispersion_spine_md": file_sha256(kz_e_path),
            "source_cen_no_go_md": file_sha256(source_cen_path),
            "bd_cen_no_go_md": file_sha256(bd_cen_path),
            "blk_energy_obstruction_md": file_sha256(blk_obstruction_path),
        },
        "a1_clean_input_status": a1_clean["status"],
        "a1_external_kls_input_registered": bool(
            a1_clean["external_kls_input_registered"]
        ),
        "subatom_rows": subatom_rows,
        "blocking_rows": blocking_rows,
        "all_sc9_subatoms_routed": all_sc9_subatoms_routed,
        "self_contained_terminal_gap": "NCBLKActualWFDCoefficientBlockNonConcentration",
        "external_terminal_gap": "ExternalDIBFIOriginalDispersionCitation",
        "terminal_gap_after_router": "NCBLKOrExternalDIBFIOriginalDispersion",
        "external_deep_theorem_version_status": (
            "closed_for_a1_clean_branch_if_original_di_bfi_dispersion_or_equivalent_windowed_kls_is_accepted"
        ),
        "self_contained_version_status": "open_at_ncblk_actual_block_nonconcentration",
        "structural_law": (
            "The A1 clean branch reaches SC-9 only after K1--K9 admission. Existing HLC/KLS "
            "documents expand SC-9 into KZ-A--KZ-E. KZ-A--KZ-D are routed by smoothing, trace "
            "specialization, Bessel decay, and spectral large-sieve/pretrace chains. KZ-E is "
            "not closed internally: block-centering identities and raw block-energy estimates "
            "have been refuted, leaving NC-BLK for actual WFD coefficients or an external "
            "DI/BFI original dispersion theorem."
        ),
        "review_conclusion": (
            "A1 的 SC-9 谱大筛口已经继续压缩：不是泛泛的 Kuznetsov 大筛缺口，"
            "而是 KZ-E 内部路线的真实阻断 `NC-BLK`，或明确转入外部 DI/BFI 原始 dispersion 引用。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Kuznetsov-LS 原子前沿路由器",
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
        "A1 clean KLS input",
        "  => SC-9 Kuznetsov-LS atom;",
        "SC-9",
        "  => KZ-A + KZ-B + KZ-C + KZ-D + KZ-E;",
        "KZ-A--KZ-D",
        "  => already routed by existing self-contained spines;",
        "KZ-E",
        "  => NC-BLK actual block non-concentration",
        "  or external DI/BFI original dispersion.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `a1_clean_input_status={result['a1_clean_input_status']}`。",
        f"- `a1_external_kls_input_registered={result['a1_external_kls_input_registered']}`。",
        f"- `all_sc9_subatoms_routed={result['all_sc9_subatoms_routed']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        f"- `self_contained_version_status={result['self_contained_version_status']}`。",
        f"- `external_deep_theorem_version_status={result['external_deep_theorem_version_status']}`。",
        "",
        "## 3. SC-9 子原子",
        "",
        "| subatom | role | status | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["subatom_rows"]:
        lines.append(
            "| `{subatom}` | {role} | `{status}` | {remaining} |".format(
                subatom=row["subatom"],
                role=row["role"],
                status=row["status"],
                remaining=row["remaining"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. KZ-E 阻断与剩余路线",
            "",
            "| candidate | verdict | reason |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["blocking_rows"]:
        lines.append(
            "| `{candidate}` | `{verdict}` | {reason} |".format(
                candidate=row["candidate"],
                verdict=row["verdict"],
                reason=row["reason"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            "A1 clean KLS 的自足版硬点现在不应再写成宽泛的 `SC-9`：",
            "",
            "```text",
            "self-contained route => prove NC-BLK for actual WFD coefficients；",
            "external route        => cite DI/BFI original dispersion or equivalent windowed KLS theorem。",
            "```",
            "",
            "这一步仍不是最终无黑箱证明；它排除了块中心化伪恒等式和裸块能量伪路线，留下真实最窄硬点。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a1-clean-json", type=Path, default=DEFAULT_A1_CLEAN)
    parser.add_argument("--kls-spine-md", type=Path, default=DEFAULT_KLS_SPINE)
    parser.add_argument("--kz-expansion-md", type=Path, default=DEFAULT_KZ_EXPANSION)
    parser.add_argument("--kz-b-md", type=Path, default=DEFAULT_KZ_B)
    parser.add_argument("--kz-c-md", type=Path, default=DEFAULT_KZ_C)
    parser.add_argument("--kz-d-md", type=Path, default=DEFAULT_KZ_D)
    parser.add_argument("--kz-e-md", type=Path, default=DEFAULT_KZ_E)
    parser.add_argument("--source-cen-md", type=Path, default=DEFAULT_SOURCE_CEN)
    parser.add_argument("--bd-cen-md", type=Path, default=DEFAULT_BD_CEN)
    parser.add_argument("--blk-obstruction-md", type=Path, default=DEFAULT_BLK_OBSTRUCTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        a1_clean_path=args.a1_clean_json,
        kls_spine_path=args.kls_spine_md,
        kz_expansion_path=args.kz_expansion_md,
        kz_b_path=args.kz_b_md,
        kz_c_path=args.kz_c_md,
        kz_d_path=args.kz_d_md,
        kz_e_path=args.kz_e_md,
        source_cen_path=args.source_cen_md,
        bd_cen_path=args.bd_cen_md,
        blk_obstruction_path=args.blk_obstruction_md,
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
                "all_sc9_subatoms_routed": result["all_sc9_subatoms_routed"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
