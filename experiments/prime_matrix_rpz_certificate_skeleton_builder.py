#!/usr/bin/env python3
"""生成 RPZ 出口证书骨架包。

用法示例：
  python3 experiments/prime_matrix_rpz_certificate_skeleton_builder.py

脚本读取两个已审计账本：

1. `prime-matrix-rpz-bcb-endpoint-phase-ledger.json`；
2. `prime-matrix-rpz-lower-descent-obstruction-ledger.json`。

输出统一证书骨架：

- `RPZ-SAE-FIN` 候选清单；
- `RPZ-PDEC` 相位行；
- `RPZ-ColumnCRT` 位移行待填接口。

该脚本只材料化证书义务，不证明这些出口已被排除。
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from prime_matrix_rpz_lower_descent_obstruction_ledger import transition_profile
from prime_matrix_zero_row_crt_audit import primes_upto


def endpoint_phase_key(phase: dict[str, Any]) -> tuple[int, int, int, int]:
    """端点失败相位键。"""
    return (
        phase["h"],
        phase["length_mod_h"],
        phase["left_residue_mod_h"],
        phase["endpoint_deficit"],
    )


def collect_endpoint_skeleton(endpoint: dict[str, Any]) -> dict[str, Any]:
    """从 BCB 端点账本抽取 SAE/PDEC/ColumnCRT 骨架。"""
    load: Counter[tuple[int, int, int, int]] = Counter()
    examples: dict[tuple[int, int, int, int], dict[str, Any]] = {}
    for record in endpoint["records"]:
        for phase in record["possible_failure_phases"]:
            key = endpoint_phase_key(phase)
            load[key] += 1
            examples.setdefault(
                key,
                {
                    "top_prime": record["top_prime"],
                    "top_zero_row": record["top_zero_row"],
                    "half_prime": record["half_prime"],
                    "length": record["length"],
                    "phase": phase,
                },
            )

    sae_candidates = []
    pdec_rows = []
    columncrt_rows = []
    for key, value in sorted(load.items()):
        h, length_mod_h, left_residue, endpoint_deficit = key
        phase_key = list(key)
        sae_candidates.append(
            {
                "source": "bcb_endpoint_possible_failure",
                "phase_key": phase_key,
                "formal_load_in_current_ledger": value,
                "example": examples[key],
                "required_certificate": [
                    "列出 carrying this phase 的正式坏窗族",
                    "逐窗给出 survivor/lift/higher-defect",
                    "若负载超过 SAE 阈值则转入 PDEC/ColumnCRT",
                ],
                "status": "candidate_not_closed",
            }
        )
        pdec_rows.append(
            {
                "source": "bcb_endpoint_possible_failure",
                "phase_type": "endpoint_grid_failure",
                "phase_key": phase_key,
                "Q": h,
                "S_tau_description": "all formal bad windows carrying this endpoint phase key",
                "S_tau_seed_residues": [left_residue],
                "F_tau_definition": "1_{S_tau}-|S_tau|/Q",
                "required_certificate": "fill U_CRT<L_PDEC or provide explicit finite certificate",
                "status": "skeleton_not_closed",
            }
        )
        columncrt_rows.append(
            {
                "source": "bcb_endpoint_possible_failure",
                "phase_key": phase_key,
                "h": h,
                "length_mod_h": length_mod_h,
                "left_residue_mod_h": left_residue,
                "endpoint_deficit": endpoint_deficit,
                "required_missing_inputs": [
                    "label selector lambda",
                    "same-column prime witness selector Pi",
                    "nonzero displacement residue a mod ell",
                    "load threshold L_D",
                ],
                "status": "skeleton_not_closed",
            }
        )

    return {
        "sae_candidates": sae_candidates,
        "pdec_rows": pdec_rows,
        "columncrt_rows": columncrt_rows,
    }


def collect_lower_descent_skeleton(descent: dict[str, Any]) -> dict[str, Any]:
    """枚举下层下降阻断相位并抽取 PDEC/ColumnCRT 骨架。"""
    max_prime = max(item["p"] for item in descent["transition_summaries"])
    primes = primes_upto(max_prime)
    failure_profiles = []
    grouped: dict[tuple[int, int, str], list[dict[str, Any]]] = defaultdict(list)

    for item in descent["transition_summaries"]:
        p = item["p"]
        r = item["r"]
        modulus = item["phase_modulus_primorial_r"]
        for residue in range(1, modulus + 1):
            profile = transition_profile(p, residue, primes)
            status = profile["status"]
            if status == "success":
                continue
            phase = {
                "p": p,
                "r": r,
                "phase_modulus_primorial_r": modulus,
                "row_phase_mod_primorial": residue % modulus,
                "row_mod_r": profile["row_mod_r"],
                "left_residue_mod_r": profile["left_residue_mod_r"],
                "delta_to_next_r_row": profile["delta_to_next_r_row"],
                "gap_p_minus_r": profile["gap_p_minus_r"],
                "puncture_active": profile["puncture_active"],
                "contained_previous_rows": profile["contained_previous_rows"],
                "blocked_previous_rows": profile["blocked_previous_rows"],
                "status": status,
            }
            failure_profiles.append(phase)
            grouped[(p, r, status)].append(phase)

    pdec_rows = []
    columncrt_rows = []
    for (p, r, status), phases in sorted(grouped.items()):
        modulus = phases[0]["phase_modulus_primorial_r"]
        residues = [phase["row_phase_mod_primorial"] for phase in phases]
        pdec_rows.append(
            {
                "source": "lower_descent_obstruction",
                "phase_type": status,
                "p": p,
                "r": r,
                "Q": modulus,
                "S_tau_size": len(residues),
                "S_tau_density": len(residues) / modulus,
                "S_tau_residues": residues,
                "F_tau_definition": "1_{S_tau}-|S_tau|/Q",
                "required_certificate": [
                    "证明正式下降路径避开该 S_tau",
                    "或证明该相位族满足 U_CRT<L_PDEC",
                    "或将同相持久负载送入 ColumnCRT",
                ],
                "status": "skeleton_not_closed",
            }
        )
        columncrt_rows.append(
            {
                "source": "lower_descent_obstruction",
                "phase_type": status,
                "p": p,
                "r": r,
                "Q": modulus,
                "S_tau_size": len(residues),
                "required_missing_inputs": [
                    "下降阻断相位到列标签 ell 的选择器",
                    "位移余类 a mod ell",
                    "同列见证选择器 Pi",
                    "负载阈值 L_D",
                ],
                "status": "skeleton_not_closed",
            }
        )

    status_counts = Counter(phase["status"] for phase in failure_profiles)
    return {
        "failure_profiles": failure_profiles,
        "pdec_rows": pdec_rows,
        "columncrt_rows": columncrt_rows,
        "summary": {
            "possible_failure_phase_count": len(failure_profiles),
            "possible_failure_status_counts": dict(sorted(status_counts.items())),
            "pdec_row_count": len(pdec_rows),
            "columncrt_row_count": len(columncrt_rows),
        },
    }


def build(endpoint_path: Path, descent_path: Path) -> dict[str, Any]:
    """构造统一证书骨架。"""
    endpoint = json.loads(endpoint_path.read_text(encoding="utf-8"))
    descent = json.loads(descent_path.read_text(encoding="utf-8"))
    endpoint_skeleton = collect_endpoint_skeleton(endpoint)
    descent_skeleton = collect_lower_descent_skeleton(descent)
    return {
        "status": "rpz_certificate_skeleton_package",
        "sources": {
            "endpoint": str(endpoint_path),
            "lower_descent": str(descent_path),
        },
        "summary": {
            "endpoint_sae_candidate_count": len(endpoint_skeleton["sae_candidates"]),
            "endpoint_pdec_row_count": len(endpoint_skeleton["pdec_rows"]),
            "endpoint_columncrt_row_count": len(endpoint_skeleton["columncrt_rows"]),
            "lower_possible_failure_phase_count": descent_skeleton["summary"][
                "possible_failure_phase_count"
            ],
            "lower_possible_failure_status_counts": descent_skeleton["summary"][
                "possible_failure_status_counts"
            ],
            "lower_pdec_row_count": descent_skeleton["summary"]["pdec_row_count"],
            "lower_columncrt_row_count": descent_skeleton["summary"][
                "columncrt_row_count"
            ],
        },
        "rpz_sae_fin_candidates": endpoint_skeleton["sae_candidates"],
        "rpz_pdec_rows": endpoint_skeleton["pdec_rows"]
        + descent_skeleton["pdec_rows"],
        "rpz_columncrt_rows": endpoint_skeleton["columncrt_rows"]
        + descent_skeleton["columncrt_rows"],
        "lower_descent_failure_profiles": descent_skeleton["failure_profiles"],
        "review_boundary": [
            "本包只把命名出口改写成证书待填行",
            "本包不排除 SAE/PDEC/ColumnCRT",
            "Prime Matrix 行命题仍不能据此升级为无条件定理",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书骨架报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ 出口证书骨架包",
        "",
        "**状态：** `rpz_certificate_skeleton_package`",
        "",
        "## 总结",
        "",
        f"- Endpoint SAE 候选数：`{summary['endpoint_sae_candidate_count']}`。",
        f"- Endpoint PDEC 行数：`{summary['endpoint_pdec_row_count']}`。",
        f"- Endpoint ColumnCRT 行数：`{summary['endpoint_columncrt_row_count']}`。",
        f"- LowerDescent 可能阻断相位数：`{summary['lower_possible_failure_phase_count']}`。",
        f"- LowerDescent 阻断状态计数：`{summary['lower_possible_failure_status_counts']}`。",
        f"- LowerDescent PDEC 行数：`{summary['lower_pdec_row_count']}`。",
        f"- LowerDescent ColumnCRT 行数：`{summary['lower_columncrt_row_count']}`。",
        "",
        "## RPZ-SAE-FIN 候选",
        "",
        "| source | phase key | ledger load | status |",
        "|---|---|---:|---|",
    ]
    for item in result["rpz_sae_fin_candidates"]:
        lines.append(
            "| {source} | `{key}` | {load} | {status} |".format(
                source=item["source"],
                key=item["phase_key"],
                load=item["formal_load_in_current_ledger"],
                status=item["status"],
            )
        )

    lines.extend(
        [
            "",
            "## RPZ-PDEC 相位行",
            "",
            "| source | type | Q | support size | status |",
            "|---|---|---:|---:|---|",
        ]
    )
    for item in result["rpz_pdec_rows"]:
        support_size = item.get("S_tau_size", len(item.get("S_tau_seed_residues", [])))
        lines.append(
            "| {source} | {kind} | {Q} | {support} | {status} |".format(
                source=item["source"],
                kind=item["phase_type"],
                Q=item["Q"],
                support=support_size,
                status=item["status"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿边界",
            "",
            "本包完成的是证书骨架材料化：所有已命名端点失败和下层下降阻断相位，都有明确的 `SAE/PDEC/ColumnCRT` 待填行。",
            "",
            "本包没有完成 `U_CRT<L_PDEC`、`SAE` 局部逃逸排斥、或 `ColumnCRT` 位移阈值证明；因此不能把 Prime Matrix 行命题升级为无条件定理。",
            "",
            "下一步最小硬点是：优先对 `endpoint` 的两个低负载相位填写 `RPZ-SAE-FIN`，同时对 `lower_descent_grid_fail` 三条 PDEC 行尝试证明正式下降路径避开其 `S_tau`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--endpoint",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger.json"),
    )
    parser.add_argument(
        "--descent",
        type=Path,
        default=Path(
            "docs/monograph/prime-matrix-rpz-lower-descent-obstruction-ledger.json"
        ),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-certificate-skeleton-package"),
    )
    args = parser.parse_args()
    result = build(args.endpoint, args.descent)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
