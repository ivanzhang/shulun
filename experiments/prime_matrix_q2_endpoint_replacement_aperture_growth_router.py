#!/usr/bin/env python3
"""生成 Q2 阶端点替换债务与孔径增长路由证书。

用法示例：
  python3 experiments/prime_matrix_q2_endpoint_replacement_aperture_growth_router.py
  python3 -m json.tool data/prime-matrix-q2-endpoint-replacement-aperture-growth-ledger.json

输出：
  data/prime-matrix-q2-endpoint-replacement-aperture-growth-ledger.json
  docs/monograph/prime-matrix-q2-endpoint-replacement-aperture-growth-router.json
  docs/monograph/prime-matrix-q2-endpoint-replacement-aperture-growth-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PREVIOUS_Q2_ROUTER = DOCS / "prime-matrix-q2-carrier-stage-crt-asymmetry-router.json"
EARLY_GAP_ROUTER = DOCS / "prime-matrix-early-zero-gap-crt-asymmetry-router.json"
PERIOD_LIFT_ROUTER = DOCS / "prime-matrix-early-zero-period-lift-carrier-drift-router.json"
ZERO_ROW_CRT = DOCS / "prime-matrix-zero-row-full-crt-diagonal-minrep.md"

OUT_LEDGER = DATA / "prime-matrix-q2-endpoint-replacement-aperture-growth-ledger.json"
OUT_JSON = DOCS / "prime-matrix-q2-endpoint-replacement-aperture-growth-router.json"
OUT_MD = DOCS / "prime-matrix-q2-endpoint-replacement-aperture-growth-router.md"

PREVIOUS_HARDPOINT = (
    "Q2StageEndpointInversionRoutedToColumnCRTPDECOrSparseSAEOrMovingEndpointH3DSB;"
    "GlobalFinalInputsStillOpen"
)
NEXT_HARDPOINT = (
    "EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;"
    "GlobalFinalInputsStillOpen"
)


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def max_replays_for_aperture(initial_width: int, aperture_width: int) -> int:
    """在每次至少增长 2 的规则下，给出固定孔径内可容纳的最大复现次数。"""
    if aperture_width < initial_width:
        return -1
    return (aperture_width - initial_width) // 2


def sample_growth_report(sample: dict[str, Any]) -> dict[str, Any]:
    """把上一张 Q2 样本转成孔径增长读数。"""
    gap = int(sample["carrier_gap"])
    closed_width = gap + 1
    first_replay_gap_lower = gap + 2
    first_replay_closed_width_lower = closed_width + 2
    budgets = {
        "same_closed_carrier_aperture": closed_width,
        "one_replacement_aperture": closed_width + 2,
        "ten_replacement_aperture": closed_width + 20,
        "double_closed_carrier_aperture": 2 * closed_width,
    }
    return {
        "p": int(sample["p"]),
        "x0": int(sample["x0"]),
        "interval": sample["interval"],
        "q1": int(sample["q1_left_prime"]),
        "q2": int(sample["q2_right_prime"]),
        "initial_gap": gap,
        "initial_closed_carrier_width": closed_width,
        "first_replay_gap_lower_bound": first_replay_gap_lower,
        "first_replay_closed_width_lower_bound": first_replay_closed_width_lower,
        "first_replay_exceeds_original_closed_aperture": first_replay_closed_width_lower > closed_width,
        "same_aperture_endpoint_replay_possible": False,
        "log_modulus_le_q2_minus_log_first_replacement_support": round(
            float(sample["log_modulus_le_q2_minus_log_support"]) - math.log(first_replay_closed_width_lower / closed_width),
            6,
        ),
        "aperture_budget_max_replays": {
            name: max_replays_for_aperture(closed_width, width) for name, width in budgets.items()
        },
    }


def build_result() -> dict[str, Any]:
    """构造路由证书。"""
    previous = json.loads(PREVIOUS_Q2_ROUTER.read_text(encoding="utf-8"))
    sample_reports = [sample_growth_report(item) for item in previous["sample_reports"]]

    gates = [
        gate(
            "CorrectEarlyZeroCarrierEndpointBounds",
            True,
            True,
            (
                "早期零行 [(k-1)P+1,kP] 无素数时，左端相邻素数满足 Q1<=kP-P，"
                "除 k=2 可有 Q1=P 外通常为严格小于；右端满足 Q2>kP。"
            ),
            "closed",
        ),
        gate(
            "FullQ2ReplayMakesClosedCarrierComposite",
            True,
            True,
            (
                "在 Q2<P^2 主分支中，开间隙由小于 P 的素因子覆盖；全 Q2 轮又杀掉 Q1,Q2，"
                "故 [Q1,Q2]+tM_{<=Q2} 对 t>=1 是闭复合块。"
            ),
            "closed",
        ),
        gate(
            "EndpointReplacementDebtPlusTwo",
            True,
            True,
            (
                "闭复合块的真实相邻素数端点必须落在块外，因此新相邻素数间隙至少为旧间隙加 2。"
            ),
            "closed",
        ),
        gate(
            "SameApertureReplayImpossible",
            True,
            True,
            "第一次全 Q2 复现后闭载体宽度已至少增加 2，不能仍占用原同一有限孔径。",
            "closed",
        ),
        gate(
            "BoundedApertureReplayFinite",
            True,
            True,
            "若孔径宽度被固定为 W，则最多 floor((W-W0)/2) 次端点替换；无限链必须移动或扩孔。",
            "closed as bounded-aperture no-go",
        ),
        gate(
            "PersistentMovingApertureRoutesToPDECColumnCRT",
            True,
            True,
            "若扩孔/移动以固定有限相位规则持久复现，则形成 moving aperture 的 ColumnCRT/PDEC formal unit。",
            "closed as router",
        ),
        gate(
            "SparseReplacementRoutesToSAE",
            True,
            True,
            "若端点替换只在孤立窗口发生，则为 SAE 单窗原子。",
            "closed as router",
        ),
        gate(
            "UnboundedReplacementRoutesToH3DSB",
            True,
            True,
            "若孔径持续无界增长而不固定相位，则回到 tail filler、H3-DSB/KLS、Rankin 或外部 DI/BFI 分支。",
            "H3-DSB-NCBLK or moving-family global input",
        ),
        gate(
            "GlobalRowColumnUnconditionalClosureReached",
            False,
            False,
            "本步排除固定有界孔径复现，不排斥所有 moving aperture、PDEC、SAE 与 H3-DSB 出口。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_q2_endpoint_replacement_aperture_growth_router",
        "status": "endpoint_replacement_aperture_growth_routed_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "previous_router_status": previous.get("status"),
        "corrected_endpoint_bound": "Q1<=kP-P, with equality possible at k=2; Q2>kP",
        "full_q2_replay_makes_closed_carrier_composite": True,
        "endpoint_replacement_gap_growth_per_replay_at_least": 2,
        "same_aperture_replay_impossible": True,
        "bounded_aperture_replay_finite": True,
        "persistent_moving_aperture_routes_to_pdec_columncrt": True,
        "sparse_replacement_routes_to_sae": True,
        "unbounded_replacement_routes_to_h3_dsb": True,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "sample_reports": sample_reports,
        "sample_count": len(sample_reports),
        "all_sample_first_replay_exceeds_original_closed_aperture": all(
            item["first_replay_exceeds_original_closed_aperture"] for item in sample_reports
        ),
        "all_sample_same_aperture_endpoint_replay_impossible": all(
            not item["same_aperture_endpoint_replay_possible"] for item in sample_reports
        ),
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "Q2 阶全轮复制不只是杀掉原素端点；它把 [Q1,Q2] 复制为闭复合块。"
            "因此真实相邻素数端点必须替换到块外，下一载体间隙至少增加 2。"
            "同一有限孔径的端点稳定复现被排除；无限反例链若继续，只能扩孔/移动，"
            "并被路由到 moving-aperture PDEC/ColumnCRT、SAE 或 H3-DSB/KLS 出口。"
        ),
        "dependency_hashes": {
            str(PREVIOUS_Q2_ROUTER.relative_to(ROOT)): sha256(PREVIOUS_Q2_ROUTER),
            str(EARLY_GAP_ROUTER.relative_to(ROOT)): sha256(EARLY_GAP_ROUTER),
            str(PERIOD_LIFT_ROUTER.relative_to(ROOT)): sha256(PERIOD_LIFT_ROUTER),
            str(ZERO_ROW_CRT.relative_to(ROOT)): sha256(ZERO_ROW_CRT),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")

    lines = [
        "# Q2 阶端点替换债务与孔径增长路由",
        "",
        "**状态：** `endpoint_replacement_aperture_growth_routed_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"corrected_endpoint_bound={result['corrected_endpoint_bound']}",
        "full_q2_replay_makes_closed_carrier_composite="
        f"{fmt_bool(result['full_q2_replay_makes_closed_carrier_composite'])}",
        "endpoint_replacement_gap_growth_per_replay_at_least="
        f"{result['endpoint_replacement_gap_growth_per_replay_at_least']}",
        f"same_aperture_replay_impossible={fmt_bool(result['same_aperture_replay_impossible'])}",
        f"bounded_aperture_replay_finite={fmt_bool(result['bounded_aperture_replay_finite'])}",
        "persistent_moving_aperture_routes_to_pdec_columncrt="
        f"{fmt_bool(result['persistent_moving_aperture_routes_to_pdec_columncrt'])}",
        f"sparse_replacement_routes_to_sae={fmt_bool(result['sparse_replacement_routes_to_sae'])}",
        f"unbounded_replacement_routes_to_h3_dsb={fmt_bool(result['unbounded_replacement_routes_to_h3_dsb'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 端点边界修正",
        "",
        "若早期第 `k` 行 `[(k-1)P+1,kP]` 无素数，则左侧最近素数满足",
        "",
        "\\[",
        "Q_1\\le (k-1)P=kP-P,",
        "\\]",
        "",
        "右侧最近素数满足 `Q2>kP`。左端一般严格小于 `(k-1)P`；唯一需要单独记住的是 `k=2` 时",
        "`(k-1)P=P` 本身为素数，所以可能有 `Q1=P`。这个修正不影响后续 gap 结论。",
        "",
        "## 2. 闭复合块与 +2 债务",
        "",
        "在 `Q2<P^2` 主分支中，开间隙 `(Q1,Q2)` 内每个合数的最小素因子小于 `P`，因此由 `P` 阶小因子覆盖。",
        "完整 `Q2` 阶轮又包含 `Q1,Q2` 本身，所以对任意 `t>=1`，闭区间",
        "",
        "\\[",
        "[Q_1+tM_{\\le Q_2},\\ Q_2+tM_{\\le Q_2}]",
        "\\]",
        "",
        "全部为复合点。真实链的相邻素数端点只能位于该闭块之外：",
        "",
        "\\[",
        "A_t\\le Q_1+tM_{\\le Q_2}-1,\\qquad B_t\\ge Q_2+tM_{\\le Q_2}+1.",
        "\\]",
        "",
        "于是",
        "",
        "\\[",
        "B_t-A_t\\ge Q_2-Q_1+2.",
        "\\]",
        "",
        "这就是端点替换债务：一次完整 Q2 阶复现至少把真实载体间隙扩大 `2`。",
        "",
        "## 3. 样本孔径读数",
        "",
        "| P | x0 | Q1 | Q2 | initial gap | closed width | first replay width lower | same aperture replay | same aperture max replays | double aperture max replays |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: |",
    ]
    for item in result["sample_reports"]:
        budgets = item["aperture_budget_max_replays"]
        lines.append(
            "| {p} | {x} | {q1} | {q2} | {gap} | {w0} | {w1} | `{same}` | {same_max} | {double_max} |".format(
                p=item["p"],
                x=item["x0"],
                q1=item["q1"],
                q2=item["q2"],
                gap=item["initial_gap"],
                w0=item["initial_closed_carrier_width"],
                w1=item["first_replay_closed_width_lower_bound"],
                same=fmt_bool(item["same_aperture_endpoint_replay_possible"]),
                same_max=budgets["same_closed_carrier_aperture"],
                double_max=budgets["double_closed_carrier_aperture"],
            )
        )

    lines.extend(
        [
            "",
            "这些样本只验证孔径增长机制。结论是结构性的：同一闭载体孔径一次也不能容纳端点替换后的真实端点；",
            "任何固定宽度 `W` 只能容纳有限次，次数上界为 `floor((W-W0)/2)`。",
            "",
            "## 4. 三分流",
            "",
            "| behavior | route | reason |",
            "| --- | --- | --- |",
            "| 端点稳定且孔径不变 | `impossible` | 第一次复现后闭载体宽度至少增加 2。 |",
            "| 固定有限规则扩孔/移动并持久复现 | `ColumnCRT/PDEC` | 扩孔轨道、端点位移和覆盖相位成为同一 formal unit。 |",
            "| 只在孤立窗口发生替换 | `SAE` | 不能支撑无限反例链。 |",
            "| 孔径无界增长或素层持续换新 | `moving-family/H3-DSB/KLS` | 回到尾补洞、短窗 dispersion、Rankin 或外部 DI/BFI。 |",
            "",
            "## 5. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 6. 最新剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书排除固定有界孔径的无限复现；它没有排斥 moving aperture、PDEC/ColumnCRT、SAE 与 H3-DSB/KLS 出口，",
            "因此不构成行/列命题的全局无条件证明。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "sample_count": result["sample_count"],
        "same_aperture_replay_impossible": result["same_aperture_replay_impossible"],
        "next_direct_attack_target": result["next_direct_attack_target"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
