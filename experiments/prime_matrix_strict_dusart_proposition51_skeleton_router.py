#!/usr/bin/env python3
"""生成 strict Dusart Proposition 5.1 证明骨架形式化路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_dusart_proposition51_skeleton_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-dusart-proposition51-skeleton-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-dusart-proposition51-skeleton-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-dusart-proposition51-skeleton-router.md"

DIRECT_DUSART = MONOGRAPH / "prime-matrix-strict-direct-internal-dusart-pnt-envelope-router.json"
FINITE_THETA = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [DIRECT_DUSART, FINITE_THETA, CLAIM_STATUS]

TARGET = "DusartProposition51ProofSkeletonFormalizationLedger"
ANALYTIC = "DusartThetaAnalyticKernelAndThresholdLedger"
MIDDLE = "DusartThetaMiddleRangeFiniteVerificationLedger"
LOW_HEIGHT = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
FINITE_CLOSED = "FiniteThetaBridgeBelow20000SelfContainedClosedByPrimeLogCertificate"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ANCHOR_X = 20_000
TARGET_DENOMINATOR = 36_260


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记本步依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


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


def skeleton_segments() -> list[dict[str, str]]:
    """列出作者侧内部化证明的无重叠分段。"""
    return [
        {
            "segment": "0 < x <= 20000",
            "responsibility": FINITE_CLOSED,
            "status": "closed",
            "role": "有限 theta 桥已经自足关闭该段。",
        },
        {
            "segment": "20000 < x < X_A",
            "responsibility": MIDDLE,
            "status": "open",
            "role": "解析阈值以下的中段必须用有限表或可复现 hash 关闭。",
        },
        {
            "segment": "x >= X_A",
            "responsibility": ANALYTIC,
            "status": "open",
            "role": "高段必须给出直接 theta/PNT 显式核和误差界。",
        },
        {
            "segment": "zero audit input",
            "responsibility": LOW_HEIGHT,
            "status": "open",
            "role": "若解析核使用零点计数/零点自由区，低高度 Turing/无零证书必须文内化。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 Dusart Proposition 5.1 证明骨架形式化证书。"""
    direct = load_json(DIRECT_DUSART)
    finite = load_json(FINITE_THETA)
    active = direct.get("next_direct_attack_target") == TARGET
    finite_ready = finite.get("finite_theta_bridge_below_20000_self_contained_closed") is True
    skeleton_closed = active and finite_ready
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            direct.get("counterexample_assumption_only") is True and direct.get("row_column_unconditional_closed") is False,
            True,
            "本步只形式化外部定理的作者侧证明结构，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "DusartSkeletonGateActive",
            active,
            True,
            "直接内部 Dusart/PNT 路由已把第一子包设为证明骨架形式化。",
            TARGET,
        ),
        row(
            "FiniteLeftSegmentAlreadyClosed",
            finite_ready,
            True,
            "左端 0<x<=20000 已由有限 theta 桥自足证书关闭。",
            FINITE_CLOSED,
        ),
        row(
            TARGET,
            skeleton_closed,
            True,
            "证明骨架闭合为三段责任：已闭合左段、中段有限桥、高段解析核，外加低高度证书。",
            f"{ANALYTIC} AND {MIDDLE} AND {LOW_HEIGHT}",
        ),
        row(
            "DirectInternalDusartThetaPNTEnvelopeClosed",
            False,
            False,
            "骨架闭合不等于定理闭合；解析核、中段表和低高度证书仍开放。",
            f"{ANALYTIC} AND {MIDDLE} AND {LOW_HEIGHT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "证明骨架形式化不产生最终反例矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_dusart_proposition51_skeleton_router",
        "status": "dusart_proposition51_skeleton_formalized_analytic_middle_lowheight_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dusart_proposition51_skeleton_formalized": skeleton_closed,
        "direct_internal_dusart_theta_pnt_envelope_closed": False,
        "finite_left_segment_closed": finite_ready,
        "analytic_kernel_and_threshold_closed": False,
        "middle_range_finite_verification_closed": False,
        "finite_low_height_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_statement_for_internalization": f"vartheta(x)-x < x/{TARGET_DENOMINATOR} for x>0",
        "anchor_x": ANCHOR_X,
        "skeleton_segments": skeleton_segments(),
        "replacement_self_contained": {
            TARGET: f"{ANALYTIC} AND {MIDDLE} AND {LOW_HEIGHT}",
        },
        "next_direct_attack_target": ANALYTIC,
        "parallel_attack_targets": [MIDDLE, LOW_HEIGHT],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Dusart Proposition 5.1 的作者侧证明骨架已形式化：`0<x<=20000` 左段由有限 theta 桥关闭；"
            "剩余必须分成 `x>=X_A` 的解析核与阈值、`20000<x<X_A` 的中段有限核验、以及低高度 Turing/无零证书。"
            "本步只关闭骨架，不关闭内部 Dusart/PNT 定理。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    replacement = next(iter(result["replacement_self_contained"].items()))
    lines = [
        "# Prime Matrix strict Dusart Proposition 5.1 证明骨架路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dusart_proposition51_skeleton_formalized={fmt_bool(result['dusart_proposition51_skeleton_formalized'])}",
        f"direct_internal_dusart_theta_pnt_envelope_closed={fmt_bool(result['direct_internal_dusart_theta_pnt_envelope_closed'])}",
        f"analytic_kernel_and_threshold_closed={fmt_bool(result['analytic_kernel_and_threshold_closed'])}",
        f"middle_range_finite_verification_closed={fmt_bool(result['middle_range_finite_verification_closed'])}",
        f"finite_low_height_self_contained_closed={fmt_bool(result['finite_low_height_self_contained_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 分段责任",
        "",
        "| segment | responsibility | status | role |",
        "| --- | --- | --- | --- |",
    ]
    for item in result["skeleton_segments"]:
        lines.append(
            f"| `{table_cell(item['segment'])}` | `{table_cell(item['responsibility'])}` | "
            f"`{table_cell(item['status'])}` | {table_cell(item['role'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 自足替换",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
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
            "## 4. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(result["status"])
    print("next_direct_attack_target=", result["next_direct_attack_target"])


if __name__ == "__main__":
    main()
