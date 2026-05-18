#!/usr/bin/env python3
"""生成 stable ladder quotient arc 的 Fourier/PDEC 证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_arc_fourier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-arc-fourier-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-quotient-phase-arc-mean-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientShortArcClusterOrPhaseCycleMeanPDECCap"

IMPORT = "StableLadderQuotientShortArcOrMeanImportedLedger"
ISOLATED = "StableLadderIsolatedSingletonCarriedForwardAfterQuotientFourierLedger"
GROUP = "StableLadderQuotientCircleGroupLedger"
MEASURE = "StableLadderQuotientActualPhaseLoadMeasureLedger"
DISCREPANCY = "StableLadderQuotientArcDiscrepancyFunctionalLedger"
DIRICHLET = "StableLadderQuotientDirichletKernelIdentityLedger"
FOURIER = "StableLadderQuotientNontrivialFrequencyLowerBoundLedger"
MEAN_TO_ARC = "StableLadderPhaseMeanCapAsPointArcLedger"
NO_ANON = "NoAnonymousShortArcOrPhaseMeanExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterQuotientFourierLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderIsolatedSingletonOrQuotientArcFourierPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {ISOLATED} AND {GROUP} AND {MEASURE} AND {DISCREPANCY} "
    f"AND {DIRICHLET} AND {FOURIER} AND {MEAN_TO_ARC} AND {NO_ANON} "
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
    """把旧活动基中的 short-arc/mean 硬点替换成 quotient Fourier 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 quotient arc Fourier 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderQuotientShortArcOrMeanImported",
            imported,
            False,
            "上一层剩余为孤立 singleton、quotient short-arc cluster、phase-cycle actual-mean cap 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderIsolatedSingletonCarriedForwardAfterQuotientFourier",
            True,
            False,
            "孤立 singleton atom 继续作为单独 summability/cap 出口；本步不证明其全局可求和。",
            ISOLATED,
        ),
        row(
            "StableLadderQuotientCircleGroupClosed",
            True,
            True,
            "quotient 相位生活在有限循环群 C_R=Z/RZ，其中 R=q_j/gcd(q_j,B)。",
            GROUP,
        ),
        row(
            "StableLadderQuotientActualPhaseLoadMeasureClosed",
            True,
            True,
            "把 actual quotient witnesses 按 t mod R 计数为 mu(r)，并以 expected/formal mean 中心化为零总量 nu(r)。",
            MEASURE,
        ),
        row(
            "StableLadderQuotientArcDiscrepancyFunctionalClosed",
            True,
            True,
            "任意短弧 A 的过载是 Delta(A)=sum_{r in A}nu(r)>0。",
            DISCREPANCY,
        ),
        row(
            "StableLadderQuotientDirichletKernelIdentityClosed",
            True,
            True,
            "Delta(A)=(1/R) sum_{h!=0} hat nu(h) hat 1_A(-h)，其中 hat 1_A 是显式 Dirichlet kernel。",
            DIRICHLET,
        ),
        row(
            "StableLadderQuotientNontrivialFrequencyLowerBoundClosed",
            True,
            True,
            "若 Delta(A)>0，则存在 h!=0 使 |hat nu(h)| >= R*Delta(A)/sum_{h!=0}|hat 1_A(h)|。",
            FOURIER,
        ),
        row(
            "StableLadderPhaseMeanCapAsPointArcClosed",
            True,
            True,
            "phase-cycle actual-mean 偏差是 A={r0} 的点弧情形，故同样进入非平凡频率证书。",
            MEAN_TO_ARC,
        ),
        row(
            "NoAnonymousShortArcOrPhaseMeanExit",
            True,
            True,
            "short-arc cluster 与 phase-cycle mean cap 被统一为 quotient arc Fourier/PDEC 输入。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterQuotientFourier",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "QuotientArcFourierCapStillOpen",
            False,
            False,
            "仍未排斥 quotient arc Fourier/PDEC 下界，也未证明孤立 singleton 或 sparse SAE 可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭孤立 singleton、quotient arc Fourier/PDEC cap 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 quotient arc Fourier 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "short-arc cluster 与 phase-cycle actual-mean cap 可统一为 C_R=Z/RZ "
        "上的零均值 actual phase load 与区间指标的相关。对任意弧 A，"
        "Delta(A)=sum_A nu=(1/R)sum_{h!=0}hat nu(h)hat 1_A(-h)。"
        "若 Delta(A)>0，则某个非平凡频率满足显式 Dirichlet-kernel 下界。"
        "因此剩余压成 quotient arc Fourier/PDEC cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_quotient_arc_fourier_router",
        "status": "short_arc_or_phase_mean_reduced_to_quotient_arc_fourier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "short_arc_or_mean_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "isolated_singleton_carried_forward": True,
        "quotient_circle_group_closed": True,
        "actual_phase_load_measure_closed": True,
        "arc_discrepancy_functional_closed": True,
        "dirichlet_kernel_identity_closed": True,
        "nontrivial_frequency_lower_bound_closed": True,
        "phase_mean_as_point_arc_closed": True,
        "anonymous_short_arc_or_mean_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "isolated_singleton_summability_proved": False,
        "quotient_arc_fourier_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "fourier_formulas": {
            "group": "C_R=Z/RZ, R=q_j/gcd(q_j,B)",
            "phase_load": "mu(r)=#{actual quotient witnesses with t congruent r mod R}",
            "centered_load": "nu(r)=mu(r)-model(r), sum_{r mod R}nu(r)=0",
            "arc_discrepancy": "Delta(A)=sum_{r in A}nu(r)",
            "fourier_transform": "hat f(h)=sum_{r mod R}f(r)exp(-2*pi*i*h*r/R)",
            "dirichlet_identity": "Delta(A)=(1/R)sum_{h=1}^{R-1}hat nu(h)hat 1_A(-h)",
            "frequency_lower_bound": "Delta(A)>0 => max_{h!=0}|hat nu(h)| >= R*Delta(A)/Lambda_R(A)",
            "dirichlet_l1": "Lambda_R(A)=sum_{h=1}^{R-1}|hat 1_A(h)|",
            "point_arc": "A={r0} gives Lambda_R(A)=R-1 and max |hat nu(h)| >= R*Delta/(R-1)",
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
        "# Prime Matrix stable-ladder quotient arc Fourier 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"short_arc_or_mean_imported={fmt_bool(cert['short_arc_or_mean_imported'])}",
        f"isolated_singleton_carried_forward={fmt_bool(cert['isolated_singleton_carried_forward'])}",
        f"quotient_circle_group_closed={fmt_bool(cert['quotient_circle_group_closed'])}",
        f"actual_phase_load_measure_closed={fmt_bool(cert['actual_phase_load_measure_closed'])}",
        f"arc_discrepancy_functional_closed={fmt_bool(cert['arc_discrepancy_functional_closed'])}",
        f"dirichlet_kernel_identity_closed={fmt_bool(cert['dirichlet_kernel_identity_closed'])}",
        f"nontrivial_frequency_lower_bound_closed={fmt_bool(cert['nontrivial_frequency_lower_bound_closed'])}",
        f"phase_mean_as_point_arc_closed={fmt_bool(cert['phase_mean_as_point_arc_closed'])}",
        f"anonymous_short_arc_or_mean_removed={fmt_bool(cert['anonymous_short_arc_or_mean_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"isolated_singleton_summability_proved={fmt_bool(cert['isolated_singleton_summability_proved'])}",
        f"quotient_arc_fourier_pdec_cap_proved={fmt_bool(cert['quotient_arc_fourier_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. quotient 相位圆",
        "",
        "沿用上一层记号：",
        "",
        "```text",
        "B=W_-j, R=q_j/gcd(q_j,B), d=n2-n1=tB.",
        "```",
        "",
        "所有 pair 的 pivot 相位只依赖 `t mod R`，因此相位空间是有限循环群：",
        "",
        "```text",
        "C_R=Z/RZ.",
        "```",
        "",
        "## 2. actual phase load",
        "",
        "令 `mu(r)` 是 actual quotient witnesses 中 `t congruent r mod R` 的个数。按对应分支的 expected/formal mean 中心化：",
        "",
        "```text",
        "nu(r)=mu(r)-model(r),",
        "sum_{r mod R}nu(r)=0.",
        "```",
        "",
        "`model(r)` 可以是完整周期均值 `a`，也可以是 short-arc cap 使用的同一 actual-load 口径期望；本证书只要求中心化后的零总量，不把 formal envelope 当成 actual load。",
        "",
        "## 3. 短弧偏差",
        "",
        "对任意弧 `A subset C_R`，定义：",
        "",
        "```text",
        "Delta(A)=sum_{r in A}nu(r).",
        "```",
        "",
        "short-arc cluster 是某个真短弧 `A` 上的 `Delta(A)>0`；phase-cycle actual-mean cap 是点弧 `A={r0}` 的同一情形。",
        "",
        "## 4. Dirichlet-kernel Fourier 证书",
        "",
        "取 Fourier 变换：",
        "",
        "```text",
        "hat f(h)=sum_{r mod R} f(r) exp(-2*pi*i*h*r/R).",
        "```",
        "",
        "由于 `sum nu=0`，平凡频率消失，故：",
        "",
        "```text",
        "Delta(A)=(1/R) sum_{h=1}^{R-1} hat nu(h) * hat 1_A(-h).",
        "```",
        "",
        "记：",
        "",
        "```text",
        "Lambda_R(A)=sum_{h=1}^{R-1}|hat 1_A(h)|.",
        "```",
        "",
        "若 `Delta(A)>0`，则存在非平凡频率 `h` 满足：",
        "",
        "```text",
        "|hat nu(h)| >= R*Delta(A)/Lambda_R(A).",
        "```",
        "",
        "当 `A={r0}` 时，`Lambda_R(A)=R-1`，得到点相位均值偏差的显式下界。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 short-arc/phase-mean 黑箱变成 quotient arc Fourier/PDEC cap，外加孤立 singleton 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 quotient arc Fourier/PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 short-arc cluster 与 phase-cycle actual-mean cap 统一为相位圆上的非平凡 Fourier 证书。",
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
