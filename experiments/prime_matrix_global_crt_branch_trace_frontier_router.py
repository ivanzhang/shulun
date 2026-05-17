#!/usr/bin/env python3
"""生成 global CRT 到 atomic branch trace 前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_global_crt_branch_trace_frontier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.json

输出：
  data/prime-matrix-global-crt-branch-trace-frontier-ledger.json
  docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.json
  docs/monograph/prime-matrix-global-crt-branch-trace-frontier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-global-crt-branch-trace-frontier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-global-crt-branch-trace-frontier-router.json"
OUT_MD = DOCS / "prime-matrix-global-crt-branch-trace-frontier-router.md"

GLOBAL_SATURATION = "prime-matrix-global-crt-terminal-saturation-sync-router.json"
PDEC_SCOPE = "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
DIRECT_PDEC = "prime-matrix-strict-direct-acyclic-same-set-pdec-dual-router.json"
NEW_JOINT_OBLIGATION = "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"
ANTISPLIT = "prime-matrix-strict-new-joint-formula-antisplit-atom-router.json"
ANTISPLIT_DECL = "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"
ATOMIC_PAIRING = "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
BUILTIN_PAIRING = "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"

PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
ANTISPLIT_ATOM = "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection"
ATOMIC_DECL = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING_ATOM = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
EXACT_UV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    GLOBAL_SATURATION,
    PDEC_SCOPE,
    DIRECT_PDEC,
    NEW_JOINT_OBLIGATION,
    ANTISPLIT,
    ANTISPLIT_DECL,
    ATOMIC_PAIRING,
    BUILTIN_PAIRING,
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记证据哈希。"""
    result: dict[str, str] = {}
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


def sync_chain() -> list[dict[str, str]]:
    """列出从上一活动基到 branch trace 的同步链。"""
    return [
        {"from": "global CRT terminal saturation basis", "to": f"{PDEC_SCOPE_ATOM} OR {NEW_JOINT}"},
        {"from": NEW_JOINT, "to": ANTISPLIT_ATOM},
        {"from": ANTISPLIT_ATOM, "to": ATOMIC_DECL},
        {"from": ATOMIC_DECL, "to": BUILTIN_PAIRING_ATOM},
        {"from": BUILTIN_PAIRING_ATOM, "to": BRANCH_TRACE},
    ]


