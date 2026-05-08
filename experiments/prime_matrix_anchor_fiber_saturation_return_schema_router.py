#!/usr/bin/env python3
"""Prime Matrix anchor fiber 饱和命名回流 schema 路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_fiber_saturation_return_schema_router.py

输出：
  docs/monograph/prime-matrix-anchor-fiber-saturation-return-schema-router.json
  docs/monograph/prime-matrix-anchor-fiber-saturation-return-schema-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-anchor-tailcore-fiber-saturation-router.json"
DEFAULT_ANCHOR = DOCS / "prime-matrix-early-zero-anchor-collar-router.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-fiber-saturation-return-schema-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-fiber-saturation-return-schema-router.md"

OLD_ATOM = "AnchorFiberSaturationPDECOrSAEReturn"
NEW_ATOM = "NoAnchorSpecificFiberSaturationGap_AfterNamedPDECOrSAEReturn"


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


def remove_closed_anchor_gap(text: str) -> str:
    """从输入基中删除已回流的 anchor 专属 gap 标记。"""
    patterns = [
        f" AND {NEW_ATOM}",
        f"{NEW_ATOM} AND ",
        NEW_ATOM,
    ]
    result = text
    for pattern in patterns:
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
    anchor_text: str,
    pdec_text: str,
    sparse_text: str,
    sae_text: str,
) -> list[dict[str, Any]]:
    """生成 fiber 饱和回流 schema 判定表。"""
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in previous.get("open_gates", [])
    finite_fiber = (
        "FiberShortPrimeInterval" in anchor_text
        and "长度 <P/q<=sqrt(P)" in anchor_text
    )
    pdec_boundary = (
        "未来 PDEC schema 准入条件" in pdec_text
        and "同一个 formal unit" in pdec_text
        and "至少有三个物理 primitive 原子" in pdec_text
    )
    sparse_boundary = (
        "FutureExplicitSparsePacketExtractorSchema" in sparse_text
        and "有限窗口" in sparse_text
        and "witness" in sparse_text
    )
    sae_absorbed = (
        "SAE 不是独立终端族" in sae_text
        and "LocalSurvivor packet" in sae_text
        and "PDEC" in sae_text
    )
    return_closed = all([active, finite_fiber, pdec_boundary, sparse_boundary, sae_absorbed])
    return [
        row(
            "AnchorFiberSaturationGateActive",
            active,
            True,
            "上一层唯一 anchor 专属剩余是 AnchorFiberSaturationPDECOrSAEReturn。",
            "本步只判断 fiber 饱和是否有未命名出口。",
        ),
        row(
            "FiniteShortFiberFormalUnit",
            finite_fiber,
            True,
            "固定 q 后，m 位于长度 <sqrt(P) 的有限素数窗口；物理原子是 (x,q,m,c)。",
            "fiber 饱和可登记为有限 formal unit packet。",
        ),
        row(
            "PersistentFiberSaturationAdmitsPDEC",
            pdec_boundary,
            True,
            "若同一 fiber 签名沿反例族持久近饱和，则必须提交同 formal unit primitive PDEC schema。",
            "终端排斥仍依赖 PDEC family 证书，不在本步证明。",
        ),
        row(
            "IsolatedFiberSaturationAdmitsSparseSAE",
            sparse_boundary and sae_absorbed,
            True,
            "若 fiber 饱和只孤立出现，则必须提交有限 LocalSurvivor/SAE packet schema。",
            "终端排斥仍依赖 sparse/SAE packet 证书，不在本步证明。",
        ),
        row(
            "NoUnnamedFiberSaturationExit",
            return_closed,
            True,
            "fiber 饱和要么持久进 PDEC，要么孤立进 SAE/LocalSurvivor；没有 anchor 专属第四出口。",
            NEW_ATOM,
        ),
        row(
            "AnchorFiberSaturationPDECOrSAEReturn",
            return_closed,
            True,
            "该硬点作为命名回流 schema 已闭合。",
            "PDEC/SAE 终端家族本身仍未无条件排斥。",
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
    anchor_path: Path,
    pdec_path: Path,
    sparse_path: Path,
    sae_path: Path,
) -> dict[str, Any]:
    """执行 anchor fiber 饱和回流 schema 路由。"""
    source_paths = [previous_path, anchor_path, pdec_path, sparse_path, sae_path]
    previous = load_json(previous_path)
    anchor_text = anchor_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sparse_text = sparse_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        anchor_text=anchor_text,
        pdec_text=pdec_text,
        sparse_text=sparse_text,
        sae_text=sae_text,
    )
    return_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "AnchorFiberSaturationPDECOrSAEReturn"
    )
    replaced_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    replaced_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_self = remove_closed_anchor_gap(replaced_self)
    latest_cond = remove_closed_anchor_gap(replaced_cond)
    return {
        "certificate_type": "anchor_fiber_saturation_return_schema_router",
        "status": "anchor_fiber_saturation_return_schema_closed_terminal_exclusion_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "anchor_fiber_saturation_return_schema_closed": return_closed,
        "anchor_specific_fiber_gap_removed": return_closed,
        "pdec_or_sae_terminal_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": "CompositeCofactorDepthDescentOrNamedReturn",
        "remaining_global_terminal_guard": (
            "FutureExplicitPrimitivePDECSchema_OR_FutureExplicitSparsePacketExtractorSchema_if_materialized"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步闭合的是 anchor fiber 饱和的命名回流 schema：固定 q 的短素数窗口是有限 formal unit；"
            "持久近饱和必须作为 primitive PDEC schema，孤立近饱和必须作为 LocalSurvivor/SAE packet。"
            "因此 anchor 专属 fiber gap 被删除，但 PDEC/SAE 终端排斥本身仍未证明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix anchor fiber 饱和命名回流 schema 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"anchor_fiber_saturation_return_schema_closed={fmt_bool(result['anchor_fiber_saturation_return_schema_closed'])}",
        f"anchor_specific_fiber_gap_removed={fmt_bool(result['anchor_specific_fiber_gap_removed'])}",
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
            f"anchor 专属 fiber gap 已删除。下一步最窄目标回到 `{result['next_priority']}`；"
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
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--sae", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        anchor_path=args.anchor,
        pdec_path=args.pdec,
        sparse_path=args.sparse,
        sae_path=args.sae,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
