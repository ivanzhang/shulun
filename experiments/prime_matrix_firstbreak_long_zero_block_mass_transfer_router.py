#!/usr/bin/env python3
"""生成首破裂长零块覆盖质量转移证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_long_zero_block_mass_transfer_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json

输出：
  data/prime-matrix-firstbreak-long-zero-block-mass-transfer-ledger.json
  docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json
  docs/monograph/prime-matrix-firstbreak-long-zero-block-mass-transfer-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-long-zero-block-mass-transfer-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json",
    DOCS / "prime-matrix-no-loss-return-accounting-router.md",
    DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.md",
    DOCS / "prime-matrix-strict-boundary-residual-mass-lower-bound-router.md",
    DOCS / "prime-matrix-bad-window-source-family-extraction-router.md",
    DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json",
]

LONG_TRANSFER = "LongZeroBlockCoverMassTransferToAPDemandOrPDEC"
NO_LOSS = "ZeroBlockHistoryProjectionNoLossLedger"
STABLE_OR_SWITCH = "StableLowCarrierPaymentTableOrHistorySwitchPDEC"
POSTBREAK_INJECTION = "PostBreakAPDemandInjectionFromStableHistory"
HISTORY_SWITCH = "HistorySwitchPDECOrColumnCRTExclusion"
SHORT_BLOCK = "ShortZeroBlockSingletonSAESummability"
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

REDUCED_TRANSFER = f"{NO_LOSS} AND {STABLE_OR_SWITCH} AND {POSTBREAK_INJECTION}"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def file_contains(path: Path, needle: str) -> bool:
    """检查文本文件中是否含有指定证据标记。"""
    if not path.exists():
        return False
    return needle in path.read_text(encoding="utf-8")


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


def build_rows(previous: dict[str, Any], no_loss_imported: bool) -> list[dict[str, Any]]:
    """构造长零块质量转移判定表。"""
    transfer_imported = previous.get("next_direct_attack_target") == LONG_TRANSFER
    zero_block_mass = previous.get("zero_block_cover_obligation_mass_closed") is True
    return [
        row(
            "LongZeroBlockTransferImported",
            transfer_imported,
            False,
            "上一层把释放质量放大主攻压到长零块覆盖质量转移或 PDEC。",
            LONG_TRANSFER,
        ),
        row(
            "ZeroBlockCoverObligationMassImported",
            zero_block_mass,
            zero_block_mass,
            "若零行块长度为 L，则源侧覆盖义务域 O_B 的大小精确为 L(P-1)。",
            "O_B={(t,c): x0<=t<y, 1<=c<P}",
        ),
        row(
            "CarrierResidueHistoryKeyDefined",
            True,
            True,
            "每个覆盖义务 q|tP+c 都给出 history key kappa=(q,a), a=c mod q，并对应行向 AP 条件 t==-a P^{-1} mod q。",
            "none for key definition",
        ),
        row(
            "NoLossReturnAccountingImported",
            no_loss_imported,
            no_loss_imported,
            "既有 no-loss 账本保证义务只能进入 SourceRecords 或 NamedReturnRecords，不允许无名消失。",
            NO_LOSS,
        ),
        row(
            "StableTableOrNamedSwitchRouteRegistered",
            True,
            False,
            "长零块历史若保持同一低 carrier/residue 支付表，则进入稳定表；若 key、carrier 或相位切换，则登记为 HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE。",
            f"{STABLE_OR_SWITCH} AND {HISTORY_SWITCH}",
        ),
        row(
            "StableHistoryPostBreakInjectionOpen",
            False,
            False,
            "仍未证明稳定历史表中的源侧质量必非循环注入首破裂后的 AP demand；不能从 AP envelope 饱和反推。",
            POSTBREAK_INJECTION,
        ),
        row(
            "HistorySwitchTerminalExcluded",
            False,
            False,
            "历史切换已命名为出口，但 PDEC/ColumnCRT/MovingCarrier/SAE 终端本身尚未排斥。",
            HISTORY_SWITCH,
        ),
        row(
            "LongZeroBlockMassTransferReduced",
            True,
            False,
            "LongZeroBlockCoverMassTransferToAPDemandOrPDEC 被压成无损投影、稳定表或命名切换、稳定历史注入三段。",
            REDUCED_TRANSFER,
        ),
        row(
            "LongZeroBlockMassTransferProved",
            False,
            False,
            "本步没有证明长零块覆盖质量已经产生 AP demand 矛盾；只关闭了无名逃逸口并暴露出稳定注入硬点。",
            f"{POSTBREAK_INJECTION} AND {HISTORY_SWITCH}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、短块 SAE、稳定历史注入、历史切换终端排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {REDUCED_TRANSFER} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造长零块质量转移证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-release-mass-zero-block-ladder-router.json")
    no_loss_imported = file_contains(
        DOCS / "prime-matrix-no-loss-return-accounting-router.md",
        "no_loss_return_accounting_closed=true",
    )
    rows = build_rows(previous, no_loss_imported)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {SHORT_BLOCK} AND {REDUCED_TRANSFER} AND {PAYMENT_INJECTION} "
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
        "长零块覆盖质量转移被压到一个更窄的非循环接口：零行块覆盖义务可按 "
        "carrier/residue history key 投影，no-loss 账本保证义务不会无名消失；"
        "若同一低 carrier 支付表稳定延续，则剩余硬点是证明其源侧质量会注入首破裂后的 AP demand；"
        "若支付表不稳定，则失败形态必须登记为 HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_long_zero_block_mass_transfer_router",
        "status": "long_zero_block_mass_transfer_reduced_to_stable_history_injection_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": LONG_TRANSFER,
        "hardpoint_after_router": REDUCED_TRANSFER,
        "zero_block_cover_obligation_mass_imported": previous.get("zero_block_cover_obligation_mass_closed") is True,
        "history_projection_key_defined": True,
        "no_loss_return_accounting_imported": no_loss_imported,
        "stable_table_or_named_switch_route_registered": True,
        "history_switch_pdec_excluded": False,
        "postbreak_ap_demand_injection_proved": False,
        "long_zero_block_mass_transfer_proved": False,
        "release_mass_amplification_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": POSTBREAK_INJECTION,
        "parallel_attack_targets": [
            HISTORY_SWITCH,
            SHORT_BLOCK,
            PAYMENT_INJECTION,
            STRICT_GAP,
            DENSE_TABLE,
            SPARSE_CELL,
            LOW_SAE,
            HIGH_RANK,
            NONREPLAY_SAE,
            MOVING_CARRIER,
        ],
        "reduced_inverse_alignment_branch": reduced_inverse,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 首破裂长零块覆盖质量转移证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"zero_block_cover_obligation_mass_imported={fmt_bool(cert['zero_block_cover_obligation_mass_imported'])}",
        f"history_projection_key_defined={fmt_bool(cert['history_projection_key_defined'])}",
        f"no_loss_return_accounting_imported={fmt_bool(cert['no_loss_return_accounting_imported'])}",
        f"stable_table_or_named_switch_route_registered={fmt_bool(cert['stable_table_or_named_switch_route_registered'])}",
        f"history_switch_pdec_excluded={fmt_bool(cert['history_switch_pdec_excluded'])}",
        f"postbreak_ap_demand_injection_proved={fmt_bool(cert['postbreak_ap_demand_injection_proved'])}",
        f"long_zero_block_mass_transfer_proved={fmt_bool(cert['long_zero_block_mass_transfer_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 义务域与 history key",
        "",
        "设长零块为 `B=[x0,y-1]`，长度 `L=y-x0`。上一层已经给出源侧覆盖义务域",
        "",
        "```text",
        "O_B={(t,c): x0<=t<y, 1<=c<P},   |O_B|=L(P-1).",
        "```",
        "",
        "对任意义务 `(t,c)`，零行条件给出某个 carrier `q<P` 使",
        "",
        "```text",
        "q | tP+c.",
        "```",
        "",
        "于是可定义同一 formal unit 内的历史键",
        "",
        "```text",
        "kappa=(q,a),   a == c mod q,   t == -a P^{-1} mod q.",
        "```",
        "",
        "这正是低 carrier AP table 的单元键；但它目前只是在零块历史中的支付键，不自动给出 post-break demand。",
        "",
        "## 2. 无损投影与切换出口",
        "",
        "no-loss return accounting 给出守恒口径：",
        "",
        "```text",
        "O_B = StableSourceRecords disjoint_union NamedReturnRecords,   Lost(O_B)=empty.",
        "```",
        "",
        "因此长零块质量不能无名消失。它只有两种合法去向：",
        "",
        "```text",
        "stable low-carrier/residue table  ->  PostBreakAPDemandInjectionFromStableHistory,",
        "history key/carrier/phase switch  ->  HistorySwitch-PDEC/ColumnCRT/MovingCarrier/SAE.",
        "```",
        "",
        "这一步把用户强调的“反例链与真实链的相位矛盾”具体化：若相位表长期稳定，就必须兑现为首破裂后的 AP demand；",
        "若相位表移动或换键，则它本身就是命名的历史切换异常，而不能再作为无名逃逸口。",
        "",
        "## 3. 新硬点",
        "",
        "因此当前硬点被压成：",
        "",
        "```text",
        f"{LONG_TRANSFER}",
        f"  -> {NO_LOSS}",
        f"  AND {STABLE_OR_SWITCH}",
        f"  AND {POSTBREAK_INJECTION}",
        "```",
        "",
        "其中前两段已经是账本/路由闭合口径；真正仍缺的是：稳定历史表如何在不借用 AP envelope 饱和的情况下，",
        "给出 post-break actual demand 下界。并行还必须排斥 history switch 的 PDEC/ColumnCRT/SAE 终端。",
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
            "- 本证书不证明长零块覆盖质量已经产生 AP demand 矛盾。",
            "- 本证书只证明该质量可按 history key 无损登记：稳定则进入注入硬点，移动则进入命名切换出口。",
            "- `PostBreakAPDemandInjectionFromStableHistory` 与 `HistorySwitchPDECOrColumnCRTExclusion` 仍未闭合。",
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
