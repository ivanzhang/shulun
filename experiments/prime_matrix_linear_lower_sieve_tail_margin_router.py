#!/usr/bin/env python3
"""Prime Matrix 线性下界筛尾段余量路由器。

用法示例：
  python3 experiments/prime_matrix_linear_lower_sieve_tail_margin_router.py

输出：
  docs/monograph/prime-matrix-linear-lower-sieve-tail-margin-router.json
  docs/monograph/prime-matrix-linear-lower-sieve-tail-margin-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-linear-lower-sieve-tail-margin-router.json"
DEFAULT_MD = DOCS / "prime-matrix-linear-lower-sieve-tail-margin-router.md"

OLD_ATOM = "LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger"
NEW_ATOM = "LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger"
EXTERNAL_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
TAIL_START = 100_000
TARGET_S = 401
EULER_GAMMA = 0.5772156649015329
TEN_PERCENT = 0.10


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def linear_sieve_f(sieve_s: float) -> float:
    """一维线性下界筛在 2<=s<=3 的 f(s)。"""
    return 2.0 * math.exp(EULER_GAMMA) * math.log(sieve_s - 1.0) / sieve_s


def model_main(p: int) -> dict[str, Any]:
    """计算 P=tail_start 处的线性筛模型主项。"""
    sieve_s = 1.0 / ALPHA
    f_value = linear_sieve_f(sieve_s)
    v_model = math.exp(-EULER_GAMMA) / (ALPHA * math.log(p))
    main = p * v_model * f_value
    ten_percent_main = TEN_PERCENT * main
    return {
        "tail_start": p,
        "alpha": ALPHA,
        "sieve_s": sieve_s,
        "linear_sieve_f": f_value,
        "v_model": v_model,
        "model_main_at_tail_start": main,
        "ten_percent_main_at_tail_start": ten_percent_main,
        "target_s": TARGET_S,
        "target_ratio_of_model_main": TARGET_S / main,
        "ten_percent_margin": ten_percent_main - TARGET_S,
        "ten_percent_suffices": ten_percent_main > TARGET_S,
    }


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的尾段线性筛原子。"""
    return text.replace(old, new)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any], model: dict[str, Any]) -> list[dict[str, Any]]:
    """生成尾段余量判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    algebra_closed = model["ten_percent_suffices"]
    compression_closed = active and guard and algebra_closed
    return [
        row(
            "LinearLowerSieveTailGateActive",
            active,
            False,
            "最新最窄点是 P>=100000 的动态粗骨架尾段 lower-sieve 账本。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内整理模型余量，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "TenPercentMainSufficesAlgebra",
            algebra_closed,
            True,
            "在 P=100000 处，线性筛模型主项的 10% 已超过目标 401；尾段随 P/logP 增长。",
            NEW_ATOM,
        ),
        row(
            "TailInputCompressedToTenPercentMainMargin",
            compression_closed,
            False,
            "尾段输入已从泛泛 lower-sieve 压成具体的 10% 主项显式余量包。",
            NEW_ATOM,
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "需要证明实际筛余计数至少达到标准线性筛模型主项的 10%，并显式支付 Mertens 乘积、端点和取整误差。",
            NEW_ATOM,
        ),
        row(
            EXTERNAL_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行尾段余量压缩。"""
    previous = load_json(paths["previous"])
    model = model_main(TAIL_START)
    rows = build_rows(previous, model)
    compressed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "TailInputCompressedToTenPercentMainMargin"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), OLD_ATOM, NEW_ATOM)

    source_paths = list(paths.values())
    return {
        "certificate_type": "linear_lower_sieve_tail_margin_router",
        "status": "linear_lower_sieve_tail_compressed_to_ten_percent_main_margin_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "tail_linear_sieve_input_compressed": compressed,
        "ten_percent_main_margin_algebra_closed": True,
        "ten_percent_main_margin_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": NEW_ATOM,
        "external_next_priority": EXTERNAL_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "model_main": model,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 P>=100000 的 lower-sieve 尾段继续压窄。"
            f"在 alpha=0.43、s=1/alpha={model['sieve_s']:.6f} 下，一维线性筛模型主项在 "
            f"P=100000 约为 {model['model_main_at_tail_start']:.6f}，其 10% 为 "
            f"{model['ten_percent_main_at_tail_start']:.6f}>401。"
            "因此剩余不再是一般 lower-sieve，而是证明实际尾段筛余至少达到模型主项 10% 的显式常数账本。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    model = result["model_main"]
    lines = [
        "# Prime Matrix 线性下界筛尾段余量路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"tail_linear_sieve_input_compressed={fmt_bool(result['tail_linear_sieve_input_compressed'])}",
        f"ten_percent_main_margin_algebra_closed={fmt_bool(result['ten_percent_main_margin_algebra_closed'])}",
        f"ten_percent_main_margin_ledger_proved={fmt_bool(result['ten_percent_main_margin_ledger_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压缩律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 常数账本",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| alpha | {model['alpha']:.6f} |",
        f"| s=1/alpha | {model['sieve_s']:.6f} |",
        f"| linear sieve f(s) | {model['linear_sieve_f']:.6f} |",
        f"| model main at P=100000 | {model['model_main_at_tail_start']:.6f} |",
        f"| 10% model main | {model['ten_percent_main_at_tail_start']:.6f} |",
        f"| target S | {model['target_s']} |",
        f"| target/main | {model['target_ratio_of_model_main']:.6f} |",
        f"| 10% margin | {model['ten_percent_margin']:.6f} |",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 5. 下一步",
            "",
            "直接攻 `LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger`：给出一个显式 lower-bound sieve 常数包，证明动态同余骨架在 `P>=100000` 时至少保留标准模型主项的 10%。这只需远弱于完整最优线性筛常数的版本。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous}
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")


if __name__ == "__main__":
    main()
