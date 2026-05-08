#!/usr/bin/env python3
"""Prime Matrix beta-sieve 自足前沿拆分路由器。

用法示例：
  python3 experiments/prime_matrix_beta_sieve_self_contained_frontier_router.py

输出：
  docs/monograph/prime-matrix-beta-sieve-self-contained-frontier-router.json
  docs/monograph/prime-matrix-beta-sieve-self-contained-frontier-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-nearsquare-canonical-terminal-absorption-router.json"
DEFAULT_LEDGER = DOCS / "prime-matrix-explicit-rosser-lower-weight-ledger-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-beta-sieve-self-contained-frontier-router.json"
DEFAULT_MD = DOCS / "prime-matrix-beta-sieve-self-contained-frontier-router.md"

SELF_BETA_ATOM = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
MAIN_ERROR_ATOM = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
LOWER_RECURSION_ATOM = "BetaSieveLowerWeightRecursiveConstructionLedger"
DOMINANCE_ATOM = "BetaSieveLowerBoundDominanceProof"
MAIN_99_ATOM = "BetaSieveMainCoefficientExplicit99PercentPGe100000"
STANDARD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
TAIL_START = 100_000
TARGET_S = 401
SAWTOOTH_LOSS_FRACTION = 0.90
CONSERVATIVE_MAIN_FRACTION = 0.99


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


def replace_pair(text: str, new_pair: str) -> str:
    """替换 beta-sieve 双原子。"""
    old_pair = f"({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM})"
    return text.replace(old_pair, new_pair)


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


def fallback_constant_ledger() -> dict[str, Any]:
    """在旧账本缺失时生成最小常数账本。"""
    euler_gamma = 0.5772156649015329
    sieve_s = 1.0 / ALPHA
    f_value = 2.0 * math.exp(euler_gamma) * math.log(sieve_s - 1.0) / sieve_s
    v_model = math.exp(-euler_gamma) / (ALPHA * math.log(TAIL_START))
    model_main = TAIL_START * v_model * f_value
    target_ratio = TARGET_S / model_main
    required_fraction = SAWTOOTH_LOSS_FRACTION + target_ratio
    return {
        "tail_start": TAIL_START,
        "alpha": ALPHA,
        "level_D_choice": "D=P",
        "s_logD_over_logz": sieve_s,
        "linear_sieve_f": f_value,
        "model_main_at_tail_start": model_main,
        "target_s": TARGET_S,
        "target_ratio_of_model_main": target_ratio,
        "sawtooth_loss_fraction_budget": SAWTOOTH_LOSS_FRACTION,
        "minimum_main_fraction_after_90pct_sawtooth_loss": required_fraction,
        "conservative_main_fraction": CONSERVATIVE_MAIN_FRACTION,
        "conservative_allowed_normalized_error_1pct_f": 0.01 * f_value,
    }


def constants_from_ledger(ledger: dict[str, Any]) -> dict[str, Any]:
    """读取上一层显式权重账本中的参数常数。"""
    constants = dict(fallback_constant_ledger())
    constants.update(ledger.get("constants", {}))
    constants["conservative_surplus_fraction"] = (
        constants["conservative_main_fraction"]
        - constants["minimum_main_fraction_after_90pct_sawtooth_loss"]
    )
    constants["conservative_surplus_count_at_tail_start"] = (
        constants["conservative_surplus_fraction"] * constants["model_main_at_tail_start"]
    )
    return constants


def self_contained_pair() -> str:
    """写出新的自足 beta-sieve 三原子包。"""
    return f"({LOWER_RECURSION_ATOM} AND {DOMINANCE_ATOM} AND {MAIN_99_ATOM})"


def conditional_pair() -> str:
    """写出允许标准定理导入的 beta-sieve 包。"""
    return f"({self_contained_pair()} OR {STANDARD_IMPORT_ATOM})"


def build_rows(previous: dict[str, Any], ledger: dict[str, Any], constants: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 beta-sieve 自足前沿判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    cond_basis = previous.get("latest_conditional_basis", "")
    active = (
        previous.get("next_priority") == SELF_BETA_ATOM
        and previous.get("secondary_priority") == MAIN_ERROR_ATOM
        and SELF_BETA_ATOM in self_basis
        and MAIN_ERROR_ATOM in self_basis
    )
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    support_pinned = (
        bool(ledger.get("explicit_rosser_iwaniec_lower_weight_ledger_compressed"))
        and constants["level_D_choice"] == "D=P"
        and constants["alpha"] == ALPHA
        and constants["s_logD_over_logz"] > 2.0
    )
    capacity_pinned = (
        constants["minimum_main_fraction_after_90pct_sawtooth_loss"] < CONSERVATIVE_MAIN_FRACTION
        and constants["conservative_surplus_count_at_tail_start"] > 0.0
    )
    standard_located = STANDARD_IMPORT_ATOM in cond_basis or bool(
        ledger.get("standard_beta_sieve_source_located")
    )
    split_closed = active and guard and support_pinned and capacity_pinned
    return [
        row(
            "BetaSieveFrontierGateActive",
            active,
            False,
            "最新 canonical 自足输入基正卡在 beta-sieve 自足构造与 99% 主系数双原子。",
            f"{SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM}",
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内整理尾段筛输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "SupportLevelAndSAlreadyPinned",
            support_pinned,
            True,
            "上一层已固定 D=P、z=P^0.43、s=1/0.43，且权重支撑只允许 squarefree d<=P、p|d=>p<z。",
            "无新的参数自由度。",
        ),
        row(
            "CapacityMultiplierDisciplinePreserved",
            capacity_pinned,
            True,
            "90% sawtooth 损失预算要求主系数至少保留 0.981899...；99% 目标在 P=100000 仍有正余量。",
            f"{MAIN_99_ATOM}",
        ),
        row(
            "SelfContainedAppendixSplitToConstructionAndDominance",
            split_closed,
            False,
            "自足 beta-sieve 附录不再是单一黑箱；它必须拆成 finite recursive lower weights 与 lower-bound 支配证明。",
            f"{LOWER_RECURSION_ATOM} AND {DOMINANCE_ATOM}",
        ),
        row(
            "MainCoefficientAtomRenormalizedToOnePercent",
            split_closed,
            False,
            "旧 99% 主系数输入被重写为一个明确的 1% 归一误差账本。",
            MAIN_99_ATOM,
        ),
        row(
            "StandardBetaSieveImportBoundaryMarked",
            standard_located,
            False,
            "标准 Rosser-Iwaniec beta-sieve 定理可作为 conditional 导入，但不能算作自足闭合。",
            STANDARD_IMPORT_ATOM,
        ),
        row(
            LOWER_RECURSION_ATOM,
            False,
            False,
            "需要逐行给出 beta-sieve lower weights 的有限递归、截断、符号与支撑。",
            LOWER_RECURSION_ATOM,
        ),
        row(
            DOMINANCE_ATOM,
            False,
            False,
            "需要证明对任意整数 n 有 sum_{d|(n,P(z))} lambda_d^- <= 1_{(n,P(z))=1}。",
            DOMINANCE_ATOM,
        ),
        row(
            MAIN_99_ATOM,
            False,
            False,
            "需要把离散权重主系数与连续 f(1/0.43) 的误差显式压到 1% 以内，且 P>=100000 全尾段有效。",
            MAIN_99_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部短区间 rough-number 下界仍可绕开整个内部 beta-sieve 包。",
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
    """执行 beta-sieve 自足前沿拆分路由。"""
    previous = load_json(paths["previous"])
    ledger = load_json(paths["ledger"])
    constants = constants_from_ledger(ledger)
    rows = build_rows(previous, ledger, constants)
    split_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "SelfContainedAppendixSplitToConstructionAndDominance"
    )

    latest_self = replace_pair(previous.get("latest_self_contained_basis", ""), self_contained_pair())
    latest_cond = replace_pair(previous.get("latest_conditional_basis", ""), self_contained_pair())
    latest_global = replace_pair(
        previous.get("latest_global_with_external_basis", ""),
        self_contained_pair(),
    )
    source_paths = list(paths.values())

    return {
        "certificate_type": "beta_sieve_self_contained_frontier_router",
        "status": "beta_sieve_frontier_split_to_three_self_contained_atoms_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "beta_sieve_frontier_split_closed": split_closed,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained_pair": {
            f"({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM})": self_contained_pair()
        },
        "replacement_with_standard_import": {
            f"({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM})": conditional_pair()
        },
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": LOWER_RECURSION_ATOM,
        "secondary_priority": DOMINANCE_ATOM,
        "tertiary_priority": MAIN_99_ATOM,
        "conditional_beta_import_priority": STANDARD_IMPORT_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "constants": constants,
        "self_contained_subatoms": [
            LOWER_RECURSION_ATOM,
            DOMINANCE_ATOM,
            MAIN_99_ATOM,
        ],
        "construction_contract": [
            "定义有限递归 lower weights lambda_d^-，并证明 lambda_1^-=1、lambda_d^- in {-1,0,1}。",
            "证明 lambda_d^- 只支撑在 squarefree d<=P 且所有素因子 <P^0.43 的 d 上。",
            "递归必须完全有限化；不能直接引用标准 beta-sieve 定理作为自足证明。",
        ],
        "dominance_contract": [
            "对任意整数 n，按 n 的小素因子集合做有限归纳。",
            "证明 lower weights 的 alternating 递归给出筛剩余指示函数的下界。",
            "该证明只依赖递归结构，不依赖真实零行缺席或统计实验。",
        ],
        "main_coefficient_contract": [
            "把 W^-(P)=sum lambda_d^-/d 与 V(z)f(s) 比较。",
            "在 P>=100000、s=1/0.43 下证明 W^-(P)>=0.99 V(z)f(s)。",
            "等价归一误差目标为 <=0.004317176892290826。",
        ],
        "plain_conclusion": (
            "本步把 beta-sieve 双输入拆成三枚可审查原子。"
            "参数、支撑与容量乘子已经由上一层账本固定：D=P、z=P^0.43、s=2.325581，"
            "且 99% 主系数足以覆盖 90% sawtooth 损失后的 401 目标。"
            "真正自足剩余现在是：有限递归 lower weights 构造、lower-bound 支配证明、"
            "以及 P>=100000 的 1% 显式主系数误差。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    constants = result["constants"]
    self_replacement = next(iter(result["replacement_self_contained_pair"].items()))
    conditional_replacement = next(iter(result["replacement_with_standard_import"].items()))
    lines = [
        "# Prime Matrix beta-sieve 自足前沿拆分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"beta_sieve_frontier_split_closed={fmt_bool(result['beta_sieve_frontier_split_closed'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"standard_beta_sieve_import_accepted={fmt_bool(result['standard_beta_sieve_import_accepted'])}",
        (
            "external_short_interval_rough_lower_bound_accepted="
            f"{fmt_bool(result['external_short_interval_rough_lower_bound_accepted'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 容量账本",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| alpha | {constants['alpha']:.6f} |",
        f"| D | {constants['level_D_choice']} |",
        f"| s=logD/logz | {constants['s_logD_over_logz']:.6f} |",
        f"| linear sieve f(s) | {constants['linear_sieve_f']:.12f} |",
        f"| model main at P=100000 | {constants['model_main_at_tail_start']:.6f} |",
        f"| target S | {constants['target_s']} |",
        f"| target/main | {constants['target_ratio_of_model_main']:.6f} |",
        f"| sawtooth loss budget | {constants['sawtooth_loss_fraction_budget']:.6f} main |",
        (
            "| minimum main fraction after 90% loss | "
            f"{constants['minimum_main_fraction_after_90pct_sawtooth_loss']:.6f} |"
        ),
        f"| conservative main fraction | {constants['conservative_main_fraction']:.6f} |",
        f"| conservative surplus fraction | {constants['conservative_surplus_fraction']:.6f} |",
        (
            "| conservative surplus count at P=100000 | "
            f"{constants['conservative_surplus_count_at_tail_start']:.6f} |"
        ),
        (
            "| normalized 1% error target | "
            f"{constants['conservative_allowed_normalized_error_1pct_f']:.12f} |"
        ),
        "",
        "## 2. 拆分律",
        "",
        "完全自足路线：",
        "",
        "```text",
        self_replacement[0],
        "  =>",
        self_replacement[1],
        "```",
        "",
        "允许标准定理导入的 conditional 路线：",
        "",
        "```text",
        conditional_replacement[0],
        "  =>",
        conditional_replacement[1],
        "```",
        "",
        "## 3. 自足证明合同",
        "",
        "构造合同：",
        "",
        *[f"- {item}" for item in result["construction_contract"]],
        "",
        "支配合同：",
        "",
        *[f"- {item}" for item in result["dominance_contract"]],
        "",
        "主系数合同：",
        "",
        *[f"- {item}" for item in result["main_coefficient_contract"]],
        "",
        "## 4. 判定表",
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
            (
                f"直接攻 `{result['next_priority']}`；随后验收 `{result['secondary_priority']}` "
                f"与 `{result['tertiary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "ledger": args.ledger,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
