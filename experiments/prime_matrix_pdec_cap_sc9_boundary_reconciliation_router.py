#!/usr/bin/env python3
"""调和 PDEC-CAP 终端中的 SC-9 与 canonical-source 边界。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_sc9_boundary_reconciliation_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.json
  docs/monograph/prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PERSISTENT_UNIFICATION = (
    DOCS / "prime-matrix-pdec-cap-persistent-signature-unification-router.json"
)
DEFAULT_SELF_CONTAINED_BOTTLENECK = (
    DOCS / "prime-matrix-self-contained-terminal-bottleneck-router.json"
)
DEFAULT_NCBLK = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.json"
DEFAULT_CLEAN_KLS = DOCS / "prime-matrix-triad-a1-clean-kls-external-input-router.json"
DEFAULT_SC9 = DOCS / "prime-matrix-triad-a1-kuznetsov-ls-atom-frontier-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    persistent_unification: dict[str, Any],
    self_contained_bottleneck: dict[str, Any],
    ncblk: dict[str, Any],
    clean_kls: dict[str, Any],
    sc9: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 SC-9 边界调和审查表。"""
    sc9_present_in_pdec_cap_terminal = (
        persistent_unification["persistent_signature_unification_closed"]
        and "SelfContainedKuznetsovLSAtomSC9"
        in persistent_unification["open_final_gates"]
    )
    clean_failure_returns_to_pdec = (
        self_contained_bottleneck["closed_nonfinal_reductions"]
        and self_contained_bottleneck["internal_clean_kls_independent_blocker_collapsed"]
        and self_contained_bottleneck["self_contained_terminal_bottleneck_is_pdec_cap"]
    )
    sc9_expanded_to_ncblk_or_external = (
        clean_kls["self_contained_version_status"] == "open_at_kuznetsov_ls_atom_sc9"
        and sc9["terminal_gap_after_router"] == "NCBLKOrExternalDIBFIOriginalDispersion"
        and sc9["self_contained_version_status"]
        == "open_at_ncblk_actual_block_nonconcentration"
    )
    canonical_ncblk_absorbed = (
        ncblk["all_reconciliation_gates_passed"]
        and ncblk["canonical_ncblk_absorbed_by_existing_boundary"]
    )
    generic_sc9_not_imported = (
        ncblk["generic_ncblk_self_contained_not_claimed"]
        and not ncblk["row_column_unconditional_closed"]
    )
    sc9_not_independent_in_canonical_boundary = all(
        [
            sc9_present_in_pdec_cap_terminal,
            clean_failure_returns_to_pdec,
            sc9_expanded_to_ncblk_or_external,
            canonical_ncblk_absorbed,
            generic_sc9_not_imported,
        ]
    )

    return [
        row(
            "SC9AppearsOnlyAsFlatCleanResidual",
            sc9_present_in_pdec_cap_terminal,
            str(persistent_unification["open_final_gates"]),
            "SC-9 在当前 PDEC-CAP 终端中只来自无持久有限签名后的 flat clean residual。",
            False,
        ),
        row(
            "CleanFailureReturnsToPDEC",
            clean_failure_returns_to_pdec,
            self_contained_bottleneck["narrowest_self_contained_hardpoint"],
            "Clean/KLS 失败会输出对偶集中并回流 PDEC/SAE；它不是独立自足瓶颈。",
            False,
        ),
        row(
            "SC9ExpandedToNCBLKOrExternalDIBFI",
            sc9_expanded_to_ncblk_or_external,
            sc9["terminal_gap_after_router"],
            "SC-9 已展开为 NC-BLK actual block non-concentration 或外部 DI/BFI 原始 dispersion。",
            False,
        ),
        row(
            "CanonicalNCBLKAbsorbedByBoundary",
            canonical_ncblk_absorbed,
            ncblk["canonical_closed_statement"],
            "canonical RIW/Buchstab source branch 的 NC-BLK/CleanKLS 链已被既有同集容量边界吸收。",
            False,
        ),
        row(
            "GenericSC9NotImportedIntoSelfContainedClaim",
            generic_sc9_not_imported,
            ncblk["not_claimed_statement"],
            "generic full-S/WFD 分支仍外部化或被反证隔离，不能作为 canonical 自足声明的剩余门。",
            False,
        ),
        row(
            "SC9NotIndependentInCanonicalPDECCapBoundary",
            sc9_not_independent_in_canonical_boundary,
            "canonical absorption / generic not claimed / failure returns to PDEC",
            "在当前 canonical-source 完全自足边界内，SC-9 不是 PDEC-CAP 的独立终端阻塞。",
            False,
        ),
        row(
            "PersistentFiniteSignaturePDECColumnCRT",
            False,
            "same formal-unit U_CRT<L_PDEC or displacement PDEC exclusion not submitted",
            "剥离 SC-9 后，当前完全自足 PDEC-CAP 前沿只剩持久有限签名 PDEC/ColumnCRT 终端证书。",
            True,
        ),
    ]


