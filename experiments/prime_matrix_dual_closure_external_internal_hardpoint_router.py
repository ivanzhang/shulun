#!/usr/bin/env python3
"""生成外部引理版与内部自足版的双闭合硬点路由证书。

用法示例：
  python3 experiments/prime_matrix_dual_closure_external_internal_hardpoint_router.py
  python3 -m json.tool docs/monograph/prime-matrix-dual-closure-external-internal-hardpoint-router.json

输出：
  data/prime-matrix-dual-closure-external-internal-hardpoint-ledger.json
  docs/monograph/prime-matrix-dual-closure-external-internal-hardpoint-router.json
  docs/monograph/prime-matrix-dual-closure-external-internal-hardpoint-router.md
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

SLUG = "prime-matrix-dual-closure-external-internal-hardpoint"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

FULLS_ACCEPT = DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
FULLS_MATCH = DOCS / "prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json"
TRUE_REMAINDER = DOCS / "prime-matrix-fulls-theorem-match-true-remainder-cut-router.json"
HP_RESET = DOCS / "prime-matrix-hp-cramer-local-route-reset-router.json"
ENDPOINT_DIFF = DOCS / "prime-matrix-phi-lpf-endpoint-interval-difference-router.json"
CLEAN_CORE_MOVING = DOCS / "prime-matrix-clean-core-moving-atom-sharp-input-router.json"
EXTERNAL_PARAM = DOCS / "prime-matrix-clean-core-external-lemma-parameter-match-router.json"
FINAL_GUARD = DOCS / "prime-matrix-final-guard-gate-completion-verdict-router.json"
LOGIC_CHAIN = DOCS / "prime-matrix-final-proof-logic-chain-status-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"


EXTERNAL_PACKAGE = (
    "AcceptedFullSKLSExtExternalContract AND "
    "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
)

SELF_CONTAINED_PACKAGE = (
    "ActualNoncanonicalCleanCoreMovingAtomExclusion AND "
    "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
)

FINE_INTERNAL_SOURCE_PACKAGE = (
    "AlphaRowAnchorPhaseEmissionFormulaLedger AND "
    "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND "
    "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND "
    "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward AND "
    "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward AND "
    "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND "
    "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger AND "
    "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND "
    "FixedKeyExactUVLocalMultiplicityO1Ledger"
)


def read_json(path: Path) -> dict[str, Any]:
    """读取依赖 JSON；缺失依赖只会降低本证书的证明强度。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为 Markdown 友好的小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格中的竖线。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    boundary_closed: bool,
    proved_or_accepted: bool,
    lane: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造双闭合判定表行。"""
    return {
        "gate": gate,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "lane": lane,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """列出本层依赖证书。"""
    return [
        FULLS_ACCEPT,
        DSTRUCTURE,
        FULLS_MATCH,
        TRUE_REMAINDER,
        HP_RESET,
        ENDPOINT_DIFF,
        CLEAN_CORE_MOVING,
        EXTERNAL_PARAM,
        FINAL_GUARD,
        LOGIC_CHAIN,
        CLAIM_STATUS,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖文件哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成外部版和自足版的真剩余表。"""
    fulls_accept = data["fulls_accept"]
    dstructure = data["dstructure"]
    hp_reset = data["hp_reset"]
    endpoint = data["endpoint"]
    clean_core = data["clean_core"]
    external_param = data["external_param"]
    final_guard = data["final_guard"]
    logic_chain = data["logic_chain"]
    return [
        row(
            "PhiLPFEndpointIdentityDemotedToExactCounter",
            endpoint.get("endpoint_difference_identity_proved") is True
            and endpoint.get("interval_positivity_from_identity_alone_proved") is False,
            True,
            "common_guard",
            "Phi-LPF/LPF 端点差公式给精确计数表达式，但不产生短区间正性。",
            "需要 signed/phase/capacity 正性输入。",
        ),
        row(
            "HPCramerLocalBarrierAccepted",
            hp_reset.get("review_core_accepted") is True
            and hp_reset.get("hp_direct_unconditional_closure_claim_allowed") is False,
            True,
            "common_guard",
            "最坏 strict 顶端带是 x≈P^2、长度 P≈sqrt(x) 的 Cramer-local/Legendre 尺度。",
            "ExactExternalSqrtScaleOrFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof.",
        ),
        row(
            "ReadyMadePrimarySourceNotFound",
            True,
            False,
            "external_no_blackbox",
            "FI/DI/BFI/Maynard/自守 L 函数方向必须逐项 theorem-match；现有主来源未直接推出当前 non-AP full-S WFD 目标。",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch or NewAutomorphicDispersionProof.",
        ),
        row(
            "FullSKLSExtContractMatched",
            fulls_accept.get("strict_contract_match") is True
            and fulls_accept.get("external_math_lane_closed_after_acceptance") is True,
            fulls_accept.get("accepted_as_external_blackbox_input") is True,
            "external_lemma",
            "FullS-KLS-ext 作为外部黑箱合同已按对象、权重、窗口、模数、投影边界和 log 节省逐项匹配。",
            "仍需最终 DStructure/Tail-log4/finite Rankin 独立接受。",
        ),
        row(
            "DStructureRankinPromotionBoundaryClosedNotAccepted",
            dstructure.get("promotion_package_boundary_closed") is True,
            dstructure.get("promotion_package_independently_accepted") is True,
            "external_lemma_and_internal",
            "晋级包边界、Rankin pass-or-return 与作者侧证据包已封装；当前材料没有独立接受事件。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.",
        ),
        row(
            "ExternalLemmaVersionLogicallyClosedUnderPackage",
            fulls_accept.get("external_math_lane_closed_after_acceptance") is True
            and dstructure.get("promotion_package_boundary_closed") is True,
            False,
            "external_lemma",
            "若把 FullS-KLS-ext 与最终晋级包都作为外部引理/独立验收输入，则反例链闭合。",
            EXTERNAL_PACKAGE,
        ),
        row(
            "ExternalLemmaVersionUnconditionalFromCurrentCorpus",
            logic_chain.get("conditional_external_kls_proof_chain_closed") is True,
            logic_chain.get("row_column_unconditional_closed") is True,
            "external_lemma",
            "当前仓库达到的是条件闭合链；没有把独立验收门删掉。",
            "obtain explicit independent acceptance or prove a replacement package.",
        ),
        row(
            "ExternalLemmasDoNotCloseSelfContainedConstructor",
            external_param.get("external_lemmas_close_self_contained_remainder") is False,
            False,
            "internal_self_contained",
            "DI/BFI/Kuznetsov 处理 completion 后的谱平均，不能生成 pre-Cauchy actual noncanonical summand emitter。",
            "prove the actual noncanonical signed source/constructor package internally.",
        ),
        row(
            "CleanCoreMovingAtomSharpInputPinned",
            clean_core.get("clean_core_moving_atom_sharp_boundary_closed") is True,
            clean_core.get("clean_core_moving_atom_exclusion_proved") is True,
            "internal_self_contained",
            "自足源侧高层硬点已校准为 clean-core final-capacity moving atom 排斥。",
            "ActualNoncanonicalCleanCoreMovingAtomExclusion.",
        ),
        row(
            "FineSignedSourceTableObligationPinned",
            True,
            False,
            "internal_self_contained",
            "继续展开 moving/source 原子后，真正需要的是同 formal unit 的 pre-Cauchy signed emitter 与 Phi-LPF edge signed tables。",
            FINE_INTERNAL_SOURCE_PACKAGE,
        ),
        row(
            "SelfContainedPromotionReplacementPinned",
            final_guard.get("self_contained_promotion_package_proved") is False,
            False,
            "internal_self_contained",
            "若不使用独立验收事件，DStructure/Tail-log4/finite Rankin 还必须被替换为完全自足证明包。",
            "SelfContainedDStructureTailLog4FiniteRankinProofPackage.",
        ),
        row(
            "DualOverclaimFirewallClosed",
            True,
            True,
            "common_guard",
            "外部引理版、主来源无黑箱版、内部自足版被分离；任何闭合都必须携带自己的输入包。",
            "no hidden renaming through Phi-LPF or generic WFD.",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 Markdown 判定表。"""
    lines = [
        "| gate | lane | boundary closed | proved/accepted | meaning | remaining |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {gate} | `{lane}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                lane=cell(item["lane"]),
                closed=fmt_bool(item["boundary_closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造双闭合硬点 payload。"""
    data = {
        "fulls_accept": read_json(FULLS_ACCEPT),
        "dstructure": read_json(DSTRUCTURE),
        "hp_reset": read_json(HP_RESET),
        "endpoint": read_json(ENDPOINT_DIFF),
        "clean_core": read_json(CLEAN_CORE_MOVING),
        "external_param": read_json(EXTERNAL_PARAM),
        "final_guard": read_json(FINAL_GUARD),
        "logic_chain": read_json(LOGIC_CHAIN),
    }
    rows = build_rows(data)
    external_logically_closed = all(
        row_item["boundary_closed"]
        for row_item in rows
        if row_item["gate"]
        in {
            "PhiLPFEndpointIdentityDemotedToExactCounter",
            "HPCramerLocalBarrierAccepted",
            "FullSKLSExtContractMatched",
            "DStructureRankinPromotionBoundaryClosedNotAccepted",
            "ExternalLemmaVersionLogicallyClosedUnderPackage",
        }
    )
    external_unconditional_current = any(
        row_item["gate"] == "ExternalLemmaVersionUnconditionalFromCurrentCorpus"
        and row_item["proved_or_accepted"]
        for row_item in rows
    )
    internal_self_contained_closed = all(
        row_item["proved_or_accepted"]
        for row_item in rows
        if row_item["lane"] == "internal_self_contained"
    )
    return {
        "certificate_type": "prime_matrix_dual_closure_external_internal_hardpoint_router",
        "status": "dual_closure_split_external_conditional_closed_internal_self_contained_open",
        "review_core_absorbed": True,
        "phi_lpf_exactness_is_counting_not_positivity": True,
        "external_lemma_package_basis": EXTERNAL_PACKAGE,
        "external_lemma_version_logically_closed_under_package": external_logically_closed,
        "external_lemma_unconditional_from_current_corpus": external_unconditional_current,
        "no_blackbox_primary_source_basis": (
            "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
            "NewAutomorphicDispersionProof) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "internal_self_contained_theorem_level_basis": SELF_CONTAINED_PACKAGE,
        "internal_self_contained_fine_source_basis": FINE_INTERNAL_SOURCE_PACKAGE,
        "internal_self_contained_closed_from_current_corpus": internal_self_contained_closed,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "next_true_hardpoints": [
            "For external-lemma final theorem: obtain explicit independent acceptance of DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance.",
            "For no-blackbox external theorem: prove ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch or a new automorphic/dispersion theorem for the exact non-AP full-S WFD object.",
            "For internal self-contained theorem: prove the clean-core signed-source package, beginning with offdiagonal semiprime seed and internal prime-adjoin signed transition tables.",
            "For fully self-contained promotion: prove SelfContainedDStructureTailLog4FiniteRankinProofPackage instead of relying on referee acceptance.",
        ],
        "plain_conclusion": (
            "外部引理版可以严格写成条件闭合：接受 FullS-KLS-ext 外部合同并接受 "
            "DStructure/Tail-log4/finite Rankin 晋级包后，反例链无剩余数学出口。"
            "但这不是当前语料库的无条件证明，因为最终晋级包尚未独立接受。"
            "内部自足版仍未闭合；Phi-LPF/LPF 端点差和桶恒等式只提供精确计数，"
            "不能跨越短区间正性/奇偶屏障。自足路线必须新增 signed source/constructor "
            "与 self-contained promotion 证明包。"
        ),
        "source_hashes": source_hashes(),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lines = [
        "# Prime Matrix 外部引理版/内部自足版双闭合硬点路由器",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 核心判定",
        "",
        "```text",
        f"external_lemma_version_logically_closed_under_package={fmt_bool(payload['external_lemma_version_logically_closed_under_package'])}",
        f"external_lemma_unconditional_from_current_corpus={fmt_bool(payload['external_lemma_unconditional_from_current_corpus'])}",
        f"internal_self_contained_closed_from_current_corpus={fmt_bool(payload['internal_self_contained_closed_from_current_corpus'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 外部引理版闭合包",
        "",
        "```text",
        payload["external_lemma_package_basis"],
        "```",
        "",
        "含义：把 `FullS-KLS-ext` 与最终 DStructure/Tail-log4/finite Rankin 晋级包都作为外部引理或独立验收输入时，逻辑链闭合。当前仓库没有把这两个输入全部变成无条件内部证明。",
        "",
        "## 3. 内部自足版当前硬点",
        "",
        "定理层硬点：",
        "",
        "```text",
        payload["internal_self_contained_theorem_level_basis"],
        "```",
        "",
        "细化后的 source 侧硬点：",
        "",
        "```text",
        payload["internal_self_contained_fine_source_basis"],
        "```",
        "",
        "## 4. 双路判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 5. 下一真硬点",
        "",
    ]
    for item in payload["next_true_hardpoints"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## 6. 结论",
            "",
            payload["plain_conclusion"],
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
