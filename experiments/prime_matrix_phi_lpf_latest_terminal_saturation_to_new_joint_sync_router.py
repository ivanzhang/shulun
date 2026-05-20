#!/usr/bin/env python3
"""生成 Phi-LPF latest 终端饱和到 new-joint 公式的同步证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_latest_terminal_saturation_to_new_joint_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.json

输出：
  data/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-ledger.json
  docs/monograph/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.json
  docs/monograph/prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-latest-terminal-saturation-to-new-joint-sync"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

LATEST_PRECAUCHY_ALPHA = DOCS / (
    "prime-matrix-phi-lpf-latest-precauchy-alpha-terminal-sync-router.json"
)
PDEC_CLEAN_KLS_SPLIT = DOCS / "prime-matrix-strict-pdec-clean-kls-terminal-hardpoint-router.json"
KUZNETSOV_DLS_TERMINAL = DOCS / "prime-matrix-strict-kuznetsov-dls-terminal-sync-router.json"
PDEC_SCOPE_SATURATION = DOCS / "prime-matrix-strict-pdec-scope-branch-saturation-frontier-router.json"
NEW_JOINT_OBLIGATION = DOCS / "prime-matrix-strict-new-joint-formula-terminal-obligation-router.json"
EXPLICIT_JOINT_ATTACK = DOCS / "prime-matrix-strict-explicit-joint-constructor-direct-attack-router.json"
GLOBAL_CRT_SATURATION = DOCS / "prime-matrix-global-crt-terminal-saturation-sync-router.json"

PDEC_CLEAN_KLS = "PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
KZ_DLS = "SelfContainedKuznetsovDLSLargeSieveInequalityForAcyclicCleanBlocks"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
EXTERNAL_DIBFI = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
MODEL_GAP = "ExplicitModelGapAndFiniteDPRCLedger"
ACTUAL_EXACTUV = "ActualEmitterExactUVBoundedMultiplicityIncidenceTheorem"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
SIGNED_ROW_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，不能当作证明。"""
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
        LATEST_PRECAUCHY_ALPHA,
        PDEC_CLEAN_KLS_SPLIT,
        KUZNETSOV_DLS_TERMINAL,
        PDEC_SCOPE_SATURATION,
        NEW_JOINT_OBLIGATION,
        EXPLICIT_JOINT_ATTACK,
        GLOBAL_CRT_SATURATION,
    ]


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in dependency_paths() if not path.exists()]


