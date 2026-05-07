#!/usr/bin/env python3
"""汇总 Triad-A1 多层 new-layer fiber 审计，形成塔门控证书。

用法示例：
  python3 experiments/prime_matrix_triad_a1_newlayer_tower_gate.py \
    --audits docs/monograph/prime-matrix-triad-a1-newlayer-fiber-audit-q2310-q30030.json,docs/monograph/prime-matrix-triad-a1-newlayer-fiber-audit-q30030-q510510.json

输出：
  docs/monograph/prime-matrix-triad-a1-newlayer-tower-gate.json
  docs/monograph/prime-matrix-triad-a1-newlayer-tower-gate.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
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
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-newlayer-tower-gate.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-newlayer-tower-gate.md"


def parse_paths(raw: str) -> list[Path]:
    """解析逗号分隔路径列表。"""
    return [Path(item.strip()) for item in raw.split(",") if item.strip()]


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def classify_layer(audit: dict[str, Any]) -> str:
    """按单层审计结果分类。"""
    if not audit["all_support_identities_hold"]:
        return "InvalidAccounting"
    if not audit["all_monotone_lift_support"]:
        return "ProjectionStitchingNeeded"
    if audit["all_classified_resparse"]:
        return "FiberDeletionLayer"
    entropy_values = [
        item["fiber_shape"]["avg_normalized_entropy_by_lift_mass"]
        for item in audit["prime_results"]
        if item["fiber_shape"]["avg_normalized_entropy_by_lift_mass"] is not None
    ]
    if entropy_values and min(entropy_values) >= audit["thresholds"]["flat_entropy_threshold"]:
        return "NearUniformCleanKLSLayer"
    return "MixedLayerNeedsPDECEntropy"


def summarize_layer(path: Path, audit: dict[str, Any]) -> dict[str, Any]:
    """汇总单层审计。"""
    prime_rows = []
    for item in audit["prime_results"]:
        support = item["support_accounting"]
        density = item["density_accounting"]
        shape = item["fiber_shape"]
        prime_rows.append(
            {
                "p": item["p"],
                "old_support_count": item["old_support_count"],
                "lift_support_count": item["lift_support_count"],
                "slot_survival_rate": support["slot_survival_rate"],
                "slot_deletion_rate": support["slot_deletion_rate"],
                "density_drop_factor": density["density_drop_factor"],
                "support_count_histogram": shape["support_count_histogram"],
                "avg_normalized_entropy_by_lift_mass": shape[
                    "avg_normalized_entropy_by_lift_mass"
                ],
                "classification": item["classification"],
            }
        )
    min_drop = min((row["density_drop_factor"] for row in prime_rows), default=None)
    max_survival = max((row["slot_survival_rate"] for row in prime_rows), default=None)
    max_entropy = max(
        (
            row["avg_normalized_entropy_by_lift_mass"]
            for row in prime_rows
            if row["avg_normalized_entropy_by_lift_mass"] is not None
        ),
        default=None,
    )
    return {
        "audit_path": str(path),
        "audit_sha256": file_sha256(path),
        "q": audit["q"],
        "q_lift": audit["q_lift"],
        "fiber_size": audit["fiber_size"],
        "p_values": audit["p_values"],
        "layer_class": classify_layer(audit),
        "all_support_identities_hold": audit["all_support_identities_hold"],
        "all_monotone_lift_support": audit["all_monotone_lift_support"],
        "all_classified_resparse": audit["all_classified_resparse"],
        "min_density_drop_factor": min_drop,
        "max_slot_survival_rate": max_survival,
        "max_entropy": max_entropy,
        "prime_rows": prime_rows,
    }


def run(audit_paths: list[Path]) -> dict[str, Any]:
    """运行塔门控汇总。"""
    layers = [summarize_layer(path, load_json(path)) for path in audit_paths]
    layer_classes = [layer["layer_class"] for layer in layers]
    return {
        "certificate_type": "triad_a1_newlayer_tower_gate",
        "status": "newlayer_tower_gate_materialized_not_global_proof",
        "source_hashes": {
            "tower_gate_script": file_sha256(Path(__file__).resolve()),
            **{f"audit_{idx}": layer["audit_sha256"] for idx, layer in enumerate(layers, start=1)},
        },
        "layers": layers,
        "all_layers_have_valid_accounting": all(
            layer["all_support_identities_hold"] for layer in layers
        ),
        "all_layers_monotone": all(layer["all_monotone_lift_support"] for layer in layers),
        "all_layers_resparse": all(layer["all_classified_resparse"] for layer in layers),
        "layer_classes": layer_classes,
        "tower_gate_law": (
            "每次 Q->rQ 升层必须落入 FiberDeletion、ProjectionStitching、"
            "PDECEntropy 或 CleanKLS 之一。对同一 LHB allowed-set 的 M_Q 支撑，"
            "ProjectionStitching 已由投影单调性引理排除。该文件只汇总已物化层，不声称覆盖所有未来层。"
        ),
        "review_conclusion": (
        "已物化两层提升均为 FiberDeletionLayer：支撑恒等式成立、投影单调、"
        "且新层通过 fiber 删除重新稀疏。投影单调性已可由同一全周期完成集合 C_P 解释；"
        "这给出递归剥离路线的第二层证据；"
        "全局闭合仍需证明任意后继层的同一门控必然可验收。"
        ),
    }


def fmt_float(value: float | None) -> str:
    """格式化浮点数。"""
    if value is None:
        return "n/a"
    return f"{value:.6g}"


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 新层塔门控汇总",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 塔门控律",
        "",
        result["tower_gate_law"],
        "",
        "形式上，每层都检查：",
        "",
        "```text",
        "Q' = rQ",
        "|A_Q'| = sum_{t in A_Q}s(t) + |N|",
        "N=empty        => 可谈 fiber 删除或近均匀；",
        "N nonempty     => 一般 formal unit 下的 Projection/Stitching；",
        "LHB M_Q 同口径 => 投影单调性给出 N=empty；",
        "删除不足且偏斜 => PDECEntropy；",
        "删除不足且平坦 => CleanKLS/DLS。",
        "```",
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
            "## 3. 层摘要",
            "",
            "| layer | r | P values | class | monotone | resparse | min drop | max survival | max entropy |",
            "| --- | ---: | --- | --- | --- | --- | ---: | ---: | ---: |",
        ]
    )
    for layer in result["layers"]:
        lines.append(
            "| Q={q}->{ql} | {r} | `{pvals}` | `{cls}` | `{mono}` | `{resp}` | {drop} | {surv} | {ent} |".format(
                q=layer["q"],
                ql=layer["q_lift"],
                r=layer["fiber_size"],
                pvals=layer["p_values"],
                cls=layer["layer_class"],
                mono=layer["all_monotone_lift_support"],
                resp=layer["all_classified_resparse"],
                drop=fmt_float(layer["min_density_drop_factor"]),
                surv=fmt_float(layer["max_slot_survival_rate"]),
                ent=fmt_float(layer["max_entropy"]),
            )
        )

    lines.extend(["", "## 4. P 级明细", ""])
    for layer in result["layers"]:
        lines.extend(
            [
                f"### Q={layer['q']} -> {layer['q_lift']}",
                "",
                "| P | old support | lifted support | survival | deletion | drop | hist | class |",
                "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
            ]
        )
        for row in layer["prime_rows"]:
            lines.append(
                "| {p} | {old} | {new} | {surv} | {dele} | {drop} | `{hist}` | `{cls}` |".format(
                    p=row["p"],
                    old=row["old_support_count"],
                    new=row["lift_support_count"],
                    surv=fmt_float(row["slot_survival_rate"]),
                    dele=fmt_float(row["slot_deletion_rate"]),
                    drop=fmt_float(row["density_drop_factor"]),
                    hist=row["support_count_histogram"],
                    cls=row["classification"],
                )
            )
        lines.append("")

    lines.extend(
        [
            "## 5. 当前边界",
            "",
            "本汇总完成的是有限塔证据：`2310 -> 30030 -> 510510` 已按同一门控重复通过。",
            "它仍未证明所有未来素因子层都会通过；下一步需把 `N=empty` 或 `N` 的 Stitching 吸收写成",
            "针对任意新增素因子 `r` 的投影兼容判据。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audits", default=DEFAULT_AUDITS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(parse_paths(args.audits))
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "layer_classes": result["layer_classes"],
                "all_layers_resparse": result["all_layers_resparse"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
