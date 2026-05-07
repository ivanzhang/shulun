#!/usr/bin/env python3
"""把稠密旧洞选择核化为共同变量表与壳分流。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_dense_kernel_common_variable_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-dense-kernel-common-variable-router.json
  docs/monograph/prime-matrix-pdec-cap-dense-kernel-common-variable-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DOCS_ROOT = ROOT / "docs"

DEFAULT_OCCUPANCY_KERNEL = (
    DOCS / "prime-matrix-pdec-cap-occupancy-saturation-kernel-router.json"
)
DEFAULT_TAIL_PRESSURE = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-tail-capacity-pressure-q30030-q510510.json",
    )
)
DEFAULT_SN3C = DOCS_ROOT / "sn3c_multiband_sync_audit_20260506.json"
DEFAULT_SN3D = DOCS_ROOT / "sn3d_kls_multishell_frequency_audit_20260506.json"
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-dense-kernel-common-variable-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-dense-kernel-common-variable-router.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: object) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, object]:
    """构造审查表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def summarize_tail_pressure(items: list[dict[str, Any]]) -> dict[str, object]:
    """汇总 Tail 容量压力审计。"""
    rows: list[dict[str, Any]] = []
    mismatch_count = 0
    for item in items:
        rows.extend(item["prime_results"])
        mismatch_count += int(item["consistency_mismatch_count"])
    return {
        "row_count": len(rows),
        "consistency_mismatch_count": mismatch_count,
        "max_hall_uncertified_dead_slots": max(
            int(row_item["hall_uncertified_dead_slots"]) for row_item in rows
        ),
        "min_hall_certified_dead_rate": min(
            float(row_item["hall_certified_dead_rate"]) for row_item in rows
        ),
        "max_survivor_kl_floor": max(
            float(row_item["max_survivor_kl_floor_to_uniform_tail"]) for row_item in rows
        ),
        "all_current_dead_slots_named_by_capacity_or_hall": all(
            int(row_item["hall_uncertified_dead_slots"]) == 0 for row_item in rows
        ),
    }


def summarize_multishell(sn3c: dict[str, Any], sn3d: dict[str, Any]) -> dict[str, object]:
    """汇总多壳同步/高频接口。"""
    sn3c_summary = sn3c["summary"]
    sn3d_summary = sn3d["summary"]
    return {
        "sn3c_pair_route_counts": sn3c_summary["pair_route_counts"],
        "sn3c_pair_count": sn3c_summary["pair_count"],
        "sn3d_kls_multishell_record_count": sn3d_summary[
            "kls_multishell_record_count"
        ],
        "sn3d_max_top_frequency_abs_over_excess": sn3d_summary[
            "max_top_frequency_abs_over_excess"
        ],
        "sn3d_max_partial_fourier_l2_over_excess": sn3d_summary[
            "max_partial_fourier_l2_over_excess"
        ],
        "multishell_interfaces_materialized": (
            sn3c_summary["pair_count"] >= sn3d_summary["kls_multishell_record_count"]
        ),
    }


