#!/usr/bin/env python3
"""生成行命题闭合输入图谱。

用法示例：
  python3 experiments/prime_matrix_closure_input_atlas_router.py

输出：
  docs/monograph/prime-matrix-closure-input-atlas-router.json
  docs/monograph/prime-matrix-closure-input-atlas-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CANONICAL_FINAL = (
    DOCS / "prime-matrix-canonical-source-self-contained-final-theorem-router.json"
)
DEFAULT_NONCANONICAL = (
    DOCS / "prime-matrix-noncanonical-complement-input-contract-router.json"
)
DEFAULT_ACTUAL_SOURCE = (
    DOCS / "prime-matrix-actual-source-bridge-global-reconciliation-router.json"
)
DEFAULT_UNNAMED = DOCS / "prime-matrix-unnamed-escape-closure-machine.md"
DEFAULT_NAMED = DOCS / "prime-matrix-named-exit-absorption-contract.md"
DEFAULT_GLOBAL_CHAIN = DOCS / "prime-matrix-global-structural-closure-chain.md"
DEFAULT_P_COLUMN = DOCS / "prime-matrix-pcolumn-anchor-dynamic-capacity.md"
DEFAULT_LAYERED_WHEEL = DOCS / "prime-matrix-dprc-cylindrical-layered-wheel-clamp.md"
DEFAULT_PDEC_FAILURE = DOCS / "prime-matrix-pdec-dual-failure-absorption-contract.md"
DEFAULT_JSON = DOCS / "prime-matrix-closure-input-atlas-router.json"
DEFAULT_MD = DOCS / "prime-matrix-closure-input-atlas-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains_all(path: Path, needles: list[str]) -> bool:
    """检查文件是否包含全部关键片段。"""
    text = path.read_text(encoding="utf-8")
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值输出成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def model_row(
    model: str,
    proved: str,
    output: str,
    closure_input: str,
    status: str,
) -> dict[str, str]:
    """构造模型图谱行。"""
    return {
        "model": model,
        "proved": proved,
        "output": output,
        "closure_input": closure_input,
        "status": status,
    }


def build_model_rows(
    canonical_final: dict[str, Any],
    noncanonical: dict[str, Any],
    actual_source: dict[str, Any],
    unnamed_path: Path,
    named_path: Path,
    global_chain_path: Path,
    p_column_path: Path,
    layered_wheel_path: Path,
    pdec_failure_path: Path,
) -> list[dict[str, str]]:
    """生成所有已探索模型到闭合输入的映射。"""
    canonical_closed = (
        canonical_final["canonical_source_self_contained_theorem_closed"]
        and canonical_final["open_self_contained_gates"] == []
    )
    noncanonical_contract_closed = noncanonical["contract_boundary_closed"]
    actual_canonical_bridge_closed = actual_source[
        "actual_source_bridge_closed_for_canonical_branch"
    ]
    unnamed_closed = contains_all(
        unnamed_path,
        ["无名逃逸闭合定理", "SAE/endpoint", "CleanMultishellKLS"],
    )
    named_absorption = contains_all(
        named_path,
        ["Abs(PDEC)", "Abs(ColumnCRT)", "generalized PDEC"],
    )
    global_chain = contains_all(
        global_chain_path,
        ["Self-Normalized Tail Dichotomy", "No-Cycle Defect Ledger"],
    )
    p_column = contains_all(
        p_column_path,
        ["T_Y(P,y)<|S_Y(P,y)|", "PColumn Dynamic Capacity"],
    )
    layered_wheel = contains_all(
        layered_wheel_path,
        ["W-unit PDEC", "圆柱斜线告诉我们"],
    )
    pdec_failure = contains_all(
        pdec_failure_path,
        ["Cap localization", "refined PDEC", "Multiplicity/Stitching"],
    )

    return [
        model_row(
            model="Full CRT / MinRep 零行等价",
            proved="零行等价于完整覆盖 CRT 证书与最小代表缺陷。",
            output="把反例固定为具体 tau 与 r_tau^+<=P。",
            closure_input="后续必须排斥 MinRep 缺陷，或把它送入容量/端点/PDEC 出口。",
            status="reduction_closed",
        ),
        model_row(
            model="方阵斜线 / 圆柱覆盖",
            proved="高素斜线补洞可以写成圆柱面残基命中；覆盖需要容量大于剩余洞。",
            output="T_Y>=|S_Y| 是零行必要条件。",
            closure_input="动态容量不等式，或失败进入 SAE/PDEC/ColumnCRT/尾锚。",
            status="reduction_closed",
        ),
        model_row(
            model="第 P 列锚点动态轮容量",
            proved="T_Y(P,y)<|S_Y(P,y)| 严格推出该行有素数洞。",
            output="全行全列夹击方程 S_Y(P,y)=圆柱平移骨架。",
            closure_input="证明所有行容量不足；若容量失败，证明近截止/远尾超额必进命名缺陷。",
            status="input_needed" if p_column else "evidence_missing",
        ),
        model_row(
            model="P^2±k 与层叠轮筛",
            proved="30/210/2310/... 单位类偏斜若不稀释则给 W-unit PDEC；若稀释则进 CleanKLS/DLS。",
            output="圆柱容量压力与小模相位同步形成夹击。",
            closure_input="W-unit PDEC/ColumnCRT 排斥，或高维分散 CleanKLS/DLS。",
            status="input_needed" if layered_wheel else "evidence_missing",
        ),
        model_row(
            model="远尾互补因子反演",
            proved="远尾 q 命中等价为 Y-rough 互补因子 m 上的短素数区间计数。",
            output="正超额不再无结构，落在 m-band/cofactor-anchor。",
            closure_input="Self-normalized tail dichotomy：超额必进 cofactor-anchor/SAE/PDEC/ColumnCRT。",
            status="input_needed" if global_chain else "evidence_missing",
        ),
        model_row(
            model="SN-1/SN-2/SN-3 递归剥离",
            proved="最小反例不能无限保持无名；低模峰、高频峰、多壳同步都必须命名。",
            output="反例有限步进入 SAE/PDEC/ColumnCRT/Bohr-cap/CleanKLS/TotalDescent。",
            closure_input="排斥这些命名出口，或证明 CleanMultishellKLS / TotalDescent。",
            status="unnamed_closed_named_open" if unnamed_closed else "evidence_missing",
        ),
        model_row(
            model="命名出口吸收合同",
            proved="Bohr-cap、EndpointSeam、CofactorAnchor 不再是自由出口，吸收到统一接口。",
            output="最终出口缩为 SAE-Cert / PDEC-Cert / ColumnCRT-Cert / CleanKLS / p=2 descent。",
            closure_input="提交这些证书或证明无缺陷下降到底。",
            status="contract_closed_certificates_open" if named_absorption else "evidence_missing",
        ),
        model_row(
            model="PDEC 对偶失败与 cap 细化",
            proved="PDEC 上界失败只能变成帽集中；持久帽进 refined PDEC，稀疏帽进 SAE。",
            output="PDEC 失败不能生成新无名分支。",
            closure_input="完成 U_CRT<L_PDEC，或完成 refined PDEC / SAE / ColumnCRT / stitching。",
            status="no_cycle_closed_certificate_open" if pdec_failure else "evidence_missing",
        ),
        model_row(
            model="Triad-A1 canonical-source 自足分支",
            proved="canonical RIW/Buchstab 来源分支的 same-set/full-S terminal 与 terminal promotion 已闭合。",
            output="NoFurtherCanonicalSourceSelfContainedTheoremBoundaryGap。",
            closure_input="无 canonical 内部输入；只需防止误升级。",
            status="closed" if canonical_closed and actual_canonical_bridge_closed else "evidence_missing",
        ),
        model_row(
            model="Noncanonical full-S 补集",
            proved="必要输入边界已闭合；generic WFD 模板不可用。",
            output="补集只能走实际源恒等、实际源强化反原子或外部/量化 DI/BFI。",
            closure_input="ProveActualFullSNonAPSourceIsCanonicalRIWBuchstab 或 FullSNonAPStrengthenedSourceAntiAtomForActualSource 或 DIBFI no-projection。",
            status="input_contract_closed_input_open" if noncanonical_contract_closed else "evidence_missing",
        ),
        model_row(
            model="D-structure / Tail-log4 / Rankin 晋级门",
            proved="作者侧组织与边界已固定；仍是独立审稿门。",
            output="PM final promotion remains referee-block。",
            closure_input="DStructureTailLog4FiniteRankinIndependentAcceptance。",
            status="referee_block",
        ),
    ]


def run(
    canonical_final_path: Path,
    noncanonical_path: Path,
    actual_source_path: Path,
    unnamed_path: Path,
    named_path: Path,
    global_chain_path: Path,
    p_column_path: Path,
    layered_wheel_path: Path,
    pdec_failure_path: Path,
) -> dict[str, Any]:
    """运行闭合输入图谱路由。"""
    canonical_final = load_json(canonical_final_path)
    noncanonical = load_json(noncanonical_path)
    actual_source = load_json(actual_source_path)

    rows = build_model_rows(
        canonical_final=canonical_final,
        noncanonical=noncanonical,
        actual_source=actual_source,
        unnamed_path=unnamed_path,
        named_path=named_path,
        global_chain_path=global_chain_path,
        p_column_path=p_column_path,
        layered_wheel_path=layered_wheel_path,
        pdec_failure_path=pdec_failure_path,
    )
    evidence_paths = [
        canonical_final_path,
        noncanonical_path,
        actual_source_path,
        unnamed_path,
        named_path,
        global_chain_path,
        p_column_path,
        layered_wheel_path,
        pdec_failure_path,
    ]
    minimal_input_basis = [
        {
            "input": "TerminalCertificatePackage",
            "contents": [
                "SAE-Cert",
                "PDEC-Cert with U_CRT<L_PDEC",
                "ColumnCRT-Cert or return to PDEC/SAE",
                "CleanMultishellKLS",
                "TotalDescent to p=2 or first-seam absorption",
            ],
            "why_needed": "无名逃逸和命名出口已被压到这些接口；排斥它们即可关闭结构反例出口。",
        },
        {
            "input": "NoncanonicalFullSComplementPackage",
            "contents": [
                "Actual full-S non-AP source equals canonical RIW/Buchstab source",
                "or strengthened anti-atom for the actual noncanonical source",
                "or quantified no-projection DI/BFI route",
            ],
            "why_needed": "canonical 分支已扣除，generic WFD 模板已反证；补集不能偷渡闭合。",
        },
        {
            "input": "DStructureRankinPromotionPackage",
            "contents": [
                "D-structure/Tail-log4 interface accepted",
                "finite Rankin and threshold interfaces accepted",
                "PM final promotion referee block removed",
            ],
            "why_needed": "完整行/列无条件定理晋级仍依赖该独立门。",
        },
    ]
    optional_shortcuts = [
        "外部平方根长度短区间素数输入可直接关闭对角端点，但不是当前自足主路线。",
        "外部 FullS-KLS / DI / BFI 可关闭 generic 外部合同版，但不能冒充 canonical 自足证明。",
    ]

    return {
        "certificate_type": "prime_matrix_closure_input_atlas_router",
        "status": "closure_input_atlas_complete_global_inputs_still_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in evidence_paths},
        "canonical_source_self_contained_closed": canonical_final[
            "canonical_source_self_contained_theorem_closed"
        ],
        "noncanonical_input_contract_closed": noncanonical["contract_boundary_closed"],
        "row_column_unconditional_closed": False,
        "models_reviewed": rows,
        "minimal_input_basis": minimal_input_basis,
        "optional_shortcuts": optional_shortcuts,
        "atlas_law": (
            "All explored structures now fall into two classes: closed reductions/contracts, "
            "or named inputs. The current corpus closes the canonical-source theorem boundary "
            "and the no-unnamed-escape logic, but full global unconditional closure still "
            "requires the terminal certificate package, the noncanonical full-S complement "
            "package, and final D-structure/Rankin promotion."
        ),
        "review_conclusion": (
            "闭合输入图谱已固定：继续突破不应再寻找无名新分支，而应集中证明终端证书包、"
            "noncanonical full-S 补集输入包和 D-structure/Rankin 晋级包。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix 行命题闭合输入图谱",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 图谱律",
        "",
        result["atlas_law"],
        "",
        "```text",
        (
            "canonical_source_self_contained_closed="
            f"{fmt_bool(result['canonical_source_self_contained_closed'])}"
        ),
        (
            "noncanonical_input_contract_closed="
            f"{fmt_bool(result['noncanonical_input_contract_closed'])}"
        ),
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 2. 已探索模型回顾",
        "",
        "| model | proved / reduced | output | closure input | status |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["models_reviewed"]:
        lines.append(
            "| {model} | {proved} | {output} | {closure_input} | `{status}` |".format(
                model=table_cell(row["model"]),
                proved=table_cell(row["proved"]),
                output=table_cell(row["output"]),
                closure_input=table_cell(row["closure_input"]),
                status=table_cell(row["status"]),
            )
        )
    lines.extend(["", "## 3. 最小闭合输入基", ""])
    for item in result["minimal_input_basis"]:
        lines.append(f"### {item['input']}")
        lines.append("")
        for content in item["contents"]:
            lines.append(f"- {content}")
        lines.append("")
        lines.append(f"需要原因：{item['why_needed']}")
        lines.append("")
    lines.extend(["## 4. 可选捷径", ""])
    for shortcut in result["optional_shortcuts"]:
        lines.append(f"- {shortcut}")
    lines.extend(
        [
            "",
            "## 5. 最终判定",
            "",
            "当前材料已经把全部主要思路压成有限输入图谱：",
            "",
            "```text",
            "方阵斜线/圆柱覆盖/第P列锚点/层叠轮筛/远尾反演/SN递归剥离",
            "=> 无名逃逸不可能",
            "=> 命名出口吸收",
            "=> 终端证书包或 CleanKLS/TotalDescent。",
            "",
            "canonical-source 分支",
            "=> 已闭合。",
            "",
            "noncanonical full-S 补集",
            "=> 必要输入边界已闭合，但输入本身仍开。",
            "```",
            "",
            "因此继续突破的正确目标不是寻找新的固定常数，也不是回到 generic WFD 模板，"
            "而是逐项证明最小输入基中的三包。只有三包全部闭合，完整行/列无条件定理才可升级。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical-final-json", type=Path, default=DEFAULT_CANONICAL_FINAL)
    parser.add_argument("--noncanonical-json", type=Path, default=DEFAULT_NONCANONICAL)
    parser.add_argument("--actual-source-json", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--unnamed-md", type=Path, default=DEFAULT_UNNAMED)
    parser.add_argument("--named-md", type=Path, default=DEFAULT_NAMED)
    parser.add_argument("--global-chain-md", type=Path, default=DEFAULT_GLOBAL_CHAIN)
    parser.add_argument("--p-column-md", type=Path, default=DEFAULT_P_COLUMN)
    parser.add_argument("--layered-wheel-md", type=Path, default=DEFAULT_LAYERED_WHEEL)
    parser.add_argument("--pdec-failure-md", type=Path, default=DEFAULT_PDEC_FAILURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        canonical_final_path=args.canonical_final_json,
        noncanonical_path=args.noncanonical_json,
        actual_source_path=args.actual_source_json,
        unnamed_path=args.unnamed_md,
        named_path=args.named_md,
        global_chain_path=args.global_chain_md,
        p_column_path=args.p_column_md,
        layered_wheel_path=args.layered_wheel_md,
        pdec_failure_path=args.pdec_failure_md,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print([item["input"] for item in result["minimal_input_basis"]])


if __name__ == "__main__":
    main()
