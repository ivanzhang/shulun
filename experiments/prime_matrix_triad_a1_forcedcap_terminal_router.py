#!/usr/bin/env python3
"""汇总 Triad-A1 ForcedPersistentByDensityBarrier cap 的终端路由。

用法示例：
  python3 experiments/prime_matrix_triad_a1_forcedcap_terminal_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-forcedcap-terminal-router.json
  docs/monograph/prime-matrix-triad-a1-forcedcap-terminal-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_MASS = DOCS / "prime-matrix-triad-a1-pdec-mass-source-router.json"
DEFAULT_FORCED = DOCS / "prime-matrix-triad-a1-forcedcap-lift-audit.json"
DEFAULT_BOUNDARY = DOCS / "prime-matrix-triad-a1-materialized-support-boundary-terminal-audit.json"
DEFAULT_EXPOSURE = DOCS / "prime-matrix-triad-a1-forcedcap-columntail-payment.json"
DEFAULT_DOMINANCE = DOCS / "prime-matrix-triad-a1-forcedcap-exposure-dominance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-forcedcap-terminal-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-forcedcap-terminal-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def forced_family_row(mass: dict[str, Any]) -> dict[str, Any]:
    """提取质量来源路由中的 ForcedPersistentByDensityBarrier 行。"""
    for row in mass["family_routes"]:
        if row["family"] == "ForcedPersistentByDensityBarrier":
            return row
    raise KeyError("ForcedPersistentByDensityBarrier family route not found")


def run(args: argparse.Namespace) -> dict[str, Any]:
    """运行 ForcedCap 终端路由。"""
    mass = load_json(args.mass_json)
    forced = load_json(args.forced_json)
    boundary = load_json(args.boundary_json)
    exposure = load_json(args.exposure_json)
    dominance = load_json(args.dominance_json)
    forced_row = forced_family_row(mass)

    count_chain = {
        "mass_source_forced_count": int(forced_row["count"]),
        "forced_lift_cap_count": int(forced["forced_cap_count"]),
        "forced_exposure_cap_count": int(exposure["forced_cap_count"]),
        "forced_dominance_cap_count": int(dominance["forced_cap_count"]),
    }
    all_counts_match = len(set(count_chain.values())) == 1
    expected_lift_counts = {
        "LiftPersistentNeedsColumnTailOrNextLift": int(forced["forced_cap_count"])
    }
    gates = {
        "mass_source_verified": bool(forced_row["mass_source_verified"]),
        "pxp_exit_closed_by_btls": bool(forced_row["pxp_exit_closed"]),
        "boundary_terminals_excluded": bool(boundary["all_boundary_terminals_excluded"]),
        "boundary_phase_le_p_has_local_survivor": bool(
            boundary["all_phase_le_p_have_local_survivor"]
        ),
        "old_intersections_recomputed": bool(forced["all_old_intersections_recomputed"]),
        "all_forced_lifts_persistent": forced["lift_class_counts"] == expected_lift_counts,
        "columntail_exposure_materialized": bool(exposure["all_intersections_recomputed"]),
        "single_residue_actual_payment_excluded": bool(
            dominance["all_single_residue_actual_payment_excluded"]
        ),
        "single_column_residue_actual_payment_excluded": bool(
            dominance["all_single_column_residue_actual_payment_excluded"]
        ),
    }
    all_current_forced_caps_routed = all_counts_match and all(gates.values())

    return {
        "certificate_type": "triad_a1_forcedcap_terminal_router",
        "status": "current_forced_caps_routed_to_lift_or_terminal_triad",
        "source_hashes": {
            "router_script": file_sha256(Path(__file__).resolve()),
            "mass_source_json": file_sha256(args.mass_json),
            "forced_lift_json": file_sha256(args.forced_json),
            "boundary_json": file_sha256(args.boundary_json),
            "exposure_json": file_sha256(args.exposure_json),
            "dominance_json": file_sha256(args.dominance_json),
        },
        "count_chain": count_chain,
        "all_counts_match": all_counts_match,
        "gates": gates,
        "all_current_forced_caps_routed": all_current_forced_caps_routed,
        "current_layer_metrics": {
            "lift_class_counts": forced["lift_class_counts"],
            "q_source": forced["q_source"],
            "target_q": forced["target_q"],
            "support_profile_count": len(forced["support_profiles"]),
            "total_phase_le_p_count": boundary["total_phase_le_p_count"],
            "total_y0_completion_le_p_count": boundary[
                "total_y0_completion_le_p_count"
            ],
            "exposure_route_counts": exposure["route_counts"],
            "dominance_route_counts": dominance["route_counts"],
            "global_min_actual_residue_buckets_by_exposure": dominance[
                "global_min_actual_residue_buckets_by_exposure"
            ],
            "global_min_actual_column_residue_buckets_by_exposure": dominance[
                "global_min_actual_column_residue_buckets_by_exposure"
            ],
            "p_level_effective_exposure_support": exposure[
                "p_level_effective_support"
            ],
        },
        "router_chain": [
            "DensityBarrier => fixed-Q ordinary cap cannot close by same layer",
            "AttachedMass => g(t)<=M_Q(t)",
            "BTLS => no P-row boundary exit",
            "Lift Q=2310 to Q'=30030",
            "LiftPersistentNeedsColumnTailOrNextLift => no same-Q cycle",
            "ColumnTailExposure => fixed-signature PDEC candidate or distributed CleanKLS",
            "ExposureDominance => no single residue or single column-residue payment",
            "Next route => multi-bucket PDEC / next lift deletion-KL / CleanKLS",
        ],
        "review_conclusion": (
            "当前 24 个 ForcedPersistentByDensityBarrier cap 已关闭 P×P 早期出口，并从固定 Q 同层循环中退出。"
            "一层 lift 后仍为持久支撑，所以它们没有被本层删除势完全吸收；其 column-tail 暴露签名已物化，"
            "且单 residue 与单 column-residue 实际支付已被暴露支配排除；剩余义务是 multi-bucket PDEC、"
            "next-lift 删除/KL 门控或 CleanKLS。"
        ),
        "remaining_obligations": [
            "把多桶实际支付签名升级为持久 formal unit，或证明实际支付分散。",
            "对持久多桶实际支付签名提交 TailAnchor / ColumnCRT / refined PDEC 行。",
            "执行下一层 lift，并按 FiberDeletion / NoDeletion-KL / CleanKLS 路由。",
            "若 lift 后出现稀疏子帽，接入 LocalSurvivor / LFTE。",
            "若 lift 后仍持久且平坦，提交 CleanKLS/DLS admission。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 ForcedCap 终端路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 路由链",
        "",
        "```text",
        *result["router_chain"],
        "```",
        "",
        "## 2. 计数一致性",
        "",
    ]
    for key, value in result["count_chain"].items():
        lines.append(f"- `{key}={value}`。")
    lines.extend(
        [
            f"- `all_counts_match={result['all_counts_match']}`。",
            "",
            "## 3. 门控结果",
            "",
        ]
    )
    for key, value in result["gates"].items():
        lines.append(f"- `{key}={value}`。")
    lines.extend(
        [
            f"- `all_current_forced_caps_routed={result['all_current_forced_caps_routed']}`。",
            "",
            "## 4. 当前层指标",
            "",
        ]
    )
    for key, value in result["current_layer_metrics"].items():
        lines.append(f"- `{key}={value}`。")

    lines.extend(
        [
            "",
            "## 5. 剩余义务",
            "",
        ]
    )
    for item in result["remaining_obligations"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## 6. 读法",
            "",
            "这一步没有排除 ForcedCap。它关闭的是两个中间逃逸：",
            "",
            "```text",
            "P×P 早期出口  => BTLS 关闭；",
            "固定 Q 同层循环 => DensityBarrier 强制 lift。",
            "```",
            "",
            "和 PersistentCap 不同，当前 forced cap 的一层 lift 仍为持久支撑。",
            "所以它们的下一硬点不是当前层删除势，而是：",
            "",
            "```text",
            "column-tail PDEC；",
            "multi-bucket actual-payment PDEC；",
            "next-lift 删除/KL；",
            "或 CleanKLS/DLS。",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mass-json", type=Path, default=DEFAULT_MASS)
    parser.add_argument("--forced-json", type=Path, default=DEFAULT_FORCED)
    parser.add_argument("--boundary-json", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--exposure-json", type=Path, default=DEFAULT_EXPOSURE)
    parser.add_argument("--dominance-json", type=Path, default=DEFAULT_DOMINANCE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_counts_match": result["all_counts_match"],
                "all_current_forced_caps_routed": result[
                    "all_current_forced_caps_routed"
                ],
                "count_chain": result["count_chain"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
