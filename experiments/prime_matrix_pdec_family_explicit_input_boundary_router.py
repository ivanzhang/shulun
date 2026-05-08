#!/usr/bin/env python3
"""固定广义 PDEC family 的显式输入边界。

用法示例：
  python3 experiments/prime_matrix_pdec_family_explicit_input_boundary_router.py

输出：
  docs/monograph/prime-matrix-pdec-family-explicit-input-boundary-router.json
  docs/monograph/prime-matrix-pdec-family-explicit-input-boundary-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SAE_ABSORB = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.json"
DEFAULT_PERSISTENT = DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.json"
DEFAULT_NONTAUTOLOGICAL = DOCS / "prime-matrix-nontautological-pdec-admission-audit.json"
DEFAULT_PRIMITIVE_RANK = DOCS / "prime-matrix-pdec-cap-primitive-multiatom-rank-router.json"
DEFAULT_RANKTWO = DOCS / "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.json"
DEFAULT_FINITE_BASIS = DOCS / "prime-matrix-pdec-cap-uniform-cap-finite-basis-router.json"
DEFAULT_FINITE_ARC = DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.json"
DEFAULT_TRANSVERSE_CLEAN = DOCS / "prime-matrix-pdec-cap-transverse-clean-reduction-router.json"
DEFAULT_CLEAN_FRONTIER = DOCS / "prime-matrix-pdec-cap-transverse-clean-atom-frontier-router.json"
DEFAULT_CANONICAL_LAYER = DOCS / "prime-matrix-pdec-cap-canonical-layer-closure-router.json"
DEFAULT_PDEC_BOUNDARY_LIFT = DOCS / "prime-matrix-self-contained-pdec-cap-boundary-lift-router.json"
DEFAULT_NONCANONICAL_TRILEMMA = DOCS / "prime-matrix-noncanonical-complement-trilemma-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造 PDEC family 边界行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    sae_absorb: dict[str, Any],
    persistent: dict[str, Any],
    nontautological: dict[str, Any],
    primitive_rank: dict[str, Any],
    ranktwo: dict[str, Any],
    finite_basis: dict[str, Any],
    finite_arc: dict[str, Any],
    transverse_clean: dict[str, Any],
    clean_frontier: dict[str, Any],
    canonical_layer: dict[str, Any],
    pdec_boundary_lift: dict[str, Any],
    noncanonical_trilemma: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成广义 PDEC family 显式输入边界表。"""
    sae_removed = (
        sae_absorb.get("sae_independent_terminal_removed") is True
        and sae_absorb.get("terminal_package_fully_proved") is False
    )
    persistent_boundary = (
        persistent.get("persistent_terminal_admission_boundary_closed") is True
        and persistent.get("current_materialized_persistent_terminal_instances_closed") is True
        and persistent.get("narrowest_next_hardpoint")
        == "PrimitiveMultiAtomSameFormalUnitPDECCertificate"
    )
    no_current_nontautological = (
        nontautological.get("current_materialized_nontautological_pdec_candidate_count")
        == 0
        and nontautological.get("all_current_routes_blocked_or_absorbed") is True
    )
    primitive_boundary = (
        primitive_rank.get("primitive_multiatom_rank_boundary_closed") is True
        and primitive_rank.get("current_materialized_primitive_multiatom_instances_closed")
        is True
        and primitive_rank.get("narrowest_next_hardpoint")
        == "RankTwoCapStablePrimitivePDECKernelInequality"
    )
    ranktwo_inverse = (
        ranktwo.get("ranktwo_capstable_kernel_inequality_closed") is True
        and ranktwo.get("narrowest_next_hardpoint")
        == "UniformCapStabilityCertificateForRankTwoPrimitiveKernels"
    )
    finite_cap_basis = (
        finite_basis.get("uniform_cap_finite_basis_closed") is True
        and finite_basis.get("narrowest_next_hardpoint")
        == "FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels"
    )
    finite_arc_named = (
        finite_arc.get("finite_arc_no_unnamed_exit_closed") is True
        and finite_arc.get("narrowest_next_hardpoint")
        == "TransverseFiberExpansionForFiniteArcCaps"
    )
    transverse_to_clean = (
        transverse_clean.get("transverse_expansion_reduced_to_clean_atom") is True
        and transverse_clean.get("narrowest_next_hardpoint")
        == "TransverseQuotientCleanLargeSieveAtom"
    )
    clean_frontier_named = (
        clean_frontier.get("transverse_clean_atom_routed_to_named_frontier") is True
        and clean_frontier.get("external_windowed_kls_version_closed_if_accepted") is True
    )
    canonical_pdec_closed = (
        canonical_layer.get("canonical_layer_transfer_closed") is True
        and canonical_layer.get("self_contained_canonical_branch_closed") is True
        and canonical_layer.get("open_self_contained_gates") == []
    )
    boundary_lifted = (
        pdec_boundary_lift.get("canonical_source_self_contained_pdec_bottleneck_closed")
        is True
        and pdec_boundary_lift.get("global_terminal_family_exclusion_closed") is False
    )
    generic_external_accounted = (
        noncanonical_trilemma.get("trilemma_boundary_closed") is True
        and noncanonical_trilemma.get("external_contract_package_closed_if_fulls_kls_ext_accepted")
        is True
    )
    final_promotion_accounted = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )

    return [
        row(
            gate="SAEIndependentTerminalRemoved",
            closed=sae_removed,
            evidence="SAE absorption router",
            meaning="第一包当前只需处理广义 PDEC 与未来显式 sparse schema。",
            remaining="PDEC boundary, future explicit sparse schema",
        ),
        row(
            gate="PersistentPDECAdmissionBoundary",
            closed=persistent_boundary,
            evidence="persistent terminal admission router",
            meaning="裸持久签名、裸 ColumnCRT、对偶失败和口径错配都不能直接准入。",
            remaining="primitive multi-atom same-formal-unit PDEC only",
        ),
        row(
            gate="NoCurrentMaterializedNonTautologicalCandidate",
            closed=no_current_nontautological,
            evidence="non-tautological PDEC admission audit",
            meaning="当前已物化前沿没有合法非二点 primitive PDEC 候选。",
            remaining="future candidate must pass admission schema",
        ),
        row(
            gate="PrimitiveRankBoundary",
            closed=primitive_boundary,
            evidence="primitive multi-atom rank router",
            meaning="零秩/一秩/二点/固定壳/ColumnCRT/cap 失败全部回流命名路线。",
            remaining="rank >= 2 cap-stable primitive kernel",
        ),
        row(
            gate="RankTwoKernelInverseBoundary",
            closed=ranktwo_inverse,
            evidence="rank-two cap-stable kernel router",
            meaning="二秩核不等式已逆否化为统一 cap-stability 证书。",
            remaining="uniform cap stability certificate",
        ),
        row(
            gate="UniformCapFiniteBasis",
            closed=finite_cap_basis,
            evidence="uniform cap finite basis router",
            meaning="连续方向帽搜索压成有限循环弧 cap 质量界。",
            remaining="finite cyclic-arc cap mass bounds",
        ),
        row(
            gate="FiniteArcNoUnnamedExit",
            closed=finite_arc_named,
            evidence="finite arc transverse router",
            meaning="高质量有限弧若失败，回流 SAE/refined PDEC/ColumnCRT/CleanKLS。",
            remaining="transverse fiber expansion or named return",
        ),
        row(
            gate="TransverseCleanReduction",
            closed=transverse_to_clean,
            evidence="transverse clean reduction router",
            meaning="横向非平坦缺陷全部命名；平坦残差只进入 clean 大筛原子。",
            remaining="CleanKLS/SC-9 frontier",
        ),
        row(
            gate="CleanFrontierNamed",
            closed=clean_frontier_named,
            evidence="transverse clean atom frontier router",
            meaning="clean 原子不是第四终端；自足入 canonical source，外部入 DI/BFI。",
            remaining="canonical source transfer or external FullS-KLS/DI-BFI",
        ),
        row(
            gate="CanonicalPDECCapClosed",
            closed=canonical_pdec_closed,
            evidence="canonical layer closure router",
            meaning="canonical-source 分支内的 PDEC-CAP 已经闭合到 A1 最终边界。",
            remaining="generic/external branch only",
        ),
        row(
            gate="PDECBoundaryLifted",
            closed=boundary_lifted,
            evidence="self-contained PDEC-CAP boundary lift router",
            meaning="旧 PDEC-CAP 自足瓶颈已提升；全局终端家族仍不是无条件闭合。",
            remaining="global family promotion / final inputs",
        ),
        row(
            gate="GenericExternalBranchAccounted",
            closed=generic_external_accounted,
            evidence="noncanonical complement trilemma",
            meaning="generic/external 分支已归入第二包三歧输入。",
            remaining="source identity, strengthened anti-atom, or FullS-KLS-ext",
        ),
        row(
            gate="FinalPromotionAccounted",
            closed=final_promotion_accounted,
            evidence="DStructure/Rankin promotion acceptance router",
            meaning="最终晋级门已命名但未独立接受。",
            remaining="DStructure/Rankin independent acceptance",
        ),
    ]


