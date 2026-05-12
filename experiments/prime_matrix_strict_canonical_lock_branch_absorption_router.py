#!/usr/bin/env python3
"""生成 strict canonical-lock 分支吸收证书。

用法示例：
  python3 experiments/prime_matrix_strict_canonical_lock_branch_absorption_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-canonical-lock-branch-absorption-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-canonical-lock-branch-absorption-router.json"
OUT_MD = DOCS / "prime-matrix-strict-canonical-lock-branch-absorption-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json",
    "prime-matrix-canonical-terminal-promotion-closure-router.json",
    "prime-matrix-strict-source-admission-branch-absorption-router.json",
    "prime-matrix-strict-exact-entropy-source-law-firewall-router.json",
    "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json",
]


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
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
    lock_exit: dict[str, Any],
    canonical_promotion: dict[str, Any],
    source_absorb: dict[str, Any],
    entropy_firewall: dict[str, Any],
    recurrence: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 canonical-lock 分支吸收判定表。"""
    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    return [
        {
            "gate": "ExactSameSetCanonicalCertificateBranchPinned",
            "closed": lock_exit.get("canonical_lock_refined_to_exact_same_set_certificate")
            is True,
            "proved": False,
            "meaning": "上一层已把 canonical-lock 精炼成五项 exact same-set canonical 晋级证书。",
            "remaining": lock_exit.get("canonical_exact_certificate_definition"),
        },
        {
            "gate": "CanonicalTerminalPromotionImportedWithScope",
            "closed": canonical_promotion.get("canonical_source_terminal_promotion_closed")
            is True
            and canonical_promotion.get("global_unrestricted_terminal_family_exclusion_closed")
            is False,
            "proved": True,
            "meaning": "canonical RIW/Buchstab source 分支内，终端晋级已闭合；但该闭合不覆盖 unrestricted/global noncanonical 分支。",
            "remaining": "scope=canonical-source branch only。",
        },
        {
            "gate": "CertificatePresentBranchDischargedConditionally",
            "closed": lock_exit.get("canonical_exact_branch_conditional_promotion_closed")
            is True,
            "proved": True,
            "meaning": "若五项证书实际提交，则对象已在同一 formal unit 和同一坏窗集合下进入 canonical 分支，按 scoped canonical promotion 处理。",
            "remaining": "不再作为活动 noncanonical 终端。",
        },
        {
            "gate": "CertificateAbsentBranchCannotUseCanonicalLock",
            "closed": True,
            "proved": True,
            "meaning": "若五项证书任一项缺失，则 finite factor 或 same-set pushforward 定义失败，canonical-lock 不能被调用。",
            "remaining": target,
        },
        {
            "gate": "A1AdmissionAbsorptionConsistent",
            "closed": source_absorb.get("source_admission_absorbed_from_active_or")
            is True,
            "proved": True,
            "meaning": "这与 A1 source-admission 分支吸收一致：canonical 分支陈述不作为 global contradiction，只作为 scoped case。",
            "remaining": target,
        },
        {
            "gate": "DirectTerminalFallbackStillRejected",
            "closed": recurrence.get("terminal_route_returns_to_source_entropy_target")
            is True,
            "proved": True,
            "meaning": "证书缺失时不能改走 direct PDEC/direct CleanKLS 标签链，因为该链已被证明回流。",
            "remaining": target,
        },
        {
            "gate": "ActiveNoncanonicalTerminalReducedToSourceEntropy",
            "closed": entropy_firewall.get("new_actual_source_entropy_theorem_proved")
            is False,
            "proved": False,
            "meaning": "吸收 canonical scoped case 后，活动 noncanonical 主线只剩原 actual-source 熵定理。",
            "remaining": target,
        },
        {
            "gate": "RowColumnUnconditionalClosureCurrentCorpusProved",
            "closed": False,
            "proved": False,
            "meaning": "本步只是分支吸收，不证明 source entropy，也不关闭 DStructure/Rankin 或最终行/列命题。",
            "remaining": f"{target} AND remaining promotion gates。",
        },
    ]


