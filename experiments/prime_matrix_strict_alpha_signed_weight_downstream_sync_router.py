#!/usr/bin/env python3
"""生成 strict alpha signed 权重律下游同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_signed_weight_downstream_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.md"

ALPHA_WEIGHT = "AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger"
INDEPENDENT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
ACTUAL_MOVING = "ActualNoncanonicalMovingBlockSpreadNCBLKForCounterexampleBranchAndReturn"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-signed-lift-failure-return-router.json",
    "prime-matrix-strict-alpha-signed-weight-law-router.json",
    "prime-matrix-strict-independent-identity-statement-taxonomy-router.json",
    "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json",
    "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json",
    "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json",
    "prime-matrix-moving-block-dprc-ledger-compatibility-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def make_row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def contains(text: Any, needle: str) -> bool:
    """检查证书字段中是否出现指定原子名。"""
    return needle in str(text)


def build_result() -> dict[str, Any]:
    """构造 alpha signed 权重律下游同步证书。"""
    lift = load_json(DOCS / "prime-matrix-strict-alpha-signed-lift-failure-return-router.json")
    weight = load_json(DOCS / "prime-matrix-strict-alpha-signed-weight-law-router.json")
    identity = load_json(DOCS / "prime-matrix-strict-independent-identity-statement-taxonomy-router.json")
    moving = load_json(DOCS / "prime-matrix-strict-actual-moving-block-spread-ncb-lk-router.json")
    ncblk = load_json(DOCS / "prime-matrix-strict-acyclic-ncblk-source-antiatom-router.json")
    global_split = load_json(DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json")
    dprc = load_json(DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json")

    lift_returns_to_weight = lift.get("next_direct_attack_target") == ALPHA_WEIGHT
    weight_to_identity = (
        weight.get("alpha_signed_weight_law_router_closed") is True
        and weight.get("alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved") is False
        and contains(weight.get("terminal_gap_after_router"), INDEPENDENT_IDENTITY)
    )
    identity_to_moving = (
        identity.get("strict_identity_statement_taxonomy_adapter_closed") is True
        and identity.get("independent_noncanonical_precauchy_arithmetic_identity_statement_proved") is False
        and identity.get("terminal_gap_after_router") == ACTUAL_MOVING
    )
    moving_to_terminal_model = (
        moving.get("strict_actual_moving_block_router_closed") is True
        and moving.get("actual_noncanonical_moving_block_spread_ncb_lk_proved") is False
        and contains(moving.get("terminal_gap_after_router"), GLOBAL_TERMINAL)
        and contains(moving.get("terminal_gap_after_router"), MODEL_LEDGER)
    )
    ncblk_no_new_terminal = (
        ncblk.get("strict_acyclic_ncblk_source_antiatom_router_closed") is True
        or contains(ncblk.get("plain_conclusion"), "不是新终端")
        or contains(ncblk.get("terminal_gap_after_router"), MODEL_LEDGER)
    )
    global_terminal_open = (
        global_split.get("terminal_gap_after_router") == GLOBAL_TERMINAL
        and global_split.get("global_terminal_family_exclusion_proved") is not True
    )
    dprc_model_retained = (
        dprc.get("exact_model_gap_dprc_compatibility_proved") is True
        or contains(dprc.get("plain_conclusion"), MODEL_LEDGER)
        or contains(dprc.get("latest_self_contained_basis"), MODEL_LEDGER)
    )

    # 中文注释：同步证书只证明链条已经对齐；不证明终端门本身。
    downstream_sync_closed = all(
        [
            lift_returns_to_weight,
            weight_to_identity,
            identity_to_moving,
            moving_to_terminal_model,
            global_terminal_open,
            dprc_model_retained,
        ]
    )

    rows = [
        make_row(
            "LiftFailureReturnsToAlphaWeightLaw",
            lift_returns_to_weight,
            True,
            "signed lift 失败登记纪律闭合后，首个未证输入回到 alpha signed 权重律。",
            ALPHA_WEIGHT,
        ),
        make_row(
            "AlphaWeightLawReducedToIndependentIdentity",
            weight_to_identity,
            True,
            "权重律已被拆成独立 pre-Cauchy 恒等式、精确公式、非零符号局部因子、反推禁用和失败回流。",
            INDEPENDENT_IDENTITY,
        ),
        make_row(
            "IndependentIdentityTaxonomyReducedToActualMoving",
            identity_to_moving,
            True,
            "独立恒等式陈述不是第五类来源；strict 自足线剩 actual noncanonical moving-block/NC-BLK。",
            ACTUAL_MOVING,
        ),
        make_row(
            "NCBLKNotNewTerminal",
            ncblk_no_new_terminal,
            True,
            "NC-BLK/source antiatom 不是新终端；它只能回到 moving/source 账本或全局终端门。",
            f"{ACTUAL_MOVING} / {GLOBAL_TERMINAL}",
        ),
        make_row(
            "ActualMovingBlockNoUnnamedExit",
            moving_to_terminal_model,
            True,
            "actual moving-block/NC-BLK 不能再作为无名出口，已压到全局终端容量/大筛门与模型余量账本。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "GlobalTerminalFamilyStillOpen",
            global_terminal_open,
            False,
            "全局终端家族已拆成 PDEC-CAP 或内部 CleanKLS/DLS，但该二选一尚未证明。",
            GLOBAL_TERMINAL,
        ),
        make_row(
            "ExplicitModelGapDPRCLedgerRetained",
            dprc_model_retained,
            False,
            "moving-block 替换没有删除模型余量账本；它仍需独立证明或有限证书。",
            MODEL_LEDGER,
        ),
        make_row(
            "DStructureRankinGateRetained",
            True,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是行/列无条件升级的独立验收门。",
            DSTRUCTURE_GATE,
        ),
        make_row(
            "DownstreamSyncClosedButTheoremOpen",
            downstream_sync_closed,
            True,
            "中间节点已同步到同一开放基；这只关闭路由循环，不关闭反例终端矛盾。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
    ]

    open_basis = f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}"
    strict_noncanonical_basis = (
        f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {WINDOWED_DLS} AND {DSTRUCTURE_GATE}"
    )

    return {
        "certificate_type": "prime_matrix_strict_alpha_signed_weight_downstream_sync_router",
        "status": "alpha_signed_weight_downstream_synced_to_terminal_modelgap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "downstream_sync_router_closed": downstream_sync_closed,
        "lift_failure_returns_to_alpha_weight_law": lift_returns_to_weight,
        "alpha_weight_law_reduced_to_independent_identity": weight_to_identity,
        "independent_identity_taxonomy_reduced_to_actual_moving": identity_to_moving,
        "actual_moving_block_no_unnamed_exit": moving_to_terminal_model,
        "ncblk_not_new_terminal": ncblk_no_new_terminal,
        "global_terminal_family_still_open": global_terminal_open,
        "explicit_model_gap_dprc_ledger_retained": dprc_model_retained,
        "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved": False,
        "independent_noncanonical_precauchy_arithmetic_identity_statement_proved": False,
        "actual_noncanonical_moving_block_spread_ncb_lk_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": ALPHA_WEIGHT,
        "synchronized_chain": [
            ALPHA_WEIGHT,
            INDEPENDENT_IDENTITY,
            ACTUAL_MOVING,
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ],
        "strict_self_contained_open_basis_after_sync": open_basis,
        "strict_noncanonical_open_basis_with_clean_dls_lane": strict_noncanonical_basis,
        "next_direct_attack_target": GLOBAL_TERMINAL,
        "parallel_attack_targets": [MODEL_LEDGER, WINDOWED_DLS, DSTRUCTURE_GATE],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`AlphaSignedWeightLawFromPreCauchyArithmeticIdentityLedger` 的下游链条已同步："
            "权重律缺口先到独立 pre-Cauchy 恒等式陈述，再到 actual noncanonical moving-block/NC-BLK，"
            "再到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 与 `ExplicitModelGapAndFiniteDPRCLedger`。"
            "因此后续不应再把 weight law、identity 或 NC-BLK 当作新的终端硬点；真正剩余是全局 PDEC-CAP/"
            "内部 CleanKLS 大筛门、模型余量账本，以及独立 DStructure/Rankin 验收门。"
            "本步只关闭路由同步，不给出行/列无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha signed 权重律下游同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"downstream_sync_router_closed={fmt_bool(result['downstream_sync_router_closed'])}",
        (
            "alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved="
            f"{fmt_bool(result['alpha_signed_weight_law_from_precauchy_arithmetic_identity_proved'])}"
        ),
        (
            "actual_noncanonical_moving_block_spread_ncb_lk_proved="
            f"{fmt_bool(result['actual_noncanonical_moving_block_spread_ncb_lk_proved'])}"
        ),
        (
            "pdec_cap_or_internal_clean_kls_large_sieve_proved="
            f"{fmt_bool(result['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}"
        ),
        (
            "explicit_model_gap_and_finite_dprc_ledger_proved="
            f"{fmt_bool(result['explicit_model_gap_and_finite_dprc_ledger_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "```text",
    ]
    lines.extend(result["synchronized_chain"])
    lines.extend(
        [
            "```",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
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
            "## 3. 同步后开放基",
            "",
            "```text",
            result["strict_self_contained_open_basis_after_sync"],
            "```",
            "",
            "保留 clean DLS 侧线时：",
            "",
            "```text",
            result["strict_noncanonical_open_basis_with_clean_dls_lane"],
            "```",
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
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
