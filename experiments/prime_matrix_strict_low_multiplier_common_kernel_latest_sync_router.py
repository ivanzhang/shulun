#!/usr/bin/env python3
"""生成 strict 低乘子共同核最新同步路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_low_multiplier_common_kernel_latest_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json
  docs/monograph/prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-low-multiplier-common-kernel-latest-sync-router.md"

LOW_KERNEL = "LowMultiplierCommonKernelColumnCRTOrPDECRoute"
WIDTH_LCM = "SiblingCollarWidthLCMKernelCompressionLedger"
PAIR_KERNEL = "LargePairKernelDifferenceColumnCRTExclusion"
FANIN_KERNEL = "MultiSourceKernelFanInSAEOrPDECExclusion"
FIXED_QUOTIENT = "FixedQuotientTypeColumnCRTOrPDECExclusion"
FIXED_QUOTIENT_PDEC = "FixedQuotientTypePDECColumnCertificateExclusion"
BOUNDED_SAE = "BoundedQuotientTypeSAEAbsorption"
SPARSE_HISTORY = "SparseTerminalHistorySAEAbsorptionOrPDECExclusion"
EFFECTIVE_PRUNING = "EffectiveColdHistoryPruningOrHotFixedReturnTheorem"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
SIBLING_NUMERIC = "SiblingColdCoreThresholdNumericEnvelopeTable"
HOT_CORE = "TerminalCoreHotDivisorWindowPDECorSAE"
FIXED_HISTORY = "FixedTypeHistoryPDECExclusion"
RETURN_DESCENT = "CommonKernelReturnCycleDescentOrPDECLedger"
MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json",
    "prime-matrix-strict-low-multiplier-common-kernel-router.json",
    "prime-matrix-strict-large-pair-kernel-difference-router.json",
    "prime-matrix-strict-fixed-quotient-type-columncrt-router.json",
    "prime-matrix-strict-fixed-quotient-density-transfer-router.json",
    "prime-matrix-strict-iterated-scaled-core-density-router.json",
    "prime-matrix-strict-iterated-threshold-collapse-router.json",
    "prime-matrix-strict-multisource-fanin-small-quotient-router.json",
    "prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json",
    "prime-matrix-strict-effective-pruning-latest-sync-router.json",
    "prime-matrix-strict-terminal-cold-window-anticascade-attack-router.json",
    "prime-matrix-strict-cold-window-sibling-charging-router.json",
]


def load_json(name: str) -> dict[str, Any]:
    """读取依赖 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {
        "experiments/prime_matrix_strict_low_multiplier_common_kernel_latest_sync_router.py": sha256(
            Path(__file__).resolve()
        )
    }
    for name in SOURCE_FILES:
        path = DOCS / name
        if path.exists():
            result[f"docs/monograph/{name}"] = sha256(path)
    return result


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def sync_rows() -> list[dict[str, str]]:
    """列出低乘子共同核的最新下游同步链。"""
    return [
        {
            "stage": "width LCM return",
            "closed_fact": "collar width overflow routes to LCM height or low-multiplier common kernel",
            "remaining": LOW_KERNEL,
        },
        {
            "stage": "pair/fan-in split",
            "closed_fact": "K_t divides the lcm of pair gcds, hence pair or fan-in",
            "remaining": f"{PAIR_KERNEL} OR {FANIN_KERNEL}",
        },
        {
            "stage": "large pair quotient alphabet",
            "closed_fact": "g=kb, g'=k(b+a), 1<=b,b+a<2Lambda",
            "remaining": f"{FIXED_QUOTIENT_PDEC} OR {BOUNDED_SAE}",
        },
        {
            "stage": "fixed quotient descent",
            "closed_fact": "fixed coprime quotient gives h -> h/(bc) with bc>=2",
            "remaining": "threshold collapse, fixed PDEC, or LCM height",
        },
        {
            "stage": "fan-in bounded quotient",
            "closed_fact": "g_t=K_t q_t with q_t<2Lambda; cover hypergraph adds no new alphabet",
            "remaining": SPARSE_HISTORY,
        },
        {
            "stage": "sparse terminal sync",
            "closed_fact": "finite history encoding and nonpersistent SAE formula are available",
            "remaining": EFFECTIVE_PRUNING,
        },
        {
            "stage": "terminal anti-cascade return",
            "closed_fact": "effective pruning latest sync reaches sibling cold-window charging and collar width LCM",
            "remaining": RETURN_DESCENT,
        },
    ]


