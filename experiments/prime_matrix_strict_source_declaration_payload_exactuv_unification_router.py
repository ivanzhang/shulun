#!/usr/bin/env python3
"""生成 strict source declaration / payload / ExactUV 合流证书。

用法示例：
  python3 experiments/prime_matrix_strict_source_declaration_payload_exactuv_unification_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json

输出：
  data/prime-matrix-strict-source-declaration-payload-exactuv-unification-ledger.json
  docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json
  docs/monograph/prime-matrix-strict-source-declaration-payload-exactuv-unification-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-source-declaration-payload-exactuv-unification-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"
OUT_MD = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.md"

PAYLOAD_TARGET = "NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward"
EXACTUV_SPLIT = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
SOURCE_TABLE_SPLIT = (
    "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter AND "
    "PrimitiveSummandEmitterFormulaRowsForActualNoncanonicalTable AND "
    "AlphaDeltaCoefficientIdentityBeforePushforwardLedger AND "
    "SourceTableNoDownstreamRecoveryAndNamedReturnLedger"
)
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"

SOURCE_FILES = [
    {
        "id": "atomic_payload_origin",
        "json": "prime-matrix-strict-atomic-payload-origin-identity-router.json",
        "role": "signed payload 被压到非循环 basis-word/signed-coefficient 来源恒等式",
    },
    {
        "id": "atomic_branch_trace_payload",
        "json": "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json",
        "role": "atomic branch trace 的可见坐标与 signed payload 分裂",
    },
    {
        "id": "branch_trace_cycle",
        "json": "prime-matrix-strict-branch-trace-signed-payload-cycle-router.json",
        "role": "branch trace signed payload 回到 row-level origin table",
    },
    {
        "id": "exact_uv_rank",
        "json": "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
        "role": "ExactUV map rank 被压到 actual emitter bounded incidence",
    },
    {
        "id": "actual_emitter_entropy",
        "json": "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
        "role": "bounded incidence 被拆成 source entropy 与 fixed-pair fiber bound",
    },
    {
        "id": "actual_emitter_source_table",
        "json": "prime-matrix-strict-actual-emitter-source-table-router.json",
        "role": "actual emitter 源表被拆成 declaration/rows/identity/return",
    },
    {
        "id": "final_open_input",
        "json": "prime-matrix-final-open-input-direct-attack-router.json",
        "role": "最终开放输入把 source lane 压到 ExactUV 支撑或外部 FullS",
    },
    {
        "id": "global_crt_signed_payload",
        "json": "prime-matrix-global-crt-signed-payload-sync-router.json",
        "role": "global CRT 可见骨架不能生成 signed payload",
    },
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，缺失本身会在账本中登记。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    hashes: dict[str, str] = {
        "experiments/prime_matrix_strict_source_declaration_payload_exactuv_unification_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for item in SOURCE_FILES:
        path = DOCS / item["json"]
        if path.exists():
            hashes[f"docs/monograph/{item['json']}"] = sha256(path)
    if OUT_LEDGER.exists():
        hashes[str(OUT_LEDGER.relative_to(ROOT))] = sha256(OUT_LEDGER)
    return hashes


def packet_fields() -> list[dict[str, str]]:
    """定义共同 source declaration packet 的字段。"""
    return [
        {
            "field": "declaration_line",
            "requirement": "在 Cauchy/Phi/payment 前声明 actual noncanonical pre-Cauchy emitter，而不是从零行或 payment 反推。",
            "feeds": "payload + ExactUV",
        },
        {
            "field": "source_tuple_domain_entropy",
            "requirement": "给出 primitive source tuple 支撑下界，足以支持 actual emitter source-domain entropy。",
            "feeds": "ExactUV",
        },
        {
            "field": "primitive_summand_rows",
            "requirement": "逐行列出 branch key、basis word、sign、local factor、exact (u,v) 与 return tag。",
            "feeds": "payload + ExactUV",
        },
        {
            "field": "basis_word_signed_coefficient_identity",
            "requirement": "证明 basis word 到 signed coefficient 的来源恒等式先于推前，且不调用 row-level 表。",
            "feeds": "payload",
        },
        {
            "field": "alpha_delta_prepushforward_identity",
            "requirement": "证明这些 primitive rows 在推前前求和等于 actual alpha/delta 贡献。",
            "feeds": "payload + final source lane",
        },
        {
            "field": "fixed_exact_uv_fiber_bound",
            "requirement": "在固定 exact (u,v) 与 branch/sign/local-factor refinement 后，证明 primitive 原像数为 polylog 级。",
            "feeds": "ExactUV",
        },
        {
            "field": "no_downstream_recovery",
            "requirement": "显式排除从 payment、零行覆盖、Gamma 图、Cauchy 后表达式或 canonical 表倒推出 source row。",
            "feeds": "acyclicity",
        },
        {
            "field": "named_return_partition",
            "requirement": "缺声明、缺 row、符号冲突、local factor 为零、fiber collapse、entropy deficit、超预算、canonical 泄漏均命名回流。",
            "feeds": "failure ledger",
        },
    ]


def evidence_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """抽取各依赖路由的当前读数。"""
    rows: list[dict[str, Any]] = []
    for item in SOURCE_FILES:
        cert = data[item["id"]]
        rows.append(
            {
                "id": item["id"],
                "file": f"docs/monograph/{item['json']}",
                "role": item["role"],
                "status": cert.get("status", "missing"),
                "next_direct_attack_target": cert.get("next_direct_attack_target"),
                "terminal_gap_after_router": cert.get("terminal_gap_after_router"),
                "row_column_unconditional_closed": bool(
                    cert.get("row_column_unconditional_closed", False)
                ),
            }
        )
    return rows


def decision_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成合流判定表。"""
    payload = data["atomic_payload_origin"]
    branch_trace = data["branch_trace_cycle"]
    entropy = data["actual_emitter_entropy"]
    source_table = data["actual_emitter_source_table"]
    exact_uv_rank = data["exact_uv_rank"]
    global_crt = data["global_crt_signed_payload"]

    return [
        {
            "gate": "AtomicPayloadReducedToNoncircularOriginIdentity",
            "closed": payload.get("next_direct_attack_target") == PAYLOAD_TARGET,
            "proved": False,
            "meaning": "signed payload 的第一生产字段已压到 atomic basis word/signed coefficient 来源恒等式。",
            "remaining": PAYLOAD_TARGET,
        },
        {
            "gate": "ExactUVIncidenceReducedToEntropyAndFiber",
            "closed": entropy.get("next_direct_attack_target") == EXACTUV_SPLIT,
            "proved": False,
            "meaning": "ActualEmitterExactUV 有界重数已拆成 source-domain entropy 与 fixed-pair fiber bound。",
            "remaining": EXACTUV_SPLIT,
        },
        {
            "gate": "SourceTableFirstLinePinned",
            "closed": source_table.get("terminal_gap_after_router") == SOURCE_TABLE_SPLIT,
            "proved": False,
            "meaning": "actual emitter 源表的第一合法字段是 pre-Cauchy declaration line。",
            "remaining": SOURCE_TABLE_SPLIT,
        },
        {
            "gate": "VisibleCRTTraceCannotEmitSignedRows",
            "closed": branch_trace.get("signed_payload_trace_returns_to_row_level_origin_table")
            is True
            and global_crt.get("finite_crt_skeleton_creates_signed_payload") is not True,
            "proved": True,
            "meaning": "CRT/trace 可给可见坐标，但不能给 orientation、local factor、signed coefficient 与 source row。",
            "remaining": COMMON_PACKET,
        },
        {
            "gate": "PayloadNeedsCommonDeclarationPacket",
            "closed": True,
            "proved": False,
            "meaning": "非循环 signed coefficient 来源恒等式必须由同一 pre-Cauchy actual source row 正向给出。",
            "remaining": COMMON_PACKET,
        },
        {
            "gate": "ExactUVNeedsCommonDeclarationPacket",
            "closed": exact_uv_rank.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved")
            is False,
            "proved": False,
            "meaning": "没有 source rows，就无法同时证明 source entropy 与 fixed exact (u,v) polylog fiber。",
            "remaining": COMMON_PACKET,
        },
        {
            "gate": "CommonPacketWouldCloseInternalSourceLaneConditionally",
            "closed": True,
            "proved": True,
            "meaning": "若共同 packet 的字段全部给出，则 signed payload 与 ActualEmitterExactUV 两条内部 source lane 同时获得所需输入。",
            "remaining": f"prove {COMMON_PACKET}",
        },
        {
            "gate": "CurrentCorpusCommonPacketProved",
            "closed": False,
            "proved": False,
            "meaning": "当前仓库没有提交该 pre-Cauchy actual source declaration packet。",
            "remaining": COMMON_PACKET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只合流两个硬点，不关闭 AP 零点包、same-set PDEC、模型余量、RatePreservation 与 DStructure/Rankin 门。",
            "remaining": (
                "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget OR "
                "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR "
                f"{COMMON_PACKET}"
            ),
        },
    ]


