#!/usr/bin/env python3
"""Prime Matrix actual 容量账本微原子路由器。

用法示例：
  python3 experiments/prime_matrix_actual_capacity_ledger_microatom_router.py

输出：
  docs/monograph/prime-matrix-actual-capacity-ledger-microatom-router.json
  docs/monograph/prime-matrix-actual-capacity-ledger-microatom-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_CORE = DOCS / "prime-matrix-noncanonical-source-core-atomization-router.json"
DEFAULT_ENTROPY = DOCS / "prime-matrix-triad-a1-exact-wfd-source-entropy-router.json"
DEFAULT_ANTIATOM = DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json"
DEFAULT_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-actual-capacity-ledger-microatom-router.json"
DEFAULT_MD = DOCS / "prime-matrix-actual-capacity-ledger-microatom-router.md"


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


def build_support_only_models() -> list[dict[str, Any]]:
    """构造“支撑宽但隐藏乘子集中”的阻断模型。"""
    rows: list[dict[str, Any]] = []
    for k in range(3, 10):
        log_y = k * math.log(10)
        required_share = log_y ** -4
        support_pairs = math.ceil(log_y**7)
        hidden_multiplier = support_pairs**2
        top_share = hidden_multiplier / (hidden_multiplier + support_pairs - 1)
        rows.append(
            {
                "k": k,
                "log_y": log_y,
                "required_share": required_share,
                "support_pairs": support_pairs,
                "hidden_multiplier": hidden_multiplier,
                "top_capacity_share": top_share,
                "raw_support_broad": support_pairs >= log_y**6,
                "antiatom_violated": top_share > required_share,
            }
        )
    return rows


def build_rows(
    core: dict[str, Any],
    entropy: dict[str, Any],
    antiatom: dict[str, Any],
    support: dict[str, Any],
    dstructure: dict[str, Any],
    model_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成微原子边界判定表。"""
    support_only_fails = all(row["antiatom_violated"] for row in model_rows)
    return [
        {
            "gate": "PreviousActualSupportCapacityCorePinned",
            "boundary_closed": core.get("atomized_self_contained_basis")
            == (
                "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput AND "
                "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
            ),
            "proved": core.get("actual_support_capacity_core_proved") is True,
            "meaning": "上一层已把完全自足源核心压到 actual noncanonical 支撑/容量合同。",
            "consequence": "可继续检查该合同内部是否还有支撑与容量口径偷换。",
        },
        {
            "gate": "SupportOnlyDoesNotImplyAntiAtom",
            "boundary_closed": support_only_fails,
            "proved": False,
            "meaning": "存在支撑很宽但单个 moving pair 获得隐藏容量乘子的模型。",
            "consequence": "不能把 exact u/v 支撑下界单独当作 source anti-atom 证明。",
        },
        {
            "gate": "RegisteredMultiplierDisciplineWouldRestoreImplication",
            "boundary_closed": True,
            "proved": False,
            "meaning": "若所有 Type/Fourier/fiber 乘子都登记进同一 formal unit 且至多多对数损失，则支撑下界可推出最终容量反原子。",
            "consequence": "证明路线应写成 exact 支撑下界 + 已登记容量乘子纪律。",
        },
        {
            "gate": "ExactUVSupportStillOpen",
            "boundary_closed": support.get("current_internal_exact_factor_support_closed") is False
            and support.get("k4_k6_imply_exact_factor_support") is False,
            "proved": False,
            "meaning": "当前 ledger 尚无 actual noncanonical exact u/v 支撑下界。",
            "consequence": "该支撑下界仍是一个真实微输入，不能由 K4/K6 或朴素 incidence 免费推出。",
        },
        {
            "gate": "TypeFourierMultiplierDisciplineStillOpen",
            "boundary_closed": entropy.get("current_internal_exact_wfd_source_entropy_closed") is False
            and antiatom.get("source_antiatom_reduction_closed") is False,
            "proved": False,
            "meaning": "Type/Fourier capacity compatibility 仍未作为同一 actual formal unit 乘子账本证明。",
            "consequence": "未登记乘子必须被证明不存在，或直接在最终 M_{u,v} 容量测度上证明无大原子。",
        },
        {
            "gate": "FinalCapacityMeasureIsSharpStatement",
            "boundary_closed": True,
            "proved": False,
            "meaning": "把所有已登记 Type/Fourier/fiber 成本吸收到最终 M_{u,v} 后，最锐利命题就是 max M_{u,v}/sum M <= log^{-2A}。",
            "consequence": "最新单原子应表述为 actual final capacity anti-atom ledger，而不是 raw support-only lemma。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "boundary_closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "consequence": "即使源容量微原子完成，也还需要独立验收才能升级为完整行/列定理。",
        },
    ]


