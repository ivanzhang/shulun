#!/usr/bin/env python3
"""生成 RPZ endpoint SAE 有限证书。

用法示例：
  python3 experiments/prime_matrix_rpz_endpoint_sae_finite_certificate.py

该脚本只处理当前证书骨架中的 endpoint 低负载候选。它区分：

1. possible load：相位账本中可能导致端点网格失败的相位次数；
2. actual load：当前 BCB 审计中实际命中该失败相位的窗口次数。

若 actual load 为 0，则当前有限账本下的 SAE 候选窗口集为空，有限证书闭合；但这不是全局
SAE 排斥证明。若未来正式反例族命中该相位，仍必须进入 PDEC/ColumnCRT 或提交新的局部证书。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def phase_key(phase: dict[str, Any]) -> tuple[int, int, int, int]:
    """返回 endpoint 相位键。"""
    return (
        phase["h"],
        phase["length_mod_h"],
        phase["left_residue_mod_h"],
        phase["endpoint_deficit"],
    )


def build(skeleton_path: Path, endpoint_path: Path) -> dict[str, Any]:
    """构造 endpoint SAE 有限证书。"""
    skeleton = json.loads(skeleton_path.read_text(encoding="utf-8"))
    endpoint = json.loads(endpoint_path.read_text(encoding="utf-8"))
    records = endpoint["records"]
    certificates = []

    for candidate in skeleton["rpz_sae_fin_candidates"]:
        key = tuple(candidate["phase_key"])
        possible_carriers = []
        actual_carriers = []

        for record in records:
            for phase in record["possible_failure_phases"]:
                if phase_key(phase) == key:
                    possible_carriers.append(
                        {
                            "top_prime": record["top_prime"],
                            "top_zero_row": record["top_zero_row"],
                            "half_prime": record["half_prime"],
                            "forced_core_interval": record["forced_core_interval"],
                            "length": record["length"],
                            "phase": phase,
                        }
                    )
            if record["actual_grid_failure"] and phase_key(record["actual_phase"]) == key:
                actual_carriers.append(
                    {
                        "top_prime": record["top_prime"],
                        "top_zero_row": record["top_zero_row"],
                        "half_prime": record["half_prime"],
                        "forced_core_interval": record["forced_core_interval"],
                        "length": record["length"],
                        "actual_phase": record["actual_phase"],
                    }
                )

        if actual_carriers:
            verdict = "actual_windows_require_local_certificate"
            current_ledger_closed = False
        else:
            verdict = "vacuous_current_ledger_closed"
            current_ledger_closed = True

        certificates.append(
            {
                "phase_key": list(key),
                "possible_load_in_current_ledger": len(possible_carriers),
                "actual_load_in_current_ledger": len(actual_carriers),
                "candidate_windows": actual_carriers,
                "possible_phase_examples": possible_carriers,
                "local_state_verdict": verdict,
                "current_ledger_closed": current_ledger_closed,
                "global_status": "not_global_exclusion",
                "if_global_load_appears": [
                    "若负载低于 SAE 阈值，必须提交实际窗口 survivor/lift/higher-defect 证书",
                    "若同相位持久重复，进入 PDEC endpoint phase row",
                    "若携带列位移见证，进入 ColumnCRT endpoint displacement row",
                ],
            }
        )

    return {
        "status": "rpz_endpoint_sae_finite_certificate_current_ledger",
        "sources": {
            "skeleton": str(skeleton_path),
            "endpoint": str(endpoint_path),
        },
        "summary": {
            "candidate_count": len(certificates),
            "total_possible_load": sum(
                item["possible_load_in_current_ledger"] for item in certificates
            ),
            "total_actual_load": sum(
                item["actual_load_in_current_ledger"] for item in certificates
            ),
            "current_ledger_closed_count": sum(
                1 for item in certificates if item["current_ledger_closed"]
            ),
            "global_exclusion_closed": False,
        },
        "certificates": certificates,
        "review_boundary": [
            "当前有限 BCB endpoint SAE 候选全部实际空载",
            "这只闭合当前有限账本的 SAE-FIN 行",
            "全局 SAE/PDEC/ColumnCRT 出口仍未排除",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 证书报告。"""
    summary = result["summary"]
    lines = [
        "# RPZ Endpoint SAE 有限证书",
        "",
        "**状态：** `rpz_endpoint_sae_finite_certificate_current_ledger`",
        "",
        "## 总结",
        "",
        f"- SAE 候选相位数：`{summary['candidate_count']}`。",
        f"- 当前账本 possible load：`{summary['total_possible_load']}`。",
        f"- 当前账本 actual load：`{summary['total_actual_load']}`。",
        f"- 当前有限账本闭合相位数：`{summary['current_ledger_closed_count']}`。",
        f"- 全局出口是否闭合：`{summary['global_exclusion_closed']}`。",
        "",
        "## 证书表",
        "",
        "| phase key | possible load | actual load | current verdict | global status |",
        "|---|---:|---:|---|---|",
    ]
    for item in result["certificates"]:
        lines.append(
            "| `{key}` | {possible} | {actual} | {verdict} | {global_status} |".format(
                key=item["phase_key"],
                possible=item["possible_load_in_current_ledger"],
                actual=item["actual_load_in_current_ledger"],
                verdict=item["local_state_verdict"],
                global_status=item["global_status"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿解释",
            "",
            "两个 endpoint 低负载候选相位在可能失败相位账本中各出现一次，但当前 BCB 审计的实际相位没有命中它们；因此当前有限账本中的 `candidate_windows` 为空，`RPZ-SAE-FIN` 在当前账本层面真空闭合。",
            "",
            "这不是全局 `SAE` 排斥。若正式反例族在这些相位上产生实际窗口，必须逐窗给出 `survivor/lift/higher-defect`，或因同相持久进入 `PDEC/ColumnCRT`。",
            "",
            "下一步最小硬点应转向三条 `lower_descent_grid_fail` 相位行：证明正式下降路径避开对应 `S_tau`，或填写 `U_CRT<L_PDEC` / `ColumnCRT` 证书。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--skeleton",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-certificate-skeleton-package.json"),
    )
    parser.add_argument(
        "--endpoint",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-endpoint-phase-ledger.json"),
    )
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-endpoint-sae-finite-certificate"),
    )
    args = parser.parse_args()
    result = build(args.skeleton, args.endpoint)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
