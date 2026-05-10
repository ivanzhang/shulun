#!/usr/bin/env python3
"""生成 strict direct acyclic 同集 PDEC 对偶作用域匹配路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_direct_acyclic_same_set_pdec_dual_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"
OUT_MD = DOCS / "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.md"

NAMED_DEDUCTION = DOCS / "prime-matrix-strict-named-return-same-parameter-deduction-router.json"
TERMINAL_FAMILY = DOCS / "prime-matrix-strict-acyclic-terminal-family-attack-router.json"
CANONICAL_LOCK = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
PDEC_GLOBAL = DOCS / "prime-matrix-pdec-cap-same-set-global-dual-router.json"
CLEAN_KLS = DOCS / "prime-matrix-strict-acyclic-clean-kls-router.json"

SOURCE_FILES = [NAMED_DEDUCTION, TERMINAL_FAMILY, CANONICAL_LOCK, PDEC_GLOBAL, CLEAN_KLS]

DIRECT_PDEC = "DirectAcyclicSameSetPDECCapDualCertificate"
CANONICAL_SCOPE = "AcyclicCanonicalExactSameSetPromotionCertificate"
CANONICAL_LOCK_ATOM = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
WINDOWED_DLS = "AcyclicWindowedKloostermanDLSInternalEstimate"
DIRECT_CLEAN = "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
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


def build_result() -> dict[str, Any]:
    """构造 strict direct acyclic 同集 PDEC 对偶路由证书。"""
    named = load_json(NAMED_DEDUCTION)
    terminal = load_json(TERMINAL_FAMILY)
    canonical = load_json(CANONICAL_LOCK)
    pdec = load_json(PDEC_GLOBAL)
    clean = load_json(CLEAN_KLS)

    guard = (
        named.get("counterexample_assumption_only") is True
        and named.get("empirical_absence_not_used") is True
        and named.get("row_column_unconditional_closed") is False
    )
    direct_active = named.get("next_direct_attack_target") == DIRECT_PDEC
    same_set_protocol = any(
        item.get("gate") == "SameSetPDECProtocolRegistered" and item.get("closed") is True
        for item in pdec.get("rows", [])
    )
    current_materialized_closed = pdec.get("closed_current_materialized_pdec_gates") is True
    canonical_source_closed = pdec.get("canonical_source_self_contained_pdec_cap_closed") is True
    canonical_lock_proved = terminal.get("acyclic_terminal_canonical_lock_proved") is True
    exact_canonical_certificate = canonical.get("acyclic_canonical_exact_same_set_promotion_certificate_proved") is True
    direct_clean_reduced = clean.get("direct_acyclic_clean_kls_dls_proved") is True
    external_dibfi_open = DIBFI in str(pdec.get("narrowest_next_hardpoint", ""))

    # 中文注释：同集对偶协议可导入；strict acyclic 作用域匹配仍未证明。
    scope_audit_closed = all(
        [guard, direct_active, same_set_protocol, current_materialized_closed, canonical_source_closed]
    )
    direct_pdec_proved = canonical_lock_proved or exact_canonical_certificate
    row_column_closed = False

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在早期零行反例链的 strict acyclic 终端门内做作用域匹配。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "DirectAcyclicSameSetPDECActive",
            direct_active,
            False,
            "上一层把 E_named 持久部分的首攻点压成 direct acyclic same-set PDEC 对偶。",
            DIRECT_PDEC,
        ),
        row(
            "SameSetPDECProtocolImported",
            same_set_protocol,
            True,
            "同集 PDEC 比较必须作用在同一坏窗推前计数；失败要输出 DualCap 或缺失行。",
            "U_CRT<L_PDEC protocol.",
        ),
        row(
            "CurrentMaterializedPDECFrontierRouted",
            current_materialized_closed,
            True,
            "当前已物化的 canonical/source PDEC 中间门均已路由，不再是无名 Fourier 常数搜索。",
            "strict acyclic scope still required.",
        ),
        row(
            "CanonicalSourceSameSetClosedButScoped",
            canonical_source_closed,
            True,
            "canonical-source 口径下的同集 PDEC-CAP 可用，但不能自动导入 acyclic noncanonical 分支。",
            CANONICAL_SCOPE,
        ),
        row(
            "AcyclicSameSetScopeMatchProved",
            canonical_lock_proved or exact_canonical_certificate,
            canonical_lock_proved or exact_canonical_certificate,
            "若要调用 canonical same-set 对偶，必须证明 acyclic 终端证书同 formal unit、同坏窗集合、同 U_CRT/L_PDEC 推前。",
            CANONICAL_LOCK_ATOM,
        ),
        row(
            "GenericExternalDIBFIRemainsExternal",
            not external_dibfi_open,
            False,
            "不经 canonical scope 的 generic/external 同集路线仍缺 DI/BFI 无投影窗口量化证书。",
            DIBFI,
        ),
        row(
            "DirectCleanFallbackNotClosed",
            direct_clean_reduced,
            direct_clean_reduced,
            "若 direct PDEC 作用域不匹配，fallback 是 acyclic clean KLS/DLS；当前也尚未自足证明。",
            WINDOWED_DLS,
        ),
        row(
            "DirectAcyclicSameSetPDECCapDualCertificateProved",
            direct_pdec_proved,
            direct_pdec_proved,
            "direct acyclic PDEC 不是已闭合定理；它已压成同集作用域匹配或外部 DI/BFI 证书。",
            f"{CANONICAL_LOCK_ATOM} OR {DIBFI}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            row_column_closed,
            row_column_closed,
            "尚未得到反例链与真实结构链的无条件终端矛盾。",
            f"{CANONICAL_LOCK_ATOM} OR {WINDOWED_DLS} OR {DIBFI} OR {DSTRUCTURE}",
        ),
    ]

    hardpoint_after = f"{CANONICAL_LOCK_ATOM} OR {WINDOWED_DLS} OR {DIBFI}"

    return {
        "certificate_type": "prime_matrix_strict_direct_acyclic_same_set_pdec_dual_router",
        "status": "direct_acyclic_same_set_pdec_scope_audited_scope_match_or_external_dibfi_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "direct_acyclic_same_set_pdec_active": direct_active,
        "same_set_pdec_protocol_imported": same_set_protocol,
        "current_materialized_pdec_frontier_routed": current_materialized_closed,
        "canonical_source_same_set_pdec_closed_but_scoped": canonical_source_closed,
        "scope_audit_closed": scope_audit_closed,
        "acyclic_same_set_scope_match_proved": canonical_lock_proved or exact_canonical_certificate,
        "generic_external_dibfi_no_projection_certificate_proved": False,
        "direct_acyclic_clean_kls_dls_proved": direct_clean_reduced,
        "direct_acyclic_same_set_pdec_cap_dual_certificate_proved": direct_pdec_proved,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": DIRECT_PDEC,
        "hardpoint_after_router": hardpoint_after,
        "next_direct_attack_target": CANONICAL_LOCK_ATOM,
        "parallel_attack_targets": [WINDOWED_DLS, DIBFI, DSTRUCTURE],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`DirectAcyclicSameSetPDECCapDualCertificate` 已完成作用域匹配审查。"
            "已有 same-set PDEC 协议和 canonical-source 同集前沿可导入为工具，但 strict acyclic 分支不能自动调用；"
            "必须先证明 acyclic 终端证书与 canonical same-set 证书在 formal unit、坏窗集合、U_CRT、L_PDEC 和质量推前上完全同口径。"
            "若不能证明该作用域匹配，剩余只能走 acyclic windowed DLS/CleanKLS 或外部 DIBFI 无投影窗口证书。"
            "因此 direct PDEC 本轮未闭合，下一最窄点回到 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary`。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict direct acyclic 同集 PDEC 对偶路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"scope_audit_closed={fmt_bool(result['scope_audit_closed'])}",
        f"same_set_pdec_protocol_imported={fmt_bool(result['same_set_pdec_protocol_imported'])}",
        (
            "canonical_source_same_set_pdec_closed_but_scoped="
            f"{fmt_bool(result['canonical_source_same_set_pdec_closed_but_scoped'])}"
        ),
        f"acyclic_same_set_scope_match_proved={fmt_bool(result['acyclic_same_set_scope_match_proved'])}",
        (
            "direct_acyclic_same_set_pdec_cap_dual_certificate_proved="
            f"{fmt_bool(result['direct_acyclic_same_set_pdec_cap_dual_certificate_proved'])}"
        ),
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(item['gate'])}`",
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
            "## 2. 下一真正最窄点",
            "",
            "首攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " OR ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本文件只完成 direct PDEC 的作用域匹配审查；它没有证明 strict acyclic same-set PDEC 对偶，也没有升级行/列命题为无条件定理。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """命令行入口。"""
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
