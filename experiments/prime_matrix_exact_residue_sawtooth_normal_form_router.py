#!/usr/bin/env python3
"""Prime Matrix 精确残基 sawtooth 二次圆弧标准形路由器。

用法示例：
  python3 experiments/prime_matrix_exact_residue_sawtooth_normal_form_router.py

输出：
  docs/monograph/prime-matrix-exact-residue-sawtooth-normal-form-router.json
  docs/monograph/prime-matrix-exact-residue-sawtooth-normal-form-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-explicit-rosser-lower-weight-ledger-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-exact-residue-sawtooth-normal-form-router.json"
DEFAULT_MD = DOCS / "prime-matrix-exact-residue-sawtooth-normal-form-router.md"

OLD_ATOM = "ExactResidueWeightedFloorSawtoothTenPercentBound"
NEW_ATOM = "RosserWeightedQuadraticArcDiscrepancyTenPercentAlpha043PGe100000"
NEAR_SQUARE_ATOM = "WellFactorableNearSquareDivisorSpreadBoundAlpha043"
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


def replace_atom(text: str, old: str, new: str) -> str:
    """替换输入基中的 sawtooth 原子。"""
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


def capacity_metrics(previous: dict[str, Any]) -> dict[str, Any]:
    """读取上一层的主项容量账本。"""
    constants = previous["constants"]
    main = constants["model_main_at_tail_start"]
    target = constants["target_s"]
    target_ratio = constants["target_ratio_of_model_main"]
    conservative_main_fraction = constants["conservative_main_fraction"]
    sawtooth_budget = constants["sawtooth_loss_fraction_budget"]
    residual_after_budget = (conservative_main_fraction - sawtooth_budget) * main
    return {
        "model_main_at_tail_start": main,
        "target_s": target,
        "target_ratio_of_model_main": target_ratio,
        "conservative_main_fraction": conservative_main_fraction,
        "sawtooth_loss_fraction_budget": sawtooth_budget,
        "residual_after_99pct_main_and_90pct_loss": residual_after_budget,
        "residual_exceeds_target": residual_after_budget > target,
        "d_equals_1_endpoint_loss": 1,
        "residual_after_endpoint_loss": residual_after_budget - 1,
        "residual_after_endpoint_loss_exceeds_target": residual_after_budget - 1 > target,
    }


def exact_identity_samples() -> list[dict[str, Any]]:
    """给出小样本验证精确恒等式，便于审稿者读懂对象。"""
    samples: list[dict[str, Any]] = []
    for p, d in [(101, 7), (101, 13), (103, 11), (107, 15)]:
        t = p % d
        floor_p_d = p // d
        for sign in ("minus", "plus"):
            rho = (t * t) % d
            if sign == "plus":
                rho = (-rho) % d
            count = sum(1 for k in range(1, p) if k % d == rho)
            formula_count = floor_p_d + (1 if 0 < rho < t else 0)
            samples.append(
                {
                    "P": p,
                    "d": d,
                    "sign": sign,
                    "t=P mod d": t,
                    "rho": rho,
                    "count_direct": count,
                    "count_formula": formula_count,
                    "error_direct": count - p / d,
                    "error_formula": (1 if 0 < rho < t else 0) - t / d,
                    "identity_holds": count == formula_count,
                }
            )
    return samples


def build_rows(previous: dict[str, Any], metrics: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 sawtooth 标准形判定表。"""
    conditional_basis = previous.get("latest_conditional_basis", "")
    global_basis = previous.get("latest_global_with_external_basis", "")
    active = OLD_ATOM in conditional_basis or OLD_ATOM in global_basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    identity_closed = True
    capacity_closed = metrics["residual_after_endpoint_loss_exceeds_target"]
    compressed = active and guard and identity_closed and capacity_closed
    return [
        row(
            "ExactSawtoothGateActive",
            active,
            False,
            "若标准 beta-sieve 权重包被接受，下一硬点就是精确加权 floor/sawtooth 余项。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条里整理余项标准形，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FloorToQuadraticArcIdentityClosed",
            identity_closed,
            True,
            "对 d>1，令 t=P mod d、rho=±t^2 mod d，则 A_d=floor(P/d)+1_{0<rho<t}。",
            "无剩余。",
        ),
        row(
            "EndpointD1LossRegistered",
            True,
            True,
            "因区间为 1<=k<P，d=1 给 A_1-P=-1；该单点损失已从容量中扣除。",
            "无剩余。",
        ),
        row(
            "NinetyNineMainVsNinetySawtoothCapacityClosed",
            capacity_closed,
            True,
            "若权重主系数保守达到 99% 模型主项，sawtooth 损失不超过 90% 主项且扣除 d=1 后仍超过目标 401。",
            "无剩余。",
        ),
        row(
            "SawtoothAtomCompressedToQuadraticArcDiscrepancy",
            compressed,
            False,
            "旧 sawtooth 原子被压成 Rosser 权重下的二次圆弧偏差界。",
            NEW_ATOM,
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "证明 sum lambda_d^-(1_{0<±(P mod d)^2 mod d<P mod d}-(P mod d)/d) >= -0.90 M(P)。",
            NEW_ATOM,
        ),
        row(
            NEAR_SQUARE_ATOM,
            False,
            False,
            "等价几何形式是 t^2 与 d 的近端余数/近平方除数扩散；这是内部结构路线。",
            NEAR_SQUARE_ATOM,
        ),
        row(
            EXTERNAL_DISPERSION_ATOM,
            False,
            False,
            "外部解析路线是 well-factorable 权重下的 sawtooth/分散估计。",
            EXTERNAL_DISPERSION_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "短区间 rough-number 下界仍可绕过内部 sawtooth 分析。",
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
    """执行 sawtooth 标准形路由。"""
    previous = load_json(paths["previous"])
    metrics = capacity_metrics(previous)
    rows = build_rows(previous, metrics)
    compressed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "SawtoothAtomCompressedToQuadraticArcDiscrepancy"
    )
    latest_self = replace_atom(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom(previous.get("latest_conditional_basis", ""), OLD_ATOM, f"({NEW_ATOM} OR {EXTERNAL_DISPERSION_ATOM})")
    latest_global = replace_atom(previous.get("latest_global_with_external_basis", ""), OLD_ATOM, f"({NEW_ATOM} OR {EXTERNAL_DISPERSION_ATOM})")

    source_paths = list(paths.values())
    return {
        "certificate_type": "exact_residue_sawtooth_normal_form_router",
        "status": "exact_sawtooth_compressed_to_quadratic_arc_discrepancy_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "exact_floor_to_quadratic_arc_identity_proved": True,
        "endpoint_d1_loss_registered": True,
        "sawtooth_atom_compressed": compressed,
        "rosser_weighted_quadratic_arc_discrepancy_proved": False,
        "near_square_divisor_spread_proved": False,
        "external_well_factorable_sawtooth_dispersion_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "replacement_with_external_dispersion": {OLD_ATOM: f"({NEW_ATOM} OR {EXTERNAL_DISPERSION_ATOM})"},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": NEW_ATOM,
        "internal_geometry_priority": NEAR_SQUARE_ATOM,
        "external_next_priority": EXTERNAL_DISPERSION_ATOM,
        "rough_fallback_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "capacity_metrics": metrics,
        "normal_form": {
            "interval": "1<=k<P",
            "d_equals_1": "A_1=P-1, A_1-P=-1",
            "d_gt_1": "t_d=P mod d, rho_d^±=±t_d^2 mod d in {1,...,d-1}",
            "count_identity": "A_d^±=floor(P/d)+1_{0<rho_d^±<t_d}",
            "sawtooth_identity": "A_d^±-P/d=1_{0<rho_d^±<t_d}-t_d/d",
        },
        "identity_samples": exact_identity_samples(),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把精确 floor 余项压成二次圆弧偏差。"
            "对每个 d>1，floor 误差完全由 t=P mod d 与 rho=±t^2 mod d 决定："
            "A_d-P/d=1_{0<rho<t}-t/d。"
            "因此剩余不再是抽象 floor 控制，而是 Rosser 权重下的二次相位圆弧非集中命题；"
            "内部几何路线可写成近平方除数扩散，外部路线可写成 well-factorable sawtooth dispersion。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    metrics = result["capacity_metrics"]
    replacement = next(iter(result["replacement"].items()))
    external_replacement = next(iter(result["replacement_with_external_dispersion"].items()))
    nf = result["normal_form"]
    lines = [
        "# Prime Matrix 精确残基 sawtooth 二次圆弧标准形路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"exact_floor_to_quadratic_arc_identity_proved={fmt_bool(result['exact_floor_to_quadratic_arc_identity_proved'])}",
        f"endpoint_d1_loss_registered={fmt_bool(result['endpoint_d1_loss_registered'])}",
        f"sawtooth_atom_compressed={fmt_bool(result['sawtooth_atom_compressed'])}",
        (
            "rosser_weighted_quadratic_arc_discrepancy_proved="
            f"{fmt_bool(result['rosser_weighted_quadratic_arc_discrepancy_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 精确标准形",
        "",
        "```text",
        f"{nf['interval']}",
        f"{nf['d_equals_1']}",
        f"{nf['d_gt_1']}",
        f"{nf['count_identity']}",
        f"{nf['sawtooth_identity']}",
        "```",
        "",
        "推导要点：对 d>1，P 与 d 互素，所以 rho_d^± 非零。写 P=floor(P/d)d+t_d，"
        "在 1<=k<P 中同余 k=rho 的点数就是 floor(P/d) 加上该残基是否落在开弧 (0,t_d) 内。",
        "",
        "## 2. 容量匹配",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| model main at P=100000 | {metrics['model_main_at_tail_start']:.6f} |",
        f"| target S | {metrics['target_s']} |",
        f"| target/main | {metrics['target_ratio_of_model_main']:.6f} |",
        f"| conservative main fraction | {metrics['conservative_main_fraction']:.6f} |",
        f"| sawtooth loss budget | {metrics['sawtooth_loss_fraction_budget']:.6f} main |",
        f"| residual after 99%-90% | {metrics['residual_after_99pct_main_and_90pct_loss']:.6f} |",
        f"| d=1 endpoint loss | {metrics['d_equals_1_endpoint_loss']} |",
        f"| residual after endpoint loss | {metrics['residual_after_endpoint_loss']:.6f} |",
        "",
        "## 3. 拆分律",
        "",
        "内部标准形：",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "允许外部分散输入：",
        "",
        "```text",
        external_replacement[0],
        "  =>",
        external_replacement[1],
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
            "## 5. 样本验算",
            "",
            "| P | d | sign | t | rho | direct | formula | holds |",
            "| ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for item in result["identity_samples"]:
        lines.append(
            "| {P} | {d} | {sign} | {t} | {rho} | {count_direct} | {count_formula} | `{holds}` |".format(
                P=item["P"],
                d=item["d"],
                sign=item["sign"],
                t=item["t=P mod d"],
                rho=item["rho"],
                count_direct=item["count_direct"],
                count_formula=item["count_formula"],
                holds=fmt_bool(item["identity_holds"]),
            )
        )
    lines.extend(
        [
            "",
            "## 6. 最新输入基",
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
            "## 7. 下一步",
            "",
            (
                f"直接攻 `{result['next_priority']}`。内部几何支路是 "
                f"`{result['internal_geometry_priority']}`；外部解析支路是 `{result['external_next_priority']}`。"
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
