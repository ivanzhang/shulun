#!/usr/bin/env python3
"""生成 strict 有限 theta 桥自足证书。

用法示例：
  python3 experiments/prime_matrix_strict_finite_theta_bridge_self_contained_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-finite-theta-bridge-self-contained-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.md"

OBSTRUCTION = MONOGRAPH / "prime-matrix-strict-internal-dusart-theta-budget-obstruction-router.json"
POST_MEISSEL = MONOGRAPH / "prime-matrix-strict-post-meissel-frontier-sync-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [OBSTRUCTION, POST_MEISSEL, CLAIM_STATUS]

ANCHOR_X = 20_000
DENOMINATOR = 36_260
DECIMAL_PRECISION = 80

THETA_TARGET = "ThetaEnvelopeTargetAt20000NumericalBudgetLedger"
FINITE_BRIDGE = "FiniteThetaEnvelopeBridgeBelowAnalyticThreshold"
FINITE_BRIDGE_CLOSED = "FiniteThetaBridgeBelow20000SelfContainedClosedByPrimeLogCertificate"
ANCHOR_CLOSED = "ThetaEnvelopeTargetAt20000SelfContainedClosedByPrimeLogCertificate"
INTERNAL_CONTOUR = "InternalZeroFreeRegionToThetaContourEnvelopeLedger"
LOW_HEIGHT = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
SELF_B1 = "SelfContainedMeisselMertensB1IntervalArithmeticLedger"
SELF_RECIPROCAL = "SelfContainedDusartReciprocalPrimeProofAppendixXGe10372"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
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


def primes_up_to(n: int) -> list[int]:
    """埃氏筛生成不超过 n 的素数。"""
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    limit = int(n**0.5)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def finite_theta_audit(n: int = ANCHOR_X) -> dict[str, Any]:
    """用高精度 Decimal 计算有限 theta 桥证书。"""
    getcontext().prec = DECIMAL_PRECISION
    one = Decimal(1)
    denom = Decimal(DENOMINATOR)
    slope = one + one / denom
    theta = Decimal(0)
    max_gap: Decimal | None = None
    max_prime = None
    max_theta = None
    prime_count = 0
    for p in primes_up_to(n):
        prime_count += 1
        theta += Decimal(p).ln()
        gap = theta - Decimal(p) * slope
        if max_gap is None or gap > max_gap:
            max_gap = gap
            max_prime = p
            max_theta = theta
    if max_gap is None or max_prime is None or max_theta is None:
        raise RuntimeError("no primes found")
    target_allowance = Decimal(n) / denom
    anchor_gap = theta - Decimal(n) - target_allowance
    return {
        "anchor_x": n,
        "target_denominator": DENOMINATOR,
        "decimal_precision": DECIMAL_PRECISION,
        "prime_count": prime_count,
        "last_prime": primes_up_to(n)[-1],
        "theta_anchor": str(theta),
        "target_allowance": str(target_allowance),
        "theta_minus_x": str(theta - Decimal(n)),
        "anchor_gap_theta_minus_x_minus_allowance": str(anchor_gap),
        "anchor_passes": anchor_gap < 0,
        "max_gap_prime": max_prime,
        "max_gap_theta": str(max_theta),
        "max_gap_theta_minus_slope_x": str(max_gap),
        "finite_bridge_passes": max_gap < 0,
        "finite_bridge_margin": str(-max_gap),
        "proof_reduction": (
            "对任意相邻素数区间 [p_k,p_{k+1})，vartheta(x) 常值而 "
            "vartheta(x)-(1+1/36260)x 严格递减；故 0<x<=20000 的最大值只需在素数点扫描。"
        ),
    }


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(obstruction: dict[str, Any], post: dict[str, Any], audit: dict[str, Any]) -> list[dict[str, Any]]:
    """生成有限 theta 桥判定表。"""
    guard = (
        obstruction.get("counterexample_assumption_only") is True
        and obstruction.get("direct_unconditional_contradiction_found") is False
        and obstruction.get("row_column_unconditional_closed") is False
        and post.get("row_column_unconditional_closed") is False
    )
    bridge_closed = audit["finite_bridge_passes"] is True
    anchor_closed = audit["anchor_passes"] is True
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只给解析输入的有限核验证书，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "FinitePrimeLogThetaCertificateBuilt",
            bridge_closed,
            True,
            "用素数点高精度 log 累加与单调性，扫描 0<x<=20000 的 theta 上界。",
            FINITE_BRIDGE_CLOSED,
        ),
        row(
            THETA_TARGET,
            anchor_closed,
            True,
            "x=20000 处 theta(x)-x 明显为负，强于 x/36260 允许值。",
            ANCHOR_CLOSED,
        ),
        row(
            FINITE_BRIDGE,
            bridge_closed,
            True,
            "最坏素数点 x=3 仍满足 theta(x)-x < x/36260，因此阈值以下有限桥自足闭合。",
            FINITE_BRIDGE_CLOSED,
        ),
        row(
            "InternalDusartGlobalThetaEnvelopeClosed",
            False,
            False,
            "有限桥只覆盖 0<x<=20000，不证明 x>=20000 的内部 Dusart/PNT 包络。",
            INTERNAL_CONTOUR,
        ),
        row(
            "SelfContainedMertensTailClosed",
            False,
            False,
            "有限 theta 桥不关闭 B1 区间、reciprocal-prime Mertens 尾段或 DStructure 门。",
            f"{SELF_B1} AND {SELF_RECIPROCAL} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "该有限桥只补解析输入，不产生最终反例矛盾。",
            DSTRUCTURE,
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造有限 theta 桥证书。"""
    obstruction = load_json(OBSTRUCTION)
    post = load_json(POST_MEISSEL)
    audit = finite_theta_audit()
    rows = build_rows(obstruction, post, audit)
    return {
        "certificate_type": "prime_matrix_strict_finite_theta_bridge_self_contained_router",
        "status": "finite_theta_bridge_and_anchor_self_contained_closed_global_theta_contour_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "theta_target_at_20000_self_contained_closed": audit["anchor_passes"],
        "finite_theta_bridge_below_20000_self_contained_closed": audit["finite_bridge_passes"],
        "internal_dusart_global_theta_envelope_closed": False,
        "internal_zero_free_region_to_theta_contour_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement_self_contained": {
            THETA_TARGET: ANCHOR_CLOSED,
            FINITE_BRIDGE: FINITE_BRIDGE_CLOSED,
        },
        "finite_theta_audit": audit,
        "remaining_self_contained_inputs_after_finite_theta": [
            LOW_HEIGHT,
            INTERNAL_CONTOUR,
            SELF_B1,
            SELF_RECIPROCAL,
        ],
        "next_direct_attack_target": INTERNAL_CONTOUR,
        "parallel_attack_targets": [LOW_HEIGHT, SELF_B1, SELF_RECIPROCAL],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "有限 theta 桥可以自足闭合：因为 `vartheta(x)-(1+1/36260)x` 在相邻素数之间严格递减，"
            "只需扫描 `p<=20000` 的素数点。高精度证书显示最坏点为 `p=3`，仍有约 `1.208` 的负余量；"
            "`x=20000` 处 `vartheta(20000)-20000≈-194.69`，远小于允许值 `20000/36260≈0.5516`。"
            "这关闭的是锚点和阈值以下有限桥，不关闭 `x>=20000` 的内部 theta/PNT contour 包络。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    audit = result["finite_theta_audit"]
    lines = [
        "# Prime Matrix strict 有限 theta 桥自足路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"theta_target_at_20000_self_contained_closed={fmt_bool(result['theta_target_at_20000_self_contained_closed'])}",
        f"finite_theta_bridge_below_20000_self_contained_closed={fmt_bool(result['finite_theta_bridge_below_20000_self_contained_closed'])}",
        f"internal_dusart_global_theta_envelope_closed={fmt_bool(result['internal_dusart_global_theta_envelope_closed'])}",
        f"internal_zero_free_region_to_theta_contour_closed={fmt_bool(result['internal_zero_free_region_to_theta_contour_closed'])}",
        f"self_contained_mertens_tail_closed={fmt_bool(result['self_contained_mertens_tail_closed'])}",
        f"b3_tv_strict_self_contained_closed={fmt_bool(result['b3_tv_strict_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 有限核验",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| anchor x | `{audit['anchor_x']}` |",
        f"| prime count | `{audit['prime_count']}` |",
        f"| last prime | `{audit['last_prime']}` |",
        f"| theta(anchor) | `{audit['theta_anchor']}` |",
        f"| theta(anchor)-anchor | `{audit['theta_minus_x']}` |",
        f"| target allowance | `{audit['target_allowance']}` |",
        f"| anchor gap | `{audit['anchor_gap_theta_minus_x_minus_allowance']}` |",
        f"| max gap prime | `{audit['max_gap_prime']}` |",
        f"| max finite bridge gap | `{audit['max_gap_theta_minus_slope_x']}` |",
        f"| finite bridge margin | `{audit['finite_bridge_margin']}` |",
        "",
        "证明化简：",
        "",
        audit["proof_reduction"],
        "",
        "## 2. 自足替换",
        "",
        "| old | new |",
        "| --- | --- |",
    ]
    for old, new in result["replacement_self_contained"].items():
        lines.append(f"| `{old}` | `{new}` |")
    lines.extend(
        [
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
