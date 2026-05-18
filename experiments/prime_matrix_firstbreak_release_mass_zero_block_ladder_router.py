#!/usr/bin/env python3
"""生成首破裂释放质量的零行块阶梯证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_release_mass_zero_block_ladder_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json

输出：
  data/prime-matrix-firstbreak-release-mass-zero-block-ladder-ledger.json
  docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json
  docs/monograph/prime-matrix-firstbreak-release-mass-zero-block-ladder-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-release-mass-zero-block-ladder-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-release-mass-zero-block-ladder-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.json",
    DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.json",
    DOCS / "prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json",
    DOCS / "prime-matrix-sparse-terminal-forced-load-lower-bound-from-early-zero-row.md",
    DOCS / "prime-matrix-bpn-bk-selberg-route.md",
    DOCS / "prime-matrix-bad-window-source-family-extraction-router.md",
]

AMPLIFICATION = "FirstBreakReleaseMassAmplificationOrSingletonSAE"
NO_BOUNDARY = "NoBoundaryOnlyReleaseAmplificationGuard"
ZERO_BLOCK_MASS = "ZeroBlockCoverObligationMassLedger"
SHORT_BLOCK = "ShortZeroBlockSingletonSAESummability"
LONG_TRANSFER = "LongZeroBlockCoverMassTransferToAPDemandOrPDEC"
PAYMENT_INJECTION = "LowCarrierActualPaymentInjectionWithoutEnvelopeReuse"
STRICT_GAP = "LowCarrierAPEnvelopeStrictGapOrDenseTablePDEC"
DENSE_TABLE = "DenseLowCarrierResidueTablePDECExclusion"
SPARSE_CELL = "SparseLowCarrierResidueCellSAESummability"
LOW_SAE = "LowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "HighCarrierRankDeficitCapacityBoundOrSingletonSAE"
NONREPLAY_SAE = "NonreplaySparseFirstBreakSAESummability"
MOVING_CARRIER = "MovingCarrierPhaseSlipPDECExclusion"
SQUARE_INPUT = "NoZeroRowAtXEqualsP_PlusOneRowAfterSquare"
SIGNED_ROW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_KZ = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

REDUCED_AMPLIFICATION = f"{SHORT_BLOCK} AND {LONG_TRANSFER}"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + SOURCE_FILES
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def build_rows(previous: dict[str, Any], transfer: dict[str, Any]) -> list[dict[str, Any]]:
    """构造零行块阶梯判定表。"""
    amplification_imported = previous.get("next_direct_attack_target") == AMPLIFICATION
    zero_block_imported = transfer.get("contiguous_zero_block_dichotomy_closed") is True
    return [
        row(
            "ReleaseMassAmplificationImported",
            amplification_imported,
            False,
            "上一层把 actual demand 的第一主攻压到首破裂释放质量放大或 singleton SAE。",
            AMPLIFICATION,
        ),
        row(
            "ContiguousZeroBlockImported",
            zero_block_imported,
            zero_block_imported,
            "early-to-square 分裂已给出：若 square-anchor 不接管，则有零行块 [x0,y-1] 和首破裂行 y。",
            "zero block [x0,y-1]",
        ),
        row(
            "BoundaryOnlyAmplificationBlocked",
            True,
            True,
            "首破裂释放列非空只给 D_y>=1；边界释放本身不能产生 Ω(H) 需求。",
            NO_BOUNDARY,
        ),
        row(
            "ZeroBlockCoverObligationMassClosed",
            True,
            True,
            "若零行块长度 L=y-x0，则块内每个 (t,c) 都有某 q<P 覆盖，源侧覆盖义务总数精确为 L(P-1)。",
            ZERO_BLOCK_MASS,
        ),
        row(
            "BlockLengthDichotomyClosed",
            True,
            True,
            "对任意阈值 A>=1，L<A 为短块 singleton/SAE 分支，L>=A 为长块覆盖质量转移或 PDEC 分支。",
            f"{SHORT_BLOCK} OR {LONG_TRANSFER}",
        ),
        row(
            "ShortBlockRoutedToSingletonSAE",
            True,
            False,
            "短零块没有足够行向质量自动超过 AP envelope；它必须作为 singleton/sparse SAE 或局部短块证书处理。",
            SHORT_BLOCK,
        ),
        row(
            "LongBlockNeedsMassTransfer",
            True,
            False,
            "长零块有 L(P-1) 覆盖义务，但仍需证明这些义务能非循环转移为 post-break AP demand；若转移失败，失败形态是持续覆盖历史 PDEC/ColumnCRT/SAE。",
            LONG_TRANSFER,
        ),
        row(
            "AmplificationReduced",
            True,
            False,
            "FirstBreakReleaseMassAmplificationOrSingletonSAE 被压成短块 SAE 排斥与长块覆盖质量转移/PDEC 二项。",
            REDUCED_AMPLIFICATION,
        ),
        row(
            "AmplificationProved",
            False,
            False,
            "本步没有证明释放质量已经放大到超过 envelope；只定位了唯一可放大的源头是前置零行块覆盖账本。",
            REDUCED_AMPLIFICATION,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、短块 SAE、长块质量转移、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {REDUCED_AMPLIFICATION} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造零行块阶梯证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.json")
    transfer = load_json(DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.json")
    rows = build_rows(previous, transfer)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {REDUCED_AMPLIFICATION} AND {PAYMENT_INJECTION} "
        f"AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} "
        f"AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "释放质量放大的源头被定位到首破裂前的连续零行块。边界释放只给单位需求；"
        "若零行块长度为 L，则源侧覆盖义务总量精确为 L(P-1)。因此短块必须进入 singleton/sparse SAE，"
        "长块则必须证明覆盖质量能非循环转移为 post-break AP demand；若转移失败，失败形态进入持续覆盖历史 "
        "PDEC/ColumnCRT/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_release_mass_zero_block_ladder_router",
        "status": "firstbreak_release_mass_reduced_to_zero_block_ladder_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": AMPLIFICATION,
        "hardpoint_after_router": REDUCED_AMPLIFICATION,
        "contiguous_zero_block_imported": transfer.get("contiguous_zero_block_dichotomy_closed") is True,
        "boundary_only_amplification_blocked": True,
        "zero_block_cover_obligation_mass_closed": True,
        "block_length_dichotomy_closed": True,
        "short_zero_block_singleton_sae_proved": False,
        "long_zero_block_mass_transfer_proved": False,
        "release_mass_amplification_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LONG_TRANSFER,
        "parallel_attack_targets": [SHORT_BLOCK, PAYMENT_INJECTION, STRICT_GAP, DENSE_TABLE, SPARSE_CELL, LOW_SAE, HIGH_RANK, NONREPLAY_SAE, MOVING_CARRIER],
        "reduced_inverse_alignment_branch": reduced_inverse,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 首破裂释放质量零行块阶梯证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"contiguous_zero_block_imported={fmt_bool(cert['contiguous_zero_block_imported'])}",
        f"boundary_only_amplification_blocked={fmt_bool(cert['boundary_only_amplification_blocked'])}",
        f"zero_block_cover_obligation_mass_closed={fmt_bool(cert['zero_block_cover_obligation_mass_closed'])}",
        f"block_length_dichotomy_closed={fmt_bool(cert['block_length_dichotomy_closed'])}",
        f"short_zero_block_singleton_sae_proved={fmt_bool(cert['short_zero_block_singleton_sae_proved'])}",
        f"long_zero_block_mass_transfer_proved={fmt_bool(cert['long_zero_block_mass_transfer_proved'])}",
        f"release_mass_amplification_proved={fmt_bool(cert['release_mass_amplification_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 零行块源质量",
        "",
        "设早期零行从 `x0` 开始，且 square-anchor 分支不接管。令 `y` 是首个非零行，",
        "于是 `[x0,y-1]` 是连续零行块，长度",
        "",
        "```text",
        "L = y - x0.",
        "```",
        "",
        "对每个 `t in [x0,y-1]` 和每个 `1<=c<P`，零行条件给出某个 `q<P` 使",
        "",
        "```text",
        "q | tP+c.",
        "```",
        "",
        "因此源侧覆盖义务总数不是估计，而是精确为",
        "",
        "```text",
        "L(P-1).",
        "```",
        "",
        "这才是可能产生放大的实际来源；首破裂释放列非空本身只给单位需求。",
        "",
        "## 2. 长短二分",
        "",
        "对任意阈值 `A>=1`，零行块只有两种情况：",
        "",
        "```text",
        "L < A   => short zero block / singleton-sparse SAE branch,",
        "L >= A  => long zero block cover-mass transfer or persistent PDEC branch.",
        "```",
        "",
        "短块没有足够行向质量自动压过 AP envelope；长块虽然有 `L(P-1)` 源质量，仍必须证明这些覆盖义务",
        "非循环地转移成 post-break 低 carrier AP demand。若不能转移，失败不再是匿名缺口，而是持续覆盖历史、",
        "固定相位表或 moving carrier 的 `PDEC/ColumnCRT/SAE` 出口。",
        "",
        "## 3. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{AMPLIFICATION}",
        f"  -> {SHORT_BLOCK}",
        f"  AND {LONG_TRANSFER}",
        "```",
        "",
        "其中 `LongZeroBlockCoverMassTransferToAPDemandOrPDEC` 是下一主攻：证明长零块覆盖义务必须变成",
        "post-break AP demand，或证明转移失败必产生命名 PDEC/SAE。",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 5. 新活动基",
            "",
            "inverse-alignment 回流分支更新为：",
            "",
            "```text",
            cert["reduced_inverse_alignment_branch"],
            "```",
            "",
            "合并 exact-UV/source-rank 前沿后的活动基：",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书不证明释放质量已经放大到超过 AP envelope。",
            "- 本证书只证明可能放大的源头必须是首破裂前的零行块覆盖义务，而不是边界单位释放。",
            "- 短块 singleton/sparse SAE 与长块覆盖质量转移/PDEC 仍未排斥。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """生成 JSON、ledger 和 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
