#!/usr/bin/env python3
"""Prime Matrix B=3 显式零点自由区常数账本路由器。

用法示例：
  python3 experiments/prime_matrix_b3_explicit_zero_free_constants_router.py

输出：
  docs/monograph/prime-matrix-b3-explicit-zero-free-constants-router.json
  docs/monograph/prime-matrix-b3-explicit-zero-free-constants-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-b3-zero-free-constants-router.json"
DEFAULT_FINAL_DRAFT = ROOT / "docs" / "final-proof-draft.md"
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_JSON = DOCS / "prime-matrix-b3-explicit-zero-free-constants-router.json"
DEFAULT_MD = DOCS / "prime-matrix-b3-explicit-zero-free-constants-router.md"

OLD_ATOM = "ExplicitZeroFreeRegionConstantNumericalLedger"
CLOG_ATOM = "ExplicitCLogHadamardStirlingJensenNumericalLedger"
OPT_ATOM = "ZeroRepulsionParameterNumericalOptimizationLedger"
PNT_ATOM = "ZeroFreeRegionToExplicitPNTContourConstantLedger"
TARGET_ATOM = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
LOW_HEIGHT_ATOM = "FiniteLowHeightZeroCheckLedger"
CONTOUR_ATOM = "ExplicitPsiThetaContourEnvelopeXGe20000FromZeroFreeRegion"
MERTENS_CONSTANT_ATOM = "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000
DUSART_THETA_DENOMINATOR = 36_260


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


def fmt_float(value: float) -> str:
    """固定小数格式。"""
    return f"{value:.12f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def target_pressure() -> dict[str, float]:
    """计算 x=20000 的 theta 目标压力。"""
    log_x = math.log(ANCHOR_X)
    sqrt_log_x = math.sqrt(log_x)
    target = 1.0 / DUSART_THETA_DENOMINATOR
    required_a_c1 = math.log(DUSART_THETA_DENOMINATOR) / sqrt_log_x
    required_a_c10 = math.log(10.0 * DUSART_THETA_DENOMINATOR) / sqrt_log_x
    return {
        "anchor_x": float(ANCHOR_X),
        "log_anchor": log_x,
        "sqrt_log_anchor": sqrt_log_x,
        "target_relative_error": target,
        "required_a_for_C1": required_a_c1,
        "required_a_for_C10": required_a_c10,
    }


def source_audit(texts: dict[str, str]) -> dict[str, Any]:
    """审查当前材料是否已经包含显式数值常数。"""
    combined = "\n".join(texts.values())
    external_dusart_registered = contains_all(combined, ["Dusart", "vartheta", "36260"])
    c_log_numeric_present = contains_all(combined, ["C_log", "Stirling", "Jensen", "numeric"])
    zero_free_numeric_present = contains_all(combined, ["zero-free", "T0", "c=", "verified"])
    pnt_contour_numeric_present = contains_all(combined, ["Perron", "contour", "theta", "x>=20000"])
    low_height_hash_present = contains_all(combined, ["zero", "height", "hash", "verified"])
    return {
        "external_dusart_theta_registered": external_dusart_registered,
        "explicit_C_log_numeric_ledger_present": c_log_numeric_present,
        "zero_free_c_T0_numeric_ledger_present": zero_free_numeric_present,
        "pnt_contour_numeric_ledger_present": pnt_contour_numeric_present,
        "finite_low_height_hash_present": low_height_hash_present,
    }


def replacement_pair() -> str:
    """写出显式零点自由常数的替换包。"""
    return f"({CLOG_ATOM} AND {OPT_ATOM} AND {PNT_ATOM} AND {TARGET_ATOM})"


def replace_atom(text: str) -> str:
    """替换旧显式常数原子。"""
    return text.replace(OLD_ATOM, replacement_pair())


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
    """生成显式零点自由常数判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM and OLD_ATOM in basis
    symbolic_repulsion_available = "DeLaValleePoussinZeroRepulsionInequalityClosedSymbolicConstants" in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    c_log_closed = bool(audit["explicit_C_log_numeric_ledger_present"])
    opt_closed = bool(audit["zero_free_c_T0_numeric_ledger_present"])
    pnt_closed = bool(audit["pnt_contour_numeric_ledger_present"])
    target_closed = False
    reduced = active and guard and symbolic_repulsion_available
    return [
        row(
            "ExplicitZeroFreeConstantsGateActive",
            active,
            False,
            "上一层唯一内部最窄点是把符号零点排斥常数数值化。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只处理假设链条的解析输入边界，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "SymbolicZeroRepulsionAvailable",
            symbolic_repulsion_available,
            True,
            "上一层已闭合存在性形式 beta<=1-c/log(|gamma|+3)。",
            "还不能用于 x>=20000 数值预算。",
        ),
        row(
            "ExternalDusartThetaRegistered",
            bool(audit["external_dusart_theta_registered"]),
            False,
            "外部 Dusart theta 界已登记，可走外部路线；它不是自足常数账本。",
            "外部路线已在 B3 主系数包中使用。",
        ),
        row(
            "ExplicitCLogNumericalLedgerMissing",
            c_log_closed,
            False,
            "还缺 Hadamard/Stirling/Jensen 剩余项的 C_log 可复算数值上界。",
            CLOG_ATOM,
        ),
        row(
            "ZeroRepulsionNumericalOptimizationMissing",
            opt_closed,
            False,
            "还缺由 C_log 推出 c、T0 和零点自由带的数值优化账本。",
            OPT_ATOM,
        ),
        row(
            "PNTContourNumericalLedgerMissing",
            pnt_closed,
            False,
            "还缺从零点自由带经 Perron/显式公式轮廓积分推出 theta/psi 误差的常数账本。",
            PNT_ATOM,
        ),
        row(
            "ThetaEnvelopeTargetAt20000BudgetMissing",
            target_closed,
            False,
            "x=20000 要达到 1/36260 级相对误差，必须单独核算解析阈值和有限桥。",
            TARGET_ATOM,
        ),
        row(
            "ExplicitZeroFreeConstantsReducedToNumericalSubledgers",
            reduced,
            False,
            "旧显式零点自由常数原子已压成 C_log、参数优化、PNT 轮廓、x=20000 目标预算四包。",
            replacement_pair(),
        ),
        row(
            "FiniteLowHeightZeroCheckStillSeparate",
            False,
            False,
            "低高度零点排除仍是独立有限证书，不能并入高高度常数优化。",
            LOW_HEIGHT_ATOM,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行显式零点自由区常数路由。"""
    previous = load_json(paths["previous"])
    texts = {name: path.read_text(encoding="utf-8") for name, path in paths.items() if name != "previous"}
    audit = source_audit(texts)
    pressure = target_pressure()
    rows = build_rows(previous, audit)
    reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "ExplicitZeroFreeConstantsReducedToNumericalSubledgers"
    )
    return {
        "certificate_type": "b3_explicit_zero_free_constants_router",
        "status": "explicit_zero_free_constants_reduced_to_numerical_subledgers_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths.values()},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "explicit_zero_free_constants_reduced": reduced,
        "explicit_zero_free_constants_self_contained_proved": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {OLD_ATOM: replacement_pair()},
        "latest_self_contained_basis": replace_atom(previous.get("latest_self_contained_basis", "")),
        "latest_conditional_basis": previous.get("latest_conditional_basis", ""),
        "latest_global_with_external_basis": previous.get("latest_global_with_external_basis", ""),
        "next_priority": CLOG_ATOM,
        "secondary_priority": OPT_ATOM,
        "tertiary_priority": PNT_ATOM,
        "quaternary_priority": TARGET_ATOM,
        "post_constants_priority": LOW_HEIGHT_ATOM,
        "post_low_height_priority": CONTOUR_ATOM,
        "post_theta_priority": MERTENS_CONSTANT_ATOM,
        "conditional_next_priority": previous.get("conditional_next_priority", DSTRUCTURE),
        "source_audit": audit,
        "target_pressure": pressure,
        "plain_conclusion": (
            "显式零点自由区常数尚未自足闭合。当前只能诚实地把它压成四个数值子账本："
            "C_log、零点排斥参数优化、PNT 轮廓积分常数、x=20000 目标预算。"
            "外部 Dusart 版仍可用，但完全自足版继续开放。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    pressure = result["target_pressure"]
    lines = [
        "# Prime Matrix B=3 显式零点自由区常数账本路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"explicit_zero_free_constants_reduced={fmt_bool(result['explicit_zero_free_constants_reduced'])}",
        (
            "explicit_zero_free_constants_self_contained_proved="
            f"{fmt_bool(result['explicit_zero_free_constants_self_contained_proved'])}"
        ),
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
        "## 2. x=20000 目标压力",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| anchor_x | `{int(pressure['anchor_x'])}` |",
        f"| log(anchor_x) | `{fmt_float(pressure['log_anchor'])}` |",
        f"| sqrt(log(anchor_x)) | `{fmt_float(pressure['sqrt_log_anchor'])}` |",
        f"| target relative error | `{pressure['target_relative_error']:.15f}` |",
        f"| required a in C=1 exp(-a sqrt(log x)) | `{fmt_float(pressure['required_a_for_C1'])}` |",
        f"| required a in C=10 exp(-a sqrt(log x)) | `{fmt_float(pressure['required_a_for_C10'])}` |",
        "",
        (
            "这说明低锚点要求极强：普通渐近零点自由区常数不能自动给出 `x=20000` 的 theta 误差，"
            "必须配合低高度核验和有限桥。"
        ),
        "",
        "## 3. 来源审查",
        "",
        "| item | value |",
        "| --- | --- |",
    ]
    for key, value in result["source_audit"].items():
        lines.append(f"| {table_cell(key)} | `{fmt_bool(value)}` |")
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
            "## 6. 下一步",
            "",
            (
                f"唯一内部最窄点更新为 `{result['next_priority']}`；"
                f"随后是 `{result['secondary_priority']}`、`{result['tertiary_priority']}`、"
                f"`{result['quaternary_priority']}`。"
            ),
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--final-draft", type=Path, default=DEFAULT_FINAL_DRAFT)
    parser.add_argument("--external-index", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
        "final_draft": args.final_draft,
        "external_index": args.external_index,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
