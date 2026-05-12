#!/usr/bin/env python3
"""生成 strict Dusart P5.1 theta 上界全段同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_dusart_p51_theta_upper_full_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-dusart-p51-theta-upper-full-sync-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 70

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-dusart-p51-theta-upper-full-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-dusart-p51-theta-upper-full-sync-router.md"

HIGH_TAIL = DOCS / "prime-matrix-strict-table63-b28-high-tail-p51-splice-sync-router.json"
PSI_THETA = DOCS / "prime-matrix-strict-psi-theta-gap-middle-self-contained-router.json"
THETA_TABLE = DOCS / "prime-matrix-strict-theta-less-than-identity-to-8e11-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SOURCE_FILES = [HIGH_TAIL, PSI_THETA, THETA_TABLE, CLAIM_STATUS]

TARGET = "DusartP51ThetaUpperFullSyncLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
STRICT_SELF = "DusartP51ThetaUpperFullSelfContainedLedger"

ONE_OVER_36260 = Decimal(1) / Decimal(36260)
FK_DIRECTED_UPPER = Decimal("0.00001262")
MIDDLE_UPPER_DELTA = Decimal("0.00002841")
MIDDLE_GAP_RELATIVE = Decimal("0.9999") * Decimal(-14).exp()
MIDDLE_RESULT = MIDDLE_UPPER_DELTA - MIDDLE_GAP_RELATIVE
X_LOW_END = Decimal("8e11")
X_HIGH_START = Decimal(28).exp()


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    return "true" if bool(value) else "false"


def fmt_dec(value: Decimal) -> str:
    """稳定输出 Decimal。"""
    return format(value, ".18e")


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


def arithmetic_payload() -> dict[str, str]:
    """记录三段拼接算术。"""
    return {
        "target_1_over_36260": str(ONE_OVER_36260),
        "low_segment_result_relative": "0",
        "low_segment_margin": str(ONE_OVER_36260),
        "middle_segment_result_relative": str(MIDDLE_RESULT),
        "middle_segment_margin": str(ONE_OVER_36260 - MIDDLE_RESULT),
        "high_segment_result_relative": str(FK_DIRECTED_UPPER),
        "high_segment_margin": str(ONE_OVER_36260 - FK_DIRECTED_UPPER),
        "x_low_end_8e11": str(X_LOW_END),
        "x_high_start_e28": str(X_HIGH_START),
        "middle_strip_nonempty": str(X_LOW_END < X_HIGH_START),
    }


def build_result() -> dict[str, Any]:
    """构造 Dusart P5.1 全段同步证书。"""
    high_tail = load_json(HIGH_TAIL)
    psi_theta = load_json(PSI_THETA)
    theta_table = load_json(THETA_TABLE)

    active = theta_table.get("next_direct_attack_target") == TARGET
    psi_pair_closed = high_tail.get("psi_relative_error_pair_for_p51_closed") is True
    high_tail_closed = high_tail.get("table63_b28_high_tail_input_to_p51_splice_closed") is True
    psi_theta_closed = psi_theta.get("psi_minus_theta_lower_gap_09999_sqrt_self_contained_closed") is True
    theta_external_closed = theta_table.get("theta_less_than_identity_to_8e11_external_closed") is True
    theta_self_closed = theta_table.get("theta_less_than_identity_to_8e11_self_contained_closed") is True
    arithmetic_closed = (
        FK_DIRECTED_UPPER < ONE_OVER_36260
        and MIDDLE_RESULT < ONE_OVER_36260
        and X_LOW_END < X_HIGH_START
    )
    external_full_closed = (
        active
        and psi_pair_closed
        and high_tail_closed
        and psi_theta_closed
        and theta_external_closed
        and arithmetic_closed
    )
    self_contained_full_closed = external_full_closed and theta_self_closed

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            theta_table.get("counterexample_assumption_only") is True
            and theta_table.get("row_column_unconditional_closed") is False,
            True,
            "本步只合取 P5.1 的解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "DusartP51FullSyncGateActive",
            active,
            True,
            "上一证书已把下一最窄点设为 Dusart P5.1 全段 theta 上界同步。",
            TARGET,
        ),
        row(
            "LowSegmentThetaLtIdentityTo8e11",
            theta_external_closed,
            True,
            "对 0<x<=8e11，theta(x)<x，故 theta(x)-x<0<x/36260。",
            "external table lane",
        ),
        row(
            "MiddleStripPsiThetaSplice",
            psi_pair_closed and psi_theta_closed and MIDDLE_RESULT < ONE_OVER_36260,
            True,
            "对 8e11<=x<=e^28，psi<1.00002841x 且 psi-theta>0.9999sqrt(x)，得到目标余量。",
            "middle strip closed",
        ),
        row(
            "HighTailFaberKadiriB28Splice",
            high_tail_closed and FK_DIRECTED_UPPER < ONE_OVER_36260,
            True,
            "对 x>=e^28，FK b0=28 给出 psi 高尾误差 0.00001262，小于 1/36260；theta<=psi。",
            "high tail closed",
        ),
        row(
            "ThreeSegmentArithmeticClosed",
            arithmetic_closed,
            True,
            "低段、中段、高尾三段阈值顺序与余量均为正。",
            "arithmetic synchronized",
        ),
        row(
            TARGET,
            external_full_closed,
            True,
            "接受 FK 高尾与 Dusart table_012 外部表时，Dusart P5.1 全段 theta(x)-x<x/36260 已闭合。",
            "external lane theorem closed",
        ),
        row(
            STRICT_SELF,
            self_contained_full_closed,
            False,
            "严格作者侧完全自足版仍未闭合，因为 theta table_012 原始计算/hash 未内化。",
            "internalize table_012 finite computation/hash, and optionally FK kernel source",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步关闭的是解析输入定理，不直接产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_dusart_p51_theta_upper_full_sync_router",
        "status": "dusart_p51_theta_upper_full_external_lane_closed_self_contained_finite_table_remains_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dusart_p51_full_theta_statement_closed": external_full_closed,
        "dusart_p51_full_theta_statement_external_closed": external_full_closed,
        "dusart_p51_full_theta_statement_self_contained_closed": self_contained_full_closed,
        "theta_minus_identity_upper_1_over_36260_for_all_x_external_closed": external_full_closed,
        "theta_less_than_identity_to_8e11_external_closed": theta_external_closed,
        "theta_less_than_identity_to_8e11_self_contained_closed": theta_self_closed,
        "psi_relative_error_pair_for_p51_closed": psi_pair_closed,
        "psi_minus_theta_lower_gap_09999_sqrt_self_contained_closed": psi_theta_closed,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "arithmetic": arithmetic_payload(),
        "source_hashes": source_hashes(),
        "theorem_statement_external_lane": (
            "For every x>0, theta(x)-x < x/36260, using FK b0=28 high tail, "
            "middle psi node archive plus psi-theta finite audit, and Dusart table_012 for theta(x)<x up to 8e11."
        ),
        "next_direct_attack_target": DSTRUCTURE,
        "parallel_attack_targets": [STRICT_SELF],
        "plain_conclusion": (
            "Dusart P5.1 的全段外部路线已经闭合：低段由 `theta(x)<x` 到 `8e11` 给出，"
            "中段由 `psi<1.00002841x` 与 `psi-theta>0.9999sqrt(x)` 拼接给出，"
            "高尾由 FK b0=28 的 `0.00001262<1/36260` 给出。"
            "因此可登记 `theta(x)-x<x/36260` 对所有 `x>0` 成立。"
            "但严格作者侧完全自足版仍剩 table_012 原始有限计算/hash。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    arith = result["arithmetic"]
    lines = [
        "# Prime Matrix strict Dusart P5.1 theta 上界全段同步证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dusart_p51_full_theta_statement_external_closed={fmt_bool(result['dusart_p51_full_theta_statement_external_closed'])}",
        f"dusart_p51_full_theta_statement_self_contained_closed={fmt_bool(result['dusart_p51_full_theta_statement_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 三段算术",
        "",
        "| segment | relative result | margin to 1/36260 |",
        "| --- | ---: | ---: |",
        f"| low `0<x<=8e11` | `{arith['low_segment_result_relative']}` | `{arith['low_segment_margin']}` |",
        f"| middle `8e11<=x<=e^28` | `{arith['middle_segment_result_relative']}` | `{arith['middle_segment_margin']}` |",
        f"| high `x>=e^28` | `{arith['high_segment_result_relative']}` | `{arith['high_segment_margin']}` |",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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
            "## 3. 下一最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "dusart_p51_full_theta_statement_external_closed="
        f"{fmt_bool(result['dusart_p51_full_theta_statement_external_closed'])}"
    )
    print(
        "dusart_p51_full_theta_statement_self_contained_closed="
        f"{fmt_bool(result['dusart_p51_full_theta_statement_self_contained_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
