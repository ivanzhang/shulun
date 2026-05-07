#!/usr/bin/env python3
"""扫描 Triad-A1 LHB 分支中的 Fourier-cap 方向支撑。

用法示例：
  python3 experiments/prime_matrix_triad_a1_lhb_fourier_cap_scan.py
  python3 experiments/prime_matrix_triad_a1_lhb_fourier_cap_scan.py --alphas 0.5,0.9 --directions 0,0.25

输出：
  docs/monograph/prime-matrix-triad-a1-lhb-fourier-cap-scan.json
  docs/monograph/prime-matrix-triad-a1-lhb-fourier-cap-scan.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_MULT = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-lhb-fourier-cap-scan.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-lhb-fourier-cap-scan.md"


def parse_float_csv(raw: str) -> list[float]:
    """解析浮点数 CSV。"""
    return [float(item.strip()) for item in raw.split(",") if item.strip()]


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


def build_caps(q: int, alphas: list[float], directions: list[float]) -> dict[tuple[float, float, int], list[int]]:
    """预计算 Fourier cap 相位列表。

    direction 以 turn 为单位，0.25 表示乘以 exp(2*pi*i*0.25)。
    """
    caps: dict[tuple[float, float, int], list[int]] = {}
    for alpha in alphas:
        for direction in directions:
            shift = 2.0 * math.pi * direction
            for h in range(1, q):
                phases = [
                    t
                    for t in range(q)
                    if math.cos((2.0 * math.pi * h * t / q) + shift) >= alpha
                ]
                caps[(alpha, direction, h)] = phases
    return caps


def classify(size: int, sparse_threshold: int) -> str:
    """按交集大小分类。"""
    if size == 0:
        return "EmptyCap"
    if size <= sparse_threshold:
        return "SparseCap"
    return "PersistentCap"


def scan_prime(
    item: dict[str, Any],
    caps: dict[tuple[float, float, int], list[int]],
    alphas: list[float],
    directions: list[float],
    sparse_threshold: int,
    top_k: int,
) -> dict[str, Any]:
    """扫描单个 P。"""
    p = int(item["p"])
    q = int(item["q"])
    m_vector = [int(value) for value in item["m_vector"]]
    nonzero = {idx for idx, value in enumerate(m_vector) if value > 0}
    alpha_reports = []
    for alpha in alphas:
        counts = {"EmptyCap": 0, "SparseCap": 0, "PersistentCap": 0}
        worst_by_mass: list[dict[str, Any]] = []
        worst_by_size: list[dict[str, Any]] = []
        for direction in directions:
            for h in range(1, q):
                phases = caps[(alpha, direction, h)]
                intersection = [t for t in phases if t in nonzero]
                size = len(intersection)
                mass = sum(m_vector[t] for t in intersection)
                cls = classify(size, sparse_threshold)
                counts[cls] += 1
                row = {
                    "h": h,
                    "direction": direction,
                    "intersection_size": size,
                    "intersection_mass": mass,
                    "class": cls,
                    "sample": intersection[:12],
                }
                worst_by_mass.append(row)
                worst_by_size.append(row)

        worst_by_mass.sort(key=lambda row: (row["intersection_mass"], row["intersection_size"]), reverse=True)
        worst_by_size.sort(key=lambda row: (row["intersection_size"], row["intersection_mass"]), reverse=True)
        total = sum(counts.values())
        alpha_reports.append(
            {
                "alpha": alpha,
                "direction_count": len(directions),
                "frequency_count": q - 1,
                "total_caps": total,
                "class_counts": counts,
                "class_rates": {key: counts[key] / total for key in counts},
                "top_by_mass": worst_by_mass[:top_k],
                "top_by_size": worst_by_size[:top_k],
            }
        )

    return {
        "p": p,
        "q": q,
        "nonzero_m_phase_count": len(nonzero),
        "total_allowed_rows": sum(m_vector),
        "max_m": max(m_vector, default=0),
        "alpha_reports": alpha_reports,
    }


def run(
    multiplicity_path: Path,
    alphas: list[float],
    directions: list[float],
    p_filter: set[int] | None,
    sparse_threshold: int,
    top_k: int,
) -> dict[str, Any]:
    """运行 Fourier-cap 扫描。"""
    data = load_json(multiplicity_path)
    q = int(data["q"])
    caps = build_caps(q, alphas, directions)
    prime_results = []
    for item in data["prime_results"]:
        p = int(item["p"])
        if p_filter is not None and p not in p_filter:
            continue
        prime_results.append(scan_prime(item, caps, alphas, directions, sparse_threshold, top_k))

    return {
        "certificate_type": "triad_a1_lhb_fourier_cap_scan",
        "status": "fourier_cap_intersections_scanned_not_proof",
        "q": q,
        "alphas": alphas,
        "directions": directions,
        "sparse_threshold": sparse_threshold,
        "p_values": [item["p"] for item in prime_results],
        "source_hashes": {
            "fourier_cap_scan_script": file_sha256(Path(__file__).resolve()),
            "multiplicity_cap_json": file_sha256(multiplicity_path),
        },
        "prime_results": prime_results,
        "review_conclusion": (
            "本扫描只审计 Fourier 半空间 cap 与 supp(M) 的交集形态。"
            "Empty/Sparse 可分别回流闭合或 LocalSurvivor；Persistent 表明仅靠方向支撑仍不足，"
            "需要 refined PDEC、column/tail 行或 CleanKLS。该扫描不是全方向连续证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 摘要。"""
    lines = [
        "# Triad-A1 LHB Fourier-Cap 扫描",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 参数",
        "",
        f"- `Q={result['q']}`。",
        f"- `alphas={result['alphas']}`。",
        f"- `directions={result['directions']}`。",
        f"- `sparse_threshold={result['sparse_threshold']}`。",
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
            "## 3. 分类汇总",
            "",
            "| P | alpha | Empty | Sparse | Persistent | persistent rate | worst mass | worst size |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for item in result["prime_results"]:
        for report in item["alpha_reports"]:
            top_mass = report["top_by_mass"][0] if report["top_by_mass"] else {"intersection_mass": 0}
            top_size = report["top_by_size"][0] if report["top_by_size"] else {"intersection_size": 0}
            counts = report["class_counts"]
            lines.append(
                "| {p} | {alpha:g} | {empty} | {sparse} | {persistent} | {rate:.6f} | {mass} | {size} |".format(
                    p=item["p"],
                    alpha=report["alpha"],
                    empty=counts["EmptyCap"],
                    sparse=counts["SparseCap"],
                    persistent=counts["PersistentCap"],
                    rate=report["class_rates"]["PersistentCap"],
                    mass=top_mass["intersection_mass"],
                    size=top_size["intersection_size"],
                )
            )

    lines.extend(
        [
            "",
            "## 4. 结构含义",
            "",
            "Fourier cap 扫描给出的是方向支撑的压力测试：",
            "",
            "```text",
            "EmptyCap      => 该方向在 LHB 分支闭合；",
            "SparseCap     => 进入 LocalSurvivor / explicit PDEC；",
            "PersistentCap => 需要 refined PDEC、列/尾结构行或 CleanKLS。",
            "```",
            "",
            "若高阈值 cap 仍大量 Persistent，说明 `C_F cap supp(M)` 本身不是终点，必须继续使用列位移、",
            "尾互补因子或更细轮层结构；不能把 Fourier 半空间统计当作最终证明。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--alphas", default="0,0.5,0.9")
    parser.add_argument("--directions", default="0,0.25,0.5,0.75")
    parser.add_argument("--p-values", default=None)
    parser.add_argument("--sparse-threshold", type=int, default=16)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        multiplicity_path=args.multiplicity_json,
        alphas=parse_float_csv(args.alphas),
        directions=parse_float_csv(args.directions),
        p_filter=parse_p_values(args.p_values),
        sparse_threshold=args.sparse_threshold,
        top_k=args.top_k,
    )
    args.json_out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(json.dumps({"status": result["status"], "p_values": result["p_values"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
