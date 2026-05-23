#!/usr/bin/env python3
"""Prime Matrix 外部前沿 residual-gap 审计。

用法示例：
  python3 experiments/prime_matrix_external_frontier_residual_gap_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-external-frontier-residual-gap-audit.json

本脚本不尝试证明目标命题；它只把最新可用外部定理逐项换算成
Prime Matrix 行/列闭合所需的剩余指数缺口，防止把平均分布、条件结果、
P2 almost-prime 或宽短区间结果误写为逐行/逐列无条件闭合。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-external-frontier-residual-gap"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"
TARGET_THETA = 0.5
TARGET_LINNIK = 2.0

DEPENDENCIES = [
    DOCS / "prime-matrix-external-frontier-theorem-stress-router.json",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt(value: float) -> str:
    """稳定输出短小数。"""
    return f"{value:.12g}"


def md_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def short_interval_row(name: str, source: str, status: str, theta: float, note: str) -> dict[str, Any]:
    """把 x^theta 点态短区间输入换算成 P 行串缺口。"""
    return {
        "kind": "pointwise_short_interval",
        "name": name,
        "source": source,
        "status": status,
        "input_theta": theta,
        "target_theta": TARGET_THETA,
        "theta_gap": theta - TARGET_THETA,
        "row_window_exponent_in_P": 2 * theta,
        "empty_row_run_residual_exponent": max(0.0, 2 * theta - 1),
        "closes_row": theta <= TARGET_THETA,
        "residual_gate": "PointwiseShortIntervalPrimeTheoremThetaLeHalf",
        "note": note,
    }


def linnik_row(name: str, source: str, status: str, exponent: float, note: str) -> dict[str, Any]:
    """把 Linnik/AP 首素数指数换算成列方向 P^2 方阵缺口。"""
    return {
        "kind": "least_prime_ap_linnik",
        "name": name,
        "source": source,
        "status": status,
        "linnik_exponent": exponent,
        "target_exponent": TARGET_LINNIK,
        "exponent_gap": exponent - TARGET_LINNIK,
        "height_overshoot_over_P2": f"P^{fmt(exponent - TARGET_LINNIK)}",
        "closes_column": exponent <= TARGET_LINNIK and "conditional" not in status,
        "residual_gate": "LinnikExponentLeTwoWithSquareWindowConstants",
        "note": note,
    }


def conditional_linnik_row(name: str, source: str, note: str) -> dict[str, Any]:
    """记录 q^(2+eps) 条件近门槛而不伪装成无条件 P^2 内闭合。"""
    return {
        "kind": "conditional_linnik_near_square",
        "name": name,
        "source": source,
        "status": "conditional_arxiv",
        "linnik_exponent": "2+epsilon",
        "target_exponent": TARGET_LINNIK,
        "symbolic_gap": "epsilon plus conditional GLH hypothesis",
        "height_overshoot_over_P2": "P^epsilon",
        "closes_column": False,
        "residual_gate": "ConditionalLinnikTwoPlusEpsilonToUnconditionalLinnikLeTwoWithConstants",
        "note": note,
    }


def almost_prime_row(name: str, source: str, exponent: float, note: str) -> dict[str, Any]:
    """记录 P2 almost-prime 已进方阵但仍卡奇偶对象。"""
    return {
        "kind": "almost_prime_ap_wrong_object",
        "name": name,
        "source": source,
        "status": "arxiv_wrong_parity_object",
        "almost_prime_exponent": exponent,
        "square_margin": TARGET_LINNIK - exponent,
        "enters_P2_square": exponent < TARGET_LINNIK,
        "closes_column": False,
        "residual_gate": "NonlinearParityBreakingActualSourceConstructor",
        "note": note,
    }


def average_ap_row(name: str, source: str, status: str, exponent: float, structure: str, note: str) -> dict[str, Any]:
    """把平均 AP 分布指数换算成 x=P^2 时的模数范围，并保留 fixed-modulus 缺口。"""
    modulus_exponent = 2 * exponent
    return {
        "kind": "average_ap_distribution",
        "name": name,
        "source": source,
        "status": status,
        "distribution_exponent_in_x": exponent,
        "modulus_range_exponent_in_P": modulus_exponent,
        "prime_modulus_P_inside_range": modulus_exponent >= 1,
        "structure": structure,
        "closes_column": False,
        "residual_gate": "MeanValueAPToFixedPrimeModulusZeroExceptionTransfer",
        "note": note,
    }


def grid_transfer_row(name: str, source: str, note: str) -> dict[str, Any]:
    """记录 almost-all/exceptional-set 输入到刚性 P 行格点之间的转移缺口。"""
    return {
        "kind": "exceptional_set_to_grid_transfer",
        "name": name,
        "source": source,
        "status": "arxiv_exceptional_set_interface",
        "almost_all_available": True,
        "rigid_P_grid_pointwise_control": False,
        "closes_row": False,
        "residual_gate": "GridTransferredShortIntervalSecondMomentAtThetaHalf",
        "note": note,
    }


def source_hashes() -> dict[str, str]:
    """登记本脚本和直接依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_payload() -> dict[str, Any]:
    """构造 residual-gap 账本。"""
    rows = [
        short_interval_row(
            "Baker-Harman-Pintz 2001",
            "https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/difference-between-consecutive-primes-ii/2EF13261B3B25458A25F41ED74AA2FC2",
            "published",
            0.525,
            "给出已发表点态短区间 side theorem；行串残余指数为 0.05。",
        ),
        short_interval_row(
            "Runbo Li short intervals",
            "https://arxiv.org/abs/2308.04458",
            "arXiv:2308.04458v8",
            0.52,
            "若接受，可把行串残余指数压到 0.04；仍大于 theta=1/2 门槛。",
        ),
        short_interval_row(
            "Guth-Maynard zero-density consequence",
            "https://arxiv.org/abs/2405.20552",
            "arXiv:2405.20552v2",
            17 / 30,
            "17/30 技术很强，但换算成行厚度仍是 P^(2/15+o(1))。",
        ),
        short_interval_row(
            "Le Duc Hieu prime APs in short intervals",
            "https://arxiv.org/abs/2509.04883",
            "arXiv:2509.04883v2",
            17 / 30,
            "短区间内素数等差数列结构更强，但长度门槛仍未到单行 P。",
        ),
        grid_transfer_row(
            "Gafni-Tao exceptional short intervals",
            "https://arxiv.org/abs/2505.24017",
            "almost-all/exceptional-set 信息不能自动控制所有 P-间隔行端点。",
        ),
        linnik_row(
            "Xylouris general Linnik published scale",
            "https://arxiv.org/abs/0906.2749",
            "published",
            5.0,
            "按当前账本记录为 <5 量级；距 P^2 方阵仍差约 P^3。",
        ),
        linnik_row(
            "Meng bounded-cubic-part AP prime",
            "https://xbna.pku.edu.cn/EN/Y2001/V37/I1/20",
            "published_special_prime_modulus_compatible",
            4.5,
            "素模数兼容，但首素数高度仍为 P^4.5，距 P^2 差 P^2.5。",
        ),
        conditional_linnik_row(
            "Bruna conditional GLH least AP prime",
            "https://arxiv.org/abs/2603.25612",
            "GLH 下到 q^(2+epsilon)，是条件近门槛，不是无条件 strict P^2 方阵内闭合。",
        ),
        almost_prime_row(
            "Li-Zhang-Cai least P2 almost-prime in AP",
            "https://arxiv.org/abs/2103.13360",
            1.8345,
            "指数进入 P^2，但对象是 P2 almost-prime；这正定位奇偶屏障。",
        ),
        average_ap_row(
            "Stadlmann smooth-moduli prime AP distribution",
            "https://arxiv.org/abs/2309.00425",
            "accepted_average_smooth_moduli",
            0.5 + 1 / 40,
            "smooth moduli average",
            "模数范围覆盖 P，但平均/光滑模数结构不能推出固定素模数 P 的零例外全 residue。",
        ),
        average_ap_row(
            "Runbo Li smooth-moduli minorant",
            "https://arxiv.org/abs/2505.09629",
            "arXiv:2505.09629v3",
            10 / 19,
            "smooth minorant average",
            "minorant 越过 1/2 后仍是平均光滑模数输入，不是逐列点态正性。",
        ),
        average_ap_row(
            "Pascadi weighted prime/smooth distribution",
            "https://arxiv.org/abs/2505.00653",
            "arXiv:2505.00653v2",
            5 / 8,
            "weighted/well-factorable mean value",
            "模数范围到 P^(5/4-o(1))，但 weighted mean value 不给固定 P 零例外。",
        ),
        average_ap_row(
            "Runbo Li large-moduli AP bilinear",
            "https://arxiv.org/abs/2602.20917",
            "arXiv:2602.20917v5",
            9 / 17,
            "bilinear moduli average",
            "q=P 在范围内，但结果仍是结构化平均而非固定素模数全 residue。",
        ),
        average_ap_row(
            "Runbo Li large-moduli AP trilinear",
            "https://arxiv.org/abs/2602.20917",
            "arXiv:2602.20917v5",
            17 / 32,
            "trilinear moduli average",
            "q=P 在范围内，但 almost-all/结构化平均不能专化成每列有素数。",
        ),
    ]

    pointwise = [r for r in rows if r["kind"] == "pointwise_short_interval"]
    linnik = [r for r in rows if r["kind"] == "least_prime_ap_linnik"]
    average = [r for r in rows if r["kind"] == "average_ap_distribution"]
    p2 = next(r for r in rows if r["kind"] == "almost_prime_ap_wrong_object")
    conditional = next(r for r in rows if r["kind"] == "conditional_linnik_near_square")

    best_published_pointwise = min(
        (r for r in pointwise if r["status"] == "published"),
        key=lambda r: r["empty_row_run_residual_exponent"],
    )
    best_preprint_pointwise = min(pointwise, key=lambda r: r["empty_row_run_residual_exponent"])
    best_linnik = min(linnik, key=lambda r: r["exponent_gap"])
    best_average = max(average, key=lambda r: r["modulus_range_exponent_in_P"])

    return {
        "certificate_type": "prime_matrix_external_frontier_residual_gap_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "residual_gaps_quantified_target_open",
        "target_row_theta": TARGET_THETA,
        "target_column_linnik_exponent": TARGET_LINNIK,
        "best_published_pointwise_row_residual": {
            "name": best_published_pointwise["name"],
            "empty_row_run_residual_exponent": best_published_pointwise["empty_row_run_residual_exponent"],
        },
        "best_preprint_pointwise_row_residual": {
            "name": best_preprint_pointwise["name"],
            "empty_row_run_residual_exponent": best_preprint_pointwise["empty_row_run_residual_exponent"],
        },
        "best_published_prime_modulus_linnik_gap": {
            "name": best_linnik["name"],
            "exponent_gap": best_linnik["exponent_gap"],
        },
        "best_conditional_linnik_gap": conditional["symbolic_gap"],
        "best_wrong_object_square_margin": {
            "name": p2["name"],
            "square_margin": p2["square_margin"],
            "wrong_object": "P2 almost-prime, not prime",
        },
        "strongest_average_ap_modulus_range": {
            "name": best_average["name"],
            "modulus_range_exponent_in_P": best_average["modulus_range_exponent_in_P"],
            "residual_gate": "MeanValueAPToFixedPrimeModulusZeroExceptionTransfer",
        },
        "latest_true_residual_basis": [
            "PointwiseShortIntervalPrimeTheoremThetaLeHalf",
            "GridTransferredShortIntervalSecondMomentAtThetaHalf",
            "LinnikExponentLeTwoWithSquareWindowConstants",
            "MeanValueAPToFixedPrimeModulusZeroExceptionTransfer",
            "ConditionalLinnikTwoPlusEpsilonToUnconditionalLinnikLeTwoWithConstants",
            "NonlinearParityBreakingActualSourceConstructor",
        ],
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """生成简明 Markdown 表格。"""
    lines = [
        "| kind | name | status | residual gate | transformed residual | closes? | note |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in rows:
        if item["kind"] == "pointwise_short_interval":
            residual = f"theta_gap={fmt(item['theta_gap'])}; run_exp={fmt(item['empty_row_run_residual_exponent'])}"
            closes = item["closes_row"]
        elif item["kind"] == "least_prime_ap_linnik":
            residual = f"L_gap={fmt(item['exponent_gap'])}; overshoot={item['height_overshoot_over_P2']}"
            closes = item["closes_column"]
        elif item["kind"] == "conditional_linnik_near_square":
            residual = item["symbolic_gap"]
            closes = item["closes_column"]
        elif item["kind"] == "almost_prime_ap_wrong_object":
            residual = f"square_margin={fmt(item['square_margin'])}; wrong_object=P2"
            closes = item["closes_column"]
        elif item["kind"] == "average_ap_distribution":
            residual = f"modulus_range=P^{fmt(item['modulus_range_exponent_in_P'])}; fixed_modulus_transfer=open"
            closes = item["closes_column"]
        else:
            residual = "grid_transfer=open"
            closes = item["closes_row"]
        lines.append(
            "| {kind} | {name} | `{status}` | `{gate}` | {residual} | `{closes}` | {note} |".format(
                kind=md_cell(item["kind"]),
                name=md_cell(item["name"]),
                status=md_cell(item["status"]),
                gate=md_cell(item["residual_gate"]),
                residual=md_cell(residual),
                closes=str(closes).lower(),
                note=md_cell(item["note"]),
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成审计文档。"""
    lines = [
        "# Prime Matrix 外部前沿 residual-gap 审计",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "- 已发表点态短区间最强可用副产品：Baker--Harman--Pintz 给连续空行串残余指数 `0.05`。",
        "- 前沿预印本近似副产品：Runbo Li v8 若接受可把残余指数压到 `0.04`，仍未到 `theta<=1/2`。",
        "- 列方向最接近方阵的条件输入：Bruna 在 GLH 下给 `q^(2+epsilon)`，仍是条件且超出 strict `P^2`。",
        "- AP 平均分布已经多次越过 `x^1/2`，但共同缺口是固定素模数 `q=P` 的零例外全剩余类转移。",
        "- P2 almost-prime 已进入 `P^2` 方阵，但对象不是素数；这把奇偶屏障定位为真实剩余硬点。",
        "",
        "## 2. 最小剩余基",
        "",
        "```text",
        *payload["latest_true_residual_basis"],
        "```",
        "",
        "## 3. 残余缺口表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 4. 审稿边界",
        "",
        "本审计是非循环推进：它把每个外部输入换算成目标窗口中的剩余指数缺口或对象缺口。"
        "它不声称外部引理版或内部自足版已经无条件闭合。",
        "",
        "```text",
        f"external_lemma_version_unconditional_closed={str(payload['external_lemma_version_unconditional_closed']).lower()}",
        f"internal_self_contained_closed={str(payload['internal_self_contained_closed']).lower()}",
        f"row_column_unconditional_closed={str(payload['row_column_unconditional_closed']).lower()}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
