#!/usr/bin/env python3
"""把仿射塌缩原子登记为 twin-prime 型必要条件门。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_prime_gate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

AFFINE_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-router.md"

NEXT_TARGET = "AffineTwinPrimeGateBoundOrAffineTwinPDECExclusion"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def is_prime(n: int) -> bool:
    """小范围素性判定。"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def gate_row(row: dict[str, Any]) -> dict[str, Any]:
    """构造 twin-prime 型必要条件行。"""
    q = int(row["gap_ell"])
    generator = int(row["generator_ell"])
    fill = int(row["fill_ell"])
    return {
        "gap_ell": q,
        "generator_ell": generator,
        "fill_ell": fill,
        "gap_is_prime": is_prime(q),
        "generator_is_gap_minus_2": generator == q - 2,
        "generator_is_prime": is_prime(generator),
        "fill_equals_gap": fill == q,
        "twin_prime_gate_closed_current_sweep": is_prime(q) and is_prime(q - 2) and generator == q - 2 and fill == q,
        "gap_mod_4": q % 4,
        "gap_congruent_3_mod_4": q % 4 == 3,
        "delta_u_integrality_gate": (q - 3) % 4 == 0,
        "margin_integrality_gate": (q - 1) % 2 == 0,
        "delta_b_integrality_gate": (q - 5) % 2 == 0,
        "affine_twin_gate_key": f"q={q}|twin={q-2},{q}|qmod4={q % 4}",
        "source_affine_key": str(row["affine_key"]),
    }


def build_result(affine_ledger: Path) -> dict[str, Any]:
    """构造 twin-prime 型必要条件门结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    affine = load_json(affine_ledger)
    rows = [gate_row(row) for row in affine["affine_rows"]]
    keys = [row["affine_twin_gate_key"] for row in rows]
    aggregate = {
        "affine_ledger": str(affine_ledger.relative_to(ROOT)),
        "affine_twin_gate_row_count": len(rows),
        "unique_affine_twin_gate_key_count": len(set(keys)),
        "repeated_affine_twin_gate_key_count": len(keys) - len(set(keys)),
        "all_twin_prime_gates_closed_current_sweep": all(row["twin_prime_gate_closed_current_sweep"] for row in rows),
        "all_gap_congruent_3_mod_4": all(row["gap_congruent_3_mod_4"] for row in rows),
        "all_affine_integrality_gates_closed": all(
            row["delta_u_integrality_gate"]
            and row["margin_integrality_gate"]
            and row["delta_b_integrality_gate"]
            for row in rows
        ),
        "affine_twin_prime_gate_bound_proved": False,
        "affine_twin_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
    }
    ledger = {
        "aggregate": aggregate,
        "affine_twin_gate_rows": rows,
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": (
            "prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_"
            "affine_twin_prime_gate_router"
        ),
        "status": "affine_twin_prime_gate_closed_current_sweep_global_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "finite_sweep_not_used_as_global_proof": True,
        "aggregate": aggregate,
        "affine_twin_gate_rows": rows,
        "affine_twin_prime_gate_bound_proved": False,
        "affine_twin_pdec_excluded_globally": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": "PrimitiveAffineCollapseGlobalBoundOrAffinePDECExclusion",
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "本步把仿射塌缩原子压成 twin-prime 型必要条件门：当前 `q=31`，"
            "`generator_ell=q-2=29` 与 `fill_ell=q=31` 均为素数，且 `q≡3 mod 4`，"
            "从而所有仿射参数为整数。全局剩余是证明此类 AffineTwin 门无法持久复现，"
            "或排斥持久 AffineTwin-PDEC/SAE。"
        ),
    }
    result["source_hashes"] = {
        "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_selector_h_lower_affine_twin_prime_gate_router.py": sha256(
            Path(__file__).resolve()
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-primitive-affine-collapse-ledger.json": sha256(
            affine_ledger
        ),
        "data/square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-ledger.json": sha256(
            OUT_LEDGER
        ),
    }
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow selector H lower affine twin prime gate router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"affine_twin_gate_row_count={agg['affine_twin_gate_row_count']}",
        f"unique_affine_twin_gate_key_count={agg['unique_affine_twin_gate_key_count']}",
        f"repeated_affine_twin_gate_key_count={agg['repeated_affine_twin_gate_key_count']}",
        f"all_twin_prime_gates_closed_current_sweep={fmt_bool(agg['all_twin_prime_gates_closed_current_sweep'])}",
        f"all_gap_congruent_3_mod_4={fmt_bool(agg['all_gap_congruent_3_mod_4'])}",
        f"all_affine_integrality_gates_closed={fmt_bool(agg['all_affine_integrality_gates_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. twin-prime 型门",
        "",
        "| q | generator ell | fill ell | q prime | q-2 prime | q mod 4 | key |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in result["affine_twin_gate_rows"]:
        lines.append(
            f"| {row['gap_ell']} | {row['generator_ell']} | {row['fill_ell']} | "
            f"`{fmt_bool(row['gap_is_prime'])}` | `{fmt_bool(row['generator_is_prime'])}` | "
            f"{row['gap_mod_4']} | `{row['affine_twin_gate_key']}` |"
        )
    lines.extend(
        [
            "",
            "## 2. 结构结论",
            "",
            "- 当前仿射塌缩不是一般整数模式，而要求 `q` 与 `q-2` 同时为素数。",
            "- `q≡3 mod 4` 是 `|delta_u|=(q-3)/4` 的整数门。",
            "- 这不是全局孪生素数定理；这里只是把持久仿射失败的必要条件登记为更窄 PDEC 入口。",
            "",
            "## 3. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 将 AffineTwin 门与 slot-depth/CRT 相位条件合并，证明其不可持久或登记为最终 AffineTwin-PDEC。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--affine-ledger", type=Path, default=AFFINE_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    affine_ledger = args.affine_ledger if args.affine_ledger.is_absolute() else ROOT / args.affine_ledger
    result = build_result(affine_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-selector-h-lower-affine-twin-prime-gate-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "affine_twin_gate_row_count": result["aggregate"]["affine_twin_gate_row_count"],
                "all_twin_prime_gates_closed_current_sweep": result["aggregate"][
                    "all_twin_prime_gates_closed_current_sweep"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
