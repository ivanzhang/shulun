#!/usr/bin/env python3
"""把半网格总压力硬点压成 no-slot 二次相位带 PDEC。

用法示例：
  python3 experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py --max-p 5000
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.json

输出：
  data/square-phase-halfgrid-noslot-phaseband-pdec-ledger.json
  docs/monograph/prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.json
  docs/monograph/prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from math import isqrt
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SPLIT_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py"
HALFGRID_ROUTER = ROOT / "experiments" / "prime_matrix_square_phase_halfgrid_boundary_word_router.py"

OUT_LEDGER = DATA / "square-phase-halfgrid-noslot-phaseband-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.md"

MAIN_TARGET = "HalfGridSurvivorBeatsActivatedTailSupportOrBoundaryWordPDEC"
NEXT_TARGET = "NoSlotTailPrimePhaseBandDensityPDECExclusion"


def load_split_router() -> Any:
    """加载 no-slot 分裂路由器。"""
    spec = importlib.util.spec_from_file_location("noslot_k0_split_router", SPLIT_ROUTER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SPLIT_ROUTER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def primes_from_flags(flags: bytearray, limit: int | None = None) -> list[int]:
    """从筛表提取素数。"""
    end = len(flags) if limit is None else min(limit + 1, len(flags))
    return [idx for idx in range(2, end) if flags[idx]]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def cutoff_alpha45(p: int) -> int:
    """返回 floor(4P/5)。"""
    return (4 * p) // 5


def tail_phase_gap(p: int, b_value: int, side: str) -> int:
    """返回 no-slot 相位 gap，范围为 1..q。"""
    q_value = p - 2 * b_value
    base_mod = (2 * b_value * b_value) % q_value
    if side == "plus":
        return q_value - base_mod if base_mod else q_value
    if side == "minus":
        return base_mod if base_mod else q_value
    raise ValueError(f"unknown side: {side}")


def phaseband_records(p: int, side: str, primes: list[int]) -> list[dict[str, int]]:
    """返回落入 no-slot 上半相位带的尾素记录。"""
    cutoff = cutoff_alpha45(p)
    half = (p - 1) // 2
    records: list[dict[str, int]] = []
    for q_value in primes:
        if q_value >= p:
            break
        if q_value <= cutoff:
            continue
        b_value = (p - q_value) // 2
        gap = tail_phase_gap(p, b_value, side)
        if gap > half:
            records.append(
                {
                    "q": q_value,
                    "b": b_value,
                    "phase_gap": gap,
                    "gap_minus_half": gap - half,
                    "q_minus_cutoff": q_value - cutoff,
                }
            )
    return records


def audit_side(split: Any, p: int, side: str, primes: list[int], prime_flags: bytearray, pi_prefix: list[int]) -> dict[str, Any]:
    """审计单侧 no-slot 相位带 PDEC。"""
    split_record = split.audit_p(p, prime_flags, pi_prefix)
    halfgrid_survivors = split_record[f"{side}_prime_window"]
    no_slot_load = split_record[f"{side}_no_slot_load"]
    phase_records = phaseband_records(p, side, primes)
    tail_prime_count = sum(1 for q_value in primes if cutoff_alpha45(p) < q_value < p)
    phaseband_count = len(phase_records)
    threshold = (halfgrid_survivors + 1) // 2
    phaseband_pressure = phaseband_count >= threshold
    total_pressure_defect = halfgrid_survivors <= 2 * no_slot_load
    phaseband_density = phaseband_count / tail_prime_count if tail_prime_count else 0.0
    required_density = threshold / tail_prime_count if tail_prime_count else None
    return {
        "p": p,
        "side": side,
        "halfgrid_survivors": halfgrid_survivors,
        "threshold_half_survivors": threshold,
        "tail_prime_count": tail_prime_count,
        "no_slot_load": no_slot_load,
        "phaseband_count": phaseband_count,
        "phaseband_density": phaseband_density,
        "required_phaseband_density_for_defect": required_density,
        "phaseband_identity_ok": no_slot_load == phaseband_count,
        "total_pressure_margin": halfgrid_survivors - 2 * no_slot_load,
        "phaseband_pressure_pdec": phaseband_pressure,
        "total_pressure_defect": total_pressure_defect,
        "pressure_equivalence_ok": phaseband_pressure == total_pressure_defect,
        "top_phaseband_records": sorted(
            phase_records,
            key=lambda row: (row["gap_minus_half"], row["q"]),
            reverse=True,
        )[:10],
    }


def compact(record: dict[str, Any]) -> dict[str, Any]:
    """压缩记录。"""
    return {
        "p": record["p"],
        "side": record["side"],
        "halfgrid_survivors": record["halfgrid_survivors"],
        "threshold_half_survivors": record["threshold_half_survivors"],
        "tail_prime_count": record["tail_prime_count"],
        "no_slot_load": record["no_slot_load"],
        "phaseband_count": record["phaseband_count"],
        "phaseband_density": record["phaseband_density"],
        "required_phaseband_density_for_defect": record["required_phaseband_density_for_defect"],
        "total_pressure_margin": record["total_pressure_margin"],
        "phaseband_pressure_pdec": record["phaseband_pressure_pdec"],
        "top_phaseband_records": record["top_phaseband_records"],
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本步闭合和开放的命题行。"""
    return [
        {
            "name": "noslot_phaseband_identity",
            "status": "closed",
            "statement": "NoSlotLoad_side(P) equals the number of tail primes q=P-2b with delta_side(b)>floor((P-1)/2).",
        },
        {
            "name": "halfgrid_pressure_to_phaseband_pdec",
            "status": "closed",
            "statement": "HalfGridSurvivors_side(P)<=2*NoSlotLoad_side(P) is equivalent to NoSlotPhaseBandCount_side(P)>=ceil(HalfGridSurvivors_side(P)/2).",
        },
        {
            "name": "finite_no_phaseband_pressure_pdec",
            "status": "finite_evidence",
            "statement": "The finite audit finds no no-slot phase-band pressure PDEC up to the tested bound.",
        },
        {
            "name": "phaseband_density_exclusion",
            "status": "open",
            "statement": "A global proof still needs to exclude the tail-prime phase-band density needed to cover half of the half-grid survivors, or route it to PDEC/SAE/ColumnCRT.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "NoSlotPhaseBandIdentityClosed",
            "closed": result["phaseband_identity_failure_count"] == 0,
            "proved": True,
            "meaning": "`NoSlotLoad` 已完全等价为尾素二次相位 gap 落入上半带。",
            "remaining": "closed",
        },
        {
            "gate": "PressureDefectEqualsPhaseBandPDECClosed",
            "closed": result["pressure_equivalence_failure_count"] == 0,
            "proved": True,
            "meaning": "最新总压力反例等价于 no-slot 相位带尾素数达到半个半网格幸存数。",
            "remaining": "closed",
        },
        {
            "gate": "FiniteNoPhaseBandPressurePDEC",
            "closed": result["phaseband_pressure_pdec_count"] == 0,
            "proved": False,
            "meaning": f"有限扫描 P<={result['parameters']['max_p']} 中没有相位带压力 PDEC。",
            "remaining": "finite evidence only",
        },
        {
            "gate": "GlobalPhaseBandDensityExcluded",
            "closed": False,
            "proved": False,
            "meaning": "仍需全局排斥尾素二次相位上半带密度异常。",
            "remaining": NEXT_TARGET,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "本步只把最新硬点压成唯一相位带 PDEC，不关闭全局行/列命题。",
            "remaining": NEXT_TARGET,
        },
    ]


