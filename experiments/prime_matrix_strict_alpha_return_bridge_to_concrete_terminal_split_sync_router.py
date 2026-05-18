#!/usr/bin/env python3
"""生成 alpha-return 独立桥到具体终端分裂前沿的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_alpha_return_bridge_to_concrete_terminal_split_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.json

输出：
  data/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-ledger.json
  docs/monograph/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.json
  docs/monograph/prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-alpha-return-bridge-to-concrete-terminal-split-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json",
    "prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json",
    "prime-matrix-strict-latest-self-contained-hardpoint-sync-router.json",
    "prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json",
    "prime-matrix-strict-actual-source-domain-entropy-atom-router.json",
    "prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json",
    "prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json",
    "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
]

CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
INDEPENDENT_BRIDGE = "IndependentActualSourceBridgeNotFactoredThroughAlphaReturn"
A1_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
EXACT_ENTROPY = "ExactCleanCoreFullSNonAPWFDSourceEntropy"
SEED = "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn"
PAIR_ENERGY = "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed"
PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
KUZNETSOV_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
SELF_DSTRUCTURE = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
MERTENS_TAIL = (
    "SelfContainedExplicitZetaZeroFreeRegionThetaEnvelopeXGe20000 "
    "AND SelfContainedMeisselMertensConstantIntervalLedgerAt20000"
)


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值输出为小写字符串。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    result: dict[str, str] = {}
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [f"docs/monograph/{name}" for name in SOURCE_FILES if not (DOCS / name).exists()]


def sync_chain() -> list[dict[str, str]]:
    """给出从 alpha-return 二选一到具体终端分裂的同步链。"""
    return [
        {
            "from": f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
            "to": "canonical-lock arm OR independent actual-source arm",
            "meaning": "上一层只说明二选一；本轮分别下钻两条手臂。",
        },
        {
            "from": INDEPENDENT_BRIDGE,
            "to": f"{A1_ADMISSION} OR {EXACT_ENTROPY}",
            "meaning": "actual-source 桥已具体化为 clean A1 源准入或 actual clean-core exact entropy。",
        },
        {
            "from": A1_ADMISSION,
            "to": "scoped A1 branch statement, not global contradiction",
            "meaning": "A1 准入只能给 scoped canonical 陈述，不能单独关闭 unrestricted noncanonical 分支。",
        },
        {
            "from": EXACT_ENTROPY,
            "to": f"{SEED} AND {PAIR_ENERGY}",
            "meaning": "exact entropy 若走 ExactUV 支撑路线，必须给无环 pre-Cauchy seed 和独立 pair L2/max-atom 能量界。",
        },
        {
            "from": CANONICAL_LOCK,
            "to": f"({PDEC_CLEAN_KLS} AND {MODEL_GAP}) OR {KUZNETSOV_DLS}",
            "meaning": "canonical-lock 直攻只给 scoped 吸收；mismatch 出口同步到 PDEC/CleanKLS+模型余量或自足 Kuznetsov/DLS。",
        },
        {
            "from": "signed source / alpha weight / pointwise routes",
            "to": "terminal-family backedge",
            "meaning": "这些旧路线继续下钻会回到 PDEC/CleanKLS 或 signed-source 固定点，不能当作新进展量。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """合并两条手臂的关键读数。"""
    alpha = data["alpha"]
    concrete = data["concrete"]
    latest = data["latest"]
    canonical = data["canonical"]
    entropy = data["entropy"]
    antiatom = data["antiatom"]
    guard = data["guard"]

    return [
        row(
            "AlphaReturnBridgeImported",
            alpha.get("next_direct_attack_target")
            == f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
            False,
            "上一层已把 terminal atoms 同步到 canonical-lock 或 alpha-return 前独立 actual-source 桥。",
            f"{CANONICAL_LOCK} OR {INDEPENDENT_BRIDGE}",
        ),
        row(
            "IndependentBridgeConcreteAtomsImported",
            concrete.get("independent_actual_source_bridge_concrete_sync_closed") is True
            and concrete.get("terminal_gap_after_router")
            == f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {EXACT_ENTROPY}",
            False,
            "独立 actual-source 桥继续压成 clean A1 source admission 或 exact clean-core source entropy。",
            f"{A1_ADMISSION} OR {EXACT_ENTROPY}",
        ),
        row(
            "A1AdmissionAbsorbedAsScopedOnly",
            latest.get("sync_closed") is True
            and latest.get("acyclic_precauchy_seed_proved") is False,
            True,
            "A1 canonical source admission 只是 scoped 分支陈述，不能作为独立全局矛盾。",
            f"{SEED} AND {PAIR_ENERGY}",
        ),
        row(
            "ExactEntropyReducedToSeedAndPairEnergy",
            latest.get("independent_exact_pair_l2_or_max_atom_bound_proved") is False
            and latest.get("acyclic_precauchy_seed_proved") is False
            and guard.get("nonrecursive_guard_closed") is True,
            False,
            "exact entropy 支撑路线不能用 moving-atom/source-entropy 自身回证 pair energy。",
            f"{SEED} AND {PAIR_ENERGY}",
        ),
        row(
            "SourceDomainEntropySignedRowRouteStillBackedge",
            entropy.get("actual_source_domain_entropy_atomization_closed") is True
            and entropy.get("acyclic_seed_primitive_row_signed_coefficient_law_proved") is False,
            False,
            "source-domain entropy 的 signed row 下钻仍缺 pre-Cauchy signed coefficient law，并回到终端家族。",
            "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward",
        ),
        row(
            "ActualSourceAntiAtomSyncedBackToTerminalFamily",
            antiatom.get("actual_source_antiatom_to_terminal_sync_boundary_closed") is True
            and antiatom.get("strict_terminal_family_proved") is False,
            False,
            "强化反原子线若继续下钻，会经 ExactUV/pair-energy/seed 回到 strict acyclic 终端家族。",
            f"{CANONICAL_LOCK} OR DirectAcyclicSameSetPDECCapDualCertificate OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn",
        ),
        row(
            "CanonicalLockDirectAttackImported",
            canonical.get("canonical_lock_direct_attack_boundary_closed") is True
            and canonical.get("acyclic_terminal_canonical_lock_proved") is False,
            False,
            "canonical-lock 直攻没有闭合；等式真时只是 scoped 吸收，mismatch 进入 DLS/PDEC/命名回流。",
            f"({PDEC_CLEAN_KLS} AND {MODEL_GAP}) OR {KUZNETSOV_DLS}",
        ),
        row(
            "KuznetsovDLSStillOpen",
            canonical.get("self_contained_kuznetsov_dls_large_sieve_inequality_proved") is False,
            False,
            "clean DLS 形式层已压到自足 Kuznetsov/DLS 大筛不等式，但该不等式未证。",
            KUZNETSOV_DLS,
        ),
        row(
            "PDECCleanKLSStillOpen",
            canonical.get("pdec_cap_or_internal_clean_kls_large_sieve_proved") is False,
            False,
            "PDEC/CleanKLS 标签仍需同集作用域、内部大筛和模型余量，不能当黑箱。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "CurrentConcreteTerminalSplitPinned",
            True,
            False,
            "当前二选一已同步为 pair-energy seed 线、Kuznetsov/DLS 线、PDEC/CleanKLS+模型余量线三类具体硬点。",
            (
                f"({SEED} AND {PAIR_ENERGY}) OR {KUZNETSOV_DLS} "
                f"OR ({PDEC_CLEAN_KLS} AND {MODEL_GAP})"
            ),
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只完成具体终端分裂同步；尚未证明 seed+pair energy、Kuznetsov/DLS、PDEC/CleanKLS+模型余量、Rate 或 DStructure。",
            (
                f"(({SEED} AND {PAIR_ENERGY}) OR {KUZNETSOV_DLS} "
                f"OR ({PDEC_CLEAN_KLS} AND {MODEL_GAP})) AND {RATE} AND {DSTRUCTURE}"
            ),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    data = {
        "alpha": load_json("prime-matrix-strict-terminal-atoms-to-alpha-return-bridge-sync-router.json"),
        "concrete": load_json("prime-matrix-strict-independent-actual-source-bridge-concrete-atom-sync-router.json"),
        "latest": load_json("prime-matrix-strict-latest-self-contained-hardpoint-sync-router.json"),
        "canonical": load_json("prime-matrix-strict-terminal-canonical-lock-direct-attack-sync-router.json"),
        "entropy": load_json("prime-matrix-strict-actual-source-domain-entropy-atom-router.json"),
        "antiatom": load_json("prime-matrix-strict-actual-source-antiatom-exactuv-terminal-sync-router.json"),
        "guard": load_json("prime-matrix-strict-new-actual-source-entropy-nonrecursive-guard-router.json"),
        "canonical_exit": load_json("prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"),
    }
    rows = build_rows(data)
    direct_contradiction = any(
        doc.get("direct_unconditional_contradiction_found") is True
        or doc.get("row_column_unconditional_closed") is True
        for doc in data.values()
    )
    concrete_split = (
        f"(({SEED} AND {PAIR_ENERGY}) OR {KUZNETSOV_DLS} "
        f"OR ({PDEC_CLEAN_KLS} AND {MODEL_GAP}))"
    )
    return {
        "certificate_type": "prime_matrix_strict_alpha_return_bridge_to_concrete_terminal_split_sync_router",
        "status": "alpha_return_bridge_synced_to_concrete_terminal_split_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "alpha_return_bridge_imported": rows[0]["closed"],
        "independent_bridge_concrete_atoms_imported": rows[1]["closed"],
        "a1_admission_absorbed_as_scoped_only": rows[2]["closed"],
        "exact_entropy_reduced_to_seed_and_pair_energy": rows[3]["closed"],
        "canonical_lock_direct_attack_imported": rows[6]["closed"],
        "concrete_terminal_split_pinned": rows[9]["closed"],
        "independent_exact_pair_l2_or_max_atom_bound_proved": False,
        "acyclic_precauchy_seed_proved": False,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "direct_unconditional_contradiction_found": direct_contradiction,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": PAIR_ENERGY,
        "parallel_attack_targets": [
            SEED,
            KUZNETSOV_DLS,
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ],
        "concrete_terminal_split": concrete_split,
        "strict_rate_packet_basis_after_router": f"{concrete_split} AND {RATE} AND {DSTRUCTURE}",
        "strict_self_contained_high_tail_basis_after_router": (
            f"{concrete_split} AND ({MERTENS_TAIL}) AND {SELF_DSTRUCTURE}"
        ),
        "with_external_mertens_high_tail_removed_basis": (
            f"{concrete_split} AND {SELF_DSTRUCTURE}"
        ),
        "sync_chain": sync_chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "当前 `canonical-lock OR independent actual-source bridge` 二选一还能继续压缩。"
            "independent bridge 侧的 A1 admission 被吸收为 scoped 陈述，exact entropy 侧必须提交"
            "无环 pre-Cauchy seed 与独立 pair L2/max-atom 能量界；canonical-lock 侧则被直攻压到"
            "Kuznetsov/DLS 或 PDEC/CleanKLS+模型余量。故最新具体终端分裂为 "
            "`(AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
            "IndependentExactPairL2EnergyOrMaxAtomBoundForAcyclicSeed) OR "
            "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks OR "
            "(PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve AND ExplicitModelGapAndFiniteDPRCLedger)`；"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict alpha-return bridge 到具体终端分裂同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"alpha_return_bridge_imported={fmt_bool(result['alpha_return_bridge_imported'])}",
        f"independent_bridge_concrete_atoms_imported={fmt_bool(result['independent_bridge_concrete_atoms_imported'])}",
        f"a1_admission_absorbed_as_scoped_only={fmt_bool(result['a1_admission_absorbed_as_scoped_only'])}",
        f"exact_entropy_reduced_to_seed_and_pair_energy={fmt_bool(result['exact_entropy_reduced_to_seed_and_pair_energy'])}",
        f"canonical_lock_direct_attack_imported={fmt_bool(result['canonical_lock_direct_attack_imported'])}",
        f"concrete_terminal_split_pinned={fmt_bool(result['concrete_terminal_split_pinned'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` | {cell(item['meaning'])} |")

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. 最新具体终端分裂",
            "",
            "```text",
            result["concrete_terminal_split"],
            "```",
            "",
            "rate-packet 口径下仍需：",
            "",
            "```text",
            result["strict_rate_packet_basis_after_router"],
            "```",
            "",
            "严格自足高段尾项口径下为：",
            "",
            "```text",
            result["strict_self_contained_high_tail_basis_after_router"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留 `AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn`、自足 Kuznetsov/DLS 大筛，以及 PDEC/CleanKLS+模型余量。不能把 A1 scoped 陈述、旧 signed-source/alpha 回边、PDEC/CleanKLS 标签或 canonical-lock mismatch 登记当成闭合证明。",
            "",
        ]
    )
    if result["missing_sources"]:
        lines.extend(["## 5. 缺失依赖", ""])
        for name in result["missing_sources"]:
            lines.append(f"- `{name}`")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 和 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    result = build_result()
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
