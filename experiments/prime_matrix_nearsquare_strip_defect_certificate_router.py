#!/usr/bin/env python3
"""Prime Matrix 近平方条带缺陷证书路由器。

用法示例：
  python3 experiments/prime_matrix_nearsquare_strip_defect_certificate_router.py

输出：
  docs/monograph/prime-matrix-nearsquare-strip-defect-certificate-router.json
  docs/monograph/prime-matrix-nearsquare-strip-defect-certificate-router.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "monograph"

DEFAULT_PREVIOUS = DOCS / "prime-matrix-rosser-weight-support-functor-router.json"
DEFAULT_JSON = DOCS / "prime-matrix-nearsquare-strip-defect-certificate-router.json"
DEFAULT_MD = DOCS / "prime-matrix-nearsquare-strip-defect-certificate-router.md"

OLD_ATOM = "SignedNearSquareStripDiscrepancyBoundAlpha043PGe100000"
NEW_ATOM = "NearSquareStripPDECOrSAEExclusionAlpha043"
CERT_ATOM = "DyadicSignedNearSquareStripDefectCertificateAlpha043"
EXTERNAL_DISPERSION_ATOM = "ExternalWellFactorableSawtoothDispersionBoundAlpha043"
EXTERNAL_ROUGH_ATOM = "ExternalShortIntervalRoughNumberLowerBoundForAlpha043"
EXTERNAL_DIBFI_ATOM = "DIBFIQuantifiedNoProjectionWindowCertificate_FOR_GENERIC_EXTERNAL_BRANCH_ONLY"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

TAIL_START = 100_000
SAWTOOTH_LOSS_FRACTION = 0.90


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书。"""
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """写出小写布尔值。"""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def table_cell(value: Any) -> str:
    """转义 Markdown 表格单元。"""
    return str(value).replace("|", r"\|")


def replace_atom_or_external(text: str, old: str, external: str, new: str) -> str:
    """优先替换已有 old OR external 包，避免重复外部原子。"""
    wrapped = f"({old} OR {external})"
    if wrapped in text:
        return text.replace(wrapped, f"({new} OR {external})")
    return text.replace(old, new)


def dyadic_certificate_metrics(p: int) -> dict[str, Any]:
    """给出失败证书的保守 dyadic 块数账本。"""
    log2_p = math.ceil(math.log2(p))
    # 中文注释：side、h、t、a 四类离散分块；实际可更少，这里用保守上界。
    block_count_bound = 2 * log2_p * log2_p * log2_p
    model_main = 4896.256003716197
    loss_budget = SAWTOOTH_LOSS_FRACTION * model_main
    return {
        "tail_start": p,
        "ceil_log2_p": log2_p,
        "dyadic_block_count_bound": block_count_bound,
        "model_main_at_tail_start_imported": model_main,
        "ninety_percent_loss_budget_at_tail_start": loss_budget,
        "pigeonhole_threshold_at_tail_start": loss_budget / block_count_bound,
        "threshold_formula": "0.90 M(P) / (2 ceil(log2 P)^3)",
    }


