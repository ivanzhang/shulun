#!/usr/bin/env python3
"""Prime Matrix anchor 低模端点相位准入 fixed-wheel 路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_lowmod_fixedwheel_admission_router.py

输出：
  docs/monograph/prime-matrix-anchor-lowmod-fixedwheel-admission-router.json
  docs/monograph/prime-matrix-anchor-lowmod-fixedwheel-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-anchor-endpoint-lowmod-tail-router.json"
DEFAULT_LOWMOD_CAP = DOCS / "prime-matrix-lowmod-pdec-capacity-failure-router.md"
DEFAULT_LOWMOD_ARC = DOCS / "prime-matrix-lowmod-finite-arc-cap-reduction-router.md"
DEFAULT_LOWPHASE = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-lowmod-fixedwheel-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-lowmod-fixedwheel-admission-router.md"

OLD_ATOM = "AnchorEndpointLowModPDECFinitePhaseExclusion"
NEW_ATOM = "DLSFixedWheelUnitPeakDilutionOrPDECReturn"


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


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


def simplify_basis(text: str) -> str:
    """化简替换后出现的 fixed-wheel 重复因子。"""
    duplicated = (
        "DLSFixedWheelUnitPeakDilutionOrPDECReturn AND "
        "((DLSFixedWheelUnitPeakDilutionOrPDECReturn AND "
        "AnchorEndpointTailCorePDECOrFiberSaturation) OR "
        "AnchorFiberSaturationPDECOrSAEReturn)"
    )
    simplified = (
        "DLSFixedWheelUnitPeakDilutionOrPDECReturn AND "
        "(AnchorEndpointTailCorePDECOrFiberSaturation OR "
        "AnchorFiberSaturationPDECOrSAEReturn)"
    )
    return text.replace(duplicated, simplified)


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(
    previous: dict[str, Any],
    lowmod_cap_text: str,
    lowmod_arc_text: str,
    lowphase_text: str,
) -> list[dict[str, Any]]:
    """生成 fixed-wheel 准入判定表。"""
    lowmod_gate_active = (
        previous.get("next_priority") == OLD_ATOM
        and OLD_ATOM in previous.get("open_gates", [])
    )
    finite_phase_closed = (
        previous.get("anchor_endpoint_pdec_dichotomy_closed") is True
        and "E_{x,<=D}" in previous.get("dichotomy_formula", "")
    )
    same_formal_unit_available = (
        "G_B=Z/Q_BZ" in lowmod_cap_text
        and "SameFormalUnitPinned" in lowmod_cap_text
    )
    finite_arc_reduction_available = (
        "fixed_wheel_arc" in lowmod_arc_text
        and "DLSFixedWheelUnitPeakDilutionOrPDECReturn" in lowmod_arc_text
    )
    lowphase_target_available = (
        "DLSFixedWheelUnitPeakDilutionOrPDECReturn" in lowphase_text
        and "W-unit PDEC" in lowphase_text
    )
    admission_closed = all(
        [
            lowmod_gate_active,
            finite_phase_closed,
            same_formal_unit_available,
            finite_arc_reduction_available,
            lowphase_target_available,
        ]
    )
    return [
        row(
            "AnchorLowModGateActive",
            lowmod_gate_active,
            True,
            "上一层最新最窄目标是 AnchorEndpointLowModPDECFinitePhaseExclusion。",
            "本步只判断它是否是独立新输入。",
        ),
        row(
            "FiniteCRTPhasePinned",
            finite_phase_closed,
            True,
            "固定 D 后，E_{x,<=D} 是有限 CRT 相位函数。",
            "可放入固定轮 formal unit。",
        ),
        row(
            "SameFormalUnitLowModProtocolImported",
            same_formal_unit_available,
            True,
            "LowMod PDEC 容量失败已有同 formal unit 协议 G_B=Z/Q_BZ。",
            "anchor 低模坏相位不允许跨口径拼接。",
        ),
        row(
            "FiniteArcReductionImported",
            finite_arc_reduction_available,
            True,
            "LowMod 有限弧 cap 已归约到 fixed-wheel/new-layer/flat DLS 三类。",
            "固定 D 的 anchor 低模坏相位属于 fixed-wheel slice。",
        ),
        row(
            "FixedWheelLowPhaseTargetAvailable",
            lowphase_target_available,
            False,
            "既有 LowPhase 路由已经把 fixed-wheel 单位类峰命名为 DLSFixedWheelUnitPeakDilutionOrPDECReturn。",
            "该目标尚未证明。",
        ),
        row(
            "AnchorLowModIndependentInputRemoved",
            admission_closed,
            True,
            "AnchorEndpointLowModPDECFinitePhaseExclusion 不是独立剩余，准入既有 fixed-wheel PDEC/稀释输入。",
            NEW_ATOM,
        ),
        row(
            "DLSFixedWheelUnitPeakDilutionOrPDECReturn",
            False,
            False,
            "仍未证明 fixed-wheel 单位峰不能持续支付反例缺陷，或失败必给 PDEC 回流。",
            "既有全局 LowPhase 微输入。",
        ),
        row(
            "AnchorEndpointTailCorePDECOrFiberSaturation",
            False,
            False,
            "低模独立性删除后，anchor 端点分支仍需处理高模 tail-core 或纤维饱和。",
            "下一步 anchor 专属最窄目标。",
        ),
    ]


def run(
    previous_path: Path,
    lowmod_cap_path: Path,
    lowmod_arc_path: Path,
    lowphase_path: Path,
) -> dict[str, Any]:
    """执行 anchor 低模 fixed-wheel 准入路由。"""
    source_paths = [previous_path, lowmod_cap_path, lowmod_arc_path, lowphase_path]
    previous = load_json(previous_path)
    lowmod_cap_text = lowmod_cap_path.read_text(encoding="utf-8")
    lowmod_arc_text = lowmod_arc_path.read_text(encoding="utf-8")
    lowphase_text = lowphase_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        lowmod_cap_text=lowmod_cap_text,
        lowmod_arc_text=lowmod_arc_text,
        lowphase_text=lowphase_text,
    )
    admission_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "AnchorLowModIndependentInputRemoved"
    )
    latest_self = simplify_basis(
        replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    )
    latest_cond = simplify_basis(
        replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    )
    return {
        "certificate_type": "anchor_lowmod_fixedwheel_admission_router",
        "status": "anchor_lowmod_endpoint_phase_admitted_to_fixedwheel_pdec",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "anchor_lowmod_independent_input_removed": admission_closed,
        "dls_fixedwheel_input_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            OLD_ATOM: NEW_ATOM,
        },
        "next_priority": "AnchorEndpointTailCorePDECOrFiberSaturation",
        "global_open_input_reused": NEW_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步证明 anchor 低模端点坏相位不是新输入：固定 D 后它是有限 CRT 相位函数，"
            "按同 formal unit 准入既有 fixed-wheel/LowPhase PDEC 输入。该步删除独立 anchor "
            "低模剩余，但不证明 DLSFixedWheelUnitPeakDilutionOrPDECReturn。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix anchor 低模端点相位 fixed-wheel 准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"anchor_lowmod_independent_input_removed={fmt_bool(result['anchor_lowmod_independent_input_removed'])}",
        f"dls_fixedwheel_input_proved={fmt_bool(result['dls_fixedwheel_input_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
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
            "## 3. 最新输入基",
            "",
            "条件输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "完全自足输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 4. 下一步",
            "",
            f"anchor 专属最窄目标更新为 `{result['next_priority']}`。全局层面仍需证明既有 "
            f"`{result['global_open_input_reused']}`。",
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
    parser.add_argument("--lowmod-cap", type=Path, default=DEFAULT_LOWMOD_CAP)
    parser.add_argument("--lowmod-arc", type=Path, default=DEFAULT_LOWMOD_ARC)
    parser.add_argument("--lowphase", type=Path, default=DEFAULT_LOWPHASE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        lowmod_cap_path=args.lowmod_cap,
        lowmod_arc_path=args.lowmod_arc,
        lowphase_path=args.lowphase,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
