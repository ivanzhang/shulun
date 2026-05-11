#!/usr/bin/env python3
"""生成 strict acyclic 终端家族主攻路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_terminal_family_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-terminal-family-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-terminal-family-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-terminal-family-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-global-terminal-scope-router.md",
    "prime-matrix-strict-high-tail-corpus-reconciliation-router.md",
    "prime-matrix-global-pdec-sparse-terminal-split-reconciliation-router.md",
    "prime-matrix-current-terminal-promotion-reconciliation-router.md",
    "prime-matrix-pdec-cap-same-set-global-dual-router.md",
    "prime-matrix-pdec-cap-sc9-boundary-reconciliation-router.md",
    "prime-matrix-triad-a1-terminal-confluence-router.md",
    "prime-matrix-profinite-actual-payment-stitching-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    terminal_before = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily"
    terminal_after = (
        "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary "
        "OR DirectAcyclicSameSetPDECCapDualCertificate "
        "OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )
    strict_basis_with_internal_high_tail = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"({terminal_after}) AND "
        "(SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 AND "
        "SelfContainedMeisselMertensConstantIntervalLedgerAt20000) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )
    strict_basis_with_external_mertens = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"({terminal_after}) AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "StrictAcyclicTerminalFamilyGateActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层 strict 基的全局终端门是 acyclic noncanonical 口径下的 PDEC-CAP 或内部 CleanKLS。",
            "remaining": terminal_before,
        },
        {
            "gate": "GlobalSplitImportedButNotProof",
            "closed": True,
            "proved": True,
            "meaning": "GlobalPDECorSparseTerminalExclusion 已被拆成 PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve。",
            "remaining": "拆分不是排斥证明，仍需同作用域终端估计。",
        },
        {
            "gate": "CanonicalPromotionAvailableOnlyUnderCanonicalSource",
            "closed": True,
            "proved": True,
            "meaning": "canonical-source 分支内 PDEC-CAP/CleanKLS 已可接到 NoFurtherCanonicalSourceTerminalPromotionGap。",
            "remaining": "不能直接导入 acyclic noncanonical 分支。",
        },
        {
            "gate": "CanonicalImportRequiresLock",
            "closed": True,
            "proved": False,
            "meaning": "若要复用 canonical 闭合，必须证明每个 acyclic terminal certificate 保持同集质量、formal unit 和层转移地嵌入 canonical-source 边界。",
            "remaining": "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary。",
        },
        {
            "gate": "DirectPDECCapAlternativePinned",
            "closed": True,
            "proved": False,
            "meaning": "不走 canonical-lock 时，可直接对 acyclic terminal family 证明同一坏窗集合上的 U_CRT<L_PDEC 对偶证书。",
            "remaining": "DirectAcyclicSameSetPDECCapDualCertificate。",
        },
        {
            "gate": "DirectCleanKLSAlternativePinned",
            "closed": True,
            "proved": False,
            "meaning": "若 terminal family 为 diffuse clean residual，则必须证明 K1--K9 准入后内部 KLS/DLS 大筛吸收，失败要命名回流 PDEC/SAE/ColumnCRT。",
            "remaining": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn。",
        },
        {
            "gate": "ExternalDIBFINotStrictSelfContained",
            "closed": True,
            "proved": False,
            "meaning": "generic DI/BFI/Kuznetsov 可作为外部条件线，但不能关闭 strict 自足终端门。",
            "remaining": "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY。",
        },
        {
            "gate": "AcyclicTerminalFamilyReducedToThreeAtoms",
            "closed": True,
            "proved": False,
            "meaning": "宽终端门被压成 canonical-lock、直接 PDEC 对偶、直接 CleanKLS 三个互斥主攻方向。",
            "remaining": terminal_after,
        },
        {
            "gate": "StrictAcyclicTerminalFamilyCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前仓库尚未证明三者之一，故 strict acyclic terminal family 仍未闭合。",
            "remaining": terminal_after,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "即便接受外部 Mertens 解析线，完整 strict 链还需 acyclic seed、终端三选一和 DStructure/Rankin 替代门。",
            "remaining": strict_basis_with_external_mertens,
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_terminal_family_attack_router",
        "status": "strict_acyclic_terminal_family_reduced_to_canonical_lock_or_direct_dual_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_acyclic_terminal_family_boundary_refined": True,
        "canonical_promotion_scope_guard_preserved": True,
        "acyclic_terminal_canonical_lock_proved": False,
        "direct_acyclic_same_set_pdec_dual_proved": False,
        "direct_acyclic_clean_kls_dls_proved": False,
        "strict_terminal_family_proved": False,
        "acyclic_pre_cauchy_seed_proved": False,
        "self_contained_dstructure_rankin_replacement_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": terminal_before,
        "terminal_gap_after_router": terminal_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_internal_high_tail,
        "with_external_mertens_high_tail_removed_basis": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "AcyclicTerminalCanonicalLock_THEN_DirectDualIfLockFails",
            "first_priority": "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary",
            "fallback_priority": "DirectAcyclicSameSetPDECCapDualCertificate",
            "parallel_priority": "DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
            "must_preserve": [
                "同一 formal unit",
                "同一坏窗集合",
                "同一推前质量 U_CRT 与 L_PDEC",
                "不从真实零行缺席取证",
                "不把 canonical-source 闭合直接导入 noncanonical 分支",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步继续主攻 strict acyclic 终端家族。已有 canonical-source PDEC/CleanKLS 闭合不能直接偷渡；"
            "要么证明 acyclic terminal certificates canonical-lock 到 canonical-source 边界，要么直接证明 acyclic 同集 PDEC 对偶，"
            "要么直接证明 acyclic clean residual 的内部 KLS/DLS 大筛吸收并把失败命名回流。"
            "这把宽口径终端门压成三个可审稿原子，但当前仍未完成其中任何一个。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic 终端家族主攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_acyclic_terminal_family_boundary_refined={str(result['strict_acyclic_terminal_family_boundary_refined']).lower()}",
        f"canonical_promotion_scope_guard_preserved={str(result['canonical_promotion_scope_guard_preserved']).lower()}",
        f"acyclic_terminal_canonical_lock_proved={str(result['acyclic_terminal_canonical_lock_proved']).lower()}",
        f"direct_acyclic_same_set_pdec_dual_proved={str(result['direct_acyclic_same_set_pdec_dual_proved']).lower()}",
        f"direct_acyclic_clean_kls_dls_proved={str(result['direct_acyclic_clean_kls_dls_proved']).lower()}",
        f"strict_terminal_family_proved={str(result['strict_terminal_family_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 三选一主攻口",
        "",
        "原终端门：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "压缩后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
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
                gate=row["gate"],
                closed=str(row["closed"]).lower(),
                proved=str(row["proved"]).lower(),
                meaning=row["meaning"],
                remaining=row["remaining"],
            )
        )

    contract = result["next_attack_contract"]
    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "严格自足基：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "若接受外部 Mertens/theta 显式定理，高段解析缺口移出后：",
            "",
            "```text",
            result["with_external_mertens_high_tail_removed_basis"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            f"主攻名：`{contract['name']}`。",
            "",
            f"- 第一优先：`{contract['first_priority']}`。",
            f"- 失败回退：`{contract['fallback_priority']}`。",
            f"- 并行备线：`{contract['parallel_priority']}`。",
            "",
            "必须保持：",
        ]
    )
    for item in contract["must_preserve"]:
        lines.append(f"- {item}。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
