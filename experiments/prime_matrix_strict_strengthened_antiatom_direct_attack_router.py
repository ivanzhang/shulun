#!/usr/bin/env python3
"""生成 strict actual-source 强化反原子直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_strengthened_antiatom_direct_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-strengthened-antiatom-direct-attack-router.json

输出：
  docs/monograph/prime-matrix-strict-strengthened-antiatom-direct-attack-router.json
  docs/monograph/prime-matrix-strict-strengthened-antiatom-direct-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-strengthened-antiatom-direct-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-strengthened-antiatom-direct-attack-router.md"

HARDPOINT = "FullSNonAPStrengthenedSourceAntiAtomForActualSource"
CONTRACT = "FullSNonAPStrengthenedSourceAntiAtomContract"
NEW_AXIOM = "AddStrengthenedActualSourceAntiAtomTheorem"
SOURCE_IDENTITY = "ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab"
NEW_JOINT_FORMULA = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
EXTERNAL_KLS = "ModulusDependentCompletedFullSKLSInput"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json",
    "prime-matrix-actual-source-antiatom-lane-audit-router.json",
    "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json",
    "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json",
    "prime-matrix-final-open-input-current-attack-router.json",
    "prime-matrix-triad-a1-source-block-entropy-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-moving-atom-entropy-normal-form-router.json",
    "prime-matrix-noncanonical-complement-input-contract-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取上游 JSON；若缺失则返回空对象，方便证书显式显示未闭合。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录本证书使用的上游证据哈希。"""
    result: dict[str, str] = {
        "script": sha256(Path(__file__).resolve()),
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


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


def required_actual_theorem_fields() -> list[dict[str, str]]:
    """列出 actual-source 强化反原子定理必须提供的字段。"""
    return [
        {
            "field": "exact_actual_source_binding",
            "meaning": "证明 M_{u,v} 是实际 RIW/Buchstab、Type/Fourier、dispersion 产生的源容量，而不是任意形式 WFD 模板容量。",
        },
        {
            "field": "scale_uniform_moving_uv_antiatom",
            "meaning": "对随尺度移动的同一 `(u,v)` 标签给出 `max M_{u,v}/sum M_{u,v} <= log^{-2A}`。",
        },
        {
            "field": "nonrecursive_source_constructor",
            "meaning": "在 Cauchy、pair-energy、joint constructor 与 terminal extraction 之前给出正向源构造或等价恒等式。",
        },
        {
            "field": "no_generic_template_substitution",
            "meaning": "不得用 formal WFD、Type-I/II、Fourier smoothing、K4/K6、naive incidence 代替 actual-source 定理。",
        },
        {
            "field": "no_exactuv_pair_joint_loop",
            "meaning": "不得通过 ExactUV/pair-energy/joint 回环证明该反原子，否则回到已记录宏循环。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """同步上游证据并直攻 strengthened actual-source anti-atom。"""
    independent = data["independent"]
    lane = data["lane"]
    source = data["source"]
    nogo = data["nogo"]
    final_open = data["final_open"]
    source_entropy = data["source_entropy"]
    firewall = data["firewall"]
    moving_normal = data["moving_normal"]
    complement = data["complement"]

    antiatom_contract = str(source.get("antiatom_contract", ""))
    contract_pinned = (
        "max_{u,v} M_{u,v}/sum_{u,v}M_{u,v} <= log^{-2A}" in antiatom_contract
        and source.get("terminal_gap_after_router") == f"{CONTRACT}OrExternalDIBFIKuznetsov"
    )
    hardpoint_active = (
        HARDPOINT in str(independent)
        or CONTRACT in str(final_open)
        or HARDPOINT in str(complement)
    )
    moving_delta_imported = (
        nogo.get("self_contained_generic_version_refuted") is True
        and source_entropy.get("all_moving_delta_models_violate_source_entropy") is True
    )
    generic_refuted = (
        lane.get("generic_self_contained_antiatom_refuted") is True
        and complement.get("generic_wfd_template_available") is False
        and moving_delta_imported
    )
    formal_shortcuts_blocked = (
        generic_refuted
        and firewall.get("formal_wfd_route_refuted") is True
        and firewall.get("fixed_projection_route_blocked") is True
    )
    actual_specific_theorem_missing = (
        lane.get("actual_source_antiatom_lane_boundary_closed") is True
        and lane.get("actual_source_antiatom_proved") is False
        and independent.get("strengthened_actual_source_antiatom_proved") is False
    )
    source_identity_open = (
        independent.get("source_identity_proved") is False
        and SOURCE_IDENTITY in str(independent.get("strict_active_basis_after_router", ""))
    )
    external_conditional = (
        EXTERNAL_SPECTRAL in str(final_open)
        or EXTERNAL_KLS in str(independent.get("conditional_external_basis", ""))
    )
    moving_normal_keeps_exact_entropy_open = (
        moving_normal.get("status") == "strict_moving_atom_reduced_to_exact_entropy_open"
    )

    return [
        row(
            "StrengthenedAntiAtomContractPinned",
            contract_pinned,
            True,
            "最终 source 反原子合同已精确钉住为实际容量测度的 moving same-(u,v) log-power 反界。",
            "none at statement-boundary level",
        ),
        row(
            "HardpointActiveInStrictBasis",
            hardpoint_active,
            True,
            "上一轮外环桥后，strict 活动基确实包含 actual-source 强化反原子硬点。",
            HARDPOINT,
        ),
        row(
            "MovingDeltaCountermodelImported",
            moving_delta_imported,
            True,
            "moving-delta 模型通过形式模板但使 `max M/sum M=1`，反证 generic 形式反原子。",
            "不能证明 generic WFD 版。",
        ),
        row(
            "GenericSelfContainedAntiAtomRefuted",
            generic_refuted,
            True,
            "unrestricted generic WFD/Type/Fourier 反原子不是未证，而是在当前形式假设下为假。",
            "必须改为 actual-source 定理或外部谱输入。",
        ),
        row(
            "FormalShortcutFirewallClosed",
            formal_shortcuts_blocked,
            True,
            "formal WFD、固定投影、K4/K6、naive incidence、Fourier smoothing 均不能推出 moving `(u,v)` 反原子。",
            HARDPOINT,
        ),
        row(
            "ActualSourceSpecificTheoremMissing",
            actual_specific_theorem_missing,
            False,
            "当前语料没有证明实际 noncanonical full-S 源满足该强化反原子；只能把它作为新增 actual-source 定理。",
            NEW_AXIOM,
        ),
        row(
            "SourceIdentityParallelExitStillOpen",
            source_identity_open,
            False,
            "另一条自足出口是证明实际源等于 canonical RIW/Buchstab 源；当前只在 canonical 分支 scoped 闭合。",
            SOURCE_IDENTITY,
        ),
        row(
            "MovingAtomExactEntropyStillOpen",
            moving_normal_keeps_exact_entropy_open,
            False,
            "moving atom normal form 仍把问题压到 exact actual-source entropy，而不是给出熵定理本身。",
            "ExactWFDSourceEntropy / strengthened actual-source anti-atom",
        ),
        row(
            "ExternalSpectralInputOnlyConditional",
            external_conditional,
            False,
            "DI/BFI/Kuznetsov 或 completed full-S KLS 可以作为外部输入线，但不能冒充 strict 自足证明。",
            f"{EXTERNAL_SPECTRAL} OR {EXTERNAL_KLS}",
        ),
        row(
            "StrengthenedActualSourceAntiAtomProved",
            False,
            False,
            "本轮直攻未从现有材料推出 actual-source 强化反原子。",
            f"{NEW_AXIOM} OR {EXTERNAL_SPECTRAL}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需 source 破环输入、ExactUV、RatePreservation 与 DStructure/Rankin 全部闭合。",
            f"({NEW_JOINT_FORMULA} OR {SOURCE_IDENTITY} OR {HARDPOINT}) AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 direct attack 证书。"""
    data = {
        "independent": load_json("prime-matrix-strict-independent-source-bridge-outside-loop-attack-router.json"),
        "lane": load_json("prime-matrix-actual-source-antiatom-lane-audit-router.json"),
        "source": load_json("prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"),
        "nogo": load_json("prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"),
        "final_open": load_json("prime-matrix-final-open-input-current-attack-router.json"),
        "source_entropy": load_json("prime-matrix-triad-a1-source-block-entropy-router.json"),
        "firewall": load_json("prime-matrix-strict-exact-entropy-source-law-firewall-router.json"),
        "moving_normal": load_json("prime-matrix-strict-moving-atom-entropy-normal-form-router.json"),
        "complement": load_json("prime-matrix-noncanonical-complement-input-contract-router.json"),
    }
    rows = build_rows(data)
    closed_by_gate = {item["gate"]: item["closed"] for item in rows}
    proved_by_gate = {item["gate"]: item["proved"] for item in rows}
    boundary_closed = all(
        closed_by_gate[name]
        for name in [
            "StrengthenedAntiAtomContractPinned",
            "HardpointActiveInStrictBasis",
            "MovingDeltaCountermodelImported",
            "GenericSelfContainedAntiAtomRefuted",
            "FormalShortcutFirewallClosed",
        ]
    )
    new_actual_source_axiom_required = closed_by_gate["ActualSourceSpecificTheoremMissing"]
    external_only_conditional = closed_by_gate["ExternalSpectralInputOnlyConditional"]
    strict_active_basis = (
        f"({NEW_JOINT_FORMULA} OR {SOURCE_IDENTITY} OR {HARDPOINT}) "
        f"AND {EXACT_UV} AND {RATE} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_strict_strengthened_antiatom_direct_attack_router",
        "status": (
            "strict_strengthened_antiatom_direct_attack_reduced_to_new_actual_source_axiom_or_external_spectral_input_open"
            if boundary_closed
            else "strict_strengthened_antiatom_direct_attack_incomplete"
        ),
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_strengthened_antiatom_direct_attack_boundary_closed": boundary_closed,
        "generic_self_contained_antiatom_refuted": closed_by_gate["GenericSelfContainedAntiAtomRefuted"],
        "formal_wfd_type_fourier_shortcuts_blocked": closed_by_gate["FormalShortcutFirewallClosed"],
        "moving_delta_countermodel_imported": closed_by_gate["MovingDeltaCountermodelImported"],
        "strengthened_actual_source_antiatom_proved": proved_by_gate["StrengthenedActualSourceAntiAtomProved"],
        "new_actual_source_axiom_required": new_actual_source_axiom_required,
        "external_spectral_input_only_conditional": external_only_conditional,
        "source_identity_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "strict_active_basis_after_router": strict_active_basis,
        "next_self_contained_input": NEW_AXIOM,
        "next_external_input": EXTERNAL_SPECTRAL,
        "required_actual_theorem_fields": required_actual_theorem_fields(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            f"本轮直接攻 {HARDPOINT}。合同本身已钉住；generic WFD/Type/Fourier 版被 "
            "moving-delta 模型反证，不能继续当作自足引理。若把命题严格限为 actual-source，"
            "当前材料尚无正向源构造、source identity 或 exact entropy 证明来推出该反原子；"
            f"因此 strict 自足线只能新增并证明 {NEW_AXIOM}，或条件接受 {EXTERNAL_SPECTRAL}。"
            "行/列命题没有无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines: list[str] = []
    lines.append("# Prime Matrix strict actual-source 强化反原子直攻证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append("")
    lines.append(result["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "strict_strengthened_antiatom_direct_attack_boundary_closed",
        "generic_self_contained_antiatom_refuted",
        "formal_wfd_type_fourier_shortcuts_blocked",
        "moving_delta_countermodel_imported",
        "strengthened_actual_source_antiatom_proved",
        "new_actual_source_axiom_required",
        "external_spectral_input_only_conditional",
        "direct_unconditional_contradiction_found",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 直攻判定")
    lines.append("")
    lines.append("```text")
    lines.append("generic formal anti-atom version: refuted by moving-delta;")
    lines.append("actual-source strengthened version: open as a new actual-source theorem;")
    lines.append("external spectral version: acceptable only as conditional input;")
    lines.append("row/column unconditional theorem: not closed.")
    lines.append("```")
    lines.append("")
    lines.append("## 2. actual-source 定理必要字段")
    lines.append("")
    lines.append("| field | meaning |")
    lines.append("| --- | --- |")
    for item in result["required_actual_theorem_fields"]:
        lines.append(f"| `{cell(item['field'])}` | {cell(item['meaning'])} |")
    lines.append("")
    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{cell(item['gate'])}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.append("## 4. 当前严格活动基")
    lines.append("")
    lines.append("```text")
    lines.append(result["strict_active_basis_after_router"])
    lines.append("```")
    lines.append("")
    lines.append("审稿边界：本文件关闭的是 strengthened anti-atom 直攻路线的边界分类；它没有证明 actual-source 强化反原子、ExactUV、RatePreservation 或 DStructure/Rankin。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"status={result['status']}")
    print(f"strengthened_actual_source_antiatom_proved={fmt_bool(result['strengthened_actual_source_antiatom_proved'])}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")
    print(f"wrote={OUT_JSON.relative_to(ROOT)}")
    print(f"wrote={OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
