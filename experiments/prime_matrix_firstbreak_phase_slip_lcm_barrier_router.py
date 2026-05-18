#!/usr/bin/env python3
"""生成首破裂相位滑移的 LCM-支撑宽度屏障证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_phase_slip_lcm_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json

输出：
  data/prime-matrix-firstbreak-phase-slip-lcm-barrier-ledger.json
  docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json
  docs/monograph/prime-matrix-firstbreak-phase-slip-lcm-barrier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-phase-slip-lcm-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-phase-slip-lcm-barrier-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.json",
    DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json",
    DOCS / "prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.json",
    DOCS / "prime-matrix-early-zero-terminal-package-reduction-router.json",
    DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json",
    DOCS / "prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json",
]

FIRST_BREAK = "FirstBreakPhaseSlipNamedReturnExclusion"
LCM_BARRIER = "FirstBreakFixedCarrierLCMWidthBarrier"
SMALL_LCM = "SmallLCMColumnCRTPDECExclusion"
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

REDUCED_FIRSTBREAK = f"{SMALL_LCM} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"


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


def build_rows(previous: dict[str, Any], phase_schema: dict[str, Any], stable_schema: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 LCM 屏障判定表。"""
    firstbreak_imported = previous.get("next_direct_attack_target") == FIRST_BREAK
    phase_schema_imported = phase_schema.get("early_zero_phase_defect_schema_admission_closed") is True
    stable_schema_imported = stable_schema.get("stable_short_return_or_defect_admission_schema_closed") is True
    return [
        row(
            "FirstBreakPhaseSlipImported",
            firstbreak_imported,
            False,
            "上一层把 early-to-square 抽象转移压到 square-zero 或首破裂 phase-slip 命名终端。",
            FIRST_BREAK,
        ),
        row(
            "CarrierPhaseMotionFormulaClosed",
            True,
            True,
            "首破裂 carrier q 的相位满足 rho_q(t+d)=rho_q(t)-dP mod q；因 (P,q)=1，同标签复现要求 q|d。",
            "none for formula",
        ),
        row(
            "FixedCarrierLCMReplayPeriodClosed",
            True,
            True,
            "对固定 carrier 标签集 Lambda，精确同标签复现步长 d 必须被 L=lcm(Lambda) 整除。",
            LCM_BARRIER,
        ),
        row(
            "SquareSupportWidthSharpened",
            True,
            True,
            "首破裂发生在 y 后，直到平方锚前只剩 H=P-y 个可复现步长；这比旧 short< P 自同构门更窄。",
            "support width H=P-y",
        ),
        row(
            "LCMExceedsWidthNoReplay",
            True,
            True,
            "若 L>H，则 1<=d<=H 内不存在固定 carrier 同标签复现；该 first-break 不能成为稳定短周期支付链。",
            f"{NONREPLAY_SAE} OR {MOVING_CARRIER}",
        ),
        row(
            "SmallLCMBranchIsStructured",
            True,
            False,
            "若 L<=H，则所有互异 carrier 的乘积已被 H<=P 控制；多标签复现只能落在小 LCM/固定列位移/ColumnCRT/PDEC 分支。",
            SMALL_LCM,
        ),
        row(
            "RepeatedCarrierResidueRouted",
            True,
            phase_schema_imported,
            "同一 q 或同一 residue 的重复使用不增加 L，但它正是 fixed-residue/ColumnCRT/PDEC 账本对象。",
            SMALL_LCM,
        ),
        row(
            "MovingCarrierIsNamedReturn",
            True,
            stable_schema_imported,
            "若反例链通过更换 carrier 标签逃避 LCM 屏障，则它不是 fixed replay，而是 moving-carrier phase slip，进入 PDEC/SAE 命名回流。",
            MOVING_CARRIER,
        ),
        row(
            "FirstBreakBarrierReduced",
            True,
            False,
            "首破裂终端已被分成小 LCM 固定复现、无复现稀疏 SAE、moving-carrier PDEC 三项；不再保留抽象 phase-slip 终端。",
            REDUCED_FIRSTBREAK,
        ),
        row(
            "FirstBreakNamedReturnExclusionProved",
            False,
            False,
            "本步只关闭固定 carrier 复现的合成模数屏障；尚未排斥小 LCM PDEC、非复现 SAE 或 moving-carrier PDEC。",
            REDUCED_FIRSTBREAK,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、上述三项终端排斥，或并行 signed-row/source-rank 前沿闭合。",
            f"({SQUARE_INPUT} AND {REDUCED_FIRSTBREAK}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 LCM 屏障证书。"""
    previous = load_json(DOCS / "prime-matrix-early-to-square-phase-transfer-split-router.json")
    phase_schema = load_json(DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json")
    stable_schema = load_json(DOCS / "prime-matrix-strict-stable-short-return-defect-terminal-schema-sync-router.json")
    rows = build_rows(previous, phase_schema, stable_schema)
    reduced_inverse_alignment = f"{SQUARE_INPUT} AND {REDUCED_FIRSTBREAK}"
    latest_basis = (
        f"(({reduced_inverse_alignment}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "首破裂 phase-slip 的固定 carrier 复现已经被压成 LCM-支撑宽度屏障："
        "若释放相位在首破裂行 y 之后以同一 carrier 标签集复现，则复现步长 d 必须被所有活动 carrier 的 lcm 整除；"
        "但到平方锚前的支撑宽度只有 H=P-y。"
        "因此 L>H 时没有非零复现，L<=H 时只剩小 LCM/ColumnCRT/PDEC 分支；"
        "逃避固定标签的情形必须登记为 moving-carrier PDEC/SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_phase_slip_lcm_barrier_router",
        "status": "firstbreak_phase_slip_lcm_width_barrier_closed_terminal_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": FIRST_BREAK,
        "hardpoint_after_router": REDUCED_FIRSTBREAK,
        "firstbreak_imported": previous.get("next_direct_attack_target") == FIRST_BREAK,
        "carrier_phase_motion_formula_closed": True,
        "fixed_carrier_lcm_replay_period_closed": True,
        "square_support_width_sharpened_to_p_minus_y": True,
        "lcm_exceeds_width_no_fixed_replay": True,
        "small_lcm_branch_structured_but_not_excluded": True,
        "moving_carrier_named_return": True,
        "firstbreak_phase_slip_named_return_exclusion_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SMALL_LCM,
        "parallel_attack_targets": [NONREPLAY_SAE, MOVING_CARRIER, SIGNED_ROW, SOURCE_TABLE, FIXED_KEY],
        "reduced_inverse_alignment_branch": reduced_inverse_alignment,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 首破裂 phase-slip LCM-支撑宽度屏障证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"fixed_carrier_lcm_replay_period_closed={fmt_bool(cert['fixed_carrier_lcm_replay_period_closed'])}",
        f"square_support_width_sharpened_to_p_minus_y={fmt_bool(cert['square_support_width_sharpened_to_p_minus_y'])}",
        f"lcm_exceeds_width_no_fixed_replay={fmt_bool(cert['lcm_exceeds_width_no_fixed_replay'])}",
        f"firstbreak_phase_slip_named_return_exclusion_proved={fmt_bool(cert['firstbreak_phase_slip_named_return_exclusion_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 屏障定理",
        "",
        "设首破裂发生在行 `y<=P`，上一行 `y-1` 仍是零行。取释放 formal unit 的活动 carrier 标签集",
        "`Lambda={q_1,...,q_s}`。若同一释放相位模式在 `y+d` 复现，并且 carrier 标签不移动，则每个活动标签都要求",
        "",
        "```text",
        "rho_q(y+d)=rho_q(y),",
        "rho_q(t)=-tP mod q.",
        "```",
        "",
        "因此",
        "",
        "```text",
        "dP == 0 mod q.",
        "```",
        "",
        "由于 `q<P` 且 `q` 为素数，`(P,q)=1`，所以 `q|d`。于是",
        "",
        "```text",
        "lcm(Lambda) | d.",
        "```",
        "",
        "从首破裂行到平方锚前的可复现宽度只有",
        "",
        "```text",
        "H=P-y.",
        "```",
        "",
        "若 `lcm(Lambda)>H`，则 `1<=d<=H` 内没有非零固定标签复现。若 `lcm(Lambda)<=H`，则活动 carrier 的合成模数已被 `H<=P` 控制，只能进入小 LCM/固定 residue 的 ColumnCRT/PDEC 分支。",
        "",
        "## 2. 三分出口",
        "",
        "首破裂 phase-slip 终端由此分成三类：",
        "",
        "```text",
        "FirstBreakPhaseSlipNamedReturnExclusion",
        f"  -> {SMALL_LCM}",
        f"  AND {NONREPLAY_SAE}",
        f"  AND {MOVING_CARRIER}",
        "```",
        "",
        "- 小 LCM 分支：固定 carrier 标签可在剩余宽度内复现，必须作为小合成模数 ColumnCRT/PDEC 排斥。",
        "- 无复现分支：`lcm>H`，不能形成稳定短周期支付链；若只孤立出现，进入 sparse SAE/LocalSurvivor 可求和问题。",
        "- moving-carrier 分支：若通过更换 carrier 标签逃避 LCM 屏障，则不再是固定同标签复现，而是 moving family PDEC/SAE。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 新活动基",
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
            "## 5. 诚实边界",
            "",
            "- 本证书不证明首破裂不存在。",
            "- 本证书只排除了固定 carrier 同标签复现在 `lcm>H` 时的可能性。",
            "- 小 LCM PDEC、非复现 sparse SAE、moving-carrier PDEC 仍需继续排斥。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
