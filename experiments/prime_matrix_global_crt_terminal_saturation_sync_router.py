#!/usr/bin/env python3
"""生成 global CRT 路线到 strict 终端饱和前沿的总同步证书。

用法示例：
  python3 experiments/prime_matrix_global_crt_terminal_saturation_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.json

输出：
  data/prime-matrix-global-crt-terminal-saturation-sync-ledger.json
  docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.json
  docs/monograph/prime-matrix-global-crt-terminal-saturation-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-global-crt-terminal-saturation-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-global-crt-terminal-saturation-sync-router.json"
OUT_MD = DOCS / "prime-matrix-global-crt-terminal-saturation-sync-router.md"

GLOBAL_CRT = "prime-matrix-global-crt-homogeneity-frontier-router.json"
ALPHA_TERMINAL = "prime-matrix-strict-alpha-row-formula-terminal-frontier-sync-router.json"
PDEC_KLS = "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"
KZ_SYNC = "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"
PDEC_SCOPE = "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
NONRECURSIVE = "prime-matrix-strict-nonrecursive-breaker-latest-cycle-sync-router.json"
SEED_SATURATION = "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json"

ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
TERMINAL_GATE = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
KZ_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
PDEC_SCOPE_ATOM = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
RATE_LEDGER = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    GLOBAL_CRT,
    ALPHA_TERMINAL,
    PDEC_KLS,
    KZ_SYNC,
    PDEC_SCOPE,
    NONRECURSIVE,
    SEED_SATURATION,
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失则返回空对象，便于显式暴露同步缺口。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本证书的证据哈希。"""
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


def contains(value: Any, needle: str) -> bool:
    """检查文本字段是否包含目标原子。"""
    return needle in str(value)


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
    """列出从 CRT 前沿到当前 strict 饱和前沿的压缩链。"""
    return [
        {"from": "Q1/Q2 full-wheel endpoint inversion", "to": "pure CRT homogeneity firewall"},
        {"from": "pure CRT homogeneity firewall", "to": ALPHA_ROW},
        {"from": ALPHA_ROW, "to": f"{TERMINAL_GATE} AND {MODEL_LEDGER}"},
        {"from": TERMINAL_GATE, "to": f"{PDEC_SCOPE_ATOM} OR {KZ_DLS}"},
        {"from": KZ_DLS, "to": "strict acyclic terminal family / nonrecursive breaker"},
        {"from": "NonrecursiveActualNoncanonicalPreCauchyConstructorRuleAndSignedLiftPackage", "to": f"AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR {PDEC_SCOPE_ATOM} OR {NEW_JOINT}"},
        {"from": "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput", "to": f"{PDEC_SCOPE_ATOM} OR {NEW_JOINT}"},
    ]


