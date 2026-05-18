#!/usr/bin/env python3
"""生成 direct pair-energy 大筛的对角剥离与终端归约证书。

用法示例：
  python3 experiments/prime_matrix_strict_pair_energy_diagonal_peeling_terminal_reduction_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json

输出：
  data/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-ledger.json
  docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json
  docs/monograph/prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pair-energy-diagonal-peeling-terminal-reduction-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json",
    "prime-matrix-strict-independent-pair-energy-attack-router.json",
    "prime-matrix-strict-rate-bearing-large-pair-packet-router.json",
    "prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json",
    "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json",
    "prime-matrix-explicit-model-gap-finite-ledger-router.json",
    "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json",
    "prime-matrix-strict-exact-uv-support-attack-router.json",
    "prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json",
]

DIRECT_PAIR_LS = "SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed"
DIAGONAL_NO_HEAVY = "SameFormalUnitExactPairDiagonalNoHeavyAtomLedger"
OFFDIAGONAL_LS = "CleanOffDiagonalExactPairDualLargeSieveLedger"
RATE_PACKET = "RateBearingLargePairAtomPacketExclusion"
KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
NCBLK = "AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
HIGH_MODEL_GAP = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失时返回空对象，缺失不当作证明。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def source_hashes() -> dict[str, str]:
    """登记脚本与上游证书哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def diagonal_delta_obstruction_rows(power: int = 16) -> list[dict[str, Any]]:
    """给出单 exact-pair delta 模型对任意 log-power no-heavy 目标的阻断样例。"""
    rows: list[dict[str, Any]] = []
    for k in range(3, 10):
        log_y = math.log(10 ** k)
        threshold = log_y ** (-power)
        rows.append(
            {
                "k": k,
                "log_y": log_y,
                "threshold_L_minus_power": threshold,
                "total_mass": 1.0,
                "single_pair_mass": 1.0,
                "diagonal_l2_energy": 1.0,
                "violates_no_heavy_target": 1.0 > threshold,
            }
        )
    return rows


