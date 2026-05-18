#!/usr/bin/env python3
"""生成 post-antisplit source-rank 收敛前沿证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_antisplit_source_rank_convergence_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json

输出：
  data/prime-matrix-strict-post-antisplit-source-rank-convergence-ledger.json
  docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.json
  docs/monograph/prime-matrix-strict-post-antisplit-source-rank-convergence-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-antisplit-source-rank-convergence-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-antisplit-source-rank-convergence-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-antisplit-source-rank-convergence-router.md"

ANTISPLIT = DOCS / "prime-matrix-strict-antisplit-trace-exactuv-atomized-frontier-router.json"
NEW_PRIMITIVE = DOCS / "prime-matrix-strict-new-primitive-payload-source-atom-alignment-router.json"
PRETERMINAL_SOURCE = DOCS / "prime-matrix-strict-preterminal-fiber-dispersion-source-atom-router.json"
SOURCE_ENTROPY = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
COMPLETE_KEY = DOCS / "prime-matrix-strict-complete-emitter-key-partition-router.json"
SOURCE_TABLE = DOCS / "prime-matrix-strict-actual-emitter-source-table-router.json"
TERMINAL_SYNC = DOCS / "prime-matrix-strict-terminal-descent-to-pointwise-kernel-sync-router.json"
FIXED_PAIR = DOCS / "prime-matrix-strict-fixed-pair-fiber-bound-router.json"

NEW_ARTIFACT = "NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXTERNAL_SPECTRAL = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
SOURCE_RANK = "ActualPreCauchySourceDomainRankAndExactUVNoCollapseLedger"
DOMAIN_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
REGISTERED_KEY = "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger"
COMPLETE_KEY_LEDGER = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SOURCE_TABLE_LEDGER = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
POINTWISE_KERNEL = "PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate"
ALPHA_ROW = "AlphaRowAnchorPhaseEmissionFormulaLedger"
INDEPENDENT_IDENTITY = "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger"
SAME_UNIT_RANK = "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失不能被解释成证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def source_hashes() -> dict[str, str]:
    """登记本证书吸收的前沿文件哈希。"""
    paths = [
        Path(__file__).resolve(),
        ANTISPLIT,
        NEW_PRIMITIVE,
        PRETERMINAL_SOURCE,
        SOURCE_ENTROPY,
        COMPLETE_KEY,
        SOURCE_TABLE,
        TERMINAL_SYNC,
        FIXED_PAIR,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def convergence_edges() -> list[dict[str, str]]:
    """列出最新吸收链条。"""
    return [
        {
            "from": "AntiSplitTraceExactUVAtomizedFrontier",
            "to": f"{NEW_ARTIFACT} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}",
            "meaning": "antisplit built-in pairing 已落入 signed-lane trace cycle，非循环出口只能走这些命名门。",
        },
        {
            "from": NEW_ARTIFACT,
            "to": SOURCE_RANK,
            "meaning": "独立 new primitive 工件若要破环，必须携带同一 pre-Cauchy actual source 的 rank/no-collapse 包。",
        },
        {
            "from": TERMINAL_DESCENT,
            "to": SOURCE_RANK,
            "meaning": "terminal descent 的当前非循环叶子已经同步到相同 source-rank/no-collapse 包。",
        },
        {
            "from": SOURCE_RANK,
            "to": f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY_LEDGER} AND {FIXED_KEY}",
            "meaning": "source-rank 包的实际内容是源域熵、complete key 分区和 fixed-key 局部重数。",
        },
        {
            "from": DOMAIN_ENTROPY,
            "to": SIGNED_ROW_LAW,
            "meaning": "源域绝对熵的第一生产性字段回到 primitive signed row coefficient law。",
        },
        {
            "from": f"{COMPLETE_KEY_LEDGER} / {REGISTERED_KEY}",
            "to": SOURCE_TABLE_LEDGER,
            "meaning": "registered complete key 分区不能后验补标签，必须来自 actual emitter source table。",
        },
        {
            "from": f"{DOMAIN_ENTROPY} / {COMPLETE_KEY_LEDGER} / {REGISTERED_KEY} / {FIXED_KEY}",
            "to": POINTWISE_KERNEL,
            "meaning": "三条源域/no-collapse 线在同 formal-unit 的逐 primitive alpha/delta 核表上汇合。",
        },
        {
            "from": POINTWISE_KERNEL,
            "to": f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}",
            "meaning": "逐点核表的当前第一硬点是 alpha row anchor/phase 发射公式，并行还需算术恒等式与同表 rank/multiplicity。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总各前沿的吸收结果。"""
    antisplit = data["antisplit"]
    new_primitive = data["new_primitive"]
    preterminal = data["preterminal"]
    entropy = data["entropy"]
    complete_key = data["complete_key"]
    source_table = data["source_table"]
    terminal = data["terminal"]
    fixed_pair = data["fixed_pair"]

    antisplit_active = antisplit.get("row_column_unconditional_closed") is False
    new_primitive_absorbed = (
        new_primitive.get("new_primitive_artifact_reduced_to_source_rank_atom") is True
        or new_primitive.get("status")
        == "strict_new_primitive_payload_reduced_to_actual_source_rank_atom_open"
    )
    source_rank_atomized = (
        preterminal.get("preterminal_fiber_dispersion_source_atomization_closed") is True
    )
    entropy_to_signed = entropy.get("next_direct_attack_target") == SIGNED_ROW_LAW
    registered_to_source_table = complete_key.get("next_direct_attack_target") == SOURCE_TABLE_LEDGER
    source_table_to_declaration = (
        source_table.get("next_direct_attack_target")
        == "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter"
    )
    terminal_to_pointwise = (
        terminal.get("pointwise_kernel_table_is_common_variable_table") is True
        and terminal.get("next_direct_attack_target") == ALPHA_ROW
    )
    fixed_pair_atomized = (
        fixed_pair.get("terminal_gap_after_router")
        == f"{REGISTERED_KEY} AND {FIXED_KEY}"
    )

    return [
        row(
            "PostAntiSplitFrontierImported",
            antisplit_active,
            False,
            "最新 antisplit trace/ExactUV 证书没有闭合行/列命题，只给出 new-primitive/terminal/PDEC/external 与 ExactUV 三原子的合取前沿。",
            antisplit.get("unified_retained_remaining_basis", "antisplit retained basis"),
        ),
        row(
            "NewPrimitiveExitAlreadyAbsorbed",
            new_primitive_absorbed,
            False,
            "`NewPrimitive...` 不是新的独立主攻点；旧证书已要求它提交 source-rank/no-collapse 包或转入命名出口。",
            SOURCE_RANK,
        ),
        row(
            "TerminalDescentConvergesToSameSourceRankPackage",
            terminal.get("source_rank_package_reached") is True,
            False,
            "terminal descent 非循环叶子也回到相同的 source-rank/no-collapse 包，不能作为独立闭合点。",
            SOURCE_RANK,
        ),
        row(
            "SourceRankPackageAtomized",
            source_rank_atomized,
            False,
            "source-rank/no-collapse 包已被拆成源域熵、complete key 与 fixed-key 局部重数。",
            f"{DOMAIN_ENTROPY} AND {COMPLETE_KEY_LEDGER} AND {FIXED_KEY}",
        ),
        row(
            "DomainEntropyReturnsToSignedRowLaw",
            entropy_to_signed,
            False,
            "源域熵首攻点回到 primitive signed row coefficient law；这解释了为什么 signed trace cycle 与 source entropy 是同一底层障碍。",
            SIGNED_ROW_LAW,
        ),
        row(
            "RegisteredKeyNeedsActualSourceTable",
            registered_to_source_table,
            False,
            "complete key 的多对数分区不能由 payment/CRT 后验标签生成，必须先有 actual source table。",
            SOURCE_TABLE_LEDGER,
        ),
        row(
            "SourceTableNeedsPreCauchyDeclaration",
            source_table_to_declaration,
            False,
            "actual source table 的首行是 pre-Cauchy constructor declaration；没有该行，summand/权重/return 都只是后验表。",
            "PreCauchyConstructorDeclarationLineForActualNoncanonicalEmitter",
        ),
        row(
            "FixedPairFiberStillUsesSameKeyMultiplicityAtoms",
            fixed_pair_atomized,
            False,
            "fixed-pair fiber 的形式不等式已闭合，但 registered key 与 fixed-key multiplicity 仍是实际数学缺口。",
            f"{REGISTERED_KEY} AND {FIXED_KEY}",
        ),
        row(
            "AllInternalSourceRankRoutesMeetAtPointwiseKernelTable",
            terminal_to_pointwise,
            False,
            "new primitive、terminal descent、source entropy、complete key 与 fixed-key multiplicity 的非后验共同变量表是逐 primitive alpha/delta 核表。",
            POINTWISE_KERNEL,
        ),
        row(
            "LatestPriorityAtomPinned",
            terminal.get("alpha_row_anchor_phase_emission_formula_proved") is False,
            False,
            "当前第一可攻原子是 alpha row anchor/phase 发射公式；并行还需 pre-Cauchy 算术恒等式和同表 rank/multiplicity。",
            f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只完成 post-antisplit 后的旧出口吸收与共同核表定位；未证明 alpha 发射、算术恒等式、rank/multiplicity、PDEC/外部谱或最终晋级门。",
            "row/column theorem still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成统一收敛证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "antisplit": load_json(ANTISPLIT),
        "new_primitive": load_json(NEW_PRIMITIVE),
        "preterminal": load_json(PRETERMINAL_SOURCE),
        "entropy": load_json(SOURCE_ENTROPY),
        "complete_key": load_json(COMPLETE_KEY),
        "source_table": load_json(SOURCE_TABLE),
        "terminal": load_json(TERMINAL_SYNC),
        "fixed_pair": load_json(FIXED_PAIR),
    }
    rows = build_rows(data)
    pointwise_basis = f"{ALPHA_ROW} AND {INDEPENDENT_IDENTITY} AND {SAME_UNIT_RANK}"
    retained_basis = (
        f"(({pointwise_basis}) OR {PDEC_SCOPE} OR {EXTERNAL_SPECTRAL}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    result = {
        "certificate_type": "prime_matrix_strict_post_antisplit_source_rank_convergence_router",
        "status": "post_antisplit_source_rank_paths_converge_to_pointwise_kernel_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "new_primitive_exit_absorbed_to_source_rank": rows[1]["closed"],
        "terminal_descent_converges_to_source_rank": rows[2]["closed"],
        "source_rank_package_atomized": rows[3]["closed"],
        "all_internal_source_rank_routes_meet_at_pointwise_kernel_table": rows[8]["closed"],
        "alpha_row_anchor_phase_emission_formula_proved": False,
        "independent_noncircular_precauchy_arithmetic_identity_statement_proved": False,
        "same_unit_exact_uv_rank_multiplicity_certificate_proved": False,
        "pdec_scope_certificate_proved": False,
        "external_spectral_input_accepted": False,
        "row_column_unconditional_closed": False,
        "next_direct_attack_target": ALPHA_ROW,
        "parallel_direct_attack_targets": [INDEPENDENT_IDENTITY, SAME_UNIT_RANK],
        "pointwise_kernel_table": POINTWISE_KERNEL,
        "pointwise_basis_after_convergence": pointwise_basis,
        "unified_retained_remaining_basis": retained_basis,
        "convergence_edges": convergence_edges(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把刚完成的 antisplit trace/ExactUV 原子化前沿与仓库中已有的 new primitive、"
            "terminal descent、source-rank、source entropy、complete key 和 source table 证书重新合并。"
            "`NewPrimitiveAtomicSignedPayloadOrTraceFormulaArtifact` 已不是独立新主攻点；它和 terminal descent "
            "都回到同一 source-rank/no-collapse 包。该包的非后验共同变量表是 "
            "`PointwiseSameFormalUnitPrimitiveAlphaDeltaKernelTableWithNonzeroRankCertificate`，当前第一硬点为 "
            "`AlphaRowAnchorPhaseEmissionFormulaLedger`。行/列命题仍未无条件闭合。"
        ),
    }
    return result


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict post-antisplit source-rank 收敛前沿",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"new_primitive_exit_absorbed_to_source_rank={fmt_bool(result['new_primitive_exit_absorbed_to_source_rank'])}",
        f"terminal_descent_converges_to_source_rank={fmt_bool(result['terminal_descent_converges_to_source_rank'])}",
        f"source_rank_package_atomized={fmt_bool(result['source_rank_package_atomized'])}",
        f"all_internal_source_rank_routes_meet_at_pointwise_kernel_table={fmt_bool(result['all_internal_source_rank_routes_meet_at_pointwise_kernel_table'])}",
        f"alpha_row_anchor_phase_emission_formula_proved={fmt_bool(result['alpha_row_anchor_phase_emission_formula_proved'])}",
        f"independent_noncircular_precauchy_arithmetic_identity_statement_proved={fmt_bool(result['independent_noncircular_precauchy_arithmetic_identity_statement_proved'])}",
        f"same_unit_exact_uv_rank_multiplicity_certificate_proved={fmt_bool(result['same_unit_exact_uv_rank_multiplicity_certificate_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "parallel_direct_attack_targets="
        + ", ".join(result["parallel_direct_attack_targets"]),
        "```",
        "",
        "## 1. 收敛边",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for edge in result["convergence_edges"]:
        lines.append(
            f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |"
        )
    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | ---: | ---: | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | {closed} | {proved} | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 当前共同核表",
            "",
            "```text",
            result["pointwise_kernel_table"],
            "```",
            "",
            "核表后仍需：",
            "",
            "```text",
            result["pointwise_basis_after_convergence"],
            "```",
            "",
            "## 4. 统一保留剩余基",
            "",
            "```text",
            result["unified_retained_remaining_basis"],
            "```",
            "",
            "## 5. 结论边界",
            "",
            "- 本文件只完成 post-antisplit 后的旧出口吸收和共同变量表定位。",
            "- `NewPrimitive...` 与 terminal descent 不再作为独立闭合点；二者都回到 source-rank/no-collapse。",
            "- 仍未证明 alpha row 发射公式、pre-Cauchy 算术恒等式、同表 rank/multiplicity、PDEC/外部谱输入或最终晋级门。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    result = build_result()
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


if __name__ == "__main__":
    main()
