#!/usr/bin/env python3
"""检查“第 P+1 行非零是否足以排除 x<P 零行”的旧仓库结论。

用法示例：
  python3 experiments/prime_matrix_inverse_alignment_pplus1_row_reduction_check_router.py
  python3 -m json.tool docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json

输出：
  data/prime-matrix-inverse-alignment-pplus1-row-reduction-check-ledger.json
  docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json
  docs/monograph/prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-inverse-alignment-pplus1-row-reduction-check-ledger.json"
OUT_JSON = DOCS / "prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.json"
OUT_MD = DOCS / "prime-matrix-inverse-alignment-pplus1-row-reduction-check-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-zero-row-minrep-route-review.md",
    DOCS / "prime-matrix-inverse-alignment-min-x-phase-scan-router.md",
    DOCS / "prime-matrix-inverse-alignment-latest-frontier-sync-router.json",
    DOCS / "prime-matrix-prime-square-x-equals-p-wheel-router.json",
    DOCS / "prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json",
    DOCS / "prime-matrix-terminal-row-square-phase-bridge-router.json",
    DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json",
]

EARLY_NO_ZERO = "NoZeroRowForAllEarlyMultipliersOneToPMinusOne"
PPLUS1_NONZERO = "NoZeroRowAtXEqualsP_PlusOneRowAfterSquare"
FIRST_HALF = "PrimeInFirstHalfAfterPrimeSquareForEveryPrimeP"
SQUARE_PHASE = "SquarePhaseRoughSurvivorUniformLowerBound"
TRANSFER = "AcyclicEarlyZeroToSquareAnchorPhaseTransferOrNamedReturn"
SIGNED_ROW = "AcyclicSeedPrimitiveRowSignedCoefficientLawBeforePushforward"
SOURCE_TABLE = "ActualNoncanonicalPrimitiveEmitterSourceTableLedger"
FIXED_KEY = "FixedKeyExactUVLocalMultiplicityO1Ledger"
NEW_JOINT = "NewExplicitActualJointAlphaDeltaConstructorFormulaArtifact"
EXTERNAL_KZ = "ExternalDIBFIKuznetsovDispersionTheoremMatch"
MODEL = "HighSegmentModelGapAlpha043C3AnalyticLedger"
RATE = "RatePreservationLedger_FOR_moving_atom_packet"
DSTRUCTURE = "DStructureTailLog4FiniteRankinFullLedgerIndependentAcceptance"


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算依赖文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证据哈希。"""
    paths = [Path(__file__).resolve()] + SOURCE_FILES
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


