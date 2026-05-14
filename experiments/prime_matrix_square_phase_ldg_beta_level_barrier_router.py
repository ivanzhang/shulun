#!/usr/bin/env python3
"""生成 square-phase LDG 的 beta-sieve 层级障碍证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_ldg_beta_level_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-ldg-beta-level-barrier-router.json

输出：
  docs/monograph/prime-matrix-square-phase-ldg-beta-level-barrier-router.json
  docs/monograph/prime-matrix-square-phase-ldg-beta-level-barrier-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-ldg-beta-level-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-ldg-beta-level-barrier-router.md"

LDG = "LDG-Lower"
OLD_BETA = "SquarePhaseBetaSieveRemainderBound"
NEAR_FULL = "PostSquareNearFullRoughSkeletonLowerBound"
LOW_DEFECT = "LowSkeletonDeficitPDECOrSAE"
RFP = "RFP-Upper"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"

SOURCE_FILES = [
    "prime-matrix-square-phase-ldg-lower-direct-attack-router.json",
    "prime-matrix-square-phase-dimension-gap-attack-router.json",
    "prime-matrix-beta-sieve-lower-bound-dominance-router.json",
    "prime-matrix-b3-continuous-beta-sieve-surplus-router.json",
    "prime-matrix-linear-sieve-tail-remainder-gap-router.md",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_ldg_beta_level_barrier_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def sample_rows() -> list[dict[str, Any]]:
    """给出 LDG 阈值下的 level 读数。"""
    samples = [2003, 10007, 100000, 1000000]
    rows = []
    for p in samples:
        z = p / math.e
        s_at_d_equals_p = math.log(p) / math.log(z)
        d_for_s2 = z * z
        rows.append(
            {
                "p": p,
                "z_approx": z,
                "s_at_D_equals_P": s_at_d_equals_p,
                "linear_lower_positive": s_at_d_equals_p > 2.0,
                "D_needed_for_s_gt_2": d_for_s2,
                "D_needed_over_P": d_for_s2 / p,
            }
        )
    return rows


def barrier_rows() -> list[dict[str, str]]:
    """列出 beta-sieve 适配障碍。"""
    return [
        {
            "name": "alpha043_package_mismatch",
            "statement": "已有 beta-sieve 包使用 z=P^0.43, D=P, s=2.325...；LDG 使用 z=P/e。",
            "effect": "不能把旧 0.43 粗骨架下界直接导入 LDG。",
        },
        {
            "name": "linear_sieve_zero_region",
            "statement": "一维线性下筛的正主系数需要 s=logD/logz>2；s<=2 时 lower function 为 0。",
            "effect": "取 D=P、z=P/e 时 s->1，标准下筛不给正下界。",
        },
        {
            "name": "required_level_too_high",
            "statement": "若 z=P/e，要使 s>2 至少需要 D>z^2≈P^2/e^2。",
            "effect": "这远超过长度 P 的平凡分布层级，绝对 floor 余项会吞掉主项。",
        },
        {
            "name": "cutoff_relaxation_breaks_tail_identity",
            "statement": "把 z 降到 P^0.43 可恢复 beta-sieve，但多尾结构回来，三曲线素对 B(P) 不再是同一对象。",
            "effect": "会离开当前 square-phase 维数差路线，必须转入非 final-tail 预算/PDEC 体系。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "LDGBetaTargetImported",
            True,
            True,
            "上一层把 LDG 暂压成 beta-sieve 余项；本步检查该适配是否合法。",
            OLD_BETA,
        ),
        row(
            "Alpha043BetaPackageApplicableToLDG",
            False,
            False,
            "LDG 的筛阈值是 P/e，不是 P^0.43；旧 beta 包参数不匹配。",
            NEAR_FULL,
        ),
        row(
            "StandardLinearLowerSievePositiveAtDEqualsP",
            False,
            False,
            "D=P、z=P/e 给 s≈1<2，线性下筛主系数为零。",
            "need D>z^2 or new structure",
        ),
        row(
            "RequiredLevelCompatibleWithLengthP",
            False,
            False,
            "D>z^2≈P^2/e^2 远超长度 P 的可控 floor 余项层级。",
            NEAR_FULL,
        ),
        row(
            "SquarePhaseBetaSieveRemainderBoundReplaced",
            True,
            False,
            "旧目标应替换为近全阈值粗骨架下界，或失败进入低骨架 PDEC。",
            f"{NEAR_FULL} OR {LOW_DEFECT}",
        ),
        row(
            "LDGLowerCurrentCorpusProved",
            False,
            False,
            "LDG 仍未闭合；当前最窄点比 beta 余项更强，是 P/e 阈值的短区间 rough 下界。",
            f"{NEAR_FULL} OR {LOW_DEFECT}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "没有得到全局无条件终端矛盾。",
            f"({LDG} AND {RFP}) OR {NONFINAL}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 LDG beta 层级障碍证书。"""
    return {
        "certificate_type": "prime_matrix_square_phase_ldg_beta_level_barrier_router",
        "status": "ldg_beta_sieve_level_barrier_identified_near_full_rough_lower_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "ldg_beta_target_imported": True,
        "alpha043_beta_package_applicable_to_ldg": False,
        "standard_linear_lower_sieve_positive_at_d_equals_p": False,
        "required_level_compatible_with_length_p": False,
        "square_phase_beta_sieve_remainder_bound_replaced": True,
        "ldg_lower_current_corpus_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": OLD_BETA,
        "hardpoint_after_router": f"{NEAR_FULL} OR {LOW_DEFECT}",
        "next_direct_attack_target": NEAR_FULL,
        "parallel_attack_targets": [LOW_DEFECT, RFP, NONFINAL],
        "level_sample_rows": sample_rows(),
        "barrier_rows": barrier_rows(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`SquarePhaseBetaSieveRemainderBound` 不能按旧 alpha=0.43 beta-sieve 包直接关闭 LDG。"
            "LDG 的低筛阈值是 `z=P/e`；若分布层级只到 `D=P`，则 "
            "`s=logD/logz` 接近 `1`，处在线性下筛正主系数为零的区域。"
            "要让标准下筛产生正主项需 `D>z^2≈P^2/e^2`，这远超长度 `P` 的可控层级。"
            "因此真正剩余应改写为 `PostSquareNearFullRoughSkeletonLowerBound`，"
            "或证明 `G(P)<0.48P/logP` 会产生 `LowSkeletonDeficit/PDEC`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase LDG beta-sieve 层级障碍路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"alpha043_beta_package_applicable_to_ldg={fmt_bool(result['alpha043_beta_package_applicable_to_ldg'])}",
        f"standard_linear_lower_sieve_positive_at_d_equals_p={fmt_bool(result['standard_linear_lower_sieve_positive_at_d_equals_p'])}",
        f"required_level_compatible_with_length_p={fmt_bool(result['required_level_compatible_with_length_p'])}",
        f"square_phase_beta_sieve_remainder_bound_replaced={fmt_bool(result['square_phase_beta_sieve_remainder_bound_replaced'])}",
        f"ldg_lower_current_corpus_proved={fmt_bool(result['ldg_lower_current_corpus_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 层级读数",
        "",
        "| P | z=P/e | s at D=P | positive lower f(s) | D needed for s>2 | D/P |",
        "| ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in result["level_sample_rows"]:
        lines.append(
            f"| {item['p']} | {item['z_approx']:.3f} | {item['s_at_D_equals_P']:.6f} | "
            f"`{fmt_bool(item['linear_lower_positive'])}` | {item['D_needed_for_s_gt_2']:.3f} | "
            f"{item['D_needed_over_P']:.3f} |"
        )
    lines.extend(
        [
            "",
            "## 2. 障碍",
            "",
            "| name | statement | effect |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["barrier_rows"]:
        lines.append(
            f"| `{item['name']}` | {table_cell(item['statement'])} | {table_cell(item['effect'])} |"
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
            f"- 主攻 `{NEAR_FULL}`：直接证明 `z=P/e` 的平方端点低筛骨架下界。",
            f"- 若该近全阈值下界失败，必须抽取 `{LOW_DEFECT}`，不能回到有限 CRT 矛盾。",
            f"- 若改用 `P^0.43` 阈值，则必须离开三曲线维数差，回到 `{NONFINAL}`。",
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
                "ldg_lower_current_corpus_proved": result["ldg_lower_current_corpus_proved"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
