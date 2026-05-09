#!/usr/bin/env python3
"""完全自足最终前沿汇总路由器。

用法示例：
  python3 experiments/prime_matrix_self_contained_final_frontier_consolidation_router.py

输出：
  docs/monograph/prime-matrix-self-contained-final-frontier-consolidation-router.json
  docs/monograph/prime-matrix-self-contained-final-frontier-consolidation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_FINAL = MONO / "prime-matrix-self-contained-final-target-attack-router.json"
DEFAULT_HARMONIC = MONO / "prime-matrix-harmonic-window-dusart-ledger-router.json"
DEFAULT_DYNAMIC = MONO / "prime-matrix-dynamic-skeleton-lower-factorization-router.json"
DEFAULT_LINEAR_TAIL = MONO / "prime-matrix-linear-lower-sieve-tail-margin-router.json"
DEFAULT_ROSSER_FLOOR = MONO / "prime-matrix-rosser-weight-floor-ledger-router.json"
DEFAULT_LOWER_RECURSION = MONO / "prime-matrix-beta-sieve-lower-weight-recursion-router.json"
DEFAULT_DOMINANCE = MONO / "prime-matrix-beta-sieve-lower-bound-dominance-router.json"
DEFAULT_CONTINUOUS = MONO / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json"
DEFAULT_STIELTJES = MONO / "prime-matrix-b3-prime-word-stieltjes-integral-router.json"
DEFAULT_BOUNDARY = MONO / "prime-matrix-b3-alternating-boundary-terminal-router.json"
DEFAULT_SAWTOOTH = MONO / "prime-matrix-exact-residue-sawtooth-normal-form-router.json"
DEFAULT_QUADRATIC = MONO / "prime-matrix-quadratic-arc-nearsquare-spread-router.json"
DEFAULT_SUPPORT = MONO / "prime-matrix-rosser-weight-support-functor-router.json"
DEFAULT_NEARSQUARE_DEFECT = MONO / "prime-matrix-nearsquare-strip-defect-certificate-router.json"
DEFAULT_NEARSQUARE_ADMISSION = MONO / "prime-matrix-nearsquare-strip-terminal-admission-router.json"
DEFAULT_NEARSQUARE_ABSORPTION = MONO / "prime-matrix-nearsquare-canonical-terminal-absorption-router.json"
DEFAULT_PROMOTION = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
DEFAULT_JSON = MONO / "prime-matrix-self-contained-final-frontier-consolidation-router.json"
DEFAULT_MD = MONO / "prime-matrix-self-contained-final-frontier-consolidation-router.md"

NO_HIDDEN = "NoFurtherCanonicalSourceTerminalPromotionGap"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
SELF_PROMOTION = "SelfContainedDStructureTailLog4FiniteRankinProofPackage"
EXTERNAL_ROUGH = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"

B3_MERTENS = "B3PrimeHarmonicMertensUniformEnvelopePGe100000"
B3_VARIATION = "B3BoundaryVariationOnePercentTransferLedger"
SIGNED_STRIP = "SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    proved: bool,
    evidence: str,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "evidence": evidence,
        "meaning": meaning,
        "remaining": remaining,
    }


def all_true(*values: Any) -> bool:
    """布尔合取辅助函数。"""
    return all(value is True for value in values)


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总各子路由给出的前沿状态。"""
    final = data["final"]
    harmonic = data["harmonic"]
    dynamic = data["dynamic"]
    linear_tail = data["linear_tail"]
    lower_recursion = data["lower_recursion"]
    dominance = data["dominance"]
    continuous = data["continuous"]
    stieltjes = data["stieltjes"]
    boundary = data["boundary"]
    sawtooth = data["sawtooth"]
    quadratic = data["quadratic"]
    support = data["support"]
    nearsquare_defect = data["nearsquare_defect"]
    nearsquare_admission = data["nearsquare_admission"]
    nearsquare_absorption = data["nearsquare_absorption"]
    promotion = data["promotion"]

    final_basis_saved = (
        final.get("latest_self_contained_basis")
        == f"{NO_HIDDEN} AND {HIGH_MODEL} AND {SELF_PROMOTION}"
    )
    harmonic_closed = harmonic.get("harmonic_window_alpha043_upper0850_closed") is True
    dynamic_finite_closed = dynamic.get("finite_dynamic_skeleton_certificate_closed") is True
    tail_compressed = linear_tail.get("tail_linear_sieve_input_compressed") is True
    beta_structural_closed = all_true(
        lower_recursion.get("lower_weight_recursive_construction_closed"),
        dominance.get("lower_weight_dominance_proved"),
        continuous.get("continuous_beta_sieve_surplus_proved"),
        stieltjes.get("prime_word_stieltjes_integral_ledger_closed"),
    )
    beta_boundary_open = (
        boundary.get("alternating_boundary_remainder_atom_reduced") is True
        and boundary.get("alternating_boundary_remainder_one_percent_proved") is False
    )
    sawtooth_structural_closed = all_true(
        sawtooth.get("exact_floor_to_quadratic_arc_identity_proved"),
        quadratic.get("arc_hit_iff_nearsquare_multiple_proved"),
        quadratic.get("nearsquare_lift_to_quotient_residue_strip_proved"),
        support.get("quotient_residue_coordinate_lift_proved"),
        support.get("rosser_weight_support_functorially_absorbed"),
    )
    signed_strip_absorbed = (
        support.get("signed_nearsquare_strip_discrepancy_proved") is False
        and nearsquare_defect.get("signed_strip_bound_compressed") is True
        and nearsquare_admission.get("nearsquare_strip_terminal_admission_closed") is True
        and nearsquare_absorption.get("nearsquare_terminal_absorbed") is True
    )
    promotion_open = (
        promotion.get("promotion_author_packet_sealed") is True
        and promotion.get("referee_gate_explicitly_accepted") is False
    )

    return [
        row(
            "FinalTwoInputBasisSaved",
            final_basis_saved,
            final_basis_saved,
            "self-contained final target attack router",
            "旧总目标已严格保存为高段模型余量与自足晋级包两输入。",
            f"{HIGH_MODEL} AND {SELF_PROMOTION}",
        ),
        row(
            "HarmonicWindowClosed",
            harmonic_closed,
            harmonic_closed,
            "harmonic window Dusart ledger router",
            "H(P)<=0.850 已由有限核查与 Dusart 尾段关闭。",
            "从高段模型余量活动输入中删除调和窗口。",
        ),
        row(
            "DynamicSkeletonFiniteBridgeClosed",
            dynamic_finite_closed,
            dynamic_finite_closed,
            "dynamic skeleton lower factorization router",
            "3001<=P<100000 的动态粗骨架有限桥接段已关闭。",
            "P>=100000 lower-sieve 尾段。",
        ),
        row(
            "TailLowerSieveCompressed",
            tail_compressed,
            False,
            "linear lower sieve tail margin router",
            "P>=100000 尾段已压成 10% 模型主项包，但未证明实际筛余达到该包。",
            "beta-sieve 主系数与精确 sawtooth 两条内部义务。",
        ),
        row(
            "BetaWeightStructuralLayersClosed",
            beta_structural_closed,
            beta_structural_closed,
            "lower recursion/dominance/continuous/Stieltjes routers",
            "lower weights 构造、逐点支配、连续 f(s) 余量和 Stieltjes 精确表示均已闭合。",
            f"{B3_MERTENS} AND {B3_VARIATION}",
        ),
        row(
            "B3BoundaryRemainderStillOpen",
            beta_boundary_open,
            False,
            "B3 alternating boundary terminal router",
            "B3 离散边界余项仍需 Mertens 统一包络与边界变差传递。",
            f"{B3_MERTENS} AND {B3_VARIATION}",
        ),
        row(
            "SawtoothNormalFormLayersClosed",
            sawtooth_structural_closed,
            sawtooth_structural_closed,
            "exact sawtooth/quadratic arc/support routers",
            "floor 余项已化为二次圆弧，再化为商余近平方条带；支撑账本被上游权重吸收。",
            SIGNED_STRIP,
        ),
        row(
            "SignedNearSquareStripTerminalAbsorbed",
            signed_strip_absorbed,
            False,
            "nearsquare defect/admission/absorption routers",
            "近平方条带失败态会生成同 formal unit 的 PDEC/SAE 证书；在 canonical 外层边界内已被吸收，不再是独立输入。",
            f"{B3_MERTENS} AND {B3_VARIATION}",
        ),
        row(
            "HighSegmentModelFrontierConsolidated",
            beta_structural_closed
            and beta_boundary_open
            and sawtooth_structural_closed
            and signed_strip_absorbed,
            False,
            "combined high-segment subrouters",
            "高段模型余量的当前自足前沿已不再是抽象 HighSegment；sawtooth/近平方终端被吸收后，只剩 beta 边界余项。",
            f"({B3_MERTENS} AND {B3_VARIATION}) OR {EXTERNAL_ROUGH}",
        ),
        row(
            "SelfContainedPromotionPackageStillOpen",
            promotion_open,
            False,
            "final promotion gate irreducibility router",
            "作者侧晋级证据包已封装，但完全自足版仍需替换独立验收门。",
            SELF_PROMOTION,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行最终自足前沿汇总。"""
    data = {name: load_json(path) for name, path in paths.items() if name not in {"json_out", "md_out"}}
    rows = build_rows(data)
    structural_frontier_closed = all(item["closed"] for item in rows)

    strict_basis = (
        f"{NO_HIDDEN} AND ({B3_MERTENS} AND {B3_VARIATION}) "
        f"AND {SELF_PROMOTION}"
    )
    with_external_bypass = (
        f"{NO_HIDDEN} AND ((({B3_MERTENS} AND {B3_VARIATION}) "
        f"OR {EXTERNAL_ROUGH})) AND {SELF_PROMOTION}"
    )

    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    return {
        "certificate_type": "prime_matrix_self_contained_final_frontier_consolidation_router",
        "status": "self_contained_final_frontier_consolidated_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "frontier_reduction_closed": structural_frontier_closed,
        "high_segment_model_gap_proved": False,
        "self_contained_promotion_package_proved": False,
        "row_column_self_contained_closed": False,
        "latest_strict_self_contained_basis": strict_basis,
        "latest_with_external_rough_bypass_basis": with_external_bypass,
        "open_strict_self_contained_inputs": [
            B3_MERTENS,
            B3_VARIATION,
            SELF_PROMOTION,
        ],
        "optional_external_bypass": EXTERNAL_ROUGH,
        "next_priority": B3_VARIATION,
        "secondary_priority": B3_MERTENS,
        "promotion_priority": SELF_PROMOTION,
        "plain_conclusion": (
            "本步没有宣布无条件闭合，而是把刚提交的两输入总目标继续合并到当前真实前沿："
            "调和窗口、有限桥接、权重构造、逐点支配、连续主项、Stieltjes 表示、floor 到二次圆弧、"
            "再到近平方条带终端吸收的结构层均已关闭；真正自足剩余压到 B3 Mertens 包络、"
            "B3 边界变差乘子，以及自足版 DStructure/Tail-log4/finite Rankin 晋级包。"
        ),
        "rows": rows,
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 完全自足最终前沿汇总路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"frontier_reduction_closed={fmt_bool(result['frontier_reduction_closed'])}",
        f"high_segment_model_gap_proved={fmt_bool(result['high_segment_model_gap_proved'])}",
        (
            "self_contained_promotion_package_proved="
            f"{fmt_bool(result['self_contained_promotion_package_proved'])}"
        ),
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 最新严格自足输入基",
        "",
        "```text",
        result["latest_strict_self_contained_basis"],
        "```",
        "",
        "## 2. 允许外部 rough 下界旁路时的输入基",
        "",
        "```text",
        result["latest_with_external_rough_bypass_basis"],
        "```",
        "",
        "## 3. 当前开放输入",
        "",
    ]
    for item in result["open_strict_self_contained_inputs"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | evidence | meaning | remaining |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {evidence} | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            (
                f"优先攻 `{result['next_priority']}`；并行保留 `{result['secondary_priority']}` "
                f"和 `{result['promotion_priority']}`。若接受 `{result['optional_external_bypass']}`，"
                "则可绕过 beta/sawtooth 内部尾段，但这不是严格自足闭合。"
            ),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--final-json", type=Path, default=DEFAULT_FINAL)
    parser.add_argument("--harmonic-json", type=Path, default=DEFAULT_HARMONIC)
    parser.add_argument("--dynamic-json", type=Path, default=DEFAULT_DYNAMIC)
    parser.add_argument("--linear-tail-json", type=Path, default=DEFAULT_LINEAR_TAIL)
    parser.add_argument("--rosser-floor-json", type=Path, default=DEFAULT_ROSSER_FLOOR)
    parser.add_argument("--lower-recursion-json", type=Path, default=DEFAULT_LOWER_RECURSION)
    parser.add_argument("--dominance-json", type=Path, default=DEFAULT_DOMINANCE)
    parser.add_argument("--continuous-json", type=Path, default=DEFAULT_CONTINUOUS)
    parser.add_argument("--stieltjes-json", type=Path, default=DEFAULT_STIELTJES)
    parser.add_argument("--boundary-json", type=Path, default=DEFAULT_BOUNDARY)
    parser.add_argument("--sawtooth-json", type=Path, default=DEFAULT_SAWTOOTH)
    parser.add_argument("--quadratic-json", type=Path, default=DEFAULT_QUADRATIC)
    parser.add_argument("--support-json", type=Path, default=DEFAULT_SUPPORT)
    parser.add_argument("--nearsquare-defect-json", type=Path, default=DEFAULT_NEARSQUARE_DEFECT)
    parser.add_argument("--nearsquare-admission-json", type=Path, default=DEFAULT_NEARSQUARE_ADMISSION)
    parser.add_argument("--nearsquare-absorption-json", type=Path, default=DEFAULT_NEARSQUARE_ABSORPTION)
    parser.add_argument("--promotion-json", type=Path, default=DEFAULT_PROMOTION)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "final": args.final_json,
        "harmonic": args.harmonic_json,
        "dynamic": args.dynamic_json,
        "linear_tail": args.linear_tail_json,
        "rosser_floor": args.rosser_floor_json,
        "lower_recursion": args.lower_recursion_json,
        "dominance": args.dominance_json,
        "continuous": args.continuous_json,
        "stieltjes": args.stieltjes_json,
        "boundary": args.boundary_json,
        "sawtooth": args.sawtooth_json,
        "quadratic": args.quadratic_json,
        "support": args.support_json,
        "nearsquare_defect": args.nearsquare_defect_json,
        "nearsquare_admission": args.nearsquare_admission_json,
        "nearsquare_absorption": args.nearsquare_absorption_json,
        "promotion": args.promotion_json,
        "json_out": args.json_out,
        "md_out": args.md_out,
    }
    result = run(paths)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["latest_strict_self_contained_basis"])


if __name__ == "__main__":
    main()
