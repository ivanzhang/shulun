#!/usr/bin/env python3
"""生成 MFAC 平方基 global seed 与 primitive-binding 缺口审计。

用法示例：
  python3 experiments/prime_matrix_mfac_square_base_seed_binding_audit.py --prime-limit 997
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from prime_matrix_mfac_colored_divisor_word_transport_audit import (
    build_colored_record,
    source_payload,
)
from prime_matrix_mfac_rough_cofactor_mobius_signed_transport_audit import mobius_values


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-square-base-seed-binding-audit"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}.json"
OUT_MD = DOCS / f"{SLUG}.md"


def primes_up_to(limit: int) -> list[int]:
    """返回不超过 limit 的素数。"""
    return [
        value
        for value in range(2, limit + 1)
        if all(value % divisor for divisor in range(2, math.isqrt(value) + 1))
    ]


def square_base_active_source(prime: int) -> dict[str, object]:
    """返回 p² 上唯一携带非零 payload 的 global colored-word source。"""
    record = build_colored_record(prime * prime, prime)
    return {
        **record,
        "payload": source_payload(record),
    }


def audit_prime(prime: int) -> dict[str, object]:
    """验证 p² 的所有非零 Möbius divisor 中仅 d=p 携带非零 payload。"""
    mobius = mobius_values(prime * prime)
    records = [
        build_colored_record(prime * prime, divisor)
        for divisor in range(1, prime * prime + 1)
        if (prime * prime) % divisor == 0 and mobius[divisor] != 0
    ]
    active = [{**record, "payload": source_payload(record)} for record in records if source_payload(record)]
    seed = square_base_active_source(prime)
    return {
        "prime": prime,
        "source_count": len(records),
        "active_source_count": len(active),
        "active_source": active[0] if active else None,
        "unique_active_source_verified": len(active) == 1 and active[0]["divisor"] == prime,
        "payload_equals_log_prime": math.isclose(seed["payload"], math.log(prime), abs_tol=1e-12),
    }


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_safe(value: object) -> object:
    """递归转换元组以供 JSON 序列化。"""
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [json_safe(item) for item in value]
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def build_certificate(prime_limit: int) -> dict[str, object]:
    """组装平方基 global seed 审计证书。"""
    rows = [audit_prime(prime) for prime in primes_up_to(prime_limit)]
    return {
        "certificate_type": "prime_matrix_mfac_square_base_seed_binding_audit",
        "status": "global_square_base_mobius_seed_closed_actual_primitive_binding_open",
        "verified_date": "2026-08-07",
        "prime_limit": prime_limit,
        "global_square_base_seed_verified": all(row["payload_equals_log_prime"] for row in rows),
        "unique_active_source_verified": all(row["unique_active_source_verified"] for row in rows),
        "actual_square_base_signed_coefficient_bound": False,
        "primitive_orientation_local_factor_law_bound": False,
        "downstream_recovery_used": False,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "plain_conclusion": (
            "每个平方基 p² 在全局 Möbius colored-word 层有唯一非零 payload source (d,e)=(p,p)，"
            "其质量为 log p。该结果给出不依赖 payment/zero-row 的 global square-base seed，"
            "但尚未定义 actual primitive coefficient a_p(p) 的 orientation、local factor 或归一化。"
        ),
        "source_hashes": {
            str(Path(__file__).resolve().relative_to(ROOT)): sha256(Path(__file__).resolve()),
            "experiments/prime_matrix_mfac_colored_divisor_word_transport_audit.py": sha256(
                ROOT / "experiments" / "prime_matrix_mfac_colored_divisor_word_transport_audit.py"
            ),
        },
    }


def render_markdown(certificate: dict[str, object]) -> str:
    """渲染人可读审计证书。"""
    lines = [
        "# MFAC 平方基 global seed 与 primitive-binding 缺口审计",
        "",
        f"**状态：** `{certificate['status']}`",
        f"**核验日期：** `{certificate['verified_date']}`",
        "",
        "对每个素数 p，p² 的 global colored-word source 中仅 (d,e)=(p,p) 携带非零质量 log p。",
        "这闭合 global square-base seed，不闭合 actual primitive coefficient。",
        "",
        "```text",
        f"global_square_base_seed_verified={str(certificate['global_square_base_seed_verified']).lower()}",
        f"unique_active_source_verified={str(certificate['unique_active_source_verified']).lower()}",
        "actual_square_base_signed_coefficient_bound=false",
        "primitive_orientation_local_factor_law_bound=false",
        "downstream_recovery_used=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 结论边界",
        "",
        str(certificate["plain_conclusion"]),
        "",
        "下一关是 `PrimitiveOrientationLocalFactorProductLawBeforePushforward`："
        "必须把 global seed 正向绑定到 actual primitive unit，或给出最小 normalization/orientation 冲突。",
    ]
    return "\n".join(lines) + "\n"


def write_certificate(certificate: dict[str, object]) -> None:
    """写出 ledger、JSON 与 Markdown。"""
    rendered = json.dumps(json_safe(certificate), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(rendered, encoding="utf-8")
    OUT_JSON.write_text(rendered, encoding="utf-8")
    OUT_MD.write_text(render_markdown(certificate), encoding="utf-8")


def main() -> None:
    """运行审计。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=997)
    args = parser.parse_args()
    certificate = build_certificate(args.prime_limit)
    write_certificate(certificate)
    print(f"global_square_base_seed_verified={str(certificate['global_square_base_seed_verified']).lower()}")
    print(f"unique_active_source_verified={str(certificate['unique_active_source_verified']).lower()}")
    print("actual_square_base_signed_coefficient_bound=false")


if __name__ == "__main__":
    main()
