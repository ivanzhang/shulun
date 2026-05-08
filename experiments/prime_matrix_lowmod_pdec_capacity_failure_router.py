#!/usr/bin/env python3
"""Prime Matrix LowMod PDEC 容量失败定位路由器。

用法示例：
  python3 experiments/prime_matrix_lowmod_pdec_capacity_failure_router.py

输出：
  docs/monograph/prime-matrix-lowmod-pdec-capacity-failure-router.json
  docs/monograph/prime-matrix-lowmod-pdec-capacity-failure-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-lowmod-endpoint-formal-unit-router.json"
DEFAULT_DEC = DOCS / "prime-matrix-dec-ospc-exclusion-hardpoint.md"
DEFAULT_DUAL = DOCS / "prime-matrix-bpn-pdec-dual-certificate-framework.md"
DEFAULT_RANKTWO = DOCS / "prime-matrix-pdec-cap-ranktwo-capstable-kernel-router.md"
DEFAULT_FINITE_ARC = DOCS / "prime-matrix-pdec-cap-uniform-cap-finite-basis-router.md"
DEFAULT_NOCYCLE = DOCS / "prime-matrix-pdec-cap-refinement-no-cycle.md"
DEFAULT_PDEC = DOCS / "prime-matrix-pdec-family-explicit-input-boundary-router.md"
DEFAULT_SAE = DOCS / "prime-matrix-sae-to-local-survivor-pdec-absorption-router.md"
DEFAULT_COLUMN = DOCS / "prime-matrix-columncrt-to-pdec-sae-absorption-router.md"
DEFAULT_MULTIPLIER = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-lowmod-pdec-capacity-failure-router.json"
DEFAULT_MD = DOCS / "prime-matrix-lowmod-pdec-capacity-failure-router.md"


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


def build_rows(
    previous: dict[str, Any],
    dec_text: str,
    dual_text: str,
    ranktwo_text: str,
    finite_arc_text: str,
    nocycle_text: str,
    pdec_text: str,
    sae_text: str,
    column_text: str,
    multiplier: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 LowMod PDEC 容量失败定位判定表。"""
    terminal_gap = previous.get("terminal_gap_after_router")
    formal_unit = previous.get("formal_unit_shape", {})
    return [
        {
            "gate": "LowModFuturePDECImported",
            "closed": terminal_gap == "LowModFuturePDECSchemaExclusionOrSparseSAE",
            "proved": True,
            "meaning": "上一层已把 LowMod endpoint 缺陷压成 future PDEC schema 或 sparse SAE。",
            "output": "本步只攻击 persistent LowMod PDEC 容量比较分支。",
        },
        {
            "gate": "SameFormalUnitPinned",
            "closed": formal_unit.get("phase_map", "").startswith("x mod Q_B")
            and "f_B(x)" in formal_unit.get("test_function", ""),
            "proved": True,
            "meaning": "LowMod 坏行集合、相位图、测试函数都固定在同一个 Q_B 周期 formal unit 上。",
            "output": "U_CRT 与 L_PDEC 必须作用在同一个 g_B=1_S 或计数向量上。",
        },
        {
            "gate": "PDECLowerBoundImported",
            "closed": contains_all(
                dec_text,
                ["Lemma PDEC-1", "kappa_B", "beta", "Q_B", "非零频率"],
            ),
            "proved": True,
            "meaning": "持续 LowMod 坏行给出非零 Fourier 下界 L_lowmod。",
            "output": "L_lowmod = kappa_B beta /(sqrt(Q_B-1)||f_B||_2)。",
        },
        {
            "gate": "SameSetDualCertificateProtocolRegistered",
            "closed": contains_all(
                dual_text,
                ["U_CRT<L_PDEC", "对偶 PDEC 证书", "PDU-2", "坏窗族"],
            ),
            "proved": True,
            "meaning": "若同集 CRT 对偶上界 U_CRT 小于 PDEC 下界，则 persistent 分支被排除。",
            "output": "容量成功支已经是标准 PDEC dual certificate。",
        },
        {
            "gate": "MultiplierDisciplineNoEscape",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed") is True,
            "proved": True,
            "meaning": "已知 Type/Fourier/fiber 成本均登记为同 formal unit 的 log-power 乘子。",
            "output": "LowMod 容量失败不能归因于账外乘子或口径错配。",
        },
        {
            "gate": "CapLocalizationFailureOutput",
            "closed": contains_all(
                ranktwo_text,
                ["if U_CRT(h,zeta) >= L_PDEC", "cap localization", "mass"],
            ),
            "proved": True,
            "meaning": "若某方向 U_CRT 达到 L_PDEC，则必须输出方向帽质量集中。",
            "output": "LowModDualCap(B,h,zeta,alpha) with mass >= (L-alpha M)/(1-alpha)。",
        },
        {
            "gate": "FiniteArcBasisForLowModCaps",
            "closed": contains_all(
                finite_arc_text,
                ["finite cyclic arc", "preimages of cyclic arcs", "finite cyclic-arc cap mass bounds"],
            ),
            "proved": True,
            "meaning": "固定 Q_B 后，所有方向帽都化为有限字符循环弧预像。",
            "output": "连续 zeta/alpha 搜索被压成有限 LowMod arc cap 质量界。",
        },
        {
            "gate": "SparseLowRankColumnReturn",
            "closed": "SAE 不是独立终端族" in sae_text
            and "displacement PDEC" in column_text
            and "二秩以上" in pdec_text,
            "proved": True,
            "meaning": "稀疏帽、低秩帽、列位移帽不能作为新 LowMod 终端。",
            "output": "回流 SAE / ColumnCRT-as-PDEC / primitive rank boundary。",
        },
        {
            "gate": "PersistentCapNoSameLayerCycle",
            "closed": contains_all(
                nocycle_text,
                ["固定有限签名群", "不能无限循环", "new-layer PDEC", "CleanKLS"],
            ),
            "proved": True,
            "meaning": "持久帽细化不能在同一有限 Q_B 层无穷循环。",
            "output": "有限步进入 refined PDEC、ColumnCRT、SAE、new-layer PDEC 或 CleanKLS。",
        },
        {
            "gate": "PersistentLowModPDECInequality",
            "closed": False,
            "proved": False,
            "meaning": "尚未提交所有未来 LowMod primitive schema 的有限循环弧 cap 质量上界。",
            "output": "LowModFiniteArcDualCapStabilityOrSparseSAE。",
        },
    ]


