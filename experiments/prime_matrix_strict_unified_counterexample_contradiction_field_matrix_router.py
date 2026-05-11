#!/usr/bin/env python3
"""生成 strict 早期零行统一矛盾场矩阵路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_unified_counterexample_contradiction_field_matrix_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONOGRAPH = DOCS / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-unified-counterexample-contradiction-field-matrix-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-counterexample-true-structure-cycle-cut-router.md",
    MONOGRAPH / "prime-matrix-strict-stable-short-return-defect-attack-router.md",
    MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.md",
    MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.md",
    MONOGRAPH / "prime-matrix-early-zero-phase-defect-schema-router.md",
    MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.md",
    DOCS / "local-label-conflict-scan.json",
]

UNIFIED_FIELD = "UnifiedCounterexampleTrueStructureContradictionField"
BLOCK_CAPACITY = "BlockCoprimeDynamicsCapacitySurplus"
FINITE_SUPPLY = "FinitePrimeSupplyVsCoprimeDynamicsLoad"
QUOTIENT_DYNAMICS = "AdjacentQuotientCoprimeDynamicsLedger"
TYPE_THRESHOLD = "FormalUnitTypeThresholdLedger"
ANTI_COLLAPSE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
B3_REMAINDER = "B3RemainderTotalVariationBudgetForLengthP"
MAIN_COEFF = "B3ContinuousBetaSieveCoefficientSurplusAlpha043AndDiscretePrimeSumUniformError"
FINITE_PREFIX = "FiniteBoundaryPrefixRoughCountCertificate"
DRIFT_DEFECT = "SignatureDriftToRegisteredPhaseDefectTheorem"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    """读取文本；缺失时返回空字符串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
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


def rigidity_laws() -> list[dict[str, str]]:
    """列出统一矛盾场使用的刚性律。"""
    return [
        {
            "law": "adjacent_integer_coprime",
            "formula": "gcd(xP+c, xP+c+1)=1.",
            "status": "closed",
            "role": "相邻列的全部因子支撑不相交。",
        },
        {
            "law": "quotient_cross_coprime",
            "formula": "If xP+c=tau_c m_c and xP+c+1=tau_{c+1}m_{c+1}, then every factor from the first product is coprime to every factor from the second.",
            "status": "closed",
            "role": "商相邻互质动力系统的基本守恒。",
        },
        {
            "law": "unimodular_neighbor_equation",
            "formula": "tau_{c+1}m_{c+1}-tau_c m_c=1.",
            "status": "closed",
            "role": "把连续合数链写成相邻乘法坐标的刚性差分系统。",
        },
        {
            "law": "short_distance_label_reuse",
            "formula": "If a prime q divides both xP+c and xP+c+d, then q divides d; hence q>d cannot be reused at distance d.",
            "status": "closed",
            "role": "大标签在短块内近似一次性消耗。",
        },
        {
            "law": "block_label_capacity",
            "formula": "For a block of length L, a fixed q can cover at most ceil(L/q) canonical prefix atoms.",
            "status": "closed",
            "role": "有限素因子供给的局部容量上界。",
        },
        {
            "law": "prefix_mass_lower_route",
            "formula": "|R_{x,z}| >= (P-1)W^- - TV(lambda^-), and M#>=|R_{x,z}|/ceil(P/z).",
            "status": "reduced_open",
            "role": "给反例链施加强制输入负载。",
        },
        {
            "law": "no_loss_named_return",
            "formula": "Every failed or drifting obligation remains as PDEC/SAE/ColumnCRT/quotient/reuse return.",
            "status": "closed_as_accounting",
            "role": "防止把矛盾压力静默丢失。",
        },
    ]


