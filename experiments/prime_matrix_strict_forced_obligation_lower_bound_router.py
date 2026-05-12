#!/usr/bin/env python3
"""生成 strict 边界帽 forced obligation 下界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_forced_obligation_lower_bound_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-forced-obligation-lower-bound-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-forced-obligation-lower-bound-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-forced-obligation-lower-bound-router.md"

FORCED_LOWER = "BoundaryCapForcedFormalUnitObligationLowerBound"
WEIGHTED_INJECTION = "CLBResidualHoleToWeightedObligationInjection"
RESIDUAL_MASS = "BoundaryResidualMassLowerBoundForTypeCompression"
NO_COLLAPSE = "NoQuotientCollapseBelowTypeThreshold"
EFFECTIVE_INSTANCE = "EffectiveDistinctTypeInstanceLowerBound"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.json",
    MONOGRAPH / "prime-matrix-early-zero-contradiction-matrix-router.json",
    MONOGRAPH / "prime-matrix-cylindrical-completion-line-barrier.md",
    MONOGRAPH / "prime-matrix-formal-unit-partition-coverage-router.json",
    MONOGRAPH / "prime-matrix-partition-coverage-no-loss-equation-router.json",
    MONOGRAPH / "prime-matrix-partition-disjointness-boundary-return-router.md",
    MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.json",
    MONOGRAPH / "prime-matrix-anchor-set-reconstruction-certificate-router.json",
    MONOGRAPH / "prime-matrix-early-zero-carry-shell-router.json",
    MONOGRAPH / "prime-matrix-early-zero-anchor-collar-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空字典。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    """读取文本；缺失时返回空字符串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def mass_transfer_laws() -> list[dict[str, str]]:
    """给出残洞到义务的质量转移律。"""
    return [
        {
            "law": "residual_hole_forcing",
            "formula": "EarlyZeroRowWithinP => each c in R_x has at least one covering label obligation.",
            "status": "conditional_closed_as_weighted_injection",
        },
        {
            "law": "no_loss_partition",
            "formula": "O(w)=SourceRecords disjoint_union NamedReturnRecords, Lost(O)=empty.",
            "status": "closed",
        },
        {
            "law": "weighted_reuse_not_erasure",
            "formula": "duplicate coordinates become quotient/reuse/weighted returns, not deleted obligations.",
            "status": "closed",
        },
        {
            "law": "unweighted_instance_gap",
            "formula": "weighted mass lower bound does not imply enough distinct row-free type instances without anti-collapse.",
            "status": "open",
        },
    ]


