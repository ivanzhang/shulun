#!/usr/bin/env python3
"""生成 strict Dusart 解析核与阈值拼接路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_dusart_analytic_kernel_threshold_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-dusart-analytic-kernel-threshold-router.json
"""

from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


getcontext().prec = 50

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.md"

SKELETON = MONOGRAPH / "prime-matrix-strict-dusart-proposition51-skeleton-router.json"
FINITE_THETA = MONOGRAPH / "prime-matrix-strict-finite-theta-bridge-self-contained-router.json"
ZERO_SUM = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
TRIVIAL_TAIL = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [SKELETON, FINITE_THETA, ZERO_SUM, TRIVIAL_TAIL, CLAIM_STATUS]

TARGET = "DusartThetaAnalyticKernelAndThresholdLedger"
PSI_EPS = "PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger"
PSI_THETA_GAP = "PsiMinusThetaLowerGap09999SqrtSelfContainedLedger"
THETA_TABLE = "ThetaLessThanIdentityFiniteTableTo8e11SelfContainedLedger"
ARITH_SPLICE = "DusartP51ArithmeticSpliceClosed"
MIDDLE = "DusartThetaMiddleRangeFiniteVerificationLedger"
LOW_HEIGHT = "CriticalLineNoZeroOn0To14FiniteLedger AND CriticalStripNoOffLineZeroBelow14TuringLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ARXIV_URL = "https://arxiv.org/abs/1002.0442"
ARXIV_ID = "arXiv:1002.0442"

TARGET_DENOMINATOR = Decimal(36_260)
TARGET_RELATIVE = Decimal(1) / TARGET_DENOMINATOR
EPS_HIGH_B28 = Decimal("0.00002224")
EPS_MIDDLE_2841 = Decimal("0.00002841")
GAP_COEFFICIENT = Decimal("0.9999")
EXP_NEG_14 = Decimal(-14).exp()
MIDDLE_GAP_RELATIVE = GAP_COEFFICIENT * EXP_NEG_14
MIDDLE_RESULT_RELATIVE = EPS_MIDDLE_2841 - MIDDLE_GAP_RELATIVE
HIGH_MARGIN = TARGET_RELATIVE - EPS_HIGH_B28
MIDDLE_MARGIN = TARGET_RELATIVE - MIDDLE_RESULT_RELATIVE
X_FINITE_TABLE = Decimal("8e11")
X_HIGH_THRESHOLD = Decimal(28).exp()
X_LOCAL_BRIDGE = Decimal(20_000)


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


def fmt_dec(value: Decimal) -> str:
    """稳定输出 Decimal 小数。"""
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


