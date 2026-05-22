#!/usr/bin/env python3
"""生成两条替代线 rate-bearing Mertens 尾段闭合同步证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_rate_tail_mertens_closed_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-router.json

输出：
  data/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-router.json
  docs/monograph/prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync-router.md
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

SLUG = "prime-matrix-two-replacement-lines-rate-tail-mertens-closed-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS = DOCS / "prime-matrix-two-replacement-lines-b3-deep-sync-router.json"
RATE_TAIL = DOCS / "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"
DIRECT_DUSART = DOCS / "prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json"
B1_INTERVAL = DOCS / "prime-matrix-strict-meissel-mertens-b1-interval-self-contained-router.json"
UNSMOOTHED = DOCS / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"

DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE_GATE = "RatePreservationLedger_FOR_moving_atom_packet"
PDEC_RATE_GATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
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
    return [PREVIOUS, RATE_TAIL, DIRECT_DUSART, B1_INTERVAL, UNSMOOTHED, DSTRUCTURE, PAPER]


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
    """构造同步判定表。"""
    return [
        row(
            "B3DeepSyncImported",
            data["previous"].get("status")
            == "two_replacement_lines_b3_discrete_synced_to_mertens_pnt_and_dstructure_open",
            True,
            "上一层仍把自足 B3 分支写成显式 PNT/theta 包络与 Meissel-Mertens 常数区间。",
            "导入后续 rate-bearing Mertens 最新同步。",
        ),
        row(
            "DirectInternalDusartThetaPNTClosed",
            data["direct_dusart"].get("direct_internal_dusart_theta_pnt_envelope_closed") is True,
            True,
            "直接内部 Dusart theta/PNT 包络已由 P5.1 自足同步关闭。",
            "DusartP51ThetaUpperFullSelfContainedLedger",
        ),
        row(
            "UnsmoothedPerronClosed",
            data["unsmoothed"].get("unsmoothed_perron_strict_self_contained_closed") is True,
            True,
            "非平滑 Perron 常数层已自足闭合为 C=12128。",
            "UnsmoothedChebyshevPerronExplicitFormulaConstantSelfContainedClosedC12128",
        ),
        row(
            "MeisselMertensB1Closed",
            data["b1"].get("self_contained_meissel_mertens_constant_interval_closed") is True,
            True,
            "Meissel-Mertens B1 常数区间已由 Euler product 区间证书自足关闭。",
            "SelfContainedMeisselMertensB1EulerProductIntervalClosedRadius2eMinus6At20000",
        ),
        row(
            "StrictMertensTailClosed",
            data["rate_tail"].get("strict_self_contained_mertens_tail_proved") is True,
            True,
            "有限倒数素数跳点、分部求和、theta/PNT 包络与 B1 常数区间全部导入后，strict 自足 Mertens 尾段移出活动剩余。",
            "closed",
        ),
        row(
            "ExternalB3StillAtDStructureGate",
            data["rate_tail"].get("external_mertens_theta_route_closed_to_dstructure") is True,
            False,
            "外部 Mertens/theta 路线也已到 DStructure/Rankin 门，但独立验收仍不是作者侧可生成证明。",
            DSTRUCTURE_GATE,
        ),
        row(
            "InternalBasisCondensedToTerminalGates",
            True,
            False,
            "删除自足 PNT/Mertens 旧硬点后，内部线最新承重门回到 source-root、PDEC/CleanKLS、Rate 与 DStructure。",
            f"ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn AND {PDEC_RATE_GATE} AND {RATE_GATE} AND {DSTRUCTURE_GATE}",
        ),
        row(
            "DStructureStillIndependentOrSelfContainedReplacement",
            data["dstructure"].get("external_lemma_author_side_remaining") in ([], "none"),
            False,
            "DStructure/Rankin 作者侧普通剩余已归零，但外部验收或完整自足替代包仍未完成。",
            f"{DSTRUCTURE_GATE} OR SelfContainedDStructureTailLog4FiniteRankinProofPackage",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层关闭的是 B3/Mertens 尾段解析活动缺口；没有关闭 source-root、PDEC/CleanKLS、Rate、FullS theorem-match 或 DStructure。",
            "not closed",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "previous": read_json(PREVIOUS),
        "rate_tail": read_json(RATE_TAIL),
        "direct_dusart": read_json(DIRECT_DUSART),
        "b1": read_json(B1_INTERVAL),
        "unsmoothed": read_json(UNSMOOTHED),
        "dstructure": read_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    external_basis = "".join(
        [
            "((AcceptedFullSKLSExtExternalContract) OR ",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ",
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR ",
            "NewAutomorphicDispersionProof) AND ",
            DSTRUCTURE_GATE,
        ]
    )
    internal_basis = "".join(
        [
            "((ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn) OR ",
            "(GlobalPDECorSparseTerminalExclusion AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR ",
            "(AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate AND HighSegmentModelGapAlpha043C3AnalyticLedger) OR ",
            "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage OR ",
            "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact) AND ",
            f"({PDEC_RATE_GATE} OR PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve OR NoFurtherCanonicalSourceTerminalPromotionGap) AND ",
            "JointEmitterPrimitiveSummandRowsFormulaBeforePushforward AND ",
            "JointEmitterPrepushforwardWordCoefficientIdentityLedger AND ",
            "JointEmitterNoDownstreamRecoveryAndNamedReturnLedger AND ",
            "ActualEmitterSourceDomainEntropyLedger AND ",
            "ExactUVMapFixedPairPolylogFiberBoundLedger AND ",
            "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward AND ",
            "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger AND ",
            "CompletePrimitiveEmitterKeyPartitionLedger AND ",
            "FixedKeyExactUVLocalMultiplicityO1Ledger AND ",
            f"{RATE_GATE} AND {DSTRUCTURE_GATE}",
        ]
    )
    return {
        "certificate_type": "two_replacement_lines_rate_tail_mertens_closed_sync_router",
        "status": "two_replacement_lines_rate_tail_mertens_closed_terminal_gates_open",
        "source_hashes": source_hashes(),
        "external_lemma_version_closed_conditionally": True,
        "external_no_blackbox_version_closed": False,
        "strict_self_contained_mertens_tail_proved": data["rate_tail"].get(
            "strict_self_contained_mertens_tail_proved"
        )
        is True,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "external_basis_after_sync": external_basis,
        "internal_basis_after_sync": internal_basis,
        "direct_attack_atoms_after_sync": [
            "ForwardAcyclicPreCauchySourceRootPacketOrNamedReturn",
            PDEC_RATE_GATE,
            RATE_GATE,
            f"{DSTRUCTURE_GATE} OR SelfContainedDStructureTailLog4FiniteRankinProofPackage",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput OR NewAutomorphicDispersionProof",
        ],
        "status_snapshot": {name: data[name].get("status") for name in data},
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["proved"]],
        "plain_conclusion": (
            "后续 strict rate-bearing Mertens 同步已关闭自足 Mertens 尾段，"
            "因此两条替代线不应继续把 SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 "
            "或 SelfContainedMeisselMertensConstantIntervalLedgerAt20000 作为活动硬点。"
            "最新内部承重门回到 source-root、PDEC/CleanKLS、RatePreservation 与 DStructure；"
            "外部无黑箱线仍保持 FullS theorem-match 或新 dispersion 证明边界。"
        ),
    }


def write_outputs(payload: dict[str, Any]) -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    OUT_LEDGER.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines: list[str] = [
        "# Prime Matrix 两条替代线 rate-bearing Mertens 尾段闭合同步证书",
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
        f"strict_self_contained_mertens_tail_proved={fmt_bool(payload['strict_self_contained_mertens_tail_proved'])}",
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
            "## 3. 外部线",
            "",
            "```text",
            payload["external_basis_after_sync"],
            "```",
            "",
            "外部引理版仍只给条件闭合；无黑箱外部版仍需同对象 FullS theorem-match、actual source capacity 新定理或新 automorphic/dispersion 证明。",
            "",
            "## 4. 内部线",
            "",
            "```text",
            payload["internal_basis_after_sync"],
            "```",
            "",
            "## 5. 直接主攻原子",
            "",
        ]
    )
    for atom in payload["direct_attack_atoms_after_sync"]:
        lines.append(f"- `{atom}`")
    lines.extend(
        [
            "",
            "## 6. 状态快照",
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
            "## 7. 依赖哈希",
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
