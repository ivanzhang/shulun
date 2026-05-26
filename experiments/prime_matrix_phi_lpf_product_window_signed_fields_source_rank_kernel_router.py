#!/usr/bin/env python3
"""归档 product-window signed fields 到 source-rank kernel 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_signed_fields_source_rank_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-signed-fields-source-rank-kernel-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-signed-fields-source-rank-kernel-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-signed-fields-source-rank-kernel-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-signed-fields-source-rank-kernel-router.md

本证书承接 product-window first-seed 到 edge-local fields 路由。它把
`PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward`
接入已有 signed atom trace-sync、new-payload source-atom alignment 与
post-antisplit source-rank convergence。结论是：signed fields 的匿名缺口被
命名 return 矩阵吸收，生产性出口不能停在 `NewPrimitive...` 名称上，而必须回到
actual pre-Cauchy source-rank/no-collapse 与共同 pointwise kernel。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-signed-fields-source-rank-kernel"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PRODUCT_FIELDS = DOCS / "prime-matrix-phi-lpf-product-window-first-seed-to-edge-local-fields-router.json"
LATEST_TRACE = DOCS / "prime-matrix-phi-lpf-latest-signed-atom-trace-sync-router.json"
LATEST_PAYLOAD = DOCS / "prime-matrix-phi-lpf-latest-new-payload-source-atom-alignment-sync-router.json"
STRICT_NEW_PAYLOAD = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
POST_ANTISPLIT = DOCS / "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"
POINTWISE_FRONTIER = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXACTUV_CERT = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"
EXTERNAL_LIVE = DOCS / "prime-matrix-external-live-frontier-applicability-sync-20260525.json"

SIGNED_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
TRACE_SYNC = "PhiLPFEdgeLocalSignedAtomSameTraceKeyAndNamedReturnMatrixBeforePushforward"
NEW_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
POINTWISE_BASIS = f"{ALPHA_ROW} AND {ARITH_ID} AND {SAME_UNIT_RANK}"

OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
TRACE_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失只作为未导入处理。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PRODUCT_FIELDS,
        LATEST_TRACE,
        LATEST_PAYLOAD,
        STRICT_NEW_PAYLOAD,
        POST_ANTISPLIT,
        POINTWISE_FRONTIER,
        EXACTUV_CERT,
        EXTERNAL_LIVE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出本轮非循环同步链。"""
    return [
        {
            "from": SIGNED_FIELDS,
            "to": TRACE_SYNC,
            "meaning": "edge-local signed value、local factor、orientation、ExactUV 与 source row 必须同属一个 pre-Cauchy trace key。",
        },
        {
            "from": TRACE_SYNC,
            "to": f"{NEW_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}",
            "meaning": "命名 return 矩阵关闭匿名缺口；生产性出口是 new payload，非生产性出口必须命名。",
        },
        {
            "from": NEW_PAYLOAD,
            "to": SOURCE_RANK,
            "meaning": "new primitive payload 若不是环内改名，必须携带 actual pre-Cauchy source-rank/no-collapse 包。",
        },
        {
            "from": SOURCE_RANK,
            "to": f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
            "meaning": "source-rank/no-collapse 包实际拆成 source entropy、complete key 与 fixed-key ExactUV local multiplicity。",
        },
        {
            "from": f"{DOMAIN_ENTROPY} / {COMPLETE_KEY} / {FIXED_KEY}",
            "to": POINTWISE_KERNEL,
            "meaning": "内部 source-rank 路线在同 formal-unit 的 primitive alpha/delta pointwise kernel 上汇合。",
        },
        {
            "from": POINTWISE_KERNEL,
            "to": POINTWISE_BASIS,
            "meaning": "共同核表的当前第一硬点是 alpha row anchor/phase emission，并行还需 pre-Cauchy 算术恒等式与同表 rank/multiplicity。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成本轮判定表。"""
    product = data["product"]
    latest_trace = data["latest_trace"]
    latest_payload = data["latest_payload"]
    strict_payload = data["strict_payload"]
    post = data["post"]
    pointwise = data["pointwise"]
    exactuv = data["exactuv"]
    return [
        row(
            "ProductWindowSignedFieldsImported",
            product.get("next_primary_attack_target") == SIGNED_FIELDS,
            False,
            "上一层 product-window first-seed 路由已把直接 signed 硬点定位到 edge-local signed atom fields。",
            SIGNED_FIELDS,
        ),
        row(
            "LatestTraceSyncImported",
            latest_trace.get("target_input_before_router") == SIGNED_FIELDS
            and latest_trace.get("next_primary_attack_target") == NEW_PAYLOAD,
            True,
            "已有 latest signed atom trace-sync 可直接作用在 product-window signed fields 入口。",
            TRACE_SYNC,
        ),
        row(
            "SameTraceKeyAndNamedReturnMatrixSynced",
            latest_trace.get("same_trace_key_and_named_return_matrix_synced") is True,
            True,
            "跨 key、缺失、冲突、零因子、超预算或后验读取均进入命名 return，不再是匿名缺口。",
            TRACE_SYNC,
        ),
        row(
            "NewPayloadSourceAtomAlignmentImported",
            latest_payload.get("target_input_before_router") == NEW_PAYLOAD
            and latest_payload.get("absorbed_to") == SOURCE_RANK,
            False,
            "`NewPrimitive...` 已接到 source-atom alignment，不再能作为未解释的新黑箱。",
            SOURCE_RANK,
        ),
        row(
            "StrictPayloadIndependentTerminalRejected",
            strict_payload.get("aggregate", {}).get("new_primitive_artifact_independent_terminal_present")
            is False,
            True,
            "当前语料没有独立 new primitive 工件；若只是 signed-lane 环内改名则不能破环。",
            SOURCE_RANK,
        ),
        row(
            "SourceRankPackageAtomized",
            latest_payload.get("latest_new_payload_reduced_to_source_rank_atom") is True
            and post.get("source_rank_package_atomized") is True,
            False,
            "source-rank/no-collapse 包被拆成 source entropy、complete key 与 fixed-key local multiplicity。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY}",
        ),
        row(
            "PostAntisplitConvergenceImported",
            post.get("new_primitive_exit_absorbed_to_source_rank") is True
            and post.get("next_direct_attack_target") == ALPHA_ROW,
            False,
            "new payload 与 terminal descent 的内部路线在 pointwise kernel 后收敛到 alpha row anchor。",
            POINTWISE_BASIS,
        ),
        row(
            "ProductWindowTupleSignedFormulaStillPaired",
            product.get("tuple_level_required_attack_target") == OFFDIAG_SIGNED_FORMULA,
            False,
            "本步只吸收 edge-local signed fields；tuple-level signed seed formula 仍是 product-window first-seed 配套硬点。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "OrientationExactUVInternalStillPaired",
            True,
            False,
            "orientation、ExactUV return 与 internal prime-adjoin transition 仍是同一 product-window first-seed 路线的配套义务。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "PointwiseSignedTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed table 仍是直接旁路，但当前未证明。",
            POINTWISE_TABLE,
        ),
        row(
            "ExactUVAndExternalInputStillIndependent",
            exactuv.get("nonterminal_exactuv_fiber_aperiodicity_proved") is False,
            False,
            "ExactUV/source entropy 与外部 trace 或平方根行尺度输入不能由本 trace-sync 自动推出。",
            f"{EXACTUV_PAIR} AND ({TRACE_BRIDGE} OR {SQRT_INPUT} OR {EXTERNAL_SPECTRAL})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 product-window signed fields 吸收到 source-rank/pointwise-kernel 前沿；未证明三命题无条件闭合。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {POINTWISE_BASIS} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
    ]


def largest_slot_sample(latest_trace: dict[str, Any]) -> dict[str, Any]:
    """抽取 latest trace-sync 的最大 slot 样本。"""
    return latest_trace.get("imported_largest_slot_sample", {})


def build_certificate() -> dict[str, Any]:
    """组装 product-window signed fields 到 source-rank kernel 证书。"""
    data = {
        "product": load_json(PRODUCT_FIELDS),
        "latest_trace": load_json(LATEST_TRACE),
        "latest_payload": load_json(LATEST_PAYLOAD),
        "strict_payload": load_json(STRICT_NEW_PAYLOAD),
        "post": load_json(POST_ANTISPLIT),
        "pointwise": load_json(POINTWISE_FRONTIER),
        "exactuv": load_json(EXACTUV_CERT),
        "external": load_json(EXTERNAL_LIVE),
    }
    rows = build_rows(data)
    retained = (
        f"(({OFFDIAG_SIGNED_FORMULA} AND {POINTWISE_BASIS} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}) OR {POINTWISE_TABLE} "
        f"OR {PRIMITIVE_ORIGIN} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} "
        f"OR {TRACE_BRIDGE} OR {SQRT_INPUT} OR {EXTERNAL_SPECTRAL}) "
        f"AND {EXACTUV_PAIR} AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_signed_fields_source_rank_kernel_router",
        "status": "product_window_signed_fields_synced_to_source_rank_kernel_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "product_window_signed_fields_imported": rows[0]["closed"],
        "latest_trace_sync_imported": rows[1]["closed"],
        "same_trace_key_and_named_return_matrix_synced": rows[2]["closed"],
        "new_payload_source_atom_alignment_imported": rows[3]["closed"],
        "strict_payload_independent_terminal_rejected": rows[4]["closed"],
        "source_rank_package_atomized": rows[5]["closed"],
        "post_antisplit_convergence_imported": rows[6]["closed"],
        "edge_local_signed_atom_fields_proved": False,
        "new_primitive_payload_or_trace_artifact_present": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SIGNED_FIELDS,
        "absorbed_to": SOURCE_RANK,
        "next_primary_attack_target": ALPHA_ROW,
        "parallel_direct_attack_targets": [
            ARITH_ID,
            SAME_UNIT_RANK,
            OFFDIAG_SIGNED_FORMULA,
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            POINTWISE_TABLE,
            TRACE_BRIDGE,
            SQRT_INPUT,
        ],
        "latest_retained_basis_after_router": retained,
        "sync_chain": sync_chain(),
        "imported_largest_slot_sample": largest_slot_sample(data["latest_trace"]),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window 的 `PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward` "
            "接入已有 signed atom trace-sync 与 source-rank convergence。无符号 edge label 只给输入域；"
            "signed fields 必须同属一个 pre-Cauchy trace key，否则进入命名 return。生产性出口 "
            "`NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 也不能作为未解释黑箱保留，必须携带 "
            "actual pre-Cauchy source-rank/no-collapse 包，并在共同 pointwise kernel 后落到 "
            "`AlphaRowAnchorPhaseEmissionFormulaLedger`、pre-Cauchy 算术恒等式与同表 rank/multiplicity。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window signed fields source-rank kernel 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"product_window_signed_fields_imported={fmt_bool(cert['product_window_signed_fields_imported'])}",
        f"latest_trace_sync_imported={fmt_bool(cert['latest_trace_sync_imported'])}",
        f"same_trace_key_and_named_return_matrix_synced={fmt_bool(cert['same_trace_key_and_named_return_matrix_synced'])}",
        f"new_payload_source_atom_alignment_imported={fmt_bool(cert['new_payload_source_atom_alignment_imported'])}",
        f"strict_payload_independent_terminal_rejected={fmt_bool(cert['strict_payload_independent_terminal_rejected'])}",
        f"source_rank_package_atomized={fmt_bool(cert['source_rank_package_atomized'])}",
        f"post_antisplit_convergence_imported={fmt_bool(cert['post_antisplit_convergence_imported'])}",
        f"edge_local_signed_atom_fields_proved={fmt_bool(cert['edge_local_signed_atom_fields_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(cert['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in cert["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    sample = cert.get("imported_largest_slot_sample", {})
    if sample:
        lines.extend(
            [
                "",
                "## 3. 导入 slot 样本",
                "",
                "| N | canonical edges | open signed slots | trace packets |",
                "| --- | ---: | ---: | ---: |",
                (
                    f"| {sample['N']} | {sample['canonical_edges']} | "
                    f"{sample['open_signed_field_slots']} | {sample['same_trace_packets_required']} |"
                ),
            ]
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
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(cert["parallel_direct_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
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
    print(f"product_window_signed_fields_imported={fmt_bool(cert['product_window_signed_fields_imported'])}")
    print(f"latest_trace_sync_imported={fmt_bool(cert['latest_trace_sync_imported'])}")
    print(f"source_rank_package_atomized={fmt_bool(cert['source_rank_package_atomized'])}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
