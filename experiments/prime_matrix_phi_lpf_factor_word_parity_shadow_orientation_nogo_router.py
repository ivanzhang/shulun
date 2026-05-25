#!/usr/bin/env python3
"""审计 factor-word parity shadow 是否能替代 Phi-LPF 取向/local-factor signed law。

用法示例：
  python3 experiments/prime_matrix_phi_lpf_factor_word_parity_shadow_orientation_nogo_router.py
  python3 -m json.tool docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.json

输出：
  data/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-ledger.json
  docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.json
  docs/monograph/prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo-router.md

本证书承接 small-to-large factor peeling：Möbius、Liouville、depth parity
确实由无符号 factor word 闭合。但 orientation/local-factor signed law 是
Cauchy/Phi/payment 推前前的奇数据；若只读取 factor word，就没有 source key、
orientation branch trace、ExactUV payload 和 named return。因此该 parity shadow
不能闭合三命题中的行/列 signed 硬点。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

SLUG = "prime-matrix-phi-lpf-factor-word-parity-shadow-orientation-nogo"
OUT_LEDGER = DATA / f"{SLUG}-ledger.json"
OUT_JSON = DOCS / f"{SLUG}-router.json"
OUT_MD = DOCS / f"{SLUG}-router.md"

SMALL_TO_LARGE = DOCS / "prime-matrix-phi-lpf-small-to-large-factor-peeling-signed-state-boundary-router.json"
POINTWISE_ORIENTATION = DOCS / "prime-matrix-phi-lpf-pointwise-signed-table-orientation-law-sync-router.json"
ROW_ORIENTATION = DOCS / "prime-matrix-strict-row-level-noncircular-orientation-law-router.json"
BRANCH_TRACE = DOCS / "prime-matrix-strict-orientation-law-branch-trace-router.json"
BUILTIN_PAIRING = DOCS / "prime-matrix-strict-builtin-pairing-closed-form-frontier-router.json"
NONCIRCULAR_KERNEL = DOCS / "prime-matrix-strict-noncircular-signed-coefficient-emission-kernel-router.json"

ORIENTATION_LAW = "PrimitiveOrientationLocalFactorProductLawBeforePushforward"
BUILTIN_PAIRING_TARGET = "BuiltInSignedCoefficientPairingClosedFormForAtomicJointRows"
ATOMIC_BRANCH_TRACE = "ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn"
ACTUAL_BRANCH_TRACE = "ExactActualNoncanonicalPrimitiveBranchTraceFormulaOrReturn"
PRECAUCHY_SOURCE = "PreCauchyActualNoncanonicalEmitterSourceDeclarationPacket"
EXACT_UV = "ActualEmitterSourceDomainEntropyLedger AND ExactUVMapFixedPairPolylogFiberBoundLedger"
POINTWISE_TABLE = "PointwiseSignedCoefficientValueTableOnPhiLPFBucketSupportBeforePushforward"
ROW_MASS = "SameFormalUnitPrimitiveRowMassNormalizationAndNoHeavyRowLedger"
MODEL = "ExplicitModelGapAndFiniteDPRCLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON 证书；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算证据文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fmt_bool(value: Any) -> str:
    """把布尔值写成小写文本。"""
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
    """登记本证书及依赖哈希。"""
    paths = [
        Path(__file__).resolve(),
        SMALL_TO_LARGE,
        POINTWISE_ORIENTATION,
        ROW_ORIENTATION,
        BRANCH_TRACE,
        BUILTIN_PAIRING,
        NONCIRCULAR_KERNEL,
    ]
    return {str(path.relative_to(ROOT)): sha256(path) for path in paths if path.exists()}


def shadow_candidates() -> list[dict[str, Any]]:
    """列出由 factor word 机械闭合的自然 parity shadows。"""
    return [
        {
            "shadow": "MobiusFactorWordShadow",
            "formula": "0 if factor_word has repeated prime else (-1)^len(factor_word)",
            "depends_only_on_unsigned_factor_word": True,
            "orientation_sensitive": False,
            "has_precauchy_source_key": False,
            "has_branch_trace": False,
            "has_exactuv_payload": False,
            "can_be_signed_law": False,
        },
        {
            "shadow": "LiouvilleFactorWordShadow",
            "formula": "(-1)^len(factor_word)",
            "depends_only_on_unsigned_factor_word": True,
            "orientation_sensitive": False,
            "has_precauchy_source_key": False,
            "has_branch_trace": False,
            "has_exactuv_payload": False,
            "can_be_signed_law": False,
        },
        {
            "shadow": "DepthParityShadow",
            "formula": "len(factor_word) mod 2",
            "depends_only_on_unsigned_factor_word": True,
            "orientation_sensitive": False,
            "has_precauchy_source_key": False,
            "has_branch_trace": False,
            "has_exactuv_payload": False,
            "can_be_signed_law": False,
        },
        {
            "shadow": "SquarefreeZeroShadow",
            "formula": "1 if factor_word has no repeated prime else 0",
            "depends_only_on_unsigned_factor_word": True,
            "orientation_sensitive": False,
            "has_precauchy_source_key": False,
            "has_branch_trace": False,
            "has_exactuv_payload": False,
            "can_be_signed_law": False,
        },
    ]


def abstract_orientation_twin_collision(largest: dict[str, Any]) -> dict[str, Any]:
    """用合同级 orientation twin 展示 factor word 不能决定反变号 signed 数据。

    这里不声称每个 twin 都已构造成实际行；它表达当前闭合合同的逻辑边界：
    已证 factor word 不含 orientation 字段，而 signed coefficient 对 orientation
    翻转敏感。因此任何只读 factor word 的函数都会把两个取向态压成同一值。
    """
    support_keys = int(largest.get("composite_support_keys", 0))
    return {
        "support_keys_in_largest_sample": support_keys,
        "abstract_orientation_states_per_key": 2,
        "abstract_twin_state_count": support_keys * 2,
        "factor_word_shadow_collision_count": support_keys,
        "collision_meaning": (
            "same unsigned factor word admits two formal orientation slots in the current "
            "contract; parity shadows are identical on the slots while a signed law must "
            "record orientation/local-factor data before pushforward"
        ),
    }


def build_rows(
    small: dict[str, Any],
    pointwise: dict[str, Any],
    row_orientation: dict[str, Any],
    branch_trace: dict[str, Any],
    builtin: dict[str, Any],
    kernel: dict[str, Any],
) -> list[dict[str, Any]]:
    """生成 parity shadow no-go 判定表。"""
    factor_shadow_closed = (
        small.get("small_to_large_factor_peeling_verified_all_samples") is True
        and small.get("mobius_liouville_state_computable_from_factor_word_all_samples") is True
    )
    orientation_flip_contract = (
        row_orientation.get("unsigned_geometry_even_under_orientation_flip") is True
        and row_orientation.get("signed_coefficient_is_orientation_sensitive") is True
    )
    pointwise_to_orientation = (
        pointwise.get("next_primary_attack_target") == ORIENTATION_LAW
        and pointwise.get("orientation_local_factor_law_proved") is False
    )
    branch_trace_open = (
        branch_trace.get("complete_branch_trace_would_imply_orientation_law") is True
        and branch_trace.get("actual_noncanonical_complete_branch_trace_formula_proved") is False
    )
    builtin_to_trace = (
        builtin.get("next_direct_attack_target") == ATOMIC_BRANCH_TRACE
        and builtin.get("exact_atomic_joint_branch_trace_signed_coefficient_formula_proved") is False
    )
    old_parity_rejected = (
        kernel.get("mobius_truncation_rejected_as_exact_kernel") is True
        and kernel.get("threeedge_parity_audits_rejected_as_exact_kernel") is True
    )
    return [
        row(
            "FactorWordParityShadowsClosed",
            factor_shadow_closed,
            True,
            "small-to-large 剥离已闭合 Möbius、Liouville、depth parity 与 squarefree 等自然 shadow。",
            "closed unsigned factor-word state table",
        ),
        row(
            "ShadowsDependOnlyOnUnsignedFactorWord",
            True,
            True,
            "这些 shadow 的输入只有非降素因子词和重复素因子信息，不读取 source、orientation、UV 或 branch tag。",
            "post-factorization labels",
        ),
        row(
            "OrientationFlipContractImported",
            orientation_flip_contract,
            True,
            "既有 row-level 证书登记：无符号几何在取向翻转下不变，而 signed coefficient 对取向敏感。",
            ORIENTATION_LAW,
        ),
        row(
            "PointwiseSignedTableStillNeedsOrientationLaw",
            pointwise_to_orientation,
            False,
            "Phi-LPF support 上的逐点 signed table 首字段仍是 primitive orientation/local-factor product law。",
            POINTWISE_TABLE,
        ),
        row(
            "BranchTraceStillMissing",
            branch_trace_open,
            False,
            "orientation/local-factor law 已压到 actual noncanonical complete branch trace formula 或命名回流。",
            ACTUAL_BRANCH_TRACE,
        ),
        row(
            "BuiltInPairingStillNeedsAtomicTrace",
            builtin_to_trace,
            False,
            "atomic joint rows 的 built-in signed pairing 仍需 ExactAtomicJointBranchTraceSignedCoefficientFormulaOrReturn。",
            ATOMIC_BRANCH_TRACE,
        ),
        row(
            "PreviousParityKernelRejectionsImported",
            old_parity_rejected,
            True,
            "既有 noncircular kernel 证书已拒绝 Mobius truncation 与 three-edge parity audit 作为 exact kernel。",
            "parity shadow is not a kernel",
        ),
        row(
            "ShadowLacksPreCauchySourceKey",
            small.get("peeling_generates_new_precauchy_signed_payload") is False,
            True,
            "factor word 不声明同 formal unit 的 pre-Cauchy source tuple 或 emitter source key。",
            PRECAUCHY_SOURCE,
        ),
        row(
            "ShadowLacksExactUVPayload",
            builtin.get("actual_emitter_exact_uv_bounded_multiplicity_incidence_proved") is False,
            False,
            "factor word 不输出 exact `(u,v)`、fixed-pair multiplicity、branch key 或 nonzero condition。",
            EXACT_UV,
        ),
        row(
            "FactorWordShadowProvesOrientationLocalFactorLaw",
            False,
            False,
            "只读 factor word 的 parity shadow 在 orientation twin 上取同值，不能给反变号取向/local-factor 乘积律。",
            ORIENTATION_LAW,
        ),
        row(
            "FactorWordShadowProvesBuiltInPairing",
            False,
            False,
            "built-in pairing 要同一 atomic trace 同时给 word、signed coefficient、alpha/delta payload 与 ExactUV；shadow 不足。",
            BUILTIN_PAIRING_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步只排除了 parity shadow 直升 signed law 的捷径；三命题仍未无条件闭合。",
            f"{ORIENTATION_LAW} OR {BUILTIN_PAIRING_TARGET}",
        ),
    ]


def external_frontier_note() -> list[dict[str, str]]:
    """记录本步对外部定理的适配边界。"""
    return [
        {
            "input_family": "DI/BFI/Kuznetsov, FKMS, Milicevic-Qin-Wu, Pascadi, Wright-type trace or Kloosterman tools",
            "usable_after": "提交 admissible averaged trace/Kloosterman/Type-II family with signed payload",
            "not_supplied_by_shadow": "factor-word parity shadow is a pointwise post-factorization label, not an averaged trace family",
        },
        {
            "input_family": "Maynard small gaps or Li short intervals",
            "usable_after": "转化为目标尺度的行/列或 residue-level positivity statement",
            "not_supplied_by_shadow": "does not provide fixed row/AP positivity or signed coefficient generation",
        },
        {
            "input_family": "linear or beta-sieve parity inputs",
            "usable_after": "出现 independent odd data or named return beyond support saturation",
            "not_supplied_by_shadow": "Möbius/Liouville visibility remains exactly parity-shadow information",
        },
    ]


def build_certificate() -> dict[str, Any]:
    """组装 parity shadow no-go 证书。"""
    small = load_json(SMALL_TO_LARGE)
    pointwise = load_json(POINTWISE_ORIENTATION)
    row_orientation = load_json(ROW_ORIENTATION)
    branch_trace = load_json(BRANCH_TRACE)
    builtin = load_json(BUILTIN_PAIRING)
    kernel = load_json(NONCIRCULAR_KERNEL)
    largest = small.get("largest_sample_summary", {})
    rows = build_rows(small, pointwise, row_orientation, branch_trace, builtin, kernel)
    return {
        "certificate_type": "prime_matrix_phi_lpf_factor_word_parity_shadow_orientation_nogo_router",
        "status": "factor_word_parity_shadow_rejected_as_orientation_or_builtin_pairing_law",
        "verified_date": "2026-05-25",
        "factor_word_mobius_shadow_closed": True,
        "factor_word_liouville_shadow_closed": True,
        "depth_parity_shadow_closed": True,
        "squarefree_shadow_closed": True,
        "shadow_depends_only_on_unsigned_factor_word": True,
        "shadow_lacks_precauchy_source_key": True,
        "shadow_lacks_orientation_branch_trace": True,
        "shadow_lacks_exactuv_payload": True,
        "shadow_orientation_twin_collision_registered": True,
        "factor_word_shadow_proves_orientation_local_factor_law": False,
        "factor_word_shadow_proves_builtin_pairing": False,
        "orientation_local_factor_law_proved": False,
        "built_in_signed_pairing_proved": False,
        "exact_atomic_joint_branch_trace_signed_coefficient_formula_proved": False,
        "peeling_generates_new_precauchy_signed_payload": False,
        "phi_lpf_parity_barrier_globally_broken": False,
        "row_column_unconditional_closed": False,
        "largest_sample_summary_imported": largest,
        "abstract_orientation_twin_collision": abstract_orientation_twin_collision(largest),
        "shadow_candidates": shadow_candidates(),
        "gate_rows": rows,
        "external_frontier_note": external_frontier_note(),
        "source_hashes": source_hashes(),
        "next_primary_attack_target": f"{ORIENTATION_LAW} OR {BUILTIN_PAIRING_TARGET}",
        "retained_strict_basis": (
            f"({ORIENTATION_LAW} AND {ROW_MASS}) OR "
            f"({BUILTIN_PAIRING_TARGET} AND {ATOMIC_BRANCH_TRACE} AND {EXACT_UV} "
            f"AND {MODEL} AND {RATE} AND {DSTRUCTURE})"
        ),
        "plain_conclusion": (
            "Factor-word parity shadows are fully computable after small-to-large LPF peeling, "
            "but they are unsigned post-factorization labels.  Because the current strict "
            "contracts require orientation-sensitive pre-Cauchy data before pushforward, "
            "a shadow depending only on the factor word cannot prove the orientation/local-factor "
            "law or built-in atomic signed pairing.  The route is therefore a no-go shortcut, "
            "not an unconditional closure."
        ),
    }


def render_markdown(result: dict[str, Any]) -> str:
    """渲染 Markdown 证书。"""
    lines: list[str] = []
    lines.append("# Prime Matrix Phi-LPF factor-word parity shadow orientation no-go 证书")
    lines.append("")
    lines.append(f"**状态：** `{result['status']}`")
    lines.append(f"**核验日期：** `{result['verified_date']}`")
    lines.append("")
    lines.append(
        "本证书检验一个最自然的捷径：把 LPF factor word 给出的 Möbius、Liouville、"
        "depth parity 或 squarefree 状态直接升级为 orientation/local-factor signed law。"
    )
    lines.append("结论是否定的：这些 shadow 全部闭合，但都只依赖无符号 factor word。")
    lines.append("")
    lines.append("```text")
    for key in [
        "factor_word_mobius_shadow_closed",
        "factor_word_liouville_shadow_closed",
        "depth_parity_shadow_closed",
        "shadow_depends_only_on_unsigned_factor_word",
        "shadow_lacks_precauchy_source_key",
        "shadow_lacks_orientation_branch_trace",
        "shadow_lacks_exactuv_payload",
        "factor_word_shadow_proves_orientation_local_factor_law",
        "factor_word_shadow_proves_builtin_pairing",
        "row_column_unconditional_closed",
        "phi_lpf_parity_barrier_globally_broken",
    ]:
        lines.append(f"{key}={fmt_bool(result[key])}")
    lines.append("```")
    lines.append("")
    lines.append("## 1. shadow 候选")
    lines.append("")
    lines.append("| shadow | formula | unsigned only | source key | branch trace | ExactUV | can be signed law |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for item in result["shadow_candidates"]:
        lines.append(
            "| `{shadow}` | `{formula}` | `{unsigned}` | `{source}` | `{branch}` | `{exactuv}` | `{law}` |".format(
                shadow=cell(item["shadow"]),
                formula=cell(item["formula"]),
                unsigned=fmt_bool(item["depends_only_on_unsigned_factor_word"]),
                source=fmt_bool(item["has_precauchy_source_key"]),
                branch=fmt_bool(item["has_branch_trace"]),
                exactuv=fmt_bool(item["has_exactuv_payload"]),
                law=fmt_bool(item["can_be_signed_law"]),
            )
        )
    lines.append("")
    lines.append("## 2. orientation twin collision")
    lines.append("")
    twin = result["abstract_orientation_twin_collision"]
    lines.append("```text")
    lines.append(f"support_keys_in_largest_sample={twin['support_keys_in_largest_sample']}")
    lines.append(f"abstract_orientation_states_per_key={twin['abstract_orientation_states_per_key']}")
    lines.append(f"abstract_twin_state_count={twin['abstract_twin_state_count']}")
    lines.append(f"factor_word_shadow_collision_count={twin['factor_word_shadow_collision_count']}")
    lines.append("```")
    lines.append("")
    lines.append(
        "含义：当前已闭合合同中，factor word 不含 orientation 字段；而 signed coefficient "
        "对 orientation/local factor 敏感。任何只读 factor word 的函数都会把取向槽压成同一值。"
    )
    lines.append("")
    lines.append("## 3. 判定表")
    lines.append("")
    lines.append("| gate | closed | proved | meaning | remaining |")
    lines.append("| --- | --- | --- | --- | --- |")
    for item in result["gate_rows"]:
        lines.append(
            f"| `{cell(item['gate'])}` | `{fmt_bool(item['closed'])}` | `{fmt_bool(item['proved'])}` | "
            f"{cell(item['meaning'])} | `{cell(item['remaining'])}` |"
        )
    lines.append("")
    lines.append("## 4. 外部前沿适配边界")
    lines.append("")
    lines.append("| external input | usable after | not supplied by shadow |")
    lines.append("| --- | --- | --- |")
    for item in result["external_frontier_note"]:
        lines.append(
            f"| {cell(item['input_family'])} | {cell(item['usable_after'])} | "
            f"{cell(item['not_supplied_by_shadow'])} |"
        )
    lines.append("")
    lines.append("## 5. 最新开放口")
    lines.append("")
    lines.append("```text")
    lines.append(result["next_primary_attack_target"])
    lines.append("```")
    lines.append("")
    lines.append("保留严格基底：")
    lines.append("")
    lines.append("```text")
    lines.append(result["retained_strict_basis"])
    lines.append("```")
    lines.append("")
    lines.append("## 6. 依赖哈希")
    lines.append("")
    lines.append("| file | sha256 |")
    lines.append("| --- | --- |")
    for path, digest in result["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    lines.append("行/列命题仍未无条件闭合。")
    lines.append("")
    return "\n".join(lines)


def write_outputs(result: dict[str, Any]) -> None:
    """写出 JSON 与 Markdown。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    OUT_LEDGER.write_text(payload + "\n", encoding="utf-8")
    OUT_JSON.write_text(payload + "\n", encoding="utf-8")
    OUT_MD.write_text(render_markdown(result), encoding="utf-8")


def main() -> None:
    """入口。"""
    result = build_certificate()
    write_outputs(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
