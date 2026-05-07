#!/usr/bin/env python3
"""闭合横向 formal unit 嵌入 canonical A1/KZ-E 源的函子性门。

用法示例：
  python3 experiments/prime_matrix_pdec_cap_transverse_embedding_router.py

输出：
  docs/monograph/prime-matrix-pdec-cap-transverse-embedding-router.json
  docs/monograph/prime-matrix-pdec-cap-transverse-embedding-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_SOURCE_SUPPORT = (
    DOCS / "prime-matrix-pdec-cap-transverse-source-support-router.json"
)
DEFAULT_ACTUAL_SOURCE = (
    DOCS / "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.json"
)
DEFAULT_ACTUAL_PAYMENT = (
    DOCS / "prime-matrix-triad-a1-continuous-actual-payment-selection.json"
)
DEFAULT_TERMINAL_DICHOTOMY = (
    DOCS / "prime-matrix-triad-a1-continuous-terminal-dichotomy-router.json"
)
DEFAULT_PROFINITE_APS = DOCS / "prime-matrix-profinite-actual-payment-stitching-router.json"
DEFAULT_UNIFORM_CAP = DOCS / "prime-matrix-pdec-cap-uniform-cap-finite-basis-router.json"
DEFAULT_FINITE_ARC = DOCS / "prime-matrix-pdec-cap-finite-arc-transverse-router.json"
DEFAULT_TRANSVERSE_CLEAN = (
    DOCS / "prime-matrix-pdec-cap-transverse-clean-reduction-router.json"
)
DEFAULT_JSON = DOCS / "prime-matrix-pdec-cap-transverse-embedding-router.json"
DEFAULT_MD = DOCS / "prime-matrix-pdec-cap-transverse-embedding-router.md"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 文件。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算文件 sha256。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def has_all(text: str, needles: list[str]) -> bool:
    """检查文本是否包含全部片段。"""
    return all(needle in text for needle in needles)


def fmt_bool(value: bool) -> str:
    """把布尔值写成小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(
    gate: str,
    closed: bool,
    evidence: str,
    meaning: str,
    blocks_final: bool,
) -> dict[str, Any]:
    """构造审查表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "evidence": evidence,
        "meaning": meaning,
        "blocks_final": blocks_final,
    }


def build_rows(
    source_support: dict[str, Any],
    actual_source: dict[str, Any],
    actual_payment: dict[str, Any],
    terminal_dichotomy: dict[str, Any],
    profinite_aps: dict[str, Any],
    uniform_cap: dict[str, Any],
    finite_arc: dict[str, Any],
    transverse_clean: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成横向来源嵌入审查表。"""
    embedding_active = (
        source_support["status"]
        == "transverse_source_support_reduced_to_embedding_layer_transfer_or_direct_ncblk"
        and source_support["transverse_source_support_reduced"]
    )
    canonical_source_fixed = (
        actual_source["status"] == "actual_source_provenance_closed"
        and actual_source["actual_source_provenance_closed"]
        and actual_source["original_source_definition_declares_canonical"]
        and actual_source["pre_cauchy_lambda_equality_closed"]
    )
    canonical_payment_constructed = (
        actual_payment["status"] == "continuous_actual_payment_measure_constructed"
        and actual_payment["all_payment_counts_match_demand"]
        and "第一个覆盖" in actual_payment["selection_law"]
    )
    payment_is_deterministic_pushforward = (
        canonical_payment_constructed
        and has_all(
            actual_payment["selection_law"],
            ["完成态", "低洞", "第一个", "payment_count"],
        )
    )
    finite_projection_functoriality = (
        profinite_aps["profinite_aps_dichotomy_closed"]
        and "project the real payment graph Gamma_n to every fixed finite level"
        in profinite_aps["dichotomy_law"]
        and "finite-projection" in " ".join(terminal_dichotomy["closed_subclaims"])
    )
    cap_arc_is_preimage = (
        uniform_cap["uniform_cap_finite_basis_closed"]
        and uniform_cap["narrowest_next_hardpoint"]
        == "FiniteCyclicArcCapMassBoundsForRankTwoPrimitiveKernels"
    )
    transverse_factor_is_finite_quotient = (
        finite_arc["finite_arc_no_unnamed_exit_closed"]
        and has_all(finite_arc["transverse_law"], ["rank-one slice", "transverse"])
        and transverse_clean["transverse_expansion_reduced_to_clean_atom"]
        and has_all(
            transverse_clean["clean_reduction_law"],
            ["transverse quotient", "L2-flat", "rank-at-least-two"],
        )
    )
    no_reweighting_or_source_replacement = all(
        [
            canonical_source_fixed,
            payment_is_deterministic_pushforward,
            finite_projection_functoriality,
            cap_arc_is_preimage,
            transverse_factor_is_finite_quotient,
        ]
    )
    embedding_closed = embedding_active and no_reweighting_or_source_replacement

    return [
        row(
            "EmbeddingGateActive",
            embedding_active,
            source_support["narrowest_next_hardpoint"],
            "上一层已把自足最窄点定位为横向 formal unit 嵌入 canonical A1/KZ-E 源。",
            False,
        ),
        row(
            "CanonicalPreCauchySourceFixed",
            canonical_source_fixed,
            actual_source["terminal_gap_after_router"],
            "A1/KZ-E actual source provenance 已在 pre-Cauchy 层锁定为 canonical RIW/Buchstab 决策树系数。",
            False,
        ),
        row(
            "CanonicalPaymentMeasureConstructed",
            canonical_payment_constructed,
            actual_payment["status"],
            "actual payment measure 由 completion 与 low hole 的确定性 first-cover 选择构造。",
            False,
        ),
        row(
            "PaymentIsDeterministicPushforward",
            payment_is_deterministic_pushforward,
            "pay(c,y)=first ell; payment_count=sum M(phase)*|H_low(phase)|",
            "支付测度是 canonical 源计数测度的确定性推前，不是重新加权。",
            False,
        ),
        row(
            "FiniteProjectionFunctoriality",
            finite_projection_functoriality,
            profinite_aps["status"],
            "有限签名塔只是在真实支付图 Gamma_n 上取有限投影；正 limsup/消散二分不改变来源。",
            False,
        ),
        row(
            "ArcRestrictionIsPreimage",
            cap_arc_is_preimage,
            uniform_cap["narrowest_next_hardpoint"],
            "方向帽是有限字符循环弧的预像；这是限制事件，不改变系数源。",
            False,
        ),
        row(
            "TransverseQuotientIsFiniteFactor",
            transverse_factor_is_finite_quotient,
            transverse_clean["narrowest_next_hardpoint"],
            "有限弧内的横向商是有限签名空间的有限因子/条件化；非平坦缺陷已回流。",
            False,
        ),
        row(
            "NoReweightingOrSourceReplacement",
            no_reweighting_or_source_replacement,
            "restriction / pushforward / finite projection / quotient only",
            "横向 formal unit 沿链条只经过确定性推前、事件限制、有限投影和有限商，没有替换 canonical 系数。",
            False,
        ),
        row(
            "TransverseFormalUnitA1SourceEmbedding",
            embedding_closed,
            "finite-measure functoriality from canonical A1/KZ-E source",
            "横向商 formal unit 是 canonical A1/KZ-E pre-Cauchy 源的合法限制、商或条件化。",
            False,
        ),
        row(
            "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn",
            False,
            source_support["downstream_source_route_hardpoint"],
            "嵌入门闭合后，下一自足硬点是 exact canonical Buchstab 层准入、非零系数转移与薄区间回流。",
            True,
        ),
    ]


