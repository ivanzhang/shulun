#!/usr/bin/env python3
"""Prime Matrix 早期零行真双素 canonical anchor collar 路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_anchor_collar_router.py
  python3 experiments/prime_matrix_early_zero_anchor_collar_router.py --p-list 101,499,997 --format table

输出：
  docs/monograph/prime-matrix-early-zero-anchor-collar-router.json
  docs/monograph/prime-matrix-early-zero-anchor-collar-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-cofactor-depth-router.json"
DEFAULT_CARRY = DOCS / "prime-matrix-early-zero-carry-shell-router.json"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-anchor-collar-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-anchor-collar-router.md"


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


def row_anchor_stats(p: int, x: int, spf: array) -> dict[str, Any]:
    """统计 x>=sqrt(P) 行中的 canonical anchor collar 数据。"""
    anchor_top = isqrt((x + 1) * p - 1)
    anchor_width = max(0, anchor_top - x)
    rough_holes = 0
    prime_holes = 0
    semiprime_holes = 0
    bad_anchor_hits = 0
    fiber_loads: dict[int, int] = {}
    for column in range(1, p):
        value = x * p + column
        factor = spf[value]
        if factor and factor <= x:
            continue
        rough_holes += 1
        if factor == 0:
            prime_holes += 1
            continue
        # 在 x>=sqrt(P) 中，上一轮已证明 cofactor 必为素数；factor 是 canonical 最小高素因子。
        semiprime_holes += 1
        if not (x < factor <= anchor_top):
            bad_anchor_hits += 1
        fiber_loads[factor] = fiber_loads.get(factor, 0) + 1
    max_fiber_load = max(fiber_loads.values(), default=0)
    saturated_fibers = sum(1 for value in fiber_loads.values() if value >= 2)
    return {
        "x": x,
        "h": p - x,
        "anchor_top": anchor_top,
        "anchor_width": anchor_width,
        "rough_holes": rough_holes,
        "prime_holes": prime_holes,
        "semiprime_holes": semiprime_holes,
        "bad_anchor_hits": bad_anchor_hits,
        "distinct_anchor_count": len(fiber_loads),
        "max_fiber_load": max_fiber_load,
        "saturated_fiber_count": saturated_fibers,
        "primepair_share": None if rough_holes == 0 else semiprime_holes / rough_holes,
        "anchor_width_over_h": None if p == x else anchor_width / (p - x),
        "top_fibers": sorted(
            [{"q": q, "load": load} for q, load in fiber_loads.items()],
            key=lambda row: (-row["load"], row["q"]),
        )[:5],
    }


def audit_p(p: int, sample_limit: int) -> dict[str, Any]:
    """审计单个 P 的 canonical anchor collar。"""
    spf = small_factor_table(p)
    sqrt_p = isqrt(p)
    rows = [row_anchor_stats(p, x, spf) for x in range(sqrt_p, p)]
    if not rows:
        return {
            "p": p,
            "sqrt_p": sqrt_p,
            "row_count": 0,
            "all_anchor_hits_in_collar": True,
            "rows": [],
        }
    max_bad = max(row["bad_anchor_hits"] for row in rows)
    max_anchor_width = max(row["anchor_width"] for row in rows)
    max_fiber_load = max(row["max_fiber_load"] for row in rows)
    max_primepair_share = max(row["primepair_share"] or 0.0 for row in rows)
    min_prime_holes = min(row["prime_holes"] for row in rows)
    weakest_prime_rows = [row for row in rows if row["prime_holes"] == min_prime_holes][
        :sample_limit
    ]
    strongest_semiprime_rows = sorted(
        rows,
        key=lambda row: (row["primepair_share"] or 0.0, row["semiprime_holes"]),
        reverse=True,
    )[:sample_limit]
    widest_anchor_rows = sorted(rows, key=lambda row: row["anchor_width"], reverse=True)[
        :sample_limit
    ]
    return {
        "p": p,
        "sqrt_p": sqrt_p,
        "x_range": [sqrt_p, p - 1],
        "row_count": len(rows),
        "all_anchor_hits_in_collar": max_bad == 0,
        "max_bad_anchor_hits": max_bad,
        "max_anchor_width": max_anchor_width,
        "max_fiber_load": max_fiber_load,
        "max_primepair_share": max_primepair_share,
        "min_prime_holes": min_prime_holes,
        "weakest_prime_rows": weakest_prime_rows,
        "strongest_semiprime_rows": strongest_semiprime_rows,
        "widest_anchor_rows": widest_anchor_rows,
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
        "status": "canonical_anchor_collar_sample_verified_capacity_open",
        "all_anchor_hits_in_collar": all(row["all_anchor_hits_in_collar"] for row in rows),
        "rows": rows,
    }


def proof_rows(
    previous: dict[str, Any],
    carry: dict[str, Any],
    pdec_text: str,
    sae_text: str,
    column_text: str,
    sample_audit: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 anchor collar 路由账本。"""
    return [
        {
            "gate": "PrimePairBranchImported",
            "closed": "PrimePairCarryShellCapacityBoundOrPDECReturn"
            in previous.get("terminal_gap_expansion", []),
            "proved": True,
            "meaning": "上一轮已把 x>=sqrt(P) 分支化为真双素 carry-shell 容量问题。",
            "output": "继续规范化 q anchor。",
        },
        {
            "gate": "CarryShellIdentityImported",
            "closed": carry.get("exact_carry_shell_identity_closed") is True,
            "proved": True,
            "meaning": "已有 h=a+b-floor(ab/P), c=ab mod P 的带进位壳恒等式。",
            "output": "可在壳上取 canonical anchor。",
        },
        {
            "gate": "CanonicalLeastAnchorCollar",
            "closed": True,
            "proved": True,
            "meaning": "取 q 为 xP+c 的最小高素因子，则 q<=sqrt(xP+c)<sqrt((x+1)P)。",
            "output": "x<q<sqrt((x+1)P)，高素 anchor 只在窄 collar 内。",
        },
        {
            "gate": "PairDuplicationQuotiented",
            "closed": True,
            "proved": True,
            "meaning": "canonical q<=m 删除 q,m 互换重复；平方点只计一次。",
            "output": "primitive physical atom 口径更窄。",
        },
        {
            "gate": "FiberShortPrimeInterval",
            "closed": True,
            "proved": True,
            "meaning": "固定 q 后，m 必须是长度 <P/q<=sqrt(P) 的短区间内素数。",
            "output": "q-fiber capacity replaces unconstrained high-prime coverage。",
        },
        {
            "gate": "SampleAnchorAudit",
            "closed": sample_audit["all_anchor_hits_in_collar"],
            "proved": False,
            "meaning": "样本中所有 canonical anchors 均落入 collar；审计只复核实现口径。",
            "output": sample_audit["status"],
        },
        {
            "gate": "NamedReturnCompatibility",
            "closed": "未来 PDEC schema 准入条件" in pdec_text
            and "LocalSurvivorCert" in sae_text
            and "ColumnCRT-Displacement Absorption" in column_text,
            "proved": True,
            "meaning": "若少数 q-fiber 持久过载则进入 PDEC；孤立短窗进入 SAE；固定列位移进入 ColumnCRT。",
            "output": "AnchorCollarPDECSAEColumnReturn。",
        },
        {
            "gate": "AnchorCollarPrimeFiberCapacity",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明所有 collar q-fiber 的短素数容量总和不能覆盖 R_x。",
            "output": "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn。",
        },
    ]


