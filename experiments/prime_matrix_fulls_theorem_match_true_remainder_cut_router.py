#!/usr/bin/env python3
"""生成 Full-S theorem-match 后的真剩余切割证书。

用法示例：
  python3 experiments/prime_matrix_fulls_theorem_match_true_remainder_cut_router.py
  python3 -m json.tool docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.json

输出：
  data/prime-matrix-fulls-theorem-match-true-remainder-cut-ledger.json
  docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.json
  docs/monograph/prime-matrix-fulls-theorem-match-true-remainder-cut-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-fulls-theorem-match-true-remainder-cut"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-ncblk-branch-alignment-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-exact-full-s-source-entropy-reduction-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-support-range-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-source-antiatom-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-terminal-split-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-self-contained-antiatom-nogo-router.json",
    DOCS / "prime-matrix-self-contained-narrowest-core-router.json",
    DOCS / "prime-matrix-noncanonical-source-core-atomization-router.json",
    DOCS / "prime-matrix-final-open-input-current-attack-router.json",
    DOCS / "prime-matrix-three-final-atoms-hard-attack-router.json",
    DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json",
]


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def gate(
    name: str,
    boundary_closed: bool,
    proved_or_accepted: bool,
    effect: str,
    remaining: str,
) -> dict[str, Any]:
    """构造切割表行。"""
    return {
        "gate": name,
        "boundary_closed": boundary_closed,
        "proved_or_accepted": proved_or_accepted,
        "effect": effect,
        "remaining": remaining,
    }


def build_gates() -> list[dict[str, Any]]:
    """生成真剩余切割账本。"""
    return [
        gate(
            "LatestTheoremMatchFrontierImported",
            True,
            False,
            "上一层给出 FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration。",
            "需要删除伪剩余并展开 NCBLK。",
        ),
        gate(
            "APSourceLiftFilteredByNoGo",
            True,
            True,
            "APSourceLift 在当前 non-AP uncentered no-projection 对象中被分支定义和对象账本阻断。",
            "若新增上游 AP source identity，那已经是新定理输入，不是现有捷径。",
        ),
        gate(
            "NCBLKExpandedToExactSourceEntropy",
            True,
            False,
            "NCBLKActualBlockNonConcentration 经 BWFD/BSC/KFLS 与 branch alignment 压成 exact full-S source entropy 或外部谱定理。",
            "ExactFullSNonAPWFDSourceEntropyOrExternalDIBFIKuznetsov。",
        ),
        gate(
            "ExactEntropyReducedToSupportCapacity",
            True,
            False,
            "exact source entropy 降为 u/v 精确因子支撑与 Type/Fourier 容量兼容；balanced range 已闭合。",
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput。",
        ),
        gate(
            "GenericAntiAtomRefuted",
            True,
            True,
            "generic full-S WFD 反原子被 moving-delta capacity model 反证。",
            "只能证明 actual noncanonical source theorem、限制 canonical source、或接受外部 FullS-KLS-ext。",
        ),
        gate(
            "ExternalContractNotPrimarySourceClosure",
            True,
            False,
            "FullS-KLS-ext 逐项匹配但只是外部合同；现有 DI/BFI/Maynard 主来源未逐行推出它。",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch or NewAutomorphicDispersionProof。",
        ),
        gate(
            "DStructureRankinPromotionIndependent",
            True,
            False,
            "即使 full-S 数学输入完成，全局晋级仍需 DStructure/Tail-log4/finite Rankin 独立验收。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。",
        ),
        gate(
            "TrueRemainderCutClosed",
            True,
            False,
            "最新三口已被切成两条数学输入线加一个独立晋级门；APSourceLift 不再是活动真剩余。",
            "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput) AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance。",
        ),
    ]


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 Markdown 表格。"""
    lines = [
        "| gate | boundary closed | proved/accepted | effect | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {effect} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["boundary_closed"]),
                proved=fmt_bool(item["proved_or_accepted"]),
                effect=cell(item["effect"]),
                remaining=cell(item["remaining"]),
            )
        )
    return "\n".join(lines)


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    dependency_hashes = {
        str(path.relative_to(ROOT)): sha256(path)
        for path in DEPENDENCIES
        if path.exists()
    }
    return {
        "certificate_type": "prime_matrix_fulls_theorem_match_true_remainder_cut_router",
        "status": "ap_lift_filtered_ncblk_expanded_true_remainder_external_or_actual_source_core_open",
        "imported_latest_frontier": (
            "FullSNonAPWFDKLSTheoremInput OR APSourceLift "
            "OR NCBLKActualBlockNonConcentration"
        ),
        "removed_from_active_true_remainder": [
            "APSourceLift",
            "generic FullS WFD anti-atom",
            "NCBLK as an opaque terminal name",
        ],
        "conditional_external_lane": (
            "Accept FullS-KLS-ext as an external blackbox contract; otherwise prove "
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch or NewAutomorphicDispersionProof."
        ),
        "self_contained_actual_source_lane": (
            "ActualNoncanonicalFullSFactorSupportCapacityTheoremInput, equivalently exact "
            "source entropy / strengthened anti-atom for the actual noncanonical full-S source."
        ),
        "independent_promotion_gate": (
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "current_true_remainder_basis": (
            "(ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch "
            "OR ActualNoncanonicalFullSFactorSupportCapacityTheoremInput) "
            "AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "external_blackbox_conditional_basis": (
            "AcceptedFullSKLSExt AND "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ),
        "unconditional_closure_reached": False,
        "row_column_unconditional_closed": False,
        "gates": build_gates(),
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "最新 theorem-match 的三口不是三个同等真剩余。APSourceLift 已由 no-go 证书过滤；"
            "NCBLK 作为黑箱名已展开到 actual noncanonical full-S 源的支撑/容量核心；"
            "FullS-KLS-ext 只在接受外部黑箱合同后给出条件闭合，尚未由 DI/BFI 主来源逐项推出。"
            "因此当前无黑箱/主来源版真剩余为 exact primary-source full-S KLS 定理匹配，"
            "或 actual noncanonical full-S factor-support/capacity 定理，再加 DStructure/Rankin 独立晋级验收。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    lines = [
        "# Prime Matrix Full-S theorem-match 真剩余切割证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 输入前沿",
        "",
        "```text",
        payload["imported_latest_frontier"],
        "```",
        "",
        "## 2. 切割表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 3. 删除的伪剩余",
        "",
    ]
    for item in payload["removed_from_active_true_remainder"]:
        lines.append(f"- `{item}`")
    lines.extend(
        [
            "",
            "## 4. 最新真剩余基",
            "",
            "无黑箱/主来源逐项版：",
            "",
            "```text",
            payload["current_true_remainder_basis"],
            "```",
            "",
            "接受外部黑箱合同版：",
            "",
            "```text",
            payload["external_blackbox_conditional_basis"],
            "```",
            "",
            "## 5. 结论",
            "",
            payload["plain_conclusion"],
            "",
            "本证书不证明无条件闭合；它只删除伪剩余并把真剩余压到更窄的数学输入格式。",
            "",
            "## 6. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in payload["dependency_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": payload["status"],
                "unconditional_closure_reached": payload["unconditional_closure_reached"],
                "current_true_remainder_basis": payload["current_true_remainder_basis"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