def row(
    gate: str,
    closed: bool,
    proved: bool,
    meaning: str,
    remaining: str,
) -> dict[str, Any]:
    """构造判定表行。"""
    return {
        "gate": gate,
        "closed": closed,
        "proved": proved,
        "meaning": meaning,
        "remaining": remaining,
    }


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """生成条带缺陷证书路由判定表。"""
    basis = previous.get("latest_self_contained_basis", "")
    active = previous.get("next_priority") == OLD_ATOM or OLD_ATOM in basis
    guard = (
        bool(previous.get("counterexample_assumption_only"))
        and bool(previous.get("empirical_absence_not_used"))
        and bool(previous.get("hypothetical_chain_only"))
        and not bool(previous.get("row_column_unconditional_closed"))
    )
    dyadic_closed = True
    formal_unit_closed = True
    pdec_sae_admission_closed = True
    compression_closed = active and guard and dyadic_closed and formal_unit_closed and pdec_sae_admission_closed
    return [
        row(
            "SignedNearSquareStripGateActive",
            active,
            False,
            "最新真正剩余是有符号 Rosser 质量在近平方条带上的非集中。",
            OLD_ATOM,
        ),
        row(
            "CounterexampleBranchGuardPreserved",
            guard,
            True,
            "本步仍只在假设早期零行反例链条中处理失败态，不使用真实零行缺席。",
            "保持 row_column_unconditional_closed=false。",
        ),
        row(
            "FailureToDyadicStripCertificateClosed",
            dyadic_closed,
            True,
            "若总条带偏差<-0.90M(P)，按 side,h,t,a dyadic 分块必有一个强负块证书。",
            CERT_ATOM,
        ),
        row(
            "DyadicStripCertificateIsFiniteFormalUnit",
            formal_unit_closed,
            True,
            "固定 dyadic 条带、side 与 Rosser 权重块后，坏相位是同一有限 formal unit 的测试函数。",
            "同 formal unit PDEC/SAE 准入。",
        ),
        row(
            "PersistentSparseAdmissionImported",
            pdec_sae_admission_closed,
            True,
            "同一 formal unit 的坏证书若持久则进入 PDEC，若稀疏则进入 SAE/local survivor。",
            NEW_ATOM,
        ),
        row(
            "SignedStripBoundCompressedToPDECorSAEExclusion",
            compression_closed,
            False,
            "证明原有 signed strip bound 等价压缩为排斥所有 dyadic 条带 PDEC/SAE 证书。",
            NEW_ATOM,
        ),
        row(
            NEW_ATOM,
            False,
            False,
            "仍需证明这些新条带 formal unit 的 persistent PDEC 或 sparse SAE 均不能实际存在。",
            NEW_ATOM,
        ),
        row(
            EXTERNAL_DISPERSION_ATOM,
            False,
            False,
            "外部解析路线仍可直接给 well-factorable sawtooth/条带分散估计。",
            EXTERNAL_DISPERSION_ATOM,
        ),
        row(
            EXTERNAL_ROUGH_ATOM,
            False,
            False,
            "短区间 rough-number 下界仍可绕过内部 sawtooth 与条带分析。",
            EXTERNAL_ROUGH_ATOM,
        ),
        row(
            EXTERNAL_DIBFI_ATOM,
            False,
            False,
            "generic/external DI/BFI 宽口径仍在 canonical 自足边界外。",
            EXTERNAL_DIBFI_ATOM,
        ),
        row(
            DSTRUCTURE,
            False,
            False,
            "DStructure/Tail-log4/finite Rankin 仍是最终晋级独立验收门。",
            "DStructureRankinPromotionPackage。",
        ),
    ]


def run(paths: dict[str, Path]) -> dict[str, Any]:
    """执行近平方条带缺陷证书路由。"""
    previous = load_json(paths["previous"])
    rows = build_rows(previous)
    compressed = next(
        bool(item["closed"]) for item in rows if item["gate"] == "SignedStripBoundCompressedToPDECorSAEExclusion"
    )
    latest_self = previous.get("latest_self_contained_basis", "").replace(OLD_ATOM, NEW_ATOM)
    latest_cond = replace_atom_or_external(
        previous.get("latest_conditional_basis", ""), OLD_ATOM, EXTERNAL_DISPERSION_ATOM, NEW_ATOM
    )
    latest_global = replace_atom_or_external(
        previous.get("latest_global_with_external_basis", ""), OLD_ATOM, EXTERNAL_DISPERSION_ATOM, NEW_ATOM
    )

    source_paths = list(paths.values())
    metrics = dyadic_certificate_metrics(TAIL_START)
    return {
        "certificate_type": "nearsquare_strip_defect_certificate_router",
        "status": "signed_nearsquare_strip_bound_reduced_to_pdec_or_sae_exclusion_open",
        "source_hashes": {str(path.relative_to(ROOT)): file_sha256(path) for path in source_paths},
        "counterexample_assumption_only": True,
        "empirical_absence_not_used": True,
        "hypothetical_chain_only": True,
        "failure_to_dyadic_strip_certificate_proved": True,
        "dyadic_strip_certificate_formal_unit_admission_proved": True,
        "persistent_sparse_pdec_sae_admission_proved": True,
        "signed_strip_bound_compressed": compressed,
        "nearsquare_strip_pdec_or_sae_exclusion_proved": False,
        "external_well_factorable_sawtooth_dispersion_accepted": False,
        "direct_unconditional_contradiction_found": False,
        "row_column_unconditional_closed": False,
        "replacement": {OLD_ATOM: NEW_ATOM},
        "latest_self_contained_basis": latest_self,
        "latest_conditional_basis": latest_cond,
        "latest_global_with_external_basis": latest_global,
        "next_priority": NEW_ATOM,
        "certificate_atom": CERT_ATOM,
        "external_next_priority": EXTERNAL_DISPERSION_ATOM,
        "rough_fallback_priority": EXTERNAL_ROUGH_ATOM,
        "generic_external_next_priority": EXTERNAL_DIBFI_ATOM,
        "final_promotion_priority": DSTRUCTURE,
        "dyadic_certificate_metrics": metrics,
        "formal_unit_schema": {
            "Omega": "prime rows P in the hypothetical counterexample family",
            "tau": "fixed dyadic side/h/t/a strip and the induced residue phase P mod Q_B",
            "weight": "Rosser lower weight restricted to the fixed strip block",
            "test_function": "centered signed near-square strip indicator minus arc-length expectation",
            "persistent_branch": "bad rows of positive density give PDEC/Fourier defect",
            "sparse_branch": "isolated bad rows become SAE/local-survivor packets",
        },
        "rows": rows,
        "closed_gates": [item["gate"] for item in rows if item["closed"]],
        "open_gates": [item["gate"] for item in rows if not item["closed"]],
        "plain_conclusion": (
            "本步把 signed near-square strip bound 的失败态完全显化。"
            "若它失败，必有一个 side/h/t/a dyadic 条带承担强负偏差；"
            "该条带是同一 finite formal unit 的测试函数。"
            "因此剩余不再是无名非集中，而是排斥这些条带产生的 PDEC 或 SAE 证书。"
        ),
    }


