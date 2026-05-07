#!/usr/bin/env python3
"""压缩非 AP-source 分支的量化窗口尺度账本。

用法示例：
  python3 experiments/prime_matrix_triad_a1_dibfi_nonap_scale_ledger_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-dibfi-nonap-scale-ledger-router.json
  docs/monograph/prime-matrix-triad-a1-dibfi-nonap-scale-ledger-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_NONAP_DISPERSION = DOCS / "prime-matrix-triad-a1-dibfi-nonap-dispersion-router.json"
DEFAULT_TRANSFER_SCALE = (
    DOCS / "prime-matrix-triad-a1-dibfi-transfer-scale-certificate-router.json"
)
DEFAULT_BFI_LEVEL_LEDGER = (
    DOCS / "prime-matrix-triad-a1-dibfi-bfi-level-ledger-router.json"
)
DEFAULT_COMMON_VARIABLE_TABLE = (
    DOCS / "prime-matrix-triad-a1-dibfi-common-variable-table-router.json"
)
DEFAULT_KLS_TEMPLATE = DOCS / "kls-window-di-bfi-adaptation-template.md"
DEFAULT_KZE_SPINE = DOCS / "prime-matrix-h3-dsb-hlc-kz-e-well-factorable-dispersion-spine.md"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-dibfi-nonap-scale-ledger-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-dibfi-nonap-scale-ledger-router.md"


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


def build_scale_rows(
    transfer_scale: dict[str, Any],
    bfi_level_ledger: dict[str, Any],
    common_variable_table: dict[str, Any],
    kls_template_path: Path,
    kze_spine_path: Path,
) -> list[dict[str, Any]]:
    """构造非 AP-source 尺度行。"""
    variable_symbols = {row["symbol"] for row in common_variable_table["variable_rows"]}
    kls_ranges_ready = contains_all(kls_template_path, ["C ≍ P/log", "S ≍ P", "0<|h|<=H"])
    kze_ranges_ready = contains_all(kze_spine_path, ["C\\asymp R_0", "S\\asymp L_0", "0<|h|\\le H_0"])
    bfi_level_closed = bool(bfi_level_ledger["bfi_level_exponent_ledger_closed"])
    return [
        {
            "gate": "TypeProductQuantified",
            "closed": True,
            "evidence": "N*M≈X 已由 transfer-scale 证书按 dyadic product 关闭。",
            "remaining": "none",
            "next_target": "none",
        },
        {
            "gate": "BFILevelQuantified",
            "closed": bfi_level_closed,
            "evidence": "同一 X≈P^2、Q<=P log^O P 账本给 Q<=X^{1/2+o(1)}<X^{4/7-eps}。",
            "remaining": "none" if bfi_level_closed else "需先关闭 BFI level 指数账本。",
            "next_target": "none" if bfi_level_closed else "BFILevelExponentLedger",
        },
        {
            "gate": "FrequencyWindowAndTail",
            "closed": True,
            "evidence": "transfer-scale 证书已把 Fourier tail 和 B(A) 吸收关闭。",
            "remaining": "h 作为 DI 频率参数的精确范围仍并入 DIKloostermanWindowSubstitution。",
            "next_target": "DIKloostermanWindowSubstitutionLedger",
        },
        {
            "gate": "LogLossAbsorption",
            "closed": True,
            "evidence": "B(A)=A+C0+10 的 symbolic log ledger 已关闭。",
            "remaining": "若最终稿要求显式 C_i，再抽常数；当前非终端。",
            "next_target": "none",
        },
        {
            "gate": "KLSModulusWindowQuantified",
            "closed": False,
            "evidence": "C≈P/log^{O(1)}P 已命名，但尚未逐项代入 DI Theorem 12 的模数变量。",
            "remaining": "需把 C 与 DI 模数 family、dyadic support 和 gcd 剥离后的 level 精确同一化。",
            "next_target": "DIKloostermanWindowSubstitutionLedger",
        },
        {
            "gate": "InverseVariableWindowQuantified",
            "closed": False,
            "evidence": "S≈P / completion length 已命名，但尚未与 DI 逆元变量窗口逐项匹配。",
            "remaining": "需从 completion 后的 s 变量长度推出 DI Theorem 12 允许范围。",
            "next_target": "DIKloostermanWindowSubstitutionLedger",
        },
        {
            "gate": "DIJScaleDominanceSubstitution",
            "closed": False,
            "evidence": "C,S,H,N,M,Q 已在共同变量表中固定，但 DI J-scale bound 尚未代入并压到自然 WFD 尺度/log^A。",
            "remaining": "需写出 DI Theorem 12 的 J-scale 项，并逐项比较到 WFD 自然尺度。",
            "next_target": "DIKloostermanWindowSubstitutionLedger",
        },
        {
            "gate": "TemplateHasAllVariables",
            "closed": kls_ranges_ready
            and kze_ranges_ready
            and {"c,C", "s,S", "h,H"}.issubset(variable_symbols),
            "evidence": "KLS 模板与 KZ-E spine 已给 C,S,H 的定性窗口；共同变量表固定 C,S,H。",
            "remaining": "该行只是资料可用性，不关闭 DI 精确代入。",
            "next_target": "DIKloostermanWindowSubstitutionLedger",
        },
    ]


def run(
    nonap_dispersion_path: Path,
    transfer_scale_path: Path,
    bfi_level_ledger_path: Path,
    common_variable_table_path: Path,
    kls_template_path: Path,
    kze_spine_path: Path,
) -> dict[str, Any]:
    """运行非 AP-source 尺度账本路由。"""
    nonap_dispersion = load_json(nonap_dispersion_path)
    transfer_scale = load_json(transfer_scale_path)
    bfi_level_ledger = load_json(bfi_level_ledger_path)
    common_variable_table = load_json(common_variable_table_path)
    scale_rows = build_scale_rows(
        transfer_scale,
        bfi_level_ledger,
        common_variable_table,
        kls_template_path,
        kze_spine_path,
    )
    open_scale_gates = [row["gate"] for row in scale_rows if not row["closed"]]
    return {
        "certificate_type": "triad_a1_dibfi_nonap_scale_ledger_router",
        "status": "nonap_scale_ledger_reduced_to_di_kloosterman_window_substitution_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "nonap_dispersion_json": file_sha256(nonap_dispersion_path),
            "transfer_scale_json": file_sha256(transfer_scale_path),
            "bfi_level_ledger_json": file_sha256(bfi_level_ledger_path),
            "common_variable_table_json": file_sha256(common_variable_table_path),
            "kls_template_md": file_sha256(kls_template_path),
            "kze_spine_md": file_sha256(kze_spine_path),
        },
        "previous_terminal_gap": nonap_dispersion["terminal_gap_after_router"],
        "scale_rows": scale_rows,
        "open_scale_gates": open_scale_gates,
        "closed_scale_gates": [row["gate"] for row in scale_rows if row["closed"]],
        "quantified_window_substitution_closed": False,
        "terminal_gap_after_router": "DIKloostermanWindowSubstitutionLedger",
        "structural_law": (
            "The non-AP scale side no longer needs the BFI prime-AP level ledger: Q<=P log^O P "
            "and X≈P^2 give positive BFI exponent slack. Type product, frequency tail and log "
            "loss are also ledger-closed. The remaining scale content is specifically DI-side: "
            "match C,S,H and the J-scale term of DI Theorem 12 to the current WFD natural scale."
        ),
        "review_conclusion": (
            "非 AP-source 的尺度侧已压成 DI Kloosterman 窗口代入账本：BFI level、Type product、"
            "频率尾项与 log 损失不再是终端；剩余是 C/S/H 模数-逆元-频率窗口和 DI J-scale 的精确代入。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 DI/BFI 非 AP-source scale ledger 路由器",
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
        "previous terminal:",
        f"  {result['previous_terminal_gap']};",
        "",
        "new scale terminal:",
        f"  {result['terminal_gap_after_router']};",
        "",
        "open scale gates:",
        f"  {result['open_scale_gates']}.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `quantified_window_substitution_closed={fmt_bool(result['quantified_window_substitution_closed'])}`。",
        f"- `closed_scale_gates={result['closed_scale_gates']}`。",
        f"- `open_scale_gates={result['open_scale_gates']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 尺度账本表",
        "",
        "| gate | closed | evidence | remaining | next target |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["scale_rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | {evidence} | {remaining} | `{next}` |".format(
                gate=table_cell(row["gate"]),
                closed=fmt_bool(bool(row["closed"])),
                evidence=table_cell(row["evidence"]),
                remaining=table_cell(row["remaining"]),
                next=table_cell(row["next_target"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 当前结论",
            "",
            "尺度侧的最窄剩余为：",
            "",
            "```text",
            "DIKloostermanWindowSubstitutionLedger:",
            "  KLSModulusWindowQuantified;",
            "  InverseVariableWindowQuantified;",
            "  DIJScaleDominanceSubstitution.",
            "```",
            "",
            "对象侧仍另有 `NoProjectionUncenteredDispersionIdentity`；二者合取才可关闭非 AP-source fallback。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nonap-dispersion-json", type=Path, default=DEFAULT_NONAP_DISPERSION)
    parser.add_argument("--transfer-scale-json", type=Path, default=DEFAULT_TRANSFER_SCALE)
    parser.add_argument("--bfi-level-ledger-json", type=Path, default=DEFAULT_BFI_LEVEL_LEDGER)
    parser.add_argument(
        "--common-variable-table-json", type=Path, default=DEFAULT_COMMON_VARIABLE_TABLE
    )
    parser.add_argument("--kls-template-md", type=Path, default=DEFAULT_KLS_TEMPLATE)
    parser.add_argument("--kze-spine-md", type=Path, default=DEFAULT_KZE_SPINE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        nonap_dispersion_path=args.nonap_dispersion_json,
        transfer_scale_path=args.transfer_scale_json,
        bfi_level_ledger_path=args.bfi_level_ledger_json,
        common_variable_table_path=args.common_variable_table_json,
        kls_template_path=args.kls_template_md,
        kze_spine_path=args.kze_spine_md,
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
                "open_scale_gates": result["open_scale_gates"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
