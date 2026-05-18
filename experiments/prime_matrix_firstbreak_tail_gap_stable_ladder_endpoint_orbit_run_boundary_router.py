#!/usr/bin/env python3
"""生成 stable ladder endpoint orbit run/boundary 归约证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_run_boundary_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-orbit-run-boundary-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-endpoint-displacement-orbit-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAEOrEndpointTranslationOrbitAdjacencyPDECCap"

IMPORT = "StableLadderEndpointTranslationOrbitAdjacencyImportedLedger"
SINGLETON = "StableLadderEndpointSingletonAtomSAECarriedForwardAfterOrbitRunLedger"
CYCLE_MODEL = "StableLadderEndpointOrbitSignedCycleModelLedger"
DYADIC_EDGE = "StableLadderEndpointOrbitDyadicEdgeCountLedger"
RUN_PARTITION = "StableLadderEndpointOrbitRunPartitionLedger"
RUN_IDENTITY = "StableLadderEndpointOrbitAdjacencyRunBoundaryIdentityLedger"
BUDGET_DICHOTOMY = "StableLadderEndpointOrbitRunBoundaryBudgetDichotomyLedger"
LONG_ARC = "StableLadderEndpointOrbitLongSameSignArcRegistrationLedger"
BOUNDARY = "StableLadderEndpointOrbitBoundaryFluxRegistrationLedger"
NO_ANON = "NoAnonymousEndpointTranslationOrbitAdjacencyExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterOrbitRunBoundaryLedger"
NEW_TARGET = (
    "SparseScaleLadderSAESummabilityOrStableLadderEndpointSingletonAtomSAE"
    "OrEndpointOrbitLongSameSignArcSAEOrEndpointOrbitBoundaryFluxPDECCap"
)

REDUCED_TARGET = (
    f"{IMPORT} AND {SINGLETON} AND {CYCLE_MODEL} AND {DYADIC_EDGE} "
    f"AND {RUN_PARTITION} AND {RUN_IDENTITY} AND {BUDGET_DICHOTOMY} "
    f"AND {LONG_ARC} AND {BOUNDARY} AND {NO_ANON} AND {SPARSE} "
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
    """把旧活动基中的 orbit adjacency 硬点替换成 run/boundary 接口。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 endpoint orbit run/boundary 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableLadderEndpointTranslationOrbitAdjacencyImported",
            imported,
            False,
            "上一层剩余含 endpoint singleton atom、translation orbit adjacency 或 sparse SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderEndpointSingletonAtomSAECarriedForwardAfterOrbitRun",
            True,
            False,
            "endpoint singleton atom/SAE 继续前传；本步不证明单点族全局可求和。",
            SINGLETON,
        ),
        row(
            "StableLadderEndpointOrbitSignedCycleModel",
            True,
            True,
            "单个平移轨道被写成 C_r=Z/rZ 上的 signed active sequence。",
            CYCLE_MODEL,
        ),
        row(
            "StableLadderEndpointOrbitDyadicEdgeCount",
            True,
            True,
            "dyadic 权重给出 lambda^2 E <= W <= 4 lambda^2 E，把加权邻接质量换成边数。",
            DYADIC_EDGE,
        ),
        row(
            "StableLadderEndpointOrbitRunPartition",
            True,
            True,
            "active 同号相邻点被唯一分解为极大循环 runs，切口来自空位或符号变化。",
            RUN_PARTITION,
        ),
        row(
            "StableLadderEndpointOrbitAdjacencyRunBoundaryIdentity",
            True,
            True,
            "除全周期同号特例外，同号邻接边数 E=n-b；全周期同号直接登记为长弧。",
            RUN_IDENTITY,
        ),
        row(
            "StableLadderEndpointOrbitRunBoundaryBudgetDichotomy",
            True,
            True,
            "对任意边界预算 B，若 b>B 则边界通量出口；若 b<=B 且 E>0，则存在长度至少 E/B 的同号弧。",
            BUDGET_DICHOTOMY,
        ),
        row(
            "StableLadderEndpointOrbitLongSameSignArcRegistration",
            True,
            False,
            "长同号弧已成为显式出口；本步不证明其 SAE 或排斥。",
            LONG_ARC,
        ),
        row(
            "StableLadderEndpointOrbitBoundaryFluxRegistration",
            True,
            False,
            "高切口/边界通量已成为显式出口；本步不证明其 PDEC cap。",
            BOUNDARY,
        ),
        row(
            "NoAnonymousEndpointTranslationOrbitAdjacencyExit",
            True,
            True,
            "抽象 translation orbit adjacency 被压成长同号弧或边界通量二分。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterOrbitRunBoundary",
            True,
            False,
            "sparse scale-ladder SAE 继续前传；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "EndpointOrbitRunBoundaryCapStillOpen",
            False,
            False,
            "仍未排斥 endpoint singleton atom/SAE、long same-sign arc SAE 或 boundary flux PDEC/cap。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需关闭 singleton、long-arc、boundary-flux 或 sparse SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 endpoint orbit run/boundary 证书。"""
    previous = load_json(PREVIOUS_CERT)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "endpoint translation orbit adjacency 可在单个循环轨道 C_r 上转成 signed active sequence。"
        "在 dyadic packet 内，加权邻接质量 W 与同号邻接边数 E 等价到常数因子。"
        "把 active 同号相邻点分解为极大 runs；除全周期同号特例外，有 E=n-b，"
        "其中 n 是 active 点数，b 是切口数。于是对任意边界预算 B，"
        "要么 b>B 形成边界通量出口，要么存在长度至少 E/B 的同号连续弧。"
        "剩余不再是匿名轨道邻接，而是长同号弧 SAE 或边界通量 PDEC/cap。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_endpoint_orbit_run_boundary_router",
        "status": "endpoint_translation_orbit_adjacency_reduced_to_run_or_boundary_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "endpoint_translation_orbit_adjacency_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "endpoint_singleton_atom_sae_carried_forward": True,
        "endpoint_orbit_signed_cycle_model_closed": True,
        "endpoint_orbit_dyadic_edge_count_closed": True,
        "endpoint_orbit_run_partition_closed": True,
        "endpoint_orbit_adjacency_run_boundary_identity_closed": True,
        "endpoint_orbit_run_boundary_budget_dichotomy_closed": True,
        "endpoint_orbit_long_same_sign_arc_registered": True,
        "endpoint_orbit_boundary_flux_registered": True,
        "anonymous_endpoint_translation_orbit_adjacency_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "endpoint_singleton_atom_sae_proved": False,
        "endpoint_orbit_long_same_sign_arc_sae_proved": False,
        "endpoint_orbit_boundary_flux_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "run_boundary_formulas": {
            "cycle": "C_r=Z/rZ, z_t=a+t*delta",
            "active_sequence": "u_t=1_{z_t in S}, sigma_t=sign F(z_t)",
            "same_sign_edge": "e_t=1 iff u_t=u_{t+1}=1 and sigma_t=sigma_{t+1}",
            "weighted_to_unweighted": "lambda^2 E <= W <= 4 lambda^2 E on a dyadic packet",
            "run_partition": "runs are maximal cyclic intervals with u_t=1 and constant sigma_t",
            "run_identity": "unless the whole cycle is one same-sign run, E=n-b",
            "full_cycle_exception": "whole cycle same-sign => long same-sign arc of length r",
            "budget_dichotomy": "for any B>=1: b>B or L_max>=E/B",
            "new_exits": "EndpointOrbitLongSameSignArcSAE or EndpointOrbitBoundaryFluxPDECCap",
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
        "# Prime Matrix stable-ladder endpoint orbit run/boundary 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"endpoint_translation_orbit_adjacency_imported={fmt_bool(cert['endpoint_translation_orbit_adjacency_imported'])}",
        f"endpoint_singleton_atom_sae_carried_forward={fmt_bool(cert['endpoint_singleton_atom_sae_carried_forward'])}",
        f"endpoint_orbit_signed_cycle_model_closed={fmt_bool(cert['endpoint_orbit_signed_cycle_model_closed'])}",
        f"endpoint_orbit_dyadic_edge_count_closed={fmt_bool(cert['endpoint_orbit_dyadic_edge_count_closed'])}",
        f"endpoint_orbit_run_partition_closed={fmt_bool(cert['endpoint_orbit_run_partition_closed'])}",
        f"endpoint_orbit_adjacency_run_boundary_identity_closed={fmt_bool(cert['endpoint_orbit_adjacency_run_boundary_identity_closed'])}",
        f"endpoint_orbit_run_boundary_budget_dichotomy_closed={fmt_bool(cert['endpoint_orbit_run_boundary_budget_dichotomy_closed'])}",
        f"endpoint_orbit_long_same_sign_arc_registered={fmt_bool(cert['endpoint_orbit_long_same_sign_arc_registered'])}",
        f"endpoint_orbit_boundary_flux_registered={fmt_bool(cert['endpoint_orbit_boundary_flux_registered'])}",
        f"anonymous_endpoint_translation_orbit_adjacency_removed={fmt_bool(cert['anonymous_endpoint_translation_orbit_adjacency_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"endpoint_singleton_atom_sae_proved={fmt_bool(cert['endpoint_singleton_atom_sae_proved'])}",
        f"endpoint_orbit_long_same_sign_arc_sae_proved={fmt_bool(cert['endpoint_orbit_long_same_sign_arc_sae_proved'])}",
        f"endpoint_orbit_boundary_flux_pdec_cap_proved={fmt_bool(cert['endpoint_orbit_boundary_flux_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单轨道有符号循环模型",
        "",
        "上一层已经把 displacement autocorrelation 压到一个平移轨道。固定该轨道后写成：",
        "",
        "```text",
        "C_r=Z/rZ,",
        "z_t=a+t*delta.",
        "```",
        "",
        "在该轨道上记 `u_t=1_{z_t in S}`，并记 `sigma_t=sign F(z_t)`。同号邻接边为：",
        "",
        "```text",
        "e_t=1 iff u_t=u_{t+1}=1 and sigma_t=sigma_{t+1}.",
        "```",
        "",
        "## 2. dyadic 权重到边数",
        "",
        "因为这是上一层能量包留下的 dyadic adjacency packet，可取一个尺度 `lambda` 使 active 点满足 `lambda <= |F_t| < 2 lambda`。于是加权邻接质量 `W` 与同号边数 `E=sum e_t` 满足：",
        "",
        "```text",
        "lambda^2 E <= W <= 4 lambda^2 E.",
        "```",
        "",
        "所以 translation orbit adjacency cap 的容量部分可转写为同号邻接边数的下界。",
        "",
        "## 3. runs 与切口恒等式",
        "",
        "把 active 且同号连续的点分成极大循环 runs。切口来自两类位置：空位，或相邻 active 点符号变化。令：",
        "",
        "```text",
        "n = active 点数,",
        "b = run/cut 数,",
        "E = 同号邻接边数.",
        "```",
        "",
        "若整个周期不是一个同号 full-cycle run，则有精确恒等式：",
        "",
        "```text",
        "E = n - b.",
        "```",
        "",
        "若整个周期是一个同号 full-cycle run，则直接得到长度 `r` 的长同号弧出口。",
        "",
        "## 4. 边界预算二分",
        "",
        "对任意边界预算 `B>=1`，若 `b>B`，则进入 boundary flux 出口。否则 `b<=B`，由 pigeonhole 得到某个 run 的长度：",
        "",
        "```text",
        "L_max >= n/b >= E/B.",
        "```",
        "",
        "因此抽象的 endpoint translation orbit adjacency 被压成二分：",
        "",
        "```text",
        "EndpointOrbitLongSameSignArcSAE",
        "  OR EndpointOrbitBoundaryFluxPDECCap.",
        "```",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 endpoint translation orbit adjacency 变成长同号弧 SAE、边界通量 PDEC/cap，外加 endpoint singleton atom 与 sparse scale-ladder SAE 全局求和问题。",
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
            "- 本证书没有证明 EndpointOrbitLongSameSignArcSAE。",
            "- 本证书没有证明 EndpointOrbitBoundaryFluxPDECCap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把单轨道邻接 cap 压成长同号弧或边界通量二分。",
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
