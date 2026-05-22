#!/usr/bin/env python3
"""生成两条替代线深终端同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_deep_terminal_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-deep-terminal-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-deep-terminal-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-deep-terminal-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-deep-terminal-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-deep-terminal-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_TWO_LINE = DOCS / "prime-matrix-two-replacement-lines-exact-layer-completed-kls-attack-router.json"
CDEP_REDUCTION = DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json"
NCBLK_ALIGNMENT = DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json"
EXACT_ENTROPY = DOCS / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json"
SOURCE_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
ACTUAL_SOURCE_AUDIT = DOCS / "prime-matrix-actual-source-antiatom-lane-audit-router.json"
FINAL_OPEN = DOCS / "prime-matrix-final-open-input-current-attack-router.json"
ROW_ORIGIN_BUCKET = DOCS / "prime-matrix-row-origin-table-phi-lpf-bucket-law-sync-router.json"
SIGNED_CYCLE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
COMMON_TABLE = DOCS / "prime-matrix-phi-lpf-latest-constructor-common-signed-table-rebase-sync-router.json"
SEMIPRIME_REBASE = (
    DOCS / "prime-matrix-phi-lpf-latest-constructor-common-table-semiprime-seed-diagonal-rebase-sync-router.json"
)
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据；缺失时返回空对象，避免脚本因旧仓库快照中断。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖哈希，方便审稿复核。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def dependency_paths() -> list[Path]:
    """列出本证书依赖文件。"""
    return [
        PREVIOUS_TWO_LINE,
        CDEP_REDUCTION,
        NCBLK_ALIGNMENT,
        EXACT_ENTROPY,
        SOURCE_ANTIATOM,
        ACTUAL_SOURCE_AUDIT,
        FINAL_OPEN,
        ROW_ORIGIN_BUCKET,
        SIGNED_CYCLE,
        COMMON_TABLE,
        SEMIPRIME_REBASE,
        CLAIM_STATUS,
        CONTRACTS,
        FRONTIER,
        EXTERNAL_INDEX,
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
    """合并两条替代线的深终端判定表。"""
    return [
        row(
            "ExactLayerCompletedKLSFrontierImported",
            data["previous"].get("status")
            == "two_replacement_lines_reduced_to_origin_ledger_and_c_dependent_completed_spectral_input_open",
            True,
            "上一层已把内部线压到 clean-core 原始生成账本，把外部线压到 c-dependent completed residue 谱输入。",
            "继续向下同步，不在旧接口处循环。",
        ),
        row(
            "CDependentResidueReducedToNCBLKOrExternal",
            data["cdep"].get("terminal_gap_after_router") == "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
            False,
            "c-dependent residue 权重经有限 Fourier/BWFD/BSC/KFLS 接入 NC-BLK 或外部 DI/BFI/Kuznetsov。",
            "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
        ),
        row(
            "NCBLKAlignedToExactEntropyOrExternal",
            data["ncblk"].get("terminal_gap_after_router")
            == "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
            False,
            "NC-BLK 不能静默借 canonical branch；自足路线必须证明 full-S non-AP exact source entropy。",
            "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
        ),
        row(
            "ExactEntropyMergedIntoSourceAntiAtom",
            data["source_antiatom"].get("terminal_gap_after_router")
            == "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov",
            False,
            "exact source entropy 经支撑/容量包合并为最终 source capacity measure 无 moving same-(u,v) atom。",
            "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov",
        ),
        row(
            "GenericSourceAntiAtomRejected",
            data["actual_source"].get("generic_self_contained_antiatom_refuted") is True,
            False,
            "generic full-S 自足反原子已被 moving-delta 模型反证；不能把形式 WFD 当成反原子证明。",
            "AddStrengthenedActualSourceAntiAtomTheorem OR ExternalDIBFIKuznetsovDispersionTheoremMatch",
        ),
        row(
            "ExternalNoBlackBoxTheoremMatchPinned",
            data["final_open"].get("current_external_or_new_deep_basis")
            == "ExternalDIBFIKuznetsovDispersionTheoremMatch AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            False,
            "若不新增 source 反原子定理，无黑箱外部线必须给同对象 no-projection DI/BFI/Kuznetsov 定理匹配。",
            "ExternalDIBFIKuznetsovDispersionTheoremMatch",
        ),
        row(
            "OriginLedgerReducedToPhiLPFBucketSignedLaw",
            data["row_origin"].get("next_primary_attack_target") == "PhiLPFBucketSignedCoefficientLawBeforePushforward",
            False,
            "clean-core row-origin 表不能从来源环自证；LPF/Phi 只支付无符号 support/capacity，剩余是 bucket signed law。",
            "PhiLPFBucketSignedCoefficientLawBeforePushforward",
        ),
        row(
            "SignedLaneSelfProofCycleCut",
            data["signed_cycle"].get("signed_lane_cycle_closed") is True,
            True,
            "common packet、built-in pairing、branch trace、payload、origin identity 已形成闭环，环内节点不能再当证明。",
            "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact OR terminal descent OR PDEC scope",
        ),
        row(
            "CommonSignedTableRebased",
            data["common_table"].get("common_same_formal_unit_signed_table_aligned") is True,
            False,
            "built-in pairing、source entropy 与 fixed-pair ExactUV 已合流为同 formal unit pre-Cauchy primitive-emitter 表。",
            data["common_table"].get("latest_internal_basis_after_router", "common signed table basis"),
        ),
        row(
            "SemiprimeSeedDiagonalRebased",
            data["semiprime"].get("semiprime_seed_diagonal_rebased") is True,
            False,
            "first-edge signed seed 表继续按 p=q/p<q 拆分；diagonal 私有 signed 出口已移除。",
            data["semiprime"].get("next_direct_attack_target", "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward"),
        ),
        row(
            "PhiLPFExactnessScopePinned",
            True,
            True,
            "Phi-LPF 恒等式是组合精确和无符号 ownership/capacity 账本；它不产生 signed coefficient 或短区间正性。",
            "signed table, row mass, key multiplicity, beta-sieve/sawtooth",
        ),
        row(
            "PromotionAndTailGatesCarried",
            True,
            False,
            "beta-sieve/sawtooth 尾段、RatePreservation 与 DStructure/Rankin 独立验收仍需保留。",
            "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix AND BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000 AND ExactResidueWeightedFloorSawtoothTenPercentBound AND RatePreservationLedger_FOR_moving_atom_packet AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只做深终端同步和循环切断；没有证明外部定理匹配、内部 signed 表、尾段或晋级门。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS_TWO_LINE),
        "cdep": read_json(CDEP_REDUCTION),
        "ncblk": read_json(NCBLK_ALIGNMENT),
        "exact_entropy": read_json(EXACT_ENTROPY),
        "source_antiatom": read_json(SOURCE_ANTIATOM),
        "actual_source": read_json(ACTUAL_SOURCE_AUDIT),
        "final_open": read_json(FINAL_OPEN),
        "row_origin": read_json(ROW_ORIGIN_BUCKET),
        "signed_cycle": read_json(SIGNED_CYCLE),
        "common_table": read_json(COMMON_TABLE),
        "semiprime": read_json(SEMIPRIME_REBASE),
    }
    latest_internal_basis = data["semiprime"].get("latest_internal_basis_after_router", "")
    latest_retained_basis = data["semiprime"].get("latest_retained_basis_after_router", "")
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_two_replacement_lines_deep_terminal_sync_router",
        "status": "two_replacement_lines_synced_to_deep_terminal_basis_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "frontier_sync_only": True,
        "previous_internal_atom": "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
        "previous_external_atom": "CDependentResidueWeightSpectralCancellationInput",
        "external_lane_deep_chain": [
            "CDependentResidueWeightSpectralCancellationInput",
            "NCBLKActualBlockNonConcentrationOrExternalDIBFI",
            "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov",
            "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov",
            "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov",
        ],
        "latest_no_blackbox_external_target": "ExternalDIBFIKuznetsovDispersionTheoremMatch",
        "external_match_required_clauses": [
            "same full-S non-AP WFD object after completion",
            "c-dependent completed residue weights B_{c,x}=sum_k beta_{x+k c}",
            "well-factorable lambda_c and smooth omega_h over c,h",
            "no APSourceLift, no silent canonical source import, no centering/projection loss",
            "gcd, smoothing, endpoint, and de-completion losses inside B(A)",
            "NaturalWFDScale/log^A(P) saving for every fixed A",
        ],
        "internal_lane_deep_chain": [
            "CleanCoreOriginalCoefficientGenerationLedgerAndReturn",
            "RowLevelCleanCoreOriginalCoefficientGenerationTableForActualNoncanonicalPrimitiveSummands",
            "NoncircularPreCauchySignedCoefficientEmissionKernelForActualNoncanonicalPrimitiveRows",
            "PhiLPFBucketSignedCoefficientLawBeforePushforward",
            "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward",
            "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward",
        ],
        "latest_internal_basis_after_router": latest_internal_basis,
        "latest_internal_direct_attack_target": data["semiprime"].get("next_direct_attack_target"),
        "latest_internal_primary_attack_target": data["semiprime"].get("next_primary_attack_target"),
        "latest_internal_retained_basis_after_router": latest_retained_basis,
        "external_lemma_version_status": (
            "conditionally_closed_only_under_AcceptedFullSKLSExtExternalContract_"
            "and_DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "no_blackbox_external_version_closed": False,
        "internal_self_contained_version_closed": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "本层把 exact-layer/completed-KLS 后的两条替代线继续接入仓库已有最深前沿。"
            "外部线中，c-dependent completed residue 谱输入若不作为外部定理接受，会经 "
            "NC-BLK、exact source entropy、支撑/容量包回到 source anti-atom；generic 自足反原子"
            "已被反例模型排除，所以无黑箱外部版的非循环目标只能是同对象 "
            "ExternalDIBFIKuznetsovDispersionTheoremMatch。内部线中，clean-core 原始生成账本"
            "继续被 row-origin/Phi-LPF 证书压到 bucket signed law，并在 common-table rebase 后收窄到 "
            "offdiagonal semiprime first-seed signed table、internal prime-adjoin transition、source 三原子、"
            "row-mass/support、complete/fixed-key 与 beta-sieve/sawtooth 尾段。Phi-LPF 的精确性只支付"
            "无符号 ownership/capacity，不能推出 signed coefficient 或短区间正性。本层不声明无条件闭合。"
        ),
        "source_status_snapshot": {
            "previous_status": data["previous"].get("status"),
            "cdep_status": data["cdep"].get("status"),
            "ncblk_status": data["ncblk"].get("status"),
            "exact_entropy_status": data["exact_entropy"].get("status"),
            "source_antiatom_status": data["source_antiatom"].get("status"),
            "actual_source_status": data["actual_source"].get("status"),
            "final_open_status": data["final_open"].get("status"),
            "row_origin_status": data["row_origin"].get("status"),
            "signed_cycle_status": data["signed_cycle"].get("status"),
            "common_table_status": data["common_table"].get("status"),
            "semiprime_rebase_status": data["semiprime"].get("status"),
        },
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 Markdown 判定表。"""
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


