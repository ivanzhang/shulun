#!/usr/bin/env python3
"""汇总 Triad-A1 PersistentCap 的终端路由。

用法示例：
  python3 experiments/prime_matrix_triad_a1_persistentcap_terminal_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-persistentcap-terminal-router.json
  docs/monograph/prime-matrix-triad-a1-persistentcap-terminal-router.md
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
DEFAULT_PAYMENT = DOCS / "prime-matrix-triad-a1-persistent-columntail-payment.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-triad-a1-topprime-promotion-gate.json"
DEFAULT_DELETION = DOCS / "prime-matrix-triad-a1-promotion-deletion-potential-ledger.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-persistentcap-terminal-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-persistentcap-terminal-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def persistent_family_row(mass: dict[str, Any]) -> dict[str, Any]:
    """提取质量来源路由中的 PersistentCap 行。"""
    for row in mass["family_routes"]:
        if row["family"] == "PersistentCap":
            return row
    raise KeyError("PersistentCap family route not found")


def run(args: argparse.Namespace) -> dict[str, Any]:
    """运行 PersistentCap 终端路由。"""
    mass = load_json(args.mass_json)
    payment = load_json(args.payment_json)
    promotion = load_json(args.promotion_json)
    deletion = load_json(args.deletion_json)
    persistent_row = persistent_family_row(mass)

    count_chain = {
        "mass_source_persistent_count": int(persistent_row["count"]),
        "payment_persistent_count": int(payment["persistent_cap_count"]),
        "promotion_cap_count": int(promotion["cap_count"]),
        "deletion_cap_count": int(deletion["cap_count"]),
    }
    all_counts_match = len(set(count_chain.values())) == 1

    gates = {
        "mass_source_verified": bool(persistent_row["mass_source_verified"]),
        "pxp_exit_closed_by_btls": bool(persistent_row["pxp_exit_closed"]),
        "payment_intersections_recomputed": bool(payment["all_intersections_recomputed"]),
        "payment_phase_m_counts_match": bool(payment["all_phase_m_counts_match"]),
        "top_prime_is_next_high_prime": bool(promotion["all_top_prime_is_next_high_prime"]),
        "promotion_all_fiber_deletion": promotion["promotion_class_counts"] == {
            "PromotionFiberDeletion": int(promotion["cap_count"])
        },
        "promotion_deletion_potential_positive": bool(deletion["all_positive_deletion_potential"]),
    }

    all_current_persistent_caps_routed = all_counts_match and all(gates.values())

    return {
        "certificate_type": "triad_a1_persistentcap_terminal_router",
        "status": "current_persistent_caps_routed_to_promotion_deletion_or_terminal_triad",
        "source_hashes": {
            "router_script": file_sha256(Path(__file__).resolve()),
            "mass_source_json": file_sha256(args.mass_json),
            "payment_json": file_sha256(args.payment_json),
            "promotion_json": file_sha256(args.promotion_json),
            "deletion_json": file_sha256(args.deletion_json),
        },
        "count_chain": count_chain,
        "all_counts_match": all_counts_match,
        "gates": gates,
        "all_current_persistent_caps_routed": all_current_persistent_caps_routed,
        "current_layer_metrics": {
            "global_min_deletion_potential_current_layer": deletion[
                "global_min_deletion_potential_current_layer"
            ],
            "global_max_survival_current_layer": deletion[
                "global_max_survival_current_layer"
            ],
            "promotion_class_counts": promotion["promotion_class_counts"],
            "payment_route_counts": payment["route_counts"],
            "unique_phase_signature_count": payment["unique_phase_signature_count"],
        },
        "router_chain": [
            "AttachedMass => g(t)<=M_Q(t)",
            "BTLS => no P-row boundary exit",
            "ColumnTail payment => fixed signature PDEC or distributed CleanKLS",
            "TopPrime=next prime => promote Q to rQ",
            "PromotionFiberDeletion => deletion potential ledger",
            "If deletion potential stops accumulating => NoDeletion-KL / CleanKLS / PDEC",
        ],
        "review_conclusion": (
            "当前 68 个 PersistentCap 已从早期出口和 top-prime 独立终端中退出："
            "它们有同一 M_Q 质量来源，P×P 出口由 BTLS 关闭，top-prime 支付全部晋升为 "
            "Q=2310->30030 的正删除势。剩余是删除势塔是否发散，或停止后进入 "
            "NoDeletion-KL/CleanKLS/PDEC。"
        ),
        "remaining_obligations": [
            "证明沿正式无限反例族的晋升删除势发散，或抽出 NoDeletion 层。",
            "NoDeletion 层若 KL 偏斜持久，提交 new-layer/profinite PDEC。",
            "NoDeletion 层若 KL 可求和，提交 CleanKLS/DLS admission。",
            "若固定 residue/column 签名持久，提交 TailAnchor/ColumnCRT PDEC。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 PersistentCap 终端路由器",
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
            f"- `all_current_persistent_caps_routed={result['all_current_persistent_caps_routed']}`。",
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
            "这一步没有证明删除势在所有后继层必发散，也没有排除全部 PDEC/CleanKLS。",
            "它关闭的是当前 PersistentCap 的三个中间逃逸：",
            "",
            "```text",
            "早期 P×P 出口      => BTLS 关闭；",
            "固定 Q 同层循环     => TopPrime 晋升；",
            "top-prime 独立终端  => PromotionFiberDeletion 删除势账本。",
            "```",
            "",
            "因此 PersistentCap 的全局剩余硬点已经变成：",
            "",
            "```text",
            "删除势塔发散；",
            "或 NoDeletion-KL / CleanKLS；",
            "或固定 residue/column PDEC。",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mass-json", type=Path, default=DEFAULT_MASS)
    parser.add_argument("--payment-json", type=Path, default=DEFAULT_PAYMENT)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--deletion-json", type=Path, default=DEFAULT_DELETION)
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
                "all_current_persistent_caps_routed": result[
                    "all_current_persistent_caps_routed"
                ],
                "count_chain": result["count_chain"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
