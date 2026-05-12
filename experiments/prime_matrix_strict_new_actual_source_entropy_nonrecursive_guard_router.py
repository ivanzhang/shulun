#!/usr/bin/env python3
"""生成 strict 新 actual-source 熵定理非递归守门证书。

用法示例：
  python3 experiments/prime_matrix_strict_new_actual_source_entropy_nonrecursive_guard_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = (
    DOCS / "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json"
)
OUT_MD = DOCS / "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json",
    "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json",
    "prime-matrix-strict-actual-source-support-seed-router.json",
    "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
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
    direct: dict[str, Any],
    pair_mass: dict[str, Any],
    support_seed: dict[str, Any],
    fusion: dict[str, Any],
    firewall: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成非递归守门判定表。"""
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    seed = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
    independent_l2 = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
    return [
        {
            "gate": "DirectAttackSpineImported",
            "closed": direct.get("same_theorem_target_preserved") is True
            and direct.get("no_theorem_switch") is True,
            "proved": True,
            "meaning": "上一层已保持目标不变，并把源熵定理内部压到 ExactUV 支撑脊柱。",
            "remaining": target,
        },
        {
            "gate": "PairMassReturnLoopDetected",
            "closed": pair_mass.get("pair_mass_dispersion_not_separate_terminal")
            is True,
            "proved": True,
            "meaning": "pair-mass 分散失败等价于 clean-core moving atom；若用 moving-atom 排斥证明 pair-mass，就回到源熵目标自身。",
            "remaining": "禁止把 PairMassDispersion 当作独立黑箱反复引用。",
        },
        {
            "gate": "CircularEntropyProofRejected",
            "closed": True,
            "proved": True,
            "meaning": "不能用 NewActualSourceEntropy/MovingAtomExclusion/ExactEntropy 作为 pair-mass 的证明输入。",
            "remaining": "必须给独立 L2/max-pair 能量账本，或命名回流。",
        },
        {
            "gate": "ElementarySupportEnergyStillAvailable",
            "closed": support_seed.get("elementary_mass_support_lemma_closed") is True,
            "proved": True,
            "meaning": "初等 Cauchy/最大原子到支撑下界的推理可用，但只在独立能量界已经证明后才能使用。",
            "remaining": independent_l2,
        },
        {
            "gate": "AcyclicSeedFusionImported",
            "closed": fusion.get("acyclic_pre_cauchy_seed_independent_input_removed")
            is True,
            "proved": False,
            "meaning": "seed 不能作为无名独立出口；若给出合法 seed，后续失败进入终端家族；若不给出 seed，也回流终端家族。",
            "remaining": "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve_FOR_AcyclicNoncanonicalTerminalFamily",
        },
        {
            "gate": "NonrecursiveEnergyInputCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明不依赖源熵目标的 exact pair L2 能量界或最大 pair 原子界。",
            "remaining": independent_l2,
        },
        {
            "gate": "TargetStillOpenAfterGuard",
            "closed": firewall.get("new_actual_source_entropy_theorem_proved")
            is False,
            "proved": False,
            "meaning": "非递归守门只删除循环证明出口，不证明新 actual-source 熵定理。",
            "remaining": target,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "源熵目标仍未证明，DStructure/Rankin 与高段自足尾项仍为独立门。",
            "remaining": direct.get("strict_self_contained_math_basis_after_router"),
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict 新 actual-source 熵定理非递归守门证书。"""
    direct = load_json(
        DOCS / "prime-matrix-strict-new-actual-source-entropy-direct-attack-router.json"
    )
    pair_mass = load_json(
        DOCS / "prime-matrix-strict-pair-mass-dispersion-to-moving-atom-router.json"
    )
    support_seed = load_json(
        DOCS / "prime-matrix-strict-actual-source-support-seed-router.json"
    )
    fusion = load_json(
        DOCS / "prime-matrix-strict-acyclic-seed-terminal-fusion-router.json"
    )
    firewall = load_json(
        DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
    )
    rows = build_rows(
        direct=direct,
        pair_mass=pair_mass,
        support_seed=support_seed,
        fusion=fusion,
        firewall=firewall,
    )
    return {
        "certificate_type": "prime_matrix_strict_new_actual_source_entropy_nonrecursive_guard_router",
        "status": "strict_new_actual_source_entropy_nonrecursive_guard_closed_energy_input_open",
        "same_theorem_target_preserved": True,
        "nonrecursive_guard_closed": True,
        "pair_mass_return_loop_detected": True,
        "circular_entropy_proof_rejected": True,
        "elementary_support_energy_lemma_available": True,
        "independent_exact_pair_l2_or_max_atom_bound_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "strict_self_contained_terminal_after_router": direct.get(
            "strict_self_contained_terminal_after_router"
        ),
        "strict_self_contained_math_basis_after_router": direct.get(
            "strict_self_contained_math_basis_after_router"
        ),
        "nonrecursive_internal_obligation": (
            "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
        ),
        "legal_nonrecursive_formula": (
            "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed "
            "=> ActualNoncanonicalExactUVSupportLowerBound "
            "=> NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
        ),
        "forbidden_recursive_formula": (
            "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem "
            "=> ExactUVPairMassDispersionOrMaxAtomBoundLedger "
            "=> NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
        ),
        "next_direct_attack_target_inside_same_theorem": (
            "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "继续硬攻后，发现并删除一个循环证明出口：`ExactUVPairMassDispersion` 的失败已经由"
            "既有路由对齐为 clean-core moving atom，因此不能再用 moving-atom 排斥或 exact entropy "
            "来证明 pair-mass 分散，否则只是把 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem` "
            "绕回自身。合法的同命题内部推进必须给出不依赖目标结论的 "
            "`IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed`，再接初等支撑能量引理。"
            "当前材料尚未证明该独立能量界，行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict 新 actual-source 熵定理非递归守门路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"nonrecursive_guard_closed={fmt_bool(result['nonrecursive_guard_closed'])}",
        f"pair_mass_return_loop_detected={fmt_bool(result['pair_mass_return_loop_detected'])}",
        f"circular_entropy_proof_rejected={fmt_bool(result['circular_entropy_proof_rejected'])}",
        f"independent_exact_pair_l2_or_max_atom_bound_proved={fmt_bool(result['independent_exact_pair_l2_or_max_atom_bound_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 非递归纪律",
        "",
        "禁止的循环公式：",
        "",
        "```text",
        result["forbidden_recursive_formula"],
        "```",
        "",
        "允许的非递归公式：",
        "",
        "```text",
        result["legal_nonrecursive_formula"],
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
    lines.extend(
        [
            "",
            "## 3. 最新同命题内部硬点",
            "",
            "```text",
            result["next_direct_attack_target_inside_same_theorem"],
            "```",
            "",
            "完整 strict 基仍保持：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """命令行入口。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
