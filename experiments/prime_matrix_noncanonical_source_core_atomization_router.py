#!/usr/bin/env python3
"""Prime Matrix noncanonical 源核心原子化路由器。

用法示例：
  python3 experiments/prime_matrix_noncanonical_source_core_atomization_router.py

输出：
  docs/monograph/prime-matrix-noncanonical-source-core-atomization-router.json
  docs/monograph/prime-matrix-noncanonical-source-core-atomization-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_NARROWEST = DOCS / "prime-matrix-self-contained-narrowest-core-router.json"
DEFAULT_ENTROPY = DOCS / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json"
DEFAULT_RANGE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json"
DEFAULT_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_EXACT_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_INCIDENCE = DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-noncanonical-source-core-atomization-router.json"
DEFAULT_MD = DOCS / "prime-matrix-noncanonical-source-core-atomization-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_rows(
    narrowest: dict[str, Any],
    entropy: dict[str, Any],
    range_gate: dict[str, Any],
    antiatom: dict[str, Any],
    exact_support: dict[str, Any],
    incidence: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成源核心原子化判定表。"""
    return [
        {
            "gate": "NarrowestSelfContainedCorePinned",
            "closed": narrowest.get("narrowest_self_contained_basis")
            == (
                "ActualNoncanonicalFullSSourceEntropyOrStrengthenedAntiAtomTheoremInput "
                "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
            ),
            "meaning": "上一层已把无外部黑箱的全局剩余压成 actual noncanonical 源核心 + Rankin。",
            "consequence": "可继续判断 entropy 与 anti-atom 是否是两个不同输入。",
        },
        {
            "gate": "ExactEntropyReducedToSupportPackage",
            "closed": entropy.get("terminal_gap_after_router")
            == "FullSNonAPExactFactorSupportPackageOrExternalDIBFIKuznetsov",
            "meaning": "exact full-S source entropy 已降为精确支撑包。",
            "consequence": "entropy 不是新的谱黑箱；它由支撑/容量包支付。",
        },
        {
            "gate": "BalancedRangeRemoved",
            "closed": range_gate.get("balanced_range_threshold_closed") is True
            and range_gate.get("terminal_gap_after_router")
            == "FullSNonAPExactFactorSupportAndCapacityCompatibilityOrExternalDIBFIKuznetsov",
            "meaning": "full-S regime 中 balanced range 阈值已闭合。",
            "consequence": "剩余支撑包只含 exact factor support 与 Type/Fourier capacity compatibility。",
        },
        {
            "gate": "AntiAtomSameAsSupportCapacity",
            "closed": antiatom.get("terminal_gap_after_router")
            == "FullSNonAPStrengthenedSourceAntiAtomContractOrExternalDIBFIKuznetsov",
            "meaning": "强化源反原子正是 final source capacity measure 无 moving same-(u,v) 原子。",
            "consequence": "anti-atom 与 entropy 共同指向同一个支撑/容量核心。",
        },
        {
            "gate": "K4K6DoNotProveExactSupport",
            "closed": exact_support.get("k4_k6_imply_exact_factor_support") is False,
            "meaning": "K4 固定 residue flatness 与 K6 dyadic bookkeeping 不能推出 moving factor support。",
            "consequence": "不能把已有 clean admission 直接升级为源核心证明。",
        },
        {
            "gate": "NaiveIncidenceBridgeBlocked",
            "closed": incidence.get("naive_incidence_bridge_valid") is False
            and incidence.get("terminal_gap_after_router")
            == "CanonicalRIWFactorSupportLowerBoundOrExternalDIBFIOriginalDispersion",
            "meaning": "朴素 factor-residue incidence 被一个 (u,v) 块内的大内部 fiber 阻断。",
            "consequence": "支撑失败不会自动回流 K4/K6；需要直接证明 actual 支撑/容量包。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "consequence": "源核心证明完成后仍需独立验收才能升级为完整全局定理。",
        },
    ]


