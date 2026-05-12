#!/usr/bin/env python3
"""生成严格高段模型余量尾段更新路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_high_model_tail_update_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-high-model-tail-update-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-high-model-tail-update-router.json"
OUT_MD = DOCS / "prime-matrix-strict-high-model-tail-update-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-global-terminal-scope-router.md",
    "prime-matrix-high-segment-model-gap-factorization-router.md",
    "prime-matrix-harmonic-window-dusart-ledger-router.md",
    "prime-matrix-dynamic-skeleton-lower-factorization-router.md",
    "prime-matrix-linear-lower-sieve-tail-margin-router.md",
    "prime-matrix-linear-sieve-tail-remainder-gap-router.md",
    "prime-matrix-rosser-weight-floor-ledger-router.md",
    "prime-matrix-explicit-rosser-lower-weight-ledger-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    strict_tail_inputs = (
        "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND "
        "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 AND "
        "ExactResidueWeightedFloorSawtoothTenPercentBound"
    )

    rows = [
        {
            "gate": "StrictHighModelInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层严格基含 HighSegmentModelGapAlpha043C3AnalyticLedger。",
            "remaining": "并入高段模型余量的后续压缩结果。",
        },
        {
            "gate": "HighModelFactorizationImported",
            "closed": True,
            "proved": True,
            "meaning": "高段模型余量已因子化为调和窗口 H<=0.850 与动态粗骨架 S>=401，桥接段 2003<=P<3001 已闭合。",
            "remaining": "HarmonicWindow 与 DynamicRoughSkeleton。",
        },
        {
            "gate": "HarmonicWindowClosedImported",
            "closed": True,
            "proved": True,
            "meaning": "HarmonicWindowAlpha043PGe3001Upper0850Ledger 已由有限枚举和 Dusart 素数倒数和闭合。",
            "remaining": "调和窗口从严格活动输入删除。",
        },
        {
            "gate": "DynamicSkeletonFiniteBridgeImported",
            "closed": True,
            "proved": True,
            "meaning": "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger 已拆成 3001<=P<100000 有限桥与 P>=100000 尾段线性筛；有限桥闭合。",
            "remaining": "LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger。",
        },
        {
            "gate": "TailLinearSieveTenPercentImported",
            "closed": True,
            "proved": True,
            "meaning": "P>=100000 尾段下界筛已压成 10% 模型主项包，10% 主项在端点已超过 401。",
            "remaining": "LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger。",
        },
        {
            "gate": "TenPercentTailSplitImported",
            "closed": True,
            "proved": True,
            "meaning": "10% 主项包的真实剩余是 Rosser-Iwaniec 加权 floor 余项控制，或外部短区间 rough 下界。",
            "remaining": "RosserIwaniecWeightedFloorRemainderTenPercentBound OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043。",
        },
        {
            "gate": "ExternalRoughBypassExcludedForStrictSelfContained",
            "closed": True,
            "proved": True,
            "meaning": "严格自足口径不能用 ExternalShortIntervalRoughNumberLowerBoundForAlpha043 旁路。",
            "remaining": "RosserIwaniecWeightedFloorRemainderTenPercentBound。",
        },
        {
            "gate": "RosserWeightedFloorSplitImported",
            "closed": True,
            "proved": True,
            "meaning": "Rosser 加权 floor 余项已拆成显式 lower weights 账本与精确 residue-weighted sawtooth 余项界。",
            "remaining": "ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound。",
        },
        {
            "gate": "StandardBetaSieveImportExcludedForStrictSelfContained",
            "closed": True,
            "proved": True,
            "meaning": "标准 Rosser-Iwaniec beta-sieve 定理可作为条件外部输入，但不能替代严格自足证明。",
            "remaining": "SelfContained beta-sieve appendix and explicit coefficient error。",
        },
        {
            "gate": "ExplicitWeightLedgerCompressedImported",
            "closed": True,
            "proved": True,
            "meaning": "显式权重账本的参数层已闭合；严格自足剩余为 beta-sieve 构造附录与 99% 主系数误差。",
            "remaining": "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000。",
        },
        {
            "gate": "StrictHighModelTailCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料尚未完成自足 beta-sieve 权重构造、99% 主系数误差和 exact sawtooth 余项界。",
            "remaining": strict_tail_inputs,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_high_model_tail_update_router",
        "status": "strict_high_model_tail_reduced_to_beta_sieve_and_sawtooth_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_high_model_tail_boundary_closed": True,
        "harmonic_window_closed_imported": True,
        "dynamic_skeleton_finite_bridge_closed_imported": True,
        "external_rough_bypass_excluded_for_strict": True,
        "standard_beta_sieve_import_excluded_for_strict": True,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "high_segment_model_gap_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": "HighSegmentModelGapAlpha043C3AnalyticLedger",
        "terminal_gap_after_router": strict_tail_inputs,
        "strict_self_contained_math_basis_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily AND "
            f"({strict_tail_inputs}) AND "
            "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
        ),
        "next_attack_contract": {
            "name": "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix_THEN_ExactSawtooth",
            "must_prove": [
                "自足构造 alpha=0.43、D=P、z=P^0.43 的 Rosser-Iwaniec lower weights",
                "证明 lower weights 的支配关系与 99% 主系数误差，覆盖 P>=100000",
                "在权重固定后证明 exact CRT residue-weighted floor sawtooth 负损失不超过 90% 模型主项",
                "若 sawtooth 失败，抽取同 formal unit 的 PDEC/SAE/ColumnCRT 或近平方条带终端证书",
                "保持外部 rough 下界与标准 beta-sieve 定理只作为条件旁路，不作为严格自足闭合",
            ],
            "cannot_use_as_proof": [
                "把调和窗口 H<=0.850 重新作为开放项",
                "把 3001<=P<100000 有限骨架桥当作 P>=100000 尾段证明",
                "用 ExternalShortIntervalRoughNumberLowerBoundForAlpha043 替代自足证明",
                "用 StandardRosserIwaniecBetaSieveTheoremImportAccepted 替代自足 beta-sieve 附录",
                "只给模型主项，不支付 floor/sawtooth 取整余项",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "高段模型余量在严格链中继续被压缩：调和窗口已经闭合，动态粗骨架的有限桥也已闭合；"
            "P>=100000 尾段转为线性下界筛 10% 主项包。严格自足口径排除外部 short-rough 旁路和标准 beta-sieve "
            "黑箱后，剩余为三项：自足 Rosser-Iwaniec beta-sieve lower weights 构造、99% 主系数显式误差、"
            "以及 exact residue-weighted floor/sawtooth 余项界。当前仍没有无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix 严格高段模型余量尾段更新路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_high_model_tail_boundary_closed={str(result['strict_high_model_tail_boundary_closed']).lower()}",
        f"harmonic_window_closed_imported={str(result['harmonic_window_closed_imported']).lower()}",
        f"dynamic_skeleton_finite_bridge_closed_imported={str(result['dynamic_skeleton_finite_bridge_closed_imported']).lower()}",
        f"external_rough_bypass_excluded_for_strict={str(result['external_rough_bypass_excluded_for_strict']).lower()}",
        f"standard_beta_sieve_import_excluded_for_strict={str(result['standard_beta_sieve_import_excluded_for_strict']).lower()}",
        f"self_contained_beta_sieve_appendix_proved={str(result['self_contained_beta_sieve_appendix_proved']).lower()}",
        f"beta_sieve_main_coefficient_99_proved={str(result['beta_sieve_main_coefficient_99_proved']).lower()}",
        f"exact_residue_weighted_floor_sawtooth_bound_proved={str(result['exact_residue_weighted_floor_sawtooth_bound_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 高段压缩链",
        "",
        "```text",
        "HighSegmentModelGapAlpha043C3AnalyticLedger",
        "  -> HarmonicWindowAlpha043PGe3001Upper0850Ledger(closed)",
        "  -> DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger",
        "  -> LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger",
        "  -> LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger",
        "  -> RosserIwaniecWeightedFloorRemainderTenPercentBound",
        "  -> ExplicitRosserIwaniecLowerWeightLedger + ExactResidueWeightedFloorSawtooth",
        "  -> SelfContainedBetaSieveAppendix + 99PercentCoefficient + ExactSawtooth",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=str(row["closed"]).lower(),
                proved=str(row["proved"]).lower(),
                meaning=row["meaning"],
                remaining=row["remaining"],
            )
        )

    contract = result["next_attack_contract"]
    lines.extend(
        [
            "",
            "## 3. 下一主攻合同",
            "",
            f"下一数学主攻点：`{contract['name']}`。",
            "",
            "必须证明：",
        ]
    )
    for item in contract["must_prove"]:
        lines.append(f"- {item}。")

    lines.extend(["", "不能作为证明使用："])
    for item in contract["cannot_use_as_proof"]:
        lines.append(f"- {item}。")

    lines.extend(
        [
            "",
            "严格自足数学基更新为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
