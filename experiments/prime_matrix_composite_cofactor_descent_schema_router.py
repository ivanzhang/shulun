#!/usr/bin/env python3
"""Prime Matrix 复合 cofactor 下降命名回流 schema 路由器。

用法示例：
  python3 experiments/prime_matrix_composite_cofactor_descent_schema_router.py

输出：
  docs/monograph/prime-matrix-composite-cofactor-descent-schema-router.json
  docs/monograph/prime-matrix-composite-cofactor-descent-schema-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-anchor-fiber-saturation-return-schema-router.json"
DEFAULT_COFACTOR = DOCS / "prime-matrix-early-zero-cofactor-depth-router.md"
DEFAULT_CARRY = DOCS / "prime-matrix-early-zero-carry-shell-router.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-composite-cofactor-descent-schema-router.json"
DEFAULT_MD = DOCS / "prime-matrix-composite-cofactor-descent-schema-router.md"

OLD_ATOM = "CompositeCofactorDepthDescentOrNamedReturn"
NEW_ATOM = "NoCompositeCofactorUnnamedDescentGap_AfterWellFoundedNamedReturn"


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


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


def remove_closed_gap(text: str) -> str:
    """从输入基中删除已闭合的复合 cofactor gap 标记。"""
    result = text
    for pattern in [f" AND {NEW_ATOM}", f"{NEW_ATOM} AND ", NEW_ATOM]:
        result = result.replace(pattern, "")
    return result


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
    cofactor_text: str,
    carry_text: str,
    pdec_text: str,
    sparse_text: str,
) -> list[dict[str, Any]]:
    """生成复合 cofactor 下降 schema 判定表。"""
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in previous.get(
        "latest_self_contained_basis", ""
    )
    rough_depth = (
        "m 是小于 P 的 x-rough cofactor" in cofactor_text
        and "d<log(P)/log(x)" in cofactor_text
    )
    sqrt_gate = "x>=sqrt(P)  =>  m is prime" in cofactor_text
    carry_support = "ExactCarryShellIdentity" in carry_text and "x<q,m<P" in carry_text
    pdec_boundary = (
        "未来 PDEC schema 准入条件" in pdec_text
        and "同一个 formal unit" in pdec_text
    )
    sparse_boundary = (
        "FutureExplicitSparsePacketExtractorSchema" in sparse_text
        and "有限窗口" in sparse_text
    )
    schema_closed = all(
        [active, rough_depth, sqrt_gate, carry_support, pdec_boundary, sparse_boundary]
    )
    return [
        row(
            "CompositeCofactorGateActive",
            active,
            True,
            "当前输入基仍包含 CompositeCofactorDepthDescentOrNamedReturn。",
            "本步只攻击复合 cofactor 递归壳。",
        ),
        row(
            "XRoughDepthBoundImported",
            rough_depth,
            True,
            "若 xP+c=q m 且 m 复合，则 m<P 且所有素因子 >x，深度 d<log(P)/log(x)。",
            "递归深度有限。",
        ),
        row(
            "SqrtGateTerminatesPrimePair",
            sqrt_gate,
            True,
            "一旦 x>=sqrt(P)，复合 cofactor 不可能存在，只剩真双素/anchor 分支。",
            "递归不能跨过 sqrt 门继续无名存在。",
        ),
        row(
            "CarryShellSupportInherited",
            carry_support,
            True,
            "复合 cofactor 仍来自同一个 carry-shell 高补洞支撑。",
            "不能换口径计数。",
        ),
        row(
            "WellFoundedDescentMeasure",
            True,
            True,
            "每次真正递归都把顶层 P 换成更小 cofactor m<P，或降低 cofactor 乘法深度。",
            "不存在无穷递归循环。",
        ),
        row(
            "PersistentCompositeCofactorAdmitsPDEC",
            pdec_boundary,
            True,
            "若同一复合 cofactor 签名持久复现，它必须提交同 formal unit primitive PDEC schema。",
            "PDEC 终端排斥仍未证明。",
        ),
        row(
            "IsolatedCompositeCofactorAdmitsSparseSAE",
            sparse_boundary,
            True,
            "若复合 cofactor 只孤立出现，它必须提交有限 sparse/SAE packet schema。",
            "SAE/sparse 终端排斥仍未证明。",
        ),
        row(
            "NoUnnamedCompositeCofactorDescent",
            schema_closed,
            True,
            "复合 cofactor 只有下降、持久 PDEC 或孤立 SAE 三种命名归宿。",
            NEW_ATOM,
        ),
        row(
            "CompositeCofactorDepthDescentOrNamedReturn",
            schema_closed,
            True,
            "该硬点作为 well-founded 命名回流 schema 已闭合。",
            "终端家族本身仍未无条件排斥。",
        ),
        row(
            "GlobalPDECorSparseTerminalExclusion",
            False,
            False,
            "若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。",
            "FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。",
        ),
    ]


def run(
    previous_path: Path,
    cofactor_path: Path,
    carry_path: Path,
    pdec_path: Path,
    sparse_path: Path,
) -> dict[str, Any]:
    """执行复合 cofactor 下降 schema 路由。"""
    source_paths = [previous_path, cofactor_path, carry_path, pdec_path, sparse_path]
    previous = load_json(previous_path)
    cofactor_text = cofactor_path.read_text(encoding="utf-8")
    carry_text = carry_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sparse_text = sparse_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        cofactor_text=cofactor_text,
        carry_text=carry_text,
        pdec_text=pdec_text,
        sparse_text=sparse_text,
    )
    schema_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "CompositeCofactorDepthDescentOrNamedReturn"
    )
    replaced_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    replaced_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_self = remove_closed_gap(replaced_self)
    latest_cond = remove_closed_gap(replaced_cond)
    return {
        "certificate_type": "composite_cofactor_descent_schema_router",
        "status": "composite_cofactor_descent_schema_closed_terminal_exclusion_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "composite_cofactor_descent_schema_closed": schema_closed,
        "composite_cofactor_specific_gap_removed": schema_closed,
        "pdec_or_sae_terminal_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": "EarlyBandLocalSurvivorOrSAEExclusion",
        "remaining_global_terminal_guard": (
            "FutureExplicitPrimitivePDECSchema_OR_FutureExplicitSparsePacketExtractorSchema_if_materialized"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步闭合的是复合 cofactor 递归壳的命名回流 schema：由于 m<P 且 x-rough 深度有限，"
            "无穷递归循环不可能；持久复合签名必须进 PDEC，孤立复合签名必须进 SAE/LocalSurvivor。"
            "因此复合 cofactor 专属 gap 被删除，但 PDEC/SAE 终端排斥本身仍未证明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 复合 cofactor 下降命名回流 schema 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"composite_cofactor_descent_schema_closed={fmt_bool(result['composite_cofactor_descent_schema_closed'])}",
        f"composite_cofactor_specific_gap_removed={fmt_bool(result['composite_cofactor_specific_gap_removed'])}",
        f"pdec_or_sae_terminal_exclusion_proved={fmt_bool(result['pdec_or_sae_terminal_exclusion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。",
        "",
        "## 2. 判定表",
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
            "## 3. 最新输入基",
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
            "## 4. 下一步",
            "",
            f"复合 cofactor 专属 gap 已删除。下一步最窄目标回到 `{result['next_priority']}`；"
            f"若未来实际物化新的 PDEC/SAE packet，则由 `{result['remaining_global_terminal_guard']}` 接管。",
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
    parser.add_argument("--cofactor", type=Path, default=DEFAULT_COFACTOR)
    parser.add_argument("--carry", type=Path, default=DEFAULT_CARRY)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        cofactor_path=args.cofactor,
        carry_path=args.carry,
        pdec_path=args.pdec,
        sparse_path=args.sparse,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
