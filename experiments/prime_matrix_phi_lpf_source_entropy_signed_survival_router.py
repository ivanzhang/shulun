#!/usr/bin/env python3
"""生成 Phi-LPF 候选支撑到 signed-survival 熵缺口的桥接证书。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_source_entropy_signed_survival_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-source-entropy-signed-survival-router.json

输出：
  data/prime-matrix-phi-lpf-source-entropy-signed-survival-ledger.json
  docs/monograph/prime-matrix-phi-lpf-source-entropy-signed-survival-router.json
  docs/monograph/prime-matrix-phi-lpf-source-entropy-signed-survival-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-source-entropy-signed-survival"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SOURCE_ENTROPY_CERT = DOCS / "prime-matrix-strict-actual-source-domain-entropy-atom-router.json"
PHI_LPF_CERT = DOCS / "prime-matrix-phi-recursive-lpf-ownership-router.json"
LPF_CANDIDATE_CERT = DOCS / "prime-matrix-lpf-candidate-row-map-alpha-rule-router.json"
SEED_EMITTER_CERT = DOCS / "prime-matrix-strict-acyclic-seed-signed-row-emitter-router.json"
SIGNED_WEIGHT_CERT = DOCS / "prime-matrix-strict-pointwise-signed-alpha-weight-formula-router.json"
NEW_PAYLOAD_BRIDGE_CERT = DOCS / "prime-matrix-phi-lpf-new-payload-source-atom-alignment-sync-router.json"

SOURCE_ENTROPY = "ActualPreCauchySourceDomainAbsoluteEntropyLedger"
ENTROPY_PACKAGE = "ActualPreCauchySourceDomainEntropyFromSignedRowsAndRowMassLedger"
SIGNED_LAW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
ROW_SUPPORT = "PrimitiveRowSupportLowerBoundBeforeExactUVProjectionLedger"
PHI_CANDIDATE_CAPACITY = "PhiLPFCandidateRowCapacityLowerBoundLedger"
SIGNED_SURVIVAL = "NonzeroSignedRowSurvivalOnPhiLPFSupportBeforePushforward"
SIGNED_EXPR = "ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
COMPLETE_KEY = "CompletePrimitiveEmitterKeyPartitionLedger"
FIXED_KEY_MULT = "FixedKeyExactUVLocalMultiplicityO1Ledger"
TERMINAL_DESCENT = "AcyclicNoncanonicalTerminalReturnWellFoundedDescentCertificate"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
EXACTUV_PAIR = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象，避免把缺失当证明。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值格式化为小写文本。"""
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


