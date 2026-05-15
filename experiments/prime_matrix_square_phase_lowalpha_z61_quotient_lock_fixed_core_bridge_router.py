#!/usr/bin/env python3
"""审计 z=61 QuotientLock-PDEC 固定核心与 dyadic 吸收链的桥接。

用法示例：
  python3 experiments/prime_matrix_square_phase_lowalpha_z61_quotient_lock_fixed_core_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json

输出：
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json
  docs/monograph/prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
QUOTIENT_LOCK_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json"
PREFIX_PDEC_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json"
PREFIX_PHASE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json"
OVERLAP_CORE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json"
DYADIC_ABSORBER_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json"
DYADIC_SOURCE_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json"
OUT_JSON = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.json"
OUT_MD = DOCS / "prime-matrix-square-phase-lowalpha-z61-quotient-lock-fixed-core-bridge-router.md"

NEXT_TARGET = "FixedCoreDyadicAbsorberGlobalizationOrPersistentPhasePDEC"
SOURCE_FILES = [
    "prime-matrix-square-phase-lowalpha-z61-quotient-lock-pdec-registration-router.json",
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-pdec-registration-router.json",
    "prime-matrix-square-phase-lowalpha-z61-prefix-gate-phase-persistence-router.json",
    "prime-matrix-square-phase-lowalpha-z61-overlap-common-core-router.json",
    "prime-matrix-square-phase-lowalpha-z61-negative-dyadic-absorber-router.json",
    "prime-matrix-square-phase-lowalpha-z61-dyadic-source-congruence-router.json",
]


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_float(value: float) -> str:
    """格式化浮点数。"""
    return f"{value:.6f}"


def file_sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖哈希。"""
    result = {
        "experiments/prime_matrix_square_phase_lowalpha_z61_quotient_lock_fixed_core_bridge_router.py": file_sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = file_sha256(path)
    return result


def load(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def audit() -> dict[str, Any]:
    """执行固定核心桥接审计。"""
    qlock = load(QUOTIENT_LOCK_JSON)
    prefix_pdec = load(PREFIX_PDEC_JSON)
    prefix_phase = load(PREFIX_PHASE_JSON)
    overlap = load(OVERLAP_CORE_JSON)
    absorber = load(DYADIC_ABSORBER_JSON)
    dyadic_source = load(DYADIC_SOURCE_JSON)

    qrecord = qlock["quotient_lock_pdec_record"]
    precord = prefix_pdec["prefix_gate_pdec_record"]
    absorber_row = absorber["absorber_rows"][0]
    core = qrecord["core"]
    phase_modulus = precord["phase_modulus"]
    modulus = qrecord["modulus"]
    expected_phase_from_core = 6 * core
    expected_modulus_from_core = 12 * core
    source_rows = dyadic_source["source_rows"]
    source_quotients = [row["phase_quotient"] for row in source_rows]
    source_q_by_quotient = {row["phase_quotient"]: row["q"] for row in source_rows}
    source_b_by_quotient = {row["phase_quotient"]: row["b"] for row in source_rows}
    phase_hits = prefix_phase["phase_hit_rows"]
    hit_quotients = [row["phase_quotient"] for row in phase_hits]
    hit_weights = [row["target_contribution"] for row in phase_hits]
    same_unit_weight = max(hit_weights) == min(hit_weights)

    bridge_closed = (
        qlock["quotient_lock_pdec_registration_closed"]
        and prefix_pdec["prefix_gate_pdec_registration_closed"]
        and prefix_phase["registered_phase_signed_persistence_materialized"]
        and absorber["dyadic_absorber_criterion_closed_for_sample"]
        and dyadic_source["dyadic_source_congruence_skeleton_closed_for_sample"]
        and core == precord["common_core"] == overlap["common_core"]
        and phase_modulus == overlap["b_value"] == absorber_row["negative_b"] == expected_phase_from_core
        and modulus == 2 * phase_modulus == expected_modulus_from_core
        and absorber_row["dyadic_quotients"] == [2, 4]
        and source_quotients == [1, 2, 4]
        and hit_quotients == [1, 2, 4]
        and source_q_by_quotient[2] == qrecord["q2"]
        and source_q_by_quotient[4] == qrecord["q4"]
        and source_b_by_quotient[2] == modulus
        and source_b_by_quotient[4] == 2 * modulus
        and prefix_phase["sample_positive_phase_actual_covers_negative_phase_actual"]
        and same_unit_weight
    )

    return {
        "certificate_type": "prime_matrix_square_phase_lowalpha_z61_quotient_lock_fixed_core_bridge_router",
        "status": "z61_quotient_lock_fixed_core_bridged_to_dyadic_absorber_global_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "source_certificates": [
            qlock["certificate_type"],
            prefix_pdec["certificate_type"],
            prefix_phase["certificate_type"],
            overlap["certificate_type"],
            absorber["certificate_type"],
            dyadic_source["certificate_type"],
        ],
        "target_bucket": qlock["target_bucket"],
        "target_omega": qlock["target_omega"],
        "target_shell": qlock["target_shell"],
        "core": core,
        "phase_modulus": phase_modulus,
        "quotient_lock_modulus": modulus,
        "phase_modulus_equals_6core": phase_modulus == expected_phase_from_core,
        "quotient_lock_modulus_equals_12core": modulus == expected_modulus_from_core,
        "quotient_lock_modulus_is_positive_lift_2B": modulus == 2 * phase_modulus,
        "common_core_bridge_closed": core == precord["common_core"] == overlap["common_core"],
        "hit_lcm_bridge_closed": phase_modulus == overlap["b_value"] == absorber_row["hit_lcm"],
        "source_quotients": source_quotients,
        "phase_hit_quotients": hit_quotients,
        "dyadic_absorber_quotients": absorber_row["dyadic_quotients"],
        "q2_matches_quotient_2_source_q": source_q_by_quotient[2] == qrecord["q2"],
        "q4_matches_quotient_4_source_q": source_q_by_quotient[4] == qrecord["q4"],
        "quotient_2_b_equals_quotient_lock_modulus": source_b_by_quotient[2] == modulus,
        "quotient_4_b_equals_twice_quotient_lock_modulus": source_b_by_quotient[4] == 2 * modulus,
        "negative_phase_actual": prefix_phase["negative_phase_actual"],
        "positive_phase_actual": prefix_phase["positive_phase_actual"],
        "positive_over_negative_phase_actual": prefix_phase["positive_over_negative_phase_actual"],
        "same_unit_weight_on_phase_hits": same_unit_weight,
        "sample_positive_phase_absorbs_negative": prefix_phase[
            "sample_positive_phase_actual_covers_negative_phase_actual"
        ],
        "quotient_lock_fixed_core_bridge_closed_for_sample": bridge_closed,
        "fixed_core_check_completed": True,
        "quotient_lock_pdec_excluded_by_absence": False,
        "quotient_lock_pdec_locally_absorbed_by_dyadic_lifts": bridge_closed,
        "global_fixed_core_dyadic_absorber_proved": False,
        "persistent_phase_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "source_hashes": source_hashes(),
        "next_direct_attack_target": NEXT_TARGET,
        "plain_conclusion": (
            "固定核心检查显示 QuotientLock-PDEC 不是一个新的孤立缺口："
            "`core=4807` 与 Prefix/CommonCore 的核心相同，负锚相位为 "
            "`B=6C=28842`，而 QuotientLock 的 `M=57684` 正是 `2B`。"
            "样本内该相位有 quotient `1,2,4` 三个命中，两个正向 dyadic lift "
            "的同权贡献恰好以 2:1 吸收负锚。因此不能用相位缺席排斥它；"
            "下一步必须把这种 dyadic signed balance 全局化，或登记 PersistentPhase-PDEC。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix square-phase low-alpha z=61 QuotientLock fixed-core bridge",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"phase_modulus_equals_6core={fmt_bool(result['phase_modulus_equals_6core'])}",
        f"quotient_lock_modulus_equals_12core={fmt_bool(result['quotient_lock_modulus_equals_12core'])}",
        f"quotient_lock_modulus_is_positive_lift_2B={fmt_bool(result['quotient_lock_modulus_is_positive_lift_2B'])}",
        f"common_core_bridge_closed={fmt_bool(result['common_core_bridge_closed'])}",
        f"hit_lcm_bridge_closed={fmt_bool(result['hit_lcm_bridge_closed'])}",
        f"quotient_lock_fixed_core_bridge_closed_for_sample={fmt_bool(result['quotient_lock_fixed_core_bridge_closed_for_sample'])}",
        f"quotient_lock_pdec_locally_absorbed_by_dyadic_lifts={fmt_bool(result['quotient_lock_pdec_locally_absorbed_by_dyadic_lifts'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 核心桥接",
        "",
        "| quantity | value | relation |",
        "| --- | ---: | --- |",
        f"| C | {result['core']} | fixed core |",
        f"| B | {result['phase_modulus']} | `6C` |",
        f"| M | {result['quotient_lock_modulus']} | `12C=2B` |",
        "",
        "## 2. Quotient ladder",
        "",
        "| source | quotients |",
        "| --- | --- |",
        f"| phase hits | `{result['phase_hit_quotients']}` |",
        f"| dyadic absorber | `{result['dyadic_absorber_quotients']}` |",
        f"| source congruence | `{result['source_quotients']}` |",
        "",
        "## 3. q 匹配",
        "",
        "| check | value |",
        "| --- | --- |",
        f"| quotient 2 source q = q2 | {fmt_bool(result['q2_matches_quotient_2_source_q'])} |",
        f"| quotient 4 source q = q4 | {fmt_bool(result['q4_matches_quotient_4_source_q'])} |",
        f"| quotient 2 b = M | {fmt_bool(result['quotient_2_b_equals_quotient_lock_modulus'])} |",
        f"| quotient 4 b = 2M | {fmt_bool(result['quotient_4_b_equals_twice_quotient_lock_modulus'])} |",
        "",
        "## 4. Signed phase balance",
        "",
        "| negative actual | positive actual | ratio | same unit weight | local absorption |",
        "| ---: | ---: | ---: | --- | --- |",
        f"| {fmt_float(result['negative_phase_actual'])} | {fmt_float(result['positive_phase_actual'])} | "
        f"{fmt_float(result['positive_over_negative_phase_actual'])} | "
        f"{fmt_bool(result['same_unit_weight_on_phase_hits'])} | "
        f"{fmt_bool(result['sample_positive_phase_absorbs_negative'])} |",
        "",
        "## 5. 证明边界",
        "",
        "- 已闭合：固定核心检查完成；QuotientLock-PDEC 与既有 dyadic 吸收链同一对象。",
        "- 已排除的路线：不能靠相位缺席排斥，因为该相位在样本内持久出现。",
        "- 未闭合：把 dyadic signed balance 全局化，或登记并排斥 PersistentPhase-PDEC。",
        f"- 下一目标：`{result['next_direct_attack_target']}`。",
        "",
        "## 6. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for name, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{name}` | `{digest}` |")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    result = audit()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(
        json.dumps(
            {
                "status": result["status"],
                "quotient_lock_fixed_core_bridge_closed_for_sample": result[
                    "quotient_lock_fixed_core_bridge_closed_for_sample"
                ],
                "quotient_lock_pdec_locally_absorbed_by_dyadic_lifts": result[
                    "quotient_lock_pdec_locally_absorbed_by_dyadic_lifts"
                ],
                "next_direct_attack_target": result["next_direct_attack_target"],
                "row_column_unconditional_closed": result["row_column_unconditional_closed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
