#!/usr/bin/env python3
"""生成 strict psi 误差表内化压力路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_psi_epsilon_table_internalization_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-psi-epsilon-table-internalization-router.json
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "docs" / "monograph"

OUT_JSON = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-internalization-router.json"
OUT_MD = MONOGRAPH / "prime-matrix-strict-psi-epsilon-table-internalization-router.md"

DUSART_ANALYTIC = MONOGRAPH / "prime-matrix-strict-dusart-analytic-kernel-threshold-router.json"
UNSMOOTHED_PERRON = MONOGRAPH / "prime-matrix-strict-unsmoothed-perron-final-sync-router.json"
ZERO_SUM = MONOGRAPH / "prime-matrix-strict-zero-sum-contour-self-contained-sync-router.json"
TRIVIAL_TAIL = MONOGRAPH / "prime-matrix-strict-trivial-tail-prime-power-self-contained-sync-router.json"
CLAIM_STATUS = MONOGRAPH / "claim-status-table.md"

SOURCE_FILES = [DUSART_ANALYTIC, UNSMOOTHED_PERRON, ZERO_SUM, TRIVIAL_TAIL, CLAIM_STATUS]

TARGET = "PsiRelativeErrorTableEpsilon28AndMiddle2841SelfContainedLedger"
HIGH_TAIL = "PsiEpsilonHighTailB28SelfContainedLedger"
MIDDLE_STRIP = "PsiUpperMiddle8e11ToE28SelfContainedLedger"
EPS_SOURCE = "SchoenfeldDusartPsiEpsilonTableInternalizationLedger"
ZERO_VERIFICATION = "CriticalLineAndStripVerifiedZeroInputForPsiEpsilonTableLedger"
SHARP_CONTOUR = "SharpVerifiedZeroPsiContourEnvelopeLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

ARXIV_URL = "https://arxiv.org/abs/1002.0442"

EPS_HIGH = 0.00002224
EPS_MIDDLE = 0.00002841
X_HIGH = math.exp(28)
X_MIDDLE_LEFT = 8.0e11
C_ZERO_SUM = 65536.0
C_REGION = 1280.0
T0 = 14.0


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


def current_zero_free_relative(x: float) -> float:
    """复用当前 C=1280,C_Z=65536 模板，估计 psi 相对包络。"""
    return C_ZERO_SUM * math.log(x * (T0 + 3.0)) ** 2 * math.exp(
        -math.log(x) / (C_REGION * math.log(T0 + 3.0))
    )


def pressure_rows() -> list[dict[str, Any]]:
    """生成 psi 误差表目标与当前模板差距。"""
    high_rel = current_zero_free_relative(X_HIGH)
    middle_rel = current_zero_free_relative(X_MIDDLE_LEFT)
    return [
        {
            "site": "high tail b=28",
            "x": X_HIGH,
            "needed_relative": EPS_HIGH,
            "current_relative": high_rel,
            "gap_factor": high_rel / EPS_HIGH,
            "beats": high_rel <= EPS_HIGH,
        },
        {
            "site": "middle left 8e11",
            "x": X_MIDDLE_LEFT,
            "needed_relative": EPS_MIDDLE,
            "current_relative": middle_rel,
            "gap_factor": middle_rel / EPS_MIDDLE,
            "beats": middle_rel <= EPS_MIDDLE,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 psi 误差表内化压力证书。"""
    analytic = load_json(DUSART_ANALYTIC)
    perron = load_json(UNSMOOTHED_PERRON)
    zero_sum = load_json(ZERO_SUM)
    trivial_tail = load_json(TRIVIAL_TAIL)
    active = analytic.get("next_direct_attack_target") == TARGET
    current_components_ready = (
        perron.get("unsmoothed_perron_strict_self_contained_closed") is True
        and zero_sum.get("zero_sum_contour_budget_self_contained_closed") is True
        and trivial_tail.get("trivial_tail_prime_power_budget_self_contained_closed") is True
    )
    pressure = pressure_rows()
    current_template_beats_targets = all(item["beats"] for item in pressure)
    rows = [
        row(
            "CounterexampleBranchGuardPreserved",
            analytic.get("counterexample_assumption_only") is True
            and analytic.get("row_column_unconditional_closed") is False,
            True,
            "本步只审查解析输入表，不使用真实零行缺席。",
            "保持 direct_unconditional_contradiction_found=false 与 row_column_unconditional_closed=false。",
        ),
        row(
            "PsiEpsilonTableGateActive",
            active,
            True,
            "Dusart 解析拼接证书已把下一最窄点压到 psi 显式误差表。",
            TARGET,
        ),
        row(
            "CurrentStrictPerronZeroSumTailComponentsReady",
            current_components_ready,
            True,
            "非平滑 Perron 常数、高高度零点和、平凡/素数幂尾项已经 strict 自足同步。",
            "这些只是粗模板组件，不等于 Dusart 误差表。",
        ),
        row(
            "CurrentC1280C65536TemplateBeatsPsiEpsilonTargets",
            current_template_beats_targets,
            False,
            "当前 C=1280,C_Z=65536 模板在 e^28 和 8e11 处均比目标大约 10^12 倍，不能推出 psi 表。",
            f"{EPS_SOURCE} OR {SHARP_CONTOUR}",
        ),
        row(
            HIGH_TAIL,
            False,
            False,
            "需要证明对所有 x>=e^28 有 |psi(x)-x|/x<=0.00002224 或足够的单侧上界。",
            EPS_SOURCE,
        ),
        row(
            MIDDLE_STRIP,
            False,
            False,
            "需要证明 8e11<=x<=e^28 上 psi(x)<1.00002841x。",
            EPS_SOURCE,
        ),
        row(
            TARGET,
            False,
            False,
            "psi 误差表尚未自足内化；必须引入可复算的 Schoenfeld/Dusart 表证明或更尖锐的 verified-zero contour。",
            f"{HIGH_TAIL} AND {MIDDLE_STRIP} AND {ZERO_VERIFICATION}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "psi 表压力审查不产生早期零行反例链与真实结构链的终端矛盾。",
            DSTRUCTURE,
        ),
    ]
    return {
        "certificate_type": "prime_matrix_strict_psi_epsilon_table_internalization_router",
        "status": "psi_epsilon_table_internalization_reduced_to_verified_zero_or_schoenfeld_dusart_table_proof",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "psi_epsilon_table_self_contained_closed": False,
        "current_strict_perron_zero_sum_tail_components_ready": current_components_ready,
        "current_c1280_c65536_template_beats_psi_epsilon_targets": current_template_beats_targets,
        "direct_internal_dusart_theta_pnt_envelope_closed": False,
        "analytic_kernel_and_threshold_closed": False,
        "middle_range_finite_verification_closed": False,
        "finite_low_height_self_contained_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "pressure_rows": pressure,
        "external_reference": {
            "id": "Dusart arXiv:1002.0442",
            "url": ARXIV_URL,
            "role": "source of the epsilon_psi values being internalized, not a self-contained proof",
        },
        "replacement_self_contained": {
            TARGET: f"{HIGH_TAIL} AND {MIDDLE_STRIP} AND {ZERO_VERIFICATION}",
            HIGH_TAIL: EPS_SOURCE,
            MIDDLE_STRIP: EPS_SOURCE,
            EPS_SOURCE: f"{SHARP_CONTOUR} AND {ZERO_VERIFICATION}",
        },
        "next_direct_attack_target": HIGH_TAIL,
        "parallel_attack_targets": [MIDDLE_STRIP, ZERO_VERIFICATION, SHARP_CONTOUR],
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "psi 误差表不能由当前 C=1280,C_Z=65536 的粗自足 contour 推出：在 `x=e^28` 处，"
            "当前相对包络约为目标 `0.00002224` 的 `2.78e12` 倍；在 `8e11` 处约为目标 "
            "`0.00002841` 的 `2.09e12` 倍。因此本步把最窄缺口压成 `PsiEpsilonHighTailB28`、"
            "`PsiUpperMiddle8e11ToE28` 与 verified-zero/Turing 输入，而不宣布 Dusart 内部化闭合。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict psi 误差表内化压力路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"psi_epsilon_table_self_contained_closed={fmt_bool(result['psi_epsilon_table_self_contained_closed'])}",
        f"current_strict_perron_zero_sum_tail_components_ready={fmt_bool(result['current_strict_perron_zero_sum_tail_components_ready'])}",
        f"current_c1280_c65536_template_beats_psi_epsilon_targets={fmt_bool(result['current_c1280_c65536_template_beats_psi_epsilon_targets'])}",
        f"direct_internal_dusart_theta_pnt_envelope_closed={fmt_bool(result['direct_internal_dusart_theta_pnt_envelope_closed'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 压力诊断",
        "",
        "| site | x | needed relative | current relative | gap factor | beats |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in result["pressure_rows"]:
        lines.append(
            f"| {table_cell(item['site'])} | `{item['x']:.12e}` | `{item['needed_relative']:.12e}` | "
            f"`{item['current_relative']:.12e}` | `{item['gap_factor']:.12e}` | `{fmt_bool(item['beats'])}` |"
        )
    lines.extend(["", "## 2. 自足替换", "", "```text"])
    for key, value in result["replacement_self_contained"].items():
        lines.extend([key, "  =>", value, ""])
    lines.extend(["```", "", "## 3. 判定表", "", "| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"])
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
