#!/usr/bin/env python3
"""生成短区间 rough-residue 屏障路由证书。

用法示例：
  python3 experiments/prime_matrix_short_interval_rough_residue_barrier_router.py
  python3 -m json.tool docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json

输出：
  data/prime-matrix-short-interval-rough-residue-barrier-ledger.json
  docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.json
  docs/monograph/prime-matrix-short-interval-rough-residue-barrier-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-short-interval-rough-residue-barrier-ledger.json"
OUT_JSON = DOCS / "prime-matrix-short-interval-rough-residue-barrier-router.json"
OUT_MD = DOCS / "prime-matrix-short-interval-rough-residue-barrier-router.md"

SOURCE_FILES = [
    "prime-matrix-lowroot-sifted-deficit-frontier-router.json",
    "prime-matrix-row-gap-supply-phase-cycle-cut-router.json",
    "prime-matrix-inverse-alignment-latest-frontier-sync-router.json",
    "prime-matrix-primorial-jacobsthal-central-block-router.json",
    "prime-matrix-square-phase-jacobsthal-special-phase-router.json",
]

ROUGH_LOWER = "NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP"
Q1Q2_TRANSPORT = "AdjacentPrimeQ1Q2CRTTransportDefectOrStableShortReturn"
SEED_CYCLE_CUT = "AcyclicSeedCycleCutPrimitiveBasisAndCoefficientSourceInput"
PDEC_SCOPE = "AcyclicSameSetScopeMatchForDirectPDECCapDualCertificate"
HIGH_MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"

EXTERNAL_GAP = "ExactExternalSqrtLengthPrimeGapInput_FOR_ROW_GAP_ONLY"


def load_json(name: str) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    path = DOCS / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + [DOCS / name for name in SOURCE_FILES]
    return {
        str(path.relative_to(ROOT)): sha256(path)
        for path in paths
        if path.exists()
    }


def fmt_bool(value: Any) -> str:
    """输出小写布尔值。"""
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


def build_rows(lowroot: dict[str, Any]) -> list[dict[str, Any]]:
    """构造屏障判定表。"""
    imported = lowroot.get("next_direct_attack_target") == ROUGH_LOWER
    return [
        row(
            "RoughResidueTargetImported",
            imported,
            False,
            "上一层把 low-root 缺口压到长度 P、筛到 sqrt(kP) 并扣除近根槽后的指定相位 rough-residue 正下界。",
            ROUGH_LOWER,
        ),
        row(
            "FullRootRoughEqualsPrimeInRow",
            True,
            True,
            "在 k<P 且 1<=a<P 时，kP+a<P^2；若未被任何 q<=sqrt(kP+P-1) 覆盖，则 kP+a 只能是素数。",
            "full-root uncovered slot iff row prime slot",
        ),
        row(
            "NearRootSubtractionKeepsEquivalence",
            True,
            True,
            "low-root 未覆盖槽扣除近根 only 槽后的正缺口，正是 full-root 未覆盖槽正性，因此等价于该行有素数。",
            "low_uncovered_minus_near_root_only > 0 iff row contains a prime",
        ),
        row(
            "MertensAverageInsufficient",
            True,
            True,
            "Mertens 或 beta-sieve 平均密度只能给期望量；不能排除某个指定 CRT 相位长度 P 短区间被完全覆盖。",
            "pointwise short-interval lower bound still missing",
        ),
        row(
            "PeriodWideJacobsthalShortcutRejected",
            True,
            True,
            "已有 primorial/Jacobsthal 审计显示全周期最长低筛覆盖块可超过 P；不能用周期全局最长块上界关闭特殊相位。",
            "must use special phase or transport/PDEC, not global Jacobsthal bound",
        ),
        row(
            "DirectRoughLowerBoundIsRowGapStrength",
            True,
            False,
            "若无条件证明该 rough-residue 正下界，就已证明每个 I_k=(kP,kP+P) 有素数；这不是辅助引理，而是行命题本身的平方根长度素数间隙形态。",
            EXTERNAL_GAP,
        ),
        row(
            "NonCircularInternalUseRejected",
            True,
            True,
            "在自足证明内把该下界当作已证输入会循环使用目标命题；只能登记为外部强输入或转攻非循环相位传输/seed/PDEC。",
            f"{Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步关闭 direct rough-residue 首攻的循环性审查，但没有给出全局无条件证明。",
            f"({Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE}) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造证书。"""
    lowroot = load_json("prime-matrix-lowroot-sifted-deficit-frontier-router.json")
    rows = build_rows(lowroot)
    noncircular_basis = (
        f"({Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE}) "
        f"AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    with_external_basis = f"({EXTERNAL_GAP} OR ({Q1Q2_TRANSPORT} OR {SEED_CYCLE_CUT} OR {PDEC_SCOPE})) AND {HIGH_MODEL} AND {RATE} AND {DSTRUCTURE}"
    plain = (
        f"`{ROUGH_LOWER}` 被审查为平方根长度短区间素数存在性的同义屏障："
        "扣除近根槽后的 rough-residue 正缺口为正，当且仅当对应 row 内已有素数。"
        "因此它不能作为自足非循环证明的内部黑箱；若不用外部短区间素数间隙输入，"
        "当前路线必须转到 Q1/Q2 CRT 传输缺陷、seed cycle-cut 或 same-set PDEC 作用域匹配。"
    )
    return {
        "certificate_type": "prime_matrix_short_interval_rough_residue_barrier_router",
        "status": "direct_rough_residue_route_classified_as_row_gap_strength_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "empirical_absence_not_used_as_proof": True,
        "rough_residue_target_imported": lowroot.get("next_direct_attack_target") == ROUGH_LOWER,
        "full_root_rough_equals_prime_in_row": True,
        "near_root_subtraction_keeps_equivalence": True,
        "mertens_average_insufficient": True,
        "periodwide_jacobsthal_shortcut_rejected": True,
        "direct_rough_lower_bound_is_row_gap_strength": True,
        "noncircular_internal_use_rejected": True,
        "external_gap_input_accepted": False,
        "noncircular_short_interval_rough_residue_lower_bound_proved": False,
        "row_column_unconditional_closed": False,
        "rejected_internal_direct_target": ROUGH_LOWER,
        "optional_external_input": EXTERNAL_GAP,
        "next_direct_attack_target": Q1Q2_TRANSPORT,
        "parallel_attack_targets": [SEED_CYCLE_CUT, PDEC_SCOPE],
        "strict_internal_basis_after_router": noncircular_basis,
        "basis_if_external_gap_input_is_accepted": with_external_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix 短区间 rough-residue 屏障路由证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        "full_root_rough_equals_prime_in_row=true",
        "near_root_subtraction_keeps_equivalence=true",
        "mertens_average_insufficient=true",
        "periodwide_jacobsthal_shortcut_rejected=true",
        "noncircular_internal_use_rejected=true",
        "noncircular_short_interval_rough_residue_lower_bound_proved=false",
        "row_column_unconditional_closed=false",
        "```",
        "",
        "## 1. 精确屏障",
        "",
        "令 `I_k={kP+a:1<=a<P}` 且 `1<=k<P`。对每个槽 `n=kP+a`，有",
        "",
        "```text",
        "n <= kP+P-1 < P^2.",
        "```",
        "",
        "若 `n` 是合数，则存在素因子 `q<=sqrt(n)<=sqrt(kP+P-1)`。反过来，若没有",
        "这样的素因子覆盖该槽，则 `n` 只能是素数。因此",
        "",
        "```text",
        "#{a in [1,P-1] : kP+a is uncovered by all q<=sqrt(kP+P-1)} > 0",
        "iff",
        "I_k contains a prime.",
        "```",
        "",
        "这说明当前 rough-residue 下界已经不是松弛辅助量，而是行命题在筛语言中的精确版本。",
        "",
        "## 2. 近根扣除",
        "",
        "上一层的 low-root 表达式把 `q<=sqrt(kP)` 的覆盖和",
        "",
        "```text",
        "sqrt(kP)<q<=sqrt(kP+P-1)",
        "```",
        "",
        "的近根 only 槽分开。若记 `L` 为 low-root 未覆盖槽数，`N` 为近根 only 槽数，则",
        "",
        "```text",
        "full_root_uncovered = L - N.",
        "```",
        "",
        "所以要证明 `L-N>0`，仍然正是证明该行存在素数。近根容量上界是正确但不足的：核心不是容量，而是指定相位短区间逐点不能全覆盖。",
        "",
        "## 3. 非循环判定",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| {gate} | `{closed}` | `{proved}` | {meaning} | {remaining} |".format(
                gate=cell(item["gate"]),
                closed=fmt_bool(item["closed"]),
                proved=fmt_bool(item["proved"]),
                meaning=cell(item["meaning"]),
                remaining=cell(item["remaining"]),
            )
        )

    lines.extend(
        [
            "",
            "## 4. 最新内部非循环基",
            "",
            "```text",
            cert["strict_internal_basis_after_router"],
            "```",
            "",
            "若接受外部平方根长度短区间素数间隙输入，可写为：",
            "",
            "```text",
            cert["basis_if_external_gap_input_is_accepted"],
            "```",
            "",
            "但该外部输入在本文中未被证明，也不能冒充自足闭合。",
            "",
            "## 5. 下一直接主攻",
            "",
            "```text",
            cert["next_direct_attack_target"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " OR ".join(cert["parallel_attack_targets"]),
            "```",
            "",
            "## 6. 诚实边界",
            "",
            "- 本证书不证明 row-gap 不存在。",
            "- 本证书不把 Mertens、平均 beta-sieve 密度、或有限样本当作逐行短区间证明。",
            "- 本证书只删除一个循环首攻点：`NonCircularShortIntervalRoughResidueLowerBoundLengthPLevelSqrtkP` 若直接使用，就是目标命题本身。",
            "",
            "## 7. 依赖哈希",
            "",
            "| file | sha256 |",
            "| --- | --- |",
        ]
    )
    for path, digest in cert["source_hashes"].items():
        lines.append(f"| `{path}` | `{digest}` |")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """写出 JSON、ledger 与 Markdown。"""
    DATA.mkdir(exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    text = json.dumps(cert, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    OUT_LEDGER.write_text(text, encoding="utf-8")
    OUT_JSON.write_text(text, encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
