#!/usr/bin/env python3
"""生成 strict 低乘子共同核分流路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_low_multiplier_common_kernel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-low-multiplier-common-kernel-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-low-multiplier-common-kernel-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-short-window-divisor-density-lcm-router.md",
    MONOGRAPH / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.md",
    MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md",
    MONOGRAPH / "h4-pdec-column-defect-routing-contract.md",
    MONOGRAPH / "h4-pdec-admissible-constraint-table.md",
]

LOW_MULTIPLIER = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
PAIR_KERNEL = "LargePairKernelDifferenceColumnCRTExclusion"
FANIN_KERNEL = "MultiSourceKernelFanInSAEOrPDECExclusion"
LOW_QUOTIENT = "LowQuotientColumnCRTOrPDECRoute"
HOT_DENSITY = "HotFrequencyDivisorDensityPDECorSAE"
LCM_DISCIPLINE = "ShortWindowLCMMultiplierDisciplineForFrequencyH"


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
    """列出共同核分流引理。"""
    return [
        {
            "name": "low_multiplier_kernel_materialization",
            "formula": "mu_t<Lambda implies K_t=gcd(g_t,L_{t-1})>Y/Lambda.",
            "status": "imported_closed",
            "meaning": "由 LCM 乘子纪律继承大共同核。",
        },
        {
            "name": "kernel_subcover",
            "formula": "K_t divides lcm_{i<t} gcd(g_t,g_i).",
            "status": "closed",
            "meaning": "新除数与旧 LCM 的共同核完全由它和旧除数的成对共同核覆盖。",
        },
        {
            "name": "pair_or_fanin_dichotomy",
            "formula": "A large K_t gives either a large pair gcd or a multi-source kernel fan-in cover.",
            "status": "closed_dichotomy",
            "meaning": "低乘子复现被拆成单对大核与多源扇入两类，不再是无名异常。",
        },
        {
            "name": "large_pair_difference_lock",
            "formula": "If k|g_t and k|g_i with Y<g_i,g_t<=2Y, then k|(g_t-g_i) and 0<|g_t-g_i|<Y.",
            "status": "closed",
            "meaning": "单对大共同核会把短窗口差值锁到小商倍数。",
        },
        {
            "name": "large_pair_to_low_quotient_columncrt",
            "formula": "A persistent large-pair kernel with |g_t-g_i|=k a and |a|<Y/k enters LowQuotient ColumnCRT/PDEC.",
            "status": "registered_route_open",
            "meaning": "若这种差值锁反复出现，它就是低商相位集中证书。",
        },
        {
            "name": "fanin_to_sae_or_pdec",
            "formula": "If K_t needs many previous divisors to cover, the minimal cover hypergraph is SAE unless it persists as PDEC.",
            "status": "registered_route_open",
            "meaning": "多源扇入是可登记的结构异常，但排斥仍待证明。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的热除数窗口分支内。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "LowMultiplierKernelImported",
            "closed": True,
            "proved": True,
            "meaning": "从 LCM 乘子纪律导入 K_t>Y/Lambda。",
            "remaining": LOW_MULTIPLIER,
        },
        {
            "gate": "KernelSubcoverClosed",
            "closed": True,
            "proved": True,
            "meaning": "大共同核必须由成对 gcd 云覆盖。",
            "remaining": "无。",
        },
        {
            "gate": "PairOrFanInDichotomyClosed",
            "closed": True,
            "proved": True,
            "meaning": "共同核出口已拆成大成对差值锁与多源扇入两类。",
            "remaining": f"{PAIR_KERNEL} OR {FANIN_KERNEL}",
        },
        {
            "gate": "LargePairDifferenceLockClosed",
            "closed": True,
            "proved": True,
            "meaning": "大成对共同核强制差值为共同核的小商倍数。",
            "remaining": LOW_QUOTIENT,
        },
        {
            "gate": "LargePairColumnCRTExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明持久差值锁不可能，或其 PDEC/ColumnCRT 证书必被排斥。",
            "remaining": PAIR_KERNEL,
        },
        {
            "gate": "FanInSAEOrPDECExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明多源共同核扇入可全局求和吸收，或持久时被 PDEC 排斥。",
            "remaining": FANIN_KERNEL,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_low_multiplier_common_kernel_router",
        "status": "low_multiplier_common_kernel_split_to_pair_difference_lock_or_fanin_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "low_multiplier_kernel_imported": True,
        "kernel_subcover_closed": True,
        "pair_or_fanin_dichotomy_closed": True,
        "large_pair_difference_lock_closed": True,
        "large_pair_columncrt_route_registered": True,
        "fanin_sae_pdec_route_registered": True,
        "large_pair_columncrt_excluded": False,
        "fanin_sae_or_pdec_excluded": False,
        "low_multiplier_common_kernel_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": PAIR_KERNEL,
        "secondary_attack_target": FANIN_KERNEL,
        "parallel_targets": [LOW_QUOTIENT, HOT_DENSITY, LCM_DISCIPLINE],
        "lemmas": lemmas(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "低乘子共同核已经拆成两个不可再混淆的出口。若新增除数 g_t 的乘子 "
            "mu_t<Lambda，则 K_t=gcd(g_t,L_{t-1})>Y/Lambda。由于 L_{t-1} "
            "由旧除数生成，K_t 必被成对共同核 gcd(g_t,g_i) 的 LCM 覆盖。"
            "于是只有两种结构：某个旧除数与 g_t 有大成对共同核，进而锁定短差值 "
            "g_t-g_i=k a；或没有单一大核，只能由多个旧除数分摊覆盖，形成多源 kernel fan-in。"
            "前者应进入低商 ColumnCRT/PDEC，后者进入 SAE/PDEC 容量账本。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 低乘子共同核分流路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"low_multiplier_kernel_imported={fmt_bool(result['low_multiplier_kernel_imported'])}",
        f"kernel_subcover_closed={fmt_bool(result['kernel_subcover_closed'])}",
        f"pair_or_fanin_dichotomy_closed={fmt_bool(result['pair_or_fanin_dichotomy_closed'])}",
        f"large_pair_difference_lock_closed={fmt_bool(result['large_pair_difference_lock_closed'])}",
        f"large_pair_columncrt_route_registered={fmt_bool(result['large_pair_columncrt_route_registered'])}",
        f"fanin_sae_pdec_route_registered={fmt_bool(result['fanin_sae_pdec_route_registered'])}",
        f"large_pair_columncrt_excluded={fmt_bool(result['large_pair_columncrt_excluded'])}",
        f"fanin_sae_or_pdec_excluded={fmt_bool(result['fanin_sae_or_pdec_excluded'])}",
        f"low_multiplier_common_kernel_excluded={fmt_bool(result['low_multiplier_common_kernel_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 成对核覆盖",
        "",
        "从上一层导入低乘子事件：",
        "",
        "```text",
        "K_t=gcd(g_t,L_{t-1}) > Y/Lambda.",
        "```",
        "",
        "因为 `L_{t-1}=lcm(g_1,...,g_{t-1})`，所以 `K_t` 的每个素幂都来自某个旧 `g_i`，即",
        "",
        "```text",
        "K_t | lcm_{i<t} gcd(g_t,g_i).",
        "```",
        "",
        "于是大共同核不是模糊对象：它要么集中在某个成对 gcd 上，要么由多个旧除数分摊覆盖。",
        "",
        "## 2. 差值锁",
        "",
        "若存在 `k=gcd(g_t,g_i)` 足够大，则因二者都在 `(Y,2Y]` 内，",
        "",
        "```text",
        "k | (g_t-g_i),  0<|g_t-g_i|<Y.",
        "```",
        "",
        "所以",
        "",
        "```text",
        "g_t-g_i=k a,  0<|a|<Y/k.",
        "```",
        "",
        "当 `k` 大时，商 `a` 很小；若这种锁定持久出现，就不是随机除数密度，而是低商列相位集中，应送入 `ColumnCRT/PDEC`。",
        "",
        "## 3. 引理表",
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
            "## 4. 判定表",
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
            "## 5. 下一步最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "备用并列硬点：",
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
            "审稿边界：本步只证明共同核可分流为成对差值锁或多源扇入；尚未排斥这两个出口。",
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
