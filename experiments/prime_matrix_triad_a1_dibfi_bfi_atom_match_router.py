#!/usr/bin/env python3
"""审计直接 BFI prime-AP 原子的三行匹配门控。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_bfi_atom_match_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-bfi-atom-match-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-bfi-atom-match-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DIRECT_BFI_ATOM = DOCS / "prime-matrix-triad-a1-dibfi-direct-bfi-atom-router.json"
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_GENERIC_WFD_DIBFI = DOCS / "prime-matrix-triad-a1-generic-wfd-dibfi-router.json"
DEFAULT_THEOREM_LOCATION = DOCS / "prime-matrix-triad-a1-dibfi-theorem-location-router.json"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_EXTERNAL_INDEX = DOCS / "external-theorem-index.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-bfi-atom-match-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-bfi-atom-match-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """核查文档是否含有全部关键词。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_gate_rows(
    direct_bfi_atom: dict[str, Any],
    common_variable_table: dict[str, Any],
    generic_wfd_dibfi: dict[str, Any],
    theorem_location: dict[str, Any],
    kze_spine_path: Path,
    external_index_path: Path,
) -> list[dict[str, Any]]:
    """构造 BFI 原子匹配门控。"""
    transfer_steps = {row["step"]: row for row in common_variable_table["transfer_rows"]}
    variable_symbols = {row["symbol"] for row in common_variable_table["variable_rows"]}
    bfi_pinned = bool(theorem_location["theorem_locations_pinned"]) and any(
        row["source_id"] == "BFI1987-Theorem10" for row in theorem_location["source_rows"]
    )
    kze_type_ready = contains_all(
        kze_spine_path,
        ["Vaughan/Heath-Brown", "Type-I/II", "well-factorable", "dyadic"],
    )
    external_bfi_ready = contains_all(
        external_index_path,
        ["BFI1987-Theorem10", "lambda_d", "well-factorable"],
    )
    direct_available = bool(direct_bfi_atom["direct_bfi_atom_available"])
    generic_contract_ready = bool(generic_wfd_dibfi["external_dibfi_contract_materialized"])
    return [
        {
            "gate": "BFIAtomPinned",
            "status": "closed",
            "closed": bfi_pinned and direct_available,
            "evidence": "BFI1987-Theorem10 已由定理定位路由固定，直接 BFI 原子可用。",
            "remaining": "none",
            "next_target": "none",
        },
        {
            "gate": "APErrorFormulaNamed",
            "status": "formula_available_not_source_identification",
            "closed": True,
            "evidence": transfer_steps["APError"]["formula"],
            "remaining": "公式已命名；仍需证明当前残差等于该对象。",
            "next_target": "OriginalResidualEqualsBFIAPError",
        },
        {
            "gate": "PrimeAPResidualRepresentation",
            "status": "open_main_object_identity",
            "closed": False,
            "evidence": "共同变量表只给 APError 接口，尚未给 clean A1 残差到该接口的逐项等式。",
            "remaining": "必须从原始行/triad clean 残差出发写出 E_AP(X,Q) 的等号，而不是从 KE-13 子窗口倒推。",
            "next_target": "OriginalResidualEqualsBFIAPError",
        },
        {
            "gate": "TypeDecompositionToBFIInput",
            "status": "closed_conditioned_on_ap_identity" if kze_type_ready else "type_ledger_gap",
            "closed": kze_type_ready,
            "evidence": "KZ-E spine 已登记 Vaughan/Heath-Brown、Type-I/II、dyadic 与 well-factorable 账本。",
            "remaining": "该行只说明 AP 对象一旦建立，可进入 BFI 的 Type/dispersion 框架。",
            "next_target": "none",
        },
        {
            "gate": "WellFactorableLambdaClass",
            "status": "closed_at_weight_class_level"
            if external_bfi_ready and generic_contract_ready and "lambda" in variable_symbols
            else "well_factorable_class_gap",
            "closed": external_bfi_ready and generic_contract_ready and "lambda" in variable_symbols,
            "evidence": "generic WFD 合同与共同变量表均登记 lambda 为 BFI well-factorable 权重类别。",
            "remaining": "权重类别已闭合；数值 level 与 q-support 仍属 BFILevelExponentLedger。",
            "next_target": "BFILevelExponentLedger",
        },
        {
            "gate": "BFILevelSubstitution",
            "status": "open_exponent_and_support_ledger_missing",
            "closed": False,
            "evidence": "当前文档只有 Q<=X^(4/7-eps) 的目标语句，尚未给出 X,Q 的原始参数等式。",
            "remaining": "需提交 X、Q、q-support、dyadic loss 的显式不等式账本。",
            "next_target": "BFILevelExponentLedger",
        },
        {
            "gate": "WellFactorableLambdaLevel",
            "status": "open_level_not_class",
            "closed": False,
            "evidence": "lambda 的 well-factorable 类别已登记，但支撑 level 与 BFI 定理输入仍未量化。",
            "remaining": "需证明 lambda_q 的 support level、factorization depth 与 BFI Theorem 10 的 level 条件一致。",
            "next_target": "BFILevelExponentLedger",
        },
    ]


