#!/usr/bin/env python3
"""生成 strict exact entropy 源律防火墙路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_exact_entropy_source_law_firewall_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-exact-entropy-source-law-firewall-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
OUT_MD = DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-moving-atom-entropy-normal-form-router.md",
    "prime-matrix-triad-a1-moving-block-spread-obstruction.md",
    "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.md",
    "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.md",
    "prime-matrix-strict-actual-source-support-seed-router.md",
    "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.md",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.md",
]


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_result() -> dict[str, Any]:
    """构造 exact entropy 源律防火墙证书。"""
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    canonical_lock = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    exact_entropy = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
    source_law = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    completed_kls = "ModulusDependentCompletedFullSKLSInput"
    terminal_after = f"{canonical_lock} OR {source_law}"
    conditional_after = f"{terminal_after} OR {completed_kls}"
    high_tail = (
        "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
    )
    strict_basis = (
        f"({terminal_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    conditional_basis = (
        f"({conditional_after}) AND ({high_tail}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    external_mertens_basis = (
        f"({terminal_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "ExactEntropyInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 clean-core moving atom 排斥标准化为 exact clean-core source entropy。",
            "remaining": exact_entropy,
        },
        {
            "gate": "FixedProjectionRouteBlocked",
            "closed": True,
            "proved": True,
            "meaning": "固定投影 diffuse 只控制固定签名总质量，不控制随尺度移动的 same-(u,v) hidden fiber。",
            "remaining": source_law,
        },
        {
            "gate": "FormalWFDRouteRefuted",
            "closed": True,
            "proved": True,
            "meaning": "moving-delta 反模型满足当前 formal WFD/Type/Fourier 模板但违反 log-power 反原子。",
            "remaining": source_law,
        },
        {
            "gate": "K4K6AndIncidenceRouteBlocked",
            "closed": True,
            "proved": True,
            "meaning": "K4/K6 投影平坦和朴素 factor-residue incidence 均看不见同一 moving block 内部 fiber。",
            "remaining": source_law,
        },
        {
            "gate": "ZeroRowGeometryRouteBlocked",
            "closed": True,
            "proved": True,
            "meaning": "早期零行、斜线覆盖、圆柱环绕和层叠筛只给 unsigned 覆盖/预算结构，不能生成 actual source entropy。",
            "remaining": source_law,
        },
        {
            "gate": "PairMassReductionIsEquivalenceNotProof",
            "closed": True,
            "proved": True,
            "meaning": "ExactUV pair-mass 分散失败等价于 moving atom；该等价只回收对象，不排斥对象。",
            "remaining": source_law,
        },
        {
            "gate": "CanonicalImportRouteBlocked",
            "closed": True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 支撑链只服务 canonical 分支，不能导入 noncanonical exact entropy。",
            "remaining": canonical_lock + " OR " + source_law,
        },
        {
            "gate": "ExactEntropySourceLawPinned",
            "closed": True,
            "proved": False,
            "meaning": "strict 自足 noncanonical 源侧剩余已经是一个新的 actual-source entropy 定理，而非形式筛法推论。",
            "remaining": source_law,
        },
        {
            "gate": "ExternalCompletedKLSStillConditional",
            "closed": True,
            "proved": False,
            "meaning": "completed full-S KLS 可作为条件外部线，但不是 strict 自足证明。",
            "remaining": completed_kls,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "仍缺 canonical-lock 或新 actual-source entropy 定理、高段自足尾项或外部接受、DStructure/Rankin 替代包。",
            "remaining": strict_basis,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_exact_entropy_source_law_firewall_router",
        "status": "strict_exact_entropy_pinned_as_new_actual_source_law_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "exact_entropy_source_law_firewall_closed": True,
        "fixed_projection_route_blocked": True,
        "formal_wfd_route_refuted": True,
        "k4k6_incidence_route_blocked": True,
        "zero_row_geometry_route_blocked": True,
        "pair_mass_equivalence_not_proof": True,
        "canonical_import_route_blocked": True,
        "new_actual_source_entropy_theorem_proved": False,
        "exact_clean_core_source_entropy_proved": False,
        "external_completed_kls_accepted": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "strict_acyclic_terminal_family_proved": False,
        "strict_terminal_family_proved": False,
        "self_contained_mertens_tail_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "strict_self_contained_terminal_after_router": terminal_after,
        "conditional_external_terminal_after_router": conditional_after,
        "strict_self_contained_math_basis_after_router": strict_basis,
        "conditional_external_math_basis_after_router": conditional_basis,
        "with_external_mertens_high_tail_removed_basis": external_mertens_basis,
        "next_attack_contract": {
            "name": "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem_OR_AcyclicTerminalCanonicalLock",
            "must_prove": [
                "新增并证明 actual clean-core full-S non-AP WFD 源熵定理：max_b M_b/M <= log^{-2A}",
                "或完成 canonical-lock：同集推前、有限因子图、无 noncanonical payload 残留",
                "若走外部线，明确接受/证明 ModulusDependentCompletedFullSKLSInput",
                "继续独立处理高段 Mertens/PNT 与 DStructure/Rankin 替代包",
            ],
            "cannot_use_as_proof": [
                "固定投影 diffuse",
                "formal WFD/Type/Fourier 模板",
                "K4/K6 投影平坦或朴素 incidence",
                "早期零行覆盖几何或数值缺席",
                "canonical-source 分支支撑链",
                "ExactUV/moving-atom 的等价命名本身",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "`ExactCleanCoreFullSNonAPWFDSourceEntropy` 继续硬攻后，所有当前可用的结构捷径都被防火墙阻断："
            "固定投影不控制 moving hidden fiber，formal WFD/Type/Fourier 被 moving-delta 反模型反证，"
            "K4/K6 与朴素 incidence 看不见同块内部 fiber，早期零行几何不能生成 signed source entropy，"
            "canonical 支撑链不能导入 noncanonical 分支。因此 strict 自足线的 noncanonical 侧剩余被精确命名为 "
            "`NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。这不是已证定理；它是当前真正的源侧新输入。"
            "当前 strict 终端为 `AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
            "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict exact entropy 源律防火墙路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_entropy_source_law_firewall_closed={fmt_bool(result['exact_entropy_source_law_firewall_closed'])}",
        f"fixed_projection_route_blocked={fmt_bool(result['fixed_projection_route_blocked'])}",
        f"formal_wfd_route_refuted={fmt_bool(result['formal_wfd_route_refuted'])}",
        f"k4k6_incidence_route_blocked={fmt_bool(result['k4k6_incidence_route_blocked'])}",
        f"zero_row_geometry_route_blocked={fmt_bool(result['zero_row_geometry_route_blocked'])}",
        f"pair_mass_equivalence_not_proof={fmt_bool(result['pair_mass_equivalence_not_proof'])}",
        f"canonical_import_route_blocked={fmt_bool(result['canonical_import_route_blocked'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"strict_self_contained_terminal_after_router={result['strict_self_contained_terminal_after_router']}",
        "```",
        "",
        "## 1. 防火墙链",
        "",
        "```text",
        "ExactCleanCoreFullSNonAPWFDSourceEntropy",
        "  not from fixed projection",
        "  not from formal WFD/Type/Fourier",
        "  not from K4/K6 or naive incidence",
        "  not from early-zero geometry",
        "  not from canonical-source import",
        "  not from equivalence naming alone",
        "  -> NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem",
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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

    contract = result["next_attack_contract"]
    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "严格自足基更新为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "条件外部线可写为：",
            "",
            "```text",
            result["conditional_external_math_basis_after_router"],
            "```",
            "",
            "若明确接受外部 Mertens/theta 显式输入，高段尾项可暂时移出活动缺口，剩：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            f"下一数学主攻点：`{contract['name']}`。",
            "",
            "必须证明：",
        ]
    )
    for item in contract["must_prove"]:
        lines.append(f"- {item}。")

    lines.extend(["", "不能作为证明使用："])
    for item in contract["cannot_use_as_proof"]:
        lines.append(f"- {item}。")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
