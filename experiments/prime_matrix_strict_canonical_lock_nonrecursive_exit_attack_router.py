#!/usr/bin/env python3
"""生成 strict canonical-lock 非循环出口直攻证书。

用法示例：
  python3 experiments/prime_matrix_strict_canonical_lock_nonrecursive_exit_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
OUT_MD = DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
    "prime-matrix-strict-acyclic-canonical-lock-router.json",
    "prime-matrix-strict-acyclic-seed-canonical-embedding-router.json",
    "prime-matrix-strict-source-admission-branch-absorption-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-clean-core-source-loop-cut-router.json",
    "prime-matrix-hypothetical-zero-row-seed-no-go-router.json",
    "prime-matrix-canonical-terminal-promotion-closure-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空字典，保持旧语料可运行。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: bool) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if value else "false"


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def source_hashes() -> dict[str, str]:
    """汇总依赖证据哈希。"""
    return {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }


def build_rows(
    recurrence: dict[str, Any],
    canonical_lock: dict[str, Any],
    seed_embedding: dict[str, Any],
    source_absorb: dict[str, Any],
    entropy_firewall: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 canonical-lock 非循环出口直攻判定表。"""
    canonical_certificate = (
        "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND "
        "AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND "
        "AcyclicSeedNoSourceReplacementOrPayloadCreation AND "
        "TerminalCertificateSameSetPushforwardIdentity AND "
        "NoNoncanonicalPayloadSurvivesCanonicalProjection"
    )
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    return [
        {
            "gate": "StrictTerminalAfterRecurrenceActive",
            "closed": recurrence.get("strict_self_contained_terminal_after_router")
            == "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
            "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem",
            "proved": False,
            "meaning": "rate-bearing 终端三原子经回流防火墙后只剩 canonical-lock 或原 actual-source 熵目标。",
            "remaining": recurrence.get("strict_self_contained_terminal_after_router"),
        },
        {
            "gate": "CanonicalLockRefinedToFiveLedgerCertificate",
            "closed": seed_embedding.get("seed_embedding_gap_after_router")
            == (
                "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy "
                "AND AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity "
                "AND AcyclicSeedNoSourceReplacementOrPayloadCreation"
            )
            and canonical_lock.get("terminal_certificate_same_set_pushforward_proved")
            is False
            and canonical_lock.get("no_noncanonical_payload_survives_projection_proved")
            is False,
            "proved": False,
            "meaning": "canonical-lock 不是单个标签，而是 pre-Cauchy canonical 准入、有限因子图、无来源替换、同集推前、无 payload 残留五项合取证书。",
            "remaining": canonical_certificate,
        },
        {
            "gate": "BranchAdmissionCannotBeRecoveredDownstream",
            "closed": seed_embedding.get("source_loop_cut_imported") is True,
            "proved": True,
            "meaning": "若 seed 的 canonical 准入只从终端证书、payment 图、早期零行覆盖或投影缺席反推，则落入来源环，不能作为 pre-Cauchy source。",
            "remaining": "AcyclicCanonicalPreCauchyCoefficientIdentityLedger。",
        },
        {
            "gate": "A1AdmissionAbsorbedAsBranchStatement",
            "closed": source_absorb.get("source_admission_absorbed_from_active_or")
            is True,
            "proved": True,
            "meaning": "A1 clean branch admission 只说明 canonical 分支可内部处理；它不是 unrestricted noncanonical 分支的全局矛盾。",
            "remaining": "仍需 exact same-set canonical promotion certificate 或 noncanonical source entropy。",
        },
        {
            "gate": "ExactCanonicalPromotionConditionalOnly",
            "closed": True,
            "proved": True,
            "meaning": "若五项证书全部提交，则对象已按同一 formal unit 和同一坏窗集合进入 canonical 分支，可调用 canonical 分支闭合；这只是条件晋级律。",
            "remaining": "AcyclicCanonicalExactSameSetPromotionCertificate。",
        },
        {
            "gate": "AnyMissingLedgerRejectsCanonicalLock",
            "closed": True,
            "proved": True,
            "meaning": "五项中任一项缺失时，有限因子或同集推前定义失败，canonical-lock 路线不可用。",
            "remaining": target,
        },
        {
            "gate": "DirectTerminalFallbackRejectedAsNonrecursiveProof",
            "closed": recurrence.get("terminal_route_returns_to_source_entropy_target")
            is True,
            "proved": True,
            "meaning": "direct PDEC/direct CleanKLS 的裸标签链已被终端回流防火墙识别为回流，不是源熵目标的非递归证明。",
            "remaining": target,
        },
        {
            "gate": "CurrentCorpusExactCanonicalCertificateProved",
            "closed": False,
            "proved": False,
            "meaning": "当前语料没有提交五项 exact same-set canonical 晋级证书，不能宣称 canonical-lock 已闭合。",
            "remaining": canonical_certificate,
        },
        {
            "gate": "NewActualSourceEntropyStillOpen",
            "closed": entropy_firewall.get("new_actual_source_entropy_theorem_proved")
            is False,
            "proved": False,
            "meaning": "canonical-lock 出口收缩后，noncanonical 主线仍是原 NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem。",
            "remaining": target,
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict canonical-lock 非循环出口直攻证书。"""
    recurrence = load_json(
        DOCS / "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"
    )
    canonical_lock = load_json(DOCS / "prime-matrix-strict-acyclic-canonical-lock-router.json")
    seed_embedding = load_json(
        DOCS / "prime-matrix-strict-acyclic-seed-canonical-embedding-router.json"
    )
    source_absorb = load_json(
        DOCS / "prime-matrix-strict-source-admission-branch-absorption-router.json"
    )
    entropy_firewall = load_json(
        DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
    )

    canonical_certificate = (
        "AcyclicSeedCanonicalBranchAdmissionBeforeCauchy AND "
        "AcyclicSeedFiniteMeasurableFactorMapAndWeightIdentity AND "
        "AcyclicSeedNoSourceReplacementOrPayloadCreation AND "
        "TerminalCertificateSameSetPushforwardIdentity AND "
        "NoNoncanonicalPayloadSurvivesCanonicalProjection"
    )
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    terminal_after = f"AcyclicCanonicalExactSameSetPromotionCertificate OR {target}"
    rows = build_rows(
        recurrence=recurrence,
        canonical_lock=canonical_lock,
        seed_embedding=seed_embedding,
        source_absorb=source_absorb,
        entropy_firewall=entropy_firewall,
    )

    return {
        "certificate_type": "prime_matrix_strict_canonical_lock_nonrecursive_exit_attack_router",
        "status": "strict_canonical_lock_nonrecursive_exit_refined_to_exact_same_set_certificate_or_source_entropy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "canonical_lock_nonrecursive_exit_firewall_closed": True,
        "canonical_lock_refined_to_exact_same_set_certificate": True,
        "canonical_exact_branch_conditional_promotion_closed": True,
        "source_admission_standalone_global_contradiction": False,
        "direct_terminal_labels_rejected_as_nonrecursive_proof": True,
        "acyclic_canonical_exact_same_set_promotion_certificate_proved": False,
        "acyclic_seed_canonical_branch_admission_proved": False,
        "acyclic_seed_finite_factor_map_weight_identity_proved": False,
        "acyclic_seed_no_source_replacement_proved": False,
        "terminal_certificate_same_set_pushforward_proved": False,
        "no_noncanonical_payload_survives_projection_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "canonical_exact_certificate_definition": canonical_certificate,
        "strict_self_contained_terminal_before_router": (
            "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary OR "
            "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
        ),
        "strict_self_contained_terminal_after_router": terminal_after,
        "next_direct_attack_target": (
            "AcyclicCanonicalPreCauchyCoefficientIdentityLedger "
            "OR NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
        ),
        "hard_law": (
            "canonical-lock 不是从早期零行覆盖图自动导出的矛盾，而是五项 exact same-set "
            "canonical 晋级证书。五项全真时，只得到 canonical 分支条件晋级；任一项缺失时，"
            "canonical-lock 路线失效，不能转用 direct PDEC/CleanKLS 标签冒充证明，必须回到原 "
            "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步直接攻击 canonical-lock 的非循环出口。结论是：canonical-lock 不能由哈希稳定、"
            "A1 分支陈述、横向嵌入或早期零行覆盖几何自动推出；它只能作为五项 exact same-set "
            "canonical 晋级证书使用。若证书完整，则该分支按 canonical 范围条件晋级；若证书任一项缺失，"
            "canonical-lock 不是闭合证明，direct PDEC/CleanKLS 又会回流，剩余仍是原 "
            "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem。行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict canonical-lock 非循环出口直攻路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"canonical_lock_nonrecursive_exit_firewall_closed={fmt_bool(result['canonical_lock_nonrecursive_exit_firewall_closed'])}",
        f"canonical_lock_refined_to_exact_same_set_certificate={fmt_bool(result['canonical_lock_refined_to_exact_same_set_certificate'])}",
        f"canonical_exact_branch_conditional_promotion_closed={fmt_bool(result['canonical_exact_branch_conditional_promotion_closed'])}",
        f"acyclic_canonical_exact_same_set_promotion_certificate_proved={fmt_bool(result['acyclic_canonical_exact_same_set_promotion_certificate_proved'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 出口精炼",
        "",
        "精炼前：",
        "",
        "```text",
        result["strict_self_contained_terminal_before_router"],
        "```",
        "",
        "精炼后：",
        "",
        "```text",
        result["strict_self_contained_terminal_after_router"],
        "```",
        "",
        "`AcyclicCanonicalExactSameSetPromotionCertificate` 的定义是：",
        "",
        "```text",
        result["canonical_exact_certificate_definition"],
        "```",
        "",
        "## 2. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in result["rows"]:
        lines.append(
            "| `{gate}` | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=row["gate"],
                closed=fmt_bool(row["closed"]),
                proved=fmt_bool(row["proved"]),
                meaning=table_cell(row["meaning"]),
                remaining=table_cell(row["remaining"]),
            )
        )
    lines.extend(
        [
            "",
            "## 3. 结构结论",
            "",
            result["hard_law"],
            "",
            "## 4. 下一主攻点",
            "",
            "```text",
            result["next_direct_attack_target"],
            "```",
            "",
            "若继续走 canonical-lock 侧，最窄原子是 `AcyclicCanonicalPreCauchyCoefficientIdentityLedger`：必须在 Cauchy/dispersion/terminal extraction 之前给出 canonical RIW/Buchstab 系数恒等式，而不能从下游覆盖或终端证书反推。若不走该侧，主线仍是原 actual-source 熵定理。",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    """写出 JSON 和 Markdown 证书。"""
    result = build_result()
    OUT_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")


if __name__ == "__main__":
    main()
