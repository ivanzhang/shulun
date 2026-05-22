#!/usr/bin/env python3
"""生成两条替代线的终端硬攻证书。

用法示例：
  python3 experiments/prime_matrix_two_replacement_lines_terminal_attack_router.py
  python3 -m json.tool docs/monograph/prime-matrix-two-replacement-lines-terminal-attack-router.json

输出：
  data/prime-matrix-two-replacement-lines-terminal-attack-ledger.json
  docs/monograph/prime-matrix-two-replacement-lines-terminal-attack-router.json
  docs/monograph/prime-matrix-two-replacement-lines-terminal-attack-router.md
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

SLUG = "prime-matrix-two-replacement-lines-terminal-attack"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

DUAL_CLOSURE = DOCS / "prime-matrix-dual-closure-external-internal-hardpoint-router.json"
THEOREM_MATCH = DOCS / "prime-matrix-fulls-nonap-wfd-theorem-match-matrix-router.json"
TRUE_REMAINDER = DOCS / "prime-matrix-fulls-theorem-match-true-remainder-cut-router.json"
DSTRUCTURE_SPLIT = DOCS / "prime-matrix-dstructure-rankin-author-remainder-split-router.json"
DSTRUCTURE_ACCEPTANCE = DOCS / "prime-matrix-dstructure-rankin-promotion-acceptance-router.json"
RKS_COMPRESSED = DOCS / "prime-matrix-strict-dstructure-tail-rankin-replacement-compression-router.json"
RKS_HARDPOINT = DOCS / "prime-matrix-strict-self-contained-replacement-package-hardpoint-router.json"
STRICT_MAINLINE = DOCS / "prime-matrix-strict-mainline-self-contained-frontier-router.json"
CLAIM_STATUS = DOCS / "claim-status-table.md"
CONTRACTS = DOCS / "three-claims-actual-load-closure-contracts.md"
FRONTIER = DOCS / "three-claims-formal-to-actual-critical-load-frontier.md"
EXTERNAL_INDEX = DOCS / "external-theorem-index.md"


def read_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空证据。"""
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
    """列出证书依赖。"""
    return [
        DUAL_CLOSURE,
        THEOREM_MATCH,
        TRUE_REMAINDER,
        DSTRUCTURE_SPLIT,
        DSTRUCTURE_ACCEPTANCE,
        RKS_COMPRESSED,
        RKS_HARDPOINT,
        STRICT_MAINLINE,
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


EXACT_FULLS_TARGET = (
    "For every fixed A>0 and prime P large enough, prove the full-S non-AP WFD "
    "Kloosterman-large-sieve estimate for W_full(C,S,H) with C≈P/log^O(P), "
    "S≈P, H<=P/log^O(P), well-factorable lambda_c, divisor-bounded beta_s, "
    "smooth omega_h, c-dependent completed residue weights, no AP-source lift, "
    "no centering/projection loss, and saving NaturalWFDScale/log^A(P)."
)

RKS_LOG_TARGET = (
    "For prime modulus P and dyadic reciprocal variables m,n with divisor-bounded "
    "Vaughan/RKS coefficients and |I||J|>=P/log^A(P), prove a BG/RKS-type "
    "bilinear or multilinear reciprocal Kloosterman fixed log-saving for "
    "e_P(xi/(mn)), strong enough to leave the prior log^-44 budget after RKS "
    "losses; equivalently supply the log^-118 block used by the ledger."
)

FINE_SOURCE_PACKAGE = [
    "AlphaRowAnchorPhaseEmissionFormulaLedger",
    "IndependentNoncanonicalPreCauchyArithmeticIdentityStatementLedger",
    "SameUnitExactUVRankMultiplicityCertificateForPrimitiveKernelRows",
    "PhiLPFOffDiagonalOrderedSemiprimeFirstSeedSignedTableBeforePushforward",
    "PhiLPFInternalPrimeAdjoinSignedTransitionLawBeforePushforward",
    "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger",
    "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger",
    "RegisteredCompletePrimitiveEmitterKeyPartitionPolylogLedger",
    "FixedKeyExactUVLocalMultiplicityO1Ledger",
]


def theorem_match_rows() -> list[dict[str, Any]]:
    """外部无黑箱线的逐项 theorem-match 表。"""
    return [
        {
            "source": "BFI1986_Theorem10",
            "object": "AP discrepancy for primes/arithmetic functions in residue classes",
            "weights": "well-factorable modulus weights match only after AP-source formulation",
            "window": "large-moduli AP average, not full-S non-AP reciprocal window",
            "moduli_range": "strong AP range; object still AP",
            "smoothing_projection": "requires AP discrepancy and main-term subtraction",
            "error_saving": "log-power AP saving is available inside its hypotheses",
            "constant_strength": "sufficient for AP branch only",
            "matches_current_target": False,
            "blocking_gap": "APSourceLift is rejected for the current uncentered no-projection non-AP WFD object",
        },
        {
            "source": "DI_Kuznetsov_spectral_large_sieve",
            "object": "post-completion Kloosterman spectral average",
            "weights": "given coefficient vectors, not actual source emitter",
            "window": "phase/modulus/frequency template is close",
            "moduli_range": "spectral level can cover KLS-style averages after completion",
            "smoothing_projection": "completion/projection must already be justified",
            "error_saving": "large-sieve saving exists for matched completed forms",
            "constant_strength": "not yet transferred to arbitrary log^A full-S target",
            "matches_current_target": False,
            "blocking_gap": "c-dependent completed residue weights and no-projection de-completion are not a ready-made corollary",
        },
        {
            "source": "Maynard2020_and_2023_large_moduli_AP",
            "object": "AP distribution with well/triply-well-factorable weights",
            "weights": "very strong AP well-factorable weights",
            "window": "AP moduli beyond square-root barrier, not every sqrt row window",
            "moduli_range": "improves AP level of distribution",
            "smoothing_projection": "AP-source and residue-class framework",
            "error_saving": "AP mean-value saving",
            "constant_strength": "does not provide full-S non-AP KLS conclusion",
            "matches_current_target": False,
            "blocking_gap": "conclusion type remains AP distribution, not uncentered non-AP full-S WFD KLS",
        },
        {
            "source": "Friedlander_Iwaniec_parity_sensitive_model",
            "object": "special polynomial/parity-breaking sieve technology",
            "weights": "conceptual Type-II/parity-sensitive guidance",
            "window": "not the current CRT row top band",
            "moduli_range": "not a theorem for the current W_full",
            "smoothing_projection": "not applicable as a direct projection",
            "error_saving": "not a ready estimate for W_full",
            "constant_strength": "technology-class only",
            "matches_current_target": False,
            "blocking_gap": "model inspiration, not a theorem-match for full-S non-AP WFD",
        },
        {
            "source": "NewAutomorphicDispersionProof",
            "object": "exact W_full full-S non-AP WFD target",
            "weights": "must handle c-dependent completed residue weights",
            "window": "must cover C≈P/log^O(P), S≈P, H<=P/log^O(P)",
            "moduli_range": "prime-matrix top band P^2/sqrt-scale",
            "smoothing_projection": "must preserve no hidden projection and de-completion errors",
            "error_saving": "must prove NaturalWFDScale/log^A(P) for every fixed A",
            "constant_strength": "must survive downstream log-loss ledger",
            "matches_current_target": True,
            "blocking_gap": "not proved yet; this is the exact new theorem to write",
        },
    ]


def internal_rows() -> list[dict[str, Any]]:
    """内部自足线的压缩表。"""
    return [
        {
            "gate": "FineSignedSourcePackage",
            "closed": False,
            "proved": False,
            "meaning": "内部自足版仍需同一 formal unit 的 pre-Cauchy signed emitter 与 Phi-LPF signed tables。",
            "remaining": " AND ".join(FINE_SOURCE_PACKAGE),
        },
        {
            "gate": "DStructureFormalShell",
            "closed": True,
            "proved": True,
            "meaning": "D/AB Structured-EHPD 壳、有限验证和 Rankin pass-or-return 已可作为作者侧证据包处理。",
            "remaining": "analytic TL4-L/RKS-log core",
        },
        {
            "gate": "SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving",
            "closed": False,
            "proved": False,
            "meaning": "DStructure/Rankin 自足替代包的真正解析硬点已压到 BG/RKS-log 倒数 Kloosterman 固定对数节省。",
            "remaining": "SelfContainedProofOfMultilinearReciprocalKloostermanFixedLogSaving OR BakerFrequencyLargeSieveOrDBGAverageReplacement",
        },
        {
            "gate": "BakerSingleFrequencyShortcut",
            "closed": True,
            "proved": False,
            "meaning": "Baker 单频率素变量估计对象不同，不能替代 coherent d/frequency average。",
            "remaining": "prove averaged reciprocal Kloosterman theorem, not just pointwise prime-variable bound",
        },
        {
            "gate": "InternalSelfContainedRowColumnClosure",
            "closed": False,
            "proved": False,
            "meaning": "内部自足版必须同时关闭 source signed package 与 RKS-log/TL4-L 固定节省；当前没有无条件闭合。",
            "remaining": "FineSignedSourcePackage AND SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving",
        },
    ]


def external_proof_tasks() -> list[dict[str, Any]]:
    """新自守/dispersion 证明必须逐项完成的任务。"""
    return [
        {
            "task": "CompletionWithoutProjectionLoss",
            "closed": False,
            "detail": "把 actual full-S non-AP 对象完成到 Kloosterman 相位，同时证明中心化/投影误差不吞掉目标 log saving。",
        },
        {
            "task": "CDependentWeightSpectralLargeSieve",
            "closed": False,
            "detail": "证明 c-dependent completed residue weights 的 Kuznetsov/谱大筛平均抵消，而不是套用固定系数模板。",
        },
        {
            "task": "WellFactorableModulusTransferNonAP",
            "closed": False,
            "detail": "保持 well-factorable 模权，但不退回 APSourceLift 或 AP discrepancy。",
        },
        {
            "task": "DecompletionAndEndpointErrorBudget",
            "closed": False,
            "detail": "把完成型估计回传到原始 uncentered full-S 窗口，保存所有端点、粗糙截断和 CRT 误差。",
        },
        {
            "task": "ArbitraryLogSavingConstants",
            "closed": False,
            "detail": "给出任意固定 A 的 log^{-A} 节省，并记录足以穿过后续 loss ledger 的常数强度。",
        },
    ]


def build_payload() -> dict[str, Any]:
    """构造证书 payload。"""
    data = {
        "dual_closure": read_json(DUAL_CLOSURE),
        "theorem_match": read_json(THEOREM_MATCH),
        "true_remainder": read_json(TRUE_REMAINDER),
        "dstructure_split": read_json(DSTRUCTURE_SPLIT),
        "dstructure_acceptance": read_json(DSTRUCTURE_ACCEPTANCE),
        "rks_compressed": read_json(RKS_COMPRESSED),
        "rks_hardpoint": read_json(RKS_HARDPOINT),
        "strict_mainline": read_json(STRICT_MAINLINE),
    }
    return {
        "certificate_type": "prime_matrix_two_replacement_lines_terminal_attack_router",
        "status": "two_replacement_lines_pinned_external_primary_and_internal_rkslog_open",
        "row_column_unconditional_closed": False,
        "external_lemma_conditional_closure": {
            "closed_under_inputs": True,
            "inputs": [
                "AcceptedFullSKLSExtExternalContract",
                "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
            ],
            "unconditional_from_current_corpus": False,
        },
        "no_blackbox_external_line": {
            "closed": False,
            "exact_target": EXACT_FULLS_TARGET,
            "remaining": "ExactPrimarySourceFullSNonAPWFDKLSTheoremMatch OR NewAutomorphicDispersionProof",
            "theorem_match_rows": theorem_match_rows(),
            "new_proof_tasks": external_proof_tasks(),
        },
        "internal_self_contained_line": {
            "closed": False,
            "fine_source_package": FINE_SOURCE_PACKAGE,
            "dstructure_rankin_narrowest_atom": "SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving",
            "rks_log_target": RKS_LOG_TARGET,
            "rows": internal_rows(),
        },
        "attack_conclusion": (
            "两条替代线已经压到可核查终端：无黑箱外部线必须逐项证明 exact full-S "
            "non-AP WFD KLS 定理，或写出新的自守/dispersion 证明；内部自足线必须同时证明 "
            "FineSignedSourcePackage 与 Tail-log4/RKS-log 倒数 Kloosterman 固定对数节省。"
            "外部引理版只在接受 FullS-KLS-ext 和 DStructure/Rankin 独立验收时条件闭合；当前语料库仍未无条件闭合。"
        ),
        "source_status_snapshot": {
            "dual_closure_status": data["dual_closure"].get("status"),
            "theorem_match_status": data["theorem_match"].get("status"),
            "true_remainder_status": data["true_remainder"].get("status"),
            "dstructure_split_status": data["dstructure_split"].get("status"),
            "rks_compressed_status": data["rks_compressed"].get("status"),
            "rks_hardpoint_status": data["rks_hardpoint"].get("status"),
            "strict_mainline_status": data["strict_mainline"].get("status"),
        },
        "source_hashes": source_hashes(),
    }


def rows_markdown(rows: list[dict[str, Any]]) -> str:
    """输出通用 Markdown 表。"""
    lines = [
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
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


def theorem_match_markdown(rows: list[dict[str, Any]]) -> str:
    """输出 theorem-match Markdown 表。"""
    lines = [
        "| source | object | weights | window | moduli range | smoothing/projection | saving | constants | match | blocking gap |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            "| {source} | {object} | {weights} | {window} | {moduli} | {projection} | {saving} | {constants} | `{match}` | {gap} |".format(
                source=cell(item["source"]),
                object=cell(item["object"]),
                weights=cell(item["weights"]),
                window=cell(item["window"]),
                moduli=cell(item["moduli_range"]),
                projection=cell(item["smoothing_projection"]),
                saving=cell(item["error_saving"]),
                constants=cell(item["constant_strength"]),
                match=fmt_bool(item["matches_current_target"]),
                gap=cell(item["blocking_gap"]),
            )
        )
    return "\n".join(lines)


def task_markdown(rows: list[dict[str, Any]]) -> str:
    """输出任务表。"""
    lines = [
        "| task | closed | detail |",
        "| --- | --- | --- |",
    ]
    for item in rows:
        lines.append(
            f"| {cell(item['task'])} | `{fmt_bool(item['closed'])}` | {cell(item['detail'])} |"
        )
    return "\n".join(lines)


def build_markdown(payload: dict[str, Any]) -> str:
    """生成 Markdown 文档。"""
    external = payload["no_blackbox_external_line"]
    internal = payload["internal_self_contained_line"]
    lines = [
        "# Prime Matrix 两条替代线终端硬攻证书",
        "",
        f"**状态：** `{payload['status']}`",
        "",
        "## 1. 总结",
        "",
        payload["attack_conclusion"],
        "",
        "```text",
        "external lemma conditional package:",
        "AcceptedFullSKLSExtExternalContract AND DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance",
        "",
        "no-blackbox external remainder:",
        external["remaining"],
        "",
        "internal self-contained remainder:",
        "FineSignedSourcePackage AND SelfContainedTailLog4RKSLogReciprocalKloostermanFixedSaving",
        "",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 2. 无黑箱外部主来源线",
        "",
        "精确定理目标：",
        "",
        "```text",
        external["exact_target"],
        "```",
        "",
        theorem_match_markdown(external["theorem_match_rows"]),
        "",
        "新自守/dispersion 证明必须补齐：",
        "",
        task_markdown(external["new_proof_tasks"]),
        "",
        "## 3. 内部自足线",
        "",
        "DStructure/Rankin 自足替代包的最窄解析原子：",
        "",
        "```text",
        internal["dstructure_rankin_narrowest_atom"],
        "```",
        "",
        "精确定理目标：",
        "",
        "```text",
        internal["rks_log_target"],
        "```",
        "",
        rows_markdown(internal["rows"]),
        "",
        "FineSignedSourcePackage 展开：",
        "",
        "```text",
        " AND ".join(internal["fine_source_package"]),
        "```",
        "",
        "## 4. 状态快照",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in payload["source_status_snapshot"].items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend(
        [
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
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
