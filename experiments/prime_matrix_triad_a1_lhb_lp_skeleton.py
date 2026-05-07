#!/usr/bin/env python3
"""生成 Triad-A1 的 Q=2310 LHB 分支 LP 骨架。

用法示例：
  python3 experiments/prime_matrix_triad_a1_lhb_lp_skeleton.py
  python3 experiments/prime_matrix_triad_a1_lhb_lp_skeleton.py --p-values 43,47

输出：
  docs/monograph/prime-matrix-triad-a1-lhb-lp-skeleton.json
  docs/monograph/prime-matrix-triad-a1-lhb-lp-skeleton.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_BLOCKS = DOCS / "h4-pdec-lhb-column-phase-blocks.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-lhb-lp-skeleton.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-lhb-lp-skeleton.md"


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析可选的逗号分隔 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def file_sha256(path: Path) -> str:
    """计算文件指纹，保证骨架来源可复核。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def index_phase_blocks(blocks: dict[str, Any]) -> dict[tuple[int, str], dict[str, Any]]:
    """按 `(p, phase_block_name)` 索引相位块。"""
    indexed: dict[tuple[int, str], dict[str, Any]] = {}
    for row in blocks["rows"]:
        indexed[(int(row["p"]), row["phase_block_name"])] = row
    return indexed


def source_hashes(mult_path: Path, blocks_path: Path) -> dict[str, str]:
    """登记输入与脚本指纹。"""
    return {
        "lp_skeleton_script": file_sha256(Path(__file__).resolve()),
        "multiplicity_cap_json": file_sha256(mult_path),
        "phase_blocks_json": file_sha256(blocks_path),
    }


def singleton_obstruction(m_vector: list[int]) -> dict[str, Any]:
    """给出 box-only 行不能强制 Fourier 抵消的最小见证。

    只要存在 M(t)>0 的相位，约束 `0<=g(t)<=M(t)` 就允许单相位质量。
    单相位质量对任意非零频率的 Fourier 模长等于其质量，因此 box-only 行本身
    不能推出稳定抵消；必须再加入方向支撑、列位移、尾锚或其他结构行。
    """
    for phase, value in enumerate(m_vector):
        if value > 0:
            return {
                "exists": True,
                "phase": phase,
                "available_multiplicity": value,
                "per_unit_fourier_abs": 1.0,
                "meaning": (
                    "仅 box 容量可行：g 可支撑在一个非零 M 相位上。"
                    "单靠 M(t) 上界不能推出 Fourier 抵消。"
                ),
            }
    return {
        "exists": False,
        "phase": None,
        "available_multiplicity": 0,
        "per_unit_fourier_abs": 0.0,
        "meaning": "M(t) is identically zero; this branch is empty.",
    }


def analyze_prime(
    item: dict[str, Any],
    phase_blocks: dict[tuple[int, str], dict[str, Any]],
) -> dict[str, Any]:
    """分析单个 P 的 LHB LP 骨架。"""
    p = int(item["p"])
    q = int(item["q"])
    m_vector = [int(value) for value in item["m_vector"]]
    zero_m = [phase for phase, value in enumerate(m_vector) if value == 0]
    nonzero_m = [phase for phase, value in enumerate(m_vector) if value > 0]

    block_reports = []
    for block_name in ("whole_deficit_phases", "bridged_critical_phases"):
        row = phase_blocks[(p, block_name)]
        phases = [int(phase) for phase in row["phase_block"]]
        bound = sum(m_vector[phase] for phase in phases)
        block_reports.append(
            {
                "block_name": block_name,
                "phase_count": len(phases),
                "bound_from_m": bound,
                "all_m_zero": all(m_vector[phase] == 0 for phase in phases),
                "row_status": "A-ready-zero-cap" if bound == 0 else "needs-dual-row",
            }
        )

    return {
        "p": p,
        "q": q,
        "row_generators": {
            "nonnegativity": "g(t)>=0 for all t",
            "phase_caps": "g(t)<=M_p(t) for all t",
            "zero_block_caps": "sum_{t in C} g(t)<=0 for WHOLEDEF/BRIDGED blocks",
            "mass": "0<=sum_t g(t)<=sum_t M_p(t); persistent lower mass must be supplied by theta",
        },
        "counts": {
            "phase_count": q,
            "phase_cap_rows": q,
            "zero_m_phase_count": len(zero_m),
            "nonzero_m_phase_count": len(nonzero_m),
            "total_allowed_rows": sum(m_vector),
            "max_m": max(m_vector, default=0),
        },
        "block_reports": block_reports,
        "box_only_obstruction": singleton_obstruction(m_vector),
            "closed_subbranch": (
            "若 PDEC 强制坏相位支撑包含于 WHOLEDEF union BRIDGED，"
            "则该 LHB 分支上的 S 质量为零。"
        ),
        "open_requirements": [
            "theta-specific persistent lower mass |S| or range",
            "direction support of F or cap set relative to M(t)",
            "column/tail/cofactor phase-compatible rows",
            "full direction-arc dual certificate U_CRT<L_PDEC",
        ],
    }


