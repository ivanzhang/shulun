#!/usr/bin/env python3
"""Prime Matrix 破奇偶候选源障碍审计。

用法示例：
  python3 experiments/prime_matrix_parity_breaking_obstruction_audit.py
  python3 -m json.tool docs/monograph/prime-matrix-parity-breaking-obstruction-audit.json

本脚本把可用的破奇偶/准破奇偶外部定理逐项验收到 Prime Matrix 行列
目标所需的五个门：素数对象、平方窗口、刚性点态网格、同对象实际源、
无条件性。它不尝试证明 H_P；目标是防止把 P2 almost-prime、平均分布、
或不同非线性对象误写成本文的无条件闭合。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-parity-breaking-obstruction"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-audit.json"
OUT_MD = DOCS / f"{SLUG}-audit.md"

FRONTIER_VERIFIED_DATE = "2026-05-23"

DEPENDENCIES = [
    DOCS / "prime-matrix-external-frontier-residual-gap-audit.json",
    DOCS / "prime-matrix-external-frontier-residual-gap-audit.md",
    DOCS / "prime-matrix-phi-lpf-combinatorial-exactness-parity-barrier-review-router.md",
    DOCS / "external-theorem-index.md",
    DOCS / "claim-status-table.md",
    DOCS / "frontier-honest-status-and-true-side-theorems-20260522.md",
    ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex",
]

GATES = [
    "PrimeObjectNotP2AlmostPrime",
    "SquareScaleWindowOrP2ColumnCompatibility",
    "RigidPointwiseGridOrFixedPrimeModulusZeroException",
    "SameObjectNonlinearActualSourceConstructorBeforeProjection",
    "UnconditionalPublishedOrIndependentlyAcceptedInput",
]


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def md_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def bool_text(value: Any) -> str:
    """把布尔值输出为小写文本。"""
    return str(bool(value)).lower()


def candidate(
    *,
    name: str,
    source: str,
    status: str,
    category: str,
    prime_object_gate: bool,
    square_scale_gate: bool,
    pointwise_grid_gate: bool,
    same_object_source_gate: bool,
    unconditional_gate: bool,
    parity_breaking_strength: str,
    obstruction: str,
    residual_gate: str,
    usable_as: str,
) -> dict[str, Any]:
    """构造候选源验收行。"""
    gates = {
        GATES[0]: prime_object_gate,
        GATES[1]: square_scale_gate,
        GATES[2]: pointwise_grid_gate,
        GATES[3]: same_object_source_gate,
        GATES[4]: unconditional_gate,
    }
    direct_closure = all(gates.values())
    return {
        "name": name,
        "source": source,
        "status": status,
        "category": category,
        "gates": gates,
        "direct_row_column_closure": direct_closure,
        "parity_breaking_strength": parity_breaking_strength,
        "obstruction": obstruction,
        "residual_gate": residual_gate,
        "usable_as": usable_as,
    }


def source_hashes() -> dict[str, str]:
    """登记本脚本和直接依赖哈希。"""
    paths = [Path(__file__).resolve(), *DEPENDENCIES]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def build_candidates() -> list[dict[str, Any]]:
    """列出当前可引用的破奇偶候选源与失败门。"""
    return [
        candidate(
            name="Li-Zhang-Cai least P2 almost-prime in AP",
            source="https://arxiv.org/abs/2103.13360",
            status="arXiv_v2_wrong_parity_object",
            category="P2_almost_prime_AP",
            prime_object_gate=False,
            square_scale_gate=True,
            pointwise_grid_gate=True,
            same_object_source_gate=False,
            unconditional_gate=False,
            parity_breaking_strength="enters_P2_square_but_keeps_P2_parity_shadow",
            obstruction="给出的是至多两个素因子的 almost-prime，不是素数；正好卡在奇偶对象门。",
            residual_gate="PrimeObjectNotP2AlmostPrime",
            usable_as="sharp_column_parity_barrier_marker",
        ),
        candidate(
            name="Friedlander-Iwaniec polynomial X^2+Y^4",
            source="https://arxiv.org/abs/math/9811185",
            status="published_model_primary_arxiv_available",
            category="nonlinear_prime_values",
            prime_object_gate=True,
            square_scale_gate=False,
            pointwise_grid_gate=False,
            same_object_source_gate=False,
            unconditional_gate=True,
            parity_breaking_strength="genuine_nonlinear_parity_breaking_model",
            obstruction="证明不同非线性多项式族含无穷多素数；没有把每个 Prime Matrix 行/列嵌入该族的同对象源构造。",
            residual_gate="SameObjectNonlinearActualSourceConstructorBeforeProjection",
            usable_as="technical_model_not_importable_closure",
        ),
        candidate(
            name="Bombieri-Friedlander-Iwaniec / Maynard well-factorable large-moduli AP",
            source="https://arxiv.org/abs/2006.07088",
            status="external_dispersion_technology_class",
            category="well_factorable_AP_dispersion",
            prime_object_gate=True,
            square_scale_gate=False,
            pointwise_grid_gate=False,
            same_object_source_gate=False,
            unconditional_gate=True,
            parity_breaking_strength="deep_average_dispersion_not_pointwise_source",
            obstruction="提供 AP/权重平均分布技术；未给固定素模数 P、每个剩余类、P^2 方阵内的零例外定理，也未匹配本文 full-S non-AP WFD 对象。",
            residual_gate="MeanValueAPToFixedPrimeModulusZeroExceptionTransfer",
            usable_as="candidate_external_theorem_match_after_exact_variable_translation",
        ),
        candidate(
            name="Deshouillers-Iwaniec / Kuznetsov spectral large sieve",
            source="https://doi.org/10.1007/BF01390728",
            status="published_spectral_tool",
            category="kloosterman_spectral_dispersion",
            prime_object_gate=False,
            square_scale_gate=False,
            pointwise_grid_gate=False,
            same_object_source_gate=False,
            unconditional_gate=True,
            parity_breaking_strength="cancellation_tool_not_prime_constructor",
            obstruction="谱大筛是 Kloosterman 平均抵消工具，不直接产生素数对象或刚性行列点态正性。",
            residual_gate="SameObjectNonlinearActualSourceConstructorBeforeProjection",
            usable_as="subtool_for_exact_KLS_match_only",
        ),
        candidate(
            name="Ford-Maynard prime-producing sieve framework",
            source="https://arxiv.org/abs/2407.14368",
            status="frontier_framework",
            category="prime_producing_sieve_theory",
            prime_object_gate=True,
            square_scale_gate=False,
            pointwise_grid_gate=False,
            same_object_source_gate=False,
            unconditional_gate=False,
            parity_breaking_strength="framework_for_sources_not_current_prime_matrix_source",
            obstruction="给出 prime-producing sieve 的理论框架；尚未包含本文 P 行/列方阵的实际构造器与逐点窗口常数。",
            residual_gate="SameObjectNonlinearActualSourceConstructorBeforeProjection",
            usable_as="design_guidance_for_future_internal_constructor",
        ),
        candidate(
            name="Maynard small gaps / multidimensional Selberg weights",
            source="https://arxiv.org/abs/1311.4600",
            status="published_prime_object_wrong_conclusion_type",
            category="multidimensional_sieve",
            prime_object_gate=True,
            square_scale_gate=False,
            pointwise_grid_gate=False,
            same_object_source_gate=False,
            unconditional_gate=True,
            parity_breaking_strength="finds_primes_in_tuples_not_every_rigid_interval",
            obstruction="结论是无穷多 admissible tuple 中多素数，而不是每个长度 P 的刚性区间或每个 mod P 列中有素数。",
            residual_gate="RigidPointwiseGridOrFixedPrimeModulusZeroException",
            usable_as="wrong_conclusion_type",
        ),
        candidate(
            name="Rosser-Iwaniec beta sieve / linear sieve",
            source="https://link.springer.com/book/10.1007/978-3-642-56342-7",
            status="classical_published_but_parity_limited",
            category="linear_sieve",
            prime_object_gate=False,
            square_scale_gate=False,
            pointwise_grid_gate=False,
            same_object_source_gate=False,
            unconditional_gate=True,
            parity_breaking_strength="does_not_break_parity",
            obstruction="在 H_P 的 s<=2 区域下界函数退化为 0；它解释屏障而不提供破屏障源。",
            residual_gate="NonlinearParityBreakingActualSourceConstructor",
            usable_as="negative_control",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造破奇偶障碍审计 payload。"""
    candidates = build_candidates()
    direct = [item for item in candidates if item["direct_row_column_closure"]]
    p2_marker = next(item for item in candidates if item["category"] == "P2_almost_prime_AP")
    nonlinear_model = next(item for item in candidates if item["category"] == "nonlinear_prime_values")
    return {
        "certificate_type": "prime_matrix_parity_breaking_obstruction_audit",
        "frontier_verified_date": FRONTIER_VERIFIED_DATE,
        "status": "parity_breaking_candidates_screened_no_direct_closure",
        "audit_gates": GATES,
        "direct_closure_candidate_count": len(direct),
        "direct_closure_candidates": [item["name"] for item in direct],
        "best_square_compatible_wrong_object": p2_marker["name"],
        "best_genuine_parity_breaking_model_not_same_object": nonlinear_model["name"],
        "external_lemma_version_unconditional_closed": False,
        "internal_self_contained_closed": False,
        "row_column_unconditional_closed": False,
        "new_residual_basis_after_parity_audit": [
            "PrimeObjectNotP2AlmostPrime",
            "RigidPointwiseGridOrFixedPrimeModulusZeroException",
            "SameObjectNonlinearActualSourceConstructorBeforeProjection",
            "MeanValueAPToFixedPrimeModulusZeroExceptionTransfer",
            "PointwiseShortIntervalPrimeTheoremThetaLeHalf",
            "LinnikExponentLeTwoWithSquareWindowConstants",
        ],
        "noncycle_progress_claim": (
            "本审计不把 P2、平均 AP 或不同非线性多项式改名为证明；"
            "它把破奇偶路线压成同对象实际源构造或固定素模数零例外转移。"
        ),
        "candidates": candidates,
        "source_hashes": source_hashes(),
    }


