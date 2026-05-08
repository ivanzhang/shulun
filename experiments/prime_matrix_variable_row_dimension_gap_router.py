#!/usr/bin/env python3
"""Prime Matrix 变量行维数差路由器。

用法示例：
  python3 experiments/prime_matrix_variable_row_dimension_gap_router.py
  python3 experiments/prime_matrix_variable_row_dimension_gap_router.py --p-list 101,499,997,1999 --format table

输出：
  docs/monograph/prime-matrix-variable-row-dimension-gap-router.json
  docs/monograph/prime-matrix-variable-row-dimension-gap-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-anchor-collar-survivor-identity-router.json"
DEFAULT_ENDPOINT_DG = DOCS / "prime-matrix-diagonal-postsquare-primepair-dimension-gap.md"
DEFAULT_EDA = DOCS / "prime-matrix-eda-gap-barrier-and-dual-route.md"
DEFAULT_JSON = DOCS / "prime-matrix-variable-row-dimension-gap-router.json"
DEFAULT_MD = DOCS / "prime-matrix-variable-row-dimension-gap-router.md"


BUCKETS = [
    (0.50, 0.60),
    (0.60, 0.70),
    (0.70, 0.80),
    (0.80, 0.90),
    (0.90, 1.01),
]


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


def row_dimension_stats(p: int, x: int, spf: array) -> dict[str, Any]:
    """统计一行的粗骨架、双素纤维与素数幸存维数差。"""
    rough = 0
    semiprime = 0
    prime = 0
    bad_identity = 0
    max_anchor = isqrt((x + 1) * p - 1)
    fiber_loads: dict[int, int] = {}

    for column in range(1, p):
        value = x * p + column
        factor = spf[value]
        if factor and factor <= x:
            continue
        rough += 1
        if factor == 0:
            prime += 1
            continue
        cofactor = value // factor
        anchor = min(factor, cofactor)
        if not (x < anchor <= max_anchor):
            bad_identity += 1
        semiprime += 1
        fiber_loads[anchor] = fiber_loads.get(anchor, 0) + 1

    alpha = log(x) / log(p)
    return {
        "x": x,
        "alpha": alpha,
        "rough": rough,
        "semiprime": semiprime,
        "prime": prime,
        "gap": rough - semiprime,
        "identity_holds": rough - semiprime == prime and bad_identity == 0,
        "bad_identity": bad_identity,
        "semiprime_share": None if rough == 0 else semiprime / rough,
        "prime_share": None if rough == 0 else prime / rough,
        "max_fiber_load": max(fiber_loads.values(), default=0),
        "distinct_anchor_count": len(fiber_loads),
        "rough_logx_over_p": rough * log(x) / p,
        "semiprime_logx_over_p": semiprime * log(x) / p,
        "prime_logx_over_p": prime * log(x) / p,
        "rough_logp_over_p": rough * log(p) / p,
        "semiprime_logp_over_p": semiprime * log(p) / p,
        "prime_logp_over_p": prime * log(p) / p,
    }


def bucket_label(alpha: float) -> str:
    """返回 alpha 桶标签。"""
    for lo, hi in BUCKETS:
        if lo <= alpha < hi:
            return f"{lo:.2f}-{hi:.2f}"
    return "out"


def summarize_bucket(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总 alpha 桶。"""
    if not rows:
        return {
            "count": 0,
            "min_prime": None,
            "max_semiprime_share": None,
            "min_prime_share": None,
            "min_gap": None,
            "max_fiber_load": None,
        }
    return {
        "count": len(rows),
        "min_prime": min(row["prime"] for row in rows),
        "min_gap": min(row["gap"] for row in rows),
        "max_semiprime_share": max(row["semiprime_share"] or 0.0 for row in rows),
        "min_prime_share": min(row["prime_share"] or 0.0 for row in rows),
        "max_fiber_load": max(row["max_fiber_load"] for row in rows),
        "min_prime_logx_over_p": min(row["prime_logx_over_p"] for row in rows),
        "max_semiprime_logx_over_p": max(row["semiprime_logx_over_p"] for row in rows),
    }


