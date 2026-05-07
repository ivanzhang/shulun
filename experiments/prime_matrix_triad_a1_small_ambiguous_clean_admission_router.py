#!/usr/bin/env python3
"""路由 APS 后的 small-ambiguous 分支到 FiberDeletion/PDEC/CleanKLS。

用法示例：
  python3 experiments/prime_matrix_triad_a1_small_ambiguous_clean_admission_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json
  docs/monograph/prime-matrix-triad-a1-small-ambiguous-clean-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_FORCED_SIGNATURE = DOCS / "prime-matrix-triad-a1-forced-gamma-signature-router.json"
DEFAULT_NODELETION_GATE = DOCS / "prime-matrix-triad-a1-nodeletion-kl-gate.json"
DEFAULT_NODELETION_WITNESS = DOCS / "prime-matrix-triad-a1-nodeletion-kl-witness-extractor.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-small-ambiguous-clean-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-small-ambiguous-clean-admission-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(
    forced_signature_path: Path,
    nodeletion_gate_path: Path,
    nodeletion_witness_path: Path,
) -> dict[str, Any]:
    """运行 small-ambiguous CleanKLS 准入路由。"""
    forced_signature = load_json(forced_signature_path)
    nodeletion_gate = load_json(nodeletion_gate_path)
    nodeletion_witness = load_json(nodeletion_witness_path)

    shape_counts = nodeletion_witness["shape_route_counts"]
    gate_counts = nodeletion_gate["gate_counts"]
    current_layers_delete = (
        not bool(nodeletion_gate["current_nodeletion_triggered"])
        and set(gate_counts) == {"FiberDeletion"}
    )
    if_nodeletion_pdec_shape = (
        set(shape_counts) == {"PhaseResidueMutualPDECWitness"}
        and int(nodeletion_witness["row_count"]) == int(
            shape_counts["PhaseResidueMutualPDECWitness"]
        )
    )
    clean_shape_currently_visible = any(
        "CleanKLS" in route for route in [*shape_counts.keys(), *gate_counts.keys()]
    )
    gates = {
        "small_ambiguous_gate_active": bool(
            forced_signature[
                "all_rows_routed_to_forced_signature_or_small_ambiguous_clean"
            ]
        ),
        "current_layers_delete_before_clean": current_layers_delete,
        "kl_chain_identity_exact": (
            float(nodeletion_witness["max_kl_chain_abs_error"]) <= 1e-12
        ),
        "if_nodeletion_then_phase_residue_pdec_witness": if_nodeletion_pdec_shape,
        "no_clean_shape_currently_visible": not clean_shape_currently_visible,
    }
    all_current_small_ambiguous_routed = bool(
        gates["small_ambiguous_gate_active"]
        and gates["kl_chain_identity_exact"]
        and (
            gates["current_layers_delete_before_clean"]
            or gates["if_nodeletion_then_phase_residue_pdec_witness"]
        )
    )
    return {
        "certificate_type": "triad_a1_small_ambiguous_clean_admission_router",
        "status": "small_ambiguous_branch_routed_before_clean_terminal",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "forced_gamma_signature_json": file_sha256(forced_signature_path),
            "nodeletion_kl_gate_json": file_sha256(nodeletion_gate_path),
            "nodeletion_kl_witness_json": file_sha256(nodeletion_witness_path),
        },
        "gates": gates,
        "all_current_small_ambiguous_routed": all_current_small_ambiguous_routed,
        "small_ambiguous_summary": {
            "global_max_ambiguous_gamma_share_upper_bound": float(
                forced_signature["global_max_ambiguous_gamma_share_upper_bound"]
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
        "nodeletion_summary": {
            "gate_counts": gate_counts,
            "shape_route_counts": shape_counts,
            "current_nodeletion_triggered": bool(
                nodeletion_gate["current_nodeletion_triggered"]
            ),
            "max_global_residue_normalized_kl": float(
                nodeletion_witness["max_global_residue_normalized_kl"]
            ),
            "min_phase_residue_mutual_normalized_kl": float(
                nodeletion_witness["min_phase_residue_mutual_normalized_kl"]
            ),
            "max_kl_chain_abs_error": float(
                nodeletion_witness["max_kl_chain_abs_error"]
            ),
        },
        "route": "CurrentLayerFiberDeletionOrNoDeletionPhaseResiduePDEC; CleanKLSOnlyAfterFlatNoDeletion",
        "structural_law": (
            "small-ambiguous 分支不能直接调用 CleanKLS。若新增层仍有 fiber deletion，则继续由删除势推进；"
            "若删除停止但 KL 或 phase-residue 互信息持久偏大，则回流 new-layer/refined PDEC；"
            "只有 deletion 停止且 KL/互信息同时趋平，才成为真正 CleanKLS/DLS 输入。"
        ),
        "review_conclusion": (
            "当前 APS small-ambiguous 分支尚未触发 clean 终端：已物化升层仍全部处于 FiberDeletion；"
            "同时 KL 形状账本显示，若把这些层视作 NoDeletion，偏斜也会以 phase-residue mutual PDEC witness 回流。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Small-Ambiguous CleanKLS 准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "small ambiguous residual",
        "  => FiberDeletion 继续推进；",
        "  or NoDeletion + KL/MI 偏斜 => refined/new-layer PDEC；",
        "  or NoDeletion + KL/MI flat => CleanKLS/DLS。",
        "```",
        "",
        "## 2. 门控",
        "",
    ]
    for key, value in result["gates"].items():
        lines.append(f"- `{key}={value}`。")
    lines.extend(
        [
            f"- `all_current_small_ambiguous_routed={result['all_current_small_ambiguous_routed']}`。",
            "",
            "## 3. Small-Ambiguous 汇总",
            "",
        ]
    )
    for key, value in result["small_ambiguous_summary"].items():
        lines.append(f"- `{key}={fmt_float(value)}`。")
    lines.extend(["", "## 4. NoDeletion/KL 汇总", ""])
    for key, value in result["nodeletion_summary"].items():
        if isinstance(value, float):
            lines.append(f"- `{key}={fmt_float(value)}`。")
        else:
            lines.append(f"- `{key}={value}`。")
    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            "当前层没有 clean KLS 终端输入。真正剩余证明义务是：若未来升层删除势停止，",
            "必须证明 KL/互信息平坦并提交 CleanKLS/DLS 证书；若不平坦，则自动回流 PDEC。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--forced-signature-json", type=Path, default=DEFAULT_FORCED_SIGNATURE)
    parser.add_argument("--nodeletion-gate-json", type=Path, default=DEFAULT_NODELETION_GATE)
    parser.add_argument(
        "--nodeletion-witness-json",
        type=Path,
        default=DEFAULT_NODELETION_WITNESS,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        forced_signature_path=args.forced_signature_json,
        nodeletion_gate_path=args.nodeletion_gate_json,
        nodeletion_witness_path=args.nodeletion_witness_json,
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
                "all_current_small_ambiguous_routed": result[
                    "all_current_small_ambiguous_routed"
                ],
                "gates": result["gates"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
