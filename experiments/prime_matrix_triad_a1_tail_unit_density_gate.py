#!/usr/bin/env python3
"""审计 Tail unit-density 给出的统一 KL 下界。

用法示例：
  python3 experiments/prime_matrix_triad_a1_tail_unit_density_gate.py
  python3 experiments/prime_matrix_triad_a1_tail_unit_density_gate.py \
    --audits docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.json,docs/monograph/prime-matrix-triad-a1-tail-capacity-pressure-q30030-q510510.json

输出：
  docs/monograph/prime-matrix-triad-a1-tail-unit-density-gate.json
  docs/monograph/prime-matrix-triad-a1-tail-unit-density-gate.md
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
DEFAULT_AUDITS = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q30030-q510510.json",
    )
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-tail-unit-density-gate.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-tail-unit-density-gate.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def tail_unit_density(tail_primes: list[int]) -> float:
    """计算 Tail CRT 中所有 Tail 素数都不命中单个固定洞的密度。"""
    density = 1.0
    for prime in tail_primes:
        density *= (prime - 1) / prime
    return density


def kl_floor_from_upper(upper: float) -> float | None:
    """由完成比例上界给出 KL 下界。"""
    if upper <= 0:
        return None
    return -math.log(upper)


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "infinity"
    return f"{value:.6g}"


def analyze_prime(path: Path, audit: dict[str, Any], item: dict[str, Any]) -> dict[str, Any]:
    """审计单个 P 的 Tail unit-density 门。"""
    tail_primes = [int(value) for value in item["tail_primes"]]
    m_tail = int(item["tail_high_period"])
    unit_density = tail_unit_density(tail_primes)
    singleton_completion_upper = 1.0 - unit_density
    structural_kl_floor = kl_floor_from_upper(singleton_completion_upper)

    positive_residual_slots = 0
    positive_residual_survivors = 0
    positive_residual_completion_mass = 0
    positive_residual_survivor_kl_sum = 0.0
    max_positive_residual_completion_ratio = 0.0
    max_positive_residual_holes_with_survival = 0
    positive_residual_rows = []

    for row in item["by_residual_hole_count"]:
        residual_holes = int(row["residual_hole_count"])
        if residual_holes <= 0:
            continue
        slots = int(row["slots"])
        survivors = int(row["surviving_slots"])
        max_completion = int(row["max_completion_count"])
        completion_ratio = max_completion / m_tail if m_tail else 0.0
        positive_residual_slots += slots
        positive_residual_survivors += survivors
        positive_residual_completion_mass += int(row["completion_mass"])
        positive_residual_survivor_kl_sum += float(row["survivor_kl_floor_sum"])
        max_positive_residual_completion_ratio = max(
            max_positive_residual_completion_ratio,
            completion_ratio,
        )
        if survivors:
            max_positive_residual_holes_with_survival = max(
                max_positive_residual_holes_with_survival,
                residual_holes,
            )
        positive_residual_rows.append(
            {
                "residual_hole_count": residual_holes,
                "slots": slots,
                "surviving_slots": survivors,
                "max_completion_count": max_completion,
                "max_completion_ratio": completion_ratio,
                "unit_density_bound_pass": completion_ratio <= singleton_completion_upper + 1e-12,
                "avg_survivor_kl_floor": row["avg_survivor_kl_floor"],
                "max_survivor_kl_floor": row["max_survivor_kl_floor"],
            }
        )

    return {
        "audit_path": str(path),
        "q": audit["q"],
        "q_lift": audit["q_lift"],
        "promoted_prime": audit["promoted_prime"],
        "p": item["p"],
        "tail_primes": tail_primes,
        "m_tail": m_tail,
        "tail_unit_density": unit_density,
        "singleton_completion_upper": singleton_completion_upper,
        "structural_kl_floor_for_nonempty_residual": structural_kl_floor,
        "positive_residual_slots": positive_residual_slots,
        "positive_residual_survivors": positive_residual_survivors,
        "positive_residual_completion_mass": positive_residual_completion_mass,
        "positive_residual_survivor_kl_sum": positive_residual_survivor_kl_sum,
        "positive_residual_survival_rate": (
            positive_residual_survivors / positive_residual_slots
            if positive_residual_slots
            else None
        ),
        "positive_residual_avg_survivor_kl_floor": (
            positive_residual_survivor_kl_sum / positive_residual_survivors
            if positive_residual_survivors
            else None
        ),
        "max_positive_residual_completion_ratio": max_positive_residual_completion_ratio,
        "max_positive_residual_holes_with_survival": max_positive_residual_holes_with_survival,
        "actual_avg_survivor_kl_floor": item["avg_survivor_kl_floor_to_uniform_tail"],
        "actual_max_survivor_kl_floor": item["max_survivor_kl_floor_to_uniform_tail"],
        "unit_density_bound_pass": (
            max_positive_residual_completion_ratio <= singleton_completion_upper + 1e-12
        ),
        "positive_residual_rows": positive_residual_rows,
    }


def run(audit_paths: list[Path]) -> dict[str, Any]:
    """运行 Tail unit-density 审计。"""
    audits = [(path, load_json(path)) for path in audit_paths]
    rows = [
        analyze_prime(path, audit, item)
        for path, audit in audits
        for item in audit["prime_results"]
    ]
    return {
        "certificate_type": "triad_a1_tail_unit_density_gate",
        "status": "tail_unit_density_kl_floor_materialized",
        "source_hashes": {
            "tail_unit_density_gate_script": file_sha256(Path(__file__).resolve()),
            **{
                f"audit_{idx}": file_sha256(path)
                for idx, (path, _audit) in enumerate(audits, start=1)
            },
        },
        "rows": rows,
        "all_unit_density_bounds_pass": all(row["unit_density_bound_pass"] for row in rows),
        "review_conclusion": (
            "任一非空残余洞都会留下 Tail unit-density 的未命中体积。"
            "因此 Tail 完成集合不能接近满层；若正式质量仍要落在其中，则支付统一 KL 下界。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Tail unit-density KL 门控",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构上界",
        "",
        "对任一非空残余洞集 `Residual_b`，取其中一个洞 `c0`。Tail 要完成整个残余洞集，至少要覆盖 `c0`。",
        "对每个 Tail 素数 `ell`，覆盖 `c0` 只占一个 `y mod ell` 残基；所以所有 Tail 素数都不覆盖 `c0` 的密度为：",
        "",
        "```text",
        "u_tail = product_{ell in Tail} (1-1/ell)。",
        "```",
        "",
        "因此：",
        "",
        "```text",
        "m_b/M_tail <= 1-u_tail",
        "KL >= -log(1-u_tail)。",
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
            "## 3. 总表",
            "",
            f"- `all_unit_density_bounds_pass={result['all_unit_density_bounds_pass']}`。",
            "",
            "| layer | P | tail primes | u_tail | 1-u_tail | KL floor | positive residual survival | max actual completion ratio | positive actual avg KL | pass |",
            "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| Q={q}->{ql} | {p} | `{tail}` | {u} | {upper} | {kl} | {surv} | {actual} | {avgkl} | `{ok}` |".format(
                q=row["q"],
                ql=row["q_lift"],
                p=row["p"],
                tail=row["tail_primes"],
                u=fmt_float(row["tail_unit_density"]),
                upper=fmt_float(row["singleton_completion_upper"]),
                kl=fmt_float(row["structural_kl_floor_for_nonempty_residual"]),
                surv=fmt_float(row["positive_residual_survival_rate"]),
                actual=fmt_float(row["max_positive_residual_completion_ratio"]),
                avgkl=fmt_float(row["positive_residual_avg_survivor_kl_floor"]),
                ok=row["unit_density_bound_pass"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 读法",
            "",
            "若非空残余洞大量幸存且 `u_tail` 不趋零，则每层都有正 KL 成本，进入 PDEC。",
            "若 KL 成本要趋零，只能让 `u_tail->0` 或让幸存残余洞趋于空；前者是高 Tail 密度极限，后者回到 promoted-prime 删除/空洞分支。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audits", type=str, default=DEFAULT_AUDITS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(parse_paths(args.audits))
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_unit_density_bounds_pass": result["all_unit_density_bounds_pass"],
                "row_count": len(result["rows"]),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