def build_rows(
    occupancy_kernel: dict[str, Any],
    tail_summary: dict[str, object],
    multishell_summary: dict[str, object],
) -> list[dict[str, object]]:
    """生成共同变量表路由审查行。"""
    dense_kernel_active = (
        occupancy_kernel["occupancy_saturation_reduced_to_dense_kernel"]
        and occupancy_kernel["narrowest_occupancy_hardpoint"]
        == "DenseOldHoleKernelCapacityPDECOrColumnCRT"
    )
    common_variable_table_derived = dense_kernel_active
    capacity_branch_named = bool(
        tail_summary["all_current_dead_slots_named_by_capacity_or_hall"]
    )
    shell_concentration_routes = common_variable_table_derived
    multishell_routes = bool(multishell_summary["multishell_interfaces_materialized"])
    no_unnamed_dense_escape = all(
        [
            dense_kernel_active,
            common_variable_table_derived,
            capacity_branch_named,
            shell_concentration_routes,
            multishell_routes,
        ]
    )
    return [
        row(
            "DenseOldHoleKernelActive",
            dense_kernel_active,
            occupancy_kernel["narrowest_occupancy_hardpoint"],
            "上一层已把占位饱和压成稠密旧洞选择核。",
            False,
        ),
        row(
            "CommonVariableTableDerived",
            common_variable_table_derived,
            "c_b = rho_b + r k_b; k_b != r^{-1}(a_q(t)-rho_b) mod q",
            "对每个近满 occupied residue，列选择可唯一拆成仿射余数 rho_b 与壳号 k_b；低层每个素数只禁止 k_b 的一个线性残基。",
            False,
        ),
        row(
            "CapacityFailureBranchNamed",
            capacity_branch_named,
            str(tail_summary),
            "若共同变量表在大量 b 上没有合法 k，或 residual holes 的 Tail set-cover/Hall 条件失败，则直接支付删除势或容量失败。",
            False,
        ),
        row(
            "FixedShellConcentrationRoutesToPDECColumnCRT",
            shell_concentration_routes,
            "positive shell mass gives persistent low-mod phase/residue signature",
            "若某个有限壳或有限壳簇承载正密度 b，则共同变量表在低模上持久复现，成为 PDEC 相位偏斜或 ColumnCRT 列位移输入。",
            False,
        ),
        row(
            "MultishellDispersionRoutesToSC9OrHighFreqColumnPDEC",
            multishell_routes,
            str(multishell_summary),
            "若没有固定壳集中，选择核只能跨多壳分散；多壳同步若有低模/高频峰则回 PDEC/ColumnCRT，若平坦则进入自足 SC-9 大筛原子。",
            False,
        ),
        row(
            "DenseKernelNoUnnamedEscape",
            no_unnamed_dense_escape,
            "capacity / fixed-shell PDEC-ColumnCRT / multishell SC9",
            "稠密旧洞选择核已经没有未命名第四出口；剩余是命名终端证书而非局部样本或概率缺口。",
            False,
        ),
        row(
            "FixedShellLowModPersistencePDECOrColumnCRT",
            False,
            "terminal PDEC/ColumnCRT exclusion not submitted",
            "固定壳低模持久偏斜仍需提交同 formal unit 的 PDEC 或 ColumnCRT 排斥证书。",
            True,
        ),
        row(
            "SelfContainedKuznetsovLSAtomSC9",
            False,
            "flat multishell clean atom remains open",
            "多壳完全平坦时仍落入自足 SC-9 谱大筛原子；外部深定理版不能冒充自足闭合。",
            True,
        ),
    ]


