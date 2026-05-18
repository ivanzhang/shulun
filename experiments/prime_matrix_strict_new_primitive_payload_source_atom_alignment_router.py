#!/usr/bin/env python3
"""生成 new primitive signed payload/trace 工件到 source atom 的对齐证书。

用法示例：
  python3 experiments/prime_matrix_strict_new_primitive_payload_source_atom_alignment_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json

输出：
  data/prime-matrix-strict-new-primitive-payload-source-atom-alignment-ledger.json
  docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json
  docs/monograph/prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
OUT_MD = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.md"

SIGNED_CYCLE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
ATOMIC_TRACE_PAYLOAD = DOCS / "prime-matrix-strict-atomic-branch-trace-payload-frontier-router.json"
PAYLOAD_ORIGIN = DOCS / "prime-matrix-strict-atomic-payload-origin-identity-router.json"
SOURCE_UNIFICATION = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"
PRETERMINAL_SUPPORT = DOCS / "prime-matrix-strict-preterminal-support-capacity-attack-router.json"
SOURCE_ATOM = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
Q2_FINAL = DOCS / "prime-matrix-q2-to-final-exact-source-alignment-router.json"
ACTIVE_FINAL = DOCS / "prime-matrix-active-final-inputs-router.json"

NEW_ARTIFACT = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_RANK_ATOM = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，避免把缺失当成证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书依赖的证据哈希。"""
    paths = [
        Path(__file__).resolve(),
        SIGNED_CYCLE,
        ATOMIC_TRACE_PAYLOAD,
        PAYLOAD_ORIGIN,
        SOURCE_UNIFICATION,
        PRETERMINAL_SUPPORT,
        SOURCE_ATOM,
        Q2_FINAL,
        ACTIVE_FINAL,
    ]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def contract_fields() -> list[dict[str, str]]:
    """列出 new primitive 工件若要破环必须携带的最低字段。"""
    return [
        {
            "field": "same_formal_unit_lock",
            "minimum_requirement": "锁定同一 actual counterexample formal unit、atomic branch trace、primitive source rows 与 exact `(u,v)` 口径。",
            "current_alignment": "已有 trace/source 证书说明该锁不能由可见坐标或 terminal 回流补出。",
            "remaining": SOURCE_RANK_ATOM,
        },
        {
            "field": "pre_cauchy_source_object",
            "minimum_requirement": "在 Cauchy、Phi、payment、零行恢复前声明 actual noncanonical primitive source object。",
            "current_alignment": "source declaration packet 与 final exact-source 原子都要求该对象。",
            "remaining": "ActualNoncanonicalPrimitiveEmitterSourceTableLedger",
        },
        {
            "field": "signed_payload_formula",
            "minimum_requirement": "正向给出 orientation、signed coefficient、local factor、truncation weight 与 nonzero/return tags。",
            "current_alignment": "若只给 coefficient 表，会回到 origin/common-packet 闭环。",
            "remaining": NEW_ARTIFACT,
        },
        {
            "field": "complete_key_partition",
            "minimum_requirement": "发射前把 primitive rows 分入 complete keys，禁止后验补标签。",
            "current_alignment": "preterminal source atom 已把它列为三原子之一。",
            "remaining": COMPLETE_KEY,
        },
        {
            "field": "source_domain_absolute_entropy",
            "minimum_requirement": "证明 actual source 质量不能集中在少数 primitive rows 或少数 key/fiber。",
            "current_alignment": "这是 source rank/no-collapse 包的首攻项。",
            "remaining": DOMAIN_ENTROPY,
        },
        {
            "field": "fixed_key_exact_uv_local_multiplicity",
            "minimum_requirement": "固定 complete key 与 fixed exact `(u,v)` 下只有 O(1) 个 admissible actual primitive source 原像。",
            "current_alignment": "缺该项时 new payload 只能命名单个原像，不能排除 fiber 坍缩。",
            "remaining": FIXED_KEY_MULT,
        },
        {
            "field": "no_cycle_or_terminal_recovery",
            "minimum_requirement": "证明没有调用 signed-lane 环、row-level origin table、terminal descent、PDEC 或外部谱输入反推。",
            "current_alignment": "若调用这些输入，工件不再是独立 new primitive artifact。",
            "remaining": f"{TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """把 new primitive 出口对齐到 final source atom。"""
    signed = data["signed"]
    trace = data["trace"]
    origin = data["origin"]
    source = data["source"]
    preterminal = data["preterminal"]
    atom = data["atom"]
    q2 = data["q2"]
    active = data["active"]

    signed_cycle_closed = signed.get("signed_lane_cycle_closed") is True
    visible_trace_insufficient = any(
        item.get("gate") == "VisibleCoordinateTraceDoesNotEmitPayload"
        and item.get("closed") is True
        for item in trace.get("rows", [])
    ) or any(
        item.get("gate") == "VisibleCoordinateTraceCannotBreakCycle"
        and item.get("closed") is True
        for item in signed.get("decision_rows", [])
    )
    origin_returns = (
        origin.get("next_direct_attack_target")
        == "NoncircularAtomicBasisWordSignedCoefficientOriginIdentityBeforePushforward"
        and source.get("next_direct_attack_target")
        == "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
    )
    preterminal_exactuv_imported = (
        preterminal.get("next_direct_attack_target")
        == "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
    )
    source_atom_imported = atom.get("terminal_gap_after_router") == SOURCE_RANK_ATOM
    active_final_imported = active.get("active_final_inputs_boundary_closed") is True
    q2_alignment_imported = q2.get("source_domain_rank_atom_package_imported") is True

    return [
        row(
            "SignedLaneCycleImported",
            signed_cycle_closed,
            signed_cycle_closed,
            "signed/payload 子线已闭环，new primitive 工件只有在闭环外正向产生 payload/source 时才有意义。",
            NEW_ARTIFACT,
        ),
        row(
            "VisibleTraceCannotServeAsNewArtifact",
            visible_trace_insufficient,
            visible_trace_insufficient,
            "可见 branch trace 只给坐标，不给 signed coefficient、orientation、local factor 或 source entropy。",
            NEW_ARTIFACT,
        ),
        row(
            "OriginIdentityWithoutSourceRankReturnsToCycle",
            origin_returns,
            True,
            "仅提交 basis-word/signed-coefficient 来源恒等式会与 ExactUV 一起回到 common source declaration packet。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "NewArtifactMustContainPreCauchySourceObject",
            True,
            False,
            "若工件不声明 Cauchy 前 actual source object，它只是后验标签或 terminal 回流，不能破环。",
            "ActualNoncanonicalPrimitiveEmitterSourceTableLedger",
        ),
        row(
            "NewArtifactRequiresExactUVFiberAperiodicity",
            preterminal_exactuv_imported,
            False,
            "破环工件必须控制同一 source 在 exact `(u,v)` fiber 上的质量分散；CRT/轮筛位置刚性不能替代。",
            "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource",
        ),
        row(
            "SourceRankAtomPackageImported",
            source_atom_imported,
            False,
            "fiber 非集中已被仓库压成 source entropy、complete key partition、fixed-key local multiplicity 三原子包。",
            SOURCE_RANK_ATOM,
        ),
        row(
            "Q2AndFinalInputAlignmentImported",
            q2_alignment_imported and active_final_imported,
            False,
            "Q2/CRT 路线的无名终端已回接到 final exact-source 原子或外部谱输入；new primitive 不能形成第三个无名终端。",
            f"{SOURCE_RANK_ATOM} OR {EXTERNAL_SPECTRAL}",
        ),
        row(
            "CurrentCorpusHasIndependentNewPrimitiveArtifact",
            False,
            False,
            "当前语料没有提交同时满足 source object、complete key、source entropy、fixed-key exact-UV multiplicity 与 no-cycle 条件的新工件。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "NewPrimitiveExitReducedToSourceAtomOrExternalRoutes",
            signed_cycle_closed and source_atom_imported,
            False,
            "因此 new primitive 出口不是独立闭合点；它要么证明 source rank/no-collapse 包，要么转入 terminal descent、PDEC 或外部谱输入。",
            f"{SOURCE_RANK_ATOM} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只完成出口对齐；source 三原子、外部谱输入与 DStructure/Rankin 独立验收均未证明。",
            (
                f"({DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
                f"OR {EXTERNAL_SPECTRAL}; {DSTRUCTURE}"
            ),
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成对齐证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "signed": load_json(SIGNED_CYCLE),
        "trace": load_json(ATOMIC_TRACE_PAYLOAD),
        "origin": load_json(PAYLOAD_ORIGIN),
        "source": load_json(SOURCE_UNIFICATION),
        "preterminal": load_json(PRETERMINAL_SUPPORT),
        "atom": load_json(SOURCE_ATOM),
        "q2": load_json(Q2_FINAL),
        "active": load_json(ACTIVE_FINAL),
    }
    rows = build_rows(data)
    preferred = data["atom"].get(
        "preferred_attack_order",
        [DOMAIN_ENTROPY, COMPLETE_KEY, FIXED_KEY_MULT],
    )
    aggregate = {
        "new_primitive_artifact_independent_terminal_present": False,
        "new_primitive_artifact_reduced_to_source_rank_atom": any(
            item["gate"] == "NewPrimitiveExitReducedToSourceAtomOrExternalRoutes"
            and item["closed"]
            for item in rows
        ),
        "source_rank_atom_imported": any(
            item["gate"] == "SourceRankAtomPackageImported" and item["closed"]
            for item in rows
        ),
        "actual_source_domain_entropy_proved": False,
        "complete_primitive_emitter_key_partition_proved": False,
        "fixed_key_exact_uv_local_multiplicity_proved": False,
        "external_spectral_input_accepted": False,
        "dstructure_rankin_independently_accepted": False,
        "row_column_unconditional_closed": False,
    }
    result = {
        "certificate_type": "prime_matrix_strict_new_primitive_payload_source_atom_alignment_router",
        "status": "strict_new_primitive_payload_reduced_to_actual_source_rank_atom_open",
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "contract_fields": contract_fields(),
        "decision_rows": rows,
        "preferred_attack_order": preferred,
        "next_direct_attack_target": preferred[0] if preferred else DOMAIN_ENTROPY,
        "parallel_direct_attack_targets": [
            COMPLETE_KEY,
            FIXED_KEY_MULT,
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            EXTERNAL_SPECTRAL,
            DSTRUCTURE,
        ],
        "latest_strict_activity_basis": (
            f"(({DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
            f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}) "
            f"AND {DSTRUCTURE}"
        ),
        "plain_conclusion": (
            f"本步直接审计 `{NEW_ARTIFACT}`。若它只是 signed-lane 环内的 trace、payload、origin 或 "
            "common packet 的改名，则不能破环；若它要作为真正的新 primitive 工件，就必须在 Cauchy/Phi/payment "
            "前声明同一 actual source object，并给出 source entropy、complete key partition 与 fixed-key exact-UV "
            f"local multiplicity。因而该出口对齐到 `{SOURCE_RANK_ATOM}`，或转入 terminal descent、PDEC、外部谱输入。"
            "当前语料没有独立 new primitive 工件，行/列命题仍未无条件闭合。"
        ),
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
    }
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix strict new primitive payload source-atom alignment router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"new_primitive_artifact_independent_terminal_present={fmt_bool(agg['new_primitive_artifact_independent_terminal_present'])}",
        f"new_primitive_artifact_reduced_to_source_rank_atom={fmt_bool(agg['new_primitive_artifact_reduced_to_source_rank_atom'])}",
        f"source_rank_atom_imported={fmt_bool(agg['source_rank_atom_imported'])}",
        f"actual_source_domain_entropy_proved={fmt_bool(agg['actual_source_domain_entropy_proved'])}",
        f"complete_primitive_emitter_key_partition_proved={fmt_bool(agg['complete_primitive_emitter_key_partition_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_proved={fmt_bool(agg['fixed_key_exact_uv_local_multiplicity_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(agg['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. New primitive 最低字段合同",
        "",
        "| field | minimum requirement | current alignment | remaining |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["contract_fields"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['field'])}`",
                    table_cell(item["minimum_requirement"]),
                    table_cell(item["current_alignment"]),
                    table_cell(item["remaining"]),
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
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
                    fmt_bool(item["closed"]),
                    fmt_bool(item["proved"]),
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 最新剩余基",
            "",
            "```text",
            result["latest_strict_activity_basis"],
            "```",
            "",
            "下一直接主攻顺序：",
            "",
            "| order | target |",
            "| ---: | --- |",
        ]
    )
    for index, target in enumerate(result["preferred_attack_order"], start=1):
        lines.append(f"| {index} | `{table_cell(target)}` |")
    lines.extend(
        [
            "",
            "## 4. 结论边界",
            "",
            "- 本步只把 new primitive signed payload/trace 出口对齐到 actual-source rank/no-collapse 原子。",
            "- 当前没有证明 source entropy、complete key partition、fixed-key exact-UV local multiplicity、外部谱输入或 DStructure/Rankin 独立验收。",
            "- 因而行/列命题仍不能标记为无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{table_cell(name)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """入口。"""
    result = build_result()
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
