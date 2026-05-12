#!/usr/bin/env python3
"""生成 strict 低有效模 endpoint PDEC/ColumnCRT 路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_low_effective_mod_endpoint_pdec_columncrt_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-low-effective-mod-endpoint-pdec-columncrt-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-fourier-upper-router.md",
    MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-deficit-fourier-pdec-router.md",
    MONOGRAPH / "prime-matrix-beta-sieve-self-contained-frontier-router.md",
    MONOGRAPH / "h4-pdec-admissible-constraint-table.md",
    MONOGRAPH / "h4-pdec-column-defect-weight-certificate.md",
]

LOW_EFFECTIVE = "LowEffectiveModEndpointPDECOrColumnCRT"
RECIP_ENV = "WeightedReciprocalCommonDivisorEnvelopeForLowEffectiveSpectrum"
HOT_DIVISOR = "HotFrequencyCommonDivisorSupportBudget"
LOW_QUOTIENT = "LowQuotientColumnCRTOrPDECRoute"
GEOM_DECAY = "EndpointArcGeometricDecayLargeEffectiveModBudget"


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


def laws() -> list[dict[str, str]]:
    """列出低有效模精确律。"""
    return [
        {
            "name": "invertible_phase_gcd",
            "formula": "gcd(hP^{-1} mod d,d)=gcd(h,d), because gcd(P,d)=1.",
            "status": "closed",
            "meaning": "低有效模完全由 h 与 d 的共同因子控制。",
        },
        {
            "name": "effective_denominator_factorization",
            "formula": "s=d/gcd(h,d); if s<=R, then d=s g with g|h.",
            "status": "closed",
            "meaning": "低有效模支撑落在少数 small-quotient times divisor-of-h 线上。",
        },
        {
            "name": "zero_mode_cancellation",
            "formula": "If s=1, then hP^{-1}=0 mod d and the centered endpoint coefficient is 0.",
            "status": "closed",
            "meaning": "最危险的 d|h 情况实际被中心化删除。",
        },
        {
            "name": "reciprocal_common_divisor_decay",
            "formula": "For s>=2, |hat phi_d(h)| <= s/(2d)=1/(2g), d=sg.",
            "status": "closed",
            "meaning": "低有效模不是免费大谱；每条共同因子线有 1/g 衰减。",
        },
        {
            "name": "low_effective_mass_bound",
            "formula": "LowEff_R(h)<=1/2 sum_{2<=s<=R} sum_{g|h, sg in D_+} w_{sg}^+/g.",
            "status": "closed_reduction",
            "meaning": "低有效模上界压成加权共同因子倒数和。",
        },
        {
            "name": "hot_divisor_or_columncrt",
            "formula": "If the reciprocal divisor envelope is too large, then some quotient s has abnormal mass on divisors of h; persistent cases are PDEC/ColumnCRT, isolated cases SAE.",
            "status": "registered_route",
            "meaning": "大低有效模不能作为无名误差保留。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链的正权端点 Fourier 上界内部。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "EffectiveGCDIdentityClosed",
            "closed": True,
            "proved": True,
            "meaning": "低有效分母等于 d/gcd(h,d)，与 P 的逆元选择无关。",
            "remaining": LOW_EFFECTIVE,
        },
        {
            "gate": "ZeroModeCancellationClosed",
            "closed": True,
            "proved": True,
            "meaning": "d|h 的零频贡献被中心化端点函数删除。",
            "remaining": "无。",
        },
        {
            "gate": "ReciprocalDivisorReductionClosed",
            "closed": True,
            "proved": True,
            "meaning": "低有效模贡献被压到 small quotient 线上的 1/g 加权倒数和。",
            "remaining": RECIP_ENV,
        },
        {
            "gate": "PDECColumnCRTRouteRegistered",
            "closed": True,
            "proved": False,
            "meaning": "倒数和若过大，必须表现为 hot common divisor 或低商模相位集中。",
            "remaining": f"{HOT_DIVISOR} OR {LOW_QUOTIENT}",
        },
        {
            "gate": "LowEffectiveModExcludedCurrentCorpus",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 reciprocal divisor envelope 小于 PDEC 下界，也未排斥 hot divisor/ColumnCRT 出口。",
            "remaining": f"{RECIP_ENV} AND {HOT_DIVISOR} AND {LOW_QUOTIENT}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_low_effective_mod_endpoint_pdec_columncrt_router",
        "status": "low_effective_mod_reduced_to_reciprocal_common_divisor_envelope_and_columncrt_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "effective_gcd_identity_closed": True,
        "zero_mode_cancellation_closed": True,
        "reciprocal_common_divisor_reduction_closed": True,
        "pdec_columncrt_route_registered": True,
        "low_effective_mod_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": RECIP_ENV,
        "parallel_targets": [HOT_DIVISOR, LOW_QUOTIENT, GEOM_DECAY],
        "laws": laws(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "低有效模共振已经被严格压成共同因子结构。因为 P 与所有筛模 d 互素，"
            "gcd(hP^{-1},d)=gcd(h,d)。若有效分母 s=d/gcd(h,d) 小，则 d=s g 且 g|h。"
            "其中 s=1 的零频已经被中心化端点函数完全删除；真正剩余的 s>=2 项有 "
            "1/g 的共同因子衰减。因此低有效模上界等价于加权共同因子倒数和。"
            "若该倒数和仍过大，就必须登记为 hot frequency common divisor 或低商模 ColumnCRT/PDEC。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 低有效模 endpoint PDEC/ColumnCRT 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"effective_gcd_identity_closed={fmt_bool(result['effective_gcd_identity_closed'])}",
        f"zero_mode_cancellation_closed={fmt_bool(result['zero_mode_cancellation_closed'])}",
        f"reciprocal_common_divisor_reduction_closed={fmt_bool(result['reciprocal_common_divisor_reduction_closed'])}",
        f"pdec_columncrt_route_registered={fmt_bool(result['pdec_columncrt_route_registered'])}",
        f"low_effective_mod_excluded={fmt_bool(result['low_effective_mod_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 共同因子压缩",
        "",
        "全局频率 `h` 在模 `d` 上看到的有效残基是 `hP^{-1} mod d`。因为 `P` 与 `d` 互素，",
        "",
        "```text",
        "gcd(hP^{-1},d)=gcd(h,d).",
        "```",
        "",
        "若有效分母 `s=d/gcd(h,d)<=R`，则",
        "",
        "```text",
        "d=s g,  g|h.",
        "```",
        "",
        "中心化端点函数删掉 `s=1` 的零频；对 `s>=2`，单模 Fourier 系数有",
        "",
        "```text",
        "|hat phi_d(h)| <= s/(2d)=1/(2g).",
        "```",
        "",
        "所以低有效模贡献不再是自由大谱，而是共同因子倒数和。",
        "",
        "## 2. 精确律",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["laws"]:
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
            "审稿边界：本步闭合低有效模的共同因子结构和零频删除；尚未证明共同因子倒数和足够小，也未排斥 hot divisor/ColumnCRT 出口。",
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
