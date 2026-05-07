#!/usr/bin/env python3
"""构造 fixed-projection diffuse 不能推出 moving-block spread 的模型证书。

用法示例：
  python3 experiments/prime_matrix_triad_a1_moving_block_spread_obstruction.py
  python3 experiments/prime_matrix_triad_a1_moving_block_spread_obstruction.py --max-k 10

输出：
  docs/monograph/prime-matrix-triad-a1-moving-block-spread-obstruction.json
  docs/monograph/prime-matrix-triad-a1-moving-block-spread-obstruction.md
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
DEFAULT_NCBLK = DOCS / "prime-matrix-triad-a1-ncblk-projection-gap-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-moving-block-spread-obstruction.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-moving-block-spread-obstruction.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_float(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6g}"


def model_row(k: int, saving_exponent: float) -> dict[str, Any]:
    """生成一个尺度上的移动块不可见性模型。

    模型含义：
    - fixed signatures 数量 K_N 增长，所以任意固定签名最终不再被命中；
    - 每个 fixed signature 下有 hidden moving blocks；
    - concentrated 模型每个 fixed signature 只用一个 moving block；
    - spread 模型把同样质量摊到 hidden_fiber_size 个 moving blocks。
    """
    y = 10**k
    log_y = math.log(y)
    fixed_signature_count = max(2, int(log_y))
    hidden_fiber_size = max(2, int(log_y))
    concentrated_block_energy = 1.0 / fixed_signature_count
    spread_block_energy = 1.0 / (fixed_signature_count * hidden_fiber_size)
    required_energy = log_y ** (-2.0 * saving_exponent)
    return {
        "k": k,
        "y": y,
        "log_y": log_y,
        "fixed_signature_count": fixed_signature_count,
        "hidden_fiber_size": hidden_fiber_size,
        "max_fixed_signature_mass": 1.0 / fixed_signature_count,
        "max_fixed_signature_mass_tends_to_zero_model": True,
        "concentrated_block_energy": concentrated_block_energy,
        "spread_block_energy": spread_block_energy,
        "required_ncblk_energy_for_exponent": required_energy,
        "concentrated_violates_required_energy": concentrated_block_energy
        > required_energy,
        "same_fixed_projection_as_spread_model": True,
        "energy_ratio_concentrated_over_spread": hidden_fiber_size,
    }


def run(ncblk_path: Path, min_k: int, max_k: int, saving_exponent: float) -> dict[str, Any]:
    """运行投影不可见性审计。"""
    ncblk = load_json(ncblk_path)
    rows = [model_row(k, saving_exponent) for k in range(min_k, max_k + 1)]
    all_rows_violate = all(row["concentrated_violates_required_energy"] for row in rows)
    max_fixed_mass_decreases = all(
        rows[idx + 1]["max_fixed_signature_mass"] <= rows[idx]["max_fixed_signature_mass"]
        for idx in range(len(rows) - 1)
    )
    return {
        "certificate_type": "triad_a1_moving_block_spread_obstruction",
        "status": "moving_block_spread_not_implied_by_fixed_projection_diffuse",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "ncblk_projection_gap_json": file_sha256(ncblk_path),
        },
        "parameters": {
            "min_k": min_k,
            "max_k": max_k,
            "saving_exponent": saving_exponent,
            "scale": "y=10^k",
        },
        "ncblk_input_status": ncblk["status"],
        "rows": rows,
        "all_rows_concentrated_model_violates_required_energy": all_rows_violate,
        "max_fixed_signature_mass_decreases": max_fixed_mass_decreases,
        "projection_indistinguishability_law": (
            "固定投影只记录 fixed signature 的总质量。若每个 fixed signature 下还有随尺度增长的"
            " hidden moving-block fiber，则集中模型和分散模型可以有完全相同的固定投影账本，"
            "但 moving-block 二能量相差 hidden_fiber_size 倍。"
        ),
        "structural_obstruction": (
            "Fixed-projection diffuse only says each named fixed signature eventually receives small mass. "
            "It does not impose arbitrary-log decay on the hidden same-(u,v) moving block energy. "
            "Therefore MovingBlockSpreadNCBLK requires a new source-block entropy/non-concentration theorem "
            "or an external DI/BFI dispersion theorem."
        ),
        "next_internal_target": "SourceBlockEntropyNCBLK",
        "terminal_gap_after_router": "SourceBlockEntropyNCBLKOrExternalDIBFIOriginalDispersion",
        "review_conclusion": (
            "当前 ledger 不能直接证明 MovingBlockSpreadNCBLK：存在投影不可见模型，"
            "固定投影 diffuse 与 moving-block 集中可同时成立。内部无黑箱路线必须新增"
            " SourceBlockEntropyNCBLK。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 MovingBlockSpread 阻断证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 投影不可见性律",
        "",
        result["projection_indistinguishability_law"],
        "",
        result["structural_obstruction"],
        "",
        "```text",
        "fixed projection ledger sees only total mass per fixed signature；",
        "moving-block NC-BLK needs energy per growing block b=(u,v)；",
        "hidden moving fibers can concentrate while fixed signatures keep diffusing。",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `ncblk_input_status={result['ncblk_input_status']}`。",
        f"- `all_rows_concentrated_model_violates_required_energy={result['all_rows_concentrated_model_violates_required_energy']}`。",
        f"- `max_fixed_signature_mass_decreases={result['max_fixed_signature_mass_decreases']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 模型审计表",
        "",
        "| k | log y | fixed signatures | hidden fiber | max fixed mass | concentrated energy | spread energy | required | violates | ratio |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: |",
    ]
    for row in result["rows"]:
        lines.append(
            "| {k} | {logy} | {fixed} | {hidden} | {maxmass} | {cenergy} | {senergy} | {required} | `{violates}` | {ratio} |".format(
                k=row["k"],
                logy=fmt_float(row["log_y"]),
                fixed=row["fixed_signature_count"],
                hidden=row["hidden_fiber_size"],
                maxmass=fmt_float(row["max_fixed_signature_mass"]),
                cenergy=fmt_float(row["concentrated_block_energy"]),
                senergy=fmt_float(row["spread_block_energy"]),
                required=fmt_float(row["required_ncblk_energy_for_exponent"]),
                violates=row["concentrated_violates_required_energy"],
                ratio=row["energy_ratio_concentrated_over_spread"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 结论",
            "",
            "这不是行命题最终证明，而是排除一个隐藏跳步：",
            "",
            "```text",
            "fixed-projection diffuse 不能推出 MovingBlockSpreadNCBLK。",
            "```",
            "",
            "下一步若坚持无黑箱路线，必须证明更强的源头块熵命题：",
            "",
            "```text",
            "SourceBlockEntropyNCBLK:",
            "actual WFD/Type-I-II/Fourier/well-factorable coefficients distribute over",
            "moving same-(u,v) blocks with enough entropy to force block-energy log saving。",
            "```",
            "",
            "否则只能转入外部 `DI/BFI original dispersion` 引用路线。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ncblk-json", type=Path, default=DEFAULT_NCBLK)
    parser.add_argument("--min-k", type=int, default=3)
    parser.add_argument("--max-k", type=int, default=9)
    parser.add_argument("--saving-exponent", type=float, default=2.0)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.ncblk_json, args.min_k, args.max_k, args.saving_exponent)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_internal_target": result["next_internal_target"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
