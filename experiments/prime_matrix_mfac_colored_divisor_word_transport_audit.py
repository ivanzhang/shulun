#!/usr/bin/env python3
"""生成 MFAC-1B 双色除数字词传输审计。

用法示例：
  python3 experiments/prime_matrix_mfac_colored_divisor_word_transport_audit.py --limit 997
"""

from __future__ import annotations

import math
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit import (
    mobius_values,
    prime_factors,
    von_mangoldt,
)


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-colored-divisor-word-transport-audit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}.json"
OUT_MD = DOCS / f"{SLUG}.md"


def is_prime(value: int) -> bool:
    """判断正整数是否为素数。"""
    return value >= 2 and prime_factors(value) == (value,)


def product(values: tuple[int, ...]) -> int:
    """计算整数元组的乘积。"""
    result = 1
    for value in values:
        result *= value
    return result


def color_factor_occurrences(factors: tuple[int, ...], divisor: int) -> tuple[str, ...]:
    """按从左到右约定，把 squarefree divisor 的因子标成唯一 D 色位置。"""
    if divisor < 1 or product(factors) % divisor != 0:
        raise ValueError("divisor 必须整除原整数")
    divisor_factors = prime_factors(divisor)
    if len(set(divisor_factors)) != len(divisor_factors):
        raise ValueError("双色 source record 只接收非零 Möbius 的 squarefree divisor")
    selected = set(divisor_factors)
    used: set[int] = set()
    colors: list[str] = []
    for factor in factors:
        if factor in selected and factor not in used:
            colors.append("D")
            used.add(factor)
        else:
            colors.append("E")
    if used != selected:
        raise ValueError("divisor 因子无法映射到完整因子词")
    return tuple(colors)


def selected_d_factors(factors: tuple[int, ...], colors: tuple[str, ...]) -> tuple[int, ...]:
    """从双色词中恢复 D 色除数因子。"""
    return tuple(factor for factor, color in zip(factors, colors, strict=True) if color == "D")


def mobius_from_selected_factors(factors: tuple[int, ...]) -> int:
    """计算 D 色因子的 Möbius 值；重复因子显式给出零。"""
    if len(set(factors)) != len(factors):
        return 0
    return -1 if len(factors) % 2 else 1


def build_colored_record(n: int, divisor: int) -> dict[str, object]:
    """构造保留完整 D/E 历史的 nonzero Möbius source record。"""
    if n < 2:
        raise ValueError("n 必须至少为 2")
    factors = prime_factors(n)
    colors = color_factor_occurrences(factors, divisor)
    selected = selected_d_factors(factors, colors)
    mu_d = mobius_from_selected_factors(selected)
    if mu_d == 0:
        raise ValueError("source record 不能携带零 Möbius divisor")
    return {
        "n": n,
        "owner_p": factors[0],
        "factor_word": factors,
        "color_word": colors,
        "divisor": divisor,
        "cofactor": n // divisor,
        "mu_d": mu_d,
        "log_d_parts": selected,
    }


def reconstruct_source_pair(record: dict[str, object]) -> tuple[int, int]:
    """从完整双色词精确重构 `(d,e)`。"""
    factors = tuple(record["factor_word"])
    colors = tuple(record["color_word"])
    selected = selected_d_factors(factors, colors)
    complement = tuple(
        factor for factor, color in zip(factors, colors, strict=True) if color == "E"
    )
    return product(selected), product(complement)


def extend_record(record: dict[str, object], *, q: int, color: str) -> dict[str, object]:
    """把素数 q 追加到非降词末端，并由新词重新构造全部字段。"""
    if color not in {"D", "E"}:
        raise ValueError("color 必须为 D 或 E")
    factors = tuple(record["factor_word"])
    if not is_prime(q) or q < factors[-1]:
        raise ValueError("q 必须是至少不小于当前词尾的素数")
    divisor, _ = reconstruct_source_pair(record)
    next_divisor = divisor * q if color == "D" else divisor
    return build_colored_record(int(record["n"]) * q, next_divisor)


def append_rough_factor(record: dict[str, object], q: int) -> dict[str, object]:
    """追加粗辅因子 q，返回 E、D 或零 Möbius D 分支。"""
    e_branch = extend_record(record, q=q, color="E")
    selected = selected_d_factors(tuple(record["factor_word"]), tuple(record["color_word"]))
    if q in selected:
        return {
            "E": e_branch,
            "D": None,
            "D_return_tag": "zero_mobius_repeated_divisor_prime",
        }
    return {
        "E": e_branch,
        "D": extend_record(record, q=q, color="D"),
        "D_return_tag": None,
    }


def source_payload(record: dict[str, object]) -> float:
    """返回 source pair 对应的精确 Möbius--von Mangoldt payload。"""
    return -int(record["mu_d"]) * sum(math.log(factor) for factor in record["log_d_parts"])


def nonzero_mobius_divisors(value: int, mobius: list[int]) -> list[int]:
    """列出 value 的所有非零 Möbius 除数。"""
    return [
        divisor
        for divisor in range(1, value + 1)
        if value % divisor == 0 and mobius[divisor] != 0
    ]


