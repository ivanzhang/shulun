#!/usr/bin/env python3
"""把 c 依赖 residue 谱输入接入 BSC/KFLS/NC-BLK 核心链。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_c_dependent_residue_spectral_reduction_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_COMPLETED_WEIGHT_SPECTRAL_GAP = (
    DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json"
)
DEFAULT_BWFD_COMPLETION = (
    DOCS / "prime-matrix-h3-dsb-hlc-bwfd-core-spectral-completion-attack.md"
)
DEFAULT_BSC_FRACTION = (
    DOCS / "prime-matrix-h3-dsb-hlc-bsc-core-kloosterman-fraction-attack.md"
)
DEFAULT_KFLS_SQUARE = (
    DOCS / "prime-matrix-h3-dsb-hlc-kfls-core-square-kernel-attack.md"
)
DEFAULT_CFQK_BLOCK = (
    DOCS / "prime-matrix-h3-dsb-hlc-cfqk-core-block-centering-attack.md"
)
DEFAULT_BD_CEN_NO_GO = DOCS / "prime-matrix-h3-dsb-hlc-bd-cen-no-go-route-fork.md"
DEFAULT_SOURCE_CEN_NO_GO = DOCS / "prime-matrix-h3-dsb-hlc-source-cen-no-go.md"
DEFAULT_BLK_ENERGY_OBSTRUCTION = (
    DOCS / "prime-matrix-h3-dsb-hlc-blk-energy-core-obstruction.md"
)
DEFAULT_JSON = (
    DOCS
    / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
)
DEFAULT_MD = (
    DOCS
    / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.md"
)


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


def build_rows(
    completed_weight_spectral_gap: dict[str, Any],
    bwfd_completion_path: Path,
    bsc_fraction_path: Path,
    kfls_square_path: Path,
    cfqk_block_path: Path,
    bd_cen_no_go_path: Path,
    source_cen_no_go_path: Path,
    blk_energy_obstruction_path: Path,
) -> list[dict[str, Any]]:
    """构造 c 依赖 residue 谱输入的内核化路由账本。"""
    prior_ready = (
        completed_weight_spectral_gap["terminal_gap_after_router"]
        == "CDependentResidueWeightSpectralCancellationInput"
        and completed_weight_spectral_gap["open_spectral_gap_gates"]
        == ["CDependentResidueWeightSpectralCancellationInput"]
    )
    residue_fourier_equivalence = contains_all(
        bwfd_completion_path,
        [
            r"\widehat\beta_c(\ell)",
            "有限群",
            "Fourier 反演",
            "S(a_h+\\ell,b_h;c)",
            "Parseval",
        ],
    )
    balanced_factorization_ready = contains_all(
        bwfd_completion_path,
        [
            "U,V=C^{1/2}",
            "S(A,B;uv)",
            "BSC-core",
            "BSC-core => BWFD-core",
        ],
    )
    bsc_to_kfls_ready = contains_all(
        bsc_fraction_path,
        [
            "BSC-core",
            "KFLS-core",
            "互逆分数相位",
            r"{\bar v R\over u}+{\bar u T\over v}",
        ],
    )
    kfls_square_gap_ready = contains_all(
        kfls_square_path,
        [
            "KFLS-core",
            "平方核",
            "CFQK-core",
            "NC-BLK",
        ],
    )
    block_centering_no_go_ready = contains_all(
        cfqk_block_path,
        ["BD-CEN", "SOURCE-CEN", "BLK-energy-core", "NC-BLK"],
    ) and contains_all(
        bd_cen_no_go_path,
        ["BD-CEN is false", "SOURCE-CEN", "BLK-energy-core", "external DI/BFI"],
    )
    false_shortcuts_blocked = contains_all(
        source_cen_no_go_path,
        ["SOURCE-CEN is false", "current WFD-core", "BLK-energy-core"],
    ) and contains_all(
        blk_energy_obstruction_path,
        ["raw BLK-energy-core is false", "NC-BLK", "actual WFD coefficients"],
    )
    reduction_chain_closed = all(
        [
            prior_ready,
            residue_fourier_equivalence,
            balanced_factorization_ready,
            bsc_to_kfls_ready,
            kfls_square_gap_ready,
            block_centering_no_go_ready,
            false_shortcuts_blocked,
        ]
    )
    return [
        {
            "gate": "PriorCDependentResidueInputPinned",
            "closed": prior_ready,
            "evidence": (
                f"previous terminal={completed_weight_spectral_gap['terminal_gap_after_router']}; "
                f"open={completed_weight_spectral_gap['open_spectral_gap_gates']}."
            ),
            "remaining": "none at previous-frontier level",
            "next_target": "ResidueFourierCompletionEquivalence",
        },
        {
            "gate": "ResidueFourierCompletionEquivalence",
            "closed": residue_fourier_equivalence,
            "evidence": (
                "B_{c,x}=sum_{s≡x(c)} beta_s W(s/S), "
                "hat_beta_c(ell)=sum_x B_{c,x} e_c(-ell*x); hence the B_{c,x} "
                "Kloosterman residue sum is exactly the finite-Fourier completed "
                "sum (1/c) sum_ell hat_beta_c(ell) S(a_h+ell,b_h;c)."
            ),
            "remaining": "none; this is a finite Fourier identity, not an estimate",
            "next_target": "BalancedBSCCompletionCore",
        },
        {
            "gate": "BalancedWellFactorableBSCReduction",
            "closed": balanced_factorization_ready,
            "evidence": (
                "The HLC BWFD completion file already performs c=uv with "
                "U,V=C^{1/2}log^O(y) and rewrites the completed Kloosterman "
                "sum as BSC-core."
            ),
            "remaining": "BSC-core still needs logarithmic saving",
            "next_target": "BSCCore",
        },
        {
            "gate": "BSCToKFLSPhaseExpansion",
            "closed": bsc_to_kfls_ready,
            "evidence": (
                "Expanding the two complete Kloosterman sums exposes the rigid "
                "phase e(bar(v)R/u + bar(u)T/v), so BSC-core reduces to KFLS-core."
            ),
            "remaining": "KFLS-core is not proved by the expansion itself",
            "next_target": "KFLSCore",
        },
        {
            "gate": "KFLSToSquareKernelAudit",
            "closed": kfls_square_gap_ready,
            "evidence": (
                "The KFLS square-kernel audit rules out positive-kernel/Schur "
                "shortcuts and reduces the self-contained route to centered "
                "four-modulus control plus block-energy duties."
            ),
            "remaining": "block diagonal/local variance cannot be discarded for free",
            "next_target": "BlockCenteredFourModulusOrNCBLK",
        },
        {
            "gate": "BlockCenteringNoGoImported",
            "closed": block_centering_no_go_ready,
            "evidence": (
                "CFQK/BD-CEN audits show that h=0 centering is not same-(u,v) "
                "block centering; BD-CEN is false for the current unblocked object."
            ),
            "remaining": "must use real source non-concentration or external dispersion",
            "next_target": "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
        },
        {
            "gate": "SourceCENAndRawBLKEnergyShortcutsBlocked",
            "closed": false_shortcuts_blocked,
            "evidence": (
                "SOURCE-CEN changes the current WFD target, and raw BLK-energy "
                "is false as an arbitrary coefficient-array theorem."
            ),
            "remaining": "only actual-coefficient NC-BLK or an external theorem remains",
            "next_target": "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
        },
        {
            "gate": "ReductionChainToNCBLKOrExternal",
            "closed": reduction_chain_closed,
            "evidence": (
                "C-dependent residue weights are the Fourier-dual form of the "
                "existing BWFD/BSC completion chain; all free centering and "
                "ordinary large-sieve exits have already been ruled out."
            ),
            "remaining": "none at reduction level",
            "next_target": "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
        },
        {
            "gate": "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
            "closed": False,
            "evidence": (
                "The repository still lacks a proof that the actual full-S non-AP "
                "WFD coefficients are same-(u,v) block-nonconcentrated with "
                "arbitrary log saving, and also lacks a fully matched primary-source "
                "external DI/BFI theorem for this exact full-S object."
            ),
            "remaining": "prove actual-coefficient NC-BLK, or cite/match an external DI/BFI/Kuznetsov dispersion theorem",
            "next_target": "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
        },
    ]


def run(
    completed_weight_spectral_gap_path: Path,
    bwfd_completion_path: Path,
    bsc_fraction_path: Path,
    kfls_square_path: Path,
    cfqk_block_path: Path,
    bd_cen_no_go_path: Path,
    source_cen_no_go_path: Path,
    blk_energy_obstruction_path: Path,
) -> dict[str, Any]:
    """运行 c 依赖 residue 谱输入内核化路由。"""
    completed_weight_spectral_gap = load_json(completed_weight_spectral_gap_path)
    rows = build_rows(
        completed_weight_spectral_gap,
        bwfd_completion_path,
        bsc_fraction_path,
        kfls_square_path,
        cfqk_block_path,
        bd_cen_no_go_path,
        source_cen_no_go_path,
        blk_energy_obstruction_path,
    )
    return {
        "certificate_type": "triad_a1_dibfi_c_dependent_residue_spectral_reduction_router",
        "status": "c_dependent_residue_spectral_input_reduced_to_kfls_ncblk_or_external_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "completed_weight_spectral_gap_json": file_sha256(
                completed_weight_spectral_gap_path
            ),
            "bwfd_completion_md": file_sha256(bwfd_completion_path),
            "bsc_fraction_md": file_sha256(bsc_fraction_path),
            "kfls_square_md": file_sha256(kfls_square_path),
            "cfqk_block_md": file_sha256(cfqk_block_path),
            "bd_cen_no_go_md": file_sha256(bd_cen_no_go_path),
            "source_cen_no_go_md": file_sha256(source_cen_no_go_path),
            "blk_energy_obstruction_md": file_sha256(blk_energy_obstruction_path),
        },
        "previous_terminal_gap": completed_weight_spectral_gap[
            "terminal_gap_after_router"
        ],
        "reduction_rows": rows,
        "closed_reduction_gates": [row["gate"] for row in rows if row["closed"]],
        "open_reduction_gates": [row["gate"] for row in rows if not row["closed"]],
        "c_dependent_residue_spectral_reduction_closed": False,
        "terminal_gap_after_router": "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
        "terminal_gap_expansion": [
            "KFLSCoreInput",
            "NCBLKActualBlockNonConcentration",
            "ExternalDIBFIOrKuznetsovDispersionTheoremMatch",
        ],
        "exact_identity_bridge": [
            "B_{c,x}=sum_{s≡x(c)} beta_s W(s/S)",
            "hat_beta_c(ell)=sum_x B_{c,x} e_c(-ell*x)",
            "sum_x^* B_{c,x} e_c(a_h*x+b_h*bar(x)) = (1/c) sum_ell hat_beta_c(ell) S(a_h+ell,b_h;c)",
        ],
        "blocked_shortcuts": [
            "flat residue mass",
            "pointwise Weil plus L2",
            "ordinary large sieve",
            "APSourceLift",
            "SOURCE-CEN",
            "BD-CEN",
            "raw BLK-energy-core as an arbitrary coefficient-array theorem",
        ],
        "structural_law": (
            "The c-dependent residue object is not a new unrelated obstacle. "
            "It is the residue-space Fourier dual of the BWFD finite completion. "
            "After c=uv, the same object becomes the BSC/KFLS reciprocal-fraction "
            "phase. The remaining self-contained obstruction is therefore not "
            "another completion estimate, but actual same-(u,v) block "
            "non-concentration for the full-S non-AP WFD coefficients, unless a "
            "precisely matched external DI/BFI/Kuznetsov dispersion theorem is used."
        ),
        "review_conclusion": (
            "`CDependentResidueWeightSpectralCancellationInput` 已经接入已有 "
            "`BWFD -> BSC -> KFLS` 内核链：`B_{c,x}` 与 `\\widehat\\beta_c(\\ell)` "
            "由有限 Fourier 反演精确等价。自足版剩余不是新的普通大筛估计，而是 "
            "`NCBLKActualBlockNonConcentrationOrExternalDIBFI`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI c-dependent residue spectral reduction 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 精确桥接恒等式",
        "",
    ]
    for item in result["exact_identity_bridge"]:
        lines.append(f"- `{item}`。")
    lines.extend(
        [
            "",
            "## 2. 结构律",
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
            "## 3. 被排除的捷径",
            "",
        ]
    )
    for item in result["blocked_shortcuts"]:
        lines.append(f"- `{item}`。")
    lines.extend(
        [
            "",
            "## 4. 汇总",
            "",
            f"- `c_dependent_residue_spectral_reduction_closed={fmt_bool(result['c_dependent_residue_spectral_reduction_closed'])}`。",
            f"- `closed_reduction_gates={result['closed_reduction_gates']}`。",
            f"- `open_reduction_gates={result['open_reduction_gates']}`。",
            f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
            "",
            "## 5. 路由账本表",
            "",
            "| gate | closed | evidence | remaining | next target |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["reduction_rows"]:
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
            "## 6. 当前结论",
            "",
            "唯一剩余继续变窄为：",
            "",
            "```text",
            "NCBLKActualBlockNonConcentrationOrExternalDIBFI:",
            "  prove actual same-(u,v) block non-concentration for the full-S",
            "  non-AP WFD coefficients, or provide a precisely matched external",
            "  DI/BFI/Kuznetsov dispersion theorem for the same uncentered object.",
            "```",
            "",
            "这一步没有证明 NC-BLK，也没有把外部定理逐项匹配完成；它关闭的是"
            " `CDependentResidueWeightSpectralCancellationInput` 到既有 KFLS/NC-BLK "
            "核心链之间的缺口。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--completed-weight-spectral-gap-json",
        type=Path,
        default=DEFAULT_COMPLETED_WEIGHT_SPECTRAL_GAP,
    )
    parser.add_argument(
        "--bwfd-completion-md", type=Path, default=DEFAULT_BWFD_COMPLETION
    )
    parser.add_argument("--bsc-fraction-md", type=Path, default=DEFAULT_BSC_FRACTION)
    parser.add_argument("--kfls-square-md", type=Path, default=DEFAULT_KFLS_SQUARE)
    parser.add_argument("--cfqk-block-md", type=Path, default=DEFAULT_CFQK_BLOCK)
    parser.add_argument("--bd-cen-no-go-md", type=Path, default=DEFAULT_BD_CEN_NO_GO)
    parser.add_argument(
        "--source-cen-no-go-md", type=Path, default=DEFAULT_SOURCE_CEN_NO_GO
    )
    parser.add_argument(
        "--blk-energy-obstruction-md",
        type=Path,
        default=DEFAULT_BLK_ENERGY_OBSTRUCTION,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        completed_weight_spectral_gap_path=args.completed_weight_spectral_gap_json,
        bwfd_completion_path=args.bwfd_completion_md,
        bsc_fraction_path=args.bsc_fraction_md,
        kfls_square_path=args.kfls_square_md,
        cfqk_block_path=args.cfqk_block_md,
        bd_cen_no_go_path=args.bd_cen_no_go_md,
        source_cen_no_go_path=args.source_cen_no_go_md,
        blk_energy_obstruction_path=args.blk_energy_obstruction_md,
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
                "terminal_gap_after_router": result["terminal_gap_after_router"],
                "open_reduction_gates": result["open_reduction_gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
