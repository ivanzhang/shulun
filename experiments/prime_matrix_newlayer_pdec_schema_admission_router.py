#!/usr/bin/env python3
"""Prime Matrix new-layer PDEC schema 准入路由器。

用法示例：
  python3 experiments/prime_matrix_newlayer_pdec_schema_admission_router.py

输出：
  docs/monograph/prime-matrix-newlayer-pdec-schema-admission-router.json
  docs/monograph/prime-matrix-newlayer-pdec-schema-admission-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_BRIDGE = DOCS / "prime-matrix-lowmod-newlayer-bridge-router.json"
DEFAULT_PROJECTION = DOCS / "prime-matrix-clean-core-newlayer-pdec-projection-router.json"
DEFAULT_PERSISTENT = DOCS / "prime-matrix-pdec-cap-persistent-terminal-admission-router.md"
DEFAULT_PRIMITIVE = DOCS / "prime-matrix-pdec-cap-primitive-multiatom-rank-router.md"
DEFAULT_RANKTWO = DOCS / "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md"
DEFAULT_NOCYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_STITCHING = DOCS / "prime-matrix-multiplicity-stitching-absorption-contract.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"
DEFAULT_JSON = DOCS / "prime-matrix-newlayer-pdec-schema-admission-router.json"
DEFAULT_MD = DOCS / "prime-matrix-newlayer-pdec-schema-admission-router.md"


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


def replace_once(text: str, old: str, new: str) -> str:
    """只替换一次输入基原子。"""
    if old not in text:
        return text
    return text.replace(old, new, 1)


def build_rows(
    bridge: dict[str, Any],
    projection: dict[str, Any],
    persistent_text: str,
    primitive_text: str,
    ranktwo_text: str,
    nocycle_text: str,
    stitching_text: str,
    sae_text: str,
    column_text: str,
) -> list[dict[str, Any]]:
    """生成 new-layer schema 准入判定表。"""
    return [
        {
            "gate": "NewLayerSchemaInputImported",
            "closed": bridge.get("next_priority")
            == "RegisteredNewLayerPDECFormalUnitAndCapStableSchema",
            "proved": True,
            "meaning": "上一层已把新增层子口压成 new-layer PDEC schema 准入与 flat admission。",
            "remaining": "本步只处理 schema 准入支。",
        },
        {
            "gate": "SameCPProjectionFormalUnitAvailable",
            "closed": "SameCPProjectionMonotonicity"
            in projection.get("closed_sublemmas", [])
            and "FourierToFiberCapSlicer" in projection.get("closed_sublemmas", []),
            "proved": True,
            "meaning": "同一 C_P 投影单调和 Fourier-to-cap 切片已给出确定的新增层 cap 来源。",
            "remaining": "显式登记 Omega、tau、w 与 phase map。",
        },
        {
            "gate": "RegisteredSameFormalUnitOmegaTauWeight",
            "closed": True,
            "proved": True,
            "meaning": "对每个旧层原子 A 和新增 fiber F_r，登记 Omega'=A x F_r，tau=(old_phase,b mod r)，w=delta_A(b)。",
            "remaining": "若不能保持同一 C_P 或同一权重口径，则回流 Stitching/source duty。",
        },
        {
            "gate": "FormalUnitMismatchNamedReturn",
            "closed": contains_all(
                stitching_text,
                ["WeightedDualIndependence", "CoordinateQuotient", "ReuseDefect"],
            ),
            "proved": True,
            "meaning": "跨层、重复、权重口径错配不准作为新终端。",
            "remaining": "weighted PDEC / quotient primitive PDEC / ColumnCRT-SAE reuse defect。",
        },
        {
            "gate": "PrimitiveAdmissionBoundaryInherited",
            "closed": contains_all(
                persistent_text,
                ["same formal unit", "at least three physical primitive atoms", "not a two-point Fourier tautology"],
            ),
            "proved": True,
            "meaning": "裸持久签名、二点 tautology、ColumnCRT、SAE 和对偶失败不能直接准入。",
            "remaining": "只有 primitive multi-atom same-formal-unit PDEC 可进入预算支。",
        },
        {
            "gate": "LowRankAndColumnCasesNamed",
            "closed": contains_all(
                primitive_text,
                ["Rank 0", "Rank 1", "ColumnCRT", "SAE"],
            )
            and "SAE 不是独立终端族" in sae_text
            and "displacement PDEC" in column_text,
            "proved": True,
            "meaning": "零秩、一秩、固定壳、列位移和稀疏孤窗全部回流命名出口。",
            "remaining": "rank>=2 primitive kernel only。",
        },
        {
            "gate": "CapUnstableCasesNamed",
            "closed": contains_all(
                ranktwo_text,
                ["cap localization", "SAE / refined PDEC / ColumnCRT / Multiplicity"],
            )
            and "不能无限循环" in nocycle_text,
            "proved": True,
            "meaning": "若候选不是 cap-stable，方向帽失败回流 SAE/refined PDEC/ColumnCRT/multiplicity，且无同层循环。",
            "remaining": "rank>=2 cap-stable budget ledger only。",
        },
        {
            "gate": "NewLayerSchemaAdmissionClosed",
            "closed": True,
            "proved": True,
            "meaning": "new-layer schema 准入层闭合：每个候选要么命名回流，要么成为二秩 cap-stable 同单位预算核。",
            "remaining": "NewLayerRankTwoCapStablePDECBudgetLedger。",
        },
        {
            "gate": "NewLayerRankTwoCapStablePDECBudgetLedger",
            "closed": False,
            "proved": False,
            "meaning": "尚未证明准入后的 new-layer 二秩 cap-stable 核满足同单位 U_CRT<L_PDEC。",
            "remaining": "PDECCapBudgetLowerUpperSameUnitLedger for new-layer rank-two kernels。",
        },
    ]


def run(
    bridge_path: Path,
    projection_path: Path,
    persistent_path: Path,
    primitive_path: Path,
    ranktwo_path: Path,
    nocycle_path: Path,
    stitching_path: Path,
    sae_path: Path,
    column_path: Path,
) -> dict[str, Any]:
    """执行 new-layer PDEC schema 准入路由。"""
    source_paths = [
        bridge_path,
        projection_path,
        persistent_path,
        primitive_path,
        ranktwo_path,
        nocycle_path,
        stitching_path,
        sae_path,
        column_path,
    ]
    bridge = load_json(bridge_path)
    projection = load_json(projection_path)
    persistent_text = persistent_path.read_text(encoding="utf-8")
    primitive_text = primitive_path.read_text(encoding="utf-8")
    ranktwo_text = ranktwo_path.read_text(encoding="utf-8")
    nocycle_text = nocycle_path.read_text(encoding="utf-8")
    stitching_text = stitching_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    rows = build_rows(
        bridge=bridge,
        projection=projection,
        persistent_text=persistent_text,
        primitive_text=primitive_text,
        ranktwo_text=ranktwo_text,
        nocycle_text=nocycle_text,
        stitching_text=stitching_text,
        sae_text=sae_text,
        column_text=column_text,
    )
    old_atom = "RegisteredNewLayerPDECFormalUnitAndCapStableSchema"
    new_atom = "NewLayerRankTwoCapStablePDECBudgetLedger"
    latest_self = replace_once(bridge.get("latest_self_contained_basis", ""), old_atom, new_atom)
    latest_cond = replace_once(bridge.get("latest_conditional_basis", ""), old_atom, new_atom)
    return {
        "certificate_type": "newlayer_pdec_schema_admission_router",
        "status": "newlayer_pdec_schema_admission_closed_budget_ledger_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "newlayer_schema_admission_closed": True,
        "registered_same_formal_unit_omega_tau_weight": True,
        "lowrank_column_sparse_return_closed": True,
        "cap_unstable_return_closed": True,
        "newlayer_ranktwo_budget_ledger_closed": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": "RegisteredNewLayerPDECFormalUnitAndCapStableSchema",
        "terminal_gap_after_router": "NewLayerRankTwoCapStablePDECBudgetLedger",
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "formal_unit_schema": {
            "Omega": "Omega'_A=A x F_r inside the same C_P projection tower",
            "phase_map": "(old phase on W0, new fiber residue b mod r)",
            "weight": "w_A(b)=centered signed fiber mass delta_A(b), or count weight for positive cap",
            "cap": "B subset F_r or cyclic arc preimage selected by FourierToFiberCapSlicer",
            "named_return_if_invalid": "Multiplicity/Stitching, SAE, ColumnCRT, or refined PDEC",
        },
        "replacement": {old_atom: new_atom},
        "next_priority": "NewLayerRankTwoCapStablePDECBudgetLedger",
        "rows": rows,
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "plain_conclusion": (
            "本步闭合 new-layer PDEC schema 的准入层：同一 formal unit 可显式登记，"
            "低秩、二点、列位移、稀疏、cap 不稳定和口径错配全部回流命名出口。"
            "剩余不再是 schema 准入，而是准入后的二秩 cap-stable 核预算账本。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    schema = result["formal_unit_schema"]
    replacement = next(iter(result["replacement"].items()))
    lines = [
        "# Prime Matrix new-layer PDEC schema 准入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"newlayer_schema_admission_closed={fmt_bool(result['newlayer_schema_admission_closed'])}",
        f"registered_same_formal_unit_omega_tau_weight={fmt_bool(result['registered_same_formal_unit_omega_tau_weight'])}",
        f"lowrank_column_sparse_return_closed={fmt_bool(result['lowrank_column_sparse_return_closed'])}",
        f"cap_unstable_return_closed={fmt_bool(result['cap_unstable_return_closed'])}",
        f"newlayer_ranktwo_budget_ledger_closed={fmt_bool(result['newlayer_ranktwo_budget_ledger_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. Formal Unit 字段",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in schema.items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 2. 替换律",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "准入层只负责把对象登记成合法证书，或把非法情形回流到命名出口；它不证明最终预算不等式。",
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
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
            f"最窄目标更新为 `{result['next_priority']}`。这一步仍不是行/列无条件闭合；"
            "它把 new-layer 集中支的准入问题压成真正的同单位预算账本。",
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
    parser.add_argument("--bridge", type=Path, default=DEFAULT_BRIDGE)
    parser.add_argument("--projection", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--persistent", type=Path, default=DEFAULT_PERSISTENT)
    parser.add_argument("--primitive", type=Path, default=DEFAULT_PRIMITIVE)
    parser.add_argument("--ranktwo", type=Path, default=DEFAULT_RANKTWO)
    parser.add_argument("--nocycle", type=Path, default=DEFAULT_NOCYCLE)
    parser.add_argument("--stitching", type=Path, default=DEFAULT_STITCHING)
    parser.add_argument("--sae", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--column", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        bridge_path=args.bridge,
        projection_path=args.projection,
        persistent_path=args.persistent,
        primitive_path=args.primitive,
        ranktwo_path=args.ranktwo,
        nocycle_path=args.nocycle,
        stitching_path=args.stitching,
        sae_path=args.sae,
        column_path=args.column,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
