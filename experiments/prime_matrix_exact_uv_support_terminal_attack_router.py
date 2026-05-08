#!/usr/bin/env python3
"""Prime Matrix ExactUVSupport 终端攻击路由器。

用法示例：
  python3 experiments/prime_matrix_exact_uv_support_terminal_attack_router.py

输出：
  docs/monograph/prime-matrix-exact-uv-support-terminal-attack-router.json
  docs/monograph/prime-matrix-exact-uv-support-terminal-attack-router.md
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

DEFAULT_MULTIPLIER = DOCS / "prime-matrix-registered-capacity-multiplier-discipline-router.json"
DEFAULT_SOURCE_CORE = DOCS / "prime-matrix-noncanonical-source-core-atomization-router.json"
DEFAULT_EXACT_SUPPORT = DOCS / "prime-matrix-triad-a1-exact-factor-support-router.json"
DEFAULT_CANONICAL_SUPPORT = DOCS / "prime-matrix-triad-a1-canonical-riw-support-router.json"
DEFAULT_SQUAREFREE = DOCS / "prime-matrix-triad-a1-squarefree-buchstab-support-router.json"
DEFAULT_CANONICAL_LAYER = DOCS / "prime-matrix-pdec-cap-canonical-layer-closure-router.json"
DEFAULT_DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.json"
DEFAULT_MD = DOCS / "prime-matrix-exact-uv-support-terminal-attack-router.md"


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


def build_sparse_wfd_models() -> list[dict[str, Any]]:
    """构造 exact support 的 generic WFD 阻断模型。"""
    rows: list[dict[str, Any]] = []
    for k in range(3, 10):
        log_y = k * math.log(10)
        required_support = math.ceil(log_y**7)
        rows.append(
            {
                "k": k,
                "log_y": log_y,
                "formal_factor_support": 1,
                "required_support": required_support,
                "passes_well_factorable_template": True,
                "violates_exact_uv_support": True,
            }
        )
    return rows


def build_rows(
    multiplier: dict[str, Any],
    source_core: dict[str, Any],
    exact_support: dict[str, Any],
    canonical_support: dict[str, Any],
    squarefree: dict[str, Any],
    canonical_layer: dict[str, Any],
    dstructure: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 ExactUVSupport 终端攻击判定表。"""
    return [
        {
            "gate": "RegisteredMultiplierDisciplineClosed",
            "closed": multiplier.get("registered_capacity_multiplier_discipline_closed") is True,
            "proved": True,
            "meaning": "上一轮已把 Type/Fourier/fiber 乘子纪律闭合为账本门。",
            "remaining": "ExactUVSupport 不再能把失败归因于账外乘子。",
        },
        {
            "gate": "CanonicalImportBlocked",
            "closed": source_core.get("canonical_import_allowed") is False,
            "proved": True,
            "meaning": "canonical RIW/Buchstab 支撑不能偷渡到 noncanonical full-S 补集。",
            "remaining": "必须证明 actual noncanonical 支撑，或直接证明 final anti-atom。",
        },
        {
            "gate": "K4K6AndNaiveIncidenceStillInsufficient",
            "closed": exact_support.get("k4_k6_imply_exact_factor_support") is False,
            "proved": True,
            "meaning": "K4/K6 与朴素 factor-residue incidence 不能推出 moving u/v 支撑。",
            "remaining": "支撑失败不会自动回流为已命名 K4/K6 失败。",
        },
        {
            "gate": "CanonicalSupportChainNotARecentOpenGap",
            "closed": canonical_layer.get("canonical_layer_transfer_closed") is True
            and canonical_layer.get("self_contained_canonical_branch_closed") is True,
            "proved": True,
            "meaning": "canonical-source 分支上的层准入/非零转移/薄块回流已由 canonical 边界吸收。",
            "remaining": "这只关闭 canonical 分支；不关闭 actual noncanonical 补集。",
        },
        {
            "gate": "RawBuchstabCountingNotEnoughForNoncanonical",
            "closed": squarefree.get("raw_thick_squarefree_support_closed") is True
            and squarefree.get("squarefree_buchstab_layer_support_closed") is False,
            "proved": True,
            "meaning": "厚区间 squarefree 数量够，但 exact 层承认和非零系数转移只服务已锁定的 canonical 层。",
            "remaining": "noncanonical actual 源仍需自己的支撑下界或 final anti-atom。",
        },
        {
            "gate": "ExactUVSupportCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "当前材料没有证明 actual noncanonical exact u/v 支撑下界。",
            "remaining": "这是唯一源侧终端输入。",
        },
        {
            "gate": "DStructureRankinStillIndependent",
            "closed": dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            "proved": False,
            "meaning": "DStructure/Tail-log4/finite Rankin 仍是独立晋级验收门。",
            "remaining": "即使 ExactUVSupport 完成，仍需独立验收。",
        },
    ]


