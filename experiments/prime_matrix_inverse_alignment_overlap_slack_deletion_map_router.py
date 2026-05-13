#!/usr/bin/env python3
"""审计 overlap/slack 到 cold supply 删除单位的注册映射。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_overlap_slack_deletion_map_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-overlap-slack-deletion-map-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-overlap-slack-deletion-map-router.json
  docs/monograph/prime-matrix-inverse-alignment-overlap-slack-deletion-map-router.md
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
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-overlap-slack-deletion-map-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-overlap-slack-deletion-map-router.md"

PROFILE_LEDGER = DATA / "inverse-alignment-exact-zero-row-charge-profile-ledger.json"
BUDGET_LEDGER = DATA / "inverse-alignment-exact-x-budget-interface-ledger.json"
DELETION_TARGET = DOCS / "prime-matrix-inverse-alignment-cold-restricted-deletion-target-router.json"
CANDIDATE = DOCS / "prime-matrix-inverse-alignment-overlap-slack-deletion-candidate-router.json"

SOURCE_FILES = [
    PROFILE_LEDGER,
    BUDGET_LEDGER,
    DELETION_TARGET,
    CANDIDATE,
    DOCS / "prime-matrix-strict-cold-window-sibling-charging-router.json",
    DOCS / "prime-matrix-strict-sibling-numeric-envelope-attack-router.json",
    DOCS / "prime-matrix-strict-common-kernel-return-cycle-descent-router.json",
]

REGISTERED_MAP = "RegisteredOverlapSlackToColdSupplyDeletionMap"
DIRECT_SUFFIX_MAP = "RegisteredDirectSuffixOverlapDeletionMap"
RESIDUAL_COMPRESSION = "ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def primes_upto(n: int) -> list[int]:
    """生成不超过 n 的素数。"""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p_value in range(2, int(n**0.5) + 1):
        if sieve[p_value]:
            for multiple in range(p_value * p_value, n + 1, p_value):
                sieve[multiple] = False
    return [idx for idx, ok in enumerate(sieve) if ok]


def inverse_phase(P: int, x: int, q: int) -> int:
    """计算行 x 下素数 q 的覆盖相位。"""
    return (-x * P) % q


def source_hashes() -> dict[str, str]:
    """登记依赖哈希，便于复查证书来源。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_overlap_slack_deletion_map_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def row_unit_audit(target_row: dict[str, Any], budget_row: dict[str, Any]) -> dict[str, Any]:
    """把一个 exact-x 行拆成 raw suffix 命中单位并审计可注册删除量。"""
    P = int(target_row["P"])
    x = int(target_row["x"])
    z = int(target_row["z"])
    msharp = float(target_row["Msharp"])
    required = int(target_row["minimum_integer_deletion_for_strict_margin"])

    qs = primes_upto(P - 1)
    small_qs = [q for q in qs if q <= z]
    large_qs = [q for q in qs if q > z]
    phases = {q: inverse_phase(P, x, q) for q in qs}
    hits_by_c = {
        c: [q for q in qs if c % q == phases[q]]
        for c in range(1, P)
    }

    # raw suffix 单位是当前 exact-x runner 原来允许计入 cold supply 的整数单位。
    raw_suffix_units = {
        (q, c)
        for c in range(1, P)
        for q in large_qs
        if q in hits_by_c[c]
    }
    residual_columns = [
        c
        for c in range(1, P)
        if not any(q in hits_by_c[c] for q in small_qs)
    ]

    # tau(c) 取该残洞列的第一条后缀命中线；零行假设保证它存在。
    tau_by_c: dict[int, int] = {}
    unlabeled_residual_columns: list[int] = []
    for c in residual_columns:
        tail_hits = [q for q in large_qs if q in hits_by_c[c]]
        if not tail_hits:
            unlabeled_residual_columns.append(c)
            continue
        tau_by_c[c] = tail_hits[0]

    assigned_tau_units = {(q, c) for c, q in tau_by_c.items()}
    direct_suffix_deletion_units = raw_suffix_units - assigned_tau_units
    appeared_tau = set(tau_by_c.values())
    charged_tau_slack_units = {
        (q, c)
        for (q, c) in raw_suffix_units
        if q in appeared_tau and (q, c) not in assigned_tau_units
    }
    unappeared_suffix_units = {
        (q, c)
        for (q, c) in raw_suffix_units
        if q not in appeared_tau
    }

    total_overlap_debt = sum(max(0, len(hits) - 1) for hits in hits_by_c.values())
    additive_proxy = total_overlap_debt + len(charged_tau_slack_units)
    direct_registered = len(direct_suffix_deletion_units)
    residual_compression_needed = max(0, required - direct_registered)
    residual_formula = math.floor(len(residual_columns) - msharp) + 1

    return {
        "P": P,
        "x": x,
        "z": z,
        "Msharp": round(msharp, 12),
        "raw_suffix_capacity": len(raw_suffix_units),
        "residual_columns": len(residual_columns),
        "assigned_tau_units": len(assigned_tau_units),
        "unlabeled_residual_columns": unlabeled_residual_columns,
        "direct_suffix_deletion_units": direct_registered,
        "charged_tau_slack_units": len(charged_tau_slack_units),
        "unappeared_suffix_units": len(unappeared_suffix_units),
        "total_overlap_debt": total_overlap_debt,
        "candidate_additive_proxy": additive_proxy,
        "candidate_proxy_from_previous_router": int(budget_row["overlap_debt"])
        + int(budget_row["charged_slack_for_appeared_tau"]),
        "minimum_required_deletion": required,
        "direct_deletion_gap_to_required": required - direct_registered,
        "residual_reciprocal_compression_needed": residual_compression_needed,
        "residual_compression_formula": residual_formula,
        "suffix_partition_identity_ok": len(raw_suffix_units)
        == len(assigned_tau_units) + direct_registered,
        "residual_assignment_identity_ok": len(assigned_tau_units) == len(residual_columns),
        "tau_charged_slack_subset_of_direct_deletion": charged_tau_slack_units
        <= direct_suffix_deletion_units,
        "unappeared_suffix_subset_of_direct_deletion": unappeared_suffix_units
        <= direct_suffix_deletion_units,
        "candidate_additive_proxy_exceeds_distinct_registered_units": additive_proxy
        > direct_registered,
        "direct_deletion_alone_closes_required_target": direct_registered >= required,
        "residual_compression_formula_ok": residual_compression_needed == residual_formula,
        "target_decomposition_identity_ok": required
        == direct_registered + residual_compression_needed,
        "strict_margin_after_direct_suffix_deletion": (
            len(raw_suffix_units) - direct_registered
        )
        < msharp,
    }


