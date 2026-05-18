#!/usr/bin/env python3
"""生成 rank-budgeted iterated-LPF moving-family 的 word-entropy/首移动坐标证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_lpf_word_entropy_motion_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-cofactor-lpf-single-r-pressure-router.json",
]

PREVIOUS_TARGET = "RankBudgetedIteratedLPFMovingFamilyOrColumnCRTPDEC"
IMPORT = "RankBudgetedMovingFamilyImportedLedger"
WORD_PARTITION = "IteratedLPFWordSignaturePartitionLedger"
WORD_ENTROPY = "LPFWordEntropyFiniteCapLedger"
SINGLE_WORD = "AggregatePressureToSingleLPFWordLedger"
FIXED_WORD = "FixedLPFWordColumnCRTExitLedger"
FIRST_MOVE = "FirstMovingLPFCoordinateLedger"
MOTION_SUPPORT = "MovingCoordinateSupportReciprocityLedger"
NO_ANON = "NoAnonymousRankBudgetedMovingFamilyLedger"
NEW_TARGET = "FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC"

REDUCED_TARGET = (
    f"{IMPORT} AND {WORD_PARTITION} AND {WORD_ENTROPY} AND {SINGLE_WORD} "
    f"AND {FIXED_WORD} AND {FIRST_MOVE} AND {MOTION_SUPPORT} "
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
    """把旧活动基中的 rank-budgeted moving-family 替换成 word-motion 分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造 word-entropy/首移动坐标判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "RankBudgetedMovingFamilyImported",
            imported,
            False,
            "上一层把自由 triple pressure 压成有显式深度预算的迭代 LPF moving-family。",
            PREVIOUS_TARGET,
        ),
        row(
            "IteratedLPFWordSignaturePartitionClosed",
            True,
            True,
            "LPF 唯一性把每个 residual 分入唯一有序因子词 omega=(s,a_1,...,a_d)，且 A(omega)<=W 或进入 product-width 出口。",
            WORD_PARTITION,
        ),
        row(
            "LPFWordEntropyFiniteCapClosed",
            True,
            True,
            "对 omega=(s,a_1,...,a_d)，深度预算 d+1<=floor(log_r W) 给出有限 word 熵 H(W,r)；活动 word 集不能作为无限匿名容量池。",
            WORD_ENTROPY,
        ),
        row(
            "AggregatePressureToSingleWordClosed",
            True,
            True,
            "有限 word 集上若总压力超界，则至少一个 word 承载平均以上压力；否则聚合压力已由 word 熵预算吸收。",
            SINGLE_WORD,
        ),
        row(
            "FixedLPFWordColumnCRTExitClosed",
            True,
            True,
            "若承压 word 的全部素坐标和相位残基在族中稳定，则它不是 moving-family，而是固定 MCRT word，回到 ColumnCRT/PDEC 或有限原子。",
            FIXED_WORD,
        ),
        row(
            "FirstMovingLPFCoordinateClosed",
            True,
            True,
            "若 word 不稳定，存在首个移动坐标 mu；其前缀 word 稳定，所有移动都集中到该首移动素层之后。",
            FIRST_MOVE,
        ),
        row(
            "MovingCoordinateSupportReciprocityClosed",
            True,
            True,
            "首移动坐标 mu 加入后，残余支撑至多 ceil(W/(A_prefix*mu))；若 A_prefix*mu>W，则直接 ColumnCRT/PDEC/有限原子。",
            MOTION_SUPPORT,
        ),
        row(
            "NoAnonymousRankBudgetedMovingFamilyClosed",
            True,
            True,
            "rank-budgeted moving-family 被拆成固定 word ColumnCRT 出口或首移动坐标压力；不再保留匿名 moving-family 终端。",
            NO_ANON,
        ),
        row(
            "FirstMovingCoordinatePressureStillOpen",
            False,
            False,
            "仍未排除首移动 LPF 坐标的持久压力；本步只把 moving-family 压到首移动坐标相位/容量接口。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥首移动 LPF 坐标压力，或证明其必回流为 ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造 word-entropy/首移动坐标证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "秩预算化迭代 LPF moving-family 被拆成有限 word 熵和首移动坐标。"
        "LPF 唯一性给出有序因子词分区；深度预算使活动 word 集有限。"
        "若承压 word 稳定，则回到固定 MCRT/ColumnCRT；若不稳定，则存在首个移动 LPF 坐标，"
        "其加入会按 A_prefix*mu 收缩 residual 支撑。剩余硬点变成首移动坐标压力，而非匿名 moving-family。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_lpf_word_entropy_motion_router",
        "status": "rank_budgeted_moving_family_reduced_to_first_moving_lpf_coordinate_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "rank_budgeted_moving_family_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "word_signature_partition_closed": True,
        "word_entropy_finite_cap_closed": True,
        "aggregate_to_single_word_closed": True,
        "fixed_word_columncrt_exit_closed": True,
        "first_moving_coordinate_closed": True,
        "moving_coordinate_support_reciprocity_closed": True,
        "anonymous_moving_family_removed": True,
        "first_moving_coordinate_pressure_excluded": False,
        "row_column_unconditional_closed": False,
        "word_motion_formulas": {
            "word": "omega=(s,a_1,...,a_d), r<=s<=a_1<=...<=a_d",
            "word_product": "A(omega)=s*prod_{i<=d}a_i",
            "product_width_exit": "A(omega)>W => ColumnCRT/PDEC or finite atom",
            "depth_budget": "d+1<=floor(log_r W) when A(omega)<=W and all factors>=r>=2",
            "word_entropy_cap": "Omega(P,C) is finite; |Omega(P,C)|<=H(W,r)",
            "single_word_pressure": "E(Omega)>U => exists omega with E_omega>U/|Omega|",
            "fixed_word_exit": "stable omega and stable residues => fixed MCRT word, not moving-family",
            "first_moving_coordinate": "mu=a_k where k is the first index whose prime/residue coordinate changes",
            "moving_support": "width_after_mu<=ceil(W/(A_prefix*mu))",
            "new_failure": "first moving LPF coordinate pressure or word-motion ColumnCRT/PDEC",
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
        "# Prime Matrix LPF word-entropy / first-moving-coordinate 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"rank_budgeted_moving_family_imported={fmt_bool(cert['rank_budgeted_moving_family_imported'])}",
        f"word_signature_partition_closed={fmt_bool(cert['word_signature_partition_closed'])}",
        f"word_entropy_finite_cap_closed={fmt_bool(cert['word_entropy_finite_cap_closed'])}",
        f"aggregate_to_single_word_closed={fmt_bool(cert['aggregate_to_single_word_closed'])}",
        f"fixed_word_columncrt_exit_closed={fmt_bool(cert['fixed_word_columncrt_exit_closed'])}",
        f"first_moving_coordinate_closed={fmt_bool(cert['first_moving_coordinate_closed'])}",
        f"moving_coordinate_support_reciprocity_closed={fmt_bool(cert['moving_coordinate_support_reciprocity_closed'])}",
        f"anonymous_moving_family_removed={fmt_bool(cert['anonymous_moving_family_removed'])}",
        f"first_moving_coordinate_pressure_excluded={fmt_bool(cert['first_moving_coordinate_pressure_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. LPF word 分区",
        "",
        "上一层把剩余压成秩预算化 moving-family。对每个 residual，由 LPF 唯一性得到唯一有序因子词：",
        "",
        "```text",
        "omega=(s,a_1,...,a_d),",
        "r<=s<=a_1<=...<=a_d,",
        "A(omega)=s*prod_{i<=d}a_i.",
        "```",
        "",
        "若 `A(omega)>W`，其中 `W` 是原 m 支撑宽度，则已进入 product-width ColumnCRT/PDEC 或有限原子。",
        "",
        "## 2. word 熵预算",
        "",
        "未进入 product-width 出口时：",
        "",
        "```text",
        "A(omega)<=W.",
        "```",
        "",
        "非有限分支所有因子至少为 `r>=2`，因此总因子深度满足：",
        "",
        "```text",
        "d+1<=floor(log_r W).",
        "```",
        "",
        "所以活动 word 集 `Omega(P,C)` 是有限集合，大小受显式熵预算 `H(W,r)` 控制。它不能作为无限匿名容量池。",
        "",
        "## 3. 聚合压力定位",
        "",
        "把总压力写为互不重叠 word cell 之和：",
        "",
        "```text",
        "E(Omega)=sum_{omega in Omega} E_omega.",
        "```",
        "",
        "若 `E(Omega)>U`，则存在单个 word 满足：",
        "",
        "```text",
        "E_omega>U/|Omega|.",
        "```",
        "",
        "因此剩余压力必须落在单个 LPF word 上，而不能停留在未命名的 moving-family 总量上。",
        "",
        "## 4. 固定 word 与首移动坐标",
        "",
        "若承压 word 的素坐标和相位残基在族中稳定，则它是固定 MCRT word：",
        "",
        "```text",
        "stable omega + stable residues => FixedLPFWordColumnCRTExit.",
        "```",
        "",
        "若不稳定，则存在首个移动坐标 `mu`。设它之前的稳定前缀乘积为：",
        "",
        "```text",
        "A_prefix.",
        "```",
        "",
        "首移动坐标加入后，残余支撑宽度满足：",
        "",
        "```text",
        "width_after_mu<=ceil(W/(A_prefix*mu)).",
        "```",
        "",
        "若 `A_prefix*mu>W`，则回到 ColumnCRT/PDEC 或有限原子；否则真正剩余只可能是首移动坐标压力。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + IMPORT,
        "  AND " + WORD_PARTITION,
        "  AND " + WORD_ENTROPY,
        "  AND " + SINGLE_WORD,
        "  AND " + FIXED_WORD,
        "  AND " + FIRST_MOVE,
        "  AND " + MOTION_SUPPORT,
        "  AND " + NO_ANON,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从秩预算化 moving-family 变成首移动 LPF 坐标压力，或 word-motion ColumnCRT/PDEC。",
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
            "- 本证书没有证明首移动 LPF 坐标压力不可能。",
            "- 本证书只删除匿名 rank-budgeted moving-family 口径，把它压成固定 word 出口或首移动坐标压力。",
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
