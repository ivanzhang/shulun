#!/usr/bin/env python3
"""归档 product-window alpha/kernel 前沿桥接证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_alpha_kernel_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-alpha-kernel-frontier-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-alpha-kernel-frontier-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-alpha-kernel-frontier-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-alpha-kernel-frontier-router.md

本证书承接 product-window signed fields source-rank kernel 路由。它把该路由留下的
`AlphaRowAnchorPhaseEmissionFormulaLedger` 接入 strict alpha row formula 的终端前沿同步，
并把 product-window 当前硬点改写为：alpha 局部公式不再是独立非终端出口，剩余必须携带
全局 PDEC/CleanKLS 终端门、模型余量、DStructure/Rankin 验收，同时保留 pre-Cauchy
算术恒等式、同表 rank/multiplicity 与 product-window offdiagonal 三个配套字段。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-alpha-kernel-frontier"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PRODUCT_KERNEL = DOCS / "prime-matrix-phi-lpf-product-window-signed-fields-source-rank-kernel-router.json"
POINTWISE_KERNEL = DOCS / "prime-matrix-strict-pointwise-primitive-kernel-table-router.json"
SAME_UNIT_ATTACK = DOCS / "prime-matrix-strict-same-formal-unit-kernel-identity-attack-router.json"
ALPHA_TERMINAL = DOCS / "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json"
ALPHA_FORMULA = DOCS / "prime-matrix-strict-alpha-row-anchor-phase-formula-router.json"
ALPHA_SIGNED_SYNC = DOCS / "prime-matrix-strict-alpha-formula-signed-lift-terminal-sync-router.json"
ALPHA_WEIGHT = DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json"
EXTERNAL_LIVE = DOCS / "prime-matrix-external-live-frontier-applicability-sync-20260525.json"

ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
ARITH_ID = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
POINTWISE_TABLE = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"

OFFDIAG_SIGNED_FORMULA = "PhiLPFOffDiagonalOrderedSemiprimeSourceTupleSignedSeedFormulaBeforePushforward"
OFFDIAG_ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
OFFDIAG_EXACTUV = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
PHI_LPF_POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
PRIMITIVE_ORIGIN = "PrimitiveSummandSignedCoefficientOriginIdentityBeforePushforward"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
TRACE_BRIDGE = "ProductWindowToCompletedKloostermanOrTraceBridgeWithSignedDefectAndAdmissibleCoefficients"
SQRT_INPUT = "PointwiseSqrtPrimeInputCOne"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时按未导入处理。"""
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
    """登记本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PRODUCT_KERNEL,
        POINTWISE_KERNEL,
        SAME_UNIT_ATTACK,
        ALPHA_TERMINAL,
        ALPHA_FORMULA,
        ALPHA_SIGNED_SYNC,
        ALPHA_WEIGHT,
        EXTERNAL_LIVE,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """列出 product-window alpha/kernel 的非循环同步链。"""
    return [
        {
            "from": "product-window signed fields source-rank kernel",
            "to": f"{ALPHA_ROW} AND {ARITH_ID} AND {SAME_UNIT_RANK}",
            "meaning": "上一 product-window 证书把 edge-local signed fields 吸收到共同 pointwise kernel 三原子。",
        },
        {
            "from": POINTWISE_TABLE,
            "to": f"{ALPHA_ROW} AND {ARITH_ID} AND {SAME_UNIT_RANK}",
            "meaning": "strict pointwise kernel 表明 alpha row、pre-Cauchy 权重恒等式、same-unit rank 必须同表给出。",
        },
        {
            "from": ALPHA_ROW,
            "to": f"{GLOBAL_TERMINAL} AND {MODEL} AND {DSTRUCTURE}",
            "meaning": "alpha row 局部分支已同步到全局终端门；这不是 alpha 证明，而是删除独立局部出口。",
        },
        {
            "from": "product-window current basis",
            "to": "terminal alpha gate plus parallel product-window/offdiagonal gates",
            "meaning": "替换 alpha 局部字段后仍必须保留 offdiagonal signed formula、orientation、ExactUV 与 internal transition。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成桥接判定表。"""
    product = data["product"]
    pointwise = data["pointwise"]
    same_unit = data["same_unit"]
    alpha_terminal = data["alpha_terminal"]
    alpha_formula = data["alpha_formula"]
    signed_sync = data["signed_sync"]
    alpha_weight = data["alpha_weight"]
    return [
        row(
            "ProductWindowAlphaAnchorImported",
            product.get("next_primary_attack_target") == ALPHA_ROW,
            False,
            "上一轮 product-window source-rank kernel 的直接主攻点确为 alpha row anchor/phase emission。",
            ALPHA_ROW,
        ),
        row(
            "PointwiseKernelThreeAtomBasisImported",
            pointwise.get("next_direct_attack_target") == ALPHA_ROW
            and pointwise.get("pointwise_primitive_kernel_table_proved") is False,
            False,
            "逐点 primitive 核表当前等价于 alpha row、pre-Cauchy 算术恒等式和 same-unit rank/multiplicity 三项。",
            f"{ALPHA_ROW} AND {ARITH_ID} AND {SAME_UNIT_RANK}",
        ),
        row(
            "SameFormalUnitKernelAttackImported",
            same_unit.get("next_direct_attack_target") == POINTWISE_TABLE
            and same_unit.get("same_formal_unit_kernel_identity_proved") is False,
            False,
            "同 formal-unit 核恒等式已归约到逐点核表；formal-unit/no-loss 账本不产生 signed coefficient value。",
            POINTWISE_TABLE,
        ),
        row(
            "AlphaFormulaSplitRegistered",
            alpha_formula.get("terminal_gap_before_router") == ALPHA_ROW
            and alpha_formula.get("alpha_row_anchor_phase_emission_formula_proved") is False,
            False,
            "alpha row 公式已拆成变量绑定、carry-shell 同余、phase-wheel、signed lift 和 overload return 五项。",
            alpha_formula.get("terminal_gap_after_router", ALPHA_ROW),
        ),
        row(
            "AlphaSignedLiftTerminalReturnImported",
            signed_sync.get("signed_lift_branch_recycles_to_terminal_gap") is True
            and signed_sync.get("alpha_formula_signed_coefficient_lift_proved") is False,
            False,
            "signed-lift 分支经 signed weight、pre-Cauchy identity、moving-block/NC-BLK 回流到终端容量/模型账本。",
            f"{GLOBAL_TERMINAL} AND {MODEL}",
        ),
        row(
            "AlphaWeightIdentityStillNotStandaloneProof",
            alpha_weight.get("next_direct_attack_target") == ARITH_ID
            and alpha_weight.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False,
            False,
            "alpha 权重律仍要求独立 pre-Cauchy 算术恒等式；它不能由 LPF/Phi survivor mass 或 payment 反推。",
            ARITH_ID,
        ),
        row(
            "AlphaLocalFrontierSyncedToTerminal",
            alpha_terminal.get("alpha_row_formula_local_frontier_synced_to_terminal") is True
            and alpha_terminal.get("next_direct_attack_target") == GLOBAL_TERMINAL,
            False,
            "alpha 局部几何分支已同步到终端门；product-window 可删除 alpha 作为独立非终端停靠点。",
            f"{GLOBAL_TERMINAL} AND {MODEL} AND {DSTRUCTURE}",
        ),
        row(
            "IndependentIdentityAndRankStillParallel",
            True,
            False,
            "alpha 局部终端同步不自动证明 pointwise kernel 的 pre-Cauchy identity 或 same-unit ExactUV rank/multiplicity。",
            f"{ARITH_ID} AND {SAME_UNIT_RANK}",
        ),
        row(
            "ProductWindowTupleAndTransportStillParallel",
            True,
            False,
            "product-window 自身还必须证明 offdiagonal tuple signed formula、orientation、ExactUV return 和 internal prime-adjoin transition。",
            f"{OFFDIAG_SIGNED_FORMULA} AND {OFFDIAG_ORIENTATION} AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}",
        ),
        row(
            "ExternalSpectralToolsStillNeedSignedFamily",
            True,
            False,
            "谱/trace/Type-II 工具仍需先有 admissible signed coefficient family；短区间素数输入仍需 sharp sqrt-scale pointwise row。",
            f"{TRACE_BRIDGE} OR {SQRT_INPUT} OR {EXTERNAL_SPECTRAL}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把 product-window alpha 入口继续下钻到终端前沿；未证明三命题无条件闭合。",
            f"{GLOBAL_TERMINAL} AND {MODEL} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 product-window alpha/kernel 前沿桥接证书。"""
    data = {
        "product": load_json(PRODUCT_KERNEL),
        "pointwise": load_json(POINTWISE_KERNEL),
        "same_unit": load_json(SAME_UNIT_ATTACK),
        "alpha_terminal": load_json(ALPHA_TERMINAL),
        "alpha_formula": load_json(ALPHA_FORMULA),
        "signed_sync": load_json(ALPHA_SIGNED_SYNC),
        "alpha_weight": load_json(ALPHA_WEIGHT),
        "external": load_json(EXTERNAL_LIVE),
    }
    rows = build_rows(data)
    alpha_terminal_imported = next(
        item["closed"] for item in rows if item["gate"] == "AlphaLocalFrontierSyncedToTerminal"
    )
    retained = (
        f"(({OFFDIAG_SIGNED_FORMULA} AND {GLOBAL_TERMINAL} AND {MODEL} AND {DSTRUCTURE} "
        f"AND {ARITH_ID} AND {SAME_UNIT_RANK} AND {OFFDIAG_ORIENTATION} "
        f"AND {OFFDIAG_EXACTUV} AND {INTERNAL_TRANSITION}) OR {PHI_LPF_POINTWISE_TABLE} "
        f"OR {PRIMITIVE_ORIGIN} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {TRACE_BRIDGE} "
        f"OR {SQRT_INPUT} OR {EXTERNAL_SPECTRAL}) AND {EXACTUV_PAIR} AND {RATE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_alpha_kernel_frontier_router",
        "status": "product_window_alpha_kernel_frontier_synced_to_terminal_gate_open",
        "verified_date": "2026-05-26",
        "same_theorem_target_preserved": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "product_window_alpha_anchor_imported": rows[0]["closed"],
        "pointwise_kernel_three_atom_basis_imported": rows[1]["closed"],
        "same_formal_unit_kernel_attack_imported": rows[2]["closed"],
        "alpha_signed_lift_terminal_return_imported": rows[4]["closed"],
        "alpha_local_frontier_synced_to_terminal": alpha_terminal_imported,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncanonical_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "trace_or_typeii_admissible_signed_family_proved": False,
        "pointwise_sqrt_prime_input_c_one_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": ALPHA_ROW,
        "absorbed_to": f"{GLOBAL_TERMINAL} AND {MODEL} AND {DSTRUCTURE}",
        "next_primary_attack_target": GLOBAL_TERMINAL,
        "parallel_direct_attack_targets": [
            ARITH_ID,
            SAME_UNIT_RANK,
            OFFDIAG_SIGNED_FORMULA,
            OFFDIAG_ORIENTATION,
            OFFDIAG_EXACTUV,
            INTERNAL_TRANSITION,
            PHI_LPF_POINTWISE_TABLE,
            TRACE_BRIDGE,
            SQRT_INPUT,
        ],
        "latest_retained_basis_after_router": retained,
        "sync_chain": sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 product-window source-rank kernel 留下的 `AlphaRowAnchorPhaseEmissionFormulaLedger` "
            "接入 strict alpha row formula 终端前沿。alpha 的 unsigned carry-shell/phase 局部分支已闭合，"
            "signed-lift 分支经权重律与 pre-Cauchy identity 回流到终端容量/模型账本，overload 进入命名 return；"
            "因此 product-window 路线不应继续停在 alpha 局部字段名上，而应把该入口改写为 "
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`、模型余量和 DStructure/Rankin 验收。"
            "这仍不是无条件闭合证明，因为 pre-Cauchy 算术恒等式、same-unit rank/multiplicity、"
            "offdiagonal signed formula、orientation、ExactUV 与 internal transition 仍未证明。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window alpha/kernel frontier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        f"**核验日期：** `{cert['verified_date']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"product_window_alpha_anchor_imported={fmt_bool(cert['product_window_alpha_anchor_imported'])}",
        f"pointwise_kernel_three_atom_basis_imported={fmt_bool(cert['pointwise_kernel_three_atom_basis_imported'])}",
        f"same_formal_unit_kernel_attack_imported={fmt_bool(cert['same_formal_unit_kernel_attack_imported'])}",
        f"alpha_signed_lift_terminal_return_imported={fmt_bool(cert['alpha_signed_lift_terminal_return_imported'])}",
        f"alpha_local_frontier_synced_to_terminal={fmt_bool(cert['alpha_local_frontier_synced_to_terminal'])}",
        f"pdec_cap_or_internal_clean_kls_large_sieve_proved={fmt_bool(cert['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}",
        f"independent_noncanonical_precauchy_arithmetic_identity_statement_proved={fmt_bool(cert['independent_noncanonical_precauchy_arithmetic_identity_statement_proved'])}",
        f"same_unit_exact_uv_rank_multiplicity_certificate_proved={fmt_bool(cert['same_unit_exact_uv_rank_multiplicity_certificate_proved'])}",
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
    lines.extend(
        [
            "",
            "## 3. 最新保留基",
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
            "## 4. 依赖哈希",
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
    print(f"product_window_alpha_anchor_imported={fmt_bool(cert['product_window_alpha_anchor_imported'])}")
    print(f"alpha_local_frontier_synced_to_terminal={fmt_bool(cert['alpha_local_frontier_synced_to_terminal'])}")
    print(f"next_primary_attack_target={cert['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
