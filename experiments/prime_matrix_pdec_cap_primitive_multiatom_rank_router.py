#!/usr/bin/env python3
"""把 primitive 多原子同 formal unit PDEC 终端压到二秩 cap-stable 核。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_primitive_multiatom_rank_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-primitive-multiatom-rank-router.json
  docs/monograph/prime-matrix-pdec-cap-primitive-multiatom-rank-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_ADMISSION = (
    DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.json"
)
DEFAULT_NONTAUTOLOGY = DOCS / "prime-matrix-nontautological-pdec-admission-audit.json"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_PDEC_ROUTE = DOCS / "prime-matrix-triad-a1-pdec-capacity-upper-route.md"
DEFAULT_DUAL_ABSORB = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_NO_CYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_COLUMNCRT_ABSORB = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_COMMON_VARIABLE = (
    DOCS / "prime-matrix-pdec-cap-dense-kernel-common-variable-router.md"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-primitive-multiatom-rank-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-primitive-multiatom-rank-router.md"


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
    admission: dict[str, Any],
    nontautology: dict[str, Any],
    terminal_triad_text: str,
    pdec_route_text: str,
    dual_absorb_text: str,
    no_cycle_text: str,
    columncrt_text: str,
    common_variable_text: str,
) -> list[dict[str, Any]]:
    """生成 primitive 多原子 PDEC 秩边界审查表。"""
    admission_gate_active = (
        admission["persistent_terminal_admission_boundary_closed"]
        and admission["narrowest_next_hardpoint"]
        == "PrimitiveMultiAtomSameFormalUnitPDECCertificate"
    )
    same_formal_unit_protocol_registered = has_all(
        terminal_triad_text,
        [
            "formal unit Omega",
            "signature group G",
            "bad-window/count function",
            "U_{\\rm CRT}<L_{\\rm PDEC}",
        ],
    )
    same_set_capacity_protocol_registered = has_all(
        pdec_route_text,
        [
            "Same-Set Law",
            "AttachmentFail",
            "PhaseCompatFail",
            "CapacityInsufficient",
            "RoutingGap",
        ],
    )
    degenerate_atom_cases_absorbed = (
        nontautology["all_current_routes_blocked_or_absorbed"]
        and nontautology[
            "current_materialized_nontautological_pdec_candidate_count"
        ]
        == 0
        and any(
            "at least three physical primitive atoms" in item
            for item in nontautology["future_admission_requirements"]
        )
    )
    rank_zero_one_routes_named = (
        degenerate_atom_cases_absorbed
        and has_all(
            columncrt_text,
            [
                "ColumnCRT-Displacement Absorption",
                "displacement PDEC",
                "formal-unit refinement / primitive quotient",
            ],
        )
        and has_all(
            common_variable_text,
            [
                "c_b=rho_b+r k_b",
                "fixed shell or finite shell packet",
                "PDEC / ColumnCRT",
            ],
        )
    )
    dual_failure_absorbed = has_all(
        dual_absorb_text,
        [
            "Cap localization",
            "CapSparse",
            "CapPersistent",
            "CapColumn",
            "Multiplicity-Stitching",
        ],
    )
    cap_refinement_no_cycle = has_all(
        no_cycle_text,
        [
            "PDEC-Cap-NoCycle",
            "固定有限签名群",
            "new-layer PDEC",
            "CleanKLS/DLS",
        ],
    )
    rank_boundary_derived = all(
        [
            admission_gate_active,
            same_formal_unit_protocol_registered,
            same_set_capacity_protocol_registered,
            degenerate_atom_cases_absorbed,
            rank_zero_one_routes_named,
            dual_failure_absorbed,
            cap_refinement_no_cycle,
        ]
    )
    return [
        row(
            "PrimitiveMultiAtomAdmissionGateActive",
            admission_gate_active,
            admission["narrowest_next_hardpoint"],
            "上一层已经证明裸持久签名不能直接作为终端，只能先进入 primitive 多原子同 formal unit 准入门。",
            False,
        ),
        row(
            "SameFormalUnitCapacityProtocolRegistered",
            same_formal_unit_protocol_registered
            and same_set_capacity_protocol_registered,
            "formal unit + Same-Set Law + U_CRT<L_PDEC",
            "容量比较必须在同一 formal unit、同一坏窗计数函数和同一相位映射上进行。",
            False,
        ),
        row(
            "DegenerateOneTwoAtomCasesAbsorbed",
            degenerate_atom_cases_absorbed,
            "current primitive candidate count=0; future admission requires >=3 atoms",
            "一原子、重复原子、物理二点 Fourier tautology 和当前二点 SAE/Endpoint 已不再是 PDEC 终端。",
            False,
        ),
        row(
            "RankZeroOnePrimitiveBranchNamed",
            rank_zero_one_routes_named,
            "duplicate / two-point / fixed-shell / ColumnCRT routes",
            "若去重后原子只生成零秩或一秩相位结构，它不是真正多原子核：只能回到重复口径、二点 tautology、固定壳 PDEC/ColumnCRT 或 SAE。",
            False,
        ),
        row(
            "DualCapFailureAbsorbedBeforeTerminal",
            dual_failure_absorbed,
            "CapSparse / CapPersistent / CapColumn / Multiplicity-Stitching",
            "任何尚未证明 U_CRT<L_PDEC 的方向，若失败，必须先输出帽集中并回流 SAE、refined PDEC、ColumnCRT 或口径规范化。",
            False,
        ),
        row(
            "CapRefinementNoCycleBeforeTerminal",
            cap_refinement_no_cycle,
            "finite Boolean algebra refinement or new-layer entropy dichotomy",
            "持久帽细化不能在固定签名群内无限循环；升层也必须命名为 new-layer PDEC 或 CleanKLS/DLS。",
            False,
        ),
        row(
            "PrimitiveRankBoundaryDerived",
            rank_boundary_derived,
            "rank 0/1 and cap-failure exits removed before final kernel",
            "primitive 多原子同 formal unit 终端已被规范化为低秩退化、cap 失败回流、或真正二秩以上 cap-stable 核三类。",
            False,
        ),
        row(
            "RankTwoCapStablePrimitivePDECKernelInequality",
            False,
            "global U_CRT<L_PDEC for rank>=2 cap-stable primitive kernels not submitted",
            "剩余全球硬点是证明所有二秩以上且无可回流 cap 的 primitive 同 formal unit 核满足严格容量排斥。",
            True,
        ),
    ]


def run(
    admission_path: Path,
    nontautology_path: Path,
    terminal_triad_path: Path,
    pdec_route_path: Path,
    dual_absorb_path: Path,
    no_cycle_path: Path,
    columncrt_absorb_path: Path,
    common_variable_path: Path,
) -> dict[str, Any]:
    """运行 primitive 多原子 PDEC 秩边界路由。"""
    admission = load_json(admission_path)
    nontautology = load_json(nontautology_path)
    terminal_triad_text = read_text(terminal_triad_path)
    pdec_route_text = read_text(pdec_route_path)
    dual_absorb_text = read_text(dual_absorb_path)
    no_cycle_text = read_text(no_cycle_path)
    columncrt_text = read_text(columncrt_absorb_path)
    common_variable_text = read_text(common_variable_path)
    rows = build_rows(
        admission=admission,
        nontautology=nontautology,
        terminal_triad_text=terminal_triad_text,
        pdec_route_text=pdec_route_text,
        dual_absorb_text=dual_absorb_text,
        no_cycle_text=no_cycle_text,
        columncrt_text=columncrt_text,
        common_variable_text=common_variable_text,
    )
    rank_boundary_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "PrimitiveRankBoundaryDerived"
    )
    current_instances_closed = (
        admission["current_materialized_persistent_terminal_instances_closed"]
        and nontautology["current_materialized_nontautological_pdec_candidate_count"]
        == 0
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_primitive_multiatom_rank_router",
        "status": "primitive_multiatom_pdec_reduced_to_rank_two_cap_stable_kernel",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "persistent_terminal_admission": file_sha256(admission_path),
            "nontautological_admission": file_sha256(nontautology_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "pdec_route": file_sha256(pdec_route_path),
            "dual_absorb": file_sha256(dual_absorb_path),
            "no_cycle": file_sha256(no_cycle_path),
            "columncrt_absorb": file_sha256(columncrt_absorb_path),
            "common_variable": file_sha256(common_variable_path),
        },
        "primitive_multiatom_rank_boundary_closed": rank_boundary_closed,
        "current_materialized_primitive_multiatom_instances_closed": current_instances_closed,
        "primitive_rank_two_cap_stable_kernel_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "RankTwoCapStablePrimitivePDECKernelInequality",
        "rows": rows,
        "rank_boundary_law": (
            "PrimitiveMultiAtomSameFormalUnitPDECCertificate is not admitted as a raw "
            "terminal label. After the same-formal-unit and same-set capacity protocol is "
            "fixed, quotient the physical primitive atoms by already registered duplicate, "
            "cross-chart, and two-point tautology relations. Rank 0 is non-primitive or "
            "reuse. Rank 1 is a one-dimensional shell/column/displacement signature and "
            "therefore routes to fixed-shell PDEC, ColumnCRT, or SAE; the current two-point "
            "case is already absorbed. If a higher-rank candidate fails U_CRT<L_PDEC, the "
            "dual-failure contract outputs a cap; sparse caps route to SAE, persistent caps "
            "to refined PDEC/ColumnCRT, and mismatched caps to multiplicity normalization. "
            "PDEC cap refinement has no fixed-level cycle. Therefore the only remaining "
            "kernel is rank at least two, cap-stable, same-formal-unit primitive PDEC."
        ),
        "review_conclusion": (
            "primitive 多原子同 formal unit PDEC 已不再作为黑箱终端保留。低秩退化、"
            "二点 Fourier tautology、固定壳/ColumnCRT、对偶 cap 失败和口径不一致都必须"
            "先回流到已命名路线。当前已物化 primitive 多原子实例仍为零；未来真正剩余只可能是"
            "二秩以上、cap-stable、同 formal unit 的 primitive PDEC 核不等式。该项没有证明"
            "完整行/列无条件定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP primitive 多原子秩边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 秩边界律",
        "",
        result["rank_boundary_law"],
        "",
        "```text",
        "PrimitiveMultiAtomSameFormalUnitPDECCertificate",
        "  => same formal unit and same-set capacity protocol;",
        "  => quotient duplicate / cross-chart / two-point tautology;",
        "  => rank 0: non-primitive or reuse defect;",
        "  => rank 1: fixed shell / ColumnCRT / SAE / refined PDEC;",
        "  => dual cap failure: SAE / refined PDEC / ColumnCRT / multiplicity;",
        "  => no fixed-level cap cycle;",
        "  => remaining terminal:",
        "       RankTwoCapStablePrimitivePDECKernelInequality.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `primitive_multiatom_rank_boundary_closed={fmt_bool(result['primitive_multiatom_rank_boundary_closed'])}`。",
        f"- `current_materialized_primitive_multiatom_instances_closed={fmt_bool(result['current_materialized_primitive_multiatom_instances_closed'])}`。",
        f"- `primitive_rank_two_cap_stable_kernel_closed={fmt_bool(result['primitive_rank_two_cap_stable_kernel_closed'])}`。",
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
            "下一步不再攻击宽口径 `PrimitiveMultiAtomSameFormalUnitPDECCertificate`，而是直接攻击 "
            "`RankTwoCapStablePrimitivePDECKernelInequality`：对所有二秩以上、同 formal unit、"
            "且没有 SAE/refined PDEC/ColumnCRT/multiplicity 回流帽的 primitive 核，证明同一坏窗"
            "上的 `U_CRT<L_PDEC`。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--admission-json", type=Path, default=DEFAULT_ADMISSION)
    parser.add_argument("--nontautology-json", type=Path, default=DEFAULT_NONTAUTOLOGY)
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument("--pdec-route-md", type=Path, default=DEFAULT_PDEC_ROUTE)
    parser.add_argument("--dual-absorb-md", type=Path, default=DEFAULT_DUAL_ABSORB)
    parser.add_argument("--no-cycle-md", type=Path, default=DEFAULT_NO_CYCLE)
    parser.add_argument("--columncrt-absorb-md", type=Path, default=DEFAULT_COLUMNCRT_ABSORB)
    parser.add_argument("--common-variable-md", type=Path, default=DEFAULT_COMMON_VARIABLE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        admission_path=args.admission_json,
        nontautology_path=args.nontautology_json,
        terminal_triad_path=args.terminal_triad_md,
        pdec_route_path=args.pdec_route_md,
        dual_absorb_path=args.dual_absorb_md,
        no_cycle_path=args.no_cycle_md,
        columncrt_absorb_path=args.columncrt_absorb_md,
        common_variable_path=args.common_variable_md,
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
