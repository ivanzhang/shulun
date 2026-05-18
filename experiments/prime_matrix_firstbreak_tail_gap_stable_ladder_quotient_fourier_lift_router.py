#!/usr/bin/env python3
"""生成 stable ladder quotient Fourier 到 endpoint bilinear 相位的提升证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_fourier_lift_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-fourier-lift-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientArcFourierPDECCap"

IMPORT = "StableLadderQuotientArcFourierImportedLedger"
ISOLATED = "StableLadderIsolatedSingletonCarriedForwardAfterFourierLiftLedger"
NONTRIVIAL = "StableLadderNontrivialQuotientFrequencyForcesRGreaterOneLedger"
COPRIME = "StableLadderQuotientCoprimeFactorizationLedger"
INVERSE = "StableLadderQuotientInverseLiftLedger"
CHARACTER = "StableLadderQuotientCharacterToPivotDifferenceLedger"
NONZERO = "StableLadderLiftedCharacterNontrivialityLedger"
BILINEAR = "StableLadderEndpointBilinearPhaseFactorizationLedger"
MODEL = "StableLadderCenteredModelKernelSeparatedLedger"
NO_ANON = "NoAnonymousQuotientArcFourierExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterFourierLiftLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientEndpointBilinearFourierPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {ISOLATED} AND {NONTRIVIAL} AND {COPRIME} AND {INVERSE} "
    f"AND {CHARACTER} AND {NONZERO} AND {BILINEAR} AND {MODEL} "
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
    """把旧活动基中的 quotient arc Fourier 硬点替换成 endpoint bilinear 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 quotient Fourier lift 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderQuotientArcFourierImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、quotient arc Fourier/PDEC cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderIsolatedSingletonCarriedForwardAfterFourierLift",
            True,
            False,
            "孤立 singleton atom 继续作为单独 summability/cap 出口；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderNontrivialQuotientFrequencyForcesRGreaterOne",
            True,
            True,
            "若存在 h=1,...,R-1 的非平凡频率，则必有 R>1；R=1 时 quotient Fourier 分支为空。",
            NONTRIVIAL,
        ),
        row(
            "StableLadderQuotientCoprimeFactorizationClosed",
            True,
            True,
            "写 g=gcd(q_j,B), B=gB0, q_j=gR，则 gcd(B0,R)=1。",
            COPRIME,
        ),
        row(
            "StableLadderQuotientInverseLiftClosed",
            True,
            True,
            "取 u B0 == 1 mod R；对 d=tB，有 t == u(d/g) mod R。",
            INVERSE,
        ),
        row(
            "StableLadderQuotientCharacterToPivotDifferenceClosed",
            True,
            True,
            "e_R(h t)=e_{q_j}(beta d)，其中 beta == h u mod R。",
            CHARACTER,
        ),
        row(
            "StableLadderLiftedCharacterNontrivialityClosed",
            True,
            True,
            "h not 0 mod R 且 u 可逆，故 beta not 0 mod R；提升后的 pivot-difference 角色非平凡。",
            NONZERO,
        ),
        row(
            "StableLadderEndpointBilinearPhaseFactorizationClosed",
            True,
            True,
            "e_{q_j}(beta(n2-n1))=e_{q_j}(beta n2) conjugate(e_{q_j}(beta n1))，成为两端点双线性相位。",
            BILINEAR,
        ),
        row(
            "StableLadderCenteredModelKernelSeparated",
            True,
            False,
            "centered Fourier coefficient 分裂为 actual endpoint bilinear sum 减显式 model/Dirichlet kernel；本步不排斥该 cap。",
            MODEL,
        ),
        row(
            "NoAnonymousQuotientArcFourierExit",
            True,
            True,
            "quotient arc Fourier 出口被提升为原始 pair endpoint bilinear Fourier/PDEC 输入。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterFourierLift",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointBilinearFourierCapStillOpen",
            False,
            False,
            "仍未排斥 endpoint bilinear Fourier/PDEC 下界，也未证明孤立 singleton 或 sparse SAE 可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、endpoint bilinear Fourier/PDEC cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 quotient Fourier lift 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "quotient arc Fourier 的非平凡频率可提升回原始 pair 差值。"
        "写 g=gcd(q_j,B), B=gB0, q_j=gR, gcd(B0,R)=1，取 uB0=1 mod R。"
        "对 d=tB，有 t=u(d/g) mod R，因此 e_R(ht)=e_{q_j}(beta d)。"
        "再把 d=n2-n1 展开，得到端点双线性相位。剩余不再是抽象 quotient "
        "频率，而是 endpoint bilinear Fourier/PDEC cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_fourier_lift_router",
        "status": "quotient_arc_fourier_lifted_to_endpoint_bilinear_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "quotient_arc_fourier_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "isolated_singleton_carried_forward": True,
        "nontrivial_frequency_forces_r_gt_one": True,
        "quotient_coprime_factorization_closed": True,
        "quotient_inverse_lift_closed": True,
        "quotient_character_to_pivot_difference_closed": True,
        "lifted_character_nontriviality_closed": True,
        "endpoint_bilinear_phase_factorization_closed": True,
        "centered_model_kernel_separated": True,
        "anonymous_quotient_arc_fourier_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "endpoint_bilinear_fourier_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "lift_formulas": {
            "factorization": "g=gcd(q_j,B), B=gB0, q_j=gR, gcd(B0,R)=1",
            "inverse": "u*B0 == 1 mod R",
            "quotient_from_difference": "d=tB => t == u*(d/g) mod R",
            "character_lift": "e_R(h*t)=e_{q_j}(beta*d), beta == h*u mod R",
            "nontriviality": "h not 0 mod R => beta not 0 mod R",
            "endpoint_factorization": "e_{q_j}(beta*(n2-n1))=e_{q_j}(beta*n2)*conj(e_{q_j}(beta*n1))",
            "centered_sum": "hat nu(h)=actual endpoint bilinear phase sum - explicit model kernel",
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
        "# Prime Matrix stable-ladder quotient Fourier lift 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"quotient_arc_fourier_imported={fmt_bool(cert['quotient_arc_fourier_imported'])}",
        f"isolated_singleton_carried_forward={fmt_bool(cert['isolated_singleton_carried_forward'])}",
        f"nontrivial_frequency_forces_r_gt_one={fmt_bool(cert['nontrivial_frequency_forces_r_gt_one'])}",
        f"quotient_coprime_factorization_closed={fmt_bool(cert['quotient_coprime_factorization_closed'])}",
        f"quotient_inverse_lift_closed={fmt_bool(cert['quotient_inverse_lift_closed'])}",
        f"quotient_character_to_pivot_difference_closed={fmt_bool(cert['quotient_character_to_pivot_difference_closed'])}",
        f"lifted_character_nontriviality_closed={fmt_bool(cert['lifted_character_nontriviality_closed'])}",
        f"endpoint_bilinear_phase_factorization_closed={fmt_bool(cert['endpoint_bilinear_phase_factorization_closed'])}",
        f"centered_model_kernel_separated={fmt_bool(cert['centered_model_kernel_separated'])}",
        f"anonymous_quotient_arc_fourier_removed={fmt_bool(cert['anonymous_quotient_arc_fourier_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"endpoint_bilinear_fourier_pdec_cap_proved={fmt_bool(cert['endpoint_bilinear_fourier_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. quotient 因子分解",
        "",
        "沿用上一层记号 `d=n2-n1=tB`。令：",
        "",
        "```text",
        "g=gcd(q_j,B),",
        "B=gB0,",
        "q_j=gR.",
        "```",
        "",
        "则：",
        "",
        "```text",
        "gcd(B0,R)=1.",
        "```",
        "",
        "若存在非平凡 quotient 频率 `1<=h<=R-1`，则 `R>1`；`R=1` 时 Fourier 分支为空。",
        "",
        "## 2. 反解 quotient 相位",
        "",
        "取 `u` 满足：",
        "",
        "```text",
        "u*B0 == 1 mod R.",
        "```",
        "",
        "因为 `d=tB=tgB0`，所以：",
        "",
        "```text",
        "d/g == tB0 mod R,",
        "t == u*(d/g) mod R.",
        "```",
        "",
        "## 3. 提升为 pivot-difference 角色",
        "",
        "对任意非平凡 quotient 频率 `h`，设：",
        "",
        "```text",
        "beta == h*u mod R.",
        "```",
        "",
        "则在所有 actual pair witnesses 上有精确恒等式：",
        "",
        "```text",
        "e_R(h*t)=e_{q_j}(beta*d).",
        "```",
        "",
        "由于 `h` 与 `u` 在 `R` 上非零/可逆，`beta` 不为 `0 mod R`，因此这是非平凡 pivot-difference 相位。",
        "",
        "## 4. endpoint bilinear 因式分解",
        "",
        "把 `d=n2-n1` 展开：",
        "",
        "```text",
        "e_{q_j}(beta*(n2-n1))",
        "  = e_{q_j}(beta*n2) * conjugate(e_{q_j}(beta*n1)).",
        "```",
        "",
        "所以 quotient arc Fourier 的非平凡频率不是抽象周期异常，而是原始 pair 两端点上的双线性相位相关。",
        "",
        "centered Fourier coefficient 仍保持 actual-load 口径：",
        "",
        "```text",
        "hat nu(h)=actual endpoint bilinear phase sum - explicit model kernel.",
        "```",
        "",
        "本证书不排斥该双线性相位 cap；它只把 cap 的对象从 quotient 频率提升到原始端点相位。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 quotient arc Fourier/PDEC cap 变成 endpoint bilinear Fourier/PDEC cap，外加孤立 singleton 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 endpoint bilinear Fourier/PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 quotient arc Fourier cap 提升为原始端点双线性相位证书。",
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