def build_result() -> dict[str, Any]:
    """构造 branch trace 前沿同步证书。"""
    global_saturation = load_json(GLOBAL_SATURATION)
    pdec_scope = load_json(PDEC_SCOPE)
    direct_pdec = load_json(DIRECT_PDEC)
    new_joint = load_json(NEW_JOINT_OBLIGATION)
    antisplit = load_json(ANTISPLIT)
    antisplit_decl = load_json(ANTISPLIT_DECL)
    atomic_pairing = load_json(ATOMIC_PAIRING)
    builtin_pairing = load_json(BUILTIN_PAIRING)

    global_basis_imported = (
        global_saturation.get("next_direct_attack_target")
        == f"{PDEC_SCOPE_ATOM}_OR_{NEW_JOINT}"
        and global_saturation.get("row_column_unconditional_closed") is False
    )
    pdec_scope_open = (
        pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
        and pdec_scope.get("pdec_scope_proved") is False
        and direct_pdec.get("acyclic_same_set_scope_match_proved") is False
    )
    new_joint_active = (
        new_joint.get("new_joint_formula_is_current_internal_noncycle_target") is True
        and new_joint.get("new_explicit_joint_constructor_formula_artifact_present") is False
    )
    antisplit_reduced = (
        antisplit.get("next_direct_attack_target") == ANTISPLIT_ATOM
        and antisplit.get("antisplit_joint_formula_proved") is False
    )
    atomic_decl_reduced = (
        antisplit_decl.get("next_direct_attack_target") == ATOMIC_DECL
        and antisplit_decl.get("atomic_antisplit_declaration_proved") is False
    )
    builtin_pairing_reduced = (
        atomic_pairing.get("next_direct_attack_target") == BUILTIN_PAIRING_ATOM
        and atomic_pairing.get("builtin_signed_coefficient_pairing_proved") is False
    )
    branch_trace_reduced = (
        builtin_pairing.get("next_direct_attack_target") == BRANCH_TRACE
        and builtin_pairing.get("exact_atomic_joint_branch_trace_signed_coefficient_formula_proved")
        is False
    )

    rows = [
        row(
            "GlobalCRTTerminalSaturationImported",
            global_basis_imported,
            False,
            "上一层已把 Q1/Q2-CRT 路线同步到 PDEC 作用域匹配或新 joint 公式二选一。",
            f"{PDEC_SCOPE_ATOM} OR {NEW_JOINT}",
        ),
        row(
            "PDECScopeBranchStillExternalOrNewCertificate",
            pdec_scope_open,
            False,
            "PDEC same-set 作用域分支在当前内部语料中已饱和；仍可作为新 scope 证书输入，但当前未证。",
            PDEC_SCOPE_ATOM,
        ),
        row(
            "NewJointFormulaTerminalObligationImported",
            new_joint_active,
            False,
            "没有新 joint 公式时，旧 declaration/alpha-side/same-row 路线回到 signed-source 固定点。",
            NEW_JOINT,
        ),
        row(
            "NewJointReducedToAntiSplitFormula",
            antisplit_reduced,
            False,
            "新公式若沿旧 alpha-side 分裂路线展开就回到来源环；真正剩余是反分裂同排公式。",
            ANTISPLIT_ATOM,
        ),
        row(
            "AntiSplitReducedToAtomicDeclaration",
            atomic_decl_reduced,
            False,
            "普通 declaration line 仍会降解到旧分裂循环；必须要原子 joint rows 声明。",
            ATOMIC_DECL,
        ),
        row(
            "AtomicDeclarationReducedToBuiltinPairing",
            builtin_pairing_reduced,
            False,
            "unsigned skeleton 已闭合；真正缺口是每条 atomic row 的内置 signed coefficient/pairing 闭式。",
            BUILTIN_PAIRING_ATOM,
        ),
        row(
            "BuiltinPairingReducedToExactBranchTrace",
            branch_trace_reduced,
            False,
            "signed coefficient 是取向/local factor 敏感数据；必须给出 Cauchy 前 exact atomic branch trace。",
            BRANCH_TRACE,
        ),
        row(
            "BranchTraceCurrentCorpusProved",
            False,
            False,
            "当前没有每条 atomic joint row 的 exact branch trace signed coefficient 公式。",
            BRANCH_TRACE,
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "本证书只把二选一活动基进一步压到 PDEC scope 或 branch trace；未产生全局无条件终端矛盾。",
            f"({PDEC_SCOPE_ATOM} OR {BRANCH_TRACE}) AND {EXACT_UV} AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]

    latest_basis = (
        f"({PDEC_SCOPE_ATOM} OR {BRANCH_TRACE}) AND {EXACT_UV} "
        f"AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"
    )

    return {
        "certificate_type": "prime_matrix_global_crt_branch_trace_frontier_router",
        "status": "global_crt_latest_frontier_reduced_to_pdec_scope_or_atomic_branch_trace_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "global_crt_terminal_saturation_imported": global_basis_imported,
        "pdec_scope_branch_still_open": pdec_scope_open,
        "new_joint_formula_terminal_obligation_imported": new_joint_active,
        "new_joint_reduced_to_antisplit_formula": antisplit_reduced,
        "antisplit_reduced_to_atomic_declaration": atomic_decl_reduced,
        "atomic_declaration_reduced_to_builtin_pairing": builtin_pairing_reduced,
        "builtin_pairing_reduced_to_exact_branch_trace": branch_trace_reduced,
        "acyclic_same_set_scope_match_proved": False,
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": f"{PDEC_SCOPE_ATOM} OR {NEW_JOINT}",
        "terminal_gap_after_router": latest_basis,
        "next_direct_attack_target": f"{PDEC_SCOPE_ATOM}_OR_{BRANCH_TRACE}",
        "latest_strict_activity_basis": latest_basis,
        "sync_chain": sync_chain(),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "最新 global CRT 活动基继续收窄：PDEC same-set 作用域匹配仍可作为独立新证书输入，"
            "但当前未证；另一侧 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 已经被压成"
            "`ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn`。这要求对每条 atomic joint row "
            "在同一 formal unit 和 Cauchy/Phi/payment 前给出完整 branch trace，同时输出 basis word、"
            "signed coefficient、alpha/delta pairing、orientation/local factor、exact UV 与回流。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix global CRT branch trace 前沿路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"global_crt_terminal_saturation_imported={fmt_bool(result['global_crt_terminal_saturation_imported'])}",
        f"pdec_scope_branch_still_open={fmt_bool(result['pdec_scope_branch_still_open'])}",
        f"new_joint_formula_terminal_obligation_imported={fmt_bool(result['new_joint_formula_terminal_obligation_imported'])}",
        f"new_joint_reduced_to_antisplit_formula={fmt_bool(result['new_joint_reduced_to_antisplit_formula'])}",
        f"antisplit_reduced_to_atomic_declaration={fmt_bool(result['antisplit_reduced_to_atomic_declaration'])}",
        f"atomic_declaration_reduced_to_builtin_pairing={fmt_bool(result['atomic_declaration_reduced_to_builtin_pairing'])}",
        f"builtin_pairing_reduced_to_exact_branch_trace={fmt_bool(result['builtin_pairing_reduced_to_exact_branch_trace'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(result['acyclic_same_set_scope_match_proved'])}",
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved="
        f"{fmt_bool(result['exact_atomic_joint_branch_trace_signed_coefficient_formula_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["sync_chain"]:
        lines.append(f"| `{table_cell(item['from'])}` | `{table_cell(item['to'])}` |")
    lines += [
        "",
        "## 2. 判定表",
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
        "## 3. 最新严格活动基",
        "",
        "```text",
        result["latest_strict_activity_basis"],
        "```",
        "",
        "下一直接主攻：",
        "",
        "```text",
        result["next_direct_attack_target"],
        "```",
        "",
        "审稿边界：本文件只完成当前活动基的前沿压缩；它没有证明 PDEC 作用域匹配，",
        "没有给出 exact atomic branch trace，也没有关闭 ExactUV、模型余量、RatePreservation 或 DStructure/Rankin。",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in result["source_hashes"].items():
        lines.append(f"| `{name}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出同步证书。"""
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
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
