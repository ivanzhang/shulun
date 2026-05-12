#!/usr/bin/env python3
"""生成 RKS-log 由 RNRS 倒数能量回填闭合的路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_rks_log_rnrs_transfer_closure_router.py

该脚本只归档作者侧证明链的依赖与边界；不会声明行/列命题无条件闭合。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = ROOT / "docs" / "monograph"
OUT_BASE = "prime-matrix-strict-rks-log-rnrs-transfer-closure-router"
MD_OUT = DOC_DIR / f"{OUT_BASE}.md"
JSON_OUT = DOC_DIR / f"{OUT_BASE}.json"


SOURCE_FILES = [
    "docs/monograph/prime-matrix-strict-multilinear-reciprocal-kloosterman-fixed-log-saving-router.json",
    "docs/monograph/prime-matrix-strict-rks23-internal-weil-barrier-and-bg-frontier-router.json",
    "docs/monograph/prime-matrix-strict-rks23-balanced-collar-l2-energy-reduction-router.json",
    "docs/monograph/prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json",
    "docs/monograph/prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json",
    "docs/monograph/prime-matrix-strict-rks23-point-plane-absorption-router.json",
    "docs/monograph/prime-matrix-strict-rks23-rnrs-energy-absorption-router.json",
    "docs/monograph/prime-matrix-strict-self-contained-replacement-package-hardpoint-router.json",
    "docs/monograph/prime-matrix-strict-self-contained-dual-lane-final-router.json",
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_certificate() -> dict:
    # 中文注释：这里记录的是纯参数吸收，不尝试重新证明 Rudnev/RNRS。
    # 已有 RNRS 证书给 E_+(J^{-1}) <= C_E N^(5/2) P^eps。
    collar_log_power = 236
    required_bilinear_log_saving = 118
    l2_log_saving = 2 * required_bilinear_log_saving
    energy_log_saving = 2 * l2_log_saving
    chosen_eps_num, chosen_eps_den = 1, 16
    chosen_delta_num, chosen_delta_den = 1, 8

    # 若 N >= P^(1/2)/L^236，则
    # C_E N^(5/2) P^(1/16) <= N^(3-1/8)
    # 等价于 C_E L^(236*(1/2-1/8)) <= P^(1/4-1/16-1/16)=P^(1/8)，
    # 幂节省最终压过固定对数损失，有限前缀交给 P0/finite 账本。
    log_exponent_to_absorb = collar_log_power * (0.5 - chosen_delta_num / chosen_delta_den)
    power_margin = 0.25 - chosen_eps_num / chosen_eps_den - (
        chosen_delta_num / chosen_delta_den
    ) / 2

    rows = [
        {
            "gate": "ExactRKSLogInputStatementImported",
            "closed": True,
            "proved": True,
            "meaning": "RKS2/RKS3 目标已固定为素数模数下倒数 Kloosterman 双/多线性 log^-118 节省。",
            "remaining": "none",
        },
        {
            "gate": "OffCollarCauchyWeilAlreadyClosed",
            "closed": True,
            "proved": True,
            "meaning": "平方根颈部之外的块由 Cauchy-Weil 与 log^236 分离吸收。",
            "remaining": "balanced collar only",
        },
        {
            "gate": "BalancedCollarL2EnergyReductionImported",
            "closed": True,
            "proved": True,
            "meaning": "平衡颈部的双线性和已归约到倒数区间加性能量。",
            "remaining": "energy input",
        },
        {
            "gate": "WeightedToUnweightedTransferImported",
            "closed": True,
            "proved": True,
            "meaning": "Vaughan/divisor-bounded 权重只消耗固定 log 幂，已登记进 RKS 账本。",
            "remaining": "unweighted reciprocal energy",
        },
        {
            "gate": "FixedPowerEnergyAbsorbsAllRegisteredLogs",
            "closed": True,
            "proved": True,
            "meaning": "在 N>=P^(1/2)/log^236(P) 的颈部，任意固定幂节省最终强于 log^-472 及权重损失。",
            "remaining": "finite transition handled by P0/finite lane",
        },
        {
            "gate": "SelfContainedRNRSReciprocalEnergyImported",
            "closed": True,
            "proved": True,
            "meaning": "Rudnev 点-平面 incidence 已回接，RNRS 倒数区间能量输入在作者侧链中闭合。",
            "remaining": "source hashes audited in this certificate",
        },
        {
            "gate": "RNRSBoundImpliesRKSLogBalancedCollarSaving",
            "closed": True,
            "proved": True,
            "meaning": "E_+(J^{-1})<=C_E N^(5/2)P^(1/16) 与颈部下界给出固定幂节省，回填 log^-118 双线性目标。",
            "remaining": "none inside RKS-log collar",
        },
        {
            "gate": "SelfContainedRKSLogReciprocalKloostermanTailLog4Input",
            "closed": True,
            "proved": True,
            "meaning": "RKS-log/TL4-L 的内部解析核心由 RNRS 能量链回填闭合。",
            "remaining": "none inside Tail-log4 RKS-log atom",
        },
        {
            "gate": "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage",
            "closed": True,
            "proved": True,
            "meaning": "在前序非 RKS 替代子包均已闭合的作者侧清单下，替代包不再被 RKS-log 阻断。",
            "remaining": "does not create independent referee acceptance event",
        },
        {
            "gate": "ActualNoncanonicalExactUVSupportLowerBound",
            "closed": False,
            "proved": False,
            "meaning": "严格自足全局源侧仍需 actual exact u/v 支撑下界；本步只关闭晋级门的自足替代包。",
            "remaining": "CleanCoreTerminalSupportIncidenceTheorem_FOR_ActualNoncanonicalExactUVSupportLowerBound",
        },
        {
            "gate": "RowColumnUnconditionalClosed",
            "closed": False,
            "proved": False,
            "meaning": "RKS-log 回填不等于完整行/列命题闭合；源侧 ExactUV 与最终吸收审计仍需处理。",
            "remaining": "ActualNoncanonicalExactUVSupportLowerBound AND final promotion absorption audit",
        },
    ]

    source_hashes = {}
    for rel in SOURCE_FILES:
        path = ROOT / rel
        if path.exists():
            source_hashes[rel] = sha256_file(path)
        else:
            source_hashes[rel] = "missing"

    return {
        "certificate_type": "prime_matrix_strict_rks_log_rnrs_transfer_closure_router",
        "status": "rks_log_rnrs_transfer_author_side_closed_exact_uv_still_open",
        "rks_log_rnrs_transfer_closed": True,
        "self_contained_rks_log_reciprocal_kloosterman_tail_log4_input_closed": True,
        "self_contained_tail_log4_rks_log_fixed_saving_closed": True,
        "self_contained_dstructure_tail_log4_finite_rankin_replacement_package_author_side_closed": True,
        "promotion_package_independently_accepted": False,
        "actual_exact_uv_support_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "parameter_absorption": {
            "collar_log_power": collar_log_power,
            "required_bilinear_log_saving": required_bilinear_log_saving,
            "l2_log_saving": l2_log_saving,
            "energy_log_saving": energy_log_saving,
            "rnrs_eps_choice": f"{chosen_eps_num}/{chosen_eps_den}",
            "fixed_power_delta_choice": f"{chosen_delta_num}/{chosen_delta_den}",
            "log_exponent_to_absorb": log_exponent_to_absorb,
            "power_margin": power_margin,
            "absorption_law": "C_E log(P)^88.5 <= P^(1/8) eventually; finite prefix remains in P0/finite lane",
        },
        "rows": rows,
        "next_direct_attack_target": "ActualNoncanonicalExactUVSupportLowerBound",
        "next_required_input": "CleanCoreTerminalSupportIncidenceTheorem_FOR_ActualNoncanonicalExactUVSupportLowerBound",
        "plain_conclusion": (
            "当前最窄 RKS-log 可攻点已由前序 RNRS/Rudnev 倒数能量链回填闭合："
            "Cauchy-Weil 处理颈部外，颈部内由 L2/能量归约、权重去除、固定幂吸收和 RNRS "
            "E_+(J^{-1})<=C_E N^(5/2)P^eps 给出所需 log^-118。"
            "因此 SelfContainedDStructureTailLog4FiniteRankinReplacementPackage 在作者侧替代包口径下不再被 RKS-log 阻断。"
            "但这仍不关闭完整行/列命题：ActualNoncanonicalExactUVSupportLowerBound 仍未证明，"
            "也没有产生独立晋级验收事件。"
        ),
        "source_hashes": source_hashes,
    }


def render_markdown(cert: dict) -> str:
    lines: list[str] = []
    lines.append("# Prime Matrix strict RKS-log RNRS 回填闭合证书")
    lines.append("")
    lines.append("**状态：** `rks_log_rnrs_transfer_author_side_closed_exact_uv_still_open`")
    lines.append("")
    lines.append(cert["plain_conclusion"])
    lines.append("")
    lines.append("```text")
    for key in [
        "rks_log_rnrs_transfer_closed",
        "self_contained_rks_log_reciprocal_kloosterman_tail_log4_input_closed",
        "self_contained_dstructure_tail_log4_finite_rankin_replacement_package_author_side_closed",
        "promotion_package_independently_accepted",
        "actual_exact_uv_support_closed",
        "direct_unconditional_contradiction_found",
        "row_column_unconditional_closed",
    ]:
        lines.append(f"{key}={str(cert[key]).lower()}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. 参数吸收")
    lines.append("")
    lines.append("| item | value |")
    lines.append("| --- | ---: |")
    for key, value in cert["parameter_absorption"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.append("")
    lines.append("关键不等式：若 `N>=P^(1/2)/log^236(P)` 且 RNRS 给出")
    lines.append("`E_+(J^{-1})<=C_E N^(5/2)P^(1/16)`，则取 `delta_E=1/8` 时只需")
    lines.append("`C_E log(P)^88.5 <= P^(1/8)`。幂函数最终压过固定对数损失；有限前缀仍由既有 P0/finite 账本处理。")
    lines.append("")
    lines.append("## 2. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for row in cert["rows"]:
        lines.append(
            f"| `{row['gate']}` | `{str(row['closed']).lower()}` | "
            f"`{str(row['proved']).lower()}` | {row['meaning']} | {row['remaining']} |"
        )
    lines.append("")
    lines.append("## 3. 下一最窄点")
    lines.append("")
    lines.append("```text")
    lines.append(cert["next_direct_attack_target"])
    lines.append(cert["next_required_input"])
    lines.append("```")
    lines.append("")
    lines.append("审稿边界：本证书关闭的是 RKS-log/Tail-log4 自足替代包中的解析核心，不把真实样本无早期零行、外部验收事件或源侧 ExactUV 支撑下界伪造成已证明。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    cert = build_certificate()
    JSON_OUT.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    MD_OUT.write_text(render_markdown(cert), encoding="utf-8")
    print(f"wrote {JSON_OUT.relative_to(ROOT)}")
    print(f"wrote {MD_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
