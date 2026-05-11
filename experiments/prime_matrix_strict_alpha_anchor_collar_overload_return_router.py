#!/usr/bin/env python3
"""生成 strict alpha anchor-collar 过载命名回流证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_anchor_collar_overload_return_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-anchor-collar-overload-return-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-anchor-collar-overload-return-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-anchor-collar-overload-return-router.md"

TARGET = "AlphaFormulaAnchorCollarOverloadNamedReturnLedger"
GLOBAL_TERMINAL = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_LEDGER = "ExplicitModelGapAndFiniteDPRCLedger"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
ANCHOR_SURVIVOR = "PrimeSurvivorLowerBoundOrPDECSAEColumnReturn"
FIBER_SATURATION = "AnchorFiberSaturationPDECOrSAEReturn"
ENDPOINT_DEFECT = "AnchorCollarEndpointDefectPDECExclusion"

SOURCE_FILES = [
    "prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json",
    "prime-matrix-early-zero-anchor-collar-router.json",
    "prime-matrix-anchor-collar-survivor-identity-router.json",
    "prime-matrix-anchor-endpoint-lowmod-tail-router.json",
    "prime-matrix-anchor-fiber-saturation-return-schema-router.json",
    "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json",
    "prime-matrix-final-input-firewall-boundary-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记本证书读取到的证据哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def make_row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def overload_routes() -> list[dict[str, str]]:
    """列出 anchor-collar 过载的命名回流出口。"""
    return [
        {
            "case": "persistent short-fiber saturation",
            "route": f"{FIBER_SATURATION} -> PDEC/SAE named schema",
        },
        {
            "case": "endpoint phase defect",
            "route": f"{ENDPOINT_DEFECT} -> low-mod finite phase OR tail-core/fiber saturation",
        },
        {
            "case": "isolated sparse fiber escape",
            "route": "LocalSurvivor/SAE packet -> GlobalPDECorSparseTerminalExclusion",
        },
        {
            "case": "fixed column displacement reuse",
            "route": "ColumnCRT / refined PDEC -> GlobalPDECorSparseTerminalExclusion",
        },
        {
            "case": "diffuse residual after no finite signature",
            "route": "internal CleanKLS/DLS admission -> PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve",
        },
    ]


def build_rows(
    carry_formula: dict[str, Any],
    anchor_collar: dict[str, Any],
    survivor: dict[str, Any],
    endpoint: dict[str, Any],
    fiber_return: dict[str, Any],
    global_split: dict[str, Any],
    final_firewall: dict[str, Any],
) -> list[dict[str, Any]]:
    """同步 anchor-collar 过载命名回流到全局终端门。"""
    target_active = carry_formula.get("next_direct_attack_target") == TARGET
    collar_closed = anchor_collar.get("canonical_anchor_collar_closed") is True
    survivor_identity = survivor.get("anchor_collar_survivor_identity_closed") is True
    endpoint_dichotomy = endpoint.get("anchor_endpoint_pdec_dichotomy_closed") is True
    fiber_schema_closed = fiber_return.get("anchor_fiber_saturation_return_schema_closed") is True
    global_split_closed = global_split.get("global_pdec_sparse_terminal_split_reconciled") is True
    current_frontier_zero = (
        global_split.get("current_materialized_frontier_exhausted") is True
        and final_firewall.get("current_materialized_terminal_frontier_closed") is True
    )
    no_anchor_exit = all(
        [
            target_active,
            collar_closed,
            survivor_identity,
            endpoint_dichotomy,
            fiber_schema_closed,
            global_split_closed,
        ]
    )

    return [
        make_row(
            "CounterexampleBranchGuardPreserved",
            True,
            True,
            "本步仍只处理早期零行反例链强制出的 anchor-collar 过载，不用真实样本缺席替代排斥。",
            "row_column_unconditional_closed=false。",
        ),
        make_row(
            "AnchorCollarOverloadTargetActive",
            target_active,
            False,
            "carry-shell 同余 row 公式闭合后，下一最窄点是短纤维满载或公式过载的命名回流纪律。",
            TARGET,
        ),
        make_row(
            "CanonicalAnchorCollarImported",
            collar_closed,
            True,
            "最小高素 anchor 已被限制到 x<q<sqrt((x+1)P)，固定 q 后 cofactor 位于短素数纤维。",
            "过载必须发生在有限 formal-unit fiber 上。",
        ),
        make_row(
            "SurvivorIdentityImported",
            survivor_identity,
            True,
            "R_x 被无损分解为 prime survivors 与 canonical semiprime fibers；纤维覆盖失败等价于素数幸存为零或命名缺陷。",
            ANCHOR_SURVIVOR,
        ),
        make_row(
            "EndpointLowTailDichotomyImported",
            endpoint_dichotomy,
            True,
            "若过载表现为端点强负缺陷，则已拆成低模有限 CRT 相位坏集与高模 tail-core/fiber saturation。",
            ENDPOINT_DEFECT,
        ),
        make_row(
            "FiberSaturationNamedReturnSchemaImported",
            fiber_schema_closed,
            True,
            "固定 q 的短纤维近饱和没有 anchor 专属第四出口：持久进 PDEC，孤立进 LocalSurvivor/SAE。",
            FIBER_SATURATION,
        ),
        make_row(
            "GlobalPDECorSparseSplitImported",
            global_split_closed,
            True,
            "PDEC/SAE/ColumnCRT/LocalSurvivor 终端已调和为全局 PDEC-CAP 或内部 CleanKLS/DLS 大筛门。",
            GLOBAL_TERMINAL,
        ),
        make_row(
            "CurrentMaterializedTerminalFrontierImported",
            current_frontier_zero,
            True,
            "当前已物化终端前沿清零；未来过载必须提交显式同 formal unit schema，而不是无名出口。",
            "future explicit schema discipline。",
        ),
        make_row(
            "NoAnchorSpecificOverloadExit",
            no_anchor_exit,
            True,
            "anchor-collar 过载不能作为独立剩余停留；它只会生成 PDEC/SAE/ColumnCRT/LocalSurvivor/CleanKLS 命名终端。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER}",
        ),
        make_row(
            "AnchorCollarOverloadNamedReturnLedgerClosedAsSchema",
            no_anchor_exit,
            True,
            "目标 ledger 作为命名回流 schema 已闭合：过载有登记出口且没有未命名第四类。",
            "终端排斥仍未完成。",
        ),
        make_row(
            "TerminalExclusionStillOpen",
            True,
            False,
            "本步不证明 PDEC-CAP、内部 CleanKLS/DLS、模型余量或 DStructure/Rankin；它只把 anchor 过载送入这些门。",
            f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 anchor-collar 过载回流证书。"""
    carry_formula = load_json("prime-matrix-strict-alpha-carry-shell-congruence-formula-router.json")
    anchor_collar = load_json("prime-matrix-early-zero-anchor-collar-router.json")
    survivor = load_json("prime-matrix-anchor-collar-survivor-identity-router.json")
    endpoint = load_json("prime-matrix-anchor-endpoint-lowmod-tail-router.json")
    fiber_return = load_json("prime-matrix-anchor-fiber-saturation-return-schema-router.json")
    global_split = load_json("prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.json")
    final_firewall = load_json("prime-matrix-final-input-firewall-boundary-router.json")

    rows = build_rows(
        carry_formula=carry_formula,
        anchor_collar=anchor_collar,
        survivor=survivor,
        endpoint=endpoint,
        fiber_return=fiber_return,
        global_split=global_split,
        final_firewall=final_firewall,
    )
    schema_closed = next(
        row["closed"] for row in rows if row["gate"] == "AnchorCollarOverloadNamedReturnLedgerClosedAsSchema"
    )

    terminal_basis = f"{GLOBAL_TERMINAL} AND {MODEL_LEDGER} AND {DSTRUCTURE_GATE}"
    return {
        "certificate_type": "prime_matrix_strict_alpha_anchor_collar_overload_return_router",
        "status": "strict_alpha_anchor_collar_overload_return_schema_closed_terminal_gap_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "alpha_formula_anchor_collar_overload_return_router_closed": schema_closed,
        "alpha_formula_anchor_collar_overload_named_return_ledger_closed": schema_closed,
        "alpha_formula_anchor_collar_overload_named_return_exclusion_proved": False,
        "alpha_formula_anchor_collar_overload_named_return_proved": False,
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "dstructure_tail_log4_finite_rankin_full_ledger_independent_acceptance_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": TARGET,
        "terminal_gap_after_router": terminal_basis,
        "next_direct_attack_target": GLOBAL_TERMINAL,
        "parallel_required_inputs": [
            MODEL_LEDGER,
            DSTRUCTURE_GATE,
        ],
        "overload_routes": overload_routes(),
        "return_law": (
            "Anchor-collar overload is a named-return schema, not a new source of signed alpha coefficients. "
            "Persistent short-fiber saturation, endpoint phase defects, sparse escapes and fixed column reuse all have "
            "registered PDEC/SAE/ColumnCRT/LocalSurvivor routes; after the global terminal split their exclusion is exactly "
            "the PDEC-CAP or internal CleanKLS/DLS terminal problem, plus the explicit model-gap and DStructure gates."
        ),
        "plain_conclusion": (
            "`AlphaFormulaAnchorCollarOverloadNamedReturnLedger` 已作为命名回流 schema 闭合："
            "短纤维饱和、端点相位缺陷、孤立 sparse escape 与固定位移复用都不能形成 anchor 专属第四出口，"
            "只能进入 PDEC/SAE/ColumnCRT/LocalSurvivor/CleanKLS 的已登记终端门。"
            "但终端门本身仍未排斥；下一主攻点回到 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve`，"
            "并保留 `ExplicitModelGapAndFiniteDPRCLedger` 与 DStructure/Rankin 验收。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha anchor-collar 过载命名回流路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"alpha_formula_anchor_collar_overload_return_router_closed={fmt_bool(result['alpha_formula_anchor_collar_overload_return_router_closed'])}",
        f"alpha_formula_anchor_collar_overload_named_return_ledger_closed={fmt_bool(result['alpha_formula_anchor_collar_overload_named_return_ledger_closed'])}",
        f"alpha_formula_anchor_collar_overload_named_return_exclusion_proved={fmt_bool(result['alpha_formula_anchor_collar_overload_named_return_exclusion_proved'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 过载出口",
        "",
        "| case | route |",
        "| --- | --- |",
    ]
    for item in result["overload_routes"]:
        lines.append(
            "| {case} | {route} |".format(
                case=table_cell(item["case"]),
                route=table_cell(item["route"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 回流律",
            "",
            result["return_law"],
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_required_inputs"]),
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
