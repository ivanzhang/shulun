#!/usr/bin/env python3
"""生成稳定 history 到 post-break AP 到达二分证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_stable_history_ap_arrival_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json

输出：
  data/prime-matrix-firstbreak-stable-history-ap-arrival-ledger.json
  docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.json
  docs/monograph/prime-matrix-firstbreak-stable-history-ap-arrival-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-stable-history-ap-arrival-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-stable-history-ap-arrival-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json",
    DOCS / "prime-matrix-firstbreak-low-carrier-ap-envelope-router.json",
    DOCS / "prime-matrix-firstbreak-actual-demand-source-cut-router.json",
    DOCS / "prime-matrix-no-loss-return-accounting-router.md",
    DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.md",
]

POSTBREAK_INJECTION = "PostBreakAPDemandInjectionFromStableHistory"
AP_SUCCESSOR = "StableHistoryAPSuccessorDichotomyLedger"
ARRIVAL_INJECTION = "ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse"
TERMINAL_NONARRIVAL = "TerminalNonarrivalLargeStepEscapePDECOrSAE"
ARRIVAL_COLLISION = "ArrivalCollisionOrDuplicatePaymentReturnLedger"
NO_LOSS = "ZeroBlockHistoryProjectionNoLossLedger"
STABLE_OR_SWITCH = "StableLowCarrierPaymentTableOrHistorySwitchPDEC"
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

REDUCED_INJECTION = f"{AP_SUCCESSOR} AND {ARRIVAL_INJECTION} AND {TERMINAL_NONARRIVAL}"


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 AP 到达二分判定表。"""
    injection_imported = previous.get("next_direct_attack_target") == POSTBREAK_INJECTION
    stable_route_imported = previous.get("stable_table_or_named_switch_route_registered") is True
    return [
        row(
            "PostBreakInjectionImported",
            injection_imported,
            False,
            "上一层把长零块稳定 history 分支的直接主攻设为 post-break AP demand 注入。",
            POSTBREAK_INJECTION,
        ),
        row(
            "StableHistoryRouteImported",
            stable_route_imported,
            stable_route_imported,
            "稳定低 carrier/residue 支付表已经从长零块无损投影中分离出来。",
            STABLE_OR_SWITCH,
        ),
        row(
            "APRowClassFormulaClosed",
            True,
            True,
            "对 history key kappa=(q,a)，因 (P,q)=1，行集合精确为 t==-a P^{-1} mod q。",
            AP_SUCCESSOR,
        ),
        row(
            "LastPrebreakHitSuccessorClosed",
            True,
            True,
            "若 t_* 是同 key 在零块 B=[x0,y-1] 中的最后一次命中，则下一次同 key 行必为 t_*+q；且由最后性知 t_*+q>=y。",
            AP_SUCCESSOR,
        ),
        row(
            "ArrivalNonarrivalDichotomyClosed",
            True,
            True,
            "同 key 后继命中落入 post-break 支撑 I_y=[y,P-1] 当且仅当 q<=P-1-t_*；否则 q>=P-t_*，成为 terminal nonarrival。",
            f"{ARRIVAL_INJECTION} OR {TERMINAL_NONARRIVAL}",
        ),
        row(
            "TerminalNonarrivalLargeStepRegistered",
            True,
            False,
            "未到达不是 demand：它精确表示 AP 步长超过平方锚前剩余支撑宽度，必须登记为 large-step escape/PDEC/SAE。",
            TERMINAL_NONARRIVAL,
        ),
        row(
            "ArrivalCandidateRegistered",
            True,
            False,
            "到达事件只给 post-break AP cell 候选；仍需证明该候选确实承担 actual demand，且不通过 envelope 饱和反推。",
            ARRIVAL_INJECTION,
        ),
        row(
            "ArrivalCollisionReturnRegistered",
            True,
            False,
            "若到达候选被重复支付、碰撞或换源吸收，则必须回到 duplicate/collision return 账本，不能删除。",
            ARRIVAL_COLLISION,
        ),
        row(
            "PostBreakInjectionReduced",
            True,
            False,
            "PostBreakAPDemandInjectionFromStableHistory 被压成 AP 后继二分、到达候选 actual 注入、未到达 large-step 出口三项。",
            REDUCED_INJECTION,
        ),
        row(
            "PostBreakInjectionProved",
            False,
            False,
            "本步没有证明稳定 history 已产生 actual demand 下界；只关闭了 AP 后继到达/越界的精确二分。",
            f"{ARRIVAL_INJECTION} AND {TERMINAL_NONARRIVAL}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、短块 SAE、到达候选 actual 注入、terminal nonarrival 排斥、history switch 排斥、低 carrier 支付注入、strict-gap/PDEC/SAE 与 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} AND {REDUCED_INJECTION} AND {PAYMENT_INJECTION} AND {STRICT_GAP} AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造稳定 history AP 到达二分证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-long-zero-block-mass-transfer-router.json")
    rows = build_rows(previous)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {SHORT_BLOCK} AND {NO_LOSS} AND {STABLE_OR_SWITCH} "
        f"AND {REDUCED_INJECTION} AND {PAYMENT_INJECTION} AND {STRICT_GAP} "
        f"AND {DENSE_TABLE} AND {SPARSE_CELL} AND {LOW_SAE} AND {HIGH_RANK} "
        f"AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "稳定 history 到 post-break AP demand 的注入被压到 AP 后继二分："
        "同一 history key 的零块最后命中 t_* 后，下一次同余行精确为 t_*+q；"
        "若 t_*+q<=P-1，则得到 post-break AP arrival candidate；若 t_*+q>=P，"
        "则该 key 在平方锚前没有支撑，必须登记为 terminal nonarrival/large-step escape。"
        "到达候选仍未自动成为 actual demand。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_stable_history_ap_arrival_router",
        "status": "stable_history_injection_reduced_to_ap_arrival_dichotomy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": POSTBREAK_INJECTION,
        "hardpoint_after_router": REDUCED_INJECTION,
        "stable_history_route_imported": previous.get("stable_table_or_named_switch_route_registered") is True,
        "ap_row_class_formula_closed": True,
        "last_prebreak_hit_successor_closed": True,
        "arrival_nonarrival_dichotomy_closed": True,
        "terminal_nonarrival_large_step_registered": True,
        "arrival_candidate_registered": True,
        "arrival_candidate_actual_demand_proved": False,
        "terminal_nonarrival_excluded": False,
        "postbreak_ap_demand_injection_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ARRIVAL_INJECTION,
        "parallel_attack_targets": [
            TERMINAL_NONARRIVAL,
            ARRIVAL_COLLISION,
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
        "# Prime Matrix 稳定 history 的 AP 到达二分证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"stable_history_route_imported={fmt_bool(cert['stable_history_route_imported'])}",
        f"ap_row_class_formula_closed={fmt_bool(cert['ap_row_class_formula_closed'])}",
        f"last_prebreak_hit_successor_closed={fmt_bool(cert['last_prebreak_hit_successor_closed'])}",
        f"arrival_nonarrival_dichotomy_closed={fmt_bool(cert['arrival_nonarrival_dichotomy_closed'])}",
        f"terminal_nonarrival_large_step_registered={fmt_bool(cert['terminal_nonarrival_large_step_registered'])}",
        f"arrival_candidate_registered={fmt_bool(cert['arrival_candidate_registered'])}",
        f"arrival_candidate_actual_demand_proved={fmt_bool(cert['arrival_candidate_actual_demand_proved'])}",
        f"terminal_nonarrival_excluded={fmt_bool(cert['terminal_nonarrival_excluded'])}",
        f"postbreak_ap_demand_injection_proved={fmt_bool(cert['postbreak_ap_demand_injection_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 后继行精确公式",
        "",
        "对稳定 history key `kappa=(q,a)`，低 carrier AP 行类为",
        "",
        "```text",
        "t == -a P^{-1} mod q.",
        "```",
        "",
        "令 `t_*` 是该 key 在零块 `B=[x0,y-1]` 中的最后一次命中。因为同一行类的相邻命中相差 `q`，",
        "下一次同 key 行精确为",
        "",
        "```text",
        "t_next = t_* + q.",
        "```",
        "",
        "由 `t_*` 的最后性，若 `t_next<y` 就仍在零块内并矛盾，因此必有 `t_next>=y`。",
        "",
        "## 2. 到达/越界二分",
        "",
        "post-break 支撑为 `I_y=[y,P-1]`，宽度 `H=P-y`。于是",
        "",
        "```text",
        "arrival candidate      <=> t_*+q <= P-1 <=> q <= P-1-t_*,",
        "terminal nonarrival   <=> t_*+q >= P   <=> q >= P-t_*.",
        "```",
        "",
        "这给出稳定 history 注入的精确相位门。到达只是 AP cell 候选；未到达不是需求，而是 AP 周期超过",
        "平方锚前支撑宽度的 large-step escape，必须进入 `PDEC/SAE` 或 moving/terminal 账本。",
        "",
        "## 3. 新硬点",
        "",
        "因此",
        "",
        "```text",
        f"{POSTBREAK_INJECTION}",
        f"  -> {AP_SUCCESSOR}",
        f"  AND {ARRIVAL_INJECTION}",
        f"  AND {TERMINAL_NONARRIVAL}",
        "```",
        "",
        "当前真正剩余是：到达候选如何不借用 envelope 饱和而变成 actual demand；以及未到达 large-step 出口如何排斥或求和。",
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
            "- 本证书不证明稳定 history 已经注入 actual demand。",
            "- 本证书只证明每个稳定 key 的下一 AP 行有精确到达/越界二分。",
            "- `ArrivalCandidateActualDemandInjectionWithoutEnvelopeReuse` 与 `TerminalNonarrivalLargeStepEscapePDECOrSAE` 仍未闭合。",
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
