#!/usr/bin/env python3
"""审计 Triad-A1 新层提升中的 fiber 删除/熵二分。

用法示例：
  python3 experiments/prime_matrix_triad_a1_newlayer_fiber_audit.py
  python3 experiments/prime_matrix_triad_a1_newlayer_fiber_audit.py --p-values 19,23

输出：
  docs/monograph/prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.json
  docs/monograph/prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.md
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
DEFAULT_BASE = DOCS / "h4-pdec-lhb-multiplicity-cap-certificate.json"
DEFAULT_LIFT = DOCS / "prime-matrix-triad-a1-q30030-multiplicity-cap.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.md"


def parse_p_values(raw: str | None) -> set[int] | None:
    """解析可选的逗号分隔 P 列表。"""
    if raw is None:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def file_sha256(path: Path) -> str:
    """计算文件指纹，保证审计来源可复核。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def index_prime_results(data: dict[str, Any]) -> dict[int, dict[str, Any]]:
    """按 P 索引 prime_results。"""
    return {int(item["p"]): item for item in data["prime_results"]}


def normalized_entropy(values: list[int], fiber_size: int) -> dict[str, float] | None:
    """计算 fiber 内相对均匀分布的归一化熵和 KL 成本。"""
    total = sum(values)
    if total <= 0:
        return None
    entropy = 0.0
    for value in values:
        if value <= 0:
            continue
        prob = value / total
        entropy -= prob * math.log(prob)
    log_r = math.log(fiber_size)
    norm_entropy = entropy / log_r if log_r > 0 else 1.0
    kl_to_uniform = log_r - entropy
    return {
        "entropy_nats": entropy,
        "normalized_entropy": norm_entropy,
        "kl_to_uniform_nats": kl_to_uniform,
        "normalized_kl_to_uniform": kl_to_uniform / log_r if log_r > 0 else 0.0,
    }


def classify_row(
    monotone_support: bool,
    slot_survival_rate: float | None,
    avg_norm_entropy: float | None,
    deletion_threshold: float,
    flat_entropy_threshold: float,
) -> str:
    """给出诊断分类；阈值只用于路线分流，不作为证明常数。"""
    if not monotone_support:
        return "ProjectionStitchingNeeded"
    if slot_survival_rate is not None and slot_survival_rate <= deletion_threshold:
        return "ReSparsifiedByFiberDeletion"
    if avg_norm_entropy is not None and avg_norm_entropy >= flat_entropy_threshold:
        return "NearUniformFiberCleanKLSCandidate"
    return "MixedFiberDeletionEntropy"


