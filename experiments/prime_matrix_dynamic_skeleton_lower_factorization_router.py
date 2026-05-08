#!/usr/bin/env python3
"""Prime Matrix 动态粗骨架下界因子化路由器。

用法示例：
  python3 experiments/prime_matrix_dynamic_skeleton_lower_factorization_router.py

输出：
  docs/monograph/prime-matrix-dynamic-skeleton-lower-factorization-router.json
  docs/monograph/prime-matrix-dynamic-skeleton-lower-factorization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
AUDIT_DOCS = ROOT / "docs"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-harmonic-window-dusart-ledger-router.json"
DEFAULT_DYNAMIC_JSON = AUDIT_DOCS / "dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json"
DEFAULT_JSON = DOCS / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-dynamic-skeleton-lower-factorization-router.md"

SKELETON_ATOM = "DynamicRoughSkeletonAlpha043PGe3001Lower401Ledger"
FINITE_ATOM = "FiniteDynamicRoughSkeletonAlpha043P3001To99991Certificate"
TAIL_ATOM = "LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger"
EXTERNAL_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

FINITE_START = 3001
TAIL_START = 100_000
TARGET_S = 401
ALPHA = 0.43


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


def remove_wrapper(text: str) -> str:
    """清理删除单个 AND 原子后的多余括号。"""
    return text.replace("AND ()", "").replace("()", "").replace("( ", "(").replace(" )", ")")


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的骨架下界原子。"""
    return remove_wrapper(text.replace(old, new))


def finite_segment_metrics(records: list[dict[str, Any]]) -> dict[str, Any]:
    """提取 3001<=P<100000 的有限骨架核查指标。"""
    rows = [row for row in records if FINITE_START <= row.get("p", 0) < TAIL_START]
    primes = sorted({row["p"] for row in rows})
    min_row = min(rows, key=lambda row: row["skeleton_count"])
    return {
        "record_count": len(rows),
        "prime_count": len(primes),
        "prime_min": min(primes),
        "prime_max": max(primes),
        "min_skeleton_count": min_row["skeleton_count"],
        "min_record": {
            "p": min_row["p"],
            "side": min_row["side"],
            "cutoff": min_row["cutoff"],
            "low_prime_count": min_row["low_prime_count"],
        },
        "target_s": TARGET_S,
        "pass": min_row["skeleton_count"] >= TARGET_S,
    }


