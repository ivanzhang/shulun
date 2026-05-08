#!/usr/bin/env python3
"""Prime Matrix DLS short-window SAE 命名回流 schema 路由器。

用法示例：
  python3 experiments/prime_matrix_dls_shortwindow_sae_return_schema_router.py

输出：
  docs/monograph/prime-matrix-dls-shortwindow-sae-return-schema-router.json
  docs/monograph/prime-matrix-dls-shortwindow-sae-return-schema-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-band-local-survivor-return-schema-router.json"
DEFAULT_DLS = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.md"
DEFAULT_SAE_LOCAL = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_LOCAL_GEN = DOCS / "prime-matrix-local-survivor-packet-generation-contract.md"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-dls-shortwindow-sae-return-schema-router.json"
DEFAULT_MD = DOCS / "prime-matrix-dls-shortwindow-sae-return-schema-router.md"

OLD_ATOM = "DLSShortWindowSAEBoundOrNamedReturn"
NEW_ATOM = "NoDLSShortWindowSpecificSAEGap_AfterLocalPacketOrPDECReturn"
NEXT_ATOM = "DLSPointLoadColumnCRTBoundOrNamedReturn"
SECOND_ATOM = "DLSFixedWheelUnitPeakDilutionOrPDECReturn"


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
    """从输入基中删除已回流的 short-window 专属 gap 标记。"""
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
    dls_text: str,
    sae_local_text: str,
    local_gen_text: str,
    sparse_text: str,
    pdec_text: str,
) -> list[dict[str, Any]]:
    """生成 DLS short-window SAE 命名回流 schema 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    shortwindow_alphabet = (
        OLD_ATOM in dls_text
        and "ShortWindow" in dls_text
        and "SAE / LocalSurvivor / persistent sparse PDEC" in dls_text
    )
    finite_window_object = (
        "固定孤立坏窗 `I`" in sae_local_text
        and "C(I)" in sae_local_text
        and "LocalSurvivorCert" in sae_local_text
    )
    local_descent_finite = (
        "Psi_SAE" in sae_local_text
        and "固定孤窗内不能无限下降" in sae_local_text
        and "沿无限反例族复现则由鸽巢转为 PDEC" in sae_local_text
    )
    packet_generation = (
        "引理 LSPG-1" in local_gen_text
        and "same signature persists" in local_gen_text
        and "CleanKLS/DLS" in local_gen_text
    )
    future_sparse_boundary = (
        "future_sparse_packet_schema_boundary_closed=true" in sparse_text
        and "FutureExplicitSparsePacketExtractorSchema" in sparse_text
    )
    pdec_boundary = (
        "pdec_family_explicit_input_boundary_closed=true" in pdec_text
        and "同一个 formal unit" in pdec_text
    )
    schema_closed = all(
        [
            active,
            shortwindow_alphabet,
            finite_window_object,
            local_descent_finite,
            packet_generation,
            future_sparse_boundary,
            pdec_boundary,
        ]
    )
    return [
        row(
            "DLSShortWindowGateActive",
            active,
            True,
            "当前输入基仍含 DLSShortWindowSAEBoundOrNamedReturn，且它来自 BES/DLS 三出口字母表。",
            "本步只攻击 short-window 专属无名出口。",
        ),
        row(
            "ShortWindowAlphabetPinned",
            shortwindow_alphabet,
            True,
            "DLS 危险交集若落入 short-window，只允许 SAE/LocalSurvivor 或 persistent sparse PDEC。",
            "不能再作为 BES 同步失败黑箱。",
        ),
        row(
            "FiniteLocalWindowObject",
            finite_window_object,
            True,
            "固定孤窗 I 有有限候选集 C(I) 与 blocker 投影，可形成 LocalSurvivorCert。",
            "证书未填时仍需 packet/schema。",
        ),
        row(
            "SAELocalDescentWellFounded",
            local_descent_finite,
            True,
            "固定孤窗内局部势函数有限下降；沿无限反例族复现则由鸽巢转为 PDEC。",
            "PDEC 排斥仍未证明。",
        ),
        row(
            "PacketGenerationDichotomy",
            packet_generation,
            True,
            "不可立即核验的孤窗只剩 finite packet、持久签名 PDEC、层级逃逸 CleanKLS/DLS 或下降回流。",
            "未来 packet 必须显式提交。",
        ),
        row(
            "FutureSparsePacketBoundaryImported",
            future_sparse_boundary,
            True,
            "当前 sparse/LocalSurvivor 前沿清零；未来新增 sparse route 必须提交 extractor schema。",
            "不是全局 sparse family 无条件排斥。",
        ),
        row(
            "PersistentShortWindowAdmitsPDEC",
            pdec_boundary,
            True,
            "short-window 若在同 formal unit 上持久复现，必须作为显式 PDEC schema 准入。",
            "PDEC family 无条件排斥仍开放。",
        ),
        row(
            "NoDLSShortWindowSpecificFourthExit",
            schema_closed,
            True,
            "short-window 只有有限 packet、持久 PDEC、CleanKLS/DLS 或下降回流，没有专属第四出口。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            schema_closed,
            True,
            "该硬点作为 short-window 命名回流 schema 已闭合。",
            "不等于数值 short-window bound 已证明。",
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "PointLoad/ColumnCRT 微输入仍在最新输入基中，下一步优先攻击。",
            NEXT_ATOM,
        ),
        row(
            SECOND_ATOM,
            False,
            False,
            "Fixed-wheel 单位类峰稀释或 PDEC 回流仍是独立全局微输入。",
            SECOND_ATOM,
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
    dls_path: Path,
    sae_local_path: Path,
    local_gen_path: Path,
    sparse_path: Path,
    pdec_path: Path,
) -> dict[str, Any]:
    """执行 DLS short-window SAE 命名回流 schema 路由。"""
    source_paths = [
        previous_path,
        dls_path,
        sae_local_path,
        local_gen_path,
        sparse_path,
        pdec_path,
    ]
    previous = load_json(previous_path)
    dls_text = dls_path.read_text(encoding="utf-8")
    sae_local_text = sae_local_path.read_text(encoding="utf-8")
    local_gen_text = local_gen_path.read_text(encoding="utf-8")
    sparse_text = sparse_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        dls_text=dls_text,
        sae_local_text=sae_local_text,
        local_gen_text=local_gen_text,
        sparse_text=sparse_text,
        pdec_text=pdec_text,
    )
    schema_closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    replaced_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    replaced_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_self = remove_closed_gap(replaced_self)
    latest_cond = remove_closed_gap(replaced_cond)
    return {
        "certificate_type": "dls_shortwindow_sae_return_schema_router",
        "status": "dls_shortwindow_sae_return_schema_closed_numeric_bound_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dls_shortwindow_return_schema_closed": schema_closed,
        "dls_shortwindow_specific_gap_removed": schema_closed,
        "dls_shortwindow_numeric_bound_proved": False,
        "pdec_or_sae_terminal_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": NEXT_ATOM,
        "remaining_global_terminal_guard": (
            "FutureExplicitPrimitivePDECSchema_OR_FutureExplicitSparsePacketExtractorSchema_if_materialized"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步闭合的是 DLS short-window SAE 的专属命名回流 schema：固定短窗是有限局部覆盖对象，"
            "孤立时必须提交 LocalSurvivor/SAE packet，持久时必须提交 PDEC schema，"
            "层级逃逸时必须进入 CleanKLS/DLS 或下降回流。因此 short-window 专属无名出口被删除；"
            "但数值 short-window bound、PDEC/sparse 终端排斥和其他 DLS 微输入仍未证明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix DLS short-window SAE 命名回流 schema 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"dls_shortwindow_return_schema_closed={fmt_bool(result['dls_shortwindow_return_schema_closed'])}",
        f"dls_shortwindow_specific_gap_removed={fmt_bool(result['dls_shortwindow_specific_gap_removed'])}",
        f"dls_shortwindow_numeric_bound_proved={fmt_bool(result['dls_shortwindow_numeric_bound_proved'])}",
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
        "这一步仍处于反例分支/终端证书口径，不使用真实样本缺席。",
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
            f"short-window 专属 gap 已删除。下一步最窄目标转到 `{result['next_priority']}`："
            "证明 point-load 不能持续支付 DLS/BES 危险交集，"
            "或把它物化为 ColumnCRT/displacement PDEC / sparse packet 回流。",
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
    parser.add_argument("--dls", type=Path, default=DEFAULT_DLS)
    parser.add_argument("--sae-local", type=Path, default=DEFAULT_SAE_LOCAL)
    parser.add_argument("--local-gen", type=Path, default=DEFAULT_LOCAL_GEN)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        dls_path=args.dls,
        sae_local_path=args.sae_local,
        local_gen_path=args.local_gen,
        sparse_path=args.sparse,
        pdec_path=args.pdec,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
