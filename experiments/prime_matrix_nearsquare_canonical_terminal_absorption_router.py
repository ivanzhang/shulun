#!/usr/bin/env python3
"""Prime Matrix 近平方 canonical 终端吸收路由器。

用法示例：
  python3 experiments/prime_matrix_nearsquare_canonical_terminal_absorption_router.py

输出：
  docs/monograph/prime-matrix-nearsquare-canonical-terminal-absorption-router.json
  docs/monograph/prime-matrix-nearsquare-canonical-terminal-absorption-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-nearsquare-strip-terminal-admission-router.json"
DEFAULT_PROMOTION = DOCS / "prime-matrix-current-terminal-promotion-reconciliation-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-nearsquare-canonical-terminal-absorption-router.json"
DEFAULT_MD = DOCS / "prime-matrix-nearsquare-canonical-terminal-absorption-router.md"

TERMINAL_ATOM = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
CANONICAL_CLOSED_ATOM = "NoFurtherCanonicalSourceTerminalPromotionGap"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
SELF_BETA_ATOM = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
MAIN_ERROR_ATOM = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
STANDARD_BETA_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_DISPERSION_ATOM = "ExternalWellFactorableSawtoothDispersionBoundAlpha043"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
C_DEP_ATOM = "CDependentResidueWeightSpectralCancellationInput"
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


def self_contained_basis() -> str:
    """写出吸收后的 canonical 自足输入基。"""
    return (
        f"{CANONICAL_CLOSED_ATOM} AND ((({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM}) "
        f"OR {EXTERNAL_ROUGH_ATOM})) AND {DSTRUCTURE}"
    )


def conditional_basis() -> str:
    """写出吸收后的 conditional 输入基。"""
    return (
        f"(({CANONICAL_CLOSED_ATOM} AND ((({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM}) "
        f"OR {STANDARD_BETA_ATOM} OR {EXTERNAL_ROUGH_ATOM})) OR {C_DEP_ATOM}) AND {DSTRUCTURE}"
    )


def global_basis() -> str:
    """写出吸收后的 global/external 输入基。"""
    return (
        f"{EXTERNAL_DIBFI_ATOM} AND ((({SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM}) "
        f"OR {STANDARD_BETA_ATOM} OR {EXTERNAL_ROUGH_ATOM})) AND {DSTRUCTURE}"
    )


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


def build_rows(previous: dict[str, Any], promotion: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 canonical 终端吸收判定表。"""
    active = previous.get("next_priority") == TERMINAL_ATOM or TERMINAL_ATOM in previous.get(
        "latest_self_contained_basis", ""
    )
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    promotion_closed = (
        bool(promotion.get("current_terminal_promotion_reconciled"))
        and bool(promotion.get("canonical_source_terminal_promotion_closed"))
        and promotion.get("terminal_gap_before_router") == TERMINAL_ATOM
        and promotion.get("terminal_gap_after_router") == CANONICAL_CLOSED_ATOM
        and not bool(promotion.get("row_column_unconditional_closed"))
    )
    outer_canonical_present = CANONICAL_CLOSED_ATOM in previous.get("latest_self_contained_basis", "")
    absorption_closed = active and guard and promotion_closed and outer_canonical_present
    return [
        row(
            "NearSquareTerminalAbsorptionGateActive",
            active,
            False,
            "上一层已经把近平方条带终端准入全局 PDEC-CAP/internal-KLS 门。",
            TERMINAL_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只整理假设早期零行反例链条，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "CanonicalTerminalPromotionImported",
            promotion_closed,
            True,
            "既有当前终端晋级调和已证明 canonical-source 边界内 PDEC-CAP/internal-KLS 无新开门。",
            CANONICAL_CLOSED_ATOM,
        ),
        row(
            "OuterCanonicalPromotionAlreadyPresent",
            outer_canonical_present,
            True,
            "当前输入基外层已含 NoFurtherCanonicalSourceTerminalPromotionGap，可吸收内层同一终端门。",
            "布尔吸收 A AND ((B AND A) OR C) => A AND (B OR C)。",
        ),
        row(
            "NearSquareTerminalAbsorbed",
            absorption_closed,
            False,
            "近平方条带终端门被 canonical 终端晋级边界吸收，不再是独立剩余。",
            f"{SELF_BETA_ATOM} AND {MAIN_ERROR_ATOM}",
        ),
        row(
            SELF_BETA_ATOM,
            False,
            False,
            "完全自足路线仍需逐行给出 Rosser-Iwaniec beta-sieve lower weights 构造。",
            SELF_BETA_ATOM,
        ),
        row(
            MAIN_ERROR_ATOM,
            False,
            False,
            "仍需显式证明 P>=100000 下主系数达到保守 99% 模型主项。",
            MAIN_ERROR_ATOM,
        ),
        row(
            STANDARD_BETA_ATOM,
            False,
            False,
            "若接受标准 beta-sieve 定理，可绕过自足权重构造，但不关闭 sawtooth 外部/generic 分支。",
            STANDARD_BETA_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部短区间 rough-number 下界仍可直接替代整个内部筛权+sawtooth 路线。",
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
    """执行 canonical 终端吸收路由。"""
    previous = load_json(paths["previous"])
    promotion = load_json(paths["promotion"])
    rows = build_rows(previous, promotion)
    absorbed = next(bool(item["closed"]) for item in rows if item["gate"] == "NearSquareTerminalAbsorbed")
    latest_self = self_contained_basis()
    latest_cond = conditional_basis()
    latest_global = global_basis()
    return {
        "certificate_type": "nearsquare_canonical_terminal_absorption_router",
        "status": "nearsquare_terminal_absorbed_beta_sieve_frontier_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "nearsquare_terminal_absorbed": absorbed,
        "self_contained_beta_sieve_appendix_proved": False,
        "beta_sieve_main_coefficient_99pct_proved": False,
        "standard_beta_sieve_import_accepted": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_absorption_law": (
            "A AND (((B AND T) OR C)) with T=>A and outer A "
            "compresses to A AND ((B OR C)) for the canonical branch."
        ),
        "replacement": {TERMINAL_ATOM: CANONICAL_CLOSED_ATOM},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": SELF_BETA_ATOM,
        "secondary_priority": MAIN_ERROR_ATOM,
        "conditional_beta_import_priority": STANDARD_BETA_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把近平方条带终端门从当前链条中吸收掉。"
            "在 canonical-source 分支内，外层已经含有 NoFurtherCanonicalSourceTerminalPromotionGap，"
            "而 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve 已由当前终端晋级调和接回该边界；"
            "所以内层终端门不再是独立剩余。当前最窄点回到 beta-sieve lower weights 的自足构造与 99% 主系数账本。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix 近平方 canonical 终端吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"nearsquare_terminal_absorbed={fmt_bool(result['nearsquare_terminal_absorbed'])}",
        f"self_contained_beta_sieve_appendix_proved={fmt_bool(result['self_contained_beta_sieve_appendix_proved'])}",
        f"beta_sieve_main_coefficient_99pct_proved={fmt_bool(result['beta_sieve_main_coefficient_99pct_proved'])}",
        f"standard_beta_sieve_import_accepted={fmt_bool(result['standard_beta_sieve_import_accepted'])}",
        f"external_short_interval_rough_lower_bound_accepted={fmt_bool(result['external_short_interval_rough_lower_bound_accepted'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 吸收律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "",
        result["terminal_absorption_law"],
        "```",
        "",
        "## 2. 判定表",
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
            "## 3. 最新输入基",
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
            "## 4. 下一步",
            "",
            f"直接攻 `{result['next_priority']}`，随后攻 `{result['secondary_priority']}`。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--promotion", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "promotion": args.promotion,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
