#!/usr/bin/env python3
"""把三短二次 Fourier 包压成 Plancherel 边界后的相关节省输入。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_tri_quadratic_plancherel_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-tri-quadratic-plancherel-barrier-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-tri-quadratic-plancherel-barrier-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-tri-quadratic-plancherel-barrier-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-tri-quadratic-fourier-factorization-router.json"
SOURCE_FILES = [PREVIOUS]

TARGET = "TriShortQuadraticFourierCorrelationPowerSaving"
NEXT_ATOM = "CorrelatedQuadraticFourierEnergyOverlapPowerSaving"
ALT_ATOM = "BeyondPlancherelSlopeOverlapQuadraticEnergySaving"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_result() -> dict[str, Any]:
    """构造 Plancherel 边界证书。"""
    previous = load_json(PREVIOUS)
    active = previous.get("next_direct_attack_target") == TARGET
    factorized = previous.get("tri_quadratic_factorization_closed") is True

    # 三因子包：
    # Dev=(1/P) sum_{r!=0} A(-r) sum_{lambda!=1} A(r lambda) B_lambda(r lambda(lambda-1)).
    # 对固定 lambda 用 Cauchy，再对 B_lambda 用 Plancherel：
    #   contribution_lambda <= P^{-1/2} sqrt(M_A(lambda) L(lambda))
    # 其中 M_A(lambda)=sum_r |A(r)|^2 |A(r lambda)|^2，L(lambda)=|X_lambda|。
    cauchy_plancherel_closed = active and factorized
    natural_barrier_quantified = active and factorized

    barrier = {
        "quadratic_sum": "A(s)=sum_{d in Delta} e_P(s*d^2)",
        "slope_overlap": "L(lambda)=|X_lambda| with X_lambda=T cap lambda^(-1)T",
        "energy_autocorrelation": "M_A(lambda)=sum_{r!=0}|A(r)|^2|A(r*lambda)|^2",
        "per_slope_cauchy": "|packet_lambda|/P <= P^(-1/2)*sqrt(M_A(lambda)*L(lambda))",
        "plancherel_inputs": "sum_s |A(s)|^2 <= 2P|Delta| and sum_h |B_lambda(h)|^2 <= 2P L(lambda)",
        "global_l2_sums": "sum_lambda M_A(lambda) <= (sum_s |A(s)|^2)^2 and sum_lambda L(lambda)=|T|^2",
        "natural_bound": "|Dev| <= P^(1/2) N^2 = N^3 log^O(P) in the square-root collar",
        "barrier": "Cauchy/Plancherel reaches the natural cubic scale but gives no fixed power saving",
        "needed_saving": "sum_lambda sqrt(M_A(lambda)L(lambda)) <= P*N^2*N^(-delta) for some fixed delta>0",
    }

    rows = [
        row(
            "TriQuadraticFourierTargetActive",
            active,
            True,
            "上一证书已把剩余压成三短二次 Fourier 相关包。",
            TARGET,
        ),
        row(
            "PerSlopeCauchyPlancherelEnvelopeClosed",
            cauchy_plancherel_closed,
            True,
            "对固定斜率，Cauchy 与 Plancherel 给出 `P^{-1/2}sqrt(M_A(lambda)L(lambda))` 包络。",
            NEXT_ATOM,
        ),
        row(
            "NaturalScaleBarrierQuantified",
            natural_barrier_quantified,
            True,
            "全局 L2 只能推出 `N^3 log^O(P)` 自然尺度，不能给固定幂节省。",
            NEXT_ATOM,
        ),
        row(
            "PlainPlancherelRouteInsufficient",
            natural_barrier_quantified,
            True,
            "若不证明 `M_A(lambda)` 与 `L(lambda)` 的相关节省，链条不能闭合。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "仓库内尚未证明二次 Fourier 能量自相关与斜率重叠之间有固定幂相关节省。",
            ALT_ATOM,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只定位 Plancherel 后的唯一缺口，未证明相关节省。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_tri_quadratic_plancherel_barrier_router",
        "status": "tri_quadratic_fourier_packet_reduced_to_correlated_energy_overlap_saving_beyond_plancherel",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "tri_quadratic_fourier_target_active": active,
        "per_slope_cauchy_plancherel_envelope_closed": cauchy_plancherel_closed,
        "natural_scale_barrier_quantified": natural_barrier_quantified,
        "plain_plancherel_route_insufficient": natural_barrier_quantified,
        "correlated_energy_overlap_power_saving_proved": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "alternate_name_for_same_atom": ALT_ATOM,
        "barrier": barrier,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "三短二次 Fourier 包经固定斜率 Cauchy/Plancherel 后，精确压成 "
            "`sum_lambda sqrt(M_A(lambda)L(lambda))` 的相关节省问题。"
            "这里 `M_A(lambda)` 是短二次和 `A` 的乘法自相关能量，`L(lambda)` 是根盒斜率重叠。"
            "普通 Plancherel 只给 `|Dev|<=P^(1/2)N^2=N^3 log^O(P)`，"
            "正好卡在自然三次尺度，不能给固定幂节省。"
            "因此当前唯一剩余是证明 `M_A(lambda)` 不能集中在大重叠斜率上。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    barrier = result["barrier"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 三短二次 Plancherel 边界证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"per_slope_cauchy_plancherel_envelope_closed={fmt_bool(result['per_slope_cauchy_plancherel_envelope_closed'])}",
        f"natural_scale_barrier_quantified={fmt_bool(result['natural_scale_barrier_quantified'])}",
        f"correlated_energy_overlap_power_saving_proved={fmt_bool(result['correlated_energy_overlap_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Plancherel 后剩余",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in barrier.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 判定表",
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
            "## 3. 下一最窄自足目标",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """写出 JSON 与 Markdown。"""
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_direct_attack_target={result['next_direct_attack_target']}")


if __name__ == "__main__":
    main()