def contradiction_matrix() -> list[dict[str, str]]:
    """给出可能矛盾交点矩阵。"""
    return [
        {
            "field": "stable_same_label_recurrence",
            "counterexample_chain": "类型压缩迫使同 formal unit 同标签短复现。",
            "true_rigidity_chain": "同标签短复现要求 prod(Q)|Delta；短 Delta<prod(Q) 不可能。",
            "closed_part": "CRT 短复现矛盾已闭合。",
            "remaining": "BoundaryCap/Prefix 有效实例下界与重复 type -> same label。",
        },
        {
            "field": "prefix_mass_vs_finite_label_supply",
            "counterexample_chain": "早期零行迫使每个 prefix 残洞选一个 tau_z(c) in (z,P)。",
            "true_rigidity_chain": "每个 q 在块长 L 中容量 <=ceil(L/q)，总容量是有限素数供给和。",
            "closed_part": "prefix 加权转移、容量乘子、M# 到粗筛余公式已闭合。",
            "remaining": f"{B3_REMAINDER} AND {MAIN_COEFF} AND {FINITE_PREFIX}",
        },
        {
            "field": "adjacent_coprime_quotient_dynamics",
            "counterexample_chain": "连续合数链要求每列都有 tau_c m_c 分解并满足 tau_{c+1}m_{c+1}-tau_c m_c=1。",
            "true_rigidity_chain": "相邻列全部因子支撑互质；大标签短距不能复用；商链也相邻互质。",
            "closed_part": "相邻互质、商互质、短距复用禁止均为整数恒等式。",
            "remaining": f"{BLOCK_CAPACITY} / {FINITE_SUPPLY}",
        },
        {
            "field": "drift_to_named_defect",
            "counterexample_chain": "为避免稳定复现，phase_key、anchor、label skeleton 或 quotient records 必须漂移。",
            "true_rigidity_chain": "no-loss 账本要求所有漂移进入 PDEC/SAE/ColumnCRT 命名桶。",
            "closed_part": "schema 准入与 no-loss accounting 已闭合。",
            "remaining": f"{DRIFT_DEFECT} and terminal exclusion。",
        },
        {
            "field": "low_prefix_mass_defect",
            "counterexample_chain": "若 prefix 粗筛余本身不足，反例避开质量压力。",
            "true_rigidity_chain": "低模端点筛余异常必须登记为 PDEC/SAE/ColumnCRT，而不是自由失败。",
            "closed_part": "缺陷路线已定义。",
            "remaining": "LowPrefixResidualMassToRegisteredPhaseDefect。",
        },
        {
            "field": "bottom_pair_curve",
            "counterexample_chain": "底部带早期零行要求残洞全部落入 c=a(h-a) 高素对曲线或素数为空。",
            "true_rigidity_chain": "底部精确分解给 |F_{P-h}|<=floor(h/2)，残洞质量若超过即矛盾。",
            "closed_part": "二次缺口曲线分解已闭合。",
            "remaining": "BottomPrimeWindow 或其 PDEC/SAE 回流。",
        },
    ]


