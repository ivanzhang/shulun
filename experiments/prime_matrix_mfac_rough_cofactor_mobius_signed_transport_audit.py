#!/usr/bin/env python3
"""生成 MFAC-1A 粗辅因子 Möbius 带符号传输状态审计证书。

用法示例：
  python3 experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py
  python3 experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py --limit 997

输出：
  data/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit-ledger.json
  docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.json
  docs/monograph/prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-mfac-rough-cofactor-mobius-signed-transport-audit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}.json"
OUT_MD = DOCS / f"{SLUG}.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-phi-lpf-bucket-signed-transport-router.json",
    DOCS / "prime-matrix-phi-lpf-affine-lpf-first-hit-von-mangoldt-lift-router.json",
    DOCS / "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json",
]


def prime_factors(value: int) -> tuple[int, ...]:
    """返回正整数的非递减素因子列，保留重数。"""
    if value < 1:
        raise ValueError("value 必须为正整数")
    remaining = value
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def least_prime_factor(value: int) -> int:
    """返回最小素因子；单位元 1 以 1 作为其明确状态标记。"""
    factors = prime_factors(value)
    return factors[0] if factors else 1


def mobius_values(limit: int) -> list[int]:
    """返回 0..limit 的 Möbius 值表。"""
    if limit < 0:
        raise ValueError("limit 不能为负")
    values = [1] * (limit + 1)
    is_prime = [True] * (limit + 1)
    if limit >= 0:
        values[0] = 0
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False
    for prime in range(2, limit + 1):
        if not is_prime[prime]:
            continue
        for multiple in range(prime, limit + 1, prime):
            is_prime[multiple] = False
            values[multiple] *= -1
        for multiple in range(prime * prime, limit + 1, prime * prime):
            values[multiple] = 0
    return values


def von_mangoldt(value: int) -> float:
    """返回 von Mangoldt 权重：素数幂为其底素数对数，其余为零。"""
    factors = prime_factors(value)
    if not factors or len(set(factors)) != 1:
        return 0.0
    return math.log(factors[0])


def verify_lambda_identity(value: int, mobius: list[int]) -> bool:
    """逐项核验 Lambda(n)=-sum_{d|n} mu(d)log(d)。"""
    divisor_sum = -sum(
        mobius[divisor] * math.log(divisor)
        for divisor in range(1, value + 1)
        if value % divisor == 0
    )
    return math.isclose(divisor_sum, von_mangoldt(value), abs_tol=1e-12)


def build_source_pairs(limit: int, mobius: list[int]) -> list[dict[str, object]]:
    """枚举每个 n<=limit 的全部非零 Möbius 除数 source pair。"""
    pairs: list[dict[str, object]] = []
    for value in range(1, limit + 1):
        for divisor in range(1, value + 1):
            if value % divisor != 0 or mobius[divisor] == 0:
                continue
            cofactor = value // divisor
            divisor_factors = prime_factors(divisor)
            pairs.append(
                {
                    "n": value,
                    "d": divisor,
                    "m": cofactor,
                    "mu_d": mobius[divisor],
                    "owner_lpf": least_prime_factor(value),
                    "rough_step_q": divisor_factors[-1] if divisor_factors else 1,
                    "log_d_parts": divisor_factors,
                }
            )
    return pairs


def lpf_local_state(
    pair: dict[str, object], *, include_divisor_history: bool
) -> tuple[object, ...]:
    """返回审计用 LPF-local 状态；默认不携带完整 Möbius 除数历史。"""
    base = (
        pair["owner_lpf"],
        pair["rough_step_q"],
        pair["m"],
    )
    return base + ((pair["log_d_parts"],) if include_divisor_history else ())


def payload_signature(pair: dict[str, object]) -> tuple[object, ...]:
    """返回 exact transport 不可省略的带符号 source payload。"""
    return (
        pair["mu_d"],
        pair["log_d_parts"],
        pair["d"],
        pair["m"],
    )


def find_minimal_collisions(pairs: list[dict[str, object]]) -> list[dict[str, object]]:
    """寻找同一 LPF-local state 却要求不同 exact payload 的最小见证。"""
    grouped: dict[tuple[object, ...], list[dict[str, object]]] = {}
    for pair in pairs:
        state = lpf_local_state(pair, include_divisor_history=False)
        grouped.setdefault(state, []).append(pair)

    witnesses: list[dict[str, object]] = []
    for state, members in grouped.items():
        payloads = {payload_signature(member) for member in members}
        if len(payloads) < 2:
            continue
        ordered = sorted(
            members,
            key=lambda item: (int(item["n"]), int(item["d"]), int(item["m"])),
        )
        first = ordered[0]
        second = next(
            member for member in ordered[1:] if payload_signature(member) != payload_signature(first)
        )
        witnesses.append(
            {
                "state": state,
                "members": [first, second],
            }
        )

    return sorted(
        witnesses,
        key=lambda item: tuple(int(member["n"]) for member in item["members"]),
    )


def has_payload_collision_with_divisor_history(pairs: list[dict[str, object]]) -> bool:
    """检查完整除数历史是否仍留下无法区分的 exact payload。"""
    grouped: dict[tuple[object, ...], set[tuple[object, ...]]] = {}
    for pair in pairs:
        state = lpf_local_state(pair, include_divisor_history=True)
        grouped.setdefault(state, set()).add(payload_signature(pair))
    return any(len(payloads) > 1 for payloads in grouped.values())


def source_pair_partition_verified(
    limit: int, mobius: list[int], pairs: list[dict[str, object]]
) -> bool:
    """核验每个非零 Möbius 除数恰好出现一次，且字段可由 (d,m) 重算。"""
    expected = {
        (value, divisor)
        for value in range(1, limit + 1)
        for divisor in range(1, value + 1)
        if value % divisor == 0 and mobius[divisor] != 0
    }
    actual = {(int(pair["n"]), int(pair["d"])) for pair in pairs}
    fields_valid = all(
        int(pair["n"]) == int(pair["d"]) * int(pair["m"])
        and int(pair["mu_d"]) == mobius[int(pair["d"])]
        and tuple(pair["log_d_parts"]) == prime_factors(int(pair["d"]))
        for pair in pairs
    )
    return actual == expected and len(actual) == len(pairs) and fields_valid


def sha256(path: Path) -> str:
    """计算依赖证书的 SHA-256 哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """返回本审计器和已存在输入证书的可复现哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def json_safe(value: object) -> object:
    """把元组递归转换为 JSON 可序列化列表。"""
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [json_safe(item) for item in value]
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def build_certificate(limit: int) -> dict[str, object]:
    """组装 MFAC-1A 局部状态碰撞审计证书。"""
    mobius = mobius_values(limit)
    pairs = build_source_pairs(limit, mobius)
    collisions = find_minimal_collisions(pairs)
    return {
        "certificate_type": "prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit",
        "status": "lpf_local_state_insufficient_for_exact_mobius_payload_audit",
        "verified_date": "2026-08-06",
        "sample_limit": limit,
        "mobius_von_mangoldt_identity_verified": all(
            verify_lambda_identity(value, mobius) for value in range(1, limit + 1)
        ),
        "source_pair_partition_verified": source_pair_partition_verified(limit, mobius, pairs),
        "source_pair_count": len(pairs),
        "lpf_local_state_collision_found": bool(collisions),
        "minimal_lpf_local_state_collision": collisions[0] if collisions else None,
        "divisor_history_augmentation_removes_payload_collision": not has_payload_collision_with_divisor_history(
            pairs
        ),
        "mfac_1a_constructed": False,
        "downstream_recovery_used": False,
        "balanced_typeii_remainder_constructed": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "全局 Möbius--von Mangoldt source pair 可逐项枚举，但仅以 owner LPF、"
            "当前 rough cofactor q 与 m 组成的局部状态会把不同 divisor-history 压到同一状态，"
            "并要求不同 Möbius 符号和 log(d) 分解。因此该 LPF-local 状态不足以构造 "
            "MFAC-1A 的 exact signed transport；必须保留完整 divisor-history 或等价的可追溯状态。"
        ),
        "source_hashes": source_hashes(),
    }


def render_markdown(certificate: dict[str, object]) -> str:
    """渲染人可读的 MFAC-1A 状态审计证书。"""
    collision = certificate["minimal_lpf_local_state_collision"]
    lines = [
        "# MFAC-1A 粗辅因子 Möbius 带符号传输状态审计",
        "",
        f"**状态：** `{certificate['status']}`",
        f"**核验日期：** `{certificate['verified_date']}`",
        "",
        "本审计只检验 source state 的充分性，不构造一般 signed transport，",
        "不提供平方根误差、零点排除或 RH 结论。",
        "",
        "## 1. 精确 source 恒等式",
        "",
        "```text",
        "Lambda(n) = - sum_{d|n} mu(d) log(d)",
        "```",
        "",
        "每个非零 Möbius 除数以 source pair `(d,m)`（其中 `n=d*m`）单独登记。",
        "",
        "## 2. 审计读数",
        "",
        "```text",
        "mobius_von_mangoldt_identity_verified="
        f"{str(certificate['mobius_von_mangoldt_identity_verified']).lower()}",
        "source_pair_partition_verified="
        f"{str(certificate['source_pair_partition_verified']).lower()}",
        f"source_pair_count={certificate['source_pair_count']}",
        "lpf_local_state_collision_found="
        f"{str(certificate['lpf_local_state_collision_found']).lower()}",
        "divisor_history_augmentation_removes_payload_collision="
        f"{str(certificate['divisor_history_augmentation_removes_payload_collision']).lower()}",
        "mfac_1a_constructed=false",
        "downstream_recovery_used=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 3. 最小碰撞",
        "",
    ]
    if isinstance(collision, dict):
        lines.append(f"LPF-local state: `{collision['state']}`")
        lines.append("")
        lines.extend(
            [
                "| source | n | d | m | mu(d) | log(d) factors |",
                "| --- | ---: | ---: | ---: | ---: | --- |",
            ]
        )
        for index, member in enumerate(collision["members"], start=1):
            lines.append(
                "| "
                f"{index} | {member['n']} | {member['d']} | {member['m']} | "
                f"{member['mu_d']} | {member['log_d_parts']} |"
            )
    else:
        lines.append("在当前有限范围未找到碰撞；该结果不能构成一般传输律。")

    lines.extend(
        [
            "",
            "## 4. 结论边界",
            "",
            str(certificate["plain_conclusion"]),
            "",
            "下一步必须把 source state 扩展为完整 divisor-history 或等价的可追溯状态，",
            "随后才可尝试定义推前前的 exact transport record。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in dict(certificate["source_hashes"]).items():
        lines.append(f"| `{path}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def write_certificate(certificate: dict[str, object]) -> None:
    """写出 data 与 docs 下的 machine-readable / human-readable 证书。"""
    serialized = json_safe(certificate)
    rendered_json = json.dumps(serialized, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(rendered_json, encoding="utf-8")
    OUT_JSON.write_text(rendered_json, encoding="utf-8")
    OUT_MD.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """运行审计并写出可复现证书。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=997)
    args = parser.parse_args()
    certificate = build_certificate(args.limit)
    write_certificate(certificate)
    print(
        "mobius_von_mangoldt_identity_verified="
        f"{str(certificate['mobius_von_mangoldt_identity_verified']).lower()}"
    )
    print(
        "lpf_local_state_collision_found="
        f"{str(certificate['lpf_local_state_collision_found']).lower()}"
    )
    print("mfac_1a_constructed=false")


if __name__ == "__main__":
    main()
