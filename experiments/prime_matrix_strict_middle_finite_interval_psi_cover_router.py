#!/usr/bin/env python3
"""生成 strict 中段有限区间 psi 覆盖路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_middle_finite_interval_psi_cover_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-middle-finite-interval-psi-cover-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-middle-finite-interval-psi-cover-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-middle-finite-interval-psi-cover-router.md"

MIDDLE_SOURCE = MONOGRAPH / "prime-matrix-strict-middle-psi-upper-source-router.json"
ALGORITHM = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-algorithm-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [MIDDLE_SOURCE, ALGORITHM, CLAIM_STATUS]

TARGET = "MiddleFiniteIntervalPsiCover8e11ToE28Ledger"
POINT_TABLE = "DusartTable62PointValuesLedger"
SHORT_INCREMENT = "CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger"
FINE_MESH = "MiddlePsiFineMeshComputationAndHashLedger"
JUMP_CONTROL = "PrimePowerJumpLocalizationOrUpperEnvelopeLedger"
ROUNDING = "MiddlePsiUpperDirectedRoundingLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TARGET_RATIO = 1.00002841
X_RIGHT = math.exp(28)
POINTS = [
    (8.0e11, 799_999_133_776.084743 + 904_203.190001),
    (9.0e11, 899_998_818_628.952024 + 958_602.924046),
    (1.0e12, 999_999_030_333.096225 + 1_009_803.669232),
    (2.0e12, 1_999_998_755_521.470649 + 1_427_105.865316),
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def fmt_float(value: float) -> str:
    """稳定输出浮点。"""
    return f"{value:.15e}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def point_rows() -> list[dict[str, Any]]:
    """计算 Table 6.2 点值的余量。"""
    rows = []
    for x, psi in POINTS:
        ratio = psi / x
        rows.append(
            {
                "x": x,
                "psi": psi,
                "ratio": ratio,
                "absolute_slack": TARGET_RATIO * x - psi,
                "beats_target": ratio <= TARGET_RATIO,
            }
        )
    return rows


def naive_interval_rows() -> list[dict[str, Any]]:
    """测试只用右端点值和 psi 单调性是否足够。"""
    rows = []
    for (left, _), (right, psi_right) in zip(POINTS, POINTS[1:]):
        clipped_right = min(right, X_RIGHT)
        if left >= X_RIGHT:
            continue
        bound = psi_right / left
        rows.append(
            {
                "interval": f"[{left:.0f}, {clipped_right:.0f}]",
                "bound": bound,
                "defect": bound - TARGET_RATIO,
                "sufficient": bound <= TARGET_RATIO,
            }
        )
    return rows


def mesh_pressure_rows() -> list[dict[str, Any]]:
    """估计若用粗跳跃包络时所需的网格尺度。"""
    # 若只用极粗的每整数最多 log(x) 权重，则 h*log(x) 不能超过点余量，网格需在百万级以下。
    rows = []
    for item in point_rows()[:3]:
        x = float(item["x"])
        slack = float(item["absolute_slack"])
        rows.append(
            {
                "x": x,
                "point_slack": slack,
                "max_mesh_under_trivial_integer_weight": slack / math.log(X_RIGHT),
                "meaning": "trivial jump envelope would require very fine certified mesh; sparse 1e11 grid cannot work",
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造中段有限区间 psi 覆盖证书。"""
    middle_source = load_json(MIDDLE_SOURCE)
    algorithm = load_json(ALGORITHM)
    active = middle_source.get("next_direct_attack_target") == TARGET
    use_site_ready = middle_source.get("middle_psi_upper_use_site_closed") is True
    p51_graph_ready = algorithm.get("p51_dependency_graph_closed") is True
    points = point_rows()
    naive = naive_interval_rows()
    point_values_all_good = all(item["beats_target"] for item in points)
    naive_monotone_fails = not any(item["sufficient"] for item in naive)
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            middle_source.get("counterexample_assumption_only") is True
            and middle_source.get("row_column_unconditional_closed") is False,
            True,
            "本步只审计假设反例链可调用的中段有限 psi 覆盖，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "MiddleFiniteIntervalPsiCoverGateActive",
            active and use_site_ready and p51_graph_ready,
            True,
            "上一层已把 1.00002841 的来源缺口压成 8e11 到 e^28 的有限区间覆盖。",
            TARGET,
        ),
        row(
            POINT_TABLE,
            point_values_all_good,
            True,
            "Table 6.2 点值在 8e11、9e11、1e12、2e12 均低于 1.00002841，且绝对余量为千万级。",
            "point values only; interval cover still open",
        ),
        row(
            "SparsePointMonotonicityCoverFails",
            naive_monotone_fails,
            True,
            "只用 psi 单调性和下一稀疏点值会得到过大的右点/左端上界，不能覆盖点间。",
            f"{SHORT_INCREMENT} OR {FINE_MESH}",
        ),
        row(
            "TrivialJumpEnvelopeRequiresFineMesh",
            True,
            True,
            "若只用每个整数贡献不超过 log x 的极粗跳跃包络，千万级余量要求约百万级网格，1e11 稀疏网格远远不够。",
            f"{FINE_MESH} AND {JUMP_CONTROL}",
        ),
        row(
            SHORT_INCREMENT,
            False,
            False,
            "需要对每个子区间证明 psi(y)-psi(x) <= 1.00002841*y - psi(x) 的短区间上界。",
            "short interval explicit upper envelope for psi increments",
        ),
        row(
            FINE_MESH,
            False,
            False,
            "需要机器可读的中段精细网格、每块端点 psi 值、最大跳点包络和 hash。",
            "fine mesh computation archive",
        ),
        row(
            JUMP_CONTROL,
            False,
            False,
            "需要定位或上界每个网格块中的素数幂跳跃，防止点间最大值逃逸。",
            "prime and prime-power jump certificate",
        ),
        row(
            ROUNDING,
            False,
            False,
            "需要证明 1.00002841 是对整段最大值的外向上舍入，而非仅对少数点值的舍入。",
            "directed rounding for interval supremum",
        ),
        row(
            TARGET,
            False,
            False,
            "当前完成点值压力和失败模式审计；整段中段 psi 覆盖尚未自足闭合。",
            f"{SHORT_INCREMENT} OR ({FINE_MESH} AND {JUMP_CONTROL} AND {ROUNDING})",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "中段有限区间 psi 覆盖审计不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_middle_finite_interval_psi_cover_router",
        "status": "middle_interval_point_values_good_sparse_monotonic_cover_fails_increment_or_fine_mesh_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "middle_finite_interval_psi_cover_closed": False,
        "table62_point_values_below_target": point_values_all_good,
        "sparse_point_monotonicity_cover_fails": naive_monotone_fails,
        "trivial_jump_envelope_requires_fine_mesh": True,
        "certified_short_interval_psi_increment_upper_closed": False,
        "middle_psi_fine_mesh_computation_hash_closed": False,
        "prime_power_jump_control_closed": False,
        "middle_psi_upper_directed_rounding_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_ratio": TARGET_RATIO,
        "x_right_e28": X_RIGHT,
        "point_rows": points,
        "naive_interval_rows": naive,
        "mesh_pressure_rows": mesh_pressure_rows(),
        "replacement_self_contained": {
            TARGET: f"{SHORT_INCREMENT} OR ({FINE_MESH} AND {JUMP_CONTROL} AND {ROUNDING})",
            SHORT_INCREMENT: "explicit upper envelope for psi increments on a certified partition of [8e11,e^28]",
        },
        "next_direct_attack_target": SHORT_INCREMENT,
        "parallel_attack_targets": [FINE_MESH, JUMP_CONTROL, ROUNDING],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "中段点值本身很强，但不能形成整段证明。Table 6.2 在几个节点的 psi/x 均低于目标，"
            "可是只用 psi 单调性和下一稀疏节点值会严重失败；点间最大值必须由短区间增量上界或精细网格加跳点证书控制。"
            "因此最新最窄点变为 `CertifiedShortIntervalPsiIncrementUpperEnvelopeLedger`。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 中段有限区间 psi 覆盖路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"middle_finite_interval_psi_cover_closed={fmt_bool(result['middle_finite_interval_psi_cover_closed'])}",
        f"table62_point_values_below_target={fmt_bool(result['table62_point_values_below_target'])}",
        f"sparse_point_monotonicity_cover_fails={fmt_bool(result['sparse_point_monotonicity_cover_fails'])}",
        f"trivial_jump_envelope_requires_fine_mesh={fmt_bool(result['trivial_jump_envelope_requires_fine_mesh'])}",
        f"certified_short_interval_psi_increment_upper_closed={fmt_bool(result['certified_short_interval_psi_increment_upper_closed'])}",
        f"middle_psi_fine_mesh_computation_hash_closed={fmt_bool(result['middle_psi_fine_mesh_computation_hash_closed'])}",
        f"prime_power_jump_control_closed={fmt_bool(result['prime_power_jump_control_closed'])}",
        f"middle_psi_upper_directed_rounding_closed={fmt_bool(result['middle_psi_upper_directed_rounding_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 点值余量",
        "",
        "| x | psi | psi/x | absolute_slack | beats_target |",
        "| ---: | ---: | ---: | ---: | --- |",
    ]
    for item in result["point_rows"]:
        lines.append(
            f"| `{fmt_float(float(item['x']))}` | `{fmt_float(float(item['psi']))}` | "
            f"`{fmt_float(float(item['ratio']))}` | `{fmt_float(float(item['absolute_slack']))}` | `{fmt_bool(item['beats_target'])}` |"
        )
    lines.extend(["", "## 2. 稀疏单调覆盖失败", "", "| interval | bound | defect | sufficient |", "| --- | ---: | ---: | --- |"])
    for item in result["naive_interval_rows"]:
        lines.append(
            f"| `{item['interval']}` | `{fmt_float(float(item['bound']))}` | "
            f"`{fmt_float(float(item['defect']))}` | `{fmt_bool(item['sufficient'])}` |"
        )
    lines.extend(["", "## 3. 粗跳跃网格压力", "", "| x | point_slack | max_mesh_under_trivial_integer_weight | meaning |", "| ---: | ---: | ---: | --- |"])
    for item in result["mesh_pressure_rows"]:
        lines.append(
            f"| `{fmt_float(float(item['x']))}` | `{fmt_float(float(item['point_slack']))}` | "
            f"`{fmt_float(float(item['max_mesh_under_trivial_integer_weight']))}` | {table_cell(item['meaning'])} |"
        )
    lines.extend(["", "## 4. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 5. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
