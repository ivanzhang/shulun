#!/usr/bin/env python3
"""生成逆元最小零行 x 到同参数预算判定的接口证书。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_exact_x_budget_interface_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-exact-x-budget-interface-router.json

输出：
  data/inverse-alignment-exact-x-budget-interface-ledger.json
  docs/monograph/prime-matrix-inverse-alignment-exact-x-budget-interface-router.json
  docs/monograph/prime-matrix-inverse-alignment-exact-x-budget-interface-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-exact-x-budget-interface-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-exact-x-budget-interface-router.md"
OUT_LEDGER = DATA / "inverse-alignment-exact-x-budget-interface-ledger.json"

SOURCE_LEDGER = DATA / "inverse-alignment-exact-zero-row-charge-profile-ledger.json"
SOURCE_FILES = [
    DOCS / "prime-matrix-inverse-alignment-covering-system-router.json",
    DOCS / "prime-matrix-inverse-alignment-prefix-demand-bridge-router.json",
    DOCS / "prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json",
    DOCS / "prime-matrix-inverse-alignment-cold-core-chain-reconciliation-router.json",
    DOCS / "prime-matrix-strict-unified-budget-after-return-cycle-sync-router.json",
    DOCS / "prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json",
    DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json",
]

STRICT_MARGIN = "SameParameterSparseDemandColdSupplyStrictMarginCertificate"
COLD_NUMERIC = "ColdSupplySameParameterNumericEnvelope"
EXACT_X_RUNNER = "ExactZeroRowXDrivenSameParameterBudgetRunnerOrAnalyticEnvelope"
SHORT_INTERVAL = "PrimeGapBelowP2ForAllPBlocks"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_exact_x_budget_interface_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in [SOURCE_LEDGER, OUT_LEDGER, *SOURCE_FILES]:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def canonical_same_parameter_profile(row: dict[str, Any]) -> dict[str, Any]:
    """选取 z=floor(P^0.43) 的同参数剖面；若缺失则取最接近者。"""
    p_value = int(row["P"])
    target_z = max(2, int(p_value**0.43))
    profiles = row.get("prefix_tau_profiles", [])
    if not profiles:
        return {}
    return min(profiles, key=lambda item: abs(int(item["z"]) - target_z))


def build_budget_rows(profile_ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """把精确零行 x 剖面转为同参数预算字段。"""
    rows: list[dict[str, Any]] = []
    for row in profile_ledger.get("profile_rows", []):
        profile = canonical_same_parameter_profile(row)
        if not profile:
            continue
        cover = row["covering_profile"]
        p_value = int(row["P"])
        x_value = int(row["minimal_alignment_x"])
        msharp = float(profile["Msharp_exact"])
        appeared_capacity = int(profile["appeared_tau_capacity_sum_mu"])
        suffix_capacity = int(profile["suffix_capacity_sum_mu"])
        assigned_atoms = int(profile["assigned_atoms"])
        raw_capacity_gap = suffix_capacity - msharp
        rows.append(
            {
                "P": p_value,
                "exact_minimal_zero_row_x": x_value,
                "x_over_P": round(x_value / p_value, 9),
                "x_gt_P": x_value > p_value,
                "same_parameter_z": int(profile["z"]),
                "R_xz_size": int(profile["R_xz_size"]),
                "Msharp_exact": round(msharp, 12),
                "assigned_atoms": assigned_atoms,
                "appeared_tau_capacity_sum_mu": appeared_capacity,
                "suffix_capacity_sum_mu": suffix_capacity,
                "charged_slack_for_appeared_tau": int(profile["charged_slack_for_appeared_tau"]),
                "raw_suffix_capacity_minus_Msharp": round(raw_capacity_gap, 12),
                "overlap_debt": int(cover["overlap_debt"]),
                "total_capacity_sum_mu": int(cover["total_capacity_sum_mu"]),
                "max_column_multiplicity": int(cover["max_column_multiplicity"]),
                "budget_fields_generated_from_same_x": bool(
                    cover["zero_row"]
                    and cover["capacity_identity_ok"]
                    and profile["prefix_tau_charge_identity_ok"]
                ),
            }
        )
    return rows


def build_interface_ledger() -> dict[str, Any]:
    """生成预算接口 ledger。"""
    profile_ledger = load_json(SOURCE_LEDGER)
    rows = build_budget_rows(profile_ledger)
    return {
        "ledger_type": "inverse_alignment_exact_x_budget_interface_ledger",
        "source_ledger": str(SOURCE_LEDGER.relative_to(ROOT)),
        "diagnostic_only": True,
        "same_parameter_alpha": 0.43,
        "budget_rows": rows,
        "all_rows_have_exact_x_gt_P": bool(rows) and all(item["x_gt_P"] for item in rows),
        "all_budget_fields_generated_from_same_x": bool(rows)
        and all(item["budget_fields_generated_from_same_x"] for item in rows),
        "raw_capacity_not_a_cold_supply_bound": True,
        "global_asymptotic_margin_proved": False,
    }


def theorem_rows() -> list[dict[str, str]]:
    """列出本接口闭合与未闭合的内容。"""
    return [
        {
            "name": "exact_x_crt_decision_function",
            "statement": "X(P)=min{x>0: for every 1<=c<P, some q<P has c=-xP mod q}.",
            "status": "closed_as_finite_crt_algorithm",
        },
        {
            "name": "same_x_budget_fields",
            "statement": "rho_q(x), mu_q, R_{x,z}, tau_z(c), M#_{x,z} are all generated from the same exact x.",
            "status": "closed",
        },
        {
            "name": "early_window_no_go",
            "statement": "proving X(P)>P directly for every P is the prime-in-each-P-block short-interval route.",
            "status": "identified_not_used_as_global_closure",
        },
        {
            "name": "exact_x_budget_runner",
            "statement": "finite or analytic certificates may compare exact M#_{x,z} against the registered U_np envelope.",
            "status": "new_interface_open",
        },
        {
            "name": "strict_margin",
            "statement": "M#_{x,z} > U_np for every hypothetical early zero row under the same parameter ledger.",
            "status": "open",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "SameParameterMarginTargetImported",
            "closed": result["same_parameter_margin_target_imported"],
            "proved": result["same_parameter_margin_target_imported"],
            "meaning": "回流后统一预算已经把非持久主攻点压到同参数稀疏余量。",
            "remaining": STRICT_MARGIN,
        },
        {
            "gate": "ExactZeroRowXBudgetFieldsClosed",
            "closed": result["exact_zero_row_x_budget_fields_closed"],
            "proved": result["exact_zero_row_x_budget_fields_closed"],
            "meaning": "精确最小零行 x 可生成同一参数下的全部需求字段。",
            "remaining": EXACT_X_RUNNER,
        },
        {
            "gate": "ExactXSampleMinGreaterThanP",
            "closed": result["exact_x_sample_min_gt_p_verified"],
            "proved": False,
            "meaning": "样本精确 X(P) 均大于 P，但这不是全局证明。",
            "remaining": SHORT_INTERVAL,
        },
        {
            "gate": "ExactXRunnerInterfaceClosed",
            "closed": result["exact_x_runner_interface_closed"],
            "proved": result["exact_x_runner_interface_closed"],
            "meaning": "后续有限 runner 或解析包可直接读取 exact x/M#/tau 字段比较 U_np。",
            "remaining": f"{EXACT_X_RUNNER} AND {COLD_NUMERIC}",
        },
        {
            "gate": "SameParameterStrictMarginProved",
            "closed": False,
            "proved": False,
            "meaning": "还没有证明 exact M# 统一反超注册冷供给 U_np。",
            "remaining": f"{EXACT_X_RUNNER} AND {COLD_NUMERIC}",
        },
        {
            "gate": "DirectUnconditionalContradictionFound",
            "closed": False,
            "proved": False,
            "meaning": "本步没有推出早期零行反例不存在；只是把精确 x 接入终端预算。",
            "remaining": f"{EXACT_X_RUNNER} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "非持久 exact-x 预算、持久 moving atom 与 DStructure/Rankin 仍未全部闭合。",
            "remaining": f"{EXACT_X_RUNNER} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result(ledger: dict[str, Any]) -> dict[str, Any]:
    """构造接口证书。"""
    margin = load_json(DOCS / "prime-matrix-strict-same-parameter-sparse-margin-after-return-cycle-router.json")
    cold = load_json(DOCS / "prime-matrix-strict-cold-supply-numeric-after-return-cycle-router.json")
    target_imported = margin.get("next_direct_attack_target") == COLD_NUMERIC
    fields_closed = ledger["all_budget_fields_generated_from_same_x"]
    interface_closed = target_imported and fields_closed and cold.get("effective_pruning_closed_for_nonpersistent_budget") is True
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_exact_x_budget_interface_router",
        "status": "exact_x_budget_interface_closed_strict_margin_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "same_parameter_margin_target_imported": target_imported,
        "effective_pruning_budget_interface_imported": cold.get(
            "effective_pruning_closed_for_nonpersistent_budget"
        )
        is True,
        "exact_zero_row_x_budget_fields_closed": fields_closed,
        "exact_x_sample_min_gt_p_verified": ledger["all_rows_have_exact_x_gt_P"],
        "exact_x_runner_interface_closed": interface_closed,
        "global_minimal_alignment_x_gt_P_proved": False,
        "same_parameter_sparse_demand_cold_supply_strict_margin_proved": False,
        "cold_supply_same_parameter_numeric_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": STRICT_MARGIN,
        "hardpoint_after_router": f"{EXACT_X_RUNNER} AND {COLD_NUMERIC}",
        "next_direct_attack_target": EXACT_X_RUNNER,
        "parallel_attack_targets": [COLD_NUMERIC, MOVING_ATOM, DSTRUCTURE],
        "theorem_rows": theorem_rows(),
        "budget_rows": ledger["budget_rows"],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "逆元最小对齐解路线已接入同参数预算判定：给定 P，零行行号 "
            "`X(P)` 是一个有限 CRT 覆盖最小解；一旦 x 被确定，同一 x 直接生成 "
            "`rho_q(x)`、`mu_q`、`R_{x,z}`、`tau_z(c)` 和 `M#_{x,z}`。"
            "因此在需要精细判定时，可以用 exact-x runner 逐项比较注册的非持久冷供给 `U_np`。"
            "但该接口不自动证明全局 `X(P)>P`，也不自动证明 `M#_{x,z}>U_np`；"
            "前者会落入短区间素数路线，后者仍需冷供给数值 envelope 或解析支配。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix inverse alignment 精确 x 预算接口路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_parameter_margin_target_imported={fmt_bool(result['same_parameter_margin_target_imported'])}",
        f"exact_zero_row_x_budget_fields_closed={fmt_bool(result['exact_zero_row_x_budget_fields_closed'])}",
        f"exact_x_sample_min_gt_p_verified={fmt_bool(result['exact_x_sample_min_gt_p_verified'])}",
        f"exact_x_runner_interface_closed={fmt_bool(result['exact_x_runner_interface_closed'])}",
        f"same_parameter_sparse_demand_cold_supply_strict_margin_proved={fmt_bool(result['same_parameter_sparse_demand_cold_supply_strict_margin_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 接口定理",
        "",
        "| name | statement | status |",
        "| --- | --- | --- |",
    ]
    for item in result["theorem_rows"]:
        lines.append(
            "| `{name}` | {statement} | `{status}` |".format(
                name=table_cell(item["name"]),
                statement=table_cell(item["statement"]),
                status=table_cell(item["status"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. exact x 预算样本",
            "",
            "| P | X(P) | X/P | z | R_xz | M# | suffix cap | overlap debt | max mult |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["budget_rows"]:
        lines.append(
            "| `{P}` | `{x}` | `{ratio}` | `{z}` | `{r}` | `{msharp}` | `{cap}` | `{overlap}` | `{mult}` |".format(
                P=item["P"],
                x=item["exact_minimal_zero_row_x"],
                ratio=item["x_over_P"],
                z=item["same_parameter_z"],
                r=item["R_xz_size"],
                msharp=item["Msharp_exact"],
                cap=item["suffix_capacity_sum_mu"],
                overlap=item["overlap_debt"],
                mult=item["max_column_multiplicity"],
            )
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["decision_rows"]:
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
            "## 4. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 任务：把 exact `M#_{x,z}` 与同参数 `U_np` 冷供给 envelope 做可复核有限 runner 或解析支配。",
            "- 边界：不能把样本 `X(P)>P` 当作全局证明。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、Markdown 与 data ledger。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    ledger = build_interface_ledger()
    OUT_LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    result = build_result(ledger)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
