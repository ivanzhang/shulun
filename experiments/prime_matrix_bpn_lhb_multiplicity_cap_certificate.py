#!/usr/bin/env python3
"""生成 H4-PDEC LHB 的 Q=2310 多重度容量证书。

用法示例：
  python3 experiments/prime_matrix_bpn_lhb_multiplicity_cap_certificate.py
  python3 experiments/prime_matrix_bpn_lhb_multiplicity_cap_certificate.py --p-values 43,47

输出：
  docs/monograph/h4-pdec-lhb-multiplicity-cap-certificate.json
  docs/monograph/h4-pdec-lhb-multiplicity-cap-certificate.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import prod
from pathlib import Path
from typing import Any

from prime_matrix_bpn_low_hole_bucket_capacity import (
    high_completion_stats,
    low_holes_for_phase,
    primes_upto,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_PHASE_BLOCKS = DOCS / "h4-pdec-lhb-column-phase-blocks.json"


def parse_p_values(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
    return [int(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256，作为证书来源指纹。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes(phase_blocks_path: Path) -> dict[str, str]:
    """登记本证书依赖的脚本与输入文件指纹。"""
    return {
        "multiplicity_cap_script": file_sha256(Path(__file__).resolve()),
        "capacity_script": file_sha256(
            ROOT / "experiments" / "prime_matrix_bpn_low_hole_bucket_capacity.py"
        ),
        "phase_blocks_json": file_sha256(phase_blocks_path),
    }


def load_phase_blocks(path: Path) -> dict[tuple[int, str], dict[str, Any]]:
    """读取已物化相位块，按 `(p, block_name)` 建索引。"""
    data = json.loads(path.read_text(encoding="utf-8"))
    rows: dict[tuple[int, str], dict[str, Any]] = {}
    for row in data["rows"]:
        rows[(row["p"], row["phase_block_name"])] = row
    return rows


def m_vector_for_prime(p: int, q: int) -> dict[str, Any]:
    """计算同一 `(p,Q)` 下的逐相位 LHB 允许全集投影计数 `M(t)`。"""
    base_primes = primes_upto(p - 1)
    if prod(base_primes) % q != 0:
        raise ValueError(f"q={q} 不整除 P={p} 的根基 CRT 周期")
    low_primes = [prime for prime in base_primes if q % prime == 0]
    high_primes = [prime for prime in base_primes if q % prime != 0]

    m_vector: list[int] = []
    low_hole_counts: list[int] = []
    for phase in range(q):
        holes = low_holes_for_phase(p, q, low_primes, phase)
        stats = high_completion_stats(p, q, phase, holes, high_primes)
        m_vector.append(int(stats["completion_count"]))
        low_hole_counts.append(len(holes))

    nonzero_entries = [
        {"phase": phase, "M": value, "low_holes": low_hole_counts[phase]}
        for phase, value in enumerate(m_vector)
        if value
    ]
    return {
        "p": p,
        "q": q,
        "base_primes": base_primes,
        "low_primes": low_primes,
        "high_primes": high_primes,
        "high_period": prod(high_primes) if high_primes else 1,
        "m_vector": m_vector,
        "nonzero_m_entries": nonzero_entries,
        "nonzero_m_phase_count": len(nonzero_entries),
        "total_allowed_rows": sum(m_vector),
        "max_m": max(m_vector, default=0),
    }


def capacity_row(
    p: int,
    q: int,
    block_name: str,
    phase_block: list[int],
    m_vector: list[int],
) -> dict[str, Any]:
    """把支撑相位块升级为 `sum_C g(t)<=sum_C M(t)` 行。"""
    bound = sum(m_vector[phase] for phase in phase_block)
    row_key = {
        "whole_deficit_phases": "WHOLEDEF",
        "bridged_critical_phases": "BRIDGED",
    }[block_name]
    return {
        "row_id": f"CC-LHB-{row_key}-MULT-Q{q}-P{p}",
        "p": p,
        "q": q,
        "phase_block_name": block_name,
        "phase_block_size": len(phase_block),
        "bound": bound,
        "inequality": "sum_{t in phase_block} g(t) <= sum_{t in phase_block} M(t)",
        "source_type": "FiniteMultiplicityCap",
        "admissibility": "A-ready-for-LHB-allowed-set-after-M-vector",
        "projection_condition": "requires S subset Z_LHB(p,Q)",
        "all_phases_have_zero_m": all(m_vector[phase] == 0 for phase in phase_block),
        "pass": bound == 0,
        "note": (
            "bound 来自同一 (p,Q) 下高层 CRT 补洞完成数 M(t)。"
            "该行对 LHB 允许全集投影有效；进入全局 PDEC 仍需证明 S subset Z_LHB。"
        ),
    }


def run(p_values: list[int], q: int, phase_blocks_path: Path) -> dict[str, Any]:
    """运行多重度容量证书生成。"""
    phase_blocks = load_phase_blocks(phase_blocks_path)
    prime_results: list[dict[str, Any]] = []
    rows: list[dict[str, Any]] = []
    for p in p_values:
        m_result = m_vector_for_prime(p, q)
        p_rows: list[dict[str, Any]] = []
        for block_name in ("whole_deficit_phases", "bridged_critical_phases"):
            source_row = phase_blocks[(p, block_name)]
            cap_row = capacity_row(
                p=p,
                q=q,
                block_name=block_name,
                phase_block=source_row["phase_block"],
                m_vector=m_result["m_vector"],
            )
            p_rows.append(cap_row)
            rows.append(cap_row)
        prime_results.append({**m_result, "capacity_rows": p_rows})

    return {
        "certificate_type": "h4_pdec_lhb_multiplicity_cap_certificate",
        "status": "q2310_lhb_multiplicity_caps_materialized_for_allowed_set",
        "q": q,
        "p_values": p_values,
        "source_hashes": source_hashes(phase_blocks_path),
        "interpretation": (
            "M(t) 是 LHB 允许全集 Z_LHB(p,Q) 在相位 t 上的投影计数，即高层 CRT "
            "补洞完成数。若正式坏窗集合 S 已证明包含于 Z_LHB，则 g(t)<=M(t)。"
        ),
        "rows": rows,
        "prime_results": prime_results,
        "all_support_rows_zero_bound": all(row["pass"] for row in rows),
        "review_conclusion": (
            "WHOLEDEF/BRIDGED 支撑相位已配套同一 Q=2310 的 M(t) 投影容量。"
            "在 LHB allowed-set 分支中这些支撑块给出 bound=0 的容量行；"
            "全局 PDEC 仍需单独证明当前 S subset Z_LHB。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写审稿摘要 Markdown；完整 `M(t)` 保存在 JSON。"""
    lines = [
        "# H4-PDEC Q=2310 LHB 多重度容量证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 证书语义",
        "",
        result["interpretation"],
        "",
        "本证书使用 `M(t)=completion_count(t)`。因此对任意已证明 `S subset Z_LHB(p,Q)` 的坏窗族，",
        "",
        "\\[",
        "g(t)\\le M(t)",
        "\\]",
        "",
        "逐相位成立。注意：这不是全局 PDEC 排除证明；它只物化 LHB allowed-set 投影容量。",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. `M(t)` 汇总",
            "",
            "| P | high primes | total allowed rows | nonzero M phases | max M |",
            "| ---: | --- | ---: | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        lines.append(
            "| {p} | `{high}` | {total} | {nonzero} | {max_m} |".format(
                p=item["p"],
                high=item["high_primes"],
                total=item["total_allowed_rows"],
                nonzero=item["nonzero_m_phase_count"],
                max_m=item["max_m"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 升级容量行",
            "",
            "| row_id | block | phase count | bound | all M=0 | pass |",
            "| --- | --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{row_id}` | `{block}` | {size} | {bound} | `{zero}` | `{passed}` |".format(
                row_id=row["row_id"],
                block=row["phase_block_name"],
                size=row["phase_block_size"],
                bound=row["bound"],
                zero=row["all_phases_have_zero_m"],
                passed=row["pass"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 审稿边界",
            "",
            "- 本证书把 `WHOLEDEF/BRIDGED` 的容量界从支撑大小替换为 `sum_C M(t)`。",
            "- 本轮全部升级行均满足 `bound=0`，因为这些相位块位于 `completion_count(t)=0` 的支撑内。",
            "- 这些行的正式使用条件是 `S subset Z_LHB(p,Q)`；没有该包含关系时不能用于任意 PDEC 坏窗集合。",
            "- 本证书仍是有限 `Q=2310`、有限 `P` 范围证书，不推广到无限族。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-values", default="13,17,19,23,29,31,37,43,47")
    parser.add_argument("--q", type=int, default=2310)
    parser.add_argument("--phase-blocks", type=Path, default=DEFAULT_PHASE_BLOCKS)
    parser.add_argument(
        "--json-output",
        type=Path,
        default=DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json",
    )
    parser.add_argument(
        "--md-output",
        type=Path,
        default=DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.md",
    )
    args = parser.parse_args()
    result = run(parse_p_values(args.p_values), args.q, args.phase_blocks)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
