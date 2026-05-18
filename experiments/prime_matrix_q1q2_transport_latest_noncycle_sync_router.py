#!/usr/bin/env python3
"""生成 Q1/Q2 传输最新非循环同步路由证书。

用法示例：
  python3 experiments/prime_matrix_q1q2_transport_latest_noncycle_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.json

输出：
  data/prime-matrix-q1q2-transport-latest-noncycle-sync-ledger.json
  docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.json
  docs/monograph/prime-matrix-q1q2-transport-latest-noncycle-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-q1q2-transport-latest-noncycle-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-q1q2-transport-latest-noncycle-sync-router.json"
OUT_MD = DOCS / "prime-matrix-q1q2-transport-latest-noncycle-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-short-interval-rough-residue-barrier-router.json",
    "prime-matrix-early-zero-gap-crt-asymmetry-router.json",
    "prime-matrix-q2-carrier-stage-crt-asymmetry-router.json",
    "prime-matrix-q2-endpoint-replacement-aperture-growth-router.json",
    "prime-matrix-q2-fresh-layer-tail-mass-dichotomy-router.json",
    "prime-matrix-q2-aperture-explosion-schema-firewall-router.json",
    "prime-matrix-q2-to-final-exact-source-alignment-router.json",
    "prime-matrix-global-crt-homogeneity-frontier-router.json",
    "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json",
    "prime-matrix-strict-post-antisplit-alpha-terminal-leaf-sync-router.json",
    "prime-matrix-strict-post-source-admission-macrocycle-sync-router.json",
    "prime-matrix-strict-seed-cycle-cut-saturation-frontier-router.json",
    "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json",
]

Q1Q2 = "AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn"
EXACT_UV = "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource"
EXTERNAL_KZ = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
SEED_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
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
    """抽取关键上游状态，供 ledger 对账。"""
    return {
        name: load_json(name).get("status")
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(latest: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 Q1/Q2 同步判定表。"""
    imported = latest.get("next_direct_attack_target") == Q1Q2
    return [
        row(
            "Q1Q2TargetImportedFromLatestBarrier",
            imported,
            False,
            "上一层删除 direct rough-residue 内部黑箱后，把首攻点转为 Q1/Q2 相邻素数 CRT 传输。",
            Q1Q2,
        ),
        row(
            "AdjacentCarrierLemmaAlreadyClosed",
            True,
            True,
            "早期零行若存在，左右最近素数确为跨行相邻素数载体，间隙大于 P。",
            "early-zero gap carrier lemma",
        ),
        row(
            "Q2EndpointStableReplayImpossible",
            True,
            True,
            "提升到全 Q2 轮后，Q1 与 Q2 的端点复本分别被自身整除；端点稳定素性复现不可能。",
            "stable endpoint replay closed",
        ),
        row(
            "PersistentClosedCarrierIsColumnCRTPDEC",
            True,
            True,
            "若不复现素端点、只持久复现同一闭覆盖块，则它就是固定相位 ColumnCRT/PDEC formal unit。",
            "ColumnCRT/PDEC route",
        ),
        row(
            "ControlledFreshEndpointTailIsSAE",
            True,
            True,
            "端点替换产生 fresh endpoint layer；受控孔径且无 PDEC 时，每层只是一禁相位尾质量，按 sum W_j/B_j 可求和。",
            "SAE route",
        ),
        row(
            "UnnamedApertureExplosionForbidden",
            True,
            True,
            "若孔径增长追赶 fresh modulus，必须提交支撑运动、阻断包变化或 fresh-layer PDEC 显式 schema；当前无名出口不可保留。",
            "future explicit schema if new",
        ),
        row(
            "PureCRTGlobalPhaseContradictionBlocked",
            True,
            True,
            "有限 CRT 前缀是同质删相位机制；它解释临界密度，但不自动给指定短区间 actual occupancy 下界。",
            EXACT_UV,
        ),
        row(
            "Q1Q2BranchReducesToExactSource",
            True,
            False,
            "Q1/Q2 位置刚性不能控制 pre-Cauchy actual source 在 exact (u,v) fiber 上的质量分散；剩余回到 exact-source 或外部谱输入。",
            f"{EXACT_UV} OR {EXTERNAL_KZ}",
        ),
        row(
            "StrictDownstreamSaturationImported",
            True,
            False,
            "既有 strict 同步显示 exact-source/seed/PDEC 继续下钻会回到 source-rank、signed-source 固定点、PDEC 作用域或新 joint 公式。",
            f"{NEW_JOINT} OR {SEED_CUT} OR {PDEC_SCOPE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭的是 Q1/Q2 作为独立纯 CRT 终端的误出口；没有证明 exact-source、new joint、外部谱、模型、Rate 或 DStructure。",
            f"(({EXACT_UV} OR {EXTERNAL_KZ}) OR {SEED_CUT} OR {PDEC_SCOPE}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造同步证书。"""
    latest = load_json("prime-matrix-short-interval-rough-residue-barrier-router.json")
    rows = build_rows(latest)
    immediate_basis = (
        f"(({EXACT_UV} OR {EXTERNAL_KZ}) OR {SEED_CUT} OR {PDEC_SCOPE}) "
        f"AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    saturated_internal_basis = (
        f"{NEW_JOINT} AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    conditional_external_basis = (
        f"({EXTERNAL_KZ} OR {PDEC_SCOPE} OR {NEW_JOINT}) "
        f"AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "Q1/Q2 相邻素数传输被同步到既有 Q2 阶 CRT 梯：端点稳定复现已由全 Q2 轮反转排除，"
        "持久闭覆盖块进入 ColumnCRT/PDEC，受控 fresh endpoint tail 进入 SAE，无名孔径爆炸被 schema 防火墙挡住。"
        "因此 Q1/Q2 不是新的独立终端；其非循环剩余回到 exact-source fiber 非集中、外部谱输入，"
        "或沿 strict 饱和链回到 seed/PDEC/new-joint 前沿。"
    )
    return {
        "certificate_type": "prime_matrix_q1q2_transport_latest_noncycle_sync_router",
        "status": "q1q2_transport_branch_synced_to_q2_ladder_and_source_frontier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "q1q2_target_imported_from_latest_barrier": latest.get("next_direct_attack_target") == Q1Q2,
        "adjacent_carrier_lemma_closed": True,
        "q2_endpoint_stable_replay_impossible": True,
        "persistent_closed_carrier_routes_to_columncrt_pdec": True,
        "controlled_fresh_endpoint_tail_routes_to_sae": True,
        "unnamed_aperture_explosion_forbidden": True,
        "pure_crt_global_phase_contradiction_blocked": True,
        "q1q2_branch_reduced_to_exact_source_or_external": True,
        "q1q2_transport_defect_or_stable_short_return_proved_as_global_contradiction": False,
        "strict_saturated_internal_new_joint_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": EXACT_UV,
        "parallel_direct_attack_targets": [EXTERNAL_KZ, SEED_CUT, PDEC_SCOPE, NEW_JOINT],
        "immediate_internal_basis_after_router": immediate_basis,
        "strict_saturated_internal_basis_if_downstream_sync_imported": saturated_internal_basis,
        "conditional_external_basis": conditional_external_basis,
        "upstream_status": status_map(),
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix Q1/Q2 传输最新非循环同步路由证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        "q2_endpoint_stable_replay_impossible=true",
        "persistent_closed_carrier_routes_to_columncrt_pdec=true",
        "controlled_fresh_endpoint_tail_routes_to_sae=true",
        "unnamed_aperture_explosion_forbidden=true",
        "pure_crt_global_phase_contradiction_blocked=true",
        "q1q2_branch_reduced_to_exact_source_or_external=true",
        "q1q2_transport_defect_or_stable_short_return_proved_as_global_contradiction=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. 同步结论",
        "",
        "`Q1<Q2` 相邻素数载体确实给出真实刚性：全 `Q2` 阶周期不能同时复现覆盖块与两个素端点。",
        "但这只排除 endpoint-stable replay。其余分支已经由旧 Q2 梯路由：",
        "",
        "- 固定闭覆盖块持久复现：`ColumnCRT/PDEC`。",
        "- 受控 fresh endpoint tail：`SAE`。",
        "- 孔径爆炸或支撑运动：必须提交显式 schema，当前不能无名保留。",
        "- 纯有限 CRT 相位矛盾：被同质删相位机制排除，必须回到 actual-source/fiber 非集中。",
        "",
        "因此，`AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn` 不能再作为独立终端硬点保留；",
        "它要么落入命名出口，要么回到 exact-source/外部谱输入。",
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
            "## 3. 立即内部基",
            "",
            "```text",
            cert["immediate_internal_basis_after_router"],
            "```",
            "",
            "若同时导入既有 seed/PDEC 分支饱和同步，strict 内部剩余进一步压到：",
            "",
            "```text",
            cert["strict_saturated_internal_basis_if_downstream_sync_imported"],
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
            "- 本证书不证明 row-gap 不存在。",
            "- 本证书只把 Q1/Q2 传输分支同已有 Q2 梯、SAE/PDEC 防火墙和 exact-source 前沿同步。",
            "- 稳定复现的 CRT 矛盾后半段已闭合；仍未证明全局反例链必产生可排斥的 exact-source 非集中或新 joint 公式。",
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