def build_skeleton(
    mult_path: Path,
    blocks_path: Path,
    p_filter: set[int] | None,
) -> dict[str, Any]:
    """构造完整 LP 骨架对象。"""
    mult = load_json(mult_path)
    blocks = load_json(blocks_path)
    phase_blocks = index_phase_blocks(blocks)

    prime_results = []
    for item in mult["prime_results"]:
        p = int(item["p"])
        if p_filter is not None and p not in p_filter:
            continue
        prime_results.append(analyze_prime(item, phase_blocks))

    return {
        "certificate_type": "triad_a1_lhb_lp_skeleton",
        "status": "lp_skeleton_materialized_dual_comparison_open",
        "q": int(mult["q"]),
        "p_values": [item["p"] for item in prime_results],
        "source_hashes": source_hashes(mult_path, blocks_path),
        "same_set_law": (
            "所有行都作用在同一个 LHB-typed 坏窗推前计数 g(t) 上。"
            "使用这些行必须先证明 S subset Z_LHB(p,Q)。"
        ),
        "prime_results": prime_results,
        "all_zero_blocks_ready": all(
            block["bound_from_m"] == 0
            for item in prime_results
            for block in item["block_reports"]
        ),
        "box_only_global_closure": False,
        "review_conclusion": (
            "LHB 分支现在已有机器可读的 g(t)<=M(t) 行生成器和 "
            "WHOLEDEF/BRIDGED 零容量行。这些行只能闭合强制支撑落在零容量块内的 "
            "PDEC 方向。由于仍存在非零 M 相位，仅靠 box 容量不能证明全局 Fourier "
            "抵消；下一证明义务是带有额外结构行的 theta 级 LP/对偶证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审稿摘要。"""
    lines = [
        f"# Triad-A1 Q={result['q']} LHB LP 骨架",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 证书语义",
        "",
        result["same_set_law"],
        "",
        "本骨架只生成同一 `g(t)` 上的合法行生成器；它不声称已经完成 `U_CRT<L_PDEC`。",
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
            "## 3. P 列表摘要",
            "",
            "| P | total M | nonzero M phases | zero M phases | max M | WHOLEDEF bound | BRIDGED bound | box-only obstruction |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["prime_results"]:
        blocks = {block["block_name"]: block for block in item["block_reports"]}
        obstruction = item["box_only_obstruction"]
        obs_text = (
            f"phase {obstruction['phase']} has M={obstruction['available_multiplicity']}"
            if obstruction["exists"]
            else "empty"
        )
        lines.append(
            "| {p} | {total} | {nonzero} | {zero} | {max_m} | {whole} | {bridged} | {obs} |".format(
                p=item["p"],
                total=item["counts"]["total_allowed_rows"],
                nonzero=item["counts"]["nonzero_m_phase_count"],
                zero=item["counts"]["zero_m_phase_count"],
                max_m=item["counts"]["max_m"],
                whole=blocks["whole_deficit_phases"]["bound_from_m"],
                bridged=blocks["bridged_critical_phases"]["bound_from_m"],
                obs=obs_text,
            )
        )

    lines.extend(
        [
            "",
            "## 4. 已闭合行",
            "",
            "对每个列出的 `P`，以下行已经可在 LHB-typed 且 `S subset Z_LHB` 的分支中使用：",
            "",
            "```text",
            "g(t)>=0；",
            "g(t)<=M_p(t)；",
            "sum_{t in WHOLEDEF} g(t)<=0；",
            "sum_{t in BRIDGED} g(t)<=0。",
            "```",
            "",
            "因此若某个 PDEC 方向强制坏相位完全落在 `WHOLEDEF union BRIDGED` 中，该分支直接空。",
            "",
            "## 5. 新发现的阻断点",
            "",
            "只靠 `g(t)<=M(t)` 不能推出全局 Fourier 抵消：只要存在 `M(t)>0`，单相位支撑就是 box-only 可行解，",
            "其非零频率 Fourier 模长等于质量本身。因此下一步不能继续调常数，必须补入以下结构行之一：",
            "",
            "```text",
            "PDEC 方向支撑相对 M(t) 的限制；",
            "column/displacement 相位兼容行；",
            "tail/cofactor nonreuse 行；",
            "direction-arc dual certificate。",
            "```",
            "",
            "## 6. 当前结论",
            "",
            "LHB 分支已经从文档骨架推进为机器可读 LP 骨架；但完整 `U_CRT<L_PDEC` 仍未提交。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--phase-blocks-json", type=Path, default=DEFAULT_BLOCKS)
    parser.add_argument("--p-values", default=None, help="可选逗号分隔 P 列表")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = build_skeleton(
        mult_path=args.multiplicity_json,
        blocks_path=args.phase_blocks_json,
        p_filter=parse_p_values(args.p_values),
    )
    args.json_out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps({"status": result["status"], "p_values": result["p_values"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