def source_hashes() -> dict[str, str]:
    """汇总本证书依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SOURCE_ENTROPY_CERT,
        PHI_LPF_CERT,
        LPF_CANDIDATE_CERT,
        SEED_EMITTER_CERT,
        SIGNED_WEIGHT_CERT,
        NEW_PAYLOAD_BRIDGE_CERT,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def sample_capacity_audit(phi_lpf: dict[str, Any]) -> list[dict[str, Any]]:
    """从 Phi-LPF 证书抽取候选容量样本。"""
    samples: list[dict[str, Any]] = []
    for item in phi_lpf.get("sample_audit", []):
        samples.append(
            {
                "N": item["N"],
                "sqrt_floor": item["sqrt_floor"],
                "phi_lpf_candidate_rows": item["bucket_sum_from_phi"],
                "composite_count": item["composite_count"],
                "prime_count": item["prime_count"],
                "pi_from_phi": item["pi_from_phi"],
                "candidate_capacity_identity_closed": (
                    item["lpf_bucket_sum_identity_holds"]
                    and item["prime_count_identity_holds"]
                    and item["phi_recursion_identity_holds_on_buckets"]
                    and item["phi_recursive_matches_direct_rough_count"]
                ),
                "actual_nonzero_signed_rows_known": False,
            }
        )
    return samples


def split_atoms() -> list[dict[str, str]]:
    """列出从候选容量到 actual signed entropy 的必要分裂。"""
    return [
        {
            "atom": PHI_CANDIDATE_CAPACITY,
            "status": "closed_unsigned",
            "role": "由 LPF 唯一 ownership 与 Phi 递推支付候选 row 容量；只说明可发射位置有多少。",
        },
        {
            "atom": SIGNED_SURVIVAL,
            "status": "open_signed",
            "role": "证明足够多候选 row 在同一 formal unit 中获得非零 signed weight，且没有局部因子归零或命名回流。",
        },
        {
            "atom": ROW_MASS,
            "status": "open_signed",
            "role": "在存活 signed rows 上证明总质量、单行上界、L2/no-heavy-row 与零权重回流。",
        },
        {
            "atom": SIGNED_EXPR,
            "status": "open_formula",
            "role": "给出每条 actual noncanonical primitive summand 的推前前 signed coefficient 表达式。",
        },
    ]


def build_rows(
    source_entropy: dict[str, Any],
    phi_lpf: dict[str, Any],
    lpf_candidate: dict[str, Any],
    seed_emitter: dict[str, Any],
    signed_weight: dict[str, Any],
    new_payload_bridge: dict[str, Any],
    samples: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """生成 source entropy signed-survival 判定表。"""
    samples_ok = bool(samples) and all(item["candidate_capacity_identity_closed"] for item in samples)
    return [
        row(
            "SourceEntropyAtomImported",
            source_entropy.get("terminal_gap_after_router") == ENTROPY_PACKAGE,
            False,
            "source-domain entropy 已被拆成 signed row emitter、row-mass normalization 与 primitive row support 下界。",
            ENTROPY_PACKAGE,
        ),
        row(
            "PhiRecursiveLPFOwnershipImported",
            phi_lpf.get("phi_recursive_lpf_bucket_formula_proved") is True
            and phi_lpf.get("prime_count_identity_from_phi_lpf_proved") is True,
            True,
            "LPF/Phi 桶恒等式已闭合：每个候选合数 row 有唯一 LPF owner，桶容量由 Phi(floor(N/p),p)-1 给出。",
            PHI_CANDIDATE_CAPACITY,
        ),
        row(
            "LPFCandidateRowMapImported",
            lpf_candidate.get("lpf_candidate_row_emission_map_closed") is True,
            True,
            "LPF ownership 已支付 alpha 侧候选 row 的非后验索引，并与 unsigned skeleton 兼容。",
            PHI_CANDIDATE_CAPACITY,
        ),
        row(
            "CandidateCapacityAuditClosed",
            samples_ok,
            True,
            "样本审计只验证 Phi-LPF 候选容量恒等式；它不是全局 signed 支撑证明。",
            PHI_CANDIDATE_CAPACITY,
        ),
        row(
            "CandidateRowsAreNotActualSignedRows",
            phi_lpf.get("primitive_summand_signed_weight_expression_proved") is False
            and lpf_candidate.get("lpf_candidate_map_not_signed_primitive_map") is True,
            True,
            "候选 row 只有 owner/capacity/geometry，没有 signed weight、local factor、orientation 或 alpha/delta side。",
            SIGNED_SURVIVAL,
        ),
        row(
            "SeedEmitterStillNeedsSignedLaw",
            seed_emitter.get("next_direct_attack_target") == SIGNED_LAW,
            False,
            "合法 seed 分支仍需逐 primitive row 的 signed coefficient law，才能把候选 row 转成 actual signed row。",
            SIGNED_LAW,
        ),
        row(
            "SignedExpressionStillOpen",
            signed_weight.get("next_direct_attack_target") == SIGNED_EXPR
            and signed_weight.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "逐行 signed weight formula 的最窄点是 actual primitive summand signed expression before pushforward。",
            SIGNED_EXPR,
        ),
        row(
            "RowSupportSplitClosed",
            samples_ok,
            False,
            "primitive row support 下界可分成已闭合的候选容量与仍开放的非零 signed survival。",
            f"{PHI_CANDIDATE_CAPACITY} AND {SIGNED_SURVIVAL}",
        ),
        row(
            "RowMassStillIndependent",
            source_entropy.get("same_formal_unit_row_mass_normalization_proved") is False,
            False,
            "即使 signed rows 存活，仍需同一表内 row-mass normalization/no-heavy-row 账本。",
            ROW_MASS,
        ),
        row(
            "NewPayloadBridgeConsistent",
            new_payload_bridge.get("next_primary_attack_target") == SOURCE_ENTROPY,
            False,
            "上一层 new-payload 桥接把首攻点压到 source-domain absolute entropy，本步给出其 LPF/Phi 支撑切分。",
            SOURCE_ENTROPY,
        ),
        row(
            "PointwisePhiLPFTableStillAlternative",
            phi_lpf.get("primitive_summand_signed_weight_expression_proved") is False,
            False,
            "若不走 signed summand 表达式，只能提交逐点 Phi-LPF signed coefficient value table。",
            POINTWISE_TABLE,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只关闭无符号候选容量和 signed-survival 的边界，不证明 signed 表达式、row-mass、complete key、fixed-key multiplicity 或最终晋级门。",
            f"{SIGNED_EXPR} AND {SIGNED_SURVIVAL} AND {ROW_MASS}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """组装 Phi-LPF source entropy signed-survival 证书。"""
    source_entropy = load_json(SOURCE_ENTROPY_CERT)
    phi_lpf = load_json(PHI_LPF_CERT)
    lpf_candidate = load_json(LPF_CANDIDATE_CERT)
    seed_emitter = load_json(SEED_EMITTER_CERT)
    signed_weight = load_json(SIGNED_WEIGHT_CERT)
    new_payload_bridge = load_json(NEW_PAYLOAD_BRIDGE_CERT)
    samples = sample_capacity_audit(phi_lpf)
    rows = build_rows(
        source_entropy=source_entropy,
        phi_lpf=phi_lpf,
        lpf_candidate=lpf_candidate,
        seed_emitter=seed_emitter,
        signed_weight=signed_weight,
        new_payload_bridge=new_payload_bridge,
        samples=samples,
    )
    latest_basis = (
        f"({SIGNED_EXPR} AND {SIGNED_SURVIVAL} AND {ROW_MASS}) "
        f"OR {POINTWISE_TABLE} OR {TERMINAL_DESCENT} OR {PDEC_SCOPE}; "
        f"parallel: {COMPLETE_KEY} AND {FIXED_KEY_MULT} AND {EXACTUV_PAIR} AND {DSTRUCTURE}"
    )
    return {
        "certificate_type": "prime_matrix_phi_lpf_source_entropy_signed_survival_router",
        "status": "phi_lpf_candidate_capacity_closed_signed_survival_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "frontier_sync_only": True,
        "finite_evidence_not_used_as_global_proof": True,
        "phi_lpf_candidate_capacity_ledger_closed": any(
            item["gate"] == "PhiRecursiveLPFOwnershipImported" and item["closed"] for item in rows
        ),
        "lpf_candidate_row_map_closed": any(
            item["gate"] == "LPFCandidateRowMapImported" and item["closed"] for item in rows
        ),
        "candidate_capacity_audit_closed": any(
            item["gate"] == "CandidateCapacityAuditClosed" and item["closed"] for item in rows
        ),
        "candidate_rows_are_actual_signed_rows": False,
        "nonzero_signed_row_survival_proved": False,
        "actual_noncanonical_primitive_summand_signed_weight_expression_proved": False,
        "same_formal_unit_row_mass_normalization_proved": False,
        "source_domain_absolute_entropy_proved": False,
        "row_column_unconditional_closed": False,
        "target_input_before_router": SOURCE_ENTROPY,
        "support_subatom_before_router": ROW_SUPPORT,
        "support_subatom_after_router": f"{PHI_CANDIDATE_CAPACITY} AND {SIGNED_SURVIVAL}",
        "next_primary_attack_target": SIGNED_EXPR,
        "parallel_attack_targets": [
            SIGNED_SURVIVAL,
            ROW_MASS,
            SIGNED_LAW,
            POINTWISE_TABLE,
            COMPLETE_KEY,
            FIXED_KEY_MULT,
            EXACTUV_PAIR,
            DSTRUCTURE,
        ],
        "split_atoms": split_atoms(),
        "sample_capacity_audit": samples,
        "gates": rows,
        "latest_retained_basis_after_router": latest_basis,
        "source_hashes": source_hashes(),
        "plain_conclusion": (
            "本步把 source-domain entropy 中的 primitive row support 下界切成两层："
            "LPF/Phi 递推已经关闭无符号候选 row 容量，但候选 row 不是 actual signed row。"
            "要把候选容量变成源域绝对熵，仍需证明 Phi-LPF 支撑上足够多行获得非零 signed weight，"
            "并给出同一 formal unit 的 row-mass/no-heavy-row 账本。最新直接硬点因此压到 "
            "`ActualNoncanonicalPrimitiveSummandSignedWeightExpressionBeforePushforward`；"
            "行/列命题仍未无条件闭合。"
        ),
    }


def render_markdown(cert: dict[str, Any]) -> str:
    """渲染 Markdown 报告。"""
    lines = [
        "# Prime Matrix Phi-LPF source entropy signed-survival 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"phi_lpf_candidate_capacity_ledger_closed={fmt_bool(cert['phi_lpf_candidate_capacity_ledger_closed'])}",
        f"lpf_candidate_row_map_closed={fmt_bool(cert['lpf_candidate_row_map_closed'])}",
        f"candidate_capacity_audit_closed={fmt_bool(cert['candidate_capacity_audit_closed'])}",
        f"candidate_rows_are_actual_signed_rows={fmt_bool(cert['candidate_rows_are_actual_signed_rows'])}",
        f"nonzero_signed_row_survival_proved={fmt_bool(cert['nonzero_signed_row_survival_proved'])}",
        f"actual_noncanonical_primitive_summand_signed_weight_expression_proved={fmt_bool(cert['actual_noncanonical_primitive_summand_signed_weight_expression_proved'])}",
        f"same_formal_unit_row_mass_normalization_proved={fmt_bool(cert['same_formal_unit_row_mass_normalization_proved'])}",
        f"source_domain_absolute_entropy_proved={fmt_bool(cert['source_domain_absolute_entropy_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        f"next_primary_attack_target={cert['next_primary_attack_target']}",
        "```",
        "",
        "## 1. 支撑切分",
        "",
        "切分前：",
        "",
        "```text",
        cert["support_subatom_before_router"],
        "```",
        "",
        "切分后：",
        "",
        "```text",
        cert["support_subatom_after_router"],
        "```",
        "",
        "| atom | status | role |",
        "| --- | --- | --- |",
    ]
    for item in cert["split_atoms"]:
        lines.append(f"| `{cell(item['atom'])}` | `{cell(item['status'])}` | {cell(item['role'])} |")
    lines.extend(
        [
            "",
            "## 2. Phi-LPF 候选容量样本",
            "",
            "| N | sqrt floor | Phi-LPF candidate rows | composites | pi from Phi | pi(N) | capacity identity | actual nonzero signed rows known |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for item in cert["sample_capacity_audit"]:
        lines.append(
            f"| {item['N']} | {item['sqrt_floor']} | {item['phi_lpf_candidate_rows']} | "
            f"{item['composite_count']} | {item['pi_from_phi']} | {item['prime_count']} | "
            f"`{fmt_bool(item['candidate_capacity_identity_closed'])}` | "
            f"`{fmt_bool(item['actual_nonzero_signed_rows_known'])}` |"
        )
    lines.extend(
        [
            "",
            "## 3. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in cert["gates"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | {cell(item['remaining'])} |"
        )
    lines.extend(
        [
            "",
            "## 4. 最新保留基",
            "",
            "```text",
            cert["latest_retained_basis_after_router"],
            "```",
            "",
            "下一直接主攻：",
            "",
            "```text",
            cert["next_primary_attack_target"],
            "```",
            "",
            "并行出口：",
            "",
            "```text",
            "\n".join(cert["parallel_attack_targets"]),
            "```",
            "",
            "行/列命题仍未无条件闭合。",
            "",
            "## 5. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{cell(path)}` | `{digest}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """写出 source entropy signed-survival 桥接证书。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True)
    OUT_LEDGER.write_text(text + "\n", encoding="utf-8")
    OUT_JSON.write_text(text + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(cert), encoding="utf-8")
    print(OUT_LEDGER.relative_to(ROOT))
    print(OUT_JSON.relative_to(ROOT))
    print(OUT_MD.relative_to(ROOT))


if __name__ == "__main__":
    main()
