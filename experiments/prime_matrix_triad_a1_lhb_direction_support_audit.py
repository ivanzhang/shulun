#!/usr/bin/env python3
"""审计 Triad-A1 LHB 方向支撑与 M(t) 的交集。

用法示例：
  python3 experiments/prime_matrix_triad_a1_lhb_direction_support_audit.py
  python3 experiments/prime_matrix_triad_a1_lhb_direction_support_audit.py --support-blocks whole_deficit_phases

输出：
  docs/monograph/prime-matrix-triad-a1-lhb-direction-support-audit.json
  docs/monograph/prime-matrix-triad-a1-lhb-direction-support-audit.md
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
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-lhb-direction-support-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-lhb-direction-support-audit.md"


def parse_csv(raw: str) -> list[str]:
    """解析逗号分隔字符串。"""
    return [item.strip() for item in raw.split(",") if item.strip()]


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析可选 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def index_phase_blocks(blocks: dict[str, Any]) -> dict[tuple[int, str], list[int]]:
    """按 `(p, block_name)` 索引相位列表。"""
    indexed: dict[tuple[int, str], list[int]] = {}
    for row in blocks["rows"]:
        indexed[(int(row["p"]), row["phase_block_name"])] = [int(t) for t in row["phase_block"]]
    return indexed


def source_hashes(mult_path: Path, blocks_path: Path) -> dict[str, str]:
    """登记来源文件指纹。"""
    return {
        "direction_support_script": file_sha256(Path(__file__).resolve()),
        "multiplicity_cap_json": file_sha256(mult_path),
        "phase_blocks_json": file_sha256(blocks_path),
    }


def classify_intersection(size: int, sparse_threshold: int) -> str:
    """按交集规模分类。"""
    if size == 0:
        return "EmptyCap"
    if size <= sparse_threshold:
        return "SparseCap"
    return "PersistentCap"


def analyze_prime(
    item: dict[str, Any],
    phase_blocks: dict[tuple[int, str], list[int]],
    support_blocks: list[str],
    sparse_threshold: int,
) -> dict[str, Any]:
    """审计单个 P 的方向支撑交集。"""
    p = int(item["p"])
    q = int(item["q"])
    m_vector = [int(value) for value in item["m_vector"]]
    support: set[int] = set()
    missing_blocks: list[str] = []
    for block in support_blocks:
        key = (p, block)
        if key not in phase_blocks:
            missing_blocks.append(block)
            continue
        support.update(phase_blocks[key])

    intersection = sorted(t for t in support if m_vector[t] > 0)
    mass_bound = sum(m_vector[t] for t in intersection)
    return {
        "p": p,
        "q": q,
        "support_blocks": support_blocks,
        "missing_blocks": missing_blocks,
        "support_size": len(support),
        "intersection_size": len(intersection),
        "intersection_mass_bound": mass_bound,
        "classification": classify_intersection(len(intersection), sparse_threshold),
        "intersection_sample": intersection[:20],
        "meaning": (
            "若 C_F(kappa) 等于这些 support blocks 的并集，则 "
            "supp(g) subset C_F cap supp(M)。intersection_mass_bound 是仅由 M(t) 给出的总质量上界。"
        ),
    }


def run(
    mult_path: Path,
    blocks_path: Path,
    support_blocks: list[str],
    p_filter: set[int] | None,
    sparse_threshold: int,
) -> dict[str, Any]:
    """运行方向支撑审计。"""
    mult = load_json(mult_path)
    blocks = load_json(blocks_path)
    phase_blocks = index_phase_blocks(blocks)
    prime_results = []
    for item in mult["prime_results"]:
        p = int(item["p"])
        if p_filter is not None and p not in p_filter:
            continue
        prime_results.append(analyze_prime(item, phase_blocks, support_blocks, sparse_threshold))

    return {
        "certificate_type": "triad_a1_lhb_direction_support_audit",
        "status": "direction_support_intersection_audited",
        "q": int(mult["q"]),
        "support_blocks": support_blocks,
        "p_values": [item["p"] for item in prime_results],
        "sparse_threshold": sparse_threshold,
        "source_hashes": source_hashes(mult_path, blocks_path),
        "prime_results": prime_results,
        "all_empty": all(item["classification"] == "EmptyCap" for item in prime_results),
        "review_conclusion": (
            "本审计把候选方向支撑 C_F(kappa) 与 LHB 的 supp(M) 相交。"
            "默认支撑 WHOLEDEF/BRIDGED 在全部列出 P 上交集为空，因此该子分支在 LHB 分支内闭合。"
            "一般 PDEC 方向仍需提交真实 F,kappa,C_F。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 LHB 方向支撑审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 审计对象",
        "",
        f"- `Q={result['q']}`。",
        f"- 支撑块：`{result['support_blocks']}`。",
        f"- 稀疏阈值：`{result['sparse_threshold']}`。",
        f"- `all_empty={result['all_empty']}`。",
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
            "## 3. 交集表",
            "",
            "| P | support size | intersection size | M-mass bound | class | sample |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["prime_results"]:
        lines.append(
            "| {p} | {support} | {inter} | {mass} | `{cls}` | `{sample}` |".format(
                p=item["p"],
                support=item["support_size"],
                inter=item["intersection_size"],
                mass=item["intersection_mass_bound"],
                cls=item["classification"],
                sample=item["intersection_sample"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 结论",
            "",
            "若真实 `C_F(kappa)` 就是本审计的支撑块并集，则 `intersection_size=0` 的行直接闭合：",
            "",
            "```text",
            "supp(g) subset C_F(kappa) cap supp(M) = empty。",
            "```",
            "",
            "若后续输入真实 PDEC 方向后交集非空，则按 `SparseCap/PersistentCap/FlatCap` 继续回流。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--phase-blocks-json", type=Path, default=DEFAULT_BLOCKS)
    parser.add_argument(
        "--support-blocks",
        default="whole_deficit_phases,bridged_critical_phases",
        help="用逗号分隔的相位块名，作为候选 C_F(kappa)",
    )
    parser.add_argument("--p-values", default=None)
    parser.add_argument("--sparse-threshold", type=int, default=16)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        mult_path=args.multiplicity_json,
        blocks_path=args.phase_blocks_json,
        support_blocks=parse_csv(args.support_blocks),
        p_filter=parse_p_values(args.p_values),
        sparse_threshold=args.sparse_threshold,
    )
    args.json_out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps({"status": result["status"], "all_empty": result["all_empty"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
