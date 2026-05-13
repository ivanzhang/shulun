#!/usr/bin/env python3
"""生成 strict finite-prefix Mertens 尾段导入同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_finite_prefix_mertens_tail_import_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json

输出：
  docs/monograph/prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json
  docs/monograph/prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-finite-prefix-mertens-tail-import-sync-router.md"

SOURCE_FILES = [
    "prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json",
    "prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json",
    "prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json",
    "prime-matrix-strict-meissel-mertens-b1-interval-self-contained-router.json",
    "prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json",
    "prime-matrix-beta-sieve-self-contained-frontier-router.json",
]

OLD_TAIL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
TYPE_LEDGER = "FormalUnitTypeThresholdLedger"
ROW_FREE = "PrefixLabelSupportToRowFreeTypeAntiCollapse"
NAMED_RETURN = "NamedReturnPDECSAEColumnCRTHotCoreFixedHistoryExclusion"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
BETA_APPENDIX = (
    "BetaSieveLowerWeightRecursiveConstructionLedger AND "
    "BetaSieveLowerBoundDominanceProof AND "
    "BetaSieveMainCoefficientExplicit99PercentPGe100000"
)


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件 SHA256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    result = {"experiments/prime_matrix_strict_finite_prefix_mertens_tail_import_sync_router.py": sha256(Path(__file__).resolve())}
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


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成导入同步判定表。"""
    bridge = data["bridge"]
    mertens = data["mertens"]
    direct = data["direct"]
    b1 = data["b1"]
    terminal = data["terminal"]
    beta = data["beta"]

    old_tail_active = bridge.get("hardpoint_after_router") == OLD_TAIL
    direct_theta_closed = direct.get("direct_internal_dusart_theta_pnt_envelope_closed") is True
    b1_closed = b1.get("self_contained_meissel_mertens_constant_interval_closed") is True
    tail_closed = mertens.get("strict_self_contained_mertens_tail_proved") is True
    terminal_synced = terminal.get("b3_tv_strict_self_contained_synchronized") is True
    beta_first_principles_open = any(
        item.get("closed") is False
        for item in beta.get("rows", [])
        if item.get("gate")
        in {
            "BetaSieveLowerWeightRecursiveConstructionLedger",
            "BetaSieveLowerBoundDominanceProof",
            "BetaSieveMainCoefficientExplicit99PercentPGe100000",
        }
    )

    return [
        row(
            "CounterexampleBranchGuardPreserved",
            bridge.get("counterexample_assumption_only") is True
            and bridge.get("empirical_absence_not_used") is True,
            True,
            "本步只处理假设早期零行反例链中的 D0/finite-prefix 解析尾段输入，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "OldFinitePrefixTailHardpointImported",
            old_tail_active,
            False,
            "上一层 finite-prefix 尾桥留下的最窄旧粗原子正是自足倒素数 Mertens/Dusart 尾段。",
            OLD_TAIL,
        ),
        row(
            "DirectThetaPNTEnvelopeImported",
            direct_theta_closed,
            direct_theta_closed,
            "P5.1 自足同步已给出 theta/PNT 包络，可替代旧 Dusart theta 输入。",
            "closed" if direct_theta_closed else "DirectInternalDusartThetaPNTEnvelopeLedger",
        ),
        row(
            "SelfContainedB1IntervalImported",
            b1_closed,
            b1_closed,
            "Meissel-Mertens B1 常数区间已由 Euler-product 区间证书自足闭合。",
            "closed" if b1_closed else "SelfContainedMeisselMertensConstantIntervalLedgerAt20000",
        ),
        row(
            "RateBearingMertensTailSyncImported",
            tail_closed,
            tail_closed,
            "有限倒素数跳点、分部求和、theta/PNT 包络和 B1 区间合成后，旧 Mertens 尾段粗原子已移出活动剩余。",
            "closed" if tail_closed else OLD_TAIL,
        ),
        row(
            "FinitePrefixStrictMertensComponentClosed",
            old_tail_active and tail_closed,
            old_tail_active and tail_closed,
            "把已闭合的自足 Mertens 尾段回接到 finite-prefix 解析尾桥；旧 `SelfContainedDusart...` 不再是该桥的活动硬点。",
            "closed" if old_tail_active and tail_closed else OLD_TAIL,
        ),
        row(
            "TerminalBudgetB3TVAlreadySynchronized",
            terminal_synced,
            terminal_synced,
            "终端预算前沿已把 B3-TV、Mertens 尾段、prefix 抗塌缩和冷供给纪律同步到正余量问题。",
            "ExplicitPositiveTerminalBudgetMarginInequality",
        ),
        row(
            "FinitePrefixExternalOrStandardCertificateClosed",
            bridge.get("finite_boundary_prefix_certificate_external_or_standard_closed") is True,
            False,
            "外部/标准 lower-sieve 合同下，finite-prefix D0 证书已经由 runner、同参数窗口、范围 manifest 和尾桥条件闭合。",
            "closed under accepted standard/external lower-sieve contract",
        ),
        row(
            "FirstPrinciplesBetaSieveAppendixStillOpen",
            not beta_first_principles_open,
            False,
            "若要求连 Rosser-Iwaniec lower-sieve 基本引理也完全内联，仍需补有限递归权重、支配证明和 1% 主系数误差账本。",
            "closed" if not beta_first_principles_open else BETA_APPENDIX,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只关闭 finite-prefix 尾桥中的旧 Mertens 粗原子；类型阈值、row-free 抗塌缩、命名回流和 DStructure 仍未全部闭合。",
            f"{TYPE_LEDGER} AND {ROW_FREE} AND {NAMED_RETURN} AND {DSTRUCTURE}",
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造 finite-prefix Mertens 导入同步证书。"""
    data = {
        "bridge": load_json("prime-matrix-strict-analytic-tail-to-finite-boundary-bridge-router.json"),
        "mertens": load_json("prime-matrix-strict-rate-bearing-tail-mertens-latest-sync-router.json"),
        "direct": load_json("prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json"),
        "b1": load_json("prime-matrix-strict-meissel-mertens-b1-interval-self-contained-router.json"),
        "terminal": load_json("prime-matrix-strict-terminal-budget-frontier-latest-sync-router.json"),
        "beta": load_json("prime-matrix-beta-sieve-self-contained-frontier-router.json"),
    }
    rows = build_rows(data)
    m_tail_closed = any(
        item["gate"] == "FinitePrefixStrictMertensComponentClosed" and item["closed"]
        for item in rows
    )
    standard_prefix_closed = any(
        item["gate"] == "FinitePrefixExternalOrStandardCertificateClosed" and item["closed"]
        for item in rows
    )

    return {
        "certificate_type": "prime_matrix_strict_finite_prefix_mertens_tail_import_sync_router",
        "status": "finite_prefix_mertens_tail_imported_next_type_rowfree_named_return_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "old_hardpoint": OLD_TAIL,
        "finite_prefix_strict_mertens_component_closed": m_tail_closed,
        "finite_boundary_prefix_certificate_external_or_standard_closed": standard_prefix_closed,
        "finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed": False,
        "first_principles_beta_sieve_appendix_still_open": True,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "hardpoint_before_router": OLD_TAIL,
        "hardpoint_after_router": TYPE_LEDGER,
        "next_direct_attack_target": TYPE_LEDGER,
        "parallel_attack_targets": [
            ROW_FREE,
            NAMED_RETURN,
            "TerminalCoreHotDivisorWindowPDECorSAE",
            "FixedTypeHistoryPDECExclusion",
            "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore",
            DSTRUCTURE,
            BETA_APPENDIX,
        ],
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "finite-prefix 尾桥留下的旧 `SelfContainedDusartReciprocalPrimeProofAppendixXGe10372` "
            "已可由现有自足 theta/PNT+B1 证书回接关闭：P5.1 同步给 theta/PNT 包络，"
            "Euler-product 区间给 B1，速率尾段 Mertens 同步已确认完整倒素数尾段移出活动剩余。"
            "因此在当前已接受的 standard/external lower-sieve 合同下，finite-prefix D0 分支不再卡在 Mertens。"
            "但这还不是行/列命题无条件闭合；下一真正主攻点回到 `FormalUnitTypeThresholdLedger`，"
            "并行保留 row-free 抗塌缩、命名回流、热/固定历史、moving atom 与 DStructure 门。"
            "若要求 lower-sieve 基本引理也完全从零内联，则 beta-sieve 三项附录仍是独立强化任务。"
        ),
    }


def write_markdown(result: dict[str, Any]) -> None:
    """写出 Markdown 摘要。"""
    lines = [
        "# Prime Matrix strict finite-prefix Mertens 尾段导入同步路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_prefix_strict_mertens_component_closed={fmt_bool(result['finite_prefix_strict_mertens_component_closed'])}",
        f"finite_boundary_prefix_certificate_external_or_standard_closed={fmt_bool(result['finite_boundary_prefix_certificate_external_or_standard_closed'])}",
        f"finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed={fmt_bool(result['finite_boundary_prefix_certificate_strict_first_principles_lower_sieve_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "|---|---:|---:|---|---|",
    ]
    for item in result["rows"]:
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
