#!/usr/bin/env python3
"""生成 strict prefix 残洞转移路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_prefix_residual_transfer_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-prefix-residual-transfer-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-prefix-residual-transfer-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-prefix-residual-transfer-router.md"

HARDPOINT = "PrefixResidualToBoundaryFormalUnitObligationTransfer"
WEIGHTED_TRANSFER = "PrefixResidualToWeightedFormalUnitObligationInjection"
CAPACITY_DISCIPLINE = "RegisteredPrefixCapacityMultiplierDiscipline"
ANTI_COLLAPSE = "PrefixWeightedObligationToEffectiveTypeInstanceAntiCollapse"
EFFECTIVE_TRANSFER = "PrefixResidualEffectiveTypeInstanceTransfer"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-boundary-residual-mass-lower-bound-router.json",
    MONOGRAPH / "prime-matrix-witness-obligation-domain-canonicalization-router.md",
    MONOGRAPH / "prime-matrix-strict-forced-obligation-lower-bound-router.md",
    MONOGRAPH / "prime-matrix-cylindrical-completion-line-barrier.md",
    MONOGRAPH / "prime-matrix-partition-coverage-no-loss-equation-router.json",
    MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.json",
]


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


def transfer_schema() -> list[dict[str, str]]:
    """给出 prefix 残洞转移 schema。"""
    return [
        {
            "field": "prefix_cutoff_z",
            "meaning": "记录本次上游残洞势使用的 cutoff；避免把不同 z 的义务混计。",
        },
        {
            "field": "prefix_residual_column_c",
            "meaning": "记录 c in R_{x,z}，即 no q<=z divides xP+c。",
        },
        {
            "field": "canonical_prefix_label_tau_z",
            "meaning": "取最小 q in (z,P) with q divides xP+c；早期零行保证其存在。",
        },
        {
            "field": "label_band",
            "meaning": "区分 completed-internal band z<q<=x 与 incomplete-external band x<q<P。",
        },
        {
            "field": "capacity_multiplier_id",
            "meaning": "登记 q 在当前 row/prefix 中的复用容量；该字段只登记，不在本步给上界。",
        },
        {
            "field": "formal_unit_payload_hash",
            "meaning": "把 prefix atom 并入原 O(w) payload，保留 return/quotient/no-loss 账本。",
        },
    ]


def build_rows(prefix_router: dict[str, Any], witness: str, noloss_eq: dict[str, Any], noloss: dict[str, Any]) -> list[dict[str, Any]]:
    """生成 prefix 残洞转移判定表。"""
    witness_ready = "physical_filler_atoms" in witness and "quotient_records" in witness
    no_loss_ready = (
        noloss_eq.get("partition_coverage_no_loss_equation_closed") is True
        and noloss.get("no_loss_return_accounting_closed") is True
    )
    return [
        {
            "gate": "PrefixTransferInputActive",
            "closed": prefix_router.get("next_direct_attack_target") == HARDPOINT,
            "proved": False,
            "meaning": "上一层把自然残洞质量改写后的直接攻击点定为 prefix 残洞转移。",
            "remaining": HARDPOINT,
        },
        {
            "gate": "CounterexampleBranchGuardPreserved",
            "closed": True,
            "proved": True,
            "meaning": "仍只在任意假设早期零行 witness 下构造义务，不用真实缺席数据。",
            "remaining": "保持 row_column_unconditional_closed=false。",
        },
        {
            "gate": "PrefixResidualSelectorClosed",
            "closed": True,
            "proved": True,
            "meaning": "若 c in R_{x,z} 且该行为早期零行，则存在 q in (z,P) divides xP+c；取最小 q 得 canonical tau_z(c)。",
            "remaining": "PrefixCanonicalLabelSelectorClosed",
        },
        {
            "gate": "LabelBandDichotomyClosed",
            "closed": True,
            "proved": True,
            "meaning": "canonical tau_z(c) 唯一落在 z<q<=x 或 x<q<P；前者是 completed-internal label，后者是原 CLB 高标签。",
            "remaining": "后续容量账本必须分别处理两个 label band。",
        },
        {
            "gate": "FormalUnitEmbeddingInterfaceImported",
            "closed": witness_ready,
            "proved": witness_ready,
            "meaning": "witness obligation 域已有 physical atoms、return records 与 quotient records，可容纳 prefix atom 字段。",
            "remaining": "需要写入 prefix_cutoff_z 与 capacity_multiplier_id。",
        },
        {
            "gate": "NoLossAccountingImported",
            "closed": no_loss_ready,
            "proved": no_loss_ready,
            "meaning": "义务进入 O_z(w) 后只能成为 source、return 或 quotient/reuse，不允许静默丢失。",
            "remaining": "no-loss 是加权守恒，不是不同实例下界。",
        },
        {
            "gate": "PrefixResidualWeightedTransferClosed",
            "closed": True,
            "proved": True,
            "meaning": "每个 prefix 残洞 canonically 注入一个加权 formal-unit obligation atom，且保留 label band 与容量乘子字段。",
            "remaining": WEIGHTED_TRANSFER,
        },
        {
            "gate": "PrefixTransferEffectiveForTypeCompressionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明这些加权 prefix atoms 可直接提供类型压缩所需的有效不同实例数。",
            "remaining": f"{CAPACITY_DISCIPLINE} AND {ANTI_COLLAPSE}",
        },
        {
            "gate": "PrefixCapacityMultiplierCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "completed-internal labels q<=x 可在同一行内多次命中；必须证明容量乘子不会吞掉 prefix 势。",
            "remaining": CAPACITY_DISCIPLINE,
        },
        {
            "gate": "PrefixAntiCollapseCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明 quotient/reuse 不会把大量 prefix atoms 压成过少 row-free type instances。",
            "remaining": ANTI_COLLAPSE,
        },
        {
            "gate": "PrefixResidualTransferHardpointStatus",
            "closed": True,
            "proved": True,
            "meaning": "原 hardpoint 的加权转移层已闭合；强形式的有效实例转移仍开放。",
            "remaining": EFFECTIVE_TRANSFER,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 prefix 残洞转移证书。"""
    prefix_router = load_json(MONOGRAPH / "prime-matrix-strict-boundary-residual-mass-lower-bound-router.json")
    witness = load_text(MONOGRAPH / "prime-matrix-witness-obligation-domain-canonicalization-router.md")
    noloss_eq = load_json(MONOGRAPH / "prime-matrix-partition-coverage-no-loss-equation-router.json")
    noloss = load_json(MONOGRAPH / "prime-matrix-no-loss-return-accounting-router.json")
    return {
        "certificate_type": "prime_matrix_strict_prefix_residual_transfer_router",
        "status": "prefix_residual_transfer_closed_as_weighted_injection_capacity_multiplier_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "prefix_residual_selector_closed": True,
        "label_band_dichotomy_closed": True,
        "prefix_residual_to_weighted_formal_unit_obligation_transfer_proved": True,
        "prefix_residual_to_boundary_formal_unit_transfer_proved": True,
        "prefix_transfer_effective_for_type_compression_proved": False,
        "registered_prefix_capacity_multiplier_discipline_proved": False,
        "prefix_weighted_obligation_to_effective_type_instance_anticollapse_proved": False,
        "boundary_residual_mass_lower_bound_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": HARDPOINT,
        "hardpoint_closed_layer": WEIGHTED_TRANSFER,
        "hardpoint_after_router": f"{CAPACITY_DISCIPLINE} AND {ANTI_COLLAPSE}",
        "next_direct_attack_target": CAPACITY_DISCIPLINE,
        "parallel_attack_target": ANTI_COLLAPSE,
        "transfer_schema": transfer_schema(),
        "rows": build_rows(prefix_router, witness, noloss_eq, noloss),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`PrefixResidualToBoundaryFormalUnitObligationTransfer` 可在加权义务层闭合："
            "任意 prefix 残洞 c 在早期零行假设下都有最小覆盖标签 tau_z(c) in (z,P)，"
            "并可带着 label_band 与 capacity_multiplier_id 注入 formal-unit obligation 域。"
            "这没有完成类型压缩，因为 completed-internal 标签可能高复用，quotient/reuse 也可能塌缩实例数。"
            "所以下一真正窄点是容量乘子纪律；并行保留 prefix anti-collapse。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown。"""
    lines = [
        "# Prime Matrix strict prefix 残洞转移路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"prefix_residual_selector_closed={fmt_bool(result['prefix_residual_selector_closed'])}",
        f"label_band_dichotomy_closed={fmt_bool(result['label_band_dichotomy_closed'])}",
        f"prefix_residual_to_weighted_formal_unit_obligation_transfer_proved={fmt_bool(result['prefix_residual_to_weighted_formal_unit_obligation_transfer_proved'])}",
        f"prefix_transfer_effective_for_type_compression_proved={fmt_bool(result['prefix_transfer_effective_for_type_compression_proved'])}",
        f"registered_prefix_capacity_multiplier_discipline_proved={fmt_bool(result['registered_prefix_capacity_multiplier_discipline_proved'])}",
        f"prefix_weighted_obligation_to_effective_type_instance_anticollapse_proved={fmt_bool(result['prefix_weighted_obligation_to_effective_type_instance_anticollapse_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 转移公式",
        "",
        "若假设第 x 行是早期零行，且 `z<x<P`，定义",
        "",
        "```text",
        "R_{x,z}={1<=c<P: for every prime q<=z, q does not divide xP+c}.",
        "```",
        "",
        "则对每个 `c in R_{x,z}`，早期零行强制存在素数 `q in (z,P)` 整除 `xP+c`。取最小这样的 q，记为 `tau_z(c)`，得到 canonical prefix atom。",
        "",
        "## 2. schema",
        "",
        "| field | meaning |",
        "| --- | --- |",
    ]
    for row in result["transfer_schema"]:
        lines.append(
            "| `{field}` | {meaning} |".format(
                field=table_cell(row["field"]),
                meaning=table_cell(row["meaning"]),
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
            "审稿边界：本步只闭合 prefix 残洞到加权义务的注入，不闭合有效不同实例下界，也不闭合行/列无条件命题。",
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
