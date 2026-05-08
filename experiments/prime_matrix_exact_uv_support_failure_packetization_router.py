#!/usr/bin/env python3
"""Prime Matrix ExactUVSupport 失败包化路由器。

用法示例：
  python3 experiments/prime_matrix_exact_uv_support_failure_packetization_router.py

输出：
  docs/monograph/prime-matrix-exact-uv-support-failure-packetization-router.json
  docs/monograph/prime-matrix-exact-uv-support-failure-packetization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_EXACT_TERMINAL = DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.json"
DEFAULT_MULTIPLIER = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_SOURCE_CORE = DOCS / "prime-matrix-noncanonical-source-core-atomization-router.json"
DEFAULT_SPARSE_SCHEMA = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-exact-uv-support-failure-packetization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-exact-uv-support-failure-packetization-router.md"


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


def support_threshold_rows(multiplier: dict[str, Any]) -> list[dict[str, Any]]:
    """抽取最终容量反原子所需的支撑阈值样本。"""
    rows: list[dict[str, Any]] = []
    for row in multiplier.get("threshold_rows", []):
        rows.append(
            {
                "k": row["k"],
                "log_y": row["log_y"],
                "required_pair_support_power": row["required_pair_support_power"],
                "required_pair_support": row["required_pair_support"],
                "failure_packet_condition": (
                    f"S_u*S_v < L^{row['required_pair_support_power']:.0f}"
                ),
            }
        )
    return rows


def packet_schema_fields() -> list[dict[str, str]]:
    """固定支撑失败 packet 必须携带的最小字段。"""
    return [
        {
            "field": "source_class",
            "meaning": "固定为 actual noncanonical full-S non-AP balanced source。",
            "why_needed": "防止 canonical 支撑链或 generic WFD 模板偷渡。",
        },
        {
            "field": "formal_unit_id",
            "meaning": "与 registered multiplier discipline 的同一 formal unit 对齐。",
            "why_needed": "防止账外 Type/Fourier/fiber 乘子重入。",
        },
        {
            "field": "block_key",
            "meaning": "记录 P、窗口、dyadic U,V、phase_key、path/tail 标签。",
            "why_needed": "使 moving block 不再是无名变量。",
        },
        {
            "field": "exact_u_support/exact_v_support",
            "meaning": "列出或证明精确 u、v 支撑集合及其绝对权重非零性。",
            "why_needed": "ExactUVSupport 失败正是这些集合乘积低于阈值。",
        },
        {
            "field": "support_threshold",
            "meaning": "登记 L^(2A+4C+E) 或更强阈值。",
            "why_needed": "与 final M_{u,v} 反原子不等式直接相连。",
        },
        {
            "field": "registered_capacity_profile",
            "meaning": "给出 packet 内 M_{u,v}、总质量、最大 pair 质量和 log-power 乘子。",
            "why_needed": "区分 raw support 失败和最终容量反原子失败。",
        },
        {
            "field": "return_tests",
            "meaning": "逐项测试 canonical、PDEC、SAE/LocalSurvivor、ColumnCRT、CleanKLS/DLS、外部 KLS。",
            "why_needed": "若不能直接排斥 packet，必须回流到已命名出口。",
        },
        {
            "field": "reproducible_certificate",
            "meaning": "脚本、JSON 字段、范围、哈希和 open_obligation_count。",
            "why_needed": "使未来新增 sparse 支撑失败路线不能作为隐藏终端。",
        },
    ]


def build_rows(
    exact_terminal: dict[str, Any],
    multiplier: dict[str, Any],
    source_core: dict[str, Any],
    sparse_schema: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成失败包化判定表。"""
    return [
        {
            "gate": "ExactSupportTerminalPinned",
            "closed": exact_terminal.get("unique_source_terminal_input")
            == "ActualNoncanonicalExactUVSupportLowerBound",
            "proved": True,
            "meaning": "上一层已把唯一源侧微输入固定为 ActualNoncanonicalExactUVSupportLowerBound。",
            "remaining": "只能攻击该输入本身，不能回到已排除伪路线。",
        },
        {
            "gate": "RegisteredCapacityAttached",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed") is True,
            "proved": True,
            "meaning": "所有 Type/Fourier/fiber 成本已经登记为同一 formal unit 的 log-power 乘子。",
            "remaining": "支撑失败不能再解释为账外乘子问题。",
        },
        {
            "gate": "FailureEquivalencePacketized",
            "closed": True,
            "proved": True,
            "meaning": "ExactUVSupport 失败等价于存在一个正质量 actual noncanonical clean block，其 exact u/v 支撑乘积低于登记阈值。",
            "remaining": "必须排斥这些 packet，或证明它们回流到已命名出口。",
        },
        {
            "gate": "CanonicalAndGenericEscapeBlocked",
            "closed": source_core.get("canonical_import_allowed") is False
            and exact_terminal.get("exact_uv_support_terminal_boundary_closed") is True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 支撑链和 generic WFD 点支撑模型都不能替代该 packet 排斥。",
            "remaining": "packet 必须在 actual noncanonical 补集内处理。",
        },
        {
            "gate": "SparseSchemaInterfaceReady",
            "closed": sparse_schema.get("future_sparse_packet_schema_boundary_closed") is True,
            "proved": True,
            "meaning": "未来 sparse 路线已经有显式 packet extractor schema 准入规则。",
            "remaining": "Actual support-failure packet 是一个新增 source class，仍需证明排斥或提交全集证书。",
        },
        {
            "gate": "NoHiddenSupportFailure",
            "closed": True,
            "proved": True,
            "meaning": "支撑失败不能继续作为抽象硬点存在；它必须物化为带字段、阈值、回流测试和哈希的 packet。",
            "remaining": "当前材料还没有排斥所有这种 packet。",
        },
        {
            "gate": "ActualSupportFailurePacketExclusionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明所有 actual noncanonical 支撑失败 packet 都不存在或必回流。",
            "remaining": "证明 ActualNoncanonicalSupportFailurePacketExclusion，或给直接 final capacity anti-atom。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧 packet 排斥完成后仍需独立验收。",
        },
    ]


