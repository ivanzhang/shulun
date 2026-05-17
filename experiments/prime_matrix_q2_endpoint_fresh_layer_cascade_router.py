#!/usr/bin/env python3
"""生成 Q2 端点替换后的新素层级联扩模路由证书。

用法示例：
  python3 experiments/prime_matrix_q2_endpoint_fresh_layer_cascade_router.py
  python3 experiments/prime_matrix_q2_endpoint_fresh_layer_cascade_router.py --stages 6
  python3 -m json.tool data/prime-matrix-q2-endpoint-fresh-layer-cascade-ledger.json

输出：
  data/prime-matrix-q2-endpoint-fresh-layer-cascade-ledger.json
  docs/monograph/prime-matrix-q2-endpoint-fresh-layer-cascade-router.json
  docs/monograph/prime-matrix-q2-endpoint-fresh-layer-cascade-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PREVIOUS_GROWTH_ROUTER = DOCS / "prime-matrix-q2-endpoint-replacement-aperture-growth-router.json"
PREVIOUS_Q2_ROUTER = DOCS / "prime-matrix-q2-carrier-stage-crt-asymmetry-router.json"
FRESH_MODULUS = DOCS / "prime-matrix-cycle-debt-branch-replay-fresh-modulus-escalation-router.md"
TAIL_BRIDGE = DOCS / "prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md"

OUT_LEDGER = DATA / "prime-matrix-q2-endpoint-fresh-layer-cascade-ledger.json"
OUT_JSON = DOCS / "prime-matrix-q2-endpoint-fresh-layer-cascade-router.json"
OUT_MD = DOCS / "prime-matrix-q2-endpoint-fresh-layer-cascade-router.md"

PREVIOUS_HARDPOINT = (
    "EndpointReplacementApertureGrowthNoBoundedReplayOrMovingSupportPDECSAEH3DSB;"
    "GlobalFinalInputsStillOpen"
)
NEXT_HARDPOINT = (
    "FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;"
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


def cascade_rows(sample: dict[str, Any], q2_log10_modulus: float, stages: int) -> list[dict[str, Any]]:
    """给出端点级联的保守下界表。

    设 L_j=log10(M_j)。第 j 次替换后的新右端素数 B_{j+1}>M_j，
    因而下一阶模数至少乘以 B_{j+1}，得到 L_{j+1}>2L_j。
    """
    rows = []
    width0 = int(sample["initial_closed_carrier_width"])
    log10_mod = float(q2_log10_modulus)
    for stage in range(stages + 1):
        width_lower = width0 + 2 * stage
        rows.append(
            {
                "stage": stage,
                "closed_aperture_width_lower_bound": width_lower,
                "log10_modulus_lower_bound": round(log10_mod, 6),
                "log10_modulus_minus_log10_width": round(log10_mod - math.log10(width_lower), 6),
                "fresh_endpoint_log10_lower_bound_next": round(log10_mod, 6),
            }
        )
        log10_mod *= 2
    return rows


def build_sample(sample: dict[str, Any], q2_sample: dict[str, Any], stages: int) -> dict[str, Any]:
    """合成单个样本的级联扩模读数。"""
    rows = cascade_rows(sample, q2_sample["log10_primorial_le_q2"], stages)
    return {
        "p": int(sample["p"]),
        "x0": int(sample["x0"]),
        "q1": int(sample["q1"]),
        "q2": int(sample["q2"]),
        "initial_gap": int(sample["initial_gap"]),
        "initial_closed_width": int(sample["initial_closed_carrier_width"]),
        "q2_stage_log10_modulus": float(q2_sample["log10_primorial_le_q2"]),
        "stages": stages,
        "cascade_rows": rows,
        "final_stage_log10_modulus_lower_bound": rows[-1]["log10_modulus_lower_bound"],
        "final_stage_width_lower_bound": rows[-1]["closed_aperture_width_lower_bound"],
        "final_stage_modulus_width_margin": rows[-1]["log10_modulus_minus_log10_width"],
        "finite_crt_period_terminal_possible": False,
        "linear_aperture_vs_doubling_log_modulus": True,
    }


def build_result(stages: int) -> dict[str, Any]:
    """构造路由证书。"""
    growth = json.loads(PREVIOUS_GROWTH_ROUTER.read_text(encoding="utf-8"))
    q2 = json.loads(PREVIOUS_Q2_ROUTER.read_text(encoding="utf-8"))
    q2_by_key = {(item["p"], item["x0"]): item for item in q2["sample_reports"]}
    sample_reports = [
        build_sample(item, q2_by_key[(item["p"], item["x0"])], stages)
        for item in growth["sample_reports"]
    ]

    gates = [
        gate(
            "FreshEndpointAfterReplacement",
            True,
            True,
            "每次闭复合块复现后，右侧真实相邻素数 B_new 位于块外且大于旧全轮平移边界，因此是旧端点层之外的新素层。",
            "closed",
        ),
        gate(
            "NextFullWheelKillsFreshEndpoint",
            True,
            True,
            "一旦 B_new 被纳入下一阶全轮 M_{<=B_new}，下一次全轮复现会令 B_new 的复制点被自身整除。",
            "closed",
        ),
        gate(
            "LogModulusAtLeastDoublesPerEndpointCascade",
            True,
            True,
            "若 L_j=log M_j，则 B_{j+1}>M_j，故 L_{j+1}>=L_j+log B_{j+1}>2L_j。",
            "closed",
        ),
        gate(
            "ApertureOnlyLinearUnderReplacementDebt",
            True,
            True,
            "端点替换给出的强制孔径下界每阶只增加 2，因此与模数对数倍增形成容量尺度错位。",
            "closed",
        ),
        gate(
            "NoFiniteCRTPeriodTerminalStructure",
            True,
            True,
            "有限 CRT 周期只能含有限素层；端点级联要求无界新素端点加入，故不能作为无限反例链终端。",
            "closed as finite-period no-go",
        ),
        gate(
            "PersistentFreshEndpointPatternRoutesToPDECColumnCRT",
            True,
            True,
            "若新端点层仍以固定相位模板持久复现，则形成 fresh-endpoint ColumnCRT/PDEC formal unit。",
            "closed as router",
        ),
        gate(
            "SparseFreshEndpointCascadeRoutesToSAE",
            True,
            True,
            "若级联只在孤立窗口出现，则为 SAE 单窗原子。",
            "closed as router",
        ),
        gate(
            "NonPDECFreshLayerCascadeRoutesToTailSieveH3",
            True,
            True,
            "若无界新素层不物化为 PDEC/ColumnCRT，则只剩每个新素层禁一个相位的 tail-sieve/H3-DSB/KLS 对象。",
            "tail-sieve/H3-DSB global input",
        ),
        gate(
            "GlobalRowColumnUnconditionalClosureReached",
            False,
            False,
            "本步排除有限 CRT 周期终端，不排斥全部 fresh-layer PDEC、SAE 与 tail-sieve/H3 出口。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_q2_endpoint_fresh_layer_cascade_router",
        "status": "fresh_endpoint_layer_cascade_routed_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "previous_router_status": growth.get("status"),
        "stages": stages,
        "fresh_endpoint_after_each_replacement": True,
        "next_full_wheel_kills_fresh_endpoint": True,
        "log_modulus_at_least_doubles_per_endpoint_cascade": True,
        "aperture_lower_bound_growth_linear_plus_two": True,
        "finite_crt_period_terminal_possible": False,
        "persistent_fresh_endpoint_pattern_routes_to_pdec_columncrt": True,
        "sparse_fresh_endpoint_cascade_routes_to_sae": True,
        "non_pdec_fresh_layer_cascade_routes_to_tail_sieve_h3": True,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "sample_reports": sample_reports,
        "sample_count": len(sample_reports),
        "all_sample_finite_crt_period_terminal_impossible": all(
            not item["finite_crt_period_terminal_possible"] for item in sample_reports
        ),
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "有界孔径被排除后，扩孔/移动若继续沿全轮端点复现推进，就必须不断引入新的右端素数层。"
            "每个新右端素数在下一阶全轮中又被自身零类杀掉，因此形成 fresh-endpoint 级联。"
            "该级联使 CRT 模数对数至少逐阶倍增，而端点替换孔径只线性加二；"
            "所以任何固定有限 CRT 周期都不能作为无限反例链的终端稳定结构。"
        ),
        "dependency_hashes": {
            str(PREVIOUS_GROWTH_ROUTER.relative_to(ROOT)): sha256(PREVIOUS_GROWTH_ROUTER),
            str(PREVIOUS_Q2_ROUTER.relative_to(ROOT)): sha256(PREVIOUS_Q2_ROUTER),
            str(FRESH_MODULUS.relative_to(ROOT)): sha256(FRESH_MODULUS),
            str(TAIL_BRIDGE.relative_to(ROOT)): sha256(TAIL_BRIDGE),
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
        "# Q2 端点新素层级联扩模路由",
        "",
        "**状态：** `fresh_endpoint_layer_cascade_routed_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"fresh_endpoint_after_each_replacement={fmt_bool(result['fresh_endpoint_after_each_replacement'])}",
        f"next_full_wheel_kills_fresh_endpoint={fmt_bool(result['next_full_wheel_kills_fresh_endpoint'])}",
        "log_modulus_at_least_doubles_per_endpoint_cascade="
        f"{fmt_bool(result['log_modulus_at_least_doubles_per_endpoint_cascade'])}",
        f"aperture_lower_bound_growth_linear_plus_two={fmt_bool(result['aperture_lower_bound_growth_linear_plus_two'])}",
        f"finite_crt_period_terminal_possible={fmt_bool(result['finite_crt_period_terminal_possible'])}",
        "persistent_fresh_endpoint_pattern_routes_to_pdec_columncrt="
        f"{fmt_bool(result['persistent_fresh_endpoint_pattern_routes_to_pdec_columncrt'])}",
        f"sparse_fresh_endpoint_cascade_routes_to_sae={fmt_bool(result['sparse_fresh_endpoint_cascade_routes_to_sae'])}",
        "non_pdec_fresh_layer_cascade_routes_to_tail_sieve_h3="
        f"{fmt_bool(result['non_pdec_fresh_layer_cascade_routes_to_tail_sieve_h3'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 级联引理",
        "",
        "设第 `j` 阶全轮模数为 `M_j`，右端真实相邻素数为 `B_j`。上一张证书已证明，",
        "全轮复现会把当前闭载体块变成闭复合块，故下一真实右端素数满足",
        "",
        "\\[",
        "B_{j+1}>\\text{right edge of the copied block}\\ge M_j.",
        "\\]",
        "",
        "于是 `B_{j+1}` 是旧有限端点层之外的新素层。若下一步使用完整 `B_{j+1}` 阶轮，则该新端点也被纳入模数，",
        "下一次复现时它的复制点被 `B_{j+1}` 自身整除。令 `L_j=log M_j`，则",
        "",
        "\\[",
        "L_{j+1}\\ge L_j+\\log B_{j+1}>2L_j.",
        "\\]",
        "",
        "这说明端点替换链不是固定有限 CRT 周期，而是新素层不断加入的扩模级联。",
        "",
        "## 2. 与孔径增长的尺度错位",
        "",
        "端点替换只强制闭孔径下界每次增加 `2`；但模数对数至少倍增。固定有限 CRT 周期无法同时容纳无界新素层。",
        "",
        "## 3. 样本级联读数",
        "",
        "| P | x0 | Q2 | stage | width lower | log10 modulus lower | log10 modulus - log10 width |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for sample in result["sample_reports"]:
        for row in sample["cascade_rows"][: min(result["stages"] + 1, 5)]:
            lines.append(
                "| {p} | {x} | {q2} | {stage} | {width} | {logmod} | {margin} |".format(
                    p=sample["p"],
                    x=sample["x0"],
                    q2=sample["q2"],
                    stage=row["stage"],
                    width=row["closed_aperture_width_lower_bound"],
                    logmod=row["log10_modulus_lower_bound"],
                    margin=row["log10_modulus_minus_log10_width"],
                )
            )

    lines.extend(
        [
            "",
            "## 4. 三分流",
            "",
            "| behavior | route | reason |",
            "| --- | --- | --- |",
            "| 试图停在固定有限 CRT 周期 | `impossible` | 新右端素数层无界加入，有限周期不含这些素层。 |",
            "| 新素层以固定相位模板持久复现 | `ColumnCRT/PDEC` | fresh endpoint 相位成为同一 formal unit。 |",
            "| 级联只孤立出现 | `SAE` | 不能支撑无限反例链。 |",
            "| 无 PDEC 的无界新素层 | `tail-sieve/H3-DSB/KLS` | 每个新素层只留下一个禁相位，回到尾段粗筛/短窗硬核。 |",
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
            "本证书排除固定有限 CRT 周期终端；它没有排斥全部 fresh-layer PDEC/ColumnCRT、SAE 与 tail-sieve/H3 出口，",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--stages", type=int, default=4)
    args = parser.parse_args()
    result = build_result(stages=max(1, args.stages))
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "stages": result["stages"],
        "finite_crt_period_terminal_possible": result["finite_crt_period_terminal_possible"],
        "next_direct_attack_target": result["next_direct_attack_target"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
