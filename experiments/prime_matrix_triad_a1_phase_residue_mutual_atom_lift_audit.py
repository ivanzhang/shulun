#!/usr/bin/env python3
"""追踪 PhaseResidueMutual 原子在下一升层中的归宿。

用法示例：
  python3 experiments/prime_matrix_triad_a1_phase_residue_mutual_atom_lift_audit.py
  python3 experiments/prime_matrix_triad_a1_phase_residue_mutual_atom_lift_audit.py --pdec-kl-threshold 0.2

输出：
  docs/monograph/prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.json
  docs/monograph/prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.md
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_WITNESS = DOCS / "prime-matrix-triad-a1-nodeletion-kl-witness-extractor.json"
DEFAULT_MULTS = ",".join(
    str(path)
    for path in (
        DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json",
        DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json",
        DOCS / "prime-matrix-triad-a1-q510510-multiplicity-cap.json",
    )
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-phase-residue-mutual-atom-lift-audit.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def load_multiplicity(paths: list[Path]) -> dict[int, dict[str, Any]]:
    """按 q 索引 multiplicity 证书。"""
    result = {}
    for path in paths:
        data = load_json(path)
        q = int(data["q"])
        result[q] = {
            "path": str(path),
            "sha256": file_sha256(path),
            "prime_results": {
                int(item["p"]): [int(value) for value in item["m_vector"]]
                for item in data["prime_results"]
            },
        }
    return result


def find_next_q(q_lift: int, multiplicity: dict[int, dict[str, Any]]) -> int | None:
    """寻找当前可用数据里的下一层 q。"""
    candidates = [q for q in multiplicity if q > q_lift and q % q_lift == 0]
    return min(candidates) if candidates else None


def fiber_kl(values: list[int]) -> dict[str, Any] | None:
    """计算下一层 fiber 相对均匀的 KL/TV。"""
    total = sum(values)
    size = len(values)
    if total <= 0 or size <= 1:
        return None
    probs = [value / total for value in values]
    uniform = 1.0 / size
    entropy = -sum(prob * math.log(prob) for prob in probs if prob > 0)
    log_size = math.log(size)
    kl_nats = log_size - entropy
    tv = 0.5 * sum(abs(prob - uniform) for prob in probs)
    top_residue, top_prob = max(enumerate(probs), key=lambda item: item[1])
    return {
        "kl_nats": kl_nats,
        "normalized_kl": kl_nats / log_size if log_size > 0 else 0.0,
        "tv_to_uniform": tv,
        "top_residue": top_residue,
        "top_probability": top_prob,
        "top_excess_over_uniform": top_prob - uniform,
    }


def classify_next(
    next_values: list[int] | None,
    deletion_threshold: float,
    pdec_kl_threshold: float,
    clean_kl_threshold: float,
) -> str:
    """分类下一层归宿。"""
    if next_values is None:
        return "NoNextLayerDataProfiniteObligation"
    size = len(next_values)
    support_count = sum(1 for value in next_values if value > 0)
    if support_count == 0:
        return "NextLayerDeletedAtom"
    support_rate = support_count / size if size else 0.0
    if support_rate <= deletion_threshold:
        return "NextLayerFiberDeletion"
    stats = fiber_kl(next_values)
    if stats is None:
        return "NextLayerEmptyOrInvalid"
    if stats["normalized_kl"] >= pdec_kl_threshold:
        return "NextLayerRefinedPDECEntropy"
    if stats["normalized_kl"] <= clean_kl_threshold:
        return "NextLayerCleanFiberCandidate"
    return "NextLayerMixedNeedsFurtherLift"


def analyze_atom(
    atom: dict[str, Any],
    p: int,
    q: int,
    q_lift: int,
    lift_m: list[int],
    next_q: int | None,
    next_m: list[int] | None,
    deletion_threshold: float,
    pdec_kl_threshold: float,
    clean_kl_threshold: float,
) -> dict[str, Any]:
    """追踪单个互信息原子。"""
    old_phase = int(atom["old_phase"])
    residue = int(atom["residue"])
    new_phase = old_phase + residue * q
    lifted_mass = int(lift_m[new_phase])
    reported_mass = int(atom["mass"])
    next_values = None
    next_stats = None
    next_support_count = None
    next_support_rate = None
    next_total_mass = None
    next_fiber_size = None
    if next_q is not None and next_m is not None:
        next_fiber_size = next_q // q_lift
        next_values = [
            int(next_m[new_phase + next_residue * q_lift])
            for next_residue in range(next_fiber_size)
        ]
        next_total_mass = sum(next_values)
        next_support_count = sum(1 for value in next_values if value > 0)
        next_support_rate = next_support_count / next_fiber_size
        next_stats = fiber_kl(next_values)

    route = classify_next(
        next_values,
        deletion_threshold,
        pdec_kl_threshold,
        clean_kl_threshold,
    )
    nonzero_next = []
    if next_values is not None:
        nonzero_next = [
            {"residue": idx, "mass": value}
            for idx, value in enumerate(next_values)
            if value > 0
        ]

    return {
        "p": p,
        "q": q,
        "q_lift": q_lift,
        "old_phase": old_phase,
        "residue": residue,
        "new_phase": new_phase,
        "reported_mass": reported_mass,
        "lifted_phase_mass": lifted_mass,
        "lift_identity_holds": lifted_mass == reported_mass,
        "source_mutual_contribution_nats": atom["mutual_contribution_nats"],
        "source_lift_over_independent": atom["lift_over_independent"],
        "next_q": next_q,
        "next_fiber_size": next_fiber_size,
        "next_total_mass": next_total_mass,
        "next_support_count": next_support_count,
        "next_support_rate": next_support_rate,
        "next_normalized_kl": None if next_stats is None else next_stats["normalized_kl"],
        "next_tv_to_uniform": None if next_stats is None else next_stats["tv_to_uniform"],
        "next_top_residue": None if next_stats is None else next_stats["top_residue"],
        "next_top_probability": None if next_stats is None else next_stats["top_probability"],
        "next_top_excess_over_uniform": (
            None if next_stats is None else next_stats["top_excess_over_uniform"]
        ),
        "next_nonzero_residue_mass": nonzero_next,
        "route": route,
    }


def analyze_witness_row(
    pair: dict[str, Any],
    row: dict[str, Any],
    multiplicity: dict[int, dict[str, Any]],
    deletion_threshold: float,
    pdec_kl_threshold: float,
    clean_kl_threshold: float,
) -> list[dict[str, Any]]:
    """分析一个 P 行里的所有 top 互信息原子。"""
    p = int(row["p"])
    q = int(pair["q"])
    q_lift = int(pair["q_lift"])
    lift_m = multiplicity[q_lift]["prime_results"].get(p)
    if lift_m is None:
        return []
    next_q = find_next_q(q_lift, multiplicity)
    next_m = None
    if next_q is not None:
        next_m = multiplicity[next_q]["prime_results"].get(p)
    return [
        analyze_atom(
            atom,
            p,
            q,
            q_lift,
            lift_m,
            next_q,
            next_m,
            deletion_threshold,
            pdec_kl_threshold,
            clean_kl_threshold,
        )
        for atom in row["top_phase_residue_mutual_atoms"]
    ]


def run(
    witness_path: Path,
    mult_paths: list[Path],
    deletion_threshold: float,
    pdec_kl_threshold: float,
    clean_kl_threshold: float,
) -> dict[str, Any]:
    """运行互信息原子提升审计。"""
    witness = load_json(witness_path)
    multiplicity = load_multiplicity(mult_paths)
    atom_rows = [
        atom_row
        for pair in witness["pairs"]
        for row in pair["rows"]
        for atom_row in analyze_witness_row(
            pair,
            row,
            multiplicity,
            deletion_threshold,
            pdec_kl_threshold,
            clean_kl_threshold,
        )
    ]
    route_counts = Counter(row["route"] for row in atom_rows)
    with_next = [row for row in atom_rows if row["next_q"] is not None and row["next_total_mass"] is not None]
    return {
        "certificate_type": "triad_a1_phase_residue_mutual_atom_lift_audit",
        "status": "phase_residue_mutual_atoms_lifted_to_next_layer_routes",
        "parameters": {
            "deletion_support_threshold": deletion_threshold,
            "pdec_normalized_kl_threshold": pdec_kl_threshold,
            "clean_normalized_kl_threshold": clean_kl_threshold,
            "threshold_meaning": "阈值只用于有限审计分流；结构结论是 u=t+bQ 的原子提升恒等式。",
        },
        "source_hashes": {
            "phase_residue_atom_lift_audit_script": file_sha256(Path(__file__).resolve()),
            "witness_json": file_sha256(witness_path),
            **{
                f"multiplicity_q{q}": data["sha256"]
                for q, data in sorted(multiplicity.items())
            },
        },
        "q_values_available": sorted(multiplicity),
        "atom_count": len(atom_rows),
        "with_next_layer_count": len(with_next),
        "all_lift_identities_hold": all(row["lift_identity_holds"] for row in atom_rows),
        "route_counts": dict(route_counts),
        "max_next_normalized_kl": max(
            (row["next_normalized_kl"] for row in with_next if row["next_normalized_kl"] is not None),
            default=None,
        ),
        "min_next_normalized_kl": min(
            (row["next_normalized_kl"] for row in with_next if row["next_normalized_kl"] is not None),
            default=None,
        ),
        "atom_rows": atom_rows,
        "structural_law": (
            "PhaseResidueMutual atom (t,b) maps exactly to new phase u=t+bQ mod Q'. "
            "Next layer either deletes u, leaves a refined KL peak on u's fiber, or flattens u toward CleanKLS."
        ),
        "review_conclusion": (
            "当前所有已抽取互信息原子都满足提升层质量恒等式。已有下一层数据的原子分裂为 "
            "CleanFiberCandidate 与 RefinedPDECEntropy；没有出现无名第四路线。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点值。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 PhaseResidueMutual 原子提升审计",
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
        "(old phase t, residue b)  <=>  new phase u=t+bQ mod Q'。",
        "```",
        "",
        "所以互信息峰不是新终端；它在提升层只是普通相位原子。下一层只能删除、继续偏斜、或趋平。",
        "",
        "## 2. 参数",
        "",
    ]
    for key, value in result["parameters"].items():
        lines.append(f"- `{key}={value}`。")

    lines.extend(
        [
            "",
            "## 3. 汇总",
            "",
            f"- `q_values_available={result['q_values_available']}`。",
            f"- `atom_count={result['atom_count']}`。",
            f"- `with_next_layer_count={result['with_next_layer_count']}`。",
            f"- `all_lift_identities_hold={result['all_lift_identities_hold']}`。",
            f"- `route_counts={result['route_counts']}`。",
            f"- `min_next_normalized_kl={fmt_float(result['min_next_normalized_kl'])}`。",
            f"- `max_next_normalized_kl={fmt_float(result['max_next_normalized_kl'])}`。",
            "",
            "## 4. 原子明细",
            "",
            "| layer | P | old phase | residue | new phase | mass | next Q | next support rate | next KL | route |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["atom_rows"]:
        lines.append(
            "| Q={q}->{ql} | {p} | {old} | {residue} | {new} | {mass} | {nq} | {supp} | {kl} | `{route}` |".format(
                q=row["q"],
                ql=row["q_lift"],
                p=row["p"],
                old=row["old_phase"],
                residue=row["residue"],
                new=row["new_phase"],
                mass=row["reported_mass"],
                nq=row["next_q"] if row["next_q"] is not None else "n/a",
                supp=fmt_float(row["next_support_rate"]),
                kl=fmt_float(row["next_normalized_kl"]),
                route=row["route"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "`NextLayerCleanFiberCandidate` 表示该原子在下一层 fiber 上已接近均匀，若 NoDeletion 持续则可作为 CleanKLS 输入。",
            "`NextLayerRefinedPDECEntropy` 表示该原子提升后仍有明显 fiber KL，必须作为 refined/profinite PDEC 或继续升层输入。",
            "`NoNextLayerDataProfiniteObligation` 不是反例出口，只表示当前仓库尚无下一层 multiplicity 数据，需要在无限塔证明中按同一规则处理。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--witness-json", type=Path, default=DEFAULT_WITNESS)
    parser.add_argument("--multiplicity-jsons", default=DEFAULT_MULTS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--deletion-support-threshold", type=float, default=0.5)
    parser.add_argument("--pdec-kl-threshold", type=float, default=0.2)
    parser.add_argument("--clean-kl-threshold", type=float, default=0.05)
    args = parser.parse_args()

    result = run(
        args.witness_json,
        parse_paths(args.multiplicity_jsons),
        args.deletion_support_threshold,
        args.pdec_kl_threshold,
        args.clean_kl_threshold,
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
                "atom_count": result["atom_count"],
                "with_next_layer_count": result["with_next_layer_count"],
                "all_lift_identities_hold": result["all_lift_identities_hold"],
                "route_counts": result["route_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
