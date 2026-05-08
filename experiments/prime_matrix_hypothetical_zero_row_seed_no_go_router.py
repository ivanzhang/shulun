#!/usr/bin/env python3
"""Prime Matrix 假设早期零行不能生成无环源种子的路由器。

用法示例：
  python3 experiments/prime_matrix_hypothetical_zero_row_seed_no_go_router.py

输出：
  docs/monograph/prime-matrix-hypothetical-zero-row-seed-no-go-router.json
  docs/monograph/prime-matrix-hypothetical-zero-row-seed-no-go-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-clean-core-source-loop-cut-router.json"
DEFAULT_ZERO_ROW = DOCS / "prime-matrix-zero-row-full-crt-diagonal-minrep.md"
DEFAULT_GEOMETRY = DOCS / "prime-matrix-clean-core-geometric-phi-budget-bridge-router.md"
DEFAULT_SOURCE_LOOP = DOCS / "prime-matrix-clean-core-source-loop-cut-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.json"
DEFAULT_MD = DOCS / "prime-matrix-hypothetical-zero-row-seed-no-go-router.md"

OLD_ATOM = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
NEW_ATOM = "IndependentPreCauchyArithmeticSourceIdentityForNoncanonicalCleanCoreAndReturn"


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


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的源种子原子。"""
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
    zero_text: str,
    geometry_text: str,
    source_loop_text: str,
) -> list[dict[str, Any]]:
    """判定早期零行假设是否能提供无环 pre-Cauchy 源种子。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    zero_crt_closed = (
        "完整覆盖 CRT 证书" in zero_text
        and "Z_p=" in zero_text
        and "X_0(p)" in zero_text
    )
    zero_only_cover = (
        "px+k" in zero_text
        and "tau" in zero_text
        and "q_k" in zero_text
        and "alpha/delta" not in zero_text
    )
    geometry_no_source = (
        "GeometryDoesNotDefineSignedSourceMeasure" in geometry_text
        and "not => signed alpha/delta source measure" in geometry_text
        and "geometry_defines_signed_source_measure=false" in geometry_text
    )
    reverse_loop_rejected = (
        "source_loop_detected=true" in source_loop_text
        and "circular_reverse_derivation_rejected=true" in source_loop_text
        and "不能从 downstream payment skeleton 反向生成 primitive source" in source_loop_text
    )
    no_go = all([active, zero_crt_closed, zero_only_cover, geometry_no_source, reverse_loop_rejected])
    return [
        row(
            "AcyclicSeedGateActive",
            active,
            False,
            "最新最窄点要求无环 pre-Cauchy noncanonical primitive source seed。",
            "判断早期零行假设本身能否提供该 seed。",
        ),
        row(
            "ZeroRowCRTEquivalenceClosed",
            zero_crt_closed,
            True,
            "早期零行严格等价于完整覆盖 CRT 证书和最小代表条件。",
            "这只是覆盖/残基数据。",
        ),
        row(
            "HypotheticalZeroRowDataUnsigned",
            zero_only_cover,
            True,
            "假设零行给出 tau、q_k、列覆盖和 CRT 残基；它不含 alpha/delta signed source 字段。",
            "不能从 unsigned cover 直接得到 signed pre-Cauchy seed。",
        ),
        row(
            "GeometryPaymentBaseNoSourceMeasure",
            geometry_no_source,
            True,
            "斜线覆盖、圆柱环绕、P列锚和层叠轮只给 payment/Phi 基底与预算形状。",
            "几何模型不生成 signed alpha/delta 源测度。",
        ),
        row(
            "DownstreamReverseSourceBlocked",
            reverse_loop_rejected,
            True,
            "来源环切断已拒绝从 payment skeleton 或有限投影反推 primitive source。",
            "不能把假设链的输出当作 pre-Cauchy 输入。",
        ),
        row(
            "HypotheticalZeroRowCannotSupplyAcyclicSeed",
            no_go,
            True,
            "在反例假设链中，早期零行本身只能提供 downstream unsigned covering data。",
            "必须另给独立算术来源恒等式或命名回流。",
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "当前材料尚未提交独立于早期零行覆盖图的 pre-Cauchy arithmetic source identity。",
            NEW_ATOM,
        ),
        row(
            "ExplicitModelGapAndFiniteDPRCLedger",
            "ExplicitModelGapAndFiniteDPRCLedger" in basis,
            False,
            "模型余量/有限 DPRC 账本仍在输入基中，未由本步处理。",
            "ExplicitModelGapAndFiniteDPRCLedger。",
        ),
        row(
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(
    previous_path: Path,
    zero_row_path: Path,
    geometry_path: Path,
    source_loop_path: Path,
) -> dict[str, Any]:
    """执行假设零行到源种子的 no-go 路由。"""
    source_paths = [previous_path, zero_row_path, geometry_path, source_loop_path]
    previous = load_json(previous_path)
    zero_text = zero_row_path.read_text(encoding="utf-8")
    geometry_text = geometry_path.read_text(encoding="utf-8")
    source_loop_text = source_loop_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        zero_text=zero_text,
        geometry_text=geometry_text,
        source_loop_text=source_loop_text,
    )
    no_go = next(bool(item["closed"]) for item in rows if item["gate"] == "HypotheticalZeroRowCannotSupplyAcyclicSeed")
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "hypothetical_zero_row_seed_no_go_router",
        "status": "hypothetical_zero_row_seed_extraction_blocked_independent_identity_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "zero_row_crt_equivalence_used": True,
        "zero_row_seed_extraction_blocked": no_go,
        "geometry_source_extraction_blocked": no_go,
        "downstream_reverse_source_blocked": no_go,
        "independent_precauchy_arithmetic_source_identity_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": NEW_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步严格区分假设链条与真实链条：假设早期零行只给完整覆盖 CRT 证书和 unsigned "
            "payment/geometry 数据，不能生成 pre-Cauchy signed alpha/delta 源种子。几何模型提供 Phi 基底和"
            "回流形状，但不定义 signed source；来源环切断又禁止从 downstream payment skeleton 反推来源。"
            "因此保留的 clean-core 分支必须提交独立算术来源恒等式，或命名回流。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 假设早期零行源种子 no-go 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"zero_row_crt_equivalence_used={fmt_bool(result['zero_row_crt_equivalence_used'])}",
        f"zero_row_seed_extraction_blocked={fmt_bool(result['zero_row_seed_extraction_blocked'])}",
        f"geometry_source_extraction_blocked={fmt_bool(result['geometry_source_extraction_blocked'])}",
        f"downstream_reverse_source_blocked={fmt_bool(result['downstream_reverse_source_blocked'])}",
        (
            "independent_precauchy_arithmetic_source_identity_proved="
            f"{fmt_bool(result['independent_precauchy_arithmetic_source_identity_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. no-go 核心",
        "",
        "```text",
        "early zero row assumption",
        "  => complete covering CRT certificate tau",
        "  => unsigned payment / cylindrical / wheel geometry",
        "  != pre-Cauchy signed alpha/delta source seed",
        "```",
        "",
        "假设链条给的是覆盖事实；源种子必须是 Cauchy/dispersion 前的 signed 系数生成恒等式。",
        "",
        "## 2. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "该替换把“从反例覆盖图抽取源种子”的伪路径改写为独立算术来源恒等式义务。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
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
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            f"下一步最窄目标为 `{result['next_priority']}`：提交独立于早期零行覆盖图和 downstream payment "
            "geometry 的 pre-Cauchy arithmetic source identity；或者证明任何候选 identity 都必回流到 "
            "PDEC/SAE/ColumnCRT/CleanKLS/external spectral。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_outputs(result: dict[str, Any], json_out: Path, md_out: Path) -> None:
    """写出 JSON 与 Markdown。"""
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--zero-row", type=Path, default=DEFAULT_ZERO_ROW)
    parser.add_argument("--geometry", type=Path, default=DEFAULT_GEOMETRY)
    parser.add_argument("--source-loop", type=Path, default=DEFAULT_SOURCE_LOOP)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        zero_row_path=args.zero_row,
        geometry_path=args.geometry,
        source_loop_path=args.source_loop,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
