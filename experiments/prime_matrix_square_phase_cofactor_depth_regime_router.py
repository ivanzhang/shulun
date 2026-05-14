#!/usr/bin/env python3
"""生成 dyadic cofactor rough interval 的因子深度分层路由证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_cofactor_depth_regime_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-cofactor-depth-regime-router.json

输出：
  docs/monograph/prime-matrix-square-phase-cofactor-depth-regime-router.json
  docs/monograph/prime-matrix-square-phase-cofactor-depth-regime-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-cofactor-depth-regime-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-cofactor-depth-regime-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

LOW_BUCHSTAB = "LowAlphaBuchstabCofactorLoadBoundOrPDEC"
SEMIPRIME_PDEC = "MiddleAlphaSemiprimeCofactorPairCorrelationPDEC"
PRIME_RFP = "HighAlphaPrimeCofactorRFPOrReciprocalFloorPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-dyadic-first-moment-cofactor-duality.json",
    "prime-matrix-square-phase-rfp-excess-dimension-collapse-router.json",
]


def cutoffs_for_p(p: int, base_d: int = BASE_D) -> list[int]:
    """生成 dyadic cutoff。"""
    y = max(2, math.floor(p / math.e))
    cuts = [base_d]
    value = base_d
    while value < y:
        value *= 2
        cuts.append(min(value, y))
    return sorted(set(cuts))


def factor_depth_bound(p: int, z: int) -> int:
    """计算 z-rough cofactor 的最大素因子个数上界。

    对 q>z，有 m <= (P^2+P-1)/q < (P^2+P)/z。
    若 m 有 t 个素因子且每个 >z，则 m>(z)^t。
    """
    upper = (p * p + p - 1) / z
    if z <= 1:
        return 999
    depth = 0
    power = 1.0
    while power < upper:
        depth += 1
        power *= z + 1
    return max(0, depth - 1)


def regime_for_depth(depth: int) -> str:
    """按最大因子数给出路线名。"""
    if depth <= 1:
        return PRIME_RFP
    if depth <= 2:
        return SEMIPRIME_PDEC
    return LOW_BUCHSTAB


def sample_rows() -> list[dict[str, Any]]:
    """生成样本 dyadic block 深度表。"""
    rows = []
    for p in DEFAULT_P_LIST:
        cutoffs = cutoffs_for_p(p)
        for index, cutoff in enumerate(cutoffs):
            previous = 0 if index == 0 else cutoffs[index - 1]
            if previous < BASE_D:
                continue
            alpha_left = math.log(previous) / math.log(p)
            depth = factor_depth_bound(p, previous)
            rows.append(
                {
                    "p": p,
                    "previous_cutoff": previous,
                    "cutoff": cutoff,
                    "alpha_left": alpha_left,
                    "max_factor_depth": depth,
                    "regime": regime_for_depth(depth),
                }
            )
    return rows


def threshold_rows() -> list[dict[str, Any]]:
    """列出 alpha 阈值含义。"""
    rows = []
    for max_depth in [1, 2, 3, 4, 5]:
        alpha_threshold = 2.0 / (max_depth + 1)
        rows.append(
            {
                "max_depth": max_depth,
                "alpha_threshold": alpha_threshold,
                "statement": f"if z>P^{alpha_threshold:.6f}, then z-rough cofactor has at most {max_depth} prime factors",
            }
        )
    return rows


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_cofactor_depth_regime_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CofactorDepthInequalityClosed",
            "closed": True,
            "proved": True,
            "meaning": "若 q>z 且 m<=P^2/z 为 z-rough，则 m 的素因子数由 z^t<P^2/z 控制。",
            "remaining": "none",
        },
        {
            "gate": "HighAlphaPrimeCofactorRoute",
            "closed": True,
            "proved": True,
            "meaning": "z>P^{2/3} 时 cofactor 必为素数，回到 RFP/reciprocal-floor 素互补因子路线。",
            "remaining": PRIME_RFP,
        },
        {
            "gate": "MiddleAlphaSemiprimeRoute",
            "closed": True,
            "proved": True,
            "meaning": "z>P^{1/2} 时 cofactor 至多半素数，剩余是双素因子 pair-correlation/PDEC。",
            "remaining": SEMIPRIME_PDEC,
        },
        {
            "gate": "LowAlphaBuchstabRoute",
            "closed": True,
            "proved": False,
            "meaning": "z<=P^{1/2} 仍需 Buchstab 多层 cofactor 负载账本或 PDEC。",
            "remaining": LOW_BUCHSTAB,
        },
        {
            "gate": "ShortCofactorLoadBoundClosed",
            "closed": False,
            "proved": False,
            "meaning": "因子深度分层已完成，但各层负载上界尚未排除。",
            "remaining": f"{LOW_BUCHSTAB} OR {SEMIPRIME_PDEC} OR {PRIME_RFP}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未排除所有 cofactor 负载层与 RFP reciprocal-floor 缺陷。",
            "remaining": "cofactor layer bounds + RFP reciprocal-floor exclusion",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造因子深度路由证书。"""
    rows = sample_rows()
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["regime"]] = counts.get(row["regime"], 0) + 1
    return {
        "certificate_type": "prime_matrix_square_phase_cofactor_depth_regime_router",
        "status": "short_cofactor_rough_load_split_by_factor_depth_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "cofactor_depth_inequality_closed": True,
        "high_alpha_prime_cofactor_route_closed": True,
        "middle_alpha_semiprime_route_closed": True,
        "low_alpha_buchstab_route_open": True,
        "short_cofactor_load_bound_closed": False,
        "row_column_unconditional_closed": False,
        "regime_counts_in_samples": counts,
        "threshold_rows": threshold_rows(),
        "sample_rows": rows,
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": LOW_BUCHSTAB,
        "parallel_attack_targets": [SEMIPRIME_PDEC, PRIME_RFP],
        "plain_conclusion": (
            "dyadic cofactor rough 负载已按因子深度分层。"
            "若块左端 `z>P^{2/3}`，互补因子只能是素数，直接并入 RFP/reciprocal-floor 路线；"
            "若 `z>P^{1/2}`，互补因子至多半素数，剩余为 pair-correlation/PDEC；"
            "低于平方根阈值的块才需要真正的多层 Buchstab cofactor 负载上界。"
            "这一步没有排除各层负载，只把一阶负载硬点拆成三个有边界的层。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase cofactor 因子深度分层路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cofactor_depth_inequality_closed={fmt_bool(result['cofactor_depth_inequality_closed'])}",
        f"high_alpha_prime_cofactor_route_closed={fmt_bool(result['high_alpha_prime_cofactor_route_closed'])}",
        f"middle_alpha_semiprime_route_closed={fmt_bool(result['middle_alpha_semiprime_route_closed'])}",
        f"short_cofactor_load_bound_closed={fmt_bool(result['short_cofactor_load_bound_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 深度阈值",
        "",
        "| max depth | alpha threshold | statement |",
        "| ---: | ---: | --- |",
    ]
    for row in result["threshold_rows"]:
        lines.append(f"| {row['max_depth']} | {row['alpha_threshold']:.6f} | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 2. 样本 dyadic 块",
            "",
            "| P | block | alpha(left) | max factor depth | regime |",
            "| ---: | --- | ---: | ---: | --- |",
        ]
    )
    for row in result["sample_rows"]:
        lines.append(
            f"| {row['p']} | `({row['previous_cutoff']},{row['cutoff']}]` | "
            f"{row['alpha_left']:.6f} | {row['max_factor_depth']} | `{row['regime']}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            f"- 主攻 `{LOW_BUCHSTAB}`：低 alpha 块的多层 Buchstab cofactor 负载上界，或失败 PDEC。",
            f"- 并行保留 `{SEMIPRIME_PDEC}` 与 `{PRIME_RFP}`，分别处理中高 alpha 的半素数/素互补因子层。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "parallel_attack_targets": result["parallel_attack_targets"],
                "short_cofactor_load_bound_closed": result["short_cofactor_load_bound_closed"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
