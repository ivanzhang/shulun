#!/usr/bin/env python3
"""生成 strict source declaration packet 下游同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_source_declaration_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json

输出：
  data/prime-matrix-strict-source-declaration-downstream-sync-ledger.json
  docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.json
  docs/monograph/prime-matrix-strict-source-declaration-downstream-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-source-declaration-downstream-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-source-declaration-downstream-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-source-declaration-downstream-sync-router.md"

COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
SIGNED_LANE_TARGET = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
EXACTUV_TARGET = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
EXACTUV_SPLIT = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"

SOURCE_FILES = [
    {
        "id": "common_packet",
        "json": "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json",
        "role": "把 payload 与 ExactUV 合流到 common source declaration packet",
    },
    {
        "id": "precauchy_declaration",
        "json": "prime-matrix-strict-precauchy-declaration-line-router.json",
        "role": "普通 pre-Cauchy declaration line 被过滤到 actual constructor formula line",
    },
    {
        "id": "joint_emitter_fields",
        "json": "prime-matrix-strict-joint-emitter-formula-field-atom-router.json",
        "role": "joint emitter 字段层把生产性首字段钉到 joint declaration line",
    },
    {
        "id": "joint_declaration_constructor",
        "json": "prime-matrix-strict-joint-declaration-constructor-sync-router.json",
        "role": "joint declaration 同步到显式 joint alpha/delta constructor rule",
    },
    {
        "id": "explicit_joint_constructor",
        "json": "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json",
        "role": "显式 joint constructor 普通路线回到 signed-source 固定点",
    },
    {
        "id": "antisplit_firewall",
        "json": "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json",
        "role": "反分裂防火墙要求原子 declaration 内置 rows/pairing/payload",
    },
    {
        "id": "atomic_builtin_pairing",
        "json": "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json",
        "role": "原子 joint rows 被压到 built-in signed coefficient pairing 闭式",
    },
    {
        "id": "exact_uv_rank",
        "json": "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
        "role": "ExactUV map rank 被压到 actual emitter bounded incidence",
    },
    {
        "id": "actual_emitter_entropy",
        "json": "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
        "role": "ExactUV incidence 被拆成 source entropy 与 fixed-pair fiber bound",
    },
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象并在账本中登记。"""
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
    hashes = {
        "experiments/prime_matrix_strict_source_declaration_downstream_sync_router.py": sha256(
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


def sync_chain_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成 common packet 到下游字段的同步链。"""
    return [
        {
            "from": COMMON_PACKET,
            "to": "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter",
            "status": data["common_packet"].get("next_direct_attack_target") == COMMON_PACKET,
            "meaning": "common packet 的 declaration/rows 字段必须先给 actual noncanonical pre-Cauchy declaration。",
        },
        {
            "from": "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter",
            "to": "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter",
            "status": data["precauchy_declaration"].get("next_direct_attack_target")
            == "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter",
            "meaning": "普通声明行经过 source-class 分类后只剩 actual constructor formula line。",
        },
        {
            "from": "ActualNoncanonicalPrimitiveConstructorFormulaLineForEmitter",
            "to": "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple",
            "status": data["joint_emitter_fields"].get("next_direct_attack_target")
            == "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple",
            "meaning": "payload packet 要求同一 source tuple 同时发射 basis word 与 signed coefficient。",
        },
        {
            "from": "PreCauchyJointWordCoefficientEmitterDeclarationLineForActualNoncanonicalSourceTuple",
            "to": "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple",
            "status": data["joint_declaration_constructor"].get("next_direct_attack_target")
            == "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple",
            "meaning": "普通 joint declaration 的生产性内容是显式 joint alpha/delta primitive rule。",
        },
        {
            "from": "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple",
            "to": "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR "
            + TERMINAL_DESCENT,
            "status": data["explicit_joint_constructor"].get("new_explicit_joint_constructor_formula_artifact_present")
            is False,
            "meaning": "现有显式构造器路线回到 signed-source 固定点；除非提交新公式工件或改走终端下降。",
        },
        {
            "from": "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection",
            "to": "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing",
            "status": data["antisplit_firewall"].get("next_direct_attack_target")
            == "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing",
            "meaning": "若要求反分裂，声明行必须内置 rows formula、word/coefficient pairing 与 prepushforward identity。",
        },
        {
            "from": "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing",
            "to": SIGNED_LANE_TARGET,
            "status": data["atomic_builtin_pairing"].get("next_direct_attack_target")
            == SIGNED_LANE_TARGET,
            "meaning": "原子声明的首个未闭合 signed 字段是每条 atomic joint row 的内置配对闭式值。",
        },
        {
            "from": EXACTUV_TARGET,
            "to": EXACTUV_SPLIT,
            "status": data["actual_emitter_entropy"].get("next_direct_attack_target") == EXACTUV_SPLIT,
            "meaning": "ExactUV 子线仍是 source-domain entropy 与 fixed exact pair fiber bound 的合取。",
        },
    ]


def decision_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CommonPacketTargetActive",
            "closed": data["common_packet"].get("next_direct_attack_target") == COMMON_PACKET,
            "proved": False,
            "meaning": "上一层已把 payload 与 ExactUV 合流到 common source declaration packet。",
            "remaining": COMMON_PACKET,
        },
        {
            "gate": "DeclarationLaneSyncedToJointConstructor",
            "closed": True,
            "proved": False,
            "meaning": "packet 的 declaration/rows/payload 字段与已有 pre-Cauchy/joint constructor 线同步。",
            "remaining": "ordinary route or antisplit route",
        },
        {
            "gate": "OrdinaryJointConstructorRouteIsFixedPoint",
            "closed": data["explicit_joint_constructor"].get(
                "joint_alpha_side_route_returns_to_signed_source_fixed_point"
            )
            is True,
            "proved": True,
            "meaning": "普通显式 joint constructor 继续展开会回到 signed-source 固定点，不能自证 common packet。",
            "remaining": "new formula artifact, antisplit atomic declaration, or terminal descent",
        },
        {
            "gate": "AntiSplitAtomicRoutePinned",
            "closed": data["antisplit_firewall"].get("next_direct_attack_target")
            == "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing",
            "proved": False,
            "meaning": "为避免分裂固定点，必须把 rows/pairing/payload 内置到同一 atomic declaration。",
            "remaining": "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing",
        },
        {
            "gate": "AtomicRouteReducedToBuiltInSignedPairing",
            "closed": data["atomic_builtin_pairing"].get("next_direct_attack_target")
            == SIGNED_LANE_TARGET,
            "proved": False,
            "meaning": "原子 joint rows 的真正 signed 首缺口是 built-in signed coefficient/pairing 闭式。",
            "remaining": SIGNED_LANE_TARGET,
        },
        {
            "gate": "ExactUVLaneStillParallel",
            "closed": data["actual_emitter_entropy"].get("next_direct_attack_target") == EXACTUV_SPLIT,
            "proved": False,
            "meaning": "built-in signed pairing 不自动给 source-domain entropy 或 fixed exact pair fiber bound。",
            "remaining": EXACTUV_SPLIT,
        },
        {
            "gate": "CommonPacketDownstreamBasisCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料没有 built-in pairing 闭式，也没有 ExactUV entropy/fiber 合取证明。",
            "remaining": f"{SIGNED_LANE_TARGET} AND {EXACTUV_SPLIT}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只同步 common packet 下游，不关闭 AP 零点包、same-set PDEC、RatePreservation 或 DStructure/Rankin 门。",
            "remaining": (
                f"({SIGNED_LANE_TARGET} OR {TERMINAL_DESCENT}) AND {EXACTUV_TARGET} "
                "AND RatePreservationLedger_FOR_moving_atom_packet "
                "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
            ),
        },
    ]


def evidence_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """抽取依赖证书状态。"""
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
                "row_column_unconditional_closed": bool(
                    cert.get("row_column_unconditional_closed", False)
                ),
            }
        )
    return rows


def theorem_rows() -> list[dict[str, str]]:
    """列出本路由形成的命题行。"""
    return [
        {
            "name": "common_packet_downstream_decomposition",
            "status": "closed_routing",
            "statement": (
                "The common packet decomposes into a signed built-in pairing lane and an independent ExactUV "
                "entropy/fixed-fiber lane."
            ),
        },
        {
            "name": "ordinary_constructor_route_rejected",
            "status": "closed_routing",
            "statement": (
                "The ordinary joint constructor route is a signed-source fixed point unless replaced by a new "
                "formula artifact, an antisplit atomic declaration, or terminal descent."
            ),
        },
        {
            "name": "row_column_unconditional_closure",
            "status": "open",
            "statement": (
                "Built-in signed pairing, ExactUV incidence, and global rate/D-structure gates are still open."
            ),
        },
    ]


def build_result() -> dict[str, Any]:
    """生成同步证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {item["id"]: load_json(item["json"]) for item in SOURCE_FILES}
    missing = [
        f"docs/monograph/{item['json']}"
        for item in SOURCE_FILES
        if not (DOCS / item["json"]).exists()
    ]
    aggregate = {
        "common_packet_before_router": COMMON_PACKET,
        "signed_lane_after_router": SIGNED_LANE_TARGET,
        "exactuv_lane_after_router": EXACTUV_SPLIT,
        "ordinary_joint_constructor_route_fixed_point": True,
        "downstream_sync_closed": True,
        "built_in_signed_pairing_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "common_packet_proved": False,
        "row_column_unconditional_closed": False,
        "current_downstream_basis": [
            SIGNED_LANE_TARGET,
            EXACTUV_SPLIT,
            "RatePreservationLedger_FOR_moving_atom_packet",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "parallel_or_external_exits": [
            TERMINAL_DESCENT,
            "PageExceptionalSingletonCarrierOrNonrealZeroPacketResidualBudget",
            "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate",
        ],
    }

    ledger = {
        "aggregate": aggregate,
        "sync_chain_rows": sync_chain_rows(data),
        "evidence_rows": evidence_rows(data),
        "missing_source_files": missing,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_strict_source_declaration_downstream_sync_router",
        "status": "strict_common_source_declaration_packet_synced_to_builtin_pairing_and_exactuv_open",
        "frontier_sync_only": True,
        "multi_target_decomposition": True,
        "finite_evidence_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "sync_chain_rows": ledger["sync_chain_rows"],
        "evidence_rows": ledger["evidence_rows"],
        "decision_rows": decision_rows(data),
        "theorem_rows": theorem_rows(),
        "missing_source_files": missing,
        "plain_conclusion": (
            f"本步把 `{COMMON_PACKET}` 的下游字段同步为两条子线：signed/payload 子线若禁止普通 "
            f"joint constructor 固定点，必须压到 `{SIGNED_LANE_TARGET}`；ExactUV 子线仍保持 "
            f"`{EXACTUV_SPLIT}`。当前语料没有 built-in pairing 闭式，也没有 ExactUV entropy/fiber "
            "合取证明，所以这不是行/列命题无条件闭合。"
        ),
        "next_direct_attack_target": SIGNED_LANE_TARGET,
        "parallel_direct_attack_target": EXACTUV_SPLIT,
        "built_in_signed_pairing_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "common_packet_proved": False,
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
        "# Prime Matrix strict source declaration downstream sync router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"common_packet={agg['common_packet_before_router']}",
        f"signed_lane_after_router={agg['signed_lane_after_router']}",
        f"exactuv_lane_after_router={agg['exactuv_lane_after_router']}",
        f"common_packet_proved={fmt_bool(agg['common_packet_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | status | meaning |",
        "| --- | --- | ---: | --- |",
    ]
    for row in result["sync_chain_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['from'])}`",
                    f"`{table_cell(row['to'])}`",
                    fmt_bool(row["status"]),
                    table_cell(row["meaning"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 证据同步表",
            "",
            "| id | role | status | next |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["evidence_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['id'])}`",
                    table_cell(row["role"]),
                    table_cell(row["status"]),
                    table_cell(row["next_direct_attack_target"] or ""),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 当前下游基",
            "",
            "| input |",
            "| --- |",
        ]
    )
    for item in agg["current_downstream_basis"]:
        lines.append(f"| `{table_cell(item)}` |")
    lines.extend(
        [
            "",
            "## 5. 命题行",
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
            "## 6. 结论边界",
            "",
            "- 本步只同步 common packet 的下游字段。",
            "- 普通 joint constructor 路线因 signed-source 固定点不能作为证明。",
            f"- 下一直接主攻是 `{SIGNED_LANE_TARGET}`；ExactUV 子线仍需 `{EXACTUV_SPLIT}`。",
            "- 不能把该同步解读为行/列命题无条件闭合。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    if result["missing_source_files"]:
        lines.extend(["", "## 8. 缺失依赖", "", "| file |", "| --- |"])
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
