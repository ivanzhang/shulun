#!/usr/bin/env python3
"""Prime Matrix 早期零行双高因子带进位壳路由器。

用法示例：
  python3 experiments/prime_matrix_early_zero_carry_shell_router.py
  python3 experiments/prime_matrix_early_zero_carry_shell_router.py --p-list 101,499,997 --format table

输出：
  docs/monograph/prime-matrix-early-zero-carry-shell-router.json
  docs/monograph/prime-matrix-early-zero-carry-shell-router.md
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

DEFAULT_PREVIOUS = DOCS / "prime-matrix-early-zero-phase-defect-schema-router.json"
DEFAULT_CLB = DOCS / "prime-matrix-cylindrical-completion-line-barrier.md"
DEFAULT_BOTTOM = DOCS / "prime-matrix-bottom-deficit-pair-bound-hard-attack.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-local-certificate-reduction.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_JSON = DOCS / "prime-matrix-early-zero-carry-shell-router.json"
DEFAULT_MD = DOCS / "prime-matrix-early-zero-carry-shell-router.md"


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


def high_filler_hits_for_row(p: int, x: int, spf: array, sample_limit: int) -> dict[str, Any]:
    """审计一行中的未完成高素补洞原子。"""
    h = p - x
    hits: list[dict[str, Any]] = []
    carry_values: set[int] = set()
    identity_ok = True
    factor_window_ok = True
    for column in range(1, p):
        value = x * p + column
        q = spf[value]
        if not (q and x < q < p):
            continue
        m = value // q
        a = p - q
        b = p - m
        carry = (a * b) // p
        residue = (a * b) % p
        row_ok = (
            x < m < p
            and 1 <= a < h
            and 1 <= b < h
            and h == a + b - carry
            and column == residue
        )
        identity_ok = identity_ok and row_ok
        factor_window_ok = factor_window_ok and x < m < p
        carry_values.add(carry)
        if len(hits) < sample_limit:
            hits.append(
                {
                    "column": column,
                    "value": value,
                    "q": q,
                    "m": m,
                    "a": a,
                    "b": b,
                    "carry": carry,
                    "ab_mod_p": residue,
                    "h_check": a + b - carry,
                    "identity_ok": row_ok,
                }
            )
    return {
        "x": x,
        "h": h,
        "hit_count": len(hits) if len(hits) < sample_limit else None,
        "actual_hit_count": sum(
            1
            for column in range(1, p)
            if (spf[x * p + column] and x < spf[x * p + column] < p)
        ),
        "identity_ok": identity_ok,
        "factor_window_ok": factor_window_ok,
        "carry_values": sorted(carry_values),
        "has_positive_carry": any(value > 0 for value in carry_values),
        "sample_hits": hits,
    }


def audit_p(p: int, sample_limit: int) -> dict[str, Any]:
    """审计单个 P 的全行带进位壳恒等式。"""
    spf = small_factor_table(p)
    rows: list[dict[str, Any]] = []
    total_hits = 0
    max_hits = 0
    max_carry = 0
    positive_carry_rows = 0
    bottom_rows = 0
    bottom_positive_carry_rows = 0
    sample_rows: list[dict[str, Any]] = []
    for x in range(1, p):
        row = high_filler_hits_for_row(p, x, spf, sample_limit)
        actual = int(row["actual_hit_count"])
        total_hits += actual
        max_hits = max(max_hits, actual)
        row_max_carry = max(row["carry_values"], default=0)
        max_carry = max(max_carry, row_max_carry)
        if row["has_positive_carry"]:
            positive_carry_rows += 1
        if row["h"] < isqrt(p):
            bottom_rows += 1
            if row["has_positive_carry"]:
                bottom_positive_carry_rows += 1
        if actual and len(sample_rows) < sample_limit:
            row_copy = dict(row)
            row_copy["hit_count"] = actual
            sample_rows.append(row_copy)
        rows.append(row)
    return {
        "p": p,
        "row_count": p - 1,
        "sqrt_p": isqrt(p),
        "total_high_filler_hits": total_hits,
        "max_high_filler_hits_in_row": max_hits,
        "max_carry": max_carry,
        "positive_carry_row_count": positive_carry_rows,
        "bottom_row_count": bottom_rows,
        "bottom_positive_carry_row_count": bottom_positive_carry_rows,
        "all_factor_windows_ok": all(row["factor_window_ok"] for row in rows),
        "all_carry_identities_ok": all(row["identity_ok"] for row in rows),
        "bottom_band_has_zero_carry": bottom_positive_carry_rows == 0,
        "sample_rows": sample_rows,
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
        "status": "carry_shell_identity_sample_verified_theorem_algebraic_budget_open",
        "all_factor_windows_ok": all(row["all_factor_windows_ok"] for row in rows),
        "all_carry_identities_ok": all(row["all_carry_identities_ok"] for row in rows),
        "all_bottom_bands_have_zero_carry": all(row["bottom_band_has_zero_carry"] for row in rows),
        "rows": rows,
    }


def proof_rows(
    previous: dict[str, Any],
    clb_text: str,
    bottom_text: str,
    pdec_text: str,
    sae_text: str,
    column_text: str,
    sample_audit: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成带进位壳路由账本。"""
    return [
        {
            "gate": "EarlyZeroTerminalPackageImported",
            "closed": previous.get("early_zero_branch_remaining") == "EarlyZeroTerminalExclusionPackage",
            "proved": True,
            "meaning": "上一轮已把早期零行分支压成 PDEC/SAE/ColumnCRT 终端排斥包。",
            "output": "当前只攻击 PDEC primitive budget 的支撑几何。",
        },
        {
            "gate": "DoubleHighFactorWindow",
            "closed": "xP+c=qm" in clb_text,
            "proved": True,
            "meaning": "若 c in R_x 且由高素 q 补洞，则 xP+c=qm，且 x<q,m<P。",
            "output": "所有补洞原子都是双高因子窗口内的物理原子。",
        },
        {
            "gate": "ExactCarryShellIdentity",
            "closed": True,
            "proved": True,
            "meaning": "写 q=P-a,m=P-b,k=floor(ab/P)，则 h=P-x=a+b-k 且 c=ab mod P。",
            "output": "高补洞支撑被限制在带进位双高因子壳。",
        },
        {
            "gate": "BottomBandK0Recovered",
            "closed": "a+b=h" in bottom_text and "c=ab" in bottom_text,
            "proved": True,
            "meaning": "当 h<sqrt(P) 时 ab<P，故 k=0，恢复底部二次缺口曲线 c=a(h-a)。",
            "output": "底部带 BDP 是 carry-shell 的 k=0 特例。",
        },
        {
            "gate": "SampleCarryAudit",
            "closed": sample_audit["all_carry_identities_ok"] and sample_audit["all_factor_windows_ok"],
            "proved": False,
            "meaning": "样本全行高补洞均满足双高因子窗口和带进位恒等式；这只是审计，不替代代数证明。",
            "output": sample_audit["status"],
        },
        {
            "gate": "PrimitivePDECSupportReframed",
            "closed": "未来 PDEC schema 准入条件" in pdec_text,
            "proved": True,
            "meaning": "早期零行的 primitive PDEC 下界不能再用任意坏窗支撑；它只能在 carry-shell 支撑上提交。",
            "output": "EarlyZeroPrimitivePDECBudgetInequality -> CarryShellPrimitiveCapacityBoundOrPDECReturn。",
        },
        {
            "gate": "NamedReturnCompatibility",
            "closed": "LocalSurvivorCert" in sae_text and "ColumnCRT-Displacement Absorption" in column_text,
            "proved": True,
            "meaning": "carry-shell 上若出现孤立窗、端点、同列位移或复用，已有 SAE/ColumnCRT/PDEC 命名回流。",
            "output": "无名出口删除。",
        },
        {
            "gate": "CarryShellPrimitiveCapacityBound",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明每个 h 壳的双高因子可用列容量严格小于 R_x，或失败必给可排斥 PDEC。",
            "output": "CarryShellPrimitiveCapacityBoundOrPDECReturn。",
        },
    ]


