#!/usr/bin/env python3
"""生成 Full-S non-AP WFD 外部定理逐项匹配矩阵证书。

用法示例：
  python3 experiments/prime_matrix_fulls_nonap_wfd_theorem_match_matrix_router.py
  python3 -m json.tool docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json

输出：
  data/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-ledger.json
  docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json
  docs/monograph/prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-fulls-nonap-wfd-theorem-match-matrix"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DEPENDENCIES = [
    DOCS / "prime-matrix-hp-cramer-local-route-reset-router.json",
    DOCS / "prime-matrix-fulls-kls-ext-acceptance-match-audit.json",
    DOCS / "prime-matrix-triad-a1-dibfi-external-full-s-match-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-full-s-kls-ext-specialization-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-primary-source-specialization-nogo-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-new-full-s-theorem-input-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-completed-weight-spectral-gap-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-ap-source-lift-nogo-router.json",
    DOCS / "prime-matrix-triad-a1-dibfi-maynard-s-compression-nogo-router.json",
    DOCS / "kls-window-di-bfi-adaptation-template.md",
    DOCS / "external-theorem-index.md",
]


MATCH_COLUMNS = [
    "object",
    "weights",
    "window",
    "moduli",
    "smoothing_projection",
    "saving_strength",
    "conclusion",
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


def gate(name: str, closed: bool, proved: bool, meaning: str, remaining: str) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": name,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def candidate(
    name: str,
    source_type: str,
    matches: dict[str, bool],
    verdict: str,
    blocking_gap: str,
    use: str,
    url: str,
) -> dict[str, Any]:
    """构造候选外部定理匹配行。"""
    missing = [item for item in MATCH_COLUMNS if not matches.get(item, False)]
    return {
        "name": name,
        "source_type": source_type,
        "matches": {item: bool(matches.get(item, False)) for item in MATCH_COLUMNS},
        "all_required_items_match": not missing,
        "missing_items": missing,
        "verdict": verdict,
        "blocking_gap": blocking_gap,
        "allowed_use": use,
        "url": url,
    }


def build_candidates() -> list[dict[str, Any]]:
    """列出候选外部输入的逐项匹配状态。"""
    return [
        candidate(
            "Baker-Harman-Pintz / Li short interval",
            "generic_short_interval",
            {
                "object": False,
                "weights": False,
                "window": False,
                "moduli": False,
                "smoothing_projection": False,
                "saving_strength": False,
                "conclusion": False,
            },
            "rejected_for_HP_top_band",
            "theta>1/2 gives intervals longer than P at x≈P^2 and gives no WFD/KLS estimate.",
            "finite or low-k range only",
            "https://arxiv.org/abs/2308.04458",
        ),
        candidate(
            "Friedlander-Iwaniec parity-sensitive sieve",
            "parity_breaking_model",
            {
                "object": False,
                "weights": True,
                "window": False,
                "moduli": False,
                "smoothing_projection": False,
                "saving_strength": False,
                "conclusion": False,
            },
            "technology_class_only",
            "breaks parity for the special polynomial x^2+y^4, not for the current full-S non-AP WFD window.",
            "conceptual model for Type-II/parity-sensitive proof design",
            "https://annals.math.princeton.edu/articles/13033",
        ),
        candidate(
            "BFI large-moduli AP theorem",
            "primary_source_ap_dispersion",
            {
                "object": False,
                "weights": True,
                "window": True,
                "moduli": True,
                "smoothing_projection": False,
                "saving_strength": True,
                "conclusion": False,
            },
            "blocked_without_APSourceLift",
            "direct theorem is AP discrepancy; current object is uncentered non-AP WFD with no hidden projection.",
            "usable only if APSourceLift is proved",
            "https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6385-11511_2006_Article_BF02399204.pdf",
        ),
        candidate(
            "DI/Kuznetsov spectral Kloosterman large sieve",
            "primary_source_spectral",
            {
                "object": False,
                "weights": True,
                "window": True,
                "moduli": True,
                "smoothing_projection": False,
                "saving_strength": True,
                "conclusion": False,
            },
            "partial_template_match_not_final_theorem",
            "phase/moduli/frequency template matches, but c-dependent completed weights and no-projection full-S object are not a ready-made corollary.",
            "core technology for a new KLS-window proof",
            "https://doi.org/10.1007/BF01390728",
        ),
        candidate(
            "Maynard/GPY small-gaps machinery",
            "multidimensional_sieve",
            {
                "object": False,
                "weights": False,
                "window": False,
                "moduli": False,
                "smoothing_projection": False,
                "saving_strength": False,
                "conclusion": False,
            },
            "blocked_by_Maynard_S_and_conclusion_mismatch",
            "bounded-gaps/admissible-tuples conclusion does not give every sqrt-window; full-S Maynard-S compression is already ruled out.",
            "secondary variable-translation research only",
            "https://annals.math.princeton.edu/2015/181-1/p07",
        ),
        candidate(
            "FullS-KLS-ext external contract",
            "new_external_contract",
            {
                "object": True,
                "weights": True,
                "window": True,
                "moduli": True,
                "smoothing_projection": True,
                "saving_strength": True,
                "conclusion": True,
            },
            "matches_if_accepted_as_new_blackbox_theorem",
            "not derived line-by-line from primary DI/BFI sources; it is the exact theorem input to prove or cite.",
            "conditional external theorem input",
            "docs/monograph/prime-matrix-fulls-kls-ext-acceptance-match-audit.md",
        ),
        candidate(
            "New automorphic/dispersion proof",
            "new_theorem_to_prove",
            {
                "object": True,
                "weights": True,
                "window": True,
                "moduli": True,
                "smoothing_projection": True,
                "saving_strength": False,
                "conclusion": False,
            },
            "open",
            "must still prove arbitrary log-saving for c-dependent residue weights or actual NC-BLK nonconcentration.",
            "primary high-risk route",
            "docs/monograph/prime-matrix-triad-a1-dibfi-c-dependent-residue-spectral-reduction-router.md",
        ),
    ]


def build_gates() -> list[dict[str, Any]]:
    """生成判定表。"""
    return [
        gate(
            "CurrentFullSNonAPWFDObjectPinned",
            True,
            True,
            "当前对象、权重、窗口、无中心化/无投影边界已固定。",
            "theorem-match only",
        ),
        gate(
            "PrimarySourcesScreenedItemwise",
            True,
            True,
            "BHP/Li、FI、BFI、DI/Kuznetsov、Maynard 均按对象/权重/窗口/模数/投影/强度逐项筛查。",
            "none at screening level",
        ),
        gate(
            "ReadyMadePrimarySourceMatchFound",
            False,
            False,
            "现有主来源没有直接覆盖 full-S non-AP uncentered no-projection WFD 对象。",
            "FullSNonAPWFDKLSTheoremInput",
        ),
        gate(
            "ExternalContractExactMatchAvailable",
            True,
            True,
            "FullS-KLS-ext 作为新外部合同与当前目标逐项匹配。",
            "accepted only as blackbox theorem input",
        ),
        gate(
            "PrimarySourceDerivationClosed",
            False,
            False,
            "尚未从 DI/BFI/Maynard/自守原文逐行推出 FullS-KLS-ext。",
            "DIBFIPrimarySourceSpecializationProof or NewAutomorphicDispersionProof",
        ),
        gate(
            "UnconditionalHPClosureReached",
            False,
            False,
            "theorem-match 矩阵只确定可用输入和缺口，不证明 H_P 无条件闭合。",
            "FullSNonAPWFDKLSTheoremInput OR APSourceLift OR NCBLKActualBlockNonConcentration",
        ),
    ]


def match_markdown(candidates: list[dict[str, Any]]) -> str:
    """输出候选定理匹配表 Markdown。"""
    columns = ["source", "type", *MATCH_COLUMNS, "verdict", "blocking gap"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for item in candidates:
        values = [
            item["name"],
            f"`{item['source_type']}`",
            *[f"`{fmt_bool(item['matches'][column])}`" for column in MATCH_COLUMNS],
            f"`{item['verdict']}`",
            item["blocking_gap"],
        ]
        lines.append("| " + " | ".join(cell(value) for value in values) + " |")
    return "\n".join(lines)


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出判定表 Markdown。"""
    lines = ["| gate | closed | proved | meaning | remaining |", "| --- | --- | --- | --- | --- |"]
    for item in rows:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
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
    candidates = build_candidates()
    return {
        "certificate_type": "prime_matrix_fulls_nonap_wfd_theorem_match_matrix_router",
        "status": "fulls_nonap_wfd_primary_sources_screened_exact_contract_or_new_theorem_remains",
        "current_target_object": {
            "symbolic_form": "W_full(C,S,H)=sum_{c~C} lambda_c sum_{0<|h|<=H} omega_h sum_{s~S,(s,c)=1} beta_s e_c(a_h s + b_h bar{s})",
            "range": "X≈P^2, C≈P/log^O P, S≈P, 0<|h|<=H<=P/log^O P",
            "weights": "lambda well-factorable; beta divisor-bounded; omega smooth",
            "boundary": "non-AP, uncentered, no hidden projection, no AP-source lift",
            "required_strength": "NaturalWFDScale(C,S,H)/log^A P for every A>0",
        },
        "match_columns": MATCH_COLUMNS,
        "candidates": candidates,
        "gates": build_gates(),
        "next_direct_attack_target": (
            "FullSNonAPWFDKLSTheoremInput OR APSourceLift "
            "OR NCBLKActualBlockNonConcentration"
        ),
        "dependency_hashes": dependency_hashes,
        "plain_conclusion": (
            "逐项 theorem-match 后，现有 FI/DI/BFI/Maynard/普通短区间主来源均不能直接关闭 "
            "当前 full-S non-AP uncentered no-projection WFD 对象。FullS-KLS-ext 与当前对象逐项匹配，"
            "但只能作为新外部黑箱定理合同；若要求从主来源推出，仍需 DIBFIPrimarySourceSpecializationProof，"
            "等价地需要证明 FullSNonAPWFDKLSTheoremInput、APSourceLift 或实际 NC-BLK 非集中。"
        ),
    }


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 证书。"""
    target = payload["current_target_object"]
    lines = [
        "# Prime Matrix Full-S non-AP WFD theorem-match 矩阵证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 当前目标对象",
        "",
        "```text",
        f"object={target['symbolic_form']}",
        f"range={target['range']}",
        f"weights={target['weights']}",
        f"boundary={target['boundary']}",
        f"required_strength={target['required_strength']}",
        "```",
        "",
        "## 2. 外部定理逐项匹配矩阵",
        "",
        match_markdown(payload["candidates"]),
        "",
        "## 3. 判定表",
        "",
        rows_markdown(payload["gates"]),
        "",
        "## 4. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "当前直接主攻口为：",
        "",
        "```text",
        payload["next_direct_attack_target"],
        "```",
        "",
        "## 5. 候选来源与允许用法",
        "",
        "| source | allowed use | url |",
        "| --- | --- | --- |",
    ]
    for item in payload["candidates"]:
        lines.append(f"| {cell(item['name'])} | {cell(item['allowed_use'])} | {item['url']} |")
    lines.extend(
        [
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
                "candidate_count": len(payload["candidates"]),
                "ready_made_primary_source_match_found": False,
                "next_direct_attack_target": payload["next_direct_attack_target"],
                "outputs": [str(OUT_LEDGER), str(OUT_JSON), str(OUT_MD)],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
