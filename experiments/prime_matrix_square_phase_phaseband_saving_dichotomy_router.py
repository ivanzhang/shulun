#!/usr/bin/env python3
"""把 no-slot 相位带压力硬点拆成尾素总包络与二次相位节省二分。

用法示例：
  python3 experiments/prime_matrix_square_phase_phaseband_saving_dichotomy_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-phaseband-saving-dichotomy-router.json

输出：
  data/square-phase-phaseband-saving-dichotomy-ledger.json
  docs/monograph/prime-matrix-square-phase-phaseband-saving-dichotomy-router.json
  docs/monograph/prime-matrix-square-phase-phaseband-saving-dichotomy-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

PHASEBAND_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py"

OUT_LEDGER = DATA / "square-phase-phaseband-saving-dichotomy-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-phaseband-saving-dichotomy-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-phaseband-saving-dichotomy-router.md"

MAIN_TARGET = "NoSlotTailPrimePhaseBandDensityPDECExclusion"
NEXT_TARGET = "TailEnvelopeOrQuadraticPhaseSavingGlobalLowerBound"


def load_phaseband_router() -> Any:
    """加载上一层 no-slot 相位带路由器。"""
    spec = importlib.util.spec_from_file_location("phaseband_router", PHASEBAND_ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {PHASEBAND_ROUTER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def decorate(record: dict[str, Any]) -> dict[str, Any]:
    """添加尾包络和相位节省字段。"""
    h_value = record["halfgrid_survivors"]
    tail_count = record["tail_prime_count"]
    phase_count = record["phaseband_count"]
    exact_margin = h_value - 2 * phase_count
    tail_envelope_margin = h_value - 2 * tail_count
    phase_saving = tail_count - phase_count
    required_saving = max(0, tail_count - ((h_value - 1) // 2))
    saving_surplus = phase_saving - required_saving
    return {
        "p": record["p"],
        "side": record["side"],
        "halfgrid_survivors": h_value,
        "tail_prime_count": tail_count,
        "phaseband_count": phase_count,
        "phase_saving": phase_saving,
        "required_phase_saving_for_positive_margin": required_saving,
        "phase_saving_surplus": saving_surplus,
        "tail_envelope_margin": tail_envelope_margin,
        "exact_pressure_margin": exact_margin,
        "decomposition_lhs": exact_margin,
        "decomposition_rhs": tail_envelope_margin + 2 * phase_saving,
        "tail_envelope_already_closes": tail_envelope_margin > 0,
        "phase_saving_rescues_tail_defect": tail_envelope_margin <= 0 and saving_surplus >= 0 and exact_margin > 0,
        "exact_pressure_defect": exact_margin <= 0,
        "top_phaseband_records": record["top_phaseband_records"],
    }


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩记录，便于写入证书。"""
    return {
        "p": record["p"],
        "side": record["side"],
        "halfgrid_survivors": record["halfgrid_survivors"],
        "tail_prime_count": record["tail_prime_count"],
        "phaseband_count": record["phaseband_count"],
        "phase_saving": record["phase_saving"],
        "required_phase_saving_for_positive_margin": record["required_phase_saving_for_positive_margin"],
        "phase_saving_surplus": record["phase_saving_surplus"],
        "tail_envelope_margin": record["tail_envelope_margin"],
        "exact_pressure_margin": record["exact_pressure_margin"],
        "tail_envelope_already_closes": record["tail_envelope_already_closes"],
        "phase_saving_rescues_tail_defect": record["phase_saving_rescues_tail_defect"],
        "top_phaseband_records": record["top_phaseband_records"][:8],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "tail_envelope_phase_saving_identity",
            "status": "closed",
            "statement": "For each side, H-2C=(H-2T)+2(T-C), where H is half-grid survivors, T is the full tail-prime envelope, and C is no-slot phase-band load.",
        },
        {
            "name": "tail_envelope_sufficient_gate",
            "status": "closed",
            "statement": "If H>2T, then the no-slot phase-band pressure defect is excluded without using the quadratic phase saving.",
        },
        {
            "name": "phase_saving_rescue_gate",
            "status": "closed",
            "statement": "When H<=2T, the exact target is equivalent to T-C >= T-floor((H-1)/2).",
        },
        {
            "name": "finite_no_exact_pressure_defect",
            "status": "finite_evidence",
            "statement": "The finite audit finds no exact phase-band pressure defect up to the tested bound.",
        },
        {
            "name": "global_tail_or_saving_bound",
            "status": "open",
            "statement": "A global proof still needs either H>2T, or enough quadratic phase saving T-C, for every prime-square side.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SavingDecompositionIdentityClosed",
            "closed": result["decomposition_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "`H-2C=(H-2T)+2(T-C)` 逐侧逐 P 精确成立。",
            "remaining": "closed",
        },
        {
            "gate": "TailEnvelopeOnlyClosesAllFiniteCases",
            "closed": result["tail_envelope_defect_count"] == 0,
            "proved": False,
            "meaning": "若为 true，尾素总包络本身已经闭合；有限审计显示它并非总是 true。",
            "remaining": "phase saving is needed where false",
        },
        {
            "gate": "PhaseSavingRescuesFiniteTailDefects",
            "closed": result["unrescued_tail_defect_count"] == 0,
            "proved": False,
            "meaning": "有限审计中所有尾包络失败点均由二次相位节省补足。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "ExactPhaseBandPressureDefectAbsentFinite",
            "closed": result["exact_pressure_defect_count"] == 0,
            "proved": False,
            "meaning": "有限扫描未出现精确相位带压力缺陷。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalTailEnvelopeOrSavingBoundClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明尾包络正余量或二次相位节省下界。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把相位带 PDEC 拆成两项可攻输入，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    phase = load_phaseband_router()
    split = phase.load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = phase.sieve(max_p)
    primes = phase.primes_from_flags(small_flags, max_p)
    p_values = [p_value for p_value in primes if p_value >= 3]
    records = [
        decorate(phase.audit_side(split, p_value, side, primes, prime_flags, pi_prefix))
        for p_value in p_values
        for side in ("plus", "minus")
    ]
    identity_failures = [row for row in records if row["decomposition_lhs"] != row["decomposition_rhs"]]
    tail_defects = [row for row in records if row["tail_envelope_margin"] <= 0]
    unrescued_tail_defects = [row for row in tail_defects if not row["phase_saving_rescues_tail_defect"]]
    exact_defects = [row for row in records if row["exact_pressure_defect"]]
    sample_set = set(sample_ps)
    sample_records = [row for row in records if row["p"] in sample_set]
    saving_frontier = sorted(records, key=lambda row: (row["phase_saving_surplus"], row["exact_pressure_margin"], row["p"], row["side"]))
    tail_frontier = sorted(records, key=lambda row: (row["tail_envelope_margin"], row["p"], row["side"]))
    exact_frontier = sorted(records, key=lambda row: (row["exact_pressure_margin"], row["p"], row["side"]))
    aggregate = {
        "record_count": len(records),
        "combined_halfgrid_survivors": sum(row["halfgrid_survivors"] for row in records),
        "combined_tail_prime_count": sum(row["tail_prime_count"] for row in records),
        "combined_phaseband_count": sum(row["phaseband_count"] for row in records),
        "combined_phase_saving": sum(row["phase_saving"] for row in records),
        "decomposition_identity_failure_count": len(identity_failures),
        "tail_envelope_defect_count": len(tail_defects),
        "tail_envelope_closure_count": sum(1 for row in records if row["tail_envelope_already_closes"]),
        "unrescued_tail_defect_count": len(unrescued_tail_defects),
        "exact_pressure_defect_count": len(exact_defects),
        "min_exact_pressure_margin": exact_frontier[0]["exact_pressure_margin"] if exact_frontier else None,
        "min_tail_envelope_margin": tail_frontier[0]["tail_envelope_margin"] if tail_frontier else None,
        "min_phase_saving_surplus": saving_frontier[0]["phase_saving_surplus"] if saving_frontier else None,
        "max_required_phase_saving": max((row["required_phase_saving_for_positive_margin"] for row in records), default=None),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "exact_margin_frontier": [compact(row) for row in exact_frontier[:80]],
        "tail_envelope_frontier": [compact(row) for row in tail_frontier[:80]],
        "saving_surplus_frontier": [compact(row) for row in saving_frontier[:80]],
        "tail_envelope_defect_records": [compact(row) for row in tail_defects[:120]],
        "unrescued_tail_defect_records": [compact(row) for row in unrescued_tail_defects[:40]],
        "exact_pressure_defect_records": [compact(row) for row in exact_defects[:40]],
        "sample_records": [compact(row) for row in sample_records],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_phaseband_saving_dichotomy_router",
        "status": "phaseband_density_pdec_reduced_to_tail_envelope_or_quadratic_phase_saving_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "decomposition_identity_failure_count": len(identity_failures),
        "tail_envelope_defect_count": len(tail_defects),
        "unrescued_tail_defect_count": len(unrescued_tail_defects),
        "exact_pressure_defect_count": len(exact_defects),
        "exact_margin_frontier": ledger["exact_margin_frontier"][:20],
        "tail_envelope_frontier": ledger["tail_envelope_frontier"][:20],
        "saving_surplus_frontier": ledger["saving_surplus_frontier"][:20],
        "sample_records": ledger["sample_records"],
        "decomposition_identity_closed": len(identity_failures) == 0,
        "finite_all_tail_defects_rescued_by_phase_saving": len(unrescued_tail_defects) == 0,
        "finite_no_exact_phaseband_pressure_defect": len(exact_defects) == 0,
        "global_tail_envelope_or_phase_saving_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_phaseband_saving_dichotomy_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py": sha256(
                PHASEBAND_ROUTER
            ),
            "data/square-phase-phaseband-saving-dichotomy-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步没有转换目标，而是把当前精确余量拆成 `H-2C=(H-2T)+2(T-C)`。"
            "`H` 是半网格幸存数，也就是平方锚侧短区间素数数；`T` 是全部尾素包络；"
            "`C` 是上一层 no-slot 二次相位带尾素数。若 `H>2T`，不需要相位信息即可闭合；"
            "若 `H<=2T`，则必须由二次相位节省 `T-C` 补足，且所需节省精确为 "
            "`max(0, T-floor((H-1)/2))`。有限扫描中尾包络失败点存在，但全部由相位节省补足；"
            "全局仍需证明尾包络正余量或二次相位节省下界。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase phase-band saving dichotomy router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"decomposition_identity_failure_count={result['decomposition_identity_failure_count']}",
        f"tail_envelope_defect_count={result['tail_envelope_defect_count']}",
        f"unrescued_tail_defect_count={result['unrescued_tail_defect_count']}",
        f"exact_pressure_defect_count={result['exact_pressure_defect_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 恒等式",
        "",
        "记",
        "",
        "```text",
        "H = HalfGridSurvivors_side(P)",
        "T = TailPrimeCount_side(P)",
        "C = NoSlotPhaseBandCount_side(P)",
        "S = T-C",
        "```",
        "",
        "则当前目标 `H>2C` 精确等价于",
        "",
        "```text",
        "H-2C = (H-2T)+2S > 0.",
        "```",
        "",
        "`H-2T` 是丢掉二次相位后的尾素总包络余量；`S=T-C` 是二次相位避让节省。",
        "",
        "## 2. 节省阈值",
        "",
        "当尾包络余量 `H-2T<=0` 时，仍要闭合 `H>2C`，所需的最小整数节省为",
        "",
        "```text",
        "S_required = max(0, T-floor((H-1)/2)).",
        "```",
        "",
        "所以剩余不再是抽象密度异常，而是一个精确的二分：要么证明 `H>2T`，要么证明 `S>=S_required`。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| record count | {agg['record_count']} |",
        f"| combined H | {agg['combined_halfgrid_survivors']} |",
        f"| combined T | {agg['combined_tail_prime_count']} |",
        f"| combined C | {agg['combined_phaseband_count']} |",
        f"| combined S=T-C | {agg['combined_phase_saving']} |",
        f"| decomposition identity failures | {agg['decomposition_identity_failure_count']} |",
        f"| tail envelope defect count | {agg['tail_envelope_defect_count']} |",
        f"| tail envelope closure count | {agg['tail_envelope_closure_count']} |",
        f"| unrescued tail defect count | {agg['unrescued_tail_defect_count']} |",
        f"| exact pressure defect count | {agg['exact_pressure_defect_count']} |",
        f"| min exact pressure margin | {agg['min_exact_pressure_margin']} |",
        f"| min tail envelope margin | {agg['min_tail_envelope_margin']} |",
        f"| min phase saving surplus | {agg['min_phase_saving_surplus']} |",
        f"| max required phase saving | {agg['max_required_phase_saving']} |",
        "",
        "## 4. 最紧边界",
        "",
        "| label | P | side | H | T | C | S | S_req | S_surplus | H-2T | H-2C |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    boundary_rows = [
        ("exact margin", result["exact_margin_frontier"][0] if result["exact_margin_frontier"] else None),
        ("tail envelope", result["tail_envelope_frontier"][0] if result["tail_envelope_frontier"] else None),
        ("saving surplus", result["saving_surplus_frontier"][0] if result["saving_surplus_frontier"] else None),
    ]
    for label, record in boundary_rows:
        if not record:
            continue
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["phaseband_count"]),
                    str(record["phase_saving"]),
                    str(record["required_phase_saving_for_positive_margin"]),
                    str(record["phase_saving_surplus"]),
                    str(record["tail_envelope_margin"]),
                    str(record["exact_pressure_margin"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 样本表",
            "",
            "| P | side | H | T | C | S | S_req | S_surplus | H-2T | H-2C |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for record in result["sample_records"][:24]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["phaseband_count"]),
                    str(record["phase_saving"]),
                    str(record["required_phase_saving_for_positive_margin"]),
                    str(record["phase_saving_surplus"]),
                    str(record["tail_envelope_margin"]),
                    str(record["exact_pressure_margin"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 6. 命题行",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for row in result["theorem_rows"]:
        lines.append(f"| `{row['name']}` | `{row['status']}` | {table_cell(row['statement'])} |")
    lines.extend(
        [
            "",
            "## 7. 决策表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['gate']}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 8. 下一步",
            "",
            "- 主攻：`TailEnvelopeOrQuadraticPhaseSavingGlobalLowerBound`。",
            "- 第一支：证明平方锚短区间素数数 `H` 全局大于两倍尾素包络 `2T`。",
            "- 第二支：在第一支失败处，证明二次相位节省 `S=T-C` 至少达到 `S_required`。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 9. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-p", type=int, default=5000)
    parser.add_argument(
        "--sample-ps",
        type=str,
        default="13,17,19,23,29,31,73,101,499,1009,2003,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-phaseband-saving-dichotomy-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "decomposition_identity_failure_count": result["decomposition_identity_failure_count"],
                "tail_envelope_defect_count": result["tail_envelope_defect_count"],
                "unrescued_tail_defect_count": result["unrescued_tail_defect_count"],
                "exact_pressure_defect_count": result["exact_pressure_defect_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
