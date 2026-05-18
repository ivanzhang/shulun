#!/usr/bin/env python3
"""生成 persistent scale-ladder signature 的尺度词熵证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_scale_ladder_word_entropy_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json",
]

PREVIOUS_TARGET = "PersistentScaleLadderSignatureOrSparseScaleLadderSAEColumnCRTPDEC"
IMPORT = "PersistentScaleLadderSignatureImportedLedger"
WORD_PARTITION = "ScaleLadderDyadicWordPartitionLedger"
PRODUCT_BUDGET = "ScaleLadderProductBudgetLedger"
WORD_ENTROPY = "ScaleLadderWordEntropyFiniteCapLedger"
SINGLE_WORD = "AggregatePersistentPressureToSingleScaleWordLedger"
FIXED_WORD = "FixedScaleLadderMCRTColumnCRTExitLedger"
FIRST_MOVE = "FirstMovingScaleLadderPhaseCoordinateLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardLedger"
NO_ANON = "NoAnonymousPersistentScaleLadderSignatureLedger"
NEW_TARGET = "FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC"

REDUCED_TARGET = (
    f"{IMPORT} AND {WORD_PARTITION} AND {PRODUCT_BUDGET} AND {WORD_ENTROPY} "
    f"AND {SINGLE_WORD} AND {FIXED_WORD} AND {FIRST_MOVE} AND {SPARSE} "
    f"AND {NO_ANON} AND {NEW_TARGET}"
)


def load_json(path: Path) -> dict[str, Any]:
    """读取 JSON；缺失时返回空对象。"""
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    """计算文件哈希。"""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_hashes() -> dict[str, str]:
    """登记脚本和上游证书哈希。"""
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


def replace_latest_basis(previous: dict[str, Any]) -> str:
    """把旧活动基中的持久尺度阶梯硬点替换成尺度词熵分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造持久尺度阶梯词熵判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "PersistentScaleLadderSignatureImported",
            imported,
            False,
            "上一层把 scale-escape 剩余压成持久尺度阶梯签名或 sparse scale-ladder SAE/ColumnCRT/PDEC。",
            PREVIOUS_TARGET,
        ),
        row(
            "ScaleLadderDyadicWordPartitionClosed",
            True,
            True,
            "每个持久尺度阶梯给出唯一 dyadic 指数词 sigma=(b_1,...,b_d)，其中 B_i=2^{b_i}, b_i>=1。",
            WORD_PARTITION,
        ),
        row(
            "ScaleLadderProductBudgetClosed",
            True,
            True,
            "未进入 product-width 出口时 prod_i B_i<=W_0，等价于 sum_i b_i<=K_0=ceil(log_2 max(W_0,1))。",
            PRODUCT_BUDGET,
        ),
        row(
            "ScaleLadderWordEntropyFiniteCapClosed",
            True,
            True,
            "正整数有序组成给出尺度词个数 N_ladder(K_0)<=2^{K_0}；持久签名不能作为匿名无限容量池。",
            WORD_ENTROPY,
        ),
        row(
            "AggregatePersistentPressureToSingleScaleWordClosed",
            True,
            True,
            "有限尺度词集合上若聚合压力超界，则至少一个尺度词承载平均以上压力。",
            SINGLE_WORD,
        ),
        row(
            "FixedScaleLadderMCRTColumnCRTExitClosed",
            True,
            True,
            "若承压尺度词下的实际素坐标和相位残基在无限子族中稳定，则进入固定 MCRT/ColumnCRT/PDEC 或有限原子。",
            FIXED_WORD,
        ),
        row(
            "FirstMovingScaleLadderPhaseCoordinateClosed",
            True,
            True,
            "若承压尺度词不稳定，则存在首个移动素坐标或相位残基；新的硬点被定位到该首移动层。",
            FIRST_MOVE,
        ),
        row(
            "SparseScaleLadderSAECarriedForward",
            True,
            False,
            "不能在同一尺度词上持久复现的事件继续登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "NoAnonymousPersistentScaleLadderSignature",
            True,
            True,
            "持久尺度阶梯签名被拆成有限尺度词、固定 MCRT 出口、首移动层或 sparse SAE；不再保留匿名签名池。",
            NO_ANON,
        ),
        row(
            "FirstMovingScaleLadderPhaseStillOpen",
            False,
            False,
            "仍未排斥固定尺度词内首个移动素坐标/相位漂移，也未证明 sparse SAE 全局可求和。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥首移动尺度阶梯相位漂移，或证明其必回流为 ColumnCRT/PDEC/SAE 且全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造持久尺度阶梯词熵证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "持久尺度阶梯签名被拆成 dyadic 指数词 sigma=(b_1,...,b_d)。"
        "未进入 product-width 出口时 sum b_i<=K_0=ceil(log_2 max(W_0,1))，"
        "因此尺度词个数至多 2^{K_0}，聚合压力必须落到单个尺度词。"
        "若该词下实际素坐标和相位稳定，则回到固定 MCRT/ColumnCRT/PDEC；"
        "否则剩余是固定尺度词内首个移动素坐标或相位漂移。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_scale_ladder_word_entropy_router",
        "status": "persistent_scale_ladder_signature_reduced_to_word_entropy_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "persistent_scale_ladder_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "dyadic_word_partition_closed": True,
        "product_budget_closed": True,
        "word_entropy_finite_cap_closed": True,
        "aggregate_to_single_scale_word_closed": True,
        "fixed_scale_ladder_columncrt_exit_closed": True,
        "first_moving_scale_ladder_phase_localized": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "anonymous_persistent_scale_ladder_removed": True,
        "first_moving_scale_ladder_phase_excluded": False,
        "sparse_scale_ladder_sae_summability_proved": False,
        "row_column_unconditional_closed": False,
        "scale_ladder_word_formulas": {
            "dyadic_coordinate": "B_i=2^{b_i}, b_i>=1",
            "scale_word": "sigma=(b_1,...,b_d)",
            "product": "A_sigma=prod_i B_i=2^{sum_i b_i}",
            "product_budget": "A_sigma<=W_0 => sum_i b_i<=K_0=ceil(log_2 max(W_0,1))",
            "word_count": "N_ladder(K_0)=1+sum_{n=1}^{K_0}2^{n-1}<=2^{K_0}",
            "pressure_pigeonhole": "E_total=sum_sigma E_sigma, so E_total>U implies some E_sigma>U/N_ladder(K_0)",
            "fixed_exit": "stable actual primes/residues under sigma => fixed MCRT/ColumnCRT/PDEC or finite atom",
            "moving_exit": "nonstable sigma has first moving prime coordinate or phase residue",
        },
        "next_direct_attack_target": NEW_TARGET,
        "latest_noncycle_basis_after_router": latest_basis,
        "decision_rows": rows,
        "source_hashes": source_hashes(),
        "plain_conclusion": plain,
    }


