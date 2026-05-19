#!/usr/bin/env python3
"""生成 phase-residue exchange normalized root-mean dipole 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_normalized_root_mean_dipole_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.json

输出：
  data/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-normalized-root-mean-dipole"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-root-star-charge-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeRootStarChargeCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeNormalizedRootMeanDipoleCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeRootStarChargeImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeNormalizedRootMeanDipoleLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeNormalizedRootMeanDipoleLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeNormalizedRootMeanDipoleLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeNormalizedRootMeanDipoleLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeNormalizedRootMeanDipoleLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeNormalizedRootMeanDipoleLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeNormalizedRootMeanDipoleLedger"
ROOT_STAR_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeRootStarChargeImportedForNormalizedRootMeanDipoleLedger"
ROOT_MEAN_NORMALIZATION = "StableLadderEndpointOrbitPhaseResidueExchangeRootMeanNormalizationLedger"
NONROOT_MEAN = "StableLadderEndpointOrbitPhaseResidueExchangeNonrootMeanMeasureLedger"
DIPOLE_FIELD = "StableLadderEndpointOrbitPhaseResidueExchangeNormalizedRootMeanDipoleFieldLedger"
DIPOLE_ZERO_MEAN = "StableLadderEndpointOrbitPhaseResidueExchangeNormalizedRootMeanDipoleZeroMeanLedger"
ROOT_MEAN_DEVIATION = "StableLadderEndpointOrbitPhaseResidueExchangeRootToNonrootMeanDeviationCoordinateLedger"
NO_MULTIPLICITY_BLOWUP = "StableLadderEndpointOrbitPhaseResidueNoArtificialRootMultiplicityAfterNormalizationLedger"
DIPOLE_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeNormalizedRootMeanDipolePacketLedger"
NO_ANON = "NoAnonymousRootStarChargeAfterNormalizedRootMeanDipoleLedger"


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


def next_target(previous: dict[str, Any]) -> str:
    """把 root-star charge 硬点替换为 normalized root-mean dipole 硬点。"""
    target = previous.get("next_direct_attack_target", "")
    if target and OLD_TARGET in target:
        return target.replace(OLD_TARGET, NEW_TARGET)
    return NEW_TARGET


def reduced_target(new_target: str) -> str:
    """给出本轮归约后的活动基片段。"""
    ledgers = [
        IMPORT,
        MULTIPLICITY_CAP,
        SINGLETON,
        FULL_MEAN,
        BRIDGE,
        AMPLITUDE_DEPTH,
        BOUNDARY,
        ROOT_STAR_IMPORT,
        ROOT_MEAN_NORMALIZATION,
        NONROOT_MEAN,
        DIPOLE_FIELD,
        DIPOLE_ZERO_MEAN,
        ROOT_MEAN_DEVIATION,
        NO_MULTIPLICITY_BLOWUP,
        DIPOLE_PACKET,
        NO_ANON,
        SPARSE,
        new_target,
    ]
    return " AND ".join(ledgers)


def replace_latest_basis(previous: dict[str, Any], reduced: str) -> str:
    """更新长活动基。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    old = previous.get("next_direct_attack_target", "")
    if basis and old and old in basis:
        return basis.replace(old, reduced)
    return reduced


