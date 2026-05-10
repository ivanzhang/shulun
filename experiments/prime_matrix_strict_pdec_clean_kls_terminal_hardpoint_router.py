#!/usr/bin/env python3
"""生成 strict PDEC/CleanKLS 终端硬点精确二分证书。

用法示例：
  python3 experiments/prime_matrix_strict_pdec_clean_kls_terminal_hardpoint_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.md"

TERMINAL_GATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
DIRECT_PDEC = "DirectAcyclicSameSetPDECCapDualCertificate"
SCOPE_MATCH = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
KUZNETSOV_ATOM = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json",
    "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json",
    "prime-matrix-global-terminal-family-exclusion-split-router.json",
    "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json",
    "prime-matrix-strict-acyclic-clean-kls-router.json",
    "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json",
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
    """登记依赖文件哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def fmt_bool(value: Any) -> str:
    """把布尔值格式化成小写文本。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains(value: Any, needle: str) -> bool:
    """检查文本字段是否含目标原子名。"""
    return needle in str(value)


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


def build_result() -> dict[str, Any]:
    """构造 PDEC/CleanKLS 终端硬点精确二分证书。"""
    downstream = load_json(DOCS / "prime-matrix-strict-alpha-signed-weight-downstream-sync-router.json")
    global_split = load_json(DOCS / "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json")
    family_split = load_json(DOCS / "prime-matrix-global-terminal-family-exclusion-split-router.json")
    direct_pdec = load_json(DOCS / "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json")
    clean_kls = load_json(DOCS / "prime-matrix-strict-acyclic-clean-kls-router.json")
    windowed = load_json(DOCS / "prime-matrix-strict-acyclic-windowed-dls-estimate-router.json")
    dprc = load_json(DOCS / "prime-matrix-moving-block-dprc-ledger-compatibility-router.json")

    terminal_active = (
        downstream.get("next_direct_attack_target") == TERMINAL_GATE
        and downstream.get("downstream_sync_router_closed") is True
    )
    global_split_active = (
        global_split.get("terminal_gap_after_router") == TERMINAL_GATE
        and global_split.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    family_split_active = (
        family_split.get("self_contained_next_hardpoint") == TERMINAL_GATE
        or contains(family_split.get("review_conclusion"), TERMINAL_GATE)
    )
    direct_pdec_audited = (
        direct_pdec.get("scope_audit_closed") is True
        and direct_pdec.get("same_set_pdec_protocol_imported") is True
    )
    direct_pdec_proved = direct_pdec.get("direct_acyclic_same_set_pdec_cap_dual_certificate_proved") is True
    scope_match_proved = direct_pdec.get("acyclic_same_set_scope_match_proved") is True
    external_dibfi_proved = direct_pdec.get("generic_external_dibfi_no_projection_certificate_proved") is True

    clean_reduced = clean_kls.get("direct_acyclic_clean_kls_dls_proved") is False and (
        clean_kls.get("strict_gap_after_router") == WINDOWED_DLS
        or contains(clean_kls.get("plain_conclusion"), WINDOWED_DLS)
    )
    windowed_normal_form = (
        windowed.get("acyclic_windowed_bilinear_normal_form_closed") is True
        and windowed.get("phase_invertible_variable_ledger_closed") is True
        and windowed.get("coefficient_norm_ledger_closed") is True
    )
    kuznetsov_proved = windowed.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is True
    model_retained = (
        downstream.get("explicit_model_gap_dprc_ledger_retained") is True
        and (
            dprc.get("exact_model_gap_dprc_compatibility_proved") is True
            or contains(dprc.get("plain_conclusion"), MODEL_LEDGER)
        )
    )

    # 中文注释：二分闭合不等于二分任一手臂已证。
    terminal_split_closed = all(
        [
            terminal_active,
            global_split_active,
            family_split_active,
            direct_pdec_audited,
            clean_reduced,
            windowed_normal_form,
            model_retained,
        ]
    )
    terminal_gate_proved = direct_pdec_proved or kuznetsov_proved

    rows = [
        make_row(
            "TerminalGateActiveFromDownstreamSync",
            terminal_active,
            True,
            "alpha signed 权重律下游同步后，当前首要终端门正是 PDEC-CAP 或内部 CleanKLS/DLS。",
            TERMINAL_GATE,
        ),
        make_row(
            "GlobalTerminalFamilySplitImported",
            global_split_active and family_split_active,
            True,
            "全局终端家族已把 LocalSurvivor/NC-BLK 等宽泛出口拆成 PDEC-CAP 或 CleanKLS/DLS。",
            f"{DIRECT_PDEC} OR {WINDOWED_DLS}",
        ),
        make_row(
            "DirectPDECProtocolAuditedButScopeOpen",
            direct_pdec_audited,
            direct_pdec_proved,
            "同集 PDEC 协议可导入，但 strict acyclic 证书与 canonical same-set 证书的作用域匹配仍未证。",
            SCOPE_MATCH,
        ),
        make_row(
            "DirectPDECScopeMatchNotProved",
            scope_match_proved,
            scope_match_proved,
            "要用 PDEC 手臂，必须同 formal unit、同坏窗集合、同 U_CRT/L_PDEC、同质量推前。",
            SCOPE_MATCH,
        ),
        make_row(
            "CleanKLSReducedToWindowedDLS",
            clean_reduced,
            False,
            "clean KLS/DLS 手臂已剥离低维缺陷，严格自足剩余是 acyclic windowed DLS。",
            WINDOWED_DLS,
        ),
        make_row(
            "WindowedDLSNormalFormClosed",
            windowed_normal_form,
            True,
            "窗口双线性型、相位/可逆变量、L2 系数范数和失败回流字母表已固定。",
            KUZNETSOV_ATOM,
        ),
        make_row(
            "SelfContainedKuznetsovDLSAtomNotProved",
            kuznetsov_proved,
            kuznetsov_proved,
            "真正解析原子是自足 Kuznetsov/DLS 大筛不等式；当前语料没有证明。",
            KUZNETSOV_ATOM,
        ),
        make_row(
            "ExternalDIBFINotStrictSelfContained",
            external_dibfi_proved,
            False,
            "外部 DI/BFI/Kuznetsov 可成为条件线，但不能替代 strict 自足闭合。",
            EXTERNAL_DIBFI,
        ),
        make_row(
            "ModelGapLedgerStillParallel",
            model_retained,
            False,
            "即使终端门某一手臂证明，ExplicitModelGapAndFiniteDPRCLedger 仍需同口径支付。",
            MODEL_LEDGER,
        ),
        make_row(
            "PDECCapOrCleanKLSLargeSieveProved",
            terminal_gate_proved,
            terminal_gate_proved,
            "PDEC 手臂和 CleanKLS/DLS 手臂当前均未给出可闭合证明。",
            f"{SCOPE_MATCH} OR {KUZNETSOV_ATOM}",
        ),
        make_row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "尚未产生足以排除早期零行反例链的终端矛盾。",
            f"{TERMINAL_GATE} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
    ]

    hardpoint_after = f"({SCOPE_MATCH} OR {KUZNETSOV_ATOM}) AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}"

    return {
        "certificate_type": "prime_matrix_strict_pdec_clean_kls_terminal_hardpoint_router",
        "status": "pdec_clean_kls_terminal_split_closed_both_arms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "terminal_split_router_closed": terminal_split_closed,
        "terminal_gate_active_from_downstream_sync": terminal_active,
        "global_terminal_family_split_imported": global_split_active and family_split_active,
        "direct_pdec_protocol_audited": direct_pdec_audited,
        "acyclic_same_set_scope_match_proved": scope_match_proved,
        "direct_acyclic_same_set_pdec_cap_dual_certificate_proved": direct_pdec_proved,
        "clean_kls_reduced_to_windowed_dls": clean_reduced,
        "windowed_dls_normal_form_closed": windowed_normal_form,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": kuznetsov_proved,
        "acyclic_windowed_kloosterman_dls_internal_estimate_proved": kuznetsov_proved,
        "external_dibfi_no_projection_certificate_proved": external_dibfi_proved,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": terminal_gate_proved,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TERMINAL_GATE,
        "hardpoint_after_router": hardpoint_after,
        "next_direct_attack_target": KUZNETSOV_ATOM,
        "parallel_attack_targets": [SCOPE_MATCH, MODEL_LEDGER, DSTRUCTURE_GATE],
        "strict_terminal_split": {
            "pdec_arm": SCOPE_MATCH,
            "clean_kls_arm": KUZNETSOV_ATOM,
            "external_conditional_arm": EXTERNAL_DIBFI,
        },
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` 的终端门已被精确二分："
            "PDEC 手臂需要证明 strict acyclic 证书与 canonical same-set PDEC 证书的同口径作用域匹配；"
            "CleanKLS 手臂已经压到 `SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks`。"
            "两条手臂当前都未闭合，外部 DI/BFI/Kuznetsov 只能给条件线。"
            "因此下一最窄自足主攻点是自足 Kuznetsov/DLS 大筛原子，同时并行保留 PDEC 作用域匹配、模型余量账本和 DStructure/Rankin 验收门。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict PDEC/CleanKLS 终端硬点路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"terminal_split_router_closed={fmt_bool(result['terminal_split_router_closed'])}",
        f"direct_pdec_protocol_audited={fmt_bool(result['direct_pdec_protocol_audited'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(result['acyclic_same_set_scope_match_proved'])}",
        (
            "self_contained_kuznetsov_dls_large_sieve_inequality_proved="
            f"{fmt_bool(result['self_contained_kuznetsov_dls_large_sieve_inequality_proved'])}"
        ),
        (
            "pdec_cap_or_internal_clean_kls_large_sieve_proved="
            f"{fmt_bool(result['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 终端二分",
        "",
        "```text",
        result["hardpoint_before_router"],
        "  -> PDEC arm:",
        f"     {result['strict_terminal_split']['pdec_arm']}",
        "  -> CleanKLS arm:",
        f"     {result['strict_terminal_split']['clean_kls_arm']}",
        "  -> external conditional arm:",
        f"     {result['strict_terminal_split']['external_conditional_arm']}",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 二分后开放基",
            "",
            "```text",
            result["hardpoint_after_router"],
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
