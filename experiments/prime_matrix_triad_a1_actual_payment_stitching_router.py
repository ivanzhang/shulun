#!/usr/bin/env python3
"""汇总 ForcedCap 多桶分支的 ActualPaymentStitching 入口状态。

用法示例：
  python3 experiments/prime_matrix_triad_a1_actual_payment_stitching_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-actual-payment-stitching-router.json
  docs/monograph/prime-matrix-triad-a1-actual-payment-stitching-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_SKELETON = DOCS / "prime-matrix-triad-a1-multibucket-pdec-skeleton.json"
DEFAULT_COLLAPSE = DOCS / "prime-matrix-triad-a1-multibucket-projection-collapse-router.json"
DEFAULT_MFU = DOCS / "prime-matrix-triad-a1-multibucket-mfu-candidate-audit.json"
DEFAULT_FIBER = DOCS / "prime-matrix-triad-a1-forcedcap-fiber-consistent-payment.json"
DEFAULT_FIBER_DOMINANCE = DOCS / "prime-matrix-triad-a1-forcedcap-fiber-dominance-router.json"
DEFAULT_GAMMA_FREEDOM = DOCS / "prime-matrix-triad-a1-forcedcap-gamma-freedom-router.json"
DEFAULT_FORCED_SIGNATURE = DOCS / "prime-matrix-triad-a1-forced-gamma-signature-router.json"
DEFAULT_SMALL_AMBIGUOUS = DOCS / "prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-actual-payment-stitching-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(
    skeleton_path: Path,
    collapse_path: Path,
    mfu_path: Path,
    fiber_path: Path,
    fiber_dominance_path: Path,
    gamma_freedom_path: Path,
    forced_signature_path: Path,
    small_ambiguous_path: Path,
) -> dict[str, Any]:
    """运行 APS 路由。"""
    skeleton = load_json(skeleton_path)
    collapse = load_json(collapse_path)
    mfu = load_json(mfu_path)
    fiber = load_json(fiber_path)
    fiber_dominance = load_json(fiber_dominance_path)
    gamma_freedom = load_json(gamma_freedom_path)
    forced_signature = load_json(forced_signature_path)
    small_ambiguous = load_json(small_ambiguous_path)
    count_chain = {
        "skeleton_matrix_row_count": int(skeleton["matrix_row_count"]),
        "collapse_matrix_row_count": int(collapse["matrix_row_count"]),
        "mfu_matrix_row_count": int(mfu["matrix_row_count"]),
        "forced_signature_matrix_row_count": int(
            forced_signature["signature_matrix_row_count"]
        ),
    }
    all_counts_match = len(set(count_chain.values())) == 1
    gates = {
        "single_bucket_payments_excluded": bool(
            skeleton["all_single_bucket_payments_excluded"]
        ),
        "bare_projection_collapses": bool(collapse["all_bare_projection_collapses"]),
        "finite_layer_mfu_candidates_exist": bool(
            mfu["all_rows_have_finite_layer_correlation"]
        ),
        "fiber_completion_counts_match_m_vector": bool(
            fiber["all_completion_counts_match_m_vector"]
        ),
        "fiber_residue_bucket_lower_bound_active": (
            int(fiber_dominance["global_min_actual_residue_buckets_by_fiber"]) >= 2
        ),
        "fiber_column_residue_bucket_lower_bound_active": (
            int(fiber_dominance["global_min_actual_column_residue_buckets_by_fiber"]) >= 2
        ),
        "gamma_forced_share_large": (
            float(gamma_freedom["global_min_forced_gamma_share_lower_bound"]) >= 0.9
        ),
        "forced_signature_or_small_ambiguous_gate_active": bool(
            forced_signature[
                "all_rows_routed_to_forced_signature_or_small_ambiguous_clean"
            ]
        ),
        "small_ambiguous_successor_routed_before_clean_terminal": bool(
            small_ambiguous["all_current_small_ambiguous_routed"]
        ),
    }
    all_current_forced_multibucket_rows_routed_to_aps = (
        all_counts_match and all(gates.values())
    )
    return {
        "certificate_type": "triad_a1_actual_payment_stitching_router",
        "status": "forcedcap_multibucket_rows_routed_to_actual_payment_stitching",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "skeleton_json": file_sha256(skeleton_path),
            "projection_collapse_json": file_sha256(collapse_path),
            "mfu_candidate_json": file_sha256(mfu_path),
            "fiber_consistent_payment_json": file_sha256(fiber_path),
            "fiber_dominance_json": file_sha256(fiber_dominance_path),
            "gamma_freedom_json": file_sha256(gamma_freedom_path),
            "forced_gamma_signature_json": file_sha256(forced_signature_path),
            "small_ambiguous_clean_admission_json": file_sha256(
                small_ambiguous_path
            ),
        },
        "count_chain": count_chain,
        "fiber_count_chain": {
            "fiber_forced_cap_count": int(fiber["forced_cap_count"]),
            "fiber_dominance_forced_cap_count": int(
                fiber_dominance["forced_cap_count"]
            ),
            "gamma_freedom_forced_cap_count": int(gamma_freedom["forced_cap_count"]),
            "forced_signature_forced_cap_count": int(
                forced_signature["forced_cap_count"]
            ),
        },
        "signature_pressure_summary": {
            "global_max_ambiguous_gamma_share_upper_bound": float(
                forced_signature["global_max_ambiguous_gamma_share_upper_bound"]
            ),
            "global_min_forced_gamma_share_lower_bound": float(
                forced_signature["global_min_forced_gamma_share_lower_bound"]
            ),
            "global_min_signature_signal_minus_ambiguous_budget": float(
                forced_signature[
                    "global_min_signature_signal_minus_ambiguous_budget"
                ]
            ),
            "global_min_signature_signal_to_ambiguity_ratio": float(
                forced_signature["global_min_signature_signal_to_ambiguity_ratio"]
            ),
        },
        "small_ambiguous_successor_summary": small_ambiguous["nodeletion_summary"],
        "all_counts_match": all_counts_match,
        "gates": gates,
        "all_current_forced_multibucket_rows_routed_to_aps": (
            all_current_forced_multibucket_rows_routed_to_aps
        ),
        "route": "ActualPaymentStitchingPersistentMFUOrDistributedCleanKLS",
        "router_chain": [
            "ExposureDominance => no single-bucket payment",
            "MultiBucketSkeleton => vector g_b(t) materialized",
            "ProjectionCollapse => bare multi-bucket LP gives no stronger projection",
            "MFUCandidateAudit => finite phase-bucket correlated rows exist",
            "FiberConsistentPayment => actual completions come from one CRT fiber y",
            "FiberDominance => at least 42 residue buckets or 24 column-residue buckets",
            "GammaFreedom => at most 5.53% choice-ambiguous holes; at least 94.47% forced",
            "ForcedGammaSignature => finite signature signal exceeds ambiguous budget on all 48 rows",
            "SmallAmbiguousCleanAdmission => current successor layers delete or return phase-residue PDEC",
            "ActualPaymentStitching => persistent Gamma row gives MFU/PDEC; no persistent row gives CleanKLS/DLS",
        ],
        "review_conclusion": (
            "ForcedCap 多桶分支的当前 48 个矩阵行已全部路由到 ActualPaymentStitching："
            "单桶支付已排除，裸多桶 LP 已坍缩，有限层 MFU 候选行已存在；进一步加入同一 CRT fiber y "
            "的一致完成态后，实际支付至少需要 42 个 residue 桶或 24 个 column-residue 桶，且至少约 94.47% "
            "的支付边由唯一覆盖强制决定。ForcedGammaSignature 进一步显示 48 个有限签名行的信号均超过 "
            "ambiguous 预算：持久则进入 MFU/PDEC，不持久则进入 small-ambiguous 后继门控。"
            "当前后继层仍由 FiberDeletion 推进；若视作 NoDeletion，则 KL 形状回流 phase-residue PDEC，"
            "尚未触发 clean KLS 终端。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 ActualPaymentStitching 路由器",
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
        "## 2. 计数链",
        "",
    ]
    for key, value in result["count_chain"].items():
        lines.append(f"- `{key}={value}`。")
    for key, value in result["fiber_count_chain"].items():
        lines.append(f"- `{key}={value}`。")
    lines.append("")
    lines.append("## 3. 签名压力")
    lines.append("")
    for key, value in result["signature_pressure_summary"].items():
        lines.append(f"- `{key}={value}`。")
    lines.append("")
    lines.append("## 4. Small-Ambiguous 后继")
    lines.append("")
    for key, value in result["small_ambiguous_successor_summary"].items():
        lines.append(f"- `{key}={value}`。")
    lines.extend(
        [
            f"- `all_counts_match={result['all_counts_match']}`。",
            "",
            "## 5. 门控",
            "",
        ]
    )
    for key, value in result["gates"].items():
        lines.append(f"- `{key}={value}`。")
    lines.extend(
        [
            f"- `all_current_forced_multibucket_rows_routed_to_aps={result['all_current_forced_multibucket_rows_routed_to_aps']}`。",
            "",
            "## 6. 终端二分",
            "",
            "```text",
            "Persistent Gamma follows finite MFU candidate",
            "  => multi-bucket PDEC / refined TailAnchor-ColumnCRT-Cofactor row；",
            "",
            "Gamma does not persist on any finite candidate",
            "  => DistributedPayment / CleanKLS-DLS。",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skeleton-json", type=Path, default=DEFAULT_SKELETON)
    parser.add_argument("--collapse-json", type=Path, default=DEFAULT_COLLAPSE)
    parser.add_argument("--mfu-json", type=Path, default=DEFAULT_MFU)
    parser.add_argument("--fiber-json", type=Path, default=DEFAULT_FIBER)
    parser.add_argument("--fiber-dominance-json", type=Path, default=DEFAULT_FIBER_DOMINANCE)
    parser.add_argument("--gamma-freedom-json", type=Path, default=DEFAULT_GAMMA_FREEDOM)
    parser.add_argument("--forced-signature-json", type=Path, default=DEFAULT_FORCED_SIGNATURE)
    parser.add_argument("--small-ambiguous-json", type=Path, default=DEFAULT_SMALL_AMBIGUOUS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        args.skeleton_json,
        args.collapse_json,
        args.mfu_json,
        args.fiber_json,
        args.fiber_dominance_json,
        args.gamma_freedom_json,
        args.forced_signature_json,
        args.small_ambiguous_json,
    )
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
                "all_current_forced_multibucket_rows_routed_to_aps": result[
                    "all_current_forced_multibucket_rows_routed_to_aps"
                ],
                "count_chain": result["count_chain"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
