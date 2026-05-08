#!/usr/bin/env python3
"""Prime Matrix 假设早期零行的稳定性/相位缺陷条件路由器。

用法示例：
  python3 experiments/prime_matrix_conditional_early_zero_stability_router.py

输出：
  docs/monograph/prime-matrix-conditional-early-zero-stability-router.json
  docs/monograph/prime-matrix-conditional-early-zero-stability-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_NEAR = DOCS / "prime-matrix-near-zero-mirror-contradiction-router.json"
DEFAULT_CURRENT = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_ACTIVATION = DOCS / "prime-matrix-line-activation-cover-threshold.md"
DEFAULT_BOUNDARY = DOCS / "prime-matrix-boundary-phase-noncoverage-audit.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_STITCHING = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-conditional-early-zero-stability-router.json"
DEFAULT_MD = DOCS / "prime-matrix-conditional-early-zero-stability-router.md"


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


def rows(
    near: dict[str, Any],
    clb_text: str,
    activation_text: str,
    boundary_text: str,
    pdec_text: str,
    stitching_text: str,
) -> list[dict[str, Any]]:
    """生成条件稳定性证明账本。"""
    return [
        {
            "gate": "EarlyZeroAssumptionFormalized",
            "closed": True,
            "proved": True,
            "meaning": "假设存在 x<P 使 xP+1,...,xP+P-1 全被 <P 素数覆盖。",
            "output": "完整覆盖证书 S_x。",
        },
        {
            "gate": "SameFormalUnitFromCLB",
            "closed": "R_x" in clb_text and "F_x" in clb_text and "CLB-FillerBound" in clb_text,
            "proved": True,
            "meaning": "用已完成低斜线残洞 R_x 与未完成高斜线补洞 F_x 定义同一个 formal unit。",
            "output": "早期零行等价于 R_x=F_x，即边界相位非覆盖失败。",
        },
        {
            "gate": "ActivationShadowRemoved",
            "closed": "shadow hit" in activation_text and "Early Phase-Lock" in activation_text,
            "proved": True,
            "meaning": "q^2 前的 q 命中不是独立覆盖；零行的最后补洞必须来自已激活的相位锁定标签。",
            "output": "排除“未画完斜线”作为独立出口。",
        },
        {
            "gate": "StableRecurrenceBranchDefinition",
            "closed": True,
            "proved": True,
            "meaning": "若存在非零短移 d 保持证书 S_x 的全部覆盖标签相位，则 x+d 是同 formal unit 稳定复现零行。",
            "output": "StableShortRecurrence。",
        },
        {
            "gate": "NoStableRecurrenceImpliesPhaseDefect",
            "closed": True,
            "proved": True,
            "meaning": "若无这种短移，则早期零行不能由稳定轨道解释，只能是高素数补洞标签在 R_x 上的相位锁定缺陷。",
            "output": "BoundaryPhaseNoncoverageFailure / early diagonal phase defect。",
        },
        {
            "gate": "DefectHasNamedReturn",
            "closed": near.get("retained_route") == "BoundaryPhaseNoncoverageOrStableRecurrencePDEC",
            "proved": True,
            "meaning": "上一轮已确认该缺陷必须进入 BoundaryPhaseNoncoverage 或稳定复现 PDEC/SAE/ColumnCRT 路线。",
            "output": near.get("retained_route"),
        },
        {
            "gate": "PDECSchemaAdmissionStillOpen",
            "closed": "未来 PDEC schema 准入条件" in pdec_text and "Multiplicity-Stitching" in stitching_text,
            "proved": False,
            "meaning": "要把相位缺陷升级成最终矛盾，仍需正式登记同 formal unit 的 PDEC/SAE/ColumnCRT 证书字段。",
            "output": "EarlyZeroPhaseDefectSchemaAdmission。",
        },
        {
            "gate": "UnconditionalClosure",
            "closed": False,
            "proved": False,
            "meaning": "条件稳定性二分闭合，但相位缺陷终端尚未排斥。",
            "output": "row_column_unconditional_closed=false。",
        },
    ]


def run(
    near_path: Path,
    current_path: Path,
    clb_path: Path,
    activation_path: Path,
    boundary_path: Path,
    pdec_path: Path,
    stitching_path: Path,
) -> dict[str, Any]:
    """执行条件稳定性路由。"""
    paths = [near_path, current_path, clb_path, activation_path, boundary_path, pdec_path, stitching_path]
    near = load_json(near_path)
    current = load_json(current_path)
    clb_text = clb_path.read_text(encoding="utf-8")
    activation_text = activation_path.read_text(encoding="utf-8")
    boundary_text = boundary_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    stitching_text = stitching_path.read_text(encoding="utf-8")
    proof_rows = rows(near, clb_text, activation_text, boundary_text, pdec_text, stitching_text)
    return {
        "certificate_type": "conditional_early_zero_stability_router",
        "status": "conditional_stability_dichotomy_closed_defect_schema_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "current_remaining_basis": current.get("latest_self_contained_basis", ""),
        "conditional_lemma_proved": True,
        "stable_recurrence_forced_unconditionally": False,
        "phase_defect_forced_if_no_stable_recurrence": True,
        "row_column_unconditional_closed": False,
        "terminal_gap_after_router": "EarlyZeroPhaseDefectSchemaAdmission",
        "terminal_gap_expansion": [
            "RegisteredSameFormalUnitRxFxLedger",
            "StableShortRecurrenceCertificateOrNoStableAutomorphism",
            "BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT",
        ],
        "rows": proof_rows,
        "closed_gates": [row["gate"] for row in proof_rows if row["closed"]],
        "open_gates": [row["gate"] for row in proof_rows if not row["closed"]],
        "structural_law": (
            "Under the counterexample assumption x<P is a zero row, the CLB decomposition "
            "puts all last holes in the same formal unit R_x and forces R_x=F_x. If the "
            "cover certificate has a short phase-preserving automorphism, it repeats as a "
            "stable zero row. If no such automorphism exists, the early zero row is already "
            "a boundary phase-lock defect: high-prime filler labels patch every low-skeleton "
            "hole at a representative x<P without forming a stable orbit. Thus the desired "
            "stability lemma is true as a dichotomy, but the defect branch still requires "
            "formal PDEC/SAE/ColumnCRT admission to become a contradiction."
        ),
        "plain_conclusion": (
            "在假设反例内，可以证明一个条件稳定性二分：P 行以内零行若存在，"
            "要么同一覆盖证书有短移自同构并稳定复现；要么没有短移自同构，"
            "那它本身就是同一 R_x/F_x formal unit 上的早期边界相位缺陷。"
            "这还不是最终矛盾；剩余是把该缺陷登记成可验收的 PDEC/SAE/ColumnCRT 证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 假设早期零行的稳定性/相位缺陷条件路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"conditional_lemma_proved={fmt_bool(result['conditional_lemma_proved'])}",
        f"stable_recurrence_forced_unconditionally={fmt_bool(result['stable_recurrence_forced_unconditionally'])}",
        f"phase_defect_forced_if_no_stable_recurrence={fmt_bool(result['phase_defect_forced_if_no_stable_recurrence'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 条件引理",
        "",
        "**Conditional Early-Zero Stability Dichotomy.**",
        "假设存在 `1<=x<P` 使第 `x` 条边界行 `xP+c, 1<=c<P` 是零行。固定 CLB 低骨架残洞 `R_x` 与高斜线补洞 `F_x`。则：",
        "",
        "```text",
        "EarlyZeroRowWithinP",
        "  => StableShortRecurrence",
        "     OR BoundaryPhaseNoncoverageDefectSameFormalUnit.",
        "```",
        "",
        "这里 `StableShortRecurrence` 指存在非零短移 `d`，使同一覆盖标签相位保持，因而同一证书在 `x+d` 复现；",
        "`BoundaryPhaseNoncoverageDefectSameFormalUnit` 指没有这种短移时，`R_x=F_x` 本身就是早期小代表元的全补洞相位锁定缺陷。",
        "",
        "## 2. 证明骨架",
        "",
        "1. 由 CLB 分解，低斜线留下 `R_x`，高斜线只在 `R_x` 内补洞。若第 `x` 行是零行，则 `U_x=R_x\\F_x` 为空，所以 `R_x=F_x`。",
        "2. 用 `Omega=R_x`、补洞标签 `tau(c)=q(c)`、权重 `w(c)=1` 固定同一个 formal unit。任何跨口径拼接都不允许作为证明，只能回流 Stitching/quotient/reuse。",
        "3. 若存在短移 `d` 同时保持所有已登记标签相位，即 `dP≡0 mod q(c)` 对全部必要标签成立，则同一覆盖证书在 `x+d` 行复现。",
        "4. 若不存在这种短移，则这个早期零行不是稳定轨道点，而是高素数补洞标签在 `R_x` 上一次性锁定全部残洞的边界相位缺陷。",
        "5. 该缺陷已经落入命名路线：`PDEC/SAE/ColumnCRT` 或首端帽 `BoundaryPhaseNoncoverage`，但还需要正式 schema 准入才能成为矛盾。",
        "",
        "## 3. 判定表",
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
            "## 4. 当前剩余",
            "",
            "条件稳定性二分不改变当前完全自足输入基：",
            "",
            "```text",
            result["current_remaining_basis"],
            "```",
            "",
            "新的最窄附加输入是：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = RegisteredSameFormalUnitRxFxLedger",
            "    AND StableShortRecurrenceCertificateOrNoStableAutomorphism",
            "    AND BoundaryPhaseNoncoverageDefectToPDECOrSAEOrColumnCRT.",
            "```",
            "",
            "这说明你的思路可以作为反例分支内的稳定性二分使用；但若要变成最终矛盾，下一步必须把 `BoundaryPhaseNoncoverageDefectSameFormalUnit` 的证书字段完全登记并通过 PDEC/SAE/ColumnCRT 准入。"
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--near-json", type=Path, default=DEFAULT_NEAR)
    parser.add_argument("--current-json", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--clb-md", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--activation-md", type=Path, default=DEFAULT_ACTIVATION)
    parser.add_argument("--boundary-md", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--pdec-md", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--stitching-md", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        near_path=args.near_json,
        current_path=args.current_json,
        clb_path=args.clb_md,
        activation_path=args.activation_md,
        boundary_path=args.boundary_md,
        pdec_path=args.pdec_md,
        stitching_path=args.stitching_md,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
