#!/usr/bin/env python3
"""汇总行列命题最后剩余原子，闭合逻辑推理链条边界。

用法示例：
  python3 experiments/prime_matrix_last_remaining_atoms_router.py

输出：
  docs/monograph/prime-matrix-last-remaining-atoms-router.json
  docs/monograph/prime-matrix-last-remaining-atoms-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_NONCANONICAL = DOCS / "prime-matrix-noncanonical-final-narrowing-router.json"
DEFAULT_SOURCE_ENTROPY_REDUCTION = DOCS / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json"
DEFAULT_SUPPORT_RANGE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json"
DEFAULT_EXACT_FACTOR_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_FACTOR_INCIDENCE = DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
DEFAULT_FULLS_COMPLETION = DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_FIREWALL = DOCS / "prime-matrix-final-input-firewall-boundary-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-last-remaining-atoms-router.json"
DEFAULT_MD = DOCS / "prime-matrix-last-remaining-atoms-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def atom(
    name: str,
    atom_type: str,
    boundary_closed: bool,
    proved_or_accepted: bool,
    evidence: str,
    meaning: str,
    minimum_completion: str,
) -> dict[str, Any]:
    """构造最后剩余原子表格行。"""
    return {
        "name": name,
        "type": atom_type,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "evidence": evidence,
        "meaning": meaning,
        "minimum_completion": minimum_completion,
    }


def build_atoms(
    noncanonical: dict[str, Any],
    entropy_reduction: dict[str, Any],
    support_range: dict[str, Any],
    exact_factor_support: dict[str, Any],
    factor_incidence: dict[str, Any],
    fulls_completion: dict[str, Any],
    dstructure: dict[str, Any],
    firewall: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最终剩余原子表。"""
    noncanonical_boundary = (
        noncanonical.get("noncanonical_narrowing_boundary_closed") is True
        and noncanonical.get("ap_source_lift_rejected") is True
        and noncanonical.get("generic_self_contained_antiatom_refuted") is True
    )
    internal_support_atom_pinned = (
        entropy_reduction.get("exact_full_s_source_entropy_reduction_closed") is False
        and "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov"
        in entropy_reduction.get("open_reduction_gates", [])
        and support_range.get("balanced_range_threshold_closed") is True
        and exact_factor_support.get("current_internal_exact_factor_support_closed") is False
        and factor_incidence.get("naive_incidence_bridge_valid") is False
    )
    external_kls_atom_pinned = (
        fulls_completion.get("full_s_completion_reduction_closed") is False
        and "ModulusDependentCompletedFullSKLSInput"
        in fulls_completion.get("open_completion_gates", [])
    )
    promotion_atom_pinned = (
        dstructure.get("promotion_package_boundary_closed") is True
        and dstructure.get("promotion_package_independently_accepted") is False
    )
    firewall_closed = firewall.get("no_hidden_terminal_remaining") is True

    return [
        atom(
            name="ActualFullSNonAPExactSupportAtom",
            atom_type="internal_new_theorem",
            boundary_closed=noncanonical_boundary and internal_support_atom_pinned,
            proved_or_accepted=False,
            evidence="noncanonical final narrowing + exact source entropy reduction + exact factor support audits",
            meaning=(
                "内部自足路线已经压成 actual full-S non-AP 源的精确因子支撑/容量兼容包；"
                "balanced range 已闭合，K4/K6 与朴素 incidence 不能自动推出该包。"
            ),
            minimum_completion=(
                "证明 FullSNonAPExactFactorSupportLowerBound 与 FullSNonAPTypeFourierCapacityCompatibility，"
                "或等价证明 ExactWFDSourceEntropy / strengthened source anti-atom for the actual source。"
            ),
        ),
        atom(
            name="ModulusDependentCompletedFullSKLSInput",
            atom_type="external_or_new_deep_theorem",
            boundary_closed=noncanonical_boundary and external_kls_atom_pinned,
            proved_or_accepted=False,
            evidence="full-S completion reduction router",
            meaning=(
                "外部/新深定理路线已完成 full-S completion；剩余不是模糊 KLS，而是处理依赖模数 c 的 residue 权重 "
                "B_{c,x} 的完成型 Kloosterman 平均估计。"
            ),
            minimum_completion=(
                "证明或接受完成型、模数依赖 residue 权重的 full-S non-AP WFD Kloosterman large-sieve theorem，"
                "给出任意对数节省并覆盖当前未中心化无投影对象。"
            ),
        ),
        atom(
            name="DStructureRankinIndependentAcceptance",
            atom_type="independent_promotion_acceptance",
            boundary_closed=firewall_closed and promotion_atom_pinned,
            proved_or_accepted=False,
            evidence="DStructure/Rankin promotion acceptance router",
            meaning=(
                "最终晋级门不是数学隐藏终端，而是独立验收原子；作者侧已给格式、样本和边界，"
                "但不能替代正式全集证书与独立接受。"
            ),
            minimum_completion=(
                "独立接受 D-structure/Structured-EHPD 入口、Tail-log4 BG/RKS 适配、有限验证 hash，"
                "并提交全部正式着色走廊 Rankin 证书或把失败者回流 PDEC/SAE。"
            ),
        ),
    ]


