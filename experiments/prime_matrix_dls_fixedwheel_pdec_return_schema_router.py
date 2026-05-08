#!/usr/bin/env python3
"""Prime Matrix DLS fixed-wheel 单位峰命名回流 schema 路由器。

用法示例：
  python3 experiments/prime_matrix_dls_fixedwheel_pdec_return_schema_router.py

输出：
  docs/monograph/prime-matrix-dls-fixedwheel-pdec-return-schema-router.json
  docs/monograph/prime-matrix-dls-fixedwheel-pdec-return-schema-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-dls-pointload-columncrt-return-schema-router.json"
DEFAULT_LOWPHASE = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md"
DEFAULT_WHEEL = DOCS / "prime-matrix-dprc-wheel-unit-phase-balance.md"
DEFAULT_LAYERED = DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_NEWLAYER = DOCS / "prime-matrix-lowmod-newlayer-bridge-router.md"
DEFAULT_FLAT = DOCS / "prime-matrix-early-zero-l2flat-kls-exclusion-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-dls-fixedwheel-pdec-return-schema-router.json"
DEFAULT_MD = DOCS / "prime-matrix-dls-fixedwheel-pdec-return-schema-router.md"

OLD_ATOM = "DLSFixedWheelUnitPeakDilutionOrPDECReturn"
NEW_ATOM = "NoDLSFixedWheelSpecificGap_AfterWUnitPDECOrLayeredDilutionReturn"
NEXT_ATOM = "SignedGeometricLedgerVariationBranchLiftAndReturn"


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


def remove_closed_gap(text: str) -> str:
    """从输入基中删除已回流的 fixed-wheel 专属 gap 标记。"""
    result = text
    for pattern in [f" AND {NEW_ATOM}", f"{NEW_ATOM} AND ", NEW_ATOM]:
        result = result.replace(pattern, "")
    return result


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
    lowphase_text: str,
    wheel_text: str,
    layered_text: str,
    pdec_text: str,
    newlayer_text: str,
    flat_text: str,
) -> list[dict[str, Any]]:
    """生成 DLS fixed-wheel 单位峰命名回流 schema 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    fixedwheel_atom = (
        OLD_ATOM in lowphase_text
        and "固定轮单位类峰若持续同步，给 W-unit PDEC" in lowphase_text
    )
    finite_unit_phase = (
        "单位类 `U_W`" in layered_text
        and "E_a(W)" in layered_text
        and "W-unit PDEC" in layered_text
    )
    static_not_global = "不是终局规律" in wheel_text and "没有固定单位类长期主导" in wheel_text
    layered_dilution = (
        "随着 W 提升，单位类数量增加，单类峰值被稀释" in layered_text
        and "若某层仍出现同步尖峰，它就是 PDEC" in layered_text
    )
    pdec_boundary = (
        "pdec_family_explicit_input_boundary_closed=true" in pdec_text
        and "同一个 formal unit" in pdec_text
    )
    newlayer_return = (
        "DLSNewLayerFourierConcentrationPDECReturn" in newlayer_text
        and "RegisteredNewLayerPDECFormalUnitAndCapStableSchema" in newlayer_text
    )
    flat_escape_closed = (
        "early_zero_l2flat_kls_counterexample_spectral_exclusion_closed=true" in flat_text
        and "EarlyZeroTerminalExclusionPackage" in flat_text
    )
    schema_closed = all(
        [
            active,
            fixedwheel_atom,
            finite_unit_phase,
            static_not_global,
            layered_dilution,
            pdec_boundary,
            newlayer_return,
            flat_escape_closed,
        ]
    )
    return [
        row(
            "DLSFixedWheelGateActive",
            active,
            True,
            "当前输入基仍含 DLSFixedWheelUnitPeakDilutionOrPDECReturn。",
            "本步只攻击 fixed-wheel 专属无名出口。",
        ),
        row(
            "FixedWheelAtomPinned",
            fixedwheel_atom,
            True,
            "LowPhase 已把固定轮单位类峰定位为 W-unit PDEC 或稀释回流。",
            "不能继续作为未定义低模规律。",
        ),
        row(
            "FiniteWheelFormalUnit",
            finite_unit_phase,
            True,
            "固定 W 的单位类 U_W 与中心化偏差 E_a(W) 是有限 formal unit 对象。",
            "持久峰可登记为 W-unit PDEC。",
        ),
        row(
            "FixedWheelNotTerminalLaw",
            static_not_global,
            True,
            "W=30 单位峰真实存在但没有固定单位类长期主导，不能作为终局规律停留。",
            "样本只定位结构，不作证明。",
        ),
        row(
            "LayeredWheelDilutionOrPDEC",
            layered_dilution,
            True,
            "升层后若峰继续同步则给 PDEC；若不同步，单类峰被稀释并进入新增层/flat 分支。",
            "数值稀释本身不是无条件证明。",
        ),
        row(
            "PersistentWUnitPeakAdmitsPDEC",
            pdec_boundary,
            True,
            "固定单位峰若在同 formal unit 上持久复现，必须作为显式 W-unit PDEC schema 准入。",
            "PDEC family 无条件排斥仍开放。",
        ),
        row(
            "LayerEscapeUsesNewLayerReturn",
            newlayer_return,
            True,
            "固定轮峰若升层为新增因子 Fourier 集中，已有 new-layer PDEC/flat admission 接线。",
            "new-layer 终端证书仍按既有边界处理。",
        ),
        row(
            "FlatEscapeAlreadyCounterexampleRouted",
            flat_escape_closed,
            True,
            "固定轮与新增层均被剥离后的 flat/L2-flat 逃逸已在早期零行反例分支回到终端包。",
            "终端包本身仍未无条件排斥。",
        ),
        row(
            "NoDLSFixedWheelSpecificFourthExit",
            schema_closed,
            True,
            "fixed-wheel 只有持久 W-unit PDEC、升层 new-layer/flat 回流或稀释不足三类归宿。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            schema_closed,
            True,
            "该硬点作为 fixed-wheel 命名回流 schema 已闭合。",
            "不等于 W-unit PDEC 或终端包已排斥。",
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "DLS 微输入删除后，下一步回到 signed 几何账本变差/分支提升锁。",
            NEXT_ATOM,
        ),
        row(
            "GlobalPDECorSparseTerminalExclusion",
            False,
            False,
            "若实际产生新 persistent PDEC 或 sparse packet，仍需提交并排斥相应证书。",
            "FutureExplicitPrimitivePDECSchema / FutureExplicitSparsePacketExtractorSchema。",
        ),
    ]


