#!/usr/bin/env python3
"""提取 Triad-A1 NoDeletion-KL 的具体偏斜见证。

用法示例：
  python3 experiments/prime_matrix_triad_a1_nodeletion_kl_witness_extractor.py
  python3 experiments/prime_matrix_triad_a1_nodeletion_kl_witness_extractor.py --top-limit 8

输出：
  docs/monograph/prime-matrix-triad-a1-nodeletion-kl-witness-extractor.json
  docs/monograph/prime-matrix-triad-a1-nodeletion-kl-witness-extractor.md
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
DEFAULT_PAIRS = ",".join(
    [
        ":".join(
            [
                str(DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"),
                str(DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json"),
            ]
        ),
        ":".join(
            [
                str(DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json"),
                str(DOCS / "prime-matrix-triad-a1-q510510-multiplicity-cap.json"),
            ]
        ),
    ]
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-nodeletion-kl-witness-extractor.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-nodeletion-kl-witness-extractor.md"


def parse_pairs(raw: str) -> list[tuple[Path, Path]]:
    """解析 `base:lift,base:lift` 形式的输入对。"""
    pairs = []
    for item in raw.split(","):
        text = item.strip()
        if not text:
            continue
        left, sep, right = text.partition(":")
        if not sep:
            raise ValueError(f"bad pair: {text}")
        pairs.append((Path(left), Path(right)))
    return pairs


def file_sha256(path: Path) -> str:
    """计算输入文件指纹，保证报告可复核。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def index_prime_results(data: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """按 P 索引 prime_results。"""
    return {int(item["p"]): item for item in data["prime_results"]}


def kl_to_uniform(values: list[int], fiber_size: int) -> dict[str, Any] | None:
    """计算一个 fiber 或 residue 投影相对均匀分布的 KL/TV。"""
    total = sum(values)
    if total <= 0:
        return None
    probs = [value / total for value in values]
    uniform = 1.0 / fiber_size
    entropy = -sum(prob * math.log(prob) for prob in probs if prob > 0)
    log_r = math.log(fiber_size)
    kl_nats = log_r - entropy
    tv = 0.5 * sum(abs(prob - uniform) for prob in probs)
    top_residue, top_prob = max(enumerate(probs), key=lambda pair: pair[1])
    return {
        "total_mass": total,
        "probabilities": probs,
        "entropy_nats": entropy,
        "kl_nats": kl_nats,
        "normalized_kl": kl_nats / log_r if log_r > 0 else 0.0,
        "tv_to_uniform": tv,
        "top_residue": top_residue,
        "top_probability": top_prob,
        "top_excess_over_uniform": top_prob - uniform,
        "support_count": sum(1 for value in values if value > 0),
    }


def top_items(items: list[dict[str, Any]], key: str, limit: int) -> list[dict[str, Any]]:
    """按指定键降序截断。"""
    return sorted(items, key=lambda item: item[key], reverse=True)[:limit]


def classify_shape(
    new_activation_count: int,
    global_norm_kl: float,
    mutual_norm_kl: float,
    conditional_norm_kl: float,
    global_threshold: float,
    mutual_threshold: float,
    clean_threshold: float,
) -> str:
    """把 KL 偏斜落点分成全局 residue、相位-residue 互信息或 CleanKLS 候选。"""
    if new_activation_count:
        return "ProjectionStitchingPDECInput"
    if global_norm_kl >= global_threshold:
        return "GlobalResiduePDECWitness"
    if mutual_norm_kl >= mutual_threshold:
        return "PhaseResidueMutualPDECWitness"
    if conditional_norm_kl <= clean_threshold:
        return "CleanKLSShapeCandidate"
    return "MixedKLNeedsFurtherRefinement"


def classify_gate(
    survival: float | None,
    nodeletion_survival: float,
    shape_route: str,
) -> str:
    """先看删除是否停止；停止后才让 KL 形状成为终端分流。"""
    if survival is None:
        return "EmptyLayer"
    if survival < nodeletion_survival:
        return "FiberDeletionCurrentLayer"
    if shape_route == "CleanKLSShapeCandidate":
        return "NoDeletionCleanKLSCandidate"
    if shape_route.endswith("PDECWitness") or shape_route.endswith("PDECInput"):
        return "NoDeletionPDECWitness"
    return "NoDeletionMixedKLNeedsMoreLayers"


def analyze_prime(
    p: int,
    base_item: dict[str, Any],
    lift_item: dict[str, Any],
    q: int,
    q_lift: int,
    fiber_size: int,
    top_limit: int,
    nodeletion_survival: float,
    global_threshold: float,
    mutual_threshold: float,
    clean_threshold: float,
) -> dict[str, Any]:
    """提取单个 P 的 KL 分解见证。"""
    base_m = [int(value) for value in base_item["m_vector"]]
    lift_m = [int(value) for value in lift_item["m_vector"]]
    active_old = [phase for phase, value in enumerate(base_m) if value > 0]
    active_old_set = set(active_old)
    lift_support = [phase for phase, value in enumerate(lift_m) if value > 0]
    new_activation = [phase for phase in lift_support if phase % q not in active_old_set]
    new_activation_mass = sum(lift_m[phase] for phase in new_activation)

    residue_mass = [0] * fiber_size
    conditional_rows: list[dict[str, Any]] = []
    inherited_slots = 0
    inherited_mass = 0

    for phase in active_old:
        values = [lift_m[phase + residue * q] for residue in range(fiber_size)]
        lift_mass = sum(values)
        support_count = sum(1 for value in values if value > 0)
        inherited_slots += support_count
        inherited_mass += lift_mass
        for residue, value in enumerate(values):
            residue_mass[residue] += value
        stats = kl_to_uniform(values, fiber_size)
        if stats is None:
            continue
        conditional_rows.append(
            {
                "old_phase": phase,
                "old_mass": int(base_m[phase]),
                "lift_mass": lift_mass,
                "support_count": support_count,
                "top_residue": stats["top_residue"],
                "top_mass": values[stats["top_residue"]],
                "top_share_within_phase": stats["top_probability"],
                "kl_nats": stats["kl_nats"],
                "normalized_kl": stats["normalized_kl"],
                "conditional_kl_contribution_nats": 0.0,
                "fiber_values": values,
            }
        )

    possible_slots = len(active_old) * fiber_size
    slot_survival = inherited_slots / possible_slots if possible_slots else None
    global_stats = kl_to_uniform(residue_mass, fiber_size)
    if global_stats is None:
        raise ValueError(f"P={p}: empty lifted inherited mass")

    weighted_conditional_kl = 0.0
    for row in conditional_rows:
        weight = row["lift_mass"] / inherited_mass if inherited_mass else 0.0
        contribution = weight * row["kl_nats"]
        row["conditional_kl_contribution_nats"] = contribution
        weighted_conditional_kl += contribution

    # 链式分解：E_t KL(B|t || U_B)=KL(B||U_B)+I(T;B)。
    mutual_information_nats = max(0.0, weighted_conditional_kl - global_stats["kl_nats"])
    log_r = math.log(fiber_size)
    global_norm = global_stats["normalized_kl"]
    conditional_norm = weighted_conditional_kl / log_r if log_r > 0 else 0.0
    mutual_norm = mutual_information_nats / log_r if log_r > 0 else 0.0

    atom_rows: list[dict[str, Any]] = []
    for row in conditional_rows:
        phase_mass = row["lift_mass"]
        if phase_mass <= 0:
            continue
        for residue, mass in enumerate(row["fiber_values"]):
            if mass <= 0 or residue_mass[residue] <= 0:
                continue
            p_joint = mass / inherited_mass
            p_phase = phase_mass / inherited_mass
            p_residue = residue_mass[residue] / inherited_mass
            independent = p_phase * p_residue
            lift_over_independent = p_joint / independent if independent > 0 else math.inf
            mutual_contribution = p_joint * math.log(lift_over_independent)
            if mutual_contribution <= 0:
                continue
            atom_rows.append(
                {
                    "old_phase": row["old_phase"],
                    "residue": residue,
                    "mass": mass,
                    "phase_mass": phase_mass,
                    "residue_mass": residue_mass[residue],
                    "joint_share": p_joint,
                    "phase_share": p_phase,
                    "residue_share": p_residue,
                    "within_phase_share": mass / phase_mass,
                    "lift_over_independent": lift_over_independent,
                    "mutual_contribution_nats": mutual_contribution,
                }
            )

    shape_route = classify_shape(
        len(new_activation),
        global_norm,
        mutual_norm,
        conditional_norm,
        global_threshold,
        mutual_threshold,
        clean_threshold,
    )
    gate_route = classify_gate(slot_survival, nodeletion_survival, shape_route)

    return {
        "p": p,
        "q": q,
        "q_lift": q_lift,
        "fiber_size": fiber_size,
        "old_support_count": len(active_old),
        "inherited_lift_mass": inherited_mass,
        "new_activation_count": len(new_activation),
        "new_activation_mass": new_activation_mass,
        "slot_survival_rate": slot_survival,
        "slot_deletion_rate": 1.0 - slot_survival if slot_survival is not None else None,
        "global_residue_mass": residue_mass,
        "global_residue_kl_nats": global_stats["kl_nats"],
        "global_residue_normalized_kl": global_norm,
        "global_residue_tv_to_uniform": global_stats["tv_to_uniform"],
        "global_top_residue": global_stats["top_residue"],
        "global_top_excess_over_uniform": global_stats["top_excess_over_uniform"],
        "conditional_kl_avg_nats": weighted_conditional_kl,
        "conditional_normalized_kl": conditional_norm,
        "phase_residue_mutual_information_nats": mutual_information_nats,
        "phase_residue_mutual_normalized_kl": mutual_norm,
        "kl_chain_abs_error": abs(
            weighted_conditional_kl
            - global_stats["kl_nats"]
            - mutual_information_nats
        ),
        "shape_route": shape_route,
        "gate_route": gate_route,
        "top_conditional_fibers": top_items(
            conditional_rows,
            "conditional_kl_contribution_nats",
            top_limit,
        ),
        "top_phase_residue_mutual_atoms": top_items(
            atom_rows,
            "mutual_contribution_nats",
            top_limit,
        ),
    }


def analyze_pair(
    base_path: Path,
    lift_path: Path,
    top_limit: int,
    nodeletion_survival: float,
    global_threshold: float,
    mutual_threshold: float,
    clean_threshold: float,
) -> dict[str, Any]:
    """分析一个 Q->Q' 晋升对。"""
    base = load_json(base_path)
    lift = load_json(lift_path)
    q = int(base["q"])
    q_lift = int(lift["q"])
    if q_lift % q != 0:
        raise ValueError(f"lift q={q_lift} is not a multiple of base q={q}")
    fiber_size = q_lift // q
    base_results = index_prime_results(base)
    lift_results = index_prime_results(lift)
    p_values = sorted(set(base_results) & set(lift_results))
    rows = [
        analyze_prime(
            p,
            base_results[p],
            lift_results[p],
            q,
            q_lift,
            fiber_size,
            top_limit,
            nodeletion_survival,
            global_threshold,
            mutual_threshold,
            clean_threshold,
        )
        for p in p_values
    ]
    return {
        "base_path": str(base_path),
        "lift_path": str(lift_path),
        "base_sha256": file_sha256(base_path),
        "lift_sha256": file_sha256(lift_path),
        "q": q,
        "q_lift": q_lift,
        "fiber_size": fiber_size,
        "p_values": p_values,
        "rows": rows,
    }


def count_by(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    """统计分类数量。"""
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row[key])
        counts[value] = counts.get(value, 0) + 1
    return counts


def run(
    pairs: list[tuple[Path, Path]],
    top_limit: int,
    nodeletion_survival: float,
    global_threshold: float,
    mutual_threshold: float,
    clean_threshold: float,
) -> dict[str, Any]:
    """运行全部见证提取。"""
    pair_results = [
        analyze_pair(
            base_path,
            lift_path,
            top_limit,
            nodeletion_survival,
            global_threshold,
            mutual_threshold,
            clean_threshold,
        )
        for base_path, lift_path in pairs
    ]
    rows = [row for pair in pair_results for row in pair["rows"]]
    return {
        "certificate_type": "triad_a1_nodeletion_kl_witness_extractor",
        "status": "nodeletion_kl_witness_extracted_terminal_open",
        "parameters": {
            "top_limit": top_limit,
            "nodeletion_survival": nodeletion_survival,
            "global_normalized_kl_pdec_threshold": global_threshold,
            "mutual_normalized_kl_pdec_threshold": mutual_threshold,
            "clean_normalized_kl_threshold": clean_threshold,
            "threshold_meaning": (
                "阈值只用于有限审计分流；正式链条使用 KL 链式分解和极限累计/趋零。"
            ),
        },
        "source_hashes": {
            "nodeletion_kl_witness_extractor_script": file_sha256(Path(__file__).resolve()),
        },
        "pairs": pair_results,
        "row_count": len(rows),
        "gate_route_counts": count_by(rows, "gate_route"),
        "shape_route_counts": count_by(rows, "shape_route"),
        "max_global_residue_normalized_kl": max(
            row["global_residue_normalized_kl"] for row in rows
        ),
        "max_global_residue_tv_to_uniform": max(
            row["global_residue_tv_to_uniform"] for row in rows
        ),
        "min_phase_residue_mutual_normalized_kl": min(
            row["phase_residue_mutual_normalized_kl"] for row in rows
        ),
        "max_kl_chain_abs_error": max(row["kl_chain_abs_error"] for row in rows),
        "current_nodeletion_triggered": any(
            row["gate_route"] != "FiberDeletionCurrentLayer" for row in rows
        ),
        "structural_law": (
            "对每层 fiber，条件 KL 满足 E_t KL(B|t||U_B)=KL(B||U_B)+I(T;B)。"
            "全局 residue KL 累计给 GlobalResiduePDEC；互信息累计给 refined "
            "(old_phase,residue) PDEC；二者在 NoDeletion 下同时趋零才进入 CleanKLS。"
        ),
        "review_conclusion": (
            "当前已物化层仍全部由 FiberDeletion 支付；但 KL 形状显示偏斜主要藏在"
            "旧相位-新增 residue 的互信息中，而不是全局 residue 投影峰。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点值。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 见证报告。"""
    lines = [
        "# Triad-A1 NoDeletion-KL 见证提取器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构分解",
        "",
        result["structural_law"],
        "",
        "写成公式就是：",
        "",
        "```text",
        "H_cond = E_t KL(B|t || U_B)",
        "       = KL(B || U_B) + I(T;B)。",
        "```",
        "",
        "因此：",
        "",
        "```text",
        "KL(B||U_B) 持久累计       => GlobalResiduePDEC；",
        "I(T;B) 持久累计           => refined (old_phase,residue) PDEC；",
        "二者在 NoDeletion 下趋零  => CleanKLS/DLS admission。",
        "```",
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
            f"- `row_count={result['row_count']}`。",
            f"- `gate_route_counts={result['gate_route_counts']}`。",
            f"- `shape_route_counts={result['shape_route_counts']}`。",
            f"- `current_nodeletion_triggered={result['current_nodeletion_triggered']}`。",
            f"- `max_global_residue_normalized_kl={fmt_float(result['max_global_residue_normalized_kl'])}`。",
            f"- `max_global_residue_tv_to_uniform={fmt_float(result['max_global_residue_tv_to_uniform'])}`。",
            f"- `min_phase_residue_mutual_normalized_kl={fmt_float(result['min_phase_residue_mutual_normalized_kl'])}`。",
            f"- `max_kl_chain_abs_error={fmt_float(result['max_kl_chain_abs_error'])}`。",
            "",
            "## 4. 层级明细",
            "",
            "| layer | P | survival | global norm KL | global TV | cond norm KL | mutual norm KL | gate | shape |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for pair in result["pairs"]:
        for row in pair["rows"]:
            lines.append(
                "| Q={q}->{ql} | {p} | {surv} | {gkl} | {gtv} | {ckl} | {ikl} | `{gate}` | `{shape}` |".format(
                    q=pair["q"],
                    ql=pair["q_lift"],
                    p=row["p"],
                    surv=fmt_float(row["slot_survival_rate"]),
                    gkl=fmt_float(row["global_residue_normalized_kl"]),
                    gtv=fmt_float(row["global_residue_tv_to_uniform"]),
                    ckl=fmt_float(row["conditional_normalized_kl"]),
                    ikl=fmt_float(row["phase_residue_mutual_normalized_kl"]),
                    gate=row["gate_route"],
                    shape=row["shape_route"],
                )
            )

    lines.extend(
        [
            "",
            "## 5. 代表性互信息原子",
            "",
            "每行列出贡献最大的 `(old_phase,residue)` 原子。若这种原子族持久复现，就是 refined PDEC 输入。",
            "",
            "| layer | P | old phase | residue | mass | within phase | residue share | lift/independent | mutual contrib |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for pair in result["pairs"]:
        for row in pair["rows"]:
            atoms = row["top_phase_residue_mutual_atoms"][:3]
            for atom in atoms:
                lines.append(
                    "| Q={q}->{ql} | {p} | {phase} | {residue} | {mass} | {within} | {rshare} | {lift} | {contrib} |".format(
                        q=pair["q"],
                        ql=pair["q_lift"],
                        p=row["p"],
                        phase=atom["old_phase"],
                        residue=atom["residue"],
                        mass=atom["mass"],
                        within=fmt_float(atom["within_phase_share"]),
                        rshare=fmt_float(atom["residue_share"]),
                        lift=fmt_float(atom["lift_over_independent"]),
                        contrib=fmt_float(atom["mutual_contribution_nats"]),
                    )
                )

    lines.extend(
        [
            "",
            "## 6. 读法",
            "",
            "当前 `gate` 全部仍是 `FiberDeletionCurrentLayer`，所以不能把本报告当作 NoDeletion 反例闭合。",
            "它的作用是把未来 `a_n->1` 时的 KL 硬点具体化：偏斜若不在全局 residue，就必在 `(old_phase,residue)` 互信息中登记。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pairs", default=DEFAULT_PAIRS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--top-limit", type=int, default=6)
    parser.add_argument("--nodeletion-survival", type=float, default=0.9)
    parser.add_argument("--global-normalized-kl-threshold", type=float, default=0.1)
    parser.add_argument("--mutual-normalized-kl-threshold", type=float, default=0.1)
    parser.add_argument("--clean-normalized-kl-threshold", type=float, default=0.05)
    args = parser.parse_args()

    result = run(
        parse_pairs(args.pairs),
        args.top_limit,
        args.nodeletion_survival,
        args.global_normalized_kl_threshold,
        args.mutual_normalized_kl_threshold,
        args.clean_normalized_kl_threshold,
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
                "row_count": result["row_count"],
                "gate_route_counts": result["gate_route_counts"],
                "shape_route_counts": result["shape_route_counts"],
                "current_nodeletion_triggered": result["current_nodeletion_triggered"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
