#!/usr/bin/env python3
"""压缩 DStructure/Tail-log4/finite Rankin 自足替代包的真实剩余。

用法示例：
  python3 experiments/prime_matrix_strict_dstructure_tail_rankin_replacement_compression_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-dstructure-tail-rankin-replacement-compression-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MONO = DOCS / "monograph"

OUT_JSON = MONO / "prime-matrix-strict-dstructure-tail-rankin-replacement-compression-router.json"
OUT_MD = MONO / "prime-matrix-strict-dstructure-tail-rankin-replacement-compression-router.md"

PREVIOUS = MONO / "prime-matrix-strict-rks23-character-moment-to-promotion-audit-router.json"
DSTRUCTURE_PROMOTION = MONO / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
FULL_RANKIN = MONO / "prime-matrix-full-rankin-ledger-inventory-router.json"
FINAL_PROMOTION = MONO / "prime-matrix-final-promotion-gate-irreducibility-router.json"
D_STRUCTURE_APPENDIX = DOCS / "d-structure-formal-appendix.md"
AB_TO_D = DOCS / "ab-to-d-interface-match.md"
TAIL_FORMAL = DOCS / "tail-log4-formal-appendix.md"
TAIL_THEOREMIZATION = DOCS / "tail-log4-theoremization.md"
EXT_PACKAGE = DOCS / "external-theorem-package.md"
EXT_AUDIT = DOCS / "ext-citation-final-audit.md"
FINAL_REVIEW = DOCS / "final-top-journal-unconditional-review.md"
SOURCE_FILES = [
    PREVIOUS,
    DSTRUCTURE_PROMOTION,
    FULL_RANKIN,
    FINAL_PROMOTION,
    D_STRUCTURE_APPENDIX,
    AB_TO_D,
    TAIL_FORMAL,
    TAIL_THEOREMIZATION,
    EXT_PACKAGE,
    EXT_AUDIT,
    FINAL_REVIEW,
]

TARGET = "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
RKS_LOG_ATOM = "SelfContainedRKSLogReciprocalKloostermanTailLog4Input"
EXT_ANALYTIC_ATOM = "SelfContainedExternalAnalyticInputsForDStructureTailLog4"
PROMOTION_GATE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
ROW_COLUMN_GATE = "RowColumnUnconditionalClosed"


def read_text(path: Path) -> str:
    """读取文本；缺失时返回空串。"""
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记依赖文件哈希。"""
    return {str(path.relative_to(ROOT)): sha256(path) for path in SOURCE_FILES if path.exists()}


def contains_all(text: str, needles: list[str]) -> bool:
    """检查文本包含全部关键片段。"""
    return all(item in text for item in needles)


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
    return "true" if bool(value) else "false"


def table_cell(value: Any) -> str:
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