def verify_one_step(record: dict[str, object]) -> tuple[bool, dict[str, object] | None]:
    """用词尾素数验证一次 D/E 追加与直接 child 重建一致。"""
    q = int(tuple(record["factor_word"])[-1])
    branches = append_rough_factor(record, q)
    e_branch = branches["E"]
    parent_divisor, parent_cofactor = reconstruct_source_pair(record)
    e_ok = reconstruct_source_pair(e_branch) == (parent_divisor, parent_cofactor * q)
    d_branch = branches["D"]
    if d_branch is None:
        return e_ok, {
            "parent": record,
            "q": q,
            "return_tag": branches["D_return_tag"],
        }
    d_ok = reconstruct_source_pair(d_branch) == (parent_divisor * q, parent_cofactor)
    d_ok = d_ok and int(d_branch["mu_d"]) == -int(record["mu_d"])
    return e_ok and d_ok, None


def sha256(path: Path) -> str:
    """计算输入脚本的 SHA-256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_safe(value: object) -> object:
    """递归把元组转换为 JSON 列表。"""
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [json_safe(item) for item in value]
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def build_certificate(limit: int) -> dict[str, object]:
    """审计 `n<=limit` 的 record 重构、一步传输与 payload 守恒。"""
    mobius = mobius_values(limit)
    reconstruction_ok = True
    one_step_ok = True
    conservation_ok = True
    record_count = 0
    zero_branch_sample: dict[str, object] | None = None
    payload_failures: list[int] = []
    for value in range(2, limit + 1):
        total_payload = 0.0
        for divisor in nonzero_mobius_divisors(value, mobius):
            record = build_colored_record(value, divisor)
            record_count += 1
            reconstruction_ok = reconstruction_ok and reconstruct_source_pair(record) == (
                divisor,
                value // divisor,
            )
            step_ok, zero_sample = verify_one_step(record)
            one_step_ok = one_step_ok and step_ok
            if zero_branch_sample is None and zero_sample is not None:
                zero_branch_sample = zero_sample
            total_payload += source_payload(record)
        if not math.isclose(total_payload, von_mangoldt(value), abs_tol=1e-12):
            conservation_ok = False
            payload_failures.append(value)
    return {
        "certificate_type": "prime_matrix_mfac_colored_divisor_word_transport_audit",
        "status": "colored_divisor_word_arithmetic_transport_closed_actual_primitive_binding_open",
        "verified_date": "2026-08-06",
        "sample_limit": limit,
        "record_count": record_count,
        "record_reconstruction_verified": reconstruction_ok,
        "one_step_transport_verified": one_step_ok,
        "global_payload_conservation_verified": conservation_ok,
        "first_payload_failure": payload_failures[0] if payload_failures else None,
        "zero_mobius_branch_sample": zero_branch_sample,
        "actual_primitive_unit_binding_constructed": False,
        "mfac_1a_general_transport_constructed": False,
        "downstream_recovery_used": False,
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "完整 D/E divisor-history 可在有限范围内逐项重构 source pair，并在追加词尾粗辅因子时"
            "给出精确 E、D 或零 Möbius 分支；按 n 汇总的 payload 恢复 Lambda(n)。"
            "这只是全局 arithmetic pre-pushforward transport，尚未构造 actual primitive unit 绑定。"
        ),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            "experiments/prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py": sha256(
                ROOT / "experiments" / "prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit.py"
            ),
        },
    }


def render_markdown(certificate: dict[str, object]) -> str:
    """渲染人可读证书。"""
    lines = [
        "# MFAC-1B 双色除数字词 pre-pushforward 传输审计",
        "",
        f"**状态：** `{certificate['status']}`",
        f"**核验日期：** `{certificate['verified_date']}`",
        "",
        "本证书只闭合全局 arithmetic 双色词传输；不构造 actual primitive unit 绑定，",
        "不提供 Type-II 平方根界、零点排除或 RH 结论。",
        "",
        "## 审计读数",
        "",
        "```text",
        f"record_reconstruction_verified={str(certificate['record_reconstruction_verified']).lower()}",
        f"one_step_transport_verified={str(certificate['one_step_transport_verified']).lower()}",
        f"global_payload_conservation_verified={str(certificate['global_payload_conservation_verified']).lower()}",
        "actual_primitive_unit_binding_constructed=false",
        "mfac_1a_general_transport_constructed=false",
        "downstream_recovery_used=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 结论边界",
        "",
        str(certificate["plain_conclusion"]),
        "",
        "下一关：把该 global colored-word record 无循环地绑定到 actual primitive unit，"
        "或输出最小 orientation/multiplicity/return-tag collision。",
        "",
        "## 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in dict(certificate["source_hashes"]).items():
        lines.append(f"| `{path}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def write_certificate(certificate: dict[str, object]) -> None:
    """写出 ledger、JSON 和 Markdown 证书。"""
    rendered_json = json.dumps(json_safe(certificate), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(rendered_json, encoding="utf-8")
    OUT_JSON.write_text(rendered_json, encoding="utf-8")
    OUT_MD.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """运行有限审计并输出证书。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=997)
    args = parser.parse_args()
    certificate = build_certificate(args.limit)
    write_certificate(certificate)
    for key in (
        "record_reconstruction_verified",
        "one_step_transport_verified",
        "global_payload_conservation_verified",
    ):
        print(f"{key}={str(certificate[key]).lower()}")
    print("actual_primitive_unit_binding_constructed=false")


if __name__ == "__main__":
    main()
