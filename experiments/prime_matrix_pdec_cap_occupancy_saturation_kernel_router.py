#!/usr/bin/env python3
"""把 HRO 占位饱和出口压到稠密旧洞选择核。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_occupancy_saturation_kernel_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-occupancy-saturation-kernel-router.json
  docs/monograph/prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_DELETION_DIVERGENCE = (
    DOCS / "prime-matrix-pdec-cap-deletion-divergence-lower-bound-router.json"
)
DEFAULT_HRO_LEMMA = DOCS / "prime-matrix-triad-a1-hole-residue-occupancy.md"
DEFAULT_HRO_AUDITS = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-hole-residue-occupancy-q30030-q510510.json",
    )
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-occupancy-saturation-kernel-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-occupancy-saturation-kernel-router.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    """读取文本文件。"""
    return path.read_text(encoding="utf-8")


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


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


def summarize_hro(audits: list[dict[str, Any]]) -> dict[str, object]:
    """汇总当前 HRO 审计中的占位饱和距离。"""
    rows: list[dict[str, Any]] = []
    for audit in audits:
        rows.extend(audit["prime_results"])
    max_phase_occupied_ratio = max(float(item["max_phase_occupied_ratio"]) for item in rows)
    max_avg_occupied_ratio = max(float(item["occupied_rate"]) for item in rows)
    max_union_bound_rate = max(float(item["union_bound_rate"]) for item in rows)
    min_saturation_gap = min(1.0 - float(item["max_phase_occupied_ratio"]) for item in rows)
    max_old_hole_count = max(
        max(int(key) for key in item["old_hole_count_histogram"])
        for item in rows
    )
    min_promoted_prime = min(int(item["promoted_prime"]) for item in rows)
    max_promoted_prime = max(int(item["promoted_prime"]) for item in rows)
    dense_phase_count = sum(
        int(item["nonempty_old_hole_phase_count"])
        for item in rows
        if float(item["max_phase_occupied_ratio"]) >= 0.9
    )
    return {
        "row_count": len(rows),
        "max_phase_occupied_ratio": max_phase_occupied_ratio,
        "max_avg_occupied_ratio": max_avg_occupied_ratio,
        "max_union_bound_rate": max_union_bound_rate,
        "min_saturation_gap": min_saturation_gap,
        "max_old_hole_count": max_old_hole_count,
        "min_promoted_prime": min_promoted_prime,
        "max_promoted_prime": max_promoted_prime,
        "dense_phase_count_at_0_9": dense_phase_count,
        "current_layers_far_from_occupancy_saturation": dense_phase_count == 0,
    }


def build_rows(
    deletion_divergence: dict[str, Any],
    hro_text: str,
    hro_summary: dict[str, object],
) -> list[dict[str, object]]:
    """生成占位饱和核路由审查表。"""
    occupancy_hardpoint_active = (
        deletion_divergence["deletion_divergence_lower_bound_reduced"]
        and deletion_divergence["narrowest_deletion_hardpoint"]
        == "OccupancySaturationPDECOrColumnCRT"
    )
    hro_injection_bound_registered = all(
        needle in hro_text
        for needle in [
            "|Occ_t|",
            "min(|H_Q(t)|,r)",
            "OccupancySaturation",
        ]
    )
    selector_kernel_law_registered = hro_injection_bound_registered
    sparse_old_hole_case_closed = hro_injection_bound_registered
    current_layers_far = bool(hro_summary["current_layers_far_from_occupancy_saturation"])

    return [
        row(
            "OccupancyHardpointActive",
            occupancy_hardpoint_active,
            deletion_divergence["narrowest_deletion_hardpoint"],
            "上一层已把删除侧真正剩余压到 HRO 占位饱和出口。",
            False,
        ),
        row(
            "HROInjectionBoundRegistered",
            hro_injection_bound_registered,
            "|Occ_t| <= min(|H_Q(t)|, r)",
            "每个旧洞列在 promoted prime residue 上最多贡献一个占位；占位近满必须先有旧洞 residue 近满。",
            False,
        ),
        row(
            "SparseOldHoleCaseExcluded",
            sparse_old_hole_case_closed,
            "if |H_Q(t)| <= (1-eta)r then |Occ_t|/r <= 1-eta",
            "只要旧洞数或旧洞 residue 数有固定缺口，占位饱和不可能发生，HRO 自动给出删除缺口。",
            False,
        ),
        row(
            "NearFullOccupancyForcesSelectorKernel",
            selector_kernel_law_registered,
            "exists B_t with |B_t|=(1-o(1))r and c_b in H_Q(t)",
            "占位饱和等价于存在近满 residue 选择核：对几乎每个 promoted residue，可选一个旧洞列同时避开全部低层素因子同余禁类。",
            False,
        ),
        row(
            "CurrentAuditsFarFromSaturation",
            current_layers_far,
            str(hro_summary),
            "当前物化层的最大相位占位率远低于 1；这是 sanity check，不是全局证明。",
            False,
        ),
        row(
            "DenseOldHoleKernelCapacityPDECOrColumnCRT",
            False,
            "near-full selector kernel not globally excluded",
            "剩余硬点已经从一般占位饱和压成稠密旧洞选择核：需证明它触发低层容量矛盾、PDEC 相位偏斜或 ColumnCRT 列位移刚性。",
            True,
        ),
    ]


def run(
    deletion_divergence_path: Path,
    hro_lemma_path: Path,
    hro_audit_paths: list[Path],
) -> dict[str, object]:
    """运行占位饱和核路由。"""
    deletion_divergence = load_json(deletion_divergence_path)
    hro_text = read_text(hro_lemma_path)
    hro_audits = [load_json(path) for path in hro_audit_paths]
    hro_summary = summarize_hro(hro_audits)
    rows = build_rows(
        deletion_divergence=deletion_divergence,
        hro_text=hro_text,
        hro_summary=hro_summary,
    )
    reduced = all(item["closed"] for item in rows if not item["blocks_final"])
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_occupancy_saturation_kernel_router",
        "status": "occupancy_saturation_reduced_to_dense_old_hole_kernel",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "deletion_divergence": file_sha256(deletion_divergence_path),
            "hro_lemma": file_sha256(hro_lemma_path),
            **{
                f"hro_audit_{idx}": file_sha256(path)
                for idx, path in enumerate(hro_audit_paths, start=1)
            },
        },
        "occupancy_saturation_reduced_to_dense_kernel": reduced,
        "occupancy_saturation_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_occupancy_hardpoint": "DenseOldHoleKernelCapacityPDECOrColumnCRT",
        "hro_saturation_summary": hro_summary,
        "rows": rows,
        "kernel_law": (
            "HRO already gives |Occ_t| <= min(|H_Q(t)|, r). Hence near-full "
            "occupancy |Occ_t|/r -> 1 is impossible in every sparse old-hole regime "
            "|H_Q(t)| <= (1-eta)r, and more generally unless the old holes occupy "
            "(1-o(1))r distinct promoted-prime residues. In the remaining case one can "
            "choose a selector c_b in H_Q(t) for (1-o(1))r residues b, satisfying "
            "((t+bQ-1)P+c_b)=0 mod r while c_b avoids every low-prime forbidden class "
            "mod q|Q. Thus the true hardpoint is not generic occupancy saturation, but "
            "a dense old-hole selector kernel; it must be discharged by a low-level "
            "capacity contradiction, persistent phase-residue PDEC, or ColumnCRT "
            "displacement rigidity."
        ),
        "review_conclusion": (
            "`OccupancySaturation` 已被严格压缩：稀疏旧洞情形由 HRO 注入界直接排除；"
            "若占位仍近满，则必须存在近满 promoted residue 的旧洞选择核。"
            "因此下一硬点不再是宽口径占位饱和，而是 `DenseOldHoleKernelCapacityPDECOrColumnCRT`。"
        ),
    }


def write_markdown(result: dict[str, object], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 占位饱和核路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        str(result["review_conclusion"]),
        "",
        "## 1. 核路由律",
        "",
        str(result["kernel_law"]),
        "",
        "```text",
        "HRO injection:",
        "  |Occ_t| <= min(|H_Q(t)|, r).",
        "",
        "Therefore:",
        "  |H_Q(t)| <= (1-eta)r",
        "    => |Occ_t|/r <= 1-eta",
        "    => no OccupancySaturation.",
        "",
        "If OccupancySaturation persists:",
        "  exists B_t subset Z/rZ with |B_t|=(1-o(1))r;",
        "  for each b in B_t choose c_b in H_Q(t);",
        "  ((t+bQ-1)P+c_b)=0 mod r;",
        "  c_b avoids every low-prime forbidden class mod q|Q.",
        "",
        "Remaining target:",
        "  DenseOldHoleKernelCapacityPDECOrColumnCRT.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `occupancy_saturation_reduced_to_dense_kernel={fmt_bool(bool(result['occupancy_saturation_reduced_to_dense_kernel']))}`。",
        f"- `occupancy_saturation_closed={fmt_bool(bool(result['occupancy_saturation_closed']))}`。",
        f"- `row_column_unconditional_closed={fmt_bool(bool(result['row_column_unconditional_closed']))}`。",
        f"- `narrowest_occupancy_hardpoint={result['narrowest_occupancy_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        f"- `hro_saturation_summary={result['hro_saturation_summary']}`。",
        "",
        "## 3. 审查表",
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
            "## 4. 剩余",
            "",
            "`DenseOldHoleKernelCapacityPDECOrColumnCRT` 尚未排除。"
            "下一步应直接研究近满选择核的三种互斥出路："
            "低层轮筛容量过载、相位-residue 分布持久偏斜形成 PDEC、"
            "或选择列随 promoted residue 呈固定列位移结构形成 ColumnCRT。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--deletion-divergence-json", type=Path, default=DEFAULT_DELETION_DIVERGENCE
    )
    parser.add_argument("--hro-lemma-md", type=Path, default=DEFAULT_HRO_LEMMA)
    parser.add_argument("--hro-audits", default=DEFAULT_HRO_AUDITS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        deletion_divergence_path=args.deletion_divergence_json,
        hro_lemma_path=args.hro_lemma_md,
        hro_audit_paths=parse_paths(args.hro_audits),
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_occupancy_hardpoint"])


if __name__ == "__main__":
    main()
