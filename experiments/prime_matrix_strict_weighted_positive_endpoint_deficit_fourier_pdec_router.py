#!/usr/bin/env python3
"""生成 strict 正权端点命中亏损到 Fourier/PDEC 的路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_weighted_positive_endpoint_deficit_fourier_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-weighted-positive-endpoint-deficit-fourier-pdec-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-deficit-fourier-pdec-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-weighted-positive-endpoint-deficit-fourier-pdec-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-weighted-dyadic-endpoint-pdec-hdl-router.md",
    MONOGRAPH / "prime-matrix-eda-lowmod-pdec-certificate-route.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-roughsurplus-pdec-certificate.md",
    MONOGRAPH / "prime-matrix-eda-alpha-tail-squaremass-pdec-certificate.md",
]

POS_DEFICIT = "WeightedPositiveEndpointHitDeficitPDEC"
FOURIER_UPPER = "WeightedPositiveEndpointFourierPDECUpperBound"
PERSISTENCE = "DeficitPersistenceOrSAEClassification"
LOW_COMPLEXITY = "PositiveWeightSupportLowComplexityLedger"
NEG_SURPLUS = "WeightedNegativeEndpointHitSurplusCoreLoad"


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


def implications() -> list[dict[str, str]]:
    """列出正权亏损到 Fourier/PDEC 的闭合蕴含。"""
    return [
        {
            "name": "centered_positive_endpoint_test",
            "formula": "Phi_I^+(x)=sum_{d in I} w_d^+(1_{rho_d(x)<=H}-H/d).",
            "status": "closed_definition",
            "meaning": "正权端点命中亏损就是中心化端点测试函数取负大值。",
        },
        {
            "name": "zero_mean_on_full_crt_period",
            "formula": "Average_{x mod Q_I} Phi_I^+(x)=0, Q_I=lcm{d in supp_+(I)}.",
            "status": "closed",
            "meaning": "因为 xP mod d 是单位旋转，端点弧在完整 CRT 周期上的均值正好是 H/d。",
        },
        {
            "name": "deficit_to_fourier_energy",
            "formula": "If Phi_I^+(x0)<=-kappa, then sum_{h!=0}|hat Phi(h)|^2 >= kappa^2/(Q_I-1).",
            "status": "closed_implication",
            "meaning": "单个强亏损点也强制非零 Fourier 能量；持续出现时即 PDEC。",
        },
        {
            "name": "persistent_bad_set_h4_input",
            "formula": "For S={x:Phi_I^+(x)<=-kappa}, F=-Phi_I^+ gives F(x)>=kappa on S and mean(F)=0.",
            "status": "closed_template",
            "meaning": "这逐项匹配 H4/PDEC 的零均值测试函数输入。",
        },
        {
            "name": "isolated_deficit_route",
            "formula": "If the bad set is not persistent across the formal family, it is registered as SAE rather than a global PDEC.",
            "status": "registered_route",
            "meaning": "防止单窗异常被误当作全局 Fourier 定理。",
        },
    ]


def decision_rows() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍在早期零行反例链下处理正权端点亏损。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "CenteredFourierPDECObjectClosed",
            "closed": True,
            "proved": True,
            "meaning": "正权亏损已写成完整 CRT 周期上的零均值测试函数。",
            "remaining": POS_DEFICIT,
        },
        {
            "gate": "FourierEnergyLowerBoundClosed",
            "closed": True,
            "proved": True,
            "meaning": "亏损点给出非零 Fourier 能量下界；持续亏损给出 H4/PDEC 输入。",
            "remaining": FOURIER_UPPER,
        },
        {
            "gate": "PersistenceOrSAERouteClosed",
            "closed": True,
            "proved": False,
            "meaning": "持久出现走 PDEC；孤立出现走 SAE。是否可排斥两者尚未证明。",
            "remaining": PERSISTENCE,
        },
        {
            "gate": "PositiveEndpointDeficitExcludedCurrentCorpus",
            "closed": False,
            "proved": False,
            "meaning": "尚未提交匹配的 Fourier 上界，也未完成 SAE 排斥。",
            "remaining": f"{FOURIER_UPPER} AND {PERSISTENCE} AND {LOW_COMPLEXITY}",
        },
        {
            "gate": "RowColumnClosed",
            "closed": False,
            "proved": False,
            "meaning": "本步是标准 PDEC 输入化，不是 PDEC 排斥。",
            "remaining": f"{FOURIER_UPPER} OR SAE exclusion; parallel {NEG_SURPLUS}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    return {
        "certificate_type": "prime_matrix_strict_weighted_positive_endpoint_deficit_fourier_pdec_router",
        "status": "weighted_positive_endpoint_deficit_converted_to_centered_fourier_pdec_input_upper_bound_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "centered_fourier_pdec_object_closed": True,
        "fourier_energy_lower_bound_closed": True,
        "persistent_or_sae_route_defined": True,
        "weighted_positive_endpoint_deficit_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": FOURIER_UPPER,
        "parallel_targets": [PERSISTENCE, LOW_COMPLEXITY, NEG_SURPLUS],
        "implications": implications(),
        "decision_rows": decision_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "正权端点命中亏损已经可以严格写成一个完整 CRT 周期上的零均值测试函数 "
            "Phi_I^+。若某个早期零行反例点使 Phi_I^+<=-kappa，则非零 Fourier 能量至少为 "
            "kappa^2/(Q_I-1)；若这类亏损在 formal family 中持久出现，就形成标准 PDEC 输入，"
            "若只孤立出现则进入 SAE。当前尚未完成的是匹配的 Fourier 上界或 SAE 排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 正权端点亏损到 Fourier/PDEC 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"centered_fourier_pdec_object_closed={fmt_bool(result['centered_fourier_pdec_object_closed'])}",
        f"fourier_energy_lower_bound_closed={fmt_bool(result['fourier_energy_lower_bound_closed'])}",
        f"persistent_or_sae_route_defined={fmt_bool(result['persistent_or_sae_route_defined'])}",
        f"weighted_positive_endpoint_deficit_excluded={fmt_bool(result['weighted_positive_endpoint_deficit_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 中心化测试函数",
        "",
        "对正权支撑块定义",
        "",
        "```text",
        "Phi_I^+(x)=sum_{d in I} w_d^+ (1_{rho_d(x)<=H}-H/d).",
        "```",
        "",
        "其中 `Q_I=lcm{d in supp_+(I)}`。在完整 `x mod Q_I` 周期上，`Phi_I^+` 均值为零。",
        "",
        "若正权端点亏损达到 `kappa`，即",
        "",
        "```text",
        "Phi_I^+(x0)<=-kappa,",
        "```",
        "",
        "则 `Phi_I^+` 的非零 Fourier 能量不能为零；这是 PDEC 证书的标准入口。",
        "",
        "## 2. 闭合蕴含",
        "",
        "| name | formula | status | meaning |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["implications"]:
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
            "审稿边界：本步只把正权亏损转成标准 PDEC/SAE 输入；没有提交 Fourier 上界，也没有排斥 SAE。",
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
