#!/usr/bin/env python3
"""生成 strict 正权端点 Fourier 上界分裂路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_weighted_positive_endpoint_fourier_upper_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-weighted-positive-endpoint-fourier-upper-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-fourier-upper-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-fourier-upper-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-deficit-fourier-pdec-router.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-frequency-split-contract.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-bilinear-bohrcap-reduction.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-lowfreq-endpoint-return.md",
]

FOURIER_UPPER = "WeightedPositiveEndpointFourierPDECUpperBound"
LOW_EFFECTIVE = "LowEffectiveModEndpointPDECOrColumnCRT"
GEOMETRIC_DECAY = "EndpointArcGeometricDecayLargeEffectiveModBudget"
LARGE_SPECTRUM = "PositiveWeightSupportLargeSpectrumBohrCapExclusion"
SAE = "DeficitPersistenceOrSAEClassification"


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def reductions() -> list[dict[str, str]]:
    """列出 Fourier 上界分裂。"""
    return [
        {
            "name": "single_mod_endpoint_coefficient",
            "formula": "|hat phi_d(r)| <= min(H/d, 1/(2d||r/d||)) for r not 0 mod d.",
            "status": "closed_classical",
            "meaning": "端点弧的非零 Fourier 系数由几何级数精确控制。",
        },
        {
            "name": "lifted_frequency_support",
            "formula": "A global frequency h only sees d through r_h(d)=h P^{-1} mod d.",
            "status": "closed",
            "meaning": "大系数要求 h 与许多 d 同时低有效分母共振。",
        },
        {
            "name": "low_effective_mod_split",
            "formula": "If many active d have small d/gcd(r_h(d),d), then the frequency is a low-effective-mod PDEC/ColumnCRT.",
            "status": "closed_route",
            "meaning": "低有效模大谱不是随机误差，而是命名相位缺陷。",
        },
        {
            "name": "large_effective_mod_decay",
            "formula": "On d/gcd(r_h(d),d)>R, each active d contributes O(w_d^+/R) after endpoint centering.",
            "status": "closed_template",
            "meaning": "远离共振的频率可由几何衰减和权重 l1/l2 预算控制。",
        },
        {
            "name": "bohrcap_large_spectrum_route",
            "formula": "If high frequencies still exceed the decay budget, active d lie in a Bohr-cap large spectrum set.",
            "status": "registered_route",
            "meaning": "这接入既有 Bohr-cap/PDEC/ColumnCRT 分支。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的正权亏损 PDEC 内部。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "FourierCoefficientFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "端点弧 Fourier 系数由有限几何级数给出。",
            "remaining": FOURIER_UPPER,
        },
        {
            "gate": "LowEffectiveModRouteClosed",
            "closed": True,
            "proved": False,
            "meaning": "低有效模大谱已命名为 PDEC/ColumnCRT，但尚未排斥。",
            "remaining": LOW_EFFECTIVE,
        },
        {
            "gate": "LargeEffectiveModDecayTemplateClosed",
            "closed": True,
            "proved": False,
            "meaning": "非共振部分有几何衰减模板，但还需要正权支撑的 l1/l2/复杂度预算。",
            "remaining": GEOMETRIC_DECAY,
        },
        {
            "gate": "LargeSpectrumFallbackRegistered",
            "closed": True,
            "proved": False,
            "meaning": "若衰减预算失败，回流 Bohr-cap/PDEC/ColumnCRT。",
            "remaining": LARGE_SPECTRUM,
        },
        {
            "gate": "WeightedPositiveEndpointFourierUpperCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "三出口尚未全部排斥，也未给出统一数值预算。",
            "remaining": f"{LOW_EFFECTIVE} AND {GEOMETRIC_DECAY} AND {LARGE_SPECTRUM} AND {SAE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_weighted_positive_endpoint_fourier_upper_router",
        "status": "weighted_positive_endpoint_fourier_upper_split_to_low_effective_decay_bohrcap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "fourier_coefficient_formula_closed": True,
        "low_effective_mod_route_closed": True,
        "large_effective_mod_decay_template_closed": True,
        "bohrcap_large_spectrum_route_registered": True,
        "weighted_positive_endpoint_fourier_upper_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": LOW_EFFECTIVE,
        "parallel_targets": [GEOMETRIC_DECAY, LARGE_SPECTRUM, SAE],
        "reductions": reductions(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "正权端点 PDEC 的 Fourier 上界被压成三部分：低有效模共振、非共振几何衰减、"
            "以及衰减失败后的 Bohr-cap 大谱。端点弧单模 Fourier 系数由几何级数严格控制；"
            "若一个全局频率在许多 d 上同时低有效分母共振，则这本身就是 LowEffectiveMod "
            "PDEC/ColumnCRT。若没有低有效模共振，则需用几何衰减和正权支撑预算给出上界；"
            "预算失败则回流 Bohr-cap/PDEC/ColumnCRT。当前仍未排斥这些出口。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 正权端点 Fourier 上界分裂路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"fourier_coefficient_formula_closed={fmt_bool(result['fourier_coefficient_formula_closed'])}",
        f"low_effective_mod_route_closed={fmt_bool(result['low_effective_mod_route_closed'])}",
        f"large_effective_mod_decay_template_closed={fmt_bool(result['large_effective_mod_decay_template_closed'])}",
        f"bohrcap_large_spectrum_route_registered={fmt_bool(result['bohrcap_large_spectrum_route_registered'])}",
        f"weighted_positive_endpoint_fourier_upper_bound_proved={fmt_bool(result['weighted_positive_endpoint_fourier_upper_bound_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Fourier 上界三分",
        "",
        "单个模数 `d` 的端点弧函数有标准几何级数界。全局频率 `h` 对 `d` 的有效残基为",
        "",
        "```text",
        "r_h(d)=h P^{-1} mod d.",
        "```",
        "",
        "若 `r_h(d)` 在很多 `d` 上有小有效分母，就是低有效模 PDEC/ColumnCRT；否则端点弧系数按有效分母衰减。",
        "",
        "## 2. 分裂表",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["reductions"]:
        lines.append(
            "| `{name}` | {formula} | `{status}` | {meaning} |".format(
                name=table_cell(row["name"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 最新最窄输入",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步只把 Fourier 上界拆成可攻的三出口；没有证明三出口都被排斥。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
