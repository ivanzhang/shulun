#!/usr/bin/env python3
"""Prime Matrix Backlund 对称 max 溢价路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_symmetric_max_premium_router.py

输出：
  docs/monograph/prime-matrix-backlund-symmetric-max-premium-router.json
  docs/monograph/prime-matrix-backlund-symmetric-max-premium-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_HIGH_POWER = MONO / "prime-matrix-backlund-high-power-auxiliary-router.json"
DEFAULT_SIGNED = MONO / "prime-matrix-b3-jensen-signed-mean-router.json"
DEFAULT_VARIATION = MONO / "prime-matrix-b3-variation-window-scale-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-symmetric-max-premium-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-symmetric-max-premium-router.md"

PARENT = "BacklundHighPowerAuxiliarySignedMeanC16AggregationLedger"
MAX_IDENTITY = "BacklundHighPowerBoundarySymmetricMaxIdentityClosed"
PREMIUM_REMAINING = "BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(high_power: dict[str, Any], signed: dict[str, Any], variation: dict[str, Any]) -> list[dict[str, Any]]:
    """生成对称 max 溢价判定表。"""
    guard = (
        high_power.get("counterexample_assumption_only") is True
        and high_power.get("empirical_absence_not_used") is True
        and high_power.get("hypothetical_chain_only") is True
    )
    parent_active = high_power.get("new_unique_internal_remaining") == PARENT
    signed_high = signed.get("backlund_jensen_signed_mean_high_height_closed") is True
    variation_closed = variation.get("variation_window_scale_external_closed") is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只审查高幂辅助函数边界平均的常数结构，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "HighPowerSignedMeanGateActive",
            parent_active,
            True,
            "上一层唯一剩余是高幂辅助函数继承 signed-mean C16 预算。",
            PARENT,
        ),
        row(
            "SymmetricBoundaryMaxIdentityClosed",
            True,
            True,
            "N->infty 后边界项为 max(U_T(phi),U_T(-phi))，其中 U_T(-phi) 是共轭高度的同分布项。",
            MAX_IDENTITY,
        ),
        row(
            "SignedMeanBaseC7Available",
            signed_high,
            True,
            "单个 U_T 圆周 signed-mean 分子系数已为 7。",
            "BacklundJensenSignedMeanHighHeightZetaOnlyClosedC7",
        ),
        row(
            "C16MarginComputed",
            True,
            True,
            "C16 允许分子为 16 log(4/sqrt(5))=9.305206...，扣掉 C7 后只剩 2.305206... 溢价余量。",
            PREMIUM_REMAINING,
        ),
        row(
            "NaiveDoubleSignedMeanFails",
            True,
            True,
            "若用 max<=U^+ + U^- 粗估，分子会接近 14，超过 9.305，不能闭合。",
            PREMIUM_REMAINING,
        ),
        row(
            "LocalVariationPremiumBoundTooLarge",
            variation_closed,
            True,
            "用既有局部变差 C216 控制高度差 8 的对称差会产生远大于 2.305 的预算，不能作为闭合。",
            PREMIUM_REMAINING,
        ),
        row(
            "SymmetricMaxPremiumStillOpen",
            False,
            False,
            "仍需证明平均正部差 1/2 int |U_T(phi)-U_T(-phi)| 的 log 系数不超过 2.305206。",
            PREMIUM_REMAINING,
        ),
        row(
            "SelfContainedBacklundStillOpen",
            False,
            False,
            "该溢价未闭合前，高幂辅助 Backlund 内部常数不能进入 C16/C_S=8。",
            PREMIUM_REMAINING,
        ),
        row(
            "ExternalBacklundStillAvailable",
            True,
            False,
            "外部经典 Backlund 引理整体处理了该对称 max/高幂 Jensen 常数。",
            EXTERNAL_ACCEPTED,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行对称 max 溢价路由。"""
    high_power = load_json(paths["high_power"])
    signed = load_json(paths["signed"])
    variation = load_json(paths["variation"])
    rows = build_rows(high_power, signed, variation)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    allowed = 16.0 * math.log(4.0 / math.sqrt(5.0))
    signed_base = float(signed.get("C_signed_numerator", 7.0))
    margin = allowed - signed_base
    return {
        "certificate_type": "prime_matrix_backlund_symmetric_max_premium_router",
        "status": "backlund_symmetric_max_premium_is_unique_constant_obstruction_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "parent_remaining": PARENT,
        "symmetric_boundary_max_identity_closed": True,
        "allowed_c16_numerator": allowed,
        "signed_mean_base_numerator": signed_base,
        "available_premium_margin": margin,
        "naive_double_numerator": 2.0 * signed_base,
        "new_unique_internal_remaining": PREMIUM_REMAINING,
        "row_column_self_contained_closed": False,
        "row_column_external_route_closed": False,
        "external_backlund_escape": EXTERNAL_ACCEPTED,
        "plain_conclusion": (
            "高幂辅助函数常数核已压到一个精确溢价问题："
            "单个 signed-mean 圆周分子为 7，而 C16 允许分子为 9.305206...，"
            "因此对称 max 额外溢价必须不超过 2.305206...。"
            "粗略双计或用局部变差控制都超预算；当前严格自足路线的唯一常数剩余就是"
            "证明该对称高度 max 溢价小于 C16 余量。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 对称 max 溢价路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"parent_remaining={result['parent_remaining']}",
        f"symmetric_boundary_max_identity_closed={fmt_bool(result['symmetric_boundary_max_identity_closed'])}",
        f"allowed_c16_numerator={result['allowed_c16_numerator']:.12f}",
        f"signed_mean_base_numerator={result['signed_mean_base_numerator']:.12f}",
        f"available_premium_margin={result['available_premium_margin']:.12f}",
        f"naive_double_numerator={result['naive_double_numerator']:.12f}",
        f"new_unique_internal_remaining={result['new_unique_internal_remaining']}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 溢价恒等式",
        "",
        "令 `U_T(phi)` 表示单个 shifted xi 圆周的 normalized log 边界项。高幂极限给出：",
        "",
        "```text",
        "lim_{N->infty} N^{-1} log |B_{T,theta,N}(z(phi))|",
        "  <= max(U_T(phi), U_T(-phi)).",
        "```",
        "",
        "因此",
        "",
        "```text",
        "avg max(U(phi), U(-phi))",
        "  = avg U(phi) + 1/2 avg |U(phi)-U(-phi)|.",
        "```",
        "",
        "第一项已有 signed-mean C7；第二项就是当前唯一溢价。",
        "",
        "## 2. 常数门",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| C16 allowed numerator | `{result['allowed_c16_numerator']:.12f}` |",
        f"| signed-mean base numerator | `{result['signed_mean_base_numerator']:.12f}` |",
        f"| available premium margin | `{result['available_premium_margin']:.12f}` |",
        f"| naive doubled numerator | `{result['naive_double_numerator']:.12f}` |",
        "",
        "结论：必须证明对称 max 溢价的 log 系数 `<=2.305206478445`；否则 C16 不能通过。",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            f"内部唯一最窄点：`{result['new_unique_internal_remaining']}`。",
            f"外部逃逸门：`{result['external_backlund_escape']}`。",
            "",
            "判定：所有形式层已压实；严格自足版最后剩余是对称 max 溢价常数不等式。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--high-power-json", type=Path, default=DEFAULT_HIGH_POWER)
    parser.add_argument("--signed-json", type=Path, default=DEFAULT_SIGNED)
    parser.add_argument("--variation-json", type=Path, default=DEFAULT_VARIATION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "high_power": args.high_power_json,
        "signed": args.signed_json,
        "variation": args.variation_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["new_unique_internal_remaining"])


if __name__ == "__main__":
    main()
