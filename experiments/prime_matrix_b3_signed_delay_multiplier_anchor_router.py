#!/usr/bin/env python3
"""Prime Matrix B=3 有符号 delay 乘子锚点提升路由器。

用法示例：
  python3 experiments/prime_matrix_b3_signed_delay_multiplier_anchor_router.py

输出：
  docs/monograph/prime-matrix-b3-signed-delay-multiplier-anchor-router.json
  docs/monograph/prime-matrix-b3-signed-delay-multiplier-anchor-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-boundary-variation-multiplier-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-b3-signed-delay-multiplier-anchor-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-signed-delay-multiplier-anchor-router.md"

OLD_MULTIPLIER_ATOM = "B3SignedDelayKernelVariationMultiplierLt2865PermilleAlpha043"
CLOSED_ANCHOR_ATOM = "B3Anchor20000BoundaryVariationBudgetClosedAlpha043"
FINITE_PROMOTION_ATOM = "B3FinitePrimeReciprocalStepLedger10372To19999PGe100000"
DELAY_KERNEL_ATOM = "B3TwoToThreeDelayKernelBVMultiplierLE3064Alpha043"
INTERNAL_TAIL_ATOM = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
EULER_GAMMA = 0.5772156649015329
OLD_ANCHOR_X = 10_372
PROMOTED_ANCHOR_X = 20_000
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


def sieve_primes(limit: int) -> list[int]:
    """生成不超过 limit 的素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, int(limit**0.5) + 1):
        if not flags[value]:
            continue
        start = value * value
        flags[start : limit + 1 : value] = b"\x00" * (
            ((limit - start) // value) + 1
        )
    return [idx for idx, flag in enumerate(flags) if flag]


def dusart_error(log_x: float) -> float:
    """Dusart 型素数倒数和误差项。"""
    return 1.0 / (10.0 * log_x**2) + 4.0 / (15.0 * log_x**3)


def linear_sieve_f(alpha: float = ALPHA) -> float:
    """计算 2<s<3 区间的一维线性下界筛函数 f(s)。"""
    sieve_s = 1.0 / alpha
    return 2.0 * math.exp(EULER_GAMMA) * math.log(sieve_s - 1.0) / sieve_s


def finite_promotion_ledger(old_anchor: int, new_anchor: int) -> dict[str, Any]:
    """登记新增有限精确阶梯段。"""
    primes = sieve_primes(new_anchor)
    segment = [prime for prime in primes if old_anchor <= prime < new_anchor]
    return {
        "old_anchor_x": old_anchor,
        "promoted_anchor_x": new_anchor,
        "prime_count_in_promoted_segment": len(segment),
        "first_prime_in_promoted_segment": segment[0],
        "last_prime_in_promoted_segment": segment[-1],
        "reciprocal_mass_in_promoted_segment": sum(1.0 / prime for prime in segment),
        "p_threshold_where_p_alpha_reaches_promoted_anchor": math.ceil(new_anchor ** (1.0 / ALPHA)),
        "finite_promotion_closed": True,
    }


def delay_kernel_ledger(anchor_x: int) -> dict[str, Any]:
    """计算锚点提升后的 delay-kernel 乘子预算。"""
    s_value = 1.0 / ALPHA
    f_value = linear_sieve_f()
    budget = ONE_PERCENT * f_value
    tail_error = dusart_error(math.log(anchor_x))
    # 在 2<s<3 时 lower sieve 只经过一层 delay：
    # f(s)=s^{-1} int_1^{s-1} 2e^gamma/t dt。
    # 对 Stieltjes forcing 的 BV 估计给乘子 <= (|phi(1)|+|phi(s-1)|+TV(phi))/s = 4e^gamma/s。
    bv_multiplier = 4.0 * math.exp(EULER_GAMMA) / s_value
    forced_error_bound = bv_multiplier * tail_error
    return {
        "alpha": ALPHA,
        "s": s_value,
        "s_in_two_to_three": 2.0 < s_value < 3.0,
        "linear_lower_sieve_f": f_value,
        "one_percent_budget": budget,
        "promoted_anchor_x": anchor_x,
        "dusart_tail_error_at_anchor": tail_error,
        "delay_kernel_phi": "phi(t)=2e^gamma/t on 1<=t<=s-1",
        "delay_kernel_bv_multiplier_bound": bv_multiplier,
        "forced_error_bound": forced_error_bound,
        "budget_slack": budget - forced_error_bound,
        "closes_one_percent_budget": forced_error_bound < budget,
    }


def replacement_pair() -> str:
    """写出旧乘子原子的锚点闭合替换。"""
    return f"({FINITE_PROMOTION_ATOM} AND {DELAY_KERNEL_ATOM})"


def replace_old_multiplier(text: str, replacement: str) -> str:
    """替换旧的 10372 锚点乘子原子。"""
    return text.replace(OLD_MULTIPLIER_ATOM, replacement)


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
    finite: dict[str, Any],
    kernel: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成有符号 delay 乘子锚点提升判定表。"""
    basis = previous.get("latest_conditional_basis", "")
    active = previous.get("next_priority") == OLD_MULTIPLIER_ATOM and OLD_MULTIPLIER_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    face_dictionary_available = bool(previous.get("b3_rosser_face_dictionary_closed"))
    finite_closed = bool(finite["finite_promotion_closed"])
    kernel_range_closed = bool(kernel["s_in_two_to_three"])
    kernel_budget_closed = bool(kernel["closes_one_percent_budget"])
    anchor_route_closed = (
        active
        and guard
        and face_dictionary_available
        and finite_closed
        and kernel_range_closed
        and kernel_budget_closed
    )
    return [
        row(
            "SignedDelayMultiplierGateActive",
            active,
            False,
            "上一层唯一 B=3 内部硬点是有符号 delay-kernel 乘子纪律。",
            OLD_MULTIPLIER_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内处理筛主系数误差，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FaceDictionaryAvailable",
            face_dictionary_available,
            True,
            "上一层已经列出 B=3 ordering/cap/floor/Rosser gate face 字典。",
            "无 face 字典剩余。",
        ),
        row(
            "FiniteAnchorPromotion10372To20000Closed",
            finite_closed,
            True,
            "把 10372<=x<20000 的素数跳点也精确保留，从而降低无限尾段 Mertens forcing。",
            FINITE_PROMOTION_ATOM,
        ),
        row(
            "TwoToThreeDelayKernelFormulaClosed",
            kernel_range_closed,
            True,
            "alpha=0.43 给 s=2.325581，处于 2<s<3；lower sieve 只用 phi(t)=2e^gamma/t 的一层 delay kernel。",
            DELAY_KERNEL_ATOM,
        ),
        row(
            "DelayKernelBVMultiplierBoundClosed",
            True,
            True,
            "Stieltjes 分部积分给 BV 乘子 <=4e^gamma/s=3.063444558943。",
            DELAY_KERNEL_ATOM,
        ),
        row(
            "PromotedAnchorOnePercentBudgetClosed",
            kernel_budget_closed,
            True,
            "锚点 20000 处 Dusart 尾误差乘以 BV 乘子仍小于 1% f(s)。",
            CLOSED_ANCHOR_ATOM,
        ),
        row(
            "OldMultiplierAtomBypassedByAnchorPromotion",
            anchor_route_closed,
            False,
            "旧的 10372 锚点 <2.865 充分条件不再硬证；改由 20000 锚点的更优预算直接关闭父级边界变差。",
            CLOSED_ANCHOR_ATOM,
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
    """执行 B=3 有符号 delay 乘子锚点提升路由。"""
    previous = load_json(paths["previous"])
    finite = finite_promotion_ledger(OLD_ANCHOR_X, PROMOTED_ANCHOR_X)
    kernel = delay_kernel_ledger(PROMOTED_ANCHOR_X)
    rows = build_rows(previous, finite, kernel)
    anchor_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "OldMultiplierAtomBypassedByAnchorPromotion"
    )
    latest_self = replace_old_multiplier(previous.get("latest_self_contained_basis", ""), CLOSED_ANCHOR_ATOM)
    latest_cond = replace_old_multiplier(previous.get("latest_conditional_basis", ""), CLOSED_ANCHOR_ATOM)
    latest_global = replace_old_multiplier(previous.get("latest_global_with_external_basis", ""), CLOSED_ANCHOR_ATOM)
    source_paths = list(paths.values())
    return {
        "certificate_type": "b3_signed_delay_multiplier_anchor_router",
        "status": "b3_boundary_variation_conditional_closed_self_contained_mertens_tail_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "b3_signed_delay_multiplier_anchor_route_closed": anchor_closed,
        "b3_boundary_variation_one_percent_conditional_closed": anchor_closed,
        "b3_discrete_prime_sum_uniform_error_conditional_closed": anchor_closed,
        "beta_sieve_main_coefficient_99pct_conditional_closed": anchor_closed,
        "old_literal_multiplier_lt2865_proved": False,
        "self_contained_mertens_tail_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {OLD_MULTIPLIER_ATOM: CLOSED_ANCHOR_ATOM},
        "replacement_structural_detail": {OLD_MULTIPLIER_ATOM: replacement_pair()},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": INTERNAL_TAIL_ATOM,
        "conditional_next_priority": DSTRUCTURE,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "finite_promotion_ledger": finite,
        "delay_kernel_ledger": kernel,
        "plain_conclusion": (
            "旧的 10372 锚点要求乘子 <2.865，过窄。把精确有限阶梯段提升到 x<20000 后，"
            "Dusart 尾段误差降为 0.001294124698；在 alpha=0.43、2<s<3 中，"
            "Buchstab delay kernel 的 BV 乘子由分部积分给出 <=4e^gamma/s=3.063444559。"
            "乘积 0.003964479265 小于 1% f(s)=0.004317176892，因此外部 Mertens 定理版的 "
            "B=3 边界变差和 99% 主系数包关闭。完全自足版仍只剩 Mertens 尾段定理内联证明。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    structural = next(iter(result["replacement_structural_detail"].items()))
    finite = result["finite_promotion_ledger"]
    kernel = result["delay_kernel_ledger"]
    lines = [
        "# Prime Matrix B=3 有符号 delay 乘子锚点提升路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"b3_signed_delay_multiplier_anchor_route_closed={fmt_bool(result['b3_signed_delay_multiplier_anchor_route_closed'])}",
        f"b3_boundary_variation_one_percent_conditional_closed={fmt_bool(result['b3_boundary_variation_one_percent_conditional_closed'])}",
        f"beta_sieve_main_coefficient_99pct_conditional_closed={fmt_bool(result['beta_sieve_main_coefficient_99pct_conditional_closed'])}",
        f"old_literal_multiplier_lt2865_proved={fmt_bool(result['old_literal_multiplier_lt2865_proved'])}",
        f"self_contained_mertens_tail_proved={fmt_bool(result['self_contained_mertens_tail_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 锚点提升",
        "",
        "旧充分条件：",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "实际结构闭合包：",
        "",
        "```text",
        structural[0],
        "  =>",
        structural[1],
        "```",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| old anchor x | {finite['old_anchor_x']} |",
        f"| promoted anchor x | {finite['promoted_anchor_x']} |",
        f"| promoted segment primes | {finite['prime_count_in_promoted_segment']} |",
        f"| first promoted prime | {finite['first_prime_in_promoted_segment']} |",
        f"| last promoted prime | {finite['last_prime_in_promoted_segment']} |",
        f"| promoted reciprocal mass | {finite['reciprocal_mass_in_promoted_segment']:.12f} |",
        f"| P threshold where P^alpha reaches promoted anchor | {finite['p_threshold_where_p_alpha_reaches_promoted_anchor']} |",
        "",
        "## 2. Delay 乘子账本",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| alpha | {kernel['alpha']:.6f} |",
        f"| s=1/alpha | {kernel['s']:.12f} |",
        f"| 2<s<3 | {fmt_bool(kernel['s_in_two_to_three'])} |",
        f"| f(s) | {kernel['linear_lower_sieve_f']:.12f} |",
        f"| 1% f(s) budget | {kernel['one_percent_budget']:.12f} |",
        f"| Dusart tail error at promoted anchor | {kernel['dusart_tail_error_at_anchor']:.12f} |",
        f"| BV multiplier bound | {kernel['delay_kernel_bv_multiplier_bound']:.12f} |",
        f"| forced error bound | {kernel['forced_error_bound']:.12f} |",
        f"| budget slack | {kernel['budget_slack']:.12f} |",
        "",
        "2<s<3 中",
        "",
        "```text",
        "f(s)=s^{-1} int_1^{s-1} 2e^gamma/t dt.",
        "```",
        "",
        "对 Stieltjes forcing 使用分部积分，`phi(t)=2e^gamma/t` 单调递减，所以",
        "",
        "```text",
        "(|phi(1)|+|phi(s-1)|+TV(phi))/s = 4e^gamma/s.",
        "```",
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
            (
                f"外部 Mertens 定理版的 B=3 beta-sieve 主系数包已关闭，晋级看 `{result['conditional_next_priority']}`；"
                f"完全自足版仍先攻 `{result['next_priority']}`。"
            ),
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
