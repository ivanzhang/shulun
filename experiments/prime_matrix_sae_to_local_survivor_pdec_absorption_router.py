#!/usr/bin/env python3
"""把 SAE 独立终端吸收到 LocalSurvivor/PDEC 回流。

用法示例：
  python3 experiments/prime_matrix_sae_to_local_survivor_pdec_absorption_router.py

输出：
  docs/monograph/prime-matrix-sae-to-local-survivor-pdec-absorption-router.json
  docs/monograph/prime-matrix-sae-to-local-survivor-pdec-absorption-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_COLUMNCRT_ABSORB = (
    DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.json"
)
DEFAULT_SAE_REDUCTION = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_MATERIALIZED_LEDGER = (
    DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.json"
)
DEFAULT_EXTRACTOR_COVERAGE = (
    DOCS / "prime-matrix-local-survivor-packet-extractor-coverage.json"
)
DEFAULT_NEW_SPARSE = DOCS / "prime-matrix-new-sparse-entry-admission-audit.json"
DEFAULT_PACKET_CONTRACT = (
    DOCS / "prime-matrix-local-survivor-packet-generation-contract.md"
)
DEFAULT_PERSISTENT_ADMISSION = (
    DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.json"
)
DEFAULT_JSON = (
    DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.json"
)
DEFAULT_MD = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """检查文件是否包含全部关键文本。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造 SAE 吸收审查行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    columncrt_absorb: dict[str, Any],
    sae_reduction_path: Path,
    materialized_ledger: dict[str, Any],
    extractor_coverage: dict[str, Any],
    new_sparse: dict[str, Any],
    packet_contract_path: Path,
    persistent_admission: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 SAE 到 LocalSurvivor/PDEC 的吸收审查表。"""
    terminal_two_family = (
        columncrt_absorb.get("columncrt_independent_terminal_removed") is True
        and any(
            "SAE" in item
            for item in columncrt_absorb.get(
                "independent_terminal_inputs_after_columncrt_absorption", []
            )
        )
    )
    sae_reduction_present = contains_all(
        sae_reduction_path,
        [
            "SAE 不再是独立结构终端",
            "LocalSurvivor certificates",
            "PDEC family",
        ],
    )
    materialized_closed = (
        materialized_ledger.get("closed_subgate")
        == "MaterializedLocalSurvivorPacketsExhausted"
        and materialized_ledger.get("open_materialized_obligation_count") == 0
        and materialized_ledger.get("current_materialized_local_survivor_packets_closed")
        is True
    )
    extractor_closed = (
        extractor_coverage.get("closed_subgate")
        == "KnownLocalSurvivorEntryExtractorsCovered"
        and extractor_coverage.get("known_entry_extractor_coverage_closed") is True
        and extractor_coverage.get("missing_or_open_count") == 0
    )
    no_unnamed_sparse = (
        new_sparse.get("closed_subgate")
        == "NoAdditionalUnnamedLocalSurvivorEntryRoute"
        and new_sparse.get("no_additional_unnamed_local_survivor_entry_route") is True
        and new_sparse.get("missing_admission_count") == 0
    )
    packet_generation_contract = contains_all(
        packet_contract_path,
        [
            "PacketExtractorCompleteness",
            "same signature persists",
            "CleanKLS/DLS",
        ],
    )
    persistent_terminal_boundary = (
        persistent_admission.get("persistent_terminal_admission_boundary_closed") is True
        and persistent_admission.get("current_materialized_persistent_terminal_instances_closed")
        is True
    )

    return [
        row(
            gate="TerminalTwoFamilyRemainderBeforeSAE",
            closed=terminal_two_family,
            evidence="ColumnCRT absorption router",
            meaning="上一轮已经把第一包压成 SAE 与广义 PDEC 两族。",
            remaining="decide whether SAE is genuinely independent",
        ),
        row(
            gate="SAELocalReduction",
            closed=sae_reduction_present,
            evidence="prime-matrix-sae-local-certificate-reduction",
            meaning="孤窗逃逸只能给 LocalSurvivor packet，或因持久/阻塞集中回流 PDEC、下降或 clean。",
            remaining="fill finite packet or route persistent signature",
        ),
        row(
            gate="MaterializedLocalSurvivorPacketsExhausted",
            closed=materialized_closed,
            evidence="local survivor materialized packet ledger",
            meaning="当前已物化的 LocalSurvivor/SAE 包没有开放局部义务。",
            remaining="not a proof for future unaudited sparse packets",
        ),
        row(
            gate="KnownEntryExtractorsCovered",
            closed=extractor_closed,
            evidence="local survivor packet extractor coverage",
            meaning="已知 LocalSurvivor 入口均有脚本或合同 extractor。",
            remaining="new explicit sparse route must bring its own schema",
        ),
        row(
            gate="NoAdditionalUnnamedSparseEntry",
            closed=no_unnamed_sparse,
            evidence="new sparse entry admission audit",
            meaning="当前合同体系内没有额外无名 sparse/LocalSurvivor 入口。",
            remaining="future new route is an explicit new input, not hidden terminal",
        ),
        row(
            gate="PacketGenerationDichotomy",
            closed=packet_generation_contract,
            evidence="local survivor packet generation contract",
            meaning="无法抽取为有限 packet 时，同签名持久化进入 PDEC，层级逃逸进入 CleanKLS/DLS。",
            remaining="PDEC exclusion or noncanonical/external clean input",
        ),
        row(
            gate="PersistentSparseFallbackAdmitted",
            closed=persistent_terminal_boundary,
            evidence="persistent terminal admission router",
            meaning="持久 sparse fallback 不能停在 SAE，必须通过 primitive/non-tautological PDEC 准入边界。",
            remaining="primitive/non-tautological PDEC family",
        ),
    ]


def run(
    columncrt_absorb_path: Path,
    sae_reduction_path: Path,
    materialized_ledger_path: Path,
    extractor_coverage_path: Path,
    new_sparse_path: Path,
    packet_contract_path: Path,
    persistent_admission_path: Path,
) -> dict[str, Any]:
    """运行 SAE 到 LocalSurvivor/PDEC 的吸收路由。"""
    columncrt_absorb = load_json(columncrt_absorb_path)
    materialized_ledger = load_json(materialized_ledger_path)
    extractor_coverage = load_json(extractor_coverage_path)
    new_sparse = load_json(new_sparse_path)
    persistent_admission = load_json(persistent_admission_path)
    rows = build_rows(
        columncrt_absorb=columncrt_absorb,
        sae_reduction_path=sae_reduction_path,
        materialized_ledger=materialized_ledger,
        extractor_coverage=extractor_coverage,
        new_sparse=new_sparse,
        packet_contract_path=packet_contract_path,
        persistent_admission=persistent_admission,
    )
    absorption_closed = all(item["closed"] for item in rows)
    evidence_paths = [
        columncrt_absorb_path,
        sae_reduction_path,
        materialized_ledger_path,
        extractor_coverage_path,
        new_sparse_path,
        packet_contract_path,
        persistent_admission_path,
    ]
    return {
        "certificate_type": "prime_matrix_sae_to_local_survivor_pdec_absorption_router",
        "status": (
            "sae_independent_terminal_absorbed_current_contract_remainder_pdec_plus_future_schema"
            if absorption_closed
            else "sae_absorption_missing_gate"
        ),
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "sae_independent_terminal_removed": absorption_closed,
        "terminal_package_fully_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_package_remainder_after_sae_absorption": [
            "PDEC family：包含 endpoint / displacement / cofactor / primitive / non-tautological 证书",
            "FutureExplicitSparsePacketExtractorSchema：若未来新增真正 sparse 路线，必须同步提交 extractor schema",
        ],
        "rows": rows,
        "absorption_law": (
            "SAE 不是独立终端族。任意 sparse/single-window escape 必须先输出有限 "
            "LocalSurvivor packet，并给出 witness 或 blocker-deficit 数据；否则若有限签名"
            "持久复现，就变成 PDEC/ColumnCRT/TailAnchor/CofactorAnchor；若签名层级逃逸，"
            "就进入 CleanKLS/DLS admission。当前已物化 LocalSurvivor 包已经耗尽，所有已知"
            " sparse 入口都有命名 extractor 或 fallback 路由。因此未来若出现新的 sparse 路线，"
            "它是显式 schema 义务，不是隐藏的第三终端。"
        ),
        "review_conclusion": (
            "SAE 独立终端已吸收到 LocalSurvivor packet 证书、PDEC 持久签名回流和 "
            "CleanKLS/DLS 层级逃逸接口。第一包当前不再有独立 SAE 终端；剩余核心是广义 "
            "PDEC 证书族，以及未来若新增显式 sparse 路线时必须同时提交 extractor schema。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix SAE 到 LocalSurvivor/PDEC 吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 吸收律",
        "",
        result["absorption_law"],
        "",
        "```text",
        f"sae_independent_terminal_removed={fmt_bool(result['sae_independent_terminal_removed'])}",
        f"terminal_package_fully_proved={fmt_bool(result['terminal_package_fully_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 审查表",
        "",
        "| gate | closed | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(["", "## 3. SAE 吸收后的第一包剩余", ""])
    for item in result["terminal_package_remainder_after_sae_absorption"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 4. 判定",
            "",
            "`SAE` 的正确边界不是“所有未来孤窗已直接证明不存在”，而是：它不能作为独立终端。"
            "一旦孤窗可以抽取为有限 packet，就必须给出 LocalSurvivor witness 或覆盖亏损；"
            "一旦同一有限签名持久复现，就回流 PDEC/ColumnCRT/TailAnchor/CofactorAnchor；"
            "一旦签名层级逃逸，就进入 CleanKLS/DLS 或外部输入包。当前已物化 packet 和已知入口"
            "已经清零，所以第一包的结构剩余压到广义 PDEC 证书族和未来显式 sparse schema 义务。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--columncrt-absorb-json", type=Path, default=DEFAULT_COLUMNCRT_ABSORB)
    parser.add_argument("--sae-reduction-md", type=Path, default=DEFAULT_SAE_REDUCTION)
    parser.add_argument("--materialized-json", type=Path, default=DEFAULT_MATERIALIZED_LEDGER)
    parser.add_argument("--extractor-json", type=Path, default=DEFAULT_EXTRACTOR_COVERAGE)
    parser.add_argument("--new-sparse-json", type=Path, default=DEFAULT_NEW_SPARSE)
    parser.add_argument("--packet-contract-md", type=Path, default=DEFAULT_PACKET_CONTRACT)
    parser.add_argument("--persistent-admission-json", type=Path, default=DEFAULT_PERSISTENT_ADMISSION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        columncrt_absorb_path=args.columncrt_absorb_json,
        sae_reduction_path=args.sae_reduction_md,
        materialized_ledger_path=args.materialized_json,
        extractor_coverage_path=args.extractor_json,
        new_sparse_path=args.new_sparse_json,
        packet_contract_path=args.packet_contract_md,
        persistent_admission_path=args.persistent_admission_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["terminal_package_remainder_after_sae_absorption"])


if __name__ == "__main__":
    main()
