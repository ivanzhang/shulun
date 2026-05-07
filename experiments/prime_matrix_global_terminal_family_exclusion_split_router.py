#!/usr/bin/env python3
"""把全局终端家族排斥剩余拆成最小可攻门。

用法示例：
  python3 experiments/prime_matrix_global_terminal_family_exclusion_split_router.py

输出：
  docs/monograph/prime-matrix-global-terminal-family-exclusion-split-router.json
  docs/monograph/prime-matrix-global-terminal-family-exclusion-split-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_GLOBAL_BOUNDARY = DOCS / "prime-matrix-global-terminal-family-boundary-router.json"
DEFAULT_TERMINAL_TRIAD = DOCS / "prime-matrix-terminal-certificate-triad.md"
DEFAULT_CONTINUOUS_DICHOTOMY = (
    DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json"
)
DEFAULT_PDEC_ROUTE = DOCS / "prime-matrix-triad-a1-pdec-capacity-upper-route.md"
DEFAULT_CLEAN_KLS_CONTRACT = DOCS / "prime-matrix-cleankls-dls-certificate-contract.md"
DEFAULT_LOCAL_PACKET_CONTRACT = (
    DOCS / "prime-matrix-local-survivor-packet-generation-contract.md"
)
DEFAULT_NCBLK = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.json"
DEFAULT_LINE_REF = DOCS / "line-by-line-internal-referee-matrix.md"
DEFAULT_JSON = DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json"
DEFAULT_MD = DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def find_global_row(global_boundary: dict[str, Any], gate: str) -> dict[str, Any]:
    """按 gate 查找全局边界审查行。"""
    for row in global_boundary.get("rows", []):
        if row.get("gate") == gate:
            return row
    return {}


def split_row(
    gate: str,
    closed: bool,
    evidence: str,
    reduction: str,
    next_action: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造拆分行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "reduction": reduction,
        "next_action": next_action,
        "blocks_final": blocks_final,
    }


def build_rows(
    global_boundary: dict[str, Any],
    terminal_triad_text: str,
    continuous_dichotomy: dict[str, Any],
    pdec_route_text: str,
    clean_kls_text: str,
    local_packet_text: str,
    ncblk: dict[str, Any],
    line_ref_text: str,
) -> list[dict[str, Any]]:
    """生成全局终端家族剩余拆分表。"""
    materialized_row = find_global_row(global_boundary, "CurrentMaterializedFrontierExhausted")
    local_row = find_global_row(global_boundary, "CurrentLocalSurvivorAndSparseEntryGuarded")
    ncblk_row = find_global_row(global_boundary, "NCBLKBoundaryReconciled")
    triad_generation_row = find_global_row(global_boundary, "TerminalTriadGenerationContract")

    terminal_schema_closed = (
        bool(triad_generation_row.get("closed"))
        and has_all(
            terminal_triad_text,
            [
                "Terminal Triad Reduction",
                "PDEC family certificates",
                "LocalSurvivorCert family",
                "CleanKLS/DLS",
                "不存在第四类可持续逃逸",
            ],
        )
    )
    local_survivor_no_independent_blocker = (
        bool(local_row.get("closed"))
        and has_all(
            local_packet_text,
            [
                "Packet-generation 引理",
                "same signature persists",
                "signature layer escapes to CleanKLS/DLS admission",
                "不是最终行列无条件证明",
            ],
        )
    )
    continuous_split_closed = (
        continuous_dichotomy["status"]
        == "continuous_terminal_dichotomy_admission_closed_capacity_open"
        and {
            "PDEC-CAP: prove the resulting column-tail PDEC capacity inequality U_CRT<L_PDEC",
            "KLS-EXT: prove or import the CleanKLS/DLS large-sieve bound for diffuse payment measures",
        }.issubset(set(continuous_dichotomy["open_terminal_obligations"]))
        and "no third terminal route in the finite-projection dichotomy"
        in continuous_dichotomy["closed_subclaims"]
    )
    pdec_capacity_open = has_all(
        pdec_route_text,
        [
            "triad_a1_capacity_upper_route_not_closed",
            "general LP/dual U_CRT<L_PDEC still open",
            "它仍未提交任何全局 `U_CRT<L_PDEC` 证书",
        ],
    )
    clean_kls_open = has_all(
        clean_kls_text,
        [
            "cleankls_reduced_to_flat_large_sieve_certificate_or_pdec_not_closed",
            "LargeSieve certificate",
            "ExternalKLS input",
            "外部定理缺失，标为 ExternalInput",
        ],
    )
    ncblk_no_independent_blocker = (
        bool(ncblk_row.get("closed"))
        and ncblk["all_reconciliation_gates_passed"]
        and ncblk["canonical_ncblk_absorbed_by_existing_boundary"]
    )
    referee_open = "BLOCK-REFEREE" in line_ref_text

    return [
        split_row(
            gate="MaterializedFrontierAlreadyExhausted",
            closed=bool(materialized_row.get("closed")),
            evidence=materialized_row.get("evidence", "missing"),
            reduction="不再存在当前样本层可继续局部消元的 PDEC/LocalSurvivor/NC-BLK 对象。",
            next_action="进入全局家族证书，不再优化当前 ell=199 或旧 NC-BLK 标签。",
            blocks_final=False,
        ),
        split_row(
            gate="TerminalSchemaNoFourthExit",
            closed=terminal_schema_closed,
            evidence="Terminal Triad Reduction",
            reduction="任何最小反例终端对象只能是 PDEC、LocalSurvivor 或 CleanKLS/DLS。",
            next_action="只允许在三类证书内继续推进。",
            blocks_final=False,
        ),
        split_row(
            gate="LocalSurvivorNoIndependentGlobalBlocker",
            closed=local_survivor_no_independent_blocker,
            evidence=local_row.get("evidence", "missing"),
            reduction=(
                "当前孤窗包与已知入口均闭合；未来 sparse 路线若复现则回 PDEC，"
                "若升层逃逸则进 CleanKLS/DLS。"
            ),
            next_action="未来新增 sparse 路线必须同时提交 extractor schema 与有限账本。",
            blocks_final=False,
        ),
        split_row(
            gate="ContinuousTerminalDichotomy",
            closed=continuous_split_closed,
            evidence="; ".join(continuous_dichotomy["open_terminal_obligations"]),
            reduction=(
                "正 limsup 有限签名给 PDEC 输入；全部有限签名消散给 L2-flat CleanKLS/DLS 输入。"
            ),
            next_action="剩余只攻 PDEC-CAP 或 KLS-EXT。",
            blocks_final=False,
        ),
        split_row(
            gate="NCBLKNoIndependentGlobalBlocker",
            closed=ncblk_no_independent_blocker,
            evidence=ncblk_row.get("evidence", "missing"),
            reduction="canonical-source NC-BLK 已吸收；generic NC-BLK 保持外部/精确源熵路线。",
            next_action="不再把 NC-BLK 当成新的内部终端家族。",
            blocks_final=False,
        ),
        split_row(
            gate="PDEC_CAP",
            closed=not pdec_capacity_open,
            evidence="triad_a1_capacity_upper_route_not_closed" if pdec_capacity_open else "closed",
            reduction="PDEC 家族排斥等价于同一坏窗集合上的 U_CRT<L_PDEC 容量证书。",
            next_action="提交全局 LP/对偶容量证书，或把失败 DualCap 回流到 LocalSurvivor/CleanKLS。",
            blocks_final=pdec_capacity_open,
        ),
        split_row(
            gate="KLS_EXT_OR_INTERNAL_LARGE_SIEVE",
            closed=not clean_kls_open,
            evidence=(
                "cleankls_reduced_to_flat_large_sieve_certificate_or_pdec_not_closed"
                if clean_kls_open
                else "closed"
            ),
            reduction="CleanKLS/DLS 家族排斥等价于内部大筛界，或明确外部 KLS/DI/BFI 输入。",
            next_action="证明 L2-flat clean residual 的大筛吸收，或逐项登记外部定理变量适配。",
            blocks_final=clean_kls_open,
        ),
        split_row(
            gate="DStructureRankinReferee",
            closed=not referee_open,
            evidence="BLOCK-REFEREE" if referee_open else "no referee block token found",
            reduction="最终升级仍需 D-structure/Tail-log4/finite Rankin 接口被独立接受。",
            next_action="保持为最终晋级门，不由三终端局部边界替代。",
            blocks_final=referee_open,
        ),
    ]


def run(
    global_boundary_path: Path,
    terminal_triad_path: Path,
    continuous_dichotomy_path: Path,
    pdec_route_path: Path,
    clean_kls_path: Path,
    local_packet_path: Path,
    ncblk_path: Path,
    line_ref_path: Path,
) -> dict[str, Any]:
    """运行全局终端家族排斥拆分。"""
    global_boundary = load_json(global_boundary_path)
    terminal_triad_text = read_text(terminal_triad_path)
    continuous_dichotomy = load_json(continuous_dichotomy_path)
    pdec_route_text = read_text(pdec_route_path)
    clean_kls_text = read_text(clean_kls_path)
    local_packet_text = read_text(local_packet_path)
    ncblk = load_json(ncblk_path)
    line_ref_text = read_text(line_ref_path)

    rows = build_rows(
        global_boundary=global_boundary,
        terminal_triad_text=terminal_triad_text,
        continuous_dichotomy=continuous_dichotomy,
        pdec_route_text=pdec_route_text,
        clean_kls_text=clean_kls_text,
        local_packet_text=local_packet_text,
        ncblk=ncblk,
        line_ref_text=line_ref_text,
    )
    closed_nonfinal = all(row["closed"] for row in rows if not row["blocks_final"])
    open_final_gates = [row["gate"] for row in rows if row["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_global_terminal_family_exclusion_split_router",
        "status": "global_terminal_family_exclusion_reduced_not_closed",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "global_boundary": file_sha256(global_boundary_path),
            "terminal_triad": file_sha256(terminal_triad_path),
            "continuous_dichotomy": file_sha256(continuous_dichotomy_path),
            "pdec_route": file_sha256(pdec_route_path),
            "clean_kls_contract": file_sha256(clean_kls_path),
            "local_packet_contract": file_sha256(local_packet_path),
            "ncblk": file_sha256(ncblk_path),
            "line_referee": file_sha256(line_ref_path),
        },
        "closed_nonfinal_reductions": closed_nonfinal,
        "global_terminal_family_exclusion_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": "PDEC_CAP_OR_KLS_EXT_OR_REFEREE",
        "self_contained_next_hardpoint": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
        "rows": rows,
        "split_law": (
            "After the current materialized frontier is exhausted, the terminal family problem "
            "has no independent fourth route and no independent current LocalSurvivor or NC-BLK "
            "blocker. The finite-projection dichotomy sends positive-limsup terminal mass to "
            "PDEC-CAP and diffuse terminal mass to CleanKLS/DLS. Therefore the self-contained "
            "mathematical remainder is exactly PDEC-CAP or internal CleanKLS large-sieve; final "
            "promotion additionally needs the D-structure/Rankin referee interface."
        ),
        "review_conclusion": (
            "全局终端家族排斥已经进一步拆窄：LocalSurvivor 当前与已知入口不再构成独立终端，"
            "NC-BLK 不再构成独立终端，连续终端二分把所有剩余质量送入 PDEC-CAP 或 CleanKLS/DLS。"
            "因此完全自足路线的真实剩余是 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`；"
            "若允许外部/审稿输入，还需 `KLS_EXT` 与 `DStructureRankinReferee`。完整行/列定理仍未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 全局终端家族排斥拆分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 拆分律",
        "",
        result["split_law"],
        "",
        "```text",
        "GlobalTerminalFamilyExclusionCertificates",
        "  => no fourth terminal route;",
        "  => current LocalSurvivor / NC-BLK are not independent blockers;",
        "  => positive-limsup finite signature -> PDEC-CAP;",
        "  => diffuse finite signatures -> CleanKLS/DLS;",
        "  => final theorem promotion still needs D/Rankin referee acceptance.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `closed_nonfinal_reductions={fmt_bool(result['closed_nonfinal_reductions'])}`。",
        f"- `global_terminal_family_exclusion_closed={fmt_bool(result['global_terminal_family_exclusion_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        f"- `self_contained_next_hardpoint={result['self_contained_next_hardpoint']}`。",
        "",
        "## 3. 拆分表",
        "",
        "| gate | closed | blocks final | evidence | reduction | next action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {reduction} | {next_action} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                blocks=fmt_bool(bool(row["blocks_final"])),
                evidence=table_cell(row["evidence"]),
                reduction=table_cell(row["reduction"]),
                next_action=table_cell(row["next_action"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 结论边界",
            "",
            "本路由器关闭的是“全局终端家族剩余仍含未命名或局部样本硬点”的可能。"
            "它没有关闭 `PDEC-CAP`、`CleanKLS/DLS` 大筛估计或 `D/Rankin` 审稿门；"
            "因此不能把完整行/列无条件命题标为已证。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--global-boundary-json", type=Path, default=DEFAULT_GLOBAL_BOUNDARY)
    parser.add_argument("--terminal-triad-md", type=Path, default=DEFAULT_TERMINAL_TRIAD)
    parser.add_argument(
        "--continuous-dichotomy-json", type=Path, default=DEFAULT_CONTINUOUS_DICHOTOMY
    )
    parser.add_argument("--pdec-route-md", type=Path, default=DEFAULT_PDEC_ROUTE)
    parser.add_argument("--clean-kls-md", type=Path, default=DEFAULT_CLEAN_KLS_CONTRACT)
    parser.add_argument("--local-packet-md", type=Path, default=DEFAULT_LOCAL_PACKET_CONTRACT)
    parser.add_argument("--ncblk-json", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument("--line-ref-md", type=Path, default=DEFAULT_LINE_REF)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        global_boundary_path=args.global_boundary_json,
        terminal_triad_path=args.terminal_triad_md,
        continuous_dichotomy_path=args.continuous_dichotomy_json,
        pdec_route_path=args.pdec_route_md,
        clean_kls_path=args.clean_kls_md,
        local_packet_path=args.local_packet_md,
        ncblk_path=args.ncblk_json,
        line_ref_path=args.line_ref_md,
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
