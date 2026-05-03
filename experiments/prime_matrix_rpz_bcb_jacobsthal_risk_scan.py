#!/usr/bin/env python3
"""扫描 RPZ-BCB Jacobsthal 闭合不等式的全局风险。

用法示例：
  python3 experiments/prime_matrix_rpz_bcb_jacobsthal_risk_scan.py

`prime-matrix-rpz-bcb-jacobsthal-closure-interface.md` 将 no-TailAnchor
BCB 分支压成不等式：

  G(h) < P + m - 1 - 2T。

当前 finite 样本取 `m=5,T=4`，且全部满足该不等式。本脚本使用
Ziller--Morack 关于 primorial Jacobsthal 函数的 arXiv 附属数据做风险扫描：
若取 formal 半宽关系的最小顶层素数 `P_min=nextprime(2h)`，检查

  G(h) < P_min - 4。

这里 `G(h)` 是含素数 2 的低筛连续覆盖长度。附属表中的 `omega` 是奇位置
压缩长度；换算为 `G=2*omega+1`。

该脚本用于暴露路线风险，不把外部数据本身写成最终证明。
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from pathlib import Path
from typing import Any


MODULI_URL = "https://arxiv.org/src/1611.03310v2/anc/moduli.txt"


def is_prime(value: int) -> bool:
    """朴素素性测试，足够处理本审计中的小数值。"""
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def next_prime_greater_than(value: int) -> int:
    """返回严格大于 `value` 的最小素数。"""
    candidate = value + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def load_moduli_text(url: str, cache_path: Path | None) -> str:
    """读取 arXiv 附属数据，可选本地缓存。"""
    if cache_path and cache_path.exists():
        return cache_path.read_text(encoding="utf-8")
    with urllib.request.urlopen(url, timeout=30) as response:
        text = response.read().decode("utf-8", errors="replace")
    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(text, encoding="utf-8")
    return text


def parse_rows(text: str, tail_threshold: int, platform_length: int) -> list[dict[str, Any]]:
    """解析 `moduli.txt` 中的 `omega` 行并计算 BCB 余量。"""
    rows = []
    for match in re.finditer(r"n=(\d+), p_n=(\d+), omega\(n\)=(\d+)", text):
        index, h, omega = map(int, match.groups())
        max_covered_run = 2 * omega + 1
        minimal_top_prime = next_prime_greater_than(2 * h)
        minimal_core_length = minimal_top_prime + platform_length - 1 - 2 * tail_threshold
        margin = minimal_core_length - max_covered_run
        required_platform_length = max(
            0,
            max_covered_run - minimal_top_prime + 2 + 2 * tail_threshold,
        )
        rows.append(
            {
                "prime_index": index,
                "h": h,
                "omega_odd_compressed": omega,
                "max_covered_run_G": max_covered_run,
                "minimal_top_prime_gt_2h": minimal_top_prime,
                "platform_length": platform_length,
                "tail_threshold": tail_threshold,
                "minimal_core_length": minimal_core_length,
                "margin_core_minus_G": margin,
                "passes_minimal_linear_test": margin > 0,
                "required_platform_length_for_minimal_top_prime": required_platform_length,
            }
        )
    return rows


def build(url: str, cache_path: Path | None, tail_threshold: int, platform_length: int) -> dict[str, Any]:
    """构造 Jacobsthal 风险扫描账本。"""
    text = load_moduli_text(url, cache_path)
    rows = parse_rows(text, tail_threshold, platform_length)
    failing = [row for row in rows if not row["passes_minimal_linear_test"]]
    first_nontrivial_failure = next(
        (
            row
            for row in failing
            if row["h"] >= 5
        ),
        None,
    )
    return {
        "status": "rpz_bcb_jacobsthal_linear_bound_risk_scan",
        "source": {
            "url": url,
            "paper": "Mario Ziller and John F. Morack, Algorithmic concepts for the computation of Jacobsthal's function, arXiv:1611.03310",
            "cache_path": None if cache_path is None else str(cache_path),
            "data_role": "risk scan only, not final proof",
        },
        "parameters": {
            "tail_threshold": tail_threshold,
            "platform_length": platform_length,
            "tested_condition": "G(h) < nextprime(2h)+m-1-2T",
        },
        "summary": {
            "rows": len(rows),
            "failing_rows": len(failing),
            "first_nontrivial_failure": first_nontrivial_failure,
            "minimum_margin": min((row["margin_core_minus_G"] for row in rows), default=None),
            "maximum_required_platform_length": max(
                (row["required_platform_length_for_minimal_top_prime"] for row in rows),
                default=0,
            ),
        },
        "rows": rows,
        "failing_rows": failing,
        "review_boundary": [
            "当前 finite BCB 样本的 Jacobsthal 长度障碍有效。",
            "若 formal 层只保证 P>2h 且 m=5,T=4，则线性不等式 G(h)<P-4 不能全局成立。",
            "因此全局闭合必须新增更强 formal 参数约束，例如平台长度随 G(h)-P 增长，或转回 TailAnchor/endpoint/first-failure 出口。",
            "该风险扫描使用外部附属数据暴露路线风险；正式论文需独立证明、精确引用或生成可审查证书。",
        ],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 风险审计报告。"""
    summary = result["summary"]
    first_failure = summary["first_nontrivial_failure"]
    lines = [
        "# RPZ-BCB Jacobsthal 线性闭合风险扫描",
        "",
        "**状态：** `rpz_bcb_jacobsthal_linear_bound_risk_scan`",
        "",
        "## 总结",
        "",
        f"- 数据行数：`{summary['rows']}`。",
        f"- 失败行数：`{summary['failing_rows']}`。",
        f"- 最小余量：`{summary['minimum_margin']}`。",
        f"- 最大所需平台长度：`{summary['maximum_required_platform_length']}`。",
        f"- 首个非平凡失败：`{first_failure}`。",
        "",
        "## 关键结论",
        "",
        "当前 finite BCB 样本满足 `G(h)<P+m-1-2T`，但若全局只知道 `P>2h` 且仍取 `m=5,T=4`，则该线性闭合不等式会失败。",
        "",
        "换言之，`G(h)<P-4` 不能作为全局无条件闭合输入。全局证明必须新增至少一项：",
        "",
        "```text",
        "1. formal BCB 平台长度 m 足够大，使 G(h)<P+m-1-2T；",
        "2. formal BCB 参数族只落在有限安全层并给出证书；",
        "3. 失败层进入 TailAnchor / endpoint / first-failure / PDEC / ColumnCRT 出口。",
        "```",
        "",
        "## 失败样本摘录",
        "",
        "| h | G(h) | minimal top P | core length m=5,T=4 | margin | required m |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in result["failing_rows"][:20]:
        lines.append(
            "| {h} | {G} | {P} | {core} | {margin} | {required} |".format(
                h=row["h"],
                G=row["max_covered_run_G"],
                P=row["minimal_top_prime_gt_2h"],
                core=row["minimal_core_length"],
                margin=row["margin_core_minus_G"],
                required=row["required_platform_length_for_minimal_top_prime"],
            )
        )

    lines.extend(
        [
            "",
            "## 审稿边界",
            "",
            "该扫描不是最终外部定理引用，也不是独立证明。它的作用是阻止把当前 finite 样本中的线性 Jacobsthal 余量错误推广为全局闭合。",
            "下一步若继续攻全局闭合，必须转向 `m` 的平台长度增长机制、TailAnchor 强制机制，或为 `G(h)` 给出适配 formal 参数的强上界。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=MODULI_URL)
    parser.add_argument(
        "--cache-path",
        type=Path,
        default=None,
    )
    parser.add_argument("--tail-threshold", type=int, default=4)
    parser.add_argument("--platform-length", type=int, default=5)
    parser.add_argument(
        "--out-prefix",
        type=Path,
        default=Path("docs/monograph/prime-matrix-rpz-bcb-jacobsthal-risk-scan"),
    )
    args = parser.parse_args()

    result = build(args.url, args.cache_path, args.tail_threshold, args.platform_length)
    args.out_prefix.with_suffix(".json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.out_prefix.with_suffix(".md"))
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