def run(
    previous_path: Path,
    carry_path: Path,
    pdec_path: Path,
    sae_path: Path,
    column_path: Path,
    p_values: list[int],
    sample_limit: int,
) -> dict[str, Any]:
    """执行 canonical anchor collar 路由。"""
    previous = load_json(previous_path)
    carry = load_json(carry_path)
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    sample_audit = audit_samples(p_values, sample_limit)
    paths = [previous_path, carry_path, pdec_path, sae_path, column_path]
    rows = proof_rows(
        previous=previous,
        carry=carry,
        pdec_text=pdec_text,
        sae_text=sae_text,
        column_text=column_text,
        sample_audit=sample_audit,
    )
    return {
        "certificate_type": "early_zero_anchor_collar_router",
        "status": "canonical_anchor_collar_closed_prime_fiber_capacity_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "sample_audit": sample_audit,
        "canonical_anchor_collar_closed": True,
        "fiber_short_interval_reduction_closed": True,
        "anchor_collar_prime_fiber_capacity_closed": False,
        "row_column_unconditional_closed": False,
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "terminal_gap_after_router": "AnchorCollarPrimeFiberCapacityBoundOrPDECReturn",
        "terminal_gap_expansion": [
            "AnchorCollarShortPrimeFiberUpperBound",
            "NoPersistentAnchorFiberConcentrationPDEC",
            "NoSparseAnchorFiberSAE",
            "NoColumnDisplacementReuseInAnchorFibers",
        ],
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "structural_law": (
            "In the x>=sqrt(P) branch every high filler is a product of two primes in "
            "(x,P). Choosing the least high prime factor gives a canonical anchor q with "
            "x<q<sqrt((x+1)P). Hence the anchor is confined to a narrow collar, and each "
            "q-fiber asks for primes m in an interval of length <P/q<=sqrt(P). Full early "
            "zero coverage would require these short prime fibers to cover all R_x; any "
            "persistent fiber overload is a PDEC object, while sparse fiber escapes route "
            "to SAE/LocalSurvivor or ColumnCRT."
        ),
        "plain_conclusion": (
            "本步把真双素 carry-shell 再压窄：取最小高素因子后，anchor `q` 不在整个 `(x,P)`，"
            "而只能在 `x<q<sqrt((x+1)P)` 的 canonical collar 中；固定 q 后，cofactor `m` "
            "只来自长度 `<P/q<=sqrt(P)` 的短素数纤维。剩余变成 anchor-collar 短素数纤维容量，"
            "或过载时的 PDEC/SAE/ColumnCRT 回流。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    sample = result["sample_audit"]
    lines = [
        "# Prime Matrix 早期零行 canonical anchor collar 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"canonical_anchor_collar_closed={fmt_bool(result['canonical_anchor_collar_closed'])}",
        f"fiber_short_interval_reduction_closed={fmt_bool(result['fiber_short_interval_reduction_closed'])}",
        f"anchor_collar_prime_fiber_capacity_closed={fmt_bool(result['anchor_collar_prime_fiber_capacity_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Canonical anchor collar",
        "",
        "在 `x>=sqrt(P)` 分支，任一高补洞点都是",
        "",
        "```text",
        "xP+c = q m,   x<q,m<P,   q,m prime.",
        "```",
        "",
        "取 `q` 为最小高素因子，则 `q<=m`，所以",
        "",
        "```text",
        "q^2 <= xP+c < (x+1)P.",
        "```",
        "",
        "因此",
        "",
        "```text",
        "x < q < sqrt((x+1)P).",
        "```",
        "",
        "这把原先的高素选择区间 `(x,P)` 压成 canonical anchor collar。用 `q=P-a` 表示时，",
        "它等价于在 carry-shell 中只取 `q<=m` 的半边，并且平方点只计一次。",
        "",
        "## 2. q-fiber 短素数窗口",
        "",
        "固定 collar 中的 `q` 后，`m` 必须满足",
        "",
        "```text",
        "ceil((xP+1)/q) <= m <= floor((xP+P-1)/q),",
        "m prime,  q<=m<P.",
        "```",
        "",
        "该窗口长度严格小于 `P/q`，而 `q>x>=sqrt(P)`，故每条 q-fiber 长度 `<sqrt(P)`。",
        "所以全覆盖不能再说成“高素很多”，而必须说成许多极短素数纤维同时满载。",
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
            "样本仅用于复核 canonical anchor 实现；collar 结论由 `q^2<=xP+c` 直接证明。",
            "",
            "```text",
            f"sample_status={sample['status']}",
            f"all_anchor_hits_in_collar={fmt_bool(sample['all_anchor_hits_in_collar'])}",
            "```",
            "",
            "| P | rows | max anchor width | max fiber load | max primepair share | min prime holes |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in sample["rows"]:
        lines.append(
            "| {p} | {rows} | {width} | {fiber} | {share:.6f} | {prime} |".format(
                p=row["p"],
                rows=row["row_count"],
                width=row["max_anchor_width"],
                fiber=row["max_fiber_load"],
                share=row["max_primepair_share"],
                prime=row["min_prime_holes"],
            )
        )
    lines.extend(
        [
            "",
            "## 5. 新最窄剩余",
            "",
            "本步把 `PrimePairCarryShellCapacityBoundOrPDECReturn` 压成：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = AnchorCollarShortPrimeFiberUpperBound",
            "    AND NoPersistentAnchorFiberConcentrationPDEC",
            "    AND NoSparseAnchorFiberSAE",
            "    AND NoColumnDisplacementReuseInAnchorFibers.",
            "```",
            "",
            "真正未闭合的是第一项：需要证明 collar 中所有短素数纤维的容量总和不能吃掉整个 `R_x`；",
            "若某些纤维承担异常大负载，则已经进入 PDEC/SAE/ColumnCRT 命名回流，而不是新的出口。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_table(result: dict[str, Any]) -> None:
    """输出审计简表。"""
    print("p rows max_anchor_width max_fiber_load max_primepair_share min_prime_holes", flush=True)
    for row in result["sample_audit"]["rows"]:
        print(
            f"{row['p']} {row['row_count']} {row['max_anchor_width']} "
            f"{row['max_fiber_load']} {row['max_primepair_share']:.6f} {row['min_prime_holes']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--carry-json", type=Path, default=DEFAULT_CARRY)
    parser.add_argument("--pdec-md", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sae-md", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--column-md", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--p-list", type=str, default="101,499,997")
    parser.add_argument("--sample-limit", type=int, default=5)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--format", choices=("write", "json", "table"), default="write")
    args = parser.parse_args()
    result = run(
        previous_path=args.previous_json,
        carry_path=args.carry_json,
        pdec_path=args.pdec_md,
        sae_path=args.sae_md,
        column_path=args.column_md,
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
