#!/usr/bin/env python3
"""生成 strict acyclic canonical-lock 原子化路由证书。

用法示例：
  python3 experiments/prime_matrix_strict_acyclic_canonical_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-strict-acyclic-canonical-lock-router.json
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"
OUT_JSON = DOCS / "prime-matrix-strict-acyclic-canonical-lock-router.json"
OUT_MD = DOCS / "prime-matrix-strict-acyclic-canonical-lock-router.md"


SOURCE_FILES = [
    "prime-matrix-strict-acyclic-terminal-family-attack-router.md",
    "prime-matrix-canonical-terminal-promotion-closure-router.md",
    "prime-matrix-clean-core-source-loop-cut-router.md",
    "prime-matrix-canonical-formal-unit-hash-stability-router.md",
    "prime-matrix-pdec-cap-transverse-embedding-router.md",
    "prime-matrix-triad-a1-source-lock-contract-router.md",
    "prime-matrix-triad-a1-dibfi-actual-source-provenance-ledger-router.md",
    "prime-matrix-noncanonical-source-core-atomization-router.md",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_result() -> dict:
    source_hashes = {
        f"docs/monograph/{name}": sha256(DOCS / name)
        for name in SOURCE_FILES
        if (DOCS / name).exists()
    }

    lock_before = "AcyclicTerminalCanonicalLockToCanonicalSourceBoundary"
    lock_after = (
        "AcyclicSeedCanonicalSourceFiniteFactorEmbedding "
        "AND TerminalCertificateSameSetPushforwardIdentity "
        "AND NoNoncanonicalPayloadSurvivesCanonicalProjection"
    )
    fallback = (
        "DirectAcyclicSameSetPDECCapDualCertificate "
        "OR DirectAcyclicCleanKLSDLSEstimateWithNamedReturn"
    )
    terminal_gap_after = f"(({lock_after}) OR {fallback})"
    strict_basis_with_external_mertens = (
        "AcyclicPreCauchyNoncanonicalPrimitiveSourceSeedAndReturn AND "
        f"{terminal_gap_after} AND "
        "SelfContainedDStructureTailLog4FiniteRankinReplacementPackage"
    )

    rows = [
        {
            "gate": "AcyclicCanonicalLockGateActive",
            "closed": True,
            "proved": False,
            "meaning": "上一层第一优先点是把 acyclic terminal family 锁入 canonical-source 边界。",
            "remaining": lock_before,
        },
        {
            "gate": "HashStabilityNotEnough",
            "closed": True,
            "proved": True,
            "meaning": "canonical formal unit hash stability 只保证记录不改名；它不证明 noncanonical payload 是 canonical 源的因子。",
            "remaining": "仍需源头因子嵌入。",
        },
        {
            "gate": "CanonicalSourceProvenanceImportedWithScope",
            "closed": True,
            "proved": True,
            "meaning": "canonical-source 的来源账本已经闭合，条件是 pre-Cauchy lambda 按定义等于 RIW/Buchstab 决策树系数。",
            "remaining": "acyclic noncanonical seed 必须证明满足这个条件或被投影成其有限因子。",
        },
        {
            "gate": "KnownTransverseEmbeddingNotUniversal",
            "closed": True,
            "proved": True,
            "meaning": "PDEC-CAP 横向 formal unit 嵌入 canonical 源的函子性已在特定横向商对象上闭合。",
            "remaining": "不能自动覆盖当前 acyclic clean-core/moving-block terminal family。",
        },
        {
            "gate": "SourceSeedEmbeddingAtomPinned",
            "closed": True,
            "proved": False,
            "meaning": "必须证明 acyclic seed 是 canonical A1/KZ-E pre-Cauchy 源的限制、商、条件化或确定性推前。",
            "remaining": "AcyclicSeedCanonicalSourceFiniteFactorEmbedding。",
        },
        {
            "gate": "SameSetPushforwardAtomPinned",
            "closed": True,
            "proved": False,
            "meaning": "即便源可嵌入，还必须证明终端证书下的 U_CRT、L_PDEC、坏窗集合和权重质量推前后完全同口径。",
            "remaining": "TerminalCertificateSameSetPushforwardIdentity。",
        },
        {
            "gate": "NoNoncanonicalPayloadAtomPinned",
            "closed": True,
            "proved": False,
            "meaning": "canonical 投影后不得残留未登记的 moving same-(u,v) 原子、Type/Fourier 容量乘子或 non-AP payload。",
            "remaining": "NoNoncanonicalPayloadSurvivesCanonicalProjection。",
        },
        {
            "gate": "CanonicalLockReducedToThreeSubatoms",
            "closed": True,
            "proved": False,
            "meaning": "canonical-lock 被压成源因子嵌入、同集推前恒等式、无 noncanonical 残留三项。",
            "remaining": lock_after,
        },
        {
            "gate": "CanonicalLockCurrentCorpusProved",
            "closed": True,
            "proved": False,
            "meaning": "当前材料尚未证明这三项，因此不能把 canonical 终端闭合导入 acyclic noncanonical 分支。",
            "remaining": f"{lock_after} OR {fallback}",
        },
    ]

    return {
        "certificate_type": "prime_matrix_strict_acyclic_canonical_lock_router",
        "status": "acyclic_canonical_lock_reduced_to_source_embedding_and_same_set_pushforward_open",
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "acyclic_canonical_lock_boundary_refined": True,
        "hash_stability_imported": True,
        "canonical_source_provenance_imported_with_scope": True,
        "known_transverse_embedding_not_universal": True,
        "acyclic_seed_canonical_source_embedding_proved": False,
        "terminal_certificate_same_set_pushforward_proved": False,
        "no_noncanonical_payload_survives_projection_proved": False,
        "acyclic_terminal_canonical_lock_proved": False,
        "row_column_unconditional_closed": False,
        "terminal_gap_before_router": lock_before,
        "terminal_gap_after_router": terminal_gap_after,
        "strict_self_contained_math_basis_after_router": strict_basis_with_external_mertens,
        "next_attack_contract": {
            "name": "AcyclicSeedCanonicalSourceFiniteFactorEmbedding",
            "must_prove": [
                "从假设早期零行反例生成的 acyclic pre-Cauchy seed 是 canonical A1/KZ-E 源的有限测度因子",
                "源因子嵌入保持同一 formal unit 与 branch key",
                "终端证书的坏窗集合、U_CRT、L_PDEC 和权重质量在推前前后一致",
                "任何未能嵌入的 noncanonical payload 必须回流 direct PDEC dual 或 direct CleanKLS/DLS",
            ],
            "cannot_use_as_proof": [
                "只给 formal_unit_id 哈希稳定",
                "只引用 canonical-source 终端闭合",
                "只证明某个横向 PDEC-CAP 子对象可嵌入",
                "把 generic WFD 或 noncanonical full-S 补集当成 canonical RIW/Buchstab 源",
            ],
        },
        "rows": rows,
        "source_hashes": source_hashes,
        "plain_conclusion": (
            "本步把 acyclic terminal canonical-lock 从宽泛作用域问题压成三个必要子原子："
            "acyclic seed 必须是 canonical A1/KZ-E pre-Cauchy 源的有限测度因子；终端证书必须保持同集推前恒等式；"
            "canonical 投影后不能残留未登记 noncanonical payload。哈希稳定和 canonical-source 来源闭合都是可用材料，"
            "但它们本身不足以证明当前 acyclic noncanonical 分支已经 canonical-lock。"
        ),
    }


def render_markdown(result: dict) -> str:
    lines = [
        "# Prime Matrix strict acyclic canonical-lock 原子化路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"acyclic_canonical_lock_boundary_refined={str(result['acyclic_canonical_lock_boundary_refined']).lower()}",
        f"hash_stability_imported={str(result['hash_stability_imported']).lower()}",
        f"canonical_source_provenance_imported_with_scope={str(result['canonical_source_provenance_imported_with_scope']).lower()}",
        f"known_transverse_embedding_not_universal={str(result['known_transverse_embedding_not_universal']).lower()}",
        f"acyclic_seed_canonical_source_embedding_proved={str(result['acyclic_seed_canonical_source_embedding_proved']).lower()}",
        f"terminal_certificate_same_set_pushforward_proved={str(result['terminal_certificate_same_set_pushforward_proved']).lower()}",
        f"no_noncanonical_payload_survives_projection_proved={str(result['no_noncanonical_payload_survives_projection_proved']).lower()}",
        f"acyclic_terminal_canonical_lock_proved={str(result['acyclic_terminal_canonical_lock_proved']).lower()}",
        f"row_column_unconditional_closed={str(result['row_column_unconditional_closed']).lower()}",
        f"terminal_gap_after_router={result['terminal_gap_after_router']}",
        "```",
        "",
        "## 1. lock 拆分",
        "",
        "拆分前：",
        "",
        "```text",
        result["terminal_gap_before_router"],
        "```",
        "",
        "拆分后：",
        "",
        "```text",
        result["terminal_gap_after_router"],
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
                closed=str(row["closed"]).lower(),
                proved=str(row["proved"]).lower(),
                meaning=row["meaning"],
                remaining=row["remaining"],
            )
        )

    contract = result["next_attack_contract"]
    lines.extend(
        [
            "",
            "## 3. 最新严格基",
            "",
            "若接受外部 Mertens/theta 显式定理，高段解析缺口移出后，当前 strict 基为：",
            "",
            "```text",
            result["strict_self_contained_math_basis_after_router"],
            "```",
            "",
            "## 4. 下一主攻合同",
            "",
            f"主攻名：`{contract['name']}`。",
            "",
            "必须证明：",
        ]
    )
    for item in contract["must_prove"]:
        lines.append(f"- {item}。")
    lines.append("")
    lines.append("不能作为证明使用：")
    for item in contract["cannot_use_as_proof"]:
        lines.append(f"- {item}。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    result = build_result()
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
