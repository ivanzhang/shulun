#!/usr/bin/env python3
"""生成首破裂小 LCM 分支的 rank-pressure 压缩证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_small_lcm_rank_pressure_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.json

输出：
  data/prime-matrix-firstbreak-small-lcm-rank-pressure-ledger.json
  docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.json
  docs/monograph/prime-matrix-firstbreak-small-lcm-rank-pressure-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-small-lcm-rank-pressure-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-small-lcm-rank-pressure-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json",
    DOCS / "prime-matrix-strict-short-window-divisor-density-lcm-router.json",
    DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.md",
    DOCS / "prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md",
    DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json",
    DOCS / "prime-matrix-early-zero-terminal-schema-reconciliation-router.json",
]

SMALL_LCM = "SmallLCMColumnCRTPDECExclusion"
LOW_CARRIER = "LowCarrierFixedResidueColumnCRTPDECExclusion"
LOW_SAE = "LowCarrierNonpersistentSparseSAESummability"
HIGH_RANK = "HighCarrierRankDeficitCapacityBoundOrSingletonSAE"
MOVING_CARRIER = "MovingCarrierPhaseSlipPDECExclusion"
NONREPLAY_SAE = "NonreplaySparseFirstBreakSAESummability"
SQUARE_INPUT = "NoZeroRowAtXEqualsP_PlusOneRowAfterSquare"
SIGNED_ROW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_KZ = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

REDUCED_SMALL_LCM = f"{LOW_CARRIER} AND {LOW_SAE} AND {HIGH_RANK}"


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


def build_rows(previous: dict[str, Any], lcm_router: dict[str, Any], phase_schema: dict[str, Any]) -> list[dict[str, Any]]:
    """构造小 LCM rank-pressure 判定表。"""
    small_lcm_imported = SMALL_LCM in previous.get("hardpoint_after_router", "")
    lcm_discipline_imported = lcm_router.get("status") == (
        "short_window_divisor_density_reduced_to_lcm_multiplier_or_common_kernel_defect_open"
    )
    phase_schema_imported = phase_schema.get("early_zero_phase_defect_schema_admission_closed") is True
    return [
        row(
            "SmallLCMBranchImported",
            small_lcm_imported,
            False,
            "上一层把首破裂终端拆成 small-LCM、nonreplay sparse SAE、moving-carrier 三项。",
            SMALL_LCM,
        ),
        row(
            "PositiveReplayWidthGuardClosed",
            True,
            True,
            "fixed small-LCM replay 只有在 H=P-y>=1 时才有非零步长；若 y=P，则没有后续复现行，回到 square-anchor/SAE 边界。",
            "H>=1 for this branch",
        ),
        row(
            "DistinctPrimeProductLawClosed",
            True,
            True,
            "首破裂固定 carrier 标签是互异素数时，L=lcm(Lambda)=prod_{q in Lambda} q。",
            "none for formula",
        ),
        row(
            "SmallLCMRankPressureClosed",
            True,
            True,
            "小 LCM 分支满足 prod Lambda=L<=H=P-y；因此任意阈值 B 下，q>B 的 carrier 数至多 floor(log H/log B)。",
            "rank_{>B} <= floor(log H/log B)",
        ),
        row(
            "TwoLargeCarrierSqrtBarrierClosed",
            True,
            True,
            "特别地，两个 q>sqrt(H) 的 carrier 不能同时出现在同一固定 small-LCM formal unit 中。",
            HIGH_RANK,
        ),
        row(
            "ShortWindowLCMDisciplineImported",
            lcm_discipline_imported,
            True,
            "仓库已有 LCM 乘子纪律：不能制造 LCM 爆炸的高密度对象必须产生共同核/固定 residue 复现。",
            LOW_CARRIER,
        ),
        row(
            "LowCarrierFixedResidueRouteRegistered",
            True,
            phase_schema_imported,
            "若小 LCM 压力由 q<=B 的低 carrier 承担，则同一 q/residue 在 H 内反复出现；持久时是 ColumnCRT/PDEC。",
            LOW_CARRIER,
        ),
        row(
            "LowCarrierNonpersistentSparseRouteRegistered",
            True,
            phase_schema_imported,
            "若低 carrier 不持久复用固定 residue，则不能形成稳定支付链，只能作为 sparse SAE/LocalSurvivor 计费。",
            LOW_SAE,
        ),
        row(
            "HighCarrierRankDeficitRouteRegistered",
            True,
            False,
            "排除低 carrier 后，高 carrier rank 被 log H/log B 控制；若仍要覆盖反例压力，必须证明低秩容量不足或退化为 singleton SAE。",
            HIGH_RANK,
        ),
        row(
            "SmallLCMBranchReduced",
            True,
            False,
            "抽象 SmallLCMColumnCRTPDECExclusion 被压成低 carrier 固定 residue、低 carrier 稀疏 SAE、高 carrier rank deficit 三项。",
            REDUCED_SMALL_LCM,
        ),
        row(
            "SmallLCMBranchExcluded",
            False,
            False,
            "本步没有排斥三项终端，只关闭了 small-LCM 的 rank-pressure 结构。",
            REDUCED_SMALL_LCM,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 square-anchor 输入、小 LCM 三项、nonreplay SAE、moving carrier 与并行 signed/source 前沿。",
            f"({SQUARE_INPUT} AND {REDUCED_SMALL_LCM} AND {NONREPLAY_SAE} AND {MOVING_CARRIER}) OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) OR {NEW_JOINT} OR {EXTERNAL_KZ}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造小 LCM rank-pressure 证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-phase-slip-lcm-barrier-router.json")
    lcm_router = load_json(DOCS / "prime-matrix-strict-short-window-divisor-density-lcm-router.json")
    phase_schema = load_json(DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json")
    rows = build_rows(previous, lcm_router, phase_schema)
    reduced_inverse = (
        f"{SQUARE_INPUT} AND {REDUCED_SMALL_LCM} "
        f"AND {NONREPLAY_SAE} AND {MOVING_CARRIER}"
    )
    latest_basis = (
        f"(({reduced_inverse}) "
        f"OR ({SIGNED_ROW} AND {SOURCE_TABLE} AND {FIXED_KEY}) "
        f"OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "首破裂 small-LCM 分支已被压成 rank-pressure 三分："
        "固定 carrier 标签集满足 L=prod Lambda<=H=P-y，故任意阈值 B 以上的独立 carrier 数最多为 floor(log H/log B)，"
        "特别是两个大于 sqrt(H) 的 carrier 不可能同处一个 fixed small-LCM formal unit。"
        "因此小 LCM 若要承担反例压力，必须由低 carrier 固定 residue 复用、非持久稀疏 SAE，"
        "或高 carrier 低秩容量缺口来解释。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_small_lcm_rank_pressure_router",
        "status": "firstbreak_small_lcm_reduced_to_low_carrier_or_rank_deficit_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": SMALL_LCM,
        "hardpoint_after_router": REDUCED_SMALL_LCM,
        "distinct_prime_product_law_closed": True,
        "small_lcm_rank_pressure_closed": True,
        "two_large_carrier_sqrt_barrier_closed": True,
        "low_carrier_fixed_residue_route_registered": True,
        "low_carrier_nonpersistent_sparse_route_registered": True,
        "high_carrier_rank_deficit_route_registered": True,
        "small_lcm_branch_excluded": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LOW_CARRIER,
        "parallel_attack_targets": [LOW_SAE, HIGH_RANK, NONREPLAY_SAE, MOVING_CARRIER, SIGNED_ROW],
        "reduced_inverse_alignment_branch": reduced_inverse,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 首破裂 small-LCM rank-pressure 压缩证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"distinct_prime_product_law_closed={fmt_bool(cert['distinct_prime_product_law_closed'])}",
        f"small_lcm_rank_pressure_closed={fmt_bool(cert['small_lcm_rank_pressure_closed'])}",
        f"two_large_carrier_sqrt_barrier_closed={fmt_bool(cert['two_large_carrier_sqrt_barrier_closed'])}",
        f"small_lcm_branch_excluded={fmt_bool(cert['small_lcm_branch_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Rank-pressure 引理",
        "",
        "在首破裂 fixed small-LCM 分支中，必须有 `H=P-y>=1`；若 `y=P`，则没有后续非零复现步长，",
        "该分支直接回到 square-anchor/SAE 边界。活动 carrier 标签集 `Lambda` 由互异素数构成，且",
        "",
        "```text",
        "L = lcm(Lambda) = product_{q in Lambda} q <= H = P-y.",
        "```",
        "",
        "对任意阈值 `B>1`，若 `Lambda_>B={q in Lambda:q>B}`，则",
        "",
        "```text",
        "B^|Lambda_>B| < product_{q in Lambda_>B} q <= L <= H,",
        "```",
        "",
        "所以",
        "",
        "```text",
        "|Lambda_>B| <= floor(log H / log B).",
        "```",
        "",
        "取 `B=sqrt(H)` 得到最尖锐的局部结论：两个 `q>sqrt(H)` 的 carrier 不可能同时出现在同一个 fixed small-LCM formal unit 中。",
        "",
        "## 2. 三分出口",
        "",
        "小 LCM 分支因此不再是宽口径 ColumnCRT 标签，而被分成：",
        "",
        "```text",
        f"{SMALL_LCM}",
        f"  -> {LOW_CARRIER}",
        f"  AND {LOW_SAE}",
        f"  AND {HIGH_RANK}",
        "```",
        "",
        "- 低 carrier 固定 residue：若 `q<=B` 的低 carrier 持久承担压力，同一 `q/residue` 在 `H` 内反复出现，进入 ColumnCRT/PDEC。",
        "- 低 carrier 非持久：若固定 residue 不持久，则不能形成稳定支付链，只能进入 sparse SAE/LocalSurvivor。",
        "- 高 carrier 低秩：排除低 carrier 后，高 carrier 独立秩被 `log H/log B` 控制；若仍要覆盖反例压力，必须证明低秩容量不足或退化为 singleton SAE。",
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
            "- 本证书不证明 small-LCM 分支不存在。",
            "- 本证书只证明小 LCM 强制 carrier rank 受限，并把持续压力压入低 carrier 复用、稀疏 SAE 或高 carrier 低秩容量缺口。",
            "- 三个终端排斥仍未完成，行/列命题仍未无条件闭合。",
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
