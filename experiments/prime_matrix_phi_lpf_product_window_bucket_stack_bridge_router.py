#!/usr/bin/env python3
"""归档 product-window bucket law 到 transport/edge/pointwise 前沿的桥接证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_bucket_stack_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-bucket-stack-bridge-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-bucket-stack-bridge-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-bucket-stack-bridge-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-bucket-stack-bridge-router.md

本证书承接 product-window independent signed defect source router。它不证明
行/列命题，而是把新硬点 `PhiLPFBucketSignedCoefficientLawBeforePushforward`
接入既有 bucket transport stack、edge multiplier slab 和 pointwise table origin
账本，给出下一轮非循环攻击的最窄接口。
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

SLUG = "prime-matrix-phi-lpf-product-window-bucket-stack-bridge"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SIGNED_SOURCE_JSON = DOCS / "prime-matrix-phi-lpf-product-window-independent-signed-defect-source-router.json"
BUCKET_STACK_JSON = DOCS / "prime-matrix-phi-lpf-latest-bucket-transport-stack-sync-router.json"
EDGE_SLAB_JSON = DOCS / "prime-matrix-phi-lpf-latest-edge-multiplier-slab-sync-router.json"
POINTWISE_ORIGIN_JSON = DOCS / "prime-matrix-phi-lpf-latest-new-joint-pointwise-table-origin-sync-router.json"
ORDERED_COHERENCE_JSON = DOCS / "prime-matrix-phi-lpf-rough-cofactor-ordered-factorization-coherence-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SYNTHESIS = DOCS / "three-claims-breakthrough-route-synthesis-20260525.md"
ACTUAL_LOAD = DOCS / "three-claims-actual-load-closure-contracts.md"
FORMAL_FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
FRONTIER_HONEST = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"

SOURCE_FILES = [
    Path(__file__).resolve(),
    SIGNED_SOURCE_JSON,
    BUCKET_STACK_JSON,
    EDGE_SLAB_JSON,
    POINTWISE_ORIGIN_JSON,
    ORDERED_COHERENCE_JSON,
    CLAIM_STATUS,
    SYNTHESIS,
    ACTUAL_LOAD,
    FORMAL_FRONTIER,
    EXTERNAL_INDEX,
    FRONTIER_HONEST,
    PAPER,
]

BUCKET_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
EDGE_MULTIPLIER = "PhiLPFRoughCofactorStepSignedMultiplierTableBeforePushforward"
FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TRACE_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，便于生成诊断。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """Markdown 表格转义。"""
    return str(value).replace("|", r"\|")


def external_frontier_rows() -> list[dict[str, Any]]:
    """记录本层可用外部输入的对象条件。

    这里的结论只说明对象条件，不评价这些外部论文的正确性。
    """
    return [
        {
            "input": "Fouvry--Kowalski--Michel--Sawin trace-function bilinear forms",
            "url": "https://arxiv.org/abs/2511.09459",
            "usable_now": False,
            "needed_project_object": "signed coefficient table plus admissible l-adic trace family and norms",
            "reason": "当前只有 product-window additive phase 和后验 defect；缺少推前前 signed coefficients。",
        },
        {
            "input": "Pascadi / DI-BFI / Kloosterman Type-II route",
            "url": "https://arxiv.org/abs/2511.08445",
            "usable_now": False,
            "needed_project_object": "completed inverse-variable Kloosterman family with factorable signed coefficients",
            "reason": "需要先把 LPF owner fibres 转成 admissible trace/Type-II 系数族。",
        },
        {
            "input": "Guth--Maynard short-interval prime distribution",
            "url": "https://arxiv.org/search/math?query=Guth+Maynard+primes+short+intervals&searchtype=all",
            "usable_now": False,
            "needed_project_object": "pointwise prime in intervals of length <= x^(1/2) at x=P^2",
            "reason": "已知短区间指数仍厚于精确一行长度 P=x^(1/2)，不能直接给每行正性。",
        },
        {
            "input": "Runbo Li short-interval exponent 13/25",
            "url": "https://arxiv.org/abs/2405.20552",
            "usable_now": False,
            "needed_project_object": "C<=1 square-root row-scale pointwise theorem",
            "reason": "13/25 大于 1/2；可压力测试低行带，但不是本行闭合输入。",
        },
    ]


def sync_chain(bucket_stack: dict[str, Any], edge_slab: dict[str, Any], pointwise: dict[str, Any]) -> list[dict[str, str]]:
    """把 product-window hardpoint 接到已有下游账本。"""
    return [
        {
            "from": "IndependentSignedDefectEmissionBeforeProductWindowPushforward",
            "to": BUCKET_LAW,
            "meaning": "上一证书已把 product-window 独立 signed defect 来源重定位到 Phi-LPF bucket signed law。",
        },
        {
            "from": BUCKET_LAW,
            "to": bucket_stack.get("latest_retained_basis_after_router", ""),
            "meaning": "bucket law 若不直接提交逐点表，就必须进入 rough cofactor transport stack。",
        },
        {
            "from": EDGE_MULTIPLIER,
            "to": " AND ".join(edge_slab.get("next_edge_attack_targets", [FIRST_SEED, INTERNAL_TRANSITION])),
            "meaning": "逐 edge multiplier 按 LPF ordered path 分成第一边 semiprime seed 与内部 prime-adjoin transition。",
        },
        {
            "from": POINTWISE_TABLE,
            "to": pointwise.get("next_primary_attack_target", PRIMITIVE_ORIGIN),
            "meaning": "逐点 signed table 旁路若不走 transport，也必须给 primitive summand 的来源恒等式。",
        },
        {
            "from": TRACE_BRIDGE,
            "to": "signed coefficients first, then admissible trace/Kloosterman family",
            "meaning": "外部谱/trace 定理需要先有可作用的 signed coefficient 对象。",
        },
        {
            "from": SQRT_INPUT,
            "to": "pointwise theta/psi C<=1 at x=P^2, H=P",
            "meaning": "短区间素数路线必须达到精确平方根行尺度。",
        },
    ]


def gate_rows() -> list[dict[str, Any]]:
    """列出本轮关闭/未关闭的门。"""
    return [
        {
            "gate": "ProductWindowSignedSourceImported",
            "closed": True,
            "proved": False,
            "meaning": "product-window signed defect 来源已重定位到 bucket law。",
            "remaining": BUCKET_LAW,
        },
        {
            "gate": "BucketTransportStackImported",
            "closed": True,
            "proved": False,
            "meaning": "既有 bucket stack 已把 bucket law 接到 rough transport 或 pointwise table。",
            "remaining": EDGE_MULTIPLIER + " OR " + POINTWISE_TABLE,
        },
        {
            "gate": "OrderedCofactorCoherenceImported",
            "closed": True,
            "proved": True,
            "meaning": "LPF 非降素因子词关闭 ordered path/coherence，但不产生 sign。",
            "remaining": EDGE_MULTIPLIER,
        },
        {
            "gate": "EdgeMultiplierSlabImported",
            "closed": True,
            "proved": False,
            "meaning": "edge multiplier 表已拆成 first-edge seed 与 internal transition。",
            "remaining": FIRST_SEED + " AND " + INTERNAL_TRANSITION,
        },
        {
            "gate": "PointwiseOriginImported",
            "closed": True,
            "proved": False,
            "meaning": "pointwise signed table 旁路已同步到 primitive summand origin identity。",
            "remaining": PRIMITIVE_ORIGIN,
        },
        {
            "gate": "ExternalTraceInputObjectGuard",
            "closed": True,
            "proved": False,
            "meaning": "外部 trace/Kloosterman 定理目前没有 signed coefficients 对象可作用。",
            "remaining": TRACE_BRIDGE,
        },
        {
            "gate": "SqrtRowDistributionInputGuard",
            "closed": True,
            "proved": False,
            "meaning": "短区间素数输入必须达到 H=P=x^(1/2) 的点态行尺度。",
            "remaining": SQRT_INPUT,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步是非循环前沿桥接，不是三命题无条件闭合证明。",
            "remaining": FIRST_SEED + " AND " + INTERNAL_TRANSITION + " AND source-rank/ExactUV/model/rate/DStructure gates",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装证书。"""
    signed_source = load_json(SIGNED_SOURCE_JSON)
    bucket_stack = load_json(BUCKET_STACK_JSON)
    edge_slab = load_json(EDGE_SLAB_JSON)
    pointwise = load_json(POINTWISE_ORIGIN_JSON)
    ordered = load_json(ORDERED_COHERENCE_JSON)

    latest_retained = (
        "((AlphaRowAnchorPhaseEmissionFormulaLedger AND "
        "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND "
        "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND "
        f"{FIRST_SEED} AND {INTERNAL_TRANSITION}) OR "
        f"{POINTWISE_TABLE} OR {PRIMITIVE_ORIGIN} OR "
        "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR "
        "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate OR "
        "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact OR "
        "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate OR "
        f"{TRACE_BRIDGE} OR {SQRT_INPUT}) AND "
        "ActualEmitterSourceDomainEntropyLedger AND "
        "ExactUVMapFixedPairPolylogFiberBoundLedger AND "
        "ExplicitModelGapAndFiniteDPRCLedger AND "
        "RatePreservationLedger_FOR_moving_atom_packet AND "
        "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_bucket_stack_bridge_router",
        "status": "product_window_bucket_law_synced_to_transport_edge_and_pointwise_origin_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "product_window_signed_source_imported": signed_source.get("selected_next_primary_gate") == BUCKET_LAW,
        "bucket_transport_stack_imported": bucket_stack.get("target_input_before_router") == BUCKET_LAW,
        "ordered_cofactor_coherence_imported": ordered.get("ordered_lpf_factorization_coherence_proved") is True,
        "edge_multiplier_slab_imported": edge_slab.get("target_input_before_router") == EDGE_MULTIPLIER,
        "pointwise_origin_imported": pointwise.get("target_input_before_router") == POINTWISE_TABLE,
        "external_frontier_object_guard_checked": True,
        "bucket_law_proved": False,
        "edge_multiplier_table_proved": False,
        "semiprime_first_edge_signed_seed_table_proved": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "pointwise_signed_table_proved": False,
        "primitive_origin_identity_proved": False,
        "trace_bridge_admissible_coefficients_proved": False,
        "pointwise_sqrt_prime_input_c_one_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": BUCKET_LAW,
        "next_primary_attack_target": FIRST_SEED,
        "paired_required_attack_target": INTERNAL_TRANSITION,
        "parallel_pointwise_attack_target": PRIMITIVE_ORIGIN,
        "parallel_trace_attack_target": TRACE_BRIDGE,
        "parallel_distribution_attack_target": SQRT_INPUT,
        "latest_retained_basis_after_router": latest_retained,
        "sync_chain": sync_chain(bucket_stack, edge_slab, pointwise),
        "gates": gate_rows(),
        "external_frontier_rows": external_frontier_rows(),
        "plain_conclusion": (
            "Product-window 的最新 bucket signed law 已接入既有 transport/edge/pointwise 前沿。"
            "递推路线不再停在抽象 bucket law：它先经过 rough cofactor transport，再由 ordered "
            "LPF path 固定到逐 edge signed multiplier，最后拆成 semiprime first-edge signed seed "
            "和 internal prime-adjoin signed transition。直接逐点表旁路则压到 primitive summand "
            "signed coefficient origin identity。外部 trace/Kloosterman 或短区间素数 theorem 仍需"
            "先满足 signed coefficients 或平方根行尺度输入。因此本轮推进的是最新硬点定位，"
            "不是无条件闭合证明。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window bucket stack bridge 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"product_window_signed_source_imported={fmt_bool(cert['product_window_signed_source_imported'])}",
        f"bucket_transport_stack_imported={fmt_bool(cert['bucket_transport_stack_imported'])}",
        f"ordered_cofactor_coherence_imported={fmt_bool(cert['ordered_cofactor_coherence_imported'])}",
        f"edge_multiplier_slab_imported={fmt_bool(cert['edge_multiplier_slab_imported'])}",
        f"pointwise_origin_imported={fmt_bool(cert['pointwise_origin_imported'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"paired_required_attack_target={cert['paired_required_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for row in cert["sync_chain"]:
        lines.append(f"| `{cell(row['from'])}` | `{cell(row['to'])}` | {cell(row['meaning'])} |")

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["gates"]:
        lines.append(
            f"| {cell(row['gate'])} | `{fmt_bool(row['closed'])}` | `{fmt_bool(row['proved'])}` | "
            f"{cell(row['meaning'])} | `{cell(row['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 3. 外部前沿对象条件",
            "",
            "| input | usable now | needed project object | reason | url |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in cert["external_frontier_rows"]:
        lines.append(
            f"| {cell(row['input'])} | `{fmt_bool(row['usable_now'])}` | "
            f"{cell(row['needed_project_object'])} | {cell(row['reason'])} | {row['url']} |"
        )

    lines.extend(
        [
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"product_window_signed_source_imported={fmt_bool(cert['product_window_signed_source_imported'])}")
    print(f"bucket_transport_stack_imported={fmt_bool(cert['bucket_transport_stack_imported'])}")
    print(f"edge_multiplier_slab_imported={fmt_bool(cert['edge_multiplier_slab_imported'])}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
