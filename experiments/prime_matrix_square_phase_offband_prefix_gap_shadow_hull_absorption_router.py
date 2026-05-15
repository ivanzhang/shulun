#!/usr/bin/env python3
"""把固定形状并集素数供给压成 hull 计数与互补孔袋吸收 PDEC。

用法示例：
  python3 experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-hull-absorption-router.json

输出：
  data/square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-hull-absorption-router.json
  docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-hull-absorption-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

INPUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-sqrt-input-ledger.json"
OUT_LEDGER = DATA / "square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-hull-absorption-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-offband-prefix-gap-shadow-hull-absorption-router.md"

SQRT_INPUT_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_offband_prefix_gap_shadow_sqrt_input_router.py"

MAIN_TARGET = "FixedShapeUnionPrimeSupplyOrSqrtScaleGapInput"
NEXT_TARGET = "HullPrimeCountBeatsCoverageDefectOrComplementPocketAbsorptionPDEC"


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sieve(limit: int) -> bytearray:
    """筛出 limit 以内素数。"""
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    for value in range(2, isqrt(limit) + 1):
        if flags[value]:
            start = value * value
            flags[start : limit + 1 : value] = b"\x00" * (((limit - start) // value) + 1)
    return flags


def parse_atom_interval(key: str) -> dict[str, Any]:
    """解析 band:k:qlo-qhi 形式的 atom 键。"""
    band, rest = key.split(":k", 1)
    k_text, q_text = rest.split(":", 1)
    q_lo_text, q_hi_text = q_text.split("-", 1)
    return {
        "band": band,
        "k": int(k_text),
        "q_lo": int(q_lo_text),
        "q_hi": int(q_hi_text),
    }


def odd_values(q_lo: int, q_hi: int) -> list[int]:
    """列出同奇偶候选 q。"""
    return list(range(q_lo, q_hi + 1, 2))


def pocket_intervals(values: list[int]) -> list[dict[str, Any]]:
    """把奇数候选值合并为步长 2 的连续孔袋。"""
    if not values:
        return []
    pockets: list[dict[str, Any]] = []
    start = values[0]
    last = values[0]
    for value in values[1:]:
        if value == last + 2:
            last = value
        else:
            pockets.append({"q_lo": start, "q_hi": last, "candidate_count": (last - start) // 2 + 1})
            start = value
            last = value
    pockets.append({"q_lo": start, "q_hi": last, "candidate_count": (last - start) // 2 + 1})
    return pockets


def prime_count(values: list[int], prime_flags: bytearray) -> int:
    """计算候选值中的素数个数。"""
    return sum(1 for value in values if prime_flags[value])


def enrich_template(row: dict[str, Any], prime_flags: bytearray) -> dict[str, Any]:
    """给模板补上 hull/union/complement 精确计数。"""
    intervals = [parse_atom_interval(key) for key in row["void_atom_keys"]]
    hull_values = odd_values(row["q_hull_lo"], row["q_hull_hi"])
    covered: set[int] = set()
    for interval in intervals:
        covered.update(odd_values(interval["q_lo"], interval["q_hi"]))
    union_values = sorted(value for value in hull_values if value in covered)
    complement_values = sorted(value for value in hull_values if value not in covered)
    complement_pockets = pocket_intervals(complement_values)
    for pocket in complement_pockets:
        values = odd_values(pocket["q_lo"], pocket["q_hi"])
        pocket["prime_count"] = prime_count(values, prime_flags)
        pocket["prime_values"] = [value for value in values if prime_flags[value]][:12]
    hull_prime_count = prime_count(hull_values, prime_flags)
    union_prime_count = prime_count(union_values, prime_flags)
    complement_prime_count = prime_count(complement_values, prime_flags)
    complement_candidate_count = len(complement_values)
    coverage_defect_identity_ok = complement_candidate_count == row["coverage_defect_candidate_count"]
    prime_partition_identity_ok = hull_prime_count == union_prime_count + complement_prime_count
    union_load_identity_ok = union_prime_count == row["actual_template_prime_load"]
    return {
        **row,
        "hull_candidate_count": len(hull_values),
        "union_candidate_count_recomputed": len(union_values),
        "complement_candidate_count": complement_candidate_count,
        "hull_prime_count": hull_prime_count,
        "union_prime_count": union_prime_count,
        "complement_prime_count": complement_prime_count,
        "hull_prime_count_beats_coverage_defect": hull_prime_count > complement_candidate_count,
        "hull_count_margin_over_coverage_defect": hull_prime_count - complement_candidate_count,
        "complement_absorption_margin": hull_prime_count - complement_prime_count,
        "exact_union_void_equiv_complement_absorbs": union_prime_count == 0 and hull_prime_count == complement_prime_count,
        "coverage_defect_identity_ok": coverage_defect_identity_ok,
        "prime_partition_identity_ok": prime_partition_identity_ok,
        "union_load_identity_ok": union_load_identity_ok,
        "identity_all_ok": coverage_defect_identity_ok and prime_partition_identity_ok and union_load_identity_ok,
        "complement_pocket_count": len(complement_pockets),
        "complement_pockets": complement_pockets,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "hull_union_complement_prime_partition",
            "status": "closed",
            "statement": "For each template, hull primes split exactly into target-union primes plus complement-pocket primes.",
        },
        {
            "name": "hull_count_beats_coverage_defect_gate",
            "status": "closed",
            "statement": "If hull_prime_count exceeds the number of complement candidates, the target union must contain a prime.",
        },
        {
            "name": "complement_absorption_pdec_registration",
            "status": "closed",
            "statement": "If the target union is prime-void, all hull primes are absorbed by explicit complement pockets.",
        },
        {
            "name": "finite_no_complement_absorption",
            "status": "finite_evidence",
            "statement": "The finite audit finds positive complement absorption margin for every template.",
        },
        {
            "name": "global_hull_count_or_absorption_exclusion",
            "status": "open",
            "statement": "A global proof still needs hull prime counts beating coverage defects, or exclusion of complement-pocket absorption.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "HullUnionComplementPartitionClosed",
            "closed": result["identity_failure_count"] == 0,
            "proved": True,
            "meaning": "hull/目标并集/互补孔袋的候选与素数计数恒等式已闭合。",
            "remaining": "closed",
        },
        {
            "gate": "HullCountBeatsCoverageDefectGateClosed",
            "closed": True,
            "proved": True,
            "meaning": "`π_hull>D_cov` 是排除穿孔并集全空的充分条件。",
            "remaining": "closed",
        },
        {
            "gate": "ComplementAbsorptionPDECRegistered",
            "closed": True,
            "proved": True,
            "meaning": "若充分条件失败，则反例必须让互补孔袋吸收全部 hull 素数。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoComplementAbsorptionPDEC",
            "closed": result["actual_union_void_count"] == 0,
            "proved": False,
            "meaning": "有限样本中没有目标并集全空。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalHullCountOrAbsorptionClosed",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局证明 hull 计数胜过覆盖缺口，或排斥互补孔袋吸收。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只完成计数恒等式和 PDEC 注册，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def compact_record(row: dict[str, Any]) -> dict[str, Any]:
    """压缩模板记录。"""
    return {
        "p": row["p"],
        "side": row["side"],
        "input_type": row["input_type"],
        "shape_key": row["shape_key"],
        "void_atom_keys": row["void_atom_keys"],
        "q_hull_lo": row["q_hull_lo"],
        "q_hull_hi": row["q_hull_hi"],
        "depth_from_p": row["depth_from_p"],
        "depth_over_sqrt_p": row["depth_over_sqrt_p"],
        "coverage_defect_candidate_count": row["coverage_defect_candidate_count"],
        "hull_prime_count": row["hull_prime_count"],
        "union_prime_count": row["union_prime_count"],
        "complement_prime_count": row["complement_prime_count"],
        "hull_count_margin_over_coverage_defect": row["hull_count_margin_over_coverage_defect"],
        "complement_absorption_margin": row["complement_absorption_margin"],
        "complement_pocket_count": row["complement_pocket_count"],
        "complement_pockets": row["complement_pockets"],
    }


def build_result(input_ledger: Path) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    source = load_json(input_ledger)
    max_q = max((row["q_hull_hi"] for row in source["template_records"]), default=2)
    prime_flags = sieve(max_q)
    records = [enrich_template(row, prime_flags) for row in source["template_records"]]
    identity_failures = [row for row in records if not row["identity_all_ok"]]
    count_gate_closed = [row for row in records if row["hull_prime_count_beats_coverage_defect"]]
    count_gate_residual = [row for row in records if not row["hull_prime_count_beats_coverage_defect"]]
    actual_union_void = [row for row in records if row["union_prime_count"] == 0]
    absorption_frontier = sorted(
        records,
        key=lambda row: (
            row["complement_absorption_margin"],
            row["hull_count_margin_over_coverage_defect"],
            -row["depth_over_sqrt_p"],
            row["p"],
        ),
    )
    residual_frontier = sorted(
        count_gate_residual,
        key=lambda row: (
            row["complement_absorption_margin"],
            -row["depth_over_sqrt_p"],
            row["p"],
        ),
    )
    aggregate = {
        "input_ledger": str(input_ledger.relative_to(ROOT)),
        "template_count": len(records),
        "identity_failure_count": len(identity_failures),
        "count_gate_closed_count": len(count_gate_closed),
        "count_gate_residual_count": len(count_gate_residual),
        "actual_union_void_count": len(actual_union_void),
        "min_hull_count_margin_over_coverage_defect": min(
            (row["hull_count_margin_over_coverage_defect"] for row in records),
            default=None,
        ),
        "min_complement_absorption_margin": min((row["complement_absorption_margin"] for row in records), default=None),
        "max_complement_candidate_count": max((row["complement_candidate_count"] for row in records), default=0),
        "max_complement_prime_count": max((row["complement_prime_count"] for row in records), default=0),
        "max_complement_pocket_count": max((row["complement_pocket_count"] for row in records), default=0),
    }
    ledger = {
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "template_records": records,
        "absorption_frontier": [compact_record(row) for row in absorption_frontier],
        "count_gate_residual_frontier": [compact_record(row) for row in residual_frontier],
        "identity_failures": identity_failures,
        "actual_union_void_records": [compact_record(row) for row in actual_union_void],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "certificate_type": "prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router",
        "status": "fixed_shape_union_supply_reduced_to_hull_count_or_complement_absorption_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": source["parameters"],
        "aggregate": aggregate,
        "identity_failure_count": len(identity_failures),
        "actual_union_void_count": len(actual_union_void),
        "absorption_frontier": ledger["absorption_frontier"][:40],
        "count_gate_residual_frontier": ledger["count_gate_residual_frontier"][:40],
        "partition_identity_closed": len(identity_failures) == 0,
        "hull_count_beats_coverage_defect_gate_closed": True,
        "complement_absorption_pdec_registered": True,
        "global_hull_count_or_absorption_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_hull_absorption_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_offband_prefix_gap_shadow_sqrt_input_router.py": sha256(
                SQRT_INPUT_ROUTER
            ),
            "data/square-phase-offband-prefix-gap-shadow-sqrt-input-ledger.json": sha256(input_ledger),
            "data/square-phase-offband-prefix-gap-shadow-hull-absorption-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把固定形状并集素数供给写成精确 hull 分解："
            "`hull primes = target-union primes + complement-pocket primes`，且覆盖缺口候选数就是互补孔袋候选数。"
            "若 `hull_prime_count > coverage_defect_candidate_count`，目标并集必含素数；"
            "否则反例必须表现为互补孔袋吸收全部 hull 素数的显式 PDEC。"
            "有限账本中没有目标并集全空，但全局仍需证明计数胜出或排斥吸收。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase off-band prefix gap shadow hull absorption router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"template_count={agg['template_count']}",
        f"identity_failure_count={agg['identity_failure_count']}",
        f"count_gate_closed_count={agg['count_gate_closed_count']}",
        f"count_gate_residual_count={agg['count_gate_residual_count']}",
        f"actual_union_void_count={agg['actual_union_void_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Hull 分解",
        "",
        "对每个模板，把 hull 内奇候选分成目标并集 `U` 与互补孔袋 `C`：",
        "",
        "```text",
        "Prime(hull) = Prime(U) + Prime(C)",
        "coverage_defect = |C|",
        "```",
        "",
        "因此若 `Prime(hull)>|C|`，即使互补孔袋全是素数，也无法吸收所有 hull 素数，目标并集必含素数。",
        "",
        "## 2. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| template records | {agg['template_count']} |",
        f"| identity failures | {agg['identity_failure_count']} |",
        f"| count-gate closed | {agg['count_gate_closed_count']} |",
        f"| count-gate residual | {agg['count_gate_residual_count']} |",
        f"| actual union void | {agg['actual_union_void_count']} |",
        f"| min hull-count margin | {agg['min_hull_count_margin_over_coverage_defect']} |",
        f"| min complement absorption margin | {agg['min_complement_absorption_margin']} |",
        f"| max complement candidates | {agg['max_complement_candidate_count']} |",
        f"| max complement primes | {agg['max_complement_prime_count']} |",
        f"| max complement pockets | {agg['max_complement_pocket_count']} |",
        "",
        "## 3. 吸收最紧边界",
        "",
        "| P | side | hull | U primes | C primes | C cand | count margin | absorption margin | pockets | atoms |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |",
    ]
    for row in result["absorption_frontier"][:24]:
        pockets = ",".join(f"{pocket['q_lo']}-{pocket['q_hi']}#{pocket['prime_count']}" for pocket in row["complement_pockets"])
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['q_hull_lo']}-{row['q_hull_hi']}`",
                    str(row["union_prime_count"]),
                    str(row["complement_prime_count"]),
                    str(row["coverage_defect_candidate_count"]),
                    str(row["hull_count_margin_over_coverage_defect"]),
                    str(row["complement_absorption_margin"]),
                    f"`{pockets}`",
                    f"`{','.join(row['void_atom_keys'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 4. Count Gate 残余",
            "",
            "| P | side | hull | hull primes | C cand | C primes | U primes | pockets |",
            "| ---: | --- | --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["count_gate_residual_frontier"][:24]:
        pockets = ",".join(f"{pocket['q_lo']}-{pocket['q_hi']}#{pocket['prime_count']}" for pocket in row["complement_pockets"])
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["p"]),
                    f"`{row['side']}`",
                    f"`{row['q_hull_lo']}-{row['q_hull_hi']}`",
                    str(row["hull_prime_count"]),
                    str(row["coverage_defect_candidate_count"]),
                    str(row["complement_prime_count"]),
                    str(row["union_prime_count"]),
                    f"`{pockets}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 命题行",
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
            "## 6. 决策表",
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
            "## 7. 下一步",
            "",
            "- 主攻：`HullPrimeCountBeatsCoverageDefectOrComplementPocketAbsorptionPDEC`。",
            "- 若能证明短 hull 内素数数超过覆盖缺口候选数，则目标并集自动含素数。",
            "- 对 count gate 残余，需排斥互补孔袋吸收全部 hull 素数的 PDEC。",
            "- 当前仍未证明全局行/列无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    parser.add_argument("--input-ledger", type=Path, default=INPUT_LEDGER)
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    input_ledger = args.input_ledger if args.input_ledger.is_absolute() else ROOT / args.input_ledger
    result = build_result(input_ledger)
    write_markdown(result)
    result["source_hashes"][
        "docs/monograph/prime-matrix-square-phase-offband-prefix-gap-shadow-hull-absorption-router.md"
    ] = sha256(OUT_MD)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "template_count": result["aggregate"]["template_count"],
                "count_gate_closed_count": result["aggregate"]["count_gate_closed_count"],
                "count_gate_residual_count": result["aggregate"]["count_gate_residual_count"],
                "actual_union_void_count": result["actual_union_void_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
