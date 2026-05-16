#!/usr/bin/env python3
"""生成 AffineTwin endpoint-release anchored parity no-go 审计证书。

用法示例：
  python3 experiments/prime_matrix_affine_twin_endpoint_release_anchored_parity_nogo_audit.py
  python3 -m json.tool data/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-ledger.json

输出：
  data/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-ledger.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-audit.json
  docs/monograph/prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-audit.md
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

ANCHORED_DEPTH_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-anchored-circular-depth-ledger.json"
)

OUT_LEDGER = DATA / (
    "prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-ledger.json"
)
OUT_JSON = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-audit.json"
)
OUT_MD = DOCS / (
    "prime-matrix-affine-twin-endpoint-release-anchored-parity-nogo-audit.md"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def is_prime(n: int) -> bool:
    """小整数素性检查。"""
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


def build_result(anchored_depth_path: Path) -> dict[str, Any]:
    """构造 anchored parity no-go 审计结果。"""
    anchored = load_json(anchored_depth_path)
    agg_in = anchored["aggregate"]
    row_in = anchored["anchored_depth_row"]

    depth = int(agg_in["required_common_left_depth_to_cover_arc"])
    support_width = int(agg_in["support_width"])
    arc_width = int(agg_in["minimal_circular_alignment_arc_width"])
    q_from_generator = 2 * depth - 5
    q_from_fill = depth + 3
    common_depth_solution = 8
    common_q_solution = 11
    depth_gap_from_common_solution = depth - common_depth_solution
    parity_no_go = depth % 2 == 1 and q_from_fill > 2 and q_from_fill % 2 == 0

    aggregate = {
        "anchored_circular_depth_ledger": str(
            anchored_depth_path.relative_to(ROOT)
        ),
        "actual_anchor_pair": str(agg_in["actual_anchor_pair"]),
        "minimal_circular_alignment_arc": agg_in[
            "minimal_circular_alignment_arc"
        ],
        "minimal_circular_alignment_arc_width": arc_width,
        "support_width": support_width,
        "required_common_left_depth": depth,
        "required_depth_parity": "odd" if depth % 2 else "even",
        "same_orientation_lower_generator_formula": "q_g=2D-5",
        "same_orientation_lower_fill_formula": "q_f=D+3",
        "q_from_generator_depth_formula": q_from_generator,
        "q_from_fill_depth_formula": q_from_fill,
        "q_from_generator_is_prime": is_prime(q_from_generator),
        "q_from_fill_is_prime": is_prime(q_from_fill),
        "q_from_fill_is_even": q_from_fill % 2 == 0,
        "q_candidate_gap": abs(q_from_generator - q_from_fill),
        "common_q_equation": "2D-5=D+3",
        "common_depth_solution": common_depth_solution,
        "common_q_solution": common_q_solution,
        "common_solution_support_width": (common_q_solution + 9) // 2,
        "required_depth_gap_from_common_solution": depth_gap_from_common_solution,
        "required_arc_width_exceeds_common_solution_support": arc_width
        > (common_q_solution + 9) // 2,
        "same_orientation_common_q_absent_by_equality": depth
        != common_depth_solution,
        "same_orientation_common_q_absent_by_parity": parity_no_go,
        "anchored_parity_nogo_closed_current_sweep": (
            bool(agg_in["actual_anchor_is_circular_arc_end"])
            and depth != common_depth_solution
            and parity_no_go
        ),
        "global_anchored_parity_nogo_excluded": False,
        "row_column_unconditional_closed": False,
    }

    return {
        "certificate_type": (
            "prime_matrix_affine_twin_endpoint_release_"
            "anchored_parity_nogo_audit"
        ),
        "status": "current_sweep_anchored_parity_nogo_structured_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "aggregate": aggregate,
        "parity_nogo_row": {
            "actual_anchor_pair": str(row_in["actual_anchor_pair"]),
            "required_common_left_depth": depth,
            "q_from_generator_depth_formula": q_from_generator,
            "q_from_fill_depth_formula": q_from_fill,
            "common_depth_solution": common_depth_solution,
            "depth_gap_from_common_solution": depth_gap_from_common_solution,
            "parity_no_go": parity_no_go,
        },
        "contract": {
            "anchored_parity_nogo_gate": [
                "same-orientation lower-side absorption needs q_g=2D-5 and q_f=D+3",
                "a common q forces D=8 and q=11",
                "the actual-anchored circular arc forces D=557",
                "since D is odd, q_f=D+3 is an even integer greater than 2, hence not an odd prime",
                "route persistent anchored depth to orientation-changing, ColumnCRT/PDEC, SAE, or moving-family multiplicity exits",
            ],
            "closed_current_sweep": aggregate[
                "anchored_parity_nogo_closed_current_sweep"
            ],
            "global_remaining": [
                "AnchoredParityNoGo promoted to global family theorem",
                "OrientationChangingPrimitiveKey-PDEC/SAE",
                "ColumnCRT/PDEC for persistent actual-anchored aperture recurrence",
                "AffineTwinEpochPairMultiplicityBoundOrColumnCRTPDECExclusion",
            ],
        },
        "dependency_hashes": {
            str(anchored_depth_path.relative_to(ROOT)): sha256(
                anchored_depth_path
            )
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
    row = result["parity_nogo_row"]
    lines = [
        "# Prime Matrix AffineTwin endpoint-release anchored parity no-go audit",
        "",
        "**状态：** `current_sweep_anchored_parity_nogo_structured_global_open`",
        "",
        "本审计把 anchored circular-depth 的 moving-key 失败从数值不等式升级为同向 lower-side 的奇偶/方程 no-go：共同深度 `D` 若要由同一个 AffineTwin key 吸收，必须同时满足 `q=2D-5` 与 `q=D+3`。",
        "",
        "```text",
        f"actual_anchor_pair={agg['actual_anchor_pair']}",
        f"minimal_circular_alignment_arc={agg['minimal_circular_alignment_arc']}",
        f"minimal_circular_alignment_arc_width={agg['minimal_circular_alignment_arc_width']}",
        f"support_width={agg['support_width']}",
        f"required_common_left_depth={agg['required_common_left_depth']}",
        f"required_depth_parity={agg['required_depth_parity']}",
        f"q_from_generator_depth_formula={agg['q_from_generator_depth_formula']}",
        f"q_from_fill_depth_formula={agg['q_from_fill_depth_formula']}",
        f"q_from_fill_is_even={fmt_bool(agg['q_from_fill_is_even'])}",
        f"q_from_fill_is_prime={fmt_bool(agg['q_from_fill_is_prime'])}",
        f"common_depth_solution={agg['common_depth_solution']}",
        f"common_q_solution={agg['common_q_solution']}",
        f"required_depth_gap_from_common_solution={agg['required_depth_gap_from_common_solution']}",
        f"same_orientation_common_q_absent_by_equality={fmt_bool(agg['same_orientation_common_q_absent_by_equality'])}",
        f"same_orientation_common_q_absent_by_parity={fmt_bool(agg['same_orientation_common_q_absent_by_parity'])}",
        f"anchored_parity_nogo_closed_current_sweep={fmt_bool(agg['anchored_parity_nogo_closed_current_sweep'])}",
        "```",
        "",
        "## 1. parity no-go row",
        "",
        "| anchor | D | q_g=2D-5 | q_f=D+3 | common D | D gap | parity no-go |",
        "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
        "| `{anchor}` | {depth} | {qg} | {qf} | {common} | {gap} | `{nogo}` |".format(
            anchor=row["actual_anchor_pair"],
            depth=row["required_common_left_depth"],
            qg=row["q_from_generator_depth_formula"],
            qf=row["q_from_fill_depth_formula"],
            common=row["common_depth_solution"],
            gap=row["depth_gap_from_common_solution"],
            nogo=fmt_bool(row["parity_no_go"]),
        ),
        "",
        "## 2. 显式矛盾点",
        "",
        "同向 lower-side AffineTwin 深度公式为：",
        "",
        "```text",
        "generator left depth D = (q+5)/2  =>  q_g=2D-5",
        "fill left depth D = q-3          =>  q_f=D+3",
        "```",
        "",
        "若同一个 `q` 同时解释两侧，则 `2D-5=D+3`，唯一解为 `D=8`、`q=11`。但 actual-anchored 圆弧强制 `D=557`，距离唯一解相差 `549`。更强地，`D=557` 是奇数，所以 `q_f=D+3=560` 为大于 `2` 的偶数，不可能是奇素数 AffineTwin key。",
        "",
        "## 3. 结论边界",
        "",
        "- 本步关闭当前 sweep 的 same-orientation anchored parity absorption。",
        "- 本步不关闭全局行/列命题；剩余是把这个 parity no-go 升格为全局族定理，或处理方向改变 key、ColumnCRT/PDEC、SAE、moving-family multiplicity 出口。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--anchored-depth-ledger",
        type=Path,
        default=ANCHORED_DEPTH_LEDGER,
        help="anchored circular-depth ledger path",
    )
    args = parser.parse_args()
    result = build_result(args.anchored_depth_ledger)
    write_outputs(result)
    print(json.dumps(result["aggregate"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
