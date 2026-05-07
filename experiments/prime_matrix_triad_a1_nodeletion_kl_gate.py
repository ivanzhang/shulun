#!/usr/bin/env python3
"""审计 Triad-A1 NoDeletion 层的 KL/PDEC/CleanKLS 门控。

用法示例：
  python3 experiments/prime_matrix_triad_a1_nodeletion_kl_gate.py
  python3 experiments/prime_matrix_triad_a1_nodeletion_kl_gate.py --nodeletion-survival 0.95

输出：
  docs/monograph/prime-matrix-triad-a1-nodeletion-kl-gate.json
  docs/monograph/prime-matrix-triad-a1-nodeletion-kl-gate.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_AUDITS = ",".join(
    str(path)
    for path in (
        DOCS / "prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.json",
        DOCS / "prime-matrix-triad-a1-newlayer-fiber-audit-q30030-q510510.json",
    )
)
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-nodeletion-kl-gate.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-nodeletion-kl-gate.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def classify_gate(
    survival: float | None,
    normalized_kl: float | None,
    nodeletion_survival: float,
    kl_pdec_threshold: float,
    clean_kl_threshold: float,
) -> str:
    """按删除与 KL 门控分类。"""
    if survival is None:
        return "EmptyOrInvalid"
    if survival < nodeletion_survival:
        return "FiberDeletion"
    if normalized_kl is None:
        return "NoDeletionNeedsKLInput"
    if normalized_kl >= kl_pdec_threshold:
        return "NoDeletionKLPDEC"
    if normalized_kl <= clean_kl_threshold:
        return "NoDeletionCleanKLSCandidate"
    return "NoDeletionMixedKL"


def pinsker_tv_bound(kl_nats: float | None) -> float | None:
    """由 Pinsker 给出总变差上界 sqrt(KL/2)。"""
    if kl_nats is None:
        return None
    return min(1.0, math.sqrt(max(0.0, kl_nats) / 2.0))


def analyze_audit(
    path: Path,
    audit: dict[str, Any],
    nodeletion_survival: float,
    kl_pdec_threshold: float,
    clean_kl_threshold: float,
) -> list[dict[str, Any]]:
    """展开单个 fiber 审计。"""
    rows = []
    for item in audit["prime_results"]:
        survival = item["support_accounting"]["slot_survival_rate"]
        normalized_kl = item["fiber_shape"]["avg_normalized_kl_to_uniform_by_lift_mass"]
        kl_nats = normalized_kl * math.log(audit["fiber_size"]) if normalized_kl is not None else None
        gate = classify_gate(
            survival,
            normalized_kl,
            nodeletion_survival,
            kl_pdec_threshold,
            clean_kl_threshold,
        )
        rows.append(
            {
                "audit_path": str(path),
                "q": audit["q"],
                "q_lift": audit["q_lift"],
                "fiber_size": audit["fiber_size"],
                "p": item["p"],
                "survival": survival,
                "deletion": item["support_accounting"]["slot_deletion_rate"],
                "density_drop_factor": item["density_accounting"]["density_drop_factor"],
                "normalized_entropy": item["fiber_shape"]["avg_normalized_entropy_by_lift_mass"],
                "normalized_kl_to_uniform": normalized_kl,
                "kl_nats_to_uniform": kl_nats,
                "pinsker_tv_upper_from_kl": pinsker_tv_bound(kl_nats),
                "gate": gate,
            }
        )
    return rows


def run(
    audit_paths: list[Path],
    nodeletion_survival: float,
    kl_pdec_threshold: float,
    clean_kl_threshold: float,
) -> dict[str, Any]:
    """运行 NoDeletion-KL 门控审计。"""
    audits = [(path, load_json(path)) for path in audit_paths]
    rows = [
        row
        for path, audit in audits
        for row in analyze_audit(
            path,
            audit,
            nodeletion_survival,
            kl_pdec_threshold,
            clean_kl_threshold,
        )
    ]
    gate_counts: dict[str, int] = {}
    for row in rows:
        gate_counts[row["gate"]] = gate_counts.get(row["gate"], 0) + 1

    return {
        "certificate_type": "triad_a1_nodeletion_kl_gate",
        "status": "nodeletion_kl_gate_materialized_current_layers_deleting",
        "parameters": {
            "nodeletion_survival": nodeletion_survival,
            "kl_pdec_threshold": kl_pdec_threshold,
            "clean_kl_threshold": clean_kl_threshold,
            "threshold_meaning": (
                "阈值只用于有限审计分流；结构定理使用极限：survival->1 后按 KL 是否累计分支。"
            ),
        },
        "source_hashes": {
            "nodeletion_kl_gate_script": file_sha256(Path(__file__).resolve()),
            **{
                f"audit_{idx}": file_sha256(path)
                for idx, (path, _audit) in enumerate(audits, start=1)
            },
        },
        "rows": rows,
        "gate_counts": gate_counts,
        "nodeletion_rows": [
            row for row in rows if row["gate"].startswith("NoDeletion")
        ],
        "current_nodeletion_triggered": any(
            row["gate"].startswith("NoDeletion") for row in rows
        ),
        "gate_law": (
            "若 survival 未趋近 1，则仍在 FiberDeletion。若 survival->1 且 KL 在正质量层上累计，"
            "进入 new-layer PDEC；若 KL 可求和并趋零，则进入 CleanKLS/DLS。"
        ),
        "review_conclusion": (
            "当前已物化层没有触发 NoDeletion；全部仍在 FiberDeletion。"
            "本文件给出后续层一旦删除停止时的 KL 分流接口。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点值。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    params = result["parameters"]
    lines = [
        "# Triad-A1 NoDeletion-KL 门控审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 门控律",
        "",
        result["gate_law"],
        "",
        "有限审计阈值：",
        "",
        f"- `nodeletion_survival={params['nodeletion_survival']}`。",
        f"- `kl_pdec_threshold={params['kl_pdec_threshold']}`。",
        f"- `clean_kl_threshold={params['clean_kl_threshold']}`。",
        "",
        "这些阈值只用于当前报告分流；正式极限命题使用 `survival->1` 与 `sum KL`。",
        "",
        "## 2. 来源指纹",
        "",
        "| source | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")

    lines.extend(
        [
            "",
            "## 3. 门控统计",
            "",
            f"- `current_nodeletion_triggered={result['current_nodeletion_triggered']}`。",
            f"- `gate_counts={result['gate_counts']}`。",
            "",
            "## 4. 明细",
            "",
            "| layer | P | survival | deletion | drop | norm entropy | norm KL | KL nats | Pinsker TV | gate |",
            "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| Q={q}->{ql} | {p} | {surv} | {dele} | {drop} | {ent} | {kl} | {kln} | {tv} | `{gate}` |".format(
                q=row["q"],
                ql=row["q_lift"],
                p=row["p"],
                surv=fmt_float(row["survival"]),
                dele=fmt_float(row["deletion"]),
                drop=fmt_float(row["density_drop_factor"]),
                ent=fmt_float(row["normalized_entropy"]),
                kl=fmt_float(row["normalized_kl_to_uniform"]),
                kln=fmt_float(row["kl_nats_to_uniform"]),
                tv=fmt_float(row["pinsker_tv_upper_from_kl"]),
                gate=row["gate"],
            )
        )

    lines.extend(
        [
            "",
            "## 5. 读法",
            "",
            "当前没有 `NoDeletion` 行，说明已物化层仍靠 fiber 删除推进。后续若出现 `NoDeletionCleanKLSCandidate`，",
            "必须检查 CleanKLS admission；若出现 `NoDeletionKLPDEC`，则把该层作为 refined/new-layer PDEC 输入。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audits", default=DEFAULT_AUDITS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    parser.add_argument("--nodeletion-survival", type=float, default=0.9)
    parser.add_argument("--kl-pdec-threshold", type=float, default=0.25)
    parser.add_argument("--clean-kl-threshold", type=float, default=0.05)
    args = parser.parse_args()

    result = run(
        parse_paths(args.audits),
        args.nodeletion_survival,
        args.kl_pdec_threshold,
        args.clean_kl_threshold,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "current_nodeletion_triggered": result["current_nodeletion_triggered"],
                "gate_counts": result["gate_counts"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
