#!/usr/bin/env python3
"""Prime Matrix anchor tail-core 到纤维饱和路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_tailcore_fiber_saturation_router.py

输出：
  docs/monograph/prime-matrix-anchor-tailcore-fiber-saturation-router.json
  docs/monograph/prime-matrix-anchor-tailcore-fiber-saturation-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-anchor-lowmod-fixedwheel-admission-router.json"
DEFAULT_BESDLS = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.md"
DEFAULT_SN3E = DOCS / "prime-matrix-sn3e-highfreq-bohrcap-no-cycle.md"
DEFAULT_ANCHOR = DOCS / "prime-matrix-early-zero-anchor-collar-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-tailcore-fiber-saturation-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-tailcore-fiber-saturation-router.md"

OLD_ATOM = "AnchorEndpointTailCorePDECOrFiberSaturation"
NEW_ATOM = "AnchorFiberSaturationPDECOrSAEReturn"


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
    """化简 tail-core 替换后出现的重复纤维饱和二分。"""
    return text.replace(
        "(AnchorFiberSaturationPDECOrSAEReturn OR AnchorFiberSaturationPDECOrSAEReturn)",
        "AnchorFiberSaturationPDECOrSAEReturn",
    )


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
    besdls_text: str,
    sn3e_text: str,
    anchor_text: str,
) -> list[dict[str, Any]]:
    """生成 tail-core 到纤维饱和判定表。"""
    tail_gate_active = (
        previous.get("next_priority") == OLD_ATOM
        and OLD_ATOM in previous.get("open_gates", [])
    )
    bes_alphabet_available = (
        "PointLoad" in besdls_text
        and "ShortWindow" in besdls_text
        and "LowPhase" in besdls_text
        and "BES-DLS 输入" in besdls_text
    )
    bohr_no_cycle_available = (
        "HighFrequencyColumn 不再是开放形态" in sn3e_text
        and "L2-flat CleanKLS" in sn3e_text
    )
    anchor_fiber_geometry_available = (
        "FiberShortPrimeInterval" in anchor_text
        and "q-fiber capacity" in anchor_text
    )
    existing_global_inputs_cover_nonfiber = all(
        token in previous.get("latest_self_contained_basis", "")
        for token in [
            "DLSPointLoadColumnCRTBoundOrNamedReturn",
            "DLSShortWindowSAEBoundOrNamedReturn",
            "DLSFixedWheelUnitPeakDilutionOrPDECReturn",
        ]
    )
    tailcore_reduced = all(
        [
            tail_gate_active,
            bes_alphabet_available,
            bohr_no_cycle_available,
            anchor_fiber_geometry_available,
            existing_global_inputs_cover_nonfiber,
        ]
    )
    return [
        row(
            "AnchorTailCoreGateActive",
            tail_gate_active,
            True,
            "上一层 anchor 专属最窄目标是 AnchorEndpointTailCorePDECOrFiberSaturation。",
            "本步只处理高模 tail-core。",
        ),
        row(
            "BESDLSNamedAlphabetImported",
            bes_alphabet_available,
            True,
            "高模 tail-core 若承担强负缺陷，必须显化为 PointLoad、ShortWindow 或 LowPhase。",
            "这些不是 anchor 新出口。",
        ),
        row(
            "HighFrequencyNoCycleImported",
            bohr_no_cycle_available,
            True,
            "非零列频率/Bohr-cap 不能形成无名循环，只能回流 PDEC/SAE/ColumnCRT 或 L2-flat。",
            "L2-flat 已在早期零行反例分支中关闭为终端包。",
        ),
        row(
            "AnchorFiberGeometryPinned",
            anchor_fiber_geometry_available,
            True,
            "anchor 专属剩余只能是 canonical q-fiber 短素数窗口的近饱和支付。",
            "即 AnchorFiberSaturation。",
        ),
        row(
            "ExistingGlobalInputsCoverNonFiberTail",
            existing_global_inputs_cover_nonfiber,
            False,
            "PointLoad、ShortWindow、FixedWheel 已在全局输入基中保留。",
            "它们尚未证明，但不再是 anchor 专属新增项。",
        ),
        row(
            "AnchorTailCoreIndependentInputRemoved",
            tailcore_reduced,
            True,
            "AnchorEndpointTailCorePDECOrFiberSaturation 被压成已有 DLS 命名出口或真正 anchor-fiber 饱和。",
            NEW_ATOM,
        ),
        row(
            "AnchorFiberSaturationPDECOrSAEReturn",
            False,
            False,
            "尚未证明 canonical q-fiber 近饱和必然给出 PDEC/SAE，或不能持续支付早期零行。",
            "下一步最窄目标。",
        ),
    ]


def run(
    previous_path: Path,
    besdls_path: Path,
    sn3e_path: Path,
    anchor_path: Path,
) -> dict[str, Any]:
    """执行 anchor tail-core 到纤维饱和路由。"""
    source_paths = [previous_path, besdls_path, sn3e_path, anchor_path]
    previous = load_json(previous_path)
    besdls_text = besdls_path.read_text(encoding="utf-8")
    sn3e_text = sn3e_path.read_text(encoding="utf-8")
    anchor_text = anchor_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        besdls_text=besdls_text,
        sn3e_text=sn3e_text,
        anchor_text=anchor_text,
    )
    tailcore_reduced = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "AnchorTailCoreIndependentInputRemoved"
    )
    latest_self = simplify_basis(
        replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    )
    latest_cond = simplify_basis(
        replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    )
    return {
        "certificate_type": "anchor_tailcore_fiber_saturation_router",
        "status": "anchor_tailcore_reduced_to_fiber_saturation",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "anchor_tailcore_independent_input_removed": tailcore_reduced,
        "anchor_fiber_saturation_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            OLD_ATOM: NEW_ATOM,
        },
        "next_priority": NEW_ATOM,
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步删除 anchor tail-core 的独立性：高模 tail 若非 fiber saturation，"
            "则已经落入全局 DLS PointLoad/ShortWindow/LowPhase 或 Bohr-cap 命名出口。"
            "anchor 专属剩余只剩 canonical q-fiber 近饱和是否必回流 PDEC/SAE。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix anchor tail-core 到纤维饱和路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"anchor_tailcore_independent_input_removed={fmt_bool(result['anchor_tailcore_independent_input_removed'])}",
        f"anchor_fiber_saturation_proved={fmt_bool(result['anchor_fiber_saturation_proved'])}",
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
            f"最窄目标更新为 `{result['next_priority']}`：证明 canonical q-fiber 近饱和不能持续支付早期零行，"
            "或从近饱和中抽取同 formal unit 的 PDEC/SAE 证书。",
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
    parser.add_argument("--besdls", type=Path, default=DEFAULT_BESDLS)
    parser.add_argument("--sn3e", type=Path, default=DEFAULT_SN3E)
    parser.add_argument("--anchor", type=Path, default=DEFAULT_ANCHOR)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        besdls_path=args.besdls,
        sn3e_path=args.sn3e,
        anchor_path=args.anchor,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
