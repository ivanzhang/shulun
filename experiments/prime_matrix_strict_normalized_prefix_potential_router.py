#!/usr/bin/env python3
"""生成 strict 归一化 prefix 残洞势路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_normalized_prefix_potential_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-normalized-prefix-potential-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-normalized-prefix-potential-router.md"

HARDPOINT = "NormalizedPrefixResidualPotentialLowerBound"
ROUGH_COUNT = "UniformPrefixRoughCountLowerBound"
THRESHOLD = "FormalUnitTypeThresholdLedger"
FINITE_CHECK = "FiniteSmallPBoundaryPrefixCertificate"
ANTICOLLAPSE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json",
    MONOGRAPH / "prime-matrix-cylindrical-completion-line-barrier.md",
    MONOGRAPH / "prime-matrix-eda-dls13-buchstab-barrier.md",
    MONOGRAPH / "prime-matrix-eda-alpha-main-gap-constant-package.md",
    MONOGRAPH / "prime-matrix-b3-meissel-mertens-interval-external-router.md",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def potential_reductions() -> list[dict[str, str]]:
    """列出 M# 势下界的确定压缩。"""
    return [
        {
            "reduction": "multiplier_to_rough_count",
            "formula": "M#_{x,z} >= |R_{x,z}| / ceil(P/z).",
            "status": "closed",
        },
        {
            "reduction": "classical_sieve_window",
            "formula": "For z<=P^(1/2-eps), a lower-bound sieve would give |R_{x,z}| >= c_eps P/log z after finite constants.",
            "status": "external_or_internal_input_open",
        },
        {
            "reduction": "normalized_growth",
            "formula": "Combining the two gives M#_{x,z} >= c_eps z/log z.",
            "status": "conditional_on_rough_count",
        },
        {
            "reduction": "type_threshold_comparison",
            "formula": "Need c_eps z/log z > T_formal(P,z) on the same row-free type alphabet.",
            "status": "open",
        },
        {
            "reduction": "finite_small_p",
            "formula": "Explicit constants leave a finite P range that must be certified separately.",
            "status": "open",
        },
    ]