def arithmetic_rows() -> list[dict[str, str]]:
    """列出 Dusart P5.1 拼接中的关键数值余量。"""
    return [
        {
            "check": "target relative error",
            "formula": "1/36260",
            "value": fmt_dec(TARGET_RELATIVE),
            "margin": "baseline",
        },
        {
            "check": "high tail x>=e^28",
            "formula": "0.00002224 < 1/36260",
            "value": fmt_dec(EPS_HIGH_B28),
            "margin": fmt_dec(HIGH_MARGIN),
        },
        {
            "check": "middle strip 8e11<=x<=e^28",
            "formula": "0.00002841 - 0.9999 e^-14 < 1/36260",
            "value": fmt_dec(MIDDLE_RESULT_RELATIVE),
            "margin": fmt_dec(MIDDLE_MARGIN),
        },
        {
            "check": "threshold ordering",
            "formula": "8e11 < e^28",
            "value": f"{fmt_dec(X_FINITE_TABLE)} < {fmt_dec(X_HIGH_THRESHOLD)}",
            "margin": fmt_dec(X_HIGH_THRESHOLD - X_FINITE_TABLE),
        },
        {
            "check": "current finite bridge reach",
            "formula": "20000 < 8e11",
            "value": f"{fmt_dec(X_LOCAL_BRIDGE)} < {fmt_dec(X_FINITE_TABLE)}",
            "margin": fmt_dec(X_FINITE_TABLE - X_LOCAL_BRIDGE),
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 Dusart 解析核与阈值拼接证书。"""
    skeleton = load_json(SKELETON)
    finite = load_json(FINITE_THETA)
    zero_sum = load_json(ZERO_SUM)
    trivial_tail = load_json(TRIVIAL_TAIL)

    gate_active = skeleton.get("next_direct_attack_target") == TARGET
    arithmetic_closed = HIGH_MARGIN > 0 and MIDDLE_MARGIN > 0 and X_FINITE_TABLE < X_HIGH_THRESHOLD
    local_bridge_ready = finite.get("finite_theta_bridge_below_20000_self_contained_closed") is True
    finite_bridge_too_short = local_bridge_ready and X_LOCAL_BRIDGE < X_FINITE_TABLE
    psi_contour_components_ready = (
        zero_sum.get("zero_sum_contour_budget_self_contained_closed") is True
        and trivial_tail.get("trivial_tail_prime_power_budget_self_contained_closed") is True
    )

    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            skeleton.get("counterexample_assumption_only") is True
            and skeleton.get("row_column_unconditional_closed") is False,
            True,
            "本步只压缩假设反例链所需解析输入，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "DusartAnalyticKernelGateActive",
            gate_active,
            True,
            "上一证书把下一最窄点设为 Dusart theta/PNT 的解析核与阈值。",
            TARGET,
        ),
        row(
            ARITH_SPLICE,
            arithmetic_closed,
            True,
            "Dusart P5.1 的高尾和中间带数值拼接余量为正；中间带余量很薄但严格为正。",
            "只关闭拼接算术，不关闭输入表和外部定理证明。",
        ),
        row(
            "HighTailThresholdArithmeticClosed",
            HIGH_MARGIN > 0,
            True,
            "若有 psi 相对误差 eps_28<=0.00002224，则 x>=e^28 自动给 theta(x)-x<x/36260。",
            PSI_EPS,
        ),
        row(
            "MiddleStripArithmeticClosed",
            MIDDLE_MARGIN > 0,
            True,
            "若有 psi 上界 0.00002841 与 psi-theta>0.9999 sqrt(x)，则 8e11<=x<=e^28 接上。",
            f"{PSI_EPS} AND {PSI_THETA_GAP}",
        ),
        row(
            "ExistingFiniteThetaBridgeTooShortForDusartP51",
            finite_bridge_too_short,
            True,
            "仓库已自足关闭 x<=20000 的 theta 桥，但 Dusart P5.1 的有限表接口要求 theta(x)<x 到 8e11。",
            THETA_TABLE,
        ),
        row(
            "PsiContourCoarseComponentsReadyButNotSharpEnough",
            psi_contour_components_ready,
            True,
            "Perron 常数、高高度零点和、平凡尾项已自足化；它们还没有给出 Dusart 表级 psi 误差。",
            PSI_EPS,
        ),
        row(
            TARGET,
            False,
            False,
            "解析核与阈值尚未闭合：关键 psi 误差表、psi-theta 下界、8e11 有限 theta 表仍需作者侧证明或可复现证书。",
            f"{PSI_EPS} AND {PSI_THETA_GAP} AND {THETA_TABLE}",
        ),
        row(
            "MiddleRangeFiniteVerificationStillOpen",
            False,
            False,
            "原来的 20000<x<X_A 中段现在被精确压成 20000<x<8e11 的 theta 有限表和 8e11<=x<=e^28 的解析拼接。",
            f"{THETA_TABLE} AND {PSI_EPS} AND {PSI_THETA_GAP}",
        ),
        row(
            "LowHeightAuditStillOpen",
            False,
            False,
            "psi 误差表若走零点路线，仍要低高度 Turing/无零证书支撑。",
            LOW_HEIGHT,
        ),
        row(
            "DirectInternalDusartThetaPNTEnvelopeClosed",
            False,
            False,
            "本步闭合的是拼接结构，不是完整内部 Dusart 定理。",
            f"{TARGET} AND {MIDDLE} AND {LOW_HEIGHT}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "解析拼接压缩不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_dusart_analytic_kernel_threshold_router",
        "status": "dusart_analytic_kernel_threshold_arithmetic_splice_closed_inputs_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dusart_analytic_kernel_threshold_arithmetic_splice_closed": arithmetic_closed,
        "analytic_kernel_and_threshold_closed": False,
        "direct_internal_dusart_theta_pnt_envelope_closed": False,
        "middle_range_finite_verification_closed": False,
        "finite_low_height_self_contained_closed": False,
        "self_contained_mertens_tail_closed": False,
        "b3_tv_strict_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "target_statement_for_internalization": "vartheta(x)-x < x/36260 for x>0",
        "external_reference": {
            "id": ARXIV_ID,
            "url": ARXIV_URL,
            "role": "source boundary for the Dusart Proposition 5.1 proof structure only",
        },
        "arithmetic_checks": arithmetic_rows(),
        "replacement_self_contained": {
            TARGET: f"{ARITH_SPLICE} AND {PSI_EPS} AND {PSI_THETA_GAP} AND {THETA_TABLE}",
            MIDDLE: f"{THETA_TABLE} AND {PSI_EPS} AND {PSI_THETA_GAP}",
        },
        "next_direct_attack_target": PSI_EPS,
        "parallel_attack_targets": [PSI_THETA_GAP, THETA_TABLE, LOW_HEIGHT],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "Dusart P5.1 的解析核与阈值已经被压成严格拼接结构：高尾 `x>=e^28` 只需 "
            "`eps_psi(28)<=0.00002224`；中间带 `8e11<=x<=e^28` 由 "
            "`0.00002841-0.9999e^-14<1/36260` 接上；而 `x<8e11` 需要 theta 有限表。"
            "本步关闭拼接算术，但不关闭 psi 误差表、psi-theta 下界、8e11 有限表和低高度证书。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict Dusart 解析核与阈值拼接路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"dusart_analytic_kernel_threshold_arithmetic_splice_closed={fmt_bool(result['dusart_analytic_kernel_threshold_arithmetic_splice_closed'])}",
        f"analytic_kernel_and_threshold_closed={fmt_bool(result['analytic_kernel_and_threshold_closed'])}",
        f"direct_internal_dusart_theta_pnt_envelope_closed={fmt_bool(result['direct_internal_dusart_theta_pnt_envelope_closed'])}",
        f"middle_range_finite_verification_closed={fmt_bool(result['middle_range_finite_verification_closed'])}",
        f"finite_low_height_self_contained_closed={fmt_bool(result['finite_low_height_self_contained_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 外部边界",
        "",
        f"- 外部来源：`{result['external_reference']['id']}`",
        f"- 链接：{result['external_reference']['url']}",
        f"- 角色：{result['external_reference']['role']}",
        "",
        "## 2. 拼接算术",
        "",
        "| check | formula | value | margin |",
        "| --- | --- | ---: | ---: |",
    ]
    for item in result["arithmetic_checks"]:
        lines.append(
            f"| {table_cell(item['check'])} | `{table_cell(item['formula'])}` | "
            f"`{table_cell(item['value'])}` | `{table_cell(item['margin'])}` |"
        )
    lines.extend(["", "## 3. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 4. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
            "## 5. 下一最窄点",
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
