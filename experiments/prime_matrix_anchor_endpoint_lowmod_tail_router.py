#!/usr/bin/env python3
"""Prime Matrix anchor 端点 PDEC 低模/尾项二分路由器。

用法示例：
  python3 experiments/prime_matrix_anchor_endpoint_lowmod_tail_router.py

输出：
  docs/monograph/prime-matrix-anchor-endpoint-lowmod-tail-router.json
  docs/monograph/prime-matrix-anchor-endpoint-lowmod-tail-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-anchor-collar-endpoint-bridge-router.json"
DEFAULT_DLS13_LOWTAIL = DOCS / "prime-matrix-eda-dls13-lowmod-tail-dichotomy.md"
DEFAULT_LOWPHASE = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.md"
DEFAULT_BESDLS = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-anchor-endpoint-lowmod-tail-router.json"
DEFAULT_MD = DOCS / "prime-matrix-anchor-endpoint-lowmod-tail-router.md"

OLD_ATOM = "AnchorCollarEndpointDefectPDECExclusion"
NEW_ATOM = (
    "(AnchorEndpointLowModPDECFinitePhaseExclusion "
    "AND AnchorEndpointTailCorePDECOrFiberSaturation)"
)


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
    dls13_lowtail_text: str,
    lowphase_text: str,
    besdls_text: str,
) -> list[dict[str, Any]]:
    """生成低模/尾项二分判定表。"""
    endpoint_gate_active = (
        previous.get("next_priority") == OLD_ATOM
        and OLD_ATOM in previous.get("open_gates", [])
    )
    endpoint_bridge_available = (
        previous.get("anchor_collar_endpoint_bridge_closed") is True
        and previous.get("endpoint_bridge", "").startswith("H_x(P)=")
    )
    lowtail_template_available = (
        "低模/尾项二分" in dls13_lowtail_text
        and "E_{\\le D}" in dls13_lowtail_text
        and "E_{>D}" in dls13_lowtail_text
    )
    lowmod_named_route_available = (
        "LowPhase" in lowphase_text
        and "W-unit PDEC" in lowphase_text
        and "DLSFixedWheelUnitPeakDilutionOrPDECReturn" in lowphase_text
    )
    tail_named_route_available = (
        "PointLoad" in besdls_text
        and "ShortWindow" in besdls_text
        and "LowPhase" in besdls_text
    )
    dichotomy_closed = all(
        [
            endpoint_gate_active,
            endpoint_bridge_available,
            lowtail_template_available,
            lowmod_named_route_available,
            tail_named_route_available,
        ]
    )
    return [
        row(
            "AnchorEndpointDefectGateActive",
            endpoint_gate_active,
            True,
            "上一层最新最窄目标是 AnchorCollarEndpointDefectPDECExclusion。",
            "本步只处理该端点缺陷。",
        ),
        row(
            "EndpointBridgeImported",
            endpoint_bridge_available,
            True,
            "早期零行若触发 anchor 主项间隙，则 E_x<=-G_x。",
            "需要排斥该强负端点缺陷。",
        ),
        row(
            "DLS13LowTailTemplateImported",
            lowtail_template_available,
            True,
            "DLS13 已有同型低模/尾项精确二分，可逐字迁移到 E_x。",
            "不新增概率假设。",
        ),
        row(
            "AnchorEndpointLowTailDichotomy",
            True,
            True,
            "对任意 D 与 0<theta<1，E_x<=-G_x 强制 E_{x,<=D}<=-theta G_x 或 E_{x,>D}<=-(1-theta)G_x。",
            "端点缺陷不能作为整体黑箱保留。",
        ),
        row(
            "LowModFinitePhasePDECRoute",
            lowmod_named_route_available,
            False,
            "低模项是有限 CRT 相位函数；若承担强负缺陷，则给 fixed-wheel/lowphase PDEC 坏相位。",
            "仍需排斥该有限相位坏集。",
        ),
        row(
            "TailCoreNamedReturnRoute",
            tail_named_route_available,
            False,
            "尾项若承担强负缺陷，必须显化为 PointLoad、ShortWindow、LowPhase 或 anchor-fiber 饱和。",
            "仍需排斥尾项 core 或回流 PDEC/SAE。",
        ),
        row(
            "AnchorEndpointPDECDichotomyClosed",
            dichotomy_closed,
            True,
            "AnchorCollarEndpointDefectPDECExclusion 已压成低模有限相位排斥与高模尾项 core/纤维饱和排斥。",
            NEW_ATOM,
        ),
        row(
            "AnchorEndpointLowModPDECFinitePhaseExclusion",
            False,
            False,
            "尚未证明固定 D 低模坏相位不能持续命中早期零行反例族。",
            "下一步最窄目标。",
        ),
        row(
            "AnchorEndpointTailCorePDECOrFiberSaturation",
            False,
            False,
            "尚未证明高模尾项强负只能回流已可排斥 PDEC/SAE 或短纤维饱和。",
            "第二剩余。",
        ),
    ]


def run(
    previous_path: Path,
    dls13_lowtail_path: Path,
    lowphase_path: Path,
    besdls_path: Path,
) -> dict[str, Any]:
    """执行 anchor 端点 PDEC 低模/尾项二分。"""
    source_paths = [previous_path, dls13_lowtail_path, lowphase_path, besdls_path]
    previous = load_json(previous_path)
    dls13_lowtail_text = dls13_lowtail_path.read_text(encoding="utf-8")
    lowphase_text = lowphase_path.read_text(encoding="utf-8")
    besdls_text = besdls_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        dls13_lowtail_text=dls13_lowtail_text,
        lowphase_text=lowphase_text,
        besdls_text=besdls_text,
    )
    dichotomy_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "AnchorEndpointPDECDichotomyClosed"
    )
    latest_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    return {
        "certificate_type": "anchor_endpoint_lowmod_tail_router",
        "status": "anchor_endpoint_pdec_reduced_to_lowmod_tail_dichotomy",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "anchor_endpoint_pdec_dichotomy_closed": dichotomy_closed,
        "anchor_endpoint_pdec_exclusion_fully_proved": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": OLD_ATOM,
        "terminal_gap_after_router": NEW_ATOM,
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            OLD_ATOM: NEW_ATOM,
        },
        "next_priority": "AnchorEndpointLowModPDECFinitePhaseExclusion",
        "dichotomy_formula": (
            "If E_x<=-G_x, then for any D and theta either "
            "E_{x,<=D}<=-theta G_x or E_{x,>D}<=-(1-theta)G_x."
        ),
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 anchor-collar 端点 PDEC 从一个整体强负误差拆成低模有限 CRT 相位坏集"
            "与高模 tail-core/纤维饱和两项。它不排斥端点缺陷，只删除整体黑箱形态，"
            "让下一步可直接攻固定低模相位坏集。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix anchor 端点 PDEC 低模/尾项二分路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"anchor_endpoint_pdec_dichotomy_closed={fmt_bool(result['anchor_endpoint_pdec_dichotomy_closed'])}",
        f"anchor_endpoint_pdec_exclusion_fully_proved={fmt_bool(result['anchor_endpoint_pdec_exclusion_fully_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 二分公式",
        "",
        "```text",
        result["dichotomy_formula"],
        "```",
        "",
        "这一步仍处于 `Assume EarlyZeroRowWithinP` 分支，不使用真实样本缺席。",
        "",
        "## 2. 替换律",
        "",
        "```text",
        replacement[0],
        "  =>",
        replacement[1],
        "```",
        "",
        "## 3. 判定表",
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
            "## 4. 最新输入基",
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
            "## 5. 下一步",
            "",
            f"最窄目标更新为 `{result['next_priority']}`：固定 `D` 后，低模项是有限 CRT 相位函数；"
            "若它能持续承担 `-theta G_x` 级负缺陷，就必须形成 fixed-wheel/lowphase PDEC 坏相位。"
            "下一步要排斥这个坏相位，或把它登记为可处理 PDEC 证书。",
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
    parser.add_argument("--dls13-lowtail", type=Path, default=DEFAULT_DLS13_LOWTAIL)
    parser.add_argument("--lowphase", type=Path, default=DEFAULT_LOWPHASE)
    parser.add_argument("--besdls", type=Path, default=DEFAULT_BESDLS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        dls13_lowtail_path=args.dls13_lowtail,
        lowphase_path=args.lowphase,
        besdls_path=args.besdls,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
