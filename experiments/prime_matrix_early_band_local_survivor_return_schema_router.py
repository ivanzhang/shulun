#!/usr/bin/env python3
"""Prime Matrix early-band LocalSurvivor/SAE 命名回流 schema 路由器。

用法示例：
  python3 experiments/prime_matrix_early_band_local_survivor_return_schema_router.py

输出：
  docs/monograph/prime-matrix-early-band-local-survivor-return-schema-router.json
  docs/monograph/prime-matrix-early-band-local-survivor-return-schema-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-composite-cofactor-descent-schema-router.json"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_LOCAL = DOCS / "prime-matrix-local-survivor-packet-generation-contract.md"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_DLS = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-early-band-local-survivor-return-schema-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-band-local-survivor-return-schema-router.md"

OLD_ATOM = "EarlyBandLocalSurvivorOrSAEExclusion"
NEW_ATOM = "NoEarlyBandSpecificLocalSurvivorSAEGap_AfterNamedReturn"
NEXT_ATOM = "DLSShortWindowSAEBoundOrNamedReturn"


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
    """从输入基中删除已回流的 early-band 专属 gap 标记。"""
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
    sae_text: str,
    local_text: str,
    sparse_text: str,
    pdec_text: str,
    dls_text: str,
) -> list[dict[str, Any]]:
    """生成 early-band LocalSurvivor/SAE 命名回流 schema 判定表。"""
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in previous.get(
        "latest_self_contained_basis", ""
    )
    early_branch_guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    sae_absorbed = (
        "SAE 不是独立终端族" in sae_text
        and "LocalSurvivor packet" in sae_text
        and "PDEC" in sae_text
    )
    packet_generation = (
        "引理 LSPG-1" in local_text
        and "same signature persists" in local_text
        and "CleanKLS/DLS" in local_text
    )
    future_sparse_boundary = (
        "future_sparse_packet_schema_boundary_closed=true" in sparse_text
        and "FutureExplicitSparsePacketExtractorSchema" in sparse_text
        and "NoAdditionalUnnamedSparseEntry" in sparse_text
    )
    pdec_boundary = (
        "未来 PDEC schema 准入条件" in pdec_text
        and "同一个 formal unit" in pdec_text
    )
    dls_shortwindow_kept = (
        NEXT_ATOM in previous.get("latest_self_contained_basis", "")
        and NEXT_ATOM in dls_text
        and "ShortWindow" in dls_text
    )
    schema_closed = all(
        [
            active,
            early_branch_guard,
            sae_absorbed,
            packet_generation,
            future_sparse_boundary,
            pdec_boundary,
            dls_shortwindow_kept,
        ]
    )
    return [
        row(
            "EarlyBandLocalSurvivorGateActive",
            active,
            True,
            "当前输入基仍含 EarlyBandLocalSurvivorOrSAEExclusion，且它来自早期零行反例分支。",
            "本步只攻击 early-band 专属无名出口。",
        ),
        row(
            "EarlyZeroCounterexampleBranchGuard",
            early_branch_guard,
            True,
            "沿用 Assume EarlyZeroRowWithinP；不使用真实样本缺席，也不宣布无条件闭合。",
            "保持反例分支口径。",
        ),
        row(
            "SAEIndependentTerminalAbsorbed",
            sae_absorbed,
            True,
            "SAE 已不是独立终端，只能成为 LocalSurvivor packet、持久 PDEC 或 CleanKLS/DLS 回流。",
            "终端排斥本身仍未证明。",
        ),
        row(
            "LocalSurvivorPacketGenerationDichotomy",
            packet_generation,
            True,
            "孤窗若能抽取就是有限 packet；若同签名持久复现则进 PDEC；若层级逃逸则进 CleanKLS/DLS。",
            "未来新增 packet 仍需提交 schema。",
        ),
        row(
            "FutureSparsePacketBoundaryImported",
            future_sparse_boundary,
            True,
            "当前 sparse/LocalSurvivor 前沿清零；未来新增 sparse 路线必须带 extractor schema。",
            "不是全局 sparse family 无条件排斥。",
        ),
        row(
            "PersistentEarlyBandSignatureAdmitsPDEC",
            pdec_boundary,
            True,
            "若 early-band 局部签名在 formal 反例族中持久复现，必须提交同 formal unit PDEC schema。",
            "PDEC 终端家族仍开放。",
        ),
        row(
            "ShortWindowGlobalInputPreserved",
            dls_shortwindow_kept,
            True,
            "early-band 孤窗属于 short-window/SAE 字母表；全局 DLSShortWindow 微输入继续保留。",
            NEXT_ATOM,
        ),
        row(
            "NoEarlyBandSpecificFourthExit",
            schema_closed,
            True,
            "early-band LocalSurvivor/SAE 没有专属第四出口：孤立进 packet，持久进 PDEC，升层进 DLS。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            schema_closed,
            True,
            "该硬点作为 early-band 专属命名回流 schema 已闭合。",
            "不等于全局 short-window/SAE 微输入已证明。",
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "全局 short-window SAE bound 或命名回流仍需证明；本步只是删掉 early-band 专属 gap。",
            NEXT_ATOM,
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
    sae_path: Path,
    local_path: Path,
    sparse_path: Path,
    pdec_path: Path,
    dls_path: Path,
) -> dict[str, Any]:
    """执行 early-band LocalSurvivor/SAE 命名回流 schema 路由。"""
    source_paths = [previous_path, sae_path, local_path, sparse_path, pdec_path, dls_path]
    previous = load_json(previous_path)
    sae_text = sae_path.read_text(encoding="utf-8")
    local_text = local_path.read_text(encoding="utf-8")
    sparse_text = sparse_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    dls_text = dls_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        sae_text=sae_text,
        local_text=local_text,
        sparse_text=sparse_text,
        pdec_text=pdec_text,
        dls_text=dls_text,
    )
    schema_closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    replaced_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    replaced_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_self = remove_closed_gap(replaced_self)
    latest_cond = remove_closed_gap(replaced_cond)
    return {
        "certificate_type": "early_band_local_survivor_return_schema_router",
        "status": "early_band_local_survivor_schema_closed_global_shortwindow_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "early_band_local_survivor_return_schema_closed": schema_closed,
        "early_band_specific_gap_removed": schema_closed,
        "sae_independent_terminal_absorbed": schema_closed,
        "pdec_or_sae_terminal_exclusion_proved": False,
        "dls_shortwindow_global_input_proved": False,
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
            "本步闭合的是 early-band LocalSurvivor/SAE 的专属无名出口：在早期零行反例分支中，"
            "孤立 early-band 窗口必须物化为有限 LocalSurvivor/SAE packet，持久同签名必须进入 PDEC，"
            "层级逃逸必须进入 CleanKLS/DLS。因此 early-band 专属 gap 被删除；"
            "但全局 DLSShortWindowSAEBoundOrNamedReturn 与 PDEC/sparse 终端排斥仍未证明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix early-band LocalSurvivor/SAE 命名回流 schema 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        (
            "early_band_local_survivor_return_schema_closed="
            f"{fmt_bool(result['early_band_local_survivor_return_schema_closed'])}"
        ),
        f"early_band_specific_gap_removed={fmt_bool(result['early_band_specific_gap_removed'])}",
        f"pdec_or_sae_terminal_exclusion_proved={fmt_bool(result['pdec_or_sae_terminal_exclusion_proved'])}",
        f"dls_shortwindow_global_input_proved={fmt_bool(result['dls_shortwindow_global_input_proved'])}",
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
            f"early-band 专属 gap 已删除。下一步最窄目标转到全局 `{result['next_priority']}`："
            "证明 short-window SAE 不能持续支付 DLS/BES 危险交集，"
            "或把它物化为有限 packet / persistent PDEC schema。",
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
    parser.add_argument("--sae", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--local", type=Path, default=DEFAULT_LOCAL)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--dls", type=Path, default=DEFAULT_DLS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        sae_path=args.sae,
        local_path=args.local,
        sparse_path=args.sparse,
        pdec_path=args.pdec,
        dls_path=args.dls,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