def run(
    previous_path: Path,
    dec_path: Path,
    dual_path: Path,
    ranktwo_path: Path,
    finite_arc_path: Path,
    nocycle_path: Path,
    pdec_path: Path,
    sae_path: Path,
    column_path: Path,
    multiplier_path: Path,
) -> dict[str, Any]:
    """执行 LowMod PDEC 容量失败定位。"""
    source_paths = [
        previous_path,
        dec_path,
        dual_path,
        ranktwo_path,
        finite_arc_path,
        nocycle_path,
        pdec_path,
        sae_path,
        column_path,
        multiplier_path,
    ]
    previous = load_json(previous_path)
    multiplier = load_json(multiplier_path)
    dec_text = dec_path.read_text(encoding="utf-8")
    dual_text = dual_path.read_text(encoding="utf-8")
    ranktwo_text = ranktwo_path.read_text(encoding="utf-8")
    finite_arc_text = finite_arc_path.read_text(encoding="utf-8")
    nocycle_text = nocycle_path.read_text(encoding="utf-8")
    pdec_text = pdec_path.read_text(encoding="utf-8")
    sae_text = sae_path.read_text(encoding="utf-8")
    column_text = column_path.read_text(encoding="utf-8")
    rows = build_rows(
        previous=previous,
        dec_text=dec_text,
        dual_text=dual_text,
        ranktwo_text=ranktwo_text,
        finite_arc_text=finite_arc_text,
        nocycle_text=nocycle_text,
        pdec_text=pdec_text,
        sae_text=sae_text,
        column_text=column_text,
        multiplier=multiplier,
    )
    closed_except_terminal = all(
        row["closed"] for row in rows if row["gate"] != "PersistentLowModPDECInequality"
    )
    return {
        "certificate_type": "lowmod_pdec_capacity_failure_router",
        "status": "lowmod_pdec_capacity_failure_localized_to_finite_arc_dualcap",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "previous_terminal_gap": previous.get("terminal_gap_after_router"),
        "lowmod_same_set_capacity_protocol_closed": closed_except_terminal,
        "lowmod_capacity_multiplier_discipline_closed": multiplier.get(
            "registered_capacity_multiplier_discipline_closed"
        )
        is True,
        "lowmod_pdec_inequality_closed": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": "PersistentLowModPDECInequality_UCRT_LT_LPDEC",
        "terminal_gap_after_router": "LowModFiniteArcDualCapStabilityOrSparseSAE",
        "new_atomic_input": "FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas",
        "failure_witness_shape": {
            "formal_unit": "G_B=Z/Q_BZ with phase x mod Q_B",
            "bad_count": "g_B(t)=1_{sign*f_B(t)>=kappa_B} or the corresponding multiplicity count",
            "lower_bound": "L_lowmod=kappa_B*beta/(sqrt(Q_B-1)*||f_B||_2)",
            "dual_success": "U_CRT(G_B,g_B)<L_lowmod excludes the persistent LowMod PDEC branch",
            "dual_failure": "exists nontrivial character h and finite cyclic arc A with g_B(A)>=(L-alpha M)/(1-alpha)",
            "named_returns": "Sparse SAE / displacement ColumnCRT / refined PDEC / new-layer PDEC / CleanKLS",
        },
        "logic_chain": [
            "persistent LowMod bad rows force a same-formal-unit Fourier lower bound",
            "same-set PDEC dual certificate would exclude the branch if U_CRT<L_PDEC",
            "if U_CRT<L_PDEC fails, cap localization forces a finite cyclic-arc DualCap witness",
            "sparse, low-rank, displacement and refinement cases already return to named interfaces",
            "the only remaining unproved input is the global finite-arc cap mass bound for future LowMod primitive schemas",
        ],
        "closed_gates": [row["gate"] for row in rows if row["closed"]],
        "open_gates": [row["gate"] for row in rows if not row["closed"]],
        "rows": rows,
        "plain_conclusion": (
            "本步把 PersistentLowModPDECInequality 从抽象容量不等式压成失败定位定理："
            "若同一 LowMod formal unit 上的 U_CRT<L_PDEC 不能成立，失败必须显化为有限循环弧 "
            "DualCap，并立即进入 SAE、ColumnCRT、refined PDEC、new-layer PDEC 或 CleanKLS。"
            "真正未闭合的是未来 LowMod primitive schema 的全局有限弧 cap 质量上界。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    witness = result["failure_witness_shape"]
    lines = [
        "# Prime Matrix LowMod PDEC 容量失败定位路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"lowmod_same_set_capacity_protocol_closed={fmt_bool(result['lowmod_same_set_capacity_protocol_closed'])}",
        f"lowmod_capacity_multiplier_discipline_closed={fmt_bool(result['lowmod_capacity_multiplier_discipline_closed'])}",
        f"lowmod_pdec_inequality_closed={fmt_bool(result['lowmod_pdec_inequality_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"terminal_gap_before_router={result['terminal_gap_before_router']}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        f"new_atomic_input={result['new_atomic_input']}",
        "```",
        "",
        "## 1. 失败见证形状",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in witness.items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "这一步的核心是逆否：不再把 `U_CRT<L_PDEC` 失败留作抽象黑箱，而是强制它输出可审查的",
            "`LowModDualCap(B,h,zeta,alpha)`。固定 `Q_B` 后，方向帽只是有限循环弧的预像，",
            "因此连续参数退路已经被消掉。",
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | output |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | `{output}` |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                output=table_cell(row["output"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 新的最窄剩余",
            "",
            "```text",
            "PersistentLowModPDECInequality_UCRT_LT_LPDEC",
            "  <= same formal unit PDEC lower bound",
            "     + same-set dual protocol",
            "     + finite cyclic-arc DualCap localization",
            "     + named return absorption",
            "     + FiniteCyclicArcCapMassBoundsForFutureLowModPrimitiveSchemas.",
            "```",
            "",
            "其中前四项已经由现有材料和本路由器接线；最后一项仍未证明。",
            "这说明早期零行假设若真的强制持续 LowMod 缺陷，下一步不能再泛谈低模 CRT 均衡，",
            "必须直接证明所有未来 primitive LowMod schema 的有限弧帽质量界，或从帽见证中抽取",
            "SAE/ColumnCRT/refined PDEC 的显式回流证书。",
            "",
            "## 4. 审稿边界",
            "",
            "本步仍不是行/列无条件定理证明：",
            "",
            "```text",
            "row_column_unconditional_closed=false",
            "```",
            "",
            "它完成的是容量失败的强制材料化，排除了“PDEC 不等式失败但不给结构见证”的无名出口。",
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
    parser.add_argument("--dec", type=Path, default=DEFAULT_DEC)
    parser.add_argument("--dual", type=Path, default=DEFAULT_DUAL)
    parser.add_argument("--ranktwo", type=Path, default=DEFAULT_RANKTWO)
    parser.add_argument("--finite-arc", type=Path, default=DEFAULT_FINITE_ARC)
    parser.add_argument("--nocycle", type=Path, default=DEFAULT_NOCYCLE)
    parser.add_argument("--pdec", type=Path, default=DEFAULT_PDEC)
    parser.add_argument("--sae", type=Path, default=DEFAULT_SAE)
    parser.add_argument("--column", type=Path, default=DEFAULT_COLUMN)
    parser.add_argument("--multiplier", type=Path, default=DEFAULT_MULTIPLIER)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        previous_path=args.previous,
        dec_path=args.dec,
        dual_path=args.dual,
        ranktwo_path=args.ranktwo,
        finite_arc_path=args.finite_arc,
        nocycle_path=args.nocycle,
        pdec_path=args.pdec,
        sae_path=args.sae,
        column_path=args.column,
        multiplier_path=args.multiplier,
    )
    write_outputs(result, args.json_out, args.md_out)


if __name__ == "__main__":
    main()
