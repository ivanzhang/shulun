#!/usr/bin/env python3
"""生成 DStructure/Rankin 作者侧剩余拆分证书。

用法示例：
  python3 experiments/prime_matrix_dstructure_rankin_author_remainder_split_router.py
  python3 -m json.tool docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json

输出：
  data/prime-matrix-dstructure-rankin-author-remainder-split-ledger.json
  docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.json
  docs/monograph/prime-matrix-dstructure-rankin-author-remainder-split-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"
PAPER = ROOT / "paper" / "contradiction-field-monograph" / "contradiction-field-monograph.tex"

SLUG = "prime-matrix-dstructure-rankin-author-remainder-split"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

AUTHOR_COMPLETION = DOCS / "prime-matrix-author-side-closure-task-completion-router.json"
DSTRUCTURE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
FINAL_GUARD = DOCS / "prime-matrix-final-guard-gate-completion-verdict-router.json"
DUAL_CLOSURE = DOCS / "prime-matrix-dual-closure-external-internal-hardpoint-router.json"
K_LESS_P = DOCS / "prime-matrix-k-less-p-endpoint-correction-author-residue-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时登记为空证据。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """格式化布尔值。"""
    return "true" if bool(value) else "false"


def cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def dependency_paths() -> list[Path]:
    """列出依赖文件。"""
    return [
        AUTHOR_COMPLETION,
        DSTRUCTURE,
        FINAL_GUARD,
        DUAL_CLOSURE,
        K_LESS_P,
        CLAIM_STATUS,
        CONTRACTS,
        FRONTIER,
        EXTERNAL_INDEX,
        PAPER,
    ]


def source_hashes() -> dict[str, str]:
    """登记脚本和依赖哈希。"""
    paths = [Path(__file__).resolve(), *dependency_paths()]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def row(
    gate: str,
    author_side: str,
    closed: bool,
    proves_unconditional: bool,
    meaning: str,
    next_action: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "author_side": author_side,
        "closed": closed,
        "proves_unconditional": proves_unconditional,
        "meaning": meaning,
        "next_action": next_action,
    }


SELF_CONTAINED_SUBPACKAGES = [
    "SelfContainedDStructureStructuredEHPDDefinitionsAndABReductionProof",
    "SelfContainedTailLog4BGOrRKSTailAdapterWithExactTheoremNumbersAndConstants",
    "ReproducibleFiniteVerificationArchiveWithHashesAndIndependentRunner",
    "SelfContainedFullRankinPassOrReturnLedgerAndDownstreamReturnIntegration",
]


def build_rows(data: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    """生成作者侧/非作者侧拆分行。"""
    final_guard = data["final_guard"]
    dstructure = data["dstructure"]
    author = data["author_completion"]
    return [
        row(
            "ExternalLemmaOrdinaryAuthorRemainder",
            "none",
            author.get("author_side_completable_tasks_done") is True
            or final_guard.get("author_side_completable_tasks_done") is True,
            False,
            "外部 FullS-KLS 合同版中，作者侧可合法补齐的条件链和证据包已经封装。",
            "do not add hidden author-side obligations; preserve the external/referee gate",
        ),
        row(
            "DStructureRankinIndependentAcceptance",
            "not author-completable",
            dstructure.get("promotion_package_boundary_closed") is True,
            dstructure.get("promotion_package_independently_accepted") is True,
            "DStructure/Tail-log4/finite Rankin 晋级包边界闭合，但独立接受事件仍缺席。",
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        ),
        row(
            "AuthorCanOnlyReplaceGateBySelfContainedProof",
            "open self-contained replacement",
            final_guard.get("self_contained_promotion_package_proved") is True,
            final_guard.get("self_contained_promotion_package_proved") is True,
            "作者侧若要绕开独立接受，只能提交完整自足替代证明包，不能用自审归档替代外审。",
            "SelfContainedDStructureTailLog4FiniteRankinProofPackage",
        ),
        row(
            "DStructureStructuredEHPDReductionSubpackage",
            "open",
            False,
            False,
            "需要把 D-structure 定义、Structured-EHPD 入口、A/B 到 D 的归约从验收接口升级为文内证明。",
            SELF_CONTAINED_SUBPACKAGES[0],
        ),
        row(
            "TailLog4ExternalAdapterSubpackage",
            "open",
            False,
            False,
            "需要给出 Tail-log4 所用 BG/RKS 或替代定理的精确定理号、常数、变量 convention 与适配证明。",
            SELF_CONTAINED_SUBPACKAGES[1],
        ),
        row(
            "FiniteVerificationArchiveSubpackage",
            "open",
            False,
            False,
            "需要把阈值以下有限验证归档为可复现实验包，含脚本哈希、输入域、输出证书和独立 runner。",
            SELF_CONTAINED_SUBPACKAGES[2],
        ),
        row(
            "FullRankinPassOrReturnSubpackage",
            "open",
            False,
            False,
            "需要把 Rankin 全账本的 pass-or-return 与失败回流逐项写成自足证明，而不是可审查清单。",
            SELF_CONTAINED_SUBPACKAGES[3],
        ),
        row(
            "NoBlackboxExternalAuthorRoute",
            "open",
            False,
            False,
            "若不接受 FullS-KLS-ext 黑箱合同，作者侧必须精确匹配主来源定理，或给出新的自守/dispersion 证明。",
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof",
        ),
        row(
            "CurrentCorpusUnconditionalPromotion",
            "blocked",
            False,
            False,
            "当前语料库不能删除 DStructure/Rankin 独立验收条件，也不能把 strict Phi-LPF 端点差当正性证明。",
            "external acceptance or full self-contained replacement package",
        ),
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "author_completion": read_json(AUTHOR_COMPLETION),
        "dstructure": read_json(DSTRUCTURE),
        "final_guard": read_json(FINAL_GUARD),
        "dual_closure": read_json(DUAL_CLOSURE),
        "k_less_p": read_json(K_LESS_P),
    }
    rows = build_rows(data)
    return {
        "certificate_type": "prime_matrix_dstructure_rankin_author_remainder_split_router",
        "status": "dstructure_rankin_author_remainder_split_closed_self_contained_replacement_open",
        "external_lemma_author_side_remaining": [],
        "external_lemma_non_author_remaining": [
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"
        ],
        "no_blackbox_external_author_remaining": [
            "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof"
        ],
        "self_contained_author_replacement_subpackages": SELF_CONTAINED_SUBPACKAGES,
        "self_contained_author_replacement_package": (
            " AND ".join(SELF_CONTAINED_SUBPACKAGES)
        ),
        "row_column_unconditional_closed": False,
        "plain_conclusion": (
            "外部 FullS-KLS 合同版的作者侧普通任务已经归零；剩余的 "
            "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance 是非作者侧独立接受事件。"
            "作者侧若要继续推进，只能走两条替代线：无黑箱外部主来源版需要精确 theorem-match "
            "或新的自守/dispersion 证明；内部自足版需要把 D-structure 归约、Tail-log4 适配、"
            "有限验证归档和 Rankin pass-or-return 全部升级成文内自足证明包。"
        ),
        "rows": rows,
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 Markdown 表格。"""
    lines = [
        "| gate | author side | closed | proves unconditional | meaning | next action |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {gate} | {author_side} | `{closed}` | `{proves}` | {meaning} | {next_action} |".format(
                gate=cell(item["gate"]),
                author_side=cell(item["author_side"]),
                closed=fmt_bool(item["closed"]),
                proves=fmt_bool(item["proves_unconditional"]),
                meaning=cell(item["meaning"]),
                next_action=cell(item["next_action"]),
            )
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    lines = [
        "# Prime Matrix DStructure/Rankin 作者侧剩余拆分",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 结论",
        "",
        payload["plain_conclusion"],
        "",
        "```text",
        "external_lemma_author_side_remaining=none",
        "external_lemma_non_author_remaining=DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 判定表",
        "",
        rows_markdown(payload["rows"]),
        "",
        "## 3. 作者侧可继续完成的替代包",
        "",
        "无黑箱外部主来源版：",
        "",
        "```text",
        *payload["no_blackbox_external_author_remaining"],
        "```",
        "",
        "内部自足版 DStructure/Rankin 替代包：",
        "",
        "```text",
        *payload["self_contained_author_replacement_subpackages"],
        "```",
        "",
        "合取形式：",
        "",
        "```text",
        payload["self_contained_author_replacement_package"],
        "```",
        "",
        "## 4. 依赖哈希",
        "",
        "| file | sha256 |",
        "| --- | --- |",
    ]
    for path, digest in sorted(payload["source_hashes"].items()):
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
