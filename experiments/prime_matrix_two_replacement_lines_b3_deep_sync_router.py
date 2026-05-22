#!/usr/bin/env python3
"""生成两条替代线 B=3 离散误差深同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_b3_deep_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-b3-deep-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-b3-deep-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-b3-deep-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-b3-deep-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-b3-deep-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

ATOMIZED = DOCS / "prime-matrix-two-replacement-lines-atomized-hard-package-router.json"
B3_DISCRETE = DOCS / "prime-matrix-b3-discrete-prime-sum-error-boundary-router.json"
B3_HARMONIC = DOCS / "prime-matrix-b3-prime-harmonic-mertens-envelope-router.json"
B3_MERTENS = DOCS / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json"
B3_ANCHOR = DOCS / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json"
B3_SELF_TAIL = DOCS / "prime-matrix-b3-self-contained-mertens-tail-router.json"
B3_EXTERNAL = DOCS / "prime-matrix-b3-external-chain-to-dstructure-gate-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SELF_CONTAINED_B3_BASIS = (
    "B3LowPrimeStepFiniteLedgerXLt286PGe100000 AND "
    "B3FinitePrimeReciprocalStepLedger286To10371PGe100000 AND "
    "B3FinitePrimeReciprocalStepLedger10372To19999PGe100000 AND "
    "PrimeReciprocalPartialSummationFromThetaEnvelopeClosed AND "
    "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
    "SelfContainedMeisselMertensConstantIntervalLedgerAt20000 AND "
    "B3RosserFaceDictionaryClosedAlpha043 AND "
    "B3Anchor20000BoundaryVariationBudgetClosedAlpha043"
)

EXTERNAL_B3_BASIS = (
    "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted AND "
    "B3RosserFaceDictionaryClosedAlpha043 AND "
    "B3Anchor20000BoundaryVariationBudgetClosedAlpha043"
)


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象，便于旧快照运行。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出 Markdown 友好的小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def dependency_paths() -> list[Path]:
    """列出本证书依赖。"""
    return [
        ATOMIZED,
        B3_DISCRETE,
        B3_HARMONIC,
        B3_MERTENS,
        B3_ANCHOR,
        B3_SELF_TAIL,
        B3_EXTERNAL,
        DSTRUCTURE,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造 B=3 深同步判定表。"""
    return [
        row(
            "AtomizedB3DiscreteGateImported",
            data["atomized"].get("status")
            == "two_replacement_lines_atomized_to_source_root_discrete_error_terminal_scope_open",
            True,
            "上一层把 beta-sieve 99% 主系数压到 B3DiscretePrimeSumUniformErrorPGe100000。",
            "继续导入 B=3 深层离散误差链。",
        ),
        row(
            "DiscretePrimeSumReducedToStieltjesAndBoundary",
            data["b3_discrete"].get("discrete_prime_sum_uniform_error_reduced") is True,
            False,
            "离散素和误差不能由有限 checkpoint 闭合，已拆成 prime-word Stieltjes 账本与交错边界余项。",
            "B3PrimeWordStieltjesIntegralUniformLedgerPGe100000 AND B3AlternatingBoundaryRemainderOnePercentLedger",
        ),
        row(
            "PrimeHarmonicMertensSplitImported",
            data["b3_harmonic"].get("prime_harmonic_mertens_envelope_reduced") is True,
            False,
            "prime-harmonic/Mertens 包络已拆成 x<286 有限阶梯与 x>=286 显式 reciprocal-prime Mertens 包络。",
            "ExplicitPrimeReciprocalMertensEnvelopeXGe286 AND B3BoundaryVariationOnePercentTransferLedger",
        ),
        row(
            "ExternalDusartMertensRouteClosed",
            data["b3_mertens"].get("explicit_prime_reciprocal_mertens_external_closed") is True,
            False,
            "接受 Dusart/Rosser-Schoenfeld 型显式素数倒数 Mertens 定理时，高阈值包络外部关闭。",
            "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted",
        ),
        row(
            "B3BoundaryVariationConditionalClosed",
            data["b3_anchor"].get("b3_boundary_variation_one_percent_conditional_closed") is True,
            False,
            "20000 锚点提升和 delay-kernel BV 乘子把外部 Mertens 版 B=3 一百分点边界变差关闭。",
            DSTRUCTURE_GATE,
        ),
        row(
            "B3ExternalChainAlreadyAtDStructureGate",
            data["b3_external"].get("b3_external_analytic_chain_closed_to_dstructure_gate") is True,
            False,
            "B=3 外部解析链已到最终 DStructure/Rankin 守门项；这只是条件外部路线，不是无条件证明。",
            DSTRUCTURE_GATE,
        ),
        row(
            "SelfContainedMertensTailReducedToPNT",
            data["b3_self_tail"].get("self_contained_mertens_tail_reduced") is True,
            False,
            "完全自足版不能引用 Dusart 尾段，已归约为显式 PNT/theta 包络、B1 常数区间和分部求和。",
            "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
        ),
        row(
            "DStructureRankinIndependentGateStillExternal",
            data["dstructure"].get("external_lemma_author_side_remaining") in ([], "none"),
            False,
            "作者侧普通剩余已归零，但独立验收事件仍不能由自审生成；若不用外审，需完整自足替代包。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把 B3Discrete 粗原子同步到更深的外部/自足分支；source-root、PDEC/CleanKLS、FullS theorem-match 与 DStructure 仍未闭合。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "atomized": read_json(ATOMIZED),
        "b3_discrete": read_json(B3_DISCRETE),
        "b3_harmonic": read_json(B3_HARMONIC),
        "b3_mertens": read_json(B3_MERTENS),
        "b3_anchor": read_json(B3_ANCHOR),
        "b3_self_tail": read_json(B3_SELF_TAIL),
        "b3_external": read_json(B3_EXTERNAL),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)

    internal_b3_replacement = (
        f"(({SELF_CONTAINED_B3_BASIS}) OR "
        "ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR "
        "StandardRosserIwaniecBetaSieveTheoremImportAccepted)"
    )
    latest_internal_basis = "".join(
        [
            "((ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR ",
            "(GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR ",
            "(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR ",
            "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR ",
            "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ",
            f"{internal_b3_replacement} AND ",
            "(PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR ",
            "ExternalWellFactorableSawtoothDispersionBoundAlpha043 OR ",
            "NoFurtherCanonicalSourceTerminalPromotionGap) AND ",
            "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND ",
            "JointEmitterPrepushforwardWordCoefficientIdentityLedger AND ",
            "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ",
            "ActualEmitterSourceDomainEntropyLedger AND ",
            "ExactUVMapFixedPairPolylogFiberBoundLedger AND ",
            "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ",
            "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND ",
            "CompletePrimitiveEmitterKeyPartitionLedger AND ",
            "FixedKeyExactUVLocalMultiplicityO1Ledger AND ",
            "RatePreservationLedger_FOR_moving_atom_packet AND ",
            DSTRUCTURE_GATE,
        ]
    )
    latest_external_basis = "".join(
        [
            "((AcceptedFullSKLSExtExternalContract) OR ",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ",
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR ",
            "NewAutomorphicDispersionProof) AND ",
            DSTRUCTURE_GATE,
        ]
    )

    return {
        "certificate_type": "two_replacement_lines_b3_deep_sync_router",
        "status": "two_replacement_lines_b3_discrete_synced_to_mertens_pnt_and_dstructure_open",
        "source_hashes": source_hashes(),
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "b3_external_mertens_version_reaches_dstructure_gate": data["b3_external"].get(
            "b3_external_analytic_chain_closed_to_dstructure_gate"
        )
        is True,
        "b3_self_contained_discrete_error_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_basis_after_sync": latest_external_basis,
        "b3_external_basis_after_sync": f"({EXTERNAL_B3_BASIS}) AND {DSTRUCTURE_GATE}",
        "b3_self_contained_basis_after_sync": SELF_CONTAINED_B3_BASIS,
        "internal_basis_after_sync": latest_internal_basis,
        "direct_attack_atoms_after_sync": [
            "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn",
            "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000",
            "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve or strict same-set PDEC scope",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance OR SelfContainedDStructureTailLog4FiniteRankinProofPackage",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof",
        ],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "plain_conclusion": (
            "B3DiscretePrimeSumUniformErrorPGe100000 已不应作为最新粗原子保留。"
            "外部 Dusart/Mertens 版的 B=3 解析链已经到 DStructure/Rankin 守门项；"
            "完全自足版则剩显式 PNT/theta 包络和 Meissel-Mertens 常数区间。"
            "这缩小了内部 beta-sieve 硬点，但不关闭 source-root、PDEC/CleanKLS、"
            "FullS theorem-match 或 DStructure/Rankin。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines: list[str] = [
        "# Prime Matrix 两条替代线 B=3 深同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"external_lemma_version_closed_conditionally={fmt_bool(payload['external_lemma_version_closed_conditionally'])}",
        f"external_no_blackbox_version_closed={fmt_bool(payload['external_no_blackbox_version_closed'])}",
        f"b3_external_mertens_version_reaches_dstructure_gate={fmt_bool(payload['b3_external_mertens_version_reaches_dstructure_gate'])}",
        f"b3_self_contained_discrete_error_closed={fmt_bool(payload['b3_self_contained_discrete_error_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in payload["rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 3. 外部 B=3 分支",
            "",
            "```text",
            payload["b3_external_basis_after_sync"],
            "```",
            "",
            "外部 Dusart/Mertens 版的 B=3 主系数链已到 DStructure/Rankin 守门项；这仍是条件输入，不是无条件闭合。",
            "",
            "## 4. 自足 B=3 分支",
            "",
            "```text",
            payload["b3_self_contained_basis_after_sync"],
            "```",
            "",
            "自足版真正剩余集中在显式 PNT/theta 包络与 Meissel-Mertens 常数区间，外加仍需 DStructure/Rankin 自足替代或独立验收。",
            "",
            "## 5. 同步后的内部基",
            "",
            "```text",
            payload["internal_basis_after_sync"],
            "```",
            "",
            "## 6. 直接主攻原子",
            "",
        ]
    )
    for atom in payload["direct_attack_atoms_after_sync"]:
        lines.append(f"- `{atom}`")
    lines.extend(
        [
            "",
            "## 7. 状态快照",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## 8. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    """入口。"""
    payload = build_payload()
    write_outputs(payload)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
