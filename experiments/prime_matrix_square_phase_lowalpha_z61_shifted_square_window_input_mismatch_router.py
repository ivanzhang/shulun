#!/usr/bin/env python3
"""审计 z=61 shifted-square-window 所需输入与可用定理形状的匹配缺口。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_input_mismatch_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
BOUNDARY_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json"
SHIFTED_FACTOR_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json"
SQUARE_WINDOW_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-input-mismatch-router.md"

NEXT_TARGET = "NewShiftedSquareWindowCompanionTheoremOrPersistentPhasePDECExclusion"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-dyadic-companion-boundary-router.json",
    "prime-matrix-square-phase-lowalpha-z61-endpoint-shifted-factor-router.json",
    "prime-matrix-square-phase-lowalpha-z61-shifted-square-window-router.json",
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
        "experiments/prime_matrix_square_phase_lowalpha_z61_shifted_square_window_input_mismatch_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        result[f"docs/monograph/{name}"] = file_sha256(DOCS / name)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def audit() -> dict[str, Any]:
    """执行定理形状匹配审查。"""
    boundary = load(BOUNDARY_JSON)
    shifted = load(SHIFTED_FACTOR_JSON)
    square = load(SQUARE_WINDOW_JSON)
    shifted_row = shifted["shifted_factor_rows"][0]
    square_row = square["square_window_rows"][0]

    required_input = {
        "linear_prime_pair": shifted_row["linear_prime_pair_forms"],
        "same_p": square_row["p"],
        "square_congruence": f"p^2 ≡ {-square_row['delta_low']} mod {square_row['base_modulus']}",
        "endpoint_window": "delta + M*span <= p-1 < delta + M*(span+1)",
        "recovered_s": square_row["s_recovered_from_square_window"],
    }

    theorem_shape_tests = [
        {
            "candidate": "single_short_interval_prime",
            "matches_required_shape": False,
            "reason": "只能给某短区间内至少一个素数；不同时给出 `a4=71s-1` 与 `a2=74s-1` 两个素数，也不控制 square-window 同余。",
        },
        {
            "candidate": "dirichlet_one_linear_form",
            "matches_required_shape": False,
            "reason": "只能处理单个等差数列中的无限素数；不提供两个同步线性型同时为素数。",
        },
        {
            "candidate": "bounded_prime_gaps_maynard_type",
            "matches_required_shape": False,
            "reason": "可给某些可容许组中至少两个素数，但不指定必须是这两个线性型，也不附带当前平方窗口锁定。",
        },
        {
            "candidate": "hardy_littlewood_prime_pair_or_dickson_input",
            "matches_required_shape": "formally_close_if_available",
            "reason": "若另行接受足够强的同步线性素数对加 square-window 版本，可闭合该输入；仓库内没有该已证输入。",
        },
    ]
    any_available_match = any(item["matches_required_shape"] is True for item in theorem_shape_tests)

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_shifted_square_window_input_mismatch_router",
        "status": "z61_shifted_square_window_input_not_supplied_by_registered_standard_routes_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            boundary["certificate_type"],
            shifted["certificate_type"],
            square["certificate_type"],
        ],
        "target_bucket": boundary["target_bucket"],
        "target_omega": boundary["target_omega"],
        "target_shell": boundary["target_shell"],
        "required_input": required_input,
        "theorem_shape_tests": theorem_shape_tests,
        "registered_standard_route_matches_required_shape": any_available_match,
        "new_shifted_square_window_companion_theorem_proved": False,
        "persistent_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "当前缺口需要的不是一般短区间素数或单个线性型素数，而是同步移位线性素数对 "
            "`a4=71s-1,a2=74s-1` 与同一个 `p` 的平方窗口同余同时成立。"
            "仓库内登记的标准路线都没有给出这个形状；若不新增该 companion theorem，"
            "就只能转向命名 PersistentPhase-PDEC 排斥。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    req = result["required_input"]
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 shifted-square-window input mismatch",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"registered_standard_route_matches_required_shape={fmt_bool(result['registered_standard_route_matches_required_shape'])}",
        f"new_shifted_square_window_companion_theorem_proved={fmt_bool(result['new_shifted_square_window_companion_theorem_proved'])}",
        f"persistent_phase_pdec_excluded={fmt_bool(result['persistent_phase_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 所需输入形状",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| linear prime pair | `{req['linear_prime_pair']}` |",
        f"| same-p | `{req['same_p']}` |",
        f"| square congruence | `{req['square_congruence']}` |",
        f"| endpoint window | `{req['endpoint_window']}` |",
        f"| recovered s | `{req['recovered_s']}` |",
        "",
        "## 2. 定理形状匹配",
        "",
        "| candidate | matches | reason |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_shape_tests"]:
        lines.append(
            f"| `{item['candidate']}` | `{item['matches_required_shape']}` | {item['reason']} |"
        )
    lines.extend(
        [
            "",
            "## 3. 证明边界",
            "",
            "- 已闭合：所需外部/内部输入的精确形状已经固定。",
            "- 未闭合：新增 shifted-square-window companion theorem，或排斥 PersistentPhase-PDEC。",
            "- 结论：当前没有可直接调用的已登记标准路线完成无条件闭合。",
            f"- 下一目标：`{result['next_direct_attack_target']}`。",
            "",
            "## 4. 依赖哈希",
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
                "registered_standard_route_matches_required_shape": result[
                    "registered_standard_route_matches_required_shape"
                ],
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
