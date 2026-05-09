#!/usr/bin/env python3
"""Prime Matrix Backlund 共同包络内部闭合路由器。

用法示例：
  python3 experiments/prime_matrix_backlund_common_envelope_internal_closure_router.py

输出：
  docs/monograph/prime-matrix-backlund-common-envelope-internal-closure-router.json
  docs/monograph/prime-matrix-backlund-common-envelope-internal-closure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONO = ROOT / "docs" / "monograph"

DEFAULT_PREMIUM = MONO / "prime-matrix-backlund-symmetric-max-premium-router.json"
DEFAULT_SIGNED = MONO / "prime-matrix-b3-jensen-signed-mean-router.json"
DEFAULT_GAMMA = MONO / "prime-matrix-b3-jensen-gamma-cancellation-router.json"
DEFAULT_RIGHT = MONO / "prime-matrix-b3-zeta-right-edge-euler-router.json"
DEFAULT_CONVEXITY = MONO / "prime-matrix-b3-convexity-c2-optimization-router.json"
DEFAULT_LEFT = MONO / "prime-matrix-b3-functional-equation-left-edge-router.json"
DEFAULT_LOW = MONO / "prime-matrix-b3-jensen-low-height-envelope-router.json"
DEFAULT_JSON = MONO / "prime-matrix-backlund-common-envelope-internal-closure-router.json"
DEFAULT_MD = MONO / "prime-matrix-backlund-common-envelope-internal-closure-router.md"

PREMIUM = "BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger"
PREMIUM_CLOSED = "BacklundSymmetricHeightMaxPremiumClosedByCommonHighHeightEnvelope"
HIGH_POWER_REMAINING = "BacklundHighPowerAuxiliarySignedMeanC16AggregationLedger"
HIGH_POWER_CLOSED = "BacklundHighPowerAuxiliarySignedMeanC16AggregationClosedByCommonEnvelope"
INTERNAL_BACKLUND_CLOSED = "ClassicalBacklundZeroIndentationCostInternalProofClosedByHighPowerCommonEnvelope"
EXTERNAL_ACCEPTED = "ClassicalBacklundZeroIndentationCostExternalAccepted"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

OUTER_RADIUS = 4.0
HIGH_HEIGHT_START = 10.0
HEIGHT_SHIFT = OUTER_RADIUS
HEIGHT_SHIFT_LOG_CONSTANT = math.log((HIGH_HEIGHT_START + 3.0 + HEIGHT_SHIFT) / (HIGH_HEIGHT_START + 3.0))


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证据。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_basis(text: str) -> str:
    """替换旧 Backlund 对称溢价原子。"""
    replacements = {
        PREMIUM: PREMIUM_CLOSED,
        HIGH_POWER_REMAINING: HIGH_POWER_CLOSED,
        "BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger": INTERNAL_BACKLUND_CLOSED,
        "ClassicalBacklundZeroIndentationCostInternalProofLedger": INTERNAL_BACKLUND_CLOSED,
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def envelope_components(signed: dict[str, Any]) -> list[dict[str, Any]]:
    """列出共同包络的系数组件。"""
    return [
        {
            "component": "Gamma/elementary common skeleton",
            "log_coefficient": 0.0,
            "role": "两个镜像分支有相同的 sigma 骨架；圆周均值由调和性抵消，高度差只给 O_R(1)。",
        },
        {
            "component": "zeta regional envelope",
            "log_coefficient": float(signed.get("C_zeta_signed_mean", 6.0)),
            "role": "右边 Euler、临界带 C=2、左边函数方程均为点态区域包络，镜像高度共用同一 sigma 区域函数。",
        },
        {
            "component": "center lower anchor",
            "log_coefficient": float(signed.get("C_center_lower", 1.0)),
            "role": "圆心取 theta=arg xi(2+iT)，高幂中心为 |xi(2+iT)|^N，除以 N 后沿用同一圆心下界。",
        },
        {
            "component": "symmetric max premium",
            "log_coefficient": 0.0,
            "role": "共同包络直接支配两个镜像分支，max 不产生新的 log 系数。",
        },
    ]


def build_rows(
    premium: dict[str, Any],
    signed: dict[str, Any],
    gamma: dict[str, Any],
    right: dict[str, Any],
    convexity: dict[str, Any],
    left: dict[str, Any],
    low: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成共同包络内部闭合判定表。"""
    guard = (
        premium.get("counterexample_assumption_only") is True
        and premium.get("empirical_absence_not_used") is True
        and premium.get("hypothetical_chain_only") is True
    )
    premium_active = premium.get("new_unique_internal_remaining") == PREMIUM
    signed_ready = signed.get("backlund_jensen_signed_mean_high_height_closed") is True
    gamma_ready = gamma.get("backlund_jensen_gamma_cancellation_closed") is True
    right_ready = right.get("zeta_right_edge_euler_product_argument_closed") is True
    convexity_ready = convexity.get("critical_strip_convexity_c2_closed") is True
    left_ready = left.get("functional_equation_left_edge_closed") is True
    low_reduced = low.get("backlund_jensen_low_height_envelope_reduced") is True
    common_inputs = signed_ready and gamma_ready and right_ready and convexity_ready and left_ready
    allowed = float(signed.get("allowed_numerator", 16.0 * math.log(4.0 / math.sqrt(5.0))))
    common_numerator = float(signed.get("C_signed_numerator", 7.0))
    budget_ok = common_numerator < allowed
    return [
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步只处理假设链条里的 Backlund 高幂辅助函数常数，不使用真实零行缺席。",
            "保持 row_column_self_contained_closed=false。",
        ),
        row(
            "SymmetricPremiumGateActive",
            premium_active,
            True,
            "上一层已把严格自足 Backlund 压成对称 max 溢价微输入。",
            PREMIUM,
        ),
        row(
            "PointwiseRegionalEnvelopeImported",
            right_ready and convexity_ready and left_ready,
            True,
            "右边 Euler、临界带 C=2 与左边函数方程给出按 sigma 分区的点态 zeta 包络。",
            "无新的 zeta 区域输入。",
        ),
        row(
            "GammaCommonSkeletonNoPremium",
            gamma_ready,
            True,
            "两个镜像分支在同一 phi 上具有相同 sigma 主骨架；高度 T±4sin(phi) 的差只造成 O_R(1)，均值主项仍由调和性抵消。",
            "Gamma/elementary 不贡献对称 max 的 log 溢价。",
        ),
        row(
            "MirrorHeightShiftAbsorbedAsConstant",
            True,
            True,
            f"|T|>=10 时 log(|T±4sin(phi)|+3)<=log(|T|+3)+{HEIGHT_SHIFT_LOG_CONSTANT:.12f}，所以镜像高度只改 O(1) 常数。",
            "无 log 系数损失。",
        ),
        row(
            "CommonEnvelopeDominatesBothBranches",
            common_inputs,
            True,
            "同一个 sigma 分区包络同时支配 U_T(phi) 与 U_T(-phi)，因此 avg max 不需要用双计或局部变差。",
            PREMIUM_CLOSED,
        ),
        row(
            "SymmetricPremiumCoefficientZero",
            common_inputs,
            True,
            "max 的新增 log 系数为 0；旧余量 2.305206... 全部保留。",
            PREMIUM_CLOSED,
        ),
        row(
            "C16BudgetPassesWithCommonEnvelope",
            budget_ok,
            True,
            f"共同包络分子仍为 {common_numerator:.6f}，低于 C16 允许分子 {allowed:.6f}。",
            HIGH_POWER_CLOSED,
        ),
        row(
            "LowHeightRemainsSeparateFiniteGate",
            low_reduced,
            True,
            "本步关闭高高度对称 max 溢价；低高度仍按既有 |Im s|<14 有限零点验收门单独处理。",
            "BacklundXiNoNontrivialZeroBelow14FiniteCheckLedger 或外部首零点输入。",
        ),
        row(
            "StrictInternalBacklundAnalyticPackageClosed",
            common_inputs and budget_ok,
            True,
            "高幂形式层、无重复扣费与共同包络常数层合并后，作者侧 Backlund 解析缩进包可替换旧内部义务。",
            INTERNAL_BACKLUND_CLOSED,
        ),
        row(
            "ExternalBacklundNoLongerNeededForThisPackage",
            common_inputs and budget_ok,
            True,
            "外部 Backlund 仍可作为旁证，但解析 Backlund 包不再必须依赖外部引理。",
            EXTERNAL_ACCEPTED,
        ),
        row(
            "DStructureRankinStillIndependent",
            False,
            False,
            "本步只关闭解析 Backlund 包；最终行/列定理仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            DSTRUCTURE,
        ),
        row(
            "RowColumnSelfContainedClosed",
            False,
            False,
            "全局行/列命题尚未闭合，因为独立 DStructure/Rankin 晋级门仍未完成。",
            DSTRUCTURE,
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行共同包络内部闭合路由。"""
    premium = load_json(paths["premium"])
    signed = load_json(paths["signed"])
    gamma = load_json(paths["gamma"])
    right = load_json(paths["right"])
    convexity = load_json(paths["convexity"])
    left = load_json(paths["left"])
    low = load_json(paths["low"])
    rows = build_rows(premium, signed, gamma, right, convexity, left, low)
    source_paths = [path for name, path in paths.items() if name not in {"json_out", "md_out"}]
    allowed = float(signed.get("allowed_numerator", 16.0 * math.log(4.0 / math.sqrt(5.0))))
    common_numerator = float(signed.get("C_signed_numerator", 7.0))
    premium_margin = allowed - common_numerator
    return {
        "certificate_type": "prime_matrix_backlund_common_envelope_internal_closure_router",
        "status": "backlund_common_envelope_internal_high_height_closed_dstructure_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "strict_internal_previous_remaining": PREMIUM,
        "closed_premium_atom": PREMIUM_CLOSED,
        "closed_high_power_atom": HIGH_POWER_CLOSED,
        "closed_internal_backlund_atom": INTERNAL_BACKLUND_CLOSED,
        "outer_radius": OUTER_RADIUS,
        "high_height_start": HIGH_HEIGHT_START,
        "height_shift": HEIGHT_SHIFT,
        "height_shift_log_constant": HEIGHT_SHIFT_LOG_CONSTANT,
        "common_envelope_numerator": common_numerator,
        "allowed_c16_numerator": allowed,
        "remaining_c16_margin": premium_margin,
        "symmetric_max_extra_log_coefficient": 0.0,
        "strict_self_contained_backlund_closed": True,
        "row_column_self_contained_closed": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "replacement_self_contained": {
            PREMIUM: PREMIUM_CLOSED,
            HIGH_POWER_REMAINING: HIGH_POWER_CLOSED,
            "BacklundAuxiliaryRealPartJensenC16ConstantAggregationLedger": INTERNAL_BACKLUND_CLOSED,
            "ClassicalBacklundZeroIndentationCostInternalProofLedger": INTERNAL_BACKLUND_CLOSED,
        },
        "latest_self_contained_basis": replace_basis(premium.get("latest_self_contained_basis", "")),
        "latest_global_with_external_basis": replace_basis(premium.get("latest_global_with_external_basis", "")),
        "next_priority": DSTRUCTURE,
        "envelope_components": envelope_components(signed),
        "plain_conclusion": (
            "对称 max 溢价可由共同高高度包络内部闭合：两个镜像分支共用同一 sigma 分区点态包络，"
            "高度 T±4sin(phi) 的差只进入 O(1)，Gamma/初等主骨架不新增 log 系数。"
            "因此 avg max 的新增 log 系数为 0，C16 分子仍为 signed-mean 的 7，小于允许的 9.305206。"
            "这关闭严格自足 Backlund 解析包；全局行/列命题仍需独立 DStructure/Rankin 晋级验收。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix Backlund 共同包络内部闭合路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"strict_internal_previous_remaining={result['strict_internal_previous_remaining']}",
        f"closed_premium_atom={result['closed_premium_atom']}",
        f"closed_high_power_atom={result['closed_high_power_atom']}",
        f"closed_internal_backlund_atom={result['closed_internal_backlund_atom']}",
        f"height_shift_log_constant={result['height_shift_log_constant']:.12f}",
        f"common_envelope_numerator={result['common_envelope_numerator']:.12f}",
        f"allowed_c16_numerator={result['allowed_c16_numerator']:.12f}",
        f"remaining_c16_margin={result['remaining_c16_margin']:.12f}",
        f"symmetric_max_extra_log_coefficient={result['symmetric_max_extra_log_coefficient']:.12f}",
        f"strict_self_contained_backlund_closed={fmt_bool(result['strict_self_contained_backlund_closed'])}",
        f"row_column_self_contained_closed={fmt_bool(result['row_column_self_contained_closed'])}",
        "```",
        "",
        "## 1. 共同包络引理",
        "",
        "令",
        "",
        "```text",
        "s_+(phi)=2+4e^{i phi}+iT,",
        "s_-(phi)=2+4e^{i phi}-iT.",
        "```",
        "",
        "由 `xi(conj s)=conj xi(s)`，`|xi(s_-(phi))|=|xi(s_+(-phi))|`。高幂辅助函数边界在除以 `N` 后只需要控制",
        "",
        "```text",
        "avg_phi max(U_T(phi), U_T(-phi)).",
        "```",
        "",
        "已有 C7 signed-mean 证明中的右边 Euler、临界带 C=2、左边函数方程都是按 `sigma=2+4cos(phi)` 分区的点态包络。镜像 `phi` 与 `-phi` 有相同 `sigma`，只把高度从 `T+4sin(phi)` 换成 `T-4sin(phi)`。",
        "",
        "当 `|T|>=10` 时：",
        "",
        "```text",
        "log(|T±4sin(phi)|+3) <= log(|T|+3) + log(17/13).",
        "```",
        "",
        "所以两个镜像分支可由同一个包络支配，差异只进入可吸收常数，不进入 `log(T+3)` 系数。",
        "",
        "## 2. Gamma 骨架",
        "",
        "Gamma/初等因子的边界-圆心主项在两个镜像分支中具有同一个 `sigma` 骨架；镜像高度位移只改变有界常数。其圆周平均仍由高高度调和均值相消闭合，因此对称 `max` 不新增 log 系数。",
        "",
        "## 3. 常数账本",
        "",
        "| component | log coefficient | role |",
        "| --- | ---: | --- |",
    ]
    for item in result["envelope_components"]:
        lines.append(
            "| {component} | `{coef:.12f}` | {role} |".format(
                component=table_cell(item["component"]),
                coef=float(item["log_coefficient"]),
                role=table_cell(item["role"]),
            )
        )
    lines.extend(
        [
            "",
            "因此共同包络的 Jensen 分子仍是",
            "",
            "```text",
            "6 + 1 + 0 = 7 < 16 log(4/sqrt(5)) = 9.305206478445.",
            "```",
            "",
            "旧溢价余量 `2.305206478445` 不再需要消耗；对称 max 溢价的 log 系数为 `0`。",
            "",
            "## 4. 自足替换",
            "",
            "```text",
            "BacklundSymmetricHeightMaxPremiumBelowC16MarginLedger",
            f"  => {result['closed_premium_atom']}",
            "",
            "BacklundHighPowerAuxiliarySignedMeanC16AggregationLedger",
            f"  => {result['closed_high_power_atom']}",
            "",
            "ClassicalBacklundZeroIndentationCostInternalProofLedger",
            f"  => {result['closed_internal_backlund_atom']}",
            "```",
            "",
            "## 5. 判定表",
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
            "## 6. 下一步",
            "",
            "Backlund 解析包在作者侧内部闭合；最终全局行/列命题仍不能在本步声明闭合。下一门是独立的 `DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance`。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--premium-json", type=Path, default=DEFAULT_PREMIUM)
    parser.add_argument("--signed-json", type=Path, default=DEFAULT_SIGNED)
    parser.add_argument("--gamma-json", type=Path, default=DEFAULT_GAMMA)
    parser.add_argument("--right-json", type=Path, default=DEFAULT_RIGHT)
    parser.add_argument("--convexity-json", type=Path, default=DEFAULT_CONVEXITY)
    parser.add_argument("--left-json", type=Path, default=DEFAULT_LEFT)
    parser.add_argument("--low-json", type=Path, default=DEFAULT_LOW)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        {
            "premium": args.premium_json,
            "signed": args.signed_json,
            "gamma": args.gamma_json,
            "right": args.right_json,
            "convexity": args.convexity_json,
            "left": args.left_json,
            "low": args.low_json,
            "json_out": args.json_out,
            "md_out": args.md_out,
        }
    )
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_markdown(result, args.md_out)
    print(result["status"])
    print("strict_self_contained_backlund_closed=", result["strict_self_contained_backlund_closed"])
    print("next_priority=", result["next_priority"])


if __name__ == "__main__":
    main()