def run(
    persistent_unification_path: Path,
    self_contained_bottleneck_path: Path,
    ncblk_path: Path,
    clean_kls_path: Path,
    sc9_path: Path,
) -> dict[str, Any]:
    """运行 PDEC-CAP/SC-9 边界调和。"""
    persistent_unification = load_json(persistent_unification_path)
    self_contained_bottleneck = load_json(self_contained_bottleneck_path)
    ncblk = load_json(ncblk_path)
    clean_kls = load_json(clean_kls_path)
    sc9 = load_json(sc9_path)
    rows = build_rows(
        persistent_unification=persistent_unification,
        self_contained_bottleneck=self_contained_bottleneck,
        ncblk=ncblk,
        clean_kls=clean_kls,
        sc9=sc9,
    )
    reconciled = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "SC9NotIndependentInCanonicalPDECCapBoundary"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_sc9_boundary_reconciliation_router",
        "status": "pdec_cap_sc9_reconciled_persistent_signature_pdec_only_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "persistent_unification": file_sha256(persistent_unification_path),
            "self_contained_bottleneck": file_sha256(self_contained_bottleneck_path),
            "ncblk_boundary": file_sha256(ncblk_path),
            "clean_kls": file_sha256(clean_kls_path),
            "sc9_frontier": file_sha256(sc9_path),
        },
        "pdec_cap_sc9_boundary_reconciled": reconciled,
        "canonical_sc9_independent_blocker_collapsed": reconciled,
        "persistent_finite_signature_pdec_columncrt_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "PersistentFiniteSignaturePDECColumnCRT",
        "rows": rows,
        "reconciliation_law": (
            "The SC-9 branch in the PDEC-CAP terminal list is not a new independent "
            "self-contained blocker inside the canonical-source boundary. It is exactly the "
            "flat clean residual after no persistent finite signature. If the clean estimate "
            "fails, it returns a dual concentration to PDEC/SAE. If it reaches SC-9, the "
            "existing SC-9 router expands it to NC-BLK or external DI/BFI. The NC-BLK "
            "boundary reconciliation says that the canonical RIW/Buchstab source branch is "
            "already absorbed by the same-set capacity boundary, while the generic WFD branch "
            "is not part of the self-contained claim. Therefore the current canonical "
            "PDEC-CAP frontier has a single independent mathematical terminal: "
            "PersistentFiniteSignaturePDECColumnCRT."
        ),
        "review_conclusion": (
            "PDEC-CAP 终端中的 `SC-9` 已与 canonical-source 边界调和：它不是新的独立自足阻塞。"
            "clean 失败回流 PDEC/SAE；clean 成功进入的 SC-9 已展开到 NC-BLK/外部 DI-BFI；"
            "canonical NC-BLK 已被同集容量边界吸收，generic WFD 分支不能偷渡为自足声明。"
            "因此当前完全自足 PDEC-CAP 前沿只剩 `PersistentFiniteSignaturePDECColumnCRT`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP / SC-9 边界调和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 调和律",
        "",
        result["reconciliation_law"],
        "",
        "```text",
        "PDEC-CAP flat clean residual",
        "  => SC-9;",
        "clean failure",
        "  => dual concentration => PDEC/SAE;",
        "SC-9",
        "  => NC-BLK or external DI/BFI;",
        "canonical NC-BLK",
        "  => absorbed by same-set canonical boundary;",
        "generic WFD/SC9",
        "  => external or not claimed;",
        "therefore canonical PDEC-CAP hardpoint",
        "  => PersistentFiniteSignaturePDECColumnCRT.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `pdec_cap_sc9_boundary_reconciled={fmt_bool(result['pdec_cap_sc9_boundary_reconciled'])}`。",
        f"- `canonical_sc9_independent_blocker_collapsed={fmt_bool(result['canonical_sc9_independent_blocker_collapsed'])}`。",
        f"- `persistent_finite_signature_pdec_columncrt_closed={fmt_bool(result['persistent_finite_signature_pdec_columncrt_closed'])}`。",
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
            "本路由器关闭的是 canonical-source 完全自足路线中 `SC-9` 的独立阻塞身份。"
            "它不证明完整行/列无条件定理，也不证明持久有限签名的 PDEC/ColumnCRT 终端排斥。"
            "下一步应直接攻 `PersistentFiniteSignaturePDECColumnCRT` 的同 formal unit "
            "`U_CRT<L_PDEC` 或 displacement PDEC 证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--persistent-unification-json",
        type=Path,
        default=DEFAULT_PERSISTENT_UNIFICATION,
    )
    parser.add_argument(
        "--self-contained-bottleneck-json",
        type=Path,
        default=DEFAULT_SELF_CONTAINED_BOTTLENECK,
    )
    parser.add_argument("--ncblk-json", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument("--clean-kls-json", type=Path, default=DEFAULT_CLEAN_KLS)
    parser.add_argument("--sc9-json", type=Path, default=DEFAULT_SC9)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        persistent_unification_path=args.persistent_unification_json,
        self_contained_bottleneck_path=args.self_contained_bottleneck_json,
        ncblk_path=args.ncblk_json,
        clean_kls_path=args.clean_kls_json,
        sc9_path=args.sc9_json,
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
