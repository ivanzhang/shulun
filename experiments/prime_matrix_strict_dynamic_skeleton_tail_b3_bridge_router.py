#!/usr/bin/env python3
"""Prime Matrix strict 动态骨架尾段到 B3 粗筛桥接路由器。

用法示例：
  python3 experiments/prime_matrix_strict_dynamic_skeleton_tail_b3_bridge_router.py

输出：
  docs/monograph/prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json
  docs/monograph/prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_FRONTIER = DOCS / "prime-matrix-strict-rate-bearing-frontier-drilldown-router.json"
DEFAULT_SKELETON = DOCS / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"
DEFAULT_ROSSER = DOCS / "prime-matrix-explicit-rosser-lower-weight-ledger-router.json"
DEFAULT_DOMINANCE = DOCS / "prime-matrix-beta-sieve-lower-bound-dominance-router.json"
DEFAULT_B3_MAIN = DOCS / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json"
DEFAULT_B3_TV = DOCS / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json"
DEFAULT_MERTENS = DOCS / "prime-matrix-b3-self-contained-mertens-tail-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json"
DEFAULT_MD = DOCS / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.md"

TAIL = "LinearLowerSieveDynamicRoughSkeletonTailPGe100000Ledger"
PDEC_KLS_PACKET = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_rate_bearing_packet"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
EXT_ROUGH = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
STD_BETA = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
SELF_MERTENS = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
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


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def constants(rosser: dict[str, Any]) -> dict[str, Any]:
    """提取尾段容量常数。"""
    data = dict(rosser.get("constants", {}))
    model = float(data["model_main_at_tail_start"])
    data["ten_percent_surplus_over_401"] = float(data["ten_percent_main_at_tail_start"]) - 401.0
    data["ninety_eight_percent_main_at_tail_start"] = 0.98 * model
    data["ninety_eight_percent_surplus_over_401"] = data["ninety_eight_percent_main_at_tail_start"] - 401.0
    return data


def build_rows(certs: dict[str, dict[str, Any]], const: dict[str, Any]) -> list[dict[str, Any]]:
    """生成尾段 B3 桥接判定表。"""
    frontier = certs["frontier"]
    skeleton = certs["skeleton"]
    dominance = certs["dominance"]
    b3_main = certs["b3_main"]
    b3_tv = certs["b3_tv"]
    mertens = certs["mertens"]

    active = frontier.get("next_nonrecursive_attack_target") == TAIL
    tail_reduced = (
        skeleton.get("dynamic_skeleton_lower_factorized") is True
        and skeleton.get("tail_linear_lower_sieve_ledger_proved") is False
    )
    dominance_closed = (
        dominance.get("lower_weight_recursive_construction_closed") is True
        and dominance.get("lower_weight_dominance_proved") is True
    )
    ten_percent_ok = (
        const.get("ten_percent_main_exceeds_target") is True
        and const["ten_percent_surplus_over_401"] > 0
    )
    main_conditional = b3_main.get("beta_sieve_main_coefficient_99pct_conditional_closed") is True
    tv_conditional = b3_tv.get("b3_tv_budget_conditional_external_closed") is True
    self_mertens_open = mertens.get("self_contained_mertens_tail_proved") is False
    external_tail_closed = active and tail_reduced and dominance_closed and ten_percent_ok and main_conditional and tv_conditional

    return [
        row(
            "TailLinearSieveGateActive",
            active,
            False,
            "前沿下钻后，非循环可攻点正是 P>=100000 的动态骨架尾段 lower-sieve 账本。",
            TAIL,
        ),
        row(
            "DynamicSkeletonTailObjectMatched",
            tail_reduced,
            True,
            "尾段对象是区间 1<=k<P 中避开每个 q<=P^0.43 的一个同余类；对任意 formal unit 与正负侧都只改变同余类名，不改变筛公式。",
            "可接入一维 beta-sieve 粗筛余框架。",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本步仍只在假设早期零行反例链条内证明必要筛余输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LowerWeightConstructionAndDominanceImported",
            dominance_closed,
            True,
            "B=3 lower weights 的有限递归、支撑、符号和逐点 lower-bound 支配已由内部组合证明关闭。",
            "不再把 lower weights 构造当活动硬点。",
        ),
        row(
            "TenPercentCapacityAlgebraImported",
            ten_percent_ok,
            True,
            "P=100000 处 10% 模型主项仍大于 401，且尾段主量随 P/log P 增长。",
            "需要主系数与 floor/TV 余项账本匹配。",
        ),
        row(
            "B3MainCoefficientConditionalExternalClosed",
            main_conditional,
            False,
            "接受外部显式 Mertens/Dusart 尾段时，B=3 主系数 99% 包已在既有证书中闭合。",
            "严格自足版仍需内联 Mertens/PNT 尾段。",
        ),
        row(
            "B3RemainderTVConditionalExternalClosed",
            tv_conditional,
            False,
            "接受外部显式 Mertens/Dusart 尾段时，长度 P 的 B3 floor/TV 余项由有符号 Stieltjes 边界预算关闭。",
            "严格自足版仍需内联 Mertens/PNT 尾段。",
        ),
        row(
            "ExternalOrStandardTailLedgerClosed",
            external_tail_closed,
            False,
            "在允许外部显式 Mertens/Dusart 或标准 beta-sieve 粗数输入时，动态骨架尾段下界可从活动剩余基移除。",
            f"{EXT_ROUGH} OR {STD_BETA}",
        ),
        row(
            "StrictSelfContainedMertensTailStillOpen",
            self_mertens_open,
            False,
            "严格自足版不能把外部 Mertens/Dusart 尾段当已证；需要内联显式 PNT/Mertens 证明。",
            SELF_MERTENS,
        ),
        row(
            "StrictSelfContainedTailLedgerProved",
            False,
            False,
            "当前仓库尚未给出完全自足的 Mertens/PNT 尾段内联证明，因此 tail lower-sieve 账本不能标成严格自足已证。",
            SELF_MERTENS,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "该桥接只关闭或压缩高段骨架尾段输入；速率终端门、RatePreservation 与 DStructure 仍未全部完成。",
            f"{PDEC_KLS_PACKET} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行动态骨架尾段到 B3 的桥接。"""
    certs = {name: load_json(path) for name, path in paths.items()}
    const = constants(certs["rosser"])
    rows = build_rows(certs, const)
    row_map = {item["gate"]: item for item in rows}
    strict_basis = f"{PDEC_KLS_PACKET} AND {SELF_MERTENS} AND {RATE} AND {DSTRUCTURE}"
    external_basis = f"{PDEC_KLS_PACKET} AND {RATE} AND {DSTRUCTURE}"

    return {
        "certificate_type": "prime_matrix_strict_dynamic_skeleton_tail_b3_bridge_router",
        "status": "dynamic_skeleton_tail_b3_bridge_conditional_external_closed_self_contained_mertens_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "tail_object_interface_closed": row_map["DynamicSkeletonTailObjectMatched"]["closed"],
        "lower_weight_construction_and_dominance_imported": row_map[
            "LowerWeightConstructionAndDominanceImported"
        ]["closed"],
        "ten_percent_capacity_algebra_imported": row_map["TenPercentCapacityAlgebraImported"]["closed"],
        "tail_ledger_external_or_standard_closed": row_map["ExternalOrStandardTailLedgerClosed"]["closed"],
        "tail_ledger_strict_self_contained_proved": False,
        "self_contained_mertens_tail_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "tail_atom_before_router": TAIL,
        "strict_self_contained_replacement": SELF_MERTENS,
        "strict_self_contained_remaining_basis": strict_basis,
        "external_or_standard_remaining_basis": external_basis,
        "next_direct_attack_target": SELF_MERTENS,
        "parallel_attack_targets": [PDEC_KLS_PACKET, RATE, DSTRUCTURE],
        "constants": const,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "source_hashes": {str(path.relative_to(ROOT)): sha256(path) for path in paths.values()},
        "plain_conclusion": (
            "本步把动态骨架尾段 lower-sieve 账本接到已有 B3 粗筛体系：对象接口、lower weights "
            "支配性和 10% 容量代数均已对齐。若接受外部显式 Mertens/Dusart 或标准 beta-sieve 输入，"
            "尾段骨架下界可条件关闭；严格自足版仍只剩 Mertens/PNT 尾段内联证明，不能声明行/列无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写出 Markdown 归档。"""
    const = result["constants"]
    lines = [
        "# Prime Matrix strict 动态骨架尾段到 B3 粗筛桥接路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"tail_object_interface_closed={fmt_bool(result['tail_object_interface_closed'])}",
        f"lower_weight_construction_and_dominance_imported={fmt_bool(result['lower_weight_construction_and_dominance_imported'])}",
        f"ten_percent_capacity_algebra_imported={fmt_bool(result['ten_percent_capacity_algebra_imported'])}",
        f"tail_ledger_external_or_standard_closed={fmt_bool(result['tail_ledger_external_or_standard_closed'])}",
        f"tail_ledger_strict_self_contained_proved={fmt_bool(result['tail_ledger_strict_self_contained_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同口径接口",
        "",
        "动态骨架尾段的目标对象可写成：",
        "",
        "```text",
        "S(P)=#{1<=k<P: k avoids one prescribed residue class modulo every prime q<=P^0.43}.",
        "```",
        "",
        "对每个 squarefree `d<P`，CRT 给出单余类计数：",
        "",
        "```text",
        "A_d(P)=(P-1)/d + r_d, |r_d|<=1.",
        "```",
        "",
        "因此该对象与已有 B3 lower-weight 粗筛余账本同口径。",
        "",
        "## 2. 容量常数",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| tail start | {int(const['tail_start'])} |",
        f"| alpha | {const['alpha']:.6f} |",
        f"| f(1/alpha) | {const['linear_sieve_f']:.12f} |",
        f"| model main at P=100000 | {const['model_main_at_tail_start']:.6f} |",
        f"| 10% main | {const['ten_percent_main_at_tail_start']:.6f} |",
        f"| 10% surplus over 401 | {const['ten_percent_surplus_over_401']:.6f} |",
        f"| 98% main | {const['ninety_eight_percent_main_at_tail_start']:.6f} |",
        f"| 98% surplus over 401 | {const['ninety_eight_percent_surplus_over_401']:.6f} |",
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
            "## 4. 剩余基",
            "",
            "严格自足路线：",
            "",
            "```text",
            result["strict_self_contained_remaining_basis"],
            "```",
            "",
            "接受外部或标准筛输入的路线：",
            "",
            "```text",
            result["external_or_standard_remaining_basis"],
            "```",
            "",
            "本证书不把外部 Mertens/Dusart 或标准 beta-sieve 输入冒充为严格自足证明。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frontier", type=Path, default=DEFAULT_FRONTIER)
    parser.add_argument("--skeleton", type=Path, default=DEFAULT_SKELETON)
    parser.add_argument("--rosser", type=Path, default=DEFAULT_ROSSER)
    parser.add_argument("--dominance", type=Path, default=DEFAULT_DOMINANCE)
    parser.add_argument("--b3-main", type=Path, default=DEFAULT_B3_MAIN)
    parser.add_argument("--b3-tv", type=Path, default=DEFAULT_B3_TV)
    parser.add_argument("--mertens", type=Path, default=DEFAULT_MERTENS)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "frontier": args.frontier,
        "skeleton": args.skeleton,
        "rosser": args.rosser,
        "dominance": args.dominance,
        "b3_main": args.b3_main,
        "b3_tv": args.b3_tv,
        "mertens": args.mertens,
    }
    result = run(paths)
    args.json_output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_output)
    print(f"wrote {args.json_output}")
    print(f"wrote {args.md_output}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
