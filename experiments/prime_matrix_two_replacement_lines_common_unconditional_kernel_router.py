#!/usr/bin/env python3
"""生成两条替代线共同无条件核证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_common_unconditional_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-common-unconditional-kernel-router.json

输出：
  data/prime-matrix-two-replacement-lines-common-unconditional-kernel-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-common-unconditional-kernel-router.json
  docs/monograph/prime-matrix-two-replacement-lines-common-unconditional-kernel-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SLUG = "prime-matrix-two-replacement-lines-common-unconditional-kernel"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

NONCYCLE = DOCS / "prime-matrix-two-replacement-lines-noncycle-hard-attack-router.json"
SIXFIELD = DOCS / "prime-matrix-two-replacement-lines-new-joint-sixfield-sync-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"
FULLS_ACCEPT = DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.json"
FULLS_MATRIX = DOCS / "prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json"

ACCEPTED_FULLS = "AcceptedFullSKLSExtExternalContract"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
DSTRUCTURE_SELF = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
FULLS_MATCH = "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch"
FULLS_CAPACITY = "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput"
NEW_AUTOMORPHIC = "NewAutomorphicDispersionProof"
SIX_FIELD = "NewActualJointAlphaDeltaSixFieldConstructorArtifact"
EXACT_CERT = "AcyclicCanonicalExactSameSetPromotionCertificate"
SOURCE_ENTROPY = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
SOURCE_IDENTITY = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab"
ANTIATOM = "FullSNonAPStrengthenedSourceAntiAtomForActualSource"
UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
PDEC_RATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，方便在旧归档上复跑。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书直接依赖。"""
    paths = [
        Path(__file__).resolve(),
        NONCYCLE,
        SIXFIELD,
        DSTRUCTURE,
        FULLS_ACCEPT,
        FULLS_MATRIX,
        PAPER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def external_conditional_basis() -> str:
    """外部引理条件版闭合基。"""
    return f"{ACCEPTED_FULLS} AND {DSTRUCTURE_GATE}"


def external_absolute_basis() -> str:
    """外部线若去掉合同/独立验收条件后的作者侧证明基。"""
    front = f"({FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC})"
    return f"{front} AND {DSTRUCTURE_SELF}"


def internal_self_contained_basis() -> str:
    """内部自足版当前合取基。"""
    front = f"({SIX_FIELD} OR {EXACT_CERT} OR {SOURCE_ENTROPY} OR {SOURCE_IDENTITY} OR {ANTIATOM})"
    return f"{front} AND {UV} AND {HIGH_MODEL} AND {PDEC_RATE} AND {RATE} AND {DSTRUCTURE_SELF}"


def front_gates() -> dict[str, str]:
    """拆出外部谱线、内部 source 线和共同核。"""
    return {
        "external_spectral_front": f"{FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC}",
        "internal_source_front": f"{SIX_FIELD} OR {EXACT_CERT} OR {SOURCE_ENTROPY} OR {SOURCE_IDENTITY} OR {ANTIATOM}",
        "internal_incidence_model_rate_front": f"{UV} AND {HIGH_MODEL} AND {PDEC_RATE} AND {RATE}",
        "common_unconditional_kernel": DSTRUCTURE_SELF,
    }


def row(
    gate: str,
    in_external_absolute: bool,
    in_internal_self_contained: bool,
    paid_currently: bool,
    substitutable_by_other_line: bool,
    meaning: str,
    next_action: str,
) -> dict[str, Any]:
    """构造共同核判定表行。"""
    return {
        "gate": gate,
        "in_external_absolute": in_external_absolute,
        "in_internal_self_contained": in_internal_self_contained,
        "paid_currently": paid_currently,
        "substitutable_by_other_line": substitutable_by_other_line,
        "meaning": meaning,
        "next_action": next_action,
    }


def matrix_rows(dstructure: dict[str, Any], sixfield: dict[str, Any], fulls: dict[str, Any]) -> list[dict[str, Any]]:
    """构造外部绝对版与内部自足版的阻塞核矩阵。"""
    subpackages = dstructure.get("self_contained_author_replacement_subpackages", [])
    sixfield_open = sixfield.get("new_joint_sixfield_artifact_proved") is False
    fulls_primary_open = fulls.get("primary_source_derivation_closed") is False

    return [
        row(
            DSTRUCTURE_SELF,
            True,
            True,
            False,
            False,
            "这是两条绝对无条件路线的交集核；外部谱线和内部 source 线都不能替代它。",
            " AND ".join(subpackages) if subpackages else DSTRUCTURE_SELF,
        ),
        row(
            FULLS_MATCH,
            True,
            False,
            not fulls_primary_open,
            False,
            "它只支付无黑箱外部谱线的同对象主来源 theorem-match；不生成内部 six-field/source 数据。",
            f"{FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC}",
        ),
        row(
            SIX_FIELD,
            False,
            True,
            not sixfield_open,
            False,
            "它只支付内部 pre-Cauchy actual joint alpha/delta 公式；不证明 FullS-KLS 外部谱估计。",
            SIX_FIELD,
        ),
        row(
            f"{UV} AND {HIGH_MODEL} AND {PDEC_RATE} AND {RATE}",
            False,
            True,
            False,
            False,
            "这些是内部自足线的并行承重门；FullS theorem-match 与 DStructure 包均不能吸收它们。",
            f"{UV} AND {HIGH_MODEL} AND {PDEC_RATE} AND {RATE}",
        ),
        row(
            f"{ACCEPTED_FULLS} AND {DSTRUCTURE_GATE}",
            False,
            False,
            True,
            False,
            "这是外部引理条件版的作者侧闭合基；它不是绝对无条件作者证明基。",
            "preserve as conditional external lemma version only",
        ),
    ]


def subpackage_rows(dstructure: dict[str, Any]) -> list[dict[str, Any]]:
    """展开 DStructure/Rankin 自足替代包。"""
    names = dstructure.get(
        "self_contained_author_replacement_subpackages",
        [
            "SelfContainedDStructureStructuredEHPDDefinitionsAndABReductionProof",
            "SelfContainedTailLog4BGOrRKSTailAdapterWithExactTheoremNumbersAndConstants",
            "ReproducibleFiniteVerificationArchiveWithHashesAndIndependentRunner",
            "SelfContainedFullRankinPassOrReturnLedgerAndDownstreamReturnIntegration",
        ],
    )
    meanings = {
        "SelfContainedDStructureStructuredEHPDDefinitionsAndABReductionProof": "D-structure 定义、Structured-EHPD 入口、A/B 到 D 的归约必须写成文内证明。",
        "SelfContainedTailLog4BGOrRKSTailAdapterWithExactTheoremNumbersAndConstants": "Tail-log4 所需外部或替代定理必须给出精确定理号、常数与变量适配。",
        "ReproducibleFiniteVerificationArchiveWithHashesAndIndependentRunner": "阈值以下有限验证必须有脚本哈希、输入域、输出证书和独立 runner。",
        "SelfContainedFullRankinPassOrReturnLedgerAndDownstreamReturnIntegration": "Rankin 全账本必须逐项给出 pass-or-return 与失败回流整合证明。",
    }
    return [
        {
            "subpackage": name,
            "proved": False,
            "common_to_both_absolute_lines": True,
            "meaning": meanings.get(name, "DStructure/Rankin 自足替代包子项。"),
        }
        for name in names
    ]


def build_payload() -> dict[str, Any]:
    """构造共同核证书。"""
    noncycle = read_json(NONCYCLE)
    sixfield = read_json(SIXFIELD)
    dstructure = read_json(DSTRUCTURE)
    fulls = read_json(FULLS_ACCEPT)
    fulls_matrix = read_json(FULLS_MATRIX)
    rows = matrix_rows(dstructure, sixfield, fulls)
    subpackages = subpackage_rows(dstructure)
    gates = front_gates()

    return {
        "certificate_type": "two_replacement_lines_common_unconditional_kernel_router",
        "status": "two_replacement_lines_common_unconditional_kernel_pinned_unconditional_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "noncycle_route_enforced": True,
        "common_unconditional_kernel_boundary_closed": True,
        "common_unconditional_kernel_proved": False,
        "external_conditional_author_side_closed": True,
        "external_absolute_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_conditional_basis": external_conditional_basis(),
        "external_absolute_basis": external_absolute_basis(),
        "internal_self_contained_basis": internal_self_contained_basis(),
        "front_gates": gates,
        "common_kernel": DSTRUCTURE_SELF,
        "common_kernel_subpackages": subpackages,
        "kernel_matrix": rows,
        "substitution_forbidden": [
            "FullS theorem-match cannot discharge six-field/source/ExactUV/model/rate gates.",
            "Six-field/source constructors cannot discharge FullS-KLS spectral theorem-match.",
            "DStructure/Rankin self-contained package cannot discharge either front; it is the shared tail gate.",
            "AcceptedFullSKLSExtExternalContract plus DStructure independent acceptance is a conditional external lemma basis, not an absolute author proof.",
        ],
        "method_discipline": [
            "Euler: source/product identities are generated before pushforward and cannot be recovered from downstream payment.",
            "Gauss: CRT phases, formal-unit keys, and same-set promotion must refer to the identical object.",
            "Riemann: spectral estimates are applied only after signed coefficients and windows have been produced.",
            "Rankin/DStructure: tail promotion is a final common pass-or-return ledger, not a source-construction shortcut.",
        ],
        "next_best_noncycle_moves": [
            {
                "target": DSTRUCTURE_SELF,
                "scope": "advances both external absolute and internal self-contained lines",
                "required": " AND ".join(item["subpackage"] for item in subpackages),
            },
            {
                "target": gates["external_spectral_front"],
                "scope": "advances external no-blackbox line only",
                "required": gates["external_spectral_front"],
            },
            {
                "target": gates["internal_source_front"],
                "scope": "advances internal source front only",
                "required": gates["internal_source_front"],
            },
        ],
        "status_snapshot": {
            "noncycle": noncycle.get("status"),
            "sixfield": sixfield.get("status"),
            "dstructure": dstructure.get("status"),
            "fulls_accept": fulls.get("status"),
            "fulls_matrix": fulls_matrix.get("status"),
        },
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "两条替代线的绝对无条件化共同核不是 FullS 谱输入，也不是 six-field/source 前端，"
            "而是 SelfContainedDStructureTailLog4FiniteRankinProofPackage。"
            "外部无黑箱线还要支付同对象 FullS theorem-match、actual source capacity 或新 automorphic/dispersion 证明；"
            "内部自足线还要支付 six-field/source/canonical 前端以及 ExactUV、模型、PDEC/CleanKLS 与 Rate。"
            "这些门互不代偿；当前闭合的是共同核边界，不是目标命题的无条件证明。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线共同无条件核证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"common_unconditional_kernel_boundary_closed={fmt_bool(payload['common_unconditional_kernel_boundary_closed'])}",
        f"common_unconditional_kernel_proved={fmt_bool(payload['common_unconditional_kernel_proved'])}",
        f"external_conditional_author_side_closed={fmt_bool(payload['external_conditional_author_side_closed'])}",
        f"external_absolute_unconditional_closed={fmt_bool(payload['external_absolute_unconditional_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 共同核矩阵",
        "",
        "| gate | external absolute | internal self-contained | paid currently | substitutable | meaning | next action |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in payload["kernel_matrix"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['in_external_absolute'])}`",
                    f"`{fmt_bool(item['in_internal_self_contained'])}`",
                    f"`{fmt_bool(item['paid_currently'])}`",
                    f"`{fmt_bool(item['substitutable_by_other_line'])}`",
                    cell(item["meaning"]),
                    cell(item["next_action"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 三条基",
            "",
            "外部引理条件版：",
            "",
            "```text",
            payload["external_conditional_basis"],
            "```",
            "",
            "外部绝对无条件作者证明版：",
            "",
            "```text",
            payload["external_absolute_basis"],
            "```",
            "",
            "内部自足版：",
            "",
            "```text",
            payload["internal_self_contained_basis"],
            "```",
            "",
            "## 4. DStructure/Rankin 自足子包",
            "",
            "| subpackage | proved | common | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in payload["common_kernel_subpackages"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["subpackage"]),
                    f"`{fmt_bool(item['proved'])}`",
                    f"`{fmt_bool(item['common_to_both_absolute_lines'])}`",
                    cell(item["meaning"]),
                ]
            )
            + " |"
        )
    lines.extend(["", "## 5. 禁止代偿", ""])
    for item in payload["substitution_forbidden"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 6. 非循环纪律", ""])
    for item in payload["method_discipline"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 7. 下一步主攻", "", "| target | scope | required |", "| --- | --- | --- |"])
    for item in payload["next_best_noncycle_moves"]:
        lines.append(f"| `{cell(item['target'])}` | {cell(item['scope'])} | `{cell(item['required'])}` |")
    lines.extend(["", "## 8. 状态快照", "", "| field | value |", "| --- | --- |"])
    for key, value in payload["status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(["", "## 9. 依赖哈希", "", "| file | sha256 |", "| --- | --- |"])
    for name, digest in payload["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """执行证书生成。"""
    write_outputs(build_payload())


if __name__ == "__main__":
    main()
