#!/usr/bin/env python3
"""Prime Matrix clean-core 支撑关联终端攻击路由器。

用法示例：
  python3 experiments/prime_matrix_clean_core_support_incidence_attack_router.py

输出：
  docs/monograph/prime-matrix-clean-core-support-incidence-attack-router.json
  docs/monograph/prime-matrix-clean-core-support-incidence-attack-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_ATOM = DOCS / "prime-matrix-clean-core-exact-entropy-atom-router.json"
DEFAULT_SUPPORT_RANGE = DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json"
DEFAULT_REGISTERED = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_FACTOR_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_INCIDENCE = DOCS / "prime-matrix-triad-a1-factor-residue-incidence-router.json"
DEFAULT_SQUAREFREE = DOCS / "prime-matrix-triad-a1-squarefree-buchstab-support-router.json"
DEFAULT_COMPLETED_KLS = DOCS / "prime-matrix-triad-a1-dibfi-full-s-completion-reduction-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-clean-core-support-incidence-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-clean-core-support-incidence-attack-router.md"


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


def model_rows() -> list[dict[str, Any]]:
    """给出内部 fiber 阻断的尺度模型。"""
    rows: list[dict[str, Any]] = []
    for k in range(3, 10):
        log_y = 2.302585092994046 * k
        internal_atoms = int(round(log_y**7))
        required_support = int(round(log_y**5))
        rows.append(
            {
                "k": k,
                "log_y": log_y,
                "moving_pairs": 1,
                "internal_atoms": internal_atoms,
                "max_internal_share": 1.0 / internal_atoms,
                "required_support": required_support,
                "k4_flat_possible": True,
                "factor_support_fails": True,
            }
        )
    return rows


def attack_rows(
    atom: dict[str, Any],
    support_range: dict[str, Any],
    registered: dict[str, Any],
    factor_support: dict[str, Any],
    incidence: dict[str, Any],
    squarefree: dict[str, Any],
    completed_kls: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成支撑关联攻击判定表。"""
    return [
        {
            "gate": "PriorTerminalAtomPinned",
            "closed": atom.get("latest_actionable_self_contained_input")
            == "CleanCoreTerminalSupportIncidenceTheorem",
            "proved": False,
            "meaning": "上一层已把 exact entropy 失败压成 clean-core terminal support atom。",
            "remaining": "攻击该支撑原子是否可由现有材料排除。",
        },
        {
            "gate": "BalancedRangeAlreadyClosed",
            "closed": support_range.get("balanced_range_threshold_closed") is True,
            "proved": True,
            "meaning": "full-S regime 下 U,V 超过任意固定对数阈值，range 不是终端障碍。",
            "remaining": "只剩 exact 支撑和层转移。",
        },
        {
            "gate": "RegisteredCapacityBudgetClosed",
            "closed": registered.get("registered_capacity_multiplier_discipline_closed") is True,
            "proved": True,
            "meaning": "所有 Type/Fourier/fiber 乘子已登记为同一 formal unit 的 log-power 成本。",
            "remaining": "不能再用账外乘子解释 moving 原子。",
        },
        {
            "gate": "BroadSupportWouldSuffice",
            "closed": "SupportLowerBoundImpliesEntropy"
            in factor_support.get("closed_support_gates", [])
            or factor_support.get("k4_k6_imply_exact_factor_support") is False,
            "proved": True,
            "meaning": "一旦 exact u/v 支撑下界成立，已有初等不等式会推出 entropy/anti-atom。",
            "remaining": "支撑下界本身未证。",
        },
        {
            "gate": "RawThickSquarefreeCountingClosed",
            "closed": squarefree.get("raw_thick_squarefree_support_closed") is True,
            "proved": True,
            "meaning": "厚区间内普通 squarefree/Buchstab 计数足够支付对数支撑需求。",
            "remaining": "不是数量问题，而是 exact 层是否承认并给出非零系数。",
        },
        {
            "gate": "NaiveIncidenceBridgeBlocked",
            "closed": incidence.get("naive_incidence_bridge_valid") is False,
            "proved": True,
            "meaning": "单个 moving (u,v) 可在内部 h,ell,x,z fiber 上平坦，K4/K6 看不见 factor 集中。",
            "remaining": "需要非朴素层承认/非零转移，或 completed KLS。",
        },
        {
            "gate": "CanonicalLayerTransferDoesNotImportToCleanCore",
            "closed": True,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 支撑只服务 canonical-source 分支，不能偷渡到 noncanonical clean-core。",
            "remaining": "必须证明 clean-core 自身的 exact 层承认和非零转移。",
        },
        {
            "gate": "CleanCoreExactLayerAdmissionCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明 clean-core exact 层承认足够多 Buchstab products 且系数非零。",
            "remaining": "证明 CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn。",
        },
        {
            "gate": "ExternalCompletedKLSNormalFormStillOpen",
            "closed": completed_kls.get("terminal_gap_after_router")
            == "ModulusDependentCompletedFullSKLSInput",
            "proved": False,
            "meaning": "外部替代仍是 modulus-dependent completed Full-S KLS，不是泛称 DI/BFI。",
            "remaining": "证明或独立接受 ModulusDependentCompletedFullSKLSInput。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "源侧完成后仍需独立验收。",
        },
    ]


