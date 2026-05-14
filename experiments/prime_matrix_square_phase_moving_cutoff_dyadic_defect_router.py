#!/usr/bin/env python3
"""生成 square-phase moving cutoff dyadic 缺陷抽取路由证书。

用法示例：
  python3 experiments/prime_matrix_square_phase_moving_cutoff_dyadic_defect_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.json

输出：
  docs/monograph/prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.json
  docs/monograph/prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-moving-cutoff-dyadic-defect-router.md"

DEFAULT_P_LIST = [10007, 36739, 83561, 200003]
BASE_D = 31

MOVING_DEFECT = "MovingCutoffNegativeSquarePhaseDefectOrTailSievePDEC"
DYADIC_DEFECT = "DyadicNegativeSquarePhaseDeletionExcessPDEC"

SOURCE_FILES = [
    "prime-matrix-square-phase-fixed-lowmod-defect-absorption-router.json",
    "prime-matrix-square-phase-low-skeleton-quadratic-defect-router.json",
    "prime-matrix-square-phase-ldg-mertens-product-margin-router.json",
]


def sieve_bool(limit: int) -> bytearray:
    """返回素数布尔表。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def primes_from_flags(flags: bytearray, limit: int) -> list[int]:
    """提取不超过 limit 的素数。"""
    return [idx for idx in range(2, min(limit + 1, len(flags))) if flags[idx]]


def parse_int_list(text: str) -> list[int]:
    """解析整数列表。"""
    return [int(part) for part in text.split(",") if part.strip()]


def cutoffs_for_p(p: int, base_d: int = BASE_D) -> list[int]:
    """生成 dyadic cutoff。"""
    y = max(2, math.floor(p / math.e))
    cuts = [base_d]
    value = base_d
    while value < y:
        value *= 2
        cuts.append(min(value, y))
    return sorted(set(cuts))


def count_survivors_at_cutoffs(p: int, primes: list[int], cutoffs: list[int]) -> dict[str, Any]:
    """计算各 cutoff 的负平方相位幸存数。"""
    y = cutoffs[-1]
    allowed = bytearray(b"\x01") * p
    allowed[0] = 0
    p2 = p * p
    prime_index = 0
    rows = []
    density = 1.0
    previous_count = p - 1
    previous_density = 1.0
    for cutoff in cutoffs:
        while prime_index < len(primes) and primes[prime_index] <= cutoff:
            q = primes[prime_index]
            residue = (-p2) % q
            start = residue if residue != 0 else q
            if start < p:
                allowed[start:p:q] = b"\x00" * (((p - 1 - start) // q) + 1)
            density *= 1.0 - 1.0 / q
            prime_index += 1
        count = sum(allowed)
        normalized = count / ((p - 1) * density)
        block_ratio = None if not rows else normalized / rows[-1]["normalized"]
        expected_block_ratio = density / previous_density
        actual_block_ratio = count / previous_count if previous_count else 0.0
        deletion_excess = (previous_count * (1.0 - expected_block_ratio)) - (
            previous_count - count
        )
        rows.append(
            {
                "cutoff": cutoff,
                "survivors": count,
                "density": density,
                "normalized": normalized,
                "actual_block_ratio": actual_block_ratio,
                "expected_block_ratio": expected_block_ratio,
                "normalized_block_ratio": block_ratio,
                "deletion_excess_vs_independent": deletion_excess,
            }
        )
        previous_count = count
        previous_density = density
    min_block = min(
        [row for row in rows if row["normalized_block_ratio"] is not None],
        key=lambda row: row["normalized_block_ratio"],
        default=None,
    )
    return {
        "p": p,
        "y": y,
        "cutoff_count": len(cutoffs),
        "final_survivors": rows[-1]["survivors"],
        "final_density": rows[-1]["density"],
        "final_normalized": rows[-1]["normalized"],
        "min_normalized_block_ratio": min_block,
        "rows": rows,
    }


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_moving_cutoff_dyadic_defect_router.py": file_sha256(
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
            "gate": "MovingCutoffTelescopingIdentityClosed",
            "closed": True,
            "proved": True,
            "meaning": "归一化幸存比 R_j=G_{z_j}/((P-1)V(z_j)) 满足 R_J/R_0=prod_j R_{j+1}/R_j。",
            "remaining": "none",
        },
        {
            "gate": "DeficitForcesDyadicBlockDrop",
            "closed": True,
            "proved": True,
            "meaning": "若 fixed 前缀正常而 final 亏损，则某个 dyadic block 的条件删除率超过独立模型平均。",
            "remaining": DYADIC_DEFECT,
        },
        {
            "gate": "DyadicBlockDefectMaterializedAsPDEC",
            "closed": True,
            "proved": False,
            "meaning": "该单块过删是固定端点负平方相位在一个移动素数块中的非零频率/二次字符偏置。",
            "remaining": DYADIC_DEFECT,
        },
        {
            "gate": "DyadicNegativeSquarePhaseDefectExcluded",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明所有移动 dyadic 块都无过删，或排斥其 PDEC 证书。",
            "remaining": DYADIC_DEFECT,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未排除 dyadic LDG defect 与 reciprocal-floor RFP defect。",
            "remaining": "LDG dyadic defect + RFP reciprocal-floor defect",
        },
    ]


