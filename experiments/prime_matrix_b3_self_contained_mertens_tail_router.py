#!/usr/bin/env python3
"""Prime Matrix B=3 自足 Mertens 尾段证明边界路由器。

用法示例：
  python3 experiments/prime_matrix_b3_self_contained_mertens_tail_router.py

输出：
  docs/monograph/prime-matrix-b3-self-contained-mertens-tail-router.json
  docs/monograph/prime-matrix-b3-self-contained-mertens-tail-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json"
DEFAULT_EXPLICIT_FORMULA = ROOT / "docs" / "rh-pc1-explicit-formula-proof-appendix.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-self-contained-mertens-tail-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-self-contained-mertens-tail-router.md"

OLD_INTERNAL_ATOM = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
FINITE_PROMOTION_ATOM = "B3FinitePrimeReciprocalStepLedger10372To19999PGe100000"
TAIL_20000_ATOM = "SelfContainedPrimeReciprocalMertensTailXGe20000"
PARTIAL_SUMMATION_ATOM = "PrimeReciprocalPartialSummationFromThetaEnvelopeClosed"
ZERO_FREE_ATOM = "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000"
MERTENS_CONSTANT_ATOM = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
EXTERNAL_DUSART_ATOM = "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted"
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


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含所有片段。"""
    return all(needle in text for needle in needles)


def replacement_pair() -> str:
    """写出自足尾段证明的替换包。"""
    return (
        f"({FINITE_PROMOTION_ATOM} AND {PARTIAL_SUMMATION_ATOM} "
        f"AND {ZERO_FREE_ATOM} AND {MERTENS_CONSTANT_ATOM})"
    )


def replace_atom(text: str) -> str:
    """替换自足 Mertens 尾段原子。"""
    return text.replace(OLD_INTERNAL_ATOM, replacement_pair())