def write_md(cert: dict[str, Any]) -> None:
    """写 Markdown 证书。"""
    lines: list[str] = [
        "# Prime Matrix scale-ladder word-entropy 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"persistent_scale_ladder_imported={fmt_bool(cert['persistent_scale_ladder_imported'])}",
        f"dyadic_word_partition_closed={fmt_bool(cert['dyadic_word_partition_closed'])}",
        f"product_budget_closed={fmt_bool(cert['product_budget_closed'])}",
        f"word_entropy_finite_cap_closed={fmt_bool(cert['word_entropy_finite_cap_closed'])}",
        f"aggregate_to_single_scale_word_closed={fmt_bool(cert['aggregate_to_single_scale_word_closed'])}",
        f"fixed_scale_ladder_columncrt_exit_closed={fmt_bool(cert['fixed_scale_ladder_columncrt_exit_closed'])}",
        f"first_moving_scale_ladder_phase_localized={fmt_bool(cert['first_moving_scale_ladder_phase_localized'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"anonymous_persistent_scale_ladder_removed={fmt_bool(cert['anonymous_persistent_scale_ladder_removed'])}",
        f"first_moving_scale_ladder_phase_excluded={fmt_bool(cert['first_moving_scale_ladder_phase_excluded'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. dyadic 尺度词",
        "",
        "持久尺度阶梯由 dyadic 尺度组成：",
        "",
        "```text",
        "B_i=2^{b_i}, b_i>=1,",
        "sigma=(b_1,...,b_d).",
        "```",
        "",
        "尺度词的合成尺度为：",
        "",
        "```text",
        "A_sigma=prod_i B_i=2^{sum_i b_i}.",
        "```",
        "",
        "## 2. product 预算与词熵",
        "",
        "若 `A_sigma>W_0`，已经进入 product-width ColumnCRT/PDEC 或有限原子。因此非出口分支满足：",
        "",
        "```text",
        "sum_i b_i<=K_0=ceil(log_2 max(W_0,1)).",
        "```",
        "",
        "正整数有序组成给出有限尺度词数：",
        "",
        "```text",
        "N_ladder(K_0)=1+sum_{n=1}^{K_0}2^{n-1}<=2^{K_0}.",
        "```",
        "",
        "所以持久尺度阶梯不能作为匿名无限容量池。",
        "",
        "## 3. 压力定位到单个尺度词",
        "",
        "尺度词单元互不混同。若聚合压力为：",
        "",
        "```text",
        "E_total=sum_sigma E_sigma",
        "```",
        "",
        "且 `E_total>U`，则至少一个尺度词满足：",
        "",
        "```text",
        "E_sigma>U/N_ladder(K_0).",
        "```",
        "",
        "## 4. 固定词出口与首移动层",
        "",
        "对承压尺度词 `sigma`，若实际素坐标和相位残基在无限子族中稳定，则它是固定 MCRT/ColumnCRT/PDEC 或有限原子。若不稳定，则存在首个移动素坐标或相位残基；新的直接硬点被定位到该首移动层。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + IMPORT,
        "  AND " + WORD_PARTITION,
        "  AND " + PRODUCT_BUDGET,
        "  AND " + WORD_ENTROPY,
        "  AND " + SINGLE_WORD,
        "  AND " + FIXED_WORD,
        "  AND " + FIRST_MOVE,
        "  AND " + SPARSE,
        "  AND " + NO_ANON,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从持久尺度阶梯签名变成固定尺度词内首个移动素坐标/相位漂移，或 sparse scale-ladder SAE/ColumnCRT/PDEC。",
        "",
        "## 6. 判定表",
        "",
        "| gate | closed | proved | meaning | remaining |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in cert["decision_rows"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    cell(item["gate"]),
                    f"`{fmt_bool(item['closed'])}`",
                    f"`{fmt_bool(item['proved'])}`",
                    cell(item["meaning"]),
                    cell(item["remaining"]),
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## 7. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 8. 诚实边界",
            "",
            "- 本证书没有证明固定尺度词内首个移动素坐标/相位漂移不可能。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书只关闭匿名持久尺度阶梯签名池和尺度词聚合压力口径。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 9. 依赖哈希",
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
    """生成全部证书文件。"""
    DATA.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)
    cert = build_certificate()
    OUT_LEDGER.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_JSON.write_text(json.dumps(cert, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(cert)
    print(f"wrote {OUT_LEDGER.relative_to(ROOT)}")
    print(f"wrote {OUT_JSON.relative_to(ROOT)}")
    print(f"wrote {OUT_MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
