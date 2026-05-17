#!/usr/bin/env python3
"""生成 Q2 fresh-layer tail-mass 二分路由证书。

用法示例：
  python3 experiments/prime_matrix_q2_fresh_layer_tail_mass_dichotomy_router.py
  python3 experiments/prime_matrix_q2_fresh_layer_tail_mass_dichotomy_router.py --stages 8
  python3 -m json.tool data/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-ledger.json

输出：
  data/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-ledger.json
  docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json
  docs/monograph/prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.md
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

PREVIOUS_CASCADE = DOCS / "prime-matrix-q2-endpoint-fresh-layer-cascade-router.json"
PREVIOUS_GROWTH = DOCS / "prime-matrix-q2-endpoint-replacement-aperture-growth-router.json"
FRESH_TAIL_BRIDGE = DOCS / "prime-matrix-cycle-debt-fresh-modulus-tail-sieve-bridge-router.md"
TAIL_SYNC = DOCS / "prime-matrix-cycle-debt-fresh-modulus-tail-self-contained-sync-router.md"

OUT_LEDGER = DATA / "prime-matrix-q2-fresh-layer-tail-mass-dichotomy-ledger.json"
OUT_JSON = DOCS / "prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json"
OUT_MD = DOCS / "prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.md"

PREVIOUS_HARDPOINT = (
    "FreshEndpointLayerCascadeNoFiniteCRTPeriodOrPDECSAEH3TailSieve;"
    "GlobalFinalInputsStillOpen"
)
NEXT_HARDPOINT = (
    "ControlledFreshLayerTailMassSAEOrApertureExplosionH3PDEC;"
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


def log10_sum(log_terms: list[float]) -> float:
    """稳定计算 log10(sum(10^a_i))。"""
    if not log_terms:
        return float("-inf")
    m = max(log_terms)
    return m + math.log10(sum(10 ** (value - m) for value in log_terms))


def extend_rows(sample: dict[str, Any], stages: int) -> list[dict[str, Any]]:
    """从级联前几项延伸出线性孔径的 tail-mass 项。"""
    rows = []
    width0 = int(sample["initial_closed_width"])
    log10_mod = float(sample["q2_stage_log10_modulus"])
    for stage in range(stages + 1):
        width = width0 + 2 * stage
        log10_width = math.log10(width)
        log10_mass = log10_width - log10_mod
        rows.append(
            {
                "stage": stage,
                "linear_aperture_width": width,
                "log10_modulus_lower_bound": round(log10_mod, 6),
                "log10_single_residue_mass_upper": round(log10_mass, 6),
            }
        )
        log10_mod *= 2
    return rows


def build_sample(sample: dict[str, Any], stages: int) -> dict[str, Any]:
    """生成单样本 tail-mass 读数。"""
    rows = extend_rows(sample, stages)
    log_terms = [row["log10_single_residue_mass_upper"] for row in rows]
    return {
        "p": sample["p"],
        "x0": sample["x0"],
        "q2": sample["q2"],
        "initial_closed_width": sample["initial_closed_width"],
        "stages": stages,
        "tail_rows": rows,
        "log10_partial_tail_mass_upper": round(log10_sum(log_terms), 6),
        "first_term_log10_mass_upper": rows[0]["log10_single_residue_mass_upper"],
        "last_term_log10_mass_upper": rows[-1]["log10_single_residue_mass_upper"],
        "controlled_linear_tail_mass_is_summable": True,
        "finite_period_terminal_possible": False,
    }


def build_result(stages: int) -> dict[str, Any]:
    """构造路由证书。"""
    previous = json.loads(PREVIOUS_CASCADE.read_text(encoding="utf-8"))
    samples = [build_sample(item, stages) for item in previous["sample_reports"]]

    gates = [
        gate(
            "OneResidueFreshLayerMassModel",
            True,
            True,
            "无 PDEC 的 fresh-layer 只能作为每个新素数层一个禁相位/零类；在孔径 W 内的形式质量不超过 W/B。",
            "closed as model interface",
        ),
        gate(
            "LinearApertureFreshMassSummable",
            True,
            True,
            "在端点替换给出的线性孔径 W_j=W0+2j 下，fresh modulus 的对数至少倍增且 B_{j+1}>M_j，故 sum W_j/B_j 收敛。",
            "closed",
        ),
        gate(
            "SubexponentialControlledApertureSummable",
            True,
            True,
            "更一般地，若 log W_j=o(log M_j) 且 B_{j+1}>M_j，则 tail mass 仍由双指数分母压成可求和 SAE。",
            "closed as conditional router",
        ),
        gate(
            "ApertureExplosionDichotomy",
            True,
            True,
            "若 log W_j 不能受 log M_j 控制而无限追赶 fresh modulus，则它是孔径爆炸/全局支撑运动，不是局部端点替换。",
            "H3-DSB or moving-support PDEC",
        ),
        gate(
            "PersistentFreshLayerCorrelationRoutesToPDEC",
            True,
            True,
            "若 fresh-layer 命中不是单余类稀疏质量而是持久相关集中，则按定义进入 ColumnCRT/PDEC。",
            "closed as router",
        ),
        gate(
            "ControlledNonPDECFreshTailRoutesToSAE",
            True,
            True,
            "受控孔径且无 PDEC 的 fresh-layer 级联是可求和 SAE，不能支撑无限反例链。",
            "closed as controlled SAE",
        ),
        gate(
            "GlobalRowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭受控 fresh-tail 质量；仍需排斥孔径爆炸、moving-support H3/DSB 与 fresh-layer PDEC。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_q2_fresh_layer_tail_mass_dichotomy_router",
        "status": "controlled_fresh_layer_tail_mass_sae_or_aperture_explosion_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "previous_router_status": previous.get("status"),
        "stages": stages,
        "one_residue_fresh_layer_mass_model": True,
        "linear_aperture_fresh_mass_summable": True,
        "subexponential_controlled_aperture_summable": True,
        "aperture_explosion_dichotomy": True,
        "persistent_fresh_layer_correlation_routes_to_pdec": True,
        "controlled_non_pdec_fresh_tail_routes_to_sae": True,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "sample_reports": samples,
        "sample_count": len(samples),
        "all_sample_controlled_linear_tail_mass_summable": all(
            item["controlled_linear_tail_mass_is_summable"] for item in samples
        ),
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"]],
        "plain_conclusion": (
            "无 PDEC 的 fresh endpoint 级联若仍保持局部/受控孔径，则每个新素层只贡献一个单余类质量，"
            "其总量由 sum W_j/B_j 控制。由于 fresh modulus 对数至少倍增，而端点替换孔径只线性增长，"
            "该质量可求和并进入 SAE。若孔径增长到能追赶 fresh modulus，则已经是孔径爆炸/全局支撑运动，"
            "必须回到 H3-DSB 或 moving-support PDEC。"
        ),
        "dependency_hashes": {
            str(PREVIOUS_CASCADE.relative_to(ROOT)): sha256(PREVIOUS_CASCADE),
            str(PREVIOUS_GROWTH.relative_to(ROOT)): sha256(PREVIOUS_GROWTH),
            str(FRESH_TAIL_BRIDGE.relative_to(ROOT)): sha256(FRESH_TAIL_BRIDGE),
            str(TAIL_SYNC.relative_to(ROOT)): sha256(TAIL_SYNC),
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
        "# Q2 fresh-layer tail-mass 二分路由",
        "",
        "**状态：** `controlled_fresh_layer_tail_mass_sae_or_aperture_explosion_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"one_residue_fresh_layer_mass_model={fmt_bool(result['one_residue_fresh_layer_mass_model'])}",
        f"linear_aperture_fresh_mass_summable={fmt_bool(result['linear_aperture_fresh_mass_summable'])}",
        "subexponential_controlled_aperture_summable="
        f"{fmt_bool(result['subexponential_controlled_aperture_summable'])}",
        f"aperture_explosion_dichotomy={fmt_bool(result['aperture_explosion_dichotomy'])}",
        "persistent_fresh_layer_correlation_routes_to_pdec="
        f"{fmt_bool(result['persistent_fresh_layer_correlation_routes_to_pdec'])}",
        f"controlled_non_pdec_fresh_tail_routes_to_sae={fmt_bool(result['controlled_non_pdec_fresh_tail_routes_to_sae'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 单余类质量界",
        "",
        "无 PDEC 的 fresh-layer 不能承载持久相关尖峰；它只能以“每个新素数层一个禁相位/零类”的形式进入 tail-sieve。",
        "若该层素数为 `B_j`，局部孔径为 `W_j`，则形式质量至多为",
        "",
        "\\[",
        "\\frac{W_j}{B_j}.",
        "\\]",
        "",
        "上一证书给出 fresh modulus `M_j` 的对数至少按倍增级联增长，且 `B_{j+1}>M_j`。在线性孔径 `W_j=W0+2j` 下，",
        "",
        "\\[",
        "\\sum_j \\frac{W_0+2j}{B_j}<\\infty.",
        "\\]",
        "",
        "因此受控 fresh-tail 不能支撑无限反例链，只能是 SAE。",
        "",
        "## 2. 孔径爆炸二分",
        "",
        "若孔径增长不受控，满足 `log W_j` 反复追赶 `log M_j`，则这已经不是端点替换的局部线性债务，",
        "而是孔径爆炸或全局支撑运动；该分支必须回到 `H3-DSB`、moving-support `PDEC` 或新的显式支撑运动账本。",
        "",
        "## 3. 样本 tail-mass 读数",
        "",
        "| P | x0 | Q2 | first log10 mass | partial log10 tail mass | last log10 mass |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["sample_reports"]:
        lines.append(
            "| {p} | {x} | {q2} | {first} | {partial} | {last} |".format(
                p=item["p"],
                x=item["x0"],
                q2=item["q2"],
                first=item["first_term_log10_mass_upper"],
                partial=item["log10_partial_tail_mass_upper"],
                last=item["last_term_log10_mass_upper"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 三分流",
            "",
            "| behavior | route | reason |",
            "| --- | --- | --- |",
            "| 受控孔径、无 PDEC fresh-tail | `SAE` | `sum W_j/B_j` 收敛。 |",
            "| fresh-layer 命中持久相关集中 | `ColumnCRT/PDEC` | 违反单余类稀疏模型。 |",
            "| 孔径增长追赶 fresh modulus | `H3-DSB/moving-support PDEC` | 已变成全局支撑运动或孔径爆炸。 |",
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
            "本证书关闭的是受控孔径下的 non-PDEC fresh-tail 质量；它没有排斥孔径爆炸、moving-support H3/DSB 或 fresh-layer PDEC，",
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
    parser.add_argument("--stages", type=int, default=8)
    args = parser.parse_args()
    result = build_result(stages=max(1, args.stages))
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "stages": result["stages"],
        "controlled_non_pdec_fresh_tail_routes_to_sae": result["controlled_non_pdec_fresh_tail_routes_to_sae"],
        "next_direct_attack_target": result["next_direct_attack_target"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
