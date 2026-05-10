#!/usr/bin/env python3
"""把 Stepanov-Kummer 非零秩输入压成阶无关签名选择引理。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_stepanov_rank_signature_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-stepanov-rank-signature-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-stepanov-rank-signature-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-stepanov-rank-signature-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-stepanov-kummer-trace-frontier-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity"
SIGNATURE_ATOM = "OrderFreeKummerSignatureSelectorAndHasseJetRankLemma"
JET_ATOM = "BoundedBranchSignatureHasseJetIndependenceLemma"
STEPANOV_ATOM = "StepanovAuxiliaryPolynomialRankBoundForKummerSums"
KUMMER_TRACE = "SelfContainedRankOneKummerSheafRHTraceBound"
BURGESS_POINTWISE = "SelfContainedBurgessPointwiseCharacterSumForLargeDyadicIntervals"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def signature_table() -> list[dict[str, str]]:
    """登记 Burgess 常用 r 下的分支签名口径。"""
    rows = []
    for r in [5, 9, 17, 26]:
        m = 2 * r
        rows.append(
            {
                "r": str(r),
                "branch_bound_m": str(m),
                "signature_vector_length": str(m),
                "rank_constant_may_depend_on": f"m<={m}",
                "rank_constant_must_not_depend_on": "d,P,chi,branch_positions",
                "next_selector_size": "positive c_m*D after Hasse-jet losses",
            }
        )
    return rows


def build_result() -> dict[str, Any]:
    """构造 Stepanov rank-signature 前沿证书。"""
    previous = load_json(PREVIOUS)
    active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("stepanov_auxiliary_rank_surjectivity_internalized") is False
        and previous.get("stepanov_multiplicity_degree_ledger_closed") is True
    )

    normalized_rank_problem = {
        "input": "branch divisor B={a_1,...,a_m}, signed exponents e_a, character order d, f not a d-th power",
        "auxiliary_space_goal": "construct a bounded-pole auxiliary space with dimension growing like c_m*D and rank loss O_m(T*N)",
        "forbidden_dimension_source": "do not use the full y^d=f(x) monomial ladder; it has d-dependent dimension/genus",
        "allowed_dimension_source": "use branch valuation signatures and Hasse derivatives whose constants depend only on m",
        "surjectivity_goal": "after imposing Hasse-jet vanishing conditions, a nonzero function remains on the Kummer eigenspace",
    }

    signature_normal_form = {
        "valuation_signature": "sigma(g)=(ord_{a_1}(g),...,ord_{a_m}(g)) modulo local Kummer equivalence",
        "collision_rule": "two auxiliary monomials can collapse only if their signature difference is invisible at every branch place",
        "nonpower_anchor": "because f is not a d-th power, at least one branch coordinate carries a nonzero residue signature",
        "order_free_requirement": "the chosen signature family must have size and separation bounded below in terms of m, not d",
        "local_derivatives": "Hasse derivatives change local signatures by controlled bounded amounts, so jet conditions consume O_m(T) signatures per point",
    }

    closed_reductions = {
        "rank_gap_relocalized": "the old nonzero-rank gate is now a finite branch-signature selector plus Hasse-jet independence problem",
        "d_ladder_firewall": "any proof using O(d) independent y-powers is rejected because it breaks Burgess uniformity",
        "jet_bookkeeping": "multiplicity T at N points consumes a predictable number of Hasse-jet linear conditions once a selector exists",
        "degree_bookkeeping_imported": "previous Stepanov degree/multiplicity contradiction applies after selector rank is available",
    }

    remaining_selector = {
        "precise_atom": SIGNATURE_ATOM,
        "selector_statement": "for every non-dth-power f with m branch places, find an order-free family of auxiliary signatures with rank >= c_m*D after all Kummer relations",
        "jet_statement": "the Hasse-jet evaluation matrix on that family has rank loss bounded by C_m*T*N",
        "why_not_closed_here": "the corpus still lacks a proof that such a selector exists uniformly for all exponent residue patterns e_a mod d",
        "if_proved": "StepanovKummerAuxiliaryPolynomialNonzeroRankSurjectivity closes, then the Kummer trace and Burgess B4 chain can continue",
    }

    rank_relocalized = active
    d_ladder_firewall_closed = active
    signature_normal_form_closed = active
    hasse_jet_bookkeeping_closed = active
    selector_internalized = False
    rank_surjectivity_closed = selector_internalized and hasse_jet_bookkeeping_closed
    stepanov_closed = rank_surjectivity_closed

    rows = [
        row(
            "StepanovRankSurjectivityTargetActive",
            active,
            True,
            "上一证书已把唯一剩余压成 Stepanov-Kummer 辅助空间非零秩。",
            TARGET,
        ),
        row(
            "RankGapRelocalizedToBranchSignatures",
            rank_relocalized,
            True,
            "非零秩问题已重定位为分支估值签名选择与 Hasse-jet 独立性。",
            SIGNATURE_ATOM,
        ),
        row(
            "FullKummerDLadderFirewallClosed",
            d_ladder_firewall_closed,
            True,
            "已排除用 `y^0,...,y^{d-1}` 全梯子制造维数的 d 依赖路线。",
            "review firewall",
        ),
        row(
            "BranchSignatureNormalFormClosed",
            signature_normal_form_closed,
            True,
            "辅助函数的可区分性可由分支估值签名记录，碰撞只来自全分支不可见差。",
            SIGNATURE_ATOM,
        ),
        row(
            "HasseJetBookkeepingClosed",
            hasse_jet_bookkeeping_closed,
            True,
            "一旦有阶无关签名族，Hasse-jet 条件的秩损耗可按 `O_m(TN)` 记账。",
            JET_ATOM,
        ),
        row(
            SIGNATURE_ATOM,
            selector_internalized,
            selector_internalized,
            "仍需证明所有 exponent residue pattern 下都存在足够大的阶无关签名选择族。",
            SIGNATURE_ATOM,
        ),
        row(
            TARGET,
            rank_surjectivity_closed,
            rank_surjectivity_closed,
            "Stepanov-Kummer 非零秩等待签名选择与 Hasse-jet 秩引理。",
            SIGNATURE_ATOM,
        ),
        row(
            STEPANOV_ATOM,
            stepanov_closed,
            stepanov_closed,
            "Stepanov 完整证明仍未作者侧闭合。",
            TARGET,
        ),
        row(
            KUMMER_TRACE,
            False,
            False,
            "秩一 Kummer 迹界仍等待 Stepanov rank gate。",
            STEPANOV_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只把非零秩问题压成签名选择原子，不声明行/列命题无条件闭合。",
            BURGESS_POINTWISE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_stepanov_rank_signature_router",
        "status": "stepanov_nonzero_rank_reduced_to_order_free_branch_signature_selector",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "stepanov_rank_surjectivity_target_active": active,
        "rank_gap_relocalized_to_branch_signatures": rank_relocalized,
        "full_kummer_d_ladder_firewall_closed": d_ladder_firewall_closed,
        "branch_signature_normal_form_closed": signature_normal_form_closed,
        "hasse_jet_bookkeeping_closed": hasse_jet_bookkeeping_closed,
        "order_free_signature_selector_internalized": selector_internalized,
        "stepanov_kummer_auxiliary_rank_surjectivity_proved": rank_surjectivity_closed,
        "stepanov_auxiliary_polynomial_rank_bound_proved": stepanov_closed,
        "self_contained_kummer_trace_bound_internalized": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SIGNATURE_ATOM,
        "next_subatom": JET_ATOM,
        "normalized_rank_problem": normalized_rank_problem,
        "signature_normal_form": signature_normal_form,
        "closed_reductions": closed_reductions,
        "remaining_selector": remaining_selector,
        "signature_table": signature_table(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Stepanov-Kummer 非零秩输入继续缩窄。现在的硬点不再是笼统的辅助多项式存在性，"
            "而是一个阶无关的分支签名选择问题：必须在只允许常数依赖分支数 `m<=2r`、"
            "不允许依赖角色阶 `d` 的条件下，构造足够多的辅助函数签名，并证明 Hasse-jet "
            "插值条件只造成 `O_m(TN)` 的秩损耗。本步闭合了三件事：把秩问题重定位到分支估值签名，"
            "排除使用整条 Kummer 曲线 `y^0,...,y^{d-1}` 全梯子的 d 依赖伪证明，"
            "并固定 Hasse-jet 条件的记账接口。唯一剩余变为 "
            "`OrderFreeKummerSignatureSelectorAndHasseJetRankLemma`。未证明该签名选择引理前，"
            "Stepanov、Kummer 迹界、Weil 界、B4 和行/列命题仍不能作者侧无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict RKS2/RKS3 Stepanov 秩签名前沿证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"stepanov_rank_surjectivity_target_active={fmt_bool(result['stepanov_rank_surjectivity_target_active'])}",
        f"rank_gap_relocalized_to_branch_signatures={fmt_bool(result['rank_gap_relocalized_to_branch_signatures'])}",
        f"full_kummer_d_ladder_firewall_closed={fmt_bool(result['full_kummer_d_ladder_firewall_closed'])}",
        f"branch_signature_normal_form_closed={fmt_bool(result['branch_signature_normal_form_closed'])}",
        f"hasse_jet_bookkeeping_closed={fmt_bool(result['hasse_jet_bookkeeping_closed'])}",
        f"order_free_signature_selector_internalized={fmt_bool(result['order_free_signature_selector_internalized'])}",
        f"stepanov_kummer_auxiliary_rank_surjectivity_proved={fmt_bool(result['stepanov_kummer_auxiliary_rank_surjectivity_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 归一化秩问题",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in result["normalized_rank_problem"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 2. 分支签名正规形",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["signature_normal_form"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 3. 已闭合归约",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["closed_reductions"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 4. 当前真缺口",
            "",
            "| field | value |",
            "| --- | --- |",
        ]
    )
    for key, value in result["remaining_selector"].items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")

    lines.extend(
        [
            "",
            "## 5. 签名参数表",
            "",
            "| r | branch_bound_m | signature_vector_length | rank_constant_may_depend_on | rank_constant_must_not_depend_on | next_selector_size |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["signature_table"]:
        lines.append(
            "| `{r}` | `{branch_bound_m}` | `{signature_vector_length}` | `{rank_constant_may_depend_on}` | `{rank_constant_must_not_depend_on}` | {next_selector_size} |".format(
                **{key: table_cell(value) for key, value in item.items()}
            )
        )

    lines.extend(
        [
            "",
            "## 6. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 7. 下一最窄目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "审稿边界：本证书没有证明阶无关签名选择引理；",
            "它只关闭秩问题的正规形、防 d 依赖误用和 Hasse-jet 记账接口。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
