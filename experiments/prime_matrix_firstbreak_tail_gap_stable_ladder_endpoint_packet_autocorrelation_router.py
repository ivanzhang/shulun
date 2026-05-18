#!/usr/bin/env python3
"""生成 stable ladder endpoint packet autocorrelation 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_packet_autocorrelation_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointDyadicEnergyPacketPDECCap"

IMPORT = "StableLadderEndpointDyadicEnergyPacketImportedLedger"
ISOLATED = "StableLadderIsolatedSingletonCarriedForwardAfterPacketAutocorrelationLedger"
GROUP = "StableLadderEndpointPacketFiniteGroupLedger"
SUPPORT = "StableLadderEndpointPacketSignedSupportLedger"
SINGLETON = "StableLadderEndpointPacketSingletonAtomLedger"
PAIRCOUNT = "StableLadderEndpointPacketNonzeroPairCountLedger"
DISPLACEMENT = "StableLadderEndpointPacketDisplacementPigeonholeLedger"
WEIGHTED = "StableLadderEndpointPacketWeightedAutocorrelationLedger"
DIMENSION = "StableLadderEndpointPacketDimensionPreservedLedger"
NO_ANON = "NoAnonymousEndpointDyadicEnergyPacketExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterPacketAutocorrelationLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointPacketSingletonAtomSAEOrEndpointDisplacementAutocorrelationPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {ISOLATED} AND {GROUP} AND {SUPPORT} AND {SINGLETON} "
    f"AND {PAIRCOUNT} AND {DISPLACEMENT} AND {WEIGHTED} AND {DIMENSION} "
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
    """把旧活动基中的 dyadic packet 硬点替换成自相关接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint packet autocorrelation 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointDyadicEnergyPacketImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、endpoint dyadic energy packet 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderIsolatedSingletonCarriedForwardAfterPacketAutocorrelation",
            True,
            False,
            "原有孤立 singleton atom 继续前传；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderEndpointPacketFiniteGroup",
            True,
            True,
            "一维边际包位于 H=Z/q_jZ，二维 balanced cell 包位于 H=(Z/q_jZ)^2。",
            GROUP,
        ),
        row(
            "StableLadderEndpointPacketSignedSupport",
            True,
            True,
            "上一层 signed half 给出同号 dyadic 支持 S；在 S 上 lambda<epsilon*F<=2lambda。",
            SUPPORT,
        ),
        row(
            "StableLadderEndpointPacketSingletonAtom",
            True,
            False,
            "若 |S|=1，则剩余成为 endpoint packet singleton atom/SAE；本步不证明其可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointPacketNonzeroPairCount",
            True,
            True,
            "若 |S|=m>=2，则有 m(m-1) 个有序非零差分支持对。",
            PAIRCOUNT,
        ),
        row(
            "StableLadderEndpointPacketDisplacementPigeonhole",
            True,
            True,
            "在有限群 H 中存在非零位移 delta，使 C_S(delta)>=m(m-1)/(|H|-1)。",
            DISPLACEMENT,
        ),
        row(
            "StableLadderEndpointPacketWeightedAutocorrelation",
            True,
            True,
            "同号与 dyadic 幅度给出 weighted autocorrelation 下界 A_F(delta)>=lambda^2*C_S(delta)。",
            WEIGHTED,
        ),
        row(
            "StableLadderEndpointPacketDimensionPreserved",
            True,
            True,
            "dimension=1 保留为端点余数位移；dimension=2 保留为端点 cell 位移。",
            DIMENSION,
        ),
        row(
            "NoAnonymousEndpointDyadicEnergyPacketExit",
            True,
            True,
            "endpoint dyadic energy packet 被压成 singleton atom 或显式非零位移自相关。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterPacketAutocorrelation",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointPacketAutocorrelationCapStillOpen",
            False,
            False,
            "仍未排斥 endpoint packet singleton atom 或 endpoint displacement autocorrelation PDEC/cap。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、endpoint packet singleton/autocorrelation 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint packet autocorrelation 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "endpoint dyadic energy packet 可压成 singleton atom 或同号支持的非零位移自相关。"
        "上一层已经给出带 sign 与尺度 lambda 的 dyadic 支持 S。若 S 是单点，成为 packet singleton atom。"
        "若 |S|=m>=2，则所有有序不同点对产生 m(m-1) 个非零差分；有限群鸽巢给出某个非零位移 delta "
        "承载至少 m(m-1)/(|H|-1) 个支持对。同号 dyadic 幅度进一步给出 weighted autocorrelation 下界。"
        "因此剩余不再是匿名能量包，而是 endpoint packet singleton 或显式 endpoint displacement autocorrelation PDEC cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_packet_autocorrelation_router",
        "status": "endpoint_dyadic_packet_reduced_to_singleton_or_displacement_autocorrelation_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_dyadic_energy_packet_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "isolated_singleton_carried_forward": True,
        "endpoint_packet_finite_group_closed": True,
        "endpoint_packet_signed_support_closed": True,
        "endpoint_packet_singleton_atom_registered": True,
        "endpoint_packet_nonzero_pair_count_closed": True,
        "endpoint_packet_displacement_pigeonhole_closed": True,
        "endpoint_packet_weighted_autocorrelation_closed": True,
        "endpoint_packet_dimension_preserved": True,
        "anonymous_endpoint_dyadic_energy_packet_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "endpoint_packet_singleton_atom_sae_proved": False,
        "endpoint_displacement_autocorrelation_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "autocorrelation_formulas": {
            "group_dimension_1": "H=Z/q_j Z",
            "group_dimension_2": "H=(Z/q_j Z)^2",
            "signed_support": "S={z in H: lambda < epsilon*F(z) <= 2lambda}",
            "singleton_branch": "|S|=1 => endpoint packet singleton atom",
            "pair_count": "|S|=m>=2 => sum_{delta!=0} C_S(delta)=m(m-1)",
            "pigeonhole": "exists delta!=0: C_S(delta)>=m(m-1)/(|H|-1)",
            "weighted_autocorrelation": "A_F(delta)=sum_{z,z+delta in S} F(z)F(z+delta) >= lambda^2*C_S(delta)",
            "dimension_preservation": "dimension=1 endpoint-residue displacement; dimension=2 endpoint-cell displacement",
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
        "# Prime Matrix stable-ladder endpoint packet autocorrelation 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_dyadic_energy_packet_imported={fmt_bool(cert['endpoint_dyadic_energy_packet_imported'])}",
        f"isolated_singleton_carried_forward={fmt_bool(cert['isolated_singleton_carried_forward'])}",
        f"endpoint_packet_finite_group_closed={fmt_bool(cert['endpoint_packet_finite_group_closed'])}",
        f"endpoint_packet_signed_support_closed={fmt_bool(cert['endpoint_packet_signed_support_closed'])}",
        f"endpoint_packet_singleton_atom_registered={fmt_bool(cert['endpoint_packet_singleton_atom_registered'])}",
        f"endpoint_packet_nonzero_pair_count_closed={fmt_bool(cert['endpoint_packet_nonzero_pair_count_closed'])}",
        f"endpoint_packet_displacement_pigeonhole_closed={fmt_bool(cert['endpoint_packet_displacement_pigeonhole_closed'])}",
        f"endpoint_packet_weighted_autocorrelation_closed={fmt_bool(cert['endpoint_packet_weighted_autocorrelation_closed'])}",
        f"endpoint_packet_dimension_preserved={fmt_bool(cert['endpoint_packet_dimension_preserved'])}",
        f"anonymous_endpoint_dyadic_energy_packet_removed={fmt_bool(cert['anonymous_endpoint_dyadic_energy_packet_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"endpoint_packet_singleton_atom_sae_proved={fmt_bool(cert['endpoint_packet_singleton_atom_sae_proved'])}",
        f"endpoint_displacement_autocorrelation_pdec_cap_proved={fmt_bool(cert['endpoint_displacement_autocorrelation_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. packet 所在有限群",
        "",
        "上一层 endpoint dyadic energy packet 有两种维度：",
        "",
        "```text",
        "dimension=1: H=Z/q_j Z,",
        "dimension=2: H=(Z/q_j Z)^2.",
        "```",
        "",
        "packet 带有尺度 `lambda`、符号 `epsilon` 与同号支持：",
        "",
        "```text",
        "S={z in H: lambda < epsilon*F(z) <= 2lambda}.",
        "```",
        "",
        "这里 `F` 是行/列边际偏差或 balanced core 偏差。",
        "",
        "## 2. singleton 分支",
        "",
        "若：",
        "",
        "```text",
        "|S|=1,",
        "```",
        "",
        "则 packet 已经是一个 endpoint packet singleton atom。该分支仍需 SAE/cap 排斥；本证书只登记该 atom。",
        "",
        "## 3. 非零位移自相关",
        "",
        "若 `|S|=m>=2`，定义支持自相关：",
        "",
        "```text",
        "C_S(delta)=#{z in S: z+delta in S}.",
        "```",
        "",
        "所有有序不同点对贡献非零差分，因此：",
        "",
        "```text",
        "sum_{delta != 0} C_S(delta)=m(m-1).",
        "```",
        "",
        "由于 `H` 是有限群，鸽巢给出某个 `delta != 0`：",
        "",
        "```text",
        "C_S(delta) >= m(m-1)/(|H|-1).",
        "```",
        "",
        "## 4. weighted autocorrelation",
        "",
        "在选中的同号 dyadic 支持上，任意两个命中点满足：",
        "",
        "```text",
        "F(z)F(z+delta) >= lambda^2.",
        "```",
        "",
        "于是加权自相关满足：",
        "",
        "```text",
        "A_F(delta)=sum_{z,z+delta in S} F(z)F(z+delta)",
        "          >= lambda^2*C_S(delta).",
        "```",
        "",
        "dimension=1 时这是端点余数位移；dimension=2 时这是端点 cell 位移。两种情况都保留 actual-load 端点口径。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 endpoint dyadic energy packet 变成 endpoint packet singleton atom 或 endpoint displacement autocorrelation cap，外加原有孤立 singleton 与 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 6. 判定表",
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
            "## 7. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 8. 诚实边界",
            "",
            "- 本证书没有证明原有孤立 singleton atom 全局可求和。",
            "- 本证书没有证明 endpoint packet singleton atom/SAE。",
            "- 本证书没有证明 endpoint displacement autocorrelation/PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 endpoint dyadic energy packet 压成 singleton 或非零位移自相关出口。",
            f"- `{NEW_TARGET}` 仍未闭合。",
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
