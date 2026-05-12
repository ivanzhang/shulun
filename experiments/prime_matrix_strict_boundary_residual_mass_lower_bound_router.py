#!/usr/bin/env python3
"""生成 strict 边界残洞质量下界路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_boundary_residual_mass_lower_bound_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-boundary-residual-mass-lower-bound-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-boundary-residual-mass-lower-bound-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-boundary-residual-mass-lower-bound-router.md"

HARDPOINT = "BoundaryResidualMassLowerBoundForTypeCompression"
PREFIX_POTENTIAL = "AdaptivePrefixResidualPotentialLowerBound"
PREFIX_TRANSFER = "PrefixResidualToBoundaryFormalUnitObligationTransfer"
PREFIX_CAPACITY = "RegisteredPrefixCapacityMultiplierDiscipline"
LOW_MASS_DEFECT = "LowPrefixResidualMassToRegisteredPhaseDefect"
EFFECTIVE_MASS = "EffectiveResidualMassForTypeCompression"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-forced-obligation-lower-bound-router.json",
    MONOGRAPH / "prime-matrix-cylindrical-completion-line-barrier.md",
    MONOGRAPH / "prime-matrix-bottom-deficit-pair-bound-hard-attack.md",
    MONOGRAPH / "prime-matrix-boundary-phase-noncoverage-hard-attack.md",
    MONOGRAPH / "prime-matrix-boundary-residual-migration-audit.md",
    MONOGRAPH / "prime-matrix-witness-obligation-domain-canonicalization-router.md",
    MONOGRAPH / "prime-matrix-anchor-collar-survivor-identity-router.md",
    MONOGRAPH / "prime-matrix-eda-primevoid-to-alpha-pdec-bridge.md",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；文件缺失时返回空对象，避免路由器被旧工作树阻塞。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    """读取文本；文件缺失时返回空字符串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总存在的依赖哈希。"""
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in SOURCE_FILES
        if path.exists()
    }


def fmt_bool(value: bool) -> str:
    """写出小写布尔。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def compression_laws() -> list[dict[str, str]]:
    """列出本轮得到的质量压缩律与障碍。"""
    return [
        {
            "law": "natural_cutoff_obstruction",
            "formula": "R_x at cutoff q<=x is the exact completed-line residual; proving it large near x~P meets the prime-window barrier.",
            "status": "diagnosed_nonfree",
        },
        {
            "law": "bottom_band_exact_split",
            "formula": "R_{P-h}=PrimeColumns disjoint_union {a(h-a): P-a and P-h+a prime}.",
            "status": "closed_as_reduction",
        },
        {
            "law": "adaptive_prefix_amplification",
            "formula": "For z<x, R_{x,z}={c: no q<=z divides xP+c}; EarlyZero forces R_{x,z} to be covered by labels q>z.",
            "status": "definition_closed_transfer_open",
        },
        {
            "law": "low_mass_defect_route",
            "formula": "If a chosen prefix z has too few residuals, the deficit is a low-mod endpoint/sieve defect rather than silent failure.",
            "status": "open_registered_exit",
        },
        {
            "law": "capacity_multiplier_discipline",
            "formula": "Prefix obligations must carry a multiplier ledger so q in (z,x] does not inflate reusable capacity for free.",
            "status": "open",
        },
    ]


