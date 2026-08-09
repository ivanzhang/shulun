"""MFAC 的 Mertens 分块随机性经验审计器。

用法示例::

    python3 experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py
    python3 experiments/prime_matrix_mfac_mertens_randomness_contraction_audit.py \
        --limit 4096 --block-length 64 --seed 17

本模块只生成有限范围的经验证书，不把代理模型升级为 Mellin 收缩定理。
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class BlockSummary:
    start: int
    length: int
    end: int
    delta_mertens: int
    zero_count: int
    layer_deltas: dict[int, int]
    values: list[int]
    reconstructs: bool


def mobius_and_omega_sieve(limit: int) -> tuple[list[int], list[int]]:
    """返回从 1 到 limit 的 Möbius 值和不同素因子数。"""
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 1:
        raise ValueError("limit 必须是至少为 1 的整数")
    mobius = [1] * (limit + 1)
    omega = [0] * (limit + 1)
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for prime in range(2, limit + 1):
        if not is_prime[prime]:
            continue
        for multiple in range(prime, limit + 1, prime):
            is_prime[multiple] = False
            omega[multiple] += 1
            mobius[multiple] *= -1
        for multiple in range(prime * prime, limit + 1, prime * prime):
            mobius[multiple] = 0
    return mobius, omega


def summarize_block(
    mobius: Sequence[int], omega: Sequence[int], start: int, length: int
) -> BlockSummary:
    """汇总区间 (start, start + length]，并按 omega 分层。"""
    if start < 0 or length < 1 or start + length >= len(mobius):
        raise ValueError("区块必须落在筛法范围内，且长度至少为 1")
    values = list(mobius[start + 1 : start + length + 1])
    layer_deltas: dict[int, int] = {}
    zero_count = 0
    for number, value in zip(range(start + 1, start + length + 1), values):
        if value == 0:
            zero_count += 1
        else:
            layer = omega[number]
            layer_deltas[layer] = layer_deltas.get(layer, 0) + value
    delta_mertens = sum(values)
    return BlockSummary(
        start=start,
        length=length,
        end=start + length,
        delta_mertens=delta_mertens,
        zero_count=zero_count,
        layer_deltas=layer_deltas,
        values=values,
        reconstructs=delta_mertens == sum(layer_deltas.values()),
    )


def collect_dyadic_blocks(
    mobius: Sequence[int], omega: Sequence[int], block_length: int
) -> list[BlockSummary]:
    """按固定宽度收集从 1 开始的连续区块。"""
    if block_length < 1:
        raise ValueError("block_length 必须至少为 1")
    limit = len(mobius) - 1
    blocks = []
    start = 0
    while start + block_length <= limit:
        blocks.append(summarize_block(mobius, omega, start, block_length))
        start += block_length
    return blocks


def summarize_samples(values: Sequence[float]) -> dict[str, Any]:
    """返回经验矩、符号偏差和固定尾部计数；不声明正态性。"""
    if not values:
        raise ValueError("样本不能为空")
    numeric = [float(value) for value in values]
    mean = sum(numeric) / len(numeric)
    variance = sum((value - mean) ** 2 for value in numeric) / len(numeric)
    zero_count = sum(value == 0 for value in numeric)
    nonzero = [value for value in numeric if value != 0]
    sign_bias = (sum(value > 0 for value in nonzero) - sum(value < 0 for value in nonzero)) / len(nonzero) if nonzero else 0.0
    tail_counts = {"abs_ge_1": sum(abs(value) >= 1 for value in numeric), "abs_ge_2": sum(abs(value) >= 2 for value in numeric)}
    result: dict[str, Any] = {
        "sample_count": len(numeric),
        "zero_count": zero_count,
        "sign_bias": sign_bias,
        "mean": mean,
        "variance": variance,
        "degenerate_variance": variance == 0.0,
        "tail_counts": tail_counts,
    }
    if variance == 0.0:
        result.update({"standardized_skewness": None, "excess_kurtosis": None})
        return result
    scale = math.sqrt(variance)
    standardized = [(value - mean) / scale for value in numeric]
    result.update({
        "standardized_skewness": sum(value ** 3 for value in standardized) / len(standardized),
        "excess_kurtosis": sum(value ** 4 for value in standardized) / len(standardized) - 3.0,
    })
    return result


def independent_sign_baseline(values: Sequence[int], seed: int) -> list[int]:
    """保留零项、对非零项独立重采样符号的经验代理。"""
    generator = random.Random(seed)
    return [0 if value == 0 else generator.choice((-1, 1)) for value in values]


def layer_shuffle_baseline(layers: Mapping[int, Sequence[int]], seed: int) -> dict[int, list[int]]:
    """在每个 omega 层内洗牌，保持各层多重集不变。"""
    generator = random.Random(seed)
    shuffled: dict[int, list[int]] = {}
    for layer, values in sorted(layers.items()):
        shuffled[layer] = list(values)
        generator.shuffle(shuffled[layer])
    return shuffled


def diagnose_layer_shuffle(layers: Mapping[int, Sequence[int]]) -> dict[str, bool | str]:
    """判定层内洗牌是否因层内符号恒定而退化。"""
    deterministic = all(len(set(values)) <= 1 for values in layers.values())
    return {
        "sign_deterministic_by_layer": deterministic,
        "comparison_status": (
            "degenerate_not_independent_baseline"
            if deterministic
            else "nondegenerate_empirical_permutation_only"
        ),
    }


def build_proxy_baselines(values: Sequence[int], layers: Mapping[int, Sequence[int]], seed: int) -> dict[str, Any]:
    """构造三类代理的状态摘要，第三类明确标记未实现。"""
    independent = independent_sign_baseline(values, seed)
    shuffled = layer_shuffle_baseline(layers, seed)
    return {
        "status": "empirical_proxy_baselines_only",
        "seed": seed,
        "independent_sign": summarize_samples(independent),
        "layer_shuffle": {str(layer): summarize_samples(items) for layer, items in shuffled.items()},
        "layer_shuffle_diagnosis": diagnose_layer_shuffle(layers),
        "local_constraint_proxy": "not_implemented_with_actual_local_constraints",
        "actual_mellin_contraction_present": False,
    }


REQUIRED_CONTRACTION_FIELDS = (
    "fixed_actual_integer_embedding", "exact_mobius_block_decomposition",
    "deterministic_dyadic_block_family", "uniform_signed_block_covariance_bound",
    "uniform_higher_cumulant_defect_bound", "uniform_large_deviation_or_high_moment_bound",
    "explicit_layer_interaction_identity", "noncircular_offconstant_coercive_energy_identity",
    "scale_summability_to_mellin_norm", "no_use_of_RH_or_zero_free_input",
)


def complete_synthetic_contraction_contract() -> dict[str, bool]:
    return {field: True for field in REQUIRED_CONTRACTION_FIELDS}


def classify_contraction_contract(contract: Mapping[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_CONTRACTION_FIELDS if contract.get(field) is not True]
    complete = not missing
    return {
        "status": "synthetic_contract_not_actual_proof" if complete else "empirical_randomness_model_not_a_rh_proof",
        "missing_contract_fields": missing,
        "contract_complete": complete,
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
    }


def audit_mertens_randomness(limit: int, block_length: int, seed: int) -> dict[str, Any]:
    mobius, omega = mobius_and_omega_sieve(limit)
    blocks = collect_dyadic_blocks(mobius, omega, block_length)
    layer_values: dict[int, list[int]] = {}
    for block in blocks:
        for number in range(block.start + 1, block.end + 1):
            if mobius[number] != 0:
                layer_values.setdefault(omega[number], []).append(mobius[number])
    certificate = {
        "certificate_type": "prime_matrix_mfac_mertens_randomness_contraction_audit",
        "status": "empirical_randomness_model_not_a_rh_proof",
        "parameters": {"limit": limit, "block_length": block_length, "seed": seed},
        "block_count": len(blocks),
        "degenerate_block_count": sum(summarize_samples([block.delta_mertens])["degenerate_variance"] for block in blocks),
        "layer_reconstruction_holds": all(block.reconstructs for block in blocks),
        "proxy_baselines": build_proxy_baselines([block.delta_mertens for block in blocks], layer_values, seed),
        "contraction_contract": classify_contraction_contract({}),
        "actual_mellin_contraction_present": False,
        "rh_proved": False,
        "next_positive_gate": "ActualMertensBlockDefectToOffConstantCoerciveEnergyLawBeforeMellin",
        "limitations": ["有限范围经验统计不等于概率定理", "代理基线不等于真实 Möbius 动力学", "不构成 RH 证明"],
    }
    return certificate


def write_certificate(certificate: Mapping[str, Any], json_path: Path, markdown_path: Path) -> None:
    json_path = Path(json_path)
    markdown_path = Path(markdown_path)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    markdown_path.write_text(
        "# MFAC Mertens 随机性缺陷审计\n\n"
        f"- 状态：`{certificate['status']}`\n"
        f"- 区块重构：`{certificate['layer_reconstruction_holds']}`\n"
        "- 实际 Mellin 收缩：`false`\n"
        "- RH 证明：`false`\n\n"
        "本证书只记录有限范围的经验读数与代理比较。按 `omega(n)` 分层的层内洗牌"
        "可能因符号恒定而退化，不能视为独立基线；本证书**不构成 RH 证明**。\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="生成 MFAC Mertens 随机性经验审计证书")
    parser.add_argument("--limit", type=int, default=4096)
    parser.add_argument("--block-length", type=int, default=64)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--json-out", type=Path, default=Path("docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.json"))
    parser.add_argument("--markdown-out", type=Path, default=Path("docs/monograph/prime-matrix-mfac-mertens-randomness-contraction-audit.md"))
    args = parser.parse_args()
    write_certificate(audit_mertens_randomness(args.limit, args.block_length, args.seed), args.json_out, args.markdown_out)


if __name__ == "__main__":
    main()