def run(
    core_path: Path,
    entropy_path: Path,
    antiatom_path: Path,
    support_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 actual 容量账本微原子路由。"""
    source_paths = [core_path, entropy_path, antiatom_path, support_path, dstructure_path]
    core = load_json(core_path)
    entropy = load_json(entropy_path)
    antiatom = load_json(antiatom_path)
    support = load_json(support_path)
    dstructure = load_json(dstructure_path)
    model_rows = build_support_only_models()
    rows = build_rows(
        core=core,
        entropy=entropy,
        antiatom=antiatom,
        support=support,
        dstructure=dstructure,
        model_rows=model_rows,
    )
    microatom_boundary_closed = all(row["boundary_closed"] for row in rows)

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_actual_capacity_ledger_microatom_router",
        "status": "actual_capacity_ledger_microatom_boundary_closed_core_open",
        "microatom_boundary_closed": microatom_boundary_closed,
        "support_only_suffices": False,
        "registered_multiplier_discipline_would_suffice_with_support": True,
        "exact_uv_support_proved": False,
        "registered_multiplier_discipline_proved": False,
        "actual_final_capacity_antiatom_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_basis": core.get("atomized_self_contained_basis"),
        "latest_self_contained_basis": (
            "ActualFinalCapacityAntiAtomLedgerForNoncanonicalFullS AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "derivation_package": (
            "ActualNoncanonicalExactUVSupportLowerBound AND "
            "ActualTypeFourierRegisteredCapacityMultiplierDiscipline"
        ),
        "conditional_inequality": (
            "若 |alpha_u|,|delta_v| <= L^C，登记乘子 W_{u,v} <= L^E，"
            "且 S_u*S_v >= L^(2A+4C+E)，则 "
            "max M_{u,v}/sum M_{u,v} <= L^(-2A)。"
        ),
        "support_only_failure_law": (
            "raw u/v 支撑下界只控制有多少 factor pair；若 Type/Fourier/fiber 阶段允许某个"
            " moving pair 获得未登记容量乘子，则最终 M_{u,v} 仍可集中。"
        ),
        "structural_law": (
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput 的最锐利表述应是"
            "最终 actual 容量测度 M_{u,v} 的反原子账本。证明它可以走两步：exact u/v 支撑下界"
            "加 registered Type/Fourier capacity multiplier discipline。当前材料二者都没有完成；"
            "但支撑-only 偷换已被阻断，且条件蕴含公式已固定。"
        ),
        "plain_conclusion": (
            "最窄自足源核心继续收紧：`支撑宽` 不是充分条件，必须同时证明所有 Type/Fourier/fiber "
            "容量乘子已在同一 formal unit 账本中登记且不会让单个 moving `(u,v)` 对额外放大。"
            "因此最新单原子是 `ActualFinalCapacityAntiAtomLedgerForNoncanonicalFullS`；"
            "可行证明包是 `ActualNoncanonicalExactUVSupportLowerBound` 加 "
            "`ActualTypeFourierRegisteredCapacityMultiplierDiscipline`。当前二者仍未证明，"
            "DStructure/Rankin 晋级验收也仍独立开放。"
        ),
        "rows": rows,
        "support_only_model_rows": model_rows,
        "source_hashes": {
            str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths
        },
    }

    json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, md_out)
    return result


def write_markdown(result: dict[str, Any], md_out: Path) -> None:
    """写出 Markdown 报告。"""
    lines: list[str] = [
        "# Prime Matrix actual 容量账本微原子路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"microatom_boundary_closed={fmt_bool(result['microatom_boundary_closed'])}",
        f"support_only_suffices={fmt_bool(result['support_only_suffices'])}",
        f"registered_multiplier_discipline_would_suffice_with_support={fmt_bool(result['registered_multiplier_discipline_would_suffice_with_support'])}",
        f"exact_uv_support_proved={fmt_bool(result['exact_uv_support_proved'])}",
        f"registered_multiplier_discipline_proved={fmt_bool(result['registered_multiplier_discipline_proved'])}",
        f"actual_final_capacity_antiatom_proved={fmt_bool(result['actual_final_capacity_antiatom_proved'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 微原子判定表",
        "",
        "| gate | boundary closed | proved | meaning | consequence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{boundary}` | `{proved}` | {meaning} | {consequence} |".format(
                gate=table_cell(row["gate"]),
                boundary=fmt_bool(row["boundary_closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                consequence=table_cell(row["consequence"]),
            )
        )

    lines.extend(
        [
            "",
            "## 2. 上一层输入基",
            "",
            "```text",
            str(result["previous_basis"]),
            "```",
            "",
            "## 3. 最新单原子输入基",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 4. 可行证明包",
            "",
            "```text",
            result["derivation_package"],
            "```",
            "",
            "## 5. 条件不等式",
            "",
            result["conditional_inequality"],
            "",
            "## 6. 支撑-only 阻断律",
            "",
            result["support_only_failure_law"],
            "",
            "| k | log y | required share | support pairs | hidden multiplier | top capacity share | support broad | antiatom violated |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["support_only_model_rows"]:
        lines.append(
            "| {k} | {log_y:.6g} | {required_share:.6g} | {support_pairs} | {hidden_multiplier} | {top_capacity_share:.6g} | `{raw_support_broad}` | `{antiatom_violated}` |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 7. 结构律",
            "",
            result["structural_law"],
            "",
            "## 8. 当前结论",
            "",
            "这一步闭合的是支撑与容量口径的边界：raw factor support 不能单独替代最终 source anti-atom。",
            "完整自足路线现在必须直接证明 final capacity anti-atom ledger，或证明 exact 支撑下界加已登记乘子纪律。",
            "当前材料尚未证明这些微原子，也未完成 DStructure/Rankin 独立验收。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core", type=Path, default=DEFAULT_CORE)
    parser.add_argument("--entropy", type=Path, default=DEFAULT_ENTROPY)
    parser.add_argument("--antiatom", type=Path, default=DEFAULT_ANTIATOM)
    parser.add_argument("--support", type=Path, default=DEFAULT_SUPPORT)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        core_path=args.core,
        entropy_path=args.entropy,
        antiatom_path=args.antiatom,
        support_path=args.support,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_self_contained_basis"])


if __name__ == "__main__":
    main()