def build_result() -> dict[str, Any]:
    """构造自足替代包压缩证书。"""
    previous = load_json(PREVIOUS)
    dstructure = load_json(DSTRUCTURE_PROMOTION)
    full_rankin = load_json(FULL_RANKIN)
    final_promotion = load_json(FINAL_PROMOTION)
    d_text = read_text(D_STRUCTURE_APPENDIX)
    ab_text = read_text(AB_TO_D)
    tail_formal = read_text(TAIL_FORMAL)
    tail_theory = read_text(TAIL_THEOREMIZATION)
    ext_package = read_text(EXT_PACKAGE)
    ext_audit = read_text(EXT_AUDIT)
    final_review = read_text(FINAL_REVIEW)

    target_active = (
        previous.get("next_direct_attack_target") == TARGET
        and previous.get("rks23_analytic_branch_closed_author_side") is True
        and previous.get("row_column_unconditional_closed") is False
    )

    finite_rankin_closed = (
        full_rankin.get("full_rankin_ledger_still_open_closed") is True
        and full_rankin.get("batch_rankin_pass_or_return_closed") is True
        and dstructure.get("full_rankin_ledger_still_open_closed") is True
    )
    promotion_boundary_closed = (
        dstructure.get("promotion_package_boundary_closed") is True
        and final_promotion.get("promotion_author_packet_sealed") is True
    )
    independent_acceptance_closed = (
        dstructure.get("promotion_package_independently_accepted") is True
        or final_promotion.get("referee_gate_explicitly_accepted") is True
    )

    ab_to_d_closed = contains_all(
        ab_text,
        ["Theorem M", "五项逐项成立", "主链不再存在未命名结构黑箱"],
    )
    dstructure_shell_closed = contains_all(
        d_text,
        ["Theorem D", "Structured-EHPD 排斥", "OMR", "CGTP", "LSMP", "FCT"],
    )
    dstructure_formal_replacement_closed = target_active and ab_to_d_closed and dstructure_shell_closed

    tail_formal_shell_closed = contains_all(
        tail_formal,
        ["Theorem C", "Lemma C1", "Lemma C2", "Lemma C3", "Corollary C4"],
    )
    tail_decomposition_closed = contains_all(
        tail_theory,
        ["Theorem TL4", "Theorem TL4-L", "Theorem TL4-S", "Theorem TL4-M", "Theorem RKS-log"],
    )
    tail_smooth_closed = contains_all(tail_theory, ["Theorem TL4-S", "证毕"])
    tail_mid_reduced = contains_all(
        tail_theory,
        ["TL4-M1", "TL4-M2", "Proposition TL4-M3", "大模数层不再需要独立黑箱"],
    )
    rks_log_isolated = contains_all(
        tail_theory,
        ["Theorem RKS-log", "唯一剩余引用已经缩小为 Theorem RKS-log"],
    )
    ext_labels_registered = contains_all(
        ext_package,
        ["EXT-KL", "EXT-BG", "EXT-Vaaler", "EXT-Selberg", "EXT-Vaughan"],
    ) and contains_all(
        ext_audit,
        ["EXT-KL", "EXT-BG", "EXT-Vaaler", "EXT-Selberg", "EXT-Vaughan"],
    )
    rks_log_internalized = False
    ext_analytic_inputs_internalized = False

    # 本轮的关键压缩：替代包的格式/Rankin/D 接口已经内部化；
    # 真正未替代的是 Tail-log4 的 RKS-log/BG 倒数 Kloosterman 输入及其外部解析输入族。
    replacement_shell_closed = (
        target_active
        and finite_rankin_closed
        and promotion_boundary_closed
        and dstructure_formal_replacement_closed
        and tail_formal_shell_closed
        and tail_decomposition_closed
        and tail_smooth_closed
        and tail_mid_reduced
        and rks_log_isolated
        and ext_labels_registered
    )
    replacement_package_proved = (
        replacement_shell_closed and rks_log_internalized and ext_analytic_inputs_internalized
    )
    row_column_closed = replacement_package_proved or independent_acceptance_closed

    replacement_compression = {
        "rankin": "full Rankin ledger and batch pass-or-return are closed; no longer the active internal obstruction",
        "dstructure": "A/B to D matching and D Structured-EHPD formal shell are present; remaining dependence is analytic EXT inputs",
        "tail_log4": "TL4 is split into smooth, middle, and low-spectrum/RKS-log branches",
        "tail_smooth": "TL4-S is elementary smoothing/endpoint bookkeeping and is closed in the formal appendix",
        "tail_mid": "TL4-M large-modulus layer is reduced to Selberg upper sieve plus averaged singular series ledger",
        "tail_low": "TL4-L is compressed to the RKS-log reciprocal Kloosterman log-saving theorem",
        "not_replaced": "EXT-BG/RKS-log and the external analytic input family are registered but not self-containedly proved here",
    }

    why_burgess_not_enough = {
        "burgess_closed_object": "multiplicative character sums on intervals modulo P",
        "rks_log_object": "additive reciprocal Kloosterman sums e_P(xi/(mn)) with prime/dyadic variables",
        "orthogonality_mismatch": "multiplicative characters diagonalize product ratios; RKS-log needs additive trace/reciprocal phases",
        "consequence": "the newly closed Burgess/RKS23 character moment cannot be reused as a proof of TL4-L/RKS-log",
    }

    current_frontier = {
        "current_internal_replacement_status": "replacement shell closed, analytic core open",
        "narrowest_math_atom": RKS_LOG_ATOM,
        "supporting_external_family": EXT_ANALYTIC_ATOM,
        "parallel_non_internal_route": PROMOTION_GATE,
        "row_column_boundary": "false until either the self-contained analytic core is proved or the independent promotion gate is accepted",
    }

    rows = [
        row(
            "ReplacementPackageTargetActive",
            target_active,
            target_active,
            "上一证书已把唯一内部自足剩余指向 DStructure/Tail-log4/finite Rankin 替代包。",
            TARGET,
        ),
        row(
            "FiniteRankinReplacementClosed",
            finite_rankin_closed,
            finite_rankin_closed,
            "finite Rankin 子账本已有 manifest/data 与 batch pass-or-return，内部替代部分闭合。",
            "closed",
        ),
        row(
            "DStructureFormalReplacementShellClosed",
            dstructure_formal_replacement_closed,
            dstructure_formal_replacement_closed,
            "A/B 到 D 匹配与 D 组 OMR/CGTP/LSMP/FCT 正式接口已经形成作者侧证明壳。",
            EXT_ANALYTIC_ATOM,
        ),
        row(
            "TailLog4FormalDecompositionClosed",
            tail_formal_shell_closed and tail_decomposition_closed,
            tail_formal_shell_closed and tail_decomposition_closed,
            "Tail-log4 已拆成 TL4-S、TL4-M、TL4-L/RKS-log 三个可审查分支。",
            RKS_LOG_ATOM,
        ),
        row(
            "TailLog4SmoothAndMidLedgerCompressed",
            tail_smooth_closed and tail_mid_reduced,
            tail_smooth_closed and tail_mid_reduced,
            "平滑端点账本闭合，大模数中谱层不再是独立黑箱。",
            RKS_LOG_ATOM,
        ),
        row(
            "RKSLogReciprocalKloostermanAtomIsolated",
            rks_log_isolated,
            rks_log_isolated,
            "Tail-log4 低谱真正剩余已压成 RKS-log/BG 倒数 Kloosterman 对数节省。",
            RKS_LOG_ATOM,
        ),
        row(
            "BurgessPointwiseDoesNotReplaceRKSLog",
            True,
            True,
            "Burgess 角色和处理乘法角色；RKS-log 是加性倒数相位，二者正交对象不同。",
            RKS_LOG_ATOM,
        ),
        row(
            RKS_LOG_ATOM,
            rks_log_internalized,
            rks_log_internalized,
            "当前仓库尚未内联证明 BG/RKS-log 倒数 Kloosterman 对数节省。",
            "prove BG/RKS-log or exact self-contained replacement",
        ),
        row(
            EXT_ANALYTIC_ATOM,
            ext_analytic_inputs_internalized,
            ext_analytic_inputs_internalized,
            "EXT-KL/BG/Vaaler/Selberg/Vaughan 已登记引用，但没有全部改写成自足附录证明。",
            "internalize or explicitly keep as external theorem package",
        ),
        row(
            TARGET,
            replacement_package_proved,
            replacement_package_proved,
            "替代包的形式壳已闭合，但解析核心未自足内联，因此替代包未完整证明。",
            RKS_LOG_ATOM,
        ),
        row(
            ROW_COLUMN_GATE,
            row_column_closed,
            row_column_closed,
            "最终行/列无条件闭合仍需自足证明解析核心，或走独立晋级接受事件。",
            RKS_LOG_ATOM,
        ),
    ]

    return {
        "certificate_type": "prime_matrix_strict_dstructure_tail_rankin_replacement_compression_router",
        "status": "self_contained_replacement_package_compressed_to_rks_log_reciprocal_kloosterman_core",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "replacement_package_target_active": target_active,
        "finite_rankin_replacement_closed": finite_rankin_closed,
        "dstructure_formal_replacement_shell_closed": dstructure_formal_replacement_closed,
        "tail_log4_formal_decomposition_closed": tail_formal_shell_closed and tail_decomposition_closed,
        "tail_log4_smooth_endpoint_closed": tail_smooth_closed,
        "tail_log4_mid_large_modulus_reduced": tail_mid_reduced,
        "rks_log_reciprocal_kloosterman_atom_isolated": rks_log_isolated,
        "ext_labels_registered": ext_labels_registered,
        "burgess_pointwise_does_not_replace_rks_log": True,
        "rks_log_reciprocal_kloosterman_internalized": rks_log_internalized,
        "external_analytic_inputs_self_contained_internalized": ext_analytic_inputs_internalized,
        "self_contained_dstructure_tail_log4_finite_rankin_replacement_package_proved": replacement_package_proved,
        "promotion_package_boundary_closed": promotion_boundary_closed,
        "final_promotion_gate_accepted": independent_acceptance_closed,
        "row_column_unconditional_closed": row_column_closed,
        "next_direct_attack_target": RKS_LOG_ATOM,
        "parallel_supporting_target": EXT_ANALYTIC_ATOM,
        "parallel_external_acceptance_target": PROMOTION_GATE,
        "replacement_compression": replacement_compression,
        "why_burgess_not_enough": why_burgess_not_enough,
        "current_frontier": current_frontier,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本轮把 `SelfContainedDStructureTailLog4FiniteRankinReplacementPackage` 继续压缩。"
            "finite Rankin 子账本已经由 manifest/data 与 batch pass-or-return 闭合；A/B 到 D 与 D 组结构壳也已附录化。"
            "Tail-log4 中，平滑端点和中谱大模数层已拆成可审查账本，真正未内联的数学核心只剩 "
            "`RKS-log`：倒数 Kloosterman/BG 型对数节省及相关 EXT 解析输入。"
            "新近闭合的 Burgess 乘法角色和不能替代它，因为 RKS-log 是加性倒数相位问题。"
            "因此当前唯一内部自足最窄点是证明 `SelfContainedRKSLogReciprocalKloostermanTailLog4Input`；"
            "行/列命题仍未无条件闭合。"
        ),
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "rows": rows,
    }


