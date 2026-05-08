#!/usr/bin/env python3
"""Prime Matrix 近平方条带终端准入路由器。

用法示例：
  python3 experiments/prime_matrix_nearsquare_strip_terminal_admission_router.py

输出：
  docs/monograph/prime-matrix-nearsquare-strip-terminal-admission-router.json
  docs/monograph/prime-matrix-nearsquare-strip-terminal-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-nearsquare-strip-defect-certificate-router.json"
DEFAULT_GLOBAL_BOUNDARY = DOCS / "prime-matrix-global-terminal-family-boundary-router.json"
DEFAULT_GLOBAL_SPLIT = DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-nearsquare-strip-terminal-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-nearsquare-strip-terminal-admission-router.md"

OLD_ATOM = "NearSquareStripPDECOrSAEExclusionAlpha043"
GLOBAL_ATOM = "GlobalPDECorSparseTerminalExclusion"
NEW_ATOM = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
EXTERNAL_DISPERSION_ATOM = "ExternalWellFactorableSawtoothDispersionBoundAlpha043"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom_or_external(text: str, old: str, external: str, new: str) -> str:
    """优先替换已有 old OR external 包，避免重复外部原子。"""
    wrapped = f"({old} OR {external})"
    if wrapped in text:
        return text.replace(wrapped, f"({new} OR {external})")
    return text.replace(old, new)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    previous: dict[str, Any],
    global_boundary: dict[str, Any],
    global_split: dict[str, Any],
    pdec: dict[str, Any],
    sparse: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成近平方条带终端准入判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    same_formal_unit = (
        bool(previous.get("dyadic_strip_certificate_formal_unit_admission_proved"))
        and bool(previous.get("persistent_sparse_pdec_sae_admission_proved"))
    )
    global_boundary_ready = (
        bool(global_boundary.get("materialized_frontier_exhausted"))
        and bool(global_boundary.get("terminal_generation_contract_closed"))
        and not bool(global_boundary.get("global_terminal_family_exclusion_closed"))
    )
    pdec_boundary_ready = (
        bool(pdec.get("pdec_family_explicit_input_boundary_closed"))
        and bool(pdec.get("current_materialized_pdec_frontier_closed"))
        and not bool(pdec.get("global_pdec_family_unconditional_closed"))
    )
    sparse_boundary_ready = (
        bool(sparse.get("future_sparse_packet_schema_boundary_closed"))
        and bool(sparse.get("current_materialized_sparse_frontier_closed"))
        and not bool(sparse.get("global_sparse_family_unconditional_closed"))
    )
    split_ready = (
        bool(global_split.get("closed_nonfinal_reductions"))
        and global_split.get("self_contained_next_hardpoint") == NEW_ATOM
        and not bool(global_split.get("global_terminal_family_exclusion_closed"))
    )
    admission_closed = all(
        [
            active,
            guard,
            same_formal_unit,
            global_boundary_ready,
            pdec_boundary_ready,
            sparse_boundary_ready,
            split_ready,
        ]
    )
    return [
        row(
            "NearSquareStripTerminalGateActive",
            active,
            False,
            "最新最窄点是排斥 dyadic 近平方条带产生的 PDEC/SAE 证书。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条中做终端准入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "NearSquareStripSameFormalUnitCertificate",
            same_formal_unit,
            True,
            "上一层已证明失败态生成同一 dyadic 条带 formal unit，且持久/稀疏二分准入 PDEC/SAE。",
            GLOBAL_ATOM,
        ),
        row(
            "CurrentMaterializedTerminalFrontierImported",
            global_boundary_ready,
            True,
            "当前已物化终端前沿耗尽；未来证书不能靠样本消元，必须进入全局终端家族。",
            GLOBAL_ATOM,
        ),
        row(
            "PDECAndSparseBoundaryImported",
            pdec_boundary_ready and sparse_boundary_ready,
            True,
            "PDEC 显式输入边界与 future sparse packet 边界均已登记；二者本身仍未无条件排斥。",
            GLOBAL_ATOM,
        ),
        row(
            "GlobalTerminalSplitImported",
            split_ready,
            True,
            "全局终端家族拆分已把 GlobalPDECorSparseTerminalExclusion 压到 PDEC-CAP 或内部 CleanKLS/DLS。",
            NEW_ATOM,
        ),
        row(
            "NearSquareIndependentTerminalRemoved",
            admission_closed,
            False,
            "近平方条带没有独立第四出口；其终端义务被吸收到全局 PDEC/sparse 终端门。",
            NEW_ATOM,
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "仍需证明全局 PDEC-CAP 容量证书，或内部 CleanKLS/DLS 大筛吸收。",
            NEW_ATOM,
        ),
        row(
            EXTERNAL_DISPERSION_ATOM,
            False,
            False,
            "外部解析路线仍可直接给 well-factorable sawtooth/条带分散估计。",
            EXTERNAL_DISPERSION_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "短区间 rough-number 下界仍可绕过内部 sawtooth 与条带分析。",
            EXTERNAL_ROUGH_ATOM,
        ),
        row(
            EXTERNAL_DIBFI_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_DIBFI_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行近平方条带终端准入路由。"""
    data = {name: load_json(path) for name, path in paths.items()}
    rows = build_rows(**data)
    admission_closed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "NearSquareIndependentTerminalRemoved"
    )
    previous = data["previous"]
    latest_self = previous.get("latest_self_contained_basis", "").replace(OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom_or_external(
        previous.get("latest_conditional_basis", ""), OLD_ATOM, EXTERNAL_DISPERSION_ATOM, NEW_ATOM
    )
    latest_global = replace_atom_or_external(
        previous.get("latest_global_with_external_basis", ""), OLD_ATOM, EXTERNAL_DISPERSION_ATOM, NEW_ATOM
    )
    return {
        "certificate_type": "nearsquare_strip_terminal_admission_router",
        "status": "nearsquare_strip_terminal_admitted_to_global_pdec_sparse_split_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "nearsquare_strip_terminal_admission_closed": admission_closed,
        "nearsquare_strip_independent_terminal_remaining": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "external_well_factorable_sawtooth_dispersion_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_intermediate": GLOBAL_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": NEW_ATOM,
        "external_next_priority": EXTERNAL_DISPERSION_ATOM,
        "rough_fallback_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "admission_chain": [
            f"{OLD_ATOM} -> {GLOBAL_ATOM}",
            f"{GLOBAL_ATOM} -> {NEW_ATOM}",
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步删除了近平方条带的独立终端地位。上一层已把失败态做成同一 dyadic 条带 "
            "formal unit 的 PDEC/SAE 证书；既有全局终端家族边界又说明这类证书不能作为第四出口，"
            "必须进入全局 PDEC/sparse 终端拆分。因此当前真正剩余改为 "
            f"{NEW_ATOM}。这仍不是行列无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 近平方条带终端准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"nearsquare_strip_terminal_admission_closed={fmt_bool(result['nearsquare_strip_terminal_admission_closed'])}",
        (
            "nearsquare_strip_independent_terminal_remaining="
            f"{fmt_bool(result['nearsquare_strip_independent_terminal_remaining'])}"
        ),
        (
            "pdec_cap_or_internal_clean_kls_large_sieve_proved="
            f"{fmt_bool(result['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 准入链条",
        "",
        "```text",
        *result["admission_chain"],
        "```",
        "",
        "## 2. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            f"直接攻 `{result['next_priority']}`；外部备线仍为 `{result['external_next_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--global-boundary", type=Path, default=DEFAULT_GLOBAL_BOUNDARY)
    parser.add_argument("--global-split", type=Path, default=DEFAULT_GLOBAL_SPLIT)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "global_boundary": args.global_boundary,
        "global_split": args.global_split,
        "pdec": args.pdec,
        "sparse": args.sparse,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
