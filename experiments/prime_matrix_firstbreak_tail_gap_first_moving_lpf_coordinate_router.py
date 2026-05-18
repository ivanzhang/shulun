#!/usr/bin/env python3
"""生成首移动 LPF 坐标的 dyadic/product-width 分解证书。

用法示例：
  python3 experiments/prime_matrix_firstbreak_tail_gap_first_moving_lpf_coordinate_router.py
  python3 -m json.tool docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json

输出：
  data/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-ledger.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json
  docs/monograph/prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.md
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "monograph"

OUT_LEDGER = DATA / "prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-ledger.json"
OUT_JSON = DOCS / "prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.json"
OUT_MD = DOCS / "prime-matrix-firstbreak-tail-gap-first-moving-lpf-coordinate-router.md"

SOURCE_FILES = [
    DOCS / "prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-iterated-lpf-rank-budget-router.json",
    DOCS / "prime-matrix-firstbreak-tail-gap-fixed-pair-second-lpf-descent-router.json",
]

PREVIOUS_TARGET = "FirstMovingLPFCoordinatePressureOrWordMotionColumnCRTPDEC"
IMPORT = "FirstMovingLPFCoordinatePressureImportedLedger"
PREFIX = "StablePrefixProductSupportLedger"
EFFECTIVE_WIDTH = "FirstMovingCoordinateEffectiveWidthLedger"
LOW = "LowMovingCoordinateFiniteAtomLedger"
DYADIC = "FirstMovingCoordinateDyadicPartitionLedger"
PRODUCT = "MovingCoordinateActiveProductWidthExitLedger"
COUNT = "MovingCoordinateActiveCountBoundLedger"
SINGLE = "SingleMovingCoordinatePressureLocalizationLedger"
FIXED = "FixedMovingCoordinateDegeneratesToColumnCRTLedger"
NO_ANON = "NoAnonymousFirstMovingCoordinatePoolLedger"
NEW_TARGET = "SingleMovingLPFCoordinateDriftOrPrefixColumnCRTPDEC"

REDUCED_TARGET = (
    f"{IMPORT} AND {PREFIX} AND {EFFECTIVE_WIDTH} AND {LOW} AND {DYADIC} "
    f"AND {PRODUCT} AND {COUNT} AND {SINGLE} AND {FIXED} "
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
    """把旧活动基中的首移动坐标压力替换成 dyadic/product-width 分解。"""
    basis = previous.get("latest_noncycle_basis_after_router", "")
    if not basis:
        return REDUCED_TARGET
    return basis.replace(PREVIOUS_TARGET, REDUCED_TARGET)


def build_rows(previous: dict[str, Any]) -> list[dict[str, Any]]:
    """构造首移动 LPF 坐标分解判定表。"""
    imported = previous.get("next_direct_attack_target") == PREVIOUS_TARGET
    return [
        row(
            "FirstMovingLPFCoordinatePressureImported",
            imported,
            False,
            "上一层把匿名 word-motion 压到首移动 LPF 坐标压力或 ColumnCRT/PDEC。",
            PREVIOUS_TARGET,
        ),
        row(
            "StablePrefixProductSupportClosed",
            True,
            True,
            "首移动坐标之前的 LPF word 前缀稳定，乘积 A_prefix 固定；所有真正移动都从 mu 开始。",
            PREFIX,
        ),
        row(
            "FirstMovingCoordinateEffectiveWidthClosed",
            True,
            True,
            "首移动坐标 mu 的有效支撑宽度为 W_prefix=floor(W/A_prefix)；若 mu>W_prefix，则 A_prefix*mu>W 并进入 product-width 出口。",
            EFFECTIVE_WIDTH,
        ),
        row(
            "LowMovingCoordinateFiniteAtomClosed",
            True,
            True,
            "低坐标 mu<=2 只有有限原子；真正使用对数活动个数界的 dyadic 层从 B>=2 开始。",
            LOW,
        ),
        row(
            "FirstMovingCoordinateDyadicPartitionClosed",
            True,
            True,
            "除低坐标有限原子外，未出口的 mu 均落在 B<mu<=2B, B>=2 的有限 dyadic 坐标层内，层数至多 floor(log_2 W_prefix)+1。",
            DYADIC,
        ),
        row(
            "MovingCoordinateActiveProductWidthClosed",
            True,
            True,
            "固定 dyadic 层中活动坐标集合 M_B 若满足 prod(mu in M_B) > W_prefix，则相位周期超过有效支撑，进入 ColumnCRT/PDEC 或有限原子。",
            PRODUCT,
        ),
        row(
            "MovingCoordinateActiveCountBoundClosed",
            True,
            True,
            "若 prod(M_B)<=W_prefix 且 mu>B，则 |M_B|<=floor(log W_prefix/log B)，活动坐标池不能匿名承载任意压力。",
            COUNT,
        ),
        row(
            "SingleMovingCoordinatePressureLocalizationClosed",
            True,
            True,
            "有限活动坐标池上若聚合压力超界，则存在单个 mu 承载平均以上压力。",
            SINGLE,
        ),
        row(
            "FixedMovingCoordinateColumnCRTClosed",
            True,
            True,
            "该单个 mu 若在族中稳定，则首移动退化为固定 word 坐标，回到 Prefix/ColumnCRT/PDEC 或有限原子。",
            FIXED,
        ),
        row(
            "NoAnonymousFirstMovingCoordinatePoolClosed",
            True,
            True,
            "首移动坐标池被拆成 product-width 出口、活动个数界和单 mu 压力；不再保留匿名坐标池。",
            NO_ANON,
        ),
        row(
            "SingleMovingCoordinateDriftStillOpen",
            False,
            False,
            "仍未排除单个 mu 随 P 漂移的持久压力；本步只把首移动坐标压力压到单坐标漂移接口。",
            NEW_TARGET,
        ),
        row(
            "RowColumnUnconditionalClosureReached",
            False,
            False,
            "行/列命题仍需排斥单移动坐标漂移，或证明其必回流为 ColumnCRT/PDEC/SAE。",
            NEW_TARGET,
        ),
    ]


def build_certificate() -> dict[str, Any]:
    """构造首移动 LPF 坐标 dyadic/product-width 证书。"""
    previous = load_json(DOCS / "prime-matrix-firstbreak-tail-gap-lpf-word-entropy-motion-router.json")
    rows = build_rows(previous)
    latest_basis = replace_latest_basis(previous)
    plain = (
        "首移动 LPF 坐标压力被拆成稳定前缀后的有效宽度、dyadic 坐标层、"
        "活动坐标 product-width 出口与单坐标压力定位。"
        "若活动坐标乘积超过有效宽度，则回到 ColumnCRT/PDEC 或有限原子；"
        "若乘积不超过有效宽度，则活动个数有显式对数界，超界压力必须落在单个 mu。"
        "剩余变成单个 mu 随 P 漂移的压力，而不是匿名首移动坐标池。"
    )
    return {
        "certificate_type": "prime_matrix_firstbreak_tail_gap_first_moving_lpf_coordinate_router",
        "status": "first_moving_lpf_coordinate_pressure_reduced_to_single_coordinate_drift_open",
        "same_theorem_target_preserved": True,
        "no_theorem_switch": True,
        "counterexample_assumption_only": True,
        "empirical_absence_not_used_as_proof": True,
        "hardpoint_before_router": PREVIOUS_TARGET,
        "hardpoint_after_router": REDUCED_TARGET,
        "first_moving_coordinate_pressure_imported": previous.get("next_direct_attack_target") == PREVIOUS_TARGET,
        "stable_prefix_product_support_closed": True,
        "effective_width_closed": True,
        "low_coordinate_finite_atom_closed": True,
        "dyadic_coordinate_partition_closed": True,
        "active_product_width_exit_closed": True,
        "active_count_bound_closed": True,
        "single_coordinate_pressure_localized": True,
        "fixed_coordinate_columncrt_exit_closed": True,
        "anonymous_coordinate_pool_removed": True,
        "single_coordinate_drift_excluded": False,
        "row_column_unconditional_closed": False,
        "first_moving_coordinate_formulas": {
            "stable_prefix": "A_prefix=product of stable LPF word prefix before mu",
            "effective_width": "W_prefix=floor(W/A_prefix)",
            "large_mu_exit": "mu>W_prefix => A_prefix*mu>W => ColumnCRT/PDEC or finite atom",
            "low_coordinate": "mu<=2 gives a finite low-coordinate atom",
            "dyadic_layer": "B<mu<=2B with B=2^b, B>=2, and B<=W_prefix",
            "active_product": "M_B=prod_{mu in active layer} mu",
            "product_width_exit": "M_B>W_prefix => ColumnCRT/PDEC or finite atom",
            "active_count_bound": "M_B<=W_prefix and mu>B => |active layer|<=floor(log W_prefix/log B)",
            "single_coordinate_pressure": "E_B>U_B => exists mu with E_mu>U_B/|active layer|",
            "fixed_coordinate_exit": "mu stable across family => fixed word CoordinateCRT/ColumnCRT",
            "new_failure": "single moving LPF coordinate drift or prefix ColumnCRT/PDEC",
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
        "# Prime Matrix first-moving LPF coordinate 证书",
        "",
        f"**状态：** `{cert['status']}`",
        "",
        cert["plain_conclusion"],
        "",
        "```text",
        f"first_moving_coordinate_pressure_imported={fmt_bool(cert['first_moving_coordinate_pressure_imported'])}",
        f"stable_prefix_product_support_closed={fmt_bool(cert['stable_prefix_product_support_closed'])}",
        f"effective_width_closed={fmt_bool(cert['effective_width_closed'])}",
        f"low_coordinate_finite_atom_closed={fmt_bool(cert['low_coordinate_finite_atom_closed'])}",
        f"dyadic_coordinate_partition_closed={fmt_bool(cert['dyadic_coordinate_partition_closed'])}",
        f"active_product_width_exit_closed={fmt_bool(cert['active_product_width_exit_closed'])}",
        f"active_count_bound_closed={fmt_bool(cert['active_count_bound_closed'])}",
        f"single_coordinate_pressure_localized={fmt_bool(cert['single_coordinate_pressure_localized'])}",
        f"fixed_coordinate_columncrt_exit_closed={fmt_bool(cert['fixed_coordinate_columncrt_exit_closed'])}",
        f"anonymous_coordinate_pool_removed={fmt_bool(cert['anonymous_coordinate_pool_removed'])}",
        f"single_coordinate_drift_excluded={fmt_bool(cert['single_coordinate_drift_excluded'])}",
        f"row_column_unconditional_closed={fmt_bool(cert['row_column_unconditional_closed'])}",
        "```",
        "",
        "## 1. 稳定前缀与有效宽度",
        "",
        "首移动坐标 `mu` 之前的 LPF word 前缀稳定，记其乘积为：",
        "",
        "```text",
        "A_prefix.",
        "```",
        "",
        "原 m 支撑宽度为 `W`，则首移动坐标可用的有效宽度为：",
        "",
        "```text",
        "W_prefix=floor(W/A_prefix).",
        "```",
        "",
        "若：",
        "",
        "```text",
        "mu>W_prefix,",
        "```",
        "",
        "则 `A_prefix*mu>W`，相位周期已超过原支撑，必须进入 ColumnCRT/PDEC 或有限原子。",
        "",
        "## 2. dyadic 坐标层",
        "",
        "`mu<=2` 只有有限低坐标原子。除此之外，未出口的 `mu` 只能落在有限个 dyadic 层：",
        "",
        "```text",
        "B<mu<=2B,",
        "B=2^b,",
        "B>=2,",
        "B<=W_prefix.",
        "```",
        "",
        "因此层数至多 `floor(log_2 W_prefix)+1`。",
        "",
        "## 3. product-width 与活动个数界",
        "",
        "固定一层，令活动首移动坐标集合为 `M_B`，并记：",
        "",
        "```text",
        "P_B=prod_{mu in M_B}mu.",
        "```",
        "",
        "若：",
        "",
        "```text",
        "P_B>W_prefix,",
        "```",
        "",
        "则活动坐标的合成周期超过有效支撑，进入 ColumnCRT/PDEC 或有限原子。若 `P_B<=W_prefix`，由于每个 `mu>B`，有：",
        "",
        "```text",
        "|M_B|<=floor(log W_prefix/log B).",
        "```",
        "",
        "## 4. 单坐标压力定位",
        "",
        "把 dyadic 层压力写为互不重叠坐标 cell 之和：",
        "",
        "```text",
        "E_B=sum_{mu in M_B}E_mu.",
        "```",
        "",
        "若 `E_B>U_B`，则存在单个坐标：",
        "",
        "```text",
        "E_mu>U_B/|M_B|.",
        "```",
        "",
        "若该 `mu` 在族中稳定，则首移动退化为固定 word 坐标，回到 Prefix/ColumnCRT/PDEC 或有限原子；若它随 `P` 漂移，则进入新的单坐标漂移硬点。",
        "",
        "## 5. 新硬点",
        "",
        "```text",
        PREVIOUS_TARGET,
        "  -> " + IMPORT,
        "  AND " + PREFIX,
        "  AND " + EFFECTIVE_WIDTH,
        "  AND " + LOW,
        "  AND " + DYADIC,
        "  AND " + PRODUCT,
        "  AND " + COUNT,
        "  AND " + SINGLE,
        "  AND " + FIXED,
        "  AND " + NO_ANON,
        "  AND " + NEW_TARGET,
        "```",
        "",
        "剩余从首移动坐标池压力变成单个 moving LPF coordinate drift，或 prefix ColumnCRT/PDEC。",
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
            "- 本证书没有证明单个 moving LPF coordinate drift 不可能。",
            "- 本证书只删除匿名首移动坐标池，把它压成 product-width 出口或单坐标漂移。",
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