def dipole_records() -> list[dict[str, str]]:
    """给出 normalized root-mean dipole 的字段。"""
    return [
        {
            "field": "root_star_charge",
            "meaning": "导入根星电荷 C=(|S|-1)[s0]-sum_{s!=s0}[s]。",
        },
        {
            "field": "normalization_denominator",
            "meaning": "当 |S|>1 时用 |S|-1 归一化；|S|=1 退回 singleton 出口。",
        },
        {
            "field": "nonroot_mean",
            "meaning": "非根均值为 mu=(1/(|S|-1))sum_{s!=s0}[s]。",
        },
        {
            "field": "normalized_dipole",
            "meaning": "D=[s0]-mu，且 C=(|S|-1)D。",
        },
        {
            "field": "zero_mean",
            "meaning": "D 的系数总和为 1-(|S|-1)/(|S|-1)=0。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 normalized root-mean dipole 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeRootStarChargeImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange root-star charge circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeNormalizedRootMeanDipole",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeNormalizedRootMeanDipole",
            True,
            False,
            "|S|=1 或根星退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeNormalizedRootMeanDipole",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeNormalizedRootMeanDipole",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeNormalizedRootMeanDipole",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeNormalizedRootMeanDipole",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeRootStarChargeImportedForNormalizedRootMeanDipole",
            True,
            True,
            "导入上一层根星电荷 C=(|S|-1)[s0]-sum_{s!=s0}[s]。",
            ROOT_STAR_IMPORT,
        ),
        row(
            "PhaseResidueExchangeRootMeanNormalization",
            True,
            True,
            "对非退化根星按 |S|-1 归一化；退化情形由 singleton 出口承接。",
            ROOT_MEAN_NORMALIZATION,
        ),
        row(
            "PhaseResidueExchangeNonrootMeanMeasure",
            True,
            True,
            "非根负端点被压成均匀均值 mu=(1/(|S|-1))sum_{s!=s0}[s]。",
            NONROOT_MEAN,
        ),
        row(
            "PhaseResidueExchangeNormalizedRootMeanDipoleField",
            True,
            True,
            "根星场等价于 C=(|S|-1)([s0]-mu)。",
            DIPOLE_FIELD,
        ),
        row(
            "PhaseResidueExchangeNormalizedRootMeanDipoleZeroMean",
            True,
            True,
            "归一化偶极 D=[s0]-mu 的总系数为零。",
            DIPOLE_ZERO_MEAN,
        ),
        row(
            "PhaseResidueExchangeRootToNonrootMeanDeviationCoordinate",
            True,
            True,
            "剩余压力只依赖根点相对非根均值的偏差坐标。",
            ROOT_MEAN_DEVIATION,
        ),
        row(
            "PhaseResidueNoArtificialRootMultiplicityAfterNormalization",
            True,
            True,
            "归一化去除 |S|-1 根点重数放大，不再把容量异常藏在倍数系数中。",
            NO_MULTIPLICITY_BLOWUP,
        ),
        row(
            "PhaseResidueExchangeNormalizedRootMeanDipolePacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange normalized root-mean dipole circuit PDEC/cap。",
            DIPOLE_PACKET,
        ),
        row(
            "NoAnonymousRootStarChargeAfterNormalizedRootMeanDipole",
            True,
            True,
            "root-star charge 不再匿名保留；它被压成根点相对非根均值的零均值偶极。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeNormalizedRootMeanDipole",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeNormalizedRootMeanDipoleStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、normalized root-mean dipole、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange normalized root-mean dipole circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 normalized root-mean dipole 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange root-star charge 已把剩余端点压力固定为"
        " C=(|S|-1)[s0]-sum_{s!=s0}[s]。"
        "本步对非退化根星除以 |S|-1，得到"
        " D=[s0]-(1/(|S|-1))sum_{s!=s0}[s]，即根点相对非根均值的零均值偶极。"
        "剩余反例不再能藏在根点重数放大中，而必须表现为 normalized root-mean dipole circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_normalized_root_mean_dipole_router",
        "status": "phase_residue_exchange_root_star_charge_reduced_to_normalized_root_mean_dipole_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "normalized_root_mean_dipole_records": dipole_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_root_star_charge_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_root_star_charge_imported_for_normalized_root_mean_dipole": True,
        "phase_residue_exchange_root_mean_normalization_closed": True,
        "phase_residue_exchange_nonroot_mean_measure_closed": True,
        "phase_residue_exchange_normalized_root_mean_dipole_field_closed": True,
        "phase_residue_exchange_normalized_root_mean_dipole_zero_mean_closed": True,
        "phase_residue_exchange_root_to_nonroot_mean_deviation_coordinate_closed": True,
        "phase_residue_no_artificial_root_multiplicity_after_normalization_closed": True,
        "phase_residue_exchange_normalized_root_mean_dipole_packet_registered": True,
        "anonymous_root_star_charge_removed_after_normalized_root_mean_dipole": True,
        "source_atom_multiplicity_cap_carried_forward": True,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_bridge_cancellation_carried_forward": True,
        "endpoint_orbit_amplitude_depth_carried_forward": True,
        "endpoint_orbit_variation_boundary_flux_carried_forward": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "source_atom_multiplicity_cap_pdec_cap_proved": False,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_bridge_cancellation_pdec_cap_proved": False,
        "endpoint_orbit_amplitude_depth_pdec_cap_proved": False,
        "endpoint_orbit_variation_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "phase_residue_exchange_normalized_root_mean_dipole_circuit_pdec_cap_proved": False,
        "row_column_unconditional_closed": False,
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "source_hashes": source_hashes(),
    }
    return cert


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix phase-residue exchange normalized root-mean dipole 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_root_star_charge_imported={fmt_bool(cert['phase_residue_exchange_root_star_charge_imported'])}",
        f"phase_residue_exchange_root_mean_normalization_closed={fmt_bool(cert['phase_residue_exchange_root_mean_normalization_closed'])}",
        f"phase_residue_exchange_nonroot_mean_measure_closed={fmt_bool(cert['phase_residue_exchange_nonroot_mean_measure_closed'])}",
        f"phase_residue_exchange_normalized_root_mean_dipole_zero_mean_closed={fmt_bool(cert['phase_residue_exchange_normalized_root_mean_dipole_zero_mean_closed'])}",
        f"phase_residue_exchange_normalized_root_mean_dipole_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_normalized_root_mean_dipole_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 根星电荷输入",
        "",
        "上一层给出根星电荷：",
        "",
        "```text",
        "C = (|S|-1)[s0] - sum_{s != s0}[s]",
        "```",
        "",
        "其中 `s0` 是共同根点，每个非根源点只出现一次负端点电荷。",
        "",
        "## 2. 非根均值归一化",
        "",
        "当 `|S|>1` 时定义非根均值：",
        "",
        "```text",
        "mu = (1/(|S|-1)) sum_{s != s0}[s]",
        "```",
        "",
        "于是根星电荷可写成：",
        "",
        "```text",
        "C = (|S|-1)([s0] - mu)",
        "```",
        "",
        "`|S|=1` 时没有非根均值，归入 singleton atom/SAE 出口。",
        "",
        "## 3. 零均值偶极场",
        "",
        "定义归一化偶极：",
        "",
        "```text",
        "D = [s0] - (1/(|S|-1)) sum_{s != s0}[s]",
        "```",
        "",
        "它的总系数为：",
        "",
        "```text",
        "1 - (|S|-1)/(|S|-1) = 0",
        "```",
        "",
        "所以剩余压力被压成根点相对非根均值的零均值偏差，而不是根点重数放大。",
        "",
        "## 4. normalized root-mean dipole 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["normalized_root_mean_dipole_records"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "## 5. 新硬点",
            "",
            "```text",
            f"{cert['source_exit']}",
            "  -> " + cert["reduced_target"].replace(" AND ", "\n  AND "),
            "```",
            "",
            "## 6. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
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
            "## 7. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 8. 诚实边界",
            "",
            "- 本证书没有证明 source-atom multiplicity-cap PDEC/cap。",
            "- 本证书没有证明 phase-residue exchange normalized root-mean dipole circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """生成 JSON、ledger 和 Markdown 三件套。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("phase_residue_exchange_normalized_root_mean_dipole_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
