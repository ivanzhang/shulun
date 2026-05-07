#!/usr/bin/env python3
"""硬攻 ActualKZESourceCoefficientIdentificationOrCleanReturn 的源头锁定合同。

用法示例：
  python3 experiments/prime_matrix_triad_a1_source_identification_router.py

输出：
  docs/monograph/prime-matrix-triad-a1-source-identification-router.json
  docs/monograph/prime-matrix-triad-a1-source-identification-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
DEFAULT_DECISION_TREE = DOCS / "prime-matrix-triad-a1-decision-tree-formula-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-triad-a1-source-identification-router.json"
DEFAULT_MD = DOCS / "prime-matrix-triad-a1-source-identification-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def build_gate_rows() -> list[dict[str, Any]]:
    """列出源头系数识别门控。"""
    return [
        {
            "gate": "FormalWFDSourceRejected",
            "available": "previous routers showed formal WFD/Type/Fourier inputs do not force source entropy",
            "needed": "do not identify lambda_c from well-factorability alone",
            "gap": "none: this false shortcut has already been blocked",
            "route": "arbitrary well-factorable lambda_c cannot use canonical support proof",
            "closed": True,
        },
        {
            "gate": "CanonicalRIWBuchstabSourceLock",
            "available": "decision-tree formula exists algebraically for canonical RIW/Buchstab weights",
            "needed": "the actual A1/KZ-E lambda_c is declared and proved equal to that canonical coefficient",
            "gap": "current A1 ledger still treats lambda_c as an exact source to be identified, not as a locked formula",
            "route": "add a source-lock contract before invoking the support chain",
            "closed": False,
        },
        {
            "gate": "SourceLockPreservesUpstreamBlocks",
            "available": "dyadic/K6 bookkeeping and Type/Fourier wrappers already exist",
            "needed": "locking lambda_c to the canonical tree does not change the upstream WFD/KZ-E object",
            "gap": "must verify source-lock is not silently replacing the original target",
            "route": "show equality before Cauchy/dispersion, not after changing coefficients",
            "closed": False,
        },
        {
            "gate": "UnlockedSourceCleanReturn",
            "available": "external DI/BFI and PDEC/SAE exits exist",
            "needed": "if source lock is absent, clean A1 cannot use the internal support proof",
            "gap": "the missing source-lock exit must be recorded as a clean failure",
            "route": "unlocked source returns to missing-row/PDEC/SAE or external DI/BFI",
            "closed": False,
        },
        {
            "gate": "SourceLockImpliesInternalSupportChain",
            "available": "all downstream reductions from canonical source to support are conditional",
            "needed": "source lock + path budget",
            "gap": "conditional implication is direct; source lock remains",
            "route": "Canonical source lock feeds the already built decision-tree/support chain",
            "closed": True,
        },
    ]


def run(decision_tree_path: Path) -> dict[str, Any]:
    """运行源头识别路由。"""
    decision_tree = load_json(decision_tree_path)
    return {
        "certificate_type": "triad_a1_source_identification_router",
        "status": "source_identification_reduced_to_canonical_source_lock_contract",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "decision_tree_formula_json": file_sha256(decision_tree_path),
        },
        "decision_tree_input_status": decision_tree["status"],
        "decision_tree_input_next_target": decision_tree["next_internal_target"],
        "gate_rows": build_gate_rows(),
        "formal_wfd_source_rejected": True,
        "canonical_source_lock_closed": False,
        "source_lock_preserves_upstream_blocks_closed": False,
        "unlocked_source_clean_return_closed": False,
        "source_identification_closed": False,
        "conditional_source_lock_implies_internal_support_chain": True,
        "reduction_law": (
            "Actual source identification cannot be replaced by the statement that lambda_c is "
            "well-factorable. The internal support chain applies only if the A1/KZ-E coefficient "
            "is locked to the canonical RIW/Buchstab decision-tree coefficient before dispersion "
            "and Cauchy steps. If the source is merely an arbitrary well-factorable coefficient, "
            "the earlier sparse formal-factor obstruction returns, so the block must exit to a "
            "missing-row/PDEC/SAE contract or use external DI/BFI original dispersion."
        ),
        "next_internal_target": "CanonicalRIWBuchstabSourceLockContract",
        "terminal_gap_after_router": (
            "CanonicalRIWBuchstabSourceLockContractOrExternalDIBFIOriginalDispersion"
        ),
        "review_conclusion": (
            "ActualKZESourceCoefficientIdentification 已被压成 canonical source lock 合同："
            "必须证明 A1/KZ-E 实际 lambda_c 在进入 Cauchy/dispersion 前就等于 "
            "RIW/Buchstab 决策树系数；仅有 well-factorable 性质不够。若没有该锁定，"
            "内部支撑证明不可用，必须回 PDEC/SAE 或外部 DI/BFI。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Triad-A1 Source Identification 路由审计",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 源头锁定律",
        "",
        result["reduction_law"],
        "",
        "```text",
        "well-factorable(lambda_c) is not enough;",
        "internal support route requires:",
        "  lambda_c == canonical RIW/Buchstab decision-tree coefficient",
        "  before Cauchy/dispersion/source transformations;",
        "if not locked:",
        "  return to missing-row/PDEC/SAE or external DI/BFI.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `decision_tree_input_status={result['decision_tree_input_status']}`。",
        f"- `decision_tree_input_next_target={result['decision_tree_input_next_target']}`。",
        f"- `formal_wfd_source_rejected={result['formal_wfd_source_rejected']}`。",
        f"- `conditional_source_lock_implies_internal_support_chain={result['conditional_source_lock_implies_internal_support_chain']}`。",
        f"- `source_identification_closed={result['source_identification_closed']}`。",
        f"- `next_internal_target={result['next_internal_target']}`。",
        f"- `terminal_gap_after_router={result['terminal_gap_after_router']}`。",
        "",
        "## 3. 门控表",
        "",
        "| gate | available | needed | gap | route | closed |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in result["gate_rows"]:
        lines.append(
            "| `{gate}` | {available} | {needed} | {gap} | {route} | `{closed}` |".format(
                gate=table_cell(row["gate"]),
                available=table_cell(row["available"]),
                needed=table_cell(row["needed"]),
                gap=table_cell(row["gap"]),
                route=table_cell(row["route"]),
                closed=row["closed"],
            )
        )

    lines.extend(
        [
            "",
            "## 4. 结论",
            "",
            "新最窄内部目标为：",
            "",
            "```text",
            "CanonicalRIWBuchstabSourceLockContract:",
            "  prove the A1/KZ-E lambda_c is locked to the canonical RIW/Buchstab decision-tree coefficient;",
            "  prove this lock preserves the original upstream WFD/KZ-E target;",
            "  otherwise route to PDEC/SAE missing-row or external DI/BFI.",
            "```",
            "",
            "这仍不是行命题最终闭合；但它把源头识别硬点压成一个明确的合同检查。",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decision-tree-json", type=Path, default=DEFAULT_DECISION_TREE)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(args.decision_tree_json)
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(
        json.dumps(
            {
                "status": result["status"],
                "next_internal_target": result["next_internal_target"],
                "terminal_gap_after_router": result["terminal_gap_after_router"],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
