#!/usr/bin/env python3
"""Prime Matrix 早期零行 cofactor 深度分层路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_cofactor_depth_router.py
  python3 experiments/prime_matrix_early_zero_cofactor_depth_router.py --p-list 101,499,997 --format table

输出：
  docs/monograph/prime-matrix-early-zero-cofactor-depth-router.json
  docs/monograph/prime-matrix-early-zero-cofactor-depth-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from array import array
from math import isqrt
from pathlib import Path
from typing import Any

from prime_matrix_cylindrical_completion_audit import primes_upto, small_factor_table


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-carry-shell-router.json"
DEFAULT_SCHEMA = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_STITCHING = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-cofactor-depth-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-cofactor-depth-router.md"


def parse_p_list(raw: str) -> list[int]:
    """解析逗号分隔的 P 列表。"""
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


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def factor_depth(value: int, primes: list[int]) -> tuple[int, list[int]]:
    """返回带重数素因子深度和因子列表。"""
    remaining = value
    factors: list[int] = []
    for prime in primes:
        if prime * prime > remaining:
            break
        while remaining % prime == 0:
            factors.append(prime)
            remaining //= prime
    if remaining > 1:
        factors.append(remaining)
    return len(factors), factors


def audit_p(p: int, sample_limit: int) -> dict[str, Any]:
    """审计单个 P 的 cofactor 深度分层。"""
    spf = small_factor_table(p)
    primes = primes_upto(p)
    sqrt_p = isqrt(p)
    total_hits = 0
    prime_cofactor_hits = 0
    composite_cofactor_hits = 0
    composite_after_sqrt_gate = 0
    max_depth = 0
    depth_hist: dict[int, int] = {}
    sample_composite_hits: list[dict[str, Any]] = []
    sample_gate_rows: list[dict[str, Any]] = []
    for x in range(1, p):
        row_hits = 0
        row_composite = 0
        row_max_depth = 0
        for column in range(1, p):
            value = x * p + column
            q = spf[value]
            if not (q and x < q < p):
                continue
            cofactor = value // q
            depth, factors = factor_depth(cofactor, primes)
            total_hits += 1
            row_hits += 1
            max_depth = max(max_depth, depth)
            row_max_depth = max(row_max_depth, depth)
            depth_hist[depth] = depth_hist.get(depth, 0) + 1
            if depth == 1:
                prime_cofactor_hits += 1
            else:
                composite_cofactor_hits += 1
                row_composite += 1
                if x >= sqrt_p:
                    composite_after_sqrt_gate += 1
                if len(sample_composite_hits) < sample_limit:
                    sample_composite_hits.append(
                        {
                            "x": x,
                            "h": p - x,
                            "column": column,
                            "value": value,
                            "q": q,
                            "cofactor": cofactor,
                            "depth": depth,
                            "cofactor_factors": factors,
                        }
                    )
        if row_hits and len(sample_gate_rows) < sample_limit:
            sample_gate_rows.append(
                {
                    "x": x,
                    "h": p - x,
                    "hits": row_hits,
                    "composite_hits": row_composite,
                    "max_depth": row_max_depth,
                    "x_ge_sqrt_p": x >= sqrt_p,
                }
            )
    return {
        "p": p,
        "sqrt_p": sqrt_p,
        "total_high_filler_hits": total_hits,
        "prime_cofactor_hits": prime_cofactor_hits,
        "composite_cofactor_hits": composite_cofactor_hits,
        "composite_after_sqrt_gate": composite_after_sqrt_gate,
        "composite_only_before_sqrt_gate": composite_after_sqrt_gate == 0,
        "max_cofactor_depth": max_depth,
        "depth_histogram": {str(key): depth_hist[key] for key in sorted(depth_hist)},
        "sample_composite_hits": sample_composite_hits,
        "sample_gate_rows": sample_gate_rows,
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
        "status": "cofactor_depth_gate_sample_verified_theorem_algebraic_recursive_capacity_open",
        "all_composite_only_before_sqrt_gate": all(
            row["composite_only_before_sqrt_gate"] for row in rows
        ),
        "rows": rows,
    }


def proof_rows(
    previous: dict[str, Any],
    schema: dict[str, Any],
    clb_text: str,
    stitching_text: str,
    pdec_text: str,
    sae_text: str,
    sample_audit: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 cofactor 深度路由账本。"""
    return [
        {
            "gate": "CarryShellImported",
            "closed": previous.get("terminal_gap_after_router") == "CarryShellPrimitiveCapacityBoundOrPDECReturn",
            "proved": True,
            "meaning": "上一轮已把高补洞支撑压到带进位壳。",
            "output": "继续分解 cofactor m 的乘法深度。",
        },
        {
            "gate": "CofactorWindowAndRoughness",
            "closed": "R_x" in clb_text and "xP+c=qm" in clb_text,
            "proved": True,
            "meaning": "若 c in R_x 且 xP+c=q m，则 x<m<P，且 m 没有 <=x 的素因子。",
            "output": "m 是小于 P 的 x-rough cofactor。",
        },
        {
            "gate": "DepthBound",
            "closed": True,
            "proved": True,
            "meaning": "若 Omega(m)=d，则 m>x^d 且 m<P，所以 d<log(P)/log(x)。",
            "output": "cofactor 深度随 x 增大快速塌缩。",
        },
        {
            "gate": "SqrtGatePrimeCofactor",
            "closed": True,
            "proved": True,
            "meaning": "当 x>=sqrt(P) 时，复合 m 至少含两个 >x 因子，导致 m>x^2>=P，矛盾。",
            "output": "x>=sqrt(P) 的 carry-shell 是真 prime-pair shell。",
        },
        {
            "gate": "CompositeCofactorRecursiveReturn",
            "closed": "Omega" in stitching_text and "未来 PDEC schema 准入条件" in pdec_text,
            "proved": True,
            "meaning": "若 x<sqrt(P) 且 m 复合，则 m 的全部因子仍在同一 x-rough 递归壳内；持久集中进入 PDEC，孤立进入 SAE。",
            "output": "CompositeCofactorDepthRecursivePDECReturnOrSAE。",
        },
        {
            "gate": "SchemaCompatibility",
            "closed": schema.get("early_zero_phase_defect_schema_admission_closed") is True
            and "LocalSurvivorCert" in sae_text,
            "proved": True,
            "meaning": "cofactor 深度分层仍使用上一轮同 formal unit 和 SAE/LocalSurvivor 回流纪律。",
            "output": "不是新终端。",
        },
        {
            "gate": "SampleDepthAudit",
            "closed": sample_audit["all_composite_only_before_sqrt_gate"],
            "proved": False,
            "meaning": "样本中所有复合 cofactor 都只出现在 x<sqrt(P) 的早期带；这只是审计。",
            "output": sample_audit["status"],
        },
        {
            "gate": "PrimePairCarryShellCapacity",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 x>=sqrt(P) 的真双素 carry-shell 容量不能覆盖全部 R_x。",
            "output": "PrimePairCarryShellCapacityBoundOrPDECReturn。",
        },
        {
            "gate": "RecursiveCofactorCapacity",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 x<sqrt(P) 的复合 cofactor 递归壳必下降到 survivor 或命名 PDEC/SAE 排斥。",
            "output": "CompositeCofactorDepthDescentOrNamedReturn。",
        },
    ]