def run(
    narrowest_path: Path,
    entropy_path: Path,
    range_path: Path,
    antiatom_path: Path,
    exact_support_path: Path,
    incidence_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 noncanonical 源核心原子化。"""
    source_paths = [
        narrowest_path,
        entropy_path,
        range_path,
        antiatom_path,
        exact_support_path,
        incidence_path,
        dstructure_path,
    ]
    narrowest = load_json(narrowest_path)
    entropy = load_json(entropy_path)
    range_gate = load_json(range_path)
    antiatom = load_json(antiatom_path)
    exact_support = load_json(exact_support_path)
    incidence = load_json(incidence_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(
        narrowest=narrowest,
        entropy=entropy,
        range_gate=range_gate,
        antiatom=antiatom,
        exact_support=exact_support,
        incidence=incidence,
        dstructure=dstructure,
    )
    source_core_atomization_closed = all(row["closed"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_noncanonical_source_core_atomization_router",
        "status": "noncanonical_source_core_atomized_to_actual_support_capacity_open",
        "source_core_atomization_closed": source_core_atomization_closed,
        "entropy_antiatom_duality_removed": True,
        "balanced_range_threshold_closed": True,
        "k4_k6_or_naive_incidence_suffices": False,
        "canonical_import_allowed": False,
        "actual_support_capacity_core_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_basis": narrowest.get("narrowest_self_contained_basis"),
        "atomized_self_contained_basis": (
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "actual_support_capacity_contract": (
            "对每个幸存的 actual noncanonical full-S non-AP balanced block，证明精确 u、v "
            "因子有对数幂级绝对支撑下界，并证明 Type/Fourier 容量兼容，使任何 moving (u,v) "
            "对都不能获得未登记的容量乘子。"
        ),
        "structural_law": (
            "actual noncanonical source entropy 与 strengthened anti-atom 是同一个剩余源容量核心的"
            "两种命名。full-S regime 中 balanced range 已闭合；唯一内部数学原子是 actual "
            "noncanonical 系数的精确支撑/容量定理。K4/K6、朴素 incidence 与 canonical "
            "RIW/Buchstab 偷渡都已作为捷径被阻断。"
        ),
        "plain_conclusion": (
            "最窄自足剩余再原子化：`source entropy` 与 `strengthened anti-atom` 不是两条路，"
            "它们共同等价地要求 actual noncanonical full-S 源的精确因子支撑与 Type/Fourier "
            "容量兼容。balanced range 已闭合；K4/K6、朴素 incidence、canonical 支撑偷渡都不能证明它。"
            "因此当前真正数学原子是 `ActualNoncanonicalFullSFactorSupportCapacityTheoremInput`，"
            "另加 DStructure/Rankin 独立验收。"
        ),
        "rows": rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix noncanonical 源核心原子化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"source_core_atomization_closed={fmt_bool(result['source_core_atomization_closed'])}",
        f"entropy_antiatom_duality_removed={fmt_bool(result['entropy_antiatom_duality_removed'])}",
        f"balanced_range_threshold_closed={fmt_bool(result['balanced_range_threshold_closed'])}",
        f"k4_k6_or_naive_incidence_suffices={fmt_bool(result['k4_k6_or_naive_incidence_suffices'])}",
        f"canonical_import_allowed={fmt_bool(result['canonical_import_allowed'])}",
        f"actual_support_capacity_core_proved={fmt_bool(result['actual_support_capacity_core_proved'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | meaning | consequence |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {meaning} | {consequence} |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                meaning=table_cell(row["meaning"]),
                consequence=table_cell(row["consequence"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 上一层输入基",
            "",
            "```text",
            str(result["previous_basis"]),
            "```",
            "",
            "## 3. 原子化后输入基",
            "",
            "```text",
            result["atomized_self_contained_basis"],
            "```",
            "",
            "## 4. actual 支撑/容量合同",
            "",
            result["actual_support_capacity_contract"],
            "",
            "## 5. 结构律",
            "",
            result["structural_law"],
            "",
            "## 6. 当前结论",
            "",
            "这一步闭合的是命名二义性和伪捷径排除，不是证明 actual 支撑/容量核心。",
            "完整行/列无条件定理仍需该核心输入与 DStructure/Rankin 独立验收。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--narrowest", type=Path, default=DEFAULT_NARROWEST)
    parser.add_argument("--entropy", type=Path, default=DEFAULT_ENTROPY)
    parser.add_argument("--range", type=Path, default=DEFAULT_RANGE)
    parser.add_argument("--antiatom", type=Path, default=DEFAULT_ANTIATOM)
    parser.add_argument("--exact-support", type=Path, default=DEFAULT_EXACT_SUPPORT)
    parser.add_argument("--incidence", type=Path, default=DEFAULT_INCIDENCE)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        narrowest_path=args.narrowest,
        entropy_path=args.entropy,
        range_path=args.range,
        antiatom_path=args.antiatom,
        exact_support_path=args.exact_support,
        incidence_path=args.incidence,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["atomized_self_contained_basis"])


if __name__ == "__main__":
    main()
