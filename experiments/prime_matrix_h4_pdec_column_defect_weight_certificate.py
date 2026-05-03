#!/usr/bin/env python3
"""生成 H4-PDEC ColumnDefect 有限相位兼容权重证书。

用法示例：
  python3 experiments/prime_matrix_h4_pdec_column_defect_weight_certificate.py
  python3 experiments/prime_matrix_h4_pdec_column_defect_weight_certificate.py --max-p 1000

本脚本承接 `prime_matrix_rci_cdb_joint_audit.py` 的紧行审计数据，把两个有限
ColumnDefect 行物化为机器可读证书：

1. `CC-FIN-TIGHT-RADIUS`：紧行中 `D_col>81` 的相位块为空；
2. `CC-FIN-DISPLOAD`：紧行中位移余类负载 `>2` 的相位块为空。

注意：这里使用的有限相位是 `tau_fin=(p,q,row)`。这保证权重对相位兼容，
但它不是全局 PDEC 的原始 `tau`。若要写入全局对偶证书，仍需给出从正式坏窗
抽取到该有限相位域的同口径映射。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from prime_matrix_rci_cdb_joint_audit import audit


def sha256_file(path: Path) -> str:
    """计算文件 SHA256，供证书复现核验。"""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def phase_key(row: dict) -> str:
    """把一条紧行记录编码为有限相位键。"""
    return "p={p};q={q};row={row}".format(
        p=row["p"],
        q=row["q"],
        row=row["row"],
    )


def collect_tight_rows(result: dict) -> list[dict]:
    """提取全部紧行记录并补充有限相位键。"""
    rows: list[dict] = []
    for record in result["records"]:
        for row in record["tight_rows"]:
            row_with_phase = dict(row)
            row_with_phase["tau_fin"] = phase_key(row)
            rows.append(row_with_phase)
    return rows


def make_certificate(
    *,
    max_p: int,
    y_ratio: float,
    keep_rows: int,
    radius_threshold: int,
    displacement_threshold: int,
) -> dict:
    """构造有限权重证书。"""
    result = audit(max_p=max_p, y_ratio=y_ratio, keep_rows=keep_rows)
    tight_rows = collect_tight_rows(result)

    radius_block = [
        row["tau_fin"]
        for row in tight_rows
        if row["max_column_witness_radius"] > radius_threshold
    ]
    displacement_block = [
        row["tau_fin"]
        for row in tight_rows
        if row["max_displacement_residue_load"] > displacement_threshold
    ]

    max_radius = max(row["max_column_witness_radius"] for row in tight_rows)
    max_displacement_load = max(
        row["max_displacement_residue_load"] for row in tight_rows
    )

    rows = [
        {
            "row_id": "CC-FIN-TIGHT-RADIUS-WEIGHT",
            "source_ledger_row": "CC-FIN-TIGHT-RADIUS",
            "admissibility": "FiniteCertWithRefinedTau",
            "tau": "tau_fin=(p,q,row)",
            "weight_name": "W_D",
            "event": "max_column_witness_radius > radius_threshold",
            "threshold": radius_threshold,
            "observed_max": max_radius,
            "phase_block": radius_block,
            "bound": 0,
            "pass": len(radius_block) == 0,
            "scope": "p<=max_p, keep_rows tight RCI rows for each p",
            "global_use_requires": [
                "同口径坏窗到 tau_fin 的抽取映射",
                "证明正式坏窗属于该有限域",
                "或给出全局 D_0 解析阈值",
            ],
        },
        {
            "row_id": "CC-FIN-DISPLOAD-WEIGHT",
            "source_ledger_row": "CC-FIN-DISPLOAD",
            "admissibility": "FiniteCertWithRefinedTau",
            "tau": "tau_fin=(p,q,row)",
            "weight_name": "W_{ell,a}",
            "event": "max_displacement_residue_load > displacement_threshold",
            "threshold": displacement_threshold,
            "observed_max": max_displacement_load,
            "phase_block": displacement_block,
            "bound": 0,
            "pass": len(displacement_block) == 0,
            "scope": "p<=max_p, keep_rows tight RCI rows for each p",
            "global_use_requires": [
                "同口径坏窗到 tau_fin 的抽取映射",
                "证明正式坏窗属于该有限域",
                "或给出全局 L_D 解析阈值",
            ],
        },
    ]

    return {
        "status": "finite_column_defect_weight_certificate_not_global_exclusion",
        "source_files": {
            "generator": {
                "path": "experiments/prime_matrix_h4_pdec_column_defect_weight_certificate.py",
                "sha256": sha256_file(Path(__file__)),
            },
            "audit_module": {
                "path": "experiments/prime_matrix_rci_cdb_joint_audit.py",
                "sha256": sha256_file(Path(__file__).with_name("prime_matrix_rci_cdb_joint_audit.py")),
            },
        },
        "parameters": {
            "max_p": max_p,
            "y_ratio": y_ratio,
            "keep_rows": keep_rows,
            "radius_threshold": radius_threshold,
            "displacement_threshold": displacement_threshold,
        },
        "domain": {
            "tau": "tau_fin=(p,q,row)",
            "phase_count": len(tight_rows),
            "prime_count": result["summary"]["prime_count"],
            "phase_compatibility": (
                "weights are functions of tau_fin, hence compatible on this finite domain"
            ),
        },
        "summary": {
            "all_rows_pass": all(row["pass"] for row in rows),
            "observed_max_column_radius": max_radius,
            "observed_max_displacement_residue_load": max_displacement_load,
            "nonempty_blocks": [
                row["row_id"] for row in rows if len(row["phase_block"]) > 0
            ],
        },
        "certificate_rows": rows,
        # 保留紧行摘要，方便审稿人复核最大值来源；不展开每列见证细节。
        "tight_row_domain": tight_rows,
    }


def write_markdown(certificate: dict, path: Path) -> None:
    """写 Markdown 证书摘要。"""
    params = certificate["parameters"]
    domain = certificate["domain"]
    summary = certificate["summary"]
    sources = certificate["source_files"]
    all_rows_pass = str(summary["all_rows_pass"]).lower()
    nonempty_blocks = json.dumps(summary["nonempty_blocks"], ensure_ascii=False)
    lines = [
        "# H4-PDEC ColumnDefect 有限权重证书",
        "",
        "**状态：** `finite_column_defect_weight_certificate_not_global_exclusion`",
        "",
        "## 参数",
        "",
        f"- `max_p`: `{params['max_p']}`",
        f"- `y_ratio`: `{params['y_ratio']}`",
        f"- `keep_rows`: `{params['keep_rows']}`",
        f"- `radius_threshold`: `{params['radius_threshold']}`",
        f"- `displacement_threshold`: `{params['displacement_threshold']}`",
        "",
        "## 复现来源",
        "",
        f"- 生成脚本：`{sources['generator']['path']}`",
        f"- 生成脚本 SHA256：`{sources['generator']['sha256']}`",
        f"- 审计模块：`{sources['audit_module']['path']}`",
        f"- 审计模块 SHA256：`{sources['audit_module']['sha256']}`",
        "",
        "## 有限相位域",
        "",
        f"- `tau`: `{domain['tau']}`",
        f"- `phase_count`: `{domain['phase_count']}`",
        f"- `prime_count`: `{domain['prime_count']}`",
        "- 相位兼容性：权重只依赖 `tau_fin=(p,q,row)`，因此在本有限域中相位兼容。",
        "",
        "## 证书结论",
        "",
        f"- 全部证书行通过：`{all_rows_pass}`。",
        f"- 观测最大列见证半径：`{summary['observed_max_column_radius']}`。",
        f"- 观测最大位移余类负载：`{summary['observed_max_displacement_residue_load']}`。",
        f"- 非空异常块：`{nonempty_blocks}`。",
        "",
        "## 证书行",
        "",
        "| row_id | event | threshold | observed_max | phase_block_size | bound | pass |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for row in certificate["certificate_rows"]:
        lines.append(
            "| {row_id} | `{event}` | {threshold} | {observed_max} | {size} | {bound} | `{passed}` |".format(
                row_id=row["row_id"],
                event=row["event"],
                threshold=row["threshold"],
                observed_max=row["observed_max"],
                size=len(row["phase_block"]),
                bound=row["bound"],
                passed=str(row["pass"]).lower(),
            )
        )

    lines.extend(
        [
            "",
            "## 审稿边界",
            "",
            f"本证书只闭合 `p<={params['max_p']}` 且每个 `p` 只取 `{params['keep_rows']}` 条最紧 RCI 行的有限相位兼容权重物化。",
            "它不能直接排除全局 `ColumnRadiusDefect` 或 `ColumnCRTDefect`，也不能替代全局阈值 `D_0,L_D` 的解析证明。",
            "",
            "若要进入全局 `PDEC-Dual-Cert`，还需证明正式坏窗抽取过程落在同一有限相位域，或把 `tau_fin` 的权重结构提升为全局相位兼容定理。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-p", type=int, default=1000)
    parser.add_argument("--y-ratio", type=float, default=1 / math.e)
    parser.add_argument("--keep-rows", type=int, default=5)
    parser.add_argument("--radius-threshold", type=int, default=81)
    parser.add_argument("--displacement-threshold", type=int, default=2)
    parser.add_argument(
        "--out-prefix",
        default="docs/monograph/h4-pdec-column-defect-weight-certificate",
    )
    args = parser.parse_args()

    certificate = make_certificate(
        max_p=args.max_p,
        y_ratio=args.y_ratio,
        keep_rows=args.keep_rows,
        radius_threshold=args.radius_threshold,
        displacement_threshold=args.displacement_threshold,
    )
    prefix = Path(args.out_prefix)
    prefix.with_suffix(".json").write_text(
        json.dumps(certificate, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(certificate, prefix.with_suffix(".md"))

    compact = {
        "status": certificate["status"],
        "domain": certificate["domain"],
        "summary": certificate["summary"],
    }
    print(json.dumps(compact, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
