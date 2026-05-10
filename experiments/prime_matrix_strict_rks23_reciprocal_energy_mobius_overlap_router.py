#!/usr/bin/env python3
"""把倒数区间固定幂能量核心改写为一参数 Möbius 重叠谱。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_reciprocal_energy_mobius_overlap_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"
ENERGY_CORE = MONO / "prime-matrix-strict-rks23-weighted-energy-to-unweighted-core-router.json"
P0_STATUS = DOCS / "explicit-p0-constants.status.md"

SOURCE_FILES = [PREVIOUS, ENERGY_CORE, P0_STATUS]

TARGET = "UnweightedReciprocalIntervalAdditiveEnergyFixedPowerSavingForBalancedRKS23"
NEXT_ATOM = "OneParameterMobiusIntervalOverlapDyadicSpectrumPowerSaving"
INCIDENCE_ROUTE = "RudnevRNRSReciprocalIntervalEnergyEstimateWithExplicitLogSaving"


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


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


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本包含全部关键片段。"""
    return all(item in text for item in needles)


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
    """构造 Möbius 重叠谱证书。"""
    previous = load_json(PREVIOUS)
    energy_core = load_json(ENERGY_CORE)
    p0_status = read_text(P0_STATUS)

    active = previous.get("next_direct_attack_target") == TARGET
    power_relaxation_closed = previous.get("fixed_power_saving_implies_required_log_saving") is True
    unweighted_core_present = energy_core.get("divisor_weighted_to_unweighted_reduction_closed") is True
    incidence_route_known = contains_all(p0_status, ["Rudnev", "sum-product", "能量"])

    # 恒等式：对 s in F_P，r_J(s)=#{(a,b) in J^2: a^{-1}+b^{-1}=s}。
    # 解出 b=a/(s a-1)，其中 s a=1 时无解；因此 r_J(s)=|J∩phi_s^{-1}(J)|。
    # 于是 E_+(J^{-1})=sum_s r_J(s)^2，完全等价于一参数 PGL2 重叠谱。
    mobius_identity_closed = active and power_relaxation_closed and unweighted_core_present
    overlap_spectrum_power_saving_proved = False

    mobius_reduction = {
        "pair_count": "r_J(s)=#{(a,b) in J^2: a^(-1)+b^(-1)=s}",
        "mobius_map": "phi_s(a)=a/(s*a-1), with s*a=1 giving no solution",
        "overlap_identity": "r_J(s)=#{a in J: phi_s(a) in J}",
        "energy_identity": "E_+(J^(-1))=sum_s r_J(s)^2",
        "dyadic_spectrum": "Omega_tau={s: tau<=r_J(s)<2tau}",
        "sufficient_spectrum_bound": "for some delta>0, sum_tau |Omega_tau| tau^2 <= |J|^(3-delta)",
        "structural_reading": "many additive-energy quadruples mean many one-parameter Mobius maps repeatedly send J back into J",
        "next_attack_shape": "prove interval-overlap power saving for the non-affine family a -> a/(s*a-1)",
    }

    rows = [
        row(
            "FixedPowerEnergyTargetActive",
            active,
            True,
            "上一证书已把对数能量目标放松为固定幂节省能量目标。",
            TARGET,
        ),
        row(
            "MobiusOverlapIdentityClosed",
            mobius_identity_closed,
            True,
            "`a^{-1}+b^{-1}=s` 等价于 `b=a/(sa-1)`，能量等于 Möbius 重叠平方和。",
            NEXT_ATOM,
        ),
        row(
            "DyadicSpectrumCriterionClosed",
            mobius_identity_closed,
            True,
            "固定幂能量节省等价于 dyadic overlap spectrum 的平方加权和节省。",
            NEXT_ATOM,
        ),
        row(
            "IncidenceRouteStillMatches",
            incidence_route_known,
            True,
            "Rudnev/RNRS incidence 可以视作该 Möbius 图族的高重叠谱控制工具。",
            INCIDENCE_ROUTE,
        ),
        row(
            NEXT_ATOM,
            overlap_spectrum_power_saving_proved,
            False,
            "仓库内尚未证明一参数非仿射 Möbius 图族对区间的 dyadic overlap spectrum 有固定幂节省。",
            INCIDENCE_ROUTE,
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步闭合的是能量到 Möbius 重叠谱的等价改写，不是谱估计本身。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_reciprocal_energy_mobius_overlap_router",
        "status": "reciprocal_interval_energy_rewritten_as_one_parameter_mobius_overlap_spectrum",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "fixed_power_energy_target_active": active,
        "mobius_overlap_identity_closed": mobius_identity_closed,
        "dyadic_spectrum_criterion_closed": mobius_identity_closed,
        "incidence_route_still_matches": incidence_route_known,
        "mobius_overlap_spectrum_power_saving_proved": overlap_spectrum_power_saving_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_incidence_target": INCIDENCE_ROUTE,
        "mobius_reduction": mobius_reduction,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "固定幂能量核心已改写成完全等价的一参数 Möbius 重叠谱问题："
            "对每个和相位 `s`，解 `a^{-1}+b^{-1}=s` 得到 `b=a/(sa-1)`，"
            "因此 `E_+(J^{-1})=Σ_s |{a∈J: a/(sa-1)∈J}|^2`。"
            "下一真正最窄输入不是泛泛四元组能量，而是证明这些非仿射 Möbius 图不能在同一区间上形成高重叠 dyadic spectrum。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    reduction = result["mobius_reduction"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 倒数能量 Möbius 重叠谱证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"mobius_overlap_identity_closed={fmt_bool(result['mobius_overlap_identity_closed'])}",
        f"dyadic_spectrum_criterion_closed={fmt_bool(result['dyadic_spectrum_criterion_closed'])}",
        f"mobius_overlap_spectrum_power_saving_proved={fmt_bool(result['mobius_overlap_spectrum_power_saving_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. Möbius 重叠等价式",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in reduction.items():
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
