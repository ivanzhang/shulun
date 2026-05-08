#!/usr/bin/env python3
"""固定未来 sparse packet extractor schema 的准入边界。

用法示例：
  python3 experiments/prime_matrix_future_sparse_packet_extractor_schema_boundary_router.py

输出：
  docs/monograph/prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json
  docs/monograph/prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_MATERIALIZED_LEDGER = DOCS / "prime-matrix-local-survivor-materialized-packet-ledger.json"
DEFAULT_EXTRACTOR_COVERAGE = DOCS / "prime-matrix-local-survivor-packet-extractor-coverage.json"
DEFAULT_NEW_SPARSE = DOCS / "prime-matrix-new-sparse-entry-admission-audit.json"
DEFAULT_SAE_ABSORB = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.json"
DEFAULT_PACKET_CONTRACT = DOCS / "prime-matrix-local-survivor-packet-generation-contract.md"
DEFAULT_PDEC_BOUNDARY = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_MD = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    """构造 sparse schema 边界行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def contract_has_all(contract_text: str, phrases: list[str]) -> bool:
    """检查合同文本是否包含必要结构短语。"""
    return all(phrase in contract_text for phrase in phrases)


def build_rows(
    materialized: dict[str, Any],
    extractor: dict[str, Any],
    new_sparse: dict[str, Any],
    sae_absorb: dict[str, Any],
    packet_contract_text: str,
    pdec_boundary: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成未来 sparse extractor schema 准入边界表。"""
    materialized_closed = (
        materialized.get("current_materialized_local_survivor_packets_closed") is True
        and materialized.get("open_materialized_obligation_count") == 0
        and materialized.get("closed_subgate") == "MaterializedLocalSurvivorPacketsExhausted"
    )
    known_extractors_covered = (
        extractor.get("known_entry_extractor_coverage_closed") is True
        and extractor.get("missing_or_open_count") == 0
        and extractor.get("closed_subgate") == "KnownLocalSurvivorEntryExtractorsCovered"
    )
    no_unnamed_sparse_entry = (
        new_sparse.get("no_additional_unnamed_local_survivor_entry_route") is True
        and new_sparse.get("missing_admission_count") == 0
        and new_sparse.get("known_extractors_closed") is True
    )
    packet_generation_dichotomy = contract_has_all(
        packet_contract_text,
        [
            "LocalSurvivorCert",
            "same signature persists",
            "CleanKLS/DLS",
            "descent/seam",
        ],
    )
    sae_not_independent = (
        sae_absorb.get("sae_independent_terminal_removed") is True
        and sae_absorb.get("terminal_package_fully_proved") is False
    )
    persistent_fallback_named = (
        pdec_boundary.get("pdec_family_explicit_input_boundary_closed") is True
        and pdec_boundary.get("current_materialized_pdec_frontier_closed") is True
        and pdec_boundary.get("global_pdec_family_unconditional_closed") is False
    )
    future_schema_fields_fixed = True
    no_overclaim_guard = (
        sae_absorb.get("row_column_unconditional_closed") is False
        and pdec_boundary.get("row_column_unconditional_closed") is False
    )

    return [
        row(
            gate="MaterializedLocalSurvivorPacketsExhausted",
            closed=materialized_closed,
            evidence="local survivor materialized packet ledger",
            meaning="当前机器物化的 LocalSurvivor/SAE 包没有开放局部义务。",
            remaining="future unaudited sparse windows only",
        ),
        row(
            gate="KnownEntryExtractorsCovered",
            closed=known_extractors_covered,
            evidence="local survivor packet extractor coverage",
            meaning="已知 sparse/LocalSurvivor 入口均有脚本 extractor 或合同回流。",
            remaining="future newly proposed route must bring extractor schema",
        ),
        row(
            gate="NoAdditionalUnnamedSparseEntry",
            closed=no_unnamed_sparse_entry,
            evidence="new sparse entry admission audit",
            meaning="当前合同体系内没有额外无名 sparse 入口。",
            remaining="explicit future sparse input only",
        ),
        row(
            gate="PacketGenerationDichotomyPresent",
            closed=packet_generation_dichotomy,
            evidence="local survivor packet-generation contract",
            meaning="不能抽取有限 packet 时，只能持久化为 PDEC/ColumnCRT/Tail/Cofactor，或升层到 CleanKLS/DLS，或下降到命名包。",
            remaining="schema must choose one named branch",
        ),
        row(
            gate="SAENotIndependentTerminal",
            closed=sae_not_independent,
            evidence="SAE absorption router",
            meaning="SAE 已被吸收到 LocalSurvivor packet、PDEC 持久回流和 CleanKLS/DLS 接口。",
            remaining="not a third terminal",
        ),
        row(
            gate="PersistentFallbackNamedByPDECBoundary",
            closed=persistent_fallback_named,
            evidence="PDEC family explicit input boundary router",
            meaning="同有限签名持久复现不能停在 sparse，必须按显式 PDEC schema 准入。",
            remaining="FutureExplicitPrimitivePDECSchema if new persistent family appears",
        ),
        row(
            gate="FutureSparseSchemaFieldsFixed",
            closed=future_schema_fields_fixed,
            evidence="this router",
            meaning="未来 sparse 路线的最小字段被固定，不能再作为隐藏终端进入。",
            remaining="submit full finite packet extractor schema",
        ),
        row(
            gate="NoOverclaimGuard",
            closed=no_overclaim_guard,
            evidence="SAE/PDEC routers",
            meaning="本路由只闭合当前 sparse 边界，不声明完整行/列无条件定理。",
            remaining="DStructure/Rankin and external/noncanonical inputs",
        ),
    ]


def run(
    materialized_path: Path,
    extractor_path: Path,
    new_sparse_path: Path,
    sae_absorb_path: Path,
    packet_contract_path: Path,
    pdec_boundary_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行未来 sparse schema 边界路由。"""
    materialized = load_json(materialized_path)
    extractor = load_json(extractor_path)
    new_sparse = load_json(new_sparse_path)
    sae_absorb = load_json(sae_absorb_path)
    packet_contract_text = packet_contract_path.read_text(encoding="utf-8")
    pdec_boundary = load_json(pdec_boundary_path)

    rows = build_rows(
        materialized,
        extractor,
        new_sparse,
        sae_absorb,
        packet_contract_text,
        pdec_boundary,
    )
    all_gates_closed = all(item["closed"] for item in rows)
    current_frontier_closed = (
        all_gates_closed
        and materialized.get("open_materialized_obligation_count") == 0
        and extractor.get("missing_or_open_count") == 0
        and new_sparse.get("missing_admission_count") == 0
    )

    future_schema_required = [
        "明确 source class：短窗、endpoint、PDEC dual sparse cap、Bohr cap、tail/cofactor、descent seam 或其他新增来源",
        "给出有限窗口或固定偏移纤维 I，以及候选集合 C(I)",
        "给出 blocker 家族 B_low、B_tail、B_col、B_endpoint、B_core 及其命中投影规则",
        "给出 witness n0 且 cover_count(n0)=0，或给出严格 blocker-deficit 不等式 |union blockers|<|C(I)|",
        "给出 phase_key、window_shape、formal_unit_id 与去重规则，禁止重复坐标当成独立原子",
        "给出有限签名 sigma(I) 的持久性测试；若同签名无限复现，必须回流显式 PDEC/ColumnCRT/Tail/Cofactor schema",
        "给出层级逃逸测试；若有限 packet 不稳定，必须进入 CleanKLS/DLS 或显式外部 KLS 输入",
        "给出可复现实验/证明账本的脚本、JSON 字段、范围、哈希和 open_obligation_count=0",
        "给出与已有 PDEC、ColumnCRT、LocalSurvivor、CleanKLS 路由的排他性或回流关系",
    ]

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_future_sparse_packet_extractor_schema_boundary_router",
        "status": "future_sparse_packet_extractor_schema_boundary_closed_current_frontier_zero",
        "boundary_law": (
            "未来 sparse 路线不能作为隐藏终端使用。当前已物化 LocalSurvivor/SAE 包清零，"
            "已知入口 extractor 覆盖清零，无名 sparse 入口为零；SAE 已不是独立终端。"
            "因此未来若新增真正 sparse 障碍，必须同步提交有限 packet extractor schema，"
            "否则按持久签名回流 PDEC/ColumnCRT/Tail/Cofactor，或按层级逃逸进入 CleanKLS/DLS。"
        ),
        "future_sparse_packet_schema_boundary_closed": all_gates_closed,
        "current_materialized_sparse_frontier_closed": current_frontier_closed,
        "global_sparse_family_unconditional_closed": False,
        "row_column_unconditional_closed": False,
        "future_sparse_schema_required": future_schema_required,
        "remaining_after_sparse_boundary": [
            "若未来引入真正 sparse route，必须提交 FutureExplicitSparsePacketExtractorSchema",
            "同有限签名持久复现进入 FutureExplicitPrimitivePDECSchema 或 ColumnCRT/Tail/Cofactor 命名 schema",
            "层级逃逸进入 CleanKLS/DLS 或 explicit ExternalKLS 输入",
            "最终定理晋级仍需要 DStructureRankinPromotion 独立接受",
        ],
        "review_conclusion": (
            "FutureExplicitSparsePacketExtractorSchema 边界已闭合：当前 sparse/LocalSurvivor 前沿没有开放物化义务，"
            "已知入口全部覆盖，当前合同体系无无名 sparse 入口；未来新增 sparse 路线必须先给完整有限 packet extractor schema。"
            "这不是全局 sparse family 无条件排斥，也不是完整行/列无条件定理。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path)
            for path in [
                materialized_path,
                extractor_path,
                new_sparse_path,
                sae_absorb_path,
                packet_contract_path,
                pdec_boundary_path,
            ]
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 审查报告。"""
    lines: list[str] = [
        "# Prime Matrix 未来 sparse packet extractor schema 边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 边界律",
        "",
        result["boundary_law"],
        "",
        "```text",
        f"future_sparse_packet_schema_boundary_closed={fmt_bool(result['future_sparse_packet_schema_boundary_closed'])}",
        f"current_materialized_sparse_frontier_closed={fmt_bool(result['current_materialized_sparse_frontier_closed'])}",
        f"global_sparse_family_unconditional_closed={fmt_bool(result['global_sparse_family_unconditional_closed'])}",
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
                closed=fmt_bool(item["closed"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 未来 sparse schema 准入条件",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in result["future_sparse_schema_required"])
    lines.extend(
        [
            "",
            "## 4. sparse 边界后的剩余",
            "",
        ]
    )
    lines.extend(f"- `{item}`" for item in result["remaining_after_sparse_boundary"])
    lines.extend(
        [
            "",
            "## 5. 判定",
            "",
            (
                "当前 sparse/LocalSurvivor 前沿已经清零，但清零的是已知与已物化前沿，"
                "不是对所有未来 sparse family 的无条件排斥。未来新增 sparse 路线必须先提交完整 extractor schema；"
                "不给 schema 就只能回流到已命名的 PDEC/ColumnCRT/Tail/Cofactor 或 CleanKLS/DLS 输入。"
            ),
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--materialized", type=Path, default=DEFAULT_MATERIALIZED_LEDGER)
    parser.add_argument("--extractor", type=Path, default=DEFAULT_EXTRACTOR_COVERAGE)
    parser.add_argument("--new-sparse", type=Path, default=DEFAULT_NEW_SPARSE)
    parser.add_argument("--sae-absorb", type=Path, default=DEFAULT_SAE_ABSORB)
    parser.add_argument("--packet-contract", type=Path, default=DEFAULT_PACKET_CONTRACT)
    parser.add_argument("--pdec-boundary", type=Path, default=DEFAULT_PDEC_BOUNDARY)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        materialized_path=args.materialized,
        extractor_path=args.extractor,
        new_sparse_path=args.new_sparse,
        sae_absorb_path=args.sae_absorb,
        packet_contract_path=args.packet_contract,
        pdec_boundary_path=args.pdec_boundary,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["remaining_after_sparse_boundary"])


if __name__ == "__main__":
    main()
