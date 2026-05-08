#!/usr/bin/env python3
"""Prime Matrix B=3 边界变差乘子路由器。

用法示例：
  python3 experiments/prime_matrix_b3_boundary_variation_multiplier_router.py

输出：
  docs/monograph/prime-matrix-b3-boundary-variation-multiplier-router.json
  docs/monograph/prime-matrix-b3-boundary-variation-multiplier-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-explicit-prime-reciprocal-mertens-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-boundary-variation-multiplier-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-boundary-variation-multiplier-router.md"

VARIATION_ATOM = "B3BoundaryVariationOnePercentTransferLedger"
FACE_ATOM = "B3RosserFaceDictionaryClosedAlpha043"
MULTIPLIER_ATOM = "B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043"
INTERNAL_TAIL_ATOM = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
EXTERNAL_MERTENS_ATOM = "DusartPrimeReciprocalMertensEnvelopeXGe286ExternalAccepted"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
EULER_GAMMA = 0.5772156649015329
ONE_PERCENT = 0.01


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


def linear_sieve_f(alpha: float = ALPHA) -> float:
    """计算 2<s<3 区间的一维线性下界筛函数 f(s)。"""
    sieve_s = 1.0 / alpha
    return 2.0 * math.exp(EULER_GAMMA) * math.log(sieve_s - 1.0) / sieve_s


def face_dictionary() -> list[dict[str, Any]]:
    """登记 B=3 admissible word 区域的符号边界字典。"""
    return [
        {
            "face": "ordering_faces",
            "equation": "u_i=u_{i+1}",
            "count_for_length_r": "max(r-1,0)",
            "role": "保证降序 prime word 无重复；相邻跳点碰撞只作为 Stieltjes 原子合并处理。",
            "closed": True,
        },
        {
            "face": "alpha_cap",
            "equation": "u_1=alpha",
            "count_for_length_r": "1 if r>=1 else 0",
            "role": "最高素因子阈值 z=P^alpha 的移动端点。",
            "closed": True,
        },
        {
            "face": "zero_floor",
            "equation": "u_r=0",
            "count_for_length_r": "1 if r>=1 else 0",
            "role": "Buchstab 递归的底边；实际素数从 2 起，低阈值已由有限阶梯账本承接。",
            "closed": True,
        },
        {
            "face": "b3_rosser_gate_faces",
            "equation": "u_1+...+u_{2m-1}+3u_{2m}=1",
            "count_for_length_r": "floor(r/2)",
            "role": "B=3 lower word rule 的偶位门控边界。",
            "closed": True,
        },
    ]


def variation_budget(previous: dict[str, Any]) -> dict[str, Any]:
    """计算一百分点预算与所需有符号乘子上限。"""
    f_value = linear_sieve_f()
    one_percent_budget = ONE_PERCENT * f_value
    tail_error = previous["tail_theorem_ledger"]["dusart_error_at_tail_start"]
    required_multiplier = one_percent_budget / tail_error
    return {
        "alpha": ALPHA,
        "s": 1.0 / ALPHA,
        "linear_lower_sieve_f": f_value,
        "one_percent_budget": one_percent_budget,
        "tail_error_source": EXTERNAL_MERTENS_ATOM,
        "dusart_tail_error_at_x_10372": tail_error,
        "required_signed_multiplier_upper_bound": required_multiplier,
        "required_signed_multiplier_atom": MULTIPLIER_ATOM,
        "finite_atoms_before_10372_exact": bool(
            previous.get("finite_prime_step_ledger_286_to_10371_closed")
        ),
        "external_mertens_closed": bool(
            previous.get("explicit_prime_reciprocal_mertens_external_closed")
        ),
        "self_contained_mertens_tail_open": not bool(
            previous.get("explicit_prime_reciprocal_mertens_self_contained_proved")
        ),
    }


def replacement_pair() -> str:
    """写出边界变差输入的替换包。"""
    return f"({FACE_ATOM} AND {MULTIPLIER_ATOM})"


def replace_atom(text: str) -> str:
    """替换 B=3 边界变差原子。"""
    return text.replace(VARIATION_ATOM, replacement_pair())


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


def build_rows(previous: dict[str, Any], budget: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 B=3 边界变差乘子判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    conditional_basis = previous.get("latest_conditional_basis", "")
    active = (
        VARIATION_ATOM in self_basis
        or (
            previous.get("conditional_next_priority") == VARIATION_ATOM
            and VARIATION_ATOM in conditional_basis
        )
    )
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    finite_exact = bool(budget["finite_atoms_before_10372_exact"])
    external_mertens = bool(budget["external_mertens_closed"])
    face_closed = all(item["closed"] for item in face_dictionary())
    multiplier_bound_proved = False
    reduced = active and guard and finite_exact and face_closed
    return [
        row(
            "BoundaryVariationGateActive",
            active,
            False,
            "当前 B=3 内部余项只剩边界变差传递；外部 Mertens 线下它是下一最窄点。",
            VARIATION_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内处理筛主系数误差，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FinitePrimeStepAtomsBefore10372Exact",
            finite_exact,
            True,
            "286<=x<10372 的素数跳点已经作为精确 Stieltjes 原子保留，不进入变差误差预算。",
            "无有限低阈值误差。",
        ),
        row(
            "ExternalMertensTailAvailableForConditionalRoute",
            external_mertens,
            False,
            "若接受 Dusart 型外部显式 Mertens 定理，尾段一维 forcing 的最大误差为 0.001506804667。",
            EXTERNAL_MERTENS_ATOM,
        ),
        row(
            "B3RosserFaceDictionaryClosed",
            face_closed,
            True,
            "B=3 admissible word 的 ordering/cap/floor/Rosser gate face 字典已完全列出。",
            FACE_ATOM,
        ),
        row(
            "RequiredMultiplierBudgetComputed",
            True,
            True,
            "1% f(s) 预算除以 Dusart 尾段最大误差，得到有符号传播乘子必须小于约 2.865。",
            MULTIPLIER_ATOM,
        ),
        row(
            "NaiveAbsoluteFaceVariationCannotBeUsed",
            True,
            True,
            "word 长度不固定，绝对 face 数随 r 增长；必须证明同一 Buchstab delay kernel 下的有符号乘子纪律。",
            MULTIPLIER_ATOM,
        ),
        row(
            "BoundaryVariationReducedToSignedMultiplier",
            reduced,
            False,
            "边界变差原子被压成已闭合的 face 字典和唯一剩余的有符号 delay-kernel 乘子上界。",
            replacement_pair(),
        ),
        row(
            MULTIPLIER_ATOM,
            multiplier_bound_proved,
            False,
            "证明 B=3 交错 Stieltjes 边界 forcing 经全长度 Buchstab 递归传播后的有效乘子 <2.865。",
            MULTIPLIER_ATOM,
        ),
        row(
            INTERNAL_TAIL_ATOM,
            False,
            False,
            "若坚持完全自足路线，还必须内联证明 reciprocal-prime Mertens 尾段定理。",
            INTERNAL_TAIL_ATOM,
        ),
        row(
            STANDARD_IMPORT_ATOM,
            False,
            False,
            "标准 Rosser-Iwaniec beta-sieve 基本引理可外部替代本乘子证明。",
            STANDARD_IMPORT_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部短区间 rough-number 下界仍可绕开内部 beta-sieve 包。",
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
    """执行 B=3 边界变差乘子路由。"""
    previous = load_json(paths["previous"])
    budget = variation_budget(previous)
    faces = face_dictionary()
    rows = build_rows(previous, budget)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "BoundaryVariationReducedToSignedMultiplier"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""))
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""))
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""))
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_boundary_variation_multiplier_router",
        "status": "b3_boundary_variation_reduced_to_signed_multiplier_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "b3_boundary_variation_reduced": reduced,
        "b3_rosser_face_dictionary_closed": all(item["closed"] for item in faces),
        "b3_signed_delay_kernel_multiplier_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {VARIATION_ATOM: replacement_pair()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": MULTIPLIER_ATOM,
        "secondary_priority": INTERNAL_TAIL_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "variation_budget": budget,
        "face_dictionary": faces,
        "plain_conclusion": (
            "B=3 边界变差的结构部分已经压实：有限小阈值素数作为精确阶梯原子保留，"
            "B=3 ordering/cap/floor/Rosser gate face 字典闭合。真正剩余不是再找一个固定常数区间，"
            "而是证明全长度 Buchstab delay kernel 的有符号传播乘子小于 2.865；"
            "一旦该乘子纪律成立，Dusart 尾段 forcing 可被 1% f(s) 预算吸收。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    budget = result["variation_budget"]
    lines = [
        "# Prime Matrix B=3 边界变差乘子路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"b3_boundary_variation_reduced={fmt_bool(result['b3_boundary_variation_reduced'])}",
        f"b3_rosser_face_dictionary_closed={fmt_bool(result['b3_rosser_face_dictionary_closed'])}",
        f"b3_signed_delay_kernel_multiplier_proved={fmt_bool(result['b3_signed_delay_kernel_multiplier_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 预算方程",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| alpha | {budget['alpha']:.6f} |",
        f"| s=1/alpha | {budget['s']:.12f} |",
        f"| f(s) | {budget['linear_lower_sieve_f']:.12f} |",
        f"| 1% f(s) budget | {budget['one_percent_budget']:.12f} |",
        f"| Dusart tail error at x=10372 | {budget['dusart_tail_error_at_x_10372']:.12f} |",
        f"| required signed multiplier upper bound | {budget['required_signed_multiplier_upper_bound']:.12f} |",
        "",
        "也就是说，若有符号边界传播乘子 `K_B3` 满足",
        "",
        "```text",
        "K_B3 < 2.865",
        "```",
        "",
        "则 `K_B3 * 0.001506804667 < 0.004317176892 = 1% f(s)`，边界变差预算关闭。",
        "",
        "## 2. 替换",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 3. Face 字典",
        "",
        "| face | equation | count for length r | role | closed |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["face_dictionary"]:
        lines.append(
            "| {face} | `{equation}` | `{count}` | {role} | `{closed}` |".format(
                face=table_cell(item["face"]),
                equation=table_cell(item["equation"]),
                count=table_cell(item["count_for_length_r"]),
                role=table_cell(item["role"]),
                closed=fmt_bool(item["closed"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 最新输入基",
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
            "## 6. 下一步",
            "",
            f"直接攻 `{result['next_priority']}`。这是当前 B=3 内部线的真正乘子纪律终端。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
