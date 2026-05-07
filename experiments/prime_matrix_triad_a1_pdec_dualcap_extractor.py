#!/usr/bin/env python3
"""从 Triad-A1 LHB Fourier-cap 扫描中提取 PDEC DualCap 账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_pdec_dualcap_extractor.py
  python3 experiments/prime_matrix_triad_a1_pdec_dualcap_extractor.py --top-k 2

输出：
  docs/monograph/prime-matrix-triad-a1-pdec-dualcap-extractor.json
  docs/monograph/prime-matrix-triad-a1-pdec-dualcap-extractor.md
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
DEFAULT_SCAN = DOCS / "prime-matrix-triad-a1-lhb-fourier-cap-scan.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-pdec-dualcap-extractor.md"


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def cap_phases(q: int, alpha: float, direction: float, h: int) -> list[int]:
    """重建 Fourier cap 相位。"""
    shift = 2.0 * math.pi * direction
    return [
        t
        for t in range(q)
        if math.cos((2.0 * math.pi * h * t / q) + shift) >= alpha
    ]


def classify_cap(
    intersection_size: int,
    support_size: int,
    cap_size: int,
    q: int,
    sparse_threshold: int,
) -> tuple[str, str]:
    """分类 DualCap 并给出路由。"""
    if intersection_size == 0:
        return "EmptyCap", "PDECClosedInLHB"
    if intersection_size <= sparse_threshold:
        return "SparseCap", "LocalSurvivorOrExplicitPDEC"
    if support_size + cap_size > q:
        return "ForcedPersistentByDensityBarrier", "LiftOrColumnTailOrCleanKLS"
    return "PersistentCap", "RefinedPDECOrColumnTailRows"


def candidate_descriptors(scan_item: dict[str, Any], top_k: int) -> list[dict[str, Any]]:
    """从扫描结果中抽取 top cap 描述符。"""
    descriptors: list[dict[str, Any]] = []
    seen: set[tuple[float, float, int, str]] = set()
    for report in scan_item["alpha_reports"]:
        alpha = float(report["alpha"])
        for source_key in ("top_by_mass", "top_by_size"):
            for row in report[source_key][:top_k]:
                key = (alpha, float(row["direction"]), int(row["h"]), source_key)
                if key in seen:
                    continue
                seen.add(key)
                descriptors.append(
                    {
                        "alpha": alpha,
                        "direction": float(row["direction"]),
                        "h": int(row["h"]),
                        "source": source_key,
                    }
                )
    return descriptors


def analyze_cap(
    p: int,
    q: int,
    m_vector: list[int],
    descriptor: dict[str, Any],
    sparse_threshold: int,
    phase_sample_limit: int,
) -> dict[str, Any]:
    """分析单个 cap 的完整交集。"""
    support = [idx for idx, value in enumerate(m_vector) if value > 0]
    support_set = set(support)
    phases = cap_phases(q, descriptor["alpha"], descriptor["direction"], descriptor["h"])
    intersection = [t for t in phases if t in support_set]
    cap_size = len(phases)
    support_size = len(support)
    intersection_size = len(intersection)
    intersection_mass = sum(m_vector[t] for t in intersection)
    total_mass = sum(m_vector)
    lower_bound = max(0, support_size + cap_size - q)
    cap_class, route = classify_cap(
        intersection_size,
        support_size,
        cap_size,
        q,
        sparse_threshold,
    )
    top_phase_rows = sorted(
        ({"phase": t, "M": m_vector[t]} for t in intersection),
        key=lambda row: row["M"],
        reverse=True,
    )[:phase_sample_limit]
    return {
        "p": p,
        "q": q,
        "alpha": descriptor["alpha"],
        "direction": descriptor["direction"],
        "h": descriptor["h"],
        "source": descriptor["source"],
        "support_size": support_size,
        "support_density": support_size / q,
        "cap_size": cap_size,
        "cap_density": cap_size / q,
        "intersection_size": intersection_size,
        "intersection_density_in_q": intersection_size / q,
        "intersection_density_in_support": (
            intersection_size / support_size if support_size else None
        ),
        "intersection_mass": intersection_mass,
        "mass_share_of_total_m": intersection_mass / total_mass if total_mass else None,
        "total_m": total_mass,
        "density_barrier_lower_bound": lower_bound,
        "density_barrier_excess": intersection_size - lower_bound,
        "classification": cap_class,
        "route": route,
        "phase_sample": intersection[:phase_sample_limit],
        "top_phase_rows": top_phase_rows,
    }


def analyze_prime(
    mult_item: dict[str, Any],
    scan_item: dict[str, Any],
    top_k: int,
    sparse_threshold: int,
    phase_sample_limit: int,
) -> dict[str, Any]:
    """分析单个 P 的 DualCap 候选。"""
    p = int(mult_item["p"])
    q = int(mult_item["q"])
    m_vector = [int(value) for value in mult_item["m_vector"]]
    caps = [
        analyze_cap(
            p=p,
            q=q,
            m_vector=m_vector,
            descriptor=descriptor,
            sparse_threshold=sparse_threshold,
            phase_sample_limit=phase_sample_limit,
        )
        for descriptor in candidate_descriptors(scan_item, top_k)
    ]
    caps.sort(
        key=lambda row: (
            row["mass_share_of_total_m"] or 0.0,
            row["intersection_size"],
        ),
        reverse=True,
    )
    class_counts: dict[str, int] = {}
    route_counts: dict[str, int] = {}
    for cap in caps:
        class_counts[cap["classification"]] = class_counts.get(cap["classification"], 0) + 1
        route_counts[cap["route"]] = route_counts.get(cap["route"], 0) + 1
    return {
        "p": p,
        "q": q,
        "candidate_count": len(caps),
        "class_counts": class_counts,
        "route_counts": route_counts,
        "top_caps": caps,
        "structural_reading": (
            "这些 cap 是固定 Q-PDEC 对偶失败时最先要登记的 DualCap 候选。"
            "Empty/Sparse 进入闭合或 LocalSurvivor；Persistent 且由密度屏障强制时，不能同层循环。"
        ),
    }


def run(
    mult_path: Path,
    scan_path: Path,
    top_k: int,
    sparse_threshold: int,
    phase_sample_limit: int,
) -> dict[str, Any]:
    """运行 DualCap 提取。"""
    mult = load_json(mult_path)
    scan = load_json(scan_path)
    mult_by_p = {int(item["p"]): item for item in mult["prime_results"]}
    scan_by_p = {int(item["p"]): item for item in scan["prime_results"]}
    p_values = sorted(set(mult_by_p) & set(scan_by_p))
    prime_results = [
        analyze_prime(
            mult_by_p[p],
            scan_by_p[p],
            top_k,
            sparse_threshold,
            phase_sample_limit,
        )
        for p in p_values
    ]
    aggregate_route_counts: dict[str, int] = {}
    aggregate_class_counts: dict[str, int] = {}
    for item in prime_results:
        for key, value in item["route_counts"].items():
            aggregate_route_counts[key] = aggregate_route_counts.get(key, 0) + value
        for key, value in item["class_counts"].items():
            aggregate_class_counts[key] = aggregate_class_counts.get(key, 0) + value
    return {
        "certificate_type": "triad_a1_pdec_dualcap_extractor",
        "status": "pdec_dualcap_candidates_materialized",
        "q": int(mult["q"]),
        "top_k": top_k,
        "sparse_threshold": sparse_threshold,
        "phase_sample_limit": phase_sample_limit,
        "p_values": p_values,
        "source_hashes": {
            "pdec_dualcap_extractor_script": file_sha256(Path(__file__).resolve()),
            "multiplicity_cap_json": file_sha256(mult_path),
            "fourier_cap_scan_json": file_sha256(scan_path),
        },
        "aggregate_class_counts": aggregate_class_counts,
        "aggregate_route_counts": aggregate_route_counts,
        "prime_results": prime_results,
        "review_conclusion": (
            "PDEC 对偶上界失败必须输出 DualCap。当前提取器把固定 Q Fourier-cap 的最重/最大失败帽"
            "重建为完整相位块，并按 Empty/Sparse/Persistent/密度屏障强制进行路由。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 PDEC DualCap 提取账本",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构语义",
        "",
        "若固定 `Q` 的 `PDEC` 对偶上界 `U_CRT<L_PDEC` 失败，失败必须显化为 Fourier/Bohr cap 中的质量集中。",
        "本账本从 LHB Fourier-cap 扫描中抽取最重/最大 cap，并重建完整相位交集：",
        "",
        "```text",
        "DualCap = C_{h,alpha,dir} cap supp(M)。",
        "```",
        "",
        "路由规则：",
        "",
        "```text",
        "EmptyCap      => 当前方向在 LHB 分支闭合；",
        "SparseCap     => LocalSurvivor 或 explicit PDEC；",
        "PersistentCap => refined PDEC / column-tail rows；",
        "DensityBarrier forced Persistent => 不能同层循环，必须升层、加行或 CleanKLS。",
        "```",
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
            "## 3. 汇总",
            "",
            f"- `aggregate_class_counts={result['aggregate_class_counts']}`。",
            f"- `aggregate_route_counts={result['aggregate_route_counts']}`。",
            "",
            "| P | candidates | classes | routes | top mass share | top intersection | top route |",
            "| ---: | ---: | --- | --- | ---: | ---: | --- |",
        ]
    )
    for item in result["prime_results"]:
        top = item["top_caps"][0] if item["top_caps"] else {}
        lines.append(
            "| {p} | {count} | `{classes}` | `{routes}` | {share} | {size} | `{route}` |".format(
                p=item["p"],
                count=item["candidate_count"],
                classes=item["class_counts"],
                routes=item["route_counts"],
                share=fmt_float(top.get("mass_share_of_total_m")),
                size=top.get("intersection_size", "n/a"),
                route=top.get("route", "n/a"),
            )
        )

    lines.extend(["", "## 4. Top DualCaps", ""])
    for item in result["prime_results"]:
        lines.extend(
            [
                f"### P={item['p']}",
                "",
                "| alpha | h | dir | source | class | route | cap size | intersection | mass share | density LB | sample |",
                "| ---: | ---: | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | --- |",
            ]
        )
        for cap in item["top_caps"][:6]:
            lines.append(
                "| {alpha} | {h} | {direction} | `{source}` | `{cls}` | `{route}` | {cap_size} | {inter} | {share} | {lb} | `{sample}` |".format(
                    alpha=fmt_float(cap["alpha"]),
                    h=cap["h"],
                    direction=fmt_float(cap["direction"]),
                    source=cap["source"],
                    cls=cap["classification"],
                    route=cap["route"],
                    cap_size=cap["cap_size"],
                    inter=cap["intersection_size"],
                    share=fmt_float(cap["mass_share_of_total_m"]),
                    lb=cap["density_barrier_lower_bound"],
                    sample=cap["phase_sample"],
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 5. 结论",
            "",
            "本账本没有排除全部 PDEC；它完成的是 PDEC 失败的强制输出。",
            "以后若固定 `Q` 对偶比较失败，必须引用这里的 `DualCap` 或生成同格式新 cap，不能停在抽象 `DualGap`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplicity-json", type=Path, default=DEFAULT_MULT)
    parser.add_argument("--scan-json", type=Path, default=DEFAULT_SCAN)
    parser.add_argument("--top-k", type=int, default=2)
    parser.add_argument("--sparse-threshold", type=int, default=16)
    parser.add_argument("--phase-sample-limit", type=int, default=16)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        mult_path=args.multiplicity_json,
        scan_path=args.scan_json,
        top_k=args.top_k,
        sparse_threshold=args.sparse_threshold,
        phase_sample_limit=args.phase_sample_limit,
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
                "aggregate_route_counts": result["aggregate_route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
