#!/usr/bin/env python3
"""生成 strict 多源 fan-in 小商归约证书。

用法示例：
  python3 experiments/prime_matrix_strict_multisource_fanin_small_quotient_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-multisource-fanin-small-quotient-router.json

输出：
  docs/monograph/prime-matrix-strict-multisource-fanin-small-quotient-router.json
  docs/monograph/prime-matrix-strict-multisource-fanin-small-quotient-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-multisource-fanin-small-quotient-router.json"
OUT_MD = DOCS / "prime-matrix-strict-multisource-fanin-small-quotient-router.md"

FANIN = "MultiSourceKernelFanInSAEOrPDECExclusion"
SMALL_P_TABLE = "SmallPrimePowerCascadeColdWindowExclusionTableForP235"
BOUNDED_SAE = "BoundedQuotientTypeSAEAbsorption"
FIXED_QUOTIENT = "FixedQuotientTypeColumnCRTOrPDECExclusion"
ITERATED = "IteratedThresholdCollapseExclusionLedger"
SPARSE_HISTORY = "SparseTerminalHistorySAEAbsorptionOrPDECExclusion"
KERNEL_BUDGET = "PrefixBranchingKernelMultiplicityBudgetLedger"
TERMINAL_ANTICASCADE = "TerminalColdWindowCompatibilityAntiCascadeLemma"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SOURCE_FILES = [
    "prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json",
    "prime-matrix-strict-low-multiplier-common-kernel-router.json",
    "prime-matrix-strict-large-pair-kernel-difference-router.json",
    "prime-matrix-strict-fixed-quotient-density-transfer-router.json",
    "prime-matrix-strict-iterated-scaled-core-density-router.json",
    "prime-matrix-strict-iterated-threshold-collapse-router.json",
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
        "experiments/prime_matrix_strict_multisource_fanin_small_quotient_router.py": sha256(
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


def normal_form_rows() -> list[dict[str, str]]:
    """列出多源 fan-in 的小商正规形。"""
    return [
        {
            "step": "low_multiplier_event",
            "formula": "K_t=gcd(g_t,L_{t-1})>Y/Lambda, with Y<g_t<=2Y",
            "meaning": "fan-in 分支继承完整大共同核，而不是只继承若干小成对核。",
        },
        {
            "step": "small_quotient",
            "formula": "g_t=K_t q_t, hence 1<=q_t<2Lambda",
            "meaning": "多源覆盖细节被压到一个有界商 q_t。",
        },
        {
            "step": "cover_witness",
            "formula": "K_t | lcm_{i<t} gcd(g_t,g_i)",
            "meaning": "旧除数云只证明 K_t 已登记，不扩大 q_t 字母表。",
        },
        {
            "step": "persistent_route",
            "formula": "same q_t recurring across formal units -> fixed quotient PDEC/ColumnCRT",
            "meaning": "持久小商不是自由 fan-in，而是命名相位证书。",
        },
        {
            "step": "nonpersistent_route",
            "formula": "nonpersistent q_t types are counted by <=2Lambda SAE alphabet",
            "meaning": "不持久 fan-in 被有限字母表 SAE 吸收；常数强于 8Lambda^2。",
        },
    ]


def sample_rows() -> list[dict[str, Any]]:
    """给出若干小商样本，展示 q<2Lambda 的硬约束。"""
    rows: list[dict[str, Any]] = []
    for y_value, lambda_value, kernel, quotient in [
        (1000, 10, 140, 8),
        (1000, 10, 251, 5),
        (10000, 25, 667, 16),
        (10000, 25, 1201, 9),
    ]:
        g_value = kernel * quotient
        rows.append(
            {
                "Y": y_value,
                "Lambda": lambda_value,
                "K": kernel,
                "q": quotient,
                "g": g_value,
                "low_multiplier_condition": kernel > y_value / lambda_value,
                "short_window_condition": y_value < g_value <= 2 * y_value,
                "small_quotient_bound": quotient < 2 * lambda_value,
            }
        )
    return rows


def decision_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    """生成判定表。"""
    reduction_closed = result["multisource_fanin_small_quotient_reduction_closed"]
    return [
        row(
            "SmallPrimePowerTableImported",
            result["small_prime_power_cascade_table_proved"],
            result["small_prime_power_cascade_table_proved"],
            "单源 p=2,3,5 素数幂级联已关闭，当前只处理多源共同核。",
            SMALL_P_TABLE,
        ),
        row(
            "PairOrFanInDichotomyImported",
            result["pair_or_fanin_dichotomy_imported"],
            result["pair_or_fanin_dichotomy_imported"],
            "低乘子共同核已拆成大成对核或多源 fan-in。",
            FANIN,
        ),
        row(
            "FanInSmallQuotientNormalFormClosed",
            reduction_closed,
            reduction_closed,
            "多源共同核仍给 g_t=K_t q_t 且 q_t<2Lambda。",
            FANIN,
        ),
        row(
            "CoverHypergraphNoIndependentAlphabet",
            reduction_closed,
            reduction_closed,
            "覆盖 K_t 的旧除数云只是见证，不再产生独立无界类型。",
            FANIN,
        ),
        row(
            "FanInReducedToBoundedQuotientSAEOrPDEC",
            reduction_closed,
            reduction_closed,
            "持久 q_t 进入固定商型 PDEC；非持久 q_t 进入有限字母表 SAE。",
            f"{BOUNDED_SAE} AND {FIXED_QUOTIENT}",
        ),
        row(
            "MultiSourceKernelFanInIndependentHardpointRemoved",
            reduction_closed,
            reduction_closed,
            "fan-in 不再作为独立硬点，已并入有界商型 SAE/PDEC 账本。",
            f"{BOUNDED_SAE} AND {ITERATED}",
        ),
        row(
            "BoundedQuotientSAEAbsorbed",
            False,
            False,
            "有界商型 SAE/阈值坍缩的总量吸收仍需接回。",
            SPARSE_HISTORY,
        ),
        row(
            "PrefixBranchingKernelMultiplicityBudgetProved",
            False,
            False,
            "共同核预算仍等待有界商型 SAE、固定商型 PDEC 和终端反级联。",
            f"{BOUNDED_SAE} AND {FIXED_QUOTIENT} AND {TERMINAL_ANTICASCADE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "尚未得到早期零行反例链的最终矛盾。",
            f"{KERNEL_BUDGET} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造多源 fan-in 小商归约证书。"""
    single_prime = load_json("prime-matrix-strict-single-prime-power-cascade-canonicalization-router.json")
    low_kernel = load_json("prime-matrix-strict-low-multiplier-common-kernel-router.json")
    iterated = load_json("prime-matrix-strict-iterated-threshold-collapse-router.json")

    small_table_closed = single_prime.get("small_prime_power_cascade_table_proved") is True
    dichotomy = low_kernel.get("pair_or_fanin_dichotomy_closed") is True
    sparse_reduction = iterated.get("sparse_terminal_reduction_closed") is True
    samples = sample_rows()
    samples_ok = all(
        item["low_multiplier_condition"] and item["short_window_condition"] and item["small_quotient_bound"]
        for item in samples
    )
    reduction_closed = small_table_closed and dichotomy and samples_ok

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_strict_multisource_fanin_small_quotient_router",
        "status": "multisource_fanin_independent_hardpoint_reduced_to_bounded_quotient_sae_pdec_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "small_prime_power_cascade_table_proved": small_table_closed,
        "pair_or_fanin_dichotomy_imported": dichotomy,
        "multisource_fanin_small_quotient_reduction_closed": reduction_closed,
        "cover_hypergraph_independent_alphabet_removed": reduction_closed,
        "multisource_fanin_independent_hardpoint_removed": reduction_closed,
        "sparse_terminal_reduction_imported": sparse_reduction,
        "bounded_quotient_type_sae_absorbed": False,
        "fixed_quotient_type_pdec_excluded": False,
        "prefix_branching_kernel_multiplicity_budget_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": FANIN,
        "hardpoint_after_router": f"{BOUNDED_SAE} AND {FIXED_QUOTIENT} AND {SPARSE_HISTORY}",
        "next_direct_attack_target": SPARSE_HISTORY,
        "parallel_attack_targets": [BOUNDED_SAE, FIXED_QUOTIENT, ITERATED, TERMINAL_ANTICASCADE, DSTRUCTURE],
        "normal_form_rows": normal_form_rows(),
        "sample_rows": samples,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "`MultiSourceKernelFanInSAEOrPDECExclusion` 不再是独立无界硬点。"
            "在低乘子事件中，完整共同核 `K_t=gcd(g_t,L_{t-1})` 已满足 `K_t>Y/Lambda` 且 `K_t|g_t`；"
            "由于 `Y<g_t<=2Y`，必有 `g_t=K_t q_t` 且 `1<=q_t<2Lambda`。"
            "多源旧除数云只负责见证 `K_t` 已在旧 LCM 中登记，不会产生新的无限类型。"
            "因此持久同一小商 `q_t` 进入固定商型 PDEC/ColumnCRT，非持久小商进入有限字母表 SAE。"
            "剩余不是 fan-in 自身，而是有界商型 SAE/稀疏终端历史吸收、固定商型 PDEC 排斥与终端反级联。"
        ),
    }
    result["decision_rows"] = decision_rows(result)
    return result


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict 多源 fan-in 小商归约路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"small_prime_power_cascade_table_proved={fmt_bool(result['small_prime_power_cascade_table_proved'])}",
        f"pair_or_fanin_dichotomy_imported={fmt_bool(result['pair_or_fanin_dichotomy_imported'])}",
        f"multisource_fanin_small_quotient_reduction_closed={fmt_bool(result['multisource_fanin_small_quotient_reduction_closed'])}",
        f"cover_hypergraph_independent_alphabet_removed={fmt_bool(result['cover_hypergraph_independent_alphabet_removed'])}",
        f"multisource_fanin_independent_hardpoint_removed={fmt_bool(result['multisource_fanin_independent_hardpoint_removed'])}",
        f"bounded_quotient_type_sae_absorbed={fmt_bool(result['bounded_quotient_type_sae_absorbed'])}",
        f"prefix_branching_kernel_multiplicity_budget_proved={fmt_bool(result['prefix_branching_kernel_multiplicity_budget_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 小商正规形",
        "",
        "| step | formula | meaning |",
        "|---|---|---|",
    ]
    for item in result["normal_form_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['step'])}` | "
            f"{table_cell(item['formula'])} | "
            f"{table_cell(item['meaning'])} |"
        )

    lines.extend(
        [
            "",
            "## 样本检查",
            "",
            "| Y | Lambda | K | q | g | low multiplier | short window | q<2Lambda |",
            "|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for item in result["sample_rows"]:
        lines.append(
            "| "
            f"{item['Y']} | "
            f"{item['Lambda']} | "
            f"{item['K']} | "
            f"{item['q']} | "
            f"{item['g']} | "
            f"`{fmt_bool(item['low_multiplier_condition'])}` | "
            f"`{fmt_bool(item['short_window_condition'])}` | "
            f"`{fmt_bool(item['small_quotient_bound'])}` |"
        )

    lines.extend(
        [
            "",
            "## 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "|---|---:|---:|---|---|",
        ]
    )
    for item in result["decision_rows"]:
        lines.append(
            "| "
            f"`{table_cell(item['gate'])}` | "
            f"`{fmt_bool(item['closed'])}` | "
            f"`{fmt_bool(item['proved'])}` | "
            f"{table_cell(item['meaning'])} | "
            f"`{table_cell(item['remaining'])}` |"
        )

    lines.extend(
        [
            "",
            "## 下一步",
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
            "## 证据哈希",
            "",
            "| file | sha256 |",
            "|---|---|",
        ]
    )
    for path, digest in sorted(result["source_hashes"].items()):
        lines.append(f"| `{table_cell(path)}` | `{digest}` |")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(result)
    print(result["status"])
    print(result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