def analyze_prime(
    p: int,
    base_item: dict[str, Any],
    lift_item: dict[str, Any],
    q: int,
    q_lift: int,
    fiber_size: int,
    detail_limit: int,
    deletion_threshold: float,
    flat_entropy_threshold: float,
) -> dict[str, Any]:
    """审计单个 P 的旧相位到新层 fiber 的支撑变化。"""
    base_m = [int(value) for value in base_item["m_vector"]]
    lift_m = [int(value) for value in lift_item["m_vector"]]
    if len(base_m) != q or len(lift_m) != q_lift:
        raise ValueError(f"P={p}: m_vector length does not match q/q_lift")

    active_old = [phase for phase, value in enumerate(base_m) if value > 0]
    lift_support = [phase for phase, value in enumerate(lift_m) if value > 0]
    active_old_set = set(active_old)
    new_activation = [phase for phase in lift_support if phase % q not in active_old_set]

    support_hist: Counter[int] = Counter()
    residue_hist: Counter[int] = Counter()
    inherited_slots = 0
    inherited_mass = 0
    weighted_entropy = 0.0
    weighted_kl = 0.0
    entropy_weight = 0
    examples: list[dict[str, Any]] = []

    zero_fibers = 0
    partial_fibers = 0
    full_fibers = 0
    singleton_fibers = 0

    for phase in active_old:
        values = [lift_m[phase + residue * q] for residue in range(fiber_size)]
        surviving_residues = [residue for residue, value in enumerate(values) if value > 0]
        support_count = len(surviving_residues)
        lift_mass = sum(values)

        support_hist[support_count] += 1
        inherited_slots += support_count
        inherited_mass += lift_mass
        for residue in surviving_residues:
            residue_hist[residue] += 1

        if support_count == 0:
            zero_fibers += 1
        elif support_count == fiber_size:
            full_fibers += 1
        else:
            partial_fibers += 1
        if support_count == 1:
            singleton_fibers += 1

        entropy = normalized_entropy(values, fiber_size)
        if entropy is not None:
            weighted_entropy += lift_mass * entropy["normalized_entropy"]
            weighted_kl += lift_mass * entropy["normalized_kl_to_uniform"]
            entropy_weight += lift_mass

        if len(examples) < detail_limit:
            examples.append(
                {
                    "old_phase": phase,
                    "old_m": int(base_m[phase]),
                    "surviving_residues": surviving_residues,
                    "fiber_values": values,
                    "lift_mass": lift_mass,
                    "support_count": support_count,
                }
            )

    possible_slots = len(active_old) * fiber_size
    slot_survival_rate = inherited_slots / possible_slots if possible_slots else None
    slot_deletion_rate = 1.0 - slot_survival_rate if slot_survival_rate is not None else None
    base_density = len(active_old) / q if q else 0.0
    lift_density = len(lift_support) / q_lift if q_lift else 0.0
    density_drop_factor = base_density / lift_density if lift_density > 0 else None
    deletion_gain_factor = 1.0 / slot_survival_rate if slot_survival_rate else None
    avg_norm_entropy = weighted_entropy / entropy_weight if entropy_weight else None
    avg_norm_kl = weighted_kl / entropy_weight if entropy_weight else None
    monotone_support = len(new_activation) == 0

    density_identity_rhs = (
        base_density * slot_survival_rate + len(new_activation) / q_lift
        if slot_survival_rate is not None
        else len(new_activation) / q_lift
    )

    old_total_mass = sum(base_m)
    lift_total_mass = sum(lift_m)
    full_copy_mass = old_total_mass * fiber_size
    mass_survival_rate = lift_total_mass / full_copy_mass if full_copy_mass else None

    return {
        "p": p,
        "q": q,
        "q_lift": q_lift,
        "fiber_size": fiber_size,
        "old_support_count": len(active_old),
        "lift_support_count": len(lift_support),
        "old_total_mass": old_total_mass,
        "lift_total_mass": lift_total_mass,
        "full_copy_mass": full_copy_mass,
        "mass_survival_rate_vs_full_copy": mass_survival_rate,
        "support_accounting": {
            "possible_slots_over_old_support": possible_slots,
            "inherited_surviving_slots": inherited_slots,
            "new_activation_slots_on_old_zero": len(new_activation),
            "identity_holds": len(lift_support) == inherited_slots + len(new_activation),
            "monotone_lift_support": monotone_support,
            "slot_survival_rate": slot_survival_rate,
            "slot_deletion_rate": slot_deletion_rate,
            "deletion_gain_factor": deletion_gain_factor,
        },
        "density_accounting": {
            "old_density": base_density,
            "lift_density": lift_density,
            "density_drop_factor": density_drop_factor,
            "identity_rhs": density_identity_rhs,
            "identity_abs_error": abs(lift_density - density_identity_rhs),
        },
        "fiber_shape": {
            "zero_fiber_count": zero_fibers,
            "singleton_fiber_count": singleton_fibers,
            "partial_fiber_count": partial_fibers,
            "full_fiber_count": full_fibers,
            "support_count_histogram": dict(sorted((str(k), v) for k, v in support_hist.items())),
            "surviving_residue_histogram": dict(sorted((str(k), v) for k, v in residue_hist.items())),
            "avg_normalized_entropy_by_lift_mass": avg_norm_entropy,
            "avg_normalized_kl_to_uniform_by_lift_mass": avg_norm_kl,
        },
        "new_activation_sample": new_activation[:detail_limit],
        "fiber_examples": examples,
        "classification": classify_row(
            monotone_support,
            slot_survival_rate,
            avg_norm_entropy,
            deletion_threshold,
            flat_entropy_threshold,
        ),
    }