def run(
    sae_absorb_path: Path,
    persistent_path: Path,
    nontautological_path: Path,
    primitive_rank_path: Path,
    ranktwo_path: Path,
    finite_basis_path: Path,
    finite_arc_path: Path,
    transverse_clean_path: Path,
    clean_frontier_path: Path,
    canonical_layer_path: Path,
    pdec_boundary_lift_path: Path,
    noncanonical_trilemma_path: Path,
    dstructure_path: Path,
) -> dict[str, Any]:
    """运行广义 PDEC family 显式输入边界路由。"""
    sae_absorb = load_json(sae_absorb_path)
    persistent = load_json(persistent_path)
    nontautological = load_json(nontautological_path)
    primitive_rank = load_json(primitive_rank_path)
    ranktwo = load_json(ranktwo_path)
    finite_basis = load_json(finite_basis_path)
    finite_arc = load_json(finite_arc_path)
    transverse_clean = load_json(transverse_clean_path)
    clean_frontier = load_json(clean_frontier_path)
    canonical_layer = load_json(canonical_layer_path)
    pdec_boundary_lift = load_json(pdec_boundary_lift_path)
    noncanonical_trilemma = load_json(noncanonical_trilemma_path)
    dstructure = load_json(dstructure_path)
    rows = build_rows(
        sae_absorb=sae_absorb,
        persistent=persistent,
        nontautological=nontautological,
        primitive_rank=primitive_rank,
        ranktwo=ranktwo,
        finite_basis=finite_basis,
        finite_arc=finite_arc,
        transverse_clean=transverse_clean,
        clean_frontier=clean_frontier,
        canonical_layer=canonical_layer,
        pdec_boundary_lift=pdec_boundary_lift,
        noncanonical_trilemma=noncanonical_trilemma,
        dstructure=dstructure,
    )
    boundary_closed = all(item["closed"] for item in rows)
    evidence_paths = [
        sae_absorb_path,
        persistent_path,
        nontautological_path,
        primitive_rank_path,
        ranktwo_path,
        finite_basis_path,
        finite_arc_path,
        transverse_clean_path,
        clean_frontier_path,
        canonical_layer_path,
        pdec_boundary_lift_path,
        noncanonical_trilemma_path,
        dstructure_path,
    ]
    return {
        "certificate_type": "prime_matrix_pdec_family_explicit_input_boundary_router",
        "status": (
            "pdec_family_boundary_closed_current_frontier_zero_future_schema_required"
            if boundary_closed
            else "pdec_family_boundary_missing_gate"
        ),
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "pdec_family_explicit_input_boundary_closed": boundary_closed,
        "current_materialized_pdec_frontier_closed": bool(
            nontautological.get("current_materialized_nontautological_pdec_candidate_count") == 0
            and persistent.get("current_materialized_persistent_terminal_instances_closed") is True
        ),
        "canonical_source_pdec_cap_closed": bool(
            canonical_layer.get("canonical_layer_transfer_closed") is True
            and pdec_boundary_lift.get("canonical_source_self_contained_pdec_bottleneck_closed")
            is True
        ),
        "global_pdec_family_unconditional_closed": False,
        "row_column_unconditional_closed": False,
        "future_pdec_schema_required": [
            "同一个 formal unit，且只有一个固定 phase map",
            "全部去重后至少有三个物理 primitive 原子",
            "不是二点 Fourier tautology",
            "不是尚未吸收的 ColumnCRT/displacement",
            "商去 shell/column 退化后秩至少为 2",
            "对每个有限循环弧 localization 都 cap-stable",
            "横向支撑既非 sparse，也非持久偏斜，也未进入 clean 外部化",
        ],
        "remaining_after_pdec_boundary": [
            "若未来引入真正可准入的 PDEC family，必须提交 FutureExplicitPrimitivePDECSchema",
            "generic/external 分支进入 NoncanonicalFullSComplementTrilemma 输入",
            "最终定理晋级需要 DStructureRankinPromotion 独立接受",
        ],
        "rows": rows,
        "boundary_law": (
            "PDEC family 不再是模糊终端输入。当前已物化 PDEC 候选已经耗尽；canonical-source "
            "PDEC-CAP 路线已经由横向来源嵌入和 canonical 层转移闭合；每一种 cap 失败、低秩、"
            "重复、二点、ColumnCRT、sparse 或 clean 残差都有命名回流。因此未来若出现 PDEC "
            "障碍，必须作为显式 primitive 同 formal unit、二秩以上、cap-stable schema 引入。"
            "generic/external 分支已由 noncanonical 三歧包接管，最终定理晋级仍受 "
            "DStructure/Rankin 验收阻断。"
        ),
        "review_conclusion": (
            "广义 PDEC family 的当前边界已闭合：当前已物化合法非二点 primitive PDEC 候选为零，"
            "canonical-source PDEC-CAP 已接回最终自足边界；未来若出现真正 PDEC 障碍，必须以"
            "显式 primitive 同 formal unit、二秩以上、cap-stable schema 进入。完整行/列无条件"
            "命题仍未闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC Family 显式输入边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 边界律",
        "",
        result["boundary_law"],
        "",
        "```text",
        (
            "pdec_family_explicit_input_boundary_closed="
            f"{fmt_bool(result['pdec_family_explicit_input_boundary_closed'])}"
        ),
        (
            "current_materialized_pdec_frontier_closed="
            f"{fmt_bool(result['current_materialized_pdec_frontier_closed'])}"
        ),
        (
            "canonical_source_pdec_cap_closed="
            f"{fmt_bool(result['canonical_source_pdec_cap_closed'])}"
        ),
        (
            "global_pdec_family_unconditional_closed="
            f"{fmt_bool(result['global_pdec_family_unconditional_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 审查表",
        "",
        "| gate | closed | evidence | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(["", "## 3. 未来 PDEC schema 准入条件", ""])
    for item in result["future_pdec_schema_required"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 4. PDEC 边界后的剩余", ""])
    for item in result["remaining_after_pdec_boundary"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 5. 判定",
            "",
            "这一步不声称全局 PDEC family 已无条件排斥；它把 PDEC 从泛称终端改写为显式准入 schema。"
            "当前材料中已经物化的 PDEC 候选全部清零，canonical-source PDEC-CAP 也已经闭合。"
            "未来任何新 PDEC 必须先提交同 formal unit、三物理原子以上、非二点 tautology、二秩以上、"
            "cap-stable 且未被 sparse/ColumnCRT/CleanKLS 吸收的完整证书字段。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sae-absorb-json", type=Path, default=DEFAULT_SAE_ABSORB)
    parser.add_argument("--persistent-json", type=Path, default=DEFAULT_PERSISTENT)
    parser.add_argument("--nontautological-json", type=Path, default=DEFAULT_NONTAUTOLOGICAL)
    parser.add_argument("--primitive-rank-json", type=Path, default=DEFAULT_PRIMITIVE_RANK)
    parser.add_argument("--ranktwo-json", type=Path, default=DEFAULT_RANKTWO)
    parser.add_argument("--finite-basis-json", type=Path, default=DEFAULT_FINITE_BASIS)
    parser.add_argument("--finite-arc-json", type=Path, default=DEFAULT_FINITE_ARC)
    parser.add_argument("--transverse-clean-json", type=Path, default=DEFAULT_TRANSVERSE_CLEAN)
    parser.add_argument("--clean-frontier-json", type=Path, default=DEFAULT_CLEAN_FRONTIER)
    parser.add_argument("--canonical-layer-json", type=Path, default=DEFAULT_CANONICAL_LAYER)
    parser.add_argument("--pdec-boundary-lift-json", type=Path, default=DEFAULT_PDEC_BOUNDARY_LIFT)
    parser.add_argument("--noncanonical-trilemma-json", type=Path, default=DEFAULT_NONCANONICAL_TRILEMMA)
    parser.add_argument("--dstructure-json", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        sae_absorb_path=args.sae_absorb_json,
        persistent_path=args.persistent_json,
        nontautological_path=args.nontautological_json,
        primitive_rank_path=args.primitive_rank_json,
        ranktwo_path=args.ranktwo_json,
        finite_basis_path=args.finite_basis_json,
        finite_arc_path=args.finite_arc_json,
        transverse_clean_path=args.transverse_clean_json,
        clean_frontier_path=args.clean_frontier_json,
        canonical_layer_path=args.canonical_layer_json,
        pdec_boundary_lift_path=args.pdec_boundary_lift_json,
        noncanonical_trilemma_path=args.noncanonical_trilemma_json,
        dstructure_path=args.dstructure_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["remaining_after_pdec_boundary"])


if __name__ == "__main__":
    main()
