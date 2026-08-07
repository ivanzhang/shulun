#!/usr/bin/env python3
"""生成 MFAC primitive orientation/local-factor 归一化不可识别性审计。

用法示例：
  python3 experiments/prime_matrix_mfac_primitive_normalization_underdetermination_audit.py
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
SLUG = "prime-matrix-mfac-primitive-normalization-underdetermination-audit"


def normalization_models(prime: int) -> list[dict[str, float | int]]:
    """返回保持同一 global seed log(p) 的互异 primitive 归一化三元组。"""
    seed = math.log(prime)
    models = [
        {"orientation": 1, "local_factor": 1.0, "coefficient": seed},
        {"orientation": -1, "local_factor": 1.0, "coefficient": -seed},
        {"orientation": 1, "local_factor": 2.0, "coefficient": seed / 2.0},
    ]
    for model in models:
        model["product"] = model["orientation"] * model["local_factor"] * model["coefficient"]
    return models


def build_certificate(prime_limit: int) -> dict[str, object]:
    """审计所有小素数上的 normalization 不可识别性。"""
    primes = [p for p in range(2, prime_limit + 1) if all(p % d for d in range(2, math.isqrt(p) + 1))]
    rows = []
    for prime in primes:
        models = normalization_models(prime)
        rows.append({
            "prime": prime,
            "model_count": len(models),
            "all_products_equal_log_prime": all(math.isclose(model["product"], math.log(prime), abs_tol=1e-12) for model in models),
        })
    return {
        "certificate_type": "prime_matrix_mfac_primitive_normalization_underdetermination_audit",
        "status": "global_square_base_seed_does_not_identify_primitive_orientation_or_local_factor",
        "verified_date": "2026-08-07",
        "prime_limit": prime_limit,
        "normalization_underdetermination_verified": all(row["all_products_equal_log_prime"] and row["model_count"] >= 3 for row in rows),
        "actual_primitive_orientation_bound": False,
        "actual_primitive_local_factor_bound": False,
        "actual_square_base_signed_coefficient_bound": False,
        "downstream_recovery_used": False,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "plain_conclusion": "global square-base seed 只固定 orientation * local_factor * coefficient=log(p) 的乘积；没有独立 pre-Cauchy 声明时，orientation、local factor 与 actual coefficient 不可唯一恢复。",
    }


def write_certificate(certificate: dict[str, object]) -> None:
    """写出机器可读与人可读证书。"""
    rendered = json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    (DATA / f"{SLUG}-ledger.json").write_text(rendered, encoding="utf-8")
    (DOCS / f"{SLUG}.json").write_text(rendered, encoding="utf-8")
    markdown = "\n".join([
        "# MFAC primitive 归一化不可识别性审计",
        "",
        f"**状态：** `{certificate['status']}`",
        "",
        "```text",
        f"normalization_underdetermination_verified={str(certificate['normalization_underdetermination_verified']).lower()}",
        "actual_primitive_orientation_bound=false",
        "actual_primitive_local_factor_bound=false",
        "actual_square_base_signed_coefficient_bound=false",
        "```",
        "",
        "global square-base seed 的 log(p) 只固定三个 primitive 字段的乘积，不能反推其中任一字段。",
        "下一关必须正向声明 `PrimitiveOrientationLocalFactorProductLawBeforePushforward`，或给出 actual primitive unit 的独立构造。",
        "",
    ])
    (DOCS / f"{SLUG}.md").write_text(markdown, encoding="utf-8")


def main() -> None:
    """运行审计并输出证书。"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-limit", type=int, default=997)
    args = parser.parse_args()
    certificate = build_certificate(args.prime_limit)
    write_certificate(certificate)
    print(f"normalization_underdetermination_verified={str(certificate['normalization_underdetermination_verified']).lower()}")
    print("actual_square_base_signed_coefficient_bound=false")


if __name__ == "__main__":
    main()
