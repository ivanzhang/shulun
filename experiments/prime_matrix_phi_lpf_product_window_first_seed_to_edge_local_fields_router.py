#!/usr/bin/env python3
"""归档 product-window first seed 到 edge-local signed fields 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_first_seed_to_edge_local_fields_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-first-seed-to-edge-local-fields-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-first-seed-to-edge-local-fields-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-first-seed-to-edge-local-fields-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-first-seed-to-edge-local-fields-router.md

本证书承接 product-window bucket stack bridge。它不证明三命题无条件闭合，
而是把 `PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward`
继续同步到已存在的 diagonal/offdiagonal、tuple-fields、no-swap 与 edge-local
field-cut 证书，明确哪些 LPF/Phi/Ferrers 无符号字段已经耗尽，哪些 signed
atom 字段仍必须正向给出或进入命名 return。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-first-seed-to-edge-local-fields"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PRODUCT_BRIDGE = DOCS / "prime-matrix-phi-lpf-product-window-bucket-stack-bridge-router.json"
LATEST_SEED_DIAG = DOCS / "prime-matrix-phi-lpf-latest-semiprime-seed-diagonal-sync-router.json"
OFFDIAG_TUPLE = DOCS / "prime-matrix-phi-lpf-offdiagonal-semiprime-seed-tuple-fields-router.json"
NO_SWAP = DOCS / "prime-matrix-phi-lpf-two-prime-ordered-no-swap-router.json"
EDGE_FIELD_CUT = DOCS / "prime-matrix-phi-lpf-edge-local-two-prime-field-cut-router.json"
LATEST_EDGE_FIELD_CUT = DOCS / "prime-matrix-phi-lpf-latest-edge-local-field-cut-sync-router.json"
SIGNED_TRACE_SYNC = DOCS / "prime-matrix-phi-lpf-latest-constructor-signed-atom-trace-sync-router.json"
POINTWISE_FRONTIER = DOCS / "prime-matrix-phi-lpf-pointwise-signed-value-table-frontier-router.json"
EXTERNAL_LIVE = DOCS / "prime-matrix-external-live-frontier-applicability-sync-20260525.json"

BUCKET_LAW = "PhiLPFBucketSignedCoefficientLawBeforePushforward"
FIRST_SEED = "PhiLPFSemiprimeFirstEdgeSignedSeedTableBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
DIAGONAL_SEED = "PhiLPFDiagonalSquareBaseFirstSeedCommonPacketSourceBeforePushforward"
OFFDIAG_SEED = "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"
OFFDIAG_TUPLE_FIELDS = "PhiLPFOffDiagonalSemiprimeSourceTupleFieldLedgerBeforePushforward"
OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
TWO_PRIME_KERNEL = "PhiLPFOffDiagonalTwoPrimeInteractionSignedKernelBeforePushforward"
EDGE_LOCAL_FORMULA = "PhiLPFEdgeLocalTwoPrimeSignedInteractionFormulaOrReturnBeforePushforward"
EDGE_LABEL_LEDGER = "PhiLPFEdgeLocalTwoPrimeClosedUnsignedEdgeLabelLedgerBeforePushforward"
SIGNED_FIELDS = "PhiLPFEdgeLocalTwoPrimeSignedAtomFieldsOrNamedReturnTagBeforePushforward"
TRACE_PAYLOAD = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
TRACE_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"

ALPHA_ANCHOR = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
RANK_CERT = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
SOURCE_ATOMS = f"{ALPHA_ANCHOR} AND {ARITH_ID} AND {RANK_CERT}"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失只能生成 false 诊断，不能当作证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
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
        PRODUCT_BRIDGE,
        LATEST_SEED_DIAG,
        OFFDIAG_TUPLE,
        NO_SWAP,
        EDGE_FIELD_CUT,
        LATEST_EDGE_FIELD_CUT,
        SIGNED_TRACE_SYNC,
        POINTWISE_FRONTIER,
        EXTERNAL_LIVE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def largest_sample(cert: dict[str, Any], key: str) -> dict[str, Any]:
    """抽取样本审计中最大的 N。"""
    samples = cert.get(key, [])
    if not samples:
        return {}
    return max(samples, key=lambda item: item.get("N", 0))


def sync_chain() -> list[dict[str, str]]:
    """列出从 product-window bucket bridge 到 edge-local field-cut 的同步链。"""
    return [
        {
            "from": BUCKET_LAW,
            "to": f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
            "meaning": "product-window bucket bridge 已把递推路线的第一直接硬点压到 first seed 与 internal transition。",
        },
        {
            "from": FIRST_SEED,
            "to": f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
            "meaning": "semiprime first edge 先按 `p=q` 与 `p<q` 唯一拆分。",
        },
        {
            "from": DIAGONAL_SEED,
            "to": SOURCE_ATOMS,
            "meaning": "diagonal square-base lane 没有私有 signed 出口，回到已携带的 source 三原子。",
        },
        {
            "from": OFFDIAG_SEED,
            "to": f"{OFFDIAG_TUPLE_FIELDS} AND {OFFDIAG_SIGNED_FORMULA}",
            "meaning": "offdiagonal occurrence 的 owner、first q 与 q-rough tail 字段闭合；signed seed 公式仍开。",
        },
        {
            "from": TWO_PRIME_KERNEL,
            "to": EDGE_LOCAL_FORMULA,
            "meaning": "two-prime pure kernel 的 swap-symmetry 伪出口已删除，只剩 canonical edge-local formula-or-return。",
        },
        {
            "from": EDGE_LOCAL_FORMULA,
            "to": f"{EDGE_LABEL_LEDGER} AND {SIGNED_FIELDS}",
            "meaning": "edge-local 入口先剥离 LPF/Phi/Ferrers 无符号 label，剩余为 signed atom fields 或命名 return。",
        },
        {
            "from": SIGNED_FIELDS,
            "to": f"{TRACE_PAYLOAD} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {POINTWISE_TABLE}",
            "meaning": "signed fields 若不直接给出，必须进入新 primitive payload/trace、terminal descent、same-set PDEC 或逐点表旁路。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成本轮桥接判定表。"""
    product = data["product"]
    diag = data["diag"]
    tuple_cert = data["tuple"]
    no_swap = data["no_swap"]
    edge = data["edge"]
    latest_edge = data["latest_edge"]
    trace = data["trace"]
    pointwise = data["pointwise"]
    _external = data["external"]
    return [
        row(
            "ProductWindowFirstSeedImported",
            product.get("next_primary_attack_target") == FIRST_SEED
            and product.get("paired_required_attack_target") == INTERNAL_TRANSITION,
            False,
            "product-window bucket bridge 的直接递推负载已经是 first seed 与 internal transition。",
            f"{FIRST_SEED} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "DiagonalOffDiagonalSplitImported",
            diag.get("target_input_before_router") == FIRST_SEED
            and diag.get("next_primary_attack_target") == OFFDIAG_SEED,
            True,
            "FIRST_SEED 可直接接入 diagonal/offdiagonal 拆分。",
            f"{DIAGONAL_SEED} AND {OFFDIAG_SEED}",
        ),
        row(
            "DiagonalPrivateSignedEscapeRemoved",
            diag.get("diagonal_private_escape_removed") is True
            or diag.get("diagonal_square_base_private_signed_escape_removed") is True,
            True,
            "diagonal `(p,p)` 不再提供私有 signed 出口，只能回到 source 三原子。",
            SOURCE_ATOMS,
        ),
        row(
            "OffDiagonalTupleUnsignedFieldsClosed",
            tuple_cert.get("offdiagonal_source_tuple_bijection_proved") is True
            and tuple_cert.get("offdiagonal_phi_tail_fiber_mass_proved") is True
            and tuple_cert.get("offdiagonal_unsigned_tuple_fields_closed") is True,
            True,
            "offdiagonal `(p,q,t)` 的 owner、first q、q-rough tail 与 Phi fiber mass 已闭合。",
            OFFDIAG_TUPLE_FIELDS,
        ),
        row(
            "OffDiagonalSignedFormulaStillOpen",
            tuple_cert.get("offdiagonal_signed_seed_formula_proved") is False,
            False,
            "tuple 的 signed seed value 不能由无符号 Phi mass 反推，必须正向给出公式或 return。",
            OFFDIAG_SIGNED_FORMULA,
        ),
        row(
            "TwoPrimeSwapExitRemoved",
            no_swap.get("lpf_owner_ordered_no_swap_identity_proved") is True
            and no_swap.get("next_primary_attack_target") == EDGE_LOCAL_FORMULA,
            True,
            "`p*q=q*p` 不产生 signed cancellation；LPF owner 域只保留 canonical `(p,q)`。",
            EDGE_LOCAL_FORMULA,
        ),
        row(
            "EdgeLocalUnsignedLabelsClosed",
            edge.get("edge_local_closed_unsigned_label_ledger_proved") is True
            and edge.get("next_primary_attack_target") == SIGNED_FIELDS,
            True,
            "pure edge 的 owner、product、LPF bucket、rank/degree 与 multiplicity-one label 已闭合。",
            EDGE_LABEL_LEDGER,
        ),
        row(
            "LatestEdgeFieldCutSynced",
            latest_edge.get("next_primary_attack_target") == SIGNED_FIELDS
            and latest_edge.get("closed_unsigned_edge_label_ledger_synced") is True,
            True,
            "最新 edge-local sync 已把 formula-or-return 替换为 signed atom fields 或命名 return。",
            SIGNED_FIELDS,
        ),
        row(
            "LPFPhiUnsignedScopeExhausted",
            True,
            True,
            "LPF/Phi/Ferrers 在本层只支付支撑、纤维、tuple 与 edge label，不支付 sign/local factor/orientation。",
            f"{SIGNED_FIELDS} AND {OFFDIAG_ORIENTATION}",
        ),
        row(
            "SignedAtomTracePayloadStillOpen",
            trace.get("next_primary_attack_target") == TRACE_PAYLOAD
            and trace.get("new_primitive_payload_or_trace_artifact_present") is False,
            False,
            "同 trace key 与命名 return 路由可接下 signed fields，但当前没有新 primitive payload/trace 工件。",
            TRACE_PAYLOAD,
        ),
        row(
            "OrientationExactUVInternalStillPaired",
            True,
            False,
            "orientation、ExactUV return 与 internal prime-adjoin transition 是同一 first-seed 路线的配套义务。",
            f"{OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "PointwiseSignedTableStillParallel",
            pointwise.get("pointwise_phi_lpf_bucket_signed_value_table_proved") is False,
            False,
            "逐点 Phi-LPF signed value table 仍是直接旁路，但当前没有证明。",
            POINTWISE_TABLE,
        ),
        row(
            "ExternalInputsStillNeedObject",
            True,
            False,
            "外部 trace/Type-II 或短区间输入仍需先有 signed coefficient 对象或平方根行尺度点态输入。",
            f"{TRACE_BRIDGE} OR {SQRT_INPUT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只同步 product-window first seed 的下游字段切分；没有证明三命题无条件闭合。",
            (
                f"{OFFDIAG_SIGNED_FORMULA} AND {SIGNED_FIELDS} AND {OFFDIAG_ORIENTATION} "
                f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION} AND {SOURCE_ATOMS}"
            ),
        ),
    ]