def unit_audit_rows() -> list[dict[str, Any]]:
    """生成所有样本行的单位级审计表。"""
    target = load_json(DELETION_TARGET)
    budget = load_json(BUDGET_LEDGER)
    budget_by_p = {int(item["P"]): item for item in budget.get("budget_rows", [])}
    rows: list[dict[str, Any]] = []
    for item in target.get("deletion_target_rows", []):
        P = int(item["P"])
        rows.append(row_unit_audit(item, budget_by_p[P]))
    return rows


def theorem_rows() -> list[dict[str, str]]:
    """列出本步真正闭合和未闭合的数学输入。"""
    return [
        {
            "name": "suffix_unit_partition",
            "status": "closed",
            "statement": "U_suf is the disjoint union of assigned tau units and direct suffix deletion units.",
        },
        {
            "name": "tau_slack_registration",
            "status": "closed",
            "statement": "charged tau slack and unappeared suffix capacity are subsets of direct suffix deletion units.",
        },
        {
            "name": "overlap_plus_tau_additive_injection",
            "status": "rejected_under_current_labels",
            "statement": "global overlap_debt + charged tau slack is not a disjoint injection into raw suffix deletion units.",
        },
        {
            "name": "deletion_target_decomposition",
            "status": "closed",
            "statement": "required deletion = direct suffix deletion + floor(|R_xz|-M#)+1 in the audited exact-x rows.",
        },
        {
            "name": "residual_assigned_atom_compression",
            "status": "open",
            "statement": "the remaining task is to compress assigned residual atoms from unit weight to reciprocal/M# weight, or route the excess to named returns.",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "PreviousOverlapSlackCandidateImported",
            "closed": result["previous_overlap_slack_candidate_imported"],
            "proved": result["previous_overlap_slack_candidate_imported"],
            "meaning": "上一层候选表已读入并逐行复核。",
            "remaining": REGISTERED_MAP,
        },
        {
            "gate": "DirectSuffixOverlapDeletionMapClosed",
            "closed": result["registered_direct_suffix_overlap_deletion_map_closed"],
            "proved": result["registered_direct_suffix_overlap_deletion_map_closed"],
            "meaning": "raw suffix 命中单位可精确分成 tau 已分配单位与可删除后缀冗余单位。",
            "remaining": RESIDUAL_COMPRESSION,
        },
        {
            "gate": "TauSlackInjectionClosed",
            "closed": result["tau_slack_injection_into_direct_suffix_deletion_closed"],
            "proved": result["tau_slack_injection_into_direct_suffix_deletion_closed"],
            "meaning": "tau charged slack 不是新增独立供给；它已包含在 direct suffix deletion 中。",
            "remaining": RESIDUAL_COMPRESSION,
        },
        {
            "gate": "OverlapSlackAdditiveMapRejected",
            "closed": result["overlap_plus_tau_additive_map_rejected_under_current_labels"],
            "proved": result["overlap_plus_tau_additive_map_rejected_under_current_labels"],
            "meaning": "样本级单位账本显示 overlap_debt + tau_slack 超过可注册的不重叠 raw suffix 删除单位，不能按原候选相加。",
            "remaining": RESIDUAL_COMPRESSION,
        },
        {
            "gate": "DeletionTargetDecompositionClosed",
            "closed": result["deletion_target_decomposition_closed"],
            "proved": result["deletion_target_decomposition_closed"],
            "meaning": "所需删除量已精确拆成后缀冗余删除与残洞已分配 atom 的 reciprocal 权重压缩。",
            "remaining": RESIDUAL_COMPRESSION,
        },
        {
            "gate": "RegisteredOverlapSlackDeletionMapProved",
            "closed": False,
            "proved": False,
            "meaning": "原 `overlap_debt + tau_slack` 映射不能闭合；必须改攻残洞已分配 atom 的权重纪律或命名回流。",
            "remaining": RESIDUAL_COMPRESSION,
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未得到早期零行反例链的终端矛盾。",
            "remaining": f"{RESIDUAL_COMPRESSION} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造注册删除映射审计证书。"""
    candidate = load_json(CANDIDATE)
    rows = unit_audit_rows()
    suffix_partition_ok = bool(rows) and all(item["suffix_partition_identity_ok"] for item in rows)
    residual_assignment_ok = bool(rows) and all(item["residual_assignment_identity_ok"] for item in rows)
    tau_subset_ok = bool(rows) and all(item["tau_charged_slack_subset_of_direct_deletion"] for item in rows)
    unappeared_subset_ok = bool(rows) and all(item["unappeared_suffix_subset_of_direct_deletion"] for item in rows)
    additive_rejected = bool(rows) and all(
        item["candidate_additive_proxy_exceeds_distinct_registered_units"] for item in rows
    )
    decomposition_ok = bool(rows) and all(item["target_decomposition_identity_ok"] for item in rows)
    direct_alone_closes = bool(rows) and all(
        item["direct_deletion_alone_closes_required_target"] for item in rows
    )
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_overlap_slack_deletion_map_router",
        "status": "direct_suffix_deletion_map_closed_residual_weight_compression_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "previous_overlap_slack_candidate_imported": candidate.get(
            "overlap_slack_candidate_dominates_samples"
        )
        is True,
        "registered_direct_suffix_overlap_deletion_map_closed": suffix_partition_ok
        and residual_assignment_ok,
        "tau_slack_injection_into_direct_suffix_deletion_closed": tau_subset_ok
        and unappeared_subset_ok,
        "overlap_plus_tau_additive_map_rejected_under_current_labels": additive_rejected,
        "deletion_target_decomposition_closed": decomposition_ok,
        "direct_suffix_deletion_alone_closes_required_target": direct_alone_closes,
        "registered_overlap_slack_deletion_map_proved": False,
        "cold_restriction_deletion_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": REGISTERED_MAP,
        "hardpoint_after_router": RESIDUAL_COMPRESSION,
        "next_direct_attack_target": RESIDUAL_COMPRESSION,
        "parallel_attack_targets": [MOVING_ATOM, DSTRUCTURE],
        "unit_audit_rows": rows,
        "theorem_rows": theorem_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 `RegisteredOverlapSlackToColdSupplyDeletionMap` 下钻到单个 raw suffix 命中单位。"
            "结论是：可无歧义注册的删除单位不是 `overlap_debt + tau_slack` 的相加量，而是"
            "`raw_suffix_capacity-|R_{x,z}|`，即所有未被残洞 tau 选中的后缀命中单位。"
            "`tau_slack` 与未出现后缀容量都包含在这个直接后缀删除集中；全局 `overlap_debt` "
            "含有小素层内部重叠，不能整体注入 raw suffix cold 删除单位。因此原相加候选不能闭合。"
            "所需删除量精确分解为直接后缀冗余删除加 `floor(|R_{x,z}|-M#)+1`，下一最窄点是"
            "`ResidualAssignedAtomReciprocalWeightCompressionOrNamedReturnLedger`。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix inverse alignment overlap/slack 注册删除映射审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"registered_direct_suffix_overlap_deletion_map_closed={fmt_bool(result['registered_direct_suffix_overlap_deletion_map_closed'])}",
        f"tau_slack_injection_into_direct_suffix_deletion_closed={fmt_bool(result['tau_slack_injection_into_direct_suffix_deletion_closed'])}",
        f"overlap_plus_tau_additive_map_rejected_under_current_labels={fmt_bool(result['overlap_plus_tau_additive_map_rejected_under_current_labels'])}",
        f"deletion_target_decomposition_closed={fmt_bool(result['deletion_target_decomposition_closed'])}",
        f"registered_overlap_slack_deletion_map_proved={fmt_bool(result['registered_overlap_slack_deletion_map_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 单位审计表",
        "",
        "| P | X(P) | z | raw | R | direct del | tau slack | unappeared | overlap total | additive proxy | required | residual compression |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["unit_audit_rows"]:
        lines.append(
            "| `{P}` | `{x}` | `{z}` | `{raw}` | `{R}` | `{direct}` | `{tau}` | `{unapp}` | `{overlap}` | `{proxy}` | `{req}` | `{res}` |".format(
                P=item["P"],
                x=item["x"],
                z=item["z"],
                raw=item["raw_suffix_capacity"],
                R=item["residual_columns"],
                direct=item["direct_suffix_deletion_units"],
                tau=item["charged_tau_slack_units"],
                unapp=item["unappeared_suffix_units"],
                overlap=item["total_overlap_debt"],
                proxy=item["candidate_additive_proxy"],
                req=item["minimum_required_deletion"],
                res=item["residual_reciprocal_compression_needed"],
            )
        )
    lines.extend(
        [
            "",
            "解释：`direct del=raw-R` 是可直接注册的后缀冗余删除单位；`residual compression=floor(R-M#)+1` 是仍需证明的已分配残洞 atom 权重压缩量。",
            "",
            "## 2. 已闭合/未闭合命题",
            "",
            "| name | status | statement |",
            "| --- | --- | --- |",
        ]
    )
    for item in result["theorem_rows"]:
        lines.append(
            "| `{name}` | `{status}` | {statement} |".format(
                name=table_cell(item["name"]),
                status=table_cell(item["status"]),
                statement=table_cell(item["statement"]),
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
            "- 具体任务：证明已分配残洞 atom 不能以单位权继续留在非持久 cold supply；它必须按 `M#=sum n_q/mu_q` 的 reciprocal 权重压缩，或触发固定历史、ColumnCRT、热核心、PDEC/SAE 等命名回流。",
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
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print(f"next={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