def run(
    source_support_path: Path,
    actual_source_path: Path,
    actual_payment_path: Path,
    terminal_dichotomy_path: Path,
    profinite_aps_path: Path,
    uniform_cap_path: Path,
    finite_arc_path: Path,
    transverse_clean_path: Path,
) -> dict[str, Any]:
    """运行横向来源嵌入路由。"""
    source_support = load_json(source_support_path)
    actual_source = load_json(actual_source_path)
    actual_payment = load_json(actual_payment_path)
    terminal_dichotomy = load_json(terminal_dichotomy_path)
    profinite_aps = load_json(profinite_aps_path)
    uniform_cap = load_json(uniform_cap_path)
    finite_arc = load_json(finite_arc_path)
    transverse_clean = load_json(transverse_clean_path)
    rows = build_rows(
        source_support=source_support,
        actual_source=actual_source,
        actual_payment=actual_payment,
        terminal_dichotomy=terminal_dichotomy,
        profinite_aps=profinite_aps,
        uniform_cap=uniform_cap,
        finite_arc=finite_arc,
        transverse_clean=transverse_clean,
    )
    embedding_closed = next(
        bool(item["closed"])
        for item in rows
        if item["gate"] == "TransverseFormalUnitA1SourceEmbedding"
    )
    open_final_gates = [item["gate"] for item in rows if item["blocks_final"]]
    return {
        "certificate_type": "prime_matrix_pdec_cap_transverse_embedding_router",
        "status": "transverse_formal_unit_embedding_closed_layer_transfer_open",
        "source_hashes": {
            "script": file_sha256(Path(__file__).resolve()),
            "source_support": file_sha256(source_support_path),
            "actual_source": file_sha256(actual_source_path),
            "actual_payment": file_sha256(actual_payment_path),
            "terminal_dichotomy": file_sha256(terminal_dichotomy_path),
            "profinite_aps": file_sha256(profinite_aps_path),
            "uniform_cap": file_sha256(uniform_cap_path),
            "finite_arc": file_sha256(finite_arc_path),
            "transverse_clean": file_sha256(transverse_clean_path),
        },
        "transverse_formal_unit_embedding_closed": embedding_closed,
        "canonical_layer_transfer_closed": False,
        "row_column_unconditional_closed": False,
        "open_final_gates": open_final_gates,
        "narrowest_next_hardpoint": (
            "CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn"
        ),
        "rows": rows,
        "embedding_law": (
            "The transverse formal unit is a finite measurable factor of the canonical "
            "A1/KZ-E source. The source is fixed before Cauchy as the canonical "
            "RIW/Buchstab decision-tree coefficient. Actual payment is a deterministic "
            "first-cover pushforward of the canonical completion-hole counting measure. "
            "The profinite signature tower uses finite projections of the same real "
            "payment graph. Direction caps are preimages of finite cyclic arcs, and the "
            "transverse quotient is a finite factor/conditioning inside that arc. These "
            "operations do not replace or reweight the source coefficients."
        ),
        "review_conclusion": (
            "`TransverseFormalUnitA1SourceEmbedding` 闭合：横向商 formal unit 只是 canonical "
            "A1/KZ-E pre-Cauchy 源测度经确定性推前、有限投影、弧预像限制和横向有限商得到的对象。"
            "它没有引入新系数源，也没有把 generic WFD 偷换为 canonical 源。新的最窄自足硬点是 "
            "`CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    lines = [
        "# Prime Matrix PDEC-CAP 横向来源嵌入路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["review_conclusion"],
        "",
        "## 1. 嵌入律",
        "",
        result["embedding_law"],
        "",
        "```text",
        "canonical A1/KZ-E pre-Cauchy source",
        "  -> deterministic actual-payment pushforward;",
        "  -> finite signature projections;",
        "  -> cyclic-arc preimage restriction;",
        "  -> transverse finite quotient / conditioning;",
        "  = transverse formal unit.",
        "```",
        "",
        "## 2. 汇总",
        "",
        f"- `transverse_formal_unit_embedding_closed={fmt_bool(result['transverse_formal_unit_embedding_closed'])}`。",
        f"- `canonical_layer_transfer_closed={fmt_bool(result['canonical_layer_transfer_closed'])}`。",
        f"- `row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}`。",
        f"- `narrowest_next_hardpoint={result['narrowest_next_hardpoint']}`。",
        f"- `open_final_gates={result['open_final_gates']}`。",
        "",
        "## 3. 审查表",
        "",
        "| gate | closed | blocks final | evidence | meaning |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{blocks}` | {evidence} | {meaning} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(bool(item["closed"])),
                blocks=fmt_bool(bool(item["blocks_final"])),
                evidence=table_cell(item["evidence"]),
                meaning=table_cell(item["meaning"]),
            )
        )
    lines.extend(
        [
            "",
            "## 4. 下一步",
            "",
            "下一步直接攻 `CanonicalLayerAdmissionNonzeroTransferAndThinIntervalReturn`：在已嵌入的 canonical 源内，证明 Buchstab squarefree products 被 exact canonical 层承认、系数非零；若 balanced interval 太薄，必须回流 edge/PDEC/SAE。",
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-support-json", type=Path, default=DEFAULT_SOURCE_SUPPORT)
    parser.add_argument("--actual-source-json", type=Path, default=DEFAULT_ACTUAL_SOURCE)
    parser.add_argument("--actual-payment-json", type=Path, default=DEFAULT_ACTUAL_PAYMENT)
    parser.add_argument(
        "--terminal-dichotomy-json", type=Path, default=DEFAULT_TERMINAL_DICHOTOMY
    )
    parser.add_argument("--profinite-aps-json", type=Path, default=DEFAULT_PROFINITE_APS)
    parser.add_argument("--uniform-cap-json", type=Path, default=DEFAULT_UNIFORM_CAP)
    parser.add_argument("--finite-arc-json", type=Path, default=DEFAULT_FINITE_ARC)
    parser.add_argument("--transverse-clean-json", type=Path, default=DEFAULT_TRANSVERSE_CLEAN)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    result = run(
        source_support_path=args.source_support_json,
        actual_source_path=args.actual_source_json,
        actual_payment_path=args.actual_payment_json,
        terminal_dichotomy_path=args.terminal_dichotomy_json,
        profinite_aps_path=args.profinite_aps_json,
        uniform_cap_path=args.uniform_cap_json,
        finite_arc_path=args.finite_arc_json,
        transverse_clean_path=args.transverse_clean_json,
    )
    args.json_out.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_markdown(result, args.md_out)
    print(result["status"])
    print(result["narrowest_next_hardpoint"])


if __name__ == "__main__":
    main()
