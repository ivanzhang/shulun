#!/usr/bin/env python3
"""Prime Matrix 完全自足最窄核心路由器。

用法示例：
  python3 experiments/prime_matrix_self_contained_narrowest_core_router.py

输出：
  docs/monograph/prime-matrix-self-contained-narrowest-core-router.json
  docs/monograph/prime-matrix-self-contained-narrowest-core-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_COMMON = DOCS / "prime-matrix-dual-lane-common-core-reconciliation-router.json"
DEFAULT_PROVENANCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_BRIDGE = DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
DEFAULT_NONCANONICAL = DOCS / "prime-matrix-noncanonical-final-narrowing-router.json"
DEFAULT_ANTIATOM_NOGO = (
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json"
)
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-self-contained-narrowest-core-router.json"
DEFAULT_MD = DOCS / "prime-matrix-self-contained-narrowest-core-router.md"


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
    common: dict[str, Any],
    provenance: dict[str, Any],
    bridge: dict[str, Any],
    noncanonical: dict[str, Any],
    antiatom_nogo: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成最窄核心判定表。"""
    return [
        {
            "gate": "SelfContainedBasisPinned",
            "closed": common.get("self_contained_basis_without_external_black_box")
            == (
                "ActualA1FullSSourceLockOrNewFullSNonAPSourceAntiAtomTheoremInput "
                "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
            ),
            "meaning": "上一轮已经去掉外部黑箱，把完全自足版压到 source-lock/新反原子 + Rankin。",
            "consequence": "可以继续检查 source-lock 这一支是否仍属于全局剩余。",
        },
        {
            "gate": "CanonicalSourceLockAbsorbed",
            "closed": provenance.get("actual_source_provenance_closed") is True
            and provenance.get("terminal_gap_after_router") == "NoFurtherActualSourceProvenanceGap",
            "meaning": "canonical RIW/Buchstab 分支的 actual source provenance 已闭合。",
            "consequence": "source-lock 不是 canonical 分支内的新缺口。",
        },
        {
            "gate": "CanonicalLockDoesNotCloseGlobalComplement",
            "closed": bridge.get("actual_source_bridge_closed_for_canonical_branch") is True
            and bridge.get("actual_source_bridge_closes_global_unrestricted") is False,
            "meaning": "canonical 分支闭合不等于 unrestricted/global full-S noncanonical 补集闭合。",
            "consequence": "全局完全自足剩余必须落到 noncanonical actual-source 核心。",
        },
        {
            "gate": "GenericSelfContainedAntiAtomUnavailable",
            "closed": antiatom_nogo.get("self_contained_generic_version_refuted") is True
            and antiatom_nogo.get("self_contained_generic_version_closed_as_proof") is False,
            "meaning": "generic full-S 自足反原子已被 moving-delta 模型反证。",
            "consequence": "不能用宽 generic WFD/Type/Fourier 模板补这个洞。",
        },
        {
            "gate": "NoncanonicalActualCorePinned",
            "closed": noncanonical.get("noncanonical_narrowing_boundary_closed") is True
            and noncanonical.get("self_contained_noncanonical_closed") is False
            and noncanonical.get("exact_source_entropy_closed") is False,
            "meaning": "noncanonical 补集已压成实际源 exact entropy / strengthened anti-atom。",
            "consequence": "真正自足数学输入变成 actual noncanonical source theorem。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "consequence": "即使 source core 证明完成，也还要独立验收才能升级全局定理。",
        },
    ]


