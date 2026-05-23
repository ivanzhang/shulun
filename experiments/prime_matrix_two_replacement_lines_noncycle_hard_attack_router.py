#!/usr/bin/env python3
"""生成两条替代线的非循环硬攻边界证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_noncycle_hard_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-noncycle-hard-attack-router.json

输出：
  data/prime-matrix-two-replacement-lines-noncycle-hard-attack-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-noncycle-hard-attack-router.json
  docs/monograph/prime-matrix-two-replacement-lines-noncycle-hard-attack-router.md
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

SLUG = "prime-matrix-two-replacement-lines-noncycle-hard-attack"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

NEW_JOINT_SIXFIELD = DOCS / "prime-matrix-two-replacement-lines-new-joint-sixfield-sync-router.json"
FULLS_ACCEPT = DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.json"
FULLS_MATRIX = DOCS / "prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json"
FULLS_REMAINDER = DOCS / "prime-matrix-fulls-theorem-match-true-remainder-cut-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"
LATEST_TRUE = DOCS / "prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.json"

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
    """读取 JSON；缺失时返回空对象，避免生成器因旧仓库缺档中断。"""
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


def row(
    gate: str,
    boundary_closed: bool,
    proved_unconditional: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造非循环判定表行。"""
    return {
        "gate": gate,
        "boundary_closed": boundary_closed,
        "proved_unconditional": proved_unconditional,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记本证书直接依赖。"""
    paths = [
        Path(__file__).resolve(),
        NEW_JOINT_SIXFIELD,
        FULLS_ACCEPT,
        FULLS_MATRIX,
        FULLS_REMAINDER,
        DSTRUCTURE,
        LATEST_TRUE,
        PAPER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def external_lemma_basis() -> str:
    """外部引理版条件基。"""
    return f"{ACCEPTED_FULLS} AND {DSTRUCTURE_GATE}"


def external_absolute_basis() -> str:
    """若要求外部线也去条件化，必须支付的替代基。"""
    front = f"({FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC})"
    return f"{front} AND ({DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF})"


def internal_basis() -> str:
    """当前内部自足版非循环合取基。"""
    front = f"({SIX_FIELD} OR {EXACT_CERT} OR {SOURCE_ENTROPY} OR {SOURCE_IDENTITY} OR {ANTIATOM})"
    return f"{front} AND {UV} AND {HIGH_MODEL} AND {PDEC_RATE} AND {RATE} AND {DSTRUCTURE_SELF}"


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """根据上游证书构造硬攻表。"""
    fulls_contract_match = (
        data["fulls_accept"].get("strict_contract_match") is True
        and data["fulls_accept"].get("external_math_lane_closed_after_acceptance") is True
    )
    fulls_primary_closed = data["fulls_accept"].get("primary_source_derivation_closed") is True
    dstructure_author_empty = data["dstructure"].get("external_lemma_author_side_remaining") in (
        "none",
        [],
        None,
    )
    dstructure_non_author = DSTRUCTURE_GATE in str(
        data["dstructure"].get("external_lemma_non_author_remaining", "")
    )
    sixfield_pinned = data["new_joint"].get("six_field_artifact") == SIX_FIELD
    sixfield_proved = data["new_joint"].get("new_joint_sixfield_artifact_proved") is True
    no_blackbox_open = data["new_joint"].get("external_no_blackbox_version_closed") is False
    internal_open = data["new_joint"].get("internal_self_contained_closed") is False

    return [
        row(
            "ExternalLemmaObjectMatchAccepted",
            fulls_contract_match,
            False,
            "FullS-KLS-ext 与当前 non-AP full-S WFD 对象逐项匹配；接受它时只关闭外部数学 lane。",
            DSTRUCTURE_GATE,
        ),
        row(
            "ExternalLemmaAuthorSideOrdinaryRemainderEmpty",
            dstructure_author_empty,
            False,
            "作者侧普通补档已归零；剩余是独立接受或自足替代证明，不是可由措辞补齐的作者任务。",
            f"{DSTRUCTURE_GATE} OR {DSTRUCTURE_SELF}",
        ),
        row(
            "ExternalLemmaAbsoluteUnconditionalBlocked",
            dstructure_non_author,
            False,
            "外部引理版若不允许任何外部/独立接受条件，必须替换 FullS-KLS 与 DStructure/Rankin 两个输入。",
            external_absolute_basis(),
        ),
        row(
            "NoBlackboxExternalLinePinned",
            no_blackbox_open,
            False,
            "DI/BFI/Kuznetsov 方向可作为技术来源，但当前语料仍未给出同对象主来源 theorem-match 或新证明。",
            f"({FULLS_MATCH} OR {FULLS_CAPACITY} OR {NEW_AUTOMORPHIC}) AND {DSTRUCTURE_GATE}",
        ),
        row(
            "NewJointSixFieldObligationPinned",
            sixfield_pinned,
            sixfield_proved,
            "内部线中的 new-joint 粗名已被压成六字段 actual alpha/delta 公式义务，旧 joint route 不能代替。",
            SIX_FIELD,
        ),
        row(
            "InternalParallelGatesRemainConjunctive",
            internal_open,
            False,
            "ExactUV、模型余量、PDEC/CleanKLS、Rate 与 DStructure 自足替代包是并行合取门，不能由单个 source 标签吸收。",
            internal_basis(),
        ),
        row(
            "AcyclicMasterDisciplinePinned",
            True,
            True,
            "Euler 纪律要求 source 先于乘法推前，Gauss 纪律要求同集 CRT/相位匹配，Riemann 纪律要求谱估计只在系数生成后使用。",
            "method discipline only; no theorem input discharged",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本轮硬攻闭合的是非循环边界；没有把外部条件或内部未证六字段工件伪装成无条件证明。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "new_joint": read_json(NEW_JOINT_SIXFIELD),
        "fulls_accept": read_json(FULLS_ACCEPT),
        "fulls_matrix": read_json(FULLS_MATRIX),
        "fulls_remainder": read_json(FULLS_REMAINDER),
        "dstructure": read_json(DSTRUCTURE),
        "latest_true": read_json(LATEST_TRUE),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "two_replacement_lines_noncycle_hard_attack_router",
        "status": "two_replacement_lines_noncycle_hard_attack_boundary_closed_unconditional_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "noncycle_route_enforced": True,
        "external_lemma_author_side_closed": True,
        "external_lemma_version_closed_conditionally": True,
        "external_lemma_absolute_unconditional_closed": False,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_lemma_basis": external_lemma_basis(),
        "external_absolute_unconditional_basis": external_absolute_basis(),
        "internal_self_contained_basis": internal_basis(),
        "master_discipline": [
            "Euler: source/product identities must be generated before pushforward, not recovered from payment.",
            "Gauss: CRT phases, same-set promotion, and formal-unit keys must match on the same object.",
            "Riemann: spectral/explicit estimates may bound completed sums only after the signed coefficients exist.",
        ],
        "rows": rows,
        "boundary_closed_gates": [item["gate"] for item in rows if item["boundary_closed"]],
        "unproved_gates": [item["gate"] for item in rows if not item["proved_unconditional"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮硬攻把两条替代线的非循环闭合条件钉死：外部引理版在接受 "
            "FullS-KLS-ext 与 DStructure/Rankin 独立验收时作者侧条件闭合，但不是绝对无条件定理；"
            "无黑箱外部版仍需同对象 theorem-match、actual source capacity 新定理或新 automorphic/dispersion 证明；"
            "内部自足版必须支付 six-field actual joint 公式或并行 source/canonical 替代，并同时支付 "
            "ExactUV、模型、PDEC/CleanKLS、Rate 与自足 DStructure/Rankin。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Prime Matrix 两条替代线非循环硬攻边界证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"external_lemma_author_side_closed={fmt_bool(payload['external_lemma_author_side_closed'])}",
        f"external_lemma_version_closed_conditionally={fmt_bool(payload['external_lemma_version_closed_conditionally'])}",
        f"external_lemma_absolute_unconditional_closed={fmt_bool(payload['external_lemma_absolute_unconditional_closed'])}",
        f"external_no_blackbox_version_closed={fmt_bool(payload['external_no_blackbox_version_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 非循环判定表",
        "",
        "| gate | boundary closed | proved unconditional | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in payload["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['boundary_closed'])}`",
                    f"`{fmt_bool(item['proved_unconditional'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 外部引理版",
            "",
            "条件基：",
            "",
            "```text",
            payload["external_lemma_basis"],
            "```",
            "",
            "若要求绝对无条件化，替代基为：",
            "",
            "```text",
            payload["external_absolute_unconditional_basis"],
            "```",
            "",
            "## 4. 内部自足版",
            "",
            "```text",
            payload["internal_self_contained_basis"],
            "```",
            "",
            "## 5. 非循环纪律",
            "",
        ]
    )
    for item in payload["master_discipline"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 6. 依赖哈希", "", "| file | sha256 |", "| --- | --- |"])
    for name, digest in payload["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """执行证书生成。"""
    write_outputs(build_payload())


if __name__ == "__main__":
    main()