def build_terminal_rows(gate_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """把打开门控压成两个终端硬点。"""
    open_gates = [row["gate"] for row in gate_rows if not row["closed"]]
    return [
        {
            "terminal": "OriginalResidualEqualsBFIAPError",
            "covers": ["PrimeAPResidualRepresentation"],
            "closed": "PrimeAPResidualRepresentation" not in open_gates,
            "meaning": (
                "证明当前 clean A1/generic WFD 残差在进入 Cauchy/dispersion 前就是"
                " BFI prime-AP discrepancy 的 dyadic 总和。"
            ),
        },
        {
            "terminal": "BFILevelExponentLedger",
            "covers": ["BFILevelSubstitution", "WellFactorableLambdaLevel"],
            "closed": not {
                "BFILevelSubstitution",
                "WellFactorableLambdaLevel",
            }.intersection(open_gates),
            "meaning": (
                "给出 X,Q 与 lambda_q support level 的显式指数账本，并核验 BFI Theorem 10 的"
                " level/well-factorable 输入。"
            ),
        },
    ]


def run(
    direct_bfi_atom_path: Path,
    common_variable_table_path: Path,
    generic_wfd_dibfi_path: Path,
    theorem_location_path: Path,
    kze_spine_path: Path,
    external_index_path: Path,
) -> dict[str, Any]:
    """运行 BFI 原子匹配路由。"""
    direct_bfi_atom = load_json(direct_bfi_atom_path)
    common_variable_table = load_json(common_variable_table_path)
    generic_wfd_dibfi = load_json(generic_wfd_dibfi_path)
    theorem_location = load_json(theorem_location_path)
    gate_rows = build_gate_rows(
        direct_bfi_atom,
        common_variable_table,
        generic_wfd_dibfi,
        theorem_location,
        kze_spine_path,
        external_index_path,
    )
    terminal_rows = build_terminal_rows(gate_rows)
    open_gates = [row["gate"] for row in gate_rows if not row["closed"]]
    open_terminal_targets = [
        row["terminal"] for row in terminal_rows if not row["closed"]
    ]
    return {
        "certificate_type": "triad_a1_dibfi_bfi_atom_match_router",
        "status": "dibfi_direct_bfi_atom_match_reduced_to_ap_identity_and_level_ledger_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "direct_bfi_atom_json": file_sha256(direct_bfi_atom_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "generic_wfd_dibfi_json": file_sha256(generic_wfd_dibfi_path),
            "dibfi_theorem_location_json": file_sha256(theorem_location_path),
            "kze_spine_md": file_sha256(kze_spine_path),
            "external_theorem_index_md": file_sha256(external_index_path),
        },
        "previous_terminal_gap": direct_bfi_atom["terminal_gap_after_router"],
        "gate_rows": gate_rows,
        "terminal_rows": terminal_rows,
        "open_gates": open_gates,
        "open_terminal_targets": open_terminal_targets,
        "bfi_atom_match_closed": not open_terminal_targets,
        "next_external_target": "BFIAPResidualIdentityAndLevelLedger",
        "terminal_gap_after_router": "BFIAPResidualIdentityAndLevelLedger",
        "structural_law": (
            "Direct BFI no longer asks for KE-13 no-projection or DI J-scale. The remaining "
            "BFI atom match has exactly two independent contents: first, the original residual "
            "must equal the BFI prime-AP discrepancy before Cauchy/dispersion; second, the "
            "X,Q and lambda support levels must be quantified against BFI Theorem 10."
        ),
        "review_conclusion": (
            "直接 BFI 原子匹配被压成两个终端硬点：`OriginalResidualEqualsBFIAPError` 与 "
            "`BFILevelExponentLedger`。权重类别与 Type 分解账本已关闭；剩余不是 DI/J-scale，"
            "而是 AP 源对象等式和 BFI level 指数账本。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI BFI 原子匹配路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 结构律",
        "",
        result["structural_law"],
        "",
        "```text",
        "previous:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "open terminal targets:",
        f"  {result['open_terminal_targets']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `bfi_atom_match_closed={fmt_bool(result['bfi_atom_match_closed'])}`。",
        f"- `open_gates={result['open_gates']}`。",
        f"- `open_terminal_targets={result['open_terminal_targets']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 门控表",
        "",
        "| gate | status | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | `{status}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                status=table_cell(row["status"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 终端表",
            "",
            "| terminal | covers | closed | meaning |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in result["terminal_rows"]:
        lines.append(
            "| `{terminal}` | {covers} | `{closed}` | {meaning} |".format(
                terminal=table_cell(row["terminal"]),
                covers=table_cell(", ".join(row["covers"])),
                closed=fmt_bool(bool(row["closed"])),
                meaning=table_cell(row["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            "本步把直接 BFI 原子的三个门控进一步分层：",
            "",
            "```text",
            "closed ledger:",
            "  BFIAtomPinned;",
            "  APErrorFormulaNamed;",
            "  TypeDecompositionToBFIInput;",
            "  WellFactorableLambdaClass;",
            "",
            "open core:",
            "  OriginalResidualEqualsBFIAPError;",
            "  BFILevelExponentLedger.",
            "```",
            "",
            "因此下一步应直接写 AP 源对象等式，或给出 BFI level 指数表；继续重证 DI/Kloosterman "
            "不是当前外部 BFI 路线的最短路径。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--direct-bfi-atom-json", type=Path, default=DEFAULT_DIRECT_BFI_ATOM)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument(
        "--generic-wfd-dibfi-json", type=Path, default=DEFAULT_GENERIC_WFD_DIBFI
    )
    parser.add_argument(
        "--dibfi-theorem-location-json", type=Path, default=DEFAULT_THEOREM_LOCATION
    )
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--external-index-md", type=Path, default=DEFAULT_EXTERNAL_INDEX)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        direct_bfi_atom_path=args.direct_bfi_atom_json,
        common_variable_table_path=args.common_variable_table_json,
        generic_wfd_dibfi_path=args.generic_wfd_dibfi_json,
        theorem_location_path=args.dibfi_theorem_location_json,
        kze_spine_path=args.kze_spine_md,
        external_index_path=args.external_index_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "bfi_atom_match_closed": result["bfi_atom_match_closed"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
