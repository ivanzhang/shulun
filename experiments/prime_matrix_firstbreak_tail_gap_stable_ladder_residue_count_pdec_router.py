#!/usr/bin/env python3
"""生成 stable ladder primitive fiber PDEC 的余数计数反演证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_stable_ladder_residue_count_pdec_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-residue-count-pdec-router.md"

PREVIOUS_CERT = DOCS / "prime-matrix-firstbreak-tail-gap-stable-ladder-pivot-fiber-pdec-router.json"
PREVIOUS_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderPrimitiveFiberPDECCap"

IMPORT = "StableActualLadderPrimitiveFiberPDECImportedLedger"
COUNT_VECTOR = "StableLadderPivotFiberResidueCountVectorLedger"
ZERO_MEAN = "StableLadderPivotFiberZeroMeanDeviationLedger"
CHAR_INVERSION = "StableLadderPivotFiberCharacterToResidueDeviationLedger"
RESIDUE_LOCALIZATION = "StableLadderPivotFiberResidueImbalanceLocalizationLedger"
THRESHOLD = "StableLadderPivotFiberResidueImbalanceThresholdLedger"
NO_ANON = "NoAnonymousPrimitiveFiberCharacterPDECExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterResidueCountLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderResidueCountPDECCap"

REDUCED_TARGET = (
    f"{IMPORT} AND {COUNT_VECTOR} AND {ZERO_MEAN} AND {CHAR_INVERSION} "
    f"AND {RESIDUE_LOCALIZATION} AND {THRESHOLD} AND {NO_ANON} "
    f"AND {SPARSE} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
    paths = [Path(__file__).resolve(), PREVIOUS_CERT]
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


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的 primitive fiber 硬点替换成余数计数分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造余数计数 PDEC 判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "StableActualLadderPrimitiveFiberPDECImported",
            imported,
            False,
            "上一层把稳定 ladder 的全局 Fourier cap 局部化为单坐标 pivot 纤维角色相关。",
            PREVIOUS_TARGET,
        ),
        row(
            "StableLadderPivotFiberResidueCountVectorClosed",
            True,
            True,
            "在固定补坐标纤维 S_h 内定义 M_r=#{n in S_h:n=r mod q_j} 与 L=|S_h|。",
            COUNT_VECTOR,
        ),
        row(
            "StableLadderPivotFiberZeroMeanDeviationClosed",
            True,
            True,
            "定义 D_r=M_r-L/q_j，则 sum_r D_r=0。",
            ZERO_MEAN,
        ),
        row(
            "StableLadderPivotFiberCharacterToResidueDeviationClosed",
            True,
            True,
            "非平凡角色满足 sum_r chi_j(r)=0，因此 A_h=sum_r D_r chi_j(r)。",
            CHAR_INVERSION,
        ),
        row(
            "StableLadderPivotFiberResidueImbalanceLocalizationClosed",
            True,
            True,
            "由 |A_h|<=sum_r |D_r|<=q_j max_r |D_r|，角色异常强制某个余数类计数偏差异常。",
            RESIDUE_LOCALIZATION,
        ),
        row(
            "StableLadderPivotFiberResidueImbalanceThresholdClosed",
            True,
            True,
            "若 |A_h|>=q_j*E/(N-1)，则存在 r 使 |M_r-L/q_j|>=E/(N-1)。",
            THRESHOLD,
        ),
        row(
            "NoAnonymousPrimitiveFiberCharacterPDECExit",
            True,
            True,
            "primitive fiber 角色相关出口被改写成固定余数类的计数偏差出口。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterResidueCount",
            True,
            False,
            "非持久实际 ladder 事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "StableActualLadderResidueCountPDECCapStillOpen",
            False,
            False,
            "仍未证明所有固定纤维余数类计数偏差都低于阈值，也未证明 sparse scale-ladder SAE 全局可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需给出 residue-count PDEC cap，或证明 sparse scale-ladder SAE 全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 stable ladder residue-count PDEC 证书。"""
    previous = load_json(PREVIOUS_CERT)
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "primitive pivot-fiber PDEC 可由有限 Fourier 反演写成余数类计数偏差。"
        "在固定补坐标纤维 S_h 中令 M_r 统计 n mod q_j=r 的点数，D_r=M_r-|S_h|/q_j。"
        "非平凡角色和 A_h=sum_r M_r chi_j(r)=sum_r D_r chi_j(r)。"
        "若 |A_h|>=q_j*E/(N-1)，则必存在余数 r 使 |M_r-|S_h|/q_j|>=E/(N-1)。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_stable_ladder_residue_count_pdec_router",
        "status": "primitive_fiber_pdec_reduced_to_residue_count_imbalance_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "primitive_fiber_pdec_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "residue_count_vector_closed": True,
        "zero_mean_deviation_closed": True,
        "character_to_residue_deviation_closed": True,
        "residue_imbalance_localization_closed": True,
        "residue_imbalance_threshold_closed": True,
        "anonymous_primitive_character_exit_removed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "residue_count_pdec_cap_proved": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "residue_count_formulas": {
            "fiber_size": "L=|S_h|",
            "counts": "M_r=#{n in S_h: n mod q_j=r}",
            "deviation": "D_r=M_r-L/q_j, sum_r D_r=0",
            "character_sum": "A_h=sum_r M_r chi_j(r)=sum_r D_r chi_j(r)",
            "localization": "|A_h|<=sum_r |D_r|<=q_j max_r |D_r|",
            "threshold": "|A_h|>=q_j*E/(N-1) => exists r with |M_r-L/q_j|>=E/(N-1)",
            "new_failure": "residue-count PDEC cap or sparse scale-ladder SAE summability",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix stable-ladder residue-count PDEC 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"primitive_fiber_pdec_imported={fmt_bool(cert['primitive_fiber_pdec_imported'])}",
        f"residue_count_vector_closed={fmt_bool(cert['residue_count_vector_closed'])}",
        f"zero_mean_deviation_closed={fmt_bool(cert['zero_mean_deviation_closed'])}",
        f"character_to_residue_deviation_closed={fmt_bool(cert['character_to_residue_deviation_closed'])}",
        f"residue_imbalance_localization_closed={fmt_bool(cert['residue_imbalance_localization_closed'])}",
        f"residue_imbalance_threshold_closed={fmt_bool(cert['residue_imbalance_threshold_closed'])}",
        f"anonymous_primitive_character_exit_removed={fmt_bool(cert['anonymous_primitive_character_exit_removed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"residue_count_pdec_cap_proved={fmt_bool(cert['residue_count_pdec_cap_proved'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定纤维内的余数计数",
        "",
        "沿用上一层的 pivot 坐标 `j` 与补坐标纤维 `S_h`。令：",
        "",
        "```text",
        "L=|S_h|,",
        "M_r=#{n in S_h: n mod q_j=r},  r in Z/q_jZ.",
        "```",
        "",
        "定义均值扣除后的偏差向量：",
        "",
        "```text",
        "D_r=M_r-L/q_j.",
        "```",
        "",
        "于是：",
        "",
        "```text",
        "sum_r D_r=0.",
        "```",
        "",
        "## 2. 角色和反演为计数偏差",
        "",
        "上一层的 primitive fiber 角色和为：",
        "",
        "```text",
        "A_h=sum_{n in S_h} chi_j(n mod q_j)=sum_r M_r chi_j(r).",
        "```",
        "",
        "由于 `chi_j` 非平凡，`sum_r chi_j(r)=0`，因此：",
        "",
        "```text",
        "A_h=sum_r D_r chi_j(r).",
        "```",
        "",
        "## 3. 原子余数类偏差",
        "",
        "由三角不等式：",
        "",
        "```text",
        "|A_h|<=sum_r |D_r|<=q_j max_r |D_r|.",
        "```",
        "",
        "上一层给出阈值：",
        "",
        "```text",
        "|A_h|>=q_j*E_a(S)/(N-1).",
        "```",
        "",
        "故存在某个余数 `r` 使：",
        "",
        "```text",
        "|M_r-L/q_j|>=E_a(S)/(N-1).",
        "```",
        "",
        "这把 primitive fiber PDEC cap 改写为固定补坐标纤维中的单余数类计数偏差 cap。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        cert["hardpoint_before_router"],
        "  -> " + cert["hardpoint_after_router"].replace(" AND ", "\n  AND "),
        "```",
        "",
        "剩余从 primitive fiber 角色相关变成 residue-count PDEC cap，或 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
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
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有证明 residue-count PDEC cap。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只把 primitive fiber 角色相关局部化为单余数类计数偏差输入。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
    """生成 JSON、ledger 与 Markdown 归档。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    payload = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    write_md(cert)
    print(json.dumps({
        "status": cert["status"],
        "next_direct_attack_target": cert["next_direct_attack_target"],
        "row_column_unconditional_closed": cert["row_column_unconditional_closed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
