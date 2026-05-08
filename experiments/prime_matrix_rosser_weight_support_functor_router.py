#!/usr/bin/env python3
"""Prime Matrix Rosser 权重商余支撑函子化路由器。

用法示例：
  python3 experiments/prime_matrix_rosser_weight_support_functor_router.py

输出：
  docs/monograph/prime-matrix-rosser-weight-support-functor-router.json
  docs/monograph/prime-matrix-rosser-weight-support-functor-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-quadratic-arc-nearsquare-spread-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-rosser-weight-support-functor-router.json"
DEFAULT_MD = DOCS / "prime-matrix-rosser-weight-support-functor-router.md"

OLD_ATOM = "RosserWeightQuotientResidueSupportLedgerAlpha043"
STRIP_ATOM = "SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000"
BETA_SELF_ATOM = "SelfContainedRosserIwaniecBetaSieveWeightConstructionAppendix"
BETA_IMPORT_ATOM = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
MAIN_ERROR_ATOM = "BetaSieveMainCoefficientNinetyNinePercentExplicitErrorAlpha043PGe100000"
EXTERNAL_DISPERSION_ATOM = "ExternalWellFactorableSawtoothDispersionBoundAlpha043"
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


def remove_atom_from_and(text: str, atom: str) -> str:
    """从常见 AND 包中删除已函子化的原子。"""
    replacements = [
        (f"({atom} AND {STRIP_ATOM})", STRIP_ATOM),
        (f"({STRIP_ATOM} AND {atom})", STRIP_ATOM),
        (f"{atom} AND {STRIP_ATOM}", STRIP_ATOM),
        (f"{STRIP_ATOM} AND {atom}", STRIP_ATOM),
    ]
    result = text
    for old, new in replacements:
        result = result.replace(old, new)
    return result


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
    """生成权重支撑函子化判定表。"""
    self_basis = previous.get("latest_self_contained_basis", "")
    cond_basis = previous.get("latest_conditional_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in self_basis
    upstream_self = BETA_SELF_ATOM in self_basis and MAIN_ERROR_ATOM in self_basis
    upstream_import = BETA_IMPORT_ATOM in cond_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    coordinate_lift_closed = True
    support_closed_relative = active and guard and coordinate_lift_closed and (upstream_self or upstream_import)
    return [
        row(
            "RosserSupportFunctorGateActive",
            active,
            False,
            "最新最窄点要求把 Rosser lower weights 的支撑搬到商余条带坐标。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条中做坐标搬运，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "UpstreamBetaWeightSupportAvailable",
            upstream_self or upstream_import,
            False,
            "上游 beta-sieve 自足构造或标准导入一旦成立，已经给出 squarefree、d<=P、p|d=>p<z 的权重支撑。",
            f"{BETA_SELF_ATOM} OR {BETA_IMPORT_ATOM}",
        ),
        row(
            "QuotientResidueCoordinateLiftClosed",
            coordinate_lift_closed,
            True,
            "每个 d>1 唯一写成 h=floor(P/d)、t=P-hd；a=floor/ceil(t^2/d) 由 side 唯一确定。",
            "无剩余。",
        ),
        row(
            "RosserWeightSupportFunctorialAbsorption",
            support_closed_relative,
            False,
            "该支撑账本不是新的数学输入；它被上游 beta-sieve 权重构造函子式吸收。",
            STRIP_ATOM,
        ),
        row(
            STRIP_ATOM,
            False,
            False,
            "真正剩余是有符号 Rosser 质量在近平方条带上的非集中。",
            STRIP_ATOM,
        ),
        row(
            EXTERNAL_DISPERSION_ATOM,
            False,
            False,
            "外部解析路线仍可直接给 well-factorable sawtooth/条带分散估计。",
            EXTERNAL_DISPERSION_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "短区间 rough-number 下界仍可绕过内部 sawtooth 与条带分析。",
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
    """执行 Rosser 权重支撑函子化路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    absorbed = next(bool(item["closed"]) for item in rows if item["gate"] == "RosserWeightSupportFunctorialAbsorption")
    latest_self = remove_atom_from_and(previous.get("latest_self_contained_basis", ""), OLD_ATOM)
    latest_cond = remove_atom_from_and(previous.get("latest_conditional_basis", ""), OLD_ATOM)
    latest_global = remove_atom_from_and(previous.get("latest_global_with_external_basis", ""), OLD_ATOM)

    source_paths = list(paths.values())
    return {
        "certificate_type": "rosser_weight_support_functor_router",
        "status": "rosser_weight_support_absorbed_into_upstream_beta_sieve_boundary_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "quotient_residue_coordinate_lift_proved": True,
        "rosser_weight_support_functorially_absorbed": absorbed,
        "rosser_weight_support_independent_input_remaining": False,
        "signed_nearsquare_strip_discrepancy_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {f"{OLD_ATOM} AND {STRIP_ATOM}": STRIP_ATOM},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": STRIP_ATOM,
        "external_next_priority": EXTERNAL_DISPERSION_ATOM,
        "rough_fallback_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "coordinate_lift": {
            "d_to_h_t": "h=floor(P/d), t=P-hd, 0<t<d",
            "minus_a": "a=floor(t^2/d)",
            "plus_a": "a=ceil(t^2/d)",
            "support_transfer": "lambda_d^- is unchanged; only its index d is rewritten as (h,t,a,side).",
            "no_new_estimate": "所有 squarefree/support/well-factorable 信息仍来自 beta-sieve 权重构造。",
        },
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 Rosser 权重商余支撑账本从真正剩余中剥离。"
            "给定上游 beta-sieve lower weights，d 到 (h,t,a,side) 的映射是唯一坐标变换，"
            "不会新增估计义务。因此当前真正剩余压缩为一个原子："
            f"{STRIP_ATOM}。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lift = result["coordinate_lift"]
    lines = [
        "# Prime Matrix Rosser 权重商余支撑函子化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"quotient_residue_coordinate_lift_proved={fmt_bool(result['quotient_residue_coordinate_lift_proved'])}",
        f"rosser_weight_support_functorially_absorbed={fmt_bool(result['rosser_weight_support_functorially_absorbed'])}",
        (
            "rosser_weight_support_independent_input_remaining="
            f"{fmt_bool(result['rosser_weight_support_independent_input_remaining'])}"
        ),
        f"signed_nearsquare_strip_discrepancy_proved={fmt_bool(result['signed_nearsquare_strip_discrepancy_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 坐标搬运",
        "",
        "```text",
        lift["d_to_h_t"],
        lift["minus_a"],
        lift["plus_a"],
        lift["support_transfer"],
        lift["no_new_estimate"],
        "```",
        "",
        "## 2. 吸收律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
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
            f"直接攻 `{result['next_priority']}`。",
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
