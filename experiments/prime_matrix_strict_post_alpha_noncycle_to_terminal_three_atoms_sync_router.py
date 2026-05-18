#!/usr/bin/env python3
"""生成 post-alpha 非循环前沿到终端三原子的同步证书。

用法示例：
  python3 experiments/prime_matrix_strict_post_alpha_noncycle_to_terminal_three_atoms_sync_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json

输出：
  data/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-ledger.json
  docs/monograph/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json
  docs/monograph/prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-ledger.json"
OUT_JSON = DOCS / "prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.json"
OUT_MD = DOCS / "prime-matrix-strict-post-alpha-noncycle-to-terminal-three-atoms-sync-router.md"

POST_ALPHA = DOCS / "prime-matrix-strict-post-alpha-terminal-leaf-latest-noncycle-sync-router.json"
BRANCH_TRACE = DOCS / "prime-matrix-global-crt-branch-trace-frontier-router.json"
SIGNED_PAYLOAD = DOCS / "prime-matrix-global-crt-signed-payload-sync-router.json"
SOURCE_UNIFICATION = DOCS / "prime-matrix-strict-source-declaration-payload-exactuv-unification-router.json"
SIGNED_LANE = DOCS / "prime-matrix-strict-signed-lane-cycle-closure-router.json"
CURRENT_GLOBAL = DOCS / "prime-matrix-strict-current-global-frontier-after-trace-cycle-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"

NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
BRANCH_TRACE_ATOM = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
SIGNED_PAYLOAD_ATOM = "AtomicSignedPayloadTraceConstructorBeforeAssignmentOrReturn"
COMMON_PACKET = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
CANONICAL_LOCK = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
A1_ADMISSION = "A1CleanBranchCanonicalSourceAdmission"
MOVING_ATOM = "ActualNoncanonicalCleanCoreMovingAtomExclusion"
INDEPENDENT_MOVING_ATOM = "IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore"
DSTRUCTURE_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
FULLS_KLS_EXT = "AcceptFullSKLSExtExternalContract"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时保留空对象并在 missing_sources 中呈现。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
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


def source_paths() -> list[Path]:
    """列出本同步使用的证据文件。"""
    return [
        Path(__file__).resolve(),
        POST_ALPHA,
        BRANCH_TRACE,
        SIGNED_PAYLOAD,
        SOURCE_UNIFICATION,
        SIGNED_LANE,
        CURRENT_GLOBAL,
        DSTRUCTURE,
    ]


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in source_paths() if path.exists()}


def missing_sources() -> list[str]:
    """列出缺失依赖。"""
    return [str(path.relative_to(ROOT)) for path in source_paths() if not path.exists()]


def sync_chain() -> list[dict[str, str]]:
    """给出本轮从 c75 非循环基到三原子的吸收链。"""
    return [
        {
            "from": NEW_JOINT,
            "to": BRANCH_TRACE_ATOM,
            "meaning": "global CRT branch-trace 前沿已把新 joint 公式压到 exact atomic branch trace。",
        },
        {
            "from": BRANCH_TRACE_ATOM,
            "to": SIGNED_PAYLOAD_ATOM,
            "meaning": "exact branch trace 的 visible coordinate 不能生成 signed payload，故继续压到 pre-assignment signed payload。",
        },
        {
            "from": SIGNED_PAYLOAD_ATOM,
            "to": f"{COMMON_PACKET} dependency cycle",
            "meaning": "signed payload 经 origin identity 与 ExactUV 合流到 common source declaration packet。",
        },
        {
            "from": COMMON_PACKET,
            "to": "signed-lane closed cycle",
            "meaning": "common packet、built-in pairing、branch trace、signed payload、origin identity 已形成闭环，不能自证。",
        },
        {
            "from": f"{PDEC_SCOPE} / trace / signed-source / ExactUV-pairmass pseudo exits",
            "to": f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
            "meaning": "current-global-after-trace-cycle 证书删除已识别自回流伪出口后，strict 当前全局前沿只剩三原子。",
        },
        {
            "from": MOVING_ATOM,
            "to": INDEPENDENT_MOVING_ATOM,
            "meaning": "moving atom 原子若要成为证明，必须给出不经 ExactUV/pair-mass/terminal 回流的独立非终端排斥机制。",
        },
    ]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """汇总依赖证书读数。"""
    post = data["post"]
    branch = data["branch"]
    payload = data["payload"]
    source = data["source"]
    signed = data["signed"]
    current = data["current"]
    dstructure = data["dstructure"]
    three_atoms = current.get("three_atoms", [])

    return [
        row(
            "PostAlphaNoncycleBasisImported",
            post.get("next_direct_attack_target") == NEW_JOINT
            and post.get("row_column_unconditional_closed") is False,
            False,
            "c75 的 post-alpha 非循环同步已把第一主攻钉在新 actual joint 公式。",
            NEW_JOINT,
        ),
        row(
            "NewJointAbsorbedToExactBranchTrace",
            branch.get("new_joint_reduced_to_antisplit_formula") is True
            and branch.get("builtin_pairing_reduced_to_exact_branch_trace") is True,
            False,
            "新 joint 公式在既有 branch-trace 前沿中已被压到 exact atomic branch trace。",
            BRANCH_TRACE_ATOM,
        ),
        row(
            "ExactBranchTraceAbsorbedToSignedPayload",
            payload.get("exact_atomic_trace_reduced_to_signed_payload") is True
            and payload.get("atomic_signed_payload_constructor_proved") is False,
            False,
            "global CRT signed payload 同步说明 exact trace 只给可见坐标，不给 signed payload。",
            SIGNED_PAYLOAD_ATOM,
        ),
        row(
            "SignedPayloadCommonPacketCycleImported",
            source.get("next_direct_attack_target") == COMMON_PACKET
            and signed.get("signed_lane_cycle_closed") is True,
            True,
            "signed payload、origin identity、common packet 与 built-in pairing 已闭成 signed-lane 环。",
            "remove signed-lane self-proof",
        ),
        row(
            "PDECScopeRetainedButInternalSelfProofRemoved",
            payload.get("external_or_new_pdec_scope_still_open") is True
            and signed.get("aggregate", {}).get("acyclic_same_set_scope_match_proved") is False,
            False,
            "PDEC same-set 仍可作为新证书或外部线，但当前内部语料中的 PDEC 自回流已被移出证明路径。",
            PDEC_SCOPE,
        ),
        row(
            "TerminalThreeAtomsPinned",
            current.get("strict_current_frontier_three_atoms") is True
            and {CANONICAL_LOCK, A1_ADMISSION, MOVING_ATOM}.issubset(set(three_atoms)),
            False,
            "删除 trace/source/terminal/pair-mass 自回流后，strict 当前全局前沿压成三原子。",
            f"{CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}",
        ),
        row(
            "MovingAtomChosenAsNarrowestDirectAttack",
            current.get("recommended_nonrecursive_form") == INDEPENDENT_MOVING_ATOM,
            False,
            "三原子中最贴近反例链 actual-load 与相位冲突的是 noncanonical clean-core moving atom 排斥。",
            INDEPENDENT_MOVING_ATOM,
        ),
        row(
            "DStructurePromotionStillIndependent",
            dstructure.get("promotion_package_boundary_closed") is True
            and dstructure.get("promotion_package_independently_accepted") is False,
            False,
            "DStructure/Rankin 守门边界已有作者侧包，但独立接受仍不能由本路由替代。",
            DSTRUCTURE_GATE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只继续同步并删除更深自回流路线，没有证明三原子或最终晋级门。",
            "row/column theorem still open",
        ),
    ]


def build_result() -> dict[str, Any]:
    """生成同步结果。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    data = {
        "post": load_json(POST_ALPHA),
        "branch": load_json(BRANCH_TRACE),
        "payload": load_json(SIGNED_PAYLOAD),
        "source": load_json(SOURCE_UNIFICATION),
        "signed": load_json(SIGNED_LANE),
        "current": load_json(CURRENT_GLOBAL),
        "dstructure": load_json(DSTRUCTURE),
    }
    rows = build_rows(data)
    strict_current_basis = (
        f"({CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM}) "
        f"AND {DSTRUCTURE_GATE}"
    )
    conditional_external_basis = (
        f"({CANONICAL_LOCK} OR {A1_ADMISSION} OR {MOVING_ATOM} "
        f"OR {PDEC_SCOPE} OR {FULLS_KLS_EXT}) AND {DSTRUCTURE_GATE}"
    )
    return {
        "certificate_type": "prime_matrix_strict_post_alpha_noncycle_to_terminal_three_atoms_sync_router",
        "status": "post_alpha_noncycle_frontier_synced_to_terminal_three_atoms_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "post_alpha_new_joint_absorbed": rows[1]["closed"],
        "branch_trace_absorbed_to_signed_payload": rows[2]["closed"],
        "signed_lane_cycle_self_proof_eliminated": rows[3]["closed"],
        "terminal_three_atoms_pinned": rows[5]["closed"],
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "strict_current_basis_after_sync": strict_current_basis,
        "conditional_external_basis_after_sync": conditional_external_basis,
        "next_direct_attack_target": INDEPENDENT_MOVING_ATOM,
        "terminal_atoms": [CANONICAL_LOCK, A1_ADMISSION, MOVING_ATOM],
        "retained_parallel_inputs": [PDEC_SCOPE, FULLS_KLS_EXT, DSTRUCTURE_GATE],
        "sync_chain": sync_chain(),
        "rows": rows,
        "source_hashes": source_hashes(),
        "missing_sources": missing_sources(),
        "plain_conclusion": (
            "本步把 c75 后的 post-alpha 非循环前沿继续同步到更深证书："
            "NewExplicit actual joint 公式已被 branch-trace 证书吸收到 exact atomic branch trace，"
            "再被 signed-payload 证书吸收到 pre-assignment signed payload；signed lane 又回到 common "
            "source declaration packet 并闭成依赖环。因此 `NewExplicit...` 不是当前最深活动硬点。"
            "在删除 trace/source/terminal/pair-mass 等自回流伪出口后，strict 当前全局前沿同步为 "
            "canonical-lock、A1 canonical source admission、actual noncanonical clean-core moving atom "
            "三原子。三者均未证明，行/列命题仍未无条件闭合；下一轮最窄直接主攻是独立非终端 moving atom 排斥。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines = [
        "# Prime Matrix strict post-alpha noncycle 到终端三原子同步",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"post_alpha_new_joint_absorbed={fmt_bool(result['post_alpha_new_joint_absorbed'])}",
        f"branch_trace_absorbed_to_signed_payload={fmt_bool(result['branch_trace_absorbed_to_signed_payload'])}",
        f"signed_lane_cycle_self_proof_eliminated={fmt_bool(result['signed_lane_cycle_self_proof_eliminated'])}",
        f"terminal_three_atoms_pinned={fmt_bool(result['terminal_three_atoms_pinned'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        f"next_direct_attack_target={result['next_direct_attack_target']}",
        "```",
        "",
        "## 1. 同步链",
        "",
        "| from | to | meaning |",
        "| --- | --- | --- |",
    ]
    for edge in result["sync_chain"]:
        lines.append(f"| `{cell(edge['from'])}` | `{cell(edge['to'])}` | {cell(edge['meaning'])} |")
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
            "## 3. 当前严格基",
            "",
            "```text",
            result["strict_current_basis_after_sync"],
            "```",
            "",
            "条件外部线：",
            "",
            "```text",
            result["conditional_external_basis_after_sync"],
            "```",
            "",
            "## 4. 下一主攻",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "三原子：",
            "",
            "```text",
            "\n".join(result["terminal_atoms"]),
            "```",
            "",
            "## 5. 结论边界",
            "",
            "- 本文件只做前沿同步和自回流删除，不证明行/列命题。",
            "- `NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact` 已不是当前最深活动硬点。",
            "- 当前最窄直接主攻是 `IndependentNonterminalMovingAtomExclusionForActualNoncanonicalCleanCore`。",
            "- 三原子和 DStructure/Rankin 独立晋级门均未闭合，不能声明全局无条件证明完成。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    if result["missing_sources"]:
        lines.extend(["", "缺失依赖："])
        for path in result["missing_sources"]:
            lines.append(f"- `{path}`")
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
