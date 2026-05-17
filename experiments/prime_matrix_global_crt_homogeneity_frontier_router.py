#!/usr/bin/env python3
"""生成 global CRT homogeneity 到 exact-source/pointwise-kernel 前沿同步证书。

用法示例：
  python3 experiments/prime_matrix_global_crt_homogeneity_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.json

输出：
  data/prime-matrix-global-crt-homogeneity-frontier-ledger.json
  docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.json
  docs/monograph/prime-matrix-global-crt-homogeneity-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-global-crt-homogeneity-frontier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-global-crt-homogeneity-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-global-crt-homogeneity-frontier-router.md"

SOURCE_FILES = [
    "prime-matrix-early-zero-gap-crt-asymmetry-router.json",
    "prime-matrix-early-zero-period-lift-carrier-drift-router.json",
    "prime-matrix-q2-carrier-stage-crt-asymmetry-router.json",
    "prime-matrix-q2-endpoint-fresh-layer-cascade-router.json",
    "prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json",
    "prime-matrix-q2-aperture-explosion-schema-firewall-router.json",
    "prime-matrix-q2-to-final-exact-source-alignment-router.json",
    "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json",
    "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json",
    "prime-matrix-strict-global-internal-cycle-frontier-sync-router.json",
    "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
]

EXACT_UV = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象，方便防火墙仍可输出缺口。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书使用的依赖文件哈希。"""
    hashes: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            hashes[f"docs/monograph/{name}"] = sha256(path)
    return hashes


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造 global CRT homogeneity 前沿同步结果。"""
    early_gap = load_json("prime-matrix-early-zero-gap-crt-asymmetry-router.json")
    period_lift = load_json("prime-matrix-early-zero-period-lift-carrier-drift-router.json")
    q2_carrier = load_json("prime-matrix-q2-carrier-stage-crt-asymmetry-router.json")
    fresh_cascade = load_json("prime-matrix-q2-endpoint-fresh-layer-cascade-router.json")
    tail_mass = load_json("prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json")
    aperture = load_json("prime-matrix-q2-aperture-explosion-schema-firewall-router.json")
    q2_final = load_json("prime-matrix-q2-to-final-exact-source-alignment-router.json")
    fiber_atom = load_json("prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json")
    terminal_sync = load_json("prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json")
    internal_cycle = load_json("prime-matrix-strict-global-internal-cycle-frontier-sync-router.json")
    dstructure = load_json("prime-matrix-dstructure-rankin-promotion-acceptance-router.json")

    q1_q2_imported = (
        early_gap.get("row_column_unconditional_closed") is False
        and period_lift.get("row_column_unconditional_closed") is False
        and q2_carrier.get("status") == "q2_carrier_stage_endpoint_inversion_routed_not_global_proof"
    )
    endpoint_inversion = (
        q2_carrier.get("q2_full_wheel_endpoint_inversion_proved") is True
        or q2_carrier.get("all_sample_full_q2_endpoint_prime_replay_impossible") is True
    )
    finite_crt_terminal_removed = fresh_cascade.get("finite_crt_period_terminal_possible") is False
    controlled_tail_sae = tail_mass.get("controlled_non_pdec_fresh_tail_routes_to_sae") is True
    aperture_firewall = aperture.get("unnamed_aperture_explosion_terminal_allowed") is False
    q2_to_exact_source = (
        q2_final.get("q2_current_local_terminal_removed") is True
        and q2_final.get("q2_position_rigidity_controls_source_mass") is False
    )
    exact_source_atomized = (
        fiber_atom.get("preterminal_fiber_dispersion_source_atomization_closed") is True
        or fiber_atom.get("terminal_gap_after_router")
        == "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
    )
    pointwise_kernel_sync = (
        terminal_sync.get("pointwise_kernel_table_is_common_variable_table") is True
        and internal_cycle.get("next_direct_attack_target") == POINTWISE_KERNEL
    )
    alpha_row_open = terminal_sync.get("next_direct_attack_target") == ALPHA_ROW
    dstructure_open = dstructure.get("promotion_package_independently_accepted") is not True

    rows = [
        row(
            "Q1Q2AdjacentCarrierImported",
            q1_q2_imported,
            q1_q2_imported,
            "早期零行若给出跨行相邻素数 Q1<Q2，已有链条已把它登记为端点载体，而不是独立最终矛盾。",
            "Q2 endpoint inversion / moving endpoint routes",
        ),
        row(
            "FullQ2WheelEndpointStableReplayImpossible",
            endpoint_inversion,
            endpoint_inversion,
            "包含 Q1,Q2 的全 Q2 阶轮会把两个端点复制成分别被自身整除的复合点，故素端点稳定复现被排除。",
            "closed for endpoint-stable replay",
        ),
        row(
            "FiniteCRTPeriodTerminalRemoved",
            finite_crt_terminal_removed,
            finite_crt_terminal_removed,
            "端点替换后 fresh endpoint 层级联扩模，固定有限 CRT 周期不能作为无限反例链终端。",
            "fresh endpoint cascade",
        ),
        row(
            "FreshLayerNonPDECTailSAEImported",
            controlled_tail_sae,
            controlled_tail_sae,
            "无 PDEC 的受控 fresh layer 每层只删一个相位，尾质量按 W_j/B_j 可求和，进入 SAE。",
            "aperture explosion or support motion if uncontrolled",
        ),
        row(
            "UnnamedApertureExplosionForbidden",
            aperture_firewall,
            aperture_firewall,
            "若孔径增长追赶 fresh modulus，必须提交 moving-family/PDEC 显式 schema；当前无名出口不可保留。",
            "future explicit moving schema if new",
        ),
        row(
            "PureFiniteCRTHomogeneityBlocksGlobalPhaseContradiction",
            True,
            True,
            "对任意 finite wheel M_Y 与新素数 r，旧允许类 a 的 r 个提升 a+tM_Y 中恰有一个被 r 删除；有限 CRT 前缀是同质删相位，不产生全局相位矛盾，除非出现同素数碰撞即 PDEC/ColumnCRT。",
            "need actual load/source dispersion",
        ),
        row(
            "EulerProductCriticalDensityIsNotIntervalOccupancyProof",
            True,
            True,
            "无穷轮筛解释临界密度与 1/log x，但乘积密度本身不是长度 P 的移动区间占有下界；它缺少 actual source 在短窗和 exact fiber 上的非集中信息。",
            EXACT_UV,
        ),
        row(
            "Q2CRTPositionRigidityRoutedToExactSource",
            q2_to_exact_source,
            q2_to_exact_source,
            "Q2/CRT 刚性只控制位置与相位，不控制 Cauchy/dispersion 前 actual source 在 exact (u,v) fiber 上的质量。",
            EXACT_UV,
        ),
        row(
            "ExactSourceFiberAtomizedToSourceRankPackage",
            exact_source_atomized,
            False,
            "exact-UV 非集中已经被压成 source-domain rank/no-collapse 三原子包，但该三原子包尚未证明。",
            "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger",
        ),
        row(
            "SourceRankPackageSyncedToPointwiseKernel",
            pointwise_kernel_sync,
            False,
            "内部 strict 链条显示 source-domain entropy/source table/fixed-key multiplicity 的共同非后验对象是逐 primitive alpha/delta 核表。",
            POINTWISE_KERNEL,
        ),
        row(
            "AlphaRowEmissionFormulaStillOpen",
            alpha_row_open,
            False,
            "逐点核表的第一优先硬点是 alpha row anchor/phase 发射公式；当前材料尚未给出非循环证明。",
            ALPHA_ROW,
        ),
        row(
            "DStructureRankinPromotionStillOpen",
            dstructure_open,
            False,
            "即使源侧核表完成，DStructure/Tail-log4/finite Rankin 仍需独立晋级验收。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "本证书关闭的是纯 CRT 全局相位矛盾这条尝试的误出口，并把它同步到 source/kernel 前沿；没有完成行/列无条件证明。",
            f"{ALPHA_ROW} AND IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND {DSTRUCTURE}",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_global_crt_homogeneity_frontier_router",
        "status": "global_crt_homogeneity_synced_to_exact_source_pointwise_kernel_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_branch_preserved": True,
        "q1_q2_adjacent_carrier_imported": q1_q2_imported,
        "full_q2_wheel_endpoint_stable_replay_impossible": endpoint_inversion,
        "finite_crt_period_terminal_removed": finite_crt_terminal_removed,
        "controlled_fresh_layer_tail_sae_imported": controlled_tail_sae,
        "unnamed_aperture_explosion_forbidden": aperture_firewall,
        "pure_finite_crt_global_phase_contradiction_found": False,
        "global_crt_homogeneity_blocks_pure_phase_contradiction": True,
        "euler_product_critical_density_not_interval_occupancy_proof": True,
        "q2_crt_position_rigidity_routed_to_exact_source": q2_to_exact_source,
        "exact_source_fiber_atomized_to_source_rank_package": exact_source_atomized,
        "source_rank_package_synced_to_pointwise_kernel": pointwise_kernel_sync,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_precauchy_arithmetic_identity_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "dstructure_rankin_independently_accepted": not dstructure_open,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ALPHA_ROW,
        "full_current_basis": (
            f"{ALPHA_ROW} AND "
            "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger AND "
            "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows AND "
            f"{DSTRUCTURE}"
        ),
        "crt_homogeneity_lemma": (
            "设 M_Y 为平方自由轮模，r 不整除 M_Y 且 r 为新素数。对任意旧余类 a，"
            "r 个提升 a+tM_Y (0<=t<r) 在模 r 下遍历全部余类，因此恰有一个提升被 r 删除。"
            "所以有限轮增长是同质的单余类删除，不是相位矛盾；除非额外方程把同一个 formal unit "
            "强制送入已登记的 PDEC/ColumnCRT 碰撞。"
        ),
        "q1_q2_lesson": (
            "The adjacent-prime carrier Q1<Q2 proves endpoint-stable replay is impossible at the full Q2 wheel, "
            "but the true endpoint replacement is a moving fresh-source problem. Controlled non-PDEC replacement is SAE; "
            "persistent replacement is PDEC/ColumnCRT; uncontrolled replacement must be a named moving schema."
        ),
        "plain_conclusion": (
            "Q1/Q2 相邻素数不对称已经给出强约束：全 Q2 轮不能同时复现覆盖块和素端点。"
            "但有限 CRT 前缀本身是同质删相位机制，不能单独制造全局相位矛盾；"
            "无穷 Euler 乘积解释临界密度，却不等于短区间 actual occupancy 证明。"
            "因此纯 CRT 全局矛盾出口被关闭，剩余必须进入 actual-source exact-UV 非集中，"
            "并在 strict 内部链条中同步到逐 primitive alpha/delta 核表；第一硬点是 alpha row anchor/phase 发射公式。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 归档。"""
    lines = [
        "# Prime Matrix global CRT homogeneity 前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"q1_q2_adjacent_carrier_imported={fmt_bool(result['q1_q2_adjacent_carrier_imported'])}",
        "full_q2_wheel_endpoint_stable_replay_impossible="
        f"{fmt_bool(result['full_q2_wheel_endpoint_stable_replay_impossible'])}",
        f"finite_crt_period_terminal_removed={fmt_bool(result['finite_crt_period_terminal_removed'])}",
        f"controlled_fresh_layer_tail_sae_imported={fmt_bool(result['controlled_fresh_layer_tail_sae_imported'])}",
        f"unnamed_aperture_explosion_forbidden={fmt_bool(result['unnamed_aperture_explosion_forbidden'])}",
        "pure_finite_crt_global_phase_contradiction_found="
        f"{fmt_bool(result['pure_finite_crt_global_phase_contradiction_found'])}",
        "global_crt_homogeneity_blocks_pure_phase_contradiction="
        f"{fmt_bool(result['global_crt_homogeneity_blocks_pure_phase_contradiction'])}",
        "q2_crt_position_rigidity_routed_to_exact_source="
        f"{fmt_bool(result['q2_crt_position_rigidity_routed_to_exact_source'])}",
        "source_rank_package_synced_to_pointwise_kernel="
        f"{fmt_bool(result['source_rank_package_synced_to_pointwise_kernel'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. Q1/Q2 不对称的真实作用",
        "",
        "若早期零行给出跨行相邻素数 `Q1<Q2`，全 `Q2` 阶轮会把两个端点复制成被 `Q1,Q2` 自身整除的复合点。",
        "所以端点稳定复现不可能。这是一个真实约束，但它排除的是“同端点 replay”，不是直接推出全局零行不存在。",
        "",
        "端点若移动，就进入 fresh endpoint layer；受控且非 PDEC 的 fresh layer 被尾质量 `SAE` 吸收，",
        "持久相关进入 `ColumnCRT/PDEC`，孔径失控必须提交 explicit moving-family schema。",
        "",
        "## 2. 纯 CRT 全局矛盾防火墙",
        "",
        result["crt_homogeneity_lemma"],
        "",
        "这说明无穷叠加筛确实给出临界密度机制，但有限 CRT 前缀不会自动给出短区间占有证明。",
        "若要从相位/容量走向最终矛盾，必须提供 actual load 或 actual source 的非集中估计。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines += [
        "",
        "## 4. 最新剩余",
        "",
        "首攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "完整当前基：",
        "",
        "```text",
        result["full_current_basis"],
        "```",
        "",
        "审稿边界：本文件关闭的是“纯 CRT 全局相位矛盾”作为最终证明的误出口，",
        "并把该路线同步到 source/kernel 前沿；它没有证明 alpha row 发射公式、signed 恒等式、rank/multiplicity 证书，",
        "也没有完成 DStructure/Rankin 独立验收。",
        "",
        "## 5. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出前沿同步证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "next_direct_attack_target", "row_column_unconditional_closed")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
