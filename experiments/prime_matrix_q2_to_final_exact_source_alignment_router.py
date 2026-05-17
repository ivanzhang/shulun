#!/usr/bin/env python3
"""生成 Q2 CRT ladder 到最终 exact-source 原子的对齐路由证书。

用法示例：
  python3 experiments/prime_matrix_q2_to_final_exact_source_alignment_router.py
  python3 -m json.tool data/prime-matrix-q2-to-final-exact-source-alignment-ledger.json

输出：
  data/prime-matrix-q2-to-final-exact-source-alignment-ledger.json
  docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.json
  docs/monograph/prime-matrix-q2-to-final-exact-source-alignment-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

Q2_FIREWALL = DOCS / "prime-matrix-q2-aperture-explosion-schema-firewall-router.json"
ACTIVE_FINAL = DOCS / "prime-matrix-active-final-inputs-router.json"
CURRENT_ATTACK = DOCS / "prime-matrix-final-open-input-current-attack-router.json"
PRETERMINAL = DOCS / "prime-matrix-strict-preterminal-support-capacity-attack-router.json"
FIBER_SOURCE = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"

OUT_LEDGER = DATA / "prime-matrix-q2-to-final-exact-source-alignment-ledger.json"
OUT_JSON = DOCS / "prime-matrix-q2-to-final-exact-source-alignment-router.json"
OUT_MD = DOCS / "prime-matrix-q2-to-final-exact-source-alignment-router.md"

PREVIOUS_HARDPOINT = "Q2ApertureExplosionCurrentSchemaFirewall;GlobalFinalInputsStillOpen"
NEXT_HARDPOINT = (
    "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource "
    "OR ExternalDIBFIKuznetsovDispersionTheoremMatch; "
    "DStructureRankinPromotionIndependentAcceptanceOpen"
)


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 依赖。"""
    return json.loads(path.read_text(encoding="utf-8"))


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定门。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造对齐路由证书。"""
    q2 = load_json(Q2_FIREWALL)
    active = load_json(ACTIVE_FINAL)
    current = load_json(CURRENT_ATTACK)
    preterminal = load_json(PRETERMINAL)
    fiber = load_json(FIBER_SOURCE)
    dstructure = load_json(DSTRUCTURE)

    q2_local_terminal_removed = (
        q2.get("unnamed_aperture_explosion_terminal_allowed") is False
        and q2.get("registered_support_motion_imported_closed") is True
        and q2.get("current_materialized_fresh_pdec_imported_closed") is True
    )
    active_final_reduced = active.get("active_final_inputs_boundary_closed") is True
    current_attack_reduced = current.get("final_open_input_boundary_closed") is True
    preterminal_aligned = preterminal.get("preterminal_support_capacity_attack_closed") is True
    fiber_atomized = fiber.get("preterminal_fiber_dispersion_source_atomization_closed") is True
    dstructure_boundary = dstructure.get("promotion_package_boundary_closed") is True

    lanes = [
        {
            "lane": "Q2 local CRT ladder",
            "status": "current unnamed terminal removed",
            "remaining": "future explicit schema only",
        },
        {
            "lane": "strict self-contained source lane",
            "status": "reduced to nonterminal exact-UV fiber aperiodicity",
            "remaining": "actual pre-Cauchy source fiber mass dispersion",
        },
        {
            "lane": "external spectral lane",
            "status": "conditional route",
            "remaining": "ExternalDIBFIKuznetsovDispersionTheoremMatch",
        },
        {
            "lane": "promotion lane",
            "status": "boundary closed but not accepted",
            "remaining": "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        },
    ]

    gates = [
        gate(
            "Q2CurrentLocalTerminalRemoved",
            q2_local_terminal_removed,
            q2_local_terminal_removed,
            "Q2 受控尾量已入 SAE，当前无名孔径爆炸、registered support motion 与材料化 fresh-layer PDEC 均不能作为终端保留。",
            "future explicit schema if new",
        ),
        gate(
            "Q2PositionRigidityNotSourceMassDispersion",
            True,
            True,
            "Q2/CRT 轮筛给的是位置与相位约束；它不生成 Cauchy/dispersion 前 actual source 在 exact `(u,v)` fiber 上的质量分散。",
            "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource",
        ),
        gate(
            "ActiveFinalInputsImported",
            active_final_reduced,
            active_final_reduced,
            "当前活跃最终输入已压成 noncanonical 数学输入加 DStructure/Rankin 独立验收。",
            "Noncanonical math input AND DStructure/Rankin",
        ),
        gate(
            "CurrentFinalAttackImported",
            current_attack_reduced,
            current_attack_reduced,
            "最终开放输入当前攻坚已对齐为 source anti-atom 或外部 DI/BFI/Kuznetsov，加独立晋级验收。",
            "FullSNonAPStrengthenedSourceAntiAtomContract OR ExternalDIBFIKuznetsovDispersionTheoremMatch",
        ),
        gate(
            "PreterminalExactUVFiberAperiodicityImported",
            preterminal_aligned,
            preterminal_aligned,
            "strict 自足 source lane 的最新数值核心是 actual pre-Cauchy source 的 exact-UV fiber 非集中估计。",
            "NonterminalExactUVFiberAperiodicityEstimateForActualPreCauchySource",
        ),
        gate(
            "SourceDomainRankAtomPackageImported",
            fiber_atomized,
            fiber_atomized,
            "fiber 非集中又等价压到 source domain absolute entropy、complete key 分区与 fixed-key local multiplicity 三原子包。",
            "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger",
        ),
        gate(
            "DStructurePromotionBoundaryImported",
            dstructure_boundary,
            dstructure_boundary and dstructure.get("promotion_package_independently_accepted") is True,
            "DStructure/Rankin 晋级边界已命名；当前仍未独立接受，不能作者侧升级为无条件定理。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        gate(
            "GlobalRowColumnUnconditionalClosureReached",
            False,
            False,
            "本步完成 Q2 路线与最终 exact-source 原子的对齐；没有证明 fiber 非集中、外部谱定理或 DStructure 独立验收。",
            NEXT_HARDPOINT,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_q2_to_final_exact_source_alignment_router",
        "status": "q2_crt_ladder_aligned_to_final_exact_source_atom_not_global_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "previous_hardpoint": PREVIOUS_HARDPOINT,
        "q2_current_local_terminal_removed": q2_local_terminal_removed,
        "q2_position_rigidity_controls_source_mass": False,
        "active_final_inputs_imported": active_final_reduced,
        "current_final_attack_imported": current_attack_reduced,
        "preterminal_exact_uv_fiber_aperiodicity_imported": preterminal_aligned,
        "source_domain_rank_atom_package_imported": fiber_atomized,
        "dstructure_promotion_boundary_imported": dstructure_boundary,
        "dstructure_independently_accepted": bool(dstructure.get("promotion_package_independently_accepted")),
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_HARDPOINT,
        "lanes": lanes,
        "gates": gates,
        "closed_gates": [item["gate"] for item in gates if item["closed"]],
        "open_gates": [item["gate"] for item in gates if not item["closed"] or not item["proved"]],
        "plain_conclusion": (
            "Q2 阶 CRT 梯已经清掉当前局部无名终端：受控尾量入 SAE，孔径爆炸必须显式 schema 化。"
            "但 CRT 位置/相位刚性不能直接证明 actual pre-Cauchy source 在 exact `(u,v)` fiber 上的质量分散。"
            "因此 Q2 路线的全局剩余必须回到最终 exact-source 原子：证明 nonterminal exact-UV fiber 非集中，"
            "或走外部 DI/BFI/Kuznetsov；无论哪条线，DStructure/Rankin 独立晋级验收仍开。"
        ),
        "dependency_hashes": {
            str(Q2_FIREWALL.relative_to(ROOT)): sha256(Q2_FIREWALL),
            str(ACTIVE_FINAL.relative_to(ROOT)): sha256(ACTIVE_FINAL),
            str(CURRENT_ATTACK.relative_to(ROOT)): sha256(CURRENT_ATTACK),
            str(PRETERMINAL.relative_to(ROOT)): sha256(PRETERMINAL),
            str(FIBER_SOURCE.relative_to(ROOT)): sha256(FIBER_SOURCE),
            str(DSTRUCTURE.relative_to(ROOT)): sha256(DSTRUCTURE),
        },
    }


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_LEDGER.write_text(payload, encoding="utf-8")
    OUT_JSON.write_text(payload, encoding="utf-8")

    lines = [
        "# Q2 CRT ladder 到最终 exact-source 原子对齐路由",
        "",
        "**状态：** `q2_crt_ladder_aligned_to_final_exact_source_atom_not_global_proof`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"previous_hardpoint={result['previous_hardpoint']}",
        f"q2_current_local_terminal_removed={fmt_bool(result['q2_current_local_terminal_removed'])}",
        f"q2_position_rigidity_controls_source_mass={fmt_bool(result['q2_position_rigidity_controls_source_mass'])}",
        f"active_final_inputs_imported={fmt_bool(result['active_final_inputs_imported'])}",
        f"current_final_attack_imported={fmt_bool(result['current_final_attack_imported'])}",
        "preterminal_exact_uv_fiber_aperiodicity_imported="
        f"{fmt_bool(result['preterminal_exact_uv_fiber_aperiodicity_imported'])}",
        f"source_domain_rank_atom_package_imported={fmt_bool(result['source_domain_rank_atom_package_imported'])}",
        f"dstructure_promotion_boundary_imported={fmt_bool(result['dstructure_promotion_boundary_imported'])}",
        f"dstructure_independently_accepted={fmt_bool(result['dstructure_independently_accepted'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 对齐结论",
        "",
        "Q2 阶 CRT 周期暴露的本质不对称已经被压成：覆盖块可复制，素端点不能复制；",
        "继续迭代会引入 fresh endpoint primes，受控部分进入 `SAE`，失控部分必须显式 schema 化。",
        "因此当前 Q2 局部不再含可保留的无名终端。",
        "",
        "但最终 source 反原子需要的是 Cauchy/dispersion 前 actual source 的 exact `(u,v)` fiber 质量非集中。",
        "CRT/轮筛位置刚性不能替代该质量估计；它只说明哪些位置被允许或禁止，不说明 actual signed source 如何分配质量。",
        "",
        "## 2. 四条线",
        "",
        "| lane | status | remaining |",
        "| --- | --- | --- |",
    ]
    for item in result["lanes"]:
        lines.append(
            "| {lane} | {status} | {remaining} |".format(
                lane=table_cell(item["lane"]),
                status=table_cell(item["status"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["gates"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 最新剩余",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "本证书不是最终证明；它把 Q2/CRT 路线的剩余精确回接到 actual-source fiber 非集中、外部谱输入与 DStructure/Rankin 晋级验收。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    write_outputs(result)
    print(json.dumps({
        "status": result["status"],
        "q2_current_local_terminal_removed": result["q2_current_local_terminal_removed"],
        "next_direct_attack_target": result["next_direct_attack_target"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
