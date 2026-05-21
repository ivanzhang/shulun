#!/usr/bin/env python3
"""生成 Phi-LPF latest new-joint 到反分裂原子的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_new_joint_antisplit_atom_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-new-joint-antisplit-atom-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_TERMINAL_SYNC = DOCS / (
    "prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.json"
)
NEW_JOINT_OBLIGATION = DOCS / "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"
ANTISPLIT_ATOM = DOCS / "prime-matrix-strict-new-joint-formula-antisplit-atom-router.json"
EXPLICIT_JOINT_ATTACK = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
ANTISPLIT_DOWNSTREAM = DOCS / (
    "prime-matrix-strict-cyclecut-unified-antisplit-downstream-sync-router.json"
)
ANTISPLIT_FIREWALL = DOCS / "prime-matrix-strict-antisplit-joint-declaration-firewall-router.json"
ATOMIC_ROWS = DOCS / "prime-matrix-strict-atomic-joint-rows-builtin-pairing-router.json"
EXACTUV_ENTROPY = DOCS / "prime-matrix-strict-actual-emitter-incidence-entropy-router.json"

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
NON_SPLIT = "NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection"
ATOMIC_ROWS_TARGET = "AtomicPreCauchyJointRowsFormulaWithBuiltInWordCoefficientPairing"
BUILTIN_PAIRING = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
SOURCE_ENTROPY = "ActualEmitterSourceDomainEntropyLedger"
FIXED_FIBER = "ExactUVMapFixedPairPolylogFiberBoundLedger"
ACTUAL_EXACTUV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失依赖不能被解释成证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值渲染为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def row(gate: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def dependency_paths() -> list[Path]:
    """返回本层依赖证书。"""
    return [
        LATEST_TERMINAL_SYNC,
        NEW_JOINT_OBLIGATION,
        ANTISPLIT_ATOM,
        EXPLICIT_JOINT_ATTACK,
        ANTISPLIT_DOWNSTREAM,
        ANTISPLIT_FIREWALL,
        ATOMIC_ROWS,
        EXACTUV_ENTROPY,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def strict_basis() -> str:
    """返回严格内部剩余基。"""
    return (
        f"{NON_SPLIT} AND {ACTUAL_EXACTUV} AND {FIXED_KEY} AND {SIGNED_ROW_LAW} "
        f"AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )


def downstream_basis() -> str:
    """返回已知反分裂下游可继续追击的基。"""
    return f"{BUILTIN_PAIRING} AND {SOURCE_ENTROPY} AND {FIXED_FIBER}"


def sync_chain() -> list[dict[str, str]]:
    """返回本层同步链。"""
    return [
        {
            "from": "Phi-LPF latest terminal saturation frontier",
            "to": NEW_JOINT,
        },
        {
            "from": NEW_JOINT,
            "to": "old split alpha/delta route OR antisplit joint row formula",
        },
        {
            "from": "old split alpha/delta route",
            "to": "row-level/signed-source fixed point",
        },
        {
            "from": "antisplit joint row formula",
            "to": NON_SPLIT,
        },
        {
            "from": NON_SPLIT,
            "to": f"{ATOMIC_ROWS_TARGET} -> {BUILTIN_PAIRING}",
        },
        {
            "from": ACTUAL_EXACTUV,
            "to": f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        },
    ]


def downstream_edges_cover_antisplit(downstream: dict[str, Any]) -> bool:
    """检查已有下游证书是否覆盖反分裂原子的后续边。"""
    edges = downstream.get("sync_edges", [])
    has_atomic = any(
        edge.get("from") == NON_SPLIT and edge.get("to") == ATOMIC_ROWS_TARGET for edge in edges
    )
    has_pairing = any(
        edge.get("from") == ATOMIC_ROWS_TARGET and edge.get("to") == BUILTIN_PAIRING for edge in edges
    )
    has_exactuv = any(
        edge.get("from") == ACTUAL_EXACTUV
        and edge.get("to") == f"{SOURCE_ENTROPY} AND {FIXED_FIBER}"
        for edge in edges
    )
    return has_atomic and has_pairing and has_exactuv


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    latest = deps["latest"]
    obligation = deps["obligation"]
    antisplit = deps["antisplit"]
    explicit = deps["explicit"]
    downstream = deps["downstream"]
    firewall = deps["firewall"]
    atomic = deps["atomic"]
    exactuv = deps["exactuv"]

    return [
        row(
            "LatestNewJointTargetImported",
            latest.get("next_primary_attack_target") == NEW_JOINT,
            False,
            "上一层 Phi-LPF latest 终端饱和已把严格内部主攻压成 new-joint 公式工件。",
            NEW_JOINT,
        ),
        row(
            "TerminalObligationImported",
            obligation.get("new_joint_formula_is_current_internal_noncycle_target") is True
            and obligation.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "new-joint 义务证书确认当前没有已提交的显式 joint formula 工件。",
            NEW_JOINT,
        ),
        row(
            "OldSplitFormulaRouteSynced",
            antisplit.get("old_split_formula_route_synced") is True,
            False,
            "沿旧 actual constructor、explicit alpha/delta、alpha-side、anchor/phase、signed lift 展开已全部同步。",
            "old split route",
        ),
        row(
            "OldSplitFormulaRouteIsNonproofCycle",
            antisplit.get("old_split_formula_route_is_nonproof_cycle") is True
            and explicit.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True,
            True,
            "旧分裂路线回到 row-level/signed-source 固定点，不能登记为非循环证明。",
            NON_SPLIT,
        ),
        row(
            "AntisplitJointFormulaTargetImported",
            antisplit.get("next_direct_attack_target") == NON_SPLIT,
            False,
            "真正的新公式必须在 alpha-side 投影前同一行同时给出 primitive word 与 signed coefficient。",
            NON_SPLIT,
        ),
        row(
            "AntiSplitFieldsImported",
            len(antisplit.get("antisplit_fields", [])) >= 6,
            False,
            "反分裂字段合同已列出 source tuple、word/coefficient、alpha/delta payload、exact UV、prepushforward identity 与 no-split 证书。",
            NON_SPLIT,
        ),
        row(
            "LPFPhiUnsignedBoundaryStillUnsigned",
            latest.get("lpf_phi_unsigned_boundary_retained") is True,
            True,
            "LPF/Phi 精准桶恒等式仍只支付无符号 ownership/support/capacity，不能生成 signed joint coefficient。",
            NON_SPLIT,
        ),
        row(
            "NonSplitFormulaCurrentCorpusProved",
            False,
            False,
            "当前仓库没有不经 alpha-side/row-level/signed-source 分裂的同排 primitive word/coefficient 公式。",
            NON_SPLIT,
        ),
        row(
            "KnownAntiSplitDownstreamAvailable",
            downstream_edges_cover_antisplit(downstream)
            and firewall.get("next_direct_attack_target") == ATOMIC_ROWS_TARGET
            and atomic.get("next_direct_attack_target") == BUILTIN_PAIRING,
            False,
            "若继续下钻，已有 strict 下游会把反分裂原子压到 atomic rows、built-in pairing 与 ExactUV entropy/fiber。",
            downstream_basis(),
        ),
        row(
            "ExactUVEntropyFiberStillParallel",
            exactuv.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "ExactUV incidence 仍是并行门；其下游 source-domain entropy 与 fixed-pair fiber bound 未由反分裂公式自动给出。",
            f"{SOURCE_ENTROPY} AND {FIXED_FIBER}",
        ),
        row(
            "ModelRateDStructureStillParallel",
            True,
            False,
            "模型余量、RatePreservation 与 DStructure/Rankin 独立验收仍保持开放。",
            f"{MODEL_GAP} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把 latest new-joint 主线同步到反分裂原子；没有得到无条件全局矛盾。",
            strict_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    deps = {
        "latest": load_json(LATEST_TERMINAL_SYNC),
        "obligation": load_json(NEW_JOINT_OBLIGATION),
        "antisplit": load_json(ANTISPLIT_ATOM),
        "explicit": load_json(EXPLICIT_JOINT_ATTACK),
        "downstream": load_json(ANTISPLIT_DOWNSTREAM),
        "firewall": load_json(ANTISPLIT_FIREWALL),
        "atomic": load_json(ATOMIC_ROWS),
        "exactuv": load_json(EXACTUV_ENTROPY),
    }
    rows = build_rows(deps)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_new_joint_antisplit_atom_sync_router",
        "status": "phi_lpf_latest_new_joint_synced_to_antisplit_atom_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "frontier_sync_only": True,
        "missing_sources": missing_sources(),
        "latest_new_joint_target_imported": rows[0]["closed"],
        "terminal_obligation_imported": rows[1]["closed"],
        "old_split_formula_route_synced": rows[2]["closed"],
        "old_split_formula_route_is_nonproof_cycle": rows[3]["closed"],
        "antisplit_joint_formula_target_imported": rows[4]["closed"],
        "antisplit_fields_imported": rows[5]["closed"],
        "lpf_phi_unsigned_boundary_retained": rows[6]["closed"],
        "non_split_actual_joint_formula_proved": False,
        "antisplit_joint_formula_proved": False,
        "known_antisplit_downstream_available": rows[8]["closed"],
        "built_in_signed_pairing_proved": False,
        "actual_emitter_source_domain_entropy_proved": False,
        "exact_uv_map_fixed_pair_polylog_fiber_bound_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "sync_chain": sync_chain(),
        "strict_internal_basis_after_sync": strict_basis(),
        "known_downstream_basis_after_antisplit": downstream_basis(),
        "next_primary_attack_target": NON_SPLIT,
        "next_downstream_attack_target_after_antisplit": BUILTIN_PAIRING,
        "parallel_attack_targets": [
            ACTUAL_EXACTUV,
            FIXED_KEY,
            SIGNED_ROW_LAW,
            SOURCE_ENTROPY,
            FIXED_FIBER,
            MODEL_GAP,
            RATE,
            DSTRUCTURE,
        ],
        "plain_conclusion": (
            "本步把 latest Phi-LPF terminal saturation 留下的 "
            "`NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 接到 strict new-joint "
            "反分裂原子证书。旧 alpha/delta、alpha-side、row-level、signed-source 展开已经同步为固定点，"
            "不能作为非循环证明；因此真实最窄原子压成 "
            "`NonSplitActualJointPrimitiveWordCoefficientFormulaBeforeAlphaSideProjection`。"
            "该原子必须在 alpha-side 投影前同一行同时给出 primitive basis word、signed coefficient、"
            "alpha/delta pairing、exact `(u,v)`、branch key、sign/local factor、prepushforward identity "
            "和 no-split 证书。LPF/Phi 桶恒等式仍只提供无符号 support/capacity，当前语料未给出该反分裂公式，"
            "行/列命题仍未无条件闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest new-joint to antisplit atom sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_new_joint_target_imported={fmt_bool(result['latest_new_joint_target_imported'])}",
        f"terminal_obligation_imported={fmt_bool(result['terminal_obligation_imported'])}",
        f"old_split_formula_route_synced={fmt_bool(result['old_split_formula_route_synced'])}",
        (
            "old_split_formula_route_is_nonproof_cycle="
            f"{fmt_bool(result['old_split_formula_route_is_nonproof_cycle'])}"
        ),
        f"antisplit_joint_formula_target_imported={fmt_bool(result['antisplit_joint_formula_target_imported'])}",
        f"antisplit_fields_imported={fmt_bool(result['antisplit_fields_imported'])}",
        f"lpf_phi_unsigned_boundary_retained={fmt_bool(result['lpf_phi_unsigned_boundary_retained'])}",
        f"non_split_actual_joint_formula_proved={fmt_bool(result['non_split_actual_joint_formula_proved'])}",
        f"known_antisplit_downstream_available={fmt_bool(result['known_antisplit_downstream_available'])}",
        f"built_in_signed_pairing_proved={fmt_bool(result['built_in_signed_pairing_proved'])}",
        (
            "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved="
            f"{fmt_bool(result['actual_emitter_exact_uv_bounded_multiplicity_incidence_proved'])}"
        ),
        f"explicit_model_gap_and_finite_dprc_ledger_proved={fmt_bool(result['explicit_model_gap_and_finite_dprc_ledger_proved'])}",
        f"rate_preservation_ledger_proved={fmt_bool(result['rate_preservation_ledger_proved'])}",
        f"dstructure_independent_gate_closed={fmt_bool(result['dstructure_independent_gate_closed'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={result['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to |",
        "| --- | --- |",
    ]
    for item in result["sync_chain"]:
        lines.append(f"| `{cell(item['from'])}` | `{cell(item['to'])}` |")

    lines.extend(
        [
            "",
            "## 2. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 3. 最新开放基",
            "",
            "严格内部主攻基：",
            "",
            "```text",
            result["strict_internal_basis_after_sync"],
            "```",
            "",
            "反分裂后已知可继续下钻基：",
            "",
            "```text",
            result["known_downstream_basis_after_antisplit"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
            "```",
            "",
            "反分裂下游首攻：",
            "",
            "```text",
            result["next_downstream_attack_target_after_antisplit"],
            "```",
            "",
            "并行仍需：",
            "",
            "```text",
            "\n".join(result["parallel_attack_targets"]),
            "```",
            "",
            "## 4. 边界",
            "",
            "- 本层只把 latest new-joint 主线同步到反分裂原子。",
            "- LPF/Phi 精准桶恒等式仍只支付无符号 ownership、support 与 capacity。",
            "- 已有下游说明反分裂原子若继续展开，会进入 atomic rows / built-in pairing 与 ExactUV entropy/fiber；这仍不是已证闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 ledger、JSON 和 Markdown 证书。"""
    result = build_result()
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_LEDGER}")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"next_primary_attack_target={result['next_primary_attack_target']}")
    print(f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}")


if __name__ == "__main__":
    main()
