#!/usr/bin/env python3
"""生成 pair-energy 到 signed 坐标环与终端三路的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_pair_energy_to_seed_coordinate_cycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json

输出：
  data/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-ledger.json
  docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json
  docs/monograph/prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pair-energy-to-seed-coordinate-cycle-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.json",
    "prime-matrix-strict-independent-pair-energy-attack-router.json",
    "prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json",
    "prime-matrix-strict-rate-bearing-large-pair-packet-router.json",
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
    "prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json",
    "prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json",
    "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
]

PAIR_ENERGY = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
DIRECT_PAIR_LS = "SelfContainedExactPairEnergyLargeSieveInequalityForAcyclicSeed"
RATE_PACKET = "RateBearingLargePairAtomPacketExclusion"
TERMINAL_THREE = (
    "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
    "DirectAcyclicSameSetPDECCapDualCertificate OR "
    "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
)
KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
COORD_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
JOINT_CONSTRUCTOR = "ExplicitJointAlphaDeltaPrimitiveWordCoefficientConstructorRuleForActualNoncanonicalSourceTuple"


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；缺失时返回空对象，避免把缺失误记为证明。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希，便于后续审查引用版本。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值渲染为 Markdown/JSON 中一致的小写文本。"""
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
    """登记依赖脚本和证书哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def sync_graph() -> list[dict[str, str]]:
    """整理 pair-energy 当前所有内部下降边与回流边。"""
    return [
        {
            "from": PAIR_ENERGY,
            "to": RATE_PACKET,
            "meaning": "独立 pair L2/max-atom 失败等价于同 formal unit 的 rate-bearing 大 exact-pair 原子包。",
        },
        {
            "from": RATE_PACKET,
            "to": TERMINAL_THREE,
            "meaning": "大原子包无第五出口，只能进入 canonical、direct PDEC、direct CleanKLS/DLS 三原子终端门。",
        },
        {
            "from": f"{PAIR_ENERGY} old ExactUV/source route",
            "to": f"{JOINT_CONSTRUCTOR} -> signed coordinate-source cycle",
            "meaning": "旧 ExactUV/source-entropy 脊柱回到同 formal unit primitive 核表和 signed 来源环，不能作为非循环证明。",
        },
        {
            "from": f"{JOINT_CONSTRUCTOR}",
            "to": f"{COORD_CYCLE_CUT} OR {TERMINAL_DESCENT}",
            "meaning": "若没有无环 primitive basis/coefficient 源输入，joint/signed 路线只能回流终端家族。",
        },
        {
            "from": SEED,
            "to": "PDEC/SAE/ColumnCRT/CleanKLS terminal family",
            "meaning": "seed 存在与不存在两支均已被路由到同一终端家族；seed 不再是独立逃逸口。",
        },
        {
            "from": TERMINAL_THREE,
            "to": f"{KUZNETSOV_DLS} OR ({PDEC_CLEAN_KLS} AND {MODEL_GAP})",
            "meaning": "canonical-lock 与 direct-terminal 标签继续下钻后，生产性数学出口压成自足 DLS 或 PDEC/CleanKLS+模型余量。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成当前同步判定表。"""
    alpha_target_active = data["alpha"].get("next_direct_attack_target") == PAIR_ENERGY
    pair_packetized = data["pair"].get("internal_obligation_after_router") == RATE_PACKET
    seed_only_blocked = data["pair"].get("seed_only_insufficient_model_verified") is True
    qualitative_blocked = data["pair"].get("qualitative_projection_dichotomy_insufficient_for_log_rate") is True
    old_spine_recursive = data["noncycle"].get("current_pair_energy_attack_spine_is_recursive") is True
    packet_trident = data["packet"].get("rate_bearing_packet_split_closed") is True
    terminal_recurrence = data["terminal"].get("terminal_route_returns_to_source_entropy_target") is True
    source_cycle = data["source_cycle"].get("seed_coordinate_source_cycle_detected") is True
    coord_cycle = data["coord_cycle"].get("seed_coordinate_source_cycle_detected") is True
    raw_cycle_rejected = data["coord_cycle"].get("raw_cycle_counts_as_closure") is False
    seed_fused = data["seed_fusion"].get("acyclic_pre_cauchy_seed_independent_input_removed") is True
    dls_open = (
        data["canonical_direct"].get("self_contained_kuznetsov_dls_large_sieve_inequality_proved")
        is False
    )
    pdec_open = data["canonical_direct"].get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    model_open = data["canonical_direct"].get("explicit_model_gap_and_finite_dprc_ledger_proved") is False

    return [
        row(
            "LatestPairEnergyTargetImported",
            alpha_target_active,
            False,
            "alpha-return 具体终端分裂把下一直接主攻钉为独立 pair L2/max-atom 能量界。",
            PAIR_ENERGY,
        ),
        row(
            "SeedOnlyAndQualitativeProjectionBlocked",
            seed_only_blocked and qualitative_blocked,
            True,
            "抽象 seed 与有限定性投影都不能给任意 log-power 速率。",
            RATE_PACKET,
        ),
        row(
            "LargePairFailurePacketized",
            pair_packetized,
            True,
            "pair-energy 失败已精确物化为同 formal unit 的 rate-bearing 大 pair packet。",
            RATE_PACKET,
        ),
        row(
            "RatePacketTerminalTridentImported",
            packet_trident,
            False,
            "大 pair packet 的合法出口只有 canonical-lock、direct PDEC、direct CleanKLS/DLS。",
            TERMINAL_THREE,
        ),
        row(
            "OldPairEnergySpineRejectedAsProof",
            old_spine_recursive and terminal_recurrence,
            True,
            "ExactUV/source-entropy/rate-packet 旧脊柱会回到原目标或终端家族，是回流不是证明。",
            "independent nonterminal proof or direct energy estimate",
        ),
        row(
            "SeedCoordinateSourceCycleSaturated",
            source_cycle and coord_cycle and raw_cycle_rejected,
            True,
            "signed row、basis word、coefficient assignment 与 word coordinate 已构成闭合来源环，不能继续当作下降量。",
            f"{COORD_CYCLE_CUT} OR {TERMINAL_DESCENT}",
        ),
        row(
            "SeedIndependentEscapeRemoved",
            seed_fused,
            True,
            "seed 存在/不存在两支均已回流同一 acyclic terminal family；seed 不是第四出口。",
            "PDEC/SAE/ColumnCRT/CleanKLS terminal family",
        ),
        row(
            "TerminalTridentConcretizedToDLSOrPDECModelGap",
            dls_open and pdec_open and model_open,
            False,
            "canonical/direct-terminal 标签继续下钻后，真正生产性数学出口是自足 Kuznetsov/DLS 或 PDEC/CleanKLS+模型余量。",
            f"{KUZNETSOV_DLS} OR ({PDEC_CLEAN_KLS} AND {MODEL_GAP})",
        ),
        row(
            "DirectPairEnergyLargeSieveCurrentCorpusProved",
            False,
            False,
            "当前语料尚未提交不经 source-coordinate 环的自足 pair-energy 大筛不等式。",
            DIRECT_PAIR_LS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只把抽象 pair-energy 硬点压成直接能量不等式/DLS/PDEC 三路；三路均未证明。",
            f"({DIRECT_PAIR_LS} OR {KUZNETSOV_DLS} OR ({PDEC_CLEAN_KLS} AND {MODEL_GAP})) AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书主体。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "alpha": load_json("prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.json"),
        "pair": load_json("prime-matrix-strict-independent-pair-energy-attack-router.json"),
        "noncycle": load_json("prime-matrix-strict-pair-energy-noncycle-reconciliation-router.json"),
        "packet": load_json("prime-matrix-strict-rate-bearing-large-pair-packet-router.json"),
        "terminal": load_json("prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"),
        "source_cycle": load_json("prime-matrix-strict-source-entropy-downstream-cycle-sync-router.json"),
        "coord_cycle": load_json("prime-matrix-strict-acyclic-seed-coordinate-source-cycle-guard-router.json"),
        "seed_fusion": load_json("prime-matrix-strict-acyclic-seed-terminal-fusion-router.json"),
        "canonical_direct": load_json("prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json"),
        "canonical_exit": load_json("prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"),
    }
    rows = build_rows(data)
    next_target = (
        f"{DIRECT_PAIR_LS} OR {KUZNETSOV_DLS} OR "
        f"({PDEC_CLEAN_KLS} AND {MODEL_GAP})"
    )
    strict_basis = f"({next_target}) AND {RATE} AND {DSTRUCTURE}"
    result = {
        "certificate_type": "prime_matrix_strict_pair_energy_to_seed_coordinate_cycle_sync_router",
        "status": "pair_energy_seed_coordinate_cycle_saturation_synced_to_direct_energy_or_terminal_trident_open",
        "frontier_sync_only": True,
        "counterexample_assumption_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "pair_energy_target_imported": data["alpha"].get("next_direct_attack_target") == PAIR_ENERGY,
        "seed_only_and_qualitative_projection_blocked": (
            data["pair"].get("seed_only_insufficient_model_verified") is True
            and data["pair"].get("qualitative_projection_dichotomy_insufficient_for_log_rate") is True
        ),
        "pair_energy_old_spine_recursive": data["noncycle"].get("current_pair_energy_attack_spine_is_recursive") is True,
        "rate_bearing_packet_terminal_trident_imported": data["packet"].get("rate_bearing_packet_split_closed") is True,
        "terminal_route_recurrence_detected": data["terminal"].get("terminal_route_returns_to_source_entropy_target") is True,
        "seed_coordinate_source_cycle_detected": data["coord_cycle"].get("seed_coordinate_source_cycle_detected") is True,
        "raw_coordinate_cycle_counts_as_closure": False,
        "seed_independent_escape_removed": data["seed_fusion"].get("acyclic_pre_cauchy_seed_independent_input_removed") is True,
        "direct_pair_energy_large_sieve_proved": False,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": PAIR_ENERGY,
        "hardpoint_after_router": next_target,
        "next_direct_attack_target": DIRECT_PAIR_LS,
        "parallel_terminal_targets": [KUZNETSOV_DLS, f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}"],
        "strict_active_basis_after_router": strict_basis,
        "sync_graph": sync_graph(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步继续攻击 `IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed`。"
            "seed-only 与定性投影已经不能给 log-power 速率；旧 ExactUV/source-entropy 脊柱又回到 "
            "signed 坐标-来源环和终端家族，不能作为非循环证明。"
            "因此 pair-energy 若要继续自足闭合，必须提交不经该来源环的直接 pair-energy 大筛不等式；"
            "否则只能落到已物化的终端三路：自足 Kuznetsov/DLS，或 PDEC/CleanKLS 加显式模型余量。"
            "这三路当前均未证明，所以行/列命题仍未无条件闭合。"
        ),
    }
    return result


def write_json(path: Path, obj: dict[str, Any]) -> None:
    """写入稳定排序 JSON。"""
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_md(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix strict pair-energy 到 signed 坐标环同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pair_energy_target_imported={fmt_bool(result['pair_energy_target_imported'])}",
        f"seed_only_and_qualitative_projection_blocked={fmt_bool(result['seed_only_and_qualitative_projection_blocked'])}",
        f"pair_energy_old_spine_recursive={fmt_bool(result['pair_energy_old_spine_recursive'])}",
        f"rate_bearing_packet_terminal_trident_imported={fmt_bool(result['rate_bearing_packet_terminal_trident_imported'])}",
        f"seed_coordinate_source_cycle_detected={fmt_bool(result['seed_coordinate_source_cycle_detected'])}",
        f"direct_pair_energy_large_sieve_proved={fmt_bool(result['direct_pair_energy_large_sieve_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步图",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for edge in result["sync_graph"]:
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
        "## 3. 最新剩余硬点",
        "",
        "抽象 pair-energy 硬点被压成三路：",
        "",
        "```text",
        result["hardpoint_after_router"],
        "```",
        "",
        "严格活动基仍需保留：",
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
        "并行终端目标：",
        "",
        "```text",
        " OR ".join(result["parallel_terminal_targets"]),
        "```",
        "",
        "## 4. 诚实边界",
        "",
        "- 本证书只完成前沿同步和回流识别，不证明直接 pair-energy 大筛、不证明 Kuznetsov/DLS，也不证明 PDEC/CleanKLS+模型余量。",
        "- signed 坐标-来源环不能作为证明使用；必须给无环新输入，或走命名终端排斥。",
        "- 行/列命题尚未无条件闭合。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ])
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、ledger 和 Markdown。"""
    result = build_result()
    write_json(OUT_LEDGER, result)
    write_json(OUT_JSON, result)
    OUT_MD.write_text(render_md(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
