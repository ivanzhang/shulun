#!/usr/bin/env python3
"""生成 phase-residue exchange root-source pair witness localization 归约证书。

用法示例：
  python3 experiments/prime_matrix_phase_residue_exchange_root_source_pair_witness_localization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.json

输出：
  data/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-ledger.json
  docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.json
  docs/monograph/prime-matrix-phase-residue-exchange-root-source-pair-witness-localization-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phase-residue-exchange-root-source-pair-witness-localization"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-phase-residue-exchange-root-source-pair-average-contrast-router.json"

OLD_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeRootSourcePairAverageContrastCircuitPDECCap"
)
NEW_TARGET = (
    "EndpointOrbitResidueShadowDualRowPhaseCellAtomSignedCoreSupportSliceResidueFiberPhaseWordSlotSourceAtom"
    "MultiplicityFiberSignedOccurrenceUnitIncidenceCellPrimitiveWitnessCRTCoordinateAtomCanonicalCongruenceEquationAtom"
    "PhaseResidueEvaluationAtomExchangeRootSourcePairWitnessLocalizationCircuitPDECCap"
)

IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairAverageContrastImportedLedger"
MULTIPLICITY_CAP = "StableLadderEndpointOrbitMultiplicityCapCarriedForwardAfterExchangeRootSourcePairWitnessLocalizationLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterExchangeRootSourcePairWitnessLocalizationLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRootSourcePairWitnessLocalizationLedger"
BRIDGE = "StableLadderEndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRootSourcePairWitnessLocalizationLedger"
AMPLITUDE_DEPTH = "StableLadderEndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRootSourcePairWitnessLocalizationLedger"
BOUNDARY = "StableLadderEndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRootSourcePairWitnessLocalizationLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterExchangeRootSourcePairWitnessLocalizationLedger"
PAIR_AVERAGE_IMPORT = "StableLadderEndpointOrbitPhaseResidueExchangePairAverageContrastImportedForWitnessLocalizationLedger"
LINEAR_WITNESS = "StableLadderEndpointOrbitPhaseResidueExchangeLinearWitnessFunctionalLedger"
PAIR_VALUE_LIST = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairWitnessValueListLedger"
MEAN_EVALUATION = "StableLadderEndpointOrbitPhaseResidueExchangePairWitnessMeanIdentityLedger"
ORIENTED_WITNESS = "StableLadderEndpointOrbitPhaseResidueExchangeOrientedWitnessSignLedger"
AVERAGE_TO_MAX = "StableLadderEndpointOrbitPhaseResidueExchangeAverageToSinglePairMaxLocalizationLedger"
SINGLE_PAIR_WITNESS = "StableLadderEndpointOrbitPhaseResidueExchangeNamedSinglePairWitnessLedger"
NO_ANON_AVERAGE = "StableLadderEndpointOrbitPhaseResidueNoAnonymousAverageOnlyPairWitnessLedger"
LOCAL_PACKET = "StableLadderEndpointOrbitPhaseResidueExchangeRootSourcePairWitnessLocalizationPacketLedger"
NO_ANON = "NoAnonymousRootSourcePairAverageContrastAfterWitnessLocalizationLedger"


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
    """把 pair-average contrast 硬点替换为 single-pair witness localization 硬点。"""
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
        PAIR_AVERAGE_IMPORT,
        LINEAR_WITNESS,
        PAIR_VALUE_LIST,
        MEAN_EVALUATION,
        ORIENTED_WITNESS,
        AVERAGE_TO_MAX,
        SINGLE_PAIR_WITNESS,
        NO_ANON_AVERAGE,
        LOCAL_PACKET,
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


def witness_records() -> list[dict[str, str]]:
    """给出 root-source pair witness localization 的字段。"""
    return [
        {
            "field": "linear_witness",
            "meaning": "导入任意线性相位/容量见证 Lambda；本步不证明该见证存在。",
        },
        {
            "field": "pair_value_list",
            "meaning": "对每个非根源点登记 a_s=Lambda([s0]-[s])。",
        },
        {
            "field": "mean_identity",
            "meaning": "Lambda(D)=(1/(|S|-1))sum_{s!=s0} a_s。",
        },
        {
            "field": "oriented_sign",
            "meaning": "若平均见证为负，乘以 -1 后转成同号正见证。",
        },
        {
            "field": "single_pair_localization",
            "meaning": "有限平均的最大项不小于平均值，故存在命名单对承载该见证强度。",
        },
    ]


def build_rows(previous: dict[str, Any], new_target: str) -> list[dict[str, Any]]:
    """构造 single-pair witness localization 判定表。"""
    old_target = previous.get("next_direct_attack_target", "")
    imported = OLD_TARGET in old_target
    return [
        row(
            "PhaseResidueExchangeRootSourcePairAverageContrastImported",
            imported,
            False,
            "上一层剩余含 phase-residue exchange root-source pair-average contrast circuit PDEC/cap 或 parallel outlets。",
            old_target or OLD_TARGET,
        ),
        row(
            "MultiplicityCapCarriedForwardAfterExchangeRootSourcePairWitnessLocalization",
            True,
            False,
            "source-atom multiplicity-cap PDEC/cap 继续作为独立出口。",
            MULTIPLICITY_CAP,
        ),
        row(
            "EndpointSingletonAtomSAECarriedForwardAfterExchangeRootSourcePairWitnessLocalization",
            True,
            False,
            "|S|=1 或见证定位退化时仍回流 singleton atom/SAE。",
            SINGLETON,
        ),
        row(
            "EndpointOrbitFullCycleMeanAtomCarriedForwardAfterExchangeRootSourcePairWitnessLocalization",
            True,
            False,
            "若只剩整周期均值异常则回流 full-cycle mean atom/SAE。",
            FULL_MEAN,
        ),
        row(
            "EndpointOrbitBridgeCancellationCarriedForwardAfterExchangeRootSourcePairWitnessLocalization",
            True,
            False,
            "反号债或镜像互付继续由 bridge-cancellation 出口承接。",
            BRIDGE,
        ),
        row(
            "EndpointOrbitAmplitudeDepthCarriedForwardAfterExchangeRootSourcePairWitnessLocalization",
            True,
            False,
            "同号跨尺度堆高继续由 amplitude-depth 出口承接。",
            AMPLITUDE_DEPTH,
        ),
        row(
            "EndpointOrbitVariationBoundaryFluxCarriedForwardAfterExchangeRootSourcePairWitnessLocalization",
            True,
            False,
            "边界迁移继续由 variation-boundary flux 出口承接。",
            BOUNDARY,
        ),
        row(
            "PhaseResidueExchangePairAverageContrastImportedForWitnessLocalization",
            True,
            True,
            "导入上一层 D=(1/(|S|-1))sum e_s。",
            PAIR_AVERAGE_IMPORT,
        ),
        row(
            "PhaseResidueExchangeLinearWitnessFunctional",
            True,
            False,
            "若当前 circuit 由线性相位/容量见证 Lambda 检测，则登记该见证；本步不证明见证存在。",
            LINEAR_WITNESS,
        ),
        row(
            "PhaseResidueExchangeRootSourcePairWitnessValueList",
            True,
            True,
            "把 Lambda 作用到每个成对对比 e_s 上，得到有限值列 a_s。",
            PAIR_VALUE_LIST,
        ),
        row(
            "PhaseResidueExchangePairWitnessMeanIdentity",
            True,
            True,
            "线性性给出 Lambda(D) 等于 a_s 的均匀平均。",
            MEAN_EVALUATION,
        ),
        row(
            "PhaseResidueExchangeOrientedWitnessSign",
            True,
            True,
            "用符号 sigma=sign(Lambda(D)) 把非零平均见证定向为正。",
            ORIENTED_WITNESS,
        ),
        row(
            "PhaseResidueExchangeAverageToSinglePairMaxLocalization",
            True,
            True,
            "有限平均不可能严格大于所有项；存在 s* 使 sigma a_s* >= |Lambda(D)|。",
            AVERAGE_TO_MAX,
        ),
        row(
            "PhaseResidueExchangeNamedSinglePairWitness",
            True,
            True,
            "平均异常可以命名到一个 root-source pair witness。",
            SINGLE_PAIR_WITNESS,
        ),
        row(
            "PhaseResidueNoAnonymousAverageOnlyPairWitness",
            True,
            True,
            "不存在只能由平均整体承载而每个单对都逃逸的线性见证。",
            NO_ANON_AVERAGE,
        ),
        row(
            "PhaseResidueExchangeRootSourcePairWitnessLocalizationPacket",
            True,
            False,
            "若已有出口不支付，剩余就是 exchange root-source pair witness localization circuit PDEC/cap。",
            LOCAL_PACKET,
        ),
        row(
            "NoAnonymousRootSourcePairAverageContrastAfterWitnessLocalization",
            True,
            True,
            "pair-average contrast 不再匿名保留；它被压到命名单对见证定位。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterExchangeRootSourcePairWitnessLocalization",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitPhaseResidueExchangeRootSourcePairWitnessLocalizationStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean、multiplicity cap、root-source pair witness localization、bridge、amplitude、boundary 或 sparse SAE。",
            new_target,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍未无条件闭合；最新硬点为 exchange root-source pair witness localization circuit 或并行出口。",
            new_target,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 root-source pair witness localization 证书。"""
    previous = load_json(PREVIOUS_CERT)
    target = next_target(previous)
    reduced = reduced_target(target)
    latest_basis = replace_latest_basis(previous, reduced)
    plain = (
        "phase-residue exchange root-source pair-average contrast 已把剩余压力固定为"
        " D=(1/(|S|-1))sum_{s!=s0}([s0]-[s])。"
        "本步对任意导入的线性相位/容量见证 Lambda 应用平均恒等式："
        " Lambda(D)=(1/(|S|-1))sum a_s，其中 a_s=Lambda([s0]-[s])。"
        "定向后有限平均不可能超过所有单项，故平均见证可定位到一个命名 root-source pair。"
        "剩余反例不再是匿名平均扇，而必须表现为 root-source pair witness localization circuit PDEC/cap 或已有出口。"
    )
    cert: dict[str, Any] = {
        "certificate_type": "prime_matrix_phase_residue_exchange_root_source_pair_witness_localization_router",
        "status": "phase_residue_exchange_root_source_pair_average_contrast_reduced_to_single_pair_witness_localization_or_existing_caps_open",
        "previous_certificate": str(PREVIOUS_CERT.relative_to(ROOT)),
        "source_exit": previous.get("next_direct_attack_target", OLD_TARGET),
        "new_exit": NEW_TARGET,
        "next_direct_attack_target": target,
        "reduced_target": reduced,
        "latest_noncycle_basis_after_router": latest_basis,
        "plain_conclusion": plain,
        "root_source_pair_witness_localization_records": witness_records(),
        "gates": build_rows(previous, target),
        "phase_residue_exchange_root_source_pair_average_contrast_imported": OLD_TARGET in previous.get("next_direct_attack_target", ""),
        "phase_residue_exchange_pair_average_contrast_imported_for_witness_localization": True,
        "phase_residue_exchange_linear_witness_functional_registered": True,
        "phase_residue_exchange_root_source_pair_witness_value_list_closed": True,
        "phase_residue_exchange_pair_witness_mean_identity_closed": True,
        "phase_residue_exchange_oriented_witness_sign_closed": True,
        "phase_residue_exchange_average_to_single_pair_max_localization_closed": True,
        "phase_residue_exchange_named_single_pair_witness_closed": True,
        "phase_residue_no_anonymous_average_only_pair_witness_closed": True,
        "phase_residue_exchange_root_source_pair_witness_localization_packet_registered": True,
        "anonymous_root_source_pair_average_contrast_removed_after_witness_localization": True,
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
        "phase_residue_exchange_root_source_pair_witness_localization_circuit_pdec_cap_proved": False,
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
        "# Prime Matrix phase-residue exchange root-source pair witness localization 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phase_residue_exchange_root_source_pair_average_contrast_imported={fmt_bool(cert['phase_residue_exchange_root_source_pair_average_contrast_imported'])}",
        f"phase_residue_exchange_pair_witness_mean_identity_closed={fmt_bool(cert['phase_residue_exchange_pair_witness_mean_identity_closed'])}",
        f"phase_residue_exchange_average_to_single_pair_max_localization_closed={fmt_bool(cert['phase_residue_exchange_average_to_single_pair_max_localization_closed'])}",
        f"phase_residue_exchange_named_single_pair_witness_closed={fmt_bool(cert['phase_residue_exchange_named_single_pair_witness_closed'])}",
        f"phase_residue_exchange_root_source_pair_witness_localization_circuit_pdec_cap_proved={fmt_bool(cert['phase_residue_exchange_root_source_pair_witness_localization_circuit_pdec_cap_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 成对平均输入",
        "",
        "上一层给出：",
        "",
        "```text",
        "D = (1/(|S|-1)) sum_{s != s0} e_s,  e_s=[s0]-[s]",
        "```",
        "",
        "`|S|=1` 的退化情形已由 singleton atom/SAE 出口承接，因此这里处理 `|S|>1`。",
        "",
        "## 2. 线性见证值列",
        "",
        "对任意导入的线性相位/容量见证 `Lambda`，定义：",
        "",
        "```text",
        "a_s = Lambda(e_s) = Lambda([s0]-[s])",
        "```",
        "",
        "线性性给出：",
        "",
        "```text",
        "Lambda(D) = (1/(|S|-1)) sum_{s != s0} a_s",
        "```",
        "",
        "## 3. 平均到单对定位",
        "",
        "令 `sigma` 为 `Lambda(D)` 的符号。若平均见证非零，则：",
        "",
        "```text",
        "max_{s != s0} sigma*a_s >= sigma*Lambda(D) = |Lambda(D)|",
        "```",
        "",
        "因此平均见证不能只由匿名整体承载；至少有一个命名 root-source pair 承载同号不小于平均的见证值。",
        "",
        "## 4. root-source pair witness localization 字段",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for item in cert["root_source_pair_witness_localization_records"]:
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
            "- 本证书没有证明 phase-residue exchange root-source pair witness localization circuit PDEC/cap。",
            "- 本证书没有证明 endpoint singleton、full-cycle mean、bridge、amplitude、boundary 或 sparse SAE 出口。",
            "- 本证书没有证明线性相位/容量见证本身存在；它只说明一旦平均见证存在，就能定位到单对。",
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
    print("phase_residue_exchange_root_source_pair_witness_localization_circuit_pdec_cap_proved=false")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