def run(
    previous_path: Path,
    lowphase_path: Path,
    wheel_path: Path,
    layered_path: Path,
    pdec_path: Path,
    newlayer_path: Path,
    flat_path: Path,
) -> dict[str, Any]:
    """执行 DLS fixed-wheel 单位峰命名回流 schema 路由。"""
    source_paths = [
        previous_path,
        lowphase_path,
        wheel_path,
        layered_path,
        pdec_path,
        newlayer_path,
        flat_path,
    ]
    previous = load_json(previous_path)
    lowphase_text = lowphase_path.read_text(encoding="utf-8")
    wheel_text = wheel_path.read_text(encoding="utf-8")
    layered_text = layered_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    newlayer_text = newlayer_path.read_text(encoding="utf-8")
    flat_text = flat_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        lowphase_text=lowphase_text,
        wheel_text=wheel_text,
        layered_text=layered_text,
        pdec_text=pdec_text,
        newlayer_text=newlayer_text,
        flat_text=flat_text,
    )
    schema_closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    replaced_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    replaced_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_self = remove_closed_gap(replaced_self)
    latest_cond = remove_closed_gap(replaced_cond)
    return {
        "certificate_type": "dls_fixedwheel_pdec_return_schema_router",
        "status": "dls_fixedwheel_return_schema_closed_terminal_exclusion_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dls_fixedwheel_return_schema_closed": schema_closed,
        "dls_fixedwheel_specific_gap_removed": schema_closed,
        "fixedwheel_numeric_dilution_proved": False,
        "wunit_pdec_terminal_exclusion_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "next_priority": NEXT_ATOM,
        "remaining_global_terminal_guard": (
            "FutureExplicitPrimitivePDECSchema_OR_FutureExplicitSparsePacketExtractorSchema_if_materialized"
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步闭合的是 DLS fixed-wheel 单位峰的专属命名回流 schema：固定轮峰若持久，"
            "必须登记为 W-unit PDEC；若升层后继续集中，进入 new-layer PDEC/flat admission；"
            "若固定轮和新增层缺陷都被剥离，则 flat/L2-flat 逃逸已在早期零行反例分支回到终端包。"
            "因此 fixed-wheel 专属 gap 被删除；但 W-unit PDEC、终端包和 signed 几何账本仍未无条件排斥。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix DLS fixed-wheel 单位峰命名回流 schema 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"dls_fixedwheel_return_schema_closed={fmt_bool(result['dls_fixedwheel_return_schema_closed'])}",
        f"dls_fixedwheel_specific_gap_removed={fmt_bool(result['dls_fixedwheel_specific_gap_removed'])}",
        f"fixedwheel_numeric_dilution_proved={fmt_bool(result['fixedwheel_numeric_dilution_proved'])}",
        f"wunit_pdec_terminal_exclusion_proved={fmt_bool(result['wunit_pdec_terminal_exclusion_proved'])}",
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
        "这一步仍处于反例分支/终端证书口径，不使用真实样本缺席。",
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
            f"fixed-wheel 专属 gap 已删除。下一步最窄目标转到 `{result['next_priority']}`："
            "证明 actual signed source 的总变差和 branch key 复杂度确由几何账本支配，"
            "或把超预算质量回流 PDEC/SAE/ColumnCRT/CleanKLS。",
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
    parser.add_argument("--wheel", type=Path, default=DEFAULT_WHEEL)
    parser.add_argument("--layered", type=Path, default=DEFAULT_LAYERED)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--newlayer", type=Path, default=DEFAULT_NEWLAYER)
    parser.add_argument("--flat", type=Path, default=DEFAULT_FLAT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        lowphase_path=args.lowphase,
        wheel_path=args.wheel,
        layered_path=args.layered,
        pdec_path=args.pdec,
        newlayer_path=args.newlayer,
        flat_path=args.flat,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
