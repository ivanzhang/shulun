#!/usr/bin/env python3
"""Prime Matrix anchor-collar 幸存者恒等分解路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_collar_survivor_identity_router.py
  python3 experiments/prime_matrix_anchor_collar_survivor_identity_router.py --p-list 101,499,997,1999 --format table

输出：
  docs/monograph/prime-matrix-anchor-collar-survivor-identity-router.json
  docs/monograph/prime-matrix-anchor-collar-survivor-identity-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from array import array
from math import isqrt, log
from pathlib import Path
from typing import Any

from prime_matrix_cylindrical_completion_audit import primes_upto, small_factor_table


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-contradiction-matrix-router.json"
DEFAULT_ANCHOR = DOCS / "prime-matrix-early-zero-anchor-collar-router.json"
DEFAULT_EDA = DOCS / "prime-matrix-eda-gap-barrier-and-dual-route.md"
DEFAULT_DIMENSION = DOCS / "prime-matrix-diagonal-postsquare-primepair-dimension-gap.md"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-collar-survivor-identity-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-collar-survivor-identity-router.md"


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的素数列表。"""
    return [int(part) for part in raw.split(",") if part.strip()]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def fmt_float(value: float | None) -> str:
    """稳定输出浮点数。"""
    if value is None:
        return "NA"
    return f"{value:.6f}"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row_survivor_identity(p: int, x: int, spf: array) -> dict[str, Any]:
    """计算 x>=sqrt(P) 行的 R_x 精确分解。"""
    rough_count = 0
    prime_survivors = 0
    semiprime_fibers = 0
    bad_composite_after_sqrt_gate = 0
    bad_anchor_after_collar = 0
    fiber_loads: dict[int, int] = {}
    anchor_top = isqrt((x + 1) * p - 1)

    for column in range(1, p):
        value = x * p + column
        factor = spf[value]
        if factor and factor <= x:
            continue
        rough_count += 1
        if factor == 0:
            prime_survivors += 1
            continue

        cofactor = value // factor
        semiprime_fibers += 1
        if cofactor < p and spf[cofactor] != 0:
            # x>=sqrt(P) 时这里按定理不应发生；只用于实现审计。
            bad_composite_after_sqrt_gate += 1
        anchor = min(factor, cofactor)
        if not (x < anchor <= anchor_top):
            bad_anchor_after_collar += 1
        fiber_loads[anchor] = fiber_loads.get(anchor, 0) + 1

    identity_margin = rough_count - semiprime_fibers
    return {
        "x": x,
        "h": p - x,
        "rough_count": rough_count,
        "prime_survivors": prime_survivors,
        "canonical_semiprime_fibers": semiprime_fibers,
        "identity_margin": identity_margin,
        "identity_holds": identity_margin == prime_survivors,
        "bad_composite_after_sqrt_gate": bad_composite_after_sqrt_gate,
        "bad_anchor_after_collar": bad_anchor_after_collar,
        "distinct_anchor_count": len(fiber_loads),
        "max_fiber_load": max(fiber_loads.values(), default=0),
        "semiprime_share_of_rough": None if rough_count == 0 else semiprime_fibers / rough_count,
        "prime_share_of_rough": None if rough_count == 0 else prime_survivors / rough_count,
        "rough_constant_logx": None if x <= 1 else rough_count * log(x) / p,
        "semiprime_constant_logp": semiprime_fibers * log(p) / p,
        "prime_constant_logp": prime_survivors * log(p) / p,
    }


def audit_p(p: int, sample_limit: int) -> dict[str, Any]:
    """审计单个 P 的幸存者恒等分解。"""
    spf = small_factor_table(p)
    sqrt_p = isqrt(p)
    rows = [row_survivor_identity(p, x, spf) for x in range(sqrt_p, p)]
    if not rows:
        return {
            "p": p,
            "sqrt_p": sqrt_p,
            "row_count": 0,
            "all_identity_holds": True,
            "all_sqrt_gate_clean": True,
            "all_anchor_collar_clean": True,
            "rows": [],
        }

    min_prime_survivors = min(row["prime_survivors"] for row in rows)
    max_semiprime_share = max(row["semiprime_share_of_rough"] or 0.0 for row in rows)
    max_fiber_load = max(row["max_fiber_load"] for row in rows)
    min_rough_constant = min(row["rough_constant_logx"] or 0.0 for row in rows)
    max_semiprime_constant = max(row["semiprime_constant_logp"] for row in rows)
    worst_prime_rows = [row for row in rows if row["prime_survivors"] == min_prime_survivors][
        :sample_limit
    ]
    densest_semiprime_rows = sorted(
        rows,
        key=lambda row: (row["semiprime_share_of_rough"] or 0.0, row["canonical_semiprime_fibers"]),
        reverse=True,
    )[:sample_limit]
    return {
        "p": p,
        "sqrt_p": sqrt_p,
        "x_range": [sqrt_p, p - 1],
        "row_count": len(rows),
        "all_identity_holds": all(row["identity_holds"] for row in rows),
        "all_sqrt_gate_clean": all(row["bad_composite_after_sqrt_gate"] == 0 for row in rows),
        "all_anchor_collar_clean": all(row["bad_anchor_after_collar"] == 0 for row in rows),
        "min_prime_survivors": min_prime_survivors,
        "max_semiprime_share": max_semiprime_share,
        "max_fiber_load": max_fiber_load,
        "min_rough_constant_logx": min_rough_constant,
        "max_semiprime_constant_logp": max_semiprime_constant,
        "worst_prime_rows": worst_prime_rows,
        "densest_semiprime_rows": densest_semiprime_rows,
    }


