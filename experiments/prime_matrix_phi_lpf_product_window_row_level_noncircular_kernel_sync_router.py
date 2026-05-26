#!/usr/bin/env python3
"""归档 product-window row-level 表到 noncircular signed kernel 的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_product_window_row_level_noncircular_kernel_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-product-window-row-level-noncircular-kernel-sync-router.json

输出：
  data/prime-matrix-phi-lpf-product-window-row-level-noncircular-kernel-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-product-window-row-level-noncircular-kernel-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-product-window-row-level-noncircular-kernel-sync-router.md

本证书承接 product-window signed-expression origin-table sync。它把当前第一硬点
`RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands`
接入 strict row-level origin-generation router、strict signed-source fixed-point breaker
和 latest constructor row-level fixed-point sync。结论是：row-level 表名仍是粗口；
删除 signed-source 自证固定点后，真正非循环输入是 pre-Cauchy signed coefficient
emission kernel。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-product-window-row-level-noncircular-kernel-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-phi-lpf-product-window-signed-expression-origin-table-sync-router.json"
ROW_LEVEL_ROUTER = DOCS / "prime-matrix-strict-row-level-origin-generation-table-router.json"
SIGNED_SOURCE_FIXED_POINT_ROUTER = DOCS / "prime-matrix-strict-signed-source-fixed-point-breaker-router.json"
LATEST_CONSTRUCTOR_ROW_LEVEL_ROUTER = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-row-level-signed-source-fixed-point-sync-router.json"
)

ROW_TABLE = "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands"
ACYCLIC_SEED_EMITTER = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedWithSignedRowEmitterAndPrepushforwardSumIdentity"
NONCIRCULAR_KERNEL = "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows"
NONZERO_SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
ACYCLIC_SOURCE_SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
SAME_SET_PDEC = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_O1 = "FixedKeyExactUVLocalMultiplicityO1Ledger"
ORIENTATION = "PhiLPFOffDiagonalSemiprimeOrientationParityAndBranchSideLawBeforePushforward"
EXACTUV_RETURN = "PhiLPFOffDiagonalSemiprimeExactUVFixedPairAndReturnTagLedgerBeforePushforward"
INTERNAL_TRANSITION = "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
TERMINAL_RETURN = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """布尔值小写输出。"""
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
    """登记依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        PREVIOUS,
        ROW_LEVEL_ROUTER,
        SIGNED_SOURCE_FIXED_POINT_ROUTER,
        LATEST_CONSTRUCTOR_ROW_LEVEL_ROUTER,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_sync_chain() -> list[dict[str, str]]:
    """列出 row-level 表到 noncircular kernel 的同步链。"""
    return [
        {
            "from": ROW_TABLE,
            "to": ACYCLIC_SEED_EMITTER,
            "meaning": "逐行原始生成表必须由无环 pre-Cauchy seed signed-row emitter 正向产生。",
        },
        {
            "from": ACYCLIC_SEED_EMITTER,
            "to": "signed source spine -> basis word -> assignment -> value map -> origin identity -> row table",
            "meaning": "现有内部展开回到同一 row-level 表，形成 signed-source 固定点。",
        },
        {
            "from": "fixed point rejected as proof",
            "to": NONCIRCULAR_KERNEL,
            "meaning": "删除自证环后，必须提交不读取 row table/payment/来源恒等式的 pre-Cauchy signed kernel。",
        },
        {
            "from": "missing kernel or failed local factor",
            "to": TERMINAL_RETURN,
            "meaning": "若 kernel、非零局部因子或作用域失败，必须进入命名终端回流。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    previous = data["previous"]
    row_level = data["row_level"]
    fixed_point = data["fixed_point"]
    latest = data["latest"]

    previous_active = (
        previous.get("next_primary_attack_target") == ROW_TABLE
        and previous.get("product_window_signed_expression_removed_from_first_target") is True
    )
    row_level_imported = (
        row_level.get("row_level_origin_generation_table_router_closed") is True
        and row_level.get("next_direct_attack_target") == ACYCLIC_SEED_EMITTER
        and row_level.get("row_level_clean_core_origin_generation_table_proved") is False
    )
    fixed_point_imported = (
        fixed_point.get("signed_source_fixed_point_breaker_closed") is True
        and fixed_point.get("current_internal_route_is_signed_source_fixed_point") is True
        and fixed_point.get("next_direct_attack_target") == NONCIRCULAR_KERNEL
    )
    latest_imported = (
        latest.get("row_level_coarse_target_removed") is True
        and latest.get("signed_source_fixed_point_cut_imported") is True
        and latest.get("next_primary_attack_target") == NONCIRCULAR_KERNEL
    )
    reverse_blocked = (
        fixed_point.get("reverse_and_zero_row_recovery_blocked") is True
        and latest.get("reverse_payment_and_zero_row_recovery_blocked") is True
    )

    return [
        row(
            "ProductWindowRowLevelTargetActiveBeforeSync",
            previous_active,
            False,
            "上一层 product-window 同步把第一硬点推进到 row-level clean-core 原始生成表。",
            ROW_TABLE,
        ),
        row(
            "StrictRowLevelRouterImported",
            row_level_imported,
            False,
            "strict row-level 证书说明该表必须由无环 pre-Cauchy seed signed-row emitter 产生。",
            ACYCLIC_SEED_EMITTER,
        ),
        row(
            "SignedSourceFixedPointCutImported",
            fixed_point_imported,
            True,
            "signed-source 内部展开回到同一 row-level 表；该固定点不能作为证明。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "LatestConstructorRowLevelSyncImported",
            latest_imported,
            False,
            "latest constructor 线已独立把 row-level 粗口删除并同步到 noncircular signed kernel。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "ReversePaymentAndZeroRowRecoveryBlocked",
            reverse_blocked,
            True,
            "payment 反推、来源环和早期零行 unsigned cover 均不能恢复 signed coefficient source。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "NoncircularSignedKernelStillOpen",
            True,
            False,
            "当前材料没有不读取 row-level 表、来源恒等式、payment/Phi 下游或零行覆盖的 Cauchy 前 signed coefficient 发射核。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "SignedSurvivalAndRowMassStillParallel",
            True,
            False,
            "kernel 只解决 signed coefficient 来源；非零 signed survival 与 row-mass/no-heavy-row 仍需独立支付。",
            f"{NONZERO_SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
        row(
            "ProductWindowRowLevelCoarseTargetRemoved",
            all([previous_active, row_level_imported, fixed_point_imported, latest_imported, reverse_blocked]),
            False,
            "product-window 第一主攻不应停在 row-level 表名；删除固定点后必须提交 noncircular signed kernel。",
            NONCIRCULAR_KERNEL,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本证书只同步 row-level fixed-point cut，不证明 kernel、signed survival、row-mass 或终端排斥。",
            "row_column_unconditional_closed=false",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    data = {
        "previous": load_json(PREVIOUS),
        "row_level": load_json(ROW_LEVEL_ROUTER),
        "fixed_point": load_json(SIGNED_SOURCE_FIXED_POINT_ROUTER),
        "latest": load_json(LATEST_CONSTRUCTOR_ROW_LEVEL_ROUTER),
    }
    rows = build_rows(data)
    parallel = [
        ACYCLIC_SOURCE_SEED,
        NONZERO_SIGNED_SURVIVAL,
        ROW_MASS,
        SAME_SET_PDEC,
        POINTWISE_TABLE,
        COMPLETE_KEY,
        FIXED_KEY_O1,
        ORIENTATION,
        EXACTUV_RETURN,
        INTERNAL_TRANSITION,
        RATE,
        DSTRUCTURE,
    ]
    latest_open_basis = (
        f"{ACYCLIC_SOURCE_SEED} AND ({SAME_SET_PDEC} OR ({NONCIRCULAR_KERNEL} "
        f"AND {NONZERO_SIGNED_SURVIVAL} AND {ROW_MASS})) AND "
        + " AND ".join([COMPLETE_KEY, FIXED_KEY_O1, ORIENTATION, EXACTUV_RETURN, INTERNAL_TRANSITION, RATE, DSTRUCTURE])
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_product_window_row_level_noncircular_kernel_sync_router",
        "status": "product_window_row_level_fixed_point_cut_to_noncircular_signed_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "counterexample_absence_not_used": True,
        "old_primary_attack_target": ROW_TABLE,
        "row_table_to_seed_emitter_imported": data["row_level"].get("row_level_origin_generation_table_router_closed")
        is True,
        "signed_source_fixed_point_cut_imported": data["fixed_point"].get("signed_source_fixed_point_breaker_closed")
        is True,
        "latest_constructor_row_level_sync_imported": data["latest"].get("row_level_coarse_target_removed") is True,
        "reverse_payment_and_zero_row_recovery_blocked": rows[4]["closed"],
        "product_window_row_level_coarse_target_removed": rows[-2]["closed"],
        "row_level_clean_core_origin_generation_table_proved": False,
        "noncircular_signed_coefficient_emission_kernel_proved": False,
        "nonzero_signed_row_survival_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "next_primary_attack_target": NONCIRCULAR_KERNEL,
        "terminal_return_if_no_kernel": TERMINAL_RETURN,
        "parallel_primary_attack_targets": parallel,
        "latest_open_basis_summary": latest_open_basis,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "本步把 product-window 最新第一硬点 "
            "`RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands` "
            "接入 strict row-level、strict signed-source fixed-point 与 latest constructor row-level sync "
            "证书。结论是：row-level 表若要成立，必须由无环 pre-Cauchy seed signed-row emitter "
            "正向产生；但现有内部展开会回到同一 row-level 表。删除该固定点后，第一主攻同步为 "
            "`NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows`。"
        ),
        "sync_chain": build_sync_chain(),
        "gates": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF product-window row-level noncircular-kernel sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "**核验日期：** `2026-05-26`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"row_table_to_seed_emitter_imported={fmt_bool(result['row_table_to_seed_emitter_imported'])}",
        f"signed_source_fixed_point_cut_imported={fmt_bool(result['signed_source_fixed_point_cut_imported'])}",
        f"latest_constructor_row_level_sync_imported={fmt_bool(result['latest_constructor_row_level_sync_imported'])}",
        f"reverse_payment_and_zero_row_recovery_blocked={fmt_bool(result['reverse_payment_and_zero_row_recovery_blocked'])}",
        f"product_window_row_level_coarse_target_removed={fmt_bool(result['product_window_row_level_coarse_target_removed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下游同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_chain"]:
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
    for item in result["gates"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 最新保留基",
            "",
            "```text",
            result["latest_open_basis_summary"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "失败回流：",
            "",
            "```text",
            result["terminal_return_if_no_kernel"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_primary_attack_targets"]),
            "```",
            "",
            "严格含义：本证书只同步 row-level fixed-point cut，不证明行/列命题。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 与 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        "product_window_row_level_coarse_target_removed="
        f"{fmt_bool(result['product_window_row_level_coarse_target_removed'])}"
    )
    print(f"next_primary_attack_target={result['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
