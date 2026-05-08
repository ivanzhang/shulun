#!/usr/bin/env python3
"""Prime Matrix 显式 Rosser-Iwaniec 下界权重账本路由器。

用法示例：
  python3 experiments/prime_matrix_explicit_rosser_lower_weight_ledger_router.py

输出：
  docs/monograph/prime-matrix-explicit-rosser-lower-weight-ledger-router.json
  docs/monograph/prime-matrix-explicit-rosser-lower-weight-ledger-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-rosser-weight-floor-ledger-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-explicit-rosser-lower-weight-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-explicit-rosser-lower-weight-ledger-router.md"

OLD_ATOM = "ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000"
SAWTOOTH_ATOM = "ExactResidueWeightedFloorSawtoothTenPercentBound"
SELF_BETA_ATOM = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
MAIN_ERROR_ATOM = "BetaSieveMainCoefficientTenPercentExplicitErrorAlpha043PGe100000"
STD_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ALPHA = 0.43
TAIL_START = 100_000
TARGET_S = 401
TEN_PERCENT = 0.10
EULER_GAMMA = 0.5772156649015329


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
    """替换输入基中的旧原子。"""
    return text.replace(old, new)


def linear_sieve_f(sieve_s: float) -> float:
    """一维线性下界筛在 2<=s<=3 的 f(s)。"""
    return 2.0 * math.exp(EULER_GAMMA) * math.log(sieve_s - 1.0) / sieve_s


def constant_ledger(p: int) -> dict[str, Any]:
    """生成 alpha=0.43, D=P 的参数和常数账本。"""
    z = p ** ALPHA
    floor_z = math.floor(z)
    sieve_s = math.log(p) / math.log(z)
    floor_s = math.log(p) / math.log(floor_z)
    f_value = linear_sieve_f(sieve_s)
    v_model = math.exp(-EULER_GAMMA) / (ALPHA * math.log(p))
    model_main = p * v_model * f_value
    ten_percent_main = TEN_PERCENT * model_main
    required_normalized_coefficient = TEN_PERCENT * f_value
    allowed_normalized_error = (1.0 - TEN_PERCENT) * f_value
    return {
        "tail_start": p,
        "alpha": ALPHA,
        "level_D_choice": "D=P",
        "z_at_tail_start": z,
        "floor_z_at_tail_start": floor_z,
        "s_logD_over_logz": sieve_s,
        "s_with_floor_z": floor_s,
        "linear_sieve_f": f_value,
        "v_model": v_model,
        "model_main_at_tail_start": model_main,
        "ten_percent_main_at_tail_start": ten_percent_main,
        "target_s": TARGET_S,
        "target_ratio_of_model_main": TARGET_S / model_main,
        "required_normalized_coefficient_10pct_f": required_normalized_coefficient,
        "allowed_normalized_error_90pct_f": allowed_normalized_error,
        "tail_main_monotone_after_e": True,
        "ten_percent_main_exceeds_target": ten_percent_main > TARGET_S,
        "s_in_linear_lower_sieve_range_2_to_3": 2.0 < sieve_s < 3.0,
        "floor_z_preserves_s_gt_2": floor_s > 2.0,
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


def build_rows(previous: dict[str, Any], constants: dict[str, Any]) -> list[dict[str, Any]]:
    """生成显式权重账本判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    parameter_closed = (
        constants["s_in_linear_lower_sieve_range_2_to_3"]
        and constants["floor_z_preserves_s_gt_2"]
        and constants["ten_percent_main_exceeds_target"]
    )
    compression_closed = active and guard and parameter_closed
    return [
        row(
            "ExplicitWeightGateActive",
            active,
            False,
            "最新最窄内部点是固定 Rosser-Iwaniec lower weights、level、s 与主项常数。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设早期零行反例链条内的尾段筛输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "LevelChoiceDEqualsPAlpha043Closed",
            parameter_closed,
            True,
            "取 D=P、z=P^0.43，则 s=logD/logz=1/0.43 位于线性下界筛 2<s<3 区间；floor(z) 后仍有 s>2。",
            "无剩余。",
        ),
        row(
            "TenPercentMainCoefficientAlgebraClosed",
            constants["ten_percent_main_exceeds_target"],
            True,
            "P=100000 处 10% 线性筛模型主项已超过 401，且 P/logP 在尾段递增。",
            "无剩余。",
        ),
        row(
            "WeightLedgerCompressedToBetaSieveBoundary",
            compression_closed,
            False,
            "显式权重原子被压成：自足 beta-sieve 构造与主系数误差，或接受标准 Rosser-Iwaniec beta-sieve 定理。",
            f"({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM}) OR {STD_IMPORT_ATOM}",
        ),
        row(
            "StandardBetaSieveSourceLocated",
            True,
            False,
            "标准外部来源可登记为 Friedlander-Iwaniec beta-sieve/Rosser-Iwaniec weights；接受它会关闭权重账本，但不是自足证明。",
            STD_IMPORT_ATOM,
        ),
        row(
            SELF_BETA_ATOM,
            False,
            False,
            "若坚持完全自足，需要逐行给出 lower weights 的构造，并证明其 lower-bound 支配关系。",
            SELF_BETA_ATOM,
        ),
        row(
            MAIN_ERROR_ATOM,
            False,
            False,
            "还需显式证明主系数 normalized error 不超过 0.9 f(s)，等价于 W^->=0.1 V(z)f(s)。",
            MAIN_ERROR_ATOM,
        ),
        row(
            SAWTOOTH_ATOM,
            False,
            False,
            "即使权重包被接受，仍必须证明精确 CRT 残基 floor 余项的加权负损失不会吞掉 10% 主项。",
            SAWTOOTH_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部短区间 rough-number 下界仍可绕开内部 beta-sieve 权重与 sawtooth 两步。",
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
    """执行显式 Rosser-Iwaniec 下界权重账本路由。"""
    previous = load_json(paths["previous"])
    constants = constant_ledger(TAIL_START)
    rows = build_rows(previous, constants)
    compressed = next(bool(item["closed"]) for item in rows if item["gate"] == "WeightLedgerCompressedToBetaSieveBoundary")

    self_replacement = f"({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM})"
    import_replacement = f"({self_replacement} OR {STD_IMPORT_ATOM})"
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, self_replacement)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, import_replacement)
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), OLD_ATOM, import_replacement)

    source_paths = list(paths.values())
    return {
        "certificate_type": "explicit_rosser_lower_weight_ledger_router",
        "status": "explicit_rosser_weight_ledger_compressed_to_beta_sieve_boundary_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "explicit_rosser_iwaniec_lower_weight_ledger_compressed": compressed,
        "explicit_rosser_iwaniec_lower_weight_ledger_proved": False,
        "standard_beta_sieve_source_located": True,
        "standard_beta_sieve_import_accepted": False,
        "self_contained_beta_sieve_appendix_proved": False,
        "main_coefficient_ten_percent_error_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: self_replacement},
        "replacement_with_standard_import": {OLD_ATOM: import_replacement},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": SELF_BETA_ATOM,
        "secondary_priority": MAIN_ERROR_ATOM,
        "after_import_next_priority": SAWTOOTH_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "constants": constants,
        "required_weight_properties": [
            "lambda_1^-=1; lambda_d^- in {-1,0,1}",
            "lambda_d^-=0 unless d is squarefree, d<=D=P, and every prime divisor of d is <z=P^0.43",
            "sum_{d|(n,P(z))} lambda_d^- <= 1_{(n,P(z))=1} for every integer n",
            "W^-(P)=sum_{d|P(z)} lambda_d^-/d >= 0.1 V(z) f(1/0.43) for P>=100000",
        ],
        "standard_sources": [
            {
                "label": "Friedlander-Iwaniec Opera de Cribro",
                "use": "beta-sieve / Rosser-Iwaniec weights standard theorem source",
                "url": "https://bookstore.ams.org/coll-57",
            },
            {
                "label": "local bibliography",
                "use": "project-level external theorem index",
                "path": "docs/bibliography.md",
            },
        ],
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把显式 Rosser-Iwaniec 下界权重输入继续压窄。"
            "参数层已闭合：D=P、z=P^0.43 给 s=1/0.43=2.325581，"
            f"f(s)={constants['linear_sieve_f']:.12f}，P=100000 处 10% 模型主项 "
            f"{constants['ten_percent_main_at_tail_start']:.6f}>401。"
            "真正剩余不是参数选择，而是：若走自足路线，必须证明 beta-sieve lower weights 构造及其主系数误差；"
            "若接受标准 Rosser-Iwaniec beta-sieve 定理，则权重账本可外部关闭，下一硬点转为精确加权 floor/sawtooth 余项。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    constants = result["constants"]
    self_replacement = next(iter(result["replacement_self_contained"].items()))
    import_replacement = next(iter(result["replacement_with_standard_import"].items()))
    lines = [
        "# Prime Matrix 显式 Rosser-Iwaniec 下界权重账本路由器",
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
            "explicit_rosser_iwaniec_lower_weight_ledger_compressed="
            f"{fmt_bool(result['explicit_rosser_iwaniec_lower_weight_ledger_compressed'])}"
        ),
        (
            "explicit_rosser_iwaniec_lower_weight_ledger_proved="
            f"{fmt_bool(result['explicit_rosser_iwaniec_lower_weight_ledger_proved'])}"
        ),
        f"standard_beta_sieve_import_accepted={fmt_bool(result['standard_beta_sieve_import_accepted'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
        f"main_coefficient_ten_percent_error_proved={fmt_bool(result['main_coefficient_ten_percent_error_proved'])}",
        (
            "exact_residue_weighted_floor_sawtooth_bound_proved="
            f"{fmt_bool(result['exact_residue_weighted_floor_sawtooth_bound_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 参数账本",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| alpha | {constants['alpha']:.6f} |",
        f"| D | {constants['level_D_choice']} |",
        f"| z at P=100000 | {constants['z_at_tail_start']:.6f} |",
        f"| floor(z) at P=100000 | {constants['floor_z_at_tail_start']} |",
        f"| s=logD/logz | {constants['s_logD_over_logz']:.6f} |",
        f"| s with floor(z) | {constants['s_with_floor_z']:.6f} |",
        f"| linear sieve f(s) | {constants['linear_sieve_f']:.12f} |",
        f"| model main at P=100000 | {constants['model_main_at_tail_start']:.6f} |",
        f"| 10% model main | {constants['ten_percent_main_at_tail_start']:.6f} |",
        f"| target S | {constants['target_s']} |",
        f"| target/main | {constants['target_ratio_of_model_main']:.6f} |",
        f"| required coefficient 0.1 f(s) | {constants['required_normalized_coefficient_10pct_f']:.12f} |",
        f"| allowed normalized error 0.9 f(s) | {constants['allowed_normalized_error_90pct_f']:.12f} |",
        "",
        "## 2. 权重对象",
        "",
        "所需 lower weights 只需满足以下弱接口：",
        "",
        "```text",
        *result["required_weight_properties"],
        "```",
        "",
        "这比完整最优线性筛常数弱：这里只要求主系数至少达到标准模型的 10%。",
        "",
        "## 3. 拆分律",
        "",
        "自足路线：",
        "",
        "```text",
        self_replacement[0],
        "  =>",
        self_replacement[1],
        "```",
        "",
        "允许标准 beta-sieve 定理导入的路线：",
        "",
        "```text",
        import_replacement[0],
        "  =>",
        import_replacement[1],
        "```",
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
            "## 6. 来源边界",
            "",
            "- 标准外部来源：Friedlander-Iwaniec, *Opera de Cribro*, AMS Colloquium Publications 57，beta-sieve/Rosser-Iwaniec weights。",
            "- 本路由尚未接受该外部输入为自足证明；若接受它，下一步直接转入 `ExactResidueWeightedFloorSawtoothTenPercentBound`。",
            "",
            "## 7. 下一步",
            "",
            (
                f"自足路线先攻 `{result['next_priority']}`，随后攻 `{result['secondary_priority']}`。"
                f"若允许标准 beta-sieve 定理导入，则权重账本让位给 `{result['after_import_next_priority']}`。"
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
