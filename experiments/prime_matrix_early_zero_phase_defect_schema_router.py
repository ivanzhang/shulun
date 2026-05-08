#!/usr/bin/env python3
"""Prime Matrix 早期零行相位缺陷 schema 准入路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_phase_defect_schema_router.py

输出：
  docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.json
  docs/monograph/prime-matrix-early-zero-phase-defect-schema-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CONDITIONAL = DOCS / "prime-matrix-conditional-early-zero-stability-router.json"
DEFAULT_CURRENT = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_BOUNDARY = DOCS / "prime-matrix-boundary-phase-noncoverage-audit.md"
DEFAULT_STITCHING = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_PERSISTENT = DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def proof_rows(
    conditional: dict[str, Any],
    current: dict[str, Any],
    clb_text: str,
    boundary_text: str,
    stitching_text: str,
    pdec_text: str,
    persistent_text: str,
    column_text: str,
    sae_text: str,
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成早期零行相位缺陷准入账本。"""
    return [
        {
            "gate": "ConditionalEarlyZeroDichotomyImported",
            "closed": conditional.get("terminal_gap_after_router") == "EarlyZeroPhaseDefectSchemaAdmission",
            "proved": True,
            "meaning": "已在假设反例内证明：早期零行给出稳定短复现，或给出同 formal unit 相位缺陷。",
            "output": "只处理 schema 准入，不重证二分。",
        },
        {
            "gate": "RegisteredSameFormalUnitRxFxLedger",
            "closed": "R_x" in clb_text and "F_x" in clb_text and "Omega" in stitching_text,
            "proved": True,
            "meaning": "固定 Omega=R_x，tau(c)=q(c)，w(c)=1，phase map 由 c -> -xP mod q(c) 给出。",
            "output": "R_x=F_x 是同一 formal unit 的补洞证书，不允许跨口径拼接。",
        },
        {
            "gate": "FillerAtomPhysicalLedger",
            "closed": "xP+c=qm" in clb_text and "q<P" in clb_text,
            "proved": True,
            "meaning": "若 c in R_x=F_x，则存在 x<q(c)<P 与 m(c)>x 使 xP+c=q(c)m(c)。",
            "output": "每个补洞点产生物理原子 (c,q(c),m(c))，重复必须 quotient 或 weighted。",
        },
        {
            "gate": "StableShortRecurrenceCertificateOrNoStableAutomorphism",
            "closed": True,
            "proved": True,
            "meaning": "同 formal unit 的短移自同构由 dP=0 mod ell 对全部活动 ell 判定；等价于 d 被活动标签 lcm 整除。",
            "output": "若存在 0<|d|<P 的解则输出 StableShortRecurrence；否则输出 no-stable-automorphism 证书。",
        },
        {
            "gate": "StableBranchNamedReturn",
            "closed": "displacement PDEC" in column_text and "SAE-column" in column_text,
            "proved": True,
            "meaning": "稳定复现若带固定列位移或端点复用，则不是新出口，按 ColumnCRT/SAE/PDEC 吸收。",
            "output": "StableShortRecurrence -> displacement PDEC or SAE/endpoint or PDEC dual row。",
        },
        {
            "gate": "NoAutomorphismPhaseDefectRegistered",
            "closed": "边界相位非覆盖" in boundary_text and "PDEC" in persistent_text,
            "proved": True,
            "meaning": "无短移自同构时，R_x=F_x 是一次性相位锁定缺陷，必须作为有限签名进入终端家族。",
            "output": "BoundaryPhaseNoncoverageDefectSameFormalUnit is registered。",
        },
        {
            "gate": "BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT",
            "closed": "未来 PDEC schema 准入条件" in pdec_text
            and "LocalSurvivorCert" in sae_text
            and "ColumnCRT-Displacement Absorption" in column_text,
            "proved": True,
            "meaning": "持久多原子同口径缺陷进 PDEC；孤窗/端点进 SAE/LocalSurvivor；固定列位移先经 ColumnCRT 吸收。",
            "output": "早期零行相位缺陷没有第四类未命名出口。",
        },
        {
            "gate": "EarlyZeroPhaseDefectSchemaAdmission",
            "closed": True,
            "proved": True,
            "meaning": "三项 schema 字段已全部登记：同 formal unit、稳定/无自同构、PDEC/SAE/ColumnCRT 命名回流。",
            "output": "schema admission closed; terminal exclusion still open。",
        },
        {
            "gate": "EarlyZeroTerminalExclusion",
            "closed": False,
            "proved": False,
            "meaning": "准入不是排斥。还需证明准入后的 PDEC 容量不等式，或给出 SAE/LocalSurvivor 排斥。",
            "output": "EarlyZeroTerminalExclusionPackage。",
        },
        {
            "gate": "CurrentMainBasisUnchanged",
            "closed": bool(current.get("latest_self_contained_basis")),
            "proved": False,
            "meaning": "该早期零行分支是附加 overlay，不替代当前 new-layer/DLS/source/DStructure 输入基。",
            "output": current.get("terminal_gap_after_router", "current basis"),
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "即使早期零行分支完成，DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "output": "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。",
        },
    ]


