#!/usr/bin/env python3
"""生成 strict 短窗口除数密度 LCM 乘子纪律路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_short_window_divisor_density_lcm_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-short-window-divisor-density-lcm-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-windowed-reciprocal-divisor-density-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-reciprocal-common-divisor-envelope-router.md",
    MONOGRAPH / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md",
    MONOGRAPH / "h4-pdec-admissible-constraint-table.md",
]

SHORT_DENSITY = "ShortWindowDivisorDensityEnvelopeForFrequencyH"
LCM_MULTIPLIER = "ShortWindowLCMMultiplierDisciplineForFrequencyH"
HEIGHT_CEILING = "FormalFrequencyHeightCeilingForEndpointPDEC"
LOW_MULTIPLIER = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
HOT_DENSITY = "HotFrequencyDivisorDensityPDECorSAE"
PDEC_COMPARE = "WeightedPositiveEndpointPDECLowerBoundComparison"
DENSE_LCM = "DenseShortWindowLCMLowerBoundAfterKernelCompression"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def lemmas() -> list[dict[str, str]]:
    """列出 LCM 乘子纪律引理。"""
    return [
        {
            "name": "short_window_antichain",
            "formula": "If Y<g<g'<=2Y, then g does not divide g'.",
            "status": "closed",
            "meaning": "同一短乘法窗口中的不同除数互不整除，不能靠简单倍数链解释高密度。",
        },
        {
            "name": "lcm_anchor_divides_frequency",
            "formula": "For A={g: Y<g<=2Y and g|h}, L(A)=lcm(A) divides h.",
            "status": "closed",
            "meaning": "热除数窗口被锚定在单个频率 h 上，LCM 不能脱离频率高度预算。",
        },
        {
            "name": "incremental_multiplier_identity",
            "formula": "L_t/L_{t-1}=g_t/gcd(g_t,L_{t-1}), and product_t L_t/L_{t-1}=L(A).",
            "status": "closed",
            "meaning": "每加入一个新除数，要么贡献新 LCM 乘子，要么与旧 LCM 有大共同核。",
        },
        {
            "name": "high_multiplier_count_bound",
            "formula": "If L(A)<=H, then #{t: mu_t>=Lambda} <= floor(log H/log Lambda).",
            "status": "closed",
            "meaning": "频率高度上界直接限制独立新乘子数量。",
        },
        {
            "name": "low_multiplier_kernel_forcing",
            "formula": "If mu_t<Lambda, then gcd(g_t,L_{t-1})>Y/Lambda.",
            "status": "closed",
            "meaning": "不能造成 LCM 爆炸的除数必须与既有除数云共享大共同核。",
        },
        {
            "name": "density_to_multiplier_pressure",
            "formula": "N_h(Y,2Y]>=eta Y forces either many high multipliers or many low-multiplier kernel recurrences.",
            "status": "closed_dichotomy",
            "meaning": "短窗口线性密度不再是裸 tau 问题，而被拆成 LCM 爆炸或共同核复现。",
        },
        {
            "name": "kernel_recurrence_to_registered_defect",
            "formula": "Persistent low-multiplier kernel recurrences must route to ColumnCRT/PDEC; isolated ones route to SAE.",
            "status": "registered_route_open",
            "meaning": "共同核复现已命名为下一个出口，但尚未完成排斥。",
        },
        {
            "name": "dense_lcm_after_kernel_compression",
            "formula": "After excluding low-multiplier kernel recurrences, dense A should force log L(A)>=c(eta,Lambda)Y.",
            "status": "open_input",
            "meaning": "这是剩余的确定性 LCM 下界输入，不能由普通 tau(h) 粗估计替代。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链产生的低有效模/端点缺陷链条内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ShortWindowDensityMaterialized",
            "closed": True,
            "proved": True,
            "meaning": "上一层已把倒数封套失败物化为 N_h(Y,2Y]>=eta Y。",
            "remaining": LCM_MULTIPLIER,
        },
        {
            "gate": "LCMAnchorClosed",
            "closed": True,
            "proved": True,
            "meaning": "该窗口全部除数的 LCM 必整除同一个正式频率 h。",
            "remaining": HEIGHT_CEILING,
        },
        {
            "gate": "IncrementalMultiplierDisciplineClosed",
            "closed": True,
            "proved": True,
            "meaning": "高独立乘子数量受 log H/log Lambda 限制；其余强制大共同核。",
            "remaining": LOW_MULTIPLIER,
        },
        {
            "gate": "LowMultiplierKernelRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "大共同核复现应形成低商 ColumnCRT/PDEC 或孤立 SAE，但排斥未完成。",
            "remaining": f"{LOW_MULTIPLIER} AND {HOT_DENSITY}",
        },
        {
            "gate": "DenseLCMAfterKernelCompressionProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明排除共同核出口后，任意热窗口必须产生超过频率高度的 LCM 爆炸。",
            "remaining": f"{DENSE_LCM} AND {HEIGHT_CEILING}",
        },
        {
            "gate": "ShortWindowDivisorDensityEnvelopeCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未完成正式频率族的短窗口除数密度上界与 PDEC 下界比较。",
            "remaining": f"{DENSE_LCM} AND {LOW_MULTIPLIER} AND {PDEC_COMPARE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_short_window_divisor_density_lcm_router",
        "status": "short_window_divisor_density_reduced_to_lcm_multiplier_or_common_kernel_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "short_window_density_materialized": True,
        "short_window_antichain_closed": True,
        "lcm_anchor_closed": True,
        "incremental_multiplier_discipline_closed": True,
        "high_multiplier_count_bound_closed": True,
        "low_multiplier_kernel_forcing_closed": True,
        "low_multiplier_kernel_route_registered": True,
        "dense_lcm_after_kernel_compression_proved": False,
        "formal_frequency_height_ceiling_matched": False,
        "low_multiplier_common_kernel_excluded": False,
        "short_window_divisor_density_envelope_proved": False,
        "hot_density_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LOW_MULTIPLIER,
        "secondary_attack_target": DENSE_LCM,
        "parallel_targets": [HEIGHT_CEILING, HOT_DENSITY, PDEC_COMPARE],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "短窗口高密度除数已经进一步压成 LCM 乘子纪律。若 A={g: Y<g<=2Y, g|h} "
            "且 |A|>=eta Y，则 L(A) 必整除同一正式频率 h。按任意顺序加入 g_t，"
            "新增乘子 mu_t=L_t/L_{t-1}=g_t/gcd(g_t,L_{t-1})。若 L(A)<=H，"
            "则 mu_t>=Lambda 的次数至多为 log H/log Lambda；剩余大量 g_t 必满足 "
            "gcd(g_t,L_{t-1})>Y/Lambda，即出现大共同核复现。"
            "因此当前硬点不再是裸除数函数估计，而是二选一：LCM 爆炸超过频率高度，"
            "或共同核复现进入 ColumnCRT/PDEC/SAE。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 短窗口除数密度 LCM 乘子纪律路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"short_window_density_materialized={fmt_bool(result['short_window_density_materialized'])}",
        f"short_window_antichain_closed={fmt_bool(result['short_window_antichain_closed'])}",
        f"lcm_anchor_closed={fmt_bool(result['lcm_anchor_closed'])}",
        f"incremental_multiplier_discipline_closed={fmt_bool(result['incremental_multiplier_discipline_closed'])}",
        f"high_multiplier_count_bound_closed={fmt_bool(result['high_multiplier_count_bound_closed'])}",
        f"low_multiplier_kernel_forcing_closed={fmt_bool(result['low_multiplier_kernel_forcing_closed'])}",
        f"low_multiplier_kernel_route_registered={fmt_bool(result['low_multiplier_kernel_route_registered'])}",
        f"dense_lcm_after_kernel_compression_proved={fmt_bool(result['dense_lcm_after_kernel_compression_proved'])}",
        f"formal_frequency_height_ceiling_matched={fmt_bool(result['formal_frequency_height_ceiling_matched'])}",
        f"low_multiplier_common_kernel_excluded={fmt_bool(result['low_multiplier_common_kernel_excluded'])}",
        f"short_window_divisor_density_envelope_proved={fmt_bool(result['short_window_divisor_density_envelope_proved'])}",
        f"hot_density_excluded={fmt_bool(result['hot_density_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 乘子纪律",
        "",
        "设",
        "",
        "```text",
        "A=A(h;Y)={g: Y<g<=2Y, g|h},  N=|A|.",
        "```",
        "",
        "若上一层热窗口给出 `N>=eta Y`，则所有 `g in A` 同时整除频率 `h`，因此",
        "",
        "```text",
        "L(A)=lcm(A) | h.",
        "```",
        "",
        "任选顺序 `g_1,...,g_N`，记 `L_t=lcm(g_1,...,g_t)`，则",
        "",
        "```text",
        "mu_t=L_t/L_{t-1}=g_t/gcd(g_t,L_{t-1}),",
        "product_t mu_t=L(A).",
        "```",
        "",
        "若正式频率有高度上界 `|h|<=H`，则 `L(A)<=H`，于是对任意 `Lambda>1`：",
        "",
        "```text",
        "#{t: mu_t>=Lambda} <= floor(log H/log Lambda).",
        "```",
        "",
        "所以当 `N` 远大于该独立乘子预算时，大部分 `g_t` 必须满足",
        "",
        "```text",
        "gcd(g_t,L_{t-1}) > Y/Lambda.",
        "```",
        "",
        "这就是新的窄口：热除数密度若不能产生 LCM 爆炸，就必须产生大共同核复现。",
        "",
        "## 2. 引理表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["lemmas"]:
        lines.append(
            "| `{name}` | {formula} | `{status}` | {meaning} |".format(
                name=table_cell(row["name"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步最窄点",
            "",
            "当前最窄点改为：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "含义：证明大量低乘子共同核复现不能在早期零行反例链中持续存在；若持续存在，必须形成低商 `ColumnCRT/PDEC`；若只孤立出现，则进入 `SAE` 并由容量账本吸收。",
            "",
            "备用同等硬点：",
            "",
            "```text",
            result["secondary_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步闭合的是 LCM 乘子纪律和共同核强迫，不闭合共同核排斥，也不宣称行/列命题无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