def audit_samples(p_values: list[int], sample_limit: int) -> dict[str, Any]:
    """审计多个样本 P。"""
    prime_set = set(primes_upto(max(p_values) if p_values else 2))
    rows = []
    skipped = []
    for p in p_values:
        if p < 3 or p not in prime_set:
            skipped.append(p)
            continue
        rows.append(audit_p(p, sample_limit))
    return {
        "p_values": p_values,
        "skipped_nonprimes": skipped,
        "status": "anchor_collar_survivor_identity_sample_verified",
        "all_identity_holds": all(row["all_identity_holds"] for row in rows),
        "all_sqrt_gate_clean": all(row["all_sqrt_gate_clean"] for row in rows),
        "all_anchor_collar_clean": all(row["all_anchor_collar_clean"] for row in rows),
        "rows": rows,
    }


def proof_rows(anchor: dict[str, Any], eda_text: str, dimension_text: str) -> list[dict[str, Any]]:
    """生成幸存者恒等分解判定账本。"""
    return [
        {
            "gate": "AnchorCollarImported",
            "closed": anchor.get("canonical_anchor_collar_closed") is True,
            "proved": True,
            "meaning": "上一轮已证明 x>=sqrt(P) 的高补洞只能来自 canonical anchor collar。",
            "output": "可对 R_x 做无损分解。",
        },
        {
            "gate": "RoughPrimeSemiprimePartition",
            "closed": True,
            "proved": True,
            "meaning": "若 x>=sqrt(P)，n<xP+P<P^2 且没有 <=x 因子，则 n 只能是素数或两个 >x 素数的乘积。",
            "output": "R_x = PrimeSurvivors_x disjoint_union SemiprimeFibers_x。",
        },
        {
            "gate": "FiberSupportEqualsSemiprimeSet",
            "closed": True,
            "proved": True,
            "meaning": "canonical q-fiber 恰好枚举上述双素乘积列；q,m 互换只计一次。",
            "output": "短纤维容量不是外估计，而是 SemiprimeFibers_x 的精确支撑。",
        },
        {
            "gate": "CapacityGapEqualsPrimeSurvivors",
            "closed": True,
            "proved": True,
            "meaning": "|R_x|-|canonical fibers| = PrimeSurvivors_x。",
            "output": "AnchorCollarShortPrimeFiberUpperBound 等价于 PrimeSurvivors_x>0。",
        },
        {
            "gate": "EarlyZeroEquivalentPrimeFreeIntervalLargeBranch",
            "closed": True,
            "proved": True,
            "meaning": "在 x>=sqrt(P) 分支，早期零行等价于该 P 对齐短区间没有素数幸存者。",
            "output": "不能再把短纤维容量当作比 EDA 更弱的纯计数问题。",
        },
        {
            "gate": "EDABarrierCompatibility",
            "closed": "EDA(p)<=>PrimeGap(p)" in eda_text
            and "短区间素数屏障" in eda_text,
            "proved": True,
            "meaning": "该分解与已有 EDA-Gap Barrier 一致：自足闭合仍需要 CRT 对偶下界或缺陷回流。",
            "output": "AnchorCollarPrimeSurvivorLowerBoundOrDefectReturn。",
        },
        {
            "gate": "DimensionGapRouteCompatibility",
            "closed": "低筛骨架是一维筛主量" in dimension_text
            and "倒数地板素对覆盖是二维筛上界" in dimension_text,
            "proved": True,
            "meaning": "可用的非循环攻法是证明一维粗骨架下界大于二维素对纤维上界，或失败进入 PDEC/Tail-anchor。",
            "output": "VariableRowRoughSkeletonVsPrimePairFiberDimensionGap。",
        },
        {
            "gate": "UnconditionalPrimeSurvivorLowerBound",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明所有 sqrt(P)<=x<P 均有 PrimeSurvivors_x>0。",
            "output": "PrimeSurvivorLowerBoundOrPDECSAEColumnReturn。",
        },
    ]


