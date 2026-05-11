#!/usr/bin/env python3
"""生成严格 moving-atom 到全局终端门的路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_moving_atom_to_global_terminal_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-moving-atom-to-global-terminal-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-moving-atom-to-global-terminal-router.json"
OUT_MD = DOCS / "prime-matrix-strict-moving-atom-to-global-terminal-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.md",
    "prime-matrix-counterexample-moving-block-terminal-router.md",
    "prime-matrix-early-zero-terminal-schema-reconciliation-router.md",
    "prime-matrix-moving-block-dprc-ledger-compatibility-router.md",
    "prime-matrix-clean-core-terminal-normal-form-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    rows = [
        {
            "gate": "StrictMovingAtomInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层严格源侧剩余包含 Acyclic seed 与 ActualNoncanonicalCleanCoreMovingAtomExclusion。",
            "remaining": "攻击 moving atom 排斥本身。",
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步仍只在 Assume EarlyZeroRowWithinP 的假设链条内推理，不用真实样本缺席。",
            "remaining": "所有输出必须是反例链内的命名终端或账本。",
        },
        {
            "gate": "AcyclicSeedOnlyProvidesObject",
            "closed": True,
            "proved": True,
            "meaning": "无环 source seed 只保证 actual source 对象准入；它本身不排斥 moving atom。",
            "remaining": "moving atom 若存在，必须继续通过终端回流测试。",
        },
        {
            "gate": "MovingBlockTerminalReductionImported",
            "closed": True,
            "proved": True,
            "meaning": "actual same-(u,v) moving block 有低维签名则进 PDEC/SAE/ColumnCRT；无签名则进早期零行终端包。",
            "remaining": "EarlyZeroTerminalExclusionPackage。",
        },
        {
            "gate": "EarlyZeroPackageReconciledImported",
            "closed": True,
            "proved": True,
            "meaning": "抽象 EarlyZeroTerminalExclusionPackage 已与命名 schema 调和，收缩为 GlobalPDECorSparseTerminalExclusion。",
            "remaining": "GlobalPDECorSparseTerminalExclusion。",
        },
        {
            "gate": "DPRCCompatibilityImported",
            "closed": True,
            "proved": True,
            "meaning": "ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock 已闭合为接口事实，可删除该兼容性门。",
            "remaining": "ExplicitModelGapAndFiniteDPRCLedger 仍保留为独立账本。",
        },
        {
            "gate": "MovingAtomExclusionReducedToGlobalTerminal",
            "closed": True,
            "proved": True,
            "meaning": "在反例链内，排斥 clean-core moving atom 足以转为排斥全局 PDEC/sparse 终端证书并支付模型账本。",
            "remaining": "GlobalPDECorSparseTerminalExclusion AND ExplicitModelGapAndFiniteDPRCLedger。",
        },
        {
            "gate": "GlobalTerminalCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料尚未无条件排斥已物化的 persistent PDEC、ColumnCRT、SAE/LocalSurvivor 或 sparse packet 终端证书。",
            "remaining": "GlobalPDECorSparseTerminalExclusion。",
        },
        {
            "gate": "ExplicitModelGapDPRCCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "模型余量/有限 DPRC 账本自身仍未闭合。",
            "remaining": "ExplicitModelGapAndFiniteDPRCLedger。",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_moving_atom_to_global_terminal_router",
        "status": "strict_moving_atom_reduced_to_global_terminal_and_model_dprc_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_moving_atom_boundary_closed": True,
        "moving_block_terminal_reduction_imported": True,
        "early_zero_schema_reconciliation_imported": True,
        "dprc_compatibility_gate_removed": True,
        "acyclic_pre_cauchy_seed_proved": False,
        "clean_core_moving_atom_exclusion_proved": False,
        "global_pdec_sparse_terminal_exclusion_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "ActualNoncanonicalCleanCoreMovingAtomExclusion"
        ),
        "terminal_gap_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "GlobalPDECorSparseTerminalExclusion AND "
            "ExplicitModelGapAndFiniteDPRCLedger"
        ),
        "strict_self_contained_math_basis_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "GlobalPDECorSparseTerminalExclusion AND "
            "ExplicitModelGapAndFiniteDPRCLedger AND "
            "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
        ),
        "next_attack_contract": {
            "name": "GlobalPDECorSparseTerminalExclusion_WITH_ExplicitModelGapAndFiniteDPRC",
            "must_prove": [
                "排斥已物化的 persistent primitive PDEC 终端证书，或给出全量 PDEC 容量上界",
                "排斥 ColumnCRT/位移/endpoint/cofactor 终端证书，或证明其必回流到 PDEC/SAE",
                "排斥 SAE/LocalSurvivor/sparse packet 终端证书，或提交有限全集 extractor",
                "闭合 P<2003 有限 DPRC 证书与 P>=2003 模型余量账本",
                "保持所有步骤在假设早期零行反例链内，不使用真实样本缺席",
            ],
            "cannot_use_as_proof": [
                "把 acyclic source seed 当作 moving atom 排斥",
                "把 EarlyZeroTerminalExclusionPackage 当作已排斥",
                "重复引用已删除的 ExactModelGapAndDPRCLedgerCompatibilityForMovingBlock",
                "把外部 KLS/DI/BFI 作为严格自足证明",
                "把命名回流 schema 当作终端家族不存在的证明",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "严格 moving-atom 输入已经接回反例链：若 acyclic source seed 下仍存在 clean-core moving atom，"
            "它作为 actual same-(u,v) moving block 必须进入已登记的低维签名终端，或无签名 L2-flat 终端包；"
            "抽象 EarlyZeroTerminalExclusionPackage 已被后续 schema 调和为 GlobalPDECorSparseTerminalExclusion，"
            "而 moving-block 专属 DPRC 兼容门已闭合并可删除。因此 moving atom 排斥不再是当前最窄项；"
            "剩余转为 GlobalPDECorSparseTerminalExclusion 与 ExplicitModelGapAndFiniteDPRCLedger，另保留 acyclic source seed "
            "和自足 DStructure/Rankin 替代包。当前仍没有无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix 严格 moving-atom 到全局终端门路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"strict_moving_atom_boundary_closed={str(result['strict_moving_atom_boundary_closed']).lower()}",
        f"dprc_compatibility_gate_removed={str(result['dprc_compatibility_gate_removed']).lower()}",
        f"acyclic_pre_cauchy_seed_proved={str(result['acyclic_pre_cauchy_seed_proved']).lower()}",
        f"global_pdec_sparse_terminal_exclusion_proved={str(result['global_pdec_sparse_terminal_exclusion_proved']).lower()}",
        f"explicit_model_gap_and_finite_dprc_ledger_proved={str(result['explicit_model_gap_and_finite_dprc_ledger_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 压缩链",
        "",
        "```text",
        "ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "  -> actual same-(u,v) moving block contradiction branch",
        "  -> EarlyZeroTerminalExclusionPackage",
        "  -> GlobalPDECorSparseTerminalExclusion",
        "  -> ExplicitModelGapAndFiniteDPRCLedger remains independent",
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
            "## 3. 下一主攻合同",
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

    lines.extend(
        [
            "",
            "严格自足数学基更新为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