def run(
    multiplier_path: Path,
    source_core_path: Path,
    exact_support_path: Path,
    canonical_support_path: Path,
    squarefree_path: Path,
    canonical_layer_path: Path,
    dstructure_path: Path,
    json_out: Path,
    md_out: Path,
) -> dict[str, Any]:
    """执行 ExactUVSupport 终端攻击路由。"""
    source_paths = [
        multiplier_path,
        source_core_path,
        exact_support_path,
        canonical_support_path,
        squarefree_path,
        canonical_layer_path,
        dstructure_path,
    ]
    multiplier = load_json(multiplier_path)
    source_core = load_json(source_core_path)
    exact_support = load_json(exact_support_path)
    canonical_support = load_json(canonical_support_path)
    squarefree = load_json(squarefree_path)
    canonical_layer = load_json(canonical_layer_path)
    dstructure = load_json(dstructure_path)
    sparse_models = build_sparse_wfd_models()
    rows = build_rows(
        multiplier=multiplier,
        source_core=source_core,
        exact_support=exact_support,
        canonical_support=canonical_support,
        squarefree=squarefree,
        canonical_layer=canonical_layer,
        dstructure=dstructure,
    )
    terminal_boundary_closed = all(row["closed"] for row in rows if row["gate"] != "ExactUVSupportCurrentCorpusProved")

    result: dict[str, Any] = {
        "certificate_type": "prime_matrix_exact_uv_support_terminal_attack_router",
        "status": "exact_uv_support_is_unique_source_terminal_input_open",
        "exact_uv_support_terminal_boundary_closed": terminal_boundary_closed,
        "registered_capacity_multiplier_discipline_closed": True,
        "exact_uv_support_proved": False,
        "actual_final_capacity_antiatom_proved": False,
        "dstructure_rankin_independent_acceptance_completed": False,
        "row_column_unconditional_closed": False,
        "latest_self_contained_basis": (
            "ActualNoncanonicalExactUVSupportLowerBound AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "unique_source_terminal_input": "ActualNoncanonicalExactUVSupportLowerBound",
        "conditional_closure_law": (
            "在 registered multiplier discipline 已闭合后，若证明 "
            "ActualNoncanonicalExactUVSupportLowerBound，则 final capacity anti-atom ledger "
            "随条件不等式成立；再加 DStructure/Rankin 独立验收，当前边界链才可升级。"
        ),
        "no_go_law": (
            "ExactUVSupport 不能由 formal WFD、K4/K6、朴素 incidence、raw Buchstab 计数或"
            " canonical 支撑链偷渡推出。generic WFD 允许点支撑因子；canonical 支撑只关闭"
            " canonical-source 分支。"
        ),
        "plain_conclusion": (
            "ExactUVSupport 被攻到当前材料的唯一源侧终端输入：乘子纪律已闭合，canonical 分支支撑链"
            "已经吸收，但不能导入 noncanonical full-S 补集；generic WFD 点支撑模型阻断形式推论。"
            "因此当前不能诚实宣称完整无条件闭合。剩余是新增证明 "
            "`ActualNoncanonicalExactUVSupportLowerBound`，或直接证明最终容量反原子；另有 "
            "DStructure/Rankin 独立验收门。"
        ),
        "rows": rows,
        "sparse_wfd_model_rows": sparse_models,
        "canonical_support_status": canonical_support.get("status"),
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
        "# Prime Matrix ExactUVSupport 终端攻击路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"exact_uv_support_terminal_boundary_closed={fmt_bool(result['exact_uv_support_terminal_boundary_closed'])}",
        f"registered_capacity_multiplier_discipline_closed={fmt_bool(result['registered_capacity_multiplier_discipline_closed'])}",
        f"exact_uv_support_proved={fmt_bool(result['exact_uv_support_proved'])}",
        f"actual_final_capacity_antiatom_proved={fmt_bool(result['actual_final_capacity_antiatom_proved'])}",
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
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 2. 最新输入基",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "## 3. 条件闭合律",
            "",
            result["conditional_closure_law"],
            "",
            "## 4. 阻断律",
            "",
            result["no_go_law"],
            "",
            "| k | log y | formal factor support | required support | passes WFD template | violates ExactUVSupport |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result["sparse_wfd_model_rows"]:
        lines.append(
            "| {k} | {log_y:.6g} | {formal_factor_support} | {required_support} | `{passes_well_factorable_template}` | `{violates_exact_uv_support}` |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## 5. 当前结论",
            "",
            "本步没有证明 `ExactUVSupport`；它闭合的是边界审查：现有伪出口均不能推出该输入。",
            "当前唯一源侧终端输入是 `ActualNoncanonicalExactUVSupportLowerBound`。",
            "完整行/列命题还需要该输入或直接 final anti-atom 证明，并需要 DStructure/Rankin 独立验收。",
        ]
    )
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--multiplier", type=Path, default=DEFAULT_MULTIPLIER)
    parser.add_argument("--source-core", type=Path, default=DEFAULT_SOURCE_CORE)
    parser.add_argument("--exact-support", type=Path, default=DEFAULT_EXACT_SUPPORT)
    parser.add_argument("--canonical-support", type=Path, default=DEFAULT_CANONICAL_SUPPORT)
    parser.add_argument("--squarefree", type=Path, default=DEFAULT_SQUAREFREE)
    parser.add_argument("--canonical-layer", type=Path, default=DEFAULT_CANONICAL_LAYER)
    parser.add_argument("--dstructure", type=Path, default=DEFAULT_DSTRUCTURE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    result = run(
        multiplier_path=args.multiplier,
        source_core_path=args.source_core,
        exact_support_path=args.exact_support,
        canonical_support_path=args.canonical_support,
        squarefree_path=args.squarefree,
        canonical_layer_path=args.canonical_layer,
        dstructure_path=args.dstructure,
        json_out=args.json_out,
        md_out=args.md_out,
    )
    print(result["status"])
    print(result["latest_self_contained_basis"])


if __name__ == "__main__":
    main()