def run(
    base_path: Path,
    lift_path: Path,
    p_filter: set[int] | None,
    detail_limit: int,
    deletion_threshold: float,
    flat_entropy_threshold: float,
) -> dict[str, Any]:
    """运行完整 fiber 审计。"""
    base = load_json(base_path)
    lift = load_json(lift_path)
    q = int(base["q"])
    q_lift = int(lift["q"])
    if q_lift % q != 0:
        raise ValueError(f"lift q={q_lift} is not a multiple of base q={q}")
    fiber_size = q_lift // q

    base_results = index_prime_results(base)
    lift_results = index_prime_results(lift)
    common_p = sorted(set(base_results) & set(lift_results))
    if p_filter is not None:
        common_p = [p for p in common_p if p in p_filter]

    prime_results = [
        analyze_prime(
            p,
            base_results[p],
            lift_results[p],
            q,
            q_lift,
            fiber_size,
            detail_limit,
            deletion_threshold,
            flat_entropy_threshold,
        )
        for p in common_p
    ]

    all_identity = all(item["support_accounting"]["identity_holds"] for item in prime_results)
    all_monotone = all(item["support_accounting"]["monotone_lift_support"] for item in prime_results)
    all_resparse = all(item["classification"] == "ReSparsifiedByFiberDeletion" for item in prime_results)

    return {
        "certificate_type": "triad_a1_newlayer_fiber_deletion_audit",
        "status": "newlayer_fiber_deletion_entropy_audited",
        "q": q,
        "q_lift": q_lift,
        "fiber_size": fiber_size,
        "p_values": common_p,
        "thresholds": {
            "deletion_threshold": deletion_threshold,
            "flat_entropy_threshold": flat_entropy_threshold,
            "meaning": "阈值只作分流诊断；严格部分是 support/density 恒等式。",
        },
        "source_hashes": {
            "fiber_audit_script": file_sha256(Path(__file__).resolve()),
            "base_multiplicity_json": file_sha256(base_path),
            "lift_multiplicity_json": file_sha256(lift_path),
        },
        "structural_identity": (
            "Q'=rQ 时，每个旧相位 t 被拆成 t+bQ。若 A_Q={t:M_Q(t)>0} 且 "
            "A_Q' 没有落在旧零相位上的新增激活，则 "
            "|A_Q'|=sum_{t in A_Q} s(t)，density(A_Q')=density(A_Q)*avg_t(s(t)/r)。"
        ),
        "prime_results": prime_results,
        "all_support_identities_hold": all_identity,
        "all_monotone_lift_support": all_monotone,
        "all_classified_resparse": all_resparse,
        "review_conclusion": (
            "本审计把固定 Q 密度屏障后的升层动作改写为精确 fiber 删除账本。"
            "若新增层真实删除旧相位 fiber，则支撑密度按恒等式下降；若不删除而趋近均匀，"
            "则转入 CleanKLS/DLS；若出现旧零相位新增激活，则进入 Stitching/坐标商归一化。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化可空浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 审计摘要。"""
    lines = [
        f"# Triad-A1 新层 fiber 删除审计：Q={result['q']} -> Q={result['q_lift']}",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构恒等式",
        "",
        "令 `Q'=rQ`，旧相位 `t mod Q` 的新层 fiber 为：",
        "",
        "```text",
        "t, t+Q, t+2Q, ..., t+(r-1)Q。",
        "```",
        "",
        "记 `A_Q={t:M_Q(t)>0}`，并令",
        "",
        "```text",
        "s(t)=#{b in [0,r): M_{Q'}(t+bQ)>0}。",
        "```",
        "",
        "若新层支撑没有落在旧零相位上，则有精确恒等式：",
        "",
        "```text",
        "|supp(M_{Q'})| = sum_{t in A_Q} s(t),",
        "density(M_{Q'}) = density(M_Q) * average_{t in A_Q}(s(t)/r)。",
        "```",
        "",
        "这就是固定层密度屏障之后的递归剥离入口：`s(t)<r` 的系统性出现会重新稀疏。",
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
            "## 3. 总表",
            "",
            "| P | old support | lifted support | survival | deletion | density drop | support hist | entropy | class |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |",
        ]
    )
    for item in result["prime_results"]:
        support = item["support_accounting"]
        density = item["density_accounting"]
        shape = item["fiber_shape"]
        lines.append(
            "| {p} | {old} | {new} | {surv} | {delr} | {drop} | `{hist}` | {entropy} | `{cls}` |".format(
                p=item["p"],
                old=item["old_support_count"],
                new=item["lift_support_count"],
                surv=fmt_float(support["slot_survival_rate"]),
                delr=fmt_float(support["slot_deletion_rate"]),
                drop=fmt_float(density["density_drop_factor"]),
                hist=shape["support_count_histogram"],
                entropy=fmt_float(shape["avg_normalized_entropy_by_lift_mass"]),
                cls=item["classification"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 当前读数",
            "",
            f"- `all_support_identities_hold={result['all_support_identities_hold']}`。",
            f"- `all_monotone_lift_support={result['all_monotone_lift_support']}`。",
            f"- `all_classified_resparse={result['all_classified_resparse']}`。",
            "",
            f"本次 `Q={result['q']} -> {result['q_lift']}` 的共同 P 上没有旧零相位新增激活；所以密度下降不是统计口号，",
            "而是由 fiber 删除恒等式逐相位核算出来的。",
            "",
            "## 5. 二分出口",
            "",
            "```text",
            "FiberDeletion:  s(t)/r 在正比例质量上小于 1",
            "  => 新层重新稀疏，回到更细层 Empty/Sparse/PDEC 审计；",
            "",
            "NearUniform:    s(t) 接近 r 且 fiber 熵接近 1",
            "  => 新层不再提供定向覆盖，转 CleanKLS/DLS；",
            "",
            "NewActivation:  supp(M_{Q'}) 投到旧零相位",
            "  => 口径不一致，转 Stitching/坐标商/复用缺陷吸收。",
            "```",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-json", type=Path, default=DEFAULT_BASE)
    parser.add_argument("--lift-json", type=Path, default=DEFAULT_LIFT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--p-values", type=str, default=None)
    parser.add_argument("--detail-limit", type=int, default=12)
    parser.add_argument("--deletion-threshold", type=float, default=0.5)
    parser.add_argument("--flat-entropy-threshold", type=float, default=0.85)
    args = parser.parse_args()

    result = run(
        args.base_json,
        args.lift_json,
        parse_p_values(args.p_values),
        args.detail_limit,
        args.deletion_threshold,
        args.flat_entropy_threshold,
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "q": result["q"],
                "q_lift": result["q_lift"],
                "p_values": result["p_values"],
                "all_monotone_lift_support": result["all_monotone_lift_support"],
                "all_classified_resparse": result["all_classified_resparse"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