def run(
    previous_path: Path,
    clb_path: Path,
    bottom_path: Path,
    pdec_path: Path,
    sae_path: Path,
    column_path: Path,
    p_values: list[int],
    sample_limit: int,
) -> dict[str, Any]:
    """执行带进位壳路由。"""
    previous = load_json(previous_path)
    clb_text = clb_path.read_text(encoding="utf-8")
    bottom_text = bottom_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    sample_audit = audit_samples(p_values, sample_limit)
    paths = [previous_path, clb_path, bottom_path, pdec_path, sae_path, column_path]
    rows = proof_rows(
        previous=previous,
        clb_text=clb_text,
        bottom_text=bottom_text,
        pdec_text=pdec_text,
        sae_text=sae_text,
        column_text=column_text,
        sample_audit=sample_audit,
    )
    return {
        "certificate_type": "early_zero_carry_shell_router",
        "status": "exact_carry_shell_identity_closed_primitive_capacity_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in paths},
        "sample_audit": sample_audit,
        "exact_carry_shell_identity_closed": True,
        "bottom_band_k0_recovered": True,
        "early_zero_primitive_pdec_budget_closed": False,
        "row_column_unconditional_closed": False,
        "previous_early_zero_remaining": previous.get("early_zero_branch_remaining"),
        "terminal_gap_after_router": "CarryShellPrimitiveCapacityBoundOrPDECReturn",
        "terminal_gap_expansion": [
            "CarryShellPrimitiveCapacityBound",
            "CarryShellPersistentConcentrationPDECReturn",
            "CarryShellSparseLocalSurvivorOrSAEReturn",
            "CarryShellDisplacementColumnCRTReturn",
        ],
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "structural_law": (
            "For every early-zero high filler atom xP+c=q m with c in R_x and x<q<P, "
            "the cofactor also satisfies x<m<P. With h=P-x, q=P-a, m=P-b and "
            "k=floor(ab/P), one has h=a+b-k and c=ab mod P. Thus high filler support "
            "is not arbitrary: it lies on finite carry shells indexed by h and k. The "
            "bottom deficit curve c=a(h-a) is the k=0 special case. The remaining "
            "primitive PDEC budget is therefore a carry-shell capacity theorem, or a "
            "named return to PDEC/SAE/ColumnCRT if capacity fails by concentration."
        ),
        "plain_conclusion": (
            "本步闭合了早期零行高补洞支撑的精确几何：所有双高因子补洞都落在 "
            "`h=a+b-floor(ab/P), c=ab mod P` 的带进位壳上。于是 "
            "`EarlyZeroPrimitivePDECBudgetInequality` 不再是泛称 PDEC 容量问题，"
            "而被压成 `CarryShellPrimitiveCapacityBoundOrPDECReturn`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    sample = result["sample_audit"]
    lines = [
        "# Prime Matrix 早期零行双高因子带进位壳路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_carry_shell_identity_closed={fmt_bool(result['exact_carry_shell_identity_closed'])}",
        f"bottom_band_k0_recovered={fmt_bool(result['bottom_band_k0_recovered'])}",
        f"early_zero_primitive_pdec_budget_closed={fmt_bool(result['early_zero_primitive_pdec_budget_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 带进位壳恒等式",
        "",
        "假设 `1<=x<P`，`c in R_x`，且该残洞被未完成高素斜线补掉：",
        "",
        "```text",
        "xP+c = q m,  x<q<P.",
        "```",
        "",
        "因为 `c in R_x`，`xP+c` 没有不超过 `x` 的素因子，所以 `m>x`。又 `q>=x+1`，于是",
        "",
        "```text",
        "m = (xP+c)/q < (x+1)P/(x+1) = P.",
        "```",
        "",
        "令",
        "",
        "```text",
        "h=P-x,  q=P-a,  m=P-b,  k=floor(ab/P).",
        "```",
        "",
        "则 `1<=a,b<h`，并且",
        "",
        "```text",
        "(P-a)(P-b) = P(P-a-b+k) + (ab mod P).",
        "```",
        "",
        "与 `xP+c=(P-h)P+c` 比较得到精确恒等式：",
        "",
        "```text",
        "h = a+b-k,",
        "c = ab mod P,",
        "k = floor(ab/P).",
        "```",
        "",
        "这说明高补洞不是任意列覆盖，而是被限制在有限的 `carry shell` 上。",
        "",
        "## 2. 底部带作为 k=0 特例",
        "",
        "若 `h<sqrt(P)`，则 `ab<h^2<P`，所以 `k=0`。恒等式退化为：",
        "",
        "```text",
        "a+b=h,",
        "c=ab=a(h-a).",
        "```",
        "",
        "这正好恢复已有底部缺口对容量定理；底部二次曲线是全局带进位壳的最低层。",
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
            "样本审计只用于防止口径错误；恒等式本身由上面的代数证明给出。",
            "",
            "```text",
            f"sample_status={sample['status']}",
            f"all_factor_windows_ok={fmt_bool(sample['all_factor_windows_ok'])}",
            f"all_carry_identities_ok={fmt_bool(sample['all_carry_identities_ok'])}",
            f"all_bottom_bands_have_zero_carry={fmt_bool(sample['all_bottom_bands_have_zero_carry'])}",
            "```",
            "",
            "| P | high filler hits | max row hits | max carry | positive carry rows | bottom positive carry rows |",
            "| ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in sample["rows"]:
        lines.append(
            "| {p} | {hits} | {maxhits} | {carry} | {pos} | {bottompos} |".format(
                p=row["p"],
                hits=row["total_high_filler_hits"],
                maxhits=row["max_high_filler_hits_in_row"],
                carry=row["max_carry"],
                pos=row["positive_carry_row_count"],
                bottompos=row["bottom_positive_carry_row_count"],
            )
        )
    lines.extend(
        [
            "",
            "## 5. 新最窄剩余",
            "",
            "本步把早期零行终端包中的 primitive PDEC 容量项进一步压缩为：",
            "",
            "```text",
            result["terminal_gap_after_router"],
            "  = CarryShellPrimitiveCapacityBound",
            "    OR CarryShellPersistentConcentrationPDECReturn",
            "    OR CarryShellSparseLocalSurvivorOrSAEReturn",
            "    OR CarryShellDisplacementColumnCRTReturn.",
            "```",
            "",
            "其中真正未闭合的是 `CarryShellPrimitiveCapacityBound`：要证明每个 `h` 壳的双高因子可用列容量不能吃掉整个 `R_x`，或者一旦吃掉就强制产生可排斥的 PDEC/SAE/ColumnCRT 证书。",
            "",
            "因此本步是支撑几何闭合，不是行命题无条件闭合；`row_column_unconditional_closed=false` 仍保持。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_table(result: dict[str, Any]) -> None:
    """输出审计简表。"""
    print(
        "p total_hits max_row_hits max_carry positive_carry_rows bottom_positive_carry_rows",
        flush=True,
    )
    for row in result["sample_audit"]["rows"]:
        print(
            f"{row['p']} {row['total_high_filler_hits']} "
            f"{row['max_high_filler_hits_in_row']} {row['max_carry']} "
            f"{row['positive_carry_row_count']} {row['bottom_positive_carry_row_count']}",
            flush=True,
        )


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-json", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--clb-md", type=Path, default=DEFAULT_CLB)
    parser.add_argument("--bottom-md", type=Path, default=DEFAULT_BOTTOM)
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
        clb_path=args.clb_md,
        bottom_path=args.bottom_md,
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