def source_audit(explicit_formula_text: str) -> dict[str, Any]:
    """审查当前内部材料能否支撑自足 Mertens 尾段。"""
    smooth_explicit_formula = contains_all(
        explicit_formula_text,
        ["Mellin", "-ζ'(s)/ζ(s)", "Ψ_W(X)", "非平凡零点"],
    )
    zero_free_region_present = contains_all(
        explicit_formula_text,
        ["zero-free", "零点自由", "de la Vallée", "Korobov"],
    )
    theta_envelope_present = contains_all(
        explicit_formula_text,
        ["vartheta", "theta", "36260", "x/log"],
    )
    return {
        "smooth_explicit_formula_appendix_present": smooth_explicit_formula,
        "zero_free_region_proof_present": zero_free_region_present,
        "explicit_theta_envelope_present_in_appendix": theta_envelope_present,
        "partial_summation_transfer_formal": True,
        "meissel_mertens_constant_interval_present": False,
        "tail_20000_self_contained_proved": False,
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


def build_rows(previous: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成自足 Mertens 尾段证明边界判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_INTERNAL_ATOM and OLD_INTERNAL_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    finite_promotion_reusable = bool(
        previous.get("b3_signed_delay_multiplier_anchor_route_closed")
    )
    partial_closed = bool(audit["partial_summation_transfer_formal"])
    zero_free_closed = bool(audit["zero_free_region_proof_present"])
    constant_closed = bool(audit["meissel_mertens_constant_interval_present"])
    reduced = active and guard and finite_promotion_reusable and partial_closed
    return [
        row(
            "SelfContainedMertensTailGateActive",
            active,
            False,
            "完全自足路线的唯一剩余是把 Dusart reciprocal-prime Mertens 定理内联证明。",
            OLD_INTERNAL_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条内的筛主系数解析输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FinitePromotionTo20000Reusable",
            finite_promotion_reusable,
            True,
            "上一层已经把 10372<=x<20000 提升为有限精确阶梯账本；自足尾段只需从 x>=20000 开始。",
            FINITE_PROMOTION_ATOM,
        ),
        row(
            "SmoothExplicitFormulaAppendixPresent",
            bool(audit["smooth_explicit_formula_appendix_present"]),
            True,
            "仓库已有平滑 Chebyshev 显式公式附录，可作为 PNT 型证明链的起点。",
            "还不能推出显式零点自由区或 Dusart 常数。",
        ),
        row(
            "PartialSummationTransferClosed",
            partial_closed,
            True,
            "一旦给出显式 theta/psi 误差和常数区间，素数倒数和由 Stieltjes 分部求和形式推出。",
            PARTIAL_SUMMATION_ATOM,
        ),
        row(
            "ExplicitZeroFreeThetaEnvelopeMissing",
            zero_free_closed,
            False,
            "当前附录没有 de la Vallee Poussin/Korobov-Vinogradov 型零点自由区与显式 theta 误差证明。",
            ZERO_FREE_ATOM,
        ),
        row(
            "MeisselMertensConstantIntervalMissing",
            constant_closed,
            False,
            "当前仓库没有自足给出 B1 常数区间并与 x=20000 基点核验对接。",
            MERTENS_CONSTANT_ATOM,
        ),
        row(
            "SelfContainedMertensTailReducedToPNTPackage",
            reduced,
            False,
            "旧 Dusart 原子被压成有限锚点、分部求和、显式零点自由 theta 包、B1 常数区间四项。",
            replacement_pair(),
        ),
        row(
            TAIL_20000_ATOM,
            False,
            False,
            "等价的简写：从 x>=20000 开始给出自足 reciprocal-prime Mertens 尾段误差。",
            f"{ZERO_FREE_ATOM} AND {MERTENS_CONSTANT_ATOM}",
        ),
        row(
            EXTERNAL_DUSART_ATOM,
            True,
            False,
            "若接受 Dusart 外部定理，本分支已经由上一层条件路线关闭。",
            DSTRUCTURE,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是外部 Mertens 版最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行自足 Mertens 尾段证明边界路由。"""
    previous = load_json(paths["previous"])
    explicit_formula_text = paths["explicit_formula"].read_text(encoding="utf-8")
    audit = source_audit(explicit_formula_text)
    rows = build_rows(previous, audit)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "SelfContainedMertensTailReducedToPNTPackage"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_self_contained_mertens_tail_router",
        "status": "self_contained_mertens_tail_reduced_to_explicit_pnt_package_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "self_contained_mertens_tail_reduced": reduced,
        "self_contained_mertens_tail_proved": False,
        "external_mertens_route_closed": bool(
            previous.get("b3_boundary_variation_one_percent_conditional_closed")
        ),
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_INTERNAL_ATOM: replacement_pair()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": ZERO_FREE_ATOM,
        "secondary_priority": MERTENS_CONSTANT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "final_promotion_priority": DSTRUCTURE,
        "source_audit": audit,
        "plain_conclusion": (
            "完全自足 Mertens 尾段没有从当前几何或 B=3 筛结构自动闭合；它等价于把显式 PNT "
            "机器内联：零点自由区/显式 theta 误差、B1 常数区间，以及分部求和转移。"
            "仓库已有平滑显式公式起点和分部求和形式，但缺少零点自由区与 B1 区间证明。"
            "因此外部 Dusart 版已经推进到 DStructure，完全自足版的唯一真正剩余是显式 PNT 包。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    audit = result["source_audit"]
    lines = [
        "# Prime Matrix B=3 自足 Mertens 尾段证明边界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"self_contained_mertens_tail_reduced={fmt_bool(result['self_contained_mertens_tail_reduced'])}",
        f"self_contained_mertens_tail_proved={fmt_bool(result['self_contained_mertens_tail_proved'])}",
        f"external_mertens_route_closed={fmt_bool(result['external_mertens_route_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 自足替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 2. 来源审查",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in audit.items():
        lines.append(f"| {table_cell(key)} | `{fmt_bool(value)}` |")
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            "## 5. 下一步",
            "",
            f"自足版先攻 `{result['next_priority']}`，随后补 `{result['secondary_priority']}`。",
            f" 外部 Mertens 版则继续晋级 `{result['conditional_next_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--explicit-formula", type=Path, default=DEFAULT_EXPLICIT_FORMULA)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "explicit_formula": args.explicit_formula,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