def build_rows(
    uniform_prefix: dict[str, Any],
    capacity: dict[str, Any],
    early_schema: str,
    noloss: dict[str, Any],
    local_scan: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成统一矛盾场判定表。"""
    adjacent_scan_ready = local_scan.get("status") == (
        "adjacent_labels_are_forced_disjoint_and_short_distance_large_label_reuse_is_forbidden"
    )
    return [
        {
            "gate": "UnifiedFieldInputActive",
            "closed": True,
            "proved": False,
            "meaning": "把当前反例链所有压力源统一到同一个矩阵，而不宣称任一开放出口已排斥。",
            "remaining": UNIFIED_FIELD,
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "所有结论都在假设早期零行下推导；不使用真实零行缺席替代证明。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "AdjacentCoprimeDynamicsClosed",
            "closed": True,
            "proved": True,
            "meaning": "连续整数相邻互质，任意因子分解后的标签与商在相邻列之间全互质。",
            "remaining": QUOTIENT_DYNAMICS,
        },
        {
            "gate": "ShortDistanceLargeLabelReuseForbiddenClosed",
            "closed": True,
            "proved": True,
            "meaning": "同一素标签若命中距离 d 的两列，则必整除 d；所以大于 d 的标签不能短距复用。",
            "remaining": "可进入 block capacity。",
        },
        {
            "gate": "LocalLabelConflictScanImportedAsDiagnostic",
            "closed": adjacent_scan_ready,
            "proved": True,
            "meaning": "已有扫描支持相邻标签不交与短距大标签不可复用，但该扫描只作诊断，不作全局证明。",
            "remaining": "正式证明由整数恒等式给出。",
        },
        {
            "gate": "BlockCapacityEnvelopeClosed",
            "closed": True,
            "proved": True,
            "meaning": "块长 L 内，每个 canonical label q 的容量 <=ceil(L/q)，有限供给容量上界可写成 sum_{z<q<P}ceil(L/q)。",
            "remaining": BLOCK_CAPACITY,
        },
        {
            "gate": "PrefixMassInputReduced",
            "closed": uniform_prefix.get("main_error_split_closed") is True,
            "proved": False,
            "meaning": "强制负载 |R_{x,z}| 已压成 beta 主项减总变差；尚未得到全局正下界。",
            "remaining": f"{B3_REMAINDER} AND {MAIN_COEFF} AND {FINITE_PREFIX}",
        },
        {
            "gate": "CapacityMultiplierImported",
            "closed": capacity.get("registered_prefix_capacity_multiplier_discipline_proved") is True,
            "proved": capacity.get("registered_prefix_capacity_multiplier_discipline_proved") is True,
            "meaning": "行内标签复用乘子已精确登记，不能重复计算同一素数供给。",
            "remaining": TYPE_THRESHOLD,
        },
        {
            "gate": "NoLossNamedReturnImported",
            "closed": noloss.get("no_loss_return_accounting_closed") is True and "schema admission" in early_schema.lower(),
            "proved": noloss.get("no_loss_return_accounting_closed") is True,
            "meaning": "漂移、复用、quotient 与终端失败不允许消失，必须回到命名缺陷桶。",
            "remaining": DRIFT_DEFECT,
        },
        {
            "gate": "CoprimeDynamicsSupplyContradictionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "相邻/商互质刚性本身已闭合，但尚未证明某个块的强制负载超过有限素因子供给容量。",
            "remaining": f"{BLOCK_CAPACITY} AND {FINITE_SUPPLY}",
        },
        {
            "gate": "UnifiedContradictionFieldCurrentCorpusClosed",
            "closed": False,
            "proved": False,
            "meaning": "统一矩阵已建立；明显直接矛盾仍需在某个交点完成严格不等式或终端排斥。",
            "remaining": f"({B3_REMAINDER} AND {MAIN_COEFF} AND {FINITE_PREFIX} AND {TYPE_THRESHOLD} AND {ANTI_COLLAPSE}) OR {BLOCK_CAPACITY} OR {DRIFT_DEFECT}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造统一矛盾场矩阵证书。"""
    uniform_prefix = load_json(MONOGRAPH / "prime-matrix-strict-uniform-prefix-rough-count-router.json")
    capacity = load_json(MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json")
    noloss = load_json(MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.json")
    local_scan = load_json(DOCS / "local-label-conflict-scan.json")
    early_schema = load_text(MONOGRAPH / "prime-matrix-early-zero-phase-defect-schema-router.md")
    return {
        "certificate_type": "prime_matrix_strict_unified_counterexample_contradiction_field_matrix_router",
        "status": "unified_contradiction_field_matrix_built_coprime_dynamics_integrated_intersection_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "adjacent_coprime_dynamics_closed": True,
        "quotient_cross_coprime_dynamics_closed": True,
        "short_distance_large_label_reuse_forbidden_closed": True,
        "block_capacity_envelope_closed": True,
        "coprime_dynamics_finite_supply_contradiction_proved": False,
        "unified_contradiction_field_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": BLOCK_CAPACITY,
        "mass_route_target": B3_REMAINDER,
        "parallel_targets": [MAIN_COEFF, FINITE_PREFIX, TYPE_THRESHOLD, ANTI_COLLAPSE, DRIFT_DEFECT],
        "rigidity_laws": rigidity_laws(),
        "contradiction_matrix": contradiction_matrix(),
        "rows": build_rows(uniform_prefix, capacity, early_schema, noloss, local_scan),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "统一矛盾场已把早期零行的连续合数链、相邻互质/商相邻互质动力系统、"
            "prefix 残洞强制负载、容量乘子、类型压缩和命名缺陷回流放进同一矩阵。"
            "新增的确定刚性是：若 xP+c=tau_c m_c 与 xP+c+1=tau_{c+1}m_{c+1}，"
            "则两侧全部因子支撑互质，并满足 tau_{c+1}m_{c+1}-tau_c m_c=1；"
            "若同一素标签命中距离 d 的两列，则该标签必须整除 d。"
            "这给出有限素因子供给的局部容量场，但尚未证明强制负载超过该容量。"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict 统一反例矛盾场矩阵路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"adjacent_coprime_dynamics_closed={fmt_bool(result['adjacent_coprime_dynamics_closed'])}",
        f"quotient_cross_coprime_dynamics_closed={fmt_bool(result['quotient_cross_coprime_dynamics_closed'])}",
        f"short_distance_large_label_reuse_forbidden_closed={fmt_bool(result['short_distance_large_label_reuse_forbidden_closed'])}",
        f"block_capacity_envelope_closed={fmt_bool(result['block_capacity_envelope_closed'])}",
        f"coprime_dynamics_finite_supply_contradiction_proved={fmt_bool(result['coprime_dynamics_finite_supply_contradiction_proved'])}",
        f"unified_contradiction_field_closed={fmt_bool(result['unified_contradiction_field_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 动力系统刚性",
        "",
        "在早期零行假设下，每个被选中的覆盖原子可写为",
        "",
        "```text",
        "xP+c = tau_c m_c.",
        "```",
        "",
        "连续列满足",
        "",
        "```text",
        "tau_{c+1} m_{c+1} - tau_c m_c = 1.",
        "```",
        "",
        "因此相邻两列的标签、商、以及它们的任意因子支撑全互质。更一般地，若同一素数 q 同时命中距离 d 的两列，则 q|d；所以 q>d 的标签不能在该短距离复用。",
        "",
        "## 2. 刚性律",
        "",
        "| law | formula | status | role |",
        "| --- | --- | --- | --- |",
    ]
    for row in result["rigidity_laws"]:
        lines.append(
            "| `{law}` | {formula} | `{status}` | {role} |".format(
                law=table_cell(row["law"]),
                formula=table_cell(row["formula"]),
                status=table_cell(row["status"]),
                role=table_cell(row["role"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 矛盾场矩阵",
            "",
            "| field | counterexample chain | true rigidity chain | closed part | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["contradiction_matrix"]:
        lines.append(
            "| `{field}` | {counterexample_chain} | {true_rigidity_chain} | {closed_part} | {remaining} |".format(
                field=table_cell(row["field"]),
                counterexample_chain=table_cell(row["counterexample_chain"]),
                true_rigidity_chain=table_cell(row["true_rigidity_chain"]),
                closed_part=table_cell(row["closed_part"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 判定表",
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
            "## 5. 下一最窄交点",
            "",
            "优先寻找局部块上的负载超过供给：",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "质量路线仍保留当前主硬点：",
            "",
            "```text",
            result["mass_route_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " AND ".join(result["parallel_targets"]),
            "```",
            "",
            "审稿边界：本步建立统一矛盾场和闭合若干整数刚性律；没有证明某个交点的不等式已经反超容量，因此不能升级为无条件闭合。",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
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
