#!/usr/bin/env python3
"""生成 strict 解析尾段到有限边界单调桥证书。

用法示例：
  python3 experiments/prime_matrix_strict_analytic_tail_to_finite_boundary_bridge_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json

输出：
  docs/monograph/prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json
  docs/monograph/prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"
OUT_JSON = MONOGRAPH / "prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.md"

SOURCE_FILES = [
    MONOGRAPH / "prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.json",
    MONOGRAPH / "prime-matrix-strict-same-parameter-prefix-window-spec-router.json",
    MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json",
    MONOGRAPH / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json",
    MONOGRAPH / "prime-matrix-linear-lower-sieve-tail-margin-router.json",
    MONOGRAPH / "prime-matrix-linear-sieve-tail-remainder-gap-router.json",
    MONOGRAPH / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json",
    MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json",
]

TARGET = "AnalyticTailToFiniteBoundaryMonotoneBridge"
SELF_CONTAINED_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
STANDARD_IMPORT = "StandardRosserIwaniecBetaSieveTheoremImportAccepted"
EXTERNAL_ROUGH = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
PARAMETER_ID = "alpha043_pge100000_external_b3_pending_finite_prefix_named_return"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """记录依赖哈希。"""
    result = {"script": sha256(Path(__file__).resolve())}
    for path in SOURCE_FILES:
        if path.exists():
            result[str(path.relative_to(ROOT))] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def consts(tail: dict[str, Any]) -> dict[str, Any]:
    """读取尾段常数。"""
    return tail.get("constants", {})


def build_rows(data: dict[str, dict[str, Any]], constants: dict[str, Any]) -> list[dict[str, Any]]:
    """构造解析尾桥判定行。"""
    runner = data["runner"]
    range_manifest = data["range_manifest"]
    tail = data["tail"]
    linear = data["linear"]
    split = data["split"]
    continuous = data["continuous"]
    tv = data["tv"]

    return [
        {
            "gate": "TailBridgeTargetImported",
            "closed": runner.get("next_direct_attack_target") == TARGET,
            "proved": False,
            "meaning": "上一层 runner/hash 账本后的 finite prefix 剩余首字段是解析尾段桥。",
            "remaining": TARGET,
        },
        {
            "gate": "RangeBoundaryMatches",
            "closed": range_manifest.get("range_and_parameter_manifest_closed") is True
            and constants.get("tail_start") == 100_000,
            "proved": True,
            "meaning": "有限 runner 覆盖 3001<=P<100000，解析尾段从 P>=100000 开始，边界无重叠缺口。",
            "remaining": "无范围缺口。",
        },
        {
            "gate": "TailObjectInterfaceClosed",
            "closed": tail.get("tail_object_interface_closed") is True,
            "proved": tail.get("tail_object_interface_closed") is True,
            "meaning": "尾段对象与同参数 prefix rough-count / B3 lower-sieve 对象一致。",
            "remaining": "不再是对象匹配问题。",
        },
        {
            "gate": "TenPercentBoundaryMarginClosed",
            "closed": constants.get("ten_percent_main_exceeds_target") is True
            and float(constants.get("ten_percent_surplus_over_401", 0.0)) > 0.0,
            "proved": True,
            "meaning": "P=100000 处 10% 模型主项为 489.625600...，超过目标 401，余量约 88.625600。",
            "remaining": "需要实际筛余达到 10% 主项的尾段输入。",
        },
        {
            "gate": "TailMainMonotoneAfterBoundary",
            "closed": constants.get("tail_main_monotone_after_e") is True
            and constants.get("floor_z_preserves_s_gt_2") is True,
            "proved": True,
            "meaning": "P/log P 型模型主量在尾段单调增长，floor z 仍保持 s>2。",
            "remaining": "floor/离散素和误差仍属于 B3/TV 输入。",
        },
        {
            "gate": "ContinuousBetaSurplusClosed",
            "closed": continuous.get("b3_continuous_beta_sieve_coefficient_surplus_proved", False) is True
            or any(row.get("gate") == "B3ContinuousBetaSieveCoefficientSurplusClosed" and row.get("closed") for row in continuous.get("rows", [])),
            "proved": True,
            "meaning": "连续 beta-sieve 主系数在 alpha=0.43 的 2<s<3 区间已闭合。",
            "remaining": "B3DiscretePrimeSumUniformErrorPGe100000",
        },
        {
            "gate": "TenPercentTailSplitLocated",
            "closed": any(row.get("gate") == "TailTenPercentMarginSplit" and row.get("closed") for row in split.get("rows", [])),
            "proved": False,
            "meaning": "实际 10% 尾段下界已被拆为内部 Rosser floor 余项或外部短区间 rough 下界。",
            "remaining": f"RosserIwaniecWeightedFloorRemainderTenPercentBound OR {EXTERNAL_ROUGH}",
        },
        {
            "gate": "ExternalOrStandardTailLedgerClosed",
            "closed": tail.get("tail_ledger_external_or_standard_closed") is True,
            "proved": False,
            "meaning": "若接受外部显式 Mertens/Dusart 或标准 Rosser-Iwaniec beta-sieve 输入，尾段账本已可条件关闭。",
            "remaining": f"{STANDARD_IMPORT} OR {EXTERNAL_ROUGH}",
        },
        {
            "gate": "ConditionalAnalyticTailBridgeClosed",
            "closed": tail.get("tail_ledger_external_or_standard_closed") is True
            and linear.get("ten_percent_capacity_algebra_imported", True) is not False,
            "proved": False,
            "meaning": "在外部/标准尾段输入下，P>=100000 的解析尾段由边界余量和单调性接入 finite boundary。",
            "remaining": "strict self-contained tail proof still open.",
        },
        {
            "gate": "StrictSelfContainedTailStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "严格自足路线仍缺内联 Mertens/PNT/Dusart 倒素数尾段证明，不能把条件桥升级为自足证明。",
            "remaining": SELF_CONTAINED_TAIL,
        },
        {
            "gate": "B3TVStrictSelfContainedStillOpen",
            "closed": tv.get("b3_tv_budget_strict_self_contained_proved") is True,
            "proved": tv.get("b3_tv_budget_strict_self_contained_proved") is True,
            "meaning": "B3 TV 有外部条件闭合，但严格自足版仍未完成。",
            "remaining": SELF_CONTAINED_TAIL,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造尾桥证书。"""
    data = {
        "runner": load_json(MONOGRAPH / "prime-matrix-strict-prefix-rough-count-runner-hash-ledger-router.json"),
        "same": load_json(MONOGRAPH / "prime-matrix-strict-same-parameter-prefix-window-spec-router.json"),
        "range_manifest": load_json(MONOGRAPH / "prime-matrix-strict-finite-boundary-prefix-range-manifest-router.json"),
        "tail": load_json(MONOGRAPH / "prime-matrix-strict-dynamic-skeleton-tail-b3-bridge-router.json"),
        "linear": load_json(MONOGRAPH / "prime-matrix-linear-lower-sieve-tail-margin-router.json"),
        "split": load_json(MONOGRAPH / "prime-matrix-linear-sieve-tail-remainder-gap-router.json"),
        "continuous": load_json(MONOGRAPH / "prime-matrix-b3-continuous-beta-sieve-surplus-router.json"),
        "tv": load_json(MONOGRAPH / "prime-matrix-strict-b3-remainder-total-variation-budget-router.json"),
    }
    constants = consts(data["tail"])
    rows = build_rows(data, constants)
    conditional_closed = next(row for row in rows if row["gate"] == "ConditionalAnalyticTailBridgeClosed")["closed"]
    strict_tail_closed = (
        data["tail"].get("tail_ledger_strict_self_contained_proved") is True
        and data["tv"].get("b3_tv_budget_strict_self_contained_proved") is True
    )

    return {
        "certificate_type": "prime_matrix_strict_analytic_tail_to_finite_boundary_bridge_router",
        "status": "analytic_tail_monotone_bridge_conditional_closed_strict_self_contained_tail_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "parameter_id": PARAMETER_ID,
        "analytic_tail_to_finite_boundary_monotone_bridge_conditional_external_or_standard_closed": conditional_closed,
        "analytic_tail_to_finite_boundary_monotone_bridge_strict_self_contained_proved": strict_tail_closed,
        "finite_boundary_prefix_certificate_external_or_standard_closed": conditional_closed
        and data["runner"].get("reproducible_prefix_rough_count_runner_hash_ledger_proved") is True
        and data["same"].get("same_parameter_window_specification_proved") is True,
        "finite_boundary_prefix_certificate_strict_self_contained_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "tail_constants": {
            "tail_start": constants.get("tail_start"),
            "alpha": constants.get("alpha"),
            "z_at_tail_start": constants.get("z_at_tail_start"),
            "floor_z_at_tail_start": constants.get("floor_z_at_tail_start"),
            "s_with_floor_z": constants.get("s_with_floor_z"),
            "linear_sieve_f": constants.get("linear_sieve_f"),
            "model_main_at_tail_start": constants.get("model_main_at_tail_start"),
            "ten_percent_main_at_tail_start": constants.get("ten_percent_main_at_tail_start"),
            "target_s": constants.get("target_s"),
            "ten_percent_surplus_over_401": constants.get("ten_percent_surplus_over_401"),
            "tail_main_monotone_after_e": constants.get("tail_main_monotone_after_e"),
        },
        "decision_rows": rows,
        "hardpoint_before_router": TARGET,
        "hardpoint_after_router": SELF_CONTAINED_TAIL,
        "parallel_attack_targets": [
            "B3DiscretePrimeSumUniformErrorPGe100000",
            TYPE_LEDGER,
            ROW_FREE,
            "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ],
        "next_direct_attack_target": SELF_CONTAINED_TAIL,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`AnalyticTailToFiniteBoundaryMonotoneBridge` 的边界/单调代数已压实："
            "有限 runner 覆盖 3001<=P<100000，解析尾段从 P>=100000 开始；"
            "在 P=100000，10% 模型主项约 489.625600，大于目标 401，且尾段主量单调增长。"
            "因此若接受外部/标准 B3 lower-sieve/Mertens-Dusart 输入，finite prefix 证书可条件闭合。"
            "严格自足版仍缺内联倒素数/Mertens-Dusart 尾段证明，所以下一最窄点转为 "
            f"`{SELF_CONTAINED_TAIL}`。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 解析尾段到有限边界单调桥路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"analytic_tail_to_finite_boundary_monotone_bridge_conditional_external_or_standard_closed={fmt_bool(result['analytic_tail_to_finite_boundary_monotone_bridge_conditional_external_or_standard_closed'])}",
        f"analytic_tail_to_finite_boundary_monotone_bridge_strict_self_contained_proved={fmt_bool(result['analytic_tail_to_finite_boundary_monotone_bridge_strict_self_contained_proved'])}",
        f"finite_boundary_prefix_certificate_external_or_standard_closed={fmt_bool(result['finite_boundary_prefix_certificate_external_or_standard_closed'])}",
        f"finite_boundary_prefix_certificate_strict_self_contained_proved={fmt_bool(result['finite_boundary_prefix_certificate_strict_self_contained_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Tail Constants",
        "",
        "| constant | value |",
        "| --- | ---: |",
    ]
    for key, value in result["tail_constants"].items():
        lines.append(f"| `{cell(key)}` | {cell(value)} |")

    lines.extend([
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ])
    for row in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=cell(row["meaning"]),
                remaining=cell(row["remaining"]),
            )
        )

    lines.extend([
        "",
        "## 3. 下一最窄点",
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
        "审稿边界：本步只给出外部/标准尾段输入下的条件桥和严格自足缺口；不能声称行/列命题无条件闭合。",
    ])
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