def field_exhaustion_table() -> list[dict[str, str]]:
    """总结已耗尽的无符号字段与仍开的 signed 字段。"""
    return [
        {
            "field_group": "diagonal square-base",
            "status": "absorbed_to_source_atoms",
            "remaining": SOURCE_ATOMS,
            "meaning": "`p=p` diagonal 不是 first-seed 的私有 signed 出口。",
        },
        {
            "field_group": "offdiagonal tuple owner/fiber",
            "status": "closed_unsigned",
            "remaining": OFFDIAG_TUPLE_FIELDS,
            "meaning": "`(owner_p, first_q, q_rough_tail_t)` 与 Phi tail mass 已闭合。",
        },
        {
            "field_group": "pure two-prime canonical edge label",
            "status": "closed_unsigned",
            "remaining": EDGE_LABEL_LEDGER,
            "meaning": "`owner_p, first_q, pq, rank/degree, multiplicity` 已闭合。",
        },
        {
            "field_group": "tuple signed seed formula",
            "status": "open_signed",
            "remaining": OFFDIAG_SIGNED_FORMULA,
            "meaning": "需要 source tuple 推前前 signed seed 公式。",
        },
        {
            "field_group": "edge-local signed atom fields",
            "status": "open_signed_or_return",
            "remaining": SIGNED_FIELDS,
            "meaning": "需要 signed value、local factor、orientation 入口、ExactUV pair 或命名 return。",
        },
        {
            "field_group": "trace/payload productive exit",
            "status": "open_payload",
            "remaining": TRACE_PAYLOAD,
            "meaning": "需要新的 primitive atomic signed payload/trace 工件，不能由无符号 label 自动生成。",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装 product-window first-seed 到 edge-local fields 证书。"""
    data = {
        "product": load_json(PRODUCT_BRIDGE),
        "diag": load_json(LATEST_SEED_DIAG),
        "tuple": load_json(OFFDIAG_TUPLE),
        "no_swap": load_json(NO_SWAP),
        "edge": load_json(EDGE_FIELD_CUT),
        "latest_edge": load_json(LATEST_EDGE_FIELD_CUT),
        "trace": load_json(SIGNED_TRACE_SYNC),
        "pointwise": load_json(POINTWISE_FRONTIER),
        "external": load_json(EXTERNAL_LIVE),
    }
    rows = build_rows(data)
    tuple_sample = largest_sample(data["tuple"], "sample_offdiagonal_tuple_audit")
    edge_sample = largest_sample(data["edge"], "sample_edge_local_field_audit")
    retained_basis = (
        f"(({SOURCE_ATOMS} AND {OFFDIAG_SIGNED_FORMULA} AND {SIGNED_FIELDS} "
        f"AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}) "
        f"OR {POINTWISE_TABLE} OR {PRIMITIVE_ORIGIN} OR {TRACE_PAYLOAD} "
        f"OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {TRACE_BRIDGE} OR {SQRT_INPUT}) "
        f"AND {EXACTUV_PAIR} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_first_seed_to_edge_local_fields_router",
        "status": "product_window_first_seed_synced_to_edge_local_signed_fields_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "product_window_first_seed_imported": rows[0]["closed"],
        "diagonal_private_signed_escape_removed": rows[2]["closed"],
        "offdiagonal_tuple_unsigned_fields_closed": rows[3]["closed"],
        "offdiagonal_signed_seed_formula_proved": False,
        "two_prime_swap_exit_removed": rows[5]["closed"],
        "edge_local_unsigned_labels_closed": rows[6]["closed"],
        "latest_edge_field_cut_synced": rows[7]["closed"],
        "lpf_phi_unsigned_scope_exhausted": True,
        "signed_atom_field_table_proved": False,
        "new_primitive_payload_or_trace_artifact_present": False,
        "internal_prime_adjoin_signed_transition_law_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": FIRST_SEED,
        "next_primary_attack_target": SIGNED_FIELDS,
        "tuple_level_required_attack_target": OFFDIAG_SIGNED_FORMULA,
        "paired_required_attack_targets": [
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            SOURCE_ATOMS,
        ],
        "parallel_attack_targets": [
            POINTWISE_TABLE,
            PRIMITIVE_ORIGIN,
            TRACE_PAYLOAD,
            TERMINAL_DESCENT,
            PDEC_SCOPE,
            TRACE_BRIDGE,
            SQRT_INPUT,
        ],
        "latest_retained_basis_after_router": retained_basis,
        "sync_chain": sync_chain(),
        "field_exhaustion_table": field_exhaustion_table(),
        "sample_readouts": {
            "offdiagonal_tuple_largest_sample": tuple_sample,
            "edge_local_largest_sample": edge_sample,
        },
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Product-window 的 first-edge semiprime seed 已同步到更窄的 edge-local signed "
            "fields 前沿。diagonal `(p,p)` 被 source 三原子吸收；offdiagonal `(p,q,t)` "
            "的 LPF/Phi tuple 与 tail fiber 是无符号闭合账本；pure `(p,q)` edge 的 "
            "owner、product、rank/degree 与 multiplicity label 也已闭合。剩余不再是 "
            "LPF/Phi 支撑或容量问题，而是 tuple-level signed seed formula、edge-local "
            "signed atom fields 或命名 return，并且仍要携带 orientation、ExactUV、internal "
            "prime-adjoin transition 与 source 三原子。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window first seed to edge-local fields 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"product_window_first_seed_imported={fmt_bool(cert['product_window_first_seed_imported'])}",
        f"diagonal_private_signed_escape_removed={fmt_bool(cert['diagonal_private_signed_escape_removed'])}",
        f"offdiagonal_tuple_unsigned_fields_closed={fmt_bool(cert['offdiagonal_tuple_unsigned_fields_closed'])}",
        f"edge_local_unsigned_labels_closed={fmt_bool(cert['edge_local_unsigned_labels_closed'])}",
        f"lpf_phi_unsigned_scope_exhausted={fmt_bool(cert['lpf_phi_unsigned_scope_exhausted'])}",
        f"signed_atom_field_table_proved={fmt_bool(cert['signed_atom_field_table_proved'])}",
        f"new_primitive_payload_or_trace_artifact_present={fmt_bool(cert['new_primitive_payload_or_trace_artifact_present'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        f"tuple_level_required_attack_target={cert['tuple_level_required_attack_target']}",
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

    lines.extend(
        [
            "",
            "## 3. 字段耗尽表",
            "",
            "| field group | status | remaining | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in cert["field_exhaustion_table"]:
        lines.append(
            f"| {cell(item['field_group'])} | `{cell(item['status'])}` | "
            f"{cell(item['remaining'])} | {cell(item['meaning'])} |"
        )

    tuple_sample = cert["sample_readouts"]["offdiagonal_tuple_largest_sample"]
    edge_sample = cert["sample_readouts"]["edge_local_largest_sample"]
    lines.extend(
        [
            "",
            "## 4. 最大样本读数",
            "",
            "| source | N | count A | count B | ok | note |",
            "| --- | ---: | ---: | ---: | --- | --- |",
        ]
    )
    if tuple_sample:
        lines.append(
            "| offdiagonal tuple | "
            f"{tuple_sample.get('N')} | {tuple_sample.get('offdiagonal_tuple_occurrences')} | "
            f"{tuple_sample.get('offdiagonal_phi_fiber_formula_sum')} | "
            f"`{fmt_bool(tuple_sample.get('tuple_phi_bijection_holds'))}` | "
            "tuple occ equals Phi tail fiber sum |"
        )
    if edge_sample:
        label_ok = all(
            edge_sample.get(key)
            for key in [
                "lpf_bucket_identity_holds",
                "row_degree_formula_holds",
                "column_degree_formula_holds",
                "atom_multiplicity_one_holds",
            ]
        )
        lines.append(
            "| edge-local label | "
            f"{edge_sample.get('N')} | {edge_sample.get('canonical_edges')} | "
            f"{edge_sample.get('unique_edge_labels')} | `{fmt_bool(label_ok)}` | "
            "canonical edges equal unique closed labels |"
        )

    lines.extend(
        [
            "",
            "## 5. 最新保留基",
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
            "tuple 层仍需：",
            "",
            "```text",
            cert["tuple_level_required_attack_target"],
            "```",
            "",
            "配套仍需：",
            "",
            "```text",
            "\n".join(cert["paired_required_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
    print(f"product_window_first_seed_imported={fmt_bool(cert['product_window_first_seed_imported'])}")
    print(f"offdiagonal_tuple_unsigned_fields_closed={fmt_bool(cert['offdiagonal_tuple_unsigned_fields_closed'])}")
    print(f"edge_local_unsigned_labels_closed={fmt_bool(cert['edge_local_unsigned_labels_closed'])}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
