#!/usr/bin/env python3
"""生成 stable ladder endpoint energy packet 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_energy_packet_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-energy-packet-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointMarginalFourierOrBalancedBilinearEnergyPDECCap"

IMPORT = "StableLadderEndpointMarginalOrBalancedEnergyImportedLedger"
ISOLATED = "StableLadderIsolatedSingletonCarriedForwardAfterEnergyPacketLedger"
MARGINAL_PARSEVAL = "StableLadderEndpointMarginalFourierParsevalVarianceLedger"
MARGINAL_DYADIC = "StableLadderEndpointMarginalVarianceDyadicPacketLedger"
BALANCED_IMPORT = "StableLadderBalancedCoreEnergyImportedLedger"
BALANCED_DYADIC = "StableLadderBalancedCoreEnergyDyadicCellPacketLedger"
SIGN_SPLIT = "StableLadderEndpointEnergyPacketSignedHalfLedger"
PACKET = "StableLadderEndpointDyadicEnergyPacketRegisteredLedger"
NO_ANON = "NoAnonymousEndpointMarginalOrBalancedEnergyExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterEndpointEnergyPacketLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointDyadicEnergyPacketPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {ISOLATED} AND {MARGINAL_PARSEVAL} AND {MARGINAL_DYADIC} "
    f"AND {BALANCED_IMPORT} AND {BALANCED_DYADIC} AND {SIGN_SPLIT} "
    f"AND {PACKET} AND {NO_ANON} AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的边际/平衡核硬点替换成 dyadic packet 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint energy packet 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointMarginalOrBalancedEnergyImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、endpoint marginal Fourier、balanced bilinear energy 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderIsolatedSingletonCarriedForwardAfterEnergyPacket",
            True,
            False,
            "孤立 singleton atom 继续作为单独 summability/cap 出口；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderEndpointMarginalFourierParsevalVariance",
            True,
            True,
            "任一端点边际非平凡 Fourier 下界经 Parseval 强制同一边际向量的 L2 方差下界。",
            MARGINAL_PARSEVAL,
        ),
        row(
            "StableLadderEndpointMarginalVarianceDyadicPacket",
            True,
            True,
            "有限 dyadic pigeonhole 把边际 L2 方差压成一维端点余数能量包。",
            MARGINAL_DYADIC,
        ),
        row(
            "StableLadderBalancedCoreEnergyImported",
            True,
            False,
            "balanced core 能量下界从上一层直接导入；本步不证明其不能发生。",
            BALANCED_IMPORT,
        ),
        row(
            "StableLadderBalancedCoreEnergyDyadicCellPacket",
            True,
            True,
            "有限 dyadic pigeonhole 把 ||K0||_HS^2 下界压成二维端点 cell 能量包。",
            BALANCED_DYADIC,
        ),
        row(
            "StableLadderEndpointEnergyPacketSignedHalf",
            True,
            True,
            "实值中心化偏差的平方能量至少有一半来自正偏差或负偏差，可登记为 signed packet。",
            SIGN_SPLIT,
        ),
        row(
            "StableLadderEndpointDyadicEnergyPacketRegistered",
            True,
            False,
            "剩余被登记为一维边际包或二维 balanced cell 包；排斥该 packet 仍是开放 PDEC/cap。",
            PACKET,
        ),
        row(
            "NoAnonymousEndpointMarginalOrBalancedEnergyExit",
            True,
            True,
            "endpoint marginal Fourier 与 balanced energy 出口都被压成显式 dyadic energy packet。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterEndpointEnergyPacket",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointDyadicEnergyPacketCapStillOpen",
            False,
            False,
            "仍未排斥 dyadic energy packet，也未证明孤立 singleton 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、endpoint dyadic energy packet 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint energy packet 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "endpoint marginal Fourier 与 balanced bilinear energy 可以统一压成 dyadic energy packet。"
        "边际 Fourier 下界先由 Parseval 变成端点边际 L2 方差；balanced 分支已经是 K0 的 Hilbert-Schmidt 能量。"
        "在有限端点域上做 dyadic pigeonhole，并按正负偏差取至少半能量的一侧，得到一维边际包或二维 balanced cell 包。"
        "因此剩余不再是匿名频率或抽象能量，而是可计数、带尺度、带符号、带端点支持的 energy packet PDEC cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_energy_packet_router",
        "status": "endpoint_marginal_or_balanced_energy_reduced_to_dyadic_packet_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_marginal_or_balanced_energy_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "isolated_singleton_carried_forward": True,
        "endpoint_marginal_fourier_parseval_variance_closed": True,
        "endpoint_marginal_variance_dyadic_packet_closed": True,
        "balanced_core_energy_imported": True,
        "balanced_core_energy_dyadic_cell_packet_closed": True,
        "endpoint_energy_packet_signed_half_closed": True,
        "endpoint_dyadic_energy_packet_registered": True,
        "anonymous_endpoint_marginal_or_balanced_energy_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "endpoint_dyadic_energy_packet_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "packet_formulas": {
            "marginal_parseval": "|hat rho(beta)|>=eta => sum_x |rho(x)|^2 >= eta^2/q_j",
            "column_parseval": "|hat sigma(beta)|>=eta => sum_y |sigma(y)|^2 >= eta^2/q_j",
            "balanced_energy": "||K0||_HS^2 >= E",
            "dyadic_marginal_packet": "exists lambda: lambda^2*#{x: lambda<|rho(x)|<=2lambda} >= ||rho||_2^2/L",
            "dyadic_cell_packet": "exists lambda: lambda^2*#{(x,y): lambda<|K0(x,y)|<=2lambda} >= ||K0||_HS^2/L",
            "signed_half": "energy(packet positive part) >= packet_energy/2 or energy(packet negative part) >= packet_energy/2",
            "packet_types": "dimension=1 marginal endpoint packet or dimension=2 balanced endpoint-cell packet",
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
        "# Prime Matrix stable-ladder endpoint energy packet 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_marginal_or_balanced_energy_imported={fmt_bool(cert['endpoint_marginal_or_balanced_energy_imported'])}",
        f"isolated_singleton_carried_forward={fmt_bool(cert['isolated_singleton_carried_forward'])}",
        f"endpoint_marginal_fourier_parseval_variance_closed={fmt_bool(cert['endpoint_marginal_fourier_parseval_variance_closed'])}",
        f"endpoint_marginal_variance_dyadic_packet_closed={fmt_bool(cert['endpoint_marginal_variance_dyadic_packet_closed'])}",
        f"balanced_core_energy_imported={fmt_bool(cert['balanced_core_energy_imported'])}",
        f"balanced_core_energy_dyadic_cell_packet_closed={fmt_bool(cert['balanced_core_energy_dyadic_cell_packet_closed'])}",
        f"endpoint_energy_packet_signed_half_closed={fmt_bool(cert['endpoint_energy_packet_signed_half_closed'])}",
        f"endpoint_dyadic_energy_packet_registered={fmt_bool(cert['endpoint_dyadic_energy_packet_registered'])}",
        f"anonymous_endpoint_marginal_or_balanced_energy_removed={fmt_bool(cert['anonymous_endpoint_marginal_or_balanced_energy_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"endpoint_dyadic_energy_packet_pdec_cap_proved={fmt_bool(cert['endpoint_dyadic_energy_packet_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 边际 Fourier 到方差",
        "",
        "上一层的 row/column endpoint marginal Fourier 出口分别给出某个非平凡 `beta` 上的下界。",
        "对行边际 `rho`，若：",
        "",
        "```text",
        "|hat rho(beta)| >= eta,",
        "```",
        "",
        "则 Parseval 直接给出：",
        "",
        "```text",
        "sum_x |rho(x)|^2 >= eta^2/q_j.",
        "```",
        "",
        "列边际 `sigma` 完全相同：",
        "",
        "```text",
        "|hat sigma(beta)| >= eta => sum_y |sigma(y)|^2 >= eta^2/q_j.",
        "```",
        "",
        "因此边际 Fourier cap 先被压成端点边际方差 cap。",
        "",
        "## 2. balanced core 能量导入",
        "",
        "上一层的 balanced 分支已经给出：",
        "",
        "```text",
        "||K0||_HS^2 >= E.",
        "```",
        "",
        "这里 `K0` 仍是双边际为零的中心化核。本步不排斥该能量，只把它转成可数尺度包。",
        "",
        "## 3. dyadic packet",
        "",
        "在有限端点域上，对任意非零实值偏差函数 `F` 做 dyadic 分层。若：",
        "",
        "```text",
        "E_F=sum_z |F(z)|^2,",
        "```",
        "",
        "则存在某个 dyadic 尺度 `lambda`，使：",
        "",
        "```text",
        "lambda^2 * #{z: lambda < |F(z)| <= 2lambda} >= E_F/L.",
        "```",
        "",
        "`L` 是该有限支持上的非空 dyadic 层数。对 `rho` 或 `sigma`，这是 `dimension=1` 的端点边际包；对 `K0`，这是 `dimension=2` 的端点 cell 包。",
        "",
        "## 4. signed half",
        "",
        "由于 `rho`、`sigma` 与 `K0` 都是实值中心化偏差，选中的 dyadic 层可继续按正负号分裂。至少一侧贡献一半平方能量：",
        "",
        "```text",
        "energy(positive packet) >= packet_energy/2",
        "or energy(negative packet) >= packet_energy/2.",
        "```",
        "",
        "所以新剩余可以统一登记为带有 `dimension`、`lambda`、`sign`、`support` 和 `energy lower bound` 的 endpoint dyadic energy packet。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从端点边际 Fourier 或 balanced bilinear energy 变成 endpoint dyadic energy packet cap，外加孤立 singleton 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明孤立 singleton atom 全局可求和。",
            "- 本证书没有证明 endpoint dyadic energy packet/PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把端点边际 Fourier 与 balanced energy 出口压成显式 dyadic energy packet。",
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