def build_result(max_p: int, sample_ps: list[int]) -> dict[str, Any]:
    """构造路由器结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    split = load_split_router()
    prime_flags = split.sieve(max_p * max_p + max_p)
    pi_prefix = split.prime_prefix(prime_flags)
    small_flags = sieve(max_p)
    primes = primes_from_flags(small_flags, max_p)
    p_values = [p for p in primes if p >= 3]
    records = [
        audit_side(split, p, side, primes, prime_flags, pi_prefix)
        for p in p_values
        for side in ("plus", "minus")
    ]
    identity_failures = [record for record in records if not record["phaseband_identity_ok"]]
    equivalence_failures = [record for record in records if not record["pressure_equivalence_ok"]]
    phaseband_pdecs = [record for record in records if record["phaseband_pressure_pdec"]]
    frontier = sorted(records, key=lambda record: (record["total_pressure_margin"], record["p"], record["side"]))
    max_phaseband_density = max(records, key=lambda record: record["phaseband_density"], default=None)
    max_required_density = max(
        (record for record in records if record["required_phaseband_density_for_defect"] is not None),
        key=lambda record: record["required_phaseband_density_for_defect"],
        default=None,
    )
    sample_set = set(sample_ps)
    sample_records = [record for record in records if record["p"] in sample_set]
    aggregate = {
        "record_count": len(records),
        "combined_halfgrid_survivors": sum(record["halfgrid_survivors"] for record in records),
        "combined_tail_prime_count": sum(record["tail_prime_count"] for record in records),
        "combined_phaseband_count": sum(record["phaseband_count"] for record in records),
        "phaseband_identity_failure_count": len(identity_failures),
        "pressure_equivalence_failure_count": len(equivalence_failures),
        "phaseband_pressure_pdec_count": len(phaseband_pdecs),
        "min_total_pressure_margin": frontier[0]["total_pressure_margin"] if frontier else None,
        "max_phaseband_density": max_phaseband_density["phaseband_density"] if max_phaseband_density else None,
        "max_required_phaseband_density_for_defect": (
            max_required_density["required_phaseband_density_for_defect"] if max_required_density else None
        ),
    }
    ledger = {
        "parameters": {"max_p": max_p, "sample_ps": sample_ps},
        "prime_count": len(p_values),
        "aggregate": aggregate,
        "frontier_records": [compact(record) for record in frontier[:80]],
        "max_phaseband_density_record": compact(max_phaseband_density) if max_phaseband_density else None,
        "max_required_density_record": compact(max_required_density) if max_required_density else None,
        "sample_records": [compact(record) for record in sample_records],
        "phaseband_identity_failures": [compact(record) for record in identity_failures[:20]],
        "pressure_equivalence_failures": [compact(record) for record in equivalence_failures[:20]],
        "phaseband_pressure_pdec_records": [compact(record) for record in phaseband_pdecs[:40]],
    }
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "certificate_type": "prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router",
        "status": "halfgrid_pressure_reduced_to_noslot_tailprime_phaseband_density_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "parameters": ledger["parameters"],
        "finite_prime_count": len(p_values),
        "aggregate": aggregate,
        "phaseband_identity_failure_count": len(identity_failures),
        "pressure_equivalence_failure_count": len(equivalence_failures),
        "phaseband_pressure_pdec_count": len(phaseband_pdecs),
        "frontier_records": ledger["frontier_records"][:20],
        "max_phaseband_density_record": ledger["max_phaseband_density_record"],
        "max_required_density_record": ledger["max_required_density_record"],
        "sample_records": ledger["sample_records"],
        "noslot_phaseband_identity_closed": len(identity_failures) == 0,
        "pressure_phaseband_equivalence_closed": len(equivalence_failures) == 0,
        "finite_no_phaseband_pressure_pdec": len(phaseband_pdecs) == 0,
        "global_phaseband_density_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": MAIN_TARGET,
        "hardpoint_after_router": NEXT_TARGET,
        "next_direct_attack_target": NEXT_TARGET,
        "theorem_rows": theorem_rows(),
        "source_hashes": {
            "experiments/prime_matrix_square_phase_halfgrid_noslot_phaseband_pdec_router.py": sha256(
                Path(__file__).resolve()
            ),
            "experiments/prime_matrix_square_phase_noslot_k0_rootwindow_split_router.py": sha256(SPLIT_ROUTER),
            "experiments/prime_matrix_square_phase_halfgrid_boundary_word_router.py": sha256(HALFGRID_ROUTER),
            "data/square-phase-halfgrid-noslot-phaseband-pdec-ledger.json": sha256(OUT_LEDGER),
        },
        "plain_conclusion": (
            "本步把 `HalfGridSurvivors>2*NoSlotLoad` 的剩余硬点压成唯一 no-slot 二次相位带 PDEC。"
            "对尾素 `q=P-2b`，令 `delta_plus(b)` 为 `-2b^2 mod q` 的正代表，"
            "`delta_minus(b)` 为 `2b^2 mod q` 的正代表。"
            "无槽条件精确等价于 `delta_side(b)>(P-1)/2`。"
            "因此总压力反例等价于落入该上半相位带的尾素数量至少达到半个半网格幸存数。"
            "有限扫描未出现此 PDEC；全局仍需排斥该二次相位带密度异常，或将持久异常送入 PDEC/SAE/ColumnCRT。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    agg = result["aggregate"]
    lines = [
        "# Prime Matrix square-phase half-grid no-slot phase-band PDEC router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"max_p={result['parameters']['max_p']}",
        f"finite_prime_count={result['finite_prime_count']}",
        f"phaseband_identity_failure_count={result['phaseband_identity_failure_count']}",
        f"pressure_equivalence_failure_count={result['pressure_equivalence_failure_count']}",
        f"phaseband_pressure_pdec_count={result['phaseband_pressure_pdec_count']}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 二次相位带正规形",
        "",
        "尾素写成 `q=P-2b`，`h=(P-1)/2`。定义",
        "",
        "```text",
        "delta_plus(b)  = least positive residue of -2b^2 mod q,",
        "delta_minus(b) = least positive residue of  2b^2 mod q.",
        "```",
        "",
        "则该尾素在对应方向没有可用半网格槽，当且仅当",
        "",
        "```text",
        "delta_side(b) > h.",
        "```",
        "",
        "于是 `NoSlotLoad` 不再是抽象负载，而是尾素在一个显式二次相位上半带中的计数。",
        "",
        "## 2. 压力反例等价式",
        "",
        "上一层目标为",
        "",
        "```text",
        "HalfGridSurvivors_side(P) > 2*NoSlotLoad_side(P).",
        "```",
        "",
        "由于 `NoSlotLoad=NoSlotPhaseBandCount`，失败当且仅当",
        "",
        "```text",
        "NoSlotPhaseBandCount_side(P) >= ceil(HalfGridSurvivors_side(P)/2).",
        "```",
        "",
        "这就是当前唯一剩余 PDEC。",
        "",
        "## 3. 有限审计摘要",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| record count | {agg['record_count']} |",
        f"| combined half-grid survivors | {agg['combined_halfgrid_survivors']} |",
        f"| combined tail prime count | {agg['combined_tail_prime_count']} |",
        f"| combined phase-band count | {agg['combined_phaseband_count']} |",
        f"| identity failures | {agg['phaseband_identity_failure_count']} |",
        f"| pressure equivalence failures | {agg['pressure_equivalence_failure_count']} |",
        f"| phase-band pressure PDEC count | {agg['phaseband_pressure_pdec_count']} |",
        f"| min total pressure margin | {agg['min_total_pressure_margin']} |",
        f"| max phase-band density | {agg['max_phaseband_density']:.6f} |",
        f"| max required density for defect | {agg['max_required_phaseband_density_for_defect']:.6f} |",
        "",
        "## 4. 边界记录",
        "",
        "| label | P | side | H | threshold | tail primes | phase-band | density | required density | margin |",
        "| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    boundary_rows = [
        ("worst margin", result["frontier_records"][0] if result["frontier_records"] else None),
        ("max phase density", result["max_phaseband_density_record"]),
        ("max required density", result["max_required_density_record"]),
    ]
    for label, record in boundary_rows:
        if not record:
            continue
        required = record["required_phaseband_density_for_defect"]
        lines.append(
            "| "
            + " | ".join(
                [
                    label,
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["threshold_half_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["phaseband_count"]),
                    f"{record['phaseband_density']:.6f}",
                    "None" if required is None else f"{required:.6f}",
                    str(record["total_pressure_margin"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 样本表",
            "",
            "| P | side | H | tail primes | phase-band | density | margin | top phase records |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for record in result["sample_records"][:24]:
        top = ",".join(f"{item['q']}:{item['gap_minus_half']}" for item in record["top_phaseband_records"][:5])
        lines.append(
            "| "
            + " | ".join(
                [
                    str(record["p"]),
                    f"`{record['side']}`",
                    str(record["halfgrid_survivors"]),
                    str(record["tail_prime_count"]),
                    str(record["phaseband_count"]),
                    f"{record['phaseband_density']:.6f}",
                    str(record["total_pressure_margin"]),
                    f"`{top}`",
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
            "- 主攻：`NoSlotTailPrimePhaseBandDensityPDECExclusion`。",
            "- 也就是排斥尾素 `q=P-2b` 在二次相位上半带中的密度高到覆盖半个 half-grid survivor 数。",
            "- 若不能直接排斥，应将持久高密度相位带登记为 PDEC、端点 SAE 或 ColumnCRT。",
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
        default="13,17,19,23,29,31,101,499,1009,2003,4999",
    )
    return parser.parse_args()


def main() -> None:
    """入口函数。"""
    args = parse_args()
    sample_ps = [int(item) for item in args.sample_ps.split(",") if item.strip()]
    result = build_result(args.max_p, sample_ps)
    write_markdown(result)
    result["source_hashes"]["docs/monograph/prime-matrix-square-phase-halfgrid-noslot-phaseband-pdec-router.md"] = sha256(
        OUT_MD
    )
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "max_p": args.max_p,
                "phaseband_identity_failure_count": result["phaseband_identity_failure_count"],
                "pressure_equivalence_failure_count": result["pressure_equivalence_failure_count"],
                "phaseband_pressure_pdec_count": result["phaseband_pressure_pdec_count"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
