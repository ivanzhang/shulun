#!/usr/bin/env python3
"""生成 exact-UV fiber 最新非循环同步路由证书。

用法示例：
  python3 experiments/prime_matrix_exactuv_fiber_latest_noncycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json

输出：
  data/prime-matrix-exactuv-fiber-latest-noncycle-sync-ledger.json
  docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json
  docs/monograph/prime-matrix-exactuv-fiber-latest-noncycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-exactuv-fiber-latest-noncycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-q1q2-transport-latest-noncycle-sync-router.json",
    "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json",
    "prime-matrix-strict-actual-source-domain-entropy-atom-router.json",
    "prime-matrix-strict-complete-emitter-key-partition-router.json",
    "prime-matrix-strict-fixed-pair-fiber-bound-router.json",
    "prime-matrix-strict-exact-uv-map-rank-incidence-router.json",
    "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json",
    "prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json",
    "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json",
    "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json",
]

EXACTUV_TARGET = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
COMPLETE_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_ROW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
ROW_SUPPORT = "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger"
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
KEY_BUDGET = "CompleteEmitterTraceKeyBudgetLedger"
SIGN_LOCAL = "SignLocalFactorRefinementNoCancellationLedger"
KEY_RETURN = "OverBudgetOrUnregisteredReturnLedger"
EXACTUV_INCIDENCE = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_KZ = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def status_map() -> dict[str, str | None]:
    """抽取关键上游状态。"""
    return {
        name: load_json(name).get("status")
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(q1q2: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 exact-UV 同步判定表。"""
    imported = q1q2.get("next_direct_attack_target") == EXACTUV_TARGET
    return [
        row(
            "ExactUVTargetImportedFromQ1Q2",
            imported,
            False,
            "Q1/Q2 同步后，纯 CRT 位置刚性剩余被压到 actual pre-Cauchy source 的 exact-UV fiber 非集中。",
            EXACTUV_TARGET,
        ),
        row(
            "PreterminalFiberAtomizationImported",
            True,
            False,
            "preterminal exact-UV fiber 分散已被原子化为源域 rank/no-collapse 包。",
            SOURCE_RANK,
        ),
        row(
            "DeterministicSourceAtomImplicationClosed",
            True,
            True,
            "源域绝对熵、complete key 多对数分区、固定 key 局部 O(1) 重数三者合取即可推出 exact-UV fiber 非集中。",
            f"{SOURCE_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "SourceEntropyReducedToSignedRows",
            True,
            False,
            "源域绝对熵不是 CRT 计数；它需要 pre-Cauchy signed primitive rows、行质量无重原子和支撑下界。",
            f"{SIGNED_ROW} AND {ROW_MASS} AND {ROW_SUPPORT}",
        ),
        row(
            "CompleteKeyReducedToActualSourceTable",
            True,
            False,
            "complete key 不能后验补标签；必须来自 actual noncanonical primitive emitter 源表及预算/refinement/return 纪律。",
            f"{SOURCE_TABLE} AND {KEY_BUDGET} AND {SIGN_LOCAL} AND {KEY_RETURN}",
        ),
        row(
            "FixedPairFiberFormalInequalityClosed",
            True,
            True,
            "若 complete key 数为 log^O(1)，且固定 key 与固定 exact (u,v) 只有 O(1) 原像，则 fixed-pair fiber 上界形式推出。",
            f"{COMPLETE_KEY} AND {FIXED_KEY_MULT}",
        ),
        row(
            "MapRankEquivalentToBoundedIncidence",
            True,
            False,
            "exact-UV map rank/no-collapse 的正面内容是 actual emitter 到 exact (u,v) 的有界重数 incidence；朴素因子-余数 incidence 已被内部 fiber 阻断。",
            EXACTUV_INCIDENCE,
        ),
        row(
            "FalseExactUVSourcesRejected",
            True,
            True,
            "CRT 位置、payment skeleton、DLS 可逆变量、signed-only 相消和 canonical cross-import 都不能生成 exact-UV fiber 非集中。",
            SOURCE_RANK,
        ),
        row(
            "SourceRankConvergesToPointwiseKernel",
            True,
            False,
            "post-antisplit 同步显示 source-rank/no-collapse、new primitive 与 terminal descent 均汇到同 formal-unit 逐 primitive alpha/delta 核表。",
            POINTWISE_KERNEL,
        ),
        row(
            "StrictDownstreamStillOpen",
            True,
            False,
            "继续下钻 pointwise kernel 会回到 alpha/signed-source/terminal 叶子或新 joint 公式；当前没有独立闭合。",
            NEW_JOINT,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭 exact-UV 作为纯 CRT/位置问题的误出口；未证明 signed row、source table、fixed-key multiplicity、new joint、模型、Rate 或 DStructure。",
            f"(({SIGNED_ROW} AND {ROW_MASS} AND {ROW_SUPPORT}) AND ({SOURCE_TABLE} AND {KEY_BUDGET} AND {SIGN_LOCAL} AND {KEY_RETURN}) AND {FIXED_KEY_MULT}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造同步证书。"""
    q1q2 = load_json("prime-matrix-q1q2-transport-latest-noncycle-sync-router.json")
    rows = build_rows(q1q2)
    atomized_basis = (
        f"(({SIGNED_ROW} AND {ROW_MASS} AND {ROW_SUPPORT}) "
        f"AND ({SOURCE_TABLE} AND {KEY_BUDGET} AND {SIGN_LOCAL} AND {KEY_RETURN}) "
        f"AND {FIXED_KEY_MULT}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    source_rank_basis = (
        f"({SOURCE_ENTROPY} AND {COMPLETE_KEY} AND {FIXED_KEY_MULT}) "
        f"AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    downstream_basis = f"{NEW_JOINT} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    external_basis = f"({EXTERNAL_KZ} OR {NEW_JOINT}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    plain = (
        "exact-UV fiber 首攻点被同步为 source-rank/no-collapse 原子包。"
        "确定性蕴含已经闭合：源域绝对熵、complete key 分区与固定 key 局部 O(1) 重数合取即可推出 fiber 非集中。"
        "真正未证的是 pre-Cauchy signed row 系数律、actual emitter 源表/complete key 预算、固定 key 局部重数；"
        "继续沿 strict 链下钻会回到逐 primitive kernel 表和 new-joint/terminal 前沿。"
    )
    return {
        "certificate_type": "prime_matrix_exactuv_fiber_latest_noncycle_sync_router",
        "status": "exactuv_fiber_branch_reduced_to_source_rank_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "exactuv_target_imported_from_q1q2": q1q2.get("next_direct_attack_target") == EXACTUV_TARGET,
        "preterminal_fiber_atomization_imported": True,
        "deterministic_source_atom_implication_closed": True,
        "source_entropy_reduced_to_signed_rows": True,
        "complete_key_reduced_to_actual_source_table": True,
        "fixed_pair_fiber_formal_inequality_closed": True,
        "map_rank_equivalent_to_bounded_incidence": True,
        "false_exactuv_sources_rejected": True,
        "source_rank_converges_to_pointwise_kernel": True,
        "nonterminal_exactuv_fiber_aperiodicity_proved": False,
        "strict_downstream_new_joint_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": SIGNED_ROW,
        "parallel_direct_attack_targets": [SOURCE_TABLE, FIXED_KEY_MULT, NEW_JOINT, EXTERNAL_KZ],
        "source_rank_basis_after_router": source_rank_basis,
        "atomized_internal_basis_after_router": atomized_basis,
        "strict_downstream_basis_if_imported": downstream_basis,
        "conditional_external_basis": external_basis,
        "upstream_status": status_map(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix exact-UV fiber 最新非循环同步路由证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        "preterminal_fiber_atomization_imported=true",
        "deterministic_source_atom_implication_closed=true",
        "source_entropy_reduced_to_signed_rows=true",
        "complete_key_reduced_to_actual_source_table=true",
        "fixed_pair_fiber_formal_inequality_closed=true",
        "map_rank_equivalent_to_bounded_incidence=true",
        "nonterminal_exactuv_fiber_aperiodicity_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. 同步结论",
        "",
        "`NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource` 不是 CRT 位置刚性问题。",
        "它是同一 actual formal unit 内 pre-Cauchy source 的源域熵与 exact `(u,v)` 映射无坍缩问题。",
        "当前已闭合的是形式蕴含：",
        "",
        "```text",
        "source entropy + complete key partition + fixed-key O(1) multiplicity",
        "=> exact-UV fiber aperiodicity / no-collapse.",
        "```",
        "",
        "未闭合的是这三个 actual 源侧输入本身。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 源域原子基",
            "",
            "```text",
            cert["source_rank_basis_after_router"],
            "```",
            "",
            "完全原子化后内部基为：",
            "",
            "```text",
            cert["atomized_internal_basis_after_router"],
            "```",
            "",
            "若导入既有 strict 下游同步，内部剩余进一步压到：",
            "",
            "```text",
            cert["strict_downstream_basis_if_imported"],
            "```",
            "",
            "条件外部保留线：",
            "",
            "```text",
            cert["conditional_external_basis"],
            "```",
            "",
            "## 4. 下一直接主攻",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " OR ".join(cert["parallel_direct_attack_targets"]),
            "```",
            "",
            "## 5. 诚实边界",
            "",
            "- 本证书不证明 exact-UV fiber 非集中。",
            "- 本证书只把 exact-UV 首攻点压成 actual 源域三原子，并排除 CRT/payment/DLS 位置刚性替代证明。",
            "- 行/列命题仍未全局无条件闭合。",
            "",
            "## 6. 上游状态",
            "",
            "| file | status |",
            "| --- | --- |",
        ]
    )
    for name, status in cert["upstream_status"].items():
        lines.append(f"| `{name}` | `{status}` |")
    lines.extend(
        [
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