def audit_p(p: int, sample_limit: int) -> dict[str, Any]:
    """审计单个 P 的变量行维数差。"""
    spf = small_factor_table(p)
    sqrt_p = isqrt(p)
    rows = [row_dimension_stats(p, x, spf) for x in range(sqrt_p, p)]
    buckets: dict[str, list[dict[str, Any]]] = {f"{lo:.2f}-{hi:.2f}": [] for lo, hi in BUCKETS}
    for row in rows:
        label = bucket_label(row["alpha"])
        if label in buckets:
            buckets[label].append(row)
    worst_prime_rows = sorted(rows, key=lambda row: (row["prime"], row["x"]))[:sample_limit]
    highest_semiprime_rows = sorted(
        rows,
        key=lambda row: (row["semiprime_share"] or 0.0, row["semiprime"]),
        reverse=True,
    )[:sample_limit]
    return {
        "p": p,
        "sqrt_p": sqrt_p,
        "x_range": [sqrt_p, p - 1],
        "row_count": len(rows),
        "all_identity_holds": all(row["identity_holds"] for row in rows),
        "min_prime": min(row["prime"] for row in rows),
        "min_gap": min(row["gap"] for row in rows),
        "max_semiprime_share": max(row["semiprime_share"] or 0.0 for row in rows),
        "min_prime_share": min(row["prime_share"] or 0.0 for row in rows),
        "max_fiber_load": max(row["max_fiber_load"] for row in rows),
        "min_prime_logx_over_p": min(row["prime_logx_over_p"] for row in rows),
        "max_semiprime_logx_over_p": max(row["semiprime_logx_over_p"] for row in rows),
        "bucket_summary": {label: summarize_bucket(bucket_rows) for label, bucket_rows in buckets.items()},
        "worst_prime_rows": worst_prime_rows,
        "highest_semiprime_rows": highest_semiprime_rows,
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
        "status": "variable_row_dimension_gap_sample_verified_router_open",
        "all_identity_holds": all(row["all_identity_holds"] for row in rows),
        "global_min_prime": min((row["min_prime"] for row in rows), default=None),
        "global_max_semiprime_share": max((row["max_semiprime_share"] for row in rows), default=None),
        "rows": rows,
    }


def proof_rows(previous: dict[str, Any], endpoint_text: str, eda_text: str) -> list[dict[str, Any]]:
    """生成变量行维数差路由账本。"""
    return [
        {
            "gate": "PrimeSurvivorIdentityImported",
            "closed": previous.get("capacity_gap_equals_prime_survivors_closed") is True,
            "proved": True,
            "meaning": "上一轮已证明 G_x(P)-B_x(P) 精确等于素数幸存数。",
            "output": "变量行维数差是等价目标，不是启发式近似。",
        },
        {
            "gate": "ExactVariableFiberFormula",
            "closed": True,
            "proved": True,
            "meaning": "B_x(P) 可精确写成 collar 中 q 的短素数窗口求和。",
            "output": "B_x(P)=sum_{x<q<sqrt((x+1)P)} #{prime m in I_{x,q}}。",
        },
        {
            "gate": "EndpointDimensionGapDoesNotUniformlyLift",
            "closed": True,
            "proved": True,
            "meaning": "端点 x=P 的 B(P)=O(P/log^2 P) 依赖 m 窗口长度 O(1)；x≈sqrt(P) 时 B_x(P) 与 G_x(P) 同为 P/log P 量级。",
            "output": "不能把端点常数合同直接用于全部变量行。",
        },
        {
            "gate": "TwoBranchSupportShape",
            "closed": True,
            "proved": True,
            "meaning": "因 x>=sqrt(P) 且 xP+c<P^2，R_x 的合数只能有两个 >x 素因子；支撑上只有一素分支与双素分支。",
            "output": "自足证明应瞄准一素分支正性或缺陷回流。",
        },
        {
            "gate": "UniformBuchstabConstants",
            "closed": False,
            "proved": False,
            "meaning": "u=log(xP)/log(x)=1+1/alpha 属于 [2,3]，但尚未证明全 alpha 的 Buchstab 常数账本和误差项。",
            "output": "UniformBuchstabOnePrimeBranchLowerBound。",
        },
        {
            "gate": "EndpointContractCompatibility",
            "closed": "低筛骨架是一维筛主量" in endpoint_text
            and "倒数地板素对覆盖是二维筛上界" in endpoint_text,
            "proved": True,
            "meaning": "端点维数差是变量行路线的 alpha=1 退化口。",
            "output": "EndpointDG remains a special case, not the uniform proof.",
        },
        {
            "gate": "EDADualCompatibility",
            "closed": "EDA(p)<=>PrimeGap(p)" in eda_text
            and "CRT 对偶路线" in eda_text,
            "proved": True,
            "meaning": "变量行维数差若失败，就是 EDA-Dual 中的低模/尾项缺陷。",
            "output": "PrimeFreeIntervalLowModPDECDefectReturn。",
        },
        {
            "gate": "UniformDimensionGapConstants",
            "closed": False,
            "proved": False,
            "meaning": "尚未给出所有 alpha in [1/2,1] 的 G_x(P)>B_x(P) 常数账本。",
            "output": "AlignedPrimeMainBuchstabBranchLowerBoundOrDefectReturn。",
        },
    ]