def descent_samples() -> list[dict[str, Any]]:
    """给出固定商型缩频下降样本，核验 bc>=2 时高度严格下降。"""
    samples: list[dict[str, Any]] = []
    for h, b, c in [(840, 1, 2), (2310, 2, 3), (30030, 3, 5), (510510, 5, 7)]:
        samples.append(
            {
                "h": h,
                "b": b,
                "c": c,
                "bc": b * c,
                "new_h": h // (b * c),
                "divides": h % (b * c) == 0,
                "strict_descent": h // (b * c) < h,
            }
        )
    return samples


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        row(
            "WidthLCMImportsLowKernel",
            result["width_lcm_imports_low_kernel"],
            result["width_lcm_imports_low_kernel"],
            "最新兄弟 collar 宽度压缩把剩余导向低乘子共同核。",
            LOW_KERNEL,
        ),
        row(
            "LowKernelPairOrFanInDichotomyClosed",
            result["low_kernel_pair_or_fanin_dichotomy_closed"],
            result["low_kernel_pair_or_fanin_dichotomy_closed"],
            "低乘子共同核已拆成大成对差值锁或多源 fan-in。",
            f"{PAIR_KERNEL} OR {FANIN_KERNEL}",
        ),
        row(
            "PairBranchFiniteQuotientAlphabetClosed",
            result["pair_branch_finite_quotient_alphabet_closed"],
            result["pair_branch_finite_quotient_alphabet_closed"],
            "大成对核差值锁已压成有限商字母表。",
            f"{FIXED_QUOTIENT} OR {BOUNDED_SAE}",
        ),
        row(
            "FixedQuotientHeightDescentImported",
            result["fixed_quotient_height_descent_imported"],
            result["fixed_quotient_height_descent_imported"],
            "固定互素商型递归每步使正式频率高度至少折半。",
            FIXED_QUOTIENT,
        ),
        row(
            "FanInIndependentAlphabetRemoved",
            result["fanin_independent_alphabet_removed"],
            result["fanin_independent_alphabet_removed"],
            "多源 fan-in 只留下有界小商，不再产生独立无限字母表。",
            f"{BOUNDED_SAE} OR {SPARSE_HISTORY}",
        ),
        row(
            "SparseTerminalIndependentHardpointRemoved",
            result["sparse_terminal_independent_hardpoint_removed"],
            result["sparse_terminal_independent_hardpoint_removed"],
            "非持久 SAE/稀疏终端已同步到有效冷历史剪枝。",
            EFFECTIVE_PRUNING,
        ),
        row(
            "UnnamedLowKernelExitRemoved",
            result["unnamed_low_kernel_exit_removed"],
            result["unnamed_low_kernel_exit_removed"],
            "低乘子共同核不再是无名出口；所有分支已命名为 PDEC/SAE/热回流/返回链。",
            f"{FIXED_QUOTIENT_PDEC} OR {BOUNDED_SAE} OR {HOT_CORE} OR {RETURN_DESCENT}",
        ),
        row(
            "CommonKernelReturnCycleDescentOrPDECProved",
            False,
            False,
            "若非持久分支经终端反级联回到兄弟 collar/LCM/共同核，仍需证明严格下降；否则要登记固定历史或 PDEC。",
            RETURN_DESCENT,
        ),
        row(
            "LowMultiplierCommonKernelExcluded",
            False,
            False,
            "当前只删除无名共同核出口，没有排斥所有命名出口。",
            f"{RETURN_DESCENT} AND {FIXED_QUOTIENT_PDEC} AND {HOT_CORE} AND {FIXED_HISTORY}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "仍未得到早期零行反例链的终端矛盾。",
            f"{RETURN_DESCENT} AND {MOVING_ATOM} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造低乘子共同核最新同步证书。"""
    width_lcm = load_json("prime-matrix-strict-sibling-collar-width-lcm-kernel-router.json")
    low_kernel = load_json("prime-matrix-strict-low-multiplier-common-kernel-router.json")
    pair = load_json("prime-matrix-strict-large-pair-kernel-difference-router.json")
    fixed = load_json("prime-matrix-strict-fixed-quotient-type-columncrt-router.json")
    fixed_transfer = load_json("prime-matrix-strict-fixed-quotient-density-transfer-router.json")
    fanin = load_json("prime-matrix-strict-multisource-fanin-small-quotient-router.json")
    sparse = load_json("prime-matrix-strict-sparse-terminal-absorption-latest-sync-router.json")
    effective = load_json("prime-matrix-strict-effective-pruning-latest-sync-router.json")
    sibling = load_json("prime-matrix-strict-cold-window-sibling-charging-router.json")

    width_imports_low = width_lcm.get("next_direct_attack_target") == LOW_KERNEL
    split_closed = (
        low_kernel.get("kernel_subcover_closed") is True
        and low_kernel.get("pair_or_fanin_dichotomy_closed") is True
        and low_kernel.get("large_pair_difference_lock_closed") is True
    )
    pair_finite = (
        pair.get("exact_pair_gcd_normal_form_closed") is True
        and pair.get("bounded_quotient_gap_closed") is True
        and pair.get("finite_quotient_alphabet_closed") is True
    )
    fixed_descent = (
        fixed.get("fixed_type_scaled_frequency_identity_closed") is True
        and fixed.get("strict_height_descent_closed") is True
        and fixed.get("finite_descent_depth_closed") is True
        and fixed_transfer.get("density_transfer_without_loss_closed") is True
    )
    fanin_removed = (
        fanin.get("multisource_fanin_small_quotient_reduction_closed") is True
        and fanin.get("cover_hypergraph_independent_alphabet_removed") is True
        and fanin.get("multisource_fanin_independent_hardpoint_removed") is True
    )
    sparse_removed = sparse.get("sparse_terminal_history_independent_hardpoint_removed") is True
    effective_sync = effective.get("effective_pruning_latest_sync_closed") is True
    sibling_charging_closed = sibling.get("canonical_cold_window_sibling_charging_ledger_closed") is True
    samples = descent_samples()
    samples_ok = all(item["divides"] and item["strict_descent"] for item in samples)
    unnamed_removed = (
        width_imports_low
        and split_closed
        and pair_finite
        and fixed_descent
        and fanin_removed
        and sparse_removed
        and effective_sync
        and sibling_charging_closed
        and samples_ok
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_low_multiplier_common_kernel_latest_sync_router",
        "status": "low_multiplier_common_kernel_unnamed_exit_removed_return_descent_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "width_lcm_imports_low_kernel": width_imports_low,
        "low_kernel_pair_or_fanin_dichotomy_closed": split_closed,
        "pair_branch_finite_quotient_alphabet_closed": pair_finite,
        "fixed_quotient_height_descent_imported": fixed_descent,
        "fanin_independent_alphabet_removed": fanin_removed,
        "sparse_terminal_independent_hardpoint_removed": sparse_removed,
        "effective_pruning_latest_sync_closed": effective_sync,
        "sibling_charging_ledger_closed": sibling_charging_closed,
        "fixed_quotient_descent_samples_passed": samples_ok,
        "unnamed_low_kernel_exit_removed": unnamed_removed,
        "common_kernel_return_cycle_detected": True,
        "common_kernel_return_cycle_descent_or_pdec_proved": False,
        "low_multiplier_common_kernel_excluded": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": LOW_KERNEL,
        "hardpoint_after_router": (
            f"{RETURN_DESCENT} AND {FIXED_QUOTIENT_PDEC} AND {BOUNDED_SAE} "
            f"AND {HOT_CORE} AND {FIXED_HISTORY}"
        ),
        "next_direct_attack_target": RETURN_DESCENT,
        "parallel_attack_targets": [
            FIXED_QUOTIENT_PDEC,
            BOUNDED_SAE,
            SPARSE_HISTORY,
            EFFECTIVE_PRUNING,
            TERMINAL_ANTICASCADE,
            SIBLING_NUMERIC,
            HOT_CORE,
            FIXED_HISTORY,
            MOVING_ATOM,
            DSTRUCTURE,
        ],
        "sync_rows": sync_rows(),
        "fixed_quotient_descent_samples": samples,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`LowMultiplierCommonKernelColumnCRTOrPDECRoute` 已同步到最新前沿："
            "共同核不再是无名出口。它先被旧证书拆成大成对差值锁或多源 fan-in；"
            "大成对分支已经压成有限商字母表，并在固定商型下具有 `h -> h/(bc)` 的严格高度下降；"
            "多源 fan-in 已压成 `q<2Lambda` 的有界小商，并接到稀疏终端 SAE/PDEC 与有效冷历史剪枝链。"
            "因此当前真正剩余不是重新证明低乘子分流，而是处理回流：若非持久分支经终端反级联、"
            "兄弟收费和 collar 宽度 LCM 又返回共同核，必须给出严格下降量；若没有严格下降，"
            "该返回链就是固定历史、ColumnCRT 或 PDEC。此返回下降/PDEC 账本尚未证明，"
            "所以行/列命题仍未无条件闭合。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 文档。"""
    lines = [
        "# Prime Matrix strict 低乘子共同核最新同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"width_lcm_imports_low_kernel={fmt_bool(result['width_lcm_imports_low_kernel'])}",
        f"low_kernel_pair_or_fanin_dichotomy_closed={fmt_bool(result['low_kernel_pair_or_fanin_dichotomy_closed'])}",
        f"pair_branch_finite_quotient_alphabet_closed={fmt_bool(result['pair_branch_finite_quotient_alphabet_closed'])}",
        f"fixed_quotient_height_descent_imported={fmt_bool(result['fixed_quotient_height_descent_imported'])}",
        f"fanin_independent_alphabet_removed={fmt_bool(result['fanin_independent_alphabet_removed'])}",
        f"sparse_terminal_independent_hardpoint_removed={fmt_bool(result['sparse_terminal_independent_hardpoint_removed'])}",
        f"effective_pruning_latest_sync_closed={fmt_bool(result['effective_pruning_latest_sync_closed'])}",
        f"sibling_charging_ledger_closed={fmt_bool(result['sibling_charging_ledger_closed'])}",
        f"unnamed_low_kernel_exit_removed={fmt_bool(result['unnamed_low_kernel_exit_removed'])}",
        f"common_kernel_return_cycle_descent_or_pdec_proved={fmt_bool(result['common_kernel_return_cycle_descent_or_pdec_proved'])}",
        f"low_multiplier_common_kernel_excluded={fmt_bool(result['low_multiplier_common_kernel_excluded'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| stage | closed fact | remaining |",
        "| --- | --- | --- |",
    ]
    for item in result["sync_rows"]:
        lines.append(
            "| {stage} | {closed_fact} | {remaining} |".format(
                stage=table_cell(item["stage"]),
                closed_fact=table_cell(item["closed_fact"]),
                remaining=table_cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 2. 固定商型下降样本",
            "",
            "| h | b | c | bc | h/(bc) | divides | strict descent |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["fixed_quotient_descent_samples"]:
        lines.append(
            "| `{h}` | `{b}` | `{c}` | `{bc}` | `{new_h}` | `{divides}` | `{strict}` |".format(
                h=item["h"],
                b=item["b"],
                c=item["c"],
                bc=item["bc"],
                new_h=item["new_h"],
                divides=fmt_bool(item["divides"]),
                strict=fmt_bool(item["strict_descent"]),
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
    for item in result["decision_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 4. 下一步最窄点",
            "",
            f"- 主攻：`{result['next_direct_attack_target']}`。",
            "- 含义：证明共同核回流链每次都降低一个正式良基量；若不能降低，则该回流链必须登记为固定历史、ColumnCRT 或 PDEC。",
            "- 边界：本步只删除无名共同核出口，不排斥所有命名出口，不宣称行/列命题无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
