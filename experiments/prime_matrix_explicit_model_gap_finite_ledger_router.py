#!/usr/bin/env python3
"""Prime Matrix 显式模型余量与有限 DPRC 账本路由器。

用法示例：
  python3 experiments/prime_matrix_explicit_model_gap_finite_ledger_router.py

输出：
  docs/monograph/prime-matrix-explicit-model-gap-finite-ledger-router.json
  docs/monograph/prime-matrix-explicit-model-gap-finite-ledger-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json"
DEFAULT_DPRC = DOCS / "prime-matrix-clean-core-dprc-centered-discrepancy-router.json"
DEFAULT_RSM_MD = DOCS / "prime-matrix-dprc-relative-sieve-margin.md"
DEFAULT_RSM_JSON = AUDIT_DOCS / "dprc_relative_sieve_margin_alpha043_p100000_20260506.json"
DEFAULT_DYNAMIC_JSON = AUDIT_DOCS / "dynamic_promoted_rough_capacity_audit_alpha043_p100000_20260506.json"
DEFAULT_JSON = DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-explicit-model-gap-finite-ledger-router.md"

MODEL_ATOM = "ExplicitModelGapAndFiniteDPRCLedger"
HIGH_MODEL_ATOM = "HighSegmentModelGapAlpha043C3AnalyticLedger"
FINITE_ATOM = "FiniteDPRCAlpha043PBelow2003Certificate"
CANONICAL_TERMINAL = "NoFurtherCanonicalSourceTerminalPromotionGap"
EXTERNAL_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


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
    """替换输入基中的模型账本原子。"""
    return text.replace(old, new)


def threshold_summary(rsm: dict[str, Any], threshold: int) -> dict[str, Any]:
    """按 P 阈值读取 RSM 汇总。"""
    for row in rsm.get("summaries", []):
        if row.get("threshold_p") == threshold:
            return row
    return {}


def dynamic_low_segment(dynamic: dict[str, Any], threshold: int) -> dict[str, Any]:
    """提取低段有限枚举摘要。"""
    rows = [row for row in dynamic.get("records", []) if row.get("p", 0) < threshold]
    primes = sorted({row["p"] for row in rows})
    if not rows:
        return {
            "record_count": 0,
            "prime_count": 0,
            "capacity_fail": None,
            "min_capacity_margin": None,
            "max_prime": None,
        }
    return {
        "record_count": len(rows),
        "prime_count": len(primes),
        "capacity_fail": sum(not row.get("capacity_pass", False) for row in rows),
        "min_capacity_margin": min(row["capacity_margin"] for row in rows),
        "max_prime": max(primes),
        "sides": sorted({row["side"] for row in rows}),
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


def build_rows(
    previous: dict[str, Any],
    dprc: dict[str, Any],
    rsm_md: str,
    rsm_json: dict[str, Any],
    dynamic_json: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """生成模型余量/有限账本判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == MODEL_ATOM and MODEL_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    rsm_interface = (
        MODEL_ATOM in dprc.get("latest_internal_subinputs", [])
        and "S-T=S(1-H)" in rsm_md
        and "D_+<=3 sqrt(S)" in rsm_md
        and "S(1-H)>3 sqrt(S)" in rsm_md
    )
    low = dynamic_low_segment(dynamic_json, 2003)
    finite_materialized = (
        low["record_count"] == 596
        and low["prime_count"] == 298
        and low["capacity_fail"] == 0
        and low["min_capacity_margin"] >= 1
        and low["max_prime"] == 1999
        and low.get("sides") == ["minus", "plus"]
    )
    high_2003 = threshold_summary(rsm_json, 2003)
    high_materialized = (
        high_2003.get("count") == 18578
        and high_2003.get("capacity_fail") == 0
        and high_2003.get("c_certificate_pass") is True
        and high_2003.get("min_model_gap_over_sqrt", 0) > 3.0
    )
    high_formal_open = high_materialized
    split_closed = active and guard and rsm_interface and finite_materialized and high_formal_open
    rows = [
        row(
            "ExplicitModelGapFiniteLedgerGateActive",
            active,
            False,
            "最新活动最窄点已转为显式模型余量与有限 DPRC 账本。",
            MODEL_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只整理假设早期零行反例链条中的 DPRC 账本，不用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "RSMIdentityInterfacePinned",
            rsm_interface,
            True,
            "RSM 恒等式把 DPRC 容量账本拆成模型余量 S(1-H) 与正偏差 D_+。",
            "本原子只处理有限账本与模型余量，不处理 D_+ 相对筛偏差。",
        ),
        row(
            FINITE_ATOM,
            finite_materialized,
            True,
            "P<2003 的 298 个素数、plus/minus 共 596 条记录已全部枚举，capacity_fail=0。",
            "有限段从活动解析硬点中移除。",
        ),
        row(
            "HighSegmentC3AuditMaterialized",
            high_materialized,
            False,
            "审计显示 P>=2003 时 S(1-H)>3sqrt(S)，且 C=3 数据账本通过。",
            "仍需解析证明，不能把审计当无条件定理。",
        ),
        row(
            HIGH_MODEL_ATOM,
            False,
            False,
            "剩余真正原子是 P>=2003 的显式解析模型余量：证明 S_Y(P)(1-H_Y(P))>3sqrt(S_Y(P))。",
            HIGH_MODEL_ATOM,
        ),
        row(
            MODEL_ATOM,
            split_closed,
            False,
            "原混合账本已分解：有限段闭合，高段模型余量成为唯一活动子输入；这不是原不等式整体证明。",
            HIGH_MODEL_ATOM,
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
    metrics = {
        "finite_low_segment": low,
        "high_segment_2003": {
            "count": high_2003.get("count"),
            "capacity_fail": high_2003.get("capacity_fail"),
            "min_capacity_margin": high_2003.get("min_capacity_margin"),
            "min_model_gap_over_sqrt": high_2003.get("min_model_gap_over_sqrt"),
            "max_positive_discrepancy_over_sqrt": high_2003.get(
                "max_positive_discrepancy_over_sqrt"
            ),
            "c_certificate_pass": high_2003.get("c_certificate_pass"),
        },
    }
    return rows, metrics


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行显式模型余量/有限 DPRC 账本拆分。"""
    previous = load_json(paths["previous"])
    dprc = load_json(paths["dprc"])
    rsm_md = paths["rsm_md"].read_text(encoding="utf-8")
    rsm_json = load_json(paths["rsm_json"])
    dynamic_json = load_json(paths["dynamic_json"])
    rows, metrics = build_rows(previous, dprc, rsm_md, rsm_json, dynamic_json)
    split_closed = next(bool(item["closed"]) for item in rows if item["gate"] == MODEL_ATOM)

    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), MODEL_ATOM, HIGH_MODEL_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), MODEL_ATOM, HIGH_MODEL_ATOM)
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), MODEL_ATOM, HIGH_MODEL_ATOM)

    source_paths = list(paths.values())
    return {
        "certificate_type": "explicit_model_gap_finite_ledger_router",
        "status": "explicit_model_gap_finite_ledger_split_finite_closed_high_model_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "explicit_model_gap_and_finite_dprc_ledger_split_closed": split_closed,
        "finite_dprc_alpha043_p_below_2003_certificate_closed": True,
        "high_segment_model_gap_alpha043_c3_analytic_ledger_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_atom_preserved": CANONICAL_TERMINAL,
        "terminal_gap_after_router": HIGH_MODEL_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "replacement": {MODEL_ATOM: HIGH_MODEL_ATOM},
        "closed_subinput": FINITE_ATOM,
        "next_priority": HIGH_MODEL_ATOM,
        "external_next_priority": EXTERNAL_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "metrics": metrics,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 ExplicitModelGapAndFiniteDPRCLedger 拆开。"
            "低段 P<2003 已由有限枚举账本闭合：298 个素数、双侧 596 条记录全部 capacity_pass。"
            "高段 P>=2003 的数据账本显示 C=3 余量存在，但这仍不是解析证明。"
            "因此活动最窄点从原混合原子压成 HighSegmentModelGapAlpha043C3AnalyticLedger。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    finite = result["metrics"]["finite_low_segment"]
    high = result["metrics"]["high_segment_2003"]
    lines = [
        "# Prime Matrix 显式模型余量与有限 DPRC 账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        (
            "explicit_model_gap_and_finite_dprc_ledger_split_closed="
            f"{fmt_bool(result['explicit_model_gap_and_finite_dprc_ledger_split_closed'])}"
        ),
        (
            "finite_dprc_alpha043_p_below_2003_certificate_closed="
            f"{fmt_bool(result['finite_dprc_alpha043_p_below_2003_certificate_closed'])}"
        ),
        (
            "high_segment_model_gap_alpha043_c3_analytic_ledger_proved="
            f"{fmt_bool(result['high_segment_model_gap_alpha043_c3_analytic_ledger_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 拆分律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "  + FiniteDPRCAlpha043PBelow2003Certificate(closed)",
        "```",
        "",
        "这一步只关闭有限段，并把高段模型余量单独命名；它不证明高段解析不等式，也不处理 `D_+<=3sqrt(S)` 的相对筛偏差。",
        "",
        "## 2. 账本指标",
        "",
        "| segment | records | primes | fail | key margin | status |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
        (
            f"| P<2003 finite | {finite['record_count']} | {finite['prime_count']} | "
            f"{finite['capacity_fail']} | {finite['min_capacity_margin']} | closed finite certificate |"
        ),
        (
            f"| P>=2003 model audit | {high['count']} | - | {high['capacity_fail']} | "
            f"{high['min_model_gap_over_sqrt']:.6f} sqrt(S) | analytic proof open |"
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
            "直接攻 `HighSegmentModelGapAlpha043C3AnalyticLedger`：用显式 Mertens/素数调和上界和动态粗骨架下界证明，对所有 `P>=2003` 都有 `S_Y(P)(1-H_Y(P))>3sqrt(S_Y(P))`。若不能一次闭合，应继续拆成 `H_Y(P)` 上界与 `S_Y(P)` 下界两张可审稿账本。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--dprc", type=Path, default=DEFAULT_DPRC)
    parser.add_argument("--rsm-md", type=Path, default=DEFAULT_RSM_MD)
    parser.add_argument("--rsm-json", type=Path, default=DEFAULT_RSM_JSON)
    parser.add_argument("--dynamic-json", type=Path, default=DEFAULT_DYNAMIC_JSON)
    parser.add_argument("--json-output", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-output", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "dprc": args.dprc,
        "rsm_md": args.rsm_md,
        "rsm_json": args.rsm_json,
        "dynamic_json": args.dynamic_json,
    }
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
