#!/usr/bin/env python3
"""Prime Matrix Rosser-Iwaniec 权重与 floor 余项账本路由器。

用法示例：
  python3 experiments/prime_matrix_rosser_weight_floor_ledger_router.py

输出：
  docs/monograph/prime-matrix-rosser-weight-floor-ledger-router.json
  docs/monograph/prime-matrix-rosser-weight-floor-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-linear-sieve-tail-remainder-gap-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-rosser-weight-floor-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-rosser-weight-floor-ledger-router.md"

OLD_ATOM = "RosserIwaniecWeightedFloorRemainderTenPercentBound"
WEIGHT_ATOM = "ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000"
SAWTOOTH_ATOM = "ExactResidueWeightedFloorSawtoothTenPercentBound"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
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
    """替换输入基中的 Rosser 余项原子。"""
    return text.replace(old, new)


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


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成权重/floor 账本判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    exact_formula = True
    split_closed = active and guard and exact_formula
    return [
        row(
            "RosserFloorRemainderGateActive",
            active,
            False,
            "最新内部最窄点是 Rosser-Iwaniec 下界权重与 floor 余项的 10% 主项控制。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条内整理尾段筛账本，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "ExactFloorFormulaAvailable",
            exact_formula,
            True,
            "一旦权重固定，余项对象有精确公式：A_d 是一个指定 CRT 残基在 1<=k<P 中的 floor 计数。",
            "需要固定 lambda_d^- 与 level D。",
        ),
        row(
            "RemainderAtomSplitToWeightAndSawtooth",
            split_closed,
            False,
            "旧余项原子先拆成权重定义账本与精确加权 sawtooth 余项界。",
            f"{WEIGHT_ATOM} AND {SAWTOOTH_ATOM}",
        ),
        row(
            WEIGHT_ATOM,
            False,
            False,
            "需要明确 Rosser-Iwaniec lower weights lambda_d^-、支撑 level D、s=log D/log z 以及主项常数。",
            WEIGHT_ATOM,
        ),
        row(
            SAWTOOTH_ATOM,
            False,
            False,
            "权重固定后，证明 sum lambda_d^-(A_d-P/d) 的负向损失不超过 90% 主项。",
            SAWTOOTH_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "外部路线仍可直接引用短区间 rough-number 下界，绕开内部权重余项账本。",
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
    """执行 Rosser 权重/floor 账本路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    split_closed = next(bool(item["closed"]) for item in rows if item["gate"] == "RemainderAtomSplitToWeightAndSawtooth")
    internal_replacement = f"({WEIGHT_ATOM} AND {SAWTOOTH_ATOM})"
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, internal_replacement)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, internal_replacement)
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), OLD_ATOM, internal_replacement)

    source_paths = list(paths.values())
    return {
        "certificate_type": "rosser_weight_floor_ledger_router",
        "status": "rosser_weighted_floor_remainder_split_to_weight_definition_and_sawtooth_bound_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "rosser_weight_floor_remainder_split": split_closed,
        "explicit_rosser_iwaniec_lower_weight_ledger_proved": False,
        "exact_residue_weighted_floor_sawtooth_bound_proved": False,
        "external_short_interval_rough_lower_bound_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {OLD_ATOM: internal_replacement},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": WEIGHT_ATOM,
        "secondary_priority": SAWTOOTH_ATOM,
        "external_next_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "exact_floor_formula": (
            "A_d^±(P)=# {1<=k<P: k ≡ rho_d^±(P) mod d}, "
            "rho_d^+(P) ≡ -P^2 mod d, rho_d^-(P) ≡ P^2 mod d."
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 Rosser-Iwaniec 加权余项命题改写成可审稿的两个原子。"
            "第一，必须固定 lower weights lambda_d^- 与 level D；第二，在这些权重固定后，"
            "证明精确 CRT 残基 floor 余项的加权负损失不超过 90% 主项。"
            "没有权重账本时，旧余项命题还不是一个良定义定理。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix Rosser-Iwaniec 权重与 floor 余项账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"rosser_weight_floor_remainder_split={fmt_bool(result['rosser_weight_floor_remainder_split'])}",
        (
            "explicit_rosser_iwaniec_lower_weight_ledger_proved="
            f"{fmt_bool(result['explicit_rosser_iwaniec_lower_weight_ledger_proved'])}"
        ),
        (
            "exact_residue_weighted_floor_sawtooth_bound_proved="
            f"{fmt_bool(result['exact_residue_weighted_floor_sawtooth_bound_proved'])}"
        ),
        (
            "external_short_interval_rough_lower_bound_accepted="
            f"{fmt_bool(result['external_short_interval_rough_lower_bound_accepted'])}"
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
        "```",
        "",
        "精确 floor 对象：",
        "",
        "```text",
        result["exact_floor_formula"],
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
            "先攻 `ExplicitRosserIwaniecLowerWeightLedgerAlpha043PGe100000`：固定可计算的 lower weights、level 与主项常数。随后才能攻 `ExactResidueWeightedFloorSawtoothTenPercentBound`。若外部路线更优，则直接登记 `ExternalShortIntervalRoughNumberLowerBoundForAlpha043`。",
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