def run(
    previous_path: Path,
    anchor_path: Path,
    eda_path: Path,
    dimension_path: Path,
    p_values: list[int],
    sample_limit: int,
) -> dict[str, Any]:
    """执行 anchor-collar 幸存者恒等分解路由。"""
    previous = load_json(previous_path)
    anchor = load_json(anchor_path)
    eda_text = eda_path.read_text(encoding="utf-8")
    dimension_text = dimension_path.read_text(encoding="utf-8")
    sample_audit = audit_samples(p_values, sample_limit)
    paths = [previous_path, anchor_path, eda_path, dimension_path]
    rows = proof_rows(anchor=anchor, eda_text=eda_text, dimension_text=dimension_text)
    return {
        "certificate_type": "anchor_collar_survivor_identity_router",
        "status": "anchor_collar_capacity_reduced_to_prime_survivor_or_named_defect",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "sample_audit": sample_audit,
        "previous_frontier": previous.get("strongest_current_frontier"),
        "anchor_collar_survivor_identity_closed": True,
        "capacity_gap_equals_prime_survivors_closed": True,
        "anchor_collar_short_fiber_capacity_closed": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_after_router": "PrimeSurvivorLowerBoundOrPDECSAEColumnReturn",
        "terminal_gap_expansion": [
            "VariableRowRoughSkeletonLowerBound",
            "VariableRowPrimePairFiberUpperBound",
            "PrimeFreeIntervalLowModPDECDefectReturn",
            "SparsePrimeSurvivorOrLocalSAEExclusion",
            "ColumnDisplacementReusePDECReturn",
        ],
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "exact_identity": (
            "For sqrt(P)<=x<P, R_x splits disjointly into actual primes in "
            "(xP,(x+1)P) and canonical anchor-collar semiprimes qm with x<q<=m<P. "
            "Therefore |R_x|-|SemiprimeFibers_x| equals the prime survivor count."
        ),
        "plain_conclusion": (
            "本步把 anchor-collar 短纤维容量硬点做成无损恒等式："
            "`R_x` 精确等于素数幸存列与 canonical 双素纤维的并。"
            "因此“短纤维不能覆盖全部 R_x”等价于“该 P 对齐短区间至少有一个素数幸存”。"
            "这不是终局证明，但它排除了继续把纤维容量当作更弱纯计数问题的退路；"
            "下一步必须证明变量行一维粗骨架和二维素对纤维的维数差，或把素数幸存为零送入 PDEC/SAE/ColumnCRT。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    sample = result["sample_audit"]
    lines = [
        "# Prime Matrix anchor-collar 幸存者恒等分解路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"anchor_collar_survivor_identity_closed={fmt_bool(result['anchor_collar_survivor_identity_closed'])}",
        f"capacity_gap_equals_prime_survivors_closed={fmt_bool(result['capacity_gap_equals_prime_survivors_closed'])}",
        f"anchor_collar_short_fiber_capacity_closed={fmt_bool(result['anchor_collar_short_fiber_capacity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 精确分解",
        "",
        "固定奇素数 `P` 与 `sqrt(P)<=x<P`。令 `R_x` 为第 `x` 行中没有 `<=x` 素因子的列：",
        "",
        "```text",
        "R_x={1<=c<P: P^-(xP+c)>x or xP+c is prime}.",
        "```",
        "",
        "因为 `xP+c<(x+1)P<=P^2`，任一 `c in R_x` 只有两种可能：",
        "",
        "```text",
        "xP+c is prime;",
        "xP+c=q m,  x<q<=m<P,  q,m prime.",
        "```",
        "",
        "第二种正是上一轮 canonical anchor collar 的短纤维支撑。因此有无损恒等式：",
        "",
        "```text",
        "R_x = PrimeSurvivors_x disjoint_union SemiprimeFibers_x",
        "|R_x|-|SemiprimeFibers_x| = |PrimeSurvivors_x|.",
        "```",
        "",
        "所以在 `x>=sqrt(P)` 分支，早期零行等价于 `PrimeSurvivors_x=empty`。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | output |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{output}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                proved=fmt_bool(bool(row["proved"])),
                meaning=table_cell(row["meaning"]),
                output=table_cell(row["output"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 样本审计",
            "",
            "样本只验证实现口径；上面的分解由唯一分解和 `x>=sqrt(P)` 直接证明。",
            "",
            "```text",
            f"sample_status={sample['status']}",
            f"all_identity_holds={fmt_bool(sample['all_identity_holds'])}",
            f"all_sqrt_gate_clean={fmt_bool(sample['all_sqrt_gate_clean'])}",
            f"all_anchor_collar_clean={fmt_bool(sample['all_anchor_collar_clean'])}",
            "```",
            "",
            "| P | rows | min prime survivors | max semiprime share | max fiber load | min rough logx/P | max semiprime logP/P |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in sample["rows"]:
        lines.append(
            "| {p} | {rows} | {prime} | {share} | {fiber} | {rough_c} | {semi_c} |".format(
                p=row["p"],
                rows=row["row_count"],
                prime=row["min_prime_survivors"],
                share=fmt_float(row["max_semiprime_share"]),
                fiber=row["max_fiber_load"],
                rough_c=fmt_float(row["min_rough_constant_logx"]),
                semi_c=fmt_float(row["max_semiprime_constant_logp"]),
            )
        )
    lines.extend(
        [
            "",
            "最弱素数幸存行示例：",
            "",
            "| P | x | rough | semiprime fibers | prime survivors | semiprime share |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for record in sample["rows"]:
        for row in record["worst_prime_rows"]:
            lines.append(
                "| {p} | {x} | {rough} | {semi} | {prime} | {share} |".format(
                    p=record["p"],
                    x=row["x"],
                    rough=row["rough_count"],
                    semi=row["canonical_semiprime_fibers"],
                    prime=row["prime_survivors"],
                    share=fmt_float(row["semiprime_share_of_rough"]),
                )
            )
    lines.extend(
        [
            "",
            "## 4. 结构结论",
            "",
            "本步说明：",
            "",
            "```text",
            "AnchorCollarShortPrimeFiberUpperBound",
            "  <=> PrimeSurvivors_x>0 on every sqrt(P)<=x<P row.",
            "```",
            "",
            "因此继续直接数 q-fiber 总容量不会绕开短区间素数屏障。可继续硬攻的非循环方向是变量行维数差：",
            "",
            "```text",
            "G_x(P)=#R_x                       一维粗骨架",
            "B_x(P)=#SemiprimeFibers_x          二维素对纤维",
            "PrimeSurvivors_x=G_x(P)-B_x(P).",
            "```",
            "",
            "若能证明 `G_x(P)>B_x(P)`，则该行闭合；若失败，则失败必须表现为低模骨架亏损、素对纤维过密、",
            "孤立幸存者逃逸或固定列位移复用，并分别回流 `PDEC/SAE/ColumnCRT`。",
            "",
            "## 5. 新最窄剩余",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = VariableRowRoughSkeletonLowerBound",
            "    AND VariableRowPrimePairFiberUpperBound",
            "    AND PrimeFreeIntervalLowModPDECDefectReturn",
            "    AND SparsePrimeSurvivorOrLocalSAEExclusion",
            "    AND ColumnDisplacementReusePDECReturn.",
            "```",
            "",
            "这一步不是终局闭合；它把 anchor-collar 的容量语言压成了精确的素数幸存/维数差语言。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_table(result: dict[str, Any]) -> None:
    """输出审计简表。"""
    print(
        "p rows min_prime_survivors max_semiprime_share max_fiber_load "
        "min_rough_logx_over_p max_semiprime_logp_over_p",
        flush=True,
    )
    for row in result["sample_audit"]["rows"]:
        print(
            f"{row['p']} {row['row_count']} {row['min_prime_survivors']} "
            f"{row['max_semiprime_share']:.6f} {row['max_fiber_load']} "
            f"{row['min_rough_constant_logx']:.6f} {row['max_semiprime_constant_logp']:.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--anchor-json", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--eda-md", type=Path, default=DEFAULT_EDA)
    parser.add_argument("--dimension-md", type=Path, default=DEFAULT_DIMENSION)
    parser.add_argument("--p-list", type=str, default="101,499,997,1999")
    parser.add_argument("--sample-limit", type=int, default=3)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--format", choices=("write", "json", "table"), default="write")
    args = parser.parse_args()
    result = run(
        previous_path=args.previous_json,
        anchor_path=args.anchor_json,
        eda_path=args.eda_md,
        dimension_path=args.dimension_md,
        p_values=parse_p_list(args.p_list),
        sample_limit=args.sample_limit,
    )
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True), flush=True)
        return
    if args.format == "table":
        print_table(result)
        return
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)


if __name__ == "__main__":
    main()