def build_result() -> dict[str, Any]:
    """构造 strict canonical-lock 分支吸收证书。"""
    lock_exit = load_json(
        DOCS / "prime-matrix-strict-canonical-lock-nonrecursive-exit-attack-router.json"
    )
    canonical_promotion = load_json(
        DOCS / "prime-matrix-canonical-terminal-promotion-closure-router.json"
    )
    source_absorb = load_json(
        DOCS / "prime-matrix-strict-source-admission-branch-absorption-router.json"
    )
    entropy_firewall = load_json(
        DOCS / "prime-matrix-strict-exact-entropy-source-law-firewall-router.json"
    )
    recurrence = load_json(
        DOCS / "prime-matrix-strict-rate-bearing-terminal-recurrence-firewall-router.json"
    )

    target = "NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem"
    rows = build_rows(
        lock_exit=lock_exit,
        canonical_promotion=canonical_promotion,
        source_absorb=source_absorb,
        entropy_firewall=entropy_firewall,
        recurrence=recurrence,
    )
    return {
        "certificate_type": "prime_matrix_strict_canonical_lock_branch_absorption_router",
        "status": "strict_canonical_lock_absorbed_as_scoped_canonical_branch_active_noncanonical_source_entropy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "canonical_lock_branch_absorption_closed": True,
        "canonical_exact_certificate_branch_discharged_conditionally": True,
        "canonical_source_terminal_promotion_imported_with_scope": True,
        "canonical_lock_standalone_global_contradiction": False,
        "global_unrestricted_terminal_family_exclusion_closed": False,
        "acyclic_canonical_exact_same_set_promotion_certificate_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "new_actual_source_entropy_theorem_proved": False,
        "row_column_unconditional_closed": False,
        "strict_terminal_before_absorption": lock_exit.get(
            "strict_self_contained_terminal_after_router"
        ),
        "strict_active_noncanonical_terminal_after_absorption": target,
        "next_direct_attack_target": target,
        "hard_law": (
            "canonical-lock 的 exact same-set 证书若存在，只把该 case 送入 canonical-source "
            "scoped promotion；若证书不存在，canonical-lock 不可用。因 direct PDEC/CleanKLS 已回流，"
            "活动 noncanonical 主线被压成唯一目标 `NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。"
            "这不是行/列命题无条件闭合。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 canonical-lock 从活动非 canonical 主线中吸收掉：五项 exact same-set 证书成立时，"
            "它只是 canonical-source 范围内的条件晋级 case；证书缺失时则不能调用 canonical-lock。"
            "因此 canonical-lock 不再是独立非循环出口，真正活动的 noncanonical 剩余目标只剩原 "
            "`NewActualCleanCoreFullSNonAPWFDSourceEntropyTheorem`。命题仍未无条件闭合。"
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix strict canonical-lock 分支吸收路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"same_theorem_target_preserved={fmt_bool(result['same_theorem_target_preserved'])}",
        f"no_theorem_switch={fmt_bool(result['no_theorem_switch'])}",
        f"canonical_lock_branch_absorption_closed={fmt_bool(result['canonical_lock_branch_absorption_closed'])}",
        f"canonical_exact_certificate_branch_discharged_conditionally={fmt_bool(result['canonical_exact_certificate_branch_discharged_conditionally'])}",
        f"canonical_lock_standalone_global_contradiction={fmt_bool(result['canonical_lock_standalone_global_contradiction'])}",
        f"global_unrestricted_terminal_family_exclusion_closed={fmt_bool(result['global_unrestricted_terminal_family_exclusion_closed'])}",
        f"acyclic_terminal_canonical_lock_proved={fmt_bool(result['acyclic_terminal_canonical_lock_proved'])}",
        f"new_actual_source_entropy_theorem_proved={fmt_bool(result['new_actual_source_entropy_theorem_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 主线压缩",
        "",
        "吸收前：",
        "",
        "```text",
        str(result["strict_terminal_before_absorption"]),
        "```",
        "",
        "吸收后，活动 noncanonical 主线为：",
        "",
        "```text",
        result["strict_active_noncanonical_terminal_after_absorption"],
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
