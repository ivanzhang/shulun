#!/usr/bin/env python3
"""审查逆元 tau 兄弟收费的统一 envelope 是否足够闭合。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_sibling_charge_uniform_envelope_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.json

输出：
  docs/monograph/prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.json
  docs/monograph/prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.md
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DATA = ROOT / "data"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-sibling-charge-uniform-envelope-router.md"

PROFILE_LEDGER = DATA / "inverse-alignment-exact-zero-row-charge-profile-ledger.json"
SOURCE_FILES = [
    PROFILE_LEDGER,
    DOCS / "prime-matrix-inverse-alignment-exact-zero-row-charge-profile-router.json",
    DOCS / "prime-matrix-strict-cold-window-sibling-charging-router.json",
    DOCS / "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json",
]

RAW_ENVELOPE = "RawInverseAlignmentTauChargeEnvelope"
TARGET = "ExactInverseAlignmentSiblingChargeUniformEnvelope"
STRICT_TARGET = "ColdRestrictedInverseAlignmentSiblingChargeEnvelope"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
ALPHA = 0.43


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    result = {
        "experiments/prime_matrix_inverse_alignment_sibling_charge_uniform_envelope_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def sample_envelope_rows(ledger: dict[str, Any]) -> list[dict[str, Any]]:
    """从精确剖面中抽取 envelope 样本。"""
    rows: list[dict[str, Any]] = []
    for profile_row in ledger.get("profile_rows", []):
        P = int(profile_row["P"])
        x = int(profile_row["minimal_alignment_x"])
        canonical_z = max(
            profile_row["prefix_tau_profiles"],
            key=lambda item: (int(item["z"]) <= int(P**ALPHA), int(item["z"])),
        )
        for item in profile_row["prefix_tau_profiles"]:
            if int(item["z"]) == int(P**ALPHA):
                canonical_z = item
                break
        assigned = int(canonical_z["assigned_atoms"])
        appeared = int(canonical_z["appeared_tau_capacity_sum_mu"])
        suffix = int(canonical_z["suffix_capacity_sum_mu"])
        rows.append(
            {
                "P": P,
                "x": x,
                "z": int(canonical_z["z"]),
                "R_xz_size": int(canonical_z["R_xz_size"]),
                "assigned_atoms": assigned,
                "appeared_capacity_sum_mu": appeared,
                "suffix_capacity_sum_mu": suffix,
                "appeared_capacity_per_atom": None if assigned == 0 else appeared / assigned,
                "suffix_capacity_per_atom": None if assigned == 0 else suffix / assigned,
                "raw_suffix_capacity_ge_assigned": suffix >= assigned,
            }
        )
    return rows


def asymptotic_rows() -> list[dict[str, Any]]:
    """给出 raw envelope 的尺度诊断。"""
    rows: list[dict[str, Any]] = []
    log_inverse_alpha = math.log(1 / ALPHA)
    for P in [10**5, 10**6, 10**9, 10**12]:
        z = P**ALPHA
        raw_scale = P * log_inverse_alpha
        demand_scale = z / math.log(z)
        rows.append(
            {
                "P": P,
                "alpha": ALPHA,
                "z": z,
                "raw_suffix_capacity_model": raw_scale,
                "normalized_demand_model": demand_scale,
                "raw_over_demand_ratio": raw_scale / demand_scale,
            }
        )
    return rows


def theorem_rows() -> list[dict[str, str]]:
    """列出本步证明和拒绝的 envelope。"""
    return [
        {
            "name": "raw_tau_capacity_envelope",
            "statement": "sum_{q>z, tau bucket appears} mu_q <= sum_{z<q<P} ceil((P-1)/q).",
            "status": "closed",
        },
        {
            "name": "mertens_scale",
            "statement": "for z=P^alpha, the raw envelope has scale about P log(1/alpha).",
            "status": "closed_as_scale_diagnostic",
        },
        {
            "name": "raw_envelope_insufficient",
            "statement": "P log(1/alpha) is too large to close the current cold-supply budget against P^alpha/log P demand.",
            "status": "closed_negative_result",
        },
        {
            "name": "cold_restricted_envelope_needed",
            "statement": "only tau buckets that remain cold-compatible after terminal window tests may be counted as cold supply.",
            "status": "next_input",
        },
    ]


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        {
            "gate": "ExactTauChargeImported",
            "closed": result["exact_tau_charge_profile_imported"],
            "proved": result["exact_tau_charge_profile_imported"],
            "meaning": "逆元剖面已给出 tau 桶、mu_tau 和实际 assigned atom。",
            "remaining": "none for raw identity",
        },
        {
            "gate": "RawInverseAlignmentTauChargeEnvelopeClosed",
            "closed": result["raw_inverse_alignment_tau_charge_envelope_closed"],
            "proved": result["raw_inverse_alignment_tau_charge_envelope_closed"],
            "meaning": "tau 兄弟收费有一个无条件 raw 上界：所有 q>z 的 mu_q 总和。",
            "remaining": "scale is too large",
        },
        {
            "gate": "RawEnvelopeScaleMismatchCertified",
            "closed": result["raw_envelope_scale_mismatch_certified"],
            "proved": result["raw_envelope_scale_mismatch_certified"],
            "meaning": "z=P^0.43 时 raw 上界为 Θ(P)，不能闭合当前冷供给预算。",
            "remaining": STRICT_TARGET,
        },
        {
            "gate": "ExactInverseAlignmentSiblingChargeUniformEnvelopeProved",
            "closed": False,
            "proved": False,
            "meaning": "不带冷兼容过滤的逆元 tau envelope 过宽，不能作为最终父级预算。",
            "remaining": STRICT_TARGET,
        },
        {
            "gate": "ColdRestrictedEnvelopeProved",
            "closed": False,
            "proved": False,
            "meaning": "还需把终端冷窗口、热回流、固定历史回流条件压入 tau 桶筛选。",
            "remaining": f"{SIBLING_NUMERIC} AND {HOT_CORE} AND {FIXED_HISTORY}",
        },
        {
            "gate": "RowColumnUnconditionalClosureReached",
            "closed": False,
            "proved": False,
            "meaning": "仍未得到早期零行反例链与真实链的终端矛盾。",
            "remaining": f"{STRICT_TARGET} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造证书对象。"""
    ledger = load_json(PROFILE_LEDGER)
    samples = sample_envelope_rows(ledger)
    raw_closed = bool(samples) and all(row["raw_suffix_capacity_ge_assigned"] for row in samples)
    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_inverse_alignment_sibling_charge_uniform_envelope_router",
        "status": "raw_inverse_alignment_tau_envelope_closed_but_scale_insufficient_cold_restricted_envelope_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "exact_tau_charge_profile_imported": bool(ledger.get("all_prefix_tau_charge_identities_ok")),
        "raw_inverse_alignment_tau_charge_envelope_closed": raw_closed,
        "raw_envelope_scale_mismatch_certified": True,
        "exact_inverse_alignment_sibling_charge_uniform_envelope_proved": False,
        "cold_restricted_inverse_alignment_sibling_charge_envelope_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": TARGET,
        "hardpoint_after_router": f"{STRICT_TARGET} AND {SIBLING_NUMERIC}",
        "next_direct_attack_target": STRICT_TARGET,
        "parallel_attack_targets": [
            SIBLING_NUMERIC,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "sample_envelope_rows": samples,
        "asymptotic_scale_rows": asymptotic_rows(),
        "theorem_rows": theorem_rows(),
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "精确逆元 tau 兄弟剖面给出了一个无条件 raw envelope：出现的 tau 桶容量不超过 "
            "`sum_{z<q<P} ceil((P-1)/q)`。但这个 envelope 在 `z=P^0.43` 时是 `Θ(P)` 级，"
            "尺度远大于当前需求侧的 `P^0.43/log P` 级目标，因此不能直接闭合冷供给预算。"
            "这说明逆元方程组必须继续与终端冷窗口条件结合：只有仍通过冷兼容测试且没有热核心、"
            "固定历史或 PDEC/ColumnCRT 回流的 tau 兄弟桶，才可以计入冷供给。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 文档。"""
    lines = [
        "# Prime Matrix 逆元 tau 兄弟收费统一 Envelope 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_tau_charge_profile_imported={fmt_bool(result['exact_tau_charge_profile_imported'])}",
        f"raw_inverse_alignment_tau_charge_envelope_closed={fmt_bool(result['raw_inverse_alignment_tau_charge_envelope_closed'])}",
        f"raw_envelope_scale_mismatch_certified={fmt_bool(result['raw_envelope_scale_mismatch_certified'])}",
        f"exact_inverse_alignment_sibling_charge_uniform_envelope_proved={fmt_bool(result['exact_inverse_alignment_sibling_charge_uniform_envelope_proved'])}",
        f"cold_restricted_inverse_alignment_sibling_charge_envelope_proved={fmt_bool(result['cold_restricted_inverse_alignment_sibling_charge_envelope_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Envelope 结论",
        "",
        "| name | statement | status |",
        "| --- | --- | --- |",
    ]
    for row in result["theorem_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['name'])}`",
                    table_cell(row["statement"]),
                    f"`{table_cell(row['status'])}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 2. 样本 Envelope",
            "",
            "| P | x | z | R_xz | appeared capacity | suffix capacity | suffix/atom |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["sample_envelope_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["P"]),
                    str(row["x"]),
                    str(row["z"]),
                    str(row["R_xz_size"]),
                    str(row["appeared_capacity_sum_mu"]),
                    str(row["suffix_capacity_sum_mu"]),
                    "nan" if row["suffix_capacity_per_atom"] is None else f"{row['suffix_capacity_per_atom']:.3f}",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 3. 尺度诊断",
            "",
            "| P | z=P^0.43 | raw model | demand model | raw/demand |",
            "| ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for row in result["asymptotic_scale_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["P"]),
                    f"{row['z']:.3f}",
                    f"{row['raw_suffix_capacity_model']:.3f}",
                    f"{row['normalized_demand_model']:.3f}",
                    f"{row['raw_over_demand_ratio']:.3f}",
                ]
            )
            + " |"
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
    for row in result["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## 5. 下一步",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 并行保留：",
        ]
    )
    for target in result["parallel_attack_targets"]:
        lines.append(f"  - `{target}`")
    lines.extend(
        [
            "",
            "审稿边界：本步证明 raw envelope 的存在和不足，不声明反例矛盾已闭合。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for file_name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(file_name)}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(json.dumps({"status": result["status"], "next": result["next_direct_attack_target"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
