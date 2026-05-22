#!/usr/bin/env python3
"""生成两条替代线原子化硬包同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_atomized_hard_package_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-atomized-hard-package-router.json

输出：
  data/prime-matrix-two-replacement-lines-atomized-hard-package-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-atomized-hard-package-router.json
  docs/monograph/prime-matrix-two-replacement-lines-atomized-hard-package-router.md
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

SLUG = "prime-matrix-two-replacement-lines-atomized-hard-package"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-latest-true-remainder-sync-router.json"
FULLS_REMAINDER = DOCS / "prime-matrix-fulls-theorem-match-true-remainder-cut-router.json"
NCBLK_FRONTIER = DOCS / "prime-matrix-strict-ncblk-source-antiatom-frontier-sync-router.json"
NCBLK_DEDUP = DOCS / "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json"
BETA_FRONTIER = DOCS / "prime-matrix-beta-sieve-self-contained-frontier-router.json"
BETA_RECURSION = DOCS / "prime-matrix-beta-sieve-lower-weight-recursion-router.json"
BETA_DOMINANCE = DOCS / "prime-matrix-beta-sieve-lower-bound-dominance-router.json"
BETA_MAIN = DOCS / "prime-matrix-beta-sieve-main-coefficient-terminal-attack-router.json"
B3_SURPLUS = DOCS / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json"
SAWTOOTH = DOCS / "prime-matrix-exact-residue-sawtooth-normal-form-router.json"
QUADRATIC_ARC = DOCS / "prime-matrix-quadratic-arc-nearsquare-spread-router.json"
NEARSQUARE_ADMISSION = DOCS / "prime-matrix-nearsquare-strip-terminal-admission-router.json"
NEARSQUARE_ABSORPTION = DOCS / "prime-matrix-nearsquare-canonical-terminal-absorption-router.json"
DSTRUCTURE_AUTHOR = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件；缺失时返回空对象，便于旧快照运行。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def dependency_paths() -> list[Path]:
    """列出证书依赖。"""
    return [
        PREVIOUS,
        FULLS_REMAINDER,
        NCBLK_FRONTIER,
        NCBLK_DEDUP,
        BETA_FRONTIER,
        BETA_RECURSION,
        BETA_DOMINANCE,
        BETA_MAIN,
        B3_SURPLUS,
        SAWTOOTH,
        QUADRATIC_ARC,
        NEARSQUARE_ADMISSION,
        NEARSQUARE_ABSORPTION,
        DSTRUCTURE_AUTHOR,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本与依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """构造原子化判定表。"""
    return [
        row(
            "LatestTrueRemainderImported",
            data["previous"].get("status") == "two_replacement_lines_latest_true_remainders_synced_open",
            True,
            "上一层已把外部线压到 FullS-KLS/no-projection theorem-match 或 actual source capacity，把内部线压到 NC-BLK/source anti-atom 与 beta-sieve/sawtooth。",
            "继续把这些粗包拆成原子。",
        ),
        row(
            "ExternalNoBlackBoxStillTheoremMatch",
            data["fulls_remainder"].get("status")
            == "ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open",
            False,
            "外部无黑箱版仍是主来源 Full-S non-AP WFD KLS theorem-match，或 actual noncanonical source support/capacity 新定理。",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput",
        ),
        row(
            "ExternalLemmaVersionStillConditional",
            True,
            False,
            "外部引理版只在接受 FullS-KLS-ext 与 DStructure/Rankin 独立验收时条件闭合；本层不把它改写成无黑箱证明。",
            "AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "NCBLKSyncedToForwardSourceRoot",
            data["ncblk_frontier"].get("status")
            == "ncblk_source_antiatom_synced_to_forward_source_root_or_global_terminal_open",
            False,
            "NC-BLK/source anti-atom 不再是最佳主攻名；actual 路线必须先给出不从 downstream 反推的 pre-Cauchy source-root packet。",
            "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn OR global terminal/PDEC-scope route",
        ),
        row(
            "NCBLKFailureDeduplicated",
            data["ncblk_dedup"].get("acyclic_ncblk_not_separate_terminal") is True,
            True,
            "generic anti-atom 被 moving-delta 阻断；actual 反原子失败等价于 exact (u,v) 大原子并回到 global PDEC/sparse terminal。",
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        ),
        row(
            "BetaLowerWeightConstructionClosed",
            data["beta_recursion"].get("lower_weight_recursive_construction_closed") is True,
            True,
            "lower weights 的 finite word rule、符号、squarefree 支撑与 d<P 已闭合。",
            "BetaSieveLowerBoundDominanceProof AND BetaSieveMainCoefficientExplicit99PercentPGe100000",
        ),
        row(
            "BetaLowerBoundDominanceClosed",
            data["beta_dominance"].get("lower_weight_dominance_proved") is True,
            True,
            "Buchstab tree parity pruning 已证明显式 lower weights 逐点支配筛剩余指示函数。",
            "BetaSieveMainCoefficientExplicit99PercentPGe100000",
        ),
        row(
            "BetaMainCoefficientReduced",
            data["beta_main"].get("beta_sieve_main_coefficient_atom_reduced") is True,
            False,
            "99% 主系数不能由有限 checkpoint 推出，已压到连续 beta 余量与离散素和统一误差。",
            "B3ContinuousBetaSieveCoefficientSurplusAlpha043 AND B3DiscretePrimeSumUniformErrorPGe100000",
        ),
        row(
            "B3ContinuousSurplusClosed",
            data["b3_surplus"].get("continuous_beta_sieve_surplus_proved") is True,
            True,
            "alpha=0.43 时 s=1/alpha 位于 2<s<3，连续线性下界筛公式给出 1% 余量。",
            "B3DiscretePrimeSumUniformErrorPGe100000",
        ),
        row(
            "SawtoothCompressedToNearSquare",
            data["sawtooth"].get("exact_floor_to_quadratic_arc_identity_proved") is True
            and data["quadratic"].get("arc_hit_iff_nearsquare_multiple_proved") is True,
            False,
            "exact floor/sawtooth 已被压成二次圆弧，再压成有符号近平方条带非集中。",
            "RosserWeightQuotientResidueSupportLedgerAlpha043 AND SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000",
        ),
        row(
            "NearSquareTerminalAdmitted",
            data["nearsquare_admission"].get("nearsquare_strip_terminal_admission_closed") is True,
            False,
            "近平方条带失败没有独立第四出口，进入 global PDEC/sparse terminal 或 PDEC_CAP/CleanKLS。",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
        ),
        row(
            "NearSquareCanonicalAbsorptionImported",
            data["nearsquare_absorption"].get("nearsquare_terminal_absorbed") is True,
            False,
            "canonical 分支中近平方终端被 NoFurtherCanonicalSourceTerminalPromotionGap 吸收；strict noncanonical 分支仍需同口径终端/PDEC/KLS。",
            "NoFurtherCanonicalSourceTerminalPromotionGap OR strict terminal scope proof",
        ),
        row(
            "DStructureRankinGateCarried",
            True,
            False,
            "DStructure/Tail-log4/finite Rankin 仍需独立验收或自足替代包。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把最新硬包原子化；没有完成外部无黑箱 theorem-match、source-root、离散素和误差、strict 终端或 DStructure。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "fulls_remainder": read_json(FULLS_REMAINDER),
        "ncblk_frontier": read_json(NCBLK_FRONTIER),
        "ncblk_dedup": read_json(NCBLK_DEDUP),
        "beta_frontier": read_json(BETA_FRONTIER),
        "beta_recursion": read_json(BETA_RECURSION),
        "beta_dominance": read_json(BETA_DOMINANCE),
        "beta_main": read_json(BETA_MAIN),
        "b3_surplus": read_json(B3_SURPLUS),
        "sawtooth": read_json(SAWTOOTH),
        "quadratic": read_json(QUADRATIC_ARC),
        "nearsquare_admission": read_json(NEARSQUARE_ADMISSION),
        "nearsquare_absorption": read_json(NEARSQUARE_ABSORPTION),
        "dstructure_author": read_json(DSTRUCTURE_AUTHOR),
    }
    rows = build_rows(data)
    external_basis = (
        "((AcceptedFullSKLSExtExternalContract) OR "
        "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR "
        "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR "
        "NewAutomorphicDispersionProof) AND "
        "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    internal_atomized_basis = (
        "((ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR "
        "(GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR "
        "(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR "
        "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR "
        "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND "
        "(B3DiscretePrimeSumUniformErrorPGe100000 OR ExternalShortIntervalRoughNumberLowerBoundForAlpha043 OR "
        "StandardRosserIwaniecBetaSieveTheoremImportAccepted) AND "
        "(PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR ExternalWellFactorableSawtoothDispersionBoundAlpha043 OR "
        "NoFurtherCanonicalSourceTerminalPromotionGap) AND "
        "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND "
        "JointEmitterPrepushforwardWordCoefficientIdentityLedger AND "
        "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND "
        "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger AND "
        "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND "
        "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND "
        "CompletePrimitiveEmitterKeyPartitionLedger AND FixedKeyExactUVLocalMultiplicityO1Ledger AND "
        "RatePreservationLedger_FOR_moving_atom_packet AND "
        "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
    )
    return {
        "certificate_type": "prime_matrix_two_replacement_lines_atomized_hard_package_router",
        "status": "two_replacement_lines_atomized_to_source_root_discrete_error_terminal_scope_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "frontier_sync_only": True,
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "latest_external_atomized_basis": external_basis,
        "latest_internal_atomized_basis": internal_atomized_basis,
        "latest_internal_direct_attack_targets": [
            "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn",
            "B3DiscretePrimeSumUniformErrorPGe100000",
            "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve or strict same-set PDEC scope",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "plain_conclusion": (
            "本层把 latest true remainder 中的内部粗包继续原子化：NC-BLK/source anti-atom 已同步到 "
            "forward pre-Cauchy source-root packet 或 global terminal/PDEC-scope；beta-sieve 的 lower "
            "weight 构造和 lower-bound 支配已经闭合，连续 B=3 主项余量也已闭合，真正剩余是 P>=100000 "
            "的离散素和统一误差；exact sawtooth 已压成二次圆弧和有符号近平方条带，失败态进入 global "
            "PDEC/sparse terminal 或 canonical terminal absorption。外部线仍保持 FullS-KLS/no-projection "
            "theorem-match 或外部合同边界。本层不宣称无条件闭合。"
        ),
        "rows": rows,
        "source_status_snapshot": {key: value.get("status") for key, value in data.items()},
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """生成 Markdown 判定表。"""
    lines = [
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    lines = [
        "# Prime Matrix 两条替代线原子化硬包同步证书",
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
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 外部线",
        "",
        "最新外部原子化基：",
        "",
        "```text",
        payload["latest_external_atomized_basis"],
        "```",
        "",
        "## 4. 内部线",
        "",
        "最新内部原子化基：",
        "",
        "```text",
        payload["latest_internal_atomized_basis"],
        "```",
        "",
        "直接主攻原子：",
        "",
    ]
    for item in payload["latest_internal_direct_attack_targets"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 5. 状态快照",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in payload["source_status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## 6. 依赖哈希",
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
    """写出证书。"""
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
