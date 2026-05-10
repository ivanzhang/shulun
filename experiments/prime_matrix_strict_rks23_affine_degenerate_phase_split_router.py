#!/usr/bin/env python3
"""分离 RKS2/RKS3 Möbius 高谱中的 s=0 仿射退化相位。

用法示例：
  python3 experiments/prime_matrix_strict_rks23_affine_degenerate_phase_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-rks23-affine-degenerate-phase-split-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-rks23-affine-degenerate-phase-split-router.json"
OUT_MD = MONO / "prime-matrix-strict-rks23-affine-degenerate-phase-split-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-mobius-to-affine-inverse-high-spectrum-router.json"
MOBIUS_FRONTIER = MONO / "prime-matrix-strict-rks23-reciprocal-energy-mobius-overlap-router.json"
POWER_RELAX = MONO / "prime-matrix-strict-rks23-unweighted-energy-power-saving-relaxation-router.json"

SOURCE_FILES = [PREVIOUS, MOBIUS_FRONTIER, POWER_RELAX]

TARGET = "AffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23"
NEXT_ATOM = "NonzeroAffineProgressionInverseSelfIntersectionHighSpectrumPowerSavingForBalancedRKS23"
PGL2_TARGET = "NonzeroPGL2IntervalAlmostStabilizerPowerSavingForMobiusInvolutions"
INCIDENCE_TARGET = "RudnevRNRSAffineProgressionInverseIntersectionIncidenceEstimate"


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
    """构造退化相位拆分证书。"""
    previous = load_json(PREVIOUS)
    mobius = load_json(MOBIUS_FRONTIER)
    power = load_json(POWER_RELAX)

    active = previous.get("next_direct_attack_target") == TARGET
    affine_identity_imported = previous.get("affine_inverse_self_intersection_identity_closed") is True
    low_overlap_imported = previous.get("low_overlap_layer_automatically_absorbed") is True
    mobius_identity_imported = mobius.get("mobius_overlap_identity_closed") is True
    power_relax_imported = power.get("fixed_power_saving_implies_required_log_saving") is True

    # s=0 给 a^{-1}+b^{-1}=0，即 b=-a。该相位可能有 r_0~N，
    # 但只贡献 r_0^2<=N^2。固定幂能量目标只需 E<=N^(3-delta)，
    # 取任意 delta<1 时，这个单相位退化都被吸收。
    degenerate_phase_split_closed = (
        active
        and affine_identity_imported
        and low_overlap_imported
        and mobius_identity_imported
        and power_relax_imported
    )
    nonzero_high_spectrum_proved = False

    degenerate_split = {
        "degenerate_phase": "s=0",
        "equation": "a^(-1)+b^(-1)=0 iff b=-a",
        "mobius_map": "phi_0(a)=-a is affine, not genuinely non-affine",
        "possible_size": "r_J(0)=|J cap (-J)| can be as large as O(|J|)",
        "energy_contribution": "r_J(0)^2 <= |J|^2",
        "absorption": "|J|^2 <= |J|^(3-delta) for every fixed delta<1 and |J|>=1",
        "pole_issue_for_s_nonzero": "the pole a=s^(-1) contributes no solution and removes at most one point",
        "remaining_scope": "only s != 0, where phi_s(a)=a/(s*a-1) is a genuine non-affine PGL2 map",
    }

    rows = [
        row(
            "AffineInverseHighSpectrumTargetActive",
            active,
            True,
            "上一证书已把剩余压成仿射等差段倒数自交高谱。",
            TARGET,
        ),
        row(
            "DegeneratePhaseS0Identified",
            degenerate_phase_split_closed,
            True,
            "`s=0` 是真实存在的仿射退化相位，对应反中心配对 `b=-a`。",
            "single affine phase",
        ),
        row(
            "DegeneratePhaseS0EnergyAbsorbed",
            degenerate_phase_split_closed,
            True,
            "`s=0` 纵使有线性重叠，也只贡献 `O(N^2)`，低于固定幂能量目标。",
            "removed from high-spectrum hardpoint",
        ),
        row(
            "NonzeroMapsAreGenuinePGL2",
            degenerate_phase_split_closed,
            True,
            "对 `s!=0`，`phi_s` 有唯一 pole 且不是仿射，剩余确为非退化 PGL2 高谱。",
            NEXT_ATOM,
        ),
        row(
            NEXT_ATOM,
            nonzero_high_spectrum_proved,
            False,
            "仓库内尚未证明非零相位的仿射进度段倒数自交高谱有固定幂节省。",
            f"{INCIDENCE_TARGET} OR {PGL2_TARGET}",
        ),
        row(
            "RowColumnUnconditionalClosed",
            False,
            False,
            "本步只分离并吸收退化相位，未证明非零 PGL2 高谱排斥。",
            NEXT_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_rks23_affine_degenerate_phase_split_router",
        "status": "s_zero_affine_degenerate_phase_absorbed_nonzero_pgl2_high_spectrum_remains",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "affine_inverse_high_spectrum_target_active": active,
        "degenerate_phase_s0_identified": degenerate_phase_split_closed,
        "degenerate_phase_s0_energy_absorbed": degenerate_phase_split_closed,
        "nonzero_maps_are_genuine_pgl2": degenerate_phase_split_closed,
        "nonzero_affine_inverse_high_spectrum_proved": nonzero_high_spectrum_proved,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": NEXT_ATOM,
        "parallel_incidence_target": INCIDENCE_TARGET,
        "parallel_group_expansion_target": PGL2_TARGET,
        "degenerate_split": degenerate_split,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "当前最窄点进一步校正：`s=0` 是真实仿射退化相位，方程退化为 `b=-a`，"
            "在对称区间中可产生线性重叠，不能被错误地并入非仿射高谱排斥。"
            "但它只有一个相位，能量贡献至多 `N^2`，被任意固定幂目标 `N^(3-delta)` 吸收。"
            "因此真正剩余变为 `s!=0` 的非退化 PGL2/Möbius 高谱排斥。"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    split = result["degenerate_split"]
    lines = [
        "# Prime Matrix strict RKS2/RKS3 仿射退化相位拆分证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"degenerate_phase_s0_identified={fmt_bool(result['degenerate_phase_s0_identified'])}",
        f"degenerate_phase_s0_energy_absorbed={fmt_bool(result['degenerate_phase_s0_energy_absorbed'])}",
        f"nonzero_affine_inverse_high_spectrum_proved={fmt_bool(result['nonzero_affine_inverse_high_spectrum_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 退化相位账本",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in split.items():
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
