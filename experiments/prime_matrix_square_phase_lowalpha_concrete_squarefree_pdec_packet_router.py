#!/usr/bin/env python3
"""从 Selberg 余项归因中抽取具体 squarefree PDEC 包。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_concrete_squarefree_pdec_packet_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-concrete-squarefree-pdec-packet-router.md"

DEFAULT_ABS_CONTRIBUTION = 20.0
NEXT_TARGET = "ConcreteSquarefreePDECExclusionOrCoefficientCancellationBound"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-selberg-remainder-attribution-router.json",
    "prime-matrix-square-phase-lowalpha-rough-b-squarefree-moduli-router.json",
]


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6f}"


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_concrete_squarefree_pdec_packet_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def packet_key(packet: dict[str, Any]) -> tuple[int, int]:
    """返回包排序键。"""
    return int(packet["z"]), int(packet["m"])


def audit(abs_contribution: float) -> dict[str, Any]:
    """从归因账本中抽取具体 PDEC 包。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    packets = []
    for row in source["rows"]:
        z = int(row["z"])
        for contribution in row["top_abs_contributions"]:
            if float(contribution["abs_contribution"]) < abs_contribution:
                continue
            packets.append(
                {
                    "z": z,
                    "m": int(contribution["m"]),
                    "coefficient": contribution["coefficient"],
                    "actual": contribution["actual"],
                    "expected": contribution["expected"],
                    "remainder": contribution["remainder"],
                    "contribution": contribution["contribution"],
                    "abs_contribution": contribution["abs_contribution"],
                    "actual_over_expected": contribution["actual_over_expected"],
                    "pdec_label": f"ConcreteSquarefreeLowModPDEC(z={z},m={int(contribution['m'])})",
                }
            )
    unique_moduli = sorted({packet["m"] for packet in packets})
    by_modulus: dict[int, dict[str, Any]] = {}
    for modulus in unique_moduli:
        entries = [packet for packet in packets if packet["m"] == modulus]
        by_modulus[modulus] = {
            "m": modulus,
            "z_values": sorted({entry["z"] for entry in entries}),
            "packet_count": len(entries),
            "total_abs_contribution": sum(float(entry["abs_contribution"]) for entry in entries),
            "max_abs_contribution": max(float(entry["abs_contribution"]) for entry in entries),
            "sample_packets": sorted(entries, key=lambda item: -float(item["abs_contribution"]))[:8],
        }
    top_moduli = sorted(by_modulus.values(), key=lambda item: -item["total_abs_contribution"])[:16]
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_concrete_squarefree_pdec_packet_router",
        "status": "concrete_squarefree_pdec_packets_extracted_exclusion_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "concrete_squarefree_pdec_packets_materialized": True,
        "coefficient_cancellation_bound_proved": False,
        "concrete_squarefree_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "abs_contribution_threshold": abs_contribution,
        "packet_count": len(packets),
        "unique_modulus_count": len(unique_moduli),
        "total_abs_contribution_in_packets": sum(float(packet["abs_contribution"]) for packet in packets),
        "top_packets": sorted(packets, key=lambda item: -float(item["abs_contribution"]))[:24],
        "top_moduli": top_moduli,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "Selberg 余项若不能由统一系数 L1 预算吸收，失败不再是抽象余项："
            "它必须落到具体的 squarefree 低模包 `ConcreteSquarefreeLowModPDEC(z,m)`。"
            "本路由从归因账本中抽取贡献量超过阈值的包，列出重复出现的模数和贡献方向。"
            "下一步可二选一：证明这些包的符号取消/系数预算，或逐个排斥具体 PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha concrete squarefree PDEC 包路由",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"concrete_squarefree_pdec_packets_materialized={fmt_bool(result['concrete_squarefree_pdec_packets_materialized'])}",
        f"coefficient_cancellation_bound_proved={fmt_bool(result['coefficient_cancellation_bound_proved'])}",
        f"concrete_squarefree_pdec_excluded={fmt_bool(result['concrete_squarefree_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 包总览",
        "",
        "| threshold | packets | unique m | total abs contribution |",
        "| ---: | ---: | ---: | ---: |",
        (
            f"| {fmt_float(result['abs_contribution_threshold'])} | {result['packet_count']} | "
            f"{result['unique_modulus_count']} | {fmt_float(result['total_abs_contribution_in_packets'])} |"
        ),
        "",
        "## 2. 最大贡献包",
        "",
        "| z | m | coefficient | actual | expected | remainder | contribution | actual/expected | label |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for packet in result["top_packets"]:
        lines.append(
            f"| {packet['z']} | {packet['m']} | {fmt_float(packet['coefficient'])} | "
            f"{packet['actual']} | {fmt_float(packet['expected'])} | "
            f"{fmt_float(packet['remainder'])} | {fmt_float(packet['contribution'])} | "
            f"{fmt_float(packet['actual_over_expected'])} | `{packet['pdec_label']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 重复模数",
            "",
            "| m | z values | packet count | total abs | max abs |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for item in result["top_moduli"]:
        lines.append(
            f"| {item['m']} | `{item['z_values']}` | {item['packet_count']} | "
            f"{fmt_float(item['total_abs_contribution'])} | {fmt_float(item['max_abs_contribution'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 证明边界",
            "",
            "- 已物化：Selberg 余项的具体 squarefree 低模 PDEC 包。",
            "- 未闭合：证明这些包按系数符号取消，或证明总系数 L1 预算。",
            "- 未闭合：逐个排斥持久 `ConcreteSquarefreeLowModPDEC(z,m)`。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--abs-contribution", type=float, default=DEFAULT_ABS_CONTRIBUTION)
    args = parser.parse_args()
    result = audit(args.abs_contribution)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "packet_count": result["packet_count"],
                "unique_modulus_count": result["unique_modulus_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