def run(
    exact_terminal_path: Path,
    multiplier_path: Path,
    source_core_path: Path,
    sparse_schema_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 ExactUVSupport 失败包化路由。"""
    source_paths = [
        exact_terminal_path,
        multiplier_path,
        source_core_path,
        sparse_schema_path,
        dstructure_path,
    ]
    exact_terminal = load_json(exact_terminal_path)
    multiplier = load_json(multiplier_path)
    source_core = load_json(source_core_path)
    sparse_schema = load_json(sparse_schema_path)
    dstructure = load_json(dstructure_path)
    rows = build_rows(
        exact_terminal=exact_terminal,
        multiplier=multiplier,
        source_core=source_core,
        sparse_schema=sparse_schema,
        dstructure=dstructure,
    )
    closed_except_exclusion = all(
        row["closed"]
        for row in rows
        if row["gate"] != "ActualSupportFailurePacketExclusionCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_exact_uv_support_failure_packetization_router",
        "status": "exact_uv_support_failure_packetized_packet_exclusion_open",
        "failure_packetization_closed": closed_except_exclusion,
        "exact_uv_support_proved": False,
        "actual_support_failure_packet_exclusion_proved": False,
        "actual_final_capacity_antiatom_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_source_input": "ActualNoncanonicalExactUVSupportLowerBound",
        "equivalent_packet_input": "ActualNoncanonicalSupportFailurePacketExclusion",
        "latest_self_contained_basis": (
            "ActualNoncanonicalSupportFailurePacketExclusion AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "equivalence_law": (
            "在已固定 actual noncanonical clean block、exact u/v 支撑定义和 registered multiplier "
            "阈值后，ActualNoncanonicalExactUVSupportLowerBound 等价于不存在正质量 "
            "ActualNoncanonicalSupportFailurePacket。"
        ),
        "packetization_law": (
            "若 ExactUVSupport 失败，则失败不再是无名硬点：它必须给出一个 finite sparse packet，"
            "携带 source_class、formal_unit_id、block_key、exact u/v 支撑、阈值、容量剖面、"
            "回流测试和可复现证书。若不能给出这样的 packet，则支撑失败命题无准入。"
        ),
        "plain_conclusion": (
            "最后源侧输入被进一步包化：不再把 `ActualNoncanonicalExactUVSupportLowerBound` "
            "当作抽象正下界，而是等价改写为排斥所有 actual noncanonical 支撑失败 packet。"
            "这关闭了“支撑失败仍可无名停留”的边界，但当前材料仍未证明 packet 全部不存在或必回流，"
            "所以完整无条件行/列命题仍未闭合。"
        ),
        "rows": rows,
        "packet_schema_fields": packet_schema_fields(),
        "threshold_rows": support_threshold_rows(multiplier),
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
        "# Prime Matrix ExactUVSupport 失败包化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"failure_packetization_closed={fmt_bool(result['failure_packetization_closed'])}",
        f"exact_uv_support_proved={fmt_bool(result['exact_uv_support_proved'])}",
        f"actual_support_failure_packet_exclusion_proved={fmt_bool(result['actual_support_failure_packet_exclusion_proved'])}",
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
            "## 2. 等价改写",
            "",
            result["equivalence_law"],
            "",
            "上一层源输入：",
            "",
            "```text",
            result["previous_source_input"],
            "```",
            "",
            "包化后的等价输入：",
            "",
            "```text",
            result["equivalent_packet_input"],
            "```",
            "",
            "连同独立晋级门，最新完全自足输入基写成：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 3. 支撑失败 packet 准入字段",
            "",
            "| field | meaning | why needed |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["packet_schema_fields"]:
        lines.append(
            "| `{field}` | {meaning} | {why_needed} |".format(
                field=table_cell(row["field"]),
                meaning=table_cell(row["meaning"]),
                why_needed=table_cell(row["why_needed"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 阈值样本",
            "",
            "| k | log y | required power | required pair support | failure packet condition |",
            "| ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["threshold_rows"]:
        lines.append(
            "| {k} | {log_y:.6g} | {required_pair_support_power:.1f} | {required_pair_support} | `{failure_packet_condition}` |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            result["packetization_law"],
            "",
            "本步没有证明 `ActualNoncanonicalSupportFailurePacketExclusion`；它闭合的是准入和等价边界。",
            "要完成源侧自足闭合，下一步必须证明所有这种 packet 不存在、或必回流到 PDEC/SAE/ColumnCRT/CleanKLS/外部 KLS，或直接证明 final capacity anti-atom。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exact-terminal", type=Path, default=DEFAULT_EXACT_TERMINAL)
    parser.add_argument("--multiplier", type=Path, default=DEFAULT_MULTIPLIER)
    parser.add_argument("--source-core", type=Path, default=DEFAULT_SOURCE_CORE)
    parser.add_argument("--sparse-schema", type=Path, default=DEFAULT_SPARSE_SCHEMA)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        exact_terminal_path=args.exact_terminal,
        multiplier_path=args.multiplier,
        source_core_path=args.source_core,
        sparse_schema_path=args.sparse_schema,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_self_contained_basis"])


if __name__ == "__main__":
    main()
