#!/usr/bin/env python3
"""Prime Matrix DLS point-load/ColumnCRT 命名回流 schema 路由器。

用法示例：
  python3 experiments/prime_matrix_dls_pointload_columncrt_return_schema_router.py

输出：
  docs/monograph/prime-matrix-dls-pointload-columncrt-return-schema-router.json
  docs/monograph/prime-matrix-dls-pointload-columncrt-return-schema-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-dls-shortwindow-sae-return-schema-router.json"
DEFAULT_DLS = DOCS / "prime-matrix-clean-core-bes-dls-named-return-router.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"
DEFAULT_DISPLACEMENT = DOCS / "prime-matrix-columncrt-displacement-pdec-absorption.md"
DEFAULT_TAIL = DOCS / "prime-matrix-tailanchor-cofactor-absorption-contract.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SPARSE = DOCS / "prime-matrix-future-sparse-packet-extractor-schema-boundary-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-dls-pointload-columncrt-return-schema-router.json"
DEFAULT_MD = DOCS / "prime-matrix-dls-pointload-columncrt-return-schema-router.md"

OLD_ATOM = "DLSPointLoadColumnCRTBoundOrNamedReturn"
NEW_ATOM = "NoDLSPointLoadColumnCRTSpecificGap_AfterDisplacementPDECOrSAEReturn"
NEXT_ATOM = "DLSFixedWheelUnitPeakDilutionOrPDECReturn"


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
    """从输入基中删除已回流的 point-load 专属 gap 标记。"""
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
    dls_text: str,
    column_text: str,
    displacement_text: str,
    tail_text: str,
    pdec_text: str,
    sparse_text: str,
) -> list[dict[str, Any]]:
    """生成 DLS point-load/ColumnCRT 命名回流 schema 判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    pointload_alphabet = (
        OLD_ATOM in dls_text
        and "PointLoad" in dls_text
        and "ColumnCRT / tail-anchor / displacement PDEC" in dls_text
    )
    column_absorbed = (
        "columncrt_independent_terminal_removed=true" in column_text
        and "ColumnCRTDisplacementAbsorption" in column_text
        and "PDEC/SAE" in column_text
    )
    displacement_signature = (
        "sigma_col" in displacement_text
        and "displacement PDEC" in displacement_text
        and "Sparse displacement" in displacement_text
        and "Persistent displacement" in displacement_text
    )
    balanced_cannot_pay = (
        "Balanced displacement" in displacement_text
        and "不能承担命名缺陷预算" in displacement_text
    )
    tail_anchor_absorbed = (
        "tailanchor_cofactor_absorbed_to_pdec_sae_columncrt_not_closed" in tail_text
        and "persistent anchor => PDEC / ColumnCRT" in tail_text
        and "sparse anchor     => SAE" in tail_text
    )
    pdec_boundary = (
        "pdec_family_explicit_input_boundary_closed=true" in pdec_text
        and "同一个 formal unit" in pdec_text
    )
    sparse_boundary = (
        "future_sparse_packet_schema_boundary_closed=true" in sparse_text
        and "FutureExplicitSparsePacketExtractorSchema" in sparse_text
    )
    schema_closed = all(
        [
            active,
            pointload_alphabet,
            column_absorbed,
            displacement_signature,
            balanced_cannot_pay,
            tail_anchor_absorbed,
            pdec_boundary,
            sparse_boundary,
        ]
    )
    return [
        row(
            "DLSPointLoadGateActive",
            active,
            True,
            "当前输入基仍含 DLSPointLoadColumnCRTBoundOrNamedReturn，且它来自 BES/DLS 三出口字母表。",
            "本步只攻击 point-load 专属无名出口。",
        ),
        row(
            "PointLoadAlphabetPinned",
            pointload_alphabet,
            True,
            "DLS 点负载只能回流 ColumnCRT、tail-anchor 或 displacement PDEC。",
            "不能作为 BES 同步失败黑箱。",
        ),
        row(
            "ColumnCRTIndependentExitAbsorbed",
            column_absorbed,
            True,
            "ColumnCRT 不是独立终端；持久非零位移是 displacement PDEC，孤立位移是 SAE/endpoint。",
            "位移 PDEC/SAE 终端排斥仍未证明。",
        ),
        row(
            "FiniteDisplacementSignature",
            displacement_signature,
            True,
            "点负载若持续，给出有限列位移签名 sigma_col=(ell,d mod ell) 或其细化。",
            "同签名持久进入 PDEC。",
        ),
        row(
            "BalancedPointLoadCannotPayDefectBudget",
            balanced_cannot_pay,
            True,
            "若所有非零位移余类均不超载，则 ColumnCRT/point-load 不能承担命名缺陷预算。",
            "这是 BoundOrNamedReturn 中的 bound 侧。",
        ),
        row(
            "TailAnchorPointLoadAbsorbed",
            tail_anchor_absorbed,
            True,
            "若 point-load 实为尾锚/互补因子锚，持久进 PDEC/ColumnCRT，孤立进 SAE。",
            "尾锚排斥仍归终端证书。",
        ),
        row(
            "PersistentPointLoadAdmitsPDEC",
            pdec_boundary,
            True,
            "同一 point-load/位移/尾锚签名持久复现，必须作为显式 PDEC schema 准入。",
            "PDEC family 无条件排斥仍开放。",
        ),
        row(
            "SparsePointLoadAdmitsSAE",
            sparse_boundary,
            True,
            "若 point-load 只孤立出现，必须物化为有限 SAE/LocalSurvivor packet schema。",
            "不是全局 sparse family 无条件排斥。",
        ),
        row(
            "NoDLSPointLoadSpecificFourthExit",
            schema_closed,
            True,
            "point-load 只有平衡不足、持久 PDEC/ColumnCRT、孤立 SAE 或 tail-anchor 回流，没有专属第四出口。",
            NEW_ATOM,
        ),
        row(
            OLD_ATOM,
            schema_closed,
            True,
            "该硬点作为 point-load 命名回流 schema 已闭合。",
            "不等于全局 PDEC/ColumnCRT/SAE 排斥已证明。",
        ),
        row(
            NEXT_ATOM,
            False,
            False,
            "Fixed-wheel 单位类峰稀释或 PDEC 回流仍是最新最窄微输入。",
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
    dls_path: Path,
    column_path: Path,
    displacement_path: Path,
    tail_path: Path,
    pdec_path: Path,
    sparse_path: Path,
) -> dict[str, Any]:
    """执行 DLS point-load/ColumnCRT 命名回流 schema 路由。"""
    source_paths = [
        previous_path,
        dls_path,
        column_path,
        displacement_path,
        tail_path,
        pdec_path,
        sparse_path,
    ]
    previous = load_json(previous_path)
    dls_text = dls_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    displacement_text = displacement_path.read_text(encoding="utf-8")
    tail_text = tail_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sparse_text = sparse_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        dls_text=dls_text,
        column_text=column_text,
        displacement_text=displacement_text,
        tail_text=tail_text,
        pdec_text=pdec_text,
        sparse_text=sparse_text,
    )
    schema_closed = next(bool(item["closed"]) for item in rows if item["gate"] == OLD_ATOM)
    replaced_self = replace_once(previous.get("latest_self_contained_basis", ""), OLD_ATOM, NEW_ATOM)
    replaced_cond = replace_once(previous.get("latest_conditional_basis", ""), OLD_ATOM, NEW_ATOM)
    latest_self = remove_closed_gap(replaced_self)
    latest_cond = remove_closed_gap(replaced_cond)
    return {
        "certificate_type": "dls_pointload_columncrt_return_schema_router",
        "status": "dls_pointload_columncrt_return_schema_closed_terminal_exclusion_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "dls_pointload_return_schema_closed": schema_closed,
        "dls_pointload_specific_gap_removed": schema_closed,
        "columncrt_independent_terminal_removed": schema_closed,
        "pdec_columncrt_sae_terminal_exclusion_proved": False,
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
            "本步闭合的是 DLS point-load/ColumnCRT 的专属命名回流 schema："
            "单点高负载若平衡则不能支付缺陷预算；若持久则给出有限列位移或尾锚签名并进入 PDEC/ColumnCRT；"
            "若孤立则进入 SAE/LocalSurvivor packet。因此 point-load 专属无名出口被删除；"
            "但 PDEC/ColumnCRT/SAE 终端排斥和 fixed-wheel 微输入仍未证明。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix DLS point-load/ColumnCRT 命名回流 schema 路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"dls_pointload_return_schema_closed={fmt_bool(result['dls_pointload_return_schema_closed'])}",
        f"dls_pointload_specific_gap_removed={fmt_bool(result['dls_pointload_specific_gap_removed'])}",
        (
            "columncrt_independent_terminal_removed="
            f"{fmt_bool(result['columncrt_independent_terminal_removed'])}"
        ),
        (
            "pdec_columncrt_sae_terminal_exclusion_proved="
            f"{fmt_bool(result['pdec_columncrt_sae_terminal_exclusion_proved'])}"
        ),
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
            f"point-load 专属 gap 已删除。下一步最窄目标转到 `{result['next_priority']}`："
            "证明固定轮单位类峰被层叠轮稀释，或把持久单位峰登记为 PDEC。",
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
    parser.add_argument("--dls", type=Path, default=DEFAULT_DLS)
    parser.add_argument("--column", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--displacement", type=Path, default=DEFAULT_DISPLACEMENT)
    parser.add_argument("--tail", type=Path, default=DEFAULT_TAIL)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sparse", type=Path, default=DEFAULT_SPARSE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        dls_path=args.dls,
        column_path=args.column,
        displacement_path=args.displacement,
        tail_path=args.tail,
        pdec_path=args.pdec,
        sparse_path=args.sparse,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