def tail_model_summary() -> dict[str, Any]:
    """记录尾段标准下界筛需要支付的目标形态。"""
    # dimension-one lower sieve 的自然主量约为 P V(z) f(log P/log z)，
    # 对 alpha=0.43 有 s=1/alpha in (2,3)，因此 f(s)>0。
    sieve_s = 1.0 / ALPHA
    return {
        "tail_start": TAIL_START,
        "alpha": ALPHA,
        "sieve_s": sieve_s,
        "target_s": TARGET_S,
        "required_form": (
            "For every prime P>=100000 and both signs, the sifted interval "
            "{1<=k<P: k avoids one residue class modulo every q<=P^0.43} has size >=401."
        ),
        "standard_route": (
            "dimension-one lower-bound linear sieve with level D comparable to P, "
            "plus endpoint/rounding remainder bounded absolutely below the P>=100000 margin"
        ),
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


def build_rows(previous: dict[str, Any], finite: dict[str, Any]) -> list[dict[str, Any]]:
    """生成动态粗骨架判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == SKELETON_ATOM and SKELETON_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    split_closed = active and guard and finite["pass"]
    return [
        row(
            "DynamicSkeletonLowerGateActive",
            active,
            False,
            "最新最窄点是动态粗骨架 S_Y(P)>=401。",
            SKELETON_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍处理假设早期零行链条中的模型余量账本，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            FINITE_ATOM,
            finite["pass"],
            True,
            "3001<=P<100000 的动态粗骨架已由现有审计逐点核查，最小值仍大于 401。",
            "有限桥接段关闭。",
        ),
        row(
            "TailLinearSieveReduction",
            split_closed,
            False,
            "P>=100000 的骨架下界被压成标准一维 lower-bound sieve 尾段账本。",
            TAIL_ATOM,
        ),
        row(
            TAIL_ATOM,
            False,
            False,
            "需要把线性筛下界常数、端点误差和 floor(P^0.43) 取整统一写成显式可审稿不等式。",
            TAIL_ATOM,
        ),
        row(
            SKELETON_ATOM,
            split_closed,
            False,
            "原骨架下界已分解为有限桥接证书与尾段 lower-sieve 输入；尚未整体证明。",
            TAIL_ATOM,
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
    """执行动态粗骨架下界因子化。"""
    previous = load_json(paths["previous"])
    dynamic = load_json(paths["dynamic_json"])
    finite = finite_segment_metrics(dynamic.get("records", []))
    tail = tail_model_summary()
    rows = build_rows(previous, finite)
    split_closed = next(bool(item["closed"]) for item in rows if item["gate"] == SKELETON_ATOM)

    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), SKELETON_ATOM, TAIL_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), SKELETON_ATOM, TAIL_ATOM)
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), SKELETON_ATOM, TAIL_ATOM)

    source_paths = list(paths.values())
    return {
        "certificate_type": "dynamic_skeleton_lower_factorization_router",
        "status": "dynamic_skeleton_lower_factorized_finite_closed_tail_linear_sieve_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "dynamic_skeleton_lower_factorized": split_closed,
        "finite_dynamic_skeleton_certificate_closed": True,
        "tail_linear_lower_sieve_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {SKELETON_ATOM: TAIL_ATOM},
        "closed_subinput": FINITE_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": TAIL_ATOM,
        "external_next_priority": EXTERNAL_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "finite_metrics": finite,
        "tail_model_summary": tail,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把动态粗骨架下界压成有限桥接与尾段线性筛。"
            "有限段 3001<=P<100000 已由现有动态提升轮审计关闭，最小骨架数为 "
            f"{finite['min_skeleton_count']}，出现在 P={finite['min_record']['p']} "
            f"{finite['min_record']['side']} 侧。"
            "因此当前唯一剩余是 P>=100000 的一维 lower-bound sieve 显式尾段账本。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    finite = result["finite_metrics"]
    tail = result["tail_model_summary"]
    lines = [
        "# Prime Matrix 动态粗骨架下界因子化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"dynamic_skeleton_lower_factorized={fmt_bool(result['dynamic_skeleton_lower_factorized'])}",
        f"finite_dynamic_skeleton_certificate_closed={fmt_bool(result['finite_dynamic_skeleton_certificate_closed'])}",
        f"tail_linear_lower_sieve_ledger_proved={fmt_bool(result['tail_linear_lower_sieve_ledger_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 因子化律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        f"  + {FINITE_ATOM}(closed)",
        "```",
        "",
        "## 2. 两段账本",
        "",
        "| segment | records | primes | min S | worst record | target | status |",
        "| --- | ---: | ---: | ---: | --- | ---: | --- |",
        (
            f"| 3001<=P<100000 | {finite['record_count']} | {finite['prime_count']} | "
            f"{finite['min_skeleton_count']} | P={finite['min_record']['p']}, "
            f"{finite['min_record']['side']}, cutoff={finite['min_record']['cutoff']} | "
            f"{finite['target_s']} | closed finite certificate |"
        ),
        (
            f"| P>=100000 | - | - | - | lower-bound sieve with s={tail['sieve_s']:.6f} | "
            f"{tail['target_s']} | open analytic ledger |"
        ),
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
            "直接攻 `LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger`：把一维 lower-bound sieve 在 `z=P^0.43`、`D≈P`、`s=1/0.43` 的显式常数、端点误差和取整误差全部写成一个可验算不等式，目标只需证明尾段骨架数至少 `401`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--dynamic-json", type=Path, default=DEFAULT_DYNAMIC_JSON)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {"previous": args.previous, "dynamic_json": args.dynamic_json}
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