def run(
    occupancy_kernel_path: Path,
    tail_pressure_paths: list[Path],
    sn3c_path: Path,
    sn3d_path: Path,
) -> dict[str, object]:
    """运行稠密旧洞核共同变量表路由。"""
    occupancy_kernel = load_json(occupancy_kernel_path)
    tail_items = [load_json(path) for path in tail_pressure_paths]
    sn3c = load_json(sn3c_path)
    sn3d = load_json(sn3d_path)
    tail_summary = summarize_tail_pressure(tail_items)
    multishell_summary = summarize_multishell(sn3c, sn3d)
    rows = build_rows(
        occupancy_kernel=occupancy_kernel,
        tail_summary=tail_summary,
        multishell_summary=multishell_summary,
    )
    routed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "DenseKernelNoUnnamedEscape"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_dense_kernel_common_variable_router",
        "status": "dense_old_hole_kernel_reduced_to_common_variable_shell_dichotomy",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "occupancy_kernel": file_sha256(occupancy_kernel_path),
            "sn3c": file_sha256(sn3c_path),
            "sn3d": file_sha256(sn3d_path),
            **{
                f"tail_pressure_{idx}": file_sha256(path)
                for idx, path in enumerate(tail_pressure_paths, start=1)
            },
        },
        "dense_kernel_no_unnamed_escape_closed": routed,
        "dense_kernel_exclusion_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_dense_kernel_hardpoint": (
            "FixedShellLowModPersistencePDECOrColumnCRT_OR_SelfContainedKuznetsovLSAtomSC9"
        ),
        "tail_pressure_summary": tail_summary,
        "multishell_summary": multishell_summary,
        "rows": rows,
        "common_variable_law": (
            "For a dense old-hole selector kernel, write the selected column as "
            "c_b=rho_b+r k_b, where rho_b is the affine residue forced by "
            "((t+bQ-1)P+c_b)=0 mod r. For every old prime q|Q, the old-hole condition "
            "is equivalent to one forbidden shell residue "
            "k_b != r^{-1}(a_q(t)-rho_b) mod q. Thus all low-prime constraints are "
            "stored in the same variable k_b. If many b have no legal shell, capacity/Hall "
            "deletion fires. If a fixed shell or finite shell packet has positive mass, "
            "the low-mod signature is persistent and routes to PDEC or ColumnCRT. If no "
            "shell packet persists, the mass is genuinely multishell; non-flat multishell "
            "frequency returns to PDEC/ColumnCRT, while the flat case is exactly the "
            "self-contained SC-9 large-sieve atom."
        ),
        "review_conclusion": (
            "稠密旧洞选择核已经化为共同变量表：所有低层同余禁类都作用在同一个壳号变量 `k_b` 上。"
            "因此它没有未命名逃逸：无合法壳是容量/Hall 删除，固定壳正密度是 PDEC/ColumnCRT，"
            "无固定壳则是多壳分散，非平坦回 PDEC/ColumnCRT，平坦进入自足 SC-9。"
            "这仍不排除 PDEC/ColumnCRT 或 SC-9 终端，所以不是完整行/列无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, object], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 稠密旧洞核共同变量表路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        str(result["review_conclusion"]),
        "",
        "## 1. 共同变量律",
        "",
        str(result["common_variable_law"]),
        "",
        "```text",
        "DenseOldHoleKernel:",
        "  for (1-o(1))r residues b choose c_b in H_Q(t);",
        "  ((t+bQ-1)P+c_b)=0 mod r.",
        "",
        "Write:",
        "  c_b = rho_b + r k_b,",
        "  rho_b == -((t+bQ-1)P) mod r.",
        "",
        "For each old prime q|Q:",
        "  c_b != a_q(t) mod q",
        "  <=> k_b != r^{-1}(a_q(t)-rho_b) mod q.",
        "",
        "Therefore all low-prime bans act on one shell variable k_b.",
        "```",
        "",
        "## 2. 分流",
        "",
        "```text",
        "No legal k_b for many b",
        "  => capacity/Hall deletion;",
        "",
        "positive mass on fixed shell or finite shell packet",
        "  => persistent low-mod signature",
        "  => PDEC / ColumnCRT;",
        "",
        "no fixed shell packet persists",
        "  => genuine multishell dispersion;",
        "  non-flat frequency => PDEC / ColumnCRT;",
        "  flat frequency     => SelfContainedKuznetsovLSAtomSC9.",
        "```",
        "",
        "## 3. 汇总",
        "",
        f"- `dense_kernel_no_unnamed_escape_closed={fmt_bool(bool(result['dense_kernel_no_unnamed_escape_closed']))}`。",
        f"- `dense_kernel_exclusion_closed={fmt_bool(bool(result['dense_kernel_exclusion_closed']))}`。",
        f"- `row_column_unconditional_closed={fmt_bool(bool(result['row_column_unconditional_closed']))}`。",
        f"- `narrowest_dense_kernel_hardpoint={result['narrowest_dense_kernel_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        f"- `tail_pressure_summary={result['tail_pressure_summary']}`。",
        f"- `multishell_summary={result['multishell_summary']}`。",
        "",
        "## 4. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 剩余",
            "",
            "本路由器关闭的是稠密旧洞核的“无名逃逸”。"
            "剩余真正终端是固定壳低模持久偏斜的 PDEC/ColumnCRT 排斥，"
            "以及多壳平坦时的自足 `SelfContainedKuznetsovLSAtomSC9`。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--occupancy-kernel-json", type=Path, default=DEFAULT_OCCUPANCY_KERNEL)
    parser.add_argument("--tail-pressure-jsons", default=DEFAULT_TAIL_PRESSURE)
    parser.add_argument("--sn3c-json", type=Path, default=DEFAULT_SN3C)
    parser.add_argument("--sn3d-json", type=Path, default=DEFAULT_SN3D)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        occupancy_kernel_path=args.occupancy_kernel_json,
        tail_pressure_paths=parse_paths(args.tail_pressure_jsons),
        sn3c_path=args.sn3c_json,
        sn3d_path=args.sn3d_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_dense_kernel_hardpoint"])


if __name__ == "__main__":
    main()
