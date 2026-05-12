#!/usr/bin/env python3
"""生成 strict theta(x)<x 到 8e11 的有限表外部闭合证书。

用法示例：
  python3 experiments/prime_matrix_strict_theta_less_than_identity_to_8e11_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-theta-less-than-identity-to-8e11-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 60

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-theta-less-than-identity-to-8e11-router.json"
OUT_MD = DOCS / "prime-matrix-strict-theta-less-than-identity-to-8e11-router.md"

PREVIOUS = DOCS / "prime-matrix-strict-psi-theta-gap-middle-self-contained-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
SOURCE_FILES = [PREVIOUS, CLAIM_STATUS]

DUSART_SOURCE = Path("/tmp/Estimates2.tex")

TARGET = "ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger"
P51_SYNC = "DusartP51ThetaUpperFullSyncLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

SMALL_LIMIT = 100_000_000
TABLE_LIMIT = Decimal("8e11")

# Dusart table_012, caption "Values for theta(x)".
# 表示在 [n*10^k,(n+1)*10^k] 上有 theta(x)<=x+b1*x/log x。
DUSART_TABLE_012_ROWS = [
    ("1E+08", "-0.00044"),
    ("2E+08", "-0.00065"),
    ("3E+08", "-0.00057"),
    ("4E+08", "-0.00049"),
    ("5E+08", "-0.00052"),
    ("6E+08", "-0.00038"),
    ("7E+08", "-0.00051"),
    ("8E+08", "-0.00044"),
    ("9E+08", "-0.00050"),
    ("1E+09", "-0.00021"),
    ("2E+09", "-0.00018"),
    ("3E+09", "-0.00015"),
    ("4E+09", "-0.00017"),
    ("5E+09", "-0.00018"),
    ("6E+09", "-0.00013"),
    ("7E+09", "-0.00018"),
    ("8E+09", "-0.00016"),
    ("9E+09", "-0.00010"),
    ("1E+10", "-0.00008"),
    ("2E+10", "-0.00006"),
    ("3E+10", "-0.00005"),
    ("4E+10", "-0.00007"),
    ("5E+10", "-0.00004"),
    ("6E+10", "-0.00006"),
    ("7E+10", "-0.00004"),
    ("8E+10", "-0.00006"),
    ("9E+10", "-0.00004"),
    ("1E+11", "-0.00002"),
    ("2E+11", "-0.00002"),
    ("3E+11", "-0.00001"),
    ("4E+11", "-0.00002"),
    ("5E+11", "-0.00001"),
    ("6E+11", "-0.00002"),
    ("7E+11", "-0.00001"),
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记仓库内依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def external_source_payload() -> dict[str, Any]:
    """登记本地 Dusart arXiv 源文件边界。"""
    if not DUSART_SOURCE.exists():
        return {
            "path": str(DUSART_SOURCE),
            "available": False,
            "sha256": None,
            "table_012_label_found": False,
            "p51_use_site_found": False,
        }
    text = DUSART_SOURCE.read_text(encoding="utf-8", errors="replace")
    return {
        "path": str(DUSART_SOURCE),
        "available": True,
        "sha256": sha256(DUSART_SOURCE),
        "table_012_label_found": "\\label{table_012}" in text,
        "p51_use_site_found": "theta(x)<x" in text and "8\\cdot10^{11}" in text,
    }


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
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


def parse_label(label: str) -> tuple[Decimal, Decimal]:
    """把 7E+11 解析为 [7e11,8e11]。"""
    mantissa, exponent = label.split("E+")
    n = Decimal(mantissa)
    scale = Decimal(10) ** int(exponent)
    return n * scale, (n + 1) * scale


def dusart_table_audit() -> dict[str, Any]:
    """机器化审计 table_012 的 b1 负号列是否覆盖 [1e8,8e11]。"""
    intervals = []
    for label, b1_text in DUSART_TABLE_012_ROWS:
        left, right = parse_label(label)
        b1 = Decimal(b1_text)
        # 相对余量为 -b1/log(x)，在每个区间右端最小。
        margin = (-b1) / right.ln()
        intervals.append(
            {
                "label": label,
                "left": str(left),
                "right": str(right),
                "b1": str(b1),
                "relative_margin_at_right": str(margin),
                "strict_upper_below_identity": b1 < 0,
            }
        )

    continuity = intervals[0]["left"] == str(Decimal(SMALL_LIMIT))
    for prev, curr in zip(intervals, intervals[1:]):
        continuity = continuity and prev["right"] == curr["left"]

    worst = min(intervals, key=lambda item: Decimal(item["relative_margin_at_right"]))
    payload = {
        "published_table": "Dusart arXiv 1002.0442 table_012 / Values for theta(x)",
        "table_rule": "theta(x)<=x+b1*x/log(x) on each [n*10^k,(n+1)*10^k]",
        "interval_count": len(intervals),
        "covers_from": intervals[0]["left"],
        "covers_to": intervals[-1]["right"],
        "target_upper_endpoint": str(TABLE_LIMIT),
        "continuous_cover_from_1e8_to_8e11": continuity and Decimal(intervals[-1]["right"]) == TABLE_LIMIT,
        "all_b1_negative": all(item["strict_upper_below_identity"] for item in intervals),
        "worst_relative_margin_row": worst,
        "intervals": intervals,
    }
    payload["table_transcription_hash"] = hashlib.sha256(
        json.dumps(DUSART_TABLE_012_ROWS, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return payload


def small_theta_audit(limit: int = SMALL_LIMIT) -> dict[str, Any]:
    """有限检查 x<=1e8：只需检查素数跳点 theta(p)<p。"""
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    root = int(limit**0.5)
    for prime in range(2, root + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (((limit - start) // prime) + 1)

    theta = 0.0
    prime_count = 0
    min_surplus = float("inf")
    min_surplus_prime = None
    max_ratio = 0.0
    max_ratio_prime = None
    for prime in range(2, limit + 1):
        if sieve[prime]:
            prime_count += 1
            theta += math.log(prime)
            surplus = prime - theta
            if surplus < min_surplus:
                min_surplus = surplus
                min_surplus_prime = prime
            ratio = theta / prime
            if ratio > max_ratio:
                max_ratio = ratio
                max_ratio_prime = prime

    payload = {
        "method": "sieve primes <=1e8 and check theta(p)<p at every jump; between jumps theta is constant",
        "limit": limit,
        "prime_count": prime_count,
        "min_surplus_p_minus_theta_p": min_surplus,
        "min_surplus_prime": min_surplus_prime,
        "max_theta_over_p": max_ratio,
        "max_ratio_prime": max_ratio_prime,
        "closed": min_surplus > 1.0,
        "rounding_guard": 1.0,
    }
    payload["audit_hash"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return payload


def build_result() -> dict[str, Any]:
    """构造 theta(x)<x 到 8e11 的外部表闭合证书。"""
    previous = load_json(PREVIOUS)
    source = external_source_payload()
    small = small_theta_audit()
    table = dusart_table_audit()

    active = previous.get("next_direct_attack_target") == TARGET
    psi_theta_gap_closed = previous.get("psi_minus_theta_lower_gap_09999_sqrt_self_contained_closed") is True
    source_identified = (
        source["available"] and source["table_012_label_found"] and source["p51_use_site_found"]
    )
    table_external_closed = (
        source_identified
        and table["continuous_cover_from_1e8_to_8e11"]
        and table["all_b1_negative"]
    )
    theta_external_closed = small["closed"] and table_external_closed
    theta_self_contained_closed = False

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            previous.get("counterexample_assumption_only") is True
            and previous.get("row_column_unconditional_closed") is False,
            True,
            "本步只补 P5.1 的低段 theta 输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "ThetaFiniteTableGateActive",
            active,
            True,
            "上一证书已把下一最窄点设为 theta(x)<x 到 8e11 的有限表/证书。",
            TARGET,
        ),
        row(
            "SmallSegmentSelfContainedFiniteAuditTo1e8",
            small["closed"],
            True,
            "对 x<=1e8，仅需检查 theta 在素数跳点 p 的值；本地筛验算 theta(p)<p 有大于 1 的保护余量。",
            small["audit_hash"],
        ),
        row(
            "DusartTable012SourceIdentified",
            source_identified,
            True,
            "本地 arXiv 源 `/tmp/Estimates2.tex` 含 table_012 和 P5.1 使用点。",
            source["sha256"] or "source missing",
        ),
        row(
            "DusartTable012NegativeB1Cover",
            table_external_closed,
            True,
            "table_012 的每个区间都有 b1<0，故 theta(x)<=x+b1*x/log x < x，连续覆盖 [1e8,8e11]。",
            table["table_transcription_hash"],
        ),
        row(
            "ThetaLessThanIdentityTo8e11ExternalClosed",
            theta_external_closed,
            True,
            "低段有限审计加 Dusart table_012 外部表，给出 0<x<=8e11 上 theta(x)<x。",
            "external table accepted",
        ),
        row(
            TARGET,
            theta_self_contained_closed,
            False,
            "严格作者侧自足版仍缺 table_012 的原始计算数据/hash；当前闭合为外部表路线。",
            "need reproducible finite computation/hash up to 8e11 for fully self-contained route",
        ),
        row(
            "P51NonPsiInputsReadyOnExternalLane",
            theta_external_closed and psi_theta_gap_closed,
            True,
            "P5.1 的两个非 psi 输入已在外部/半自足路线齐备：theta<x 到 8e11，psi-theta 中段下界。",
            P51_SYNC,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步关闭的是 P5.1 低段 theta 输入，不直接产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_theta_less_than_identity_to_8e11_router",
        "status": "theta_less_than_identity_to_8e11_external_closed_self_contained_table_hash_remains_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "theta_less_than_identity_to_8e11_external_closed": theta_external_closed,
        "theta_less_than_identity_to_8e11_self_contained_closed": theta_self_contained_closed,
        "theta_less_than_identity_to_1e8_self_contained_closed": small["closed"],
        "dusart_table012_negative_b1_cover_closed": table_external_closed,
        "psi_minus_theta_lower_gap_09999_sqrt_self_contained_closed": psi_theta_gap_closed,
        "dusart_p51_nonpsi_inputs_ready_external_lane": theta_external_closed and psi_theta_gap_closed,
        "dusart_p51_full_theta_statement_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "external_source": source,
        "small_segment_audit": small,
        "dusart_table012_audit": table,
        "source_hashes": source_hashes(),
        "replacement_self_contained": {
            "SmallSegmentThetaLtIdentityTo1e8": "FiniteSieveAuditAtPrimeJumps",
            "ThetaLtIdentity1e8To8e11": "DusartTable012ExternalNegativeB1Cover",
        },
        "next_direct_attack_target": P51_SYNC,
        "parallel_attack_targets": [TARGET, DSTRUCTURE],
        "plain_conclusion": (
            "`theta(x)<x` 到 `8e11` 已在外部表路线闭合：`x<=1e8` 由本地有限筛检查素数跳点，"
            "`1e8<=x<=8e11` 由 Dusart `table_012` 的负 `b1` 列推出 "
            "`theta(x)<=x+b1*x/log(x)<x`。严格自足版仍缺 table_012 背后的原始有限计算/hash，"
            "但接受发表表格时，P5.1 的非 psi 输入已经齐备。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    small = result["small_segment_audit"]
    table = result["dusart_table012_audit"]
    worst = table["worst_relative_margin_row"]
    lines = [
        "# Prime Matrix strict theta(x)<x 到 8e11 外部表证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"theta_less_than_identity_to_8e11_external_closed={fmt_bool(result['theta_less_than_identity_to_8e11_external_closed'])}",
        f"theta_less_than_identity_to_8e11_self_contained_closed={fmt_bool(result['theta_less_than_identity_to_8e11_self_contained_closed'])}",
        f"dusart_p51_full_theta_statement_closed={fmt_bool(result['dusart_p51_full_theta_statement_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 低段有限审计",
        "",
        "| field | value |",
        "| --- | ---: |",
        f"| `limit` | `{small['limit']}` |",
        f"| `prime_count` | `{small['prime_count']}` |",
        f"| `min_surplus_p_minus_theta_p` | `{small['min_surplus_p_minus_theta_p']}` |",
        f"| `min_surplus_prime` | `{small['min_surplus_prime']}` |",
        f"| `max_theta_over_p` | `{small['max_theta_over_p']}` |",
        f"| `max_ratio_prime` | `{small['max_ratio_prime']}` |",
        f"| `rounding_guard` | `{small['rounding_guard']}` |",
        f"| `audit_hash` | `{small['audit_hash']}` |",
        "",
        "## 2. Dusart table_012 审计",
        "",
        "| field | value |",
        "| --- | --- |",
        f"| `interval_count` | `{table['interval_count']}` |",
        f"| `covers_from` | `{table['covers_from']}` |",
        f"| `covers_to` | `{table['covers_to']}` |",
        f"| `continuous_cover_from_1e8_to_8e11` | `{fmt_bool(table['continuous_cover_from_1e8_to_8e11'])}` |",
        f"| `all_b1_negative` | `{fmt_bool(table['all_b1_negative'])}` |",
        f"| `worst_margin_label` | `{worst['label']}` |",
        f"| `worst_margin_right` | `{worst['right']}` |",
        f"| `worst_relative_margin_at_right` | `{worst['relative_margin_at_right']}` |",
        f"| `table_transcription_hash` | `{table['table_transcription_hash']}` |",
        "",
        "## 3. 判定表",
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
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result) + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(
        "theta_less_than_identity_to_8e11_external_closed="
        f"{fmt_bool(result['theta_less_than_identity_to_8e11_external_closed'])}"
    )
    print(
        "theta_less_than_identity_to_8e11_self_contained_closed="
        f"{fmt_bool(result['theta_less_than_identity_to_8e11_self_contained_closed'])}"
    )
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