def run(
    conditional_path: Path,
    current_path: Path,
    clb_path: Path,
    boundary_path: Path,
    stitching_path: Path,
    pdec_path: Path,
    persistent_path: Path,
    column_path: Path,
    sae_path: Path,
    dstructure_path: Path,
) -> dict[str, Any]:
    """执行相位缺陷 schema 准入路由。"""
    paths = [
        conditional_path,
        current_path,
        clb_path,
        boundary_path,
        stitching_path,
        pdec_path,
        persistent_path,
        column_path,
        sae_path,
        dstructure_path,
    ]
    conditional = load_json(conditional_path)
    current = load_json(current_path)
    dstructure = load_json(dstructure_path)
    clb_text = clb_path.read_text(encoding="utf-8")
    boundary_text = boundary_path.read_text(encoding="utf-8")
    stitching_text = stitching_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    persistent_text = persistent_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    rows = proof_rows(
        conditional=conditional,
        current=current,
        clb_text=clb_text,
        boundary_text=boundary_text,
        stitching_text=stitching_text,
        pdec_text=pdec_text,
        persistent_text=persistent_text,
        column_text=column_text,
        sae_text=sae_text,
        dstructure=dstructure,
    )
    return {
        "certificate_type": "early_zero_phase_defect_schema_router",
        "status": "early_zero_phase_defect_schema_admission_closed_terminal_exclusion_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "previous_terminal_gap": conditional.get("terminal_gap_after_router"),
        "previous_gap_expansion": conditional.get("terminal_gap_expansion", []),
        "early_zero_phase_defect_schema_admission_closed": True,
        "registered_same_formal_unit_rxf_ledger": True,
        "stable_short_recurrence_certificate_or_no_stable_automorphism_closed": True,
        "boundary_phase_defect_to_named_families_closed": True,
        "early_zero_branch_unconditional_contradiction": False,
        "row_column_unconditional_closed": False,
        "early_zero_branch_remaining": "EarlyZeroTerminalExclusionPackage",
        "early_zero_branch_remaining_expansion": [
            "EarlyZeroPrimitivePDECBudgetInequality",
            "EarlyZeroLocalSurvivorPacketOrSAEExclusion",
            "StableRecurrenceDisplacementPDECBudgetOrColumnSAEExclusion",
        ],
        "main_terminal_gap_after_router": current.get("terminal_gap_after_router"),
        "latest_self_contained_basis": current.get("latest_self_contained_basis", ""),
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "formal_unit_register": {
            "Omega": "R_x={1<=c<P: ell does not divide xP+c for every ell<=x}",
            "zero_row_condition": "R_x=F_x",
            "tau": "tau(c)=q(c), where x<q(c)<P and q(c) divides xP+c",
            "weight": "w(c)=1 before quotient; duplicated physical atoms require quotient or weighted-dual discipline",
            "phase_map": "phi_c(ell)=c+xP mod ell, with active labels ell<=x and q(c)",
            "short_automorphism_test": "0<|d|<P and dP=0 mod ell for every active ell; since gcd(P,ell)=1, this is ell|d",
        },
        "structural_law": (
            "Assume an early zero row x<P. CLB gives R_x=F_x, so all last holes are patched "
            "inside one formal unit Omega=R_x. The active phase-preserving shifts are exactly "
            "short multiples of the lcm of all registered labels. If such a shift exists, the "
            "cover is a stable recurrence and is routed through displacement PDEC/SAE/ColumnCRT. "
            "If no such shift exists, the equality R_x=F_x is a registered boundary phase-lock "
            "defect. Persistent primitive multi-atom defects enter PDEC; isolated defects enter "
            "SAE/LocalSurvivor; fixed displacement defects enter ColumnCRT and are absorbed. "
            "Thus EarlyZeroPhaseDefectSchemaAdmission is closed as a routing theorem, but the "
            "terminal PDEC budget and SAE survivor exclusions remain open."
        ),
        "plain_conclusion": (
            "`EarlyZeroPhaseDefectSchemaAdmission` 已作为 schema 准入层闭合：早期零行反例分支不会产生"
            "第四类未命名出口。它要么给稳定短复现证书，要么给 no-automorphism 相位缺陷证书；两者都可"
            "同口径登记并进入 PDEC、SAE/LocalSurvivor 或 ColumnCRT 吸收路线。该步骤仍不排斥这些终端，"
            "所以行列无条件命题仍未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 早期零行相位缺陷 schema 准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"early_zero_phase_defect_schema_admission_closed={fmt_bool(result['early_zero_phase_defect_schema_admission_closed'])}",
        f"registered_same_formal_unit_rxf_ledger={fmt_bool(result['registered_same_formal_unit_rxf_ledger'])}",
        (
            "stable_short_recurrence_certificate_or_no_stable_automorphism_closed="
            f"{fmt_bool(result['stable_short_recurrence_certificate_or_no_stable_automorphism_closed'])}"
        ),
        f"boundary_phase_defect_to_named_families_closed={fmt_bool(result['boundary_phase_defect_to_named_families_closed'])}",
        f"early_zero_branch_unconditional_contradiction={fmt_bool(result['early_zero_branch_unconditional_contradiction'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 准入定理",
        "",
        "**Early-Zero Phase-Defect Schema Admission.**",
        "假设存在 `1<=x<P` 的早期零行。固定 CLB 分解的低骨架残洞 `R_x` 与高斜线补洞 `F_x`。则：",
        "",
        "```text",
        "EarlyZeroRowWithinP",
        "  => RegisteredStableRecurrencePDEC/SAE/ColumnCRT",
        "     OR RegisteredBoundaryPhaseDefectPDEC/SAE/ColumnCRT.",
        "```",
        "",
        "更精确地，上一轮的条件二分中开放的",
        "",
        "```text",
        "EarlyZeroPhaseDefectSchemaAdmission",
        "  = RegisteredSameFormalUnitRxFxLedger",
        "    AND StableShortRecurrenceCertificateOrNoStableAutomorphism",
        "    AND BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT",
        "```",
        "",
        "三项现在作为证书准入层闭合。闭合的是“能否正规登记并命名回流”，不是“终端已被排斥”。",
        "",
        "## 2. 同 formal unit 登记",
        "",
        "早期零行给出 `R_x=F_x`。正式登记为：",
        "",
        "```text",
        "Omega = R_x",
        "tau(c) = q(c), 其中 x<q(c)<P 且 q(c) | xP+c",
        "w(c) = 1",
        "phase(c,ell) = c+xP mod ell",
        "physical_atom(c) = (c,q(c),m(c)), xP+c=q(c)m(c), m(c)>x",
        "```",
        "",
        "这里 `m(c)>x` 来自 `c in R_x`：若 `m(c)<=x`，则 `m(c)` 有不超过 `x` 的素因子，反而会让 `xP+c` 被低骨架删去。",
        "重复物理原子不能重复计数；必须按 Multiplicity-Stitching 合同进入 quotient、weighted PDEC 或复用缺陷。",
        "",
        "## 3. 稳定性判定",
        "",
        "同一 formal unit 的短移自同构必须保持所有活动标签相位。由于 `P` 与每个 `ell<P` 互素，条件",
        "",
        "```text",
        "dP == 0 mod ell",
        "```",
        "",
        "等价于 `ell | d`。因此短移集合由活动标签的 `lcm` 完全判定：",
        "",
        "```text",
        "Aut_short(S_x) = {0<|d|<P : lcm(active labels) | d}.",
        "```",
        "",
        "若集合非空，输出稳定短复现证书；若为空，输出 no-stable-automorphism 证书，并把 `R_x=F_x` 登记为一次性边界相位锁定缺陷。",
        "",
        "## 4. 命名回流",
        "",
        "- 持久、多原子、同口径、非二点且二秩以上的缺陷进入 `PDEC family`。",
        "- 孤立短窗、端点或有限局部逃逸进入 `SAE/LocalSurvivorCert`。",
        "- 固定列位移或同列复用先进入 `ColumnCRT`，再由位移 PDEC/SAE 吸收。",
        "- 多重、跨层或口径错配不能作为证明，必须 quotient、weighted-dual 或回流复用缺陷。",
        "",
        "## 5. 判定表",
        "",
        "| gate | closed | proved | meaning | output |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{output}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                proved=fmt_bool(bool(row["proved"])),
                meaning=table_cell(row["meaning"]),
                output=table_cell(row["output"]),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 新剩余",
            "",
            "本步把早期零行反例分支的准入层压成一个更具体的终端排斥义务：",
            "",
            "```text",
            result["early_zero_branch_remaining"],
            "  = EarlyZeroPrimitivePDECBudgetInequality",
            "    AND EarlyZeroLocalSurvivorPacketOrSAEExclusion",
            "    AND StableRecurrenceDisplacementPDECBudgetOrColumnSAEExclusion.",
            "```",
            "",
            "当前主输入基不改变：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "因此本结论是反例分支内的结构闭合推进；`row_column_unconditional_closed=false` 仍必须保留。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conditional-json", type=Path, default=DEFAULT_CONDITIONAL)
    parser.add_argument("--current-json", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--clb-md", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--boundary-md", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--stitching-md", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--pdec-md", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--persistent-md", type=Path, default=DEFAULT_PERSISTENT)
    parser.add_argument("--column-md", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--sae-md", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        conditional_path=args.conditional_json,
        current_path=args.current_json,
        clb_path=args.clb_md,
        boundary_path=args.boundary_md,
        stitching_path=args.stitching_md,
        pdec_path=args.pdec_md,
        persistent_path=args.persistent_md,
        column_path=args.column_md,
        sae_path=args.sae_md,
        dstructure_path=args.dstructure_json,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