def run(
    common_path: Path,
    provenance_path: Path,
    bridge_path: Path,
    noncanonical_path: Path,
    antiatom_nogo_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行最窄核心路由。"""
    source_paths = [
        common_path,
        provenance_path,
        bridge_path,
        noncanonical_path,
        antiatom_nogo_path,
        dstructure_path,
    ]
    common = load_json(common_path)
    provenance = load_json(provenance_path)
    bridge = load_json(bridge_path)
    noncanonical = load_json(noncanonical_path)
    antiatom_nogo = load_json(antiatom_nogo_path)
    dstructure = load_json(dstructure_path)

    rows = build_rows(
        common=common,
        provenance=provenance,
        bridge=bridge,
        noncanonical=noncanonical,
        antiatom_nogo=antiatom_nogo,
        dstructure=dstructure,
    )
    narrowest_core_reduction_closed = all(row["closed"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_self_contained_narrowest_core_router",
        "status": "self_contained_narrowest_core_reduced_to_noncanonical_actual_source_open",
        "narrowest_core_reduction_closed": narrowest_core_reduction_closed,
        "canonical_source_lock_absorbed_for_canonical_branch": True,
        "source_lock_option_removed_from_global_remainder": True,
        "external_black_box_used": False,
        "generic_self_contained_antiatom_available": False,
        "noncanonical_actual_source_core_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_self_contained_basis": common.get(
            "self_contained_basis_without_external_black_box"
        ),
        "narrowest_self_contained_basis": (
            "ActualNoncanonicalFullSSourceEntropyOrStrengthenedAntiAtomTheoremInput "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "noncanonical_source_core_contract": (
            "Prove exact source entropy / no moving same-(u,v) atom for the actual "
            "noncanonical full-S non-AP WFD coefficients, not for an unrestricted "
            "generic WFD template."
        ),
        "structural_law": (
            "完全自足路线中的 source-lock 选项已经被 canonical RIW/Buchstab 分支吸收。"
            "它不能关闭 global/unrestricted noncanonical 补集；而 generic 自足反原子又被 "
            "moving-delta 反证。因此全局完全自足数学剩余不再是 "
            "ActualA1FullSSourceLock OR generic anti-atom，而是 actual noncanonical "
            "full-S source entropy / strengthened anti-atom。"
        ),
        "plain_conclusion": (
            "最后自足剩余又窄了一层：canonical source-lock 已经不是全局剩余，"
            "它只关闭 canonical 分支；外部黑箱被排除后，真正剩余是证明 actual noncanonical "
            "full-S non-AP 源没有 moving same-(u,v) 大原子，或等价证明 exact source entropy。"
            "此外 DStructure/Rankin 晋级验收仍独立开放。"
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
        "# Prime Matrix 完全自足最窄核心路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"narrowest_core_reduction_closed={fmt_bool(result['narrowest_core_reduction_closed'])}",
        f"canonical_source_lock_absorbed_for_canonical_branch={fmt_bool(result['canonical_source_lock_absorbed_for_canonical_branch'])}",
        f"source_lock_option_removed_from_global_remainder={fmt_bool(result['source_lock_option_removed_from_global_remainder'])}",
        f"external_black_box_used={fmt_bool(result['external_black_box_used'])}",
        f"generic_self_contained_antiatom_available={fmt_bool(result['generic_self_contained_antiatom_available'])}",
        f"noncanonical_actual_source_core_proved={fmt_bool(result['noncanonical_actual_source_core_proved'])}",
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
            "## 2. 上一层完全自足输入基",
            "",
            "```text",
            str(result["previous_self_contained_basis"]),
            "```",
            "",
            "## 3. 最新最窄完全自足输入基",
            "",
            "```text",
            result["narrowest_self_contained_basis"],
            "```",
            "",
            "## 4. noncanonical 源核心合同",
            "",
            result["noncanonical_source_core_contract"],
            "",
            "## 5. 结构律",
            "",
            result["structural_law"],
            "",
            "## 6. 当前结论",
            "",
            "这一步删除了 source-lock 作为 global/unrestricted 剩余的歧义。",
            "它没有证明 actual noncanonical source entropy，也没有完成 DStructure/Rankin 独立验收。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--common", type=Path, default=DEFAULT_COMMON)
    parser.add_argument("--provenance", type=Path, default=DEFAULT_PROVENANCE)
    parser.add_argument("--bridge", type=Path, default=DEFAULT_BRIDGE)
    parser.add_argument("--noncanonical", type=Path, default=DEFAULT_NONCANONICAL)
    parser.add_argument("--antiatom-nogo", type=Path, default=DEFAULT_ANTIATOM_NOGO)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        common_path=args.common,
        provenance_path=args.provenance,
        bridge_path=args.bridge,
        noncanonical_path=args.noncanonical,
        antiatom_nogo_path=args.antiatom_nogo,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["narrowest_self_contained_basis"])


if __name__ == "__main__":
    main()
