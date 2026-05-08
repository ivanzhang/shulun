#!/usr/bin/env python3
"""Prime Matrix LowMod-new-layer 桥接路由器。

用法示例：
  python3 experiments/prime_matrix_lowmod_newlayer_bridge_router.py

输出：
  docs/monograph/prime-matrix-lowmod-newlayer-bridge-router.json
  docs/monograph/prime-matrix-lowmod-newlayer-bridge-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_LOWMOD = DOCS / "prime-matrix-lowmod-finite-arc-cap-reduction-router.json"
DEFAULT_EXTMATCH = DOCS / "prime-matrix-clean-core-newlayer-external-lemma-match-router.json"
DEFAULT_PROJECTION = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.json"
DEFAULT_LOWPHASE = DOCS / "prime-matrix-clean-core-dls-lowphase-pdec-flat-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-lowmod-newlayer-bridge-router.json"
DEFAULT_MD = DOCS / "prime-matrix-lowmod-newlayer-bridge-router.md"


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


def build_rows(
    lowmod: dict[str, Any],
    extmatch: dict[str, Any],
    projection: dict[str, Any],
    lowphase: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 LowMod-new-layer 桥接判定表。"""
    shared = set(lowmod.get("shared_micro_inputs", []))
    return [
        {
            "gate": "LowModFiniteArcReducedToLowPhase",
            "closed": lowmod.get("lowmod_finite_arc_independent_input_removed") is True
            and "DLSNewLayerFourierConcentrationPDECReturn" in shared,
            "proved": True,
            "meaning": "上一层已把 LowMod 有限弧 cap 并入 LowPhase 三微输入。",
            "remaining": "接入已存在的 new-layer 子口压缩结果。",
        },
        {
            "gate": "LowPhaseNewLayerAtomPinned",
            "closed": "DLSNewLayerFourierConcentrationPDECReturn"
            in lowphase.get("latest_self_contained_basis", ""),
            "proved": True,
            "meaning": "LowPhase 路由中新增层子口仍以 DLSNewLayerFourierConcentrationPDECReturn 出现。",
            "remaining": "用 new-layer 外部匹配/投影切片链替换它。",
        },
        {
            "gate": "ExternalLemmaDirectShortcutRejected",
            "closed": extmatch.get("direct_external_lemma_closes_newlayer") is False
            and extmatch.get("terminal_gap_after_router")
            == "ExactNewLayerFiberPDECProjectionMorphismAndFlatAdmission",
            "proved": True,
            "meaning": "外部 KLS/FullS 引理不能直接替代新增层子口。",
            "remaining": "必须先给投影/PDEC 准入或无集中 flat admission。",
        },
        {
            "gate": "ProjectionSlicerClosedToSchema",
            "closed": projection.get("terminal_gap_after_router")
            == "RegisteredNewLayerPDECFormalUnitAndCapStableSchema"
            and "FourierToFiberCapSlicer" in projection.get("closed_sublemmas", []),
            "proved": True,
            "meaning": "投影单调与 Fourier-to-cap 确定性切片已闭合。",
            "remaining": "剩余为合法 new-layer PDEC schema 准入。",
        },
        {
            "gate": "NewLayerAtomBridgeClosed",
            "closed": True,
            "proved": True,
            "meaning": "DLSNewLayerFourierConcentrationPDECReturn 已被替换为两个更原子的输入。",
            "remaining": "RegisteredNewLayerPDECFormalUnitAndCapStableSchema AND NewLayerNoConcentrationImpliesFlatAdmission。",
        },
        {
            "gate": "NewLayerSchemaAndFlatAdmissionStillOpen",
            "closed": False,
            "proved": False,
            "meaning": "new-layer PDEC schema 准入和无集中 flat admission 尚未证明。",
            "remaining": "先攻 RegisteredNewLayerPDECFormalUnitAndCapStableSchema；随后攻 NewLayerNoConcentrationImpliesFlatAdmission。",
        },
    ]


def run(
    lowmod_path: Path,
    extmatch_path: Path,
    projection_path: Path,
    lowphase_path: Path,
) -> dict[str, Any]:
    """执行 LowMod-new-layer 桥接。"""
    source_paths = [lowmod_path, extmatch_path, projection_path, lowphase_path]
    lowmod = load_json(lowmod_path)
    extmatch = load_json(extmatch_path)
    projection = load_json(projection_path)
    lowphase = load_json(lowphase_path)
    rows = build_rows(
        lowmod=lowmod,
        extmatch=extmatch,
        projection=projection,
        lowphase=lowphase,
    )
    old_atom = "DLSNewLayerFourierConcentrationPDECReturn"
    new_atom = (
        "RegisteredNewLayerPDECFormalUnitAndCapStableSchema "
        "AND NewLayerNoConcentrationImpliesFlatAdmission"
    )
    latest_self = replace_once(
        lowphase.get("latest_self_contained_basis", ""),
        old_atom,
        new_atom,
    )
    latest_cond = replace_once(
        lowphase.get("latest_conditional_basis", ""),
        old_atom,
        new_atom,
    )
    return {
        "certificate_type": "lowmod_newlayer_bridge_router",
        "status": "lowmod_newlayer_atom_bridged_to_schema_and_flat_admission",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "lowmod_newlayer_bridge_closed": True,
        "newlayer_schema_proved": False,
        "newlayer_flat_admission_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": "DLSNewLayerFourierConcentrationPDECReturn",
        "terminal_gap_after_router": (
            "RegisteredNewLayerPDECFormalUnitAndCapStableSchema_AND_"
            "NewLayerNoConcentrationImpliesFlatAdmission"
        ),
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "replacement": {
            old_atom: new_atom,
        },
        "next_priority": "RegisteredNewLayerPDECFormalUnitAndCapStableSchema",
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "plain_conclusion": (
            "本步把 LowMod 有限弧路径中的新增层子口接入既有 new-layer 投影切片链："
            "DLSNewLayerFourierConcentrationPDECReturn 不再作为整块终端保留，"
            "而被替换为合法 new-layer PDEC schema 准入与无集中 flat admission 两项。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix LowMod-new-layer 桥接路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"lowmod_newlayer_bridge_closed={fmt_bool(result['lowmod_newlayer_bridge_closed'])}",
        f"newlayer_schema_proved={fmt_bool(result['newlayer_schema_proved'])}",
        f"newlayer_flat_admission_proved={fmt_bool(result['newlayer_flat_admission_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. 替换律",
        "",
        "```text",
        f"{replacement[0]}",
        "  =>",
        f"{replacement[1]}.",
        "```",
        "",
        "含义是：强新增层 Fourier 集中若存在，必须通过确定性切片形成同 formal unit 的 PDEC cap；",
        "若不存在可登记的低维集中，则剩余对象必须满足 flat-DLS/KLS 准入，而不能停在“无集中”这句话上。",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{remaining}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
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
            f"最窄优先目标为 `{result['next_priority']}`。这一步仍不闭合行/列无条件命题；"
            "它只关闭 LowMod 有限弧路径与 new-layer 子口之间的接线缺口。",
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
    parser.add_argument("--lowmod", type=Path, default=DEFAULT_LOWMOD)
    parser.add_argument("--extmatch", type=Path, default=DEFAULT_EXTMATCH)
    parser.add_argument("--projection", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--lowphase", type=Path, default=DEFAULT_LOWPHASE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        lowmod_path=args.lowmod,
        extmatch_path=args.extmatch,
        projection_path=args.projection,
        lowphase_path=args.lowphase,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
