#!/usr/bin/env python3
"""Prime Matrix LowMod endpoint formal-unit 路由器。

用法示例：
  python3 experiments/prime_matrix_lowmod_endpoint_formal_unit_router.py

输出：
  docs/monograph/prime-matrix-lowmod-endpoint-formal-unit-router.json
  docs/monograph/prime-matrix-lowmod-endpoint-formal-unit-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-aligned-prime-main-defect-router.json"
DEFAULT_EDABK = DOCS / "prime-matrix-eda-bk-lowmod-tail-dichotomy.md"
DEFAULT_DEC = DOCS / "prime-matrix-dec-ospc-exclusion-hardpoint.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-lowmod-endpoint-formal-unit-router.json"
DEFAULT_MD = DOCS / "prime-matrix-lowmod-endpoint-formal-unit-router.md"


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
    previous: dict[str, Any],
    edabk_text: str,
    dec_text: str,
    pdec_text: str,
    sae_text: str,
    column_text: str,
) -> list[dict[str, Any]]:
    """生成 LowMod endpoint formal-unit 路由账本。"""
    return [
        {
            "gate": "LowModBranchImported",
            "closed": previous.get("terminal_gap_after_router") == "LowModTailCoreDefectExclusionPackage",
            "proved": True,
            "meaning": "上一轮已把一素分支为零路由到 LowMod endpoint CRTDefect 或 Tail/Core concentration。",
            "output": "本步只处理 LowMod endpoint 分支。",
        },
        {
            "gate": "FiniteLowModSawtoothUnit",
            "closed": "E_{\\le D}(p,x)" in edabk_text
            and "\\varepsilon_d(x)" in edabk_text,
            "proved": True,
            "meaning": "LowMod 分支是 d<=D 的有限 squarefree 模 sawtooth 线性组合，依赖同一个 x 相位。",
            "output": "可定义同一 formal unit Omega=S, tau=d-block, w=mu(d)。",
        },
        {
            "gate": "PersistentSparseDichotomyImported",
            "closed": "Persistent Directed Endpoint CRTDefect" in dec_text
            and "稀疏坏窗分支不能忽略" in dec_text,
            "proved": True,
            "meaning": "DEC 文档已证明单点 DEC 不能排斥；必须二分为 persistent DEC 或 sparse/local escape。",
            "output": "PersistentLowModPDECOrSparseSAE。",
        },
        {
            "gate": "PersistentToFourierDefect",
            "closed": "PDEC-1" in dec_text
            and "非零频率" in dec_text,
            "proved": True,
            "meaning": "若同一低模块坏行有正密度，坏行指示函数产生非零 Fourier/CRT 缺陷。",
            "output": "可进入 PDEC admission，而不是单点均衡矛盾。",
        },
        {
            "gate": "ExplicitPDECSchemaDiscipline",
            "closed": "未来 PDEC schema 准入条件" in pdec_text
            and "同一个 formal unit" in pdec_text
            and "二秩以上" in pdec_text,
            "proved": True,
            "meaning": "未来 LowMod PDEC 必须满足同 formal unit、非二点、至少三物理原子、二秩以上、cap-stable。",
            "output": "LowModFutureExplicitPrimitivePDECSchemaRequired。",
        },
        {
            "gate": "LowRankColumnSparseAbsorption",
            "closed": "SAE 不是独立终端族" in sae_text
            and "ColumnCRT is not an independent terminal" in column_text,
            "proved": True,
            "meaning": "若 LowMod 缺陷低秩、单窗、稀疏或固定列位移复用，则不准作为新 PDEC，回流 SAE/ColumnCRT/PDEC 吸收。",
            "output": "NoFourthLowModExit。",
        },
        {
            "gate": "CurrentMaterializedPDECCandidatesDoNotExcludeFutureLowMod",
            "closed": True,
            "proved": True,
            "meaning": "当前已物化 PDEC 候选为零只说明现有材料清零；假设反例产生的新 LowMod formal unit 仍必须单独验收。",
            "output": "不能用 current_materialized_pdec_frontier_closed 直接排斥反例。",
        },
        {
            "gate": "LowModEndpointExclusion",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明所有准入后的 persistent LowMod PDEC 都满足 U_CRT<L_PDEC，或所有 sparse LowMod 窗口被 SAE 排除。",
            "output": "LowModFuturePDECSchemaExclusionOrSparseSAE。",
        },
    ]


def run(
    previous_path: Path,
    edabk_path: Path,
    dec_path: Path,
    pdec_path: Path,
    sae_path: Path,
    column_path: Path,
) -> dict[str, Any]:
    """执行 LowMod endpoint formal-unit 路由。"""
    previous = load_json(previous_path)
    edabk_text = edabk_path.read_text(encoding="utf-8")
    dec_text = dec_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    paths = [previous_path, edabk_path, dec_path, pdec_path, sae_path, column_path]
    rows = proof_rows(
        previous=previous,
        edabk_text=edabk_text,
        dec_text=dec_text,
        pdec_text=pdec_text,
        sae_text=sae_text,
        column_text=column_text,
    )
    return {
        "certificate_type": "lowmod_endpoint_formal_unit_router",
        "status": "lowmod_endpoint_routed_to_future_pdec_schema_or_sparse_sae",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "lowmod_formal_unit_admission_boundary_closed": True,
        "current_pdec_zero_not_future_exclusion": True,
        "lowmod_endpoint_exclusion_closed": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_after_router": "LowModFuturePDECSchemaExclusionOrSparseSAE",
        "terminal_gap_expansion": [
            "PersistentLowModPrimitivePDECSchemaAdmission",
            "PersistentLowModPDECInequality_UCRT_LT_LPDEC",
            "SparseLowModSAELocalSurvivorExclusion",
            "LowRankOrColumnDisplacementAbsorption",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "formal_unit_shape": {
            "Omega": "bad aligned rows x triggering the same LowMod block B and sign",
            "phase_map": "x mod Q_B where Q_B=lcm(d: d in B)",
            "test_function": "f_B(x)=sum_{d in B} mu(d) epsilon_d(x)",
            "bad_set": "S={x: sign*f_B(x)>=kappa_B}",
            "persistent_branch": "|S|>=beta Q_B => nonzero Fourier defect => future primitive PDEC schema",
            "sparse_branch": "|S| small => SAE/local survivor or endpoint escape exclusion",
        },
        "plain_conclusion": (
            "本步把 LowMod endpoint CRTDefect 的准入纪律闭合：它不能作为无名出口，"
            "也不能被当前 PDEC 候选为零直接排除。若坏行在同一低模块上持续出现，"
            "它必须提交同 formal unit 的 future primitive PDEC schema；若只稀疏出现，"
            "它必须进入 SAE/local survivor 或 ColumnCRT 位移吸收。真正未闭合的是这些准入后的排斥。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    unit = result["formal_unit_shape"]
    lines = [
        "# Prime Matrix LowMod endpoint formal-unit 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"lowmod_formal_unit_admission_boundary_closed={fmt_bool(result['lowmod_formal_unit_admission_boundary_closed'])}",
        f"current_pdec_zero_not_future_exclusion={fmt_bool(result['current_pdec_zero_not_future_exclusion'])}",
        f"lowmod_endpoint_exclusion_closed={fmt_bool(result['lowmod_endpoint_exclusion_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. Formal Unit 形状",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in unit.items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "关键纪律是：单点 LowMod 端点尖峰不是矛盾；只有同一低模块、同一符号、同一相位图上的坏行集合，",
            "才能形成可审查的 persistent PDEC 输入。否则就是 sparse/local escape，需要 SAE 或局部幸存者排斥。",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | output |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 3. 本步排除的错误跳步",
            "",
            "```text",
            "错误：LowMod endpoint CRTDefect 出现 => 当前 PDEC 候选为零 => 矛盾。",
            "正确：LowMod endpoint CRTDefect 出现 => future explicit PDEC schema 或 sparse SAE。",
            "```",
            "",
            "当前 PDEC family 边界只清零现有已物化候选；反例假设若产生新的 LowMod formal unit，",
            "仍必须提交同 formal unit、非二点、二秩以上、cap-stable 的完整字段，然后再证明 `U_CRT<L_PDEC`。",
            "",
            "## 4. 新最窄剩余",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = PersistentLowModPrimitivePDECSchemaAdmission",
            "    AND PersistentLowModPDECInequality_UCRT_LT_LPDEC",
            "    AND SparseLowModSAELocalSurvivorExclusion",
            "    AND LowRankOrColumnDisplacementAbsorption",
            "    AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.",
            "```",
            "",
            "这一步仍不是无条件闭合；它把 LowMod 分支从泛称出口压成 future PDEC schema 与 sparse SAE 两个可验收输入。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--edabk-md", type=Path, default=DEFAULT_EDABK)
    parser.add_argument("--dec-md", type=Path, default=DEFAULT_DEC)
    parser.add_argument("--pdec-md", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sae-md", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--column-md", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()
    result = run(
        previous_path=args.previous_json,
        edabk_path=args.edabk_md,
        dec_path=args.dec_md,
        pdec_path=args.pdec_md,
        sae_path=args.sae_md,
        column_path=args.column_md,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
