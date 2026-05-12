#!/usr/bin/env python3
"""生成严格 pair-mass 分散到 moving-atom 终端的对齐证书。

用法示例：
  python3 experiments/prime_matrix_strict_pair_mass_dispersion_to_moving_atom_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json"
OUT_MD = DOCS / "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-actual-source-support-seed-router.md",
    "prime-matrix-exact-uv-support-failure-packetization-router.md",
    "prime-matrix-support-failure-packet-return-dichotomy-router.md",
    "prime-matrix-clean-core-moving-atom-sharp-input-router.md",
    "prime-matrix-clean-core-terminal-normal-form-router.md",
    "prime-matrix-registered-capacity-multiplier-discipline-router.md",
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
            "gate": "PairMassDispersionInputActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层把 ExactUV 支撑数值负担压成 exact pair 最大原子/能量控制。",
            "remaining": "判断 pair-mass 分散失败是否是新终端。",
        },
        {
            "gate": "LargePairAtomEquivalenceClosed",
            "closed": True,
            "proved": True,
            "meaning": "最大 pair 界失败等价于存在同一 formal unit 内的 sign-refined exact (u,v) 大原子。",
            "remaining": "把该大原子接入已登记容量与回流字母表。",
        },
        {
            "gate": "RegisteredMultiplierBridgeImported",
            "closed": True,
            "proved": True,
            "meaning": "Type/Fourier/fiber 乘子纪律已闭合，exact pair 质量阈值可与最终容量大原子阈值对齐。",
            "remaining": "桥接不排斥大原子，只防止账外乘子解释。",
        },
        {
            "gate": "FailurePacketReturnAlphabetImported",
            "closed": True,
            "proved": True,
            "meaning": "非 clean-core 的大原子必须回流到 finite sparse、PDEC、SAE/ColumnCRT、CleanKLS/DLS 或外部谱分支。",
            "remaining": "只剩通过全部回流测试的 clean-core moving atom。",
        },
        {
            "gate": "CleanCoreMovingAtomNormalFormImported",
            "closed": True,
            "proved": True,
            "meaning": "clean-core 大 pair 原子的 sharp 标准形是 ActualNoncanonicalCleanCoreMovingAtomExclusion，内部等价为 exact clean-core source entropy。",
            "remaining": "证明 moving atom 排斥或 exact source entropy。",
        },
        {
            "gate": "PairMassDispersionNotSeparateTerminal",
            "closed": True,
            "proved": True,
            "meaning": "ExactUVPairMassDispersionOrMaxAtomBoundLedger 不是新增第三终端；失败对象就是已命名 moving atom。",
            "remaining": "保留源种子 + moving atom 排斥两个真实输入。",
        },
        {
            "gate": "MovingAtomExclusionCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料没有证明 actual noncanonical clean-core moving atom exclusion 或 exact source entropy。",
            "remaining": "ActualNoncanonicalCleanCoreMovingAtomExclusion。",
        },
        {
            "gate": "AcyclicSeedCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料仍未提交无环 pre-Cauchy actual noncanonical primitive source seed。",
            "remaining": "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn。",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_pair_mass_dispersion_to_moving_atom_router",
        "status": "pair_mass_dispersion_reduced_to_acyclic_seed_and_clean_core_moving_atom_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "pair_mass_dispersion_boundary_closed": True,
        "large_pair_atom_equivalence_closed": True,
        "registered_multiplier_bridge_imported": True,
        "failure_packet_return_alphabet_imported": True,
        "pair_mass_dispersion_not_separate_terminal": True,
        "acyclic_pre_cauchy_seed_proved": False,
        "clean_core_moving_atom_exclusion_proved": False,
        "exact_clean_core_source_entropy_proved": False,
        "actual_exact_uv_support_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "ExactUVPairMassDispersionOrMaxAtomBoundLedger"
        ),
        "terminal_gap_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "ActualNoncanonicalCleanCoreMovingAtomExclusion"
        ),
        "normal_form_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "ExactCleanCoreFullSNonAPWFDSourceEntropy"
        ),
        "strict_self_contained_math_basis_after_router": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "ActualNoncanonicalCleanCoreMovingAtomExclusion AND "
            "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
        ),
        "next_attack_contract": {
            "name": "ActualNoncanonicalCleanCoreMovingAtomExclusion_FOR_AcyclicPreCauchySeed",
            "must_prove": [
                "给出无环 pre-Cauchy actual noncanonical primitive source seed",
                "在同一 formal unit 内定义最终登记容量测度 M_{u,v}",
                "证明通过全部回流测试的 clean-core 残余没有 moving same-(u,v) 大原子",
                "等价地证明 exact clean-core full-S non-AP WFD source entropy",
                "把大原子、熵失败、source 缺失、超预算和抵消全部命名回流",
            ],
            "cannot_use_as_proof": [
                "把 ExactUVPairMassDispersion 当作独立新黑箱反复引用",
                "formal WFD、K4/K6、Type/Fourier fixed projection 平坦性",
                "canonical RIW/Buchstab source entropy 跨分支导入",
                "早期零行真实样本缺席或 payment skeleton 反推 source",
                "未精确匹配的外部 KLS/DI/BFI",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "pair-mass 分散失败不会产生一个新的终端硬点。最大 pair 原子界失败，等价于同一 formal unit "
            "中出现 sign-refined exact (u,v) 大原子；registered multiplier discipline 把它与最终容量大原子"
            "对齐，支撑失败 packet 回流字母表再排除非 clean-core 出口。剩下的正是既有终端 "
            "ActualNoncanonicalCleanCoreMovingAtomExclusion，其内部标准形是 ExactCleanCoreFullSNonAPWFDSourceEntropy。"
            "因此严格自足源侧剩余被去重为：无环 pre-Cauchy source seed + clean-core moving atom 排斥。"
            "当前二者仍未证明，不能声明行/列无条件闭合。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix 严格 pair-mass 分散到 moving-atom 对齐路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"pair_mass_dispersion_boundary_closed={str(result['pair_mass_dispersion_boundary_closed']).lower()}",
        f"pair_mass_dispersion_not_separate_terminal={str(result['pair_mass_dispersion_not_separate_terminal']).lower()}",
        f"acyclic_pre_cauchy_seed_proved={str(result['acyclic_pre_cauchy_seed_proved']).lower()}",
        f"clean_core_moving_atom_exclusion_proved={str(result['clean_core_moving_atom_exclusion_proved']).lower()}",
        f"actual_exact_uv_support_proved={str(result['actual_exact_uv_support_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 去重压缩链",
        "",
        "```text",
        "ExactUVPairMassDispersionOrMaxAtomBoundLedger fails",
        "  -> sign-refined exact (u,v) large pair atom",
        "  -> registered capacity large atom",
        "  -> support-failure packet return alphabet",
        "  -> clean-core moving atom",
        "  -> ActualNoncanonicalCleanCoreMovingAtomExclusion",
        "  -> ExactCleanCoreFullSNonAPWFDSourceEntropy",
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
            "等价内部标准形：",
            "",
            "```text",
            result["normal_form_after_router"],
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
