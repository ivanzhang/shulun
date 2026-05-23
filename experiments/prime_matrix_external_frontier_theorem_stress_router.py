#!/usr/bin/env python3
"""生成 Prime Matrix 外部前沿定理压力测试证书。

用法示例：
  python3 experiments/prime_matrix_external_frontier_theorem_stress_router.py
  python3 -m json.tool docs/monograph/prime-matrix-external-frontier-theorem-stress-router.json

输出：
  data/prime-matrix-external-frontier-theorem-stress-ledger.json
  docs/monograph/prime-matrix-external-frontier-theorem-stress-router.json
  docs/monograph/prime-matrix-external-frontier-theorem-stress-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SLUG = "prime-matrix-external-frontier-theorem-stress"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

HONEST_STATUS = DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md"
CLAIM_STATUS = DOCS / "claim-status-table.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
SEED_TERMINAL = DOCS / "prime-matrix-two-replacement-lines-seed-moving-atom-global-terminal-sync-router.json"

TARGET_SHORT_INTERVAL_THETA = 0.5
TARGET_LINNIK_EXPONENT = 2.0


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def dependency_paths() -> list[Path]:
    """列出直接依赖文件。"""
    return [HONEST_STATUS, CLAIM_STATUS, EXTERNAL_INDEX, SEED_TERMINAL, PAPER]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def row(
    theorem: str,
    source: str,
    status: str,
    payload: str,
    transformed_payload: str,
    helps: str,
    closes_target: bool,
    obstruction: str,
) -> dict[str, Any]:
    """构造外部定理压力测试行。"""
    return {
        "theorem": theorem,
        "source": source,
        "status": status,
        "payload": payload,
        "transformed_payload": transformed_payload,
        "helps": helps,
        "closes_target": closes_target,
        "obstruction": obstruction,
    }


def short_interval_gap(theta: float) -> dict[str, Any]:
    """把 x^theta 短区间转成 P^alpha 行尺度。"""
    return {
        "theta": theta,
        "target_theta": TARGET_SHORT_INTERVAL_THETA,
        "theta_gap": theta - TARGET_SHORT_INTERVAL_THETA,
        "row_length_exponent_in_P": 2 * theta,
        "empty_row_run_exponent_bound": max(0.0, 2 * theta - 1),
    }


def linnik_gap(exponent: float) -> dict[str, Any]:
    """计算 Linnik 指数缺口。"""
    return {
        "linnik_exponent": exponent,
        "target_exponent": TARGET_LINNIK_EXPONENT,
        "exponent_gap": exponent - TARGET_LINNIK_EXPONENT,
        "column_height_exponent_in_rows": exponent - 1,
    }


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    bhp = short_interval_gap(0.525)
    li052 = short_interval_gap(0.52)
    guth_maynard = short_interval_gap(17 / 30)
    xylouris52 = linnik_gap(5.2)
    xylouris5 = linnik_gap(5.0)
    meng45 = linnik_gap(4.5)

    rows = [
        row(
            "Baker-Harman-Pintz 2001 prime gaps",
            "https://doi.org/10.1112/plms/83.3.532",
            "published_external",
            "Every large interval of length x^0.525 contains a prime.",
            "For x~P^2 this forbids prime-free row runs longer than P^0.05 up to constants.",
            "Closes a genuine side theorem: no asymptotically long consecutive empty-row block of exponent >0.05.",
            False,
            "Target row theorem needs theta<=1/2, i.e. empty-run exponent <0.",
        ),
        row(
            "Runbo Li 2025 Harman-sieve computation",
            "https://arxiv.org/abs/2308.04458",
            "frontier_preprint_external",
            "Claims every large interval of length x^0.52 contains a prime.",
            "If accepted, this improves the empty-row run exponent bound from 0.05 to 0.04.",
            "Best known-looking pointwise short-interval candidate located in this audit.",
            False,
            "Still has theta=0.52>1/2 and is preprint status; it does not give one prime in each P-long row.",
        ),
        row(
            "Guth-Maynard 2024/2026 zero-density consequence",
            "https://arxiv.org/abs/2405.20552",
            "arxiv_external",
            "Uniform short-interval PNT at exponents theta>17/30.",
            "For x~P^2 this gives row windows of size P^(17/15+o(1)), weaker than BHP/Li for pointwise row closure.",
            "Important for zero-density and exceptional-set technology, but not the pointwise row gate.",
            False,
            "17/30>1/2; pointwise length is still too long.",
        ),
        row(
            "Gafni-Tao 2025 exceptional short intervals",
            "https://arxiv.org/abs/2505.24017",
            "arxiv_external",
            "Relates zero-density estimates to exceptional sets; records all-x theta>17/30 and almost-all theta>2/15 context.",
            "Almost-all x control does not imply control on the rigid lattice endpoints kP or P^2-row blocks.",
            "Useful for density-style side bounds and for checking that row-grid control is the missing interface.",
            False,
            "Needs lattice/grid transfer from continuous exceptional measure to every P-spaced row endpoint.",
        ),
        row(
            "Xylouris 2011 Linnik exponent 5.2",
            "https://arxiv.org/abs/0906.2749",
            "published_external",
            "Least prime in a reduced residue class mod q is O(q^5.2).",
            "For q=P this gives a column prime by height P^5.2, far beyond the P^2 square.",
            "Confirms the AP route is real but much too weak for P x P column closure.",
            False,
            "Column theorem needs Linnik exponent <=2 with compatible constants/window.",
        ),
        row(
            "Xylouris 2018 Linnik exponent <5",
            "https://www.mathnet.ru/eng/cheb681",
            "published_external_nonenglish",
            "Improves the general Linnik exponent below 5.",
            "For q=P this is still height P^(5-o(1)), not P^2.",
            "Best general published direction found for least prime AP, still not target-compatible.",
            False,
            "Exponent gap remains nearly 3.",
        ),
        row(
            "Meng 2001 bounded-cubic-part AP exponent 4.5",
            "https://xbna.pku.edu.cn/EN/Y2001/V37/I1/20",
            "published_external_special_moduli",
            "For moduli with bounded cubic part, least AP prime is O(q^4.5).",
            "Prime modulus P is structurally compatible with bounded cubic part, but P^4.5 is still outside the P^2 square.",
            "Stronger special-modulus AP side theorem; gives no column closure.",
            False,
            "Exponent gap 2.5 above the needed L<=2 threshold.",
        ),
        row(
            "Li-Zhang-Cai 2021 least P2 almost-prime in AP",
            "https://arxiv.org/abs/2103.13360",
            "arxiv_external_wrong_object",
            "Least at-most-two-prime-factor number in a reduced residue class is O(q^1.8345).",
            "For q=P this enters the P^2 square, but it is an almost-prime, not a prime.",
            "Sharp parity-barrier diagnostic: the AP sieve reaches the square for P2, not for primes.",
            False,
            "Wrong parity object; cannot replace column prime existence.",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_external_frontier_theorem_stress_router",
        "status": "external_frontier_theorems_imported_side_bounds_closed_main_target_open",
        "target_short_interval_theta": TARGET_SHORT_INTERVAL_THETA,
        "target_linnik_exponent": TARGET_LINNIK_EXPONENT,
        "best_published_pointwise_short_interval_theta": bhp["theta"],
        "best_frontier_preprint_pointwise_short_interval_theta": li052["theta"],
        "best_published_empty_row_run_exponent_bound": bhp["empty_row_run_exponent_bound"],
        "best_frontier_preprint_empty_row_run_exponent_bound": li052["empty_row_run_exponent_bound"],
        "best_general_linnik_exponent_recorded": xylouris5["linnik_exponent"],
        "best_special_prime_modulus_compatible_linnik_exponent_recorded": meng45["linnik_exponent"],
        "least_almost_prime_ap_exponent_inside_square": 1.8345,
        "published_external_side_bounds": [
            "BHPNoLongEmptyRowRunExponent005",
            "XylourisLinnikColumnPrimeByHeightP5Plus",
            "MengPrimeModulusColumnPrimeByHeightP45",
        ],
        "arxiv_or_preprint_side_diagnostics": [
            "LeastP2AlmostPrimeInEachColumnInsideP2Square",
            "Li052NoLongEmptyRowRunExponent004_if_accepted",
        ],
        "new_required_external_or_internal_breakthrough": (
            "PointwiseShortIntervalPrimeTheoremThetaLeHalf OR "
            "LinnikExponentLeTwoWithSquareWindowConstants OR "
            "GridTransferredShortIntervalSecondMomentAtThetaHalf OR "
            "NonlinearParityBreakingActualSourceConstructor"
        ),
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "short_interval_transforms": {
            "BHP2001": bhp,
            "Li2025_preprint": li052,
            "GuthMaynard2026": guth_maynard,
        },
        "linnik_transforms": {
            "Xylouris2011": xylouris52,
            "Xylouris2018": xylouris5,
            "Meng2001_bounded_cubic_part": meng45,
        },
        "plain_conclusion": (
            "外部前沿定理已经能给出真实副产品：Baker-Harman-Pintz 2001 禁止长度约 "
            "P^0.05 以上的连续空行串；若 Runbo Li 2025 预印本被接受，可把指数改进到 "
            "P^0.04。Xylouris/Meng 的 Linnik 型结果保证列方向最终出现素数，但高度仍为 "
            "P^5 或 P^4.5 量级，不能进入 P^2 方阵；Li-Zhang-Cai 的 P2 almost-prime "
            "结果进入 P^2，却正好是错误奇偶对象。故所有有帮助的外部定理都已定位为 side "
            "bounds/parity diagnostics；目标命题仍需要 theta<=1/2 的点态短区间定理、"
            "Linnik<=2 的同窗口常数版本、theta=1/2 二阶矩到行格点的转移，或真正非线性破奇偶构造。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 Markdown 表格。"""
    lines = [
        "| theorem | status | payload | transformed payload | helps | closes target | obstruction |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {theorem} | `{status}` | {payload} | {transformed} | {helps} | `{closes}` | {obstruction} |".format(
                theorem=cell(item["theorem"]),
                status=cell(item["status"]),
                payload=cell(item["payload"]),
                transformed=cell(item["transformed_payload"]),
                helps=cell(item["helps"]),
                closes=fmt_bool(item["closes_target"]),
                obstruction=cell(item["obstruction"]),
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    lines = [
        "# Prime Matrix 外部前沿定理压力测试证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"target_short_interval_theta={payload['target_short_interval_theta']}",
        f"best_published_pointwise_short_interval_theta={payload['best_published_pointwise_short_interval_theta']}",
        f"best_frontier_preprint_pointwise_short_interval_theta={payload['best_frontier_preprint_pointwise_short_interval_theta']}",
        f"best_published_empty_row_run_exponent_bound={payload['best_published_empty_row_run_exponent_bound']}",
        f"best_frontier_preprint_empty_row_run_exponent_bound={payload['best_frontier_preprint_empty_row_run_exponent_bound']}",
        f"target_linnik_exponent={payload['target_linnik_exponent']}",
        f"best_general_linnik_exponent_recorded={payload['best_general_linnik_exponent_recorded']}",
        f"best_special_prime_modulus_compatible_linnik_exponent_recorded={payload['best_special_prime_modulus_compatible_linnik_exponent_recorded']}",
        f"least_almost_prime_ap_exponent_inside_square={payload['least_almost_prime_ap_exponent_inside_square']}",
        f"external_lemma_version_unconditional_closed={fmt_bool(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={fmt_bool(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(payload['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 外部定理压力表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 真实副产品",
        "",
        "已由已发表外部定理登记的副产品：",
        "",
        "```text",
        *payload["published_external_side_bounds"],
        "```",
        "",
        "预印本/错误奇偶对象诊断：",
        "",
        "```text",
        *payload["arxiv_or_preprint_side_diagnostics"],
        "```",
        "",
        "## 4. 仍需的新突破",
        "",
        "```text",
        payload["new_required_external_or_internal_breakthrough"],
        "```",
        "",
        "## 5. 来源链接",
        "",
        "| theorem | source |",
        "| --- | --- |",
    ]
    for item in payload["rows"]:
        lines.append(f"| {cell(item['theorem'])} | <{item['source']}> |")
    lines.extend(
        [
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
