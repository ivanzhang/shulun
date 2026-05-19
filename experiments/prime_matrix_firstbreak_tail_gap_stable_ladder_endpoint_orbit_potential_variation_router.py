#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit potential-variation 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_potential_variation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-potential-variation-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-arc-endpoint-potential-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitArcEndpointPotentialPDECCap"
)

IMPORT = "StableLadderEndpointOrbitArcEndpointPotentialImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPotentialVariationLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPotentialVariationLedger"
CENTERED = "StableLadderEndpointOrbitCenteredPotentialIncrementLedger"
DIRECTED = "StableLadderEndpointOrbitEndpointGapDirectedArcLedger"
POS_VAR = "StableLadderEndpointOrbitPositiveVariationLowerBoundLedger"
NEG_VAR = "StableLadderEndpointOrbitNegativeVariationLowerBoundLedger"
VAR_PACKET = "StableLadderEndpointOrbitSignedVariationPacketLedger"
NO_ANON = "NoAnonymousEndpointPotentialGapExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPotentialVariationLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedVariationPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {FULL_MEAN} AND {CENTERED} "
    f"AND {DIRECTED} AND {POS_VAR} AND {NEG_VAR} AND {VAR_PACKET} "
    f"AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
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


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的 endpoint-potential 硬点替换成 signed-variation 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit potential-variation 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitArcEndpointPotentialImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、full-cycle mean atom、arc endpoint-potential cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterPotentialVariation",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomCarriedForwardAfterPotentialVariation",
            True,
            False,
            "full-cycle mean atom/SAE 继续前传；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitCenteredPotentialIncrement",
            True,
            True,
            "中心化势能满足 F(j+1)-F(j)=Y_j 且 sum_C Y_j=0。",
            CENTERED,
        ),
        row(
            "StableLadderEndpointOrbitEndpointGapDirectedArc",
            True,
            True,
            "若 F(v)-F(u)>=G，则弧 I=[u,v) 的增量和至少 G，补弧 J=[v,u) 的增量和至多 -G。",
            DIRECTED,
        ),
        row(
            "StableLadderEndpointOrbitPositiveVariationLowerBound",
            True,
            True,
            "sum_{j in I}(Y_j)_+ >= G；否则弧 I 不可能累积出 G 的正势能差。",
            POS_VAR,
        ),
        row(
            "StableLadderEndpointOrbitNegativeVariationLowerBound",
            True,
            True,
            "sum_{j in J}(Y_j)_- >= G；补弧必须支付同等反向势能回落。",
            NEG_VAR,
        ),
        row(
            "StableLadderEndpointOrbitSignedVariationPacket",
            True,
            False,
            "endpoint-potential cap 被登记为实际边增量 signed variation 包；本步不排斥该 cap。",
            VAR_PACKET,
        ),
        row(
            "NoAnonymousEndpointPotentialGapExit",
            True,
            True,
            "剩余不再是匿名两端点势能差，而是正/负边增量 variation 负载。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPotentialVariation",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitSignedVariationCapStillOpen",
            False,
            False,
            "仍未排斥 singleton、full-cycle mean atom、signed variation PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean、signed variation cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit potential-variation 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "arc endpoint-potential cap 给出 F(v)-F(u)>=G，其中 G=L/2。"
        "中心化势能满足 F(j+1)-F(j)=Y_j 且全周期增量和为零。"
        "沿弧 I=[u,v) 的增量和至少 G，因此正 variation 至少 G；补弧 J=[v,u) 的增量和至多 -G，"
        "因此负 variation 至少 G。于是匿名端点势能差被压成实际轨道边增量上的 signed variation PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_potential_variation_router",
        "status": "endpoint_orbit_endpoint_potential_reduced_to_signed_variation_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_arc_endpoint_potential_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_full_cycle_mean_atom_carried_forward": True,
        "endpoint_orbit_centered_potential_increment_closed": True,
        "endpoint_orbit_endpoint_gap_directed_arc_closed": True,
        "endpoint_orbit_positive_variation_lower_bound_closed": True,
        "endpoint_orbit_negative_variation_lower_bound_closed": True,
        "endpoint_orbit_signed_variation_packet_registered": True,
        "anonymous_endpoint_potential_gap_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_signed_variation_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "potential_variation_formulas": {
            "imported_gap": "F(v)-F(u)>=G, G=L/2",
            "increments": "Y_j=F(j+1)-F(j), sum_{j in C_m}Y_j=0",
            "direct_arc": "I=[u,v), sum_{j in I}Y_j=F(v)-F(u)>=G",
            "complement_arc": "J=[v,u), sum_{j in J}Y_j=F(u)-F(v)<=-G",
            "positive_variation": "sum_{j in I}(Y_j)_+ >= G",
            "negative_variation": "sum_{j in J}(Y_j)_- >= G",
            "new_exit": "EndpointOrbitSignedVariationPDECCap",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": build_rows(previous),
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder endpoint orbit potential-variation 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_arc_endpoint_potential_imported={fmt_bool(cert['endpoint_orbit_arc_endpoint_potential_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_full_cycle_mean_atom_carried_forward={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_carried_forward'])}",
        f"endpoint_orbit_centered_potential_increment_closed={fmt_bool(cert['endpoint_orbit_centered_potential_increment_closed'])}",
        f"endpoint_orbit_endpoint_gap_directed_arc_closed={fmt_bool(cert['endpoint_orbit_endpoint_gap_directed_arc_closed'])}",
        f"endpoint_orbit_positive_variation_lower_bound_closed={fmt_bool(cert['endpoint_orbit_positive_variation_lower_bound_closed'])}",
        f"endpoint_orbit_negative_variation_lower_bound_closed={fmt_bool(cert['endpoint_orbit_negative_variation_lower_bound_closed'])}",
        f"endpoint_orbit_signed_variation_packet_registered={fmt_bool(cert['endpoint_orbit_signed_variation_packet_registered'])}",
        f"anonymous_endpoint_potential_gap_removed={fmt_bool(cert['anonymous_endpoint_potential_gap_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_signed_variation_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_signed_variation_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 端点势能差包",
        "",
        "上一层给出：",
        "",
        "```text",
        "F(v)-F(u) >= G,",
        "G=L/2.",
        "```",
        "",
        "中心化增量为：",
        "",
        "```text",
        "Y_j=F(j+1)-F(j),",
        "sum_{j in C_m}Y_j=0.",
        "```",
        "",
        "## 2. 有向弧与补弧",
        "",
        "令：",
        "",
        "```text",
        "I=[u,v),",
        "J=[v,u).",
        "```",
        "",
        "则：",
        "",
        "```text",
        "sum_{j in I}Y_j = F(v)-F(u) >= G,",
        "sum_{j in J}Y_j = F(u)-F(v) <= -G.",
        "```",
        "",
        "## 3. signed variation 负载",
        "",
        "由弧和下界得到：",
        "",
        "```text",
        "sum_{j in I}(Y_j)_+ >= G.",
        "```",
        "",
        "由补弧回落得到：",
        "",
        "```text",
        "sum_{j in J}(Y_j)_- >= G.",
        "```",
        "",
        "因此端点势能差不再是匿名两端点事件；它强制实际轨道边增量携带正/负 variation 负载。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 arc endpoint-potential PDEC/cap 变成 endpoint orbit signed variation PDEC/cap，外加 endpoint singleton atom、full-cycle mean atom 与 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
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
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 endpoint singleton atom/SAE。",
            "- 本证书没有证明 EndpointOrbitFullCycleMeanAtomSAE。",
            "- 本证书没有证明 EndpointOrbitSignedVariationPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 arc endpoint-potential cap 压成轨道边增量 signed variation 包。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