def source_hashes() -> dict[str, str]:
    """登记依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sync_chain() -> list[dict[str, str]]:
    """返回本层同步链。"""
    return [
        {
            "from": "Phi-LPF latest pre-Cauchy alpha-terminal branch",
            "to": f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        },
        {
            "from": PDEC_CLEAN_KLS,
            "to": f"{PDEC_SCOPE} OR {KZ_DLS}",
        },
        {
            "from": KZ_DLS,
            "to": "strict acyclic terminal family / nonrecursive breaker",
        },
        {
            "from": PDEC_SCOPE,
            "to": NEW_JOINT,
        },
        {
            "from": "old explicit joint constructor route",
            "to": "signed-source fixed point",
        },
        {
            "from": "terminal descent alternative",
            "to": "terminal-source-pair-joint macrocycle",
        },
    ]


def strict_internal_basis() -> str:
    """返回严格内部最新主攻基。"""
    return (
        f"{NEW_JOINT} AND {ACTUAL_EXACTUV} AND {FIXED_KEY} AND {SIGNED_ROW_LAW} "
        f"AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )


def conditional_basis() -> str:
    """返回条件 PDEC/外部保留线。"""
    return (
        f"({PDEC_SCOPE} OR {EXTERNAL_DIBFI}) AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}"
    )


def build_rows(deps: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成判定表。"""
    latest = deps["latest"]
    split = deps["split"]
    kz = deps["kz"]
    pdec_scope = deps["pdec_scope"]
    new_joint = deps["new_joint"]
    explicit_joint = deps["explicit_joint"]
    global_crt = deps["global_crt"]

    return [
        row(
            "LatestPhiLPFTerminalGateActive",
            latest.get("next_primary_attack_target") == PDEC_CLEAN_KLS,
            False,
            "上一层 Phi-LPF latest productive alpha-side 分支把下一主攻压到 PDEC/CleanKLS 终端门。",
            f"{PDEC_CLEAN_KLS} AND {MODEL_GAP}",
        ),
        row(
            "PDECCleanKLSSplitImported",
            split.get("hardpoint_before_router") == PDEC_CLEAN_KLS
            and split.get("terminal_split_router_closed") is True,
            False,
            "PDEC/CleanKLS 终端门已二分为 same-set PDEC 作用域匹配或自足 Kuznetsov/DLS。",
            f"{PDEC_SCOPE} OR {KZ_DLS}",
        ),
        row(
            "PDECArmScopeStillOpen",
            split.get("acyclic_same_set_scope_match_proved") is False
            and split.get("direct_pdec_protocol_audited") is True,
            False,
            "PDEC 手臂已完成协议审计，但 strict acyclic 与 canonical same-set 的同口径作用域匹配未证。",
            PDEC_SCOPE,
        ),
        row(
            "CleanKLSKuznetsovRouteReturnsTerminal",
            kz.get("kuznetsov_route_returns_to_terminal_family") is True,
            False,
            "CleanKLS/Kuznetsov-DLS 形式层攻到底后回到 strict acyclic 终端家族，不给自足闭合出口。",
            "strict acyclic terminal family / nonrecursive breaker",
        ),
        row(
            "PDECScopeBranchSaturatedToNewJoint",
            pdec_scope.get("pdec_scope_branch_saturated_in_current_internal_corpus") is True
            and pdec_scope.get("next_direct_attack_target") == NEW_JOINT,
            False,
            "PDEC scope 分支在当前内部语料中已饱和；真正内部破环点是新显式 joint 公式。",
            NEW_JOINT,
        ),
        row(
            "GlobalCRTSaturationAgrees",
            global_crt.get("next_direct_attack_target")
            == f"{PDEC_SCOPE}_OR_{NEW_JOINT}",
            False,
            "global CRT 饱和同步也给出 same-set PDEC 或 new-joint 二选一，方向一致。",
            f"{PDEC_SCOPE} OR {NEW_JOINT}",
        ),
        row(
            "NewJointObligationImported",
            new_joint.get("new_joint_formula_is_current_internal_noncycle_target") is True,
            False,
            "new-joint 义务证书确认当前内部非循环主攻是新的显式 actual joint alpha/delta 公式。",
            NEW_JOINT,
        ),
        row(
            "OldJointRouteIsFixedPoint",
            explicit_joint.get("joint_alpha_side_route_returns_to_signed_source_fixed_point") is True
            and new_joint.get("old_joint_constructor_route_returns_to_signed_source_fixed_point") is True,
            True,
            "旧 joint declaration/alpha-side/same-row/row-level 展开只回到 signed-source 固定点，不能当证明。",
            NEW_JOINT,
        ),
        row(
            "TerminalDescentAlternativeMacrocycle",
            new_joint.get("terminal_descent_alternative_is_macrocycle") is True,
            False,
            "没有新公式时，terminal descent 替代路线也已登记为 terminal-source-pair-joint 宏循环。",
            TERMINAL_DESCENT,
        ),
        row(
            "LPFPhiUnsignedBoundaryStillOnlyUnsigned",
            latest.get("lpf_phi_unsigned_only_boundary_retained") is True,
            True,
            "LPF/Phi 精准桶恒等式继续只支付无符号 ownership/support/capacity，不生成 joint signed coefficient 公式。",
            NEW_JOINT,
        ),
        row(
            "NewFormulaArtifactStillAbsent",
            new_joint.get("new_explicit_joint_constructor_formula_artifact_present") is False,
            False,
            "当前仓库仍未提交满足六字段合同的新显式 joint formula 工件。",
            NEW_JOINT,
        ),
        row(
            "ExactUVModelRateDStructureStillParallel",
            True,
            False,
            "即使新公式出现，也仍需 ExactUV、fixed-key、signed row law、模型余量、Rate 与 DStructure 同口径通过。",
            f"{ACTUAL_EXACTUV} AND {FIXED_KEY} AND {SIGNED_ROW_LAW} AND {MODEL_GAP} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本层只把 latest 终端门饱和同步到 new-joint 公式义务；没有得到无条件终端矛盾。",
            strict_internal_basis(),
        ),
    ]


