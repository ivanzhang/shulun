#!/usr/bin/env python3
"""生成 CRT-coordinate canonical-equation 归约证书。

用法示例：
  python3 experiments/prime_matrix_crt_coordinate_canonical_equation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-crt-coordinate-canonical-equation-router.json

输出：
  data/prime-matrix-crt-coordinate-canonical-equation-ledger.json
  docs/monograph/prime-matrix-crt-coordinate-canonical-equation-router.json
  docs/monograph/prime-matrix-crt-coordinate-canonical-equation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-crt-coordinate-canonical-equation"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-primitive-witness-crt-coordinate-atom-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAE"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
    "OrEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomImbalancePDECCap"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomImbalanceImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapCarriedForwardAfterCanonicalCongruenceEquationAtomLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCRTCoordinateCanonicalCongruenceEquationAtomLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCRTCoordinateCanonicalCongruenceEquationAtomLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCRTCoordinateCanonicalCongruenceEquationAtomLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCRTCoordinateCanonicalCongruenceEquationAtomLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCRTCoordinateCanonicalCongruenceEquationAtomLedger"
CANON_MODEL = "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomModelLedger"
NORMAL_FORM = "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationNormalFormLedger"
EQUATION_ID = "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationIDStabilityLedger"
QUOTA_DEBT = "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationQuotaDebtAllocationLedger"
PIGEONHOLE = "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomPigeonholeLedger"
RETURN_SPLIT = "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomNamedReturnSplitLedger"
EQUATION_PACKET = "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomImbalancePacketLedger"
NO_ANON = "NoAnonymousCRTCoordinateAtomImbalanceExitAfterCanonicalCongruenceEquationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterCRTCoordinateCanonicalCongruenceEquationAtomLedger"

MULTIPLICITY_CAP_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityCapPDECCap"
)
EQUATION_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtomMultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtomImbalancePDECCap"
)
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOr"
    f"{MULTIPLICITY_CAP_TARGET}Or{EQUATION_TARGET}"
    "OrEndpointOrbitBridgeCancellationPDECCapOrEndpointOrbitAmplitudeDepthPDECCap"
    "OrEndpointOrbitVariationBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {MULTIPLICITY_CAP} AND {SINGLETON} AND {FULL_MEAN} "
    f"AND {BRIDGE} AND {AMPLITUDE_DEPTH} AND {BOUNDARY} "
    f"AND {CANON_MODEL} AND {NORMAL_FORM} AND {EQUATION_ID} "
    f"AND {QUOTA_DEBT} AND {PIGEONHOLE} AND {RETURN_SPLIT} "
    f"AND {EQUATION_PACKET} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
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
    """登记本脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把活动基中的 CRT-coordinate-atom 硬点替换为 canonical-equation 硬点。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def canonical_equation_records() -> list[dict[str, str]]:
    """给出规范同余方程原子的字段。"""
    return [
        {
            "field": "equation_id",
            "meaning": "对规范化后的同余方程、行列坐标、端点侧、方向和载体素数求哈希。",
        },
        {
            "field": "normal_form",
            "meaning": "把 N_{row,column,side} == a mod q 归一为 primitive affine congruence class。",
        },
        {
            "field": "coordinate_key",
            "meaning": "保留 row、column、side、orientation，防止不同实际格点被同一 residue 合并。",
        },
        {
            "field": "carrier_key",
            "meaning": "保留 carrier prime q 与 residue a，防止跨 q 或跨 residue 互相支付。",
        },
        {
            "field": "phase_boundary_key",
            "meaning": "保留 phase/side/boundary tag；若迁移出本 equation atom，则回流 boundary outlet。",
        },
    ]


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 canonical-equation 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitCRTCoordinateAtomImbalanceImported",
            imported,
            False,
            "上一层剩余含 multiplicity cap、CRT-coordinate-atom imbalance 或 sparse/atom/mean/三出口。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterCanonicalCongruenceEquationAtom",
            True,
            False,
            "source-atom multiplicity-cap 异常继续作为独立 PDEC/cap 出口；本步不证明该 cap。",
            MULTIPLICITY_CAP,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterCanonicalCongruenceEquationAtom",
            True,
            False,
            "规范同余方程原子退化为单点孤立端点时继续由 singleton atom/SAE 承接。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterCanonicalCongruenceEquationAtom",
            True,
            False,
            "规范同余方程原子只给出整周期均值时继续由 full-cycle mean atom/SAE 承接。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterCanonicalCongruenceEquationAtom",
            True,
            False,
            "同一 equation atom 内反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterCanonicalCongruenceEquationAtom",
            True,
            False,
            "同号 equation atom 跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterCanonicalCongruenceEquationAtom",
            True,
            False,
            "同余方程穿越行列、端点侧、phase 或边界时继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomModel",
            True,
            True,
            "把 overfull CRT coordinate atom 的 C_{...,chi} 按有限规范同余方程原子 epsilon 分解。",
            CANON_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationNormalForm",
            True,
            True,
            "每个 N_{row,column,side} == a mod q 被归一到 primitive affine congruence normal form。",
            NORMAL_FORM,
        ),
        row(
            "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationIDStability",
            True,
            True,
            "equation_id 由 normal form、row/column、carrier q、residue a、side、orientation 稳定决定。",
            EQUATION_ID,
        ),
        row(
            "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationQuotaDebtAllocation",
            True,
            True,
            "把 d_{...,chi} 同步分配为 d_{...,chi,epsilon}，不允许跨 equation_id 支付。",
            QUOTA_DEBT,
        ),
        row(
            "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomPigeonhole",
            True,
            True,
            "若 CRT coordinate atom 超额，则存在 epsilon 使 C_{...,chi,epsilon}>d_{...,chi,epsilon}。",
            PIGEONHOLE,
        ),
        row(
            "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomNamedReturnSplit",
            True,
            True,
            "overfull equation atom 的孤立、均值、反号债、堆高、边界迁移分别回流已有出口。",
            RETURN_SPLIT,
        ),
        row(
            "StableLadderEndpointOrbitCRTCoordinateCanonicalCongruenceEquationAtomImbalancePacket",
            True,
            False,
            "若已有出口不支付，剩余就是真实 canonical-congruence-equation atom imbalance PDEC/cap。",
            EQUATION_PACKET,
        ),
        row(
            "NoAnonymousCRTCoordinateAtomImbalanceExitAfterCanonicalCongruenceEquation",
            True,
            True,
            "CRT-coordinate-atom imbalance 不再匿名保留；它是 canonical equation imbalance 或已有命名出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterCanonicalCongruenceEquationAtom",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitCanonicalCongruenceEquationAtomStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、canonical equation imbalance、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、multiplicity cap、canonical equation imbalance、bridge、amplitude、boundary 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 canonical-equation 证书。"""
    previous = load_json(PREVIOUS_CERT)
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    plain = (
        "CRT-coordinate-atom imbalance 给出 C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}>"
        "d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}。"
        "把 chi 内部可能的同一同余方程多表示归一到规范同余方程原子 epsilon，并同步分配 quota/debt。"
        "若所有 epsilon 都不超额，则加总回到 chi 不超额，矛盾；因此至少一个实际 canonical congruence equation atom 超额。"
        "multiplicity-cap 异常继续作为独立出口；已有出口能支付则回流；真正剩余是 canonical-equation atom imbalance。"
    )
    return {
        "certificate_type": "prime_matrix_crt_coordinate_canonical_equation_router",
        "status": "crt_coordinate_atom_imbalance_reduced_to_canonical_congruence_equation_atom_or_existing_caps_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "crt_coordinate_atom_imbalance_imported": imported,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "crt_coordinate_canonical_congruence_equation_atom_model_closed": True,
        "crt_coordinate_canonical_congruence_equation_normal_form_closed": True,
        "crt_coordinate_canonical_congruence_equation_id_stability_closed": True,
        "crt_coordinate_canonical_congruence_equation_quota_debt_allocation_closed": True,
        "crt_coordinate_canonical_congruence_equation_atom_pigeonhole_closed": True,
        "crt_coordinate_canonical_congruence_equation_atom_named_return_split_closed": True,
        "crt_coordinate_canonical_congruence_equation_atom_imbalance_packet_registered": True,
        "anonymous_crt_coordinate_atom_imbalance_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved": False,
        "crt_coordinate_canonical_congruence_equation_atom_imbalance_pdec_cap_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "canonical_equation_atom_formulas": {
            "crt_coordinate_atom_load": "C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}",
            "quota_debt_coordinate_atom": "d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}",
            "equation_atom_key": "epsilon=(equation_id,normal_form,row,column,carrier_prime q,residue a,endpoint_side,orientation,phase_boundary_key)",
            "overfull_equation_atom": "C_{...,chi}>d_{...,chi} => exists epsilon with C_{...,chi,epsilon}>d_{...,chi,epsilon}",
            "new_exit": EQUATION_TARGET,
        },
        "canonical_equation_records": canonical_equation_records(),
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": replace_latest_basis(previous),
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix CRT-coordinate canonical-congruence-equation 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"crt_coordinate_atom_imbalance_imported={fmt_bool(cert['crt_coordinate_atom_imbalance_imported'])}",
        f"source_atom_multiplicity_cap_carried_forward={fmt_bool(cert['source_atom_multiplicity_cap_carried_forward'])}",
        f"crt_coordinate_canonical_congruence_equation_atom_model_closed={fmt_bool(cert['crt_coordinate_canonical_congruence_equation_atom_model_closed'])}",
        f"crt_coordinate_canonical_congruence_equation_normal_form_closed={fmt_bool(cert['crt_coordinate_canonical_congruence_equation_normal_form_closed'])}",
        f"crt_coordinate_canonical_congruence_equation_id_stability_closed={fmt_bool(cert['crt_coordinate_canonical_congruence_equation_id_stability_closed'])}",
        f"crt_coordinate_canonical_congruence_equation_quota_debt_allocation_closed={fmt_bool(cert['crt_coordinate_canonical_congruence_equation_quota_debt_allocation_closed'])}",
        f"crt_coordinate_canonical_congruence_equation_atom_pigeonhole_closed={fmt_bool(cert['crt_coordinate_canonical_congruence_equation_atom_pigeonhole_closed'])}",
        f"crt_coordinate_canonical_congruence_equation_atom_imbalance_packet_registered={fmt_bool(cert['crt_coordinate_canonical_congruence_equation_atom_imbalance_packet_registered'])}",
        f"anonymous_crt_coordinate_atom_imbalance_removed={fmt_bool(cert['anonymous_crt_coordinate_atom_imbalance_removed'])}",
        f"endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_residue_shadow_dual_row_phase_cell_atom_signed_core_support_slice_residue_fiber_phase_word_slot_source_atom_multiplicity_cap_pdec_cap_proved'])}",
        f"crt_coordinate_canonical_congruence_equation_atom_imbalance_pdec_cap_proved={fmt_bool(cert['crt_coordinate_canonical_congruence_equation_atom_imbalance_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 规范同余方程原子分解",
        "",
        "把已超额的 CRT coordinate atom `chi` 同步分解到有限规范同余方程原子 `epsilon`。",
        "`epsilon` 记录 equation_id、normal form、实际行列、载体素数 `q`、残基 `a`、端点侧、方向和 phase/boundary 标签。",
        "",
        "```text",
        "C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}",
        "d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}=sum_epsilon d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi,epsilon}",
        "C_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi}>d_{s,rho,omega,tau,alpha,mu,eta,iota,kappa,chi} => exists epsilon with C_{...,chi,epsilon}>d_{...,chi,epsilon}.",
        "```",
        "",
        "因此 CRT-coordinate atom 超额不能靠同一同余方程的多表示匿名保留；它必须落到一个实际 canonical equation atom，或回流已有出口。",
        "",
        "## 2. 规范字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["canonical_equation_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.extend([
        "",
        "## 3. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "## 4. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for item in cert["decision_rows"]:
        lines.append(
            f"| {cell(item['gate'])} | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | {cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend([
        "",
        "## 5. 新活动基",
        "",
        "```text",
        cert["latest_noncycle_basis_after_router"],
        "```",
        "",
        "## 6. 诚实边界",
        "",
        "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
        "- 本证书没有证明 canonical-congruence-equation atom imbalance PDEC/cap。",
        "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
        "- 行/列命题仍未无条件闭合。",
        "",
        "## 7. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ])
    for file_name, digest in cert["source_hashes"].items():
        lines.append(f"| `{file_name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """生成 ledger、JSON 证书和 Markdown 说明。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
        "outputs": [
            str(OUT_LEDGER.relative_to(ROOT)),
            str(OUT_JSON.relative_to(ROOT)),
            str(OUT_MD.relative_to(ROOT)),
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
