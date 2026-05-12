#!/usr/bin/env python3
"""生成 strict fixed-pair fiber bound 原子化证书。

用法示例：
  python3 experiments/prime_matrix_strict_fixed_pair_fiber_bound_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-fixed-pair-fiber-bound-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"
OUT_MD = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-actual-emitter-incidence-entropy-router.json",
    "prime-matrix-clean-core-fiber-emitter-field-audit-router.json",
    "prime-matrix-clean-core-alpha-delta-disintegration-router.json",
    "prime-matrix-clean-core-geometric-variation-branch-budget-router.json",
    "prime-matrix-clean-core-reverse-provenance-functor-router.json",
    "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(
    incidence_entropy: dict[str, Any],
    field_audit: dict[str, Any],
    disintegration: dict[str, Any],
    branch_budget: dict[str, Any],
    reverse_functor: dict[str, Any],
    signed_phi: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 fixed-pair fiber bound 原子化判定表。"""
    target = "ExactUVMapFixedPairPolylogFiberBoundLedger"
    next_basis = (
        "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND "
        "FixedKeyExactUVLocalMultiplicityO1Ledger"
    )
    terminal_after = incidence_entropy.get("terminal_gap_after_router", "")
    return [
        {
            "gate": "FixedPairFiberTargetActive",
            "closed": target in terminal_after,
            "proved": False,
            "meaning": "上一层已把 bounded incidence 拆成源域熵账本与 fixed-pair 纤维上界账本。",
            "remaining": target,
        },
        {
            "gate": "DeterministicKeyFiberInequalityClosed",
            "closed": True,
            "proved": True,
            "meaning": (
                "若 primitive emitter 被完整 key 分区，key 数为 log^C，且每个固定 `(u,v,key)` "
                "最多 O(1) 个源原像，则每个固定 `(u,v)` 纤维至多 log^O(1)。"
            ),
            "remaining": "这是形式不等式，不提供 actual key 表或局部 O(1) 原像证明。",
        },
        {
            "gate": "CompleteKeyPartitionIsNecessary",
            "closed": True,
            "proved": True,
            "meaning": "branch key 必须是 complete key：包含 formal unit、branch path、sign/local factor、dyadic/truncation 与 exact `(u,v)` map 口径。",
            "remaining": "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger。",
        },
        {
            "gate": "PaymentSkeletonNotACompleteKeyPartition",
            "closed": field_audit.get("payment_fiber_skeleton_closed") is True,
            "proved": True,
            "meaning": "payment skeleton 只给 completion-hole/first-cover 计数，不给 pre-Cauchy primitive summand 的 complete key。",
            "remaining": "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger。",
        },
        {
            "gate": "DisintegrationDictionaryNotAFiberBound",
            "closed": disintegration.get("registered_alpha_delta_disintegration_dictionary_proved")
            is False,
            "proved": True,
            "meaning": "逐纤维字典即使形式可写，也可在同一 `(u,v)` 中塞入任意多 summand；还需要 complete key 与固定 key 局部重数。",
            "remaining": next_basis,
        },
        {
            "gate": "ReverseProvenanceNoGoImported",
            "closed": reverse_functor.get("pushforward_reverse_uniqueness_rejected") is True,
            "proved": True,
            "meaning": "从 Gamma 或有限投影反推 primitive preimage 不唯一，不能由下游图推出 fixed-pair 纤维 polylog。",
            "remaining": next_basis,
        },
        {
            "gate": "SignedPhiReductionIdentifiesSameEmitter",
            "closed": signed_phi.get("terminal_gap_after_router")
            == "RegisteredPrimitivePrePushforwardFiberEmitterAndReturn",
            "proved": True,
            "meaning": "actual signed/Phi 预算已被压到同一个 pre-pushforward emitter，说明本步没有改换证明对象。",
            "remaining": next_basis,
        },
        {
            "gate": "BranchBudgetCurrentCorpusProved",
            "closed": (
                field_audit.get("polylog_branch_schema_proved") is True
                or branch_budget.get("branch_key_multiplicity_budget_proved") is True
            ),
            "proved": False,
            "meaning": "当前材料尚未证明 actual noncanonical primitive emitter 的 complete branch/key 数为 log^O(1)。",
            "remaining": "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger。",
        },
        {
            "gate": "FixedKeyLocalMultiplicityCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有 actual emitter 公式/Jacobian/三角恢复律来证明固定 complete key 与 fixed `(u,v)` 下只有 O(1) 原像。",
            "remaining": "FixedKeyExactUVLocalMultiplicityO1Ledger。",
        },
        {
            "gate": "CurrentCorpusFixedPairFiberBoundProved",
            "closed": False,
            "proved": False,
            "meaning": "complete key 分区与固定 key 局部 O(1) 重数都未证明，所以 fixed-pair polylog fiber bound 仍开放。",
            "remaining": next_basis,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict fixed-pair fiber bound 证书。"""
    incidence_entropy = load_json(
        DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"
    )
    field_audit = load_json(DOCS / "prime-matrix-clean-core-fiber-emitter-field-audit-router.json")
    disintegration = load_json(DOCS / "prime-matrix-clean-core-alpha-delta-disintegration-router.json")
    branch_budget = load_json(
        DOCS / "prime-matrix-clean-core-geometric-variation-branch-budget-router.json"
    )
    reverse_functor = load_json(
        DOCS / "prime-matrix-clean-core-reverse-provenance-functor-router.json"
    )
    signed_phi = load_json(DOCS / "prime-matrix-actual-signed-phi-budget-emitter-reduction-router.json")

    target = "ExactUVMapFixedPairPolylogFiberBoundLedger"
    next_basis = (
        "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger AND "
        "FixedKeyExactUVLocalMultiplicityO1Ledger"
    )
    rows = build_rows(
        incidence_entropy=incidence_entropy,
        field_audit=field_audit,
        disintegration=disintegration,
        branch_budget=branch_budget,
        reverse_functor=reverse_functor,
        signed_phi=signed_phi,
    )
    return {
        "certificate_type": "prime_matrix_strict_fixed_pair_fiber_bound_router",
        "status": "strict_fixed_pair_fiber_bound_reduced_to_complete_key_partition_and_fixed_key_multiplicity_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "fixed_pair_fiber_bound_router_closed": True,
        "deterministic_key_fiber_inequality_closed": True,
        "registered_complete_primitive_emitter_key_partition_polylog_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": target,
        "terminal_gap_after_router": next_basis,
        "next_direct_attack_target": "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger",
        "deterministic_lemma": (
            "Let D be the actual primitive pre-Cauchy emitter domain, pi:D->Omega_exact the exact `(u,v)` map, "
            "and kappa:D->K a complete primitive emitter key. If |K|<=L^C and "
            "sup_{(u,v),k}|{d in D: pi(d)=(u,v), kappa(d)=k}|<=C0, then "
            "sup_{(u,v)}|pi^{-1}(u,v)|<=C0*L^C=log^O(1)."
        ),
        "hard_law": (
            "fixed-pair 纤维上界不是 payment 计数，也不是 CRT 位置刚性。它必须在 Cauchy/dispersion 前的 actual primitive emitter "
            "上证明：先有完整 key 的 polylog 分区，再有固定 key 下 exact-UV map 的 O(1) 局部重数。缺任一项都会允许大量 "
            "preimage 坍缩到同一个 `(u,v)`。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`ExactUVMapFixedPairPolylogFiberBoundLedger` 被压成两个真正原子："
            "`RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger` 与 "
            "`FixedKeyExactUVLocalMultiplicityO1Ledger`。其中 key-to-fiber 的形式不等式已闭合，"
            "但 actual complete key 分区和固定 key 局部 O(1) 原像证明尚未给出；因此行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict fixed-pair fiber bound 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"fixed_pair_fiber_bound_router_closed={fmt_bool(result['fixed_pair_fiber_bound_router_closed'])}",
        f"deterministic_key_fiber_inequality_closed={fmt_bool(result['deterministic_key_fiber_inequality_closed'])}",
        f"registered_complete_primitive_emitter_key_partition_polylog_proved={fmt_bool(result['registered_complete_primitive_emitter_key_partition_polylog_proved'])}",
        f"fixed_key_exact_uv_local_multiplicity_o1_proved={fmt_bool(result['fixed_key_exact_uv_local_multiplicity_o1_proved'])}",
        f"exact_uv_map_fixed_pair_polylog_fiber_bound_proved={fmt_bool(result['exact_uv_map_fixed_pair_polylog_fiber_bound_proved'])}",
        f"actual_emitter_exact_uv_bounded_multiplicity_incidence_proved={fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 形式引理",
        "",
        "```text",
        result["deterministic_lemma"],
        "```",
        "",
        "## 2. 原子化",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
        "```",
        "",
        "## 3. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 4. 结构结论",
            "",
            result["hard_law"],
            "",
            "## 5. 下一主攻点",
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
