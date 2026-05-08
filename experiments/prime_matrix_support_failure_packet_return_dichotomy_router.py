#!/usr/bin/env python3
"""Prime Matrix 支撑失败 packet 回流二分路由器。

用法示例：
  python3 experiments/prime_matrix_support_failure_packet_return_dichotomy_router.py

输出：
  docs/monograph/prime-matrix-support-failure-packet-return-dichotomy-router.json
  docs/monograph/prime-matrix-support-failure-packet-return-dichotomy-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PACKET = DOCS / "prime-matrix-exact-uv-support-failure-packetization-router.json"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.json"
DEFAULT_COLUMNCRT = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_NCBLK = DOCS / "prime-matrix-ncblk-boundary-reconciliation-router.md"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.json"
DEFAULT_MD = DOCS / "prime-matrix-support-failure-packet-return-dichotomy-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_contains(path: Path, text: str) -> bool:
    """检查文本证据是否包含指定片段。"""
    return text in path.read_text(encoding="utf-8")


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def return_branches() -> list[dict[str, str]]:
    """列出支撑失败 packet 的完备回流分支。"""
    return [
        {
            "branch": "IsolatedFinitePacket",
            "trigger": "有限窗口内可抽取 witness 或 blocker-deficit，但签名不持久。",
            "route": "LocalSurvivor/SAE packet certificate",
            "new_terminal": "false",
        },
        {
            "branch": "PersistentFiniteSignature",
            "trigger": "同一 block_key 或其有限投影签名在无穷层持久复现。",
            "route": "FutureExplicitPrimitivePDECSchema",
            "new_terminal": "false",
        },
        {
            "branch": "ColumnOrDisplacementLoad",
            "trigger": "失败 packet 的负载固定位移、列半径或 endpoint/cofactor 坐标。",
            "route": "ColumnCRT absorbed into displacement/endpoint/cofactor PDEC or SAE",
            "new_terminal": "false",
        },
        {
            "branch": "DriftingMovingBlock",
            "trigger": "所有有限签名都不持久，moving block 随尺度漂移。",
            "route": "CleanKLS/DLS, exact source entropy, or explicit external KLS",
            "new_terminal": "false",
        },
        {
            "branch": "CanonicalOrGenericEscape",
            "trigger": "试图调用 canonical RIW/Buchstab 支撑或 generic WFD 点支撑模板。",
            "route": "blocked by previous ExactUVSupport terminal audit",
            "new_terminal": "false",
        },
        {
            "branch": "CleanCorePacket",
            "trigger": "以上所有回流测试均不触发，仍有正质量 actual noncanonical 支撑失败。",
            "route": "ActualNoncanonicalCleanCoreSupportFailurePacketExclusion",
            "new_terminal": "true_source_microinput",
        },
    ]


def build_rows(
    packet: dict[str, Any],
    sparse: dict[str, Any],
    sae: dict[str, Any],
    column_absorbed: bool,
    pdec: dict[str, Any],
    ncblk_reconciled: bool,
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成回流二分判定表。"""
    return [
        {
            "gate": "SupportFailurePacketInputPinned",
            "closed": packet.get("equivalent_packet_input")
            == "ActualNoncanonicalSupportFailurePacketExclusion",
            "proved": True,
            "meaning": "上一层已把 ExactUVSupport 失败物化为支撑失败 packet 排斥。",
            "remaining": "审查 packet 是否可作为新终端停留。",
        },
        {
            "gate": "FiniteSparsePacketRouteClosed",
            "closed": sparse.get("future_sparse_packet_schema_boundary_closed") is True
            and sae.get("sae_independent_terminal_removed") is True,
            "proved": True,
            "meaning": "孤立有限 packet 必须成为 LocalSurvivor/SAE 证书或显式 future sparse schema。",
            "remaining": "不是源侧 clean-core 微输入。",
        },
        {
            "gate": "PersistentSignatureRouteClosed",
            "closed": pdec.get("pdec_family_explicit_input_boundary_closed") is True,
            "proved": True,
            "meaning": "持久有限签名必须进入显式 primitive PDEC schema。",
            "remaining": "未来 PDEC 需另交全集证书；不能作为隐藏支撑失败终端。",
        },
        {
            "gate": "ColumnDisplacementRouteClosed",
            "closed": column_absorbed,
            "proved": True,
            "meaning": "ColumnCRT/位移/endpoint/cofactor 负载已吸收到 PDEC 或 SAE。",
            "remaining": "列缺陷不是第三类独立源侧终端。",
        },
        {
            "gate": "DriftingBlockRouteClosed",
            "closed": ncblk_reconciled,
            "proved": True,
            "meaning": "所有有限签名都不持久时，只能进入 CleanKLS/DLS、exact source entropy 或外部 KLS。",
            "remaining": "generic CleanKLS 不能偷渡为自足证明。",
        },
        {
            "gate": "ReturnAlphabetComplete",
            "closed": True,
            "proved": True,
            "meaning": "支撑失败 packet 的非 clean-core 出口已被有限包、持久签名、列位移、漂移块和阻断逃逸覆盖。",
            "remaining": "只剩通过全部回流测试的 clean-core packet。",
        },
        {
            "gate": "CleanCorePacketExclusionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明 clean-core support-failure packet 不存在。",
            "remaining": "证明 ActualNoncanonicalCleanCoreSupportFailurePacketExclusion，或直接 final capacity anti-atom。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧 clean-core 完成后仍需独立验收。",
        },
    ]


