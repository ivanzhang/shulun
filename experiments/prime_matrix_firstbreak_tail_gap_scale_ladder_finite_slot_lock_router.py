#!/usr/bin/env python3
"""生成 fixed scale word 内首移动相位漂移的有限槽锁定证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_scale_ladder_finite_slot_lock_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-finite-slot-lock-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-scale-escape-support-clock-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-single-moving-lpf-coordinate-scale-escape-router.json",
]

PREVIOUS_TARGET = "FirstMovingScaleLadderPhaseDriftOrSparseScaleLadderSAEColumnCRTPDEC"
IMPORT = "FirstMovingScaleLadderPhaseDriftImportedLedger"
FIXED_WORD = "FixedScaleWordSlotLedger"
FINITE_PRIMES = "FinitePrimeChoicesPerScaleSlotLedger"
FINITE_PHASES = "FiniteResidueChoicesPerPrimeSlotLedger"
FINITE_ATOMS = "FiniteActualScaleLadderAtomSetLedger"
PIGEONHOLE = "InfinitePigeonholeStableActualScaleLadderLedger"
NO_DRIFT = "NoPersistentFirstMovingScaleLadderPhaseDriftLedger"
FIXED_EXIT = "StableActualScaleLadderMCRTColumnCRTExitLedger"
SPARSE = "SparseScaleLadderSAECarriedForwardAfterFiniteSlotLockLedger"
NO_ANON = "NoAnonymousFirstMovingScaleLadderPhaseDriftLedger"
NEW_TARGET = "SparseScaleLadderSAESummabilityOrStableActualLadderColumnCRTPDEC"

REDUCED_TARGET = (
    f"{IMPORT} AND {FIXED_WORD} AND {FINITE_PRIMES} AND {FINITE_PHASES} "
    f"AND {FINITE_ATOMS} AND {PIGEONHOLE} AND {NO_DRIFT} AND {FIXED_EXIT} "
    f"AND {SPARSE} AND {NO_ANON} AND {NEW_TARGET}"
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
    """把旧活动基中的首移动尺度阶梯相位漂移替换成有限槽锁定分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造有限槽锁定判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "FirstMovingScaleLadderPhaseDriftImported",
            imported,
            False,
            "上一层把持久尺度阶梯签名压到固定尺度词内首个移动素坐标/相位漂移，或 sparse scale-ladder SAE。",
            PREVIOUS_TARGET,
        ),
        row(
            "FixedScaleWordSlotClosed",
            True,
            True,
            "承压分支已固定 dyadic 尺度词 sigma=(b_1,...,b_d)，每个槽的 dyadic 指数 b_i 固定。",
            FIXED_WORD,
        ),
        row(
            "FinitePrimeChoicesPerSlotClosed",
            True,
            True,
            "固定槽 i 的实际素数必须满足 2^{b_i}<=q_i<2^{b_i+1}，所以可选素数有限。",
            FINITE_PRIMES,
        ),
        row(
            "FiniteResidueChoicesPerSlotClosed",
            True,
            True,
            "固定实际素数 q_i 后，相位残基只在 Z/q_iZ 中取值；每槽相位选择有限。",
            FINITE_PHASES,
        ),
        row(
            "FiniteActualScaleLadderAtomSetClosed",
            True,
            True,
            "固定尺度词 sigma 下，实际素数-相位词集合是有限直积；不存在无限匿名移动槽。",
            FINITE_ATOMS,
        ),
        row(
            "InfinitePigeonholeStableActualScaleLadderClosed",
            True,
            True,
            "若同一固定尺度词在无限子族中持久承压，则由无限鸽巢存在稳定实际素数-相位词子族。",
            PIGEONHOLE,
        ),
        row(
            "NoPersistentFirstMovingScaleLadderPhaseDrift",
            True,
            True,
            "固定尺度词内的首移动素坐标/相位漂移不能作为持久无限分支；持久分支必固定化，非持久分支为 SAE。",
            NO_DRIFT,
        ),
        row(
            "StableActualScaleLadderMCRTColumnCRTExitClosed",
            True,
            True,
            "稳定实际素数-相位词是固定 MCRT cell，回到 ColumnCRT/PDEC 或有限原子出口。",
            FIXED_EXIT,
        ),
        row(
            "SparseScaleLadderSAECarriedForwardAfterFiniteSlotLock",
            True,
            False,
            "不能在任一稳定实际词上持久复现的事件登记为 sparse scale-ladder SAE；本步不证明全局求和。",
            SPARSE,
        ),
        row(
            "NoAnonymousFirstMovingScaleLadderPhaseDrift",
            True,
            True,
            "首移动尺度阶梯相位漂移被拆成稳定实际 MCRT 出口或 sparse SAE；不再保留匿名 first-moving 漂移。",
            NO_ANON,
        ),
        row(
            "SparseScaleLadderSummabilityStillOpen",
            False,
            False,
            "仍未证明 sparse scale-ladder SAE 全局可求和，也未排斥稳定实际 ladder 的 ColumnCRT/PDEC 出口。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥稳定实际 ladder ColumnCRT/PDEC，或证明 sparse scale-ladder SAE 全局可控。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造有限槽锁定证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-scale-ladder-word-entropy-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "固定尺度词 sigma=(b_1,...,b_d) 后，每个槽的实际素数只在有限 dyadic 区间 "
        "2^{b_i}<=q_i<2^{b_i+1} 中，相位残基也有限。"
        "因此实际素数-相位词集合有限；无限持久承压分支必有稳定实际词子族，"
        "回到固定 MCRT/ColumnCRT/PDEC 或有限原子。所谓首移动相位漂移只能是非持久 sparse SAE。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_scale_ladder_finite_slot_lock_router",
        "status": "first_moving_scale_ladder_phase_drift_reduced_to_finite_slot_lock_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "first_moving_scale_ladder_phase_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "fixed_scale_word_slot_closed": True,
        "finite_prime_choices_per_slot_closed": True,
        "finite_residue_choices_per_slot_closed": True,
        "finite_actual_scale_ladder_atom_set_closed": True,
        "infinite_pigeonhole_stable_actual_ladder_closed": True,
        "persistent_first_moving_scale_ladder_phase_excluded": True,
        "stable_actual_ladder_columncrt_exit_closed": True,
        "sparse_scale_ladder_sae_carried_forward": True,
        "anonymous_first_moving_scale_ladder_phase_removed": True,
        "sparse_scale_ladder_sae_summability_proved": False,
        "stable_actual_ladder_columncrt_pdec_excluded": False,
        "row_column_unconditional_closed": False,
        "finite_slot_formulas": {
            "fixed_scale_word": "sigma=(b_1,...,b_d), b_i fixed",
            "prime_slot": "Q_i={q prime: 2^{b_i}<=q<2^{b_i+1}}, |Q_i|<infty",
            "phase_slot": "for q in Q_i, a_i in Z/qZ, finitely many residues",
            "actual_atom_count": "N_actual(sigma)<=prod_i sum_{q in Q_i} q < infinity",
            "pigeonhole": "infinite persistent branch over finite actual atoms has stable actual atom subfamily",
            "fixed_exit": "stable actual atom => fixed MCRT/ColumnCRT/PDEC or finite atom",
            "sparse_exit": "nonpersistent atoms route to sparse scale-ladder SAE",
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
        "# Prime Matrix scale-ladder finite-slot lock 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"first_moving_scale_ladder_phase_imported={fmt_bool(cert['first_moving_scale_ladder_phase_imported'])}",
        f"fixed_scale_word_slot_closed={fmt_bool(cert['fixed_scale_word_slot_closed'])}",
        f"finite_prime_choices_per_slot_closed={fmt_bool(cert['finite_prime_choices_per_slot_closed'])}",
        f"finite_residue_choices_per_slot_closed={fmt_bool(cert['finite_residue_choices_per_slot_closed'])}",
        f"finite_actual_scale_ladder_atom_set_closed={fmt_bool(cert['finite_actual_scale_ladder_atom_set_closed'])}",
        f"infinite_pigeonhole_stable_actual_ladder_closed={fmt_bool(cert['infinite_pigeonhole_stable_actual_ladder_closed'])}",
        f"persistent_first_moving_scale_ladder_phase_excluded={fmt_bool(cert['persistent_first_moving_scale_ladder_phase_excluded'])}",
        f"stable_actual_ladder_columncrt_exit_closed={fmt_bool(cert['stable_actual_ladder_columncrt_exit_closed'])}",
        f"sparse_scale_ladder_sae_carried_forward={fmt_bool(cert['sparse_scale_ladder_sae_carried_forward'])}",
        f"anonymous_first_moving_scale_ladder_phase_removed={fmt_bool(cert['anonymous_first_moving_scale_ladder_phase_removed'])}",
        f"sparse_scale_ladder_sae_summability_proved={fmt_bool(cert['sparse_scale_ladder_sae_summability_proved'])}",
        f"stable_actual_ladder_columncrt_pdec_excluded={fmt_bool(cert['stable_actual_ladder_columncrt_pdec_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 固定尺度词的有限槽",
        "",
        "承压分支已经固定 dyadic 尺度词：",
        "",
        "```text",
        "sigma=(b_1,...,b_d), b_i fixed.",
        "```",
        "",
        "每个槽的实际素数只能来自有限集合：",
        "",
        "```text",
        "Q_i={q prime: 2^{b_i}<=q<2^{b_i+1}}.",
        "```",
        "",
        "固定 `q in Q_i` 后，相位残基 `a_i in Z/qZ` 也只有有限个。",
        "",
        "## 2. 实际 ladder 原子有限",
        "",
        "固定尺度词下的实际素数-相位词数量有粗上界：",
        "",
        "```text",
        "N_actual(sigma)<=prod_i sum_{q in Q_i} q < infinity.",
        "```",
        "",
        "因此固定尺度词内不存在无限匿名移动槽。",
        "",
        "## 3. 无限鸽巢锁定",
        "",
        "若某固定尺度词在无限子族中持久承压，则有限实际词集合上必有一个实际素数-相位词无限复现。该子族上所有素坐标与相位残基稳定。",
        "",
        "稳定实际词是固定 MCRT cell，回到 ColumnCRT/PDEC 或有限原子。不能在任一实际词上持久复现的事件只登记为 sparse scale-ladder SAE。",
        "",
        "## 4. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + IMPORT,
        "  AND " + FIXED_WORD,
        "  AND " + FINITE_PRIMES,
        "  AND " + FINITE_PHASES,
        "  AND " + FINITE_ATOMS,
        "  AND " + PIGEONHOLE,
        "  AND " + NO_DRIFT,
        "  AND " + FIXED_EXIT,
        "  AND " + SPARSE,
        "  AND " + NO_ANON,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从固定尺度词内首移动漂移变成稳定实际 ladder 的 ColumnCRT/PDEC 出口，或 sparse scale-ladder SAE 全局求和问题。",
        "",
        "## 5. 判定表",
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
            "## 6. 新活动基",
            "",
            "```text",
            cert["latest_noncycle_basis_after_router"],
            "```",
            "",
            "## 7. 诚实边界",
            "",
            "- 本证书没有排斥稳定实际 ladder 的 ColumnCRT/PDEC 出口。",
            "- 本证书没有证明 sparse scale-ladder SAE 全局可求和。",
            "- 本证书关闭固定尺度词内持久首移动素坐标/相位漂移。",
            f"- `{NEW_TARGET}` 仍未闭合。",
            "- 行/列命题仍未无条件闭合。",
            "",
            "## 8. 依赖哈希",
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