def build_rows(capacity_router: dict[str, Any]) -> list[dict[str, Any]]:
    """生成归一化 prefix 势判定表。"""
    return [
        {
            "gate": "NormalizedPotentialInputActive",
            "closed": capacity_router.get("next_direct_attack_target") == HARDPOINT,
            "proved": False,
            "meaning": "上一层已把容量乘子纪律后的直接硬点定为 M# 归一化势下界。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍只在早期零行假设下研究 prefix 残洞势，不使用真实缺席数据。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "MultiplierToRoughCountReductionClosed",
            "closed": True,
            "proved": True,
            "meaning": "由 mu_q<=ceil(P/z) 得 M#>=|R_{x,z}|/ceil(P/z)，把归一化势压到 prefix 粗筛余数量。",
            "remaining": "需要 |R_{x,z}| 下界。",
        },
        {
            "gate": "NoncircularCutoffWindowIdentified",
            "closed": True,
            "proved": True,
            "meaning": "若取 z<=P^(1/2-eps)，筛的 level 可保持在窗口长度 P 内，避免自然 cutoff x~P 的短素数屏障。",
            "remaining": "需要显式低界筛常数或内部化证明。",
        },
        {
            "gate": "UniformPrefixRoughCountCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未逐行证明 |R_{x,z}|>=c P/log z；这可作为经典低界筛外部输入或内部化目标。",
            "remaining": ROUGH_COUNT,
        },
        {
            "gate": "FormalUnitTypeThresholdLedgerCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未给出同一 row-free type alphabet 的阈值 T_formal(P,z)，所以还不能比较 M# 与类型数。",
            "remaining": THRESHOLD,
        },
        {
            "gate": "FiniteSmallPBoundaryPrefixCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "即使采用显式筛常数，也会留下有限小 P 段；该证书尚未物化。",
            "remaining": FINITE_CHECK,
        },
        {
            "gate": "NormalizedPrefixPotentialCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "M# 势的内部公式已闭合，但全局下界、阈值比较和有限段证书仍未完成。",
            "remaining": f"{ROUGH_COUNT} AND {THRESHOLD} AND {FINITE_CHECK}",
        },
        {
            "gate": "StillNeedsAntiCollapseAfterPotential",
            "closed": False,
            "proved": False,
            "meaning": "即便 M# 足够大，仍需证明不同标签支撑不在 row-free type/quotient 中塌缩。",
            "remaining": ANTICOLLAPSE,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造归一化 prefix 残洞势证书。"""
    capacity_router = load_json(MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json")
    return {
        "certificate_type": "prime_matrix_strict_normalized_prefix_potential_router",
        "status": "normalized_prefix_potential_reduced_to_rough_count_type_threshold_finite_check_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "multiplier_to_rough_count_reduction_closed": True,
        "noncircular_prefix_cutoff_window_identified": True,
        "uniform_prefix_rough_count_lower_bound_proved": False,
        "formal_unit_type_threshold_ledger_proved": False,
        "finite_small_p_boundary_prefix_certificate_proved": False,
        "normalized_prefix_residual_potential_lower_bound_proved": False,
        "prefix_label_support_to_row_free_type_anticollapse_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{ROUGH_COUNT} AND {THRESHOLD} AND {FINITE_CHECK}",
        "next_direct_attack_target": ROUGH_COUNT,
        "parallel_attack_targets": [THRESHOLD, FINITE_CHECK, ANTICOLLAPSE],
        "potential_reductions": potential_reductions(),
        "rows": build_rows(capacity_router),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`NormalizedPrefixResidualPotentialLowerBound` 已被压成确定的筛余问题："
            "容量纪律给出 M#_{x,z}>=|R_{x,z}|/ceil(P/z)。"
            "因此只要在某个非循环 prefix 窗口 z<=P^(1/2-eps) 证明统一粗筛余下界 "
            "|R_{x,z}|>=c P/log z，就得到 M#>=c z/log z。"
            "剩余是三件事：证明或引用显式低界筛、给出 formal-unit 类型阈值账本、"
            "并补有限小 P 证书；之后仍要做标签到类型的抗塌缩。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 归一化 prefix 残洞势路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"multiplier_to_rough_count_reduction_closed={fmt_bool(result['multiplier_to_rough_count_reduction_closed'])}",
        f"noncircular_prefix_cutoff_window_identified={fmt_bool(result['noncircular_prefix_cutoff_window_identified'])}",
        f"uniform_prefix_rough_count_lower_bound_proved={fmt_bool(result['uniform_prefix_rough_count_lower_bound_proved'])}",
        f"formal_unit_type_threshold_ledger_proved={fmt_bool(result['formal_unit_type_threshold_ledger_proved'])}",
        f"finite_small_p_boundary_prefix_certificate_proved={fmt_bool(result['finite_small_p_boundary_prefix_certificate_proved'])}",
        f"normalized_prefix_residual_potential_lower_bound_proved={fmt_bool(result['normalized_prefix_residual_potential_lower_bound_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 势下界公式",
        "",
        "容量纪律已给出",
        "",
        "```text",
        "M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)},",
        "mu_{tau_z(c)}<=ceil(P/z),",
        "so M#_{x,z}>=|R_{x,z}|/ceil(P/z).",
        "```",
        "",
        "若能在 `z<=P^(1/2-eps)` 上用低界筛证明 `|R_{x,z}|>=c_eps P/log z`，则得到",
        "",
        "```text",
        "M#_{x,z}>=c_eps z/log z.",
        "```",
        "",
        "这条路径绕开了自然 cutoff `z=x` 的短素数屏障，但引入了显式筛常数、类型阈值和有限段证书。",
        "",
        "## 2. 压缩表",
        "",
        "| reduction | formula | status |",
        "| --- | --- | --- |",
    ]
    for row in result["potential_reductions"]:
        lines.append(
            "| `{reduction}` | {formula} | `{status}` |".format(
                reduction=table_cell(row["reduction"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
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
    for row in result["rows"]:
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步只把 M# 势压成显式筛余下界与阈值比较；尚未提供低界筛证明或有限段证书。",
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