def run(
    previous_path: Path,
    endpoint_path: Path,
    eda_path: Path,
    p_values: list[int],
    sample_limit: int,
) -> dict[str, Any]:
    """执行变量行维数差路由。"""
    previous = load_json(previous_path)
    endpoint_text = endpoint_path.read_text(encoding="utf-8")
    eda_text = eda_path.read_text(encoding="utf-8")
    sample_audit = audit_samples(p_values, sample_limit)
    paths = [previous_path, endpoint_path, eda_path]
    rows = proof_rows(previous=previous, endpoint_text=endpoint_text, eda_text=eda_text)
    return {
        "certificate_type": "variable_row_dimension_gap_router",
        "status": "variable_row_dimension_gap_reduced_to_aligned_prime_main_or_named_defect",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "sample_audit": sample_audit,
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "variable_row_dimension_gap_identity_closed": True,
        "endpoint_dimension_gap_uniform_lift_rejected": True,
        "uniform_dimension_gap_constants_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_after_router": "AlignedPrimeMainBuchstabBranchLowerBoundOrDefectReturn",
        "terminal_gap_expansion": [
            "UniformBuchstabOnePrimeBranchLowerBound",
            "VariableRowRoughSkeletonLowerBound",
            "VariableRowPrimePairFiberUpperBound",
            "LowModSkeletonDeficitPDEC",
            "PrimePairFiberConcentrationTailPDEC",
            "SparsePrimeSurvivorSAE",
            "ColumnDisplacementReusePDEC",
        ],
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "exact_fiber_formula": (
            "B_x(P)=sum_{q prime, x<q<=sqrt((x+1)P)} "
            "# {m prime: max(q,ceil((xP+1)/q))<=m<=floor((xP+P-1)/q)}."
        ),
        "plain_conclusion": (
            "本步把变量行维数差写成精确公式，并排除一个危险捷径："
            "端点 x=P 的 P/log^2P 双素上界不能统一搬到 x≈sqrt(P)。"
            "在变量行上，R_x 的一素分支与双素分支共同处于 Buchstab u∈[2,3] 的两分支区间；"
            "真正剩余是证明一素分支在每个 P 对齐行中为正，或把为零的分支送入低模 PDEC、"
            "素对纤维集中、SAE 或 ColumnCRT。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    sample = result["sample_audit"]
    lines = [
        "# Prime Matrix 变量行维数差路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"variable_row_dimension_gap_identity_closed={fmt_bool(result['variable_row_dimension_gap_identity_closed'])}",
        f"endpoint_dimension_gap_uniform_lift_rejected={fmt_bool(result['endpoint_dimension_gap_uniform_lift_rejected'])}",
        f"uniform_dimension_gap_constants_proved={fmt_bool(result['uniform_dimension_gap_constants_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 精确变量行公式",
        "",
        "对 `sqrt(P)<=x<P`：",
        "",
        "```text",
        "G_x(P)=#R_x",
        "B_x(P)=#SemiprimeFibers_x",
        "PrimeSurvivors_x=G_x(P)-B_x(P).",
        "```",
        "",
        "双素纤维有精确求和式：",
        "",
        "```text",
        result["exact_fiber_formula"],
        "```",
        "",
        "因此变量行维数差不是启发式口号，而是完全等价的幸存者恒等式。",
        "",
        "## 2. 端点合同不能直接统一外推",
        "",
        "对角端点 `x=P` 中，双素覆盖被三条倒数地板曲线压到 `P/log^2 P` 型对象；",
        "但在变量行，尤其 `x≈sqrt(P)` 时，collar 中的 `m` 窗口长度可达 `sqrt(P)`，双素纤维仍有 `P/log P` 量级。",
        "所以端点维数差合同是 `alpha=1` 的退化口，不是 `alpha in [1/2,1]` 的统一证明。",
        "",
        "## 3. 判定表",
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
            "## 4. 样本审计",
            "",
            "样本用于定位危险 alpha 区间，不作为证明。",
            "",
            "```text",
            f"sample_status={sample['status']}",
            f"all_identity_holds={fmt_bool(sample['all_identity_holds'])}",
            f"global_min_prime={sample['global_min_prime']}",
            f"global_max_semiprime_share={fmt_float(sample['global_max_semiprime_share'])}",
            "```",
            "",
            "| P | rows | min prime | max semiprime share | max fiber load | min prime logx/P | max semiprime logx/P |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in sample["rows"]:
        lines.append(
            "| {p} | {rows} | {prime} | {share} | {fiber} | {pconst} | {sconst} |".format(
                p=row["p"],
                rows=row["row_count"],
                prime=row["min_prime"],
                share=fmt_float(row["max_semiprime_share"]),
                fiber=row["max_fiber_load"],
                pconst=fmt_float(row["min_prime_logx_over_p"]),
                sconst=fmt_float(row["max_semiprime_logx_over_p"]),
            )
        )
    lines.extend(
        [
            "",
            "按 `alpha=log x/log P` 分桶的压力读数：",
            "",
            "| P | alpha bucket | rows | min prime | max semiprime share | min prime share | max fiber load |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for record in sample["rows"]:
        for label, bucket in record["bucket_summary"].items():
            if bucket["count"] == 0:
                continue
            lines.append(
                "| {p} | {label} | {count} | {prime} | {sshare} | {pshare} | {fiber} |".format(
                    p=record["p"],
                    label=label,
                    count=bucket["count"],
                    prime=bucket["min_prime"],
                    sshare=fmt_float(bucket["max_semiprime_share"]),
                    pshare=fmt_float(bucket["min_prime_share"]),
                    fiber=bucket["max_fiber_load"],
                )
            )
    lines.extend(
        [
            "",
            "## 5. 新最窄剩余",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = UniformBuchstabOnePrimeBranchLowerBound",
            "    AND VariableRowRoughSkeletonLowerBound",
            "    AND VariableRowPrimePairFiberUpperBound",
            "    AND LowModSkeletonDeficitPDEC",
            "    AND PrimePairFiberConcentrationTailPDEC",
            "    AND SparsePrimeSurvivorSAE",
            "    AND ColumnDisplacementReusePDEC.",
            "```",
            "",
            "含义是：若不能直接证明每行一素分支为正，就必须把失败转成同 formal unit 的低模亏损、",
            "素对纤维集中、孤立幸存者逃逸或固定列位移复用。该路由仍未给出无条件闭合。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_table(result: dict[str, Any]) -> None:
    """输出审计简表。"""
    print("p rows min_prime max_semiprime_share max_fiber_load min_prime_logx/P max_semiprime_logx/P", flush=True)
    for row in result["sample_audit"]["rows"]:
        print(
            f"{row['p']} {row['row_count']} {row['min_prime']} "
            f"{row['max_semiprime_share']:.6f} {row['max_fiber_load']} "
            f"{row['min_prime_logx_over_p']:.6f} {row['max_semiprime_logx_over_p']:.6f}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--endpoint-md", type=Path, default=DEFAULT_ENDPOINT_DG)
    parser.add_argument("--eda-md", type=Path, default=DEFAULT_EDA)
    parser.add_argument("--p-list", type=str, default="101,499,997,1999")
    parser.add_argument("--sample-limit", type=int, default=3)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--format", choices=("write", "json", "table"), default="write")
    args = parser.parse_args()
    result = run(
        previous_path=args.previous_json,
        endpoint_path=args.endpoint_md,
        eda_path=args.eda_md,
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