def run(
    noncanonical_path: Path,
    entropy_reduction_path: Path,
    support_range_path: Path,
    exact_factor_support_path: Path,
    factor_incidence_path: Path,
    fulls_completion_path: Path,
    dstructure_path: Path,
    firewall_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行最后剩余原子汇总路由。"""
    noncanonical = load_json(noncanonical_path)
    entropy_reduction = load_json(entropy_reduction_path)
    support_range = load_json(support_range_path)
    exact_factor_support = load_json(exact_factor_support_path)
    factor_incidence = load_json(factor_incidence_path)
    fulls_completion = load_json(fulls_completion_path)
    dstructure = load_json(dstructure_path)
    firewall = load_json(firewall_path)

    atoms = build_atoms(
        noncanonical=noncanonical,
        entropy_reduction=entropy_reduction,
        support_range=support_range,
        exact_factor_support=exact_factor_support,
        factor_incidence=factor_incidence,
        fulls_completion=fulls_completion,
        dstructure=dstructure,
        firewall=firewall,
    )
    all_boundaries_closed = all(item["boundary_closed"] for item in atoms)
    all_atoms_proved_or_accepted = all(item["proved_or_accepted"] for item in atoms)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_last_remaining_atoms_router",
        "status": "last_remaining_atoms_pinned_logic_chain_closed_conditional_unconditional_open",
        "last_atom_law": (
            "所有非终端分叉已被删除：PDEC/sparse 当前无义务，APSourceLift 与 generic anti-atom 已排除，"
            "full-S 外部路线已完成到模数依赖 completed KLS 原子，DStructure/Rankin 已完成到独立验收原子。"
            "因此证明逻辑链条已经闭合到三个最后原子；完整无条件定理等价于补齐这些原子。"
        ),
        "last_remaining_atom_boundaries_closed": all_boundaries_closed,
        "all_last_atoms_proved_or_accepted": all_atoms_proved_or_accepted,
        "conditional_logic_chain_complete": all_boundaries_closed,
        "row_column_unconditional_closed": False,
        "unconditional_closure_equivalent_to_atoms": [
            item["name"] for item in atoms
        ],
        "conditional_final_theorem": (
            "若 ActualFullSNonAPExactSupportAtom 或 ModulusDependentCompletedFullSKLSInput 之一成立，"
            "并且 DStructureRankinIndependentAcceptance 成立，则在当前无隐藏终端防火墙下，"
            "行/列命题证明逻辑链条完整闭合并可升级为无条件定理。"
        ),
        "current_corpus_verdict": (
            "当前材料已经完成逻辑链条边界闭合，但没有证明或独立接受最后原子；"
            "因此不能声称完整全局无条件定理已证。"
        ),
        "atoms": atoms,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path)
            for path in [
                noncanonical_path,
                entropy_reduction_path,
                support_range_path,
                exact_factor_support_path,
                factor_incidence_path,
                fulls_completion_path,
                dstructure_path,
                firewall_path,
            ]
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 审查报告。"""
    lines: list[str] = [
        "# Prime Matrix 最后剩余原子路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["last_atom_law"],
        "",
        "```text",
        f"last_remaining_atom_boundaries_closed={fmt_bool(result['last_remaining_atom_boundaries_closed'])}",
        f"all_last_atoms_proved_or_accepted={fmt_bool(result['all_last_atoms_proved_or_accepted'])}",
        f"conditional_logic_chain_complete={fmt_bool(result['conditional_logic_chain_complete'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 最后原子表",
        "",
        "| atom | type | boundary_closed | proved_or_accepted | evidence | meaning | minimum_completion |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in result["atoms"]:
        lines.append(
            "| `{name}` | `{type}` | `{boundary}` | `{accepted}` | {evidence} | {meaning} | {minimum} |".format(
                name=table_cell(item["name"]),
                type=table_cell(item["type"]),
                boundary=fmt_bool(item["boundary_closed"]),
                accepted=fmt_bool(item["proved_or_accepted"]),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
                minimum=table_cell(item["minimum_completion"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 条件最终定理",
            "",
            result["conditional_final_theorem"],
            "",
            "## 3. 当前材料判定",
            "",
            result["current_corpus_verdict"],
            "",
            "## 4. 无条件闭合等价原子",
            "",
        ]
    )
    lines.extend(f"- `{item}`" for item in result["unconditional_closure_equivalent_to_atoms"])
    lines.append("")
    md_out.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--noncanonical", type=Path, default=DEFAULT_NONCANONICAL)
    parser.add_argument("--entropy-reduction", type=Path, default=DEFAULT_SOURCE_ENTROPY_REDUCTION)
    parser.add_argument("--support-range", type=Path, default=DEFAULT_SUPPORT_RANGE)
    parser.add_argument("--exact-factor-support", type=Path, default=DEFAULT_EXACT_FACTOR_SUPPORT)
    parser.add_argument("--factor-incidence", type=Path, default=DEFAULT_FACTOR_INCIDENCE)
    parser.add_argument("--fulls-completion", type=Path, default=DEFAULT_FULLS_COMPLETION)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--firewall", type=Path, default=DEFAULT_FIREWALL)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        noncanonical_path=args.noncanonical,
        entropy_reduction_path=args.entropy_reduction,
        support_range_path=args.support_range,
        exact_factor_support_path=args.exact_factor_support,
        factor_incidence_path=args.factor_incidence,
        fulls_completion_path=args.fulls_completion,
        dstructure_path=args.dstructure,
        firewall_path=args.firewall,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["unconditional_closure_equivalent_to_atoms"])


if __name__ == "__main__":
    main()
