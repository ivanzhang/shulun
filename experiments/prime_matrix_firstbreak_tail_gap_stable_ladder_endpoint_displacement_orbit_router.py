#!/usr/bin/env python3
"""生成 stable ladder endpoint displacement orbit 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_displacement_orbit_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-packet-autocorrelation-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointPacketSingletonAtomSAEOrEndpointDisplacementAutocorrelationPDECCap"

IMPORT = "StableLadderEndpointSingletonOrDisplacementAutocorrelationImportedLedger"
SINGLETON_UNIFY = "StableLadderEndpointSingletonAtomSAEUnifiedLedger"
DISPLACEMENT = "StableLadderEndpointDisplacementAutocorrelationImportedLedger"
ORDER = "StableLadderEndpointNonzeroDisplacementOrderLedger"
ORBIT_PARTITION = "StableLadderEndpointDisplacementOrbitPartitionLedger"
ORBIT_DECOMP = "StableLadderEndpointAutocorrelationOrbitDecompositionLedger"
ORBIT_PIGEON = "StableLadderEndpointWeightedOrbitPigeonholeLedger"
CYCLIC = "StableLadderEndpointOrbitCyclicAdjacencyPacketLedger"
DIMENSION = "StableLadderEndpointOrbitDimensionPreservedLedger"
NO_ANON = "NoAnonymousEndpointDisplacementAutocorrelationExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterDisplacementOrbitLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointTranslationOrbitAdjacencyPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON_UNIFY} AND {DISPLACEMENT} AND {ORDER} "
    f"AND {ORBIT_PARTITION} AND {ORBIT_DECOMP} AND {ORBIT_PIGEON} "
    f"AND {CYCLIC} AND {DIMENSION} AND {NO_ANON} AND {SPARSE} "
    f"AND {NEW_TARGET}"
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
    """把旧活动基中的 singleton/autocorrelation 硬点替换成 orbit adjacency 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint displacement orbit 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointSingletonOrDisplacementAutocorrelationImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、endpoint packet singleton、displacement autocorrelation 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAEUnified",
            True,
            False,
            "原有孤立 singleton 与 packet singleton 合并为 endpoint singleton atom/SAE；本步不证明其可求和。",
            SINGLETON_UNIFY,
        ),
        row(
            "StableLadderEndpointDisplacementAutocorrelationImported",
            True,
            False,
            "非零位移 weighted autocorrelation 分支从上一层导入；本步不排斥该 cap。",
            DISPLACEMENT,
        ),
        row(
            "StableLadderEndpointNonzeroDisplacementOrder",
            True,
            True,
            "对有限群 H 中非零 delta，r=ord_H(delta)>1，平移 T_delta 生成长度 r 的循环轨道。",
            ORDER,
        ),
        row(
            "StableLadderEndpointDisplacementOrbitPartition",
            True,
            True,
            "H 被商 H/<delta> 分解为互不相交的 T_delta 轨道。",
            ORBIT_PARTITION,
        ),
        row(
            "StableLadderEndpointAutocorrelationOrbitDecomposition",
            True,
            True,
            "A_F(delta) 精确分解为各轨道上的邻接加权和 A_O(delta)。",
            ORBIT_DECOMP,
        ),
        row(
            "StableLadderEndpointWeightedOrbitPigeonhole",
            True,
            True,
            "若全局 A_F(delta) 超阈，则存在单个轨道 O 承载至少平均值的加权邻接质量。",
            ORBIT_PIGEON,
        ),
        row(
            "StableLadderEndpointOrbitCyclicAdjacencyPacket",
            True,
            False,
            "该单轨道成为 Z/rZ 上的 signed cyclic adjacency packet；排斥仍是开放 PDEC/cap。",
            CYCLIC,
        ),
        row(
            "StableLadderEndpointOrbitDimensionPreserved",
            True,
            True,
            "dimension=1 保留端点余数周期轨道；dimension=2 保留端点 cell 周期轨道。",
            DIMENSION,
        ),
        row(
            "NoAnonymousEndpointDisplacementAutocorrelationExit",
            True,
            True,
            "endpoint displacement autocorrelation 被压成单个 translation orbit adjacency packet。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterDisplacementOrbit",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointTranslationOrbitAdjacencyCapStillOpen",
            False,
            False,
            "仍未排斥 endpoint singleton atom/SAE 或 endpoint translation orbit adjacency PDEC/cap。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 endpoint singleton、translation orbit adjacency 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint displacement orbit 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "endpoint displacement autocorrelation 可压到单个平移轨道上的循环邻接包。"
        "先把原有 isolated singleton 与 packet singleton 统一为 endpoint singleton atom/SAE。"
        "对非零位移 delta，令 r=ord_H(delta)>1；有限群 H 被 T_delta 轨道分解。"
        "全局 weighted autocorrelation 是各轨道邻接加权和之和，因此若全局分支超阈，"
        "必有一个轨道承载至少平均邻接质量。剩余不再是全群匿名位移，而是 Z/rZ 上的 signed translation orbit adjacency packet。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_displacement_orbit_router",
        "status": "endpoint_displacement_autocorrelation_reduced_to_translation_orbit_adjacency_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_singleton_or_displacement_autocorrelation_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_unified": True,
        "endpoint_displacement_autocorrelation_imported": True,
        "endpoint_nonzero_displacement_order_closed": True,
        "endpoint_displacement_orbit_partition_closed": True,
        "endpoint_autocorrelation_orbit_decomposition_closed": True,
        "endpoint_weighted_orbit_pigeonhole_closed": True,
        "endpoint_orbit_cyclic_adjacency_packet_registered": True,
        "endpoint_orbit_dimension_preserved": True,
        "anonymous_endpoint_displacement_autocorrelation_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_translation_orbit_adjacency_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "orbit_formulas": {
            "order": "r=ord_H(delta)>1",
            "orbit_space": "Omega=H/<delta>, |Omega|=|H|/r",
            "orbit_parametrization": "O=a+<delta>={a+t*delta: t in Z/rZ}",
            "global_decomposition": "A_F(delta)=sum_{O in Omega} A_O(delta)",
            "orbit_sum": "A_O(delta)=sum_{t in Z/rZ} F(a+t*delta)F(a+(t+1)*delta) 1_{both in S}",
            "pigeonhole": "exists O: A_O(delta)>=A_F(delta)/|Omega|",
            "cyclic_packet": "single orbit becomes signed adjacency packet on Z/rZ",
            "singleton_unification": "isolated singleton or packet singleton => EndpointSingletonAtomSAE",
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
        "# Prime Matrix stable-ladder endpoint displacement orbit 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_singleton_or_displacement_autocorrelation_imported={fmt_bool(cert['endpoint_singleton_or_displacement_autocorrelation_imported'])}",
        f"endpoint_singleton_atom_sae_unified={fmt_bool(cert['endpoint_singleton_atom_sae_unified'])}",
        f"endpoint_displacement_autocorrelation_imported={fmt_bool(cert['endpoint_displacement_autocorrelation_imported'])}",
        f"endpoint_nonzero_displacement_order_closed={fmt_bool(cert['endpoint_nonzero_displacement_order_closed'])}",
        f"endpoint_displacement_orbit_partition_closed={fmt_bool(cert['endpoint_displacement_orbit_partition_closed'])}",
        f"endpoint_autocorrelation_orbit_decomposition_closed={fmt_bool(cert['endpoint_autocorrelation_orbit_decomposition_closed'])}",
        f"endpoint_weighted_orbit_pigeonhole_closed={fmt_bool(cert['endpoint_weighted_orbit_pigeonhole_closed'])}",
        f"endpoint_orbit_cyclic_adjacency_packet_registered={fmt_bool(cert['endpoint_orbit_cyclic_adjacency_packet_registered'])}",
        f"endpoint_orbit_dimension_preserved={fmt_bool(cert['endpoint_orbit_dimension_preserved'])}",
        f"anonymous_endpoint_displacement_autocorrelation_removed={fmt_bool(cert['anonymous_endpoint_displacement_autocorrelation_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_translation_orbit_adjacency_pdec_cap_proved={fmt_bool(cert['endpoint_translation_orbit_adjacency_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. singleton 合并",
        "",
        "上一层有两个单点来源：原有 isolated singleton 与 endpoint packet singleton。二者都不在本步排斥，而是统一登记为：",
        "",
        "```text",
        "EndpointSingletonAtomSAE.",
        "```",
        "",
        "## 2. 非零位移的周期轨道",
        "",
        "对 displacement autocorrelation 分支，存在有限群 `H` 与非零位移 `delta`。令：",
        "",
        "```text",
        "r=ord_H(delta)>1.",
        "```",
        "",
        "平移 `T_delta:z -> z+delta` 把 `H` 分解为互不相交的循环轨道：",
        "",
        "```text",
        "Omega=H/<delta>,",
        "O=a+<delta>={a+t*delta: t in Z/rZ}.",
        "```",
        "",
        "其中 `|Omega|=|H|/r`。",
        "",
        "## 3. 自相关按轨道分解",
        "",
        "上一层的加权自相关可写成：",
        "",
        "```text",
        "A_F(delta)=sum_{z,z+delta in S} F(z)F(z+delta).",
        "```",
        "",
        "按轨道分解为：",
        "",
        "```text",
        "A_F(delta)=sum_{O in Omega} A_O(delta),",
        "A_O(delta)=sum_{t in Z/rZ} F(a+t*delta)F(a+(t+1)*delta) 1_{both in S}.",
        "```",
        "",
        "因此如果全局 `A_F(delta)` 达到下界，则存在一个轨道 `O` 满足：",
        "",
        "```text",
        "A_O(delta) >= A_F(delta)/|Omega|.",
        "```",
        "",
        "## 4. 单轨道邻接包",
        "",
        "固定该轨道后，问题变成 `Z/rZ` 上的同号 dyadic 邻接包：",
        "",
        "```text",
        "t in Z/rZ,",
        "z_t=a+t*delta,",
        "edge t occurs when z_t,z_{t+1} in S.",
        "```",
        "",
        "dimension=1 时这是端点余数周期轨道；dimension=2 时这是端点 cell 周期轨道。这个口径把全群自相关压成单个 CRT 平移周期上的容量/相位问题。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 endpoint displacement autocorrelation 变成 endpoint translation orbit adjacency cap，外加 endpoint singleton atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 endpoint singleton atom/SAE。",
            "- 本证书没有证明 endpoint translation orbit adjacency/PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把非零位移自相关压到单个平移轨道的循环邻接包。",
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
