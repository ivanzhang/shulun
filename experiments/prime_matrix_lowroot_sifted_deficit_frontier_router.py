#!/usr/bin/env python3
"""生成 low-root 筛余缺口前沿证书。

用法示例：
  python3 experiments/prime_matrix_lowroot_sifted_deficit_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json

输出：
  data/prime-matrix-lowroot-sifted-deficit-frontier-ledger.json
  docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.json
  docs/monograph/prime-matrix-lowroot-sifted-deficit-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-lowroot-sifted-deficit-frontier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-lowroot-sifted-deficit-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-lowroot-sifted-deficit-frontier-router.md"

SOURCE_FILES = [
    "prime-matrix-row-gap-supply-phase-cycle-cut-router.json",
    "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.json",
    "prime-matrix-strict-stable-short-return-defect-attack-router.json",
    "prime-matrix-strict-named-return-exclusion-compression-router.json",
]

LOWROOT_DEFICIT = "UniformLowRootSiftedResidueDeficitAfterNearRootSlots"
ROUGH_LOWER = "NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP"
ROOT_UPPER = "NearRootSemiprimeSlotCapacityUpperBound"
Q1Q2_TRANSPORT = "AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
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


def build_rows(row_gap: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 low-root 前沿判定表。"""
    row_gap_imported = row_gap.get("next_direct_attack_target") == LOWROOT_DEFICIT
    return [
        row(
            "LowRootDeficitTargetImported",
            row_gap_imported,
            False,
            "上一层把具体零行模型压到低根筛余扣除近根槽后的统一正缺口。",
            LOWROOT_DEFICIT,
        ),
        row(
            "ExactDeficitIdentityClosed",
            True,
            True,
            "对 1<=a<P，未被 q<=sqrt(kP+P-1) 覆盖的槽等价于 kP+a 为素数。",
            "full_uncovered_slots equals row prime slots",
        ),
        row(
            "NearRootSlotUpperBoundElementary",
            True,
            True,
            "近根素数只在 sqrt(kP)<q<=sqrt(kP+P-1) 中出现；每个 q 只给一个 residue class，容量有初等上界。",
            ROOT_UPPER,
        ),
        row(
            "RawCapacityStillIrrelevant",
            True,
            True,
            "低根 raw capacity 带重数大并不推出覆盖；反过来容量大也不构成矛盾。",
            "need sifted residue lower bound, not raw capacity",
        ),
        row(
            "MertensHeuristicNotProof",
            True,
            True,
            "Mertens 密度预测给出约 P/log(kP) 个筛余槽，但短区间逐行下界不能由平均密度替代。",
            ROUGH_LOWER,
        ),
        row(
            "JacobsthalBarrierIdentified",
            True,
            False,
            "要无条件排除零行，需要证明长度 P 的指定相位短区间不能被低根 residue classes 与近根槽完全覆盖。",
            ROUGH_LOWER,
        ),
        row(
            "Q1Q2TransportParallelStillNeeded",
            True,
            False,
            "若低根筛余下界无法直接给出，必须从相邻素数 Q1/Q2 的 CRT 传输中逼出短复现或登记缺陷。",
            Q1Q2_TRANSPORT,
        ),
        row(
            "LowRootDeficitCurrentCorpusProved",
            False,
            False,
            "当前材料没有给出统一短区间 rough-residue 下界；样本正缺口不能替代证明。",
            ROUGH_LOWER,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "近根容量上界和精确等价已闭合，但核心 low-root 筛余下界仍未证明。",
            f"({ROUGH_LOWER} OR {Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造证书。"""
    row_gap = load_json("prime-matrix-row-gap-supply-phase-cycle-cut-router.json")
    rows = build_rows(row_gap)
    strict_basis = (
        f"({ROUGH_LOWER} OR {Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE}) "
        f"AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "`UniformLowRootSiftedResidueDeficitAfterNearRootSlots` 被进一步拆解：近根槽的来源与容量"
        "可以初等控制，真正缺口是长度 P、筛到 sqrt(kP) 的指定相位短区间 rough-residue 正下界。"
        "Mertens 密度只给启发，不能替代逐行下界；否则会把目标行命题循环写回自身。若该下界"
        "暂不能证明，必须转攻 Q1/Q2 CRT 传输的短复现/登记缺陷，或给循环外 seed/PDEC 输入。"
    )
    return {
        "certificate_type": "prime_matrix_lowroot_sifted_deficit_frontier_router",
        "status": "lowroot_deficit_reduced_to_short_interval_rough_residue_lower_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "exact_deficit_identity_closed": True,
        "near_root_slot_upper_bound_elementary": True,
        "mertens_heuristic_not_proof": True,
        "jacobsthal_barrier_identified": True,
        "noncircular_short_interval_rough_residue_lower_bound_proved": False,
        "q1q2_transport_parallel_still_needed": True,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ROUGH_LOWER,
        "parallel_attack_targets": [Q1Q2_TRANSPORT, SEED_CYCLE_CUT, PDEC_SCOPE],
        "strict_internal_basis_after_router": strict_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix low-root 筛余缺口前沿证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        "exact_deficit_identity_closed=true",
        "near_root_slot_upper_bound_elementary=true",
        "mertens_heuristic_not_proof=true",
        "jacobsthal_barrier_identified=true",
        "noncircular_short_interval_rough_residue_lower_bound_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. 精确等价",
        "",
        "在 `I_k={kP+a:1<=a<P}` 中，`kP+a<P^2`。因此若某个槽没有被任何",
        "`q<=sqrt(kP+P-1)` 覆盖，它不可能是合数，只能是素数。于是：",
        "",
        "```text",
        "full_uncovered_slots > 0  <=>  row contains a prime.",
        "```",
        "",
        "这说明 low-root 缺口目标非常锋利：它不是辅助弱估计，而是行命题的核心等价形式。",
        "",
        "## 2. 近根槽",
        "",
        "近根槽只来自",
        "",
        "```text",
        "sqrt(kP) < q <= sqrt(kP+P-1).",
        "```",
        "",
        "每个这样的 `q` 在 row 内只给一个 residue class，容量有初等上界；它不是主要未知。",
        "主要未知是低根覆盖后仍能保留多少 rough residue。",
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
            "## 4. 最新非循环基",
            "",
            "```text",
            cert["strict_internal_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "## 5. 诚实边界",
            "",
            "- 本证书不把 Mertens 平均密度当作短区间逐行证明。",
            "- 本证书不证明 row-gap 不存在；它把剩余压到短区间 rough-residue 正下界或 Q1/Q2 传输矛盾。",
            "- 若直接证明 rough-residue 下界失败，必须从相位传输、seed cycle-cut 或 PDEC 作用域匹配破环。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(cert["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    OUT_LEDGER.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