def build_rows(
    type_router: dict[str, Any],
    early_zero: dict[str, Any],
    clb_text: str,
    partition: dict[str, Any],
    noloss_eq: dict[str, Any],
    noloss: dict[str, Any],
    carry: dict[str, Any],
    collar: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 forced obligation 下界判定表。"""
    clb_available = "R_x=F_x" in clb_text or "CLB" in clb_text
    return [
        {
            "gate": "ForcedLowerBoundInputActive",
            "closed": type_router.get("next_direct_attack_target") == FORCED_LOWER,
            "proved": False,
            "meaning": "上一层把类型压缩的第一缺口定为边界帽 forced obligation 下界。",
            "remaining": FORCED_LOWER,
        },
        {
            "gate": "CLBResidualEqualityImported",
            "closed": clb_available and early_zero.get("no_unnamed_exit_for_early_zero") is True,
            "proved": True,
            "meaning": "早期零行假设下 CLB 把残洞集合压成必须被补洞支付的对象。",
            "remaining": "需要把残洞数量转成类型压缩可用的有效实例数。",
        },
        {
            "gate": "NoLossWeightedObligationImported",
            "closed": partition.get("formal_unit_partition_coverage_lemma_closed") is True
            and noloss_eq.get("partition_coverage_no_loss_equation_closed") is True
            and noloss.get("no_loss_return_accounting_closed") is True,
            "proved": True,
            "meaning": "覆盖义务不会丢失；普通来源、命名回流、quotient/reuse 均保留在 O(w) 中。",
            "remaining": "这给加权质量守恒，不给未加权不同类型数量。",
        },
        {
            "gate": "CarryCollarRigidityImported",
            "closed": carry.get("exact_carry_shell_identity_closed") is True
            and collar.get("canonical_anchor_collar_closed") is True,
            "proved": True,
            "meaning": "残洞支付必须满足 carry-shell 与 anchor-collar 短纤维刚性。",
            "remaining": "刚性可限制类型，但具体计数尚未证明。",
        },
        {
            "gate": "WeightedResidualHoleInjectionClosed",
            "closed": True,
            "proved": True,
            "meaning": "每个残洞至少贡献一个加权 obligation；重复或复用只能作为加权/quotient return 保留。",
            "remaining": WEIGHTED_INJECTION,
        },
        {
            "gate": "BoundaryResidualMassLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未给出足以压过 row-free type alphabet 的边界残洞质量下界。",
            "remaining": RESIDUAL_MASS,
        },
        {
            "gate": "NoQuotientCollapseCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 quotient/reuse/weighted returns 不能把大量残洞压成太少的不同 type instances。",
            "remaining": NO_COLLAPSE,
        },
        {
            "gate": "EffectiveDistinctTypeInstanceLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "类型压缩需要的是有效不同实例数，而不仅是加权质量；当前该下界未证。",
            "remaining": EFFECTIVE_INSTANCE,
        },
        {
            "gate": "BoundaryCapForcedFormalUnitObligationLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "已闭合残洞到加权义务的注入，但未闭合残洞质量和抗商化塌缩，所以 forced lower bound 仍未完成。",
            "remaining": f"{RESIDUAL_MASS} AND {NO_COLLAPSE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 forced obligation 下界证书。"""
    type_router = load_json(MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.json")
    early_zero = load_json(MONOGRAPH / "prime-matrix-early-zero-contradiction-matrix-router.json")
    clb_text = load_text(MONOGRAPH / "prime-matrix-cylindrical-completion-line-barrier.md")
    partition = load_json(MONOGRAPH / "prime-matrix-formal-unit-partition-coverage-router.json")
    noloss_eq = load_json(MONOGRAPH / "prime-matrix-partition-coverage-no-loss-equation-router.json")
    noloss = load_json(MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.json")
    carry = load_json(MONOGRAPH / "prime-matrix-early-zero-carry-shell-router.json")
    collar = load_json(MONOGRAPH / "prime-matrix-early-zero-anchor-collar-router.json")

    rows = build_rows(
        type_router=type_router,
        early_zero=early_zero,
        clb_text=clb_text,
        partition=partition,
        noloss_eq=noloss_eq,
        noloss=noloss,
        carry=carry,
        collar=collar,
    )
    after = f"{RESIDUAL_MASS} AND {NO_COLLAPSE}"
    return {
        "certificate_type": "prime_matrix_strict_forced_obligation_lower_bound_router",
        "status": "forced_obligation_lower_bound_reduced_to_residual_mass_and_no_quotient_collapse_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "clb_residual_to_weighted_obligation_injection_closed": True,
        "no_loss_weighted_accounting_imported": True,
        "boundary_residual_mass_lower_bound_proved": False,
        "no_quotient_collapse_below_type_threshold_proved": False,
        "effective_distinct_type_instance_lower_bound_proved": False,
        "boundary_cap_forced_obligation_lower_bound_proved": False,
        "boundary_cap_formal_unit_type_compression_dichotomy_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": FORCED_LOWER,
        "hardpoint_after_router": after,
        "next_direct_attack_target": RESIDUAL_MASS,
        "parallel_attack_target": NO_COLLAPSE,
        "mass_transfer_laws": mass_transfer_laws(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`BoundaryCapForcedFormalUnitObligationLowerBound` 继续下钻后，必须区分两种量。"
            "早期零行与 CLB/no-loss 账本已经给出残洞到加权 obligation 的注入：残洞不会被删除，"
            "重复和复用也只能作为 quotient/reuse/weighted return 保留。"
            "但类型压缩需要的是可和 row-free type alphabet 比较的有效不同实例数。当前还缺边界残洞质量下界，"
            "以及防止 quotient/reuse 把大量残洞塌缩成少数类型的 anti-collapse 证明。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 边界帽 forced obligation 下界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clb_residual_to_weighted_obligation_injection_closed={fmt_bool(result['clb_residual_to_weighted_obligation_injection_closed'])}",
        f"no_loss_weighted_accounting_imported={fmt_bool(result['no_loss_weighted_accounting_imported'])}",
        f"boundary_residual_mass_lower_bound_proved={fmt_bool(result['boundary_residual_mass_lower_bound_proved'])}",
        f"no_quotient_collapse_below_type_threshold_proved={fmt_bool(result['no_quotient_collapse_below_type_threshold_proved'])}",
        f"effective_distinct_type_instance_lower_bound_proved={fmt_bool(result['effective_distinct_type_instance_lower_bound_proved'])}",
        f"boundary_cap_forced_obligation_lower_bound_proved={fmt_bool(result['boundary_cap_forced_obligation_lower_bound_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 下界拆分",
        "",
        "拆分前：",
        "",
        "```text",
        result["hardpoint_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["hardpoint_after_router"],
        "```",
        "",
        "## 2. 质量转移律",
        "",
        "| law | formula | status |",
        "| --- | --- | --- |",
    ]
    for row in result["mass_transfer_laws"]:
        lines.append(
            "| `{law}` | {formula} | `{status}` |".format(
                law=table_cell(row["law"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
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
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行硬点：",
            "",
            "```text",
            result["parallel_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
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