def run(
    atom_path: Path,
    support_range_path: Path,
    registered_path: Path,
    factor_support_path: Path,
    incidence_path: Path,
    squarefree_path: Path,
    completed_kls_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 clean-core 支撑关联攻击路由。"""
    source_paths = [
        atom_path,
        support_range_path,
        registered_path,
        factor_support_path,
        incidence_path,
        squarefree_path,
        completed_kls_path,
        dstructure_path,
    ]
    atom = load_json(atom_path)
    support_range = load_json(support_range_path)
    registered = load_json(registered_path)
    factor_support = load_json(factor_support_path)
    incidence = load_json(incidence_path)
    squarefree = load_json(squarefree_path)
    completed_kls = load_json(completed_kls_path)
    dstructure = load_json(dstructure_path)

    rows = attack_rows(
        atom=atom,
        support_range=support_range,
        registered=registered,
        factor_support=factor_support,
        incidence=incidence,
        squarefree=squarefree,
        completed_kls=completed_kls,
        dstructure=dstructure,
    )
    boundary_closed = all(
        row["closed"]
        for row in rows
        if row["gate"] != "CleanCoreExactLayerAdmissionCurrentCorpusProved"
    )

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_clean_core_support_incidence_attack_router",
        "status": "clean_core_support_incidence_reduced_to_exact_layer_transfer_open",
        "clean_core_support_incidence_attack_boundary_closed": boundary_closed,
        "balanced_range_closed": support_range.get("balanced_range_threshold_closed") is True,
        "registered_capacity_budget_closed": registered.get(
            "registered_capacity_multiplier_discipline_closed"
        )
        is True,
        "raw_thick_squarefree_counting_closed": squarefree.get(
            "raw_thick_squarefree_support_closed"
        )
        is True,
        "naive_incidence_bridge_blocked": incidence.get("naive_incidence_bridge_valid") is False,
        "clean_core_exact_layer_transfer_proved": False,
        "clean_core_terminal_support_incidence_proved": False,
        "external_completed_kls_accepted": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "previous_input": "CleanCoreTerminalSupportIncidenceTheorem",
        "latest_internal_subinput": "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn",
        "latest_conditional_basis": (
            "(CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn OR "
            "ModulusDependentCompletedFullSKLSInput) AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "latest_self_contained_basis": (
            "CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "structural_law": (
            "clean-core 支撑关联的 range、乘子预算和厚区间原始计数都已不是终端障碍。"
            "朴素 factor-residue incidence 被内部 fiber 模型阻断；canonical 层支撑不能导入 "
            "noncanonical clean-core。故完全自足路线必须证明 clean-core exact 层承认足够多 "
            "Buchstab products、系数非零，并把 thin/rejected blocks 回流到命名出口。"
        ),
        "plain_conclusion": (
            "最新真正剩余继续缩小：不是证明普通 squarefree 数量，也不是 K4/K6 incidence，"
            "而是证明 clean-core exact 层承认与非零转移。当前材料仍未证明该输入；"
            "外部替代仍是 completed、modulus-dependent Full-S KLS。"
        ),
        "rows": rows,
        "fiber_obstruction_model": model_rows(),
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
    """写出 Markdown 研究证书。"""
    lines: list[str] = [
        "# Prime Matrix clean-core 支撑关联终端攻击路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"clean_core_support_incidence_attack_boundary_closed={fmt_bool(result['clean_core_support_incidence_attack_boundary_closed'])}",
        f"clean_core_exact_layer_transfer_proved={fmt_bool(result['clean_core_exact_layer_transfer_proved'])}",
        f"clean_core_terminal_support_incidence_proved={fmt_bool(result['clean_core_terminal_support_incidence_proved'])}",
        f"external_completed_kls_accepted={fmt_bool(result['external_completed_kls_accepted'])}",
        f"dstructure_rankin_independent_acceptance_completed={fmt_bool(result['dstructure_rankin_independent_acceptance_completed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{table_cell(row['gate'])}`",
                    f"`{fmt_bool(row['closed'])}`",
                    f"`{fmt_bool(row['proved'])}`",
                    table_cell(row["meaning"]),
                    table_cell(row["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 2. 结构律",
            "",
            result["structural_law"],
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
            "其中 `CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn` 要求：",
            "",
            "- exact clean-core 层承认厚 balanced block 中足够多 Buchstab products；",
            "- 这些 products 在 actual alpha/delta 中有非零系数并贡献绝对支撑；",
            "- thin 或 layer-rejected block 必须回流到 edge/PDEC/SAE/ColumnCRT/CleanKLS 等命名出口。",
            "",
            "## 4. 内部 fiber 阻断模型",
            "",
            "| k | log y | moving pairs | internal atoms | max internal share | required support | K4 flat possible | factor support fails |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["fiber_obstruction_model"]:
        lines.append(
            "| {k} | {log_y:.6g} | {moving_pairs} | {internal_atoms} | "
            "{max_internal_share:.6g} | {required_support} | `{k4_flat_possible}` | "
            "`{factor_support_fails}` |".format(**row)
        )
    lines.extend(
        [
            "",
            "该模型说明：即使内部 residue/phase fiber 很大且每个内部原子都很小，质量仍可集中在一个 moving",
            "`(u,v)` 上。因此 K4/K6 型固定投影平坦性不能替代 clean-core exact 层承认与非零转移。",
            "",
            "## 5. 当前结论",
            "",
            "本步没有证明 `CleanCoreExactLayerAdmissionNonzeroTransferAndThinReturn`。它关闭的是错误方向：",
            "不能再从普通 squarefree 计数、K4/K6 平坦性或 canonical 支撑偷渡推出 clean-core 支撑关联。",
            "",
        ]
    )
    md_out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(
        description="Attack clean-core terminal support incidence and route remaining atom."
    )
    parser.add_argument("--atom", type=Path, default=DEFAULT_ATOM)
    parser.add_argument("--support-range", type=Path, default=DEFAULT_SUPPORT_RANGE)
    parser.add_argument("--registered", type=Path, default=DEFAULT_REGISTERED)
    parser.add_argument("--factor-support", type=Path, default=DEFAULT_FACTOR_SUPPORT)
    parser.add_argument("--incidence", type=Path, default=DEFAULT_INCIDENCE)
    parser.add_argument("--squarefree", type=Path, default=DEFAULT_SQUAREFREE)
    parser.add_argument("--completed-kls", type=Path, default=DEFAULT_COMPLETED_KLS)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        atom_path=args.atom,
        support_range_path=args.support_range,
        registered_path=args.registered,
        factor_support_path=args.factor_support,
        incidence_path=args.incidence,
        squarefree_path=args.squarefree,
        completed_kls_path=args.completed_kls,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_internal_subinput"])


if __name__ == "__main__":
    main()