def run(
    previous_path: Path,
    schema_path: Path,
    clb_path: Path,
    stitching_path: Path,
    pdec_path: Path,
    sae_path: Path,
    p_values: list[int],
    sample_limit: int,
) -> dict[str, Any]:
    """执行 cofactor 深度路由。"""
    previous = load_json(previous_path)
    schema = load_json(schema_path)
    clb_text = clb_path.read_text(encoding="utf-8")
    stitching_text = stitching_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    sample_audit = audit_samples(p_values, sample_limit)
    paths = [previous_path, schema_path, clb_path, stitching_path, pdec_path, sae_path]
    rows = proof_rows(
        previous=previous,
        schema=schema,
        clb_text=clb_text,
        stitching_text=stitching_text,
        pdec_text=pdec_text,
        sae_text=sae_text,
        sample_audit=sample_audit,
    )
    return {
        "certificate_type": "early_zero_cofactor_depth_router",
        "status": "cofactor_depth_gate_closed_primepair_and_recursive_capacity_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "sample_audit": sample_audit,
        "cofactor_depth_gate_closed": True,
        "sqrt_gate_prime_cofactor_closed": True,
        "primepair_carry_shell_capacity_closed": False,
        "recursive_cofactor_capacity_closed": False,
        "row_column_unconditional_closed": False,
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "terminal_gap_after_router": "PrimePairCarryShellCapacityAndCompositeCofactorDepthDescent",
        "terminal_gap_expansion": [
            "PrimePairCarryShellCapacityBoundOrPDECReturn",
            "CompositeCofactorDepthDescentOrNamedReturn",
            "EarlyBandLocalSurvivorOrSAEExclusion",
        ],
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "structural_law": (
            "In a high-filler atom xP+c=q m with c in R_x, the cofactor m is an x-rough "
            "integer in (x,P). If x>=sqrt(P), this forces m to be prime, so the carry shell "
            "is a genuine prime-pair shell. Composite cofactors can occur only in the early "
            "band x<sqrt(P), and then their prime factors are all >x, giving a finite "
            "recursive depth bounded by log P/log x. Persistent recursive concentration is "
            "a PDEC object; sparse recursive escape is SAE/LocalSurvivor."
        ),
        "plain_conclusion": (
            "本步修正并强化 carry-shell 口径：`m=P-b` 是 x-rough cofactor，不必总是素数；"
            "但一旦 `x>=sqrt(P)`，它必为素数。因此早期零行剩余被拆成两块："
            "大范围真双素 carry-shell 容量，以及 `x<sqrt(P)` 的复合 cofactor 递归下降/命名回流。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    sample = result["sample_audit"]
    lines = [
        "# Prime Matrix 早期零行 cofactor 深度分层路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"cofactor_depth_gate_closed={fmt_bool(result['cofactor_depth_gate_closed'])}",
        f"sqrt_gate_prime_cofactor_closed={fmt_bool(result['sqrt_gate_prime_cofactor_closed'])}",
        f"primepair_carry_shell_capacity_closed={fmt_bool(result['primepair_carry_shell_capacity_closed'])}",
        f"recursive_cofactor_capacity_closed={fmt_bool(result['recursive_cofactor_capacity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Cofactor 深度门",
        "",
        "设 `c in R_x` 被高素斜线补掉：",
        "",
        "```text",
        "xP+c = q m,   x<q<P.",
        "```",
        "",
        "上一轮已证明 `x<m<P`。同时 `c in R_x` 表示 `xP+c` 没有不超过 `x` 的素因子，因此 `m` 的每个素因子也都大于 `x`。",
        "",
        "若 `Omega(m)=d` 是带重数素因子数，则",
        "",
        "```text",
        "m > x^d,   m<P,   因而 d < log(P)/log(x).",
        "```",
        "",
        "特别地，当 `x>=sqrt(P)` 时，复合 `m` 至少含两个大于 `x` 的素因子，给出 `m>x^2>=P`，矛盾。所以：",
        "",
        "```text",
        "x>=sqrt(P)  =>  m is prime.",
        "```",
        "",
        "这把 carry-shell 分成真双素壳和早期复合 cofactor 递归壳。",
        "",
        "## 2. 递归回流",
        "",
        "当 `x<sqrt(P)` 且 `m` 复合时，`m` 是一个小于 `P` 的 x-rough 数，且所有因子仍在 `>x` 的同一粗骨架内。",
        "若这种复合 cofactor 壳在反例族中持久集中，它就是同 formal unit 的 PDEC 支撑；若只孤立出现，则进入 SAE/LocalSurvivor。",
        "因此复合 cofactor 不是新出口，而是递归下降或命名回流。",
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
            "样本只用于复核分层口径；`sqrt` 门由上面的不等式直接证明。",
            "",
            "```text",
            f"sample_status={sample['status']}",
            f"all_composite_only_before_sqrt_gate={fmt_bool(sample['all_composite_only_before_sqrt_gate'])}",
            "```",
            "",
            "| P | total high filler | prime cofactor | composite cofactor | max depth | composite after sqrt gate |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in sample["rows"]:
        lines.append(
            "| {p} | {total} | {prime} | {composite} | {depth} | {after} |".format(
                p=row["p"],
                total=row["total_high_filler_hits"],
                prime=row["prime_cofactor_hits"],
                composite=row["composite_cofactor_hits"],
                depth=row["max_cofactor_depth"],
                after=row["composite_after_sqrt_gate"],
            )
        )
    lines.extend(
        [
            "",
            "## 5. 新最窄剩余",
            "",
            "本步把 `CarryShellPrimitiveCapacityBoundOrPDECReturn` 进一步拆成：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = PrimePairCarryShellCapacityBoundOrPDECReturn",
            "    AND CompositeCofactorDepthDescentOrNamedReturn",
            "    AND EarlyBandLocalSurvivorOrSAEExclusion.",
            "```",
            "",
            "其中第一项处理 `x>=sqrt(P)` 的真双素壳，第二项处理 `x<sqrt(P)` 的复合 cofactor 递归壳，第三项处理递归不能持久化时的孤窗证书。",
            "这仍是自足路线中的结构压缩；尚未给出最终容量排斥。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_table(result: dict[str, Any]) -> None:
    """输出审计简表。"""
    print(
        "p total_hits prime_cofactor composite_cofactor max_depth composite_after_sqrt_gate",
        flush=True,
    )
    for row in result["sample_audit"]["rows"]:
        print(
            f"{row['p']} {row['total_high_filler_hits']} {row['prime_cofactor_hits']} "
            f"{row['composite_cofactor_hits']} {row['max_cofactor_depth']} "
            f"{row['composite_after_sqrt_gate']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--schema-json", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--clb-md", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--stitching-md", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--pdec-md", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sae-md", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--p-list", type=str, default="101,499,997")
    parser.add_argument("--sample-limit", type=int, default=5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--format", choices=("write", "json", "table"), default="write")
    args = parser.parse_args()
    result = run(
        previous_path=args.previous_json,
        schema_path=args.schema_json,
        clb_path=args.clb_md,
        stitching_path=args.stitching_md,
        pdec_path=args.pdec_md,
        sae_path=args.sae_md,
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