def gate_summary(item: dict[str, Any]) -> str:
    """压缩输出失败门。"""
    failed = [name for name, ok in item["gates"].items() if not ok]
    return ", ".join(failed) if failed else "none"


def candidates_markdown(candidates: list[dict[str, Any]]) -> str:
    """生成候选源审计表。"""
    lines = [
        "| candidate | category | status | direct closure | failed gates | usable as | obstruction |",
        "|---|---|---|---|---|---|---|",
    ]
    for item in candidates:
        lines.append(
            "| {name} | `{category}` | `{status}` | `{closed}` | {failed} | {usable} | {obstruction} |".format(
                name=md_cell(item["name"]),
                category=md_cell(item["category"]),
                status=md_cell(item["status"]),
                closed=bool_text(item["direct_row_column_closure"]),
                failed=md_cell(gate_summary(item)),
                usable=md_cell(item["usable_as"]),
                obstruction=md_cell(item["obstruction"]),
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 审计文档。"""
    lines = [
        "# Prime Matrix 破奇偶候选源障碍审计",
        "",
        f"**状态**：`{payload['status']}`",
        f"**核验日期**：`{payload['frontier_verified_date']}`",
        "",
        "## 1. 原子结论",
        "",
        "- 当前没有任何外部破奇偶候选源同时通过五个门。",
        "- Li--Zhang--Cai 的 `P2` AP 结果进入 `P^2` 方阵，但对象不是素数。",
        "- Friedlander--Iwaniec 是真正非线性破奇偶模型，但对象不是 Prime Matrix 行/列。",
        "- BFI/DI/Kuznetsov/Maynard 技术只能作为未来同对象 theorem-match 或构造器的工具，不能直接替代固定网格点态正性。",
        "- 因此最新硬点不是“再找一个筛恒等式”，而是构造同对象实际素数源，或证明 fixed `q=P` 零例外转移。",
        "",
        "## 2. 五门验收",
        "",
        "```text",
        *payload["audit_gates"],
        "```",
        "",
        "## 3. 候选源审计表",
        "",
        candidates_markdown(payload["candidates"]),
        "",
        "## 4. 最新剩余基",
        "",
        "```text",
        *payload["new_residual_basis_after_parity_audit"],
        "```",
        "",
        "## 5. 边界声明",
        "",
        payload["noncycle_progress_claim"],
        "",
        "```text",
        f"external_lemma_version_unconditional_closed={bool_text(payload['external_lemma_version_unconditional_closed'])}",
        f"internal_self_contained_closed={bool_text(payload['internal_self_contained_closed'])}",
        f"row_column_unconditional_closed={bool_text(payload['row_column_unconditional_closed'])}",
        f"direct_closure_candidate_count={payload['direct_closure_candidate_count']}",
        "```",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 与 Markdown 证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")
    print("direct_closure_candidate_count=0")
    print("row_column_unconditional_closed=false")


if __name__ == "__main__":
    main()