def theorem_rows() -> list[dict[str, str]]:
    """列出本路由形成的命题行。"""
    return [
        {
            "name": "payload_exactuv_common_source_root",
            "status": "closed_routing",
            "statement": (
                "Atomic signed payload and ActualEmitterExactUV incidence both require a pre-Cauchy "
                "actual noncanonical source declaration packet when the proof is kept self-contained."
            ),
        },
        {
            "name": "common_packet_conditional_sufficiency",
            "status": "conditional",
            "statement": (
                "A packet containing declaration rows, signed coefficient identities, prepushforward equality, "
                "source entropy, fixed-pair fiber bounds, and named returns would close the internal source lane."
            ),
        },
        {
            "name": "row_column_unconditional_closure",
            "status": "open",
            "statement": (
                "The packet is not present in the current corpus, and AP zero-packet, same-set PDEC, "
                "rate/model, and D-structure inputs remain outside this routing step."
            ),
        },
    ]


def build_result() -> dict[str, Any]:
    """生成合流证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {item["id"]: load_json(item["json"]) for item in SOURCE_FILES}
    missing = [
        f"docs/monograph/{item['json']}"
        for item in SOURCE_FILES
        if not (DOCS / item["json"]).exists()
    ]

    aggregate = {
        "previous_payload_target": PAYLOAD_TARGET,
        "previous_exactuv_target": EXACTUV_SPLIT,
        "previous_source_table_split": SOURCE_TABLE_SPLIT,
        "common_source_declaration_packet": COMMON_PACKET,
        "frontier_unification_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "common_packet_proved": False,
        "atomic_signed_payload_constructor_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "row_column_unconditional_closed": False,
        "still_independent_or_parallel_inputs": [
            "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget",
            "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate",
            "ExplicitModelGapAndFiniteDPRCLedger",
            "RatePreservationLedger_FOR_moving_atom_packet",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
    }

    ledger = {
        "aggregate": aggregate,
        "packet_fields": packet_fields(),
        "evidence_rows": evidence_rows(data),
        "missing_source_files": missing,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_strict_source_declaration_payload_exactuv_unification_router",
        "status": "strict_payload_and_exactuv_reduced_to_common_precauchy_source_declaration_packet_open",
        "same_theorem_target_preserved": False,
        "source_lane_frontier_preserved": True,
        "multi_target_unification": True,
        "no_theorem_switch": True,
        "frontier_unification_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "packet_fields": packet_fields(),
        "evidence_rows": ledger["evidence_rows"],
        "decision_rows": decision_rows(data),
        "theorem_rows": theorem_rows(),
        "missing_source_files": missing,
        "plain_conclusion": (
            "本步把 signed payload 线与 ActualEmitterExactUV 线合流到同一个 "
            f"`{COMMON_PACKET}`。payload 需要它给出非循环 basis word/signed coefficient 来源恒等式；"
            "ExactUV 需要它给出 source-domain entropy 与 fixed exact (u,v) fiber bound。"
            "当前语料没有该 packet，所以这只是最新硬点压缩，不是行/列命题无条件闭合。"
        ),
        "next_direct_attack_target": COMMON_PACKET,
        "common_packet_proved": False,
        "atomic_signed_payload_constructor_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "row_column_unconditional_closed": False,
    }
    result["source_hashes"] = source_hashes()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix strict source declaration / payload / ExactUV 合流路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"common_packet={agg['common_source_declaration_packet']}",
        f"common_packet_proved={fmt_bool(agg['common_packet_proved'])}",
        f"atomic_signed_payload_constructor_proved={fmt_bool(agg['atomic_signed_payload_constructor_proved'])}",
        f"actual_emitter_exact_uv_bounded_multiplicity_incidence_proved={fmt_bool(agg['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 共同 packet 字段",
        "",
        "| field | feeds | requirement |",
        "| --- | --- | --- |",
    ]
    for row in result["packet_fields"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['field'])}`",
                    table_cell(row["feeds"]),
                    table_cell(row["requirement"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 证据同步表",
            "",
            "| id | role | status | next/after |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["evidence_rows"]:
        next_or_after = row["next_direct_attack_target"] or row["terminal_gap_after_router"] or ""
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['id'])}`",
                    table_cell(row["role"]),
                    table_cell(row["status"]),
                    table_cell(next_or_after),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    fmt_bool(row["closed"]),
                    fmt_bool(row["proved"]),
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(
            f"| `{table_cell(row['name'])}` | `{table_cell(row['status'])}` | {table_cell(row['statement'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 结论边界",
            "",
            "- 本步只合流 strict 内部 source lane 的两个活动硬点。",
            "- `PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket` 是下一直接主攻对象。",
            "- AP 零点包、same-set PDEC、模型余量、RatePreservation 与 DStructure/Rankin 验收门仍独立开放。",
            "- 不能把该合流路由解读为行/列命题无条件闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    if result["missing_source_files"]:
        lines.extend(["", "## 7. 缺失依赖", "", "| file |", "| --- |"])
        for name in result["missing_source_files"]:
            lines.append(f"| `{table_cell(name)}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
