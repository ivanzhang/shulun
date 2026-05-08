#!/usr/bin/env python3
"""Prime Matrix 线性筛尾段余项缺口路由器。

用法示例：
  python3 experiments/prime_matrix_linear_sieve_tail_remainder_gap_router.py

输出：
  docs/monograph/prime-matrix-linear-sieve-tail-remainder-gap-router.json
  docs/monograph/prime-matrix-linear-sieve-tail-remainder-gap-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-linear-lower-sieve-tail-margin-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-linear-sieve-tail-remainder-gap-router.json"
DEFAULT_MD = DOCS / "prime-matrix-linear-sieve-tail-remainder-gap-router.md"

OLD_ATOM = "LinearLowerSieveTailTenPercentMainMarginPGe100000Ledger"
REMAINDER_ATOM = "RosserIwaniecWeightedFloorRemainderTenPercentBound"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TAIL_START = 100_000
TARGET_S = 401


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


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的尾段原子。"""
    return text.replace(old, new)


def remainder_metrics(previous: dict[str, Any]) -> dict[str, Any]:
    """计算主项与余项缺口指标。"""
    model = previous["model_main"]
    main = model["model_main_at_tail_start"]
    ten_percent = model["ten_percent_main_at_tail_start"]
    allowed_loss_to_target = main - TARGET_S
    allowed_loss_to_ten_percent = main - ten_percent
    trivial_level_loss = TAIL_START
    z = TAIL_START ** model["alpha"]
    z_square = z * z
    return {
        "main_at_tail_start": main,
        "ten_percent_main": ten_percent,
        "target_s": TARGET_S,
        "allowed_loss_to_target": allowed_loss_to_target,
        "allowed_loss_to_ten_percent": allowed_loss_to_ten_percent,
        "trivial_level_loss_d_equals_p": trivial_level_loss,
        "z_at_tail_start": z,
        "z_square_at_tail_start": z_square,
        "trivial_d_equals_p_exceeds_allowed_loss": trivial_level_loss > allowed_loss_to_ten_percent,
        "z_square_exceeds_allowed_loss_to_ten_percent": z_square > allowed_loss_to_ten_percent,
    }


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


def build_rows(previous: dict[str, Any], metrics: dict[str, Any]) -> list[dict[str, Any]]:
    """生成尾段余项缺口判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    algebra_imported = (
        previous.get("ten_percent_main_margin_algebra_closed") is True
        and metrics["ten_percent_main"] > TARGET_S
    )
    naive_remainder_gap = (
        metrics["trivial_d_equals_p_exceeds_allowed_loss"]
        and metrics["z_square_exceeds_allowed_loss_to_ten_percent"]
    )
    split_closed = active and guard and algebra_imported and naive_remainder_gap
    return [
        row(
            "TenPercentTailGateActive",
            active,
            False,
            "最新最窄点是尾段筛余达到线性筛模型主项 10%。",
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
            "TenPercentMainAlgebraImported",
            algebra_imported,
            True,
            "10% 主项大于目标 401 的代数余量已由上一层闭合。",
            "还需证明实际筛余达到该 10% 主项。",
        ),
        row(
            "NaiveAbsoluteRemainderCannotClose",
            naive_remainder_gap,
            True,
            "若只用 |r_d|<=1 的绝对余项，level D≈P 或 even z^2 的总损失都超过 10% 余量。",
            "必须控制 Rosser 权重 floor 余项，或改用外部短区间粗数下界。",
        ),
        row(
            "TailTenPercentMarginSplit",
            split_closed,
            False,
            "尾段 10% 主项包被压成二选一：内部权重余项控制，或外部短区间粗数定理。",
            f"{REMAINDER_ATOM} OR {EXTERNAL_ROUGH_ATOM}",
        ),
        row(
            REMAINDER_ATOM,
            False,
            False,
            "证明 Rosser-Iwaniec 下界权重与 floor 余项配对后，总损失不超过 90% 主项。",
            REMAINDER_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "引用或证明长度 P、阈值 P^0.43 的短区间 y-rough 数下界，直接给 S_Y(P)>=401。",
            EXTERNAL_ROUGH_ATOM,
        ),
        row(
            EXTERNAL_DIBFI_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_DIBFI_ATOM,
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
    """执行尾段余项缺口路由。"""
    previous = load_json(paths["previous"])
    metrics = remainder_metrics(previous)
    rows = build_rows(previous, metrics)
    split_closed = next(bool(item["closed"]) for item in rows if item["gate"] == "TailTenPercentMarginSplit")
    new_atom = f"({REMAINDER_ATOM} OR {EXTERNAL_ROUGH_ATOM})"
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, new_atom)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, new_atom)
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), OLD_ATOM, new_atom)

    source_paths = list(paths.values())
    return {
        "certificate_type": "linear_sieve_tail_remainder_gap_router",
        "status": "linear_sieve_tail_ten_percent_split_to_weighted_remainder_or_external_rough_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "tail_ten_percent_margin_split": split_closed,
        "rosser_iwaniec_weighted_floor_remainder_proved": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {OLD_ATOM: new_atom},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": REMAINDER_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "metrics": metrics,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步定位了 10% 主项包的真实剩余。主项常数足够，但不能用黑箱绝对余项关闭："
            f"P=100000 时主项约 {metrics['main_at_tail_start']:.6f}，10% 主项约 "
            f"{metrics['ten_percent_main']:.6f}，而 |r_d|<=1 的 D≈P 余项尺度是 "
            f"{metrics['trivial_level_loss_d_equals_p']:.0f}。"
            "因此真正最窄点是 Rosser-Iwaniec 权重下的 floor 余项控制；外部路线则是短区间粗数下界。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    metrics = result["metrics"]
    lines = [
        "# Prime Matrix 线性筛尾段余项缺口路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"tail_ten_percent_margin_split={fmt_bool(result['tail_ten_percent_margin_split'])}",
        (
            "rosser_iwaniec_weighted_floor_remainder_proved="
            f"{fmt_bool(result['rosser_iwaniec_weighted_floor_remainder_proved'])}"
        ),
        (
            "external_short_interval_rough_lower_bound_accepted="
            f"{fmt_bool(result['external_short_interval_rough_lower_bound_accepted'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 缺口定位",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 余项尺度",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| main at P=100000 | {metrics['main_at_tail_start']:.6f} |",
        f"| 10% main | {metrics['ten_percent_main']:.6f} |",
        f"| target S | {metrics['target_s']} |",
        f"| allowed loss to 10% main | {metrics['allowed_loss_to_ten_percent']:.6f} |",
        f"| naive D=P remainder scale | {metrics['trivial_level_loss_d_equals_p']:.0f} |",
        f"| z at P=100000 | {metrics['z_at_tail_start']:.6f} |",
        f"| z^2 at P=100000 | {metrics['z_square_at_tail_start']:.6f} |",
        "",
        "这说明“主项很大”不是最后证明；最后证明必须说明 Rosser-Iwaniec 权重与 floor 余项不会发生最坏同向叠加。",
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
            "优先攻 `RosserIwaniecWeightedFloorRemainderTenPercentBound`：写出下界筛权重的精确 floor-sum 账本，证明加权余项总损失不超过 90% 主项；若走外部路线，则需登记一个直接适配 `x=P^2`、区间长 `P`、粗阈值 `P^0.43` 的短区间 rough-number 下界。",
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