def audit(p_list: list[int]) -> dict[str, Any]:
    """执行样本 dyadic profile 审计。"""
    limit = max(max(p_list), 2)
    flags = sieve_bool(limit)
    profiles = []
    for p in p_list:
        y = max(2, math.floor(p / math.e))
        primes = primes_from_flags(flags, y)
        profiles.append(count_survivors_at_cutoffs(p, primes, cutoffs_for_p(p)))
    worst_profile = min(profiles, key=lambda item: item["final_normalized"])
    worst_block_candidates = [
        profile["min_normalized_block_ratio"]
        for profile in profiles
        if profile["min_normalized_block_ratio"] is not None
    ]
    worst_block = min(worst_block_candidates, key=lambda item: item["normalized_block_ratio"])
    return {
        "certificate_type": "prime_matrix_square_phase_moving_cutoff_dyadic_defect_router",
        "status": "moving_cutoff_defect_reduced_to_dyadic_negative_square_phase_deletion_excess_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "moving_cutoff_telescoping_identity_closed": True,
        "deficit_forces_dyadic_block_drop": True,
        "dyadic_block_defect_materialized_as_pdec": True,
        "dyadic_negative_square_phase_defect_excluded": False,
        "row_column_unconditional_closed": False,
        "p_list": p_list,
        "base_d": BASE_D,
        "profiles": profiles,
        "worst_profile_by_final_normalized": worst_profile,
        "worst_normalized_block_ratio": worst_block,
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "next_direct_attack_target": DYADIC_DEFECT,
        "plain_conclusion": (
            "moving cutoff 亏损可由归一化幸存比的 telescoping 精确抽取到某个 dyadic 素数块。"
            "若固定低模前缀已吸收，而最终 `G(P)` 仍低于 Mertens 主项安全余量，"
            "则至少一个移动块 `(z,2z]` 的实际条件删除率超过独立模型，形成"
            "`DyadicNegativeSquarePhaseDeletionExcessPDEC`。该 dyadic 块缺陷尚未排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase moving cutoff dyadic 缺陷路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"moving_cutoff_telescoping_identity_closed={fmt_bool(result['moving_cutoff_telescoping_identity_closed'])}",
        f"deficit_forces_dyadic_block_drop={fmt_bool(result['deficit_forces_dyadic_block_drop'])}",
        f"dyadic_negative_square_phase_defect_excluded={fmt_bool(result['dyadic_negative_square_phase_defect_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 抽取引理",
        "",
        "取 dyadic cutoff `z_0<z_1<...<z_J=floor(P/e)`，定义",
        "",
        "```text",
        "G_j = #{1<=k<P: k != -P^2 mod q for all q<=z_j}",
        "V_j = prod_{q<=z_j}(1-1/q)",
        "R_j = G_j / ((P-1)V_j).",
        "```",
        "",
        "则",
        "",
        "```text",
        "R_J/R_0 = prod_{j=0}^{J-1} R_{j+1}/R_j.",
        "```",
        "",
        "所以若 `R_0` 已由固定低模吸收而 `R_J` 仍异常低，则某个 dyadic block 的 `R_{j+1}/R_j` 异常小；这就是单块条件过删证书。",
        "",
        "## 2. 样本 profile",
        "",
        "| P | y | cutoffs | final survivors | final normalized | worst block cutoff | worst block ratio |",
        "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for profile in result["profiles"]:
        block = profile["min_normalized_block_ratio"]
        lines.append(
            f"| {profile['p']} | {profile['y']} | {profile['cutoff_count']} | "
            f"{profile['final_survivors']} | {profile['final_normalized']:.6f} | "
            f"{block['cutoff'] if block else 'NA'} | "
            f"{block['normalized_block_ratio'] if block else 0:.6f} |"
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
            f"- 直接攻 `{DYADIC_DEFECT}`：对单个移动 dyadic 素数块证明条件删除率不可能持续超过独立模型，或把失败登记为 PDEC。",
            "- 这一步已经把 moving cutoff 的全局亏损压成单块局部相位偏差，不再是整条筛链的模糊亏损。",
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--p-list", default=",".join(str(item) for item in DEFAULT_P_LIST))
    args = parser.parse_args()
    result = audit(parse_int_list(args.p_list))
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "dyadic_negative_square_phase_defect_excluded": result["dyadic_negative_square_phase_defect_excluded"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
