#!/usr/bin/env python3
"""生成 stable ladder endpoint bilinear balance 三分证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_bilinear_balance_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-bilinear-balance-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientEndpointBilinearFourierPDECCap"

IMPORT = "StableLadderEndpointBilinearFourierImportedLedger"
ISOLATED = "StableLadderIsolatedSingletonCarriedForwardAfterBilinearBalanceLedger"
MATRIX = "StableLadderEndpointPairMatrixRegisteredLedger"
CENTERED = "StableLadderEndpointCenteredKernelTotalZeroLedger"
DECOMP = "StableLadderEndpointMarginalBalancedDecompositionLedger"
PAIRING = "StableLadderEndpointBilinearPhasePairingLedger"
TRICHOTOMY = "StableLadderEndpointBilinearTriangleTrichotomyLedger"
ROW = "StableLadderEndpointRowMarginalFourierExitLedger"
COL = "StableLadderEndpointColumnMarginalFourierExitLedger"
ENERGY = "StableLadderEndpointBalancedCoreEnergyLowerBoundLedger"
NO_ANON = "NoAnonymousEndpointBilinearFourierExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterBilinearBalanceLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrEndpointMarginalFourierOrBalancedBilinearEnergyPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {ISOLATED} AND {MATRIX} AND {CENTERED} AND {DECOMP} "
    f"AND {PAIRING} AND {TRICHOTOMY} AND {ROW} AND {COL} AND {ENERGY} "
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
    """把旧活动基中的 endpoint bilinear 硬点替换成边际/平衡核接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint bilinear balance 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointBilinearFourierImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、endpoint bilinear Fourier/PDEC cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderIsolatedSingletonCarriedForwardAfterBilinearBalance",
            True,
            False,
            "孤立 singleton atom 继续作为单独 summability/cap 出口；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderEndpointPairMatrixRegistered",
            True,
            True,
            "actual pair witnesses 按端点余数 x=n1 mod q_j、y=n2 mod q_j 登记为二部矩阵 M(x,y)。",
            MATRIX,
        ),
        row(
            "StableLadderEndpointCenteredKernelTotalZero",
            True,
            True,
            "从 M 中减去显式 model/Dirichlet kernel 得到中心化 K；总质量差为 0，model 不作为 actual load 计数。",
            CENTERED,
        ),
        row(
            "StableLadderEndpointMarginalBalancedDecomposition",
            True,
            True,
            "K 精确分解为 row marginal、column marginal 与双边际为零的 balanced core。",
            DECOMP,
        ),
        row(
            "StableLadderEndpointBilinearPhasePairing",
            True,
            True,
            "endpoint 相位和写成 S_beta=<K, conj(phi_beta) otimes phi_beta>。",
            PAIRING,
        ),
        row(
            "StableLadderEndpointBilinearTriangleTrichotomy",
            True,
            True,
            "若 |S_beta| 超过 cap 阈值，则 row marginal Fourier、column marginal Fourier 或 balanced core 三者至少一个超阈。",
            TRICHOTOMY,
        ),
        row(
            "StableLadderEndpointRowMarginalFourierExit",
            True,
            False,
            "row marginal 异常成为端点边际 Fourier/PDEC cap；本步不排斥该 cap。",
            ROW,
        ),
        row(
            "StableLadderEndpointColumnMarginalFourierExit",
            True,
            False,
            "column marginal 异常成为端点边际 Fourier/PDEC cap；本步不排斥该 cap。",
            COL,
        ),
        row(
            "StableLadderEndpointBalancedCoreEnergyLowerBound",
            True,
            False,
            "若两侧边际不异常，则 Hilbert-Schmidt/Cauchy 给出 balanced core 能量下界；本步不排斥该能量 cap。",
            ENERGY,
        ),
        row(
            "NoAnonymousEndpointBilinearFourierExit",
            True,
            True,
            "endpoint bilinear Fourier 出口被压成边际 Fourier 或平衡核能量输入。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterBilinearBalance",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointMarginalOrBalancedEnergyCapStillOpen",
            False,
            False,
            "仍未排斥端点边际 Fourier cap、balanced bilinear energy cap、孤立 singleton 或 sparse SAE。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、端点边际/平衡核 cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint bilinear balance 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "endpoint bilinear Fourier cap 可转写为端点二部矩阵的中心化相位相关。"
        "令 M(x,y) 计数 actual pair witnesses，x=n1 mod q_j, y=n2 mod q_j；"
        "减去显式 model 得 K。K 按行边际、列边际和平衡核作精确 ANOVA 分解。"
        "若非平凡相位 S_beta 仍超阈，则三分为 row marginal Fourier、column marginal Fourier "
        "或 balanced core Hilbert-Schmidt/additive-energy 异常。"
        "因此剩余不再是匿名 endpoint bilinear cap，而是端点边际 Fourier 或平衡核能量 PDEC cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_bilinear_balance_router",
        "status": "endpoint_bilinear_split_to_marginal_or_balanced_energy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_bilinear_fourier_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "isolated_singleton_carried_forward": True,
        "endpoint_pair_matrix_registered": True,
        "endpoint_centered_kernel_total_zero": True,
        "endpoint_marginal_balanced_decomposition_closed": True,
        "endpoint_bilinear_phase_pairing_closed": True,
        "endpoint_bilinear_triangle_trichotomy_closed": True,
        "endpoint_row_marginal_fourier_exit_registered": True,
        "endpoint_column_marginal_fourier_exit_registered": True,
        "endpoint_balanced_core_energy_lower_bound_registered": True,
        "anonymous_endpoint_bilinear_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "endpoint_marginal_fourier_pdec_cap_proved": False,
        "balanced_bilinear_energy_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "matrix_formulas": {
            "endpoint_group": "G=Z/q_j Z, x=n1 mod q_j, y=n2 mod q_j",
            "actual_matrix": "M(x,y)=# actual pair witnesses with endpoints (x,y)",
            "centered_kernel": "K(x,y)=M(x,y)-Model(x,y), sum_{x,y}K(x,y)=0",
            "row_marginal": "rho(x)=sum_y K(x,y)",
            "column_marginal": "sigma(y)=sum_x K(x,y)",
            "balanced_core": "K0(x,y)=K(x,y)-rho(x)/|Y|-sigma(y)/|X|",
            "balanced_margins": "sum_y K0(x,y)=0 and sum_x K0(x,y)=0",
            "phase_pairing": "S_beta=sum_{x,y}K(x,y)*conj(phi_beta(x))*phi_beta(y)",
            "trichotomy": "|S_beta|>=eta => row exit or column exit or |<K0,conj(phi)otimes phi>|>=eta/3",
            "energy_lower_bound": "|<K0,conj(phi)otimes phi>|>=eta/3 => ||K0||_HS^2>=eta^2/(9|X||Y|)",
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
        "# Prime Matrix stable-ladder endpoint bilinear balance 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_bilinear_fourier_imported={fmt_bool(cert['endpoint_bilinear_fourier_imported'])}",
        f"isolated_singleton_carried_forward={fmt_bool(cert['isolated_singleton_carried_forward'])}",
        f"endpoint_pair_matrix_registered={fmt_bool(cert['endpoint_pair_matrix_registered'])}",
        f"endpoint_centered_kernel_total_zero={fmt_bool(cert['endpoint_centered_kernel_total_zero'])}",
        f"endpoint_marginal_balanced_decomposition_closed={fmt_bool(cert['endpoint_marginal_balanced_decomposition_closed'])}",
        f"endpoint_bilinear_phase_pairing_closed={fmt_bool(cert['endpoint_bilinear_phase_pairing_closed'])}",
        f"endpoint_bilinear_triangle_trichotomy_closed={fmt_bool(cert['endpoint_bilinear_triangle_trichotomy_closed'])}",
        f"endpoint_row_marginal_fourier_exit_registered={fmt_bool(cert['endpoint_row_marginal_fourier_exit_registered'])}",
        f"endpoint_column_marginal_fourier_exit_registered={fmt_bool(cert['endpoint_column_marginal_fourier_exit_registered'])}",
        f"endpoint_balanced_core_energy_lower_bound_registered={fmt_bool(cert['endpoint_balanced_core_energy_lower_bound_registered'])}",
        f"anonymous_endpoint_bilinear_removed={fmt_bool(cert['anonymous_endpoint_bilinear_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"endpoint_marginal_fourier_pdec_cap_proved={fmt_bool(cert['endpoint_marginal_fourier_pdec_cap_proved'])}",
        f"balanced_bilinear_energy_pdec_cap_proved={fmt_bool(cert['balanced_bilinear_energy_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 端点二部矩阵",
        "",
        "令 `G=Z/q_j Z`。对上一层得到的 actual pair witnesses，记录两个端点余数：",
        "",
        "```text",
        "x=n1 mod q_j,",
        "y=n2 mod q_j.",
        "```",
        "",
        "定义二部计数矩阵：",
        "",
        "```text",
        "M(x,y)=# actual pair witnesses with endpoint residues (x,y).",
        "```",
        "",
        "从 `M` 中减去上一层已经分离出的显式 model/Dirichlet kernel，得到中心化核：",
        "",
        "```text",
        "K(x,y)=M(x,y)-Model(x,y),",
        "sum_{x,y} K(x,y)=0.",
        "```",
        "",
        "这里的 `Model` 只作为显式核扣除，不作为 actual load 计数。",
        "",
        "## 2. 行列边际与平衡核",
        "",
        "在活动端点域 `X,Y` 上写：",
        "",
        "```text",
        "rho(x)=sum_y K(x,y),",
        "sigma(y)=sum_x K(x,y).",
        "```",
        "",
        "由于总质量中心化，定义：",
        "",
        "```text",
        "K0(x,y)=K(x,y)-rho(x)/|Y|-sigma(y)/|X|.",
        "```",
        "",
        "于是有精确分解：",
        "",
        "```text",
        "K(x,y)=rho(x)/|Y| + sigma(y)/|X| + K0(x,y),",
        "sum_y K0(x,y)=0,",
        "sum_x K0(x,y)=0.",
        "```",
        "",
        "若活动域就是完整 residue group，非平凡角色会直接杀掉纯行/列项；若存在窗口或 aperture，行/列项则成为端点边际 Fourier cap。",
        "",
        "## 3. 双线性相位配对",
        "",
        "令：",
        "",
        "```text",
        "phi_beta(z)=e_{q_j}(beta*z).",
        "```",
        "",
        "上一层的 endpoint bilinear 异常写成：",
        "",
        "```text",
        "S_beta=sum_{x,y} K(x,y)*conjugate(phi_beta(x))*phi_beta(y).",
        "```",
        "",
        "代入分解得到：",
        "",
        "```text",
        "S_beta=S_row(beta)+S_col(beta)+S_bal(beta).",
        "```",
        "",
        "`S_row` 与 `S_col` 只依赖端点边际的 Fourier 系数；`S_bal` 是双边际为零的平衡核相位能量。",
        "",
        "## 4. 三分与能量下界",
        "",
        "若 endpoint bilinear cap 给出：",
        "",
        "```text",
        "|S_beta| >= eta,",
        "```",
        "",
        "则三角不等式强制至少一个出口发生：",
        "",
        "```text",
        "|S_row(beta)| >= eta/3,",
        "or |S_col(beta)| >= eta/3,",
        "or |S_bal(beta)| >= eta/3.",
        "```",
        "",
        "前两项是 row/column endpoint marginal Fourier 异常。第三项由 Cauchy-Schwarz 给出：",
        "",
        "```text",
        "|S_bal(beta)| <= sqrt(|X|*|Y|) * ||K0||_HS.",
        "```",
        "",
        "所以若边际不异常而 `|S_bal(beta)| >= eta/3`，则：",
        "",
        "```text",
        "||K0||_HS^2 >= eta^2/(9|X||Y|).",
        "```",
        "",
        "这就是 balanced bilinear energy/PDEC cap 的显式能量形态。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从匿名 endpoint bilinear Fourier/PDEC cap 变成端点边际 Fourier cap 或 balanced bilinear energy cap，外加孤立 singleton 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明端点边际 Fourier/PDEC cap。",
            "- 本证书没有证明 balanced bilinear energy/PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 endpoint bilinear Fourier cap 拆成边际或平衡核能量出口。",
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