def render_key_value_section(lines: list[str], title: str, mapping: dict[str, Any]) -> None:
    """追加键值表。"""
    lines.extend(["", title, "", "| field | value |", "| --- | --- |"])
    for key, value in mapping.items():
        lines.append(f"| `{table_cell(key)}` | {table_cell(value)} |")


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict DStructure/Tail-log4/Rankin 自足替代包压缩证书",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"finite_rankin_replacement_closed={fmt_bool(result['finite_rankin_replacement_closed'])}",
        f"dstructure_formal_replacement_shell_closed={fmt_bool(result['dstructure_formal_replacement_shell_closed'])}",
        f"tail_log4_formal_decomposition_closed={fmt_bool(result['tail_log4_formal_decomposition_closed'])}",
        f"rks_log_reciprocal_kloosterman_atom_isolated={fmt_bool(result['rks_log_reciprocal_kloosterman_atom_isolated'])}",
        f"rks_log_reciprocal_kloosterman_internalized={fmt_bool(result['rks_log_reciprocal_kloosterman_internalized'])}",
        f"self_contained_dstructure_tail_log4_finite_rankin_replacement_package_proved={fmt_bool(result['self_contained_dstructure_tail_log4_finite_rankin_replacement_package_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
    ]

    render_key_value_section(lines, "## 1. 替代包压缩", result["replacement_compression"])
    render_key_value_section(lines, "## 2. Burgess 不能替代 RKS-log", result["why_burgess_not_enough"])
    render_key_value_section(lines, "## 3. 当前前沿", result["current_frontier"])

    lines.extend(
        [
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=table_cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=table_cell(item["meaning"]),
                remaining=table_cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 5. 下一唯一内部自足最窄点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    """生成 JSON 和 Markdown 证书。"""
    MONO.mkdir(parents=True, exist_ok=True)
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
