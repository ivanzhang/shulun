#!/usr/bin/env python3
"""审计 z=61 五项 signed-sum 门的主系数剥离。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_signed_sum_dominant_peel_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.md"

NEXT_TARGET = "DominantPeelSignedSumGlobalBoundOrPeelPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-signed-sum-residue-gate-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_signed_sum_dominant_peel_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def sign_word(signs: tuple[int, ...]) -> str:
    """把 ±1 符号向量写成短字。"""
    return "".join("+" if sign > 0 else "-" for sign in signs)


def enumerate_hits(
    coefficients: list[int],
    interval_start: int,
    interval_stop: int,
    modulus: int,
    targets: list[int],
) -> list[dict[str, Any]]:
    """枚举指定 signed-sum 区间同余命中。"""
    hits = []
    target_set = set(targets)
    for signs in product([1, -1], repeat=len(coefficients)):
        value = sum(sign * coefficient for sign, coefficient in zip(signs, coefficients))
        if interval_start <= value < interval_stop and value % modulus in target_set:
            hits.append(
                {
                    "sign_word": sign_word(signs),
                    "signed_sum": value,
                    "sum_mod": value % modulus,
                }
            )
    return hits


def interval_count(coefficients: list[int], interval_start: int, interval_stop: int) -> int:
    """统计只满足区间、不管同余的符号数。"""
    count = 0
    for signs in product([1, -1], repeat=len(coefficients)):
        value = sum(sign * coefficient for sign, coefficient in zip(signs, coefficients))
        if interval_start <= value < interval_stop:
            count += 1
    return count


def peel_branch(
    coefficient: int,
    rest: list[int],
    interval_start: int,
    interval_stop: int,
    modulus: int,
    targets: list[int],
    sign: int,
) -> dict[str, Any]:
    """剥离一个符号分支。"""
    next_start = interval_start - sign * coefficient
    next_stop = interval_stop - sign * coefficient
    next_targets = sorted({(target - sign * coefficient) % modulus for target in targets})
    return {
        "peeled_coefficient": coefficient,
        "peeled_sign": "+" if sign > 0 else "-",
        "rest_coefficients": rest,
        "rest_interval_start": next_start,
        "rest_interval_stop": next_stop,
        "rest_targets_mod": next_targets,
        "rest_abs_sum": sum(abs(value) for value in rest),
        "interval_candidate_count": interval_count(rest, next_start, next_stop),
        "hit_count": len(enumerate_hits(rest, next_start, next_stop, modulus, next_targets)),
        "hits": enumerate_hits(rest, next_start, next_stop, modulus, next_targets),
    }


def dominant_peel_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """执行主系数剥离审计。"""
    rows = []
    for group in source["signed_sum_rows"]:
        coefficients = group["signed_coefficients"]
        modulus = group["q2"] * group["q4"]
        selected = group["selected_residue"]
        carry_layer = next(layer for layer in group["layer_rows"] if layer["carry"] == group["selected_carry"])
        interval_start = carry_layer["interval_start"]
        interval_stop = carry_layer["interval_stop_exclusive"]
        targets = carry_layer["shifted_combined_sum_targets"]

        dominant_index = max(range(len(coefficients)), key=lambda index: abs(coefficients[index]))
        dominant = coefficients[dominant_index]
        rest_after_dominant = [
            coefficient for index, coefficient in enumerate(coefficients) if index != dominant_index
        ]
        dominant_branches = [
            peel_branch(dominant, rest_after_dominant, interval_start, interval_stop, modulus, targets, sign)
            for sign in [1, -1]
        ]
        selected_dominant_branch = next(branch for branch in dominant_branches if branch["hit_count"] == 1)

        # 第二步剥离剩余项中的最大系数 36708。
        second_coefficients = selected_dominant_branch["rest_coefficients"]
        second_index = max(range(len(second_coefficients)), key=lambda index: abs(second_coefficients[index]))
        second = second_coefficients[second_index]
        rest_after_second = [
            coefficient for index, coefficient in enumerate(second_coefficients) if index != second_index
        ]
        second_branches = [
            peel_branch(
                second,
                rest_after_second,
                selected_dominant_branch["rest_interval_start"],
                selected_dominant_branch["rest_interval_stop"],
                modulus,
                selected_dominant_branch["rest_targets_mod"],
                sign,
            )
            for sign in [1, -1]
        ]
        selected_second_branch = next(branch for branch in second_branches if branch["hit_count"] == 1)
        terminal_hits = selected_second_branch["hits"]

        rows.append(
            {
                "modulus": group["modulus"],
                "target_modulus": modulus,
                "selected_residue": selected,
                "source_coefficients": coefficients,
                "source_interval_start": interval_start,
                "source_interval_stop": interval_stop,
                "source_targets_mod": targets,
                "dominant_coefficient": dominant,
                "dominant_branches": dominant_branches,
                "selected_dominant_sign": selected_dominant_branch["peeled_sign"],
                "second_coefficient": second,
                "second_branches": second_branches,
                "selected_second_sign": selected_second_branch["peeled_sign"],
                "terminal_coefficients": selected_second_branch["rest_coefficients"],
                "terminal_interval_start": selected_second_branch["rest_interval_start"],
                "terminal_interval_stop": selected_second_branch["rest_interval_stop"],
                "terminal_targets_mod": selected_second_branch["rest_targets_mod"],
                "terminal_hit_count": len(terminal_hits),
                "terminal_hits": terminal_hits,
                "recovered_full_sign_word": (
                    selected_dominant_branch["peeled_sign"]
                    + selected_second_branch["peeled_sign"]
                    + terminal_hits[0]["sign_word"]
                    if terminal_hits
                    else None
                ),
                "dominant_peel_closed_for_group": (
                    len(terminal_hits) == 1
                    and selected_dominant_branch["peeled_sign"] == "+"
                    and selected_second_branch["peeled_sign"] == "+"
                    and terminal_hits[0]["sign_word"] == "---"
                ),
            }
        )
    return rows


def audit() -> dict[str, Any]:
    """执行主系数剥离审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = dominant_peel_rows(source)
    all_rows_closed = bool(rows) and all(row["dominant_peel_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_signed_sum_dominant_peel_router",
        "status": "z61_five_term_signed_sum_reduced_to_dominant_peel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "dominant_peel_group_count": len(rows),
        "all_dominant_peels_closed": all_rows_closed,
        "dominant_peel_rows": rows,
        "dominant_peel_signed_sum_global_bound_proved": False,
        "peel_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "五项 signed-sum 门可按主系数剥离：先剥离 `382536`，"
            "负号分支被区间直接排除，正号分支把问题降到四项和 "
            "`[-36432,21252)` 与模 `2627` 目标 `[325,1027,1879,2100]`。"
            "再剥离 `36708`，负号分支无同余命中，正号分支降到三项全负 "
            "`---`，和为 `-46189`。合并得到唯一全符号 `++---` 在剥离坐标中，"
            "对应原坐标 `--++-` 与 `r=26951`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 signed-sum dominant peel",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dominant_peel_group_count={result['dominant_peel_group_count']}",
        f"all_dominant_peels_closed={fmt_bool(result['all_dominant_peels_closed'])}",
        f"dominant_peel_signed_sum_global_bound_proved={fmt_bool(result['dominant_peel_signed_sum_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 剥离摘要",
        "",
        "| M | source coefficients | source interval | source targets | dominant | second | terminal coefficients | terminal hits | closed |",
        "| ---: | --- | --- | --- | ---: | ---: | --- | --- | --- |",
    ]
    for row in result["dominant_peel_rows"]:
        lines.append(
            f"| {row['modulus']} | `{row['source_coefficients']}` | "
            f"`[{row['source_interval_start']},{row['source_interval_stop']})` | "
            f"`{row['source_targets_mod']}` | {row['dominant_coefficient']} | "
            f"{row['second_coefficient']} | `{row['terminal_coefficients']}` | "
            f"`{row['terminal_hits']}` | {fmt_bool(row['dominant_peel_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 主系数分支",
            "",
            "| peeled | sign | rest interval | rest targets | interval candidates | hits |",
            "| ---: | --- | --- | --- | ---: | --- |",
        ]
    )
    for row in result["dominant_peel_rows"]:
        for branch in row["dominant_branches"]:
            lines.append(
                f"| {branch['peeled_coefficient']} | `{branch['peeled_sign']}` | "
                f"`[{branch['rest_interval_start']},{branch['rest_interval_stop']})` | "
                f"`{branch['rest_targets_mod']}` | {branch['interval_candidate_count']} | "
                f"`{branch['hits']}` |"
            )
    lines.extend(
        [
            "",
            "## 3. 第二系数分支",
            "",
            "| peeled | sign | rest interval | rest targets | interval candidates | hits |",
            "| ---: | --- | --- | --- | ---: | --- |",
        ]
    )
    for row in result["dominant_peel_rows"]:
        for branch in row["second_branches"]:
            lines.append(
                f"| {branch['peeled_coefficient']} | `{branch['peeled_sign']}` | "
                f"`[{branch['rest_interval_start']},{branch['rest_interval_stop']})` | "
                f"`{branch['rest_targets_mod']}` | {branch['interval_candidate_count']} | "
                f"`{branch['hits']}` |"
            )
    lines.extend(
        [
            "",
            "## 4. 自足小引理",
            "",
            "若 `S=epsilon A+U` 且目标为 `I=[L,H)` 与 `S mod Q in T`，"
            "则固定 `epsilon` 后等价于",
            "",
            "```text",
            "U in [L-epsilon*A, H-epsilon*A),",
            "U mod Q in T-epsilon*A.",
            "```",
            "",
            "因此可逐个剥离主系数，并把不可能分支登记为区间空分支或同余空分支。",
            "",
            "## 5. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的五项 signed-sum 门经两次主系数剥离后只剩三项全负终端命中。",
            "- 未闭合：把这种主系数剥离机制提升为全局 signed-sum 容量界，或排斥 Peel-PDEC。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 6. 依赖哈希",
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "all_dominant_peels_closed": result["all_dominant_peels_closed"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