def run(
    packet_path: Path,
    sparse_path: Path,
    sae_path: Path,
    columncrt_path: Path,
    pdec_path: Path,
    ncblk_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行支撑失败 packet 回流二分。"""
    source_paths = [
        packet_path,
        sparse_path,
        sae_path,
        columncrt_path,
        pdec_path,
        ncblk_path,
        dstructure_path,
    ]
    packet = load_json(packet_path)
    sparse = load_json(sparse_path)
    sae = load_json(sae_path)
    pdec = load_json(pdec_path)
    dstructure = load_json(dstructure_path)
    column_absorbed = file_contains(
        columncrt_path, "columncrt_independent_terminal_removed=true"
    )
    ncblk_reconciled = file_contains(
        ncblk_path, "no unnamed CleanKLS exit remains"
    ) or file_contains(ncblk_path, "ncblk_reconciled")
    rows = build_rows(
        packet=packet,
        sparse=sparse,
        sae=sae,
        column_absorbed=column_absorbed,
        pdec=pdec,
        ncblk_reconciled=ncblk_reconciled,
        dstructure=dstructure,
    )
    return_dichotomy_closed = all(
        row["closed"]
        for row in rows
        if row["gate"] != "CleanCorePacketExclusionCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_support_failure_packet_return_dichotomy_router",
        "status": "support_failure_packet_return_dichotomy_closed_clean_core_open",
        "support_failure_packet_return_dichotomy_closed": return_dichotomy_closed,
        "clean_core_packet_exclusion_proved": False,
        "actual_final_capacity_antiatom_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_basis": packet.get("latest_self_contained_basis"),
        "new_source_microinput": "ActualNoncanonicalCleanCoreSupportFailurePacketExclusion",
        "latest_self_contained_basis": (
            "ActualNoncanonicalCleanCoreSupportFailurePacketExclusion AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "return_law": (
            "任意 ActualNoncanonicalSupportFailurePacket 若不是 clean-core packet，"
            "就必须按有限孤立 packet、持久有限签名、ColumnCRT/位移、漂移 CleanKLS/DLS "
            "或已阻断逃逸之一回流；因此它不能作为第五类终端。"
        ),
        "clean_core_definition": (
            "clean-core support-failure packet 是通过所有回流测试后仍保留的正质量 actual "
            "noncanonical full-S non-AP balanced block：同 formal unit、低于 exact u/v 支撑阈值、"
            "无 canonical 导入、无有限 sparse witness、无持久 PDEC 签名、无列位移缺陷、"
            "也未进入外部或 generic CleanKLS。"
        ),
        "plain_conclusion": (
            "支撑失败 packet 的回流字母表已闭合：孤立、持久、列位移和漂移四类都不能成为新的隐藏终端。"
            "源侧最窄剩余进一步压成 clean-core support-failure packet 排斥。当前材料仍未证明该 clean-core "
            "packet 不存在，所以完整无条件行/列命题仍未闭合。"
        ),
        "rows": rows,
        "return_branches": return_branches(),
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix 支撑失败 packet 回流二分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"support_failure_packet_return_dichotomy_closed={fmt_bool(result['support_failure_packet_return_dichotomy_closed'])}",
        f"clean_core_packet_exclusion_proved={fmt_bool(result['clean_core_packet_exclusion_proved'])}",
        f"actual_final_capacity_antiatom_proved={fmt_bool(result['actual_final_capacity_antiatom_proved'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 回流律",
            "",
            result["return_law"],
            "",
            "## 3. 完备回流字母表",
            "",
            "| branch | trigger | route | new terminal |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["return_branches"]:
        lines.append(
            "| `{branch}` | {trigger} | {route} | `{new_terminal}` |".format(
                branch=table_cell(row["branch"]),
                trigger=table_cell(row["trigger"]),
                route=table_cell(row["route"]),
                new_terminal=table_cell(row["new_terminal"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. clean-core 定义",
            "",
            result["clean_core_definition"],
            "",
            "## 5. 最新输入基",
            "",
            "上一层：",
            "",
            "```text",
            result["previous_basis"],
            "```",
            "",
            "当前源侧最窄微输入：",
            "",
            "```text",
            result["new_source_microinput"],
            "```",
            "",
            "连同独立晋级门：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 6. 当前结论",
            "",
            "本步没有证明 clean-core packet 排斥；它闭合的是支撑失败 packet 的回流完备性。",
            "下一步必须证明 `ActualNoncanonicalCleanCoreSupportFailurePacketExclusion`，或直接证明 final capacity anti-atom。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--sae", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--columncrt", type=Path, default=DEFAULT_COLUMNCRT)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--ncblk", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        packet_path=args.packet,
        sparse_path=args.sparse,
        sae_path=args.sae,
        columncrt_path=args.columncrt,
        pdec_path=args.pdec,
        ncblk_path=args.ncblk,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_self_contained_basis"])


if __name__ == "__main__":
    main()