def list_block(items: list[str]) -> list[str]:
    """生成 Markdown 列表。"""
    return [f"- `{item}`" for item in items]


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    lines = [
        "# Prime Matrix 两条替代线深终端同步证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"latest_no_blackbox_external_target={payload['latest_no_blackbox_external_target']}",
        f"latest_internal_primary_attack_target={payload['latest_internal_primary_attack_target']}",
        f"no_blackbox_external_version_closed={fmt_bool(payload['no_blackbox_external_version_closed'])}",
        f"internal_self_contained_version_closed={fmt_bool(payload['internal_self_contained_version_closed'])}",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 外部无黑箱线",
        "",
        "深同步链条：",
        "",
        "```text",
        *payload["external_lane_deep_chain"],
        "```",
        "",
        "`ExternalDIBFIKuznetsovDispersionTheoremMatch` 必须逐项匹配：",
        "",
        *list_block(payload["external_match_required_clauses"]),
        "",
        "## 4. 内部自足线",
        "",
        "深同步链条：",
        "",
        "```text",
        *payload["internal_lane_deep_chain"],
        "```",
        "",
        "最新内部基：",
        "",
        "```text",
        payload["latest_internal_basis_after_router"],
        "```",
        "",
        "保留条件基：",
        "",
        "```text",
        payload["latest_internal_retained_basis_after_router"],
        "```",
        "",
        "## 5. 状态快照",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
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
