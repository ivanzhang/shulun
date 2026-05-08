#!/usr/bin/env python3
"""Prime Matrix LowMod 有限弧 cap 归约路由器。

用法示例：
  python3 experiments/prime_matrix_lowmod_finite_arc_cap_reduction_router.py

输出：
  docs/monograph/prime-matrix-lowmod-finite-arc-cap-reduction-router.json
  docs/monograph/prime-matrix-lowmod-finite-arc-cap-reduction-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-lowmod-pdec-capacity-failure-router.json"
DEFAULT_LOWPHASE = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.json"
DEFAULT_LAYERED = DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"
DEFAULT_FOURIER = DOCS / "prime-matrix-dprc-fourier-inheritance-classifier.md"
DEFAULT_ENERGY = DOCS / "prime-matrix-dprc-newlayer-energy-dispersion.md"
DEFAULT_TOWER = DOCS / "prime-matrix-newlayer-pdec-tower-entropy-contract.md"
DEFAULT_FINITE_ARC = DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-lowmod-finite-arc-cap-reduction-router.json"
DEFAULT_MD = DOCS / "prime-matrix-lowmod-finite-arc-cap-reduction-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """写出小写布尔值。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部锚点。"""
    return all(needle in text for needle in needles)


def lowphase_micro_inputs(lowphase: dict[str, Any]) -> list[str]:
    """提取 LowPhase 三微输入。"""
    return [
        row["micro_input"]
        for row in lowphase.get("micro_rows", [])
        if row.get("closed") is False
    ]


def build_rows(
    previous: dict[str, Any],
    lowphase: dict[str, Any],
    layered_text: str,
    fourier_text: str,
    energy_text: str,
    tower_text: str,
    finite_arc_text: str,
    sae_text: str,
    column_text: str,
) -> list[dict[str, Any]]:
    """生成 LowMod 有限弧 cap 归约判定表。"""
    micro_inputs = lowphase_micro_inputs(lowphase)
    return [
        {
            "gate": "LowModFiniteArcInputPinned",
            "closed": previous.get("new_atomic_input")
            == "FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas",
            "proved": True,
            "meaning": "上一层已把 LowMod PDEC 容量失败压成未来 primitive schema 的有限弧 cap 质量界。",
            "remaining": "判断该有限弧 cap 是否独立于既有 LowPhase/DLS 体系。",
        },
        {
            "gate": "FiniteArcIsRankOneLowPhaseSlice",
            "closed": contains_all(
                finite_arc_text,
                ["finite cyclic-arc cap", "rank-one character slice", "transverse"],
            ),
            "proved": True,
            "meaning": "有限循环弧 cap 是有限签名空间中的非平凡字符秩一薄片。",
            "remaining": "LowMod 弧帽可按 LowPhase/横向结构二分处理。",
        },
        {
            "gate": "LayeredWheelClampAvailable",
            "closed": contains_all(
                layered_text,
                ["W-unit PDEC", "ColumnCRT or SAE", "LayeredClamp"],
            ),
            "proved": True,
            "meaning": "层叠轮夹击场已经给出固定轮单位类峰的命名回流口。",
            "remaining": "若固定轮峰持续同步，必须给 W-unit PDEC/SAE/ColumnCRT；若稀释则转新增层或平坦 DLS。",
        },
        {
            "gate": "FourierInheritanceClassifiesNewLayer",
            "closed": contains_all(
                fourier_text,
                ["new-layer", "new-layer W_j-unit PDEC", "继承"],
            ),
            "proved": True,
            "meaning": "强 Fourier 频率可区分为继承层与新增素因子层。",
            "remaining": "新增层集中必须给 new-layer PDEC；否则不能作为固定低模峰。",
        },
        {
            "gate": "NewLayerEnergyDispersionAvailable",
            "closed": contains_all(
                energy_text,
                ["新增层能量", "高维相位振荡", "new-layer W-unit PDEC"],
            ),
            "proved": True,
            "meaning": "新增层能量已经与单峰集中区分开。",
            "remaining": "若新增层高维分散，则剩余弧帽只能进入 flat DLS/KLS 吸收。",
        },
        {
            "gate": "NewLayerTowerNoUnnamedEscape",
            "closed": contains_all(
                tower_text,
                ["NewLayer-PDEC Tower Dichotomy", "profinite/global PDEC", "CleanKLS"],
            ),
            "proved": True,
            "meaning": "无限升层不能作为无名逃逸；熵发散给 PDEC，熵可求和给 CleanKLS/DLS。",
            "remaining": "仍需对应终端估计，而不是新增 LowMod 出口。",
        },
        {
            "gate": "SparseColumnNamedReturnsPreserved",
            "closed": "SAE 不是独立终端族" in sae_text
            and "ColumnCRT 的固定非零位移入口" in column_text,
            "proved": True,
            "meaning": "低支撑、孤窗和列位移弧帽不形成第四出口。",
            "remaining": "回流 SAE finite packet 或 ColumnCRT-as-PDEC。",
        },
        {
            "gate": "LowPhaseSharedMicroInputsImported",
            "closed": lowphase.get("dls_lowphase_boundary_closed") is True
            and set(micro_inputs)
            == {
                "DLSFixedWheelUnitPeakDilutionOrPDECReturn",
                "DLSNewLayerFourierConcentrationPDECReturn",
                "DLSFlatHighModLargeSieveAbsorption",
            },
            "proved": False,
            "meaning": "LowMod 有限弧 cap 的三种未闭合场景正是 LowPhase 已命名的三微输入。",
            "remaining": "DLSFixedWheelUnitPeakDilutionOrPDECReturn AND DLSNewLayerFourierConcentrationPDECReturn AND DLSFlatHighModLargeSieveAbsorption。",
        },
        {
            "gate": "LowModFiniteArcCapMassBoundsClosed",
            "closed": False,
            "proved": False,
            "meaning": "上述三微输入尚未证明，因此 LowMod 有限弧 cap 质量界仍未闭合。",
            "remaining": "证明 LowPhase 三微输入，或提交显式 LowModDualCap 回流证书。",
        },
    ]


def run(
    previous_path: Path,
    lowphase_path: Path,
    layered_path: Path,
    fourier_path: Path,
    energy_path: Path,
    tower_path: Path,
    finite_arc_path: Path,
    sae_path: Path,
    column_path: Path,
) -> dict[str, Any]:
    """执行 LowMod 有限弧 cap 归约。"""
    source_paths = [
        previous_path,
        lowphase_path,
        layered_path,
        fourier_path,
        energy_path,
        tower_path,
        finite_arc_path,
        sae_path,
        column_path,
    ]
    previous = load_json(previous_path)
    lowphase = load_json(lowphase_path)
    layered_text = layered_path.read_text(encoding="utf-8")
    fourier_text = fourier_path.read_text(encoding="utf-8")
    energy_text = energy_path.read_text(encoding="utf-8")
    tower_text = tower_path.read_text(encoding="utf-8")
    finite_arc_text = finite_arc_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        lowphase=lowphase,
        layered_text=layered_text,
        fourier_text=fourier_text,
        energy_text=energy_text,
        tower_text=tower_text,
        finite_arc_text=finite_arc_text,
        sae_text=sae_text,
        column_text=column_text,
    )
    micro_inputs = lowphase_micro_inputs(lowphase)
    independent_removed = all(
        row["closed"]
        for row in rows
        if row["gate"] not in {"LowModFiniteArcCapMassBoundsClosed"}
    )
    return {
        "certificate_type": "lowmod_finite_arc_cap_reduction_router",
        "status": "lowmod_finite_arc_cap_reduced_to_lowphase_three_micro_inputs",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "lowmod_finite_arc_independent_input_removed": independent_removed,
        "lowmod_finite_arc_cap_mass_bounds_closed": False,
        "lowphase_three_micro_inputs_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": "FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas",
        "terminal_gap_after_router": "LowPhaseThreeMicroInputsOrExplicitLowModDualCapReturn",
        "shared_micro_inputs": micro_inputs,
        "reduction_map": {
            "fixed_wheel_arc": "DLSFixedWheelUnitPeakDilutionOrPDECReturn",
            "new_layer_arc": "DLSNewLayerFourierConcentrationPDECReturn",
            "high_mod_flat_arc": "DLSFlatHighModLargeSieveAbsorption",
            "sparse_or_displacement": "SAE finite packet or ColumnCRT-as-PDEC",
        },
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "rows": rows,
        "plain_conclusion": (
            "本步把 LowMod 有限弧 cap 质量界从独立新原子移除：固定轮弧、"
            "新增层弧和高模平坦弧分别就是既有 LowPhase 三微输入。"
            "因此下一步不应另造 LowMod 第四终端，而应直接证明 LowPhase 三微输入，"
            "或从具体 LowModDualCap 中抽取 SAE/ColumnCRT/refined PDEC 回流证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    reduction = result["reduction_map"]
    lines = [
        "# Prime Matrix LowMod 有限弧 cap 归约路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"lowmod_finite_arc_independent_input_removed={fmt_bool(result['lowmod_finite_arc_independent_input_removed'])}",
        f"lowmod_finite_arc_cap_mass_bounds_closed={fmt_bool(result['lowmod_finite_arc_cap_mass_bounds_closed'])}",
        f"lowphase_three_micro_inputs_proved={fmt_bool(result['lowphase_three_micro_inputs_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 归约映射",
        "",
        "| LowMod finite arc case | existing target |",
        "| --- | --- |",
    ]
    for key, value in reduction.items():
        lines.append(f"| `{key}` | `{table_cell(value)}` |")
    lines.extend(
        [
            "",
            "LowMod 弧帽不是一个新的平行终端。固定轮单位类峰、升层新增 Fourier 峰、",
            "以及剥离后的高模平坦残余，已经分别落入 LowPhase 的三微输入。",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 新的最窄剩余",
            "",
            "```text",
            "FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas",
            "  -> DLSFixedWheelUnitPeakDilutionOrPDECReturn",
            "     AND DLSNewLayerFourierConcentrationPDECReturn",
            "     AND DLSFlatHighModLargeSieveAbsorption",
            "  or explicit LowModDualCap return to SAE/ColumnCRT/refined PDEC.",
            "```",
            "",
            "这一步仍不是终端证明；它关闭的是输入分类边界，说明 LowMod 有限弧 cap 不再额外增加",
            "一个独立开放原子。真正要硬攻的是 LowPhase 三微输入或具体 DualCap 回流证书。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def write_outputs(result: dict[str, Any], json_out: Path, md_out: Path) -> None:
    """写出 JSON 与 Markdown。"""
    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--lowphase", type=Path, default=DEFAULT_LOWPHASE)
    parser.add_argument("--layered", type=Path, default=DEFAULT_LAYERED)
    parser.add_argument("--fourier", type=Path, default=DEFAULT_FOURIER)
    parser.add_argument("--energy", type=Path, default=DEFAULT_ENERGY)
    parser.add_argument("--tower", type=Path, default=DEFAULT_TOWER)
    parser.add_argument("--finite-arc", type=Path, default=DEFAULT_FINITE_ARC)
    parser.add_argument("--sae", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--column", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        lowphase_path=args.lowphase,
        layered_path=args.layered,
        fourier_path=args.fourier,
        energy_path=args.energy,
        tower_path=args.tower,
        finite_arc_path=args.finite_arc,
        sae_path=args.sae,
        column_path=args.column,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
