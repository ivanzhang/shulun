#!/usr/bin/env python3
"""生成 phase-residue exchange root-source pair-average contrast 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_root_source_pair_average_contrast_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.json

输出：
  data/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-root-source-pair-average-contrast"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-normalized-root-mean-dipole-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeNormalizedRootMeanDipoleCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeRootSourcePairAverageContrastCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeNormalizedRootMeanDipoleImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeRootSourcePairAverageContrastLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeRootSourcePairAverageContrastLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRootSourcePairAverageContrastLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRootSourcePairAverageContrastLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRootSourcePairAverageContrastLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRootSourcePairAverageContrastLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeRootSourcePairAverageContrastLedger"
DIPOLE_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeNormalizedRootMeanDipoleImportedForPairAverageLedger"
PAIR_FAN = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairFanLedger"
PAIR_CONTRAST_FAMILY = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairContrastFamilyLedger"
UNIFORM_WEIGHT = "StableLadderEndpointOrbitPhaseResidueExchangeUniformPairWeightLedger"
PAIR_AVERAGE_IDENTITY = "StableLadderEndpointOrbitPhaseResidueExchangePairAverageContrastIdentityLedger"
UNIT_BALANCE = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairUnitBalanceLedger"
NO_NONROOT_MEAN_ANON = "StableLadderEndpointOrbitPhaseResidueNoAnonymousNonrootMeanAfterPairAverageLedger"
PAIR_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairAverageContrastPacketLedger"
NO_ANON = "NoAnonymousNormalizedRootMeanDipoleAfterPairAverageLedger"


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
    """把 normalized root-mean dipole 硬点替换为 pair-average contrast 硬点。"""
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
        DIPOLE_IMPORT,
        PAIR_FAN,
        PAIR_CONTRAST_FAMILY,
        UNIFORM_WEIGHT,
        PAIR_AVERAGE_IDENTITY,
        UNIT_BALANCE,
        NO_NONROOT_MEAN_ANON,
        PAIR_PACKET,
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


def pair_average_records() -> list[dict[str, str]]:
    """给出 root-source pair-average contrast 的字段。"""
    return [
        {
            "field": "normalized_dipole",
            "meaning": "导入 D=[s0]-(1/(|S|-1))sum_{s!=s0}[s]。",
        },
        {
            "field": "pair_contrast_family",
            "meaning": "对每个非根源点登记 e_s=[s0]-[s]。",
        },
        {
            "field": "uniform_pair_weight",
            "meaning": "每个成对对比的权重都是 1/(|S|-1)。",
        },
        {
            "field": "pair_average_identity",
            "meaning": "D=(1/(|S|-1))sum_{s!=s0} e_s。",
        },
        {
            "field": "unit_balance",
            "meaning": "每个 e_s 都有一个根点正单位和一个源点负单位，总系数为零。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 pair-average contrast 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeNormalizedRootMeanDipoleImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange normalized root-mean dipole circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeRootSourcePairAverageContrast",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeRootSourcePairAverageContrast",
            True,
            False,
            "|S|=1 或成对扇退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRootSourcePairAverageContrast",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRootSourcePairAverageContrast",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRootSourcePairAverageContrast",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRootSourcePairAverageContrast",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangeNormalizedRootMeanDipoleImportedForPairAverage",
            True,
            True,
            "导入上一层 D=[s0]-(1/(|S|-1))sum_{s!=s0}[s]。",
            DIPOLE_IMPORT,
        ),
        row(
            "PhaseResidueExchangeRootSourcePairFan",
            True,
            True,
            "非根均值云被展开为根点到每个非根源点的成对扇。",
            PAIR_FAN,
        ),
        row(
            "PhaseResidueExchangeRootSourcePairContrastFamily",
            True,
            True,
            "对每个 s!=s0 登记 e_s=[s0]-[s]。",
            PAIR_CONTRAST_FAMILY,
        ),
        row(
            "PhaseResidueExchangeUniformPairWeight",
            True,
            True,
            "每条成对对比的权重固定为 1/(|S|-1)，不存在可调配重。",
            UNIFORM_WEIGHT,
        ),
        row(
            "PhaseResidueExchangePairAverageContrastIdentity",
            True,
            True,
            "D 恰等于所有 e_s 的均匀平均。",
            PAIR_AVERAGE_IDENTITY,
        ),
        row(
            "PhaseResidueExchangeRootSourcePairUnitBalance",
            True,
            True,
            "每个成对对比都是 +1 根点与 -1 源点的零均值单位对比。",
            UNIT_BALANCE,
        ),
        row(
            "PhaseResidueNoAnonymousNonrootMeanAfterPairAverage",
            True,
            True,
            "非根均值不再匿名保留；它已分解为命名 root-source pair fan。",
            NO_NONROOT_MEAN_ANON,
        ),
        row(
            "PhaseResidueExchangeRootSourcePairAverageContrastPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange root-source pair-average contrast circuit PDEC/cap。",
            PAIR_PACKET,
        ),
        row(
            "NoAnonymousNormalizedRootMeanDipoleAfterPairAverage",
            True,
            True,
            "normalized root-mean dipole 不再匿名保留；它被压成均匀成对对比平均。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeRootSourcePairAverageContrast",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeRootSourcePairAverageContrastStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、root-source pair-average contrast、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange root-source pair-average contrast circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 root-source pair-average contrast 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange normalized root-mean dipole 已把剩余压力固定为"
        " D=[s0]-(1/(|S|-1))sum_{s!=s0}[s]。"
        "本步把非根均值展开为根点到每个非根源点的成对对比均匀平均："
        " D=(1/(|S|-1))sum_{s!=s0}([s0]-[s])。"
        "剩余反例不再是匿名非根均值云，而必须表现为 root-source pair-average contrast circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_root_source_pair_average_contrast_router",
        "status": "phase_residue_exchange_normalized_root_mean_dipole_reduced_to_root_source_pair_average_contrast_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "root_source_pair_average_contrast_records": pair_average_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_normalized_root_mean_dipole_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_normalized_root_mean_dipole_imported_for_pair_average": True,
        "phase_residue_exchange_root_source_pair_fan_closed": True,
        "phase_residue_exchange_root_source_pair_contrast_family_closed": True,
        "phase_residue_exchange_uniform_pair_weight_closed": True,
        "phase_residue_exchange_pair_average_contrast_identity_closed": True,
        "phase_residue_exchange_root_source_pair_unit_balance_closed": True,
        "phase_residue_no_anonymous_nonroot_mean_after_pair_average_closed": True,
        "phase_residue_exchange_root_source_pair_average_contrast_packet_registered": True,
        "anonymous_normalized_root_mean_dipole_removed_after_pair_average": True,
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
        "phase_residue_exchange_root_source_pair_average_contrast_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange root-source pair-average contrast 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_normalized_root_mean_dipole_imported={fmt_bool(cert['phase_residue_exchange_normalized_root_mean_dipole_imported'])}",
        f"phase_residue_exchange_root_source_pair_fan_closed={fmt_bool(cert['phase_residue_exchange_root_source_pair_fan_closed'])}",
        f"phase_residue_exchange_uniform_pair_weight_closed={fmt_bool(cert['phase_residue_exchange_uniform_pair_weight_closed'])}",
        f"phase_residue_exchange_pair_average_contrast_identity_closed={fmt_bool(cert['phase_residue_exchange_pair_average_contrast_identity_closed'])}",
        f"phase_residue_exchange_root_source_pair_average_contrast_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_root_source_pair_average_contrast_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 归一化偶极输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "D = [s0] - (1/(|S|-1)) sum_{s != s0}[s]",
        "```",
        "",
        "`|S|=1` 的退化情形已由 singleton atom/SAE 出口承接，因此这里处理 `|S|>1`。",
        "",
        "## 2. 成对对比扇",
        "",
        "对每个非根源点定义成对对比：",
        "",
        "```text",
        "e_s = [s0] - [s],  s != s0",
        "```",
        "",
        "每个 `e_s` 都是一个根点正单位和一个源点负单位的零均值单位对比。",
        "",
        "## 3. 均匀平均恒等式",
        "",
        "归一化偶极恰等于这些成对对比的均匀平均：",
        "",
        "```text",
        "D = (1/(|S|-1)) sum_{s != s0} e_s",
        "  = (1/(|S|-1)) sum_{s != s0} ([s0] - [s])",
        "```",
        "",
        "所以非根均值云不再匿名；剩余压力被固定为一个 root-source pair fan 的均匀平均。",
        "",
        "## 4. root-source pair-average contrast 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["root_source_pair_average_contrast_records"]:
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
            "- 本证书没有证明 phase-residue exchange root-source pair-average contrast circuit PDEC/cap。",
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
    print("phase_residue_exchange_root_source_pair_average_contrast_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