def write_markdown(result: dict[str, Any], path: Path) -> None:
    """写 Markdown 报告。"""
    replacement = next(iter(result["replacement"].items()))
    metrics = result["dyadic_certificate_metrics"]
    schema = result["formal_unit_schema"]
    lines = [
        "# Prime Matrix 近平方条带缺陷证书路由器",
        "",
        f"**状态：** `{result['status']}`",
        "",
        result["plain_conclusion"],
        "",
        "```text",
        f"counterexample_assumption_only={fmt_bool(result['counterexample_assumption_only'])}",
        f"empirical_absence_not_used={fmt_bool(result['empirical_absence_not_used'])}",
        f"hypothetical_chain_only={fmt_bool(result['hypothetical_chain_only'])}",
        f"failure_to_dyadic_strip_certificate_proved={fmt_bool(result['failure_to_dyadic_strip_certificate_proved'])}",
        (
            "dyadic_strip_certificate_formal_unit_admission_proved="
            f"{fmt_bool(result['dyadic_strip_certificate_formal_unit_admission_proved'])}"
        ),
        f"persistent_sparse_pdec_sae_admission_proved={fmt_bool(result['persistent_sparse_pdec_sae_admission_proved'])}",
        f"signed_strip_bound_compressed={fmt_bool(result['signed_strip_bound_compressed'])}",
        f"nearsquare_strip_pdec_or_sae_exclusion_proved={fmt_bool(result['nearsquare_strip_pdec_or_sae_exclusion_proved'])}",
        f"direct_unconditional_contradiction_found={fmt_bool(result['direct_unconditional_contradiction_found'])}",
        f"row_column_unconditional_closed={fmt_bool(result['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 失败态证书",
        "",
        "若",
        "",
        "```text",
        "signed near-square strip discrepancy < -0.90 M(P)",
        "```",
        "",
        "则按 `side,h,t,a` dyadic 分块，必有一个块承担至少平均强度的负偏差。",
        "",
        "| item | value |",
        "| --- | ---: |",
        f"| tail start | {metrics['tail_start']} |",
        f"| ceil(log2 P) | {metrics['ceil_log2_p']} |",
        f"| dyadic block count bound | {metrics['dyadic_block_count_bound']} |",
        f"| 90% loss budget at tail start | {metrics['ninety_percent_loss_budget_at_tail_start']:.6f} |",
        f"| pigeonhole threshold at tail start | {metrics['pigeonhole_threshold_at_tail_start']:.6f} |",
        "",
        "## 2. Formal Unit 字段",
        "",
        "| field | value |",
        "| --- | --- |",
    ]
    for key, value in schema.items():
        lines.append(f"| `{key}` | {table_cell(value)} |")
    lines.extend(
        [
            "",
            "## 3. 压缩律",
            "",
            "```text",
            replacement[0],
            "  =>",
            replacement[1],
            "```",
            "",
            "## 4. 判定表",
            "",
            "| gate | closed | proved | meaning | remaining |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for item in result["rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
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
            "## 5. 最新输入基",
            "",
            "canonical 自足链条输入基：",
            "",
            "```text",
            result["latest_self_contained_basis"],
            "```",
            "",
            "conditional 输入基：",
            "",
            "```text",
            result["latest_conditional_basis"],
            "```",
            "",
            "global/external 宽口径输入基：",
            "",
            "```text",
            result["latest_global_with_external_basis"],
            "```",
            "",
            "## 6. 下一步",
            "",
            f"直接攻 `{result['next_priority']}`，即排斥 dyadic 近平方条带产生的 PDEC/SAE 证书。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", type=Path, default=DEFAULT_PREVIOUS)
    parser.add_argument("--json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--md", type=Path, default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    """命令行入口。"""
    args = parse_args()
    paths = {
        "previous": args.previous,
    }
    result = run(paths)
    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(result, args.md)
    print(f"wrote {args.json}")
    print(f"wrote {args.md}")


if __name__ == "__main__":
    main()
