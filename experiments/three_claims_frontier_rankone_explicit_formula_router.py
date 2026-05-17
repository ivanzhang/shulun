#!/usr/bin/env python3
"""梳理三个命题前沿，并把 rank-one 硬点路由到显式 AP/零点屏障。

用法示例：
  python3 experiments/three_claims_frontier_rankone_explicit_formula_router.py
  python3 -m json.tool docs/monograph/three-claims-frontier-rankone-explicit-formula-router.json

输出：
  data/three-claims-frontier-rankone-explicit-formula-ledger.json
  docs/monograph/three-claims-frontier-rankone-explicit-formula-router.json
  docs/monograph/three-claims-frontier-rankone-explicit-formula-router.md
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

OUT_LEDGER = DATA / "three-claims-frontier-rankone-explicit-formula-ledger.json"
OUT_JSON = DOCS / "three-claims-frontier-rankone-explicit-formula-router.json"
OUT_MD = DOCS / "three-claims-frontier-rankone-explicit-formula-router.md"

RANKONE = "prime-matrix-linnik2-rankone-phase-capacity-router.json"
NONPRINCIPAL = "prime-matrix-linnik2-nonprincipal-character-obstruction-router.json"
LINNIK2 = "prime-matrix-localized-pcrt-transfer-linnik2-barrier-router.json"
STATUS_TABLE = "claim-status-table.md"
FINAL_PROOF_DRAFT = ROOT / "docs" / "final-proof-draft.md"
PRIME_DENSITY_WAVES_V = ROOT / "docs" / "prime-density-waves-V.md"
PRIME_DENSITY_WAVES_VIII = ROOT / "docs" / "prime-density-waves-VIII.md"
PRIME_DENSITY_WAVES_X = ROOT / "docs" / "prime-density-waves-X.md"

RANKONE_TARGET = "RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2"
AP_POSITIVITY = "SharpPointwiseThetaAPPositivityAtXEqualsP2ForPrimeModuli"
ZERO_PACKET = "ExplicitAPZeroPacketBoundBeatingMainTermAtXEqualsP2"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    DOCS / RANKONE,
    DOCS / NONPRINCIPAL,
    DOCS / LINNIK2,
    DOCS / STATUS_TABLE,
    FINAL_PROOF_DRAFT,
    PRIME_DENSITY_WAVES_V,
    PRIME_DENSITY_WAVES_VIII,
    PRIME_DENSITY_WAVES_X,
    PAPER,
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result: dict[str, str] = {}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def three_claim_frontiers() -> list[dict[str, Any]]:
    """梳理三个命题的当前最前沿。"""
    return [
        {
            "claim": "Prime Matrix row/column",
            "target": "奇素数 P x P 方阵中每行和 P 列外每列都有素数",
            "latest_chain": [
                "A/B counterexample reduction to Structured-EHPD",
                "complete P-wheel non-P column uniformity is global average only",
                "localized P-CRT transfer equals least prime in every nonzero class mod P below P^2",
                "Linnik=2 zero column forces nonprincipal projection N_a=-T_0",
                "energy capacity-only route rejected; latest hard point is rank-one evaluation phase coherence",
            ],
            "latest_open": RANKONE_TARGET,
            "closed_this_round": "frontier synthesized; rank-one target routed to explicit AP positivity / zero-packet barrier",
            "unconditional_closed": False,
        },
        {
            "claim": "Two-point / quadratic secondary sieve",
            "target": "后半方阵中存在差/和为任意固定偶数的素数对候选之一",
            "latest_chain": [
                "two-point rough-pair condition p∤x(x-w) would imply fixed-gap prime pairs",
                "secondary-sieve field decomposes into TLI/BST/BMD/WBE2/BE2-3K/KLS-window",
                "external DI/BFI-Kloosterman large-sieve route can close BMD as an external-deep-theorem chain",
                "fully self-contained route still needs I3-Core / true-residual total large-incidence estimate",
            ],
            "latest_open": "I3CoreTrueResidualTotalLargeIncidenceOrExternalDIBFIKLSWindow",
            "closed_this_round": "status separated from row/column rank-one AP hard point",
            "unconditional_closed": False,
        },
        {
            "claim": "RH contradiction field",
            "target": "ζ(s) 的非平凡零点实部均为 1/2",
            "latest_chain": [
                "off-critical zero creates smooth prime anomaly",
                "anomaly is routed through sparse/dense/tail/internal/global controlled exits",
                "current manuscript is a verification package under recorded local theorems and restricted external inputs",
                "final promotion requires independent line-by-line referee verification of controlled exits",
            ],
            "latest_open": "IndependentRefereeAcceptanceOfAllRHControlledExits",
            "closed_this_round": "status boundary restated; no row/column AP lemma is reused as RH proof",
            "unconditional_closed": False,
        },
    ]


def rankone_to_explicit_formula_chain() -> list[dict[str, str]]:
    """列出 rank-one 硬点到显式 AP/零点屏障的链条。"""
    return [
        {
            "from": RANKONE_TARGET,
            "to": "rho_a(P)<1 for every a in F_P^*",
        },
        {
            "from": "rho_a(P)=1-theta_a(P)/(T_0(P)/(P-1))",
            "to": "theta_a(P)>0 for every a in F_P^*",
        },
        {
            "from": "theta_a(P)>0",
            "to": AP_POSITIVITY,
        },
        {
            "from": "character explicit formula",
            "to": ZERO_PACKET,
        },
        {
            "from": "GRH-shape error O(P log^2 P)",
            "to": "not enough to beat main term of size about P at x=P^2",
        },
        {
            "from": "BV / mean AP / complete CRT uniformity",
            "to": "average only; cannot remove a single exceptional residue direction",
        },
    ]


def explicit_formula_ledger() -> dict[str, str]:
    """登记 rank-one AP positivity 的显式公式口径。"""
    return {
        "theta_class": "theta(P^2;P,a)=sum_{ell<=P^2, ell prime, ell=a mod P} log ell",
        "main_term": "T_0(P)/(P-1) ~ P",
        "rankone_ratio": "rho_a(P)=1-theta(P^2;P,a)/(T_0(P)/(P-1))",
        "zero_column": "rho_a(P)=1 iff theta(P^2;P,a)=0",
        "explicit_formula_shape": "theta(P^2;P,a)=main - (1/(P-1))*sum_{chi!=chi0} conjugate(chi(a))*sum_{rho_chi} P^(2 rho_chi)/rho_chi + controlled trivial terms",
        "needed_bound": "for every a, the signed zero packet plus trivial terms must be strictly smaller than the main term",
        "grh_shape_not_enough": "sqrt(x) log^2(Px)=P log^2(P^3) is larger than the main term scale P",
        "linnik2_barrier": "standard Linnik gives P^L with L>2; it does not imply positivity at P^2",
    }


def build_rows(rankone: dict[str, Any]) -> list[dict[str, Any]]:
    """构造判定表。"""
    rankone_imported = (
        rankone.get("next_direct_attack_target") == RANKONE_TARGET
        and rankone.get("rankone_phase_coherence_exclusion_proved") is False
    )
    return [
        row(
            "ThreeClaimFrontierSynthesisClosed",
            True,
            True,
            "三个命题的最前沿状态已按行/列、二次筛、RH 分离，避免状态串用。",
            "none",
        ),
        row(
            "RankOneHardPointImported",
            rankone_imported,
            False,
            "上一层已关闭 L2 capacity-only 误出口，并把行/列列侧硬点压到 rank-one evaluation 相位。",
            RANKONE_TARGET,
        ),
        row(
            "RankOneEquivalentToThetaAPPositivity",
            True,
            True,
            "rho_a<1 等价于 theta(P^2;P,a)>0；这就是每个非零 AP 类在 P^2 前有素数。",
            AP_POSITIVITY,
        ),
        row(
            "ExplicitFormulaBarrierIdentified",
            True,
            True,
            "显式公式显示需要逐 residue 的带符号零点包小于主项，而不是平均能量控制。",
            ZERO_PACKET,
        ),
        row(
            "CurrentClassicalInputsInsufficient",
            True,
            True,
            "GRH 形状、BV 平均、完整 CRT 均匀性和标准 Linnik 均不推出 x=P^2 的逐类正性。",
            ZERO_PACKET,
        ),
        row(
            "TargetUnconditionallyClosed",
            False,
            False,
            "本步没有证明 sharp pointwise AP positivity；行/列、二次筛、RH 均仍不能称无条件终稿。",
            f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {ZERO_PACKET}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造前沿综合证书。"""
    rankone = load_json(DOCS / RANKONE)
    rows = build_rows(rankone)
    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {SIGNED_PAYLOAD_ATOM} OR {ZERO_PACKET}) "
        f"AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "three_claims_frontier_rankone_explicit_formula_router",
        "status": "three_claim_frontiers_synthesized_rankone_routed_to_explicit_ap_zero_packet_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "three_claim_frontiers": three_claim_frontiers(),
        "rankone_to_explicit_formula_chain": rankone_to_explicit_formula_chain(),
        "explicit_formula_ledger": explicit_formula_ledger(),
        "rankone_equivalent_to_theta_ap_positivity": True,
        "explicit_formula_barrier_identified": True,
        "current_classical_inputs_sufficient": False,
        "row_column_unconditional_closed": False,
        "two_point_unconditional_closed": False,
        "rh_unconditional_closed": False,
        "target_input_before_router": RANKONE_TARGET,
        "next_direct_attack_target": ZERO_PACKET,
        "latest_strict_activity_basis": latest_basis,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "三个命题的当前前沿必须分开看：行/列链最新硬点是 `RankOneNegativeEvaluationProjectionPhaseCoherenceExclusionAtP2`；"
            "二次筛链仍需要 I3-Core/true-residual total incidence 或外部 DI/BFI-KLS；RH 链仍是待独立审稿的验证包。"
            "继续攻击行/列最新硬点可得精确等价：rank-one 排斥就是 `theta(P^2;P,a)>0` 对每个非零类成立。"
            "显式公式把它压成带符号零点包必须逐类小于主项的屏障；当前 GRH 形状、BV 平均、完整 CRT 均匀性和标准 Linnik 都不足以给出该 sharp P^2 正性。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Three Claims Frontier / Rank-one Explicit Formula Router",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"rankone_equivalent_to_theta_ap_positivity={fmt_bool(result['rankone_equivalent_to_theta_ap_positivity'])}",
        f"explicit_formula_barrier_identified={fmt_bool(result['explicit_formula_barrier_identified'])}",
        f"current_classical_inputs_sufficient={fmt_bool(result['current_classical_inputs_sufficient'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"two_point_unconditional_closed={fmt_bool(result['two_point_unconditional_closed'])}",
        f"rh_unconditional_closed={fmt_bool(result['rh_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 三个命题前沿",
        "",
        "| claim | target | latest open | unconditional closed |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["three_claim_frontiers"]:
        lines.append(
            f"| `{table_cell(item['claim'])}` | {table_cell(item['target'])} | "
            f"`{table_cell(item['latest_open'])}` | `{fmt_bool(item['unconditional_closed'])}` |"
        )

    lines += [
        "",
        "## 2. 行/列最新链条",
        "",
    ]
    for item in result["three_claim_frontiers"][0]["latest_chain"]:
        lines.append(f"- {item}")

    lines += [
        "",
        "## 3. 二次筛最新链条",
        "",
    ]
    for item in result["three_claim_frontiers"][1]["latest_chain"]:
        lines.append(f"- {item}")

    lines += [
        "",
        "## 4. RH 最新链条",
        "",
    ]
    for item in result["three_claim_frontiers"][2]["latest_chain"]:
        lines.append(f"- {item}")

    lines += [
        "",
        "## 5. Rank-one 到显式公式屏障",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["rankone_to_explicit_formula_chain"]:
        lines.append(f"| `{table_cell(item['from'])}` | `{table_cell(item['to'])}` |")

    lines += [
        "",
        "## 6. 显式公式账本",
        "",
        "| item | formula |",
        "| --- | --- |",
    ]
    for key, value in result["explicit_formula_ledger"].items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")

    lines += [
        "",
        "## 7. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            f"| `{table_cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | {table_cell(item['meaning'])} | {table_cell(item['remaining'])} |"
        )

    lines += [
        "",
        "## 8. 最新活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "审稿边界：本文件没有证明 sharp pointwise AP positivity，也没有把二次筛或 RH 提升为无条件终稿；它只完成三命题前沿同步并关闭若干误用路线。",
        "",
        "## 9. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出路由证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
                "two_point_unconditional_closed": result["two_point_unconditional_closed"],
                "rh_unconditional_closed": result["rh_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
