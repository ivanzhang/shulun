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
FRONTIER_VERIFIED_DATE = "2026-05-23"


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


def ap_distribution_gap(theta: float) -> dict[str, Any]:
    """把 AP 平均分布指数换成 x=P^2 时的模数尺度。"""
    return {
        "distribution_exponent_in_x": theta,
        "modulus_range_exponent_in_P": 2 * theta,
        "square_root_barrier_excess_in_x": theta - 0.5,
        "fixed_prime_modulus_P_is_inside_range": theta >= 0.5,
    }


def version_row(name: str, source: str, version: str, date: str, audited_payload: str) -> dict[str, str]:
    """记录本轮核验到的外部源版本。"""
    return {
        "name": name,
        "source": source,
        "version": version,
        "date": date,
        "audited_payload": audited_payload,
    }


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    bhp = short_interval_gap(0.525)
    li052 = short_interval_gap(0.52)
    guth_maynard = short_interval_gap(17 / 30)
    hieu_ap = short_interval_gap(17 / 30)
    xylouris52 = linnik_gap(5.2)
    xylouris5 = linnik_gap(5.0)
    meng45 = linnik_gap(4.5)
    stadlmann_smooth = ap_distribution_gap(0.5 + 1 / 40)
    li_smooth_minorant = ap_distribution_gap(10 / 19)
    pascadi_weighted = ap_distribution_gap(5 / 8)
    li_large_bilinear = ap_distribution_gap(9 / 17)
    li_large_trilinear = ap_distribution_gap(17 / 32)
    bruna_glh = linnik_gap(2.0)

    source_versions = [
        version_row(
            "Baker-Harman-Pintz 2001",
            "https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/difference-between-consecutive-primes-ii/2EF13261B3B25458A25F41ED74AA2FC2",
            "published",
            "2001-10-22 online / 2001-11 issue",
            "Published pointwise prime in [x, x+x^0.525] for large x.",
        ),
        version_row(
            "Runbo Li short intervals",
            "https://arxiv.org/abs/2308.04458",
            "arXiv:2308.04458v8",
            "2025-10-16",
            "Preprint claims primes in [x-x^0.52, x] for all sufficiently large x.",
        ),
        version_row(
            "Guth-Maynard large values",
            "https://arxiv.org/abs/2405.20552",
            "arXiv:2405.20552v2",
            "2026-04-07",
            "Zero-density estimate and short-interval prime asymptotics at length x^(17/30+o(1)).",
        ),
        version_row(
            "Gafni-Tao exceptional intervals",
            "https://arxiv.org/abs/2505.24017",
            "arXiv:2505.24017v1",
            "2025-05-29",
            "Exceptional-set interface: all x for theta>17/30 and almost all x for theta>2/15 are not row-grid pointwise closure.",
        ),
        version_row(
            "Le Duc Hieu short-interval prime APs",
            "https://arxiv.org/abs/2509.04883",
            "arXiv:2509.04883v2",
            "2025-09-24",
            "Many k-term prime APs in every interval [x,x+x^theta] for theta>17/30; structurally stronger but length gate unchanged.",
        ),
        version_row(
            "Li-Zhang-Cai least P2 almost-prime in AP",
            "https://arxiv.org/abs/2103.13360",
            "arXiv:2103.13360v2",
            "2021-07-19",
            "P2(a,q) << q^1.8345, inside P^2 after q=P but wrong parity object.",
        ),
        version_row(
            "Stadlmann smooth-moduli prime AP distribution",
            "https://arxiv.org/abs/2309.00425",
            "arXiv:2309.00425v3 / accepted Adv. Math.",
            "2025-02-22",
            "Average prime equidistribution to smooth moduli up to x^(1/2+1/40-epsilon); smooth-modulus average, not fixed prime modulus P.",
        ),
        version_row(
            "Runbo Li smooth-moduli minorant",
            "https://arxiv.org/abs/2505.09629",
            "arXiv:2505.09629v3",
            "2025-12-29",
            "Minorant for prime indicator with level 10/19 in APs to smooth moduli; still not a fixed prime-modulus all-residue theorem.",
        ),
        version_row(
            "Pascadi weighted prime/smooth distribution",
            "https://arxiv.org/abs/2505.00653",
            "arXiv:2505.00653v2",
            "2025-06-29",
            "Weighted/well-factorable prime distribution to moduli up to x^(5/8-o(1)); mean-value weighted input, not column closure.",
        ),
        version_row(
            "Runbo Li large-moduli Harman-sieve APs",
            "https://arxiv.org/abs/2602.20917",
            "arXiv:2602.20917v5",
            "2026-05-05",
            "Mean-value theorems for primes to bilinear moduli up to x^(9/17) and trilinear moduli up to x^(17/32); almost-all q, not fixed q=P all residues.",
        ),
        version_row(
            "Bruna conditional least AP prime",
            "https://arxiv.org/abs/2603.25612",
            "arXiv:2603.25612v1",
            "2026-03-26",
            "Assuming generalized Lindelof for Dirichlet L-functions, p(a mod q) <<_epsilon q^(2+epsilon); conditional and still outside a fixed q^2 square.",
        ),
        version_row(
            "Xylouris Linnik constant",
            "https://arxiv.org/abs/0906.2749",
            "Acta Arith. 150 (2011)",
            "2011",
            "Least AP prime exponent L=5.2; later <5 records remain far above the needed L<=2 gate.",
        ),
    ]

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
            "Le Duc Hieu 2025 prime APs in short intervals",
            "https://arxiv.org/abs/2509.04883",
            "arxiv_external_structural_stress",
            "For theta>17/30, every sufficiently long interval [x,x+x^theta] contains many k-term APs of primes.",
            "At x~P^2 the interval length remains P^(17/15+o(1)); it certifies rich prime structure only after thickening each row by P^(2/15+o(1)) rows.",
            "Rules out the hope that adding Green-Tao/transference structure at the 17/30 scale alone closes the P-row theorem.",
            False,
            "The row window is still wider than one P-row; structural abundance does not imply a prime in each individual row.",
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
        row(
            "Stadlmann 2025 smooth-moduli AP distribution",
            "https://arxiv.org/abs/2309.00425",
            "accepted_external_average_smooth_moduli",
            "Primes are equidistributed on average to smooth moduli up to x^(1/2+1/40-epsilon).",
            "At x=P^2 this reaches moduli up to P^(1.05-o(1)), but the prime modulus P is not a smooth-modulus average input.",
            "Confirms that distribution beyond the square-root barrier is available only with averaging/smoothness structure.",
            False,
            "Column closure needs the fixed prime modulus q=P and every reduced residue class, not an average over smooth q.",
        ),
        row(
            "Runbo Li 2025 smooth-moduli minorant",
            "https://arxiv.org/abs/2505.09629",
            "arxiv_external_minorant_average",
            "Constructs a prime-indicator minorant with distribution level 10/19 for APs to smooth moduli.",
            "At x=P^2 the modulus range is P^(20/19), again an averaged smooth-modulus input rather than fixed q=P.",
            "Useful as a lower-bound sieve diagnostic: genuine minorants exist past 1/2 only after smooth-modulus averaging.",
            False,
            "The minorant does not certify a prime in each residue class for the single prime modulus P.",
        ),
        row(
            "Pascadi 2025 weighted distribution exponent 5/8",
            "https://arxiv.org/abs/2505.00653",
            "arxiv_external_weighted_mean_value",
            "Primes and smooth numbers are equidistributed in APs to moduli up to x^(5/8-o(1)) with triply-well-factorable weights.",
            "At x=P^2 this reaches P^(5/4-o(1)) in modulus range, far beyond P, but only in weighted mean-value form.",
            "Marks the strongest recorded distribution-exponent technology in this audit.",
            False,
            "Weighted mean values do not imply a zero-exception theorem for the fixed prime modulus P and all columns.",
        ),
        row(
            "Runbo Li 2026 large-moduli Harman-sieve APs",
            "https://arxiv.org/abs/2602.20917",
            "frontier_preprint_average_ap",
            "Mean-value theorems for primes with bilinear moduli up to x^(9/17) and trilinear moduli up to x^(17/32); almost-all q bounds for pi(x;q,a).",
            "At x=P^2 the bilinear/trilinear ranges are P^(18/17) and P^(17/16), so q=P lies below range, but only inside structured averages.",
            "Newest AP-distribution frontier found this round; it sharpens the column stress test but does not give a pointwise column theorem.",
            False,
            "Average over moduli and factorization classes cannot be specialized to every prime P and every residue a without a new fixed-modulus transfer.",
        ),
        row(
            "Bruna 2026 conditional GLH least AP prime",
            "https://arxiv.org/abs/2603.25612",
            "conditional_arxiv_linnik_near_gate",
            "Assuming generalized Lindelof for Dirichlet L-functions, the least prime p≡a mod q satisfies p <<_eps q^(2+eps).",
            "For q=P this gives P^(2+eps), a conditional near-square bound but not a prime guaranteed inside the strict P^2 square.",
            "Pins the conditional Linnik route almost exactly at the square barrier.",
            False,
            "It is conditional and has an epsilon/logarithmic overshoot; unconditional target needs L<=2 with compatible constants/window.",
        ),
    ]

    return {
        "certificate_type": "prime_matrix_external_frontier_theorem_stress_router",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "external_frontier_theorems_imported_side_bounds_closed_main_target_open",
        "target_short_interval_theta": TARGET_SHORT_INTERVAL_THETA,
        "target_linnik_exponent": TARGET_LINNIK_EXPONENT,
        "best_published_pointwise_short_interval_theta": bhp["theta"],
        "best_frontier_preprint_pointwise_short_interval_theta": li052["theta"],
        "best_arxiv_uniform_structural_theta": 17 / 30,
        "best_arxiv_uniform_structural_theta_label": "17/30",
        "best_published_empty_row_run_exponent_bound": bhp["empty_row_run_exponent_bound"],
        "best_frontier_preprint_empty_row_run_exponent_bound": li052["empty_row_run_exponent_bound"],
        "best_published_empty_row_run_exponent_bound_label": "0.05+epsilon",
        "best_frontier_preprint_empty_row_run_exponent_bound_label": "0.04+epsilon_if_accepted",
        "best_general_linnik_exponent_recorded": xylouris5["linnik_exponent"],
        "best_special_prime_modulus_compatible_linnik_exponent_recorded": meng45["linnik_exponent"],
        "best_average_ap_distribution_exponent_recorded": "5/8-o(1)",
        "best_large_moduli_average_ap_exponents_recorded": {
            "RunboLi2026_bilinear": "9/17",
            "RunboLi2026_trilinear": "17/32",
            "Stadlmann2025_smooth_moduli": "1/2+1/40",
            "RunboLi2025_smooth_minorant": "10/19",
        },
        "best_conditional_linnik_near_square_recorded": "2+epsilon under generalized Lindelof",
        "least_almost_prime_ap_exponent_inside_square": 1.8345,
        "transfer_gate_lemmas": {
            "pointwise_short_interval_to_row_run": (
                "A pointwise theorem giving a prime in every interval of length x^theta at x~P^2 "
                "only gives no empty row-run longer than P^(2theta-1+o(1)); every-row closure requires theta<=1/2."
            ),
            "linnik_to_square_column": (
                "A least-prime-in-AP theorem p(a mod P) << P^L enters the P^2 square only if L<=2 "
                "with compatible constants and reduced residue classes."
            ),
            "almost_all_exceptional_to_lattice": (
                "Almost-all x short-interval PNT does not control the rigid lattice of P-spaced row starts "
                "without an additional grid-transfer or second-moment input."
            ),
            "mean_value_ap_to_fixed_prime_modulus": (
                "Bombieri-Vinogradov/Elliott-Halberstam style mean-value distribution, even beyond x^1/2, "
                "does not imply the fixed-modulus statement for q=P and all reduced residue classes without "
                "a zero-exception or fixed-prime-modulus transfer theorem."
            ),
        },
        "source_version_snapshot": source_versions,
        "published_external_side_bounds": [
            "BHPNoLongEmptyRowRunExponent005",
            "XylourisLinnikColumnPrimeByHeightP5Plus",
            "MengPrimeModulusColumnPrimeByHeightP45",
        ],
        "arxiv_or_preprint_side_diagnostics": [
            "LeastP2AlmostPrimeInEachColumnInsideP2Square",
            "Li052NoLongEmptyRowRunExponent004_if_accepted",
            "HieuPrimeAPsTheta17over30_structural_abundance_no_row_closure",
            "AverageAPBeyondHalfNoFixedPrimeModulusClosure",
            "ConditionalGLHLinnikTwoPlusEpsilonNearMiss",
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
            "Hieu2025_AP_structure": hieu_ap,
        },
        "linnik_transforms": {
            "Xylouris2011": xylouris52,
            "Xylouris2018": xylouris5,
            "Meng2001_bounded_cubic_part": meng45,
            "Bruna2026_GLH_conditional": bruna_glh,
        },
        "average_ap_distribution_transforms": {
            "Stadlmann2025_smooth_moduli": stadlmann_smooth,
            "RunboLi2025_smooth_minorant": li_smooth_minorant,
            "Pascadi2025_weighted": pascadi_weighted,
            "RunboLi2026_bilinear": li_large_bilinear,
            "RunboLi2026_trilinear": li_large_trilinear,
        },
        "plain_conclusion": (
            "外部前沿定理已经能给出真实副产品：Baker-Harman-Pintz 2001 禁止长度约 "
            "P^0.05 以上的连续空行串；若 Runbo Li 2025 预印本被接受，可把指数改进到 "
            "P^0.04。Xylouris/Meng 的 Linnik 型结果保证列方向最终出现素数，但高度仍为 "
            "P^5 或 P^4.5 量级，不能进入 P^2 方阵；Li-Zhang-Cai 的 P2 almost-prime "
            "结果进入 P^2，却正好是错误奇偶对象。Guth--Maynard v2 与 Le Duc Hieu v2 "
            "在 theta>17/30 短区间内给出点态 PNT/等差数列结构，但换算到行尺度仍需要 "
            "P^(2/15+o(1)) 个行厚度。Stadlmann/Runbo Li/Pascadi 的大模数 AP 平均分布"
            "越过 x^1/2 甚至达到加权 5/8-o(1)，但不能转成固定素模数 P 的全 residue "
            "列闭合；Bruna 2026 在广义 Lindelof 下得到 q^(2+epsilon) 条件近门槛，仍有"
            "条件性与 epsilon 超方阵误差。故所有有帮助的外部定理都已定位为 side "
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
        f"**外部源核验日期：** `{payload['frontier_verified_date']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        f"target_short_interval_theta={payload['target_short_interval_theta']}",
        f"best_published_pointwise_short_interval_theta={payload['best_published_pointwise_short_interval_theta']}",
        f"best_frontier_preprint_pointwise_short_interval_theta={payload['best_frontier_preprint_pointwise_short_interval_theta']}",
        f"best_arxiv_uniform_structural_theta={payload['best_arxiv_uniform_structural_theta_label']}",
        f"best_published_empty_row_run_exponent_bound={payload['best_published_empty_row_run_exponent_bound_label']}",
        f"best_frontier_preprint_empty_row_run_exponent_bound={payload['best_frontier_preprint_empty_row_run_exponent_bound_label']}",
        f"target_linnik_exponent={payload['target_linnik_exponent']}",
        f"best_general_linnik_exponent_recorded={payload['best_general_linnik_exponent_recorded']}",
        f"best_special_prime_modulus_compatible_linnik_exponent_recorded={payload['best_special_prime_modulus_compatible_linnik_exponent_recorded']}",
        f"best_average_ap_distribution_exponent_recorded={payload['best_average_ap_distribution_exponent_recorded']}",
        f"best_conditional_linnik_near_square_recorded={payload['best_conditional_linnik_near_square_recorded']}",
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
        "## 3. 转换门槛引理",
        "",
        "```text",
        f"pointwise_short_interval_to_row_run={payload['transfer_gate_lemmas']['pointwise_short_interval_to_row_run']}",
        f"linnik_to_square_column={payload['transfer_gate_lemmas']['linnik_to_square_column']}",
        f"almost_all_exceptional_to_lattice={payload['transfer_gate_lemmas']['almost_all_exceptional_to_lattice']}",
        f"mean_value_ap_to_fixed_prime_modulus={payload['transfer_gate_lemmas']['mean_value_ap_to_fixed_prime_modulus']}",
        "```",
        "",
        "## 4. 真实副产品",
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
        "## 5. 仍需的新突破",
        "",
        "```text",
        payload["new_required_external_or_internal_breakthrough"],
        "```",
        "",
        "## 6. 来源版本快照",
        "",
        "| name | version | date | audited payload | source |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in payload["source_version_snapshot"]:
        lines.append(
            "| {name} | `{version}` | {date} | {audited} | <{source}> |".format(
                name=cell(item["name"]),
                version=cell(item["version"]),
                date=cell(item["date"]),
                audited=cell(item["audited_payload"]),
                source=item["source"],
            )
        )
    lines.extend(
        [
            "",
            "## 7. 来源链接",
        "",
        "| theorem | source |",
        "| --- | --- |",
        ]
    )
    for item in payload["rows"]:
        lines.append(f"| {cell(item['theorem'])} | <{item['source']}> |")
    lines.extend(
        [
            "",
            "## 8. 依赖哈希",
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
