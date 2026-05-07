#!/usr/bin/env python3
"""把横向商 clean 大筛原子接入既有 A1 CleanKLS/SC-9 前沿。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_transverse_clean_atom_frontier_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.json
  docs/monograph/prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_TRANSVERSE_CLEAN = (
    DOCS / "prime-matrix-pdec-cap-transverse-clean-reduction-router.json"
)
DEFAULT_A1_CLEAN = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_SC9_FRONTIER = (
    DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json"
)
DEFAULT_NCBLK = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.json"
DEFAULT_EXACT_FACTOR_SUPPORT = (
    DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
)
DEFAULT_FACTOR_INCIDENCE = (
    DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
)
DEFAULT_DIBFI_TRANSFER = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.json"
)
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


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
    """构造审查表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    transverse_clean: dict[str, Any],
    a1_clean: dict[str, Any],
    sc9_frontier: dict[str, Any],
    ncblk: dict[str, Any],
    exact_factor_support: dict[str, Any],
    factor_incidence: dict[str, Any],
    dibfi_transfer: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成横向 clean 原子前沿审查表。"""
    transverse_atom_active = (
        transverse_clean["status"]
        == "transverse_expansion_reduced_to_clean_large_sieve_atom"
        and transverse_clean["transverse_expansion_reduced_to_clean_atom"]
        and transverse_clean["narrowest_next_hardpoint"]
        == "TransverseQuotientCleanLargeSieveAtom"
    )
    a1_clean_admission_available = (
        a1_clean["all_admission_verified_or_routed"]
        and a1_clean["terminal_gap_after_router"]
        == "KuznetsovLSAtomSC9OrExternalCitation"
    )
    transverse_specializes_a1_clean = (
        transverse_atom_active
        and a1_clean_admission_available
        and has_all(
            transverse_clean["clean_reduction_law"],
            ["transverse quotient", "L2-flat", "CleanKLS/DLS"],
        )
        and "L2-flat Kloosterman/dispersion formal unit"
        in a1_clean["structural_law"]
    )
    sc9_frontier_named = (
        sc9_frontier["terminal_gap_after_router"]
        == "NCBLKOrExternalDIBFIOriginalDispersion"
        and sc9_frontier["self_contained_terminal_gap"]
        == "NCBLKActualWFDCoefficientBlockNonConcentration"
        and sc9_frontier["external_terminal_gap"]
        == "ExternalDIBFIOriginalDispersionCitation"
    )
    canonical_boundary_available = (
        ncblk["all_reconciliation_gates_passed"]
        and ncblk["canonical_ncblk_absorbed_by_existing_boundary"]
        and ncblk["generic_ncblk_self_contained_not_claimed"]
        and not ncblk["row_column_unconditional_closed"]
    )
    source_support_not_automatic = (
        exact_factor_support["status"]
        == "exact_factor_support_not_implied_by_k4_k6_without_incidence_bridge"
        and exact_factor_support["next_internal_target"]
        == "FactorResidueIncidenceBridgeOrCanonicalRIWFactorSupport"
    )
    naive_incidences_blocked = (
        factor_incidence["status"]
        == "factor_residue_incidence_bridge_blocked_by_internal_atom_fiber"
        and not factor_incidence["naive_incidence_bridge_valid"]
        and factor_incidence["next_internal_target"]
        == "CanonicalRIWFactorSupportLowerBound"
    )
    dibfi_quantified_open = (
        dibfi_transfer["terminal_gap_after_router"]
        == "DIBFIQuantifiedNoProjectionWindowCertificate"
        and not dibfi_transfer["all_certificate_rows_closed"]
    )
    transverse_atom_routed_to_named_frontier = all(
        [
            transverse_specializes_a1_clean,
            sc9_frontier_named,
            canonical_boundary_available,
            source_support_not_automatic,
            naive_incidences_blocked,
        ]
    )

    return [
        row(
            "TransverseCleanAtomActive",
            transverse_atom_active,
            transverse_clean["narrowest_next_hardpoint"],
            "上一层已把横向纤维扩张压成横向商 L2-flat clean residual。",
            False,
        ),
        row(
            "A1CleanKLSAdmissionAvailable",
            a1_clean_admission_available,
            a1_clean["terminal_gap_after_router"],
            "K1--K9 clean admission 已登记：失败回流 PDEC/SAE/Multiplicity/Promotion，通过才进入 KLS/SC-9。",
            False,
        ),
        row(
            "TransverseAtomSpecializesA1CleanUnit",
            transverse_specializes_a1_clean,
            "transverse quotient L2-flat residual -> Kloosterman/dispersion formal unit",
            "横向商 clean 原子不是第四出口；它是 A1 clean KLS/SC-9 formal unit 的横向特化。",
            False,
        ),
        row(
            "SC9FrontierNamed",
            sc9_frontier_named,
            sc9_frontier["terminal_gap_after_router"],
            "SC-9 已展开成实际系数 NC-BLK 或外部 DI/BFI 原始 dispersion。",
            False,
        ),
        row(
            "CanonicalBoundaryAvailableButNotGenericUpgrade",
            canonical_boundary_available,
            ncblk["canonical_closed_statement"],
            "canonical NC-BLK 可由已闭合边界吸收；generic WFD 不能偷渡为自足证明。",
            False,
        ),
        row(
            "ExactFactorSupportNotAutomatic",
            source_support_not_automatic,
            exact_factor_support["terminal_gap_after_router"],
            "K4/K6 clean 平坦性不能自动推出因子支撑下界；还需源支撑/非集中证书。",
            False,
        ),
        row(
            "NaiveFactorResidueIncidenceBlocked",
            naive_incidences_blocked,
            factor_incidence["terminal_gap_after_router"],
            "单个 moving factor-pair 内有增长的内部 fiber，朴素 incidence 桥不能闭合自足版。",
            False,
        ),
        row(
            "TransverseCleanAtomRoutedToNamedFrontier",
            transverse_atom_routed_to_named_frontier,
            "A1 CleanKLS/SC-9 + NC-BLK boundary + source-support obstruction",
            "横向 clean 大筛原子已接入既有前沿；剩余不再是宽泛 LargeSieve 标签。",
            False,
        ),
        row(
            "TransverseSourceSupportNonconcentrationCertificate",
            False,
            "canonical RIW/Buchstab support lower bound or actual transverse NC-BLK not submitted",
            "完全自足路线还需证明横向商系数具有 canonical 源支撑下界，或直接证明实际块非集中。",
            True,
        ),
        row(
            "DIBFIQuantifiedNoProjectionWindowCertificate",
            not dibfi_quantified_open,
            dibfi_transfer["terminal_gap_after_router"],
            "外部原始 DI/BFI 路线还需无投影对象恒等式与量化尺度代入；直接接受窗口化 KLS 外部定理则属于外部输入版。",
            dibfi_quantified_open,
        ),
    ]


def run(
    transverse_clean_path: Path,
    a1_clean_path: Path,
    sc9_frontier_path: Path,
    ncblk_path: Path,
    exact_factor_support_path: Path,
    factor_incidence_path: Path,
    dibfi_transfer_path: Path,
) -> dict[str, Any]:
    """运行横向 clean 原子前沿路由。"""
    transverse_clean = load_json(transverse_clean_path)
    a1_clean = load_json(a1_clean_path)
    sc9_frontier = load_json(sc9_frontier_path)
    ncblk = load_json(ncblk_path)
    exact_factor_support = load_json(exact_factor_support_path)
    factor_incidence = load_json(factor_incidence_path)
    dibfi_transfer = load_json(dibfi_transfer_path)
    rows = build_rows(
        transverse_clean=transverse_clean,
        a1_clean=a1_clean,
        sc9_frontier=sc9_frontier,
        ncblk=ncblk,
        exact_factor_support=exact_factor_support,
        factor_incidence=factor_incidence,
        dibfi_transfer=dibfi_transfer,
    )
    routed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "TransverseCleanAtomRoutedToNamedFrontier"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_transverse_clean_atom_frontier_router",
        "status": "transverse_clean_atom_routed_to_source_support_or_external_dibfi_frontier",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "transverse_clean": file_sha256(transverse_clean_path),
            "a1_clean": file_sha256(a1_clean_path),
            "sc9_frontier": file_sha256(sc9_frontier_path),
            "ncblk_boundary": file_sha256(ncblk_path),
            "exact_factor_support": file_sha256(exact_factor_support_path),
            "factor_incidence": file_sha256(factor_incidence_path),
            "dibfi_transfer": file_sha256(dibfi_transfer_path),
        },
        "transverse_clean_atom_routed_to_named_frontier": routed,
        "transverse_quotient_clean_large_sieve_closed": False,
        "row_column_unconditional_closed": False,
        "external_windowed_kls_version_closed_if_accepted": bool(
            a1_clean["external_kls_input_registered"]
        ),
        "open_final_gates": open_final_gates,
        "narrowest_self_contained_hardpoint": (
            "TransverseSourceSupportNonconcentrationCertificate"
        ),
        "narrowest_external_hardpoint": (
            "DIBFIQuantifiedNoProjectionWindowCertificate"
        ),
        "narrowest_next_hardpoint": (
            "TransverseSourceSupportNonconcentrationCertificate_OR_"
            "DIBFIQuantifiedNoProjectionWindowCertificate"
        ),
        "rows": rows,
        "frontier_law": (
            "The transverse quotient clean large-sieve atom is not a fourth terminal. "
            "Once transverse sparse support, persistent transverse bias, and shell/column "
            "concentration have been removed, the residual satisfies the same K1--K9 clean "
            "admission grammar as the A1 CleanKLS branch. Hence it routes to the SC-9 "
            "frontier: self-contained actual-coefficient NC-BLK or external DI/BFI. The "
            "canonical NC-BLK branch is already absorbed only when canonical RIW/Buchstab "
            "source support is proved. K4/K6 flatness alone does not imply that support, "
            "and the naive factor-residue incidence bridge is blocked by the internal "
            "fiber obstruction. Therefore the self-contained next certificate is a "
            "transverse source-support/nonconcentration certificate. The external original "
            "DI/BFI route remains the quantified no-projection window certificate."
        ),
        "review_conclusion": (
            "`TransverseQuotientCleanLargeSieveAtom` 已被拆成可审查前沿：它接入 A1 "
            "CleanKLS/SC-9，不再是无名大筛黑箱。自足路线不能直接调用 canonical 吸收，"
            "因为横向商系数的 canonical RIW/Buchstab 源支撑或实际 NC-BLK 非集中尚未证明；"
            "朴素 factor-residue incidence 桥已被内部 fiber 反例阻断。外部 DI/BFI 路线则压到 "
            "`DIBFIQuantifiedNoProjectionWindowCertificate`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 横向 clean 原子前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 前沿律",
        "",
        result["frontier_law"],
        "",
        "```text",
        "TransverseQuotientCleanLargeSieveAtom",
        "  => A1 K1--K9 clean admission;",
        "admission failure",
        "  => PDEC / SAE / ColumnCRT / Multiplicity;",
        "admission success",
        "  => SC-9 frontier;",
        "SC-9",
        "  => actual-coefficient NC-BLK or external DI/BFI;",
        "self-contained route",
        "  => TransverseSourceSupportNonconcentrationCertificate;",
        "external original DI/BFI route",
        "  => DIBFIQuantifiedNoProjectionWindowCertificate.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `transverse_clean_atom_routed_to_named_frontier={fmt_bool(result['transverse_clean_atom_routed_to_named_frontier'])}`。",
        f"- `transverse_quotient_clean_large_sieve_closed={fmt_bool(result['transverse_quotient_clean_large_sieve_closed'])}`。",
        f"- `external_windowed_kls_version_closed_if_accepted={fmt_bool(result['external_windowed_kls_version_closed_if_accepted'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_self_contained_hardpoint={result['narrowest_self_contained_hardpoint']}`。",
        f"- `narrowest_external_hardpoint={result['narrowest_external_hardpoint']}`。",
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
            "## 4. 下一步",
            "",
            "自足路线直接攻 `TransverseSourceSupportNonconcentrationCertificate`：证明横向商系数继承 canonical RIW/Buchstab 源支撑下界，或直接证明实际 transverse NC-BLK 块非集中。外部路线则只能在明确接受窗口化 KLS 定理，或闭合 `DIBFIQuantifiedNoProjectionWindowCertificate` 后使用。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--transverse-clean-json", type=Path, default=DEFAULT_TRANSVERSE_CLEAN
    )
    parser.add_argument("--a1-clean-json", type=Path, default=DEFAULT_A1_CLEAN)
    parser.add_argument("--sc9-frontier-json", type=Path, default=DEFAULT_SC9_FRONTIER)
    parser.add_argument("--ncblk-json", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument(
        "--exact-factor-support-json",
        type=Path,
        default=DEFAULT_EXACT_FACTOR_SUPPORT,
    )
    parser.add_argument(
        "--factor-incidence-json", type=Path, default=DEFAULT_FACTOR_INCIDENCE
    )
    parser.add_argument("--dibfi-transfer-json", type=Path, default=DEFAULT_DIBFI_TRANSFER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        transverse_clean_path=args.transverse_clean_json,
        a1_clean_path=args.a1_clean_json,
        sc9_frontier_path=args.sc9_frontier_json,
        ncblk_path=args.ncblk_json,
        exact_factor_support_path=args.exact_factor_support_json,
        factor_incidence_path=args.factor_incidence_json,
        dibfi_transfer_path=args.dibfi_transfer_json,
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