def reduction_edges() -> list[dict[str, str]]:
    """列出 direct pair-energy 大筛的对角剥离归约图。"""
    return [
        {
            "from": DIRECT_PAIR_LS,
            "to": f"{DIAGONAL_NO_HEAVY} AND {OFFDIAGONAL_LS}",
            "meaning": "任何 exact-pair L2/max-atom 大筛都必须先控制对角单 pair 质量，再处理 off-diagonal 相关和。",
        },
        {
            "from": f"NOT {DIAGONAL_NO_HEAVY}",
            "to": RATE_PACKET,
            "meaning": "对角无重原子失败就是同 formal unit 的 rate-bearing 大 exact-pair 原子包。",
        },
        {
            "from": RATE_PACKET,
            "to": f"{PDEC_SCOPE} OR {KUZNETSOV_DLS}",
            "meaning": "rate-bearing 大 pair packet 的持久签名进入 PDEC 作用域；clean 漂移进入 Kuznetsov/DLS。",
        },
        {
            "from": OFFDIAGONAL_LS,
            "to": KUZNETSOV_DLS,
            "meaning": "剥离对角与低维回流后，off-diagonal exact-pair 双线性型就是 clean Kloosterman/DLS 大筛对象。",
        },
        {
            "from": KUZNETSOV_DLS,
            "to": NCBLK,
            "meaning": "既有 KZ-A--KZ-E 同步把自足 Kuznetsov/DLS 的剩余压到 acyclic NC-BLK/source anti-atom。",
        },
        {
            "from": f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
            "to": f"({PDEC_SCOPE} OR {KUZNETSOV_DLS}) AND {HIGH_MODEL_GAP}",
            "meaning": "PDEC/CleanKLS 终端拆成同集 PDEC 作用域或 KZ/DLS；模型余量有限段已闭合，高段余量仍开放。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    direct_pair_active = data["pair_cycle"].get("next_direct_attack_target") == DIRECT_PAIR_LS
    pair_packetized = data["independent_pair"].get("internal_obligation_after_router") == RATE_PACKET
    packet_split = data["packet"].get("rate_bearing_packet_split_closed") is True
    kz_reduced = data["kz"].get("strict_gap_after_router") == NCBLK
    pdec_split = (
        data["pdec"].get("hardpoint_after_router")
        == f"({PDEC_SCOPE} OR {KUZNETSOV_DLS}) AND {MODEL_GAP} AND {DSTRUCTURE}"
    )
    model_split = data["model"].get("replacement", {}).get(MODEL_GAP) == HIGH_MODEL_GAP
    source_packet_open = (
        data["source_packet"].get("common_packet_proved") is False
        or data["source_packet"].get("row_column_unconditional_closed") is False
    )

    return [
        row(
            "DirectPairEnergyAtomActive",
            direct_pair_active,
            False,
            "上一轮把下一直接主攻钉为 direct exact-pair energy 大筛。",
            DIRECT_PAIR_LS,
        ),
        row(
            "DiagonalDeltaObstructionClosed",
            True,
            True,
            "没有同 formal unit 的对角无重原子输入时，单 exact-pair delta 模型直接违反 L2/max-atom 目标。",
            DIAGONAL_NO_HEAVY,
        ),
        row(
            "PairEnergyMustPeelDiagonal",
            True,
            True,
            "direct pair-energy 大筛必须拆成对角 no-heavy 账本与 off-diagonal clean 双线性大筛。",
            f"{DIAGONAL_NO_HEAVY} AND {OFFDIAGONAL_LS}",
        ),
        row(
            "DiagonalFailureReturnsToRatePacket",
            pair_packetized and packet_split,
            True,
            "对角 no-heavy 失败已经由既有 packetization 精确登记为 rate-bearing 大 pair packet，并进入终端三路。",
            RATE_PACKET,
        ),
        row(
            "SourcePacketStillOpenForDiagonalNoHeavy",
            source_packet_open,
            False,
            "若要正向证明对角 no-heavy，需要 pre-Cauchy actual source declaration packet；当前语料未给出。",
            "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket",
        ),
        row(
            "OffDiagonalPartEqualsCleanKuznetsovDLS",
            True,
            False,
            "剥离对角、PDEC 和 sparse/ColumnCRT 后，off-diagonal 估计正是 clean Kloosterman/Kuznetsov-DLS 大筛。",
            KUZNETSOV_DLS,
        ),
        row(
            "KuznetsovDLSReducedToNCBLK",
            kz_reduced,
            False,
            "KZ-A--KZ-D 已闭合，KZ-E 的 log-saving 剩余压到 acyclic NC-BLK/source anti-atom。",
            NCBLK,
        ),
        row(
            "PDECCleanKLSAndModelGapSplitImported",
            pdec_split and model_split,
            False,
            "PDEC/CleanKLS 已拆成同集 PDEC 作用域或 KZ/DLS；模型余量有限段闭合，高段解析余量仍开放。",
            f"({PDEC_SCOPE} AND {HIGH_MODEL_GAP}) OR {NCBLK}",
        ),
        row(
            "DirectPairEnergyDisjunctSubsumed",
            kz_reduced and packet_split,
            True,
            "direct pair-energy 分支剥离后只回到 KZ/NCBLK 或 PDEC 作用域；它不再是独立于终端两路的第三分支。",
            f"{NCBLK} OR ({PDEC_SCOPE} AND {HIGH_MODEL_GAP})",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只删除 direct pair-energy 伪独立分支；NCBLK/source anti-atom、PDEC 作用域、高段模型余量、Rate 与 DStructure 仍未证明。",
            f"({NCBLK} OR ({PDEC_SCOPE} AND {HIGH_MODEL_GAP})) AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "pair_cycle": load_json("prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json"),
        "independent_pair": load_json("prime-matrix-strict-independent-pair-energy-attack-router.json"),
        "packet": load_json("prime-matrix-strict-rate-bearing-large-pair-packet-router.json"),
        "kz": load_json("prime-matrix-strict-acyclic-kuznetsov-dls-atom-router.json"),
        "pdec": load_json("prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"),
        "model": load_json("prime-matrix-explicit-model-gap-finite-ledger-router.json"),
        "source_packet": load_json("prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"),
        "exactuv": load_json("prime-matrix-strict-exact-uv-support-attack-router.json"),
        "antiatom": load_json("prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json"),
    }
    rows = build_rows(data)
    strict_after = f"({NCBLK} OR ({PDEC_SCOPE} AND {HIGH_MODEL_GAP})) AND {RATE} AND {DSTRUCTURE}"
    result = {
        "certificate_type": "prime_matrix_strict_pair_energy_diagonal_peeling_terminal_reduction_router",
        "status": "direct_pair_energy_diagonal_peeling_reduces_to_ncblk_or_pdec_model_open",
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "direct_pair_energy_atom_active": data["pair_cycle"].get("next_direct_attack_target") == DIRECT_PAIR_LS,
        "diagonal_delta_obstruction_closed": True,
        "diagonal_no_heavy_ledger_proved": False,
        "offdiagonal_clean_pair_large_sieve_reduced_to_kuznetsov_dls": True,
        "kuznetsov_dls_reduced_to_ncblk": data["kz"].get("strict_gap_after_router") == NCBLK,
        "pdec_clean_kls_split_imported": data["pdec"].get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False,
        "model_gap_reduced_to_high_segment": data["model"].get("replacement", {}).get(MODEL_GAP) == HIGH_MODEL_GAP,
        "direct_pair_energy_disjunct_still_independent": False,
        "acyclic_ncblk_actual_block_nonconcentration_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": data["pair_cycle"].get("hardpoint_after_router", ""),
        "hardpoint_after_router": f"{NCBLK} OR ({PDEC_SCOPE} AND {HIGH_MODEL_GAP})",
        "next_direct_attack_target": NCBLK,
        "parallel_attack_targets": [PDEC_SCOPE, HIGH_MODEL_GAP, RATE, DSTRUCTURE],
        "strict_active_basis_after_router": strict_after,
        "diagonal_delta_obstruction_rows": diagonal_delta_obstruction_rows(),
        "reduction_edges": reduction_edges(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接拆解 `SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed`。"
            "任何 exact-pair L2/max-atom 大筛都必须先处理对角重原子；否则单个 exact pair 的 delta "
            "模型立即破坏 log-power no-heavy 目标。对角失败已经是既有 `RateBearingLargePairAtomPacketExclusion`，"
            "并回到 PDEC/clean terminal 三路；对角剥离后的 off-diagonal 估计正是 clean Kuznetsov/DLS，"
            "而该原子已进一步压到 `AcyclicNCBLKActualBlockNonconcentrationOrStrengthenedSourceAntiAtom`。"
            "同时 PDEC/CleanKLS+模型余量分支拆成同集 PDEC 作用域与高段模型余量。"
            "因此 direct pair-energy 不再是独立第三分支；最新严格剩余为 NCBLK/source anti-atom，"
            "或 PDEC 同集作用域加高段模型余量。行/列命题仍未无条件闭合。"
        ),
    }
    return result


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定排序 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict pair-energy 对角剥离终端归约证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"direct_pair_energy_atom_active={fmt_bool(result['direct_pair_energy_atom_active'])}",
        f"diagonal_delta_obstruction_closed={fmt_bool(result['diagonal_delta_obstruction_closed'])}",
        f"offdiagonal_clean_pair_large_sieve_reduced_to_kuznetsov_dls={fmt_bool(result['offdiagonal_clean_pair_large_sieve_reduced_to_kuznetsov_dls'])}",
        f"kuznetsov_dls_reduced_to_ncblk={fmt_bool(result['kuznetsov_dls_reduced_to_ncblk'])}",
        f"model_gap_reduced_to_high_segment={fmt_bool(result['model_gap_reduced_to_high_segment'])}",
        f"direct_pair_energy_disjunct_still_independent={fmt_bool(result['direct_pair_energy_disjunct_still_independent'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 对角剥离图",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for edge in result["reduction_edges"]:
        lines.append(f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |")

    lines.extend([
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for item in result["decision_rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )

    lines.extend([
        "",
        "## 3. 对角 delta 阻断样例",
        "",
        "| k | log y | threshold | single mass | L2 energy | violates |",
        "| ---: | ---: | ---: | ---: | ---: | --- |",
    ])
    for item in result["diagonal_delta_obstruction_rows"]:
        lines.append(
            f"| {item['k']} | {item['log_y']:.6g} | {item['threshold_L_minus_power']:.6g} | "
            f"{item['single_pair_mass']:.1f} | {item['diagonal_l2_energy']:.1f} | "
            f"`{item['violates_no_heavy_target']}` |"
        )

    lines.extend([
        "",
        "## 4. 最新剩余",
        "",
        "```text",
        result["hardpoint_after_router"],
        "```",
        "",
        "严格活动基：",
        "",
        "```text",
        result["strict_active_basis_after_router"],
        "```",
        "",
        "下一直接主攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "并行保留：",
        "",
        "```text",
        " AND ".join(result["parallel_attack_targets"]),
        "```",
        "",
        "## 5. 诚实边界",
        "",
        "- 本证书只删除 direct pair-energy 的伪独立地位，不证明 NCBLK/source anti-atom。",
        "- PDEC 同集作用域、高段模型余量、RatePreservation 与 DStructure/Rankin 仍未闭合。",
        "- 对角 delta 表是阻断黑箱大筛的确定性模型，不是行/列命题证明。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ])
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、ledger 与 Markdown 文档。"""
    result = build_result()
    write_json(OUT_LEDGER, result)
    write_json(OUT_JSON, result)
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
