#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit signed Fourier 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_signed_fourier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-signed-fourier-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.json"
PREVIOUS_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitLongSameSignArcSAEOrEndpointOrbitBoundaryFluxPDECCap"
)

IMPORT = "StableLadderEndpointOrbitRunBoundaryImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterSignedFourierLedger"
SIGNED_SEQ = "StableLadderEndpointOrbitSignedIndicatorSequenceLedger"
FULL_MEAN = "StableLadderEndpointOrbitFullCycleMeanAtomRegistrationLedger"
LONG_DISC = "StableLadderEndpointOrbitLongArcCenteredDiscrepancyLedger"
ARC_KERNEL = "StableLadderEndpointOrbitArcDirichletKernelLedger"
BOUNDARY_DERIV = "StableLadderEndpointOrbitBoundaryDerivativeSupportLedger"
DERIV_FOURIER = "StableLadderEndpointOrbitBoundaryDerivativeFourierLedger"
SIGNED_FOURIER = "StableLadderEndpointOrbitSignedFourierCapRegistrationLedger"
NO_ANON = "NoAnonymousEndpointOrbitLongArcBoundaryExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterOrbitSignedFourierLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitFullCycleMeanAtomSAEOrEndpointOrbitSignedFourierPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {SIGNED_SEQ} AND {FULL_MEAN} "
    f"AND {LONG_DISC} AND {ARC_KERNEL} AND {BOUNDARY_DERIV} "
    f"AND {DERIV_FOURIER} AND {SIGNED_FOURIER} AND {NO_ANON} "
    f"AND {SPARSE} AND {NEW_TARGET}"
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
    """把旧活动基中的 long-arc/boundary 硬点替换成 signed Fourier 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit signed Fourier 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointOrbitRunBoundaryImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton、long same-sign arc、boundary flux 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterSignedFourier",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitSignedIndicatorSequence",
            True,
            True,
            "在 C_r 上定义 g_t=sigma_t u_t in {-1,0,1}，长弧和边界均由 g_t 统一编码。",
            SIGNED_SEQ,
        ),
        row(
            "StableLadderEndpointOrbitFullCycleMeanAtomRegistration",
            True,
            False,
            "若整周期同号，则登记为 full-cycle mean atom；本步不证明其 SAE。",
            FULL_MEAN,
        ),
        row(
            "StableLadderEndpointOrbitLongArcCenteredDiscrepancy",
            True,
            True,
            "非全周期极大长同号 run I 给出正中心化区间差 Delta_eps(I)>=|I|/r。",
            LONG_DISC,
        ),
        row(
            "StableLadderEndpointOrbitArcDirichletKernel",
            True,
            True,
            "区间差由非零频率和显式 Dirichlet kernel 表示，故产生 signed Fourier 下界。",
            ARC_KERNEL,
        ),
        row(
            "StableLadderEndpointOrbitBoundaryDerivativeSupport",
            True,
            True,
            "边界通量 b 给出循环差分 Dg 的支持/能量下界 sum |Dg|^2 >= b。",
            BOUNDARY_DERIV,
        ),
        row(
            "StableLadderEndpointOrbitBoundaryDerivativeFourier",
            True,
            True,
            "Parseval 给出某个非零频率的 derivative Fourier 下界。",
            DERIV_FOURIER,
        ),
        row(
            "StableLadderEndpointOrbitSignedFourierCapRegistration",
            True,
            False,
            "长弧与边界两支均进入 signed Fourier PDEC/cap；本步不排斥该 cap。",
            SIGNED_FOURIER,
        ),
        row(
            "NoAnonymousEndpointOrbitLongArcBoundaryExit",
            True,
            True,
            "匿名 long-arc/boundary 出口被压成 full-cycle mean atom 或 signed Fourier cap。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterOrbitSignedFourier",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitSignedFourierCapStillOpen",
            False,
            False,
            "仍未排斥 singleton atom/SAE、full-cycle mean atom/SAE、signed Fourier PDEC/cap 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、full-cycle mean atom、signed Fourier 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit signed Fourier 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "把单轨道上的 active/sign 信息统一写成 g_t=sigma_t u_t。"
        "非全周期极大长同号 run 给出正中心化区间差，并经 Dirichlet kernel 产生非零频率下界。"
        "高边界通量给出 Dg 的能量下界，并经 Parseval 产生 derivative Fourier 下界。"
        "因此 long-arc 与 boundary-flux 两支统一压成 full-cycle mean atom 或 endpoint orbit signed Fourier/PDEC cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_signed_fourier_router",
        "status": "endpoint_orbit_long_arc_boundary_reduced_to_signed_fourier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_orbit_run_boundary_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_signed_indicator_sequence_closed": True,
        "endpoint_orbit_full_cycle_mean_atom_registered": True,
        "endpoint_orbit_long_arc_centered_discrepancy_closed": True,
        "endpoint_orbit_arc_dirichlet_kernel_closed": True,
        "endpoint_orbit_boundary_derivative_support_closed": True,
        "endpoint_orbit_boundary_derivative_fourier_closed": True,
        "endpoint_orbit_signed_fourier_cap_registered": True,
        "anonymous_endpoint_orbit_long_arc_boundary_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_full_cycle_mean_atom_sae_proved": False,
        "endpoint_orbit_signed_fourier_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "signed_fourier_formulas": {
            "cycle": "C_r=Z/rZ",
            "signed_indicator": "g_t=sigma_t u_t in {-1,0,1}",
            "mean": "bar_g=(1/r)sum_t g_t, nu_t=g_t-bar_g",
            "long_arc_discrepancy": "if I is a maximal same-sign run with g_t=epsilon and not full-cycle, Delta_epsilon(I)=epsilon*sum_{t in I}nu_t>=|I|/r",
            "arc_fourier_identity": "Delta_epsilon(I)=(epsilon/r)sum_{h!=0}hat g(h)hat 1_I(-h)",
            "arc_frequency_lower_bound": "exists h!=0: |hat g(h)| >= r*Delta_epsilon(I)/Lambda_r(I)",
            "boundary_derivative": "Dg_t=g_{t+1}-g_t",
            "boundary_energy": "boundary count b => sum_t |Dg_t|^2 >= b",
            "derivative_parseval": "sum_{h!=0}|(exp(2*pi*i*h/r)-1)hat g(h)|^2=r*sum_t |Dg_t|^2",
            "derivative_frequency_lower_bound": "exists h!=0: |(exp(2*pi*i*h/r)-1)hat g(h)| >= sqrt(r*b/(r-1))",
            "full_cycle_exception": "g_t is constant epsilon on all C_r => EndpointOrbitFullCycleMeanAtomSAE",
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
        "# Prime Matrix stable-ladder endpoint orbit signed Fourier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_orbit_run_boundary_imported={fmt_bool(cert['endpoint_orbit_run_boundary_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_signed_indicator_sequence_closed={fmt_bool(cert['endpoint_orbit_signed_indicator_sequence_closed'])}",
        f"endpoint_orbit_full_cycle_mean_atom_registered={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_registered'])}",
        f"endpoint_orbit_long_arc_centered_discrepancy_closed={fmt_bool(cert['endpoint_orbit_long_arc_centered_discrepancy_closed'])}",
        f"endpoint_orbit_arc_dirichlet_kernel_closed={fmt_bool(cert['endpoint_orbit_arc_dirichlet_kernel_closed'])}",
        f"endpoint_orbit_boundary_derivative_support_closed={fmt_bool(cert['endpoint_orbit_boundary_derivative_support_closed'])}",
        f"endpoint_orbit_boundary_derivative_fourier_closed={fmt_bool(cert['endpoint_orbit_boundary_derivative_fourier_closed'])}",
        f"endpoint_orbit_signed_fourier_cap_registered={fmt_bool(cert['endpoint_orbit_signed_fourier_cap_registered'])}",
        f"anonymous_endpoint_orbit_long_arc_boundary_removed={fmt_bool(cert['anonymous_endpoint_orbit_long_arc_boundary_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_full_cycle_mean_atom_sae_proved={fmt_bool(cert['endpoint_orbit_full_cycle_mean_atom_sae_proved'])}",
        f"endpoint_orbit_signed_fourier_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_signed_fourier_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有符号循环函数",
        "",
        "固定上一层的轨道 `C_r=Z/rZ`。令：",
        "",
        "```text",
        "g_t=sigma_t*u_t in {-1,0,1},",
        "bar_g=(1/r) sum_t g_t,",
        "nu_t=g_t-bar_g.",
        "```",
        "",
        "这里 `u_t` 是 active 指示，`sigma_t` 是符号。`nu` 是零均值的 actual signed load。",
        "",
        "## 2. 长同号弧到区间 Fourier",
        "",
        "若存在非全周期极大同号 run `I`，且 `g_t=epsilon` 于 `I` 上，则：",
        "",
        "```text",
        "Delta_epsilon(I)=epsilon*sum_{t in I} nu_t >= |I|/r > 0.",
        "```",
        "",
        "Fourier 展开给出：",
        "",
        "```text",
        "Delta_epsilon(I)=(epsilon/r) sum_{h!=0} hat g(h) hat 1_I(-h).",
        "```",
        "",
        "因此存在非零频率：",
        "",
        "```text",
        "|hat g(h)| >= r*Delta_epsilon(I)/Lambda_r(I),",
        "Lambda_r(I)=sum_{h!=0}|hat 1_I(h)|.",
        "```",
        "",
        "若整周期都是同一符号，则不走 Fourier，而登记为 `EndpointOrbitFullCycleMeanAtomSAE`。",
        "",
        "## 3. 边界通量到差分 Fourier",
        "",
        "令循环差分：",
        "",
        "```text",
        "Dg_t=g_{t+1}-g_t.",
        "```",
        "",
        "若边界通量给出切口数 `b`，则每个切口贡献非零差分，故：",
        "",
        "```text",
        "sum_t |Dg_t|^2 >= b.",
        "```",
        "",
        "Parseval 恒等式给出：",
        "",
        "```text",
        "sum_{h!=0}|(exp(2*pi*i*h/r)-1)hat g(h)|^2 = r*sum_t |Dg_t|^2.",
        "```",
        "",
        "所以存在非零频率：",
        "",
        "```text",
        "|(exp(2*pi*i*h/r)-1)hat g(h)| >= sqrt(r*b/(r-1)).",
        "```",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 long same-sign arc / boundary flux 变成 full-cycle mean atom 或 signed Fourier PDEC/cap，外加 endpoint singleton atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitSignedFourierPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 long-arc/boundary 二出口压成 full-cycle mean atom 或 signed Fourier cap。",
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
