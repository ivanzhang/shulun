#!/usr/bin/env python3
"""审计 z=61 dominant peel 后三项终端符号强制。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_terminal_sign_forcing_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.md
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
SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-terminal-sign-forcing-router.md"

NEXT_TARGET = "TerminalSignForcingGlobalBoundOrTerminalPDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-signed-sum-dominant-peel-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_terminal_sign_forcing_router.py": file_sha256(
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


def enumerate_rows(
    coefficients: list[int],
    interval_start: int,
    interval_stop: int,
    modulus: int,
    targets: list[int],
) -> list[dict[str, Any]]:
    """枚举 signed-sum 行。"""
    target_set = set(targets)
    rows = []
    for signs in product([1, -1], repeat=len(coefficients)):
        value = sum(sign * coefficient for sign, coefficient in zip(signs, coefficients))
        in_interval = interval_start <= value < interval_stop
        target_hit = value % modulus in target_set
        rows.append(
            {
                "sign_word": sign_word(signs),
                "signed_sum": value,
                "sum_mod": value % modulus,
                "in_interval": in_interval,
                "target_hit": target_hit,
                "full_hit": in_interval and target_hit,
            }
        )
    return rows


def branch_after_peel(
    coefficients: list[int],
    interval_start: int,
    interval_stop: int,
    modulus: int,
    targets: list[int],
    sign: int,
) -> dict[str, Any]:
    """固定首项符号后生成分支。"""
    peeled = coefficients[0]
    rest = coefficients[1:]
    next_start = interval_start - sign * peeled
    next_stop = interval_stop - sign * peeled
    next_targets = sorted({(target - sign * peeled) % modulus for target in targets})
    rows = enumerate_rows(rest, next_start, next_stop, modulus, next_targets)
    return {
        "peeled_coefficient": peeled,
        "peeled_sign": "+" if sign > 0 else "-",
        "rest_coefficients": rest,
        "rest_interval_start": next_start,
        "rest_interval_stop": next_stop,
        "rest_targets_mod": next_targets,
        "interval_candidate_count": sum(row["in_interval"] for row in rows),
        "target_candidate_count": sum(row["target_hit"] for row in rows),
        "hit_count": sum(row["full_hit"] for row in rows),
        "rows": rows,
        "hits": [row for row in rows if row["full_hit"]],
    }


def terminal_rows(source: dict[str, Any]) -> list[dict[str, Any]]:
    """执行三项终端符号强制审计。"""
    result_rows = []
    for group in source["dominant_peel_rows"]:
        coefficients = group["terminal_coefficients"]
        modulus = group["target_modulus"]
        interval_start = group["terminal_interval_start"]
        interval_stop = group["terminal_interval_stop"]
        targets = group["terminal_targets_mod"]

        first_branches = [
            branch_after_peel(coefficients, interval_start, interval_stop, modulus, targets, sign)
            for sign in [1, -1]
        ]
        selected_first = next(branch for branch in first_branches if branch["hit_count"] == 1)
        second_branches = [
            branch_after_peel(
                selected_first["rest_coefficients"],
                selected_first["rest_interval_start"],
                selected_first["rest_interval_stop"],
                modulus,
                selected_first["rest_targets_mod"],
                sign,
            )
            for sign in [1, -1]
        ]
        selected_second = next(branch for branch in second_branches if branch["hit_count"] == 1)
        third_rows = selected_second["rows"]
        terminal_hits = selected_second["hits"]
        forced_terminal_word = (
            selected_first["peeled_sign"] + selected_second["peeled_sign"] + terminal_hits[0]["sign_word"]
            if terminal_hits
            else None
        )
        result_rows.append(
            {
                "modulus": group["modulus"],
                "target_modulus": modulus,
                "selected_residue": group["selected_residue"],
                "terminal_coefficients": coefficients,
                "terminal_interval_start": interval_start,
                "terminal_interval_stop": interval_stop,
                "terminal_targets_mod": targets,
                "first_forced_coefficient": coefficients[0],
                "first_branches": first_branches,
                "selected_first_sign": selected_first["peeled_sign"],
                "second_forced_coefficient": coefficients[1],
                "second_branches": second_branches,
                "selected_second_sign": selected_second["peeled_sign"],
                "last_coefficient": coefficients[2],
                "last_rows": third_rows,
                "terminal_hit_count": len(terminal_hits),
                "terminal_hits": terminal_hits,
                "forced_terminal_sign_word": forced_terminal_word,
                "recovered_full_peel_order_sign_word": (
                    group["selected_dominant_sign"]
                    + group["selected_second_sign"]
                    + forced_terminal_word
                    if forced_terminal_word
                    else None
                ),
                "terminal_sign_forcing_closed_for_group": (
                    len(terminal_hits) == 1
                    and selected_first["peeled_sign"] == "-"
                    and selected_second["peeled_sign"] == "-"
                    and terminal_hits[0]["sign_word"] == "-"
                ),
            }
        )
    return result_rows


def audit() -> dict[str, Any]:
    """执行终端符号强制审计。"""
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    rows = terminal_rows(source)
    all_rows_closed = bool(rows) and all(row["terminal_sign_forcing_closed_for_group"] for row in rows)
    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_terminal_sign_forcing_router",
        "status": "z61_dominant_peel_reduced_to_terminal_sign_forcing_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificate": source["certificate_type"],
        "target_bucket": source["target_bucket"],
        "target_omega": source["target_omega"],
        "target_shell": source["target_shell"],
        "terminal_sign_forcing_group_count": len(rows),
        "all_terminal_sign_forcings_closed": all_rows_closed,
        "terminal_rows": rows,
        "terminal_sign_forcing_global_bound_proved": False,
        "terminal_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "dominant peel 后的三项终端门也可完全剥离："
            "`14421` 正号分支有区间候选但无同余命中，负号分支保留；"
            "`19228` 正号分支区间空，负号分支保留；"
            "最后 `12540` 只有负号同时满足区间和同余。"
            "因此当前 formal unit 的终端三项被强制为 `---`，"
            "与上游 `382536,36708` 的正号合成剥离坐标 `++---`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 terminal sign forcing",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"terminal_sign_forcing_group_count={result['terminal_sign_forcing_group_count']}",
        f"all_terminal_sign_forcings_closed={fmt_bool(result['all_terminal_sign_forcings_closed'])}",
        f"terminal_sign_forcing_global_bound_proved={fmt_bool(result['terminal_sign_forcing_global_bound_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端摘要",
        "",
        "| M | coefficients | interval | targets | forced terminal sign | full peel-order sign | closed |",
        "| ---: | --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["terminal_rows"]:
        lines.append(
            f"| {row['modulus']} | `{row['terminal_coefficients']}` | "
            f"`[{row['terminal_interval_start']},{row['terminal_interval_stop']})` | "
            f"`{row['terminal_targets_mod']}` | `{row['forced_terminal_sign_word']}` | "
            f"`{row['recovered_full_peel_order_sign_word']}` | "
            f"{fmt_bool(row['terminal_sign_forcing_closed_for_group'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 剥离 14421",
            "",
            "| sign | rest interval | rest targets | interval candidates | target candidates | hits |",
            "| --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in result["terminal_rows"]:
        for branch in row["first_branches"]:
            lines.append(
                f"| `{branch['peeled_sign']}` | "
                f"`[{branch['rest_interval_start']},{branch['rest_interval_stop']})` | "
                f"`{branch['rest_targets_mod']}` | {branch['interval_candidate_count']} | "
                f"{branch['target_candidate_count']} | `{branch['hits']}` |"
            )
    lines.extend(
        [
            "",
            "## 3. 剥离 19228",
            "",
            "| sign | rest interval | rest targets | interval candidates | target candidates | hits |",
            "| --- | --- | --- | ---: | ---: | --- |",
        ]
    )
    for row in result["terminal_rows"]:
        for branch in row["second_branches"]:
            lines.append(
                f"| `{branch['peeled_sign']}` | "
                f"`[{branch['rest_interval_start']},{branch['rest_interval_stop']})` | "
                f"`{branch['rest_targets_mod']}` | {branch['interval_candidate_count']} | "
                f"{branch['target_candidate_count']} | `{branch['hits']}` |"
            )
    lines.extend(
        [
            "",
            "## 4. 最后一项 12540",
            "",
            "| sign | signed sum | mod 2627 | in interval | target hit | full hit |",
            "| --- | ---: | ---: | --- | --- | --- |",
        ]
    )
    for row in result["terminal_rows"]:
        for last_row in row["last_rows"]:
            lines.append(
                f"| `{last_row['sign_word']}` | {last_row['signed_sum']} | "
                f"{last_row['sum_mod']} | {fmt_bool(last_row['in_interval'])} | "
                f"{fmt_bool(last_row['target_hit'])} | {fmt_bool(last_row['full_hit'])} |"
            )
    lines.extend(
        [
            "",
            "## 5. 自足小引理",
            "",
            "终端三项仍使用同一个剥离恒等式：固定首项符号后，区间和目标同余同时平移。",
            "若某分支没有区间候选，则为 interval-empty；若有区间候选但没有目标命中，"
            "则为 residue-empty。当前终端唯一幸存路径是",
            "",
            "```text",
            "14421 -> -, 19228 -> -, 12540 -> -.",
            "```",
            "",
            "## 6. 证明边界",
            "",
            "- 已闭合：当前 z=61 formal unit 的终端三项符号被区间和同余共同强制为全负。",
            "- 未闭合：全局终端符号强制机制，或 Terminal-PDEC 排斥。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 7. 依赖哈希",
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
                "all_terminal_sign_forcings_closed": result["all_terminal_sign_forcings_closed"],
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
