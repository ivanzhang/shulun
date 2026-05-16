#!/usr/bin/env python3
"""生成 AffineTwin moving-key depth formula 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_moving_key_depth_formula_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-moving-key-depth-formula-ledger.json

输出：
  data/prime-matrix-affine-twin-moving-key-depth-formula-ledger.json
  docs/monograph/prime-matrix-affine-twin-moving-key-depth-formula-audit.json
  docs/monograph/prime-matrix-affine-twin-moving-key-depth-formula-audit.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PRIMITIVE_DEFECT_LEDGER = DATA / (
    "prime-matrix-affine-twin-support-motion-primitive-defect-ledger.json"
)
SUPPORT_MOTION_LEDGER = DATA / "prime-matrix-affine-twin-support-motion-depth-ledger.json"

OUT_LEDGER = DATA / "prime-matrix-affine-twin-moving-key-depth-formula-ledger.json"
OUT_JSON = DOCS / "prime-matrix-affine-twin-moving-key-depth-formula-audit.json"
OUT_MD = DOCS / "prime-matrix-affine-twin-moving-key-depth-formula-audit.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def formula_row(row: dict[str, Any]) -> dict[str, Any]:
    """把 primitive-depth defect 行转成 moving-q 公式相容性行。"""
    depth = int(row["required_common_side_depth"])
    side = str(row["window_side"])
    if side == "below":
        q_from_generator = 2 * depth - 5
        q_from_fill = depth + 3
        q_candidate_gap = abs(q_from_generator - q_from_fill)
        common_q_exists = q_from_generator == q_from_fill
        obstruction = "lower_depth_q_mismatch"
    elif side == "above":
        q_from_generator = 4 * depth + 7
        q_from_fill = None
        q_candidate_gap = None
        common_q_exists = depth == 1
        obstruction = "fill_right_depth_fixed_one"
    else:
        raise RuntimeError(f"unsupported side: {side}")

    return {
        "source_pair_key": str(row["source_pair_key"]),
        "window_side": side,
        "nearest_representative": int(row["nearest_representative"]),
        "required_common_side_depth": depth,
        "q_from_generator_depth_formula": q_from_generator,
        "q_from_fill_depth_formula": q_from_fill,
        "q_candidate_gap": q_candidate_gap,
        "fill_right_depth_residual": None if side == "below" else depth - 1,
        "same_orientation_affine_depth_common_q_exists": common_q_exists,
        "same_orientation_affine_depth_obstruction": obstruction,
        "support_motion_primitive_defect_total": int(row["total_affine_depth_defect"]),
    }


def build_result(primitive_defect_path: Path, support_motion_path: Path) -> dict[str, Any]:
    """构造 moving-key depth formula 审计结果。"""
    primitive_defect = load_json(primitive_defect_path)
    support_motion = load_json(support_motion_path)
    rows = [
        formula_row(row)
        for row in primitive_defect["support_motion_primitive_defect_rows"]
    ]
    if not rows:
        raise RuntimeError("no primitive-defect rows found")

    side_histogram = Counter(str(row["window_side"]) for row in rows)
    lower_rows = [row for row in rows if row["window_side"] == "below"]
    above_rows = [row for row in rows if row["window_side"] == "above"]
    lower_gaps = [int(row["q_candidate_gap"]) for row in lower_rows]
    above_residuals = [
        int(row["fill_right_depth_residual"]) for row in above_rows
    ]
    narrowest_formula_row = min(
        rows,
        key=lambda row: (
            int(row["q_candidate_gap"])
            if row["q_candidate_gap"] is not None
            else int(row["fill_right_depth_residual"]),
            int(row["required_common_side_depth"]),
            str(row["source_pair_key"]),
        ),
    )

    aggregate = {
        "primitive_defect_ledger": str(primitive_defect_path.relative_to(ROOT)),
        "support_motion_depth_ledger": str(support_motion_path.relative_to(ROOT)),
        "moving_key_depth_formula_candidate_count": len(rows),
        "support_motion_side_histogram": dict(sorted(side_histogram.items())),
        "lower_side_candidate_count": len(lower_rows),
        "above_side_candidate_count": len(above_rows),
        "min_lower_q_candidate_gap": min(lower_gaps) if lower_gaps else None,
        "max_lower_q_candidate_gap": max(lower_gaps) if lower_gaps else None,
        "min_above_fill_right_depth_residual": min(above_residuals)
        if above_residuals
        else None,
        "max_above_fill_right_depth_residual": max(above_residuals)
        if above_residuals
        else None,
        "narrowest_formula_obstruction_atom": {
            "source_pair_key": narrowest_formula_row["source_pair_key"],
            "window_side": narrowest_formula_row["window_side"],
            "required_common_side_depth": narrowest_formula_row[
                "required_common_side_depth"
            ],
            "q_from_generator_depth_formula": narrowest_formula_row[
                "q_from_generator_depth_formula"
            ],
            "q_from_fill_depth_formula": narrowest_formula_row[
                "q_from_fill_depth_formula"
            ],
            "q_candidate_gap": narrowest_formula_row["q_candidate_gap"],
            "fill_right_depth_residual": narrowest_formula_row[
                "fill_right_depth_residual"
            ],
            "obstruction": narrowest_formula_row[
                "same_orientation_affine_depth_obstruction"
            ],
        },
        "all_same_orientation_affine_depth_common_q_absent": all(
            not bool(row["same_orientation_affine_depth_common_q_exists"])
            for row in rows
        ),
        "same_orientation_moving_key_depth_absorption_closed_current_sweep": all(
            not bool(row["same_orientation_affine_depth_common_q_exists"])
            for row in rows
        ),
        "global_moving_primitive_key_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": "prime_matrix_affine_twin_moving_key_depth_formula_audit",
        "status": "current_sweep_same_orientation_moving_key_depth_formula_closed_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "moving_key_depth_formula_rows": rows,
        "contract": {
            "same_orientation_moving_key_gate": (
                "For a support-motion depth D to be absorbed by another same-orientation "
                "AffineTwin key, the generator and fill AffineTwin depth formulas must "
                "produce the same q. Current support-motion depths fail this condition."
            ),
            "closed_current_sweep": aggregate[
                "same_orientation_moving_key_depth_absorption_closed_current_sweep"
            ],
            "global_remaining": [
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "SourceRematerialization-PDEC/SAE",
                "MovingPrimitiveKeyNonPersistence",
                "EndpointReleaseCoupling-PDEC",
            ],
        },
        "dependency_hashes": {
            str(path.relative_to(ROOT)): sha256(path)
            for path in (primitive_defect_path, support_motion_path)
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    for path in (OUT_LEDGER, OUT_JSON):
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    agg = result["aggregate"]
    lines = [
        "# Prime Matrix AffineTwin moving-key depth formula audit",
        "",
        "**状态：** `current_sweep_same_orientation_moving_key_depth_formula_closed_global_open`",
        "",
        "本审计继续下钻 `MovingPrimitiveKey`：即使允许 `q` 移动，只要保持同一 AffineTwin 深度公式和同侧吸收，support-motion 所需共同深度也不能由 generator/fill 两侧给出同一个 `q`。",
        "",
        "```text",
        f"moving_key_depth_formula_candidate_count={agg['moving_key_depth_formula_candidate_count']}",
        f"support_motion_side_histogram={agg['support_motion_side_histogram']}",
        f"min_lower_q_candidate_gap={agg['min_lower_q_candidate_gap']}",
        f"max_lower_q_candidate_gap={agg['max_lower_q_candidate_gap']}",
        f"min_above_fill_right_depth_residual={agg['min_above_fill_right_depth_residual']}",
        f"max_above_fill_right_depth_residual={agg['max_above_fill_right_depth_residual']}",
        f"same_orientation_moving_key_depth_absorption_closed_current_sweep={fmt_bool(agg['same_orientation_moving_key_depth_absorption_closed_current_sweep'])}",
        "```",
        "",
        "## 1. moving-q formula 表",
        "",
        "| pair | side | depth D | q from g | q from f | q gap | right residual | obstruction |",
        "| --- | --- | ---: | ---: | --- | --- | --- | --- |",
    ]
    for row in result["moving_key_depth_formula_rows"]:
        lines.append(
            "| `{pair}` | `{side}` | {depth} | {qg} | {qf} | {gap} | {residual} | `{obs}` |".format(
                pair=row["source_pair_key"],
                side=row["window_side"],
                depth=row["required_common_side_depth"],
                qg=row["q_from_generator_depth_formula"],
                qf="-" if row["q_from_fill_depth_formula"] is None else row["q_from_fill_depth_formula"],
                gap="-" if row["q_candidate_gap"] is None else row["q_candidate_gap"],
                residual="-" if row["fill_right_depth_residual"] is None else row["fill_right_depth_residual"],
                obs=row["same_orientation_affine_depth_obstruction"],
            )
        )

    narrow = agg["narrowest_formula_obstruction_atom"]
    lines.extend(
        [
            "",
            "## 2. 当前读数",
            "",
            "- lower-side 同侧吸收要求 `(q+5)/2=D` 且 `q-3=D`，即 `q=2D-5` 与 `q=D+3` 必须相等；这只在 `D=8` 时可能。",
            "- above-side 同侧吸收要求 `(q-7)/4=D` 且 `1=D`，而当前 above depths 远大于 `1`。",
            f"- 当前最窄公式阻塞 atom 是 `{narrow['source_pair_key']}`，side `{narrow['window_side']}`，`D={narrow['required_common_side_depth']}`，阻塞类型 `{narrow['obstruction']}`。",
            "- 因此当前支撑运动不能由同向 AffineTwin moving key 的深度公式吸收。",
            "",
            "## 3. 结论边界",
            "",
            "- 本步关闭当前 sweep 的 same-orientation moving-key depth absorption。",
            "- 本步不证明所有 moving primitive key 全局不复现；剩余是方向改变、source 重物化或 key 迁移的非持久性证明，或路由到 `OrientationChangingPrimitiveKey-PDEC/SAE`、`SourceRematerialization-PDEC/SAE`、`EndpointReleaseCoupling-PDEC`。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="生成 AffineTwin moving-key depth formula 审计证书。"
    )
    parser.add_argument(
        "--primitive-defect-ledger", type=Path, default=PRIMITIVE_DEFECT_LEDGER
    )
    parser.add_argument("--support-motion-ledger", type=Path, default=SUPPORT_MOTION_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口。"""
    args = parse_args()
    result = build_result(args.primitive_defect_ledger, args.support_motion_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
