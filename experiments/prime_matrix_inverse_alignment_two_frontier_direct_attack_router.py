#!/usr/bin/env python3
"""生成 inverse-alignment 两条最新剩余的直接攻坚同步证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_two_frontier_direct_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-two-frontier-direct-attack-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-two-frontier-direct-attack-router.json
  docs/monograph/prime-matrix-inverse-alignment-two-frontier-direct-attack-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-two-frontier-direct-attack-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-two-frontier-direct-attack-router.md"

FIRST_HALF = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"
NONFINAL = "NonFinalTailPDECSAEBudgetAmplificationOrAlternativeContradiction"
SPARSE_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
HOT_FIXED = "TerminalCoreHotDivisorWindowPDECorSAE AND FixedTypeHistoryPDECExclusion"

SOURCE_FILES = [
    "prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json",
    "prime-matrix-postsquare-first-half-finite-boundary-router.json",
    "prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.json",
    "prime-matrix-strict-sparse-budget-after-unified-sync-router.json",
    "prime-matrix-strict-same-parameter-sparse-margin-attack-router.json",
    "prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json",
    "prime-matrix-strict-terminal-defect-exhaustion-router.json",
    "prime-matrix-strict-atomic-origin-identity-cycle-cut-sync-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_two_frontier_direct_attack_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
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


def first_half_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """平方后前半窗输入线判定。"""
    final_tail = data["final_tail"]
    finite = data["finite_first_half"]
    finite_scan = finite.get("finite_scan", {})
    return [
        row(
            "FinalTailReductionToFirstHalfPrimeSquareImported",
            final_tail.get("final_tail_uniform_bound_implies_first_half_prime_square_input") is True,
            True,
            "final-tail 全局粗幸存下界已经严格压到平方后前半窗素数输入。",
            FIRST_HALF,
        ),
        row(
            "FiniteFirstHalfPrimeSquareBoundaryChecked",
            finite_scan.get("failure_count") == 0 and bool(finite_scan),
            False,
            f"有限边界已检查到 P<= {finite_scan.get('parameters', {}).get('max_p', 'NA')}；这是证据，不是全局证明。",
            "finite evidence only",
        ),
        row(
            "ExternalGeneralPrimeGapDirectlySufficient",
            False,
            False,
            "通用短区间素数定理当前不能直接给出长度 P 的 (P^2,P^2+P) 全局结论。",
            FIRST_HALF,
        ),
        row(
            "FirstHalfPrimeSquareAuthorSideClosed",
            False,
            False,
            "该输入仍是 final-tail 线的作者侧开放点；不能用有限验证替代。",
            f"{FIRST_HALF} OR {NONFINAL}",
        ),
    ]


def nonfinal_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """非 final-tail 预算放大线判定。"""
    cold_chain = data["cold_chain"]
    sparse = data["sparse"]
    sparse_margin = data["sparse_margin"]
    cold_numeric = data["cold_numeric"]
    terminal = data["terminal"]
    moving = data["moving"]
    return [
        row(
            "InverseAlignmentColdCoreChainReconciled",
            cold_chain.get("inverse_alignment_cold_core_chain_reconciled") is True,
            True,
            "逆元相位和 exact-x 冷限制出口已接到 C_core/产品支撑/Rankin/热核心终端链。",
            f"{SPARSE_MARGIN} AND {MOVING_ATOM}",
        ),
        row(
            "SparseBudgetNormalFormImported",
            sparse.get("same_parameter_sparse_demand_cold_supply_normal_form_closed") is True,
            False,
            "非持久预算已经压成同参数标量缺口 M#-E_registered>U_np。",
            SPARSE_MARGIN,
        ),
        row(
            "SparseStrictMarginReducedToColdNumericEnvelope",
            sparse_margin.get("same_parameter_sparse_margin_internal_reduction_closed") is True,
            False,
            "纯非持久内部剩余已压到冷供给同参数数值包。",
            COLD_NUMERIC,
        ),
        row(
            "ColdNumericEnvelopeStillOpen",
            cold_numeric.get("cold_supply_same_parameter_numeric_envelope_proved") is True,
            False,
            "当前材料明确显示粗 full-depth 历史包过宽，必须证明有效冷历史剪枝与 C_core/T_PDEC 数值表。",
            "EffectiveColdHistoryPruningOrHotFixedReturnTheorem AND ColdCoreThresholdFunctionNumericTable AND SameParameterPDECThresholdNumericTable",
        ),
        row(
            "TerminalDefectNoFreeExitImported",
            terminal.get("terminal_defect_no_free_exit_closed") is True,
            True,
            "终端缺陷没有自由第四出口；失败必须进入命名回流或统一预算。",
            f"{COLD_NUMERIC} AND {MOVING_ATOM}",
        ),
        row(
            "MovingAtomRecommendedButOpen",
            moving.get("next_direct_attack_target") == MOVING_ATOM or moving.get("status") is not None,
            False,
            "持久 actual noncanonical moving atom 是最贴近终端矛盾的并行开放点。",
            MOVING_ATOM,
        ),
        row(
            "NonFinalTailPDECSAEBudgetAmplificationCurrentCorpusProved",
            False,
            False,
            "非 final-tail 线已精准收缩，但冷数值包、热/固定出口、moving atom 和 DStructure 仍未同时关闭。",
            f"{COLD_NUMERIC} AND {HOT_FIXED} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造双线攻坚证书。"""
    data = {
        "final_tail": load_json("prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json"),
        "finite_first_half": load_json("prime-matrix-postsquare-first-half-finite-boundary-router.json"),
        "cold_chain": load_json("prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.json"),
        "sparse": load_json("prime-matrix-strict-sparse-budget-after-unified-sync-router.json"),
        "sparse_margin": load_json("prime-matrix-strict-same-parameter-sparse-margin-attack-router.json"),
        "cold_numeric": load_json("prime-matrix-strict-cold-supply-numeric-envelope-attack-router.json"),
        "terminal": load_json("prime-matrix-strict-terminal-defect-exhaustion-router.json"),
        "moving": load_json("prime-matrix-strict-atomic-origin-identity-cycle-cut-sync-router.json"),
    }
    fh_rows = first_half_rows(data)
    nf_rows = nonfinal_rows(data)
    return {
        "certificate_type": "prime_matrix_inverse_alignment_two_frontier_direct_attack_router",
        "status": "two_frontiers_attacked_first_half_open_nonfinal_reduced_to_cold_numeric_moving_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_for_global_proof": True,
        "first_half_prime_square_author_side_closed": False,
        "nonfinal_pdec_sae_budget_amplification_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "persistent_terminal_family_excluded": False,
        "dstructure_rankin_independently_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": f"{FIRST_HALF} AND {NONFINAL}",
        "hardpoint_after_router": f"{COLD_NUMERIC} AND {MOVING_ATOM} AND {DSTRUCTURE}; parallel strong input {FIRST_HALF}",
        "next_direct_attack_target": COLD_NUMERIC,
        "parallel_attack_targets": [MOVING_ATOM, DSTRUCTURE, FIRST_HALF],
        "first_half_rows": fh_rows,
        "nonfinal_rows": nf_rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "两条最新剩余已经区分清楚：final-tail 线若继续直接闭合，必须证明 "
            f"`{FIRST_HALF}`，这是当前作者侧未闭合的强短区间输入；非 final-tail 线没有换命题，"
            f"已经沿逆元相位、C_core/Rankin 和终端缺陷耗尽链压到 `{COLD_NUMERIC}`，"
            f"并行开放 `{MOVING_ATOM}` 与 `{DSTRUCTURE}`。"
            "因此本轮完成的是双线边界收缩与证据归档，尚不能声明行/列命题无条件闭合。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix inverse alignment 双线直接攻坚路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"first_half_prime_square_author_side_closed={fmt_bool(result['first_half_prime_square_author_side_closed'])}",
        f"nonfinal_pdec_sae_budget_amplification_proved={fmt_bool(result['nonfinal_pdec_sae_budget_amplification_proved'])}",
        f"cold_supply_same_parameter_numeric_envelope_proved={fmt_bool(result['cold_supply_same_parameter_numeric_envelope_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Final-tail / 平方后前半窗线",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    for item in result["first_half_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 非 final-tail / PDEC-SAE-预算放大线",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["nonfinal_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{item['gate']}`",
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    table_cell(item["meaning"]),
                    table_cell(item["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 下一步",
            "",
            f"- 主攻 `{COLD_NUMERIC}`：证明有效冷历史剪枝、`C_core` 数值表和 `T_PDEC` 数值表，使非持久供给严格小于 `M#` 需求。",
            f"- 并行攻 `{MOVING_ATOM}`：排斥持久 actual noncanonical 终端族，避免命名回流吞掉余量。",
            f"- 保留 `{DSTRUCTURE}` 独立验收门；final-tail 强输入 `{FIRST_HALF}` 只作为平行强路线，不作为已证事实。",
            "",
            "## 4. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "direct_unconditional_contradiction_found": result["direct_unconditional_contradiction_found"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
