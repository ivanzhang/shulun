#!/usr/bin/env python3
"""生成 strict prefix 容量乘子纪律路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_prefix_capacity_multiplier_discipline_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-prefix-capacity-multiplier-discipline-router.md"

HARDPOINT = "RegisteredPrefixCapacityMultiplierDiscipline"
NORMALIZED_MASS = "NormalizedPrefixResidualPotentialLowerBound"
LABEL_ANTICOLLAPSE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
EFFECTIVE_INSTANCE = "PrefixCapacityNormalizedEffectiveTypeInstanceLowerBound"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-prefix-residual-transfer-router.json",
    MONOGRAPH / "prime-matrix-cylindrical-completion-line-barrier.md",
    MONOGRAPH / "prime-matrix-strict-boundary-cap-type-compression-router.md",
    MONOGRAPH / "prime-matrix-strict-forced-obligation-lower-bound-router.md",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


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


def multiplier_laws() -> list[dict[str, str]]:
    """列出容量乘子纪律公式。"""
    return [
        {
            "law": "row_hit_multiplicity_formula",
            "formula": "mu_q(x;P)=#{1<=c<P: c == -xP mod q}=1+floor((P-1-a_q)/q), a_q in [1,q].",
            "status": "closed",
        },
        {
            "law": "uniform_capacity_ceiling",
            "formula": "mu_q(x;P)<=ceil(P/q); in particular q>z gives mu_q<=ceil(P/z).",
            "status": "closed",
        },
        {
            "law": "capacity_normalized_charge",
            "formula": "M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}.",
            "status": "defined_closed",
        },
        {
            "law": "distinct_label_lower_bound",
            "formula": "#distinct tau_z labels >= M#_{x,z}.",
            "status": "closed",
        },
        {
            "law": "label_to_type_gap",
            "formula": "distinct labels do not yet imply enough row-free formal-unit types without anti-collapse.",
            "status": "open",
        },
    ]


def build_rows(prefix_transfer: dict[str, Any]) -> list[dict[str, Any]]:
    """生成容量乘子纪律判定表。"""
    return [
        {
            "gate": "CapacityMultiplierInputActive",
            "closed": prefix_transfer.get("next_direct_attack_target") == HARDPOINT,
            "proved": False,
            "meaning": "上一层把 prefix 加权转移后的直接硬点定为容量乘子纪律。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "本步仍只在早期零行假设下登记每个 q 的行内命中容量。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "ExactRowHitMultiplicityFormulaClosed",
            "closed": True,
            "proved": True,
            "meaning": "固定 q<P 时，覆盖列是单个模 q 余类在 [1,P-1] 的截断，故 mu_q 有显式整式公式。",
            "remaining": "无。",
        },
        {
            "gate": "UniformCapacityCeilingClosed",
            "closed": True,
            "proved": True,
            "meaning": "由公式立得 mu_q<=ceil(P/q)，所以降低 cutoff 后的复用风险被显式乘子控制。",
            "remaining": "乘子可控不等于归一化质量足够大。",
        },
        {
            "gate": "CapacityNormalizedChargeClosed",
            "closed": True,
            "proved": True,
            "meaning": "给每个 prefix atom 赋权 1/mu_tau；同一标签的总权重不超过 1。",
            "remaining": "需要证明总归一化权重超过类型阈值。",
        },
        {
            "gate": "DistinctLabelLowerBoundClosed",
            "closed": True,
            "proved": True,
            "meaning": "按标签分组求和，#distinct labels >= sum_c 1/mu_tau(c)。",
            "remaining": "不同标签到不同 row-free type 仍需防止哈希/quotient 塌缩。",
        },
        {
            "gate": "RegisteredCapacityMultiplierDisciplineClosed",
            "closed": True,
            "proved": True,
            "meaning": "容量乘子字段和归一化记账纪律已经闭合；不能再把 completed-internal 标签的多命中当作免费独立实例。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "NormalizedPrefixPotentialLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 M#_{x,z} 对某个统一 prefix z 超过类型压缩阈值。",
            "remaining": NORMALIZED_MASS,
        },
        {
            "gate": "PrefixLabelToTypeAntiCollapseCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明不同 tau_z 标签或标签骨架不会在 row-free type 投影下大量合并。",
            "remaining": LABEL_ANTICOLLAPSE,
        },
        {
            "gate": "EffectiveTypeInstanceLowerBoundCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "有了容量纪律后，最终仍需归一化质量下界与标签到类型抗塌缩合取。",
            "remaining": f"{NORMALIZED_MASS} AND {LABEL_ANTICOLLAPSE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造容量乘子纪律证书。"""
    prefix_transfer = load_json(MONOGRAPH / "prime-matrix-strict-prefix-residual-transfer-router.json")
    return {
        "certificate_type": "prime_matrix_strict_prefix_capacity_multiplier_discipline_router",
        "status": "prefix_capacity_multiplier_discipline_closed_normalized_potential_anticollapse_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "exact_row_hit_multiplicity_formula_closed": True,
        "uniform_capacity_ceiling_closed": True,
        "capacity_normalized_charge_closed": True,
        "distinct_label_lower_bound_closed": True,
        "registered_prefix_capacity_multiplier_discipline_proved": True,
        "normalized_prefix_residual_potential_lower_bound_proved": False,
        "prefix_label_support_to_row_free_type_anticollapse_proved": False,
        "prefix_capacity_normalized_effective_type_instance_lower_bound_proved": False,
        "boundary_residual_mass_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_after_router": f"{NORMALIZED_MASS} AND {LABEL_ANTICOLLAPSE}",
        "next_direct_attack_target": NORMALIZED_MASS,
        "parallel_attack_target": LABEL_ANTICOLLAPSE,
        "multiplier_laws": multiplier_laws(),
        "rows": build_rows(prefix_transfer),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`RegisteredPrefixCapacityMultiplierDiscipline` 可以闭合为精确乘子记账："
            "每个标签 q 在同一行只命中 mu_q(x;P) 个列，且 mu_q<=ceil(P/q)。"
            "因此 prefix atom 按 1/mu_q 赋权后，同一 q 的总权重至多 1，"
            "归一化质量 M# 下界不同标签数。剩余不是乘子纪律本身，"
            "而是证明 M# 足够大，并证明不同标签不会在 row-free type/quotient 投影下塌缩。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict prefix 容量乘子纪律路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_row_hit_multiplicity_formula_closed={fmt_bool(result['exact_row_hit_multiplicity_formula_closed'])}",
        f"uniform_capacity_ceiling_closed={fmt_bool(result['uniform_capacity_ceiling_closed'])}",
        f"capacity_normalized_charge_closed={fmt_bool(result['capacity_normalized_charge_closed'])}",
        f"distinct_label_lower_bound_closed={fmt_bool(result['distinct_label_lower_bound_closed'])}",
        f"registered_prefix_capacity_multiplier_discipline_proved={fmt_bool(result['registered_prefix_capacity_multiplier_discipline_proved'])}",
        f"normalized_prefix_residual_potential_lower_bound_proved={fmt_bool(result['normalized_prefix_residual_potential_lower_bound_proved'])}",
        f"prefix_label_support_to_row_free_type_anticollapse_proved={fmt_bool(result['prefix_label_support_to_row_free_type_anticollapse_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 乘子公式",
        "",
        "固定 `q<P`，令 `a_q` 是 `-xP mod q` 在 `[1,q]` 中的正代表，其中余数 `0` 写成 `q`。则",
        "",
        "```text",
        "mu_q(x;P)=1+floor((P-1-a_q)/q),",
        "mu_q(x;P)<=ceil(P/q).",
        "```",
        "",
        "对 prefix canonical label `tau_z(c)` 定义",
        "",
        "```text",
        "M#_{x,z}=sum_{c in R_{x,z}} 1/mu_{tau_z(c)}.",
        "```",
        "",
        "同一标签 `q` 至多贡献 `mu_q` 个 atom，因此其归一化总贡献至多 `1`，从而 `#distinct labels >= M#_{x,z}`。",
        "",
        "## 2. 乘子律",
        "",
        "| law | formula | status |",
        "| --- | --- | --- |",
    ]
    for row in result["multiplier_laws"]:
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            result["parallel_attack_target"],
            "```",
            "",
            "审稿边界：本步闭合的是 prefix 标签复用的精确乘子记账；它没有证明归一化残洞势下界，也没有关闭行/列无条件命题。",
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