def build_rows() -> list[dict[str, Any]]:
    """构造第 P+1 行归约检查表。"""
    return [
        row(
            "OldMinRepEquivalenceClosed",
            True,
            True,
            "旧稿已闭合：最小对齐解 X_0(P)>P 等价于 1<=x<=P 全部非零行，也等价于每个 P 对齐短区间有素数。",
            "none for equivalence",
        ),
        row(
            "PPlusOneRowIsXEqualsP",
            True,
            True,
            "按仓库记号，x=P 是一编号第 P+1 行，窗口为 P^2+r, 1<=r<P。",
            "none for notation",
        ),
        row(
            "XEqualsPNoCoverEquivalentToFirstHalfPrimeSquare",
            True,
            True,
            "旧稿已闭合：x=P 无全覆盖等价于 (P^2,P^2+P) 内存在素数。",
            FIRST_HALF,
        ),
        row(
            "FinalTailRouteNeedsPPlusOneAsHardInput",
            True,
            True,
            "final-tail 统一下界若要闭合，代入 x=P 必须先得到平方后前半窗素数输入；这是必要阻塞，不是充分归约。",
            FIRST_HALF,
        ),
        row(
            "PPlusOneNonzeroImpliesAllEarlyRowsNonzero",
            False,
            False,
            "旧仓库没有证明第 P+1 行非零可推出全部 x<P 非零；不同 x 给出不同相位 rho_q(x)=-xP mod q，不能由 x=P 的负平方相位自动控制。",
            TRANSFER,
        ),
        row(
            "ValidConditionalReduction",
            True,
            False,
            "若新增证明：任一 x<P 零行必转移到 x=P 零行，或进入命名 PDEC/SAE/ColumnCRT/source-rank 出口；再排除这些出口，则可由第 P+1 行非零推出早期无零行。",
            f"{TRANSFER} AND {PPLUS1_NONZERO}",
        ),
        row(
            "LatestNoncycleFrontierPreserved",
            True,
            False,
            "该检查只新增一个旧路线回流接口；exact-UV 后的 signed-row/source-table/fixed-key 主前沿仍保持开放。",
            f"({SIGNED_ROW} OR {TRANSFER}) AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "本步确认旧稿没有把第 P+1 行非零提升为全早期窗口排斥；行/列命题仍未无条件闭合。",
            f"({SIGNED_ROW} OR {TRANSFER} OR {SOURCE_TABLE} OR {FIXED_KEY} OR {NEW_JOINT} OR {EXTERNAL_KZ}) AND {MODEL} AND {RATE} AND {DSTRUCTURE}",
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造同步证书。"""
    x_equals_p = load_json(DOCS / "prime-matrix-prime-square-x-equals-p-wheel-router.json")
    final_tail = load_json(DOCS / "prime-matrix-inverse-alignment-final-tail-rough-survivor-obstruction-router.json")
    exactuv = load_json(DOCS / "prime-matrix-exactuv-fiber-latest-noncycle-sync-router.json")
    rows = build_rows()
    conditional_basis = (
        f"{TRANSFER} AND {PPLUS1_NONZERO} AND "
        "PDEC_SAE_ColumnCRT_NamedReturnExclusion"
    )
    latest_basis = (
        f"(({SIGNED_ROW} OR {TRANSFER}) OR {SOURCE_TABLE} OR {FIXED_KEY} OR {NEW_JOINT} OR {EXTERNAL_KZ}) "
        f"AND {MODEL} AND {RATE} AND {DSTRUCTURE}"
    )
    plain = (
        "旧仓库确实已经把 x=P 特化为第 P+1 行/平方后前半窗问题，"
        "并证明该行无全覆盖等价于 (P^2,P^2+P) 内存在素数。"
        "但旧仓库没有证明“第 P+1 行非零 => 全部 x<P 非零”。"
        "这个方向还需要一个新的非循环相位转移定理：任一早期零行要么强制平方锚 x=P 也零行，"
        "要么进入命名 PDEC/SAE/ColumnCRT/source-rank 出口。"
    )
    return {
        "certificate_type": "prime_matrix_inverse_alignment_pplus1_row_reduction_check_router",
        "status": "pplus1_row_reduction_checked_transfer_missing_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "old_minrep_equivalence_closed": True,
        "pplus1_row_is_x_equals_p": True,
        "x_equals_p_no_cover_equivalent_to_first_half_prime_square": True,
        "x_equals_p_no_solution_global_proved": x_equals_p.get("x_equals_p_no_solution_global_proved") is True,
        "first_half_prime_square_current_corpus_proved": final_tail.get("first_half_prime_square_input_current_corpus_proved") is True,
        "pplus1_nonzero_suffices_for_all_early_rows_proved": False,
        "needed_transfer_theorem": TRANSFER,
        "valid_conditional_reduction_basis": conditional_basis,
        "latest_noncycle_basis_after_check": latest_basis,
        "global_previous_direct_attack_target_preserved": exactuv.get("next_direct_attack_target", SIGNED_ROW),
        "next_direct_attack_target_for_this_branch": TRANSFER,
        "parallel_direct_attack_targets": [SIGNED_ROW, SOURCE_TABLE, FIXED_KEY, NEW_JOINT, EXTERNAL_KZ, SQUARE_PHASE],
        "row_column_unconditional_closed": False,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix inverse alignment 第 P+1 行归约检查证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"old_minrep_equivalence_closed={fmt_bool(cert['old_minrep_equivalence_closed'])}",
        f"pplus1_row_is_x_equals_p={fmt_bool(cert['pplus1_row_is_x_equals_p'])}",
        f"x_equals_p_no_cover_equivalent_to_first_half_prime_square={fmt_bool(cert['x_equals_p_no_cover_equivalent_to_first_half_prime_square'])}",
        f"pplus1_nonzero_suffices_for_all_early_rows_proved={fmt_bool(cert['pplus1_nonzero_suffices_for_all_early_rows_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 结论",
        "",
        "按当前仓库记号，行乘数 `x` 的窗口是 `xP+r, 1<=r<P`；因此 `x=P` 是一编号第 `P+1` 行，也就是平方锚后首行。",
        "旧材料已经证明 `x=P` 无全覆盖等价于平方后前半窗有素数；这回答了“第 P+1 行”本身的强度。",
        "",
        "但这不是全早期窗口的充分条件。若 `x` 改变，所有小素数的覆盖相位同步变为 `rho_q(x)=-xP mod q`；",
        "`x=P` 的负平方相位只是一条特殊相位线，不能自动支配 `1<=x<P` 的全部相位线。",
        "",
        "## 2. 判定表",
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
            "## 3. 有效条件归约",
            "",
            "可安全使用的条件命题是：",
            "",
            "```text",
            "EarlyZero(x<P)",
            "=> ZeroAtXEqualsP OR NamedReturn(PDEC/SAE/ColumnCRT/source-rank)",
            "```",
            "",
            "在该转移定理与命名出口排斥都闭合后，`x=P` 非零才可推出早期无零行。当前缺失项为：",
            "",
            "```text",
            cert["needed_transfer_theorem"],
            "```",
            "",
            "因此本分支的条件闭合基为：",
            "",
            "```text",
            cert["valid_conditional_reduction_basis"],
            "```",
            "",
            "与 exact-UV 后最新非循环前沿合并后的活动基为：",
            "",
            "```text",
            cert["latest_noncycle_basis_after_check"],
            "```",
            "",
            "## 4. 下一直接主攻",
            "",
            "本分支下一主攻：",
            "",
            "```text",
            cert["next_direct_attack_target_for_this_branch"],
            "```",
            "",
            "全局上一主攻仍保留：",
            "",
            "```text",
            cert["global_previous_direct_attack_target_preserved"],
            "```",
            "",
            "并行保留：",
            "",
            "```text",
            " OR ".join(cert["parallel_direct_attack_targets"]),
            "```",
            "",
            "## 5. 诚实边界",
            "",
            "- 本证书确认旧稿存在 `x=P`/第 `P+1` 行等价链。",
            "- 本证书同时确认旧稿没有证明第 `P+1` 行非零足以排除所有 `x<P` 零行。",
            "- 行/列命题仍未全局无条件闭合。",
            "",
            "## 6. 依赖哈希",
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