def build_result() -> dict[str, Any]:
    """构造总同步证书。"""
    global_crt = load_json(GLOBAL_CRT)
    alpha_terminal = load_json(ALPHA_TERMINAL)
    pdec_kls = load_json(PDEC_KLS)
    kz_sync = load_json(KZ_SYNC)
    pdec_scope = load_json(PDEC_SCOPE)
    nonrecursive = load_json(NONRECURSIVE)
    seed_saturation = load_json(SEED_SATURATION)

    pure_crt_blocked = (
        global_crt.get("global_crt_homogeneity_blocks_pure_phase_contradiction") is True
        and global_crt.get("pure_finite_crt_global_phase_contradiction_found") is False
    )
    alpha_to_terminal = (
        alpha_terminal.get("alpha_row_formula_local_frontier_synced_to_terminal") is True
        and alpha_terminal.get("next_direct_attack_target") == TERMINAL_GATE
    )
    terminal_split = (
        pdec_kls.get("terminal_split_router_closed") is True
        and pdec_kls.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False
    )
    kz_returns = (
        kz_sync.get("kuznetsov_route_returns_to_terminal_family") is True
        and kz_sync.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False
    )
    pdec_scope_saturated = (
        pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
        and pdec_scope.get("pdec_scope_proved") is False
    )
    nonrecursive_cycle = (
        nonrecursive.get("current_nonrecursive_attack_chain_synced") is True
        and nonrecursive.get("seed_coordinate_source_cycle_detected") is True
        and nonrecursive.get("current_chain_contains_nonproof_cycle") is True
    )
    seed_saturated = (
        seed_saturation.get("seed_cycle_cut_branch_saturated") is True
        and seed_saturation.get("joint_basis_word_coefficient_emitter_proved") is False
    )
    pdec_scope_open = (
        pdec_scope.get("acyclic_same_set_scope_match_proved") is False
        or seed_saturation.get("acyclic_same_set_scope_match_proved") is False
    )
    new_joint_absent = (
        pdec_scope.get("new_explicit_joint_constructor_formula_artifact_present") is False
        and seed_saturation.get("new_explicit_joint_constructor_formula_artifact_present") is False
    )

    rows = [
        row(
            "PureCRTHomogeneityFirewallImported",
            pure_crt_blocked,
            pure_crt_blocked,
            "Q1/Q2 端点反转和有限轮同质删相位已关闭纯 CRT 全局相位矛盾出口。",
            ALPHA_ROW,
        ),
        row(
            "AlphaRowLocalFrontierTerminalSynced",
            alpha_to_terminal,
            False,
            "alpha row 局部几何分支已同步到终端门，signed lift 与 overload 不再构成独立局部出口。",
            f"{TERMINAL_GATE} AND {MODEL_LEDGER}",
        ),
        row(
            "PDECCapCleanKLSTerminalSplitImported",
            terminal_split,
            False,
            "PDEC/CleanKLS 终端门已拆成 PDEC same-set 作用域匹配或自足 Kuznetsov/DLS 手臂。",
            f"{PDEC_SCOPE_ATOM} OR {KZ_DLS}",
        ),
        row(
            "KuznetsovDLSRouteReturnsToTerminalFamily",
            kz_returns,
            False,
            "KZ/DLS 形式层已攻到底；当前内部语料中没有自足 log-saving 定理，路线回到终端家族。",
            "strict acyclic terminal family / nonrecursive breaker",
        ),
        row(
            "PDECScopeBranchSaturated",
            pdec_scope_saturated,
            False,
            "PDEC same-set 作用域分支已按当前内部材料攻到边界；仍可作为新证书输入，但不是已证出口。",
            f"{PDEC_SCOPE_ATOM} OR {NEW_JOINT}",
        ),
        row(
            "NonrecursiveBreakerCycleDetected",
            nonrecursive_cycle,
            False,
            "非递归 constructor/signed-lift 破环包下钻到 signed 坐标-来源闭环；该环不能作为证明。",
            f"AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput OR {PDEC_SCOPE_ATOM} OR {NEW_JOINT}",
        ),
        row(
            "SeedCycleCutBranchSaturated",
            seed_saturated,
            False,
            "seed-cycle-cut 分支已饱和：顺序拆分被排除，联合发射器未证，继续展开回到 row-level 固定点。",
            f"{PDEC_SCOPE_ATOM} OR {NEW_JOINT}",
        ),
        row(
            "PDECScopeStillOpen",
            pdec_scope_open,
            False,
            "direct PDEC 手臂仍缺 acyclic/canonical same-set 作用域匹配；这不是由 CRT 同质性自动给出的。",
            PDEC_SCOPE_ATOM,
        ),
        row(
            "NewExplicitJointFormulaStillAbsent",
            new_joint_absent,
            False,
            "新的显式 joint alpha/delta 构造公式尚未提交；现有展开会回到 signed-source 固定点。",
            NEW_JOINT,
        ),
        row(
            "RowColumnUnconditionalClosureCurrentCorpusProved",
            False,
            False,
            "本证书把 global CRT 路线同步到当前 strict 饱和前沿；仍未给出排除早期零行反例链的终端矛盾。",
            f"({PDEC_SCOPE_ATOM} OR {NEW_JOINT}) AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}",
        ),
    ]

    latest_basis = f"({PDEC_SCOPE_ATOM} OR {NEW_JOINT}) AND {MODEL_LEDGER} AND {RATE_LEDGER} AND {DSTRUCTURE}"

    return {
        "certificate_type": "prime_matrix_global_crt_terminal_saturation_sync_router",
        "status": "global_crt_route_synced_to_pdec_scope_or_new_joint_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "pure_crt_homogeneity_firewall_imported": pure_crt_blocked,
        "alpha_row_local_frontier_terminal_synced": alpha_to_terminal,
        "pdec_cap_clean_kls_terminal_split_imported": terminal_split,
        "kuznetsov_dls_route_returns_to_terminal_family": kz_returns,
        "pdec_scope_branch_saturated": pdec_scope_saturated,
        "nonrecursive_breaker_cycle_detected": nonrecursive_cycle,
        "seed_cycle_cut_branch_saturated": seed_saturated,
        "acyclic_same_set_scope_match_proved": False,
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": ALPHA_ROW,
        "terminal_gap_after_router": latest_basis,
        "next_direct_attack_target": f"{PDEC_SCOPE_ATOM}_OR_{NEW_JOINT}",
        "latest_strict_activity_basis": latest_basis,
        "sync_chain": sync_chain(),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"] or not item["proved"]],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "global CRT/Q1-Q2 路线继续下钻后，不再停在 `AlphaRowAnchorPhaseEmissionFormulaLedger`。"
            "alpha row 局部前沿已同步到终端门，PDEC/CleanKLS 终端门又被当前内部语料攻成饱和循环。"
            "严格自足路线的最新非循环剩余压成 `AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate` "
            "或 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`，并行保留模型余量、RatePreservation "
            "与 DStructure/Rankin。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix global CRT 到终端饱和前沿同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pure_crt_homogeneity_firewall_imported={fmt_bool(result['pure_crt_homogeneity_firewall_imported'])}",
        f"alpha_row_local_frontier_terminal_synced={fmt_bool(result['alpha_row_local_frontier_terminal_synced'])}",
        f"pdec_cap_clean_kls_terminal_split_imported={fmt_bool(result['pdec_cap_clean_kls_terminal_split_imported'])}",
        f"kuznetsov_dls_route_returns_to_terminal_family={fmt_bool(result['kuznetsov_dls_route_returns_to_terminal_family'])}",
        f"pdec_scope_branch_saturated={fmt_bool(result['pdec_scope_branch_saturated'])}",
        f"nonrecursive_breaker_cycle_detected={fmt_bool(result['nonrecursive_breaker_cycle_detected'])}",
        f"seed_cycle_cut_branch_saturated={fmt_bool(result['seed_cycle_cut_branch_saturated'])}",
        f"acyclic_same_set_scope_match_proved={fmt_bool(result['acyclic_same_set_scope_match_proved'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}",
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
        "审稿边界：本文件只同步 global CRT 路线与当前 strict 饱和前沿；它没有证明 PDEC 作用域匹配，",
        "没有提交新的 joint alpha/delta 公式，也没有关闭模型余量、RatePreservation 或 DStructure/Rankin。",
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