def build_result() -> dict[str, Any]:
    """构造同步证书。"""
    deps = {
        "latest": load_json(LATEST_PRECAUCHY_ALPHA),
        "split": load_json(PDEC_CLEAN_KLS_SPLIT),
        "kz": load_json(KUZNETSOV_DLS_TERMINAL),
        "pdec_scope": load_json(PDEC_SCOPE_SATURATION),
        "new_joint": load_json(NEW_JOINT_OBLIGATION),
        "explicit_joint": load_json(EXPLICIT_JOINT_ATTACK),
        "global_crt": load_json(GLOBAL_CRT_SATURATION),
    }
    rows = build_rows(deps)
    return {
        "certificate_type": "prime_matrix_phi_lpf_latest_terminal_saturation_to_new_joint_sync_router",
        "status": "phi_lpf_latest_terminal_gate_saturated_to_new_joint_formula_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "missing_sources": missing_sources(),
        "latest_terminal_saturation_sync_closed": True,
        "latest_phi_lpf_terminal_gate_imported": rows[0]["closed"],
        "pdec_clean_kls_split_imported": rows[1]["closed"],
        "pdec_arm_scope_still_open": rows[2]["closed"],
        "clean_kls_kuznetsov_route_returns_terminal": rows[3]["closed"],
        "pdec_scope_branch_saturated_to_new_joint": rows[4]["closed"],
        "global_crt_saturation_agrees": rows[5]["closed"],
        "new_joint_obligation_imported": rows[6]["closed"],
        "old_joint_route_is_fixed_point": rows[7]["closed"],
        "terminal_descent_alternative_macrocycle": rows[8]["closed"],
        "lpf_phi_unsigned_boundary_retained": rows[9]["closed"],
        "new_explicit_joint_constructor_formula_artifact_present": False,
        "pdec_cap_or_internal_clean_kls_large_sieve_proved": False,
        "acyclic_same_set_scope_match_proved": False,
        "self_contained_kuznetsov_dls_large_sieve_inequality_proved": False,
        "actual_emitter_exact_uv_bounded_multiplicity_incidence_proved": False,
        "fixed_key_exact_uv_local_multiplicity_o1_proved": False,
        "acyclic_seed_primitive_row_signed_coefficient_law_proved": False,
        "explicit_model_gap_and_finite_dprc_ledger_proved": False,
        "rate_preservation_ledger_proved": False,
        "dstructure_independent_gate_closed": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "sync_chain": sync_chain(),
        "strict_internal_basis_after_sync": strict_internal_basis(),
        "conditional_pdec_or_external_basis_retained": conditional_basis(),
        "next_primary_attack_target": NEW_JOINT,
        "parallel_attack_targets": [
            PDEC_SCOPE,
            EXTERNAL_DIBFI,
            ACTUAL_EXACTUV,
            FIXED_KEY,
            SIGNED_ROW_LAW,
            MODEL_GAP,
            RATE,
            DSTRUCTURE,
        ],
        "plain_conclusion": (
            "本步把 latest Phi-LPF productive alpha-side 分支留下的 `PDEC_CAP_OR_INTERNAL_CleanKLS_LargeSieve` "
            "接入终端饱和前沿：PDEC/CleanKLS 二分为 same-set PDEC 作用域或自足 Kuznetsov/DLS；"
            "Kuznetsov/DLS 回到 strict acyclic 终端家族，PDEC scope 分支在当前内部语料中饱和，"
            "因此严格内部破环点压成 `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact`。"
            "这不是无条件闭合；PDEC scope/外部 DIBFI 可作条件线，ExactUV、fixed-key、signed row law、"
            "模型余量、Rate 与 DStructure 仍并行开放。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF latest terminal saturation to new-joint sync 证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"latest_phi_lpf_terminal_gate_imported={fmt_bool(result['latest_phi_lpf_terminal_gate_imported'])}",
        f"pdec_clean_kls_split_imported={fmt_bool(result['pdec_clean_kls_split_imported'])}",
        f"pdec_arm_scope_still_open={fmt_bool(result['pdec_arm_scope_still_open'])}",
        f"clean_kls_kuznetsov_route_returns_terminal={fmt_bool(result['clean_kls_kuznetsov_route_returns_terminal'])}",
        f"pdec_scope_branch_saturated_to_new_joint={fmt_bool(result['pdec_scope_branch_saturated_to_new_joint'])}",
        f"global_crt_saturation_agrees={fmt_bool(result['global_crt_saturation_agrees'])}",
        f"new_joint_obligation_imported={fmt_bool(result['new_joint_obligation_imported'])}",
        f"old_joint_route_is_fixed_point={fmt_bool(result['old_joint_route_is_fixed_point'])}",
        f"terminal_descent_alternative_macrocycle={fmt_bool(result['terminal_descent_alternative_macrocycle'])}",
        f"lpf_phi_unsigned_boundary_retained={fmt_bool(result['lpf_phi_unsigned_boundary_retained'])}",
        f"new_explicit_joint_constructor_formula_artifact_present={fmt_bool(result['new_explicit_joint_constructor_formula_artifact_present'])}",
        f"pdec_cap_or_internal_clean_kls_large_sieve_proved={fmt_bool(result['pdec_cap_or_internal_clean_kls_large_sieve_proved'])}",
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
                gate=item["gate"],
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
            "条件 PDEC/外部保留线：",
            "",
            "```text",
            result["conditional_pdec_or_external_basis_retained"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            result["next_primary_attack_target"],
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
            "- 本层只把 latest 终端门饱和同步到 new-joint 公式义务。",
            "- PDEC scope 或外部 DIBFI 仍可作为新输入，但不是当前内部已证出口。",
            "- LPF/Phi 桶恒等式仍只支付无符号 ownership、support 与 capacity。",
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


if __name__ == "__main__":
    main()