def build_rows(forced_router: dict[str, Any], clb: str, bottom: str, bpn: str, witness: str) -> list[dict[str, Any]]:
    """生成边界残洞质量下界判定表。"""
    clb_has_residual = "R_x" in clb and "F_x" in clb
    bottom_has_split = "R_{P-h}" in bottom and (
        "disjoint" in bottom or "\\sqcup" in bottom or "精确并集" in bottom
    )
    bpn_has_prime_window = "短区间" in bpn or "BPN(P)" in bpn
    witness_has_atoms = "physical_filler_atoms" in witness
    return [
        {
            "gate": "ResidualMassInputActive",
            "closed": forced_router.get("next_direct_attack_target") == HARDPOINT,
            "proved": False,
            "meaning": "上一层已把 forced obligation 下界的首要缺口压到边界残洞质量。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步仍只在假设早期零行反例链内推导，不使用真实零行缺席。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "NaturalCutoffResidualEquationImported",
            "closed": clb_has_residual,
            "proved": clb_has_residual,
            "meaning": "CLB 已给出自然 cutoff q<=x 的恒等分解 U_x=R_x\\F_x；早期零行等价于 R_x 被高标签补完。",
            "remaining": "这只是等价式，不给 |R_x| 的可用下界。",
        },
        {
            "gate": "NaturalCutoffMassNotFreeDiagnosed",
            "closed": bottom_has_split and bpn_has_prime_window,
            "proved": True,
            "meaning": "在 x 接近 P 的底部带，R_x 已精确分解为素数列与高素对曲线；证其足够大等价撞上短区间素数/平方根窗口输入。",
            "remaining": "不能把自然 cutoff 残洞下界当成免费内部引理。",
        },
        {
            "gate": "SylvesterLargeFactorOnlyWeak",
            "closed": True,
            "proved": True,
            "meaning": "Sylvester 只保证某列含 >P 的大因子，不保证该列没有 <=x 小因子，因此不给 R_x 质量。",
            "remaining": "需要筛余质量或登记缺陷，而不是单个大因子。",
        },
        {
            "gate": "AdaptivePrefixResidualDefinitionClosed",
            "closed": True,
            "proved": True,
            "meaning": "对任意 z<x 可定义 R_{x,z}；若存在早期零行，则每个 prefix 残洞都必须由 q>z 的标签支付。",
            "remaining": "要证明这些 prefix 义务能进入同一 formal-unit 类型压缩账本。",
        },
        {
            "gate": "WitnessAtomInterfaceImported",
            "closed": witness_has_atoms,
            "proved": witness_has_atoms,
            "meaning": "已有 witness obligation 域可记录 physical filler atoms、return 与 quotient；这给 prefix 义务转移的接口。",
            "remaining": PREFIX_TRANSFER,
        },
        {
            "gate": "AdaptivePrefixPotentialLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料尚未给出某个统一 z=z(P,x) 的全局筛余下界；可走经典低界筛外部输入，或内部化该筛余势。",
            "remaining": PREFIX_POTENTIAL,
        },
        {
            "gate": "PrefixTransferToFormalUnitCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明从 R_{x,z} 产生的覆盖义务在升回边界 formal unit 后不丢失、不换题、不破坏 row-free type key。",
            "remaining": PREFIX_TRANSFER,
        },
        {
            "gate": "PrefixCapacityMultiplierDisciplineCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "降低 cutoff 会引入 q in (z,x] 的额外标签；必须登记容量乘子，防止同一标签复用被误算为大量不同实例。",
            "remaining": PREFIX_CAPACITY,
        },
        {
            "gate": "LowPrefixMassDefectCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "若 prefix 筛余质量异常偏低，应推出低模端点/PDEC/SAE 缺陷；该回流尚未逐行证明。",
            "remaining": LOW_MASS_DEFECT,
        },
        {
            "gate": "BoundaryResidualMassLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "自然 cutoff 质量下界不能直接闭合；最窄非循环路线转为 prefix 势、prefix 转移和容量乘子纪律三项。",
            "remaining": f"{PREFIX_POTENTIAL} AND {PREFIX_TRANSFER} AND {PREFIX_CAPACITY} AND {LOW_MASS_DEFECT}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造边界残洞质量下界路由证书。"""
    forced_router = load_json(MONOGRAPH / "prime-matrix-strict-forced-obligation-lower-bound-router.json")
    clb = load_text(MONOGRAPH / "prime-matrix-cylindrical-completion-line-barrier.md")
    bottom = load_text(MONOGRAPH / "prime-matrix-bottom-deficit-pair-bound-hard-attack.md")
    bpn = load_text(MONOGRAPH / "prime-matrix-boundary-phase-noncoverage-hard-attack.md")
    witness = load_text(MONOGRAPH / "prime-matrix-witness-obligation-domain-canonicalization-router.md")

    after = f"{PREFIX_POTENTIAL} AND {PREFIX_TRANSFER} AND {PREFIX_CAPACITY} AND {LOW_MASS_DEFECT}"
    return {
        "certificate_type": "prime_matrix_strict_boundary_residual_mass_lower_bound_router",
        "status": "boundary_residual_mass_reduced_to_adaptive_prefix_potential_transfer_capacity_defect_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "natural_cutoff_residual_equation_imported": "R_x" in clb and "F_x" in clb,
        "natural_cutoff_mass_not_free_diagnosed": True,
        "adaptive_prefix_residual_definition_closed": True,
        "adaptive_prefix_residual_potential_lower_bound_proved": False,
        "prefix_residual_to_boundary_formal_unit_transfer_proved": False,
        "registered_prefix_capacity_multiplier_discipline_proved": False,
        "low_prefix_residual_mass_to_registered_phase_defect_proved": False,
        "effective_residual_mass_for_type_compression_proved": False,
        "boundary_residual_mass_lower_bound_proved": False,
        "no_quotient_collapse_below_type_threshold_proved": False,
        "boundary_cap_forced_obligation_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": after,
        "next_direct_attack_target": PREFIX_TRANSFER,
        "parallel_attack_targets": [PREFIX_POTENTIAL, PREFIX_CAPACITY, LOW_MASS_DEFECT],
        "effective_mass_target": EFFECTIVE_MASS,
        "compression_laws": compression_laws(),
        "rows": build_rows(forced_router, clb, bottom, bpn, witness),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`BoundaryResidualMassLowerBoundForTypeCompression` 的自然 cutoff 版本不能作为免费内部输入："
            "在 x 接近 P 时，它已经与短区间素数/底部平方根窗口同强。"
            "继续非循环推进的更紧源头是 adaptive prefix：把 cutoff 从 x 降到 z<x，"
            "先制造更厚的 prefix 残洞势，再证明早期零行迫使这些残洞无损转入同一 formal-unit 义务场。"
            "这一步产生三个真正剩余：prefix 势下界、prefix 到边界义务转移、以及容量乘子纪律；"
            "若 prefix 势异常偏低，则必须另证其登记为 PDEC/SAE/ColumnCRT 缺陷。"
            "当前仍未发现无条件直接矛盾，行/列命题不能升级为闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 边界残洞质量下界路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"natural_cutoff_mass_not_free_diagnosed={fmt_bool(result['natural_cutoff_mass_not_free_diagnosed'])}",
        f"adaptive_prefix_residual_definition_closed={fmt_bool(result['adaptive_prefix_residual_definition_closed'])}",
        f"adaptive_prefix_residual_potential_lower_bound_proved={fmt_bool(result['adaptive_prefix_residual_potential_lower_bound_proved'])}",
        f"prefix_residual_to_boundary_formal_unit_transfer_proved={fmt_bool(result['prefix_residual_to_boundary_formal_unit_transfer_proved'])}",
        f"registered_prefix_capacity_multiplier_discipline_proved={fmt_bool(result['registered_prefix_capacity_multiplier_discipline_proved'])}",
        f"low_prefix_residual_mass_to_registered_phase_defect_proved={fmt_bool(result['low_prefix_residual_mass_to_registered_phase_defect_proved'])}",
        f"boundary_residual_mass_lower_bound_proved={fmt_bool(result['boundary_residual_mass_lower_bound_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 硬点压缩",
        "",
        "拆分前：",
        "",
        "```text",
        result["hardpoint_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["hardpoint_after_router"],
        "```",
        "",
        "## 2. 残洞质量律",
        "",
        "| law | formula | status |",
        "| --- | --- | --- |",
    ]
    for row in result["compression_laws"]:
        lines.append(
            "| `{law}` | {formula} | `{status}` |".format(
                law=table_cell(row["law"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
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
            "## 4. 最窄继续点",
            "",
            "直接攻：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_attack_targets"]),
            "```",
            "",
            "审稿边界：本步证明的是自然残洞质量硬点的非循环改写；它没有证明 prefix 势下界、没有证明容量乘子纪律，也没有关闭行/列无条件命题。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
