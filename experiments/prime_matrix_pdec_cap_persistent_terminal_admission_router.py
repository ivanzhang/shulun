#!/usr/bin/env python3
"""把持久有限签名 PDEC/ColumnCRT 终端压到 primitive 多原子 PDEC 准入门。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_persistent_terminal_admission_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.json
  docs/monograph/prime-matrix-pdec-cap-persistent-terminal-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SC9_RECONCILIATION = (
    DOCS / "prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.json"
)
DEFAULT_NONTAUTOLOGICAL_AUDIT = (
    DOCS / "prime-matrix-nontautological-pdec-admission-audit.json"
)
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_COLUMNCRT_ABSORB = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_PDEC_DUAL_ABSORB = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_MULTIPLICITY_ABSORB = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.md"


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
    sc9_reconciliation: dict[str, Any],
    nontautological_audit: dict[str, Any],
    terminal_triad_text: str,
    columncrt_text: str,
    pdec_dual_text: str,
    multiplicity_text: str,
) -> list[dict[str, Any]]:
    """生成持久终端准入审查表。"""
    persistent_terminal_is_active = (
        sc9_reconciliation["pdec_cap_sc9_boundary_reconciled"]
        and sc9_reconciliation["narrowest_next_hardpoint"]
        == "PersistentFiniteSignaturePDECColumnCRT"
    )
    pdec_certificate_contract_registered = has_all(
        terminal_triad_text,
        [
            "formal unit Omega",
            "signature group G",
            "bad-window/count function",
            "U_{\\rm CRT}<L_{\\rm PDEC}",
            "PDEC family certificates",
        ],
    )
    columncrt_absorbed = has_all(
        columncrt_text,
        [
            "ColumnCRT-Displacement Absorption",
            "displacement PDEC",
            "formal-unit refinement / primitive quotient",
        ],
    )
    pdec_dual_failure_absorbed = has_all(
        pdec_dual_text,
        [
            "Cap localization",
            "CapPersistent",
            "refined PDEC / ColumnCRT",
            "Cap 细化无循环",
        ],
    )
    multiplicity_absorbed = has_all(
        multiplicity_text,
        [
            "Formal unit 原则",
            "weighted PDEC-Cert",
            "primitive/physical PDEC-Cert",
            "ReuseDefect",
        ],
    )
    current_materialized_candidates_exhausted = (
        nontautological_audit["all_current_routes_blocked_or_absorbed"]
        and nontautological_audit[
            "current_materialized_nontautological_pdec_candidate_count"
        ]
        == 0
    )
    primitive_multiatom_admission_boundary = all(
        [
            persistent_terminal_is_active,
            pdec_certificate_contract_registered,
            columncrt_absorbed,
            pdec_dual_failure_absorbed,
            multiplicity_absorbed,
            current_materialized_candidates_exhausted,
        ]
    )

    return [
        row(
            "PersistentTerminalIsActive",
            persistent_terminal_is_active,
            sc9_reconciliation["narrowest_next_hardpoint"],
            "SC-9 调和后，当前 PDEC-CAP 只剩持久有限签名 PDEC/ColumnCRT 终端。",
            False,
        ),
        row(
            "PDECCertificateContractRegistered",
            pdec_certificate_contract_registered,
            "formal unit / signature group / U_CRT<L_PDEC",
            "任何持久终端必须先提交同 formal unit 的 PDEC 证书字段，而不是裸 Fourier 常数。",
            False,
        ),
        row(
            "ColumnCRTAbsorbedBeforeAdmission",
            columncrt_absorbed,
            "ColumnCRT => displacement PDEC / SAE / primitive quotient",
            "列位移持久不会作为独立终端准入；它先改写为 displacement/primitive PDEC 或 SAE。",
            False,
        ),
        row(
            "PDECDualFailureAbsorbedBeforeAdmission",
            pdec_dual_failure_absorbed,
            "dual failure => cap localization / refined PDEC / ColumnCRT / SAE",
            "对偶失败不是准入对象；它必须先输出 cap 细化、ColumnCRT、SAE 或口径义务。",
            False,
        ),
        row(
            "MultiplicityNormalizedBeforeAdmission",
            multiplicity_absorbed,
            "weighted PDEC / quotient primitive PDEC / reuse defect",
            "多重或拼接口径不一致必须先规范化为同 formal unit，或回流复用缺陷。",
            False,
        ),
        row(
            "CurrentMaterializedPrimitiveCandidatesExhausted",
            current_materialized_candidates_exhausted,
            (
                "count="
                f"{nontautological_audit['current_materialized_nontautological_pdec_candidate_count']}"
            ),
            "当前已物化 primitive 非二点 PDEC 候选为零；二点 tautology 与 SAE/Endpoint 已吸收。",
            False,
        ),
        row(
            "PrimitiveMultiAtomAdmissionBoundaryDerived",
            primitive_multiatom_admission_boundary,
            "same formal unit + >=3 physical primitive atoms + non-tautological + not SAE",
            "未来真正可进入终端的对象只能是 primitive 多原子同集 PDEC 证书。",
            False,
        ),
        row(
            "PrimitiveMultiAtomSameFormalUnitPDECCertificate",
            False,
            "global U_CRT<L_PDEC for every admitted primitive multi-atom formal unit not submitted",
            "剩余全球硬点是证明所有准入后的 primitive 多原子同 formal unit PDEC 满足容量排斥。",
            True,
        ),
    ]


def run(
    sc9_reconciliation_path: Path,
    nontautological_audit_path: Path,
    terminal_triad_path: Path,
    columncrt_absorb_path: Path,
    pdec_dual_absorb_path: Path,
    multiplicity_absorb_path: Path,
) -> dict[str, Any]:
    """运行持久终端准入路由。"""
    sc9_reconciliation = load_json(sc9_reconciliation_path)
    nontautological_audit = load_json(nontautological_audit_path)
    terminal_triad_text = read_text(terminal_triad_path)
    columncrt_text = read_text(columncrt_absorb_path)
    pdec_dual_text = read_text(pdec_dual_absorb_path)
    multiplicity_text = read_text(multiplicity_absorb_path)
    rows = build_rows(
        sc9_reconciliation=sc9_reconciliation,
        nontautological_audit=nontautological_audit,
        terminal_triad_text=terminal_triad_text,
        columncrt_text=columncrt_text,
        pdec_dual_text=pdec_dual_text,
        multiplicity_text=multiplicity_text,
    )
    admission_boundary_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "PrimitiveMultiAtomAdmissionBoundaryDerived"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_persistent_terminal_admission_router",
        "status": "persistent_terminal_reduced_to_primitive_multiatom_pdec_certificate",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "sc9_reconciliation": file_sha256(sc9_reconciliation_path),
            "nontautological_audit": file_sha256(nontautological_audit_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "columncrt_absorb": file_sha256(columncrt_absorb_path),
            "pdec_dual_absorb": file_sha256(pdec_dual_absorb_path),
            "multiplicity_absorb": file_sha256(multiplicity_absorb_path),
        },
        "persistent_terminal_admission_boundary_closed": admission_boundary_closed,
        "current_materialized_persistent_terminal_instances_closed": True,
        "primitive_multiatom_same_formal_unit_pdec_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "PrimitiveMultiAtomSameFormalUnitPDECCertificate",
        "future_admission_requirements": [
            "same formal unit and one fixed phase map",
            "at least three physical primitive atoms after all quotients",
            "not a two-point Fourier tautology",
            "not a ColumnCRT displacement before absorption",
            "not a cap-refinement failure before no-cycle processing",
            "not absorbed by LocalSurvivor/SAE/Endpoint",
        ],
        "rows": rows,
        "admission_law": (
            "PersistentFiniteSignaturePDECColumnCRT is not admitted as a raw label. Before "
            "it can be a terminal certificate, ColumnCRT must be converted into displacement "
            "PDEC or SAE, dual failure must be converted into cap refinement or SAE, and "
            "multiplicity mismatch must be normalized to one formal unit. The current "
            "materialized primitive frontier has no non-tautological candidate. Therefore the "
            "remaining global family is exactly: primitive multi-atom same-formal-unit PDEC "
            "certificates, each requiring U_CRT<L_PDEC on the same bad-window count function."
        ),
        "review_conclusion": (
            "`PersistentFiniteSignaturePDECColumnCRT` 已被压到准入门：不能以裸持久签名、列位移、"
            "对偶失败或多重口径作为终端。当前已物化 primitive 非二点候选为零；未来只有通过"
            "同 formal unit、去重后三点以上、非二点 tautology、未被 SAE/Endpoint 吸收的对象，"
            "才是真正剩余的 `PrimitiveMultiAtomSameFormalUnitPDECCertificate`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 持久终端准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 准入律",
        "",
        result["admission_law"],
        "",
        "```text",
        "PersistentFiniteSignaturePDECColumnCRT",
        "  => normalize formal unit;",
        "  => absorb ColumnCRT as displacement/primitive PDEC or SAE;",
        "  => absorb dual failure as cap refinement / SAE / ColumnCRT;",
        "  => remove multiplicity and two-point tautology;",
        "  => admitted terminal only if primitive multi-atom same-formal-unit PDEC.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `persistent_terminal_admission_boundary_closed={fmt_bool(result['persistent_terminal_admission_boundary_closed'])}`。",
        f"- `current_materialized_persistent_terminal_instances_closed={fmt_bool(result['current_materialized_persistent_terminal_instances_closed'])}`。",
        f"- `primitive_multiatom_same_formal_unit_pdec_closed={fmt_bool(result['primitive_multiatom_same_formal_unit_pdec_closed'])}`。",
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
    lines.extend(["", "## 4. 未来准入要求", ""])
    for item in result["future_admission_requirements"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 5. 剩余",
            "",
            "本路由器关闭的是持久终端的准入边界和当前已物化实例，不关闭全局 PDEC family。"
            "下一步硬点是对所有准入后的 primitive 多原子同 formal unit 证明 "
            "`U_CRT<L_PDEC`，或给出失败时的 cap/SAE/ColumnCRT 回流证书。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sc9-reconciliation-json", type=Path, default=DEFAULT_SC9_RECONCILIATION)
    parser.add_argument(
        "--nontautological-audit-json", type=Path, default=DEFAULT_NONTAUTOLOGICAL_AUDIT
    )
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--columncrt-absorb-md", type=Path, default=DEFAULT_COLUMNCRT_ABSORB)
    parser.add_argument("--pdec-dual-absorb-md", type=Path, default=DEFAULT_PDEC_DUAL_ABSORB)
    parser.add_argument(
        "--multiplicity-absorb-md", type=Path, default=DEFAULT_MULTIPLICITY_ABSORB
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        sc9_reconciliation_path=args.sc9_reconciliation_json,
        nontautological_audit_path=args.nontautological_audit_json,
        terminal_triad_path=args.terminal_triad_md,
        columncrt_absorb_path=args.columncrt_absorb_md,
        pdec_dual_absorb_path=args.pdec_dual_absorb_md,
        multiplicity_absorb_path=args.multiplicity_absorb_md,
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
